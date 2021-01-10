import streamlit as st
from mangafetcher import SearchEngine


def run_app():
    st.markdown('# Manga Downloader')
    st.markdown('---')
    manga_query = st.text_input('Search your Manga...')
    if len(manga_query) > 0:
        search_results = SearchEngine.search(query_string=manga_query)
        for result in search_results:
            result.display()


if __name__ == '__main__':
    run_app()
