"""Instagram API (Instagram Login): görsel post yayınla, token yenile."""
import datetime as dt
import os
import sys
import time

import requests

API = "https://graph.instagram.com/" + os.environ.get("IG_API_VERSION", "v26.0")


def konteyner_olustur(oturum, token: str, kullanici_id: str, gorsel_url: str, metin: str) -> str:
    r = oturum.post(
        f"{API}/{kullanici_id}/media",
        data={"image_url": gorsel_url, "caption": metin, "access_token": token},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()["id"]


def hazir_bekle(oturum, token: str, konteyner_id: str, uyu=time.sleep, deneme: int = 10, bekleme: float = 3.0) -> None:
    for _ in range(deneme):
        r = oturum.get(f"{API}/{konteyner_id}", params={"fields": "status_code", "access_token": token}, timeout=30)
        r.raise_for_status()
        durum = r.json().get("status_code")
        if durum == "FINISHED":
            return
        if durum in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Instagram konteyner durumu: {durum}")
        uyu(bekleme)
    raise TimeoutError("Instagram konteyneri zamanında hazır olmadı")


def yayinla(metin: str, gorsel_url: str, token: str, kullanici_id: str, oturum=None, uyu=time.sleep) -> str:
    oturum = oturum or requests.Session()
    konteyner = konteyner_olustur(oturum, token, kullanici_id, gorsel_url, metin)
    hazir_bekle(oturum, token, konteyner, uyu=uyu)
    r = oturum.post(
        f"{API}/{kullanici_id}/media_publish",
        data={"creation_id": konteyner, "access_token": token},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()["id"]


def token_yenile(token: str, oturum=None) -> dict:
    r = (oturum or requests).get(
        "https://graph.instagram.com/refresh_access_token",
        params={"grant_type": "ig_refresh_token", "access_token": token},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def kim(token: str, oturum=None) -> dict:
    r = (oturum or requests).get(f"{API}/me", params={"fields": "user_id,username", "access_token": token}, timeout=30)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    komut = sys.argv[1:]
    if komut == ["kim"]:
        print(kim(os.environ["IG_TOKEN"]))
    elif komut == ["yenile"]:
        yeni = token_yenile(os.environ["IG_TOKEN"])
        bitis = dt.date.today() + dt.timedelta(seconds=yeni["expires_in"])
        print(f"IG_TOKEN={yeni['access_token']}\nIG_TOKEN_EXPIRES={bitis.isoformat()}")
    else:
        sys.exit("kullanım: python scripts/instagram.py kim|yenile")
