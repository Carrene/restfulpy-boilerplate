from nanohttp import html, json, RestController
from restfulpy.authorization import authorize
from restfulpy.controllers import RootController

import restfulpy_boilerplate
from .members import MembersController


class ApiV1(RestController):
    members = MembersController()

    @json
    def version(self):
        return {
            'version': restfulpy_boilerplate.__version__
        }


class Root(RootController):
    apiv1 = ApiV1()

    @html
    @authorize
    def index(self):
        return 'Index'

