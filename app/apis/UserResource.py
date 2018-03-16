from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash

from app.ext import model
from app.models import User

parser = reqparse.RequestParser()

parser.add_argument('username',type=str)
parser.add_argument("password",type=str)

user_fields={
    'id':fields.Integer,
    'name':fields.String,
}



result_fields={
    'status':fields.String(default='201'),
    'msg':fields.String(default='ok'),
    'data':fields.Nested(user_fields)
}


class UsersResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        args=parser.parse_args()

        username=args.get('username')
        password = args.get('password')
        user = User.query.filter_by(name=username).first()

        if user:
            if user.verify_password(password):
                return {'data':user}
        return {'msg':'error','status':'805'}


    @marshal_with(result_fields)
    def put(self):
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        user = User()
        user.name=username
        user.set_password(password)
        # password_hash = generate_password_hash(password=password)
        # user.password = password
        result = user.save()
        # check_password_hash(password_hash,password)
        if result=='success':
            return {'data':user}
        else:
            return {'msg':result}

    def delete(self):
        pass









