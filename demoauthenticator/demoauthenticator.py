from jupyterhub.auth import DummyAuthenticator
from jupyterhub import orm
from traitlets import Bool, Integer, Set, Unicode, Dict, Any, default, observe


class DemoAuthenticator(DummyAuthenticator):
    """Dummy Authenticator for demos

    Allows passwords for user-level accounts and admin-level.

    If both passwords are the same, users are created, NOT admins.
    """

    password = Unicode(
        config=True,
        help="""
        Set a global password for all users wanting to log in.

        This allows users with any username to log in with the same static password.
        """,
    )

    admin_password = Unicode(
        config=True,
        help="""
        Set a global password for admin accounts. This password must be set for admin access.

        This allows users with any username to log in with the same static password.
        """,
    )

    async def authenticate(self, handler, data):
        """Checks global passwords for user/admin logins"""
        login_state = {'name': data['username'], 'admin': False}

        user_lookup = orm.User.find(db=self.db, name=self.normalize_username(data['username']))
        user_exists = user_lookup is not None

        if self.admin_password and data['password'] == self.admin_password and data['password'] != self.password:
            if user_exists and not user_lookup.admin:
                self.log.debug('%s (user) logging attempt with admin password', data['username'])
                login_state = None
            else:
                self.log.debug('%s logging in as admin', data['username']):
                login_state['admin'] = True
            return login_state

        if self.password:
            if data['password'] == self.password:
                if user_exists and user_lookup.admin:
                    self.log.warning('%s (admin) login attempt with user password!', data['username'])
                    login_state = None
                else:
                    self.log.debug('%s logging in as user', data['username'])
            else:
                self.log.debug('%s login rejected', data['username'])
                login_state = None

        return login_state
