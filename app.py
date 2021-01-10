import streamlit as st
from mangafetcher.mangahere_manager import SearchEngine, MangaChapterManager


def run_app():
    st.markdown('# Manga Downloader')
    st.markdown('---')
    manga_query = st.text_input('Search your Manga...')
    if len(manga_query) > 0:
        search_results = SearchEngine.search(query_string=manga_query)
        if len(search_results) > 0:
            st.markdown('## Search Results')
            st.markdown('---')
            for result in search_results:
                result.display()
                st.markdown('---')
            manga_url = st.text_input('Enter URL of desired Manga:')
            if len(manga_url) > 0:
                manga_chapters = MangaChapterManager.get_manga_chapters(manga_url=manga_url)
                st.text('Number of Chapters: {}'.format(len(manga_chapters)))
                st.markdown('## Search Results')
                st.markdown('---')
                for chapter in manga_chapters[:5]:
                    chapter.display()
                    st.markdown('---')
        else:
            st.error('No Results Found!!! :(')


if __name__ == '__main__':
    run_app()
