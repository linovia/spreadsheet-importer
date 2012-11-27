"""
Test csv import
"""

from unittest2 import TestCase

from spreadsheet_importer import Importer


class DemoImporter(Importer):
    header = {
        'firstname': (),
        'value': ('optional'),
        'lastname': (),
    }


class TestToto(TestCase):

    def test_well_formed_csv(self):
        csv = """
firstname,value,lastname
Abraham,,Lincoln
Napoleon,emperor,Bonaparte
"""
        importer = DemoImporter.from_csv(csv)
        self.assertEqual(importer.results, [
            {
                'firstname': 'Abraham',
                'lastname': 'Lincoln',
            }, {
                'firstname': 'Napoleon',
                'value': 'emperor',
                'lastname': 'Bonaparte',
            }
        ])
