from .clr import configure_celery
from celery.schedules import crontab
from celery.task import periodic_task
from app.extensions import db
from app.factory import create_app
import json
import urllib.request
import pandas as pd
import logging

app = create_app()
celery = configure_celery(app)


@periodic_task(
    run_every=crontab(month_of_year="1,5,9", day_of_month=1, hour=8, minute=30),  # Israel time = UTC + 3
    name="get_provident_fund_data_and_add_to_db", ignore_result=True)
def get_provident_fund_data_and_add_to_db():
    with app.app_context():
        url_data = 'https://data.gov.il/api/3/action/datastore_search?resource_id=a30dcbea-a1d2-482c-ae29-8f781f5025fb&limit=2855'
        web_url = urllib.request.urlopen(url_data)
        data = web_url.read()
        encoding = web_url.info().get_content_charset('utf-8')
        json_data = json.loads(data.decode(encoding))
        records = json_data['result']['records']
        df = pd.json_normalize(records)
        for col in df:
            try:
                df[col] = pd.to_numeric(df[col])
            except Exception as e:
                logging.exception(e)
                try:
                    df[col] = pd.to_datetime(df[col])
                except Exception as e:
                    logging.exception(e)
                    continue
        from models.provident_fund import ProvidentFund
        columns = ['FUND_NAME',  # שם המסלול לפי  החברה - לא חלק משאלות ששואלים את המשתמש
                   'FUND_CLASSIFICATION',  # סוג הקופה
                   'MANAGING_CORPORATION',  # החברה שמנהלת את הקופה
                   'REPORT_PERIOD',  # צריך לסנן ולמחוק
                   'TARGET_POPULATION',  # אוכלוסיית יעד
                   'SPECIALIZATION',  # התמחות עיקרית
                   'SUB_SPECIALIZATION',  # התמחות משנית
                   'AVG_ANNUAL_MANAGEMENT_FEE',  # דמי ניהול ממוצעים- מחסכון
                   'AVG_DEPOSIT_FEE',  # דמי ניהול ממוצעים- מהפקדה
                   'YEAR_TO_DATE_YIELD',  # תשואה שנתית
                   'AVG_ANNUAL_YIELD_TRAILING_3YRS',  # תשואה מצטברת ל-3 שנים
                   'AVG_ANNUAL_YIELD_TRAILING_5YRS']  # תשואה מצטברת ל-5 שנים
        df_need_col = pd.DataFrame(df, columns=columns)
        report_period_maxes = df_need_col.groupby(
            ['FUND_NAME', 'FUND_CLASSIFICATION', "MANAGING_CORPORATION"]).REPORT_PERIOD.transform(max)
        df_need_col_after_filter = df_need_col.loc[df_need_col.REPORT_PERIOD == report_period_maxes]
        df_need_col_after_filter = df_need_col_after_filter.drop(columns=['REPORT_PERIOD'])
        df_need_col_after_filter = df_need_col_after_filter.dropna(subset=["AVG_ANNUAL_MANAGEMENT_FEE",
                                                                           "AVG_DEPOSIT_FEE", "YEAR_TO_DATE_YIELD",
                                                                           "AVG_ANNUAL_YIELD_TRAILING_3YRS",
                                                                           "AVG_ANNUAL_YIELD_TRAILING_5YRS"],
                                                                   how='all')
        df_need_col_after_filter.columns = ["fund_name", "fund_classification", "management_corporation",
                                            "target_population", "specialization", "sub_specialization",
                                            "avg_annual_management_fee", "avg_deposit_fee", "year_to_date_yield",
                                            "avg_annual_yield_trailing_3yrs", "avg_annual_yield_trailing_5yrs"]
        db.session.query(ProvidentFund).delete()
        db.session.commit()
        with db.engine.begin():
            df_need_col_after_filter.to_sql('provident_fund', db.engine, if_exists='append', index=False)
