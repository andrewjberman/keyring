# ETFS_RIVALS -- round 1 remediations (site-Z fabric)

<sweep_watermark>2026-09-30T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01. Graduated at round 1's L9 (`adjudications/ADJUDICATION_v1.Z.md`). Eight items. None carries a route: the slug goes to the CTO at round 2's L10, once TO-RIV-d-3 is terminal.

```json
[
  {
    "id": "ETFS_RIVALS-Z-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD C-SHAPES (ETFS_RIVALS_PRD.md:307, at HEAD) says a GICS sector never stands in for a sub-asset class. The vocabulary the PRD names (etf_positioning_gold.py:150) defines the equity sub_asset_class AS the GICS sector. Both cannot hold for an equity row once GICS arrives.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S1 (2.0.0_SA_COO~RV)",
      "ETFS_RIVALS_DECOMP.md:97-98: GICS stays UNRESOLVED because its source G4 is round 3; 'sub_asset_class stays UNRESOLVED for equities until the CTO rules row ETFS_RIVALS-Z-S1 (still open)'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The CTO rules between the row's readings (a) and (b) before round 3 cuts the G4 cell that lands GICS, and the PRD line is amended to match the ruling.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S4",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The crosswalk indexes only Bloomberg-form identifiers, so the issuer's plain ticker, CUSIP, ISIN and SEDOL miss: 0 of 35 BASG positions resolve, and security_id is null across the issuer-sourced gold.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S4 (0.9.0_WK_ETFS_RIVALS~1): g-1.AC1 '2026-09-28: rows 35 resolved 0 unresolved 35'",
      "ETFS_RIVALS_DECOMP.md:123 places CUSIP coverage outside round 2 and names no round for it",
      "round-2 row ETFS_RIVALS-Z-W3-S9 (G5 keys on the Bloomberg id because G1's security_id is null): the gap now shapes a second table",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Place identity coverage for issuer-sourced positions in a named round and cell, either a crosswalk that carries CUSIP/ISIN/SEDOL forms or an authorised exchange-aware adapter. Raise the resolved-fraction floor (now 0.0, row W1-S5) with it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S5",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No contract names the stage status or marker rule for a page published deliberately as not-updated. The cell chose PARTIAL with no marker, and every guardrail threshold is PROVISIONAL (resolved floor 0.0).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S5 (0.9.0_WK_ETFS_RIVALS~1)",
      "round-2 row ETFS_RIVALS-Z-W1-S15 raises the same silence for a multi-fund page where some funds fail: the gap recurred in the next round",
      "ETFS_RIVALS_DECOMP.md:121 places FWD-9 (thresholds from real data) outside round 2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A PRD contract line (C-GUARDRAILS or the stage contract) names the status and marker for a published not-updated page, per fund and per batch. FWD-9's cell sets the thresholds from real data.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S3",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The opal-gateway stack and deploy cannot be reproduced from a fresh worktree. The plan needs two required variables with no default and two gitignored mcportal grant-writer build outputs. The mcportal gitlink (fa1ff9693b) is README-only, so deploy-to-ec2.sh refuses a freshly initialised tree. And the stack carries 2 untargeted pending changes from other work.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S3 (0.9.0_WK_ETFS_RIVALS~5): 'No value for required variable' mcportal_owner_key_claim, mcportal_owner_key (mcportal_grant_writer.tf:142,151)",
      "investigation row ETFS_RIVALS-Z-W5-S11: the gitlink README-only; the working checkout had to be the manifest's mcportal_commit a3bff71ffa",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The gateway stack's owner makes a fresh-tree plan and deploy reproducible: defaults or a documented source for the two variables, a build step for the grant-writer outputs, and a gitlink at the commit the live bundle was built from. Whoever owns the 2 pending untargeted changes applies or withdraws them.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S7",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The naming gate classifies any slashed literal whose first segment is a tier word as an S3 key, so a Lambda-tree-relative destination ('gold/etf_positioning_gold.py') is refused as OUT-OF-PATTERN. Splitting the literal passed it with the same built bytes.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S7 (0.9.0_WK_ETFS_RIVALS~5): NAMING REFUSE infra/aws/lambda/etfs-pipeline/rivalfunds_package.py:39",
      "rivalfunds_package.py:39 at HEAD carries the split form \"gold\" + \"/etf_positioning_gold.py\"",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The naming gate's owner decides between a carve-out for package-relative paths and keeping the refusal. A split literal that defeats the classifier is the workaround the gate now teaches every packager.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S12",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A worker cannot commit or deploy a deploy-only ref. owned-paths-validate (W5-S10) and the HALTGT identity gate (W5-S12) both read the worker's grant from HEAD of the tree they run in, and a ref cut at the deployed BASE carries no order by construction. The gateway leg therefore fell to the issuer's seat, and the worker-identity friction (W5-S2) is the same root.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S12: halt-gate-check.sh halt_gate_worker_issuer :165-188, safe-ec2-deploy.sh sets HALT_GATE_REPO_ROOT to the calling tree; 'Do NOT override this'",
      "investigation row ETFS_RIVALS-Z-W5-S10: owned-paths-validate.py:116-120 reads the grant at the committing tree's HEAD; the sibling release 288fa78c93 was committed under an audited override",
      "investigation row ETFS_RIVALS-Z-W5-S2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The CTO rules on one path for every deploy-only release: either the issuer commits and deploys the ref at its own seat as the standing rule (the de-facto path today), or the two gates resolve a worker's grant against the order-carrying tree. Either way, decomposition authors stop cutting deploy legs a worker cannot run.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S14",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-ec2-deploy.sh's jq rewrite of EC2_MANIFEST.json re-encodes escaped non-ASCII in unrelated entries as raw mojibake. On this device only a byte-surgical hand edit records a deploy safely.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S14 (0.9.0_WK_ETFS_RIVALS~5)",
      "the manifest's own opal-gateway release_note names the same class (row NFRA_OPALAI-Z-W2-S4): a second project hit it",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The wrapper's owner makes the manifest write preserve unrelated entries byte for byte (ASCII-escaped output, or an edit of the one service entry only).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W5-S15",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Deploy-only gateway refs 288fa78c93 (the rollback base of ETFS_RIVALS' ref) and 093fc247c6 are held only by branch refs, so pruning a branch exposes a recorded rollback target to GC.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W5-S15",
      "this seat ~04:2xZ: `git tag --points-at 288fa78c93` and `git tag --points-at 093fc247c6` print nothing; `git tag -l 'deploy-gw*'` lists only deploy-gw-etfs-rivalfunds-r1",
      "ETFS_RIVALS_DECOMP.md:124 calls it CTO-class and carries it in the drain-end read",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R1_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Tag both refs, and make tagging the deployed commit part of every deploy-only release (the ETFS_RIVALS ref is the one that was tagged).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  }
]
```
