# Architecture Overview — Public / Vendor-Neutral

This document presents a high-level architecture suitable for public review. It intentionally excludes product credentials, internal addresses, production sizing, private endpoints, firewall/VPN configuration, and detailed security topology.

```mermaid
flowchart LR
    A[External / Internal Data Sources] --> B[Secure API & Integration Boundary]
    D[Documents / Files] --> C[Ingestion & OCR]
    B --> E[Integration / Ingestion Services]
    C --> E
    E --> F[Validation / Transformation / Audit]
    F --> G[(Operational & Analytical Data Stores)]
    G --> H[Transaction & Relationship Analysis]
    G --> I[Case Management]
    G --> J[Refund / Asset Return Workflows]
    G --> K[Reporting & Dashboard]
    G --> L[Chatbot / Assistance]
    M[SSO / MFA / IAM / RBAC] -. access control .-> B
    M -. access control .-> H
    M -. access control .-> I
    M -. access control .-> J
    M -. access control .-> K
    M -. access control .-> L
    N[Logging / Monitoring / Audit] -. observability .-> B
    N -. observability .-> E
    N -. observability .-> I
```

## Architecture principles

- Secure integration boundary
- Controlled ingestion and provenance
- Separation of concerns
- Identity-first security
- Environment separation

## Excluded from public architecture

- endpoint lists, IP addresses, DNS names, private network ranges
- firewall, WAF, VPN, IDS/IPS rules
- production account/project/subscription identifiers
- keys, certificates, secrets, tokens, or passwords
- exact infrastructure sizing and capacity values
- security-test findings or remediation details
