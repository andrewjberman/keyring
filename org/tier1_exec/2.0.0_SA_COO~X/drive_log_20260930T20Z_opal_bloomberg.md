# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 20Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 20:02Z | L10 | 25 | the CTO's round-25 analysis `19207dfb83` (msg 27357): round 25 CLOSED; round 26 is 5 cells led by `Z-S71`; ruling 2 (series median), ruling 3 (`case_rule` refuses the mixed input), ruling 4 (every count states its key population) |
| 20:1xZ-20:5xZ | L6 | 26 | ONE issuance `65ed3968c1`, merged `f40d29ede1`, as below; 4 workers spawned (`~5` after its worktree finished) |
| 20:5xZ | L7 | 26 | the 19Z log committed; workers in flight |

**The issuance:**
- ab-1 dossier slash-safe (`~1`, worker-light);
- ab-2 series-median units (`~2`);
- ab-3 `case_rule` mixed input (`~3`, worker-light);
- ab-5 BP/NG denomination (`~5`);
- ab-4 is the issuer's WORLD act after them.

**Checks dry-run at base, each FAIL as designed:** ab1 `raw`; ab2 31 UNRESOLVED over 100 keys; ab3 778.57; ab5 population 6 on 2.

**Found at the cut:** the scoped API recomputes the case per request from the DEPLOYED `case_rule` (`scoped_amgt.py:3195`), so ab-3
reaches `/thesis` only with AMGT_RESAPP's redeploy.

**A correction recorded:** round 25's "375 pointer units measured" is 365 measured plus 10 to UNRESOLVED.

## Compiler Tools

- `ab1_check.py`, `ab2_check.py`, `ab3_check.py` (a write-capturing `stage_derive`) and `ab5_check.py`.
- Gaps:
  - the gate2 seating lint misparses `0.9.0_WK_AMGT_CORPUS~n` as `0.9.0_WK_AMGT` (ANNOUNCE mode, not blocking);
  - a stray `C:\OPALBL~1\x.txt` was written by mistake again and removed.
