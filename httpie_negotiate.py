"""
SPNEGO (GSS Negotiate) auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin


__version__ = '1.0.0'
__author__ = 'Nan Zou'
__licence__ = 'BSD'


class NegotiateAuthPlugin(AuthPlugin):

    name = 'SPNEGO auth'
    auth_type = 'negotiate'
    description = ''

    def get_auth(self, username, password):
        from requests_kerberos import HTTPKerberosAuth
        return HTTPKerberosAuth()
