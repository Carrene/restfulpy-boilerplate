from restfulpy.testing import WebAppTestCase

from bddrest.authoring import given
from restfulpy_boilerplate import Application as RestfulpyBoilerplate


class BDDTestClass(WebAppTestCase):
    application = RestfulpyBoilerplate()

    def given(self, *args, **kwargs):
        return given(self.application, *args, **kwargs)


