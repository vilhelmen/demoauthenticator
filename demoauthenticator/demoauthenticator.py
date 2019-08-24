from jupyterhub.auth import DummyAuthenticator
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

        if self.admin_password and data['password'] == self.admin_password and data['password'] != self.password:
            login_state['admin'] = True
            return login_state

        if self.password:
            if data['password'] != self.password:
                login_state = None

        return login_state
