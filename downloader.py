
"""Download all files with an extension from a webpage"""


import requests
import urllib
from lxml import html
from configs import NEEDS_CRED, LOGIN_URL, LOGIN_FORM_INDEX, \
    USER_FIELD_NAME, USERNAME, PASS_FIELD_NAME, PASSWORD, LOGOUT_URL, TARGET_URL, MAX_FILES, EXTS


def login(session):
    """Login to the website"""
    response = session.get(LOGIN_URL)
    response.raise_for_status()
    login_form = html.fromstring(response.content).forms[login_form_index]
    payload = dict(login_form.fields)
    payload[user_field_name] = USERNAME
    payload[pass_field_name] = PASSWORD
    response = session.post(LOGIN_URL, payload)


def file_ext(url):
    """returns the url file extension"""
    return url.split('.')[-1]


def download(session):
    """Download all files in that webpage"""
    response = session.get(TARGET_URL)
    response.raise_for_status()
    page_html = html.fromstring(response.content)
    for link in page_html.iterlinks():
        if link[1] == 'href':
            if file_ext(link[2]) in EXTS:
                print link[2]


def logout(session):
    """Logout from the website"""
    response = session.get(LOGOUT_URL)
    response.raise_for_status()


SESSION = requests.session()
if NEEDS_CRED:
    login(SESSION)
download(SESSION)
if NEEDS_CRED:
    logout(SESSION)
