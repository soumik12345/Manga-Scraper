import streamlit as st
from appmodule import comics_download_module


def run_app():
    option = st.selectbox(
        'What would you like to download?',
        ('', 'Comics', 'Manga')
    )
    if option == 'Comics':
        comics_download_module()
    elif option == 'Manga':
        st.error('Under Development')


if __name__ == '__main__':
    run_app()
