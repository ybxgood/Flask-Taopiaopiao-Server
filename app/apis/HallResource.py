from flask_login import current_user
from flask_restful import Resource, abort

from app.models import Permission


def require_login(f):
    def check(*args,**kwargs):
        if current_user.is_active:
            return f(*args,**kwargs)
        else:
            abort(404)
    return check


def require_permission(per):
    def require(f):
        def check(*args,**kwargs):
            if current_user.is_active:
                if (current_user.permission & per)==per:
                    return f(*args,**kwargs)
                else:
                    abort(403)
            else:
                abort(401)
        return check
    return require



class HallsResource(Resource):
    @require_permission(Permission.WRITE)
    def get(self):
        return {'data':'nihao'}

    @require_login
    def post(self):
        return {'data':'welcome'}



