from os.path import dirname, join

from restfulpy import Application as BaseApplication

from restfulpy_boilerplate import basedata, mockup
from restfulpy_boilerplate.controllers import Root
from restfulpy_boilerplate.authentication import Authenticator


__version__ = '0.1.0'


class Application(BaseApplication):
    __authenticator__ = Authenticator()
    builtin_configuration = """
    db: 
      url: postgresql://postgres:postgres@localhost/restfulpy_boilerplate
      test_url: postgresql://postgres:postgres@localhost/restfulpy_boilerplate_test
      administrative_url: postgresql://postgres:postgres@localhost/postgres
    """

    def __init__(self):
        super().__init__(
            'restfulpy-boilerplate',
            root=Root(),
            root_path=join(dirname(__file__), '..'),
            version=__version__,
        )

    # noinspection PyArgumentList
    def insert_basedata(self):  # pragma: no cover
        basedata.insert()

    # noinspection PyArgumentList
    def insert_mockup(self):
        mockup.insert()


restfulpy_boilerplate = Application()
