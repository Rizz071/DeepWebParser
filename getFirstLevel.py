import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def getFirstLevel(url_main):
    ua = UserAgent()

    headers = {
        'user-agent': ua.random
    }

    # Adding '/' to end of url_main if there are not such a one
    if url_main[-1] != '/':
        url_main += '/'

    # Getting bare site title
    if 'https://www.' in url_main:
        url_first_level_barebone = url_main.replace('https://www.', '')
    if 'http://www.' in url_main:
        url_first_level_barebone = url_main.replace('http://www.', '')
    if 'https://' in url_main:
        url_first_level_barebone = url_main.replace('https://', '')
    if 'http://' in url_main:
        url_first_level_barebone = url_main.replace('http://', '')

    url_first_level_barebone = url_first_level_barebone[0:url_first_level_barebone.find('/')]
    url_first_level = url_main[0:url_main.find('/')] + '//' + url_first_level_barebone + '/'




    return url_first_level, url_first_level_barebone