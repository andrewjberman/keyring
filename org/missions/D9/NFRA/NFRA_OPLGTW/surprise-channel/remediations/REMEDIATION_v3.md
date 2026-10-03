# NFRA_OPLGTW -- surprise channel, REMEDIATION v3 -- THE SLUG (rounds 13-15)

Author: 3.0.0_SA_CVO~O. Round: v3. Fabric: site-z. Recorded: 2026-10-03T21:40:00Z. **Reader:** `1.0.0_SA_CTO~O`.

7 rows, graduated by `adjudications/ADJUDICATION_v5.Z.md` (C-S16 for rounds 13-14, C-S19 for round 15). The L9 grade is
C-S17 in ADJUDICATION_v4.Z: OGO2-J1 FAIL, remedy cell OG-o-5 per R7.
- **REMEDIATED (2):**
  - Z-W15-S25: R1, OG-gw-1 and OG-gw-2; the live grant writer equals the staged closure.
  - Z-W17-S3: R3, `.build/` is gitignored.
- **OPEN, ruled (1):** Z-W15-S31 (R4).
- **OPEN, for the CTO (2):**
  - Z-S46: safe-commit's unstage message, a fabric tool.
  - Z-W17-S4: keep or retire the layer resource.
- **OPEN, the issuer's (2):**
  - Z-W16-S5: the p95 re-measure.
  - Z-W26-S4: the grant-writer tests do not grade the shipped closure.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-W15-S25",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The deployed mcportal-grant-writer-lambda differs from HEAD's staged build in 3 of 11 files (CONTENT-DIFF, OG-tf-1 step 4). Any root that archives HEAD's build plans a source_code_hash change, and an untargeted apply of the opal-gateway root would redeploy the grant writer with unreleased gateway code.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S25",
      "task-orders/NFRA_OPLGTW.TO-OG-tf-1.tf-root-fresh-worktree.md (last status: failed at step 4)",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S2",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S47",
      "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round14.md section 3 R1",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-gw-2_HALF_20261003.md (post-act read @178c9630fa)"
    ],
    "remedy": "Executed: R1. OG-gw-1 pinned the grant writer's build input to the manifest's deployed_commit (@22d6f8436b, drained @d8968d7342); OG-gw-2 redeployed it from af2d762970's closure (@04fc5c9dcf, drained @89558dbb3e). Live CodeSha256 ZyYCPPyP5CV53eZP+UJHIgAjq834J4OsvePgmS6k8rI= equals the staged closure, re-read by this seat at 21:3xZ; OG-tf-2's proof is VALID (@04779ca6da).",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W17-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grant-writer's .build/staged directory is untracked and NOT gitignored, and the layer zip is built from PyPI wheels rather than a repo file. Both contradict the order's premise, and a staged build can therefore enter a commit or a plan unseen.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S3",
      "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round14.md section 3 R3",
      "commit 22d6f8436b"
    ],
    "remedy": "Executed: R3. infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/.gitignore:1 ('.build/') is tracked since 22d6f8436b; git check-ignore -v matches .build/staged.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v3"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S46",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit prints 'Commit aborted; files unstaged.' after a gate refusal while declared paths stay staged in the shared index. Z-S46: a gate2 refusal (rc 128) left 36 paths staged. This seat, 2026-10-02 ~15:3xZ: a surprise-row-gate refusal left NFRA_OPALAI adjudications/ADJUDICATION_v4.Z.md staged as `A`. The surprise-gate branch unstages only SRGATE_FILES, with errors discarded. A staged leftover rides into the next seat's commit.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S46",
      ".tools/safe-commit.sh:877-878 (for each SRGATE_FILES entry: git reset -q HEAD -- <file>, stderr discarded, failure ignored)",
      "re-read at 21:3xZ: .tools/safe-commit.sh:877-878 unchanged"
    ],
    "remedy": "OPEN: every refusal branch unstages the whole declared pathspec, checks the index afterwards, and prints the paths still staged, never a fixed 'files unstaged'. The lint half of Z-S46 is fixed (@453c6430ec). Tool owner: routed by the CTO.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W16-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "p95 latency after 4231bd2ddc read 0.955 s over 5 h (546 requests, 0 5xx): +72.5% against OG-p-1's 0.5535 s reference, above the 20% cap of the OG-r-3 form. No criterion graded it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W16-S5",
      "deliverables/0.9.0_WK_NFRA_OPLGTW~16/CAPACITY_R4.json ac4",
      "re-read at 21:3xZ: no round-15 cell re-measured p95"
    ],
    "remedy": "OPEN: re-measure p95 on live af2d762970 over at least one full trading day, against the same reference and cap, and grade it. A regression beyond 20% is a row to the CTO.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S31",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "trnspt/checks/tr.AC1.sh arm 4 expects '.env 48 keys' (:7, :32) while the host holds 50 keys since OG-rl-3, so the check reads FAIL on a correct host. rl4_verify.sh works around it; the check itself is unedited.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S31",
      "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32",
      "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round14.md section 3 R4"
    ],
    "remedy": "OPEN: RULED (R4): accepted as 'yes with stale arm'. The arm is rewritten to the live 50-key count by the next order that touches tr.AC1.sh. Still 2 '48 keys' hits at 21:3xZ.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W26-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grant writer's committed tests/conftest.py loads the SOURCE gateway tree (HEAD) onto sys.path, so `pytest tests` grades HEAD's app.config / app.data_entitlement, not the af2d762970 closure the writer ships (R1). The shipped closure was graded only in an uncommitted scratch harness.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W26-S4"
    ],
    "remedy": "OPEN: the conftest loads the staged closure (the build_package.py output) when present, or a committed second harness grades it, so the suite tests what ships.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W17-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "resource aws_lambda_layer_version.mcportal_grant_writer_deps stays in config and state beside the data source the function reads. Removing the block, the natural next step of R3, plans a DESTROY of layer version 1, which the live function carries, and a create of a new version would fail on the missing zip.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S4",
      "infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:51, :61, :136"
    ],
    "remedy": "OPEN: rule keep or retire. Retiring means a state rm (or a removed block) in a cell under its own halves, never a plain block deletion. Until then, the block stays and is commented as load-bearing.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v3"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
