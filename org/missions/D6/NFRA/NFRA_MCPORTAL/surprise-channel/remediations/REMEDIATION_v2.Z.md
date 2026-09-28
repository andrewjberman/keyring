# NFRA_MCPORTAL -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-2 SLUG

Author: 3.0.0_SA_CVO~O. Round: v2. Fabric: site-z. Recorded: 2026-09-28T13:47:55Z. **Reader:** `1.0.0_SA_CTO~O`.

Three rows graduated this round, all OPEN for the round-3 recut.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W2-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "tests/test_owner_gate.py runs with AUDIT_PATH defaulting to ./audit.jsonl (app/config.py:307), so every suite run appends a real audit line to the TRACKED infra/aws/ec2/opal-gateway/audit.jsonl, and a wide commit or drain can carry it.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S3",
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S5",
      "infra/aws/ec2/opal-gateway/app/config.py:307 (read 13:4xZ)"
    ],
    "remedy": "OPEN: a test fixture that points AUDIT_PATH at a temp file (the issuer's own planned enrichment, Z-S5). Disarms when the suite leaves the tracked file clean.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MP-b-2 retired MCPORTAL_OWNER_OID for MCPORTAL_OWNER_KEY_CLAIM + MCPORTAL_OWNER_KEY, but lambda-source-map.json still describes the oid-only match, and any apply still passing mcportal_owner_oid names an undeclared variable.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W1-S5",
      "infra/aws/lambda/ci/lambda-source-map.json (MCPORTAL_OWNER_OID count 1, read 13:4xZ)"
    ],
    "remedy": "OPEN: the MP-a-1 re-cut (round 3) supplies the two new variables and refreshes the source-map note.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "EC2_MANIFEST.json services.opal-gateway.file_checksums is not refreshed by the gateway deploys, so it describes neither the deployed artifact nor the current release.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W2-S6",
      "infra/aws/ec2/EC2_MANIFEST.json (app/server.py a101f27e..., deployed_commit 6a98a0553a, read 13:4xZ)"
    ],
    "remedy": "OPEN: either the deploy refreshes file_checksums, or the field is retired. A consumer reading it today reads a stale value.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
