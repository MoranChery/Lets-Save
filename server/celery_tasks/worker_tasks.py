from .clr import configure_celery
from celery.schedules import crontab
from celery.task import periodic_task
from app.extensions import db
from app.factory import create_app
import json
import urllib.request
import pandas as pd
import datetime
from models.monthly_yield_fund import MonthlyYieldFund
from models.provident_fund import ProvidentFund


app = create_app()
celery = configure_celery(app)
report_period = 202109


def from_string_to_num(val):
    if len(val) > 0:
        return_val = val
        if '-' in return_val:
            return_val = return_val[1:]
            return_val = float(return_val)
            return_val = return_val * -1
        else:
            return_val = float(return_val)
        return return_val
    else:
        return


def update_provident_fund(provident_fund):
    get_provident_fund = db.session.query(ProvidentFund).filter_by(fund_id=provident_fund["fund_id"])
    if get_provident_fund.first():
        get_provident_fund.update({
            ProvidentFund.fund_name: provident_fund["fund_name"],
            ProvidentFund.fund_classification: provident_fund["fund_classification"],
            ProvidentFund.management_corporation: provident_fund["management_corporation"],
            ProvidentFund.target_population: provident_fund["target_population"],
            ProvidentFund.specialization: provident_fund["specialization"],
            ProvidentFund.sub_specialization: provident_fund["sub_specialization"],
            ProvidentFund.avg_annual_management_fee: provident_fund["avg_annual_management_fee"],
            ProvidentFund.avg_deposit_fee: provident_fund["avg_deposit_fee"],
            ProvidentFund.year_to_date_yield: provident_fund["year_to_date_yield"],
            ProvidentFund.yield_trailing_3_yrs: provident_fund["yield_trailing_3_yrs"],
            ProvidentFund.yield_trailing_5_yrs: provident_fund["yield_trailing_5_yrs"],
            ProvidentFund.avg_annual_yield_trailing_3yrs: provident_fund["avg_annual_yield_trailing_3yrs"],
            ProvidentFund.avg_annual_yield_trailing_5yrs: provident_fund["avg_annual_yield_trailing_5yrs"],
            ProvidentFund.standard_deviation: provident_fund["standard_deviation"],
            ProvidentFund.alpha: provident_fund["alpha"],
            ProvidentFund.sharpe_ratio: provident_fund["sharpe_ratio"]
        },
            synchronize_session=False)
    else:
        new_provident_fund = ProvidentFund(
            fund_name=provident_fund["fund_name"],
            fund_classification= provident_fund["fund_classification"],
            management_corporation= provident_fund["management_corporation"],
            target_population= provident_fund["target_population"],
            specialization= provident_fund["specialization"],
            sub_specialization= provident_fund["sub_specialization"],
            avg_annual_management_fee= provident_fund["avg_annual_management_fee"],
            avg_deposit_fee= provident_fund["avg_deposit_fee"],
            year_to_date_yield= provident_fund["year_to_date_yield"],
            yield_trailing_3_yrs= provident_fund["yield_trailing_3_yrs"],
            yield_trailing_5_yrs= provident_fund["yield_trailing_5_yrs"],
            avg_annual_yield_trailing_3yrs= provident_fund["avg_annual_yield_trailing_3yrs"],
            avg_annual_yield_trailing_5yrs= provident_fund["avg_annual_yield_trailing_5yrs"],
            standard_deviation= provident_fund["standard_deviation"],
            alpha= provident_fund["alpha"],
            sharpe_ratio= provident_fund["sharpe_ratio"]
        )
        db.session.add(new_provident_fund)
    db.session.commit()
    db.session.close()


def update_monthly_yield_fund(monthly_yield_fund):
    get_monthly_yield_fund = db.session.query(MonthlyYieldFund).filter_by(provident_fund_id=monthly_yield_fund["provident_fund_id"], date=monthly_yield_fund["date"])
    if not get_monthly_yield_fund.first():
        get_provident_fund = db.session.query(ProvidentFund).filter_by(fund_id=monthly_yield_fund["provident_fund_id"]).first()
        new_monthly_yield_fund = MonthlyYieldFund(provident_fund_id=monthly_yield_fund["provident_fund_id"],
                                                  date=monthly_yield_fund["date"],
                                                  monthly_yield=monthly_yield_fund["monthly_yield"], provident_fund= get_provident_fund)
        db.session.commit()
        db.session.close()


@periodic_task(
    run_every=(crontab(hour=22, minute=35)),  # Israel time
    name="get_provident_fund_data_and_add_to_db",
    ignore_result=True)
def get_provident_fund_data_and_add_to_db():
    print("-----------------------Start-----------------------")
    with app.app_context():
        start_time = datetime.datetime.now()
        # Step 1: Get all the data into 1 table
        print("Step 1: Get all the data into 1 table")
        url_data = 'https://data.gov.il/api/3/action/datastore_search?resource_id=a30dcbea-a1d2-482c-ae29-8f781f5025fb&limit=2855'
        web_url = urllib.request.urlopen(url_data)
        data = web_url.read()
        encoding = web_url.info().get_content_charset('utf-8')
        json_data = json.loads(data.decode(encoding))
        records = json_data['result']['records']
        df = pd.json_normalize(records)
        number_col = ['AVG_ANNUAL_MANAGEMENT_FEE', 'AVG_DEPOSIT_FEE', 'YEAR_TO_DATE_YIELD',
                      'YIELD_TRAILING_3_YRS', 'YIELD_TRAILING_5_YRS', 'AVG_ANNUAL_YIELD_TRAILING_3YRS',
                      'AVG_ANNUAL_YIELD_TRAILING_5YRS', 'STANDARD_DEVIATION', 'MONTHLY_YIELD',
                      'ALPHA', 'SHARPE_RATIO']
        for col in df:
            if col in number_col:
                df[col] = df[col].map(lambda a: from_string_to_num(a))
                df[col].round(3)
            else:
                try:
                    df[col] = pd.to_numeric(df[col])
                    df[col].round(3)
                except Exception:
                    try:
                        df[col] = pd.to_datetime(df[col])
                    except Exception:
                        continue
        columns = ['FUND_ID',
                   'FUND_NAME',  # שם המסלול לפי  החברה - לא חלק משאלות ששואלים את המשתמש
                   'FUND_CLASSIFICATION',  # סוג הקופה
                   'MANAGING_CORPORATION',  # החברה שמנהלת את הקופה
                   'REPORT_PERIOD',  #
                   'TARGET_POPULATION',  # אוכלוסיית יעד
                   'SPECIALIZATION',  # התמחות עיקרית
                   'SUB_SPECIALIZATION',  # התמחות משנית
                   'AVG_ANNUAL_MANAGEMENT_FEE',  # דמי ניהול ממוצעים- מחסכון
                   'AVG_DEPOSIT_FEE',  # דמי ניהול ממוצעים- מהפקדה
                   "MONTHLY_YIELD",
                   'YEAR_TO_DATE_YIELD',  # תשואה שנתית
                   "YIELD_TRAILING_3_YRS",
                   "YIELD_TRAILING_5_YRS",
                   'AVG_ANNUAL_YIELD_TRAILING_3YRS',  # תשואה מצטברת ל-3 שנים
                   'AVG_ANNUAL_YIELD_TRAILING_5YRS',  # תשואה מצטברת ל-5 שנים
                   "STANDARD_DEVIATION",
                   "ALPHA",
                   "SHARPE_RATIO"]
        df_need_col = pd.DataFrame(df, columns=columns)

        # Step 2: Create table for monthly yield for each fund
        print("Step 2: Create table for monthly yield for each fund")
        df_monthly_yield_fund = df_need_col[["FUND_ID", "REPORT_PERIOD", "MONTHLY_YIELD"]]
        df_monthly_yield_fund['REPORT_PERIOD'] = pd.to_datetime(df_monthly_yield_fund['REPORT_PERIOD'], format='%Y%m')

        # Step 3: Create table for each fund
        print("Step 3: Create table for each provident_fund")
        columns_provident_fund = ['FUND_ID',
                                  'FUND_NAME',  # שם המסלול לפי  החברה - לא חלק משאלות ששואלים את המשתמש
                                  'FUND_CLASSIFICATION',  # סוג הקופה
                                  'MANAGING_CORPORATION',  # החברה שמנהלת את הקופה
                                  'TARGET_POPULATION',  # אוכלוסיית יעד
                                  'SPECIALIZATION',  # התמחות עיקרית
                                  'SUB_SPECIALIZATION',  # התמחות משנית
                                  'AVG_ANNUAL_MANAGEMENT_FEE',  # דמי ניהול ממוצעים- מחסכון
                                  'AVG_DEPOSIT_FEE',  # דמי ניהול ממוצעים- מהפקדה
                                  'YEAR_TO_DATE_YIELD',  # תשואה שנתית
                                  "YIELD_TRAILING_3_YRS",
                                  "YIELD_TRAILING_5_YRS",
                                  'AVG_ANNUAL_YIELD_TRAILING_3YRS',  # תשואה מצטברת ל-3 שנים
                                  'AVG_ANNUAL_YIELD_TRAILING_5YRS',  # תשואה מצטברת ל-5 שנים
                                  "STANDARD_DEVIATION",
                                  "ALPHA",
                                  "SHARPE_RATIO",
                                  'REPORT_PERIOD'
                                  ]
        df_provident_fund = df_need_col[columns_provident_fund]
        df_provident_fund_after_filter = df_provident_fund.loc[df_provident_fund.REPORT_PERIOD == report_period]
        df_provident_fund_after_filter = df_provident_fund_after_filter.drop(columns=['REPORT_PERIOD'])

        # db.session.query(ProvidentFund).delete()
        # db.session.query(MonthlyYieldFund).delete()
        # db.session.commit()

        # Step 4: Insert provident_fund to DB
        print("Step 4: Insert provident_fund to DB")
        df_provident_fund_after_filter.columns = ['fund_id',
                                                  'fund_name',
                                                  'fund_classification',
                                                  'management_corporation',
                                                  'target_population',
                                                  'specialization',
                                                  'sub_specialization',
                                                  'avg_annual_management_fee',
                                                  'avg_deposit_fee',
                                                  'year_to_date_yield',
                                                  'yield_trailing_3_yrs',
                                                  'yield_trailing_5_yrs',
                                                  'avg_annual_yield_trailing_3yrs',
                                                  'avg_annual_yield_trailing_5yrs',
                                                  'standard_deviation',
                                                  'alpha',
                                                  'sharpe_ratio']
        df_provident_fund_after_filter.reset_index(drop=True, inplace=True)

        for index, row in df_provident_fund_after_filter.iterrows():
            update_provident_fund(row)

        # Step 5: Insert monthly_yield_fund to DB
        print("Step 5: Insert monthly_yield_fund to DB")
        df_monthly_yield_fund.columns = ['provident_fund_id',
                                         'date',
                                         'monthly_yield'
                                         ]
        df_monthly_yield_fund.reset_index(drop=True, inplace=True)
        for index, row in df_monthly_yield_fund.iterrows():
            update_monthly_yield_fund(row)

        end_time = datetime.datetime.now()
        date_time_difference = end_time - start_time
        date_time_difference_in_min = date_time_difference.total_seconds() / 60
        print("------------------------------FIN------------------------------")
        print("Takes ", date_time_difference_in_min, " Minutes")
