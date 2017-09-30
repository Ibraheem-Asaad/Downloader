
"""Credentials and configurations for downloader module"""


REQ_AUTH = False
LOGIN_URL = ''
LOGIN_FORM_INDEX = 0
USER_FIELD_NAME = ''
USERNAME = ''
PASS_FIELD_NAME = ''
PASSWORD = ''
LOGOUT_URL = ''

TARGET_URLS = {
    r'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho_Lectures.html',
    r'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho_Tutorials.html',
    r'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho.html'
}
TARGET_FOLDER = r'C:\Users\brhoo_000\Downloads\Documents'

# TODO: fix MAX_FILES limit
MAX_FILES = 100
EXTS = {'pdf', 'doc', 'docx', 'txt'}
NAME_PATTERN = '*CRY*'  # '*' for no restrictions
REQ_CONF = True


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
