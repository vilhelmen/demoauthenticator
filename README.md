# DemoAuthenticator

Tweaked DummyAuthenticator to allow for users and admins via configurable passwords.

Useful for demo/tutorial days.

Needs JH 1.0 because that's when I added 'admin' to the authentication dict.

Install:
```
pip install git+https://github.com/vilhelmen/demoauthenticator.git
```

Enable/configure:
```
c.JupyterHub.authenticator_class = 'demoauthenticator.DemoAuthenticator'
c.Authenticator.user_password = 'userpass123'
c.Authenticator.admin_password = 'adminpassword'
```

Or just dump the class into your JH config file, it probably works.

The admin password must be set to create admin-level accounts.

If the user and admin passwords are the same, only users will be created.
