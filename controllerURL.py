try:
    import _ssl
    _ssl.PROTOCOL_SSLv23 = _ssl.PROTOCOL_TLSv1
except:
    pass

try:
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
except:
    pass


import cookielib
import urllib2

import json
import logging


log = logging.getLogger(__name__)

print 'h'

class APIError(Exception):
    pass


class Controller:

    def __init__(self, host, username, password, port=8443):

        self.host = host
        self.port = port
        self.version = 'v4'
        self.username = username
        self.password = password
        self.site_id = 'default'
        self.url = 'https://' + host + ':' + str(port) + '/'
        self.api_url = self.url + 'api/s/default/'
        log.debug('Controller for %s', self.url)
        cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        log.debug('login() as %s', self.username)
        params = {'username': self.username, 'password': self.password}
        login_url = self.url
        login_url += 'api/login'
        params = json.dumps(params)
        self.opener.open(login_url, params).read()





    def _jsondec(self, data):

        obj = json.loads(data)
        if 'meta' in obj:
            if obj['meta']['rc'] != 'ok':
                raise APIError(obj['meta']['msg'])
        if 'data' in obj:
            return obj['data']
        return obj

    def _read(self, url, params=None):
        res = self.opener.open(url, params)
        return self._jsondec(res.read())

    def _login(self):
        log.debug('login() as %s', self.username)
        params = {'username': self.username, 'password': self.password}
        login_url = self.url
        login_url += 'api/login'
        params = json.dumps(params)
        self.opener.open(login_url, params).read()

    def _logout(self):
        log.debug('logout()')

        self.opener.open(self.url + 'logout').read()

