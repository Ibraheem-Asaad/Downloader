
"""Download all files with an extension from a webpage"""


import requests
from lxml import html
from configs import needs_cred, login_url, login_form_index, user_field_name, username, \ 
pass_field_name, password, logout_url, target_url, max_files, exts


def login(session):
    """Login to the website"""
    response = session.get(LOGIN_URL)
    response.raise_for_status()
    login_form = html.fromstring(response.content).forms[login_form_index]
    payload = dict(login_form.fields)
    payload[user_field_name] = USERNAME
    payload[pass_field_name] = PASSWORD
    response = session.post(LOGIN_URL, payload)


def download(session):
    """Download all files in that webpage"""
    course_url = TARGET_URL + '/' + course_number
    response = session.get(course_url)
    response.raise_for_status()
    course_html = html.fromstring(response.content)
    vacancie_list = course_html.find_class('label label-success')
    vacancies = 0
    for vacancy in vacancie_list:
        vacancies = vacancies + int(vacancy.text)
    print 'Total vacancies in ' + course_number + ': ' + str(vacancies)
    if vacancies > 0:
        if BEEP_ON_SUCCESS:
            print '\a'  # cross-platform beep
        if STOP_ON_SUCCESS:
            exit(0)


def logout(session):
    """Logout from the website"""
    response = session.get(LOGOUT_URL)
    response.raise_for_status()


SESSION = requests.session()
if needs_cred:
	login(SESSION)
download(SESSION)
if needs_cred:
	logout(SESSION)