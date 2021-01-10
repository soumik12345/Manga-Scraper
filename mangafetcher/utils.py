import requests
from requests_html import HTMLSession


def get_content(url: str, allow_redirects: bool = True) -> str:
    response = requests.get(url, allow_redirects=allow_redirects)
    content = response.content.decode()
    return content


def get_rendered_content(url: str) -> str:
    session = HTMLSession()
    response = session.get(url)
    return response
