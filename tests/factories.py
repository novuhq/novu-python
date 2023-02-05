from json.decoder import JSONDecodeError

from requests.models import HTTPError


class MockResponse:
    def __init__(self, status, data=None, headers=None, raise_on_call=False):
        self.status_code = status
        self.data = data
        self.headers = headers
        self.raise_on_call = raise_on_call

        if not self.data:
            self.data = {}

    def json(self) -> dict:
        if self.raise_on_call:
            raise JSONDecodeError("test", "", 0)
        return self.data

    def raise_for_status(self):
        if self.status_code > 399:
            raise HTTPError(response=self)

    def close(self):
        pass

    @property
    def ok(self):  # pylint: disable=C0103
        return self.status_code < 399

    def iter_content(self, chunk_size):
        i = 0
        while i < len(self.data):
            if i + chunk_size < len(self.data):
                yield self.data[i : i + chunk_size]  # noqa: E203
            else:
                yield self.data[i : len(self.data)]  # noqa: E203
            i += chunk_size
