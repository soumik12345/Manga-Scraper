import string
import typing
import dataclasses
from bs4 import BeautifulSoup
from mangafetcher.manganelo_manager.base import ThreadedFetcher


@dataclasses.dataclass(frozen=True)
class SearchResult:
    title: str
    url: str


class SearchEngine(ThreadedFetcher):

    def __init__(self, query: str, *, threaded: bool = False) -> None:
        self.url = None
        self._query = query
        self._response = None
        super(SearchEngine, self).__init__(threaded)

    def _start(self) -> None:
        self.url = self._generate_url(self._query)
        self._response = self.send_request(self.url)

    def results(self) -> typing.Generator[SearchResult, None, None]:
        self._join_thread()
        soup = BeautifulSoup(self._response.content, "html.parser")
        results = soup.find_all(class_="search-story-item")
        for i, ele in enumerate(results):
            manga = ele.find(class_="item-img")
            title = manga.get("title", None)
            link = manga.get("href", None)
            yield SearchResult(title=title, url=link)

    @staticmethod
    def _generate_url(query: str) -> str:
        allowed_characters: str = string.ascii_letters + string.digits + "_"
        query = "".join([char.lower() for char in query.replace(" ", "_") if char in allowed_characters])
        return "http://manganelo.com/search/story/" + query
