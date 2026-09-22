import datetime as dt
import json

import pytest

import publish

ORTAM = {
    "LINKEDIN_TOKEN": "LI-GIZLI", "LINKEDIN_PERSON_URN": "urn:li:person:x",
    "IG_TOKEN": "IG-GIZLI", "IG_USER_ID": "U1",
    "LINKEDIN_TOKEN_EXPIRES": "2026-12-01", "IG_TOKEN_EXPIRES": "2026-12-01",
}
BUGUN = dt.date(2026, 9, 22)


@pytest.fixture
def depo(tmp_path):
    (tmp_path / "yayinlananlar.md").write_text("# Yayınlanan konular\n\n", encoding="utf-8")
    klasor = tmp_path / "taslaklar" / "2026-09-22"
    klasor.mkdir(parents=True)
    (klasor / "linkedin.md").write_text("LI metni\n", encoding="utf-8")
    (klasor / "instagram.md").write_text("IG metni\n", encoding="utf-8")
    (klasor / "kart.jpg").write_bytes(b"jpeg")
    meta = {"tarih": "2026-09-22", "konu": "Gemini", "kaynak_url": "https://k", "alt_metin": "alt",
            "durum": "taslak", "linkedin_post": None, "instagram_post": None}
    (klasor / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    return klasor


def meta_oku(klasor):
    return json.loads((klasor / "meta.json").read_text(encoding="utf-8"))


def li_basarili(*a, **k):
    return {"post": "urn:li:share:9", "yorum_hatasi": None}


def ig_basarili(metin, url, token, uid):
    assert url == "https://raw.test/taslaklar/2026-09-22/kart.jpg"
    return "M1"


def ig_hatali(*a, **k):
    raise RuntimeError("bozuk token IG-GIZLI")


def test_iki_platform_basarili(depo):
    sonuc = publish.yayinla(depo, ORTAM, "https://raw.test/", li=li_basarili, ig=ig_basarili, bugun=BUGUN)
    assert sonuc["durum"] == "yayinlandi"
    assert meta_oku(depo)["durum"] == "yayinlandi"
    assert "- 2026-09-22 · Gemini" in (depo.parent.parent / "yayinlananlar.md").read_text(encoding="utf-8")


def test_bir_platform_hatasi_digerini_etkilemez_ve_token_gizlenir(depo):
    sonuc = publish.yayinla(depo, ORTAM, "https://raw.test", li=li_basarili, ig=ig_hatali, bugun=BUGUN)
    assert sonuc["durum"] == "kismi"
    assert sonuc["linkedin"] == "urn:li:share:9"
    assert sonuc["hatalar"] == ["Instagram: bozuk token ***"]
    assert "Gemini" not in (depo.parent.parent / "yayinlananlar.md").read_text(encoding="utf-8")


def test_kismi_tekrar_sadece_eksigi_dener(depo):
    publish.yayinla(depo, ORTAM, "https://raw.test", li=li_basarili, ig=ig_hatali, bugun=BUGUN)

    def li_cagrilmamali(*a, **k):
        raise AssertionError("LinkedIn ikinci kez çağrıldı")

    sonuc = publish.yayinla(depo, ORTAM, "https://raw.test", li=li_cagrilmamali, ig=ig_basarili, bugun=BUGUN)
    assert sonuc["durum"] == "yayinlandi"


def test_yayinlanmis_taslak_atlanir(depo):
    publish.yayinla(depo, ORTAM, "https://raw.test", li=li_basarili, ig=ig_basarili, bugun=BUGUN)
    sonuc = publish.yayinla(depo, ORTAM, "https://raw.test", li=None, ig=None, bugun=BUGUN)
    assert sonuc["durum"] == "atlandi"


def test_uzun_instagram_metni_reddedilir(depo):
    (depo / "instagram.md").write_text("x" * 2201, encoding="utf-8")
    sonuc = publish.yayinla(depo, ORTAM, "https://raw.test", li=li_basarili, ig=ig_basarili, bugun=BUGUN)
    assert sonuc["durum"] == "kismi"
    assert "2201" in sonuc["hatalar"][0]


def test_token_uyarilari():
    ortam = dict(ORTAM, LINKEDIN_TOKEN_EXPIRES="2026-09-27")
    ortam.pop("IG_TOKEN_EXPIRES")
    uyarilar = publish.token_uyarilari(BUGUN, ortam)
    assert "LinkedIn anahtarının süresi 5 gün içinde doluyor (2026-09-27). Yenile." in uyarilar
    assert "Instagram: IG_TOKEN_EXPIRES tanımlı değil, anahtar süresi izlenemiyor" in uyarilar


def test_varsayilan_gorsel_adresi():
    assert publish.VARSAYILAN_GORSEL_TABAN == "https://raw.githubusercontent.com/denizozcivi/yapay-zeka-radari/main"
