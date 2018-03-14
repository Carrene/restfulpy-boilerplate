import unittest

from restfulpy.orm import DBSession
from restfulpy.principal import JwtPrincipal
from bddrest.authoring import when, then, response, and_

from restfulpy_boilerplate.tests.helpers import BDDTestClass
from restfulpy_boilerplate.models import God


class AuthenticationTestCase(BDDTestClass):

    @classmethod
    def mockup(cls):
        god = God()
        god.email = 'god@example.com'
        god.password = '123456'
        god.is_active = True
        DBSession.add(god)
        DBSession.commit()

    def test_login(self):
        call = dict(
            title='Login',
            description='Login to system as god',
            url='/apiv1/members',
            verb='LOGIN',
            form={
                'email': 'god@example.com',
                'password': '123456',
            }
        )
        with self.given(**call):
            then(response.status_code == 200)
            and_('token' in response.json)
            principal = JwtPrincipal.load(response.json['token'])
            and_('sessionId' in principal.payload)

            when(
                'Trying to login with invalid email and_ password',
                form={
                    'email': 'invalidEmail@example.com',
                    'password': 'invalidPassword',
                }
            )
            then(response.status_code == 400)

            when(
                'Trying to login with invalid password',
                form={
                    'email': 'god@example.com',
                    'password': 'invalidPassword',
                }
            )
            then(response.status_code == 400)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
