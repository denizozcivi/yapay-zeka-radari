import json
from pathlib import Path

import pytest

import render

KART = {
    "tarih": "22.09.2026",
    "etiket": "KAPSAM <DIŞI>",
    "baslik_html": 'Test <span class="hl">vurgu</span>',
    "alt_satir": 'Alt "satır"',
    "gorsel_html": '<div class="pencere"><div class="cubugu"><b>CVE-0000-0001.json</b></div><pre>{}</pre></div><div class="not">look</div>',
    "kaynak": "NBC News",
}


def test_tum_alanlar_dolar():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "{{" not in sonuc
    assert "22.09.2026" in sonuc
    assert '<span class="hl">vurgu</span>' in sonuc
    assert "<b>CVE-0000-0001.json</b>" in sonuc


def test_kart_ingilizce_seri_adini_tasir():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "AI News" in sonuc
    assert "Source: NBC News" in sonuc
    assert "#AINews" in sonuc
    assert "Kaynak:" not in sonuc


def test_fontlar_gomulu_internet_gerekmez():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "fonts.googleapis.com" not in sonuc
    assert "data:font/woff2;base64," in sonuc


def test_el_yazisi_fontu_gomulu():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "font-family: 'Caveat'" in sonuc


def test_eski_cizim_svg_alani_yetmez():
    eski = {k: v for k, v in KART.items() if k != "gorsel_html"} | {"cizim_svg": "<svg></svg>"}
    with pytest.raises(ValueError, match="gorsel_html"):
        render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), eski)


def test_ornek_kart_sablonu_doldurur():
    ornek = json.loads((render.KOK / "sablon" / "ornek-kart.json").read_text(encoding="utf-8"))
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), ornek)
    assert "{{" not in sonuc


def test_hazir_chromium_varsa_kullanilir(tmp_path, monkeypatch):
    sahte = tmp_path / "chromium"
    sahte.write_text("")
    monkeypatch.delenv("CHROMIUM_PATH", raising=False)
    monkeypatch.setattr(render, "HAZIR_CHROMIUM", sahte)
    assert render.chromium_yolu() == str(sahte)
    monkeypatch.setattr(render, "HAZIR_CHROMIUM", tmp_path / "yok")
    assert render.chromium_yolu() is None
    monkeypatch.setenv("CHROMIUM_PATH", "/ozel/chrome")
    assert render.chromium_yolu() == "/ozel/chrome"


def test_duz_metin_alanlari_kacislanir():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "KAPSAM &lt;DIŞI&gt;" in sonuc
    assert "Alt &quot;satır&quot;" in sonuc


def test_eksik_alan_hata_verir():
    eksik = {k: v for k, v in KART.items() if k != "kaynak"}
    with pytest.raises(ValueError, match="kaynak"):
        render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), eksik)


@pytest.mark.tarayici
def test_jpeg_boyutu(tmp_path: Path):
    from PIL import Image

    cikti = tmp_path / "kart.jpg"
    render.jpeg_uret(render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART), cikti)
    with Image.open(cikti) as resim:
        assert resim.format == "JPEG"
        assert resim.size == (1080, 1350)
