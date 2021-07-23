from sqlalchemy import inspect
from app.extensions import db


class ProvidentFund(db.Model):

    __tablename__ = 'provident_fund'

    fund_name = db.Column(db.String, primary_key=True)
    fund_classification =  db.Column(db.String, nullable=False)
    management_corporation = db.Column(db.String, nullable=False)
    target_population = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    sub_specialization = db.Column(db.String, nullable=False)
    avg_annual_management_fee = db.Column(db.DECIMAL, nullable=False)
    avg_deposit_fee = db.Column(db.DECIMAL, nullable=False)
    year_to_date_yield = db.Column(db.DECIMAL, nullable=False)
    avg_annual_yield_trailing_3yrs = db.Column(db.DECIMAL, nullable=False)
    avg_annual_yield_trailing_5yrs = db.Column(db.DECIMAL, nullable=False)

    @staticmethod
    def columns():
        return list(map(lambda c: c.key, inspect(__class__).attrs))

    def as_dict(self):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return ret

