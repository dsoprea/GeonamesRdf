try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    # Python 2.7
    from urllib import urlencode

try:
    unicode
except NameError:
    def make_unicode(s):
        return str(s)
else:
    def make_unicode(s):
        return unicode(s)
