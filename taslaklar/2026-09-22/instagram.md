🛰️ Yapay Zeka Radarı | 22 Eylül

Yabancı bir depoyu açıp Codex'e "bu kod ne yapıyor?" diye sormak yetiyordu.
O kodu yazan kişi, sizin makinenizde komut çalıştırıyordu.

📌 Ne oldu?
• Araştırmacılar OpenAI Codex'in sanal alanından (sandbox) iki ayrı yolla çıktı: Heapjack ve Overpatch.
• Heapjack, Codex Desktop'ın node_repl bileşenini hedefliyor. Güvenilir ve güvenilmeyen JavaScript aynı süreçte, aynı bellek yığınında çalışıyordu; güvenilmeyen taraf yığını okuyup güvenilir tarafı ayıran jetonu buluyor ve sandbox dışında komut çalıştırıyordu. Salt-okunur modda bile.
• Overpatch ise apply_patch aracını kullanıyor: yamada adı geçen yollardan yazma yetkisi türetildiği için çalışma alanının dışına yazılabiliyordu.
• Accomplish AI 12 Ağustos'ta bildirdi, OpenAI sekiz gün içinde kapattı. Düzeltmeler Codex CLI 0.149.0 ve Codex Desktop 26.818.21641 sürümlerinde.

🔍 Bulgu
Asıl mesele "OpenAI hata yaptı" değil. Sandbox, kontrol ettiği ajanla aynı süreçte yaşıyorsa o bir güvenlik sınırı değil, bir temennidir. Pentest'te yıllardır aynı cümleyi kuruyoruz: aynı bellekte duran sır, sır değildir. Yeni olan, bu sınırın geliştiricinin dizüstünde ve kurum ağına bağlı halde durması.

✅ Bugün yapılacak tek şey
Envanterden Codex CLI ve Desktop sürümlerini çıkarın; 0.149.0 ve 26.818.21641 altındaki kurulumları bugün güncelleyin.

Sizde ajan araçları geliştiricinin ana makinesinde mi çalışıyor, yoksa "ayrı makine" kuralınız var mı? 👇

🇬🇧 Researchers escaped OpenAI Codex's sandbox twice: Heapjack and Overpatch. Opening an untrusted repository was enough for unsandboxed command execution on the host. Fixed in Codex CLI 0.149.0 and Desktop 26.818.21641.

Kaynak: BleepingComputer

#YapayZekaRadarı #SiberGüvenlik #YapayZeka #DevSecOps #AIGüvenliği #Pentest #BilgiGüvenliği #Codex #OpenAI #ITYönetimi

Günlük yapay zeka radarı için takip et.
