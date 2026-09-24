import linkedin
from sahte import SahteOturum, Yanit

URN = "urn:li:person:abc"


def test_little_text_rezerve_karakterleri_kacislar():
    assert linkedin.little_text("a (b) [c] *d*") == r"a \(b\) \[c\] \*d\*"


def test_little_text_hashtagleri_donusturur():
    assert linkedin.little_text("#YapayZeka ve #SiberGüvenlik") == (
        r"{hashtag|\#|YapayZeka} ve {hashtag|\#|SiberGüvenlik}"
    )


def test_yayinla_akisi(monkeypatch):
    monkeypatch.setenv("LINKEDIN_ILK_YORUM", "1")
    oturum = SahteOturum([
        Yanit(veri={"value": {"uploadUrl": "https://yukle", "image": "urn:li:image:1"}}),
        Yanit(201),
        Yanit(201, basliklar={"x-restli-id": "urn:li:share:9"}),
        Yanit(201),
    ])
    sonuc = linkedin.yayinla("Merhaba #AI", b"jpeg", "alt", "https://kaynak", "tok", URN, oturum=oturum)

    assert sonuc == {"post": "urn:li:share:9", "yorum_hatasi": None}
    yontemler = [c[0] for c in oturum.cagrilar]
    assert yontemler == ["POST", "PUT", "POST", "POST"]
    post_govdesi = oturum.cagrilar[2][2]["json"]
    assert post_govdesi["author"] == URN
    assert post_govdesi["content"]["media"]["id"] == "urn:li:image:1"
    assert post_govdesi["commentary"] == r"Merhaba {hashtag|\#|AI}"
    assert oturum.cagrilar[3][1].endswith("/rest/socialActions/urn%3Ali%3Ashare%3A9/comments")
    assert oturum.cagrilar[3][2]["json"]["message"]["text"] == "Source: https://kaynak"


def test_yorum_hatasi_postu_bozmaz(monkeypatch):
    monkeypatch.setenv("LINKEDIN_ILK_YORUM", "1")
    oturum = SahteOturum([
        Yanit(veri={"value": {"uploadUrl": "https://yukle", "image": "urn:li:image:1"}}),
        Yanit(201),
        Yanit(201, basliklar={"x-restli-id": "urn:li:share:9"}),
        Yanit(500),
    ])
    sonuc = linkedin.yayinla("x", b"j", "a", "https://k", "tok", URN, oturum=oturum)
    assert sonuc["post"] == "urn:li:share:9"
    assert "500" in sonuc["yorum_hatasi"]


def test_ilk_yorum_varsayilan_kapali(monkeypatch):
    monkeypatch.delenv("LINKEDIN_ILK_YORUM", raising=False)
    oturum = SahteOturum([
        Yanit(veri={"value": {"uploadUrl": "https://yukle", "image": "urn:li:image:1"}}),
        Yanit(201),
        Yanit(201, basliklar={"x-restli-id": "urn:li:share:9"}),
    ])
    sonuc = linkedin.yayinla("x", b"j", "a", "https://k", "tok", URN, oturum=oturum)
    assert sonuc == {"post": "urn:li:share:9", "yorum_hatasi": None}
    assert len(oturum.cagrilar) == 3


def test_kim():
    oturum = SahteOturum([Yanit(veri={"sub": "abc"})])
    assert linkedin.kim("tok", oturum=oturum) == URN
