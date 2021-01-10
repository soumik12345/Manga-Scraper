from typing import List
from mangafetcher.manga import Manga
from bs4 import BeautifulSoup
from mangafetcher.utils import get_rendered_content


class SearchEngine:

    @staticmethod
    def search(query_string: str) -> List[Manga]:
        query_string = query_string.strip().lower().replace(' ', '+')
        response = get_rendered_content(url='http://www.mangahere.cc/search?title=' + query_string)
        content = response.html.find('.line-list')[0].html
        soup = BeautifulSoup(content)
        li_tags = soup.findAll('ul')[0].findAll('li')
        image_urls = [li_tag.findAll('a')[0].findAll('img')[0]['src'] for li_tag in li_tags]
        titles = [li_tag.findAll(
            'p', {'class': 'manga-list-4-item-title'})[0].findAll('a')[0].text for li_tag in li_tags]
        manga_urls = ['http://www.mangahere.cc/' + li_tag.findAll(
            'p', {'class': 'manga-list-4-item-title'})[0].findAll('a')[0]['href'] for li_tag in li_tags]
        authors = [
            [a_tag.text for a_tag in li_tag.findAll('p', {'class': 'manga-list-4-item-tip'})[0].findAll('a')]
            for li_tag in li_tags
        ]
        latest_chapters = [
            li_tag.findAll('p', {'class': 'manga-list-4-item-tip'})[1].findAll('a')[0].text
            for li_tag in li_tags
        ]
        overviews = [li_tag.findAll('p', {'class': 'manga-list-4-item-tip'})[2].text for li_tag in li_tags]
        # print(latest_chapters)
        mangas = []
        for index, image_url in enumerate(image_urls):
            mangas.append(Manga(
                image_url=image_url, title=titles[index], manga_url=manga_urls[index],
                authors=authors[index], latest_chapter=latest_chapters[index], overview=overviews[index]
            ))
        return mangas
