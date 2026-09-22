import pytest
import requests

import instagram
from sahte import SahteOturum, Yanit


def test_yayinla_akisi():
    oturum = SahteOturum([
        Yanit(veri={"id": "K1"}),
        Yanit(veri={"status_code": "IN_PROGRESS"}),
        Yanit(veri={"status_code": "FINISHED"}),
        Yanit(veri={"id": "M1"}),
    ])
    medya = instagram.yayinla("metin", "https://g/kart.jpg", "tok", "U1", oturum=oturum, uyu=lambda s: None)

    assert medya == "M1"
    olustur = oturum.cagrilar[0]
    assert olustur[1].endswith("/U1/media")
    assert olustur[2]["data"]["image_url"] == "https://g/kart.jpg"
    assert olustur[2]["data"]["caption"] == "metin"
    yayin = oturum.cagrilar[3]
    assert yayin[1].endswith("/U1/media_publish")
    assert yayin[2]["data"]["creation_id"] == "K1"


def test_konteyner_hatasi():
    oturum = SahteOturum([Yanit(veri={"id": "K1"}), Yanit(veri={"status_code": "ERROR"})])
    with pytest.raises(RuntimeError, match="ERROR"):
        instagram.yayinla("m", "https://g", "tok", "U1", oturum=oturum, uyu=lambda s: None)


def test_konteyner_zaman_asimi():
    oturum = SahteOturum([Yanit(veri={"id": "K1"})] + [Yanit(veri={"status_code": "IN_PROGRESS"})] * 10)
    with pytest.raises(TimeoutError):
        instagram.yayinla("m", "https://g", "tok", "U1", oturum=oturum, uyu=lambda s: None)


class PatlayanOturum:
    """requests gibi davranır: hata mesajına token'lı URL'yi koyar."""

    def _patla(self, url, **kw):
        token = (kw.get("params") or kw.get("data") or {}).get("access_token", "")
        raise requests.ConnectionError(f"Max retries exceeded with url: {url}?access_token={token}")

    get = post = _patla


def test_hata_mesajinda_token_gorunmez():
    with pytest.raises(RuntimeError) as hata:
        instagram.kim("GIZLI-IG-TOKEN", oturum=PatlayanOturum())
    assert "GIZLI-IG-TOKEN" not in str(hata.value)
    assert "***" in str(hata.value)
    assert hata.value.__cause__ is None and hata.value.__suppress_context__


def test_yayinla_hatasinda_token_gorunmez():
    with pytest.raises(RuntimeError) as hata:
        instagram.yayinla("m", "https://g", "GIZLI-IG-TOKEN", "U1", oturum=PatlayanOturum(), uyu=lambda s: None)
    assert "GIZLI-IG-TOKEN" not in str(hata.value)


def test_token_yenile():
    oturum = SahteOturum([Yanit(veri={"access_token": "YENI", "expires_in": 5184000})])
    assert instagram.token_yenile("ESKI", oturum=oturum)["access_token"] == "YENI"
    assert oturum.cagrilar[0][2]["params"]["grant_type"] == "ig_refresh_token"
