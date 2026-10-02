16,000 requests in two days tried to decrypt GPT's reasoning.

If your app replays a model's encrypted reasoning block each turn, you are moving recoverable plaintext.

OpenAI published the case on October 1. Attempts started July 1, 2026, spiked on July 24 and 25 to 16,000 requests from over 4,000 users, and the same prompt pattern showed up across more than 15,000 accounts. OpenAI disrupted it on July 28 and tied the core cluster to individuals associated with Moonshot AI in Beijing. No encryption was broken.

Reasoning models do not keep the chain of thought on the server. They return it to the client as an encrypted block that the client sends back with each request. An August 2026 study from MATS Research, the ELLIS Institute Tübingen and Synk found those blocks are "interchangeable across different sessions, users, and models within a provider's ecosystem" on Claude, Gemini and GPT. Paste a strong model's block into a weaker, less safeguarded sibling, ask it to repeat the thinking word for word, and it prints the trace. The capable model is never jailbroken. OpenAI says it closed the pathway that let anyone holding another user's block replay it.

I'd put that block in the same bucket as a session token. Request logs, agent traces in a repo, a gateway cache: each is plaintext reasoning for whoever holds it.

Do this today: grep your LLM gateway logs and stored agent traces for persisted reasoning fields, then drop them from the schema.

Which of your systems still keeps a model's encrypted reasoning after the turn ends?

🛰️ AI News · Oct 2
🇹🇷 OpenAI 1 Ekim'de açıkladı: temmuzda 15 binden fazla hesap, başka kullanıcıların şifreli akıl yürütme bloklarını zayıf bir modele verip düz metin olarak geri okutmayı denedi. O blokları logda tutuyorsanız elinizde şifreli veri değil açık metin var.
Source: The Hacker News
#AINews #LLMSecurity #DevSecOps #AISecurity #PromptInjection #ChainOfThought #CloudSecurity #Infosec #OpenAI #SecOps
Follow for daily AI security news.
