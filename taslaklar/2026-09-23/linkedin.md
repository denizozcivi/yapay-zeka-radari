🛰️ Yapay Zeka Radarı | 23 Eylül

Zararlı yazılım "sıradaki hamlem ne?" diye artık operatörüne sormuyor.
Dört ticari yapay zeka modeline soruyor ve çoğunluğun dediğini yapıyor.

📌 Ne oldu?
• Cisco Talos, CLOSEDQUORUM adlı Windows implantını belgeledi: komuta-kontrol kararlarını ticari dil modellerine devreden, belgelenmiş ilk örnek.
• Go ile yazılan implant keşif verisini Gemini, DeepSeek, Qwen ve Mistral'a soruyor. Eşitlikte son sözü DeepSeek söylüyor; sonra Qwen, Mistral, Gemini.
• Seçebildiği eylemler: LSASS bellek dökümü, tarayıcı parolaları, kripto cüzdanları, süreç enjeksiyonu, kalıcılık. Çalınan veri Discord webhook'una gidiyor.
• Talos örneği sahada kullanılmış olarak görmedi; binary, aynı gün açık kaynak yayımlanan CAIRN aracıyla bulundu.

🔍 Bulgu
Asıl kırılma "zararlı yazılım akıllandı" değil: engelleyecek bir C2 sunucusu kalmadı. Tespit mantığımız yıllardır "tanımadık bir alan adına düzenli trafik" üzerineydi. Bu implantın konuştuğu adresler ise geliştiricilerinizin gün boyu konuştuğu adresler; çıkış kuralınızda açık, itibar listenizde temiz. Pentest'te en sevdiğim yol hep buydu: yasak olanı zorlamak yerine serbest olanın içinden geçmek.

✅ Bugün yapılacak tek şey
Çıkış (egress) kurallarınıza bakın: LLM API uç noktaları her makineye mi açık? Geliştirici olmayan uçlardan bu adreslere giden trafiği bugün loglayın.

LLM API'leri sıradan bir iş uygulaması mı, yoksa çıkışta kısıtlanması gereken bir kanal mı? 👇

🇬🇧 Cisco Talos documented CLOSEDQUORUM, a Windows implant that asks Gemini, DeepSeek, Qwen and Mistral what to do next and follows the majority vote. There is no attacker-run C2 to block: it talks to commercial LLM APIs most egress rules already allow. Not seen in the wild yet.

Kaynak ilk yorumda.

#YapayZekaRadarı #SiberGüvenlik #YapayZeka #ITYönetimi
