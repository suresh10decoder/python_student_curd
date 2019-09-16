from marshmallow import fields

from student.data_access.db_models import Students
from student.extensions import ma


class StudentSchema(ma.ModelSchema):

    student = fields.Nested('LenderSchema', only=['id', 'studentname', 'cgpa', 'dob', 'college_code', 'location'])

    class Meta:
        model = Students
