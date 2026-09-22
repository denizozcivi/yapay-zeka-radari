import requests


class Yanit:
    def __init__(self, durum=200, veri=None, basliklar=None):
        self.status_code = durum
        self._veri = veri or {}
        self.headers = basliklar or {}

    def json(self):
        return self._veri

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class SahteOturum:
    def __init__(self, yanitlar):
        self.yanitlar = list(yanitlar)
        self.cagrilar = []

    def _cagir(self, yontem, url, **kw):
        self.cagrilar.append((yontem, url, kw))
        return self.yanitlar.pop(0)

    def get(self, url, **kw):
        return self._cagir("GET", url, **kw)

    def post(self, url, **kw):
        return self._cagir("POST", url, **kw)

    def put(self, url, **kw):
        return self._cagir("PUT", url, **kw)
