"""LinkedIn Posts API: görsel yükle, post at, kaynağı ilk yoruma yaz."""
import os
import re
import sys
from urllib.parse import quote

import requests

API = "https://api.linkedin.com"
SURUM = os.environ.get("LINKEDIN_VERSION", "202608")
REZERVE = "\\|{}@[]()<>#*_~"  # LinkedIn "little text" rezerve karakterleri


def little_text(metin: str) -> str:
    kacisli = "".join("\\" + c if c in REZERVE else c for c in metin)
    return re.sub(r"\\#(\w+)", r"{hashtag|\\#|\1}", kacisli)


def _basliklar(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "LinkedIn-Version": SURUM,
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }


def gorsel_yukle(oturum, token: str, yazar_urn: str, jpeg: bytes) -> str:
    r = oturum.post(
        f"{API}/rest/images?action=initializeUpload",
        headers=_basliklar(token),
        json={"initializeUploadRequest": {"owner": yazar_urn}},
        timeout=30,
    )
    r.raise_for_status()
    deger = r.json()["value"]
    yukleme = oturum.put(deger["uploadUrl"], headers={"Authorization": f"Bearer {token}"}, data=jpeg, timeout=60)
    yukleme.raise_for_status()
    return deger["image"]


def post_at(oturum, token: str, yazar_urn: str, metin: str, gorsel_urn: str, alt_metin: str) -> str:
    govde = {
        "author": yazar_urn,
        "commentary": metin,
        "visibility": "PUBLIC",
        "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []},
        "content": {"media": {"id": gorsel_urn, "altText": alt_metin}},
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    r = oturum.post(f"{API}/rest/posts", headers=_basliklar(token), json=govde, timeout=30)
    r.raise_for_status()
    return r.headers["x-restli-id"]


def yorum_yaz(oturum, token: str, yazar_urn: str, post_urn: str, metin: str) -> None:
    r = oturum.post(
        f"{API}/rest/socialActions/{quote(post_urn, safe='')}/comments",
        headers=_basliklar(token),
        json={"actor": yazar_urn, "object": post_urn, "message": {"text": metin}},
        timeout=30,
    )
    r.raise_for_status()


def yayinla(metin: str, jpeg: bytes, alt_metin: str, kaynak_url: str, token: str, yazar_urn: str, oturum=None) -> dict:
    oturum = oturum or requests.Session()
    gorsel = gorsel_yukle(oturum, token, yazar_urn, jpeg)
    post = post_at(oturum, token, yazar_urn, little_text(metin), gorsel, alt_metin)
    try:
        yorum_yaz(oturum, token, yazar_urn, post, f"Kaynak: {kaynak_url}")
        yorum_hatasi = None
    except requests.RequestException as e:
        yorum_hatasi = str(e)
    return {"post": post, "yorum_hatasi": yorum_hatasi}


def kim(token: str, oturum=None) -> str:
    r = (oturum or requests).get(f"{API}/v2/userinfo", headers={"Authorization": f"Bearer {token}"}, timeout=30)
    r.raise_for_status()
    return f"urn:li:person:{r.json()['sub']}"


if __name__ == "__main__":
    if sys.argv[1:] == ["kim"]:
        print(kim(os.environ["LINKEDIN_TOKEN"]))
    else:
        sys.exit("kullanım: python scripts/linkedin.py kim")
