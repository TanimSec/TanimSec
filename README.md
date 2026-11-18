<a href="https://tanim.my.id"><img src="./assets/hero.svg" width="100%" alt="Tasnim Rahman Tanim — Lead Solutions Architect and ISO/IEC 27001 Lead Auditor, designing and securing multi-cloud platforms on OCI, AWS and Azure."></a>

<p>
  <a href="mailto:mail.tasnimrahman@gmail.com"><img src="./assets/btn-talk.svg" height="44" alt="Let's talk"></a>&nbsp;
  <a href="./Tasnim_Rahman_Tanim_Resume.pdf"><img src="./assets/btn-cv.svg" height="44" alt="Download CV"></a>&nbsp;
  <a href="https://tanim.my.id"><img src="./assets/btn-portfolio.svg" height="44" alt="Portfolio"></a>&nbsp;
  <a href="https://linkedin.com/in/contacttasnimrahmantanim"><img src="./assets/btn-linkedin.svg" height="44" alt="LinkedIn"></a>
</p>

<img src="./assets/stats.svg" width="100%" alt="99.9% uptime across client clouds · 15% higher presales win rate · 220+ engineers trained · 10+ ERP modules shipped">

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-about-dark.svg">
  <img src="./assets/h-about-light.svg" width="100%" alt="About — Cloud platforms built to pass the audit.">
</picture>

Multi-cloud platforms on **OCI, AWS and Azure**, secured with **EDR and SIEM** and audited against **ISO 27001 and NIST**. Lead Solutions Architect at Goinnovior; cybersecurity and networking trainer at Skill Jobs.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-expertise-dark.svg">
  <img src="./assets/h-expertise-light.svg" width="100%" alt="Expertise — What the work covers">
</picture>

<table>
<tr>
<td width="50%" valign="top">

**01 — Cybersecurity & GRC**

Detection engineering, EDR/XDR rollouts, perimeter defense and audit-ready compliance.

<sub>WAZUH · SURICATA · SYSMON · KASPERSKY EDR · FORTINET · SOPHOS · ISO 27001 · NIST CSF · SOC 2</sub>

</td>
<td width="50%" valign="top">

**02 — Cloud & Infrastructure**

Highly available multi-cloud architecture with identity and access at the core.

<sub>OCI · AWS · AZURE · ENTRA ID · INTUNE · M365 · LINUX · MIKROTIK · WIREGUARD · IPSEC</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

**03 — DevOps & Observability**

Infrastructure as code, containerized delivery and monitoring measured against SLOs.

<sub>TERRAFORM · DOCKER · GITHUB ACTIONS · PROMETHEUS · GRAFANA · LOKI · K6 · LOCUST</sub>

</td>
<td width="50%" valign="top">

**04 — Software Development**

Business systems and web apps that ship to production.

<sub>PYTHON · POSTGRESQL · ODOO 19 · NEXT.JS · REACT · TYPESCRIPT · REST APIS</sub>

</td>
</tr>
</table>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-work-dark.svg">
  <img src="./assets/h-work-light.svg" width="100%" alt="Work — Selected projects">
</picture>

<table>
<tr>
<td width="50%" valign="top">

**Enterprise SIEM & SOC Telemetry**

Production Wazuh SIEM/XDR cluster with Sysmon endpoint auditing, Suricata network detection and VirusTotal enrichment. Automated triage for privilege escalation, lateral movement and suspicious egress.

<sub>WAZUH · SYSMON · SURICATA · VIRUSTOTAL API</sub>

</td>
<td width="50%" valign="top">

**AI-Driven Vulnerability Management**

One DevSecOps pipeline: Strix AI finds issues, DefectDojo centralizes them and LLM triage removes false positives, cutting time to remediation.

<sub>STRIX AI · DEFECTDOJO · AISOC</sub> &nbsp;·&nbsp; [View repo ↗](https://github.com/TanimSec/AI-Driven-Vulnerability-Assessment-Management)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Multi-Cloud Observability Stack**

Oracle Cloud instances provisioned with Terraform, wired into metrics, logs and alerting, then load-tested with k6 and Locust to tune kernel and resource limits.

<sub>TERRAFORM · OCI · PROMETHEUS · GRAFANA · LOKI · ALERTMANAGER</sub>

</td>
<td width="50%" valign="top">

**Custom Enterprise ERP on Odoo 19**

10+ custom modules (Payroll, Attendance, Time-off, Document Management) and a browser-native office suite, with strict RBAC and automated off-site backups.

<sub>PYTHON · POSTGRESQL · ODOO 19</sub> &nbsp;·&nbsp; [Visit ↗](https://odoo.goinnovior.com)

</td>
</tr>
</table>

<details>
<summary><b>Architecture diagrams</b></summary>
<br>

**SIEM & detection pipeline**

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#141517','primaryTextColor':'#fafafa','primaryBorderColor':'#F65802','lineColor':'#F65802','clusterBkg':'#0c0d0e','clusterBorder':'#3f3f46','titleColor':'#fafafa','edgeLabelBackground':'#0c0d0e','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    subgraph Sources
        W["Windows + Sysmon"]
        L["Linux servers"]
        S["Suricata NIDS"]
    end
    W & L -->|agent| M["Wazuh Manager"]
    S -->|IDS alerts| M
    M <-->|hash / IP lookups| VT["VirusTotal API"]
    M --> I[("Indexer")] --> D["Hunting dashboards"]
    M --> A["Automated triage & alerts"]
```

**Observability on OCI**

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#141517','primaryTextColor':'#fafafa','primaryBorderColor':'#F65802','lineColor':'#F65802','edgeLabelBackground':'#0c0d0e','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    TF["Terraform"] --> VM["OCI instances"]
    VM -->|metrics| P["Prometheus"] --> G["Grafana"]
    VM -->|logs| LK["Loki"] --> G
    P --> AM["Alertmanager"]
    K["k6 / Locust"] -->|load tests| VM
```

**AI vulnerability pipeline**

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#141517','primaryTextColor':'#fafafa','primaryBorderColor':'#F65802','lineColor':'#F65802','edgeLabelBackground':'#0c0d0e','fontFamily':'Inter, Segoe UI, sans-serif'}}}%%
flowchart LR
    CA["Cloud assets"] --> ST["Strix AI"] --> DD["DefectDojo"]
    CR["Code scan results"] --> DD
    DD --> AI["AiSOC triage"] --> F["Validated findings"]
```

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-career-dark.svg">
  <img src="./assets/h-career-light.svg" width="100%" alt="Career — Where it happened">
</picture>

**Lead Solutions Architect & Security Auditor** — Goinnovior Limited<br>
<sub>JUL 2024 — PRESENT</sub><br>
Multi-cloud and security architecture on OCI, AWS and Azure at 99.9% uptime. Lead ISO 27001 / NIST auditor. EDR/XDR, NGFW and Odoo 19 ERP delivery, Docker + GitHub Actions CI/CD, and executive presales that lifted win rate by 15%.

**Cybersecurity & Networking Trainer** — Skill Jobs<br>
<sub>NOV 2024 — PRESENT</sub><br>
15+ four-month cohorts and 220+ professionals trained, with 95% completion and 60% job placement into SOC, IT and network roles.

**Cybersecurity Engineering Intern** — Skylark Soft Limited<br>
<sub>JAN 2023 — MAY 2023</sub><br>
Security policy and compliance controls. Selected for the government-sponsored Cybersecurity Advancement Program (IIT & EDGE).

<sub>EDUCATION — B.Sc. Information & Communication Engineering, Daffodil International University (2023)</sub>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-credentials-dark.svg">
  <img src="./assets/h-credentials-light.svg" width="100%" alt="Credentials — Certified to audit">
</picture>

**ISO/IEC 27001:2022 Lead Auditor** — MasterMind, 2026

- KATA & EDR Expert · Next EDR Administration — Kaspersky, 2025
- Google Cybersecurity Professional Certificate — Google, 2023
- Cybersecurity Specialization — ICT Division & IIT, University of Dhaka, 2023
- Full Stack Web Engineering — Programming Hero, 2026

<details>
<summary>All certifications</summary>
<br>

- Google IT Support Professional Certificate — Google, 2023–24
- Connect and Protect: Networks and Network Security — Google, 2025
- IT Security: Defense Against the Digital Dark Arts — Google, 2025
- Network & Server Administration — Skill Jobs, 2023
- Kaspersky: Next EDR Optimum · MDR · Security for Mail Server · Safe Web · SD-WAN · KUMA Sales & Presales
- OPSWAT Cybersecurity Associate · OWASP CIIP · Password Hacking & Malware Security · Play It Safe: Manage Security Risks
- Microsoft 365 Administration · Azure Administration · Google Networking · Google OS & Systems Fundamentals · Meta MySQL

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./dist/snake-dark.svg">
  <img src="./dist/snake.svg" width="100%" alt="Contribution graph">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/h-contact-dark.svg">
  <img src="./assets/h-contact-light.svg" width="100%" alt="Contact — Let's build something secure.">
</picture>

<p>
  <a href="mailto:mail.tasnimrahman@gmail.com"><img src="./assets/btn-talk.svg" height="44" alt="Let's talk"></a>&nbsp;
  <a href="./Tasnim_Rahman_Tanim_Resume.pdf"><img src="./assets/btn-cv.svg" height="44" alt="Download CV"></a>
</p>
