import streamlit as st
from mangafetcher.mangahere_manager import SearchEngine as MangahereSearchEngine
from mangafetcher.manganelo_manager import SearchEngine as ManganeloSearchEngine
from mangafetcher.manganelo_manager import ChapterManager as ManganeloChapterManager
from mangafetcher.mangahere_manager import MangaChapterManager as MangahereChapterManager


def run_app():
    st.markdown('# Manga Downloader')
    st.markdown('---')
    option = st.selectbox(
        'Which site would you like to scrape?',
        ('', 'Mangahere', 'Manganelo')
    )
    if option == 'Mangahere':
        manga_query = st.text_input('Search your Manga...')
        if len(manga_query) > 0:
            search_results = MangahereSearchEngine.search(query_string=manga_query)
            if len(search_results) > 0:
                st.markdown('## Search Results')
                st.markdown('---')
                for result in search_results:
                    result.display()
                    st.markdown('---')
                manga_url = st.text_input('Enter URL of desired Manga:')
                if len(manga_url) > 0:
                    manga_chapters = MangahereChapterManager.get_manga_chapters(manga_url=manga_url)
                    st.text('Number of Chapters: {}'.format(len(manga_chapters)))
                    st.markdown('## Search Results')
                    st.markdown('---')
                    for chapter in manga_chapters[:5]:
                        chapter.display()
                        st.markdown('---')
            else:
                st.error('No Results Found!!! :(')
    elif option == 'Manganelo':
        manga_query = st.text_input('Search your Manga...')
        if len(manga_query) > 0:
            fetcher = ManganeloSearchEngine(query=manga_query, threaded=True)
            results = fetcher.results()
            for result in results:
                st.markdown('[{}]({})'.format(result.title, result.url))
            manga_url = st.text_input('Enter URL of desired Manga:')
            if len(manga_url) > 0:
                chapters = ManganeloChapterManager.get_chapter_links(chapter_url=manga_url)
                st.text('Total Number of Chapters: {}'.format(len(chapters)))
                for chapter in chapters[:5]:
                    st.markdown('[{}]({})'.format(chapter.title, chapter.url))


if __name__ == '__main__':
    run_app()
