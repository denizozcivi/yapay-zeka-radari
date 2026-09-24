"""kart.json + sablon/kart.html -> kart.html + kart.jpg (1080x1350 JPEG)."""
import html
import json
import os
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
SABLON = KOK / "sablon" / "kart.html"
FONTLAR = KOK / "sablon" / "fontlar.css"  # base64 gömülü, bulutta Google Fonts erişimi yok
HAZIR_CHROMIUM = Path("/opt/pw-browsers/chromium")  # bulut ortamında önceden kurulu
GENISLIK, YUKSEKLIK = 1080, 1350
ALANLAR = ("tarih", "etiket", "baslik_html", "alt_satir", "gorsel_html", "kaynak")
HAM_ALANLAR = {"baslik_html", "gorsel_html"}  # Claude'un yazdığı HTML, kaçışsız girer


def sablon_doldur(sablon: str, kart: dict) -> str:
    eksik = [alan for alan in ALANLAR if alan not in kart]
    if eksik:
        raise ValueError(f"kart.json eksik alan: {', '.join(eksik)}")
    for alan in ALANLAR:
        deger = str(kart[alan])
        if alan not in HAM_ALANLAR:
            deger = html.escape(deger)
        sablon = sablon.replace("{{" + alan.upper() + "}}", deger)
    sablon = sablon.replace("{{FONTLAR}}", FONTLAR.read_text(encoding="utf-8"))
    if "{{" in sablon:
        raise ValueError("şablonda doldurulmamış alan kaldı")
    return sablon


def chromium_yolu() -> str | None:
    if os.environ.get("CHROMIUM_PATH"):
        return os.environ["CHROMIUM_PATH"]
    return str(HAZIR_CHROMIUM) if HAZIR_CHROMIUM.exists() else None


def jpeg_uret(html_metni: str, cikti: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        tarayici = p.chromium.launch(executable_path=chromium_yolu())
        sayfa = tarayici.new_page(viewport={"width": GENISLIK, "height": YUKSEKLIK})
        sayfa.set_content(html_metni, wait_until="networkidle")
        sayfa.evaluate("document.fonts.ready")
        sayfa.screenshot(path=str(cikti), type="jpeg", quality=92)
        tarayici.close()


def main(klasor: Path) -> Path:
    kart = json.loads((klasor / "kart.json").read_text(encoding="utf-8"))
    dolu = sablon_doldur(SABLON.read_text(encoding="utf-8"), kart)
    (klasor / "kart.html").write_text(dolu, encoding="utf-8")
    jpeg_uret(dolu, klasor / "kart.jpg")
    return klasor / "kart.jpg"


if __name__ == "__main__":
    print(main(Path(sys.argv[1])))
