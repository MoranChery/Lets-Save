from sqlalchemy import inspect
from app.extensions import db
from sqlalchemy.orm import relationship


class ProvidentFund(db.Model):

    __tablename__ = 'provident_fund'

    fund_id = db.Column(db.Integer, primary_key=True, unique=True)
    fund_name = db.Column(db.String, nullable=False)
    fund_classification = db.Column(db.String, nullable=False)
    management_corporation = db.Column(db.String, nullable=False)
    target_population = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    sub_specialization = db.Column(db.String, nullable=True)
    avg_annual_management_fee = db.Column(db.DECIMAL, nullable=True)
    avg_deposit_fee = db.Column(db.DECIMAL, nullable=True)
    year_to_date_yield = db.Column(db.DECIMAL, nullable=True)
    yield_trailing_3_yrs = db.Column(db.DECIMAL, nullable=True)
    yield_trailing_5_yrs = db.Column(db.DECIMAL, nullable=True)
    avg_annual_yield_trailing_3yrs = db.Column(db.DECIMAL, nullable=True)
    avg_annual_yield_trailing_5yrs = db.Column(db.DECIMAL, nullable=True)
    standard_deviation = db.Column(db.DECIMAL, nullable=True)
    alpha = db.Column(db.DECIMAL, nullable=True)
    sharpe_ratio = db.Column(db.DECIMAL, nullable=True)
    monthly_yield = relationship("MonthlyYieldFund", back_populates="provident_fund")


    @staticmethod
    def columns():
        return list(map(lambda c: c.key, inspect(__class__).attrs))

    def as_dict(self):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return ret
