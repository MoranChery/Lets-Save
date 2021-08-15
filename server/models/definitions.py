from sqlalchemy import inspect
from app.extensions import db


class Definitions(db.Model):
    __tablename__ = 'definitions'
    definitions_name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)

    @staticmethod
    def columns():
        return list(map(lambda c: c.key, inspect(__class__).attrs))

    def as_dict(self):
        ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return ret
