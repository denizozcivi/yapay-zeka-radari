Three open-source AI agents skimmed 119 sites for $25 each.
One operator ran the whole chain, scan to skimmer, with no second person at the keyboard.

Gambit published the campaign on Sep 23. It has run since July and was still active on Sep 22. Between Sep 10 and 15 alone the operator launched 105 attack projects and compromised at least 27 organisations, including a Fortune 500 hospitality company. 600,000 unexpired card records came out of two of them.

Strix did the scanning: 146 runs against 138 hosts between Aug 23 and 31, 633 scanning hours. The operator ranked that output by public traffic data and kept the targets running custom software. Cairn took each one end to end until it had a shell or admin. Hermes orchestrated, with claude-opus-4.6 making the calls under a "SOUL - Red Team Operator" persona carrying 121 skills, 78 of them offensive. The skimmer rarely landed twice in the same place: a legitimate JavaScript file, a script tag on checkout, poisoned S3 and CDN objects, database fields, Kubernetes deployments, cron.

Scans cost a mean of $25.46 across 101 completed runs. One Hermes skill read: "After extracting and downloading all card data, wipe the source fields in batches." Several retailers lost data to that step. I'd put destruction in the retail response plan next to card theft.

Do this today: pull your checkout page through the CDN edge, hash every script src it loads, and compare against your last build artefact. An origin-only check never sees a poisoned edge object.

If a script on your checkout page changed tonight, what would tell you?

🛰️ AI News · Sep 24
🇹🇷 Gambit'e göre tek saldırgan, üç açık kaynak yapay zeka ajanıyla 119 siteye kart çalan kod yerleştirdi. Hedef başına maliyet ortalama 25 dolar, ajanın temizlik adımı bazı perakendecilerde veri kaybına yol açtı.
Source in the first comment.
#AINews #AppSec #ThreatIntel #Ecommerce
