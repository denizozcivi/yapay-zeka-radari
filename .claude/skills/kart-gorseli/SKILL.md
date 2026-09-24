---
name: kart-gorseli
description: Use when writing kart.json for an AI News post, choosing what the card image should show, or when a rendered kart.jpg looks generic, decorative, or AI-generated (radar, neon, abstract arrows).
---

# Card visual (AI News)

## Core
The card looks like a page from a codebase or a terminal session: the actual diff, config, code, log, advisory record or command the story is about. On top of it sits one hand-drawn red box and one handwritten note from Deniz saying what it means. Evidence, not decoration. All card text is English.

Template: `sablon/kart.html`. Example: `sablon/ornek-kart.json`.

## kart.json fields
| Field | Rule |
|---|---|
| `tarih` | "Sep 24, 2026" |
| `etiket` | Vendor/product · area, max 40 chars, shown in mono ("MemTensor · npm + PyPI") |
| `baslik_html` | Like the hook: concrete, max ~50 chars (2 lines). Key 2-4 words in `<span class="hl">…</span>` |
| `alt_satir` | One sentence, max ~65 chars: the consequence |
| `gorsel_html` | One or two `.pencere` windows plus one `.not` |
| `kaynak` | Source name |

## What to show: the artifact closest to the mechanism
| Story | Artifact | Window title |
|---|---|---|
| Malicious commit, patch, config change | diff | the file path |
| Vulnerability, CVE | advisory as JSON or YAML | `CVE-2026-85889.json` |
| Attack logic, malware behaviour | real code (trimmed) or pseudo-code | file or module name |
| Detection, incident trail, timeline | log lines with timestamps or dates | `access.log`, `incident.log` |
| What the reader should run | terminal commands | `~/check` |

A second window is allowed only when it is the reader's check (terminal).

## Components
```html
<!-- plain window: code, terminal, log, json. Newlines inside <pre> are real line breaks. -->
<div class="pencere">
  <div class="cubugu"><b>~/check</b><span>dev hosts + CI runners</span></div>
  <pre><span class="y"># bad: 2.0.34</span>
<span class="m">$</span> pip show MemoryOS</pre>
</div>

<!-- diff window: one <div> per line inside .satirlar -->
<div class="pencere kucuk">
  <div class="cubugu"><b>.github/scripts/validate-release-confirmation.mjs</b><span>malicious commit</span></div>
  <div class="satirlar">
    <div class="hunk">@@ added by the attacker, via SafeDep (reformatted) @@</div>
    <div class="arti">+ appendFileSync(env.GITHUB_ENV,</div>
    <div class="eksi">- removed line</div>
    <div>  context line</div>
  </div>
</div>
```
Colour classes inside a window: `.y` muted (comments, timestamps, prompts' output), `.k` red (danger, denied, malicious), `.g` green (allowed, fixed), `.m` blue (prompt `$`, keys, strings).

Size: default 24px fits ~60 chars per line; `pencere kucuk` 20px fits ~72; `pencere buyuk` 28px fits ~50 and is for a single window with 5 lines or fewer. Window title max ~50 chars.

## Mark and note
- **Exactly one `.isaret`:** the line the reader must look at. In `<pre>` wrap it: `<span class="isaret">…</span>`. In `.satirlar` add the class to the line's div.
- **Exactly one `.not`:** `<div class="not">…</div>` after the windows, arrow pointing up. If the marked line is in the first window or the upper half, write `<div class="not ust">…</div>` **before** the first window instead.
- Note text: English, lowercase, what the marked line means, never a restatement. Max ~35 chars per line, 2 lines (`<br>`).

## Honesty
- Anything not copied verbatim from the source says so in the window bar's right label: `representative`, `pseudo-code`, `via SafeDep (reformatted)`.
- Representative data uses documentation ranges: `203.0.113.x`, `198.51.100.x`, `example.com`. Real IOCs are defanged (`skyleen[.]fr`).
- Versions, CVEs, paths and commands must be verified in the source.

## After rendering: look at kart.jpg
Title within 2 lines; no code line clipped at the window edge; windows clear of the footer; the note and arrow cover no text; the red box sits on the intended line. Fix kart.json and render again.

## Don't
Radar or target circles, glow, abstract node-and-arrow diagrams, stock icons, emoji (the cloud renderer has no emoji font), inline `style=` positioning, Turkish text on the card.
