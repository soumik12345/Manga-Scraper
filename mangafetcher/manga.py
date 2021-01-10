from typing import List
import streamlit as st


class Manga:

    def __init__(
            self, image_url: str, title: str, manga_url: str,
            authors: List[str], latest_chapter: str, overview: str):
        self._image_url = image_url
        self._title = title
        self._manga_url = manga_url
        self._authors = authors
        self._latest_chapter = latest_chapter
        self._overview = overview

    def get_image_url(self) -> str:
        return self._image_url

    def get_title(self) -> str:
        return self._title

    def get_manga_url(self) -> str:
        return self._manga_url

    def get_authors(self) -> List[str]:
        return self._authors

    def get_latest_chapter(self) -> str:
        return self._latest_chapter

    def get_overview(self) -> str:
        return self._overview

    def display(self):
        st.markdown('![]({})'.format(self._image_url))
        st.markdown('Title: [{}]({})'.format(self._title, self._manga_url))
        st.markdown('Authors: {}'.format(', '.join([author for author in self._authors])))
        st.markdown('Latest Chapter: {}'.format(self._latest_chapter))
        st.markdown('Overview: {}'.format(self._overview))
