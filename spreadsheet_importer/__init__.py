"""
spreadsheet_importer
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 201~2 by Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry_hipchat').version
except Exception, e:
    VERSION = 'unknown'


class Importer(object):
    header = {}
