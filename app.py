import streamlit as st
from mangafetcher import SearchEngine


def run_app():
    st.markdown('# Manga Downloader')
    st.markdown('---')
    col1, col2 = st.beta_columns(2)
    with col1:
        manga_query = st.text_input('Search your Manga...')
    with col2:
        n_top_results = st.number_input('Maximum Results to be Shown', value=10, min_value=1, step=1)
    search_engine = SearchEngine(manga_query, threaded=True)
    results = list(search_engine.results())
    if len(results) > 0:
        if len(results) > n_top_results:
            results = results[:n_top_results]
            st.markdown('### Top 10 Results:')
        else:
            st.markdown('### Top {} results'.format(len(results)))
        for result in results:
            st.markdown('[{}]({})'.format(result.title, result.url))


if __name__ == '__main__':
    run_app()
