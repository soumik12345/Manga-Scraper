import streamlit as st


class Chapter:

    def __init__(self, title: str, date: str, url: str):
        self._title = title
        self._date = date
        self._url = url

    def get_title(self):
        return self._title

    def get_date(self):
        return self._date

    def get_url(self):
        return self._url

    def display(self):
        st.markdown('Title: [{}]({})'.format(self._title, self._url))
        st.markdown('Date: {}'.format(self._date))
