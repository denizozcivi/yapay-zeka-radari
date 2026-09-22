from pathlib import Path

import pytest

import render

KART = {
    "tarih": "22.09.2026",
    "etiket": "KAPSAM <DIŞI>",
    "baslik_html": 'Test <span class="hl">vurgu</span>',
    "alt_satir": 'Alt "satır"',
    "cizim_svg": '<svg width="630" height="630" viewBox="-280 -280 560 560"><circle r="100" fill="#3DDC97"/></svg>',
    "kaynak": "NBC News",
}


def test_tum_alanlar_dolar():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "{{" not in sonuc
    assert "22.09.2026" in sonuc
    assert '<span class="hl">vurgu</span>' in sonuc
    assert '<circle r="100"' in sonuc


def test_fontlar_gomulu_internet_gerekmez():
    sonuc = render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), KART)
    assert "fonts.googleapis.com" not in sonuc
    assert "data:font/woff2;base64," in sonuc


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
