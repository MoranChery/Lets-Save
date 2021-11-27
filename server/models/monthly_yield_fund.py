from sqlalchemy import inspect
from app.extensions import db


class MonthlyYieldFund(db.Model):

    __tablename__ = 'monthly_yield_fund'

    date = db.Column(db.DATE, primary_key=True)
    monthly_yield = db.Column(db.DECIMAL, nullable=True)
    provident_fund_id = db.Column(db.Integer, db.ForeignKey('provident_fund.fund_id'), primary_key=True)


    @staticmethod
    def columns():
        return list(map(lambda c: c.key, inspect(__class__).attrs))

    def as_dict(self):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return ret
