MCP Python SDK 1.9.1 to 1.29.1 hands over OAuth secrets.
Run an MCP client over HTTP with the SDK's OAuth providers and a hostile server takes credentials you use elsewhere.

GHSA-qx49-fqc8-xw99 landed Sep 28: High, CVSS 7.5, no CVE. Cycode reported it. Affected: mcp 1.9.1-1.29.1 and 2.0.0-2.1.1 on OAuthClientProvider, ClientCredentialsOAuthProvider and PrivateKeyJWTOAuthProvider. The fix shipped Sep 7 in 1.30.0 and 2.2.0, three weeks before the advisory said what it was.

The client learns which authorization server to use from the MCP server it just connected to. Before the fix it never compared the issuer field in the metadata it got back against the server it expected. So a malicious server advertises its own authorization server, and the client posts the client secret, authorization code and PKCE verifier to the attacker's token endpoint. In 2.0.0-2.1.1 that check existed but was skipped when a server published no protected resource metadata or answered 403 insufficient_scope.

Upgrading is not the whole fix. The two credential providers still follow the server's pointer unless you pass issuer=, and 1.30.0 raises only a DeprecationWarning, which Python hides by default. Registrations stored before the upgrade carry no issuer binding, so clear them. I'd treat any old client that reached a third-party MCP server as a credential incident.

Do this today: run pip freeze | grep -i "^mcp==" on every host running an MCP client, then grep the code for OAuthProvider( and check each call passes issuer=.

How many of your MCP clients could name the authorization server they trust?

🛰️ AI News · Sep 29
🇹🇷 MCP Python SDK'nın OAuth istemcisi, sunucunun gösterdiği yetkilendirme sunucusuna client secret'ı ve PKCE doğrulayıcısını gönderiyordu. 1.30.0 ya da 2.2.0'a geçin, provider çağrılarına issuer= ekleyin.
Source: GitHub Security Advisory
#AINews #MCP #OAuth #AIAgents #AppSec #DevSecOps #PythonSecurity #SupplyChainSecurity #InfoSec #CyberSecurity
Follow for daily AI security news.
