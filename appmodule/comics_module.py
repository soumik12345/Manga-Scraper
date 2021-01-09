import streamlit as st
from comics_downloader import ReadComicsOnlineDownloader


def comics_download_module():
    issue_list_url = st.text_input('Enter Url of Issue List Page:')
    if len(issue_list_url) > 0:
        downloader = ReadComicsOnlineDownloader(issue_list_url=issue_list_url, search_string='')
        downloader.get_list_of_issues(using_app=True)
