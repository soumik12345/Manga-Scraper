from typing import List
from dataclasses import dataclass
from ..utils import get_rendered_content


@dataclass(frozen=True)
class ChapterResult:
    title: str
    url: str


class ChapterManager:

    @staticmethod
    def get_chapter_links(chapter_url) -> List[ChapterResult]:
        response = get_rendered_content(url=chapter_url)
        chapters = [
            ChapterResult(title=a.text, url=a.attrs['href'])
            for a in response.html.find('.row-content-chapter')[0].find('a')
        ]
        return chapters
