from typing import List
from mangafetcher.mangahere_manager.chapter import Chapter
from ..utils import get_rendered_content


class MangaChapterManager:

    @staticmethod
    def get_manga_chapters(manga_url: str) -> List[Chapter]:
        response = get_rendered_content(manga_url)
        chapters = []
        for li in response.html.find('.detail-main-list')[0].find('li'):
            chapters.append(Chapter(
                title=li.find('.title3')[0].text, date=li.find('.title2')[0].text,
                url='http://www.mangahere.cc/' + li.find('a')[0].attrs['href']
            ))
        return chapters
