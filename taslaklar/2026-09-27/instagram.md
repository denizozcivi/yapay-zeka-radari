Three Agentforce flaws let a public form read your CRM.
Anyone on the internet could send the payload, and nobody had to click it.

Zenity Labs published the set this week as SalesBleed. All three sat in Salesforce Agentforce, reachable through Web-to-Lead, the public lead form that writes straight into the CRM. Zenity reported them on June 1, Salesforce fixed all three by August 19. Two gave zero-click exfiltration of lead and account data, the third turned the agent into a phishing sender.

The instructions went into a lead and stayed dormant until an employee asked their agent to work the newest one. The control that failed is Trusted URLs, the allowlist deciding which URLs and images Agentforce may render. Zenity found it did not recognize top-level domains, and that some character sequences tampered with URL parsing, so data smuggled into an HTML image tag left the tenant while Agentforce reported the content blocked by security policy. The Slack variant needed no rendering: a crafted link makes Slack fetch the target the moment the message appears.

The third flaw is the one I keep thinking about. The agent did not identify who asked it to send a Slack message, so a poisoned lead could post phishing to internal channels under the agent's identity.

Do this today: list every Agentforce agent that can read Lead records, then check which of those also has a Slack send action. An agent with both is a path from a public form into your Slack.

Which of your AI agents can read a record an anonymous stranger created?

🛰️ AI News · Sep 27
🇹🇷 Zenity Labs, Salesforce Agentforce'ta SalesBleed adlı üç açık buldu. Saldırgan herkese açık Web-to-Lead formuna gizli talimat bırakıyor, çalışan ajandan yeni kaydı incelemesini isteyince CRM verisi dışarı sızıyor.
Source: SecurityWeek
#AINews #AIsecurity #PromptInjection #Salesforce #Agentforce #AgenticAI #CRMSecurity #DevSecOps #InfoSec #BlueTeam
Follow for daily AI security news.
