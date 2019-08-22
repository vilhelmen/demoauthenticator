"""
Demo authenticator that allows a user-level password and an admin-level password

Configure via c.Ju

After installation, you can enable it and configure by adding::

    c.JupyterHub.authenticator_class = 'demoauthenticator.DemoAuthenticator'
    c.Authenticator.user_password = 'userpass123'
    c.Authenticator.admin_password = 'adminpassword'

in your `jupyterhub_config.py` file.
"""

from demoauthenticator.demoauthenticator import DemoAuthenticator

__all__ = [DemoAuthenticator]
