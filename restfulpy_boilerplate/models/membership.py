import os
import uuid
from hashlib import sha256

from sqlalchemy import Unicode, Integer, ForeignKey
from sqlalchemy.orm import synonym
from nanohttp import HttpBadRequest
from restfulpy.principal import JwtPrincipal, JwtRefreshToken
from restfulpy.orm import DeclarativeBase, Field, ModifiedMixin, ActivationMixin, SoftDeleteMixin


class Member(ActivationMixin, SoftDeleteMixin, ModifiedMixin, DeclarativeBase):
    __tablename__ = 'member'

    id = Field(Integer, primary_key=True)
    email = Field(Unicode(100), unique=True, index=True, json='email',
                  pattern=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    _password = Field('password', Unicode(128), index=True, json='password', protected=True, min_length=6)

    type = Field(Unicode(50))

    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'polymorphic_on': type
    }

    @property
    def roles(self):
        return []

    @classmethod
    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hashed_pass = sha256()
        # Make sure password is a str because we cannot hash unicode objects
        hashed_pass.update((password + salt).encode('utf-8'))
        hashed_pass = hashed_pass.hexdigest()

        password = salt + hashed_pass
        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        min_length = self.__class__.password.info['min_length']
        if len(password) < min_length:
            raise HttpBadRequest('Please enter at least %d characters for password.' % min_length)
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym('_password', descriptor=property(_get_password, _set_password), info=dict(protected=True))

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hashed_pass = sha256()
        hashed_pass.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hashed_pass.hexdigest()

    def create_jwt_principal(self, session_id=None):
        # FIXME: IMPORTANT Include user password as salt in signature

        if session_id is None:
            session_id = str(uuid.uuid4())

        return JwtPrincipal(dict(
            id=self.id,
            roles=self.roles,
            email=self.email,
            sessionId=session_id,
        ))

    def create_refresh_principal(self):
        return JwtRefreshToken(dict(
            id=self.id
        ))


class God(Member):
    __tablename__ = 'god'
    __mapper_args__ = {
        'polymorphic_identity': __tablename__
    }

    id = Field(Integer, ForeignKey(Member.id), primary_key=True)

    @property
    def roles(self):
        return ['god']
