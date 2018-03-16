from flask_login import login_user, current_user, logout_user
from flask_restful import Resource, reqparse, fields, marshal_with, abort

from app.models import User, Permission

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


def check_login():
    return current_user.is_active



def checkPermission(permission,hasPermission):
    return (permission & hasPermission) == hasPermission




class UserStatussResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        user = current_user
        print(user.permission)
        # if user.permission == 1:
        #     return {'data':user}
        # else:
        #     return {'msg':'sorry no permission'}
        if checkPermission(user.permission,Permission.READ):
            print('you ')
        else:
            print('no permission')

    @marshal_with(result_fields)
    def post(self):
        args = parser.parse_args()

        username = args.get('username')
        password = args.get('password')
        user = User.query.filter_by(name=username).first()

        if user:
            if user.verify_password(password):
                login_user(user)
                return {'data': user}
        return {'msg': 'error', 'status': '805'}

    @marshal_with(result_fields)
    def delete(self):
        if check_login():
            logout_user()
            return {'msg':'ok'}
        else:
            abort(403)







