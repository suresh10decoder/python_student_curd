from flask import Blueprint
from flask_restplus import Api, Resource

from student.api.v1.student.api import ns as student_api
from student.middleware.restplus import api

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api.init_app(blueprint)

api.add_namespace(student_api)
