"""Bir taslak klasörünü LinkedIn + Instagram'a yayınlar, sonucu JSON olarak basar."""
import datetime as dt
import json
import os
import sys
from pathlib import Path

import instagram
import linkedin

UYARI_GUN = 7
IG_SINIR = 2200
GIZLI = ("LINKEDIN_TOKEN", "IG_TOKEN")
VARSAYILAN_GORSEL_TABAN = "https://raw.githubusercontent.com/denizozcivi/yapay-zeka-radari/main"


def token_uyarilari(bugun: dt.date, ortam) -> list[str]:
    uyarilar = []
    for ad, anahtar in (("LinkedIn", "LINKEDIN_TOKEN_EXPIRES"), ("Instagram", "IG_TOKEN_EXPIRES")):
        deger = ortam.get(anahtar)
        if not deger:
            uyarilar.append(f"{ad}: {anahtar} tanımlı değil, anahtar süresi izlenemiyor")
            continue
        kalan = (dt.date.fromisoformat(deger) - bugun).days
        if kalan <= UYARI_GUN:
            uyarilar.append(f"{ad} anahtarının süresi {kalan} gün içinde doluyor ({deger}). Yenile.")
    return uyarilar


def _temizle(mesaj: str, ortam) -> str:
    for anahtar in GIZLI:
        if ortam.get(anahtar):
            mesaj = mesaj.replace(ortam[anahtar], "***")
    return mesaj


def yayinla(klasor: Path, ortam, gorsel_taban_url: str, li=linkedin.yayinla, ig=instagram.yayinla, bugun=None) -> dict:
    meta_yolu = klasor / "meta.json"
    meta = json.loads(meta_yolu.read_text(encoding="utf-8"))
    if meta.get("durum") not in ("taslak", "kismi"):
        return {"durum": "atlandi", "neden": f"meta durumu '{meta.get('durum')}'",
                "linkedin": meta.get("linkedin_post"), "instagram": meta.get("instagram_post"),
                "hatalar": [], "uyarilar": []}

    hatalar, uyarilar = [], token_uyarilari(bugun or dt.date.today(), ortam)

    if not meta.get("linkedin_post"):
        try:
            sonuc = li((klasor / "linkedin.md").read_text(encoding="utf-8").strip(), (klasor / "kart.jpg").read_bytes(),
                       meta["alt_metin"], meta["kaynak_url"], ortam["LINKEDIN_TOKEN"], ortam["LINKEDIN_PERSON_URN"])
            meta["linkedin_post"] = sonuc["post"]
            if sonuc.get("yorum_hatasi"):
                uyarilar.append(_temizle("LinkedIn ilk yorum yazılamadı: " + sonuc["yorum_hatasi"], ortam))
        except Exception as e:
            hatalar.append(_temizle(f"LinkedIn: {e}", ortam))

    if not meta.get("instagram_post"):
        try:
            metin = (klasor / "instagram.md").read_text(encoding="utf-8").strip()
            if len(metin) > IG_SINIR:
                raise ValueError(f"metin {len(metin)} karakter, sınır {IG_SINIR}")
            url = f"{gorsel_taban_url.rstrip('/')}/taslaklar/{klasor.name}/kart.jpg"
            meta["instagram_post"] = ig(metin, url, ortam["IG_TOKEN"], ortam["IG_USER_ID"])
        except Exception as e:
            hatalar.append(_temizle(f"Instagram: {e}", ortam))

    meta["durum"] = "yayinlandi" if meta.get("linkedin_post") and meta.get("instagram_post") else "kismi"
    meta_yolu.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    if meta["durum"] == "yayinlandi":
        with open(klasor.parent.parent / "yayinlananlar.md", "a", encoding="utf-8") as f:
            f.write(f"- {meta['tarih']} · {meta['konu']}\n")

    return {"durum": meta["durum"], "linkedin": meta.get("linkedin_post"),
            "instagram": meta.get("instagram_post"), "hatalar": hatalar, "uyarilar": uyarilar}


if __name__ == "__main__":
    sonuc = yayinla(Path(sys.argv[1]), os.environ, os.environ.get("RADAR_IMAGE_BASE_URL", VARSAYILAN_GORSEL_TABAN))
    print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    sys.exit(0 if sonuc["durum"] in ("yayinlandi", "atlandi") else 1)
