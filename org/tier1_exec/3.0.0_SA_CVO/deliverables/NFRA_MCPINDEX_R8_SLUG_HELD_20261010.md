# NFRA_MCPINDEX -- surprise channel, REMEDIATION v6 -- THE ROUND-8 SLUG

Author: 3.0.0_SA_CVO~Z. Round: v6 (round 8). Fabric: site-z. Recorded: 2026-10-10 ~23:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 8 is terminal: 4 of 4 orders complete, and the release d3c31e972e is live with its labels repaired. L8 and L9 are
at `adjudications/ADJUDICATION_v7.md`. Z-C-S40 and Z-C-S41 dismiss 15 rows (every BLOCKING or ARMED row of the round is
among them). Z-C-S42 graduates the rows below. J2 is graded: FWD-12 PASS (Z-C-S43), FWD-18 FAIL narrow (Z-C-S44).

**The thread criterion (FWD-11, Alyssa's own run) is NOT graded.** It is HELD at Andrew through `0.0.0_AB_MSTR~Z`; its
precondition is met. The issuer's live run (packet section 2) routed "how did the growth model do against its benchmark"
to E-13, which served data as of 2026-10-09 (T-1 for a Saturday). No model is named "growth". Whether discover or the
tool answer asks which model is a design call for the CTO (packet section 5 item 3), and it is part of what the thread
grade judges.

**For the analysis:** the deploy procedure (row Z-S92 below), the catalog tag fix (Z-C-S44), and round 9 (FWD-19
readers), which is cut after this L10 per the CTO ruling call 9c9d.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S44",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "E-25 (Bloomberg prices, SERVED) carries retires C1, but C1 is the YCharts report workflow (E-20, GAP), so the catalog's served-retired count reads 4 of 14 where 3 of 14 is true; and no entry carries C3, though E-4, E-5 and E-9 are its needs",
    "evidence": [
      "ADJUDICATION_v7 Z-C-S44: SERVED retires = C1, C2, W5, W6; untagged C3, C7, C8 (C7, C8 named outside at brief :88)"
    ],
    "remedy": "In the next catalog cell, drop C1 from E-25's retires (or mark it partial with a reason a reader can reject on) and add C3 to E-4, E-5 and E-9; re-read the FWD-18 count from the served catalog.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S92",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy-to-ec2.sh names and stamps the artifact from the deploy worktree's rev-parse HEAD, so a release shipped as uncommitted edits over a detached base is mislabelled; the manifest auto-commit fails in a sparse tree (commit_gate_runner.py:96, ModuleNotFoundError comp_constants_cli) on both MX-r-9 runs",
    "evidence": [
      "Z-S92 (the instance, disarmed by Z-S95 and re-read at Z-C-S40)",
      "L8_PACKET_ROUND8.md section 5 item 1"
    ],
    "remedy": "The release procedure requires the deploy tree's HEAD to BE the deploy-only commit, and the wrapper refuses a dirty tree; fix the sparse-tree import in the manifest commit. deploy-to-ec2.sh is shared with NFRA_OPLGTW: the CTO names which issuer cuts it.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S88",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the opal-gateway test suite is red at the round-8 base with 34 to 38 pre-existing failures (schwab_*, asker_scope, portal_grant, data_entitlement_*, principal_cutover, local_acceptance) plus order-dependent ones; it was 13 named at round 6 (Z-W21-S15)",
    "evidence": [
      "Z-S88 (34 failed / 657 passed on the branch)",
      "Z-W28-S8 (38 / 600 / 4 on the sparse release trees)"
    ],
    "remedy": "Name an owner per failing family (most are NFRA_OPLGTW's schwab and grant tests) and run the suite at the drain against a recorded baseline id list, so a NEW failure is visible against the old ones.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W28-S8",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the suite's BEFORE figure depends on the tree and the test order: 38 failed / 600 passed / 4 errors on the sparse release trees against Z-S88's 34 / 657 on a full tree, and 2 schwab tests fail or pass by order",
    "evidence": [
      "Z-W28-S8 (run 1 and run 2 on the release tree)"
    ],
    "remedy": "Record the baseline as a failing-id list per tree shape, and fix or quarantine the order-dependent tests, so a drain's suite delta is read by id and not by count; rides Z-S88's cell.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W29-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the catalog emitter, given a --census-dir in the main tree from a linked worktree, rewrites every census_ref as ../ajb_workspace/..., changing 32 catalog lines outside needs:",
    "evidence": [
      "Z-W29-S1; Z-S86 confirmed the worktree's tracked census is the right input"
    ],
    "remedy": "Default the emitter's census dir to the checkout it runs in, or refuse a census dir outside it; until then every catalog cell's face names the worktree census.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-W28-S4",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "two of Alyssa's six phrasings ('statement', 'S&P YTD') reach their entries only through need-local folds and a one-word fallback the order did not name",
    "evidence": [
      "Z-W28-S4; Z-S87 confirmed it as an enrichment"
    ],
    "remedy": "Move her phrasings into E-9 and E-19 example_questions in the next catalog cell, then retire the folds.",
    "owner": "2.0.0_SA_COO~MI",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~MI",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-S94",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the gateway deploy extracts the tarball over /opt/opal-gateway and prunes nothing, so 2 orphaned mcportal vite assets accumulate (105 host files against 103 in the artifact)",
    "evidence": [
      "Z-S94; Z-S95 routed it to 2.0.0_SA_COO~O as NFRA_OPLGTW's deploy surface"
    ],
    "remedy": "Prune files absent from the artifact at extract time, or state the host census as artifact-subset-of-host; NFRA_OPLGTW's issuer cuts it.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S42",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check.py:388 requires a grading row to name the order only for AC<n> ids, so a bare judgment id of the J<n> form is graded by any CVO-kind row in any round; NFRA_MCPINDEX round 8 reads graded=2 / MAY-CLOSE while its thread criterion has never run",
    "evidence": [
      "round-close-check --project NFRA_MCPINDEX --round 8 at ~23:0xZ 2026-10-10: the thread criterion reads GRADED by adjudication row Z-C-S26 (3.0.0_SA_CVO~O, an earlier round)"
    ],
    "remedy": "Extend the order-name requirement to every id that is not order-unique (J<n> included), with a test planting a stale CVO row; same family as the id fallback 2.0.0_SA_COO~C holds (NFRA_REPORT Z-S26 / NFRA_MCPMSP-Z-S4).",
    "owner": "2.0.0_SA_COO~C",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v6"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
