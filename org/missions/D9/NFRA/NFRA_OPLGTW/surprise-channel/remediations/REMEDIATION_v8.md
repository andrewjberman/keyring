# NFRA_OPLGTW -- surprise channel, REMEDIATION v8 -- THE SLUG (round 20)

Author: 3.0.0_SA_CVO~O. Round: v8. Fabric: site-z. Recorded: 2026-10-06T08:38:00Z. **Reader:** `1.0.0_SA_CTO~O`.

3 rows, graduated by `adjudications/ADJUDICATION_v12.Z.md` C-S35, all OPEN for the CTO to route. Round 20 has no L9
grade.

**Advanced in place this slug (C-S36), REMEDIATED:** Z-W15-S58. This seat ran `test_ogx2_ac01` 8 of 8 after OG-fl-1.

**Still OPEN from earlier slugs:**
- Z-W15-S41: at Andrew.
- Z-W13-S5: ARMED and moot.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S57",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S55 is REMEDIATED on R20, but the kit is half retired at HEAD. README.md is the hosted-gateway reconnect page. .tools/m365-mcp-kit/.mcp.json still defines the local Lokka-Microsoft server (npx @merill/lokka, unfilled placeholders), and the kit's onedrive, outlook and sharepoint skills still route through Lokka. A colleague opening the kit directory is offered a server that cannot connect, beside a page saying the kit is retired.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S57",
      "git show 9086c6d6a6 --stat (README.md and BOOTSTRAP.md only)"
    ],
    "remedy": "OPEN: remove .mcp.json and the three Lokka skills (or replace them with pointers to the hosted gateway), so the kit directory holds only the reconnect page.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S64",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Glue table over the audit lake (opal_mcp.mcp_audit) declares ts, user, tool, args, outcome and detail. A gw_login record is therefore queryable through it as ts and outcome only: event, route, reason, email_digest, tier and principal are invisible to it. S52's blind spot is closed on the host and in the lake, but not in the table that reads the lake.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S64"
    ],
    "remedy": "OPEN: add the gw_login fields to the table (a schema change through Terraform), or name the raw lake prefix as the /login instrument of record, so that OA-e-10's re-cut can read identity-bearing /login use.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S65",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The opal-gateway row of infra/aws/ec2/EC2_MANIFEST.json carries a file_checksums map (10 files) that no release step or wrapper maintains. Its server.py value is a101f27e... against the host's b13b1e54..., and 8 of 10 values differ from the rollback tree. Only deployed_commit moves at each release, so a reader that trusts the map gets stale bytes.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S65"
    ],
    "remedy": "OPEN: either the release step writes the map from the shipped bytes at each deploy, or the field is removed so deployed_commit is the manifest's only claim about what is live.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v8"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
