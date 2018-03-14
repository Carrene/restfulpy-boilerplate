
from nanohttp import HttpConflict, HttpBadRequest
from restfulpy.authentication import StatefulAuthenticator

from restfulpy_boilerplate.models import Member


class Authenticator(StatefulAuthenticator):

    @staticmethod
    def safe_member_lookup(condition):
        member = Member.exclude_deleted().filter(condition).one_or_none()

        if member is None:
            raise HttpBadRequest()

        if not member.is_active:
            raise HttpConflict(reason='user-deactivated')

        return member

    def create_principal(self, member_id=None, session_id=None, **kwargs):
        member = self.safe_member_lookup(Member.id == member_id)
        return member.create_jwt_principal(session_id=session_id)

    def create_refresh_principal(self, member_id=None):
        member = self.safe_member_lookup(Member.id == member_id)
        return member.create_refresh_principal()

    def validate_credentials(self, credentials):
        email, password = credentials
        member = self.safe_member_lookup(Member.email == email)

        if not member.validate_password(password):
            return None
        return member
