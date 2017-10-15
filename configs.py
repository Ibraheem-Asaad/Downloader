
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
    r'https://webcourse.cs.technion.ac.il/236350/Spring2017/ho_Previous%20Exams.html'
}
TARGET_FOLDER = r'C:\Users\brhoo_000\Downloads\Documents'

# TODO: fix MAX_FILES limit
MAX_FILES = 100
EXTS = {'pdf', 'doc', 'docx', 'txt'}
NAME_PATTERN = '*'  # '*' for no restrictions
REQ_CONF = False


def name_mapping(name, file_num):
    """Changes each downloaded file name accordingly"""
    # TODO: generalize UTF-8 encoding
    # manipulate name patterns - use file_num for incremental numbering:
    return name.replace('%20', ' ').replace('_', ' ').replace('-', ' ')
