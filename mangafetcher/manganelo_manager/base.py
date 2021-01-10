import requests
import threading


class ThreadedFetcher:

    def __init__(self, threaded: bool):
        if threaded:
            self._thread: threading.Thread = threading.Thread(target=self._start)
            self._thread.start()
        else:
            self._start()

    def _start(self) -> None:
        raise NotImplementedError()

    def _join_thread(self):
        if hasattr(self, "_thread") and self._thread.is_alive():
            self._thread.join()

    @staticmethod
    def send_request(url: str) -> requests.Response:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
        return requests.get(url, stream=True, timeout=5, headers=headers)