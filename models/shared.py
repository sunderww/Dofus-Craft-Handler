from flask_sqlalchemy       import SQLAlchemy
from sqlalchemy.inspection  import inspect
from datetime               import datetime


db = SQLAlchemy()

class Serializable(object):

    def serialize(self, **kwargs):
        # Get all the attributes in a dict then transform
        # the attributes that are not JSON serializable (e.g. dates)
        d = {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        return {k: v.isoformat() if hasattr(v, 'isoformat') else v for (k, v) in d.items()}

    @staticmethod
    def serialize_list(l, **kwargs):
        return [m.serialize(**kwargs) for m in l]

class Auditable(object):
    created_at = db.Column(db.Date, default=datetime.now())
    updated_at = db.Column(db.Date, default=datetime.now(), onupdate=datetime.now())
