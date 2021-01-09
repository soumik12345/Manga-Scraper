import pandas as pd
import streamlit as st
from operator import is_not
from functools import partial
from bs4 import BeautifulSoup
from .utils import get_page_content


class ReadComicsOnlineDownloader:

    def __init__(self, issue_list_url: str, search_string: str):
        self.issue_list_url = issue_list_url
        self.issue_names = []
        self.issue_urls = []

    def get_list_of_issues(self, using_app: bool):
        page_content = get_page_content(self.issue_list_url)
        soup = BeautifulSoup(page_content)
        issue_lists_content = list(filter(
            partial(is_not, None),
            [div_outer.find('ul') for div_outer in soup.findAll('div', {'class': 'section group'})]))[0]
        list_tags = issue_lists_content.findAll('a')
        self.issue_urls = ['https://readcomiconline.to' + list_tag['href'] for list_tag in list_tags]
        self.issue_names = [list_tag.findAll('span')[0].text for list_tag in list_tags]
        assert len(self.issue_urls) == len(self.issue_names)
        for i, issue_name in enumerate(self.issue_names):
            print(issue_name, self.issue_urls[i])
        if using_app:
            dataframe = pd.DataFrame(data={
                'Issue': self.issue_names, 'URL': self.issue_urls
            })
            if using_app:
                st.dataframe(data=dataframe)
