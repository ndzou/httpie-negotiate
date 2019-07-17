"""
SPNEGO (GSS Negotiate) auth plugin for HTTPie.

"""
import os

from httpie.plugins import AuthPlugin


__version__ = '1.0.1'
__author__ = 'Nan Zou'
__licence__ = 'BSD'


class NegotiateAuthPlugin(AuthPlugin):

    name = 'SPNEGO auth'
    auth_type = 'negotiate'
    description = ''

    def get_auth(self, username, password):
        from requests_kerberos import HTTPKerberosAuth, OPTIONAL, DISABLED, REQUIRED
        pref = os.environ.get("HTTPIE_KERBEROS_MUTUAL")
        if pref in  ["optional","OPTIONAL"]:
            kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
        elif pref in ["disabled","DISABLED"]:
            kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)
        elif pref == None or pref in ["required","REQUIRED"]:
            kerberos_auth = HTTPKerberosAuth()
        else:
            raise Exception("Invalid HTTPIE_KEBEROS_MUTUAL value {}".format(pref))
        return kerberos_auth
