# AMGT_HARVST -- round 99 remediations (dell1)

<sweep_watermark>2026-10-20T16:28:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-20T16:28:00Z. Graduated at ADJUDICATION_v94 (C-S79), 6 rows:
- S67 and S68 are a served-data stall and an unexplained daily skip, owned by 2.0.0_SA_COO~W1.
- W183-S10, S11, S16 and S17 are ARMED instrument blind spots, whose owner and disarm owner is 0.0.0_AB_MSTR, per the round-99 packet s.3.

```json
[
  {
    "id": "AMGT_HARVST-D1-S67",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gold chatter tables are not rebuilt by any schedule: s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/ has 11 partitions, newest date=2026-10-08 (read by this seat 2026-10-20 ~16:2xZ). That is 8 trading days behind 2026-10-20. The dell1 runner collects bronze and silver only; the gold writer lib/research/harvest/publication_gold.py has no scheduled caller (the issuer's read).",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S67",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "A scheduled gold rebuild of the chatter and article-mention tables, on their own clock, under its own pair (CLAUDE.md: production pipelines MUST be scheduled). Close when: a scheduled fire, not an ad-hoc run, writes the trading-day-current chatter_daily partition, and it is read in S3.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v99",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v99"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-S68",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The first scheduled dossier fire (ECS task bc80a834..., 2026-10-20) stopped three names at the valued-rows guard: BZLFY_US_Equity 55 vs 56, PBR_US_Equity 55 vs 56 and TSM_US_Equity 53 vs 54. None of the three has an as_of=2026-10-20 object (this seat's S3 read: 92 of 92 written keys, none of the three). Only PBR's dropped row is named (cn-2: typecast|BEST_DPS|FY1), and it was not re-measured on this fire.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S68",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "Name the dropped valued row and its cause for BZLFY and TSM (the cn-2 method), and rule whether a one-row guard STOP is the right limit for a daily fire. Close when: each stopped name's cause is named, and the next scheduled fire's census shows the ruled outcome.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v99",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v99"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-D1-W183-S10",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The commit path grades no CodeBuild buildspec: safe-commit printed 'commit-gate checked 0 of 1 file(s) -- NOTHING WAS CHECKED' for the cn-5 amendment-5 buildspec fix. The defect it missed, an unquoted colon-space YAML list item, failed the live build (row S65).",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W183-S10",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "The commit path parses a staged buildspec.yml (YAML load at minimum), or names it as ungraded loudly. Close when: a staged malformed buildspec is refused or flagged by the commit path (a positive control).",
    "owner": "0.0.0_AB_MSTR",
    "round": "v99",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR",
      "round": "v99"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-20T17:11:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-D1-W183-S11",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The pre-commit risk reflex answers PARTIAL_OR_BLIND on a linked worktree ('build guard refused: linked worktree', 'scanned 0 of 1 file(s)'), and safe-commit still lands the commit. Every worker commit in a linked worktree is unreflexed.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W183-S11",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "The risk reflex reads a linked worktree, or safe-commit treats PARTIAL_OR_BLIND as a named hold. Close when: a linked-worktree commit of a risky diff is graded, not blind (a positive control).",
    "owner": "0.0.0_AB_MSTR",
    "round": "v99",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR",
      "round": "v99"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-20T17:11:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-D1-W183-S16",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "safe-commit's client-data check printed WARN: the hashed account-id list is ABSENT on dell1, so commit 0bf0e821b4, and every dell1 commit, is not checked for client account ids.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W183-S16",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "The hashed account-id list is provisioned on dell1, or its absence is a hold. Close when: a dell1 safe-commit reads the list present and flags a planted account id (a positive control).",
    "owner": "0.0.0_AB_MSTR",
    "round": "v99",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "0.0.0_AB_MSTR",
      "round": "v99",
      "closure": {
        "reason": "ACCEPTED_BY_RULING",
        "pointer": "org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md@c7381f6135 (ADVI_COTBKF-D1-S6: the dell1 account-id scan is unprovisioned BY DESIGN on Andrew's 2026-10-09 word; CTO no-restore, msg 8731)"
      }
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-20T17:11:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-D1-W183-S17",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The pre-commit risk reflex answered PARTIAL_OR_BLIND for the cn-5 tf diff: the danger map was 92.3h STALE and the build guard refused a linked worktree, so a Terraform diff with a destroy hazard (row W183-S14) committed unreflexed.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-W183-S17",
      "adjudication row AMGT_HARVST-D1-C-S79 (ADJUDICATION_v94)"
    ],
    "remedy": "The danger map is refreshed on its own clock, and a stale map is a named hold for a .tf diff. Close when: the danger map's age reads within its bound on dell1, and a .tf diff is graded against it.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v99",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v99"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    }
  }
]
```

-- 3.0.0_SA_CVO~DELL1

## Disposition lines (appended, 3.0.0_SA_CVO~DELL1, dell1, 2026-10-20T16:45:00Z)

- `AMGT_HARVST-D1-W183-S10`: the disarm is NOT written; the clock stays ARMED. The disarm owner 0.0.0_AB_MSTR~DELL1 (msg 8717) landed a YAML load of buildspec*.yml in `.tools/commit_gate_runner.py` (6f17a0569b, in HEAD and on origin/box/dell1), with a ScannerError negative control. The decisive control fails: the buildspec that failed the live CodeBuild run (row S65), `git show d8f3448b9b:infra/aws/harvest/dossier-refresh/buildspec.yml`, reads `OK: pre-commit gate clean for 1 of 1 file(s)`, rc 0, on this seat's run of `python .tools/commit_gate_runner.py <file>`. That file is valid YAML: `yaml.safe_load` succeeds, and its two defective items parse as one-key MAPPINGS (`{'echo "SMOKE': ...}`, `{'echo "Push complete': ...}`), not strings. CodeBuild refuses that shape (YAML_FILE_ERROR), and a YAML load cannot see it. Close condition, restated to the row's own defect: the commit path refuses a buildspec in which any `phases.*.commands` item is not a string, with the d8f3448b9b file as its positive control.

-- 3.0.0_SA_CVO~DELL1

## Disposition lines (appended, 3.0.0_SA_CVO~DELL1, dell1, 2026-10-20T17:11:00Z)

- `AMGT_HARVST-D1-W183-S10`: DISARMED and REMEDIATED. bff9f2d966 (0.0.0_AB_MSTR~DELL1, in HEAD) refuses a non-string `phases.*.commands` or `finally` item. This seat ran `python .tools/commit_gate_runner.py` on four files: the S65 buildspec as it failed CodeBuild (`git show d8f3448b9b:...`) reads rc 1; the repaired HEAD buildspec reads rc 0; a valid sample reads rc 0; a mapping-item sample reads rc 1. My earlier refusal (bcb40719f9) is answered.
- `AMGT_HARVST-D1-W183-S11`: DISARMED and REMEDIATED. 97cb3abc4c (in HEAD) makes `resolve_risk_map` read the main tree's map when a linked worktree's own map is stale. This seat drove that function in a fresh linked worktree at HEAD (C:/dev/cvo-s11-ctl), treated as non-sparse, with its own committed map STALE and a refusing rebuild. NEW code reads "linked worktree: own map STALE; read the MAIN tree's map ... no build here"; the pre-fix code (97cb3abc4c^) reads "NOT-DECIDABLE: build guard refused: linked worktree", which is the row's blindness. The cure holds only while the main map is fresh (23.8h old at this read, not stale), so that half stays with W183-S17, which stays ARMED.
- `AMGT_HARVST-D1-W183-S16`: DISARMED and CLOSED_UNREMEDIATED, BY DESIGN on Andrew's 2026-10-09 word (c7381f6135) and the CTO's no-restore ruling (msg 8731). Dell1 commits stay unchecked for client account ids; that is the declared limit.
- `AMGT_HARVST-D1-W183-S17`: still ARMED. The danger-map refresh has no schedule (MSTR~DELL1 msg 8726).

-- 3.0.0_SA_CVO~DELL1
