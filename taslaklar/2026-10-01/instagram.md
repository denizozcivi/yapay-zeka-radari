AI agent chained two Zammad zero-days to root in seconds.
If you self-host a ticket system on the internet, this is your stack.

DIVD, the Dutch disclosure institute, said on Sep 29 that its network had been breached. On Sep 30 it published the two zero-days found while investigating, both rated 9.4. CVE-2026-102489 is a session hijack in Zammad 6.3.0 through 6.5.4 that ends in code execution as the zammad user. CVE-2026-102490 takes that local account to root and affects all versions, including the latest alpha. Zammad lists over 55,000 users.

Neither link is exotic. Hijack a session, run code as the service account, escalate. In 7.0.0 through 7.1.3 the hijack is present but not exploitable, so moving to 7 removes the first link and leaves the second standing: the privilege escalation has no fix in any version. The post-exploitation ran as an autonomous agent picking its next action after each result. DIVD called it loud and very, very messy: it sprayed passwords into its own adversary-in-the-middle attack, and it wrote out its reasoning as it worked, so DIVD rebuilt the intrusion from the attacker's own tool.

Root in seconds breaks any detection window sized for a human operator. Segmentation held here, response time did not. The clumsy, talkative agent is the part I would not plan around.

Do this today: inventory every Zammad instance you run, match it against 6.3.0-6.5.4, then upgrade to 7 or take it off the internet.

After the ticket system, which internal app does an attacker reach next?

🛰️ AI News · Oct 1
🇹🇷 DIVD kendi ağındaki ihlali incelerken Zammad'da iki sıfırıncı gün buldu: 6.3.0-6.5.4'te oturum kaçırmayla kod çalıştırma, her sürümde de zammad kullanıcısından root'a yükselme. Sömürü sonrası adımları otonom bir yapay zeka ajanı yürüttü, saniyeler içinde root oldu.
Source: BleepingComputer
#AINews #AISecurity #ZeroDay #Zammad #IncidentResponse #BlueTeam #Pentest #ThreatIntel #DevSecOps #CVE
Follow for daily AI security news.
