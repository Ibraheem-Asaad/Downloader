
"""Download all files of a certiain file extension from a webpage"""


import re
import urlparse
import os
import urllib
from fnmatch import fnmatch
import requests
from lxml import html
from configs import REQ_AUTH, LOGIN_URL, LOGIN_FORM_INDEX, USER_FIELD_NAME, \
    USERNAME, PASS_FIELD_NAME, PASSWORD, LOGOUT_URL, TARGET_URLS, TARGET_FOLDER, \
    MAX_FILES, EXTS, REQ_CONF, NAME_PATTERN, name_mapping


def login(session):
    # TODO: check downloads with creds
    """Login to the website"""
    response = session.get(LOGIN_URL)
    response.raise_for_status()
    login_form = html.fromstring(response.content).forms[LOGIN_FORM_INDEX]
    payload = dict(login_form.fields)
    payload[USER_FIELD_NAME] = USERNAME
    payload[PASS_FIELD_NAME] = PASSWORD
    response = session.post(LOGIN_URL, payload)


def url_enc_non_ascii(url):
    """iri_to_uri auxiliary function"""
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), url)


def iri_to_uri(iri):
    """Converts an IRI to a URI"""
    parts = urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti == 1 else url_enc_non_ascii(
            part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )


def file_name_match(file_name):
    """returns if the file_name matches requirements (extension and pattern)"""
    return file_name.split('.')[-1] in EXTS and fnmatch(file_name, NAME_PATTERN)


def url_file_name(url):
    """returns the url's file name"""
    return url[url.rfind('/') + 1:]


def url_base(url):
    """returns the url's base url"""
    return url[:url.rfind('/')]


def logout(session):
    """Logout from the website"""
    response = session.get(LOGOUT_URL)
    response.raise_for_status()


if __name__ == '__main__':
    SESSION = requests.session()
    if REQ_AUTH:
        login(SESSION)

    os.chdir(TARGET_FOLDER)
    FILE_COUNT = 1

    for target_url in TARGET_URLS:
        response = SESSION.get(target_url)
        response.raise_for_status()
        page_html = html.fromstring(response.content)
        page_html.make_links_absolute(base_url=url_base(target_url))
        for (_, link_type, link_url, _) in page_html.iterlinks():
            if link_type == 'href':
                file_name = url_file_name(link_url)
                if file_name_match(file_name):
                    print link_url
                    if not REQ_CONF or raw_input('Download ' + file_name + ' ? (y/n)') == 'y':
                        FILE_COUNT = FILE_COUNT + 1
                        file_name = name_mapping(file_name, str(FILE_COUNT))
                        print 'Downloading as ' + file_name + ' ...'
                        urllib.urlretrieve(iri_to_uri(link_url), file_name)

    if REQ_AUTH:
        logout(SESSION)
