from unittest import mock
import os
import pytz

from utils import get_current_date, download_zip_file, concate_strings, save_to_gcs

m = mock.Mock()
m.str1 = 'str1'
m.str2 = 'str2'
m.strf = 'str1str2'

m.time_zone = os.environ['TIME_ZONE']

def test_concate_strings():
    strf = concate_strings(m.str1, m.str2)
    assert m.strf == strf

def test_get_current_date():
    BTZ = pytz.timezone(m.time_zone)
    current_date = get_current_date(BTZ)
    assert current_date != None