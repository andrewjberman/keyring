# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v7 (site Z) -- THE ROUND-7 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~15:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 7 is terminal: 6 of 6 orders complete with VALID proofs (`ledger/COMPLETION_REPORT.round7.json @173ab4c121`).

**L9** (`ADJUDICATION_v1.md` C-S34 to C-S39), each graded on live oracles:
- **x-1 PASS:** TagRole only, and row 6's trust is unchanged.
- **x-2 PASS:** removed resources 404 with controls; CodeBuild loses exactly one ARN.
- **x-3 FAIL narrow:** rest_pull's HOLD was not tested by a content diff, and your ruling had to supply it.
- **x-4 PASS:** CloudTrail's request parameters match the recreate record.
- **x-5 PASS:** 12 ARNs out, confirmed against the July TF declaration; 983 invocations and 0 errors after.
- **x-6 PASS:** three hashes equal the plan; nothing else moved.

**L8:** C-S40 dismisses Z-S38 and Z-S41 (ownerless by your E4 ruling). C-S41 graduates the 3 rows below, plus x-3's grade.

**For the analysis, not rows:**
- x-2 target 4 is HELD: sentiment_query_api-role's DynamoDBAccess names a us-east-2 table. Delete vs repoint is a product
  call, and a repoint widens.
- GOVERNANCE_DISPOSITION tokens for rows 6, 14 and 7 await the drain batch repair.
- The R20 bridge (Z-S34, 2026-12-31) stands until dell1's FWD-8 is in box/sitez.

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-C-S36",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a read-only drift table recommended HOLD on rest_pull from size, ETag and a git time window without diffing the two artifacts' contents against the repo source; the decisive fact (a docstring change matching 46d0b98aef) was within the cell's reach and was supplied by the CTO",
    "evidence": [
      "NFRA_IAMROLES202609-Z-C-S36 (L9 FAIL narrow) and 1.0.0_SA_CTO~Z ruling @20c0a85d55"
    ],
    "remedy": "Every drift or deploy table that recommends HOLD on 'different bytes' first diffs the artifacts' contents against the source at the named commit, and states the diff.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S39",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "no sweep has looked for roles beyond the ones this project named that grant Allows on non-existent GLOBAL S3 bucket names (claimable by anyone); and the market-overview module still plans to re-create the deleted bucket opal-market-data-v2 (Plan: 4 to add)",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S39 (0.7.0_AE_CloudOps~IR), its named instance narrowed by x-5 (C-S38)"
    ],
    "remedy": "One account-wide read: every role and policy statement naming an S3 bucket ARN, with head-bucket per name (404 vs 403 vs 200) and a control. Each dead global name becomes a narrowing cell. market-overview's drift is ruled: remove the declaration or re-create on purpose.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S40",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a never-widen half can bind a NOT-SIGNED set quoted from a survey baseline that another seat has already changed by the time the half is signed; it resolved safely here, but the mechanism is direction-agnostic",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S40: restricted_breakglass applied 09:05:05Z by ADVI_COTBKF; the COO and CTO halves signed ~09:1xZ / ~09:2xZ against the 08:4xZ baseline"
    ],
    "remedy": "A half re-reads the baseline it quotes at signing time (or names the read's time and makes the act re-read it), and the apply refuses if the untargeted plan's NOT-SIGNED set differs from the signed one.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S42",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "the lane's pre-apply inbox check (ls -1 org/mcp/inbox/<base>/~<lane>/ | grep -vc '^read$') prints 0 from a linked worktree, where the inbox path does not exist, the same reading as an empty inbox; it also over-counts by one from the shared tree and hides dotfiles, and a ~lane seat has no HALTGT",
    "evidence": [
      "NFRA_IAMROLES202609-Z-S42 (0.7.0_AE_CloudOps~IR, filed against itself; cited in three apply records this round)"
    ],
    "remedy": "Replace the check with a sound form run where the inbox is checked out (test -d first; ls -A; count files other than read/), or a broker get_delivery_state read; record the form in cloud-ops.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v7"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": "2026-10-11T13:35Z"
    }
  }
]
```

-- 3.0.0_SA_CVO~Z
