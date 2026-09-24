# Yazım Tarzı: "AI News" (v3)

Günlük seri. Her gün **1 haber**, özet listesi değil. Farkımız: haberi bir **IT Manager + pentester gözüyle**, teknik derinlikle yorumlamak.

## Kimlik
- Seri adı: 🛰️ AI News
- Dil: **İngilizce ana metin** + en altta 1-2 cümlelik 🇹🇷 Türkçe özet.
- Okur: güvenlik mühendisleri, IT yöneticileri, geliştiriciler. CI token'ı, CVE, egress kuralı gibi kavramları bilirler; açıklamaya gerek yok.
- Ses: Sahadan konuşan, net, abartısız, teknik. Korkutma da yok, coşku da yok.
- Bakış: Olayın nasıl çalıştığını (mekanizma) ve neyi doğurduğunu anlatır. Kaynak ne kadar ayrıntı veriyorsa o kadar teknik: bileşen, dosya, fonksiyon, bayrak, sürüm, CVE, IOC.
- Kişi: 1. tekil ("I'd check…"). Deneyim cümleleri genel meslek gözlemi olur; olay, müşteri ya da sayı uydurulmaz.
- **Yazmadan önce `.claude/skills/post-yazimi/SKILL.md` dosyasını oku, metni ona göre yaz, sonra oradaki kontrol listesinden geçir.**

## Şablon (her post aynı akış, bölüm başlığı yok)
Akışta sadece ilk ~200 karakter görünür ve okur "…more"a ilk satıra bakarak karar verir. Bu yüzden ilk satır haberin kendisidir; seri adı ve tarih en sona gider.

1. **Hook (1. satır):** En fazla 10 kelime. Somut bir olgu, mümkünse bir sayı. Soru değil, seri adı ya da tarih değil.
2. **2. satır:** Bu olayın benzer sistem işleten okuru neden ilgilendirdiği, tek cümle.
3. **Gövde, 3 kısa paragraf, başlıksız:**
   - What happened: doğrulanmış olgular, isimler, sürümler.
   - How it worked: kod/konfigürasyon seviyesinde mekanizma.
   - What it means: okurun ortamına etkisi, senin yorumun.
4. **`Do this today:`** Düz metin etiketiyle başlayan tek somut adım. Komut, sorgu ya da konfigürasyon kontrolü olabilir. Serinin imzası bu.
5. **Kapanış sorusu:** Okurun kendi ortamına dair cevaplayabileceği tek soru.
6. `🛰️ AI News · <Mon> <day>`
7. `🇹🇷 <1-2 cümle Türkçe özet>`
8. LinkedIn: `Source in the first comment.` (Linki posta koyma, erişimi düşürür. İlk yoruma sen ekle; bot `LINKEDIN_ILK_YORUM=1` olmadan yorum atmaz.) Instagram: `Source: <kaynak adı>`.
9. **Hashtag:** LinkedIn'de 3-5, Instagram'da 8-12 adet, İngilizce. Her zaman `#AINews` ilk sırada.

Örnek akış:
```
4 MemTensor releases shipped a credential-stealing Go binary.
They were published by the project's own GitHub Actions release job, a setup most teams also run.

<What happened>

<How it worked>

<What it means>

Do this today: <one action>

<Closing question>

🛰️ AI News · Sep 24
🇹🇷 <Türkçe özet>
Source in the first comment.
#AINews #SupplyChainSecurity #DevSecOps #GitHubActions
```

## Haber seçme kuralı (öncelik sırası)
1. Yapay zeka + güvenlik (senin en güçlü alanın)
2. Şirketlerin/IT ekiplerinin yarın etkileneceği gelişmeler (ajanlar, araçlar, regülasyon)
3. Büyük model/şirket haberleri, ama sadece "IT için ne anlama geliyor" açısıyla
4. Türkiye'den yapay zeka haberi varsa haftada 1 kez

## Görsel (her posta 1 kart)
- Kart bir kod tabanı ya da terminal sayfası gibi görünür: haberin konusu olan gerçek diff, kod, log, advisory kaydı ya da kontrol komutu. Üstünde tek bir kırmızı kutu ve Deniz'in el yazısı notu.
- **kart.json'u `.claude/skills/kart-gorseli/SKILL.md`'ye göre yaz.** Şablon: `sablon/kart.html`, örnek: `sablon/ornek-kart.json`.
- Boyut: 1080×1350 (4:5 dikey). Açık (kağıt) zemin, koyu kod pencereleri, vurgu rengi kırmızı.
- Kart tamamen İngilizce. Başlık en fazla 2 satır. Altta her zaman isim + unvan + `#AINews`.

## Kurallar
- Uzunluk (LinkedIn, Türkçe özet dahil): 1.300-1.900 karakter.
- Sayı, tarih, sürüm ve komut sadece doğrulanmış kaynakta yazıyorsa.
- Emoji sadece seri satırında (🛰️) ve Türkçe özette (🇹🇷).
- Yayın: Her gün 12:30 (LinkedIn + Instagram, onaylı). Yayından sonraki ilk 1 saat gelen yorumlara cevap ver (algoritma bunu ödüllendiriyor).
