# NFRA_MCPORTAL -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Recorded: 2026-09-25T04:35:00Z. **Reader:** `1.0.0_SA_CTO~O`
only. The recut is `2.0.0_SA_COO~O`'s.

Input snapshot: workspace `c5cdf8027c`; mcportal `r1-drain` @`920efd1`. Investigation:
`INVESTIGATION_v1.Z.md@fa00039009` (9 rows). Adjudication: `adjudications/ADJUDICATION_v1.Z.md` (same commit): 9 of 9
items dispositioned (5 GRADUATED, 4 DISMISSED_WITH_REASON), plus 2 CVO findings (C-S10, C-S11). Terminality: 7 of 7
orders (5 complete, 2 superseded under R-1). Instances: 6 of 6 VALID rc=0 on this seat's run. Judgment criteria this
round: 0.

Seven rows: **1 REMEDIATED** inside the round (the checker) and **6 OPEN** for the recut. The OPEN rows are:
- round 2's first cell (the staged build, R-1);
- **an unmeasured premise that sits under that cell** (C-S10, ARMED): the writer matches an `oid` claim and needs an
  `iat` claim in the ALB header, and no one has seen a real header's claims;
- the owner oid's carriage;
- one fabric-tool gap shared with NFRA_OPALAI;
- two enrichments: a global changes feed for FWD-4, and a plain refusal on a non-JSON response.

No row carries `route` or `loop_target`.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W3-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issuer's shared check helper held statements inside a python -c list comprehension (SyntaxError), and its 2>/dev/null turned the crash into an empty lookup, so t2.AC1-AC3 FAILed for every build and the base dry-run read that as the expected FAIL.",
    "evidence": [
      "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S1, #NFRA_MCPORTAL-Z-S1",
      "fix 259e1cf375 (ancestor of HEAD); _root.sh:15-21 at c5cdf8027c",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S1"
    ],
    "remedy": "Executed inside the round: the fixed checker at 259e1cf375, a two-arm control (base entries=0, branch entries=1), and MP-t-2 re-graded 3 of 3 PASS. No cell is cut.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": true,
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~O", "at": "2026-09-24T23:55:00Z"}
  },
  {
    "id": "NFRA_MCPORTAL-Z-W3-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The grant writer climbs parents[5] to a repo root and imports app.access_state and ops.schwab_entitlement_admin from the gateway tree, but its Terraform zips only the function's own directory and names a root-level handler, so at /var/task the import fails before any branch runs. MP-t-2's three mechanical criteria never imported the handler from the built package.",
    "evidence": [
      "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S3",
      "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:42-48; infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:25-28, :85",
      "deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@aed83d11fe R-1",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S8"
    ],
    "remedy": "R-1, verbatim in substance: round 2's FIRST cell is a staged build that carries the writer plus the exact gateway modules it imports, from the same source at the same commit; the package root is resolved from the package, with no parents[N]; the proof imports the handler FROM INSIDE THE BUILT ZIP. MP-t-3 and MP-t-6 re-cut behind it. This seat adds one requirement: the in-zip import proof runs the handler on one refusal arm (no header), so it exercises the imported modules and not only the import.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null}
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S10",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "C4's owner check is built on the verified header's `oid` claim, with a replay window on its `iat` claim. The ALB fills that header from its configured userinfo endpoint (graph.microsoft.com/oidc/userinfo, scope 'openid profile email'). No one has observed a real header's claim set, and the writer's tests plant both claims themselves. If either claim is absent, the deployed writer refuses the owner on every call, while every negative arm still 'passes'.",
    "evidence": [
      "infra/aws/terraform/opal-gateway/alb.tf:170-179; infra/aws/ec2/opal-gateway/app/identity.py:65-66",
      "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:107-120; tests/test_grant_writer.py:77-80",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S10 (claim class INFERRED; the measurement that settles it is named there)"
    ],
    "remedy": "Before the staged-build cell is cut: measure ONE real x-amzn-oidc-data header from an ALB-authenticated request and record its claim KEYS, with values redacted. Then: (a) if oid is present, no change; (b) if it is absent, the PRD owner rules which carried claim is the owner key (C4 names 'Andrew's Entra object id', so a different key is a C4 wording decision for 1.0.0_SA_CTO~O), and the owner config value is re-measured on that key; (c) if iat is absent, the window is anchored on a claim the header does carry. In every case, A1n asserts the refusal REASON per arm (NOT-OWNER, HEADER-STALE, NO-OWNER-HEADER), never only the verdict.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~O", "at": null}
  },
  {
    "id": "NFRA_MCPORTAL-Z-W3-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The writer's owner configuration needs Andrew's Entra oid. The worker found no record naming it; the issuer then measured it in gateway-access-state-table (6 of 6 of Andrew's rows, 118 of 118 items), and the PRD owner accepted it (R-1) because the setting fails closed.",
    "evidence": [
      "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W3-S2, #NFRA_MCPORTAL-Z-S2, #NFRA_MCPORTAL-Z-S3",
      "deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md@aed83d11fe R-1",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S7"
    ],
    "remedy": "The re-cut MP-t-3 carries oid 2e21f8e5-55ca-45c1-91b9-a4607bf28d4f as var.mcportal_owner_oid, subject to C-S10's measurement: if the header carries no oid, the value is re-measured on the key the PRD owner rules.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "owned-paths-validate's --check-agent resolves a lane before it consults the task-order grant, so a worker's order that names a path with no .owned-paths.yaml entry is refused UNDEFINED. Every such first commit takes the audited override, and the override log fills with legitimate entries.",
    "evidence": [
      "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W1-S1",
      ".tools/owned-paths-validate.py:414 at c5cdf8027c; last changed 4e3142cfb3 (2026-09-10), before the row",
      "the same mechanism on record as NFRA_OPALAI-Z-W1-S1",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S3"
    ],
    "remedy": "Let the UNDEFINED branch in _cmd_check_agent (and check_agent's early return) fall through to _owns_task_order_paths before concluding UNDEFINED. Control: a worker whose non-terminal order names a new top-level path is admitted, and the same path with no order is refused. One fix serves both projects. Whose fix is for 1.0.0_SA_CTO, the disarm owner.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false,
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null}
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "operator_audit lives per principal (POLICY#<tid>#<oid>) and the store reads one partition, so GET /api/admin/changes is tid/oid-scoped. FWD-4's 'each change is listed newest first' is the dashboard's history, which needs a cross-principal feed.",
    "evidence": [
      "INVESTIGATION_v1.Z.md@fa00039009#NFRA_MCPORTAL-Z-W2-S1",
      "PRD v0.2 FWD-4 ACCEPT and C5",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S4"
    ],
    "remedy": "An enrichment for the FWD-4 round. The CTO chooses the feed's source (an index on operator_audit, the writer's own log group, or a rollup); an index touches NFRA_OPLGTW's store and may meet G-OPLGTW. Until then the page states that it shows one person's history.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S11",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A static host's SPA fallback answers an unknown /api path with index.html and 200, and the typed client parses it as JSON, so Recent Changes shows a raw parse error instead of a reason.",
    "evidence": [
      "deliverables/2.0.0_SA_COO~O/round1/real_run/RESULT.md@c24f9788e9; recent-changes.png",
      "ADJUDICATION_v1.Z.md#NFRA_MCPORTAL-Z-C-S11"
    ],
    "remedy": "The issuer's own enrichment: the typed client refuses a response whose content type is not JSON and shows a plain, quotable reason. Its test plants an HTML 200 response.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O", "round": "v1"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
