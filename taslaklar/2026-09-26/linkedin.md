Carbonato hijacks Docker port 2375, then installs an AI agent.
A host answering on 2375 hands the operator a shell that writes its own commands.

ThreatDown published the research yesterday, traced from an unauthenticated Docker registry the operators left exposed. The botnet compromises Docker daemons reachable without authentication on port 2375, then scans nearby networks every five minutes for more. Language and timezone clues put the operators in Costa Rica.

The post-exploitation tool is not custom. The implant installs Hermes Agent, Nous Research's MIT-licensed open source framework, then replaces its persona file, SOUL.md, with instructions to take tasks from the operators' Telegram chat, maintain persistence and collect credentials, ranking AI API keys first. Hermes already ships a gateway that speaks Telegram, and terminal backends for local, Docker and SSH, so the operator's own contribution amounts to a config file.

Detection is the awkward part. The persona is Markdown under ~/.hermes, and the traffic is TLS to a Telegram API host many teams already allow outbound. It is the second Hermes case this quarter: in July Hunt.io documented the same framework run in YOLO mode against Thailand's Ministry of Finance. The question stops being whether a binary is malicious and becomes why an agent runtime sits on a build host.

Do this today: run ss -lntp | grep 2375 on every Docker host. Anything bound to a non-loopback address is a remote root shell.

Which of your CI runners could reach a Docker daemon over the network right now?

🛰️ AI News · Sep 26
🇹🇷 Carbonato, kimlik doğrulaması kapalı 2375 portundaki Docker daemon'larını ele geçiriyor. Açık kaynak Hermes Agent'ı kurup persona dosyasını değiştiriyor. Ajan komutları Telegram'dan alıyor, önce yapay zeka API anahtarlarını topluyor.
Source in the first comment.
#AINews #ContainerSecurity #DevSecOps #ThreatIntel
