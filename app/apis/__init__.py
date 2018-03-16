from flask_restful import Api

from app.apis import CityResource, UserResource
from app.apis.CinemasResource import CinemasResource
from app.apis.CityResource import CitiesResource
from app.apis.HallResource import HallsResource
from app.apis.MovieResource import MoviesResource
from app.apis.UserResource import UsersResource
from app.apis.UserStatusResource import UserStatussResource

errors={
    'FBI':{
        'message':'FBI warning',
        'status':403,
    },
    'Not found':{
        'message':'lost',
        'status':404,
    }
}



api = Api(errors=errors,catch_all_404s=True)


def init_api(app):
    api.init_app(app)


api.add_resource(CitiesResource,'/cities/')
api.add_resource(MoviesResource,'/movies/')
api.add_resource(UsersResource,'/users/')
api.add_resource(UserStatussResource,'/userstatus/')
api.add_resource(HallsResource,'/halls/')
api.add_resource(CinemasResource,'/cinemas/')