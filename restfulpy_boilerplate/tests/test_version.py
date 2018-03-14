import unittest

from bddrest.authoring import then, response, and_

import restfulpy_boilerplate
from restfulpy_boilerplate.tests.helpers import BDDTestClass


class VersionTestCase(BDDTestClass):

    def test_version(self):
        call = dict(
            title='Application version',
            description='Get application version',
            url='/apiv1/version',
            verb='GET',
        )

        with self.given(**call):
            then(response.status_code == 200)
            and_('version' in response.json)
            and_(response.json['version'] == restfulpy_boilerplate.__version__)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
