from student.data_access.db_models.base import Base
from student.extensions import db


class Students(db.Model, Base):
    """Basic Product model
    """
    id = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.String(30))
    cgpa = db.Column(db.Integer())
    dob = db.Column(db.String(30))
    college_code = db.Column(db.Integer())
    location = db.Column(db.String(30))

    def __init__(self, **kwargs):
        super(Students, self).__init__(**kwargs)

    def __repr__(self):
        return "<Students %s>" % self.id
