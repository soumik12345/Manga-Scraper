import requests


def get_page_content(url: str):
    response = requests.get(url, allow_redirects=True)
    page_content = response.content.decode()
    return page_content
