from sqlalchemy import inspect
from app.extensions import db


class Definitions(db.Model):
    __tablename__ = 'definitions'
    definitions_name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)

    # todo : need to and those description
    description_needed = ['FUND_NAME',  # שם המסלול לפי  החברה - לא חלק משאלות ששואלים את המשתמש
                          'FUND_CLASSIFICATION',  # סוג הקופה
                          'MANAGING_CORPORATION',  # החברה שמנהלת את הקופה
                          'TARGET_POPULATION',  # אוכלוסיית יעד
                          'SPECIALIZATION',  # התמחות עיקרית
                          'SUB_SPECIALIZATION',  # התמחות משנית
                          'AVG_ANNUAL_MANAGEMENT_FEE',  # דמי ניהול ממוצעים- מחסכון
                          'AVG_DEPOSIT_FEE',  # דמי ניהול ממוצעים- מהפקדה
                          'YEAR_TO_DATE_YIELD',  # תשואה שנתית
                          'AVG_ANNUAL_YIELD_TRAILING_3YRS',  # תשואה מצטברת ל-3 שנים
                          'AVG_ANNUAL_YIELD_TRAILING_5YRS']  # תשואה מצטברת ל-5 שנים

    @staticmethod
    def columns():
        return list(map(lambda c: c.key, inspect(__class__).attrs))

    def as_dict(self):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return ret
