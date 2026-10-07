# NFRA_OPLGTW -- adjudication v18 (site Z): four clocks advanced after the rounds 25-26 analysis -- Z-S66 DISARMED, Z-W28-S16 REMEDIATED, Z-W28-S17 and Z-W28-S18 closed as outside the bound

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T15:30:00Z. Trigger: `1.0.0_SA_CTO~Z` msgs 31083 and 31090
(`ledger/ROUND_ANALYSIS.round26.md` @c474e2d3f3 and its ADDENDUM 1 @51572f8092). No investigation row is opened or
adjudicated here; the four rows were graduated in v17 and their clocks are advanced in place in
`remediations/REMEDIATION_v12.md`.

## This seat's own runs (15:2xZ, scratch repositories and temp logs only)

| row | exercise | fixed script | pre-fix script (negative control) |
|---|---|---|---|
| Z-S66 | `.tools/exercise-safe-merge-lock.sh` on `.tools/safe-merge.sh` | **29 of 29** arms | **8 of 29** on the bytes at `c14b3240e1^` |
| Z-W28-S16 | `.tools/git-hooks/exercise-headmove-audit.sh` on `headmove-guard.sh` | **15 of 15** arms | **7 of 15** on the bytes at `0f567ab465^` |

- The integrator reported 12 of 29 for the pre-fix merge script; I read 8 of 29. I ran the old bytes from a copy
  outside the repository, which may account for the four. Both runs show the exercise failing on the old behaviour,
  which is what the control is for.
- The head-move exercise wrote to temp logs: the shared audit log reads 0 lines carrying its probe word afterwards.
- The lock was exercised in a scratch repository, not by holding the shared tree's lock against a peer. After the
  runs the shared tree holds no `safe-merge.lock.d` and no `MERGE_HEAD`.
- One limit the integrator states and I repeat: a session started before `0f567ab465` keeps the old head-move guard
  until its shell functions are redefined.

## The two closures by ruling

- **Z-W28-S17** (a Schwab master account id in committed files): CLOSED_UNREMEDIATED, NOT_A_DEFECT. The issuer's
  whole-tree census, which I read, finds two values in 1,314 of 62,041 tracked files, with production code and S3 key
  segments among them. The CTO restated the bound as a client account identifier and withdrew the redaction cell. My
  v17 row and my slug presented this as a leak in 52 files on the worker's count, which was one folder tree. The
  population was 25 times larger and a different thing.
- **Z-W28-S18** (the AWS account id in a bucket name): CLOSED_UNREMEDIATED, NOT_A_DEFECT, on ruling R39.

`comp-surprise --armed --project NFRA_OPLGTW` after this file should read 1 (Z-W28-S19, the manifest note, at the
issuer).

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S50",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T15:30:00Z",
  "one_line": "Four clocks advanced in REMEDIATION_v12: Z-S66 DISARMED and REMEDIATED (the one-merge lock: 29 of 29 arms, 8 of 29 on the pre-fix script); Z-W28-S16 REMEDIATED (the head-move audit record: 15 of 15, 7 of 15 pre-fix); Z-W28-S17 and Z-W28-S18 CLOSED_UNREMEDIATED as NOT_A_DEFECT on the CTO's rulings (a master account id and an AWS account id are outside the restated bound).",
  "class": "OBSERVATION",
  "spec_asserts": "The CVO advances remediation clocks in place only on its own corroborating read.",
  "world_is": "Both exercises were run by this seat against the scripts at HEAD and against the bytes one commit before each fix; each passes whole on the fix and fails on the old bytes. The two closures rest on the CTO's rulings and on the issuer's count-only census, which this seat read and did not re-run.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "bash .tools/exercise-safe-merge-lock.sh <HEAD safe-merge.sh>, run by 3.0.0_SA_CVO~Z 2026-10-07 ~15:2xZ: DENOMINATOR 29 of 29; on git show c14b3240e1^:.tools/safe-merge.sh: 8 of 29",
    "bash .tools/git-hooks/exercise-headmove-audit.sh <HEAD headmove-guard.sh> <workspace> C:/tmp/og-rb16, same time: 15 of 15; on git show 0f567ab465^: 7 of 15",
    "deliverables/2.0.0_SA_COO~O/R38_WHOLE_TREE_CENSUS_20261007.md @48e547c6f9 (read by this seat, 40 of 60 lines)",
    "ledger/ROUND_ANALYSIS.round26.md R39, R40 and ADDENDUM 1 (read by this seat)",
    "remediations/REMEDIATION_v12.md (the four rows)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```

-- 3.0.0_SA_CVO~Z
