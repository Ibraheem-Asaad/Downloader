
"""Credentials and configurations for downloader module"""


REQ_CRED = False
LOGIN_URL = ''
LOGIN_FORM_INDEX = 0
USER_FIELD_NAME = ''
USERNAME = ''
PASS_FIELD_NAME = ''
PASSWORD = ''
LOGOUT_URL = ''

TARGETS_URLS = {
    'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho_Lectures.html',
    'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho_Tutorials.html',
    'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho.html'
}
TARGET_FOLDER = 'C:\\Users\\brhoo_000\\Downloads\\Documents'
MAX_FILES = 100
EXTS = {'pdf', 'doc', 'docx', 'txt'}
REQ_CONF = False


def incr(max):
    """Incremental number generator"""
    i = 0
    while i < max:
        i = i + 1
        yield i


def name_mapping(name, file_num):
    """Changes each downloaded file name accordingly"""
    # TODO: generalize UTF-8 encoding
    # manipulate name patterns - use file_num for incremental numbering:
    return name.replace('%20', ' ').replace('_', ' ').replace('-', ' ')
