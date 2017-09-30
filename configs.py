
"""Credentials and configurations for downloader module"""


REQ_CRED = False
LOGIN_URL = ''
LOGIN_FORM_INDEX = 0
USER_FIELD_NAME = ''
USERNAME = ''
PASS_FIELD_NAME = ''
PASSWORD = ''
LOGOUT_URL = ''

TARGET_URL = 'http://webcourse.cs.technion.ac.il/236353/Spring2017/ho_Additional%20Materials.html'
TARGET_FOLDER = 'C:\\Users\\brhoo_000\\Downloads'
MAX_FILES = 3
EXTS = {'pdf', 'doc', 'docx', 'txt'}
REQ_CONF = False


def incr(max):
    """Incremental number generator"""
    i = 0
    while i < max:
        i = i + 1
        yield i

# this works because, in python
# default parameters are static - evaluated once
def name_mapping(name, num=incr(MAX_FILES)):
    """Changes each downloaded file name accordingly"""
    # TODO: generalize UTF-8 encoding
    # manipulate name patterns - use num.next() for incremental numbering:
    return name.replace('%20', ' ').replace('_', ' ').replace('-', ' ')
