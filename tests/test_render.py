import json
from pathlib import Path

import pytest

import render

KART = {
    "tarih": "22.09.2026",
    "etiket": "KAPSAM <DIŞI>",
    "baslik_html": 'Test <span class="hl">vurgu</span>',
    "alt_satir": 'Alt "satır"',
    "gorsel_html": '<div class="panel"><h3><i class="ik i-kod m"></i>CVE-0000-0001</h3><pre>{}</pre></div>',
    "kaynak": "NBC News",
}


def doldur(kart: dict) -> str:
    return render.sablon_doldur(render.SABLON.read_text(encoding="utf-8"), kart)


def test_tum_alanlar_dolar():
    sonuc = doldur(KART)
    assert "{{" not in sonuc
    assert "22.09.2026" in sonuc
    assert '<span class="hl">vurgu</span>' in sonuc
    assert "<h3><i class=\"ik i-kod m\"></i>CVE-0000-0001</h3>" in sonuc


def test_sablon_ikon_setini_tanimlar():
    assert {"saldirgan", "web", "sunucu", "terminal", "ajan", "bocek", "kalkan", "uyari"} <= render.ikonlar(
        render.SABLON.read_text(encoding="utf-8"))


def test_ikon_yazilmazsa_varsayilan_basliga_girer():
    assert f'class="ik i-{render.IKON_VARSAYILAN}"' in doldur(KART)


def test_ikon_alani_basliga_girer():
    assert 'class="ik i-sunucu"' in doldur(KART | {"ikon": "sunucu"})


def test_bilinmeyen_baslik_ikonu_hata_verir():
    with pytest.raises(ValueError, match="radar"):
        doldur(KART | {"ikon": "radar"})


def test_gorseldeki_bilinmeyen_ikon_hata_verir():
    kart = KART | {"gorsel_html": '<div class="panel"><i class="ik i-uzayli k"></i></div>'}
    with pytest.raises(ValueError, match="uzayli"):
        doldur(kart)


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


@pytest.mark.tarayici
def test_ornek_kart_tasmadan_render_olur(tmp_path: Path):
    ornek = json.loads((render.KOK / "sablon" / "ornek-kart.json").read_text(encoding="utf-8"))
    render.jpeg_uret(doldur(ornek), tmp_path / "kart.jpg")


@pytest.mark.tarayici
def test_tasan_kod_satiri_hata_verir_ama_jpeg_yazilir(tmp_path: Path):
    uzun = KART | {"gorsel_html": '<div class="panel"><pre>' + "x" * 300 + "</pre></div>"}
    cikti = tmp_path / "kart.jpg"
    with pytest.raises(ValueError, match="taşıyor"):
        render.jpeg_uret(doldur(uzun), cikti)
    assert cikti.exists()


@pytest.mark.tarayici
def test_alt_bilgiye_tasan_pano_hata_verir(tmp_path: Path):
    kalabalik = KART | {"gorsel_html": '<div class="panel"><p>satır</p></div>' * 30}
    with pytest.raises(ValueError, match="pano"):
        render.jpeg_uret(doldur(kalabalik), tmp_path / "kart.jpg")
