# NFRA_OPLGTW -- adjudication v13 (site Z): round 21's L8 (the project parks per R26)

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T09:05:00Z. Trigger: `2.0.0_SA_COO~O` msg 29984 (round 21 TERMINAL, 3 of 3:
OG-dc-2, OG-mf-1, OG-o-6; last drain 98e4253cb0; per R26 no round 22 is cut).

**Terminality and census.** All 3 orders are complete per the issuer. Round 21 carries no judgment criterion, so this
round has no L9 grade. `comp-surprise --project NFRA_OPLGTW` reads 365 investigation items, 0 OPEN, and 1 ARMED
(Z-W13-S5, standing). The round filed no new investigation row, so this file holds one record row: the three
remediation rows round 21 was cut for, advanced to REMEDIATED in place on this seat's own reads.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S37",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T09:05:00Z",
    "one_line": "Round 21 L8 (no new rows): Z-S57, Z-W15-S64 and Z-W15-S65 advanced to REMEDIATED on this seat's reads at CLOUD; the channel reads 0 OPEN of 365; the only gateway-tree difference live..CLOUD is the runbook, which does not ship.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read.",
    "world_is": "Z-S57 (OG-dc-2): git ls-files .tools/m365-mcp-kit/ lists README.md only; .mcp.json and the three Lokka skills are gone. Z-W15-S65 (OG-mf-1): the opal-gateway row of infra/aws/ec2/EC2_MANIFEST.json reads file_checksums {} beside a _checksums_note, with deployed_commit 2c27f3a795 the manifest's claim about live. Z-W15-S64 (OG-o-6): infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md:161 names the raw lake (bucket opal-mcp-audit, prefix audit/dt=<YYYY-MM-DD>/) as the /login instrument of record, lists every gw_login field, and states that the Glue table mcp_audit shows only ts and outcome; that is the remedy's second branch. git diff --name-only 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway lists the runbook only, which is not host-shipped and is listed in LINEAGE_R18. Still OPEN on the channel: Z-W15-S41 (at Andrew); Z-W13-S5 (ARMED, moot, the issuer's disarm); and older rows from rounds v1-v3 that the gate's staleness disclosure lists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files .tools/m365-mcp-kit/ (1 path), read ~09:0xZ",
        "infra/aws/ec2/EC2_MANIFEST.json opal-gateway row: file_checksums {}, _checksums_note present",
        "infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md:161",
        "git diff --name-only 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway (1 path: the runbook)",
        "comp-surprise --project NFRA_OPLGTW: investigation_items 365, open 0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
