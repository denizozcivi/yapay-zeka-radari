---
name: post-yazimi
description: Use when writing or revising an AI News post for LinkedIn or Instagram from a news story, or when a draft reads generic, translated, or AI-generated.
---

# Writing AI News posts

## Core
Deniz writes as a practitioner: IT manager and pentester. He reads an incident, works out **how it actually worked** and **what it causes**, and explains that mechanism to peers. Readers are security engineers, IT leads and developers; assume they know what a CI token, a CVE or an egress rule is. Go technical: name the component, file, function, flag, version, CVE and IOC whenever the source gives them.

Flow, labels and length are in `YAZIM-TARZI.md`. This skill covers what goes inside each part.

## Process
1. Read the sources, then close them. Write from your notes, never by paraphrasing the article sentence by sentence.
2. Answer for yourself: What happened? How did it work (the mechanism, the assumption that broke)? What does it mean for someone running similar systems?
3. Write plain, specific sentences: one idea each, active voice, concrete nouns.
4. Run the checklist below, then check length. Over the limit: cut repetition or commentary, never the technical facts.

## Parts
- **Hook (line 1):** at most 10 words, a concrete fact, ideally with a number. Never a question: question hooks get about a third less engagement.
- **Line 2:** why a reader running similar systems should care. One sentence.
- **What happened:** facts, names, versions, dates. At most one version list per sentence.
- **How it worked:** the mechanism at code or config level ("the script appends X to Y, so Z runs before W"). This paragraph is where Deniz's depth shows.
- **What it means:** the consequence for the reader's environment. Opinion is welcome ("I'd check…"). Experience lines stay general professional observations; never invent an incident, client or number.
- **Do this today:** one concrete action. A command, query or config check is ideal.
- **Closing question:** something readers can answer about their own setup.

## AI-tell checklist: rewrite when you see these
| Pattern | Why it hurts | Instead |
|---|---|---|
| "It's not X, it's Y" / "X isn't the problem. Y is." / "wasn't X. It was Y." | Most-flagged AI formula; about -4.9% reach in a 287k-post study | State Y and explain it |
| "Here's what/how/why…" | About -4.3% reach | Just say it |
| "The result?" / "The kicker?" / "The catch?" | Cliffhanger formula, about -4.8% reach | Plain sentence |
| "Stop X. Start Y." / "The key is…" | About -6.7% reach | Describe the practice |
| An em dash (—) in most sentences | Dense dashes plus bland copy read as AI | Periods and commas; one dash per post at most |
| Moreover, Furthermore, It's worth noting, In today's…, landscape, delve, crucial, robust, seamless, leverage, game-changer, wake-up call, stark reminder, let that sink in | Dead giveaways | Cut, or use the plain word |
| Rule-of-three lists, stacks of one-line paragraphs | Mechanical rhythm | 2-4 sentence paragraphs, varied length |
| Aphorisms ("A sandbox you share with the agent is a wish.") | Written to be quoted, explains nothing | Explain the mechanism |
| Emoji bullets, 🚨, 👇, "Thoughts?", "Agree?" | Engagement bait | A specific closing question |

## Technical accuracy
- Every name, version, path, command and IOC comes from a verified source. Defang domains and IPs (`skyleen[.]fr`).
- Keep the source's certainty: "no evidence of exploitation" stays that, never "not exploited".
- LinkedIn and Instagram have no code formatting. Write commands inline as plain text; code belongs on the card.

## 🇹🇷 Turkish summary (1-2 sentences)
Write it fresh in natural Turkish, never as a translation of the English text. Short sentences, verb last, no semicolons. Keep technical terms the way Turkish practitioners say them (token, commit, CI, npm). Suffixes on names and abbreviations take an apostrophe and follow pronunciation (npm'deki, PyPI'daki, CVE'yi). Month names are capitalized only with a day ("23 Eylül'de", but "ağustosta").

## Example
**Before (formula):** "This isn't a supply chain problem — it's a pipeline problem. The result? Tokens gone."

**After:** "The attacker pushed commits that changed a script the release workflow runs. The new line appends BASH_ENV=…/sckit-publish-bridge.sh to $GITHUB_ENV. Bash sources that file before every later step, so the attacker's script ran before the publish step and took the npm token."
