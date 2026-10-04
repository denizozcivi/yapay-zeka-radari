A hidden Gemini Desktop setting drops the ask-first rule.
If Macs in your fleet run Google's desktop app, you need a policy answer now.

TestingCatalog found the setting on October 2, BleepingComputer reported it on October 3. It is called Additional sandbox options, it is not live, and Google has not confirmed it. Enabling it lets Gemini read, create, modify or even delete files anywhere on the Mac, outside the folders you explicitly connected, and act through apps such as Mail, Safari or Messages. One line carries the rest: "Gemini may be permitted to take actions without asking for your permission first."

Today the app works off an allowlist, the folders you connect, asking per action. The setting swaps that for standing consent, and what it still stops for is short: money transfers, new accounts, legal terms, edits to sensitive information about you. Reading every file under /Users is not on that list. Neither is sending mail. The remaining gate is macOS itself: Full Disk Access and Automation are granted per app and kept once given, so one approval covers reading a document and driving Mail in the same step.

Google has not said which model powers it or when it ships. I would stop filing these apps under chat clients. A desktop agent with standing file rights is an endpoint agent, and what decides its next move is the text it just read.

Do this today: list which apps hold Full Disk Access and Automation on your managed Macs, then decide whether Gemini Desktop belongs in that build.

Which app on your Macs holds Full Disk Access nobody reviewed?

🛰️ AI News · Oct 4
🇹🇷 Gemini'nin Mac uygulamasında gizli bir ayar bulundu: açıkken uygulama, bağlamadığınız klasörlerdeki dosyaları da silebiliyor, Mail ve Safari üzerinden işlem yapabiliyor. Üstelik her adımda izin istemiyor.
Source: BleepingComputer
#AINews #AISecurity #macOS #EndpointSecurity #AIAgents #Gemini #InfoSec #CyberSecurity #ITSecurity #DataProtection
Follow for daily AI security news.
