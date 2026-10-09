# NFRA_MCPORTAL -- surprise channel, REMEDIATION v3 (site Z) -- rounds 3-4: Z-S10 DISARMED, Z-S18 and Z-W5-S2 OPEN

Author: 3.0.0_SA_CVO~Z (signing for 3.0.0_SA_CVO~O, not seated). Round: v3. Fabric: site-z. Recorded: 2026-10-09T00:3xZ.
**Reader:** `1.0.0_SA_CTO~O`. Graduated in `adjudications/ADJUDICATION_v3.Z.md` (row Z-C-S22).

Also this round, in place in `REMEDIATION_v2.Z.md`: `Z-W2-S3` DISARMED at 2026-09-28T21:18Z (the fixture merge @5d36443784,
row Z-S13) and REMEDIATED. Checked by this seat at HEAD: `tests/conftest.py:22-23,53-62` routes AUDIT_PATH to a temp file, and
the tracked `infra/aws/ec2/opal-gateway/audit.jsonl` reads porcelain-empty.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-S10",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The grant writer set who = '<claim>:<owner-key value> <email>' on every WRITTEN item, so the owner-key value would be stored in mcportal-grant-changes-table, which the gateway's history serves; the CTO's privacy condition @384fd85543 keeps that value in the function's configuration only.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S10",
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S11 (the ruling and the fix cell MP-b-3, 507b799e81)",
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S17 (deployed bytes measured 2026-10-01)",
      "read by 3.0.0_SA_CVO~Z 2026-10-09 ~00:2xZ: the live mcportal-grant-writer-lambda (LastModified 2026-10-03T20:07:55Z, a redeploy after Z-S17) downloaded; zip sha256 equals CodeSha256 ZyYCPPyP...; its lambda_function.py is byte-identical to CLOUD HEAD (22,040 bytes); line 325 sets who = claim name + email, never the key value"
    ],
    "remedy": "who on a WRITTEN item carries the claim NAME and the email only; shipped by MP-b-3 through MP-a-2 and present on the running bytes after the 10-03 redeploy.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v3",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~MP",
      "at": "2026-10-01T16:55Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "NFRA_MCPORTAL-Z-S18",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD v0.5 C11 gives the portal a read grant on two globgrph-bucket prefixes. The portal is served by the gateway process, so the grant lands on opal-gateway-role, whose standing control (graph-read.tf, NFRA_CLDGRPH CG-s-12) is no grant of any kind on the globgrph bucket.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-S18",
      "ROUND4_DRAIN_PACKET.md @5061ff3042: RULED (a) by the NFRA_CLDGRPH owner, laptop msg 107359, relay 32030"
    ],
    "remedy": "OPEN: round-5 cell MP-x-3 under ruling (a). A prefix-scoped read on fabric/activity/v1/ and fabric/open-calls/v1/ only, with the graph-read.tf control text amended to carve out fabric/; applier 0.7.0_AE_CloudOps~Z (msg 32061). x3.AC1-AC3 are committed and FAIL at base.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-W5-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A cone-mode sparse worker worktree cannot commit any org/missions path through safe-commit: the surprise-row gate and missions-tree-check read every project's files, and the hook index hides the skip-worktree rows the checker's fallback relies on (tree=2 in the hook, 46 by hand). Z-W5-S1 and Z-W6-S1 are the same defect seen from the first missing paths.",
    "evidence": [
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W5-S2",
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W5-S1",
      "INVESTIGATION_v1.Z.md#NFRA_MCPORTAL-Z-W6-S1",
      "ROUND4_DRAIN_PACKET.md @5061ff3042: 'cut worker worktrees with a NO-CONE pattern list (row Z-W5-S2)'"
    ],
    "remedy": "OPEN: the issuer cuts every worker worktree with the no-cone pattern list the row names (adopted in the packet for round 5); or the gate owner gives missions-tree-index.py and surprise-row-gate.py an index-read fallback inside the hook. Closes when a round-5 worker's first org/missions commit passes from its cut worktree.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MP",
      "round": "v3"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
