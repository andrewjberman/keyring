# NFRA_OPLGTW rounds 13-14 -- HELD graduations (draft, NOT a channel carrier)

Author: 3.0.0_SA_CVO~O. Written: 2026-10-03T18:40:00Z. State: HELD.

Why held: `.tools/surprise-row-gate.py` refused these 5 remediation rows, because a new remediation row IS the slug, and
1 of 78 orders is not terminal at HEAD: `NFRA_OPLGTW.TO-OG-v-8.pilot-walkthrough-grading-r2.md` [staged], round 3, held
on its gates (Andrew-direct 2026-09-03, LD-0521: "We do not route until the job is over"). No override is used. The
file sits outside the surprise-channel paths, so nothing here is routed. The 5 items stay UNDER_INVESTIGATION until
OG-v-8 is terminal or the CTO rules. Then this seat re-measures them and lands the graduation below as a new
adjudication row and `REMEDIATION_v3.md`.

## Adjudication row to land (draft)

```text
{
  "id": "NFRA_OPLGTW-Z-C-S16",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~O",
  "surfaced_at": "2026-10-03T18:20:00Z",
  "one_line": "Round 13-14 L8: 5 rows are GRADUATED as real defects still live, all OPEN in REMEDIATION_v3.md. One needs a CTO ruling (Z-W15-S25, the grant-writer build source), and four are tool or check repairs (Z-S46, Z-W17-S3, Z-W16-S5, Z-W15-S31).",
  "class": "OBSERVATION",
  "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
  "world_is": "Z-W15-S25 with Z-W17-S3: OG-tf-1 ended `failed` at step 4 (CONTENT-DIFF, 3 of 11 grant-writer files). Z-S47 disarmed the hazard because no order applies the root untargeted, but the build-source choice it routes to the CTO is still open, and .build/staged is still untracked and not ignored. Z-S46: the lint half is fixed (@453c6430ec, CTO ruling 3). The second half is live: safe-commit.sh:877-878 unstages only SRGATE_FILES, with errors discarded, then prints 'Commit aborted; files unstaged.' This seat's own refused commit on 2026-10-02 ~15:3xZ left adjudications/ADJUDICATION_v4.Z.md (NFRA_OPALAI) staged as `A` under that message. Z-W16-S5: the p95 is +72.5% over a 5 h window that no criterion grades; it needs a full-window re-measure on af2d762970. Z-W15-S31: deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32 still expects 48 keys while the host holds 50, so arm 4 reads FAIL on a correct host.",
  "adjudicates": [
    "NFRA_OPLGTW-Z-S46",
    "NFRA_OPLGTW-Z-W15-S25",
    "NFRA_OPLGTW-Z-W17-S3",
    "NFRA_OPLGTW-Z-W16-S5",
    "NFRA_OPLGTW-Z-W15-S31"
  ],
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S46",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S25",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S3",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W16-S5",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S31",
      ".tools/safe-commit.sh:877-878",
      "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32",
      "task-orders/NFRA_OPLGTW.TO-OG-tf-1.tf-root-fresh-worktree.md last <status>: failed (step 4)",
      "remediations/REMEDIATION_v3.md"
    ]
  },
  "disposition": "GRADUATED"
}
```

## Remediation rows to land (draft)

```text
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
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S47"
    ],
    "remedy": "OPEN: rule the build source: either deploy HEAD's build deliberately in a separate apply cell, or pin the archive to a released build. OG-tf-1's AC1/AC2 are re-cut after the ruling. Disarmed meanwhile by Z-S47, because no order applies the root untargeted.",
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
    "id": "NFRA_OPLGTW-Z-W17-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grant-writer's .build/staged directory is untracked and NOT gitignored, and the layer zip is built from PyPI wheels rather than a repo file. Both contradict the order's premise, and a staged build can therefore enter a commit or a plan unseen.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W17-S3"
    ],
    "remedy": "OPEN: a cell whose <paths> include infra/aws/lambda adds the ignore line, or the build moves out of the tree. This rides with the Z-W15-S25 ruling.",
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
    "id": "NFRA_OPLGTW-Z-S46",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit prints 'Commit aborted; files unstaged.' after a gate refusal while declared paths stay staged in the shared index. Z-S46: a gate2 refusal (rc 128) left 36 paths staged. This seat, 2026-10-02 ~15:3xZ: a surprise-row-gate refusal left NFRA_OPALAI adjudications/ADJUDICATION_v4.Z.md staged as `A`. The surprise-gate branch unstages only SRGATE_FILES, with errors discarded. A staged leftover rides into the next seat's commit.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S46",
      ".tools/safe-commit.sh:877-878 (for each SRGATE_FILES entry: git reset -q HEAD -- <file>, stderr discarded, failure ignored)"
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
      "deliverables/0.9.0_WK_NFRA_OPLGTW~16/CAPACITY_R4.json ac4"
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
      "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/tr.AC1.sh:7,32"
    ],
    "remedy": "OPEN: the issuer amends arm 4 to the live key count, or to a count read from the template's printf so that the next key addition cannot stale it again.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v3"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
