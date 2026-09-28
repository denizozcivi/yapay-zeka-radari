---
name: kart-gorseli
description: Use when writing kart.json for an AI News post, choosing what the card image should show, or when a rendered kart.jpg overflows, clips text, fails with "kart taşıyor" or "bilinmeyen ikon", or looks generic and decorative.
---

# Card visual (AI News)

## Core
The card is a one-page security briefing on dark navy: what it is, four key facts, how it works in four steps, the flow from attacker (or actor) to impact, the real evidence (payload, diff, request, log, command) and how to defend. Every panel carries facts from the source, nothing decorative. All card text is English.

Template: `sablon/kart.html`. Worked example (a non-CVE story): `sablon/ornek-kart.json`.

## kart.json fields
| Field | Rule |
|---|---|
| `tarih` | "Sep 24, 2026" |
| `etiket` | Vendor/product · area, max 40 chars ("MemTensor · npm + PyPI") |
| `ikon` | Header icon, a name from the icon list below. Optional, default `bocek` |
| `baslik_html` | Name + key fact, max ~45 chars (2 lines). Key part in `<span class="hl">…</span>` (red): `Comment2Shell <span class="hl">— CVE-2026-12345</span>` |
| `alt_satir` | One sentence, max ~65 chars: the consequence |
| `gorsel_html` | The skeleton below, filled in |
| `kaynak` | Source name |

## gorsel_html skeleton
Copy it and replace every `…`. Keep the order and every block. Only `p.aciklama` and `.uyari-kutu` may be dropped.

```html
<div class="sira uc">
  <div class="panel">
    <h3><i class="ik i-uyari k"></i>What is it?</h3>
    <p>… <span class="k">…</span> …</p>
  </div>
  <div class="panel">
    <ul class="kunye">
      <li><i class="ik i-hedef m"></i><b>CVE ID</b>CVE-2026-…</li>
      <li><i class="ik i-simsek k"></i><b>Impact</b>…</li>
      <li><i class="ik i-paket m"></i><b>Affected</b>…</li>
      <li><i class="ik i-zil k"></i><b>CVSS</b>…</li>
    </ul>
  </div>
  <div class="panel">
    <h3><i class="ik i-disli m"></i>How it works</h3>
    <ol class="adimlar"><li>…</li><li>…</li><li>…</li><li>…</li></ol>
  </div>
</div>
<div class="panel akis">
  <div class="dugum"><i class="ik i-saldirgan k"></i><b>Attacker</b><span>…</span></div>
  <div class="ok">…</div>
  <div class="dugum"><i class="ik i-web m"></i><b>…</b><span>…</span></div>
  <div class="ok">…</div>
  <div class="dugum mekanizma"><b>…</b><code>…</code><span>…</span></div>
  <div class="ok">…</div>
  <div class="dugum"><i class="ik i-sunucu m"></i><b>…</b><span>…</span></div>
</div>
<div class="sira iki">
  <div class="panel">
    <h3><i class="ik i-kod m"></i>… <em>(example)</em></h3>
    <p class="aciklama">…</p>
    <pre>…</pre>
  </div>
  <div class="panel">
    <h3><i class="ik i-terminal m"></i>Check it today</h3>
    <pre><span class="m">$</span> …</pre>
    <div class="uyari-kutu"><i class="ik i-uyari"></i>…</div>
  </div>
</div>
<div class="panel">
  <h3 class="g"><i class="ik i-kalkan"></i>How to defend</h3>
  <ul class="kontrol"><li>…</li><li>…</li><li>…</li><li>…</li></ul>
</div>
<div class="slogan">… <b>…</b></div>
```

## Limits (1080×1350, nothing may overflow)
| Block | Limit |
|---|---|
| What is it? | 40-50 words, exactly one `<span class="k">` phrase: the worst consequence |
| Facts (`kunye`) | exactly 4 rows; label ≤ 16 chars, value ≤ 30 chars |
| How it works | exactly 4 steps, ≤ 45 chars each, in order |
| Flow (`akis`) | 4 nodes (3 or 5 allowed), exactly one `dugum mekanizma`; name ≤ 16, sub-line ≤ 20, arrow label ≤ 16, `<code>` ≤ 22 chars |
| Code panels | ≤ 5 lines of ≤ 42 chars in `<pre>`; ≤ 4 lines when the warning box is used |
| How to defend | 4 items of ≤ 42 chars (two columns) |
| Slogan | ≤ 55 chars, one line, the punchline in `<b>` |

## Facts rows by story type
| Story | The four rows |
|---|---|
| CVE, vulnerability | CVE ID · Impact · Affected component/versions · CVSS or Fixed in |
| Malware, campaign | Actor · Tools or agents · Targets · Cost or scale |
| Supply chain | Package · Bad versions · Payload · Registry or CI |
| AI product or policy | Vendor · What changed · Who is affected · Date or availability |

## Evidence panels
Left: the mechanism itself (payload, diff, pseudo-code, advisory JSON, injected prompt). Right: the request or log that shows it happening, or the reader's check (`Check it today`, terminal commands). Newlines inside `<pre>` are real line breaks. Colours: `.y` muted (comments, timestamps), `.k` red (malicious, denied), `.g` green (fixed, allowed), `.m` blue (prompt `$`, keys).

## Icons
`<i class="ik i-NAME COLOR"></i>`, COLOR: `k` red (attacker, danger, impact), `m` blue (systems, neutral facts), `g` green. An unknown name stops render.py with the valid list.

saldirgan (hooded attacker) · kullanici · ajan (AI agent) · model (LLM) · web (web app, browser) · sunucu · terminal · bulut · veritabani · paket (npm, PyPI, image) · git (repo, CI) · eposta · yorum (comment, chat) · belge · kod · kure (network, HTTP) · anahtar (token, secret) · kilit · bocek (vulnerability) · uyari · hedef (target, CVE ID) · simsek (impact, exploit) · zil (severity) · kalkan (defense) · disli (mechanism) · para (cost) · saat (time)

## Honesty
- Anything not copied verbatim from the source says so in its panel title: `<em>(example)</em>`, `<em>(pseudo-code)</em>`, `<em>(representative)</em>`.
- CVE IDs, versions, CVSS, paths and commands must be verified in the source. No published CVSS: use `Fixed in` or another verified fact. `(estimated)` only when the source itself gives the estimate.
- Payloads are trimmed to show the mechanism. Hosts use documentation ranges (`203.0.113.x`, `198.51.100.x`, `attacker.example`). Real IOCs are defanged (`skyleen[.]fr`).

## meta.json alt text
`alt_metin`: one sentence naming what the card shows, e.g. "Infographic on CVE-2026-12345: four facts, a flow from a crafted comment to code execution on the server, an example payload and HTTP request, and four defenses."

## After rendering
render.py fails with `kart taşıyor: …` when panels push into the footer, a code line is clipped or the title passes 2 lines; kart.jpg is still written. Shorten the named block and render again. Then look at kart.jpg: every panel filled, arrows run from actor to impact, the red phrase is the key fact, no single word alone on a title line.

## Don't
Emoji (the cloud renderer has no emoji font), `<img>`, inline `style=`, extra or reordered panels, Turkish text on the card.
