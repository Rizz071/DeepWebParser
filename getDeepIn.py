def getDeepIn():
    ua = UserAgent()

    headers = {
        'user-agent': ua.random
    }

    # Adding '/' to end of url_main if there are not such a one
    if url_main[-1] != '/':
        url_main += '/'

    # Getting bare site title
    if 'https://www.' in url_main:
        bare_site_title = url_main.replace('https://www.', '')
    if 'http://www.' in url_main:
        bare_site_title = url_main.replace('http://www.', '')
    if 'https://' in url_main:
        bare_site_title = url_main.replace('https://', '')
    if 'http://' in url_main:
        bare_site_title = url_main.replace('http://', '')

    response = requests.get(url=url_main, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    # Searching for site url structure
    urls = soup.findAll('a')
    # for url in urls:
    #     print(url)

    # Sorting for <a> where is 'href'
    urls_href = []
    for url in urls:
        if (url.get('href') != None) and (bare_site_title in url.get('href')):
            urls_href.append(url.get('href'))

    return urls_href
