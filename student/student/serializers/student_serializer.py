from flask_restplus import fields

from student.middleware.restplus import api

student = api.model('Student', {
    'studentname': fields.String(required=True),
    'cgpa': fields.Integer(required=True),
    'dob': fields.String(required=True),
    'college_code': fields.Integer(required=True),
    'location': fields.String(required=True)
})
