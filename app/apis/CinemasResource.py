import fields as fields
from flask_restful import Resource, marshal_with, fields, reqparse
from sqlalchemy import and_

from app.models import Cinemas


cinemas_fields = {
    'name':fields.String,
    'address':fields.String,
    'phone':fields.String,
    'score':fields.Float,
    'hallnum':fields.String,
}



result_fields = {
    'data':fields.List(fields.Nested(cinemas_fields)),
    'msg':fields.String('ok'),
    'status':fields.String('200'),
}


parser = reqparse.RequestParser()
parser.add_argument('score')
parser.add_argument('city')


class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        score_args = args.get('score')
        city = args.get('city')
        select = []
        if score_args:
           select.append(Cinemas.score.__gt__(score_args))
        if city:
            select.append(Cinemas.city.__eq__(city))
        selection = and_(*select)
        cinemas = Cinemas.query.filter(selection).all()

        return {'data':cinemas}




    def post(self):
        pass


