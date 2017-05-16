from .exceptions import *
import requests
import re


class JolokiaClient(object):

    def __init__(self, base_url, *args, **kwargs):

        if not base_url:
            raise UrlNotSpecifiedException()

        self.base_url = base_url
        self.session = requests.Session()

    def execute(self, *args, **kwargs):
        """Execute JMX operation on MBean."""
        pass

    def list(self, *args, **kwargs):
        """Return a list of all MBeans on all available MBean servers."""
        pass

    def search(self, *args, **kwargs):
        """Search all available MBean servers for the desired MBean"""
        pass

    def version(self, *args, **kwargs):
        pass

    def get_attribute(self, *args, **kwargs):
        """Returns an attribute's value. Domain and MBean type must be specified"""
        domain = kwargs.pop('domain', '')
        mbean = kwargs.pop('mbean', '')
        attribute = kwargs.pop('attribute', '')

        if not domain or not mbean:
            raise IllegalArgumentException('You must specify a domain and MBean type.')

        data = {
            'type': 'read',
            'mbean': '{0}:{1}'.format(domain, mbean),
            'attribute': attribute
        }

        return self.session.post(self.base_url, data=data)

    def set_attribute(self, data=None, *args, **kwargs):
        pass

    """Private methods are not guaranteed to be stable. Use at your peril!"""
    def _validate_url(self, url):
        if not url:
            raise UrlNotSpecifiedException()

        regex = re.compile(r'^https?://([\w\d]+\.)*[\w\d]+(:[\d]{2,})*(/+[\w\d]*)*$')
        if not regex.match(url):
            raise MalformedUrlException('Base url should be of the form http[s]://hostname[:port][path]')


class JBossJolokiaClient(JolokiaClient):

    def read(self, domain='jboss.as.expr', type=None, attribute=None, *args, **kwargs):
        pass
