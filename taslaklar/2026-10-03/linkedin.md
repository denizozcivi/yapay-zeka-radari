A crafted Duo flow runs commands on your AI Gateway.
If you self-host GitLab's AI Gateway, CVE-2026-90970 is a 9.9 you patch today, not this sprint.

GitLab shipped AI Gateway 19.2.4, 19.3.2 and 19.4.1 on October 2. Affected: 18.1.6 up to 19.2.4, 19.3 up to 19.3.2, and 19.4.0. Nothing below 19.2.4 has a fix, so the 19.1 line and earlier must move forward. Gateways GitLab hosts were patched before the announcement. A HackerOne reporter, invisiblemeerkat, found it.

The flaw is in the prompt template engine that renders custom flows for Duo Agent Platform. An authenticated user with Duo Agent Platform access submits a flow configuration, template expressions in it break out of the rendering sandbox, and commands run on the gateway process. CWE-1336, vector AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H. The S:C reads worse than the 9.9 does: that host signs the gateway's JWTs and reaches both your GitLab instance and your model providers. CVE-2026-1868 hit the same engine class in February, also 9.9.

Duo Agent Platform access usually goes to every developer, so "low privilege" means most of your engineering org. I'd treat the gateway host as a secret store and ask what code running there could reach. No in-the-wild exploitation has been reported.

Do this today: check which AI Gateway image your deployment runs, upgrade to 19.2.4, 19.3.2 or 19.4.1, then confirm that host egresses only to your GitLab instance and model provider.

Which keys would code running on your AI Gateway find tonight?

🛰️ AI News · Oct 3
🇹🇷 GitLab, self-hosted AI Gateway'de CVSS 9.9'luk bir açığı kapattı (CVE-2026-90970): Duo Agent Platform erişimi olan bir kullanıcı, hazırladığı flow yapılandırmasıyla şablon kum havuzundan çıkıp gateway'de komut çalıştırabiliyordu. 19.2.4, 19.3.2 ya da 19.4.1'e geçin.
Source in the first comment.
#AINews #GitLab #DevSecOps #AISecurity #AppSec
