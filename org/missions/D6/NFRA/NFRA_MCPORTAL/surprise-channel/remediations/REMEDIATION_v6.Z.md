# NFRA_MCPORTAL -- remediation v6 (site Z): the project slug's remediation rows

Author: 3.0.0_SA_CVO~Z. Round: v6. Fabric: site-z. Recorded: 2026-10-21 ~00:5xZ. Committed with ADJUDICATION_v14.Z.md.

The rows:
- **Z-S77:** graduated in v14. OPEN and ARMED, with its owner. Z-S63 was dismissed in v14 and has no row here.
- **Z-W31-S6 and Z-W31-S7:** graduated earlier as C-S41. Both are REMEDIATED on catalog counts this seat re-measured.
- **Z-W25-S2:** graduated as C-S40, CLOSED_UNREMEDIATED with NOT_A_DEFECT.
- **Z-C-S60:** disarms Z-W3-S2. That is a graduated item, and it leaves ARMED only through a remediation row whose
  `disarm.state` is DISARMED (`.tools/comp-surprise.py:246-260`).

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-S77",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Every gateway rollback through safe-ec2-deploy.sh first runs .tools/halt-gate-check.sh's per-message scan (L456-475; HALT_ACK read only at L515); on 2026-09-25 it took about 12 minutes over 186 pending messages, so a 60-second /health rollback trigger can leave the gateway down for minutes.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S77, #NFRA_MCPORTAL-Z-W2-S8",
      "ADJUDICATION_v13.Z.md#NFRA_MCPORTAL-Z-C-S59 @a19cd08032",
      "ADJUDICATION_v14.Z.md#NFRA_MCPORTAL-Z-C-S65"
    ],
    "remedy": "OPEN: batch16's CLOSED report (2026-10-21) carries the first measured halt-gate time; under 60 s disarms. The scan itself is 0.0.0_AB_MSTR's lane if it must change.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v6"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPORTAL-Z-W31-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The real catalog's tool_index block carried no vendor or firm, so the breakdown could not segment tools by (vendor, firm).",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W31-S6",
      "ADJUDICATION_v*.Z.md#NFRA_MCPORTAL-Z-C-S41",
      "infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml @13917ef993 tool_index lines 1349-3356: 'vendor:' 23, 'firm:' 23 (re-measured by 3.0.0_SA_CVO~Z 2026-10-21)"
    ],
    "remedy": "Executed: the live release's tool_index carries vendor and firm. Bound: the count is non-zero, not proven complete against every assets/bd tool; the worker's second note (273 'firm:' lines outside tool_index with another meaning) stands and is read only from tool_index by the handler.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v6"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPORTAL-Z-W31-S7",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MP-pf-3 built the serves list and the store kind, but the real catalog carried neither, so the real breakdown could not show them.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W31-S7",
      "ADJUDICATION_v*.Z.md#NFRA_MCPORTAL-Z-C-S41",
      "infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml @13917ef993 tool_index lines 1349-3356: 'serves:' 7, 'kind: store' 15, 'source_group:' 127 (re-measured by 3.0.0_SA_CVO~Z 2026-10-21)"
    ],
    "remedy": "Executed: the live catalog carries serves, store kinds and source groups. Bound: non-zero, not proven complete; completeness of serves per tool is NFRA_MCPINDEX's FWD-23 routing table, which re-reads it.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v6"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPORTAL-Z-W25-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order's face gave a zero-argument call form for app.admin_gateway_breakdown._scan_principals, which takes a required client; the worker used the served module's own host-role client, the correct form.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W25-S2",
      "ADJUDICATION_v*.Z.md#NFRA_MCPORTAL-Z-C-S40"
    ],
    "remedy": "None needed in the product: the defect was in the order text, and the product is unchanged and right.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v6",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v6",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W25-S2 -- the order's call form, not the product"
      }
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S60",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-W3-S2: the grant writer's owner configuration needed Andrew's Entra oid and no record named it; the re-cut MP-t-3 carried the oid the issuer measured in gateway-access-state-table, accepted by the PRD owner because the setting fails closed (REMEDIATION_v1.Z.md row Z-W3-S2, R-1).",
    "evidence": [
      "deliverables/0.9.0_WK_NFRA_MCPORTAL~45/row_evidence.json row Z-W3-S2: MCPORTAL_OWNER_KEY and MCPORTAL_OWNER_KEY_CLAIM present (names only); zo5.AC2.sh no-header invoke status=200 REFUSED NO-OWNER-HEADER, PASS",
      "ADJUDICATION_v13.Z.md#NFRA_MCPORTAL-Z-C-S57 @a19cd08032",
      "infra/aws/ec2/opal-gateway/app/owner_gate.py:34 (the gateway owner gate admits andrew@ only)"
    ],
    "remedy": "Executed: the deployed writer carries the owner key and answers past its owner-configuration check. The key's equality with Andrew's oid is proven at the close run's owner-header write (MP-zo-4), which records it.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v6"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~MP",
      "at": "2026-10-21T00:50:00Z"
    },
    "disarms": [
      "NFRA_MCPORTAL-Z-W3-S2"
    ]
  }
]
```

-- 3.0.0_SA_CVO~Z
