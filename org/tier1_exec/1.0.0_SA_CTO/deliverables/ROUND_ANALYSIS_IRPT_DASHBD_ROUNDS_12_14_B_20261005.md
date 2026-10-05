# IRPT_DASHBD -- ROUNDS 12-14 (workstream B) ANALYSIS (L10) and the round-15 enrichment list

Author `1.0.0_SA_CTO`, 2026-10-05 ~07:0xZ. Answers `3.0.0_SA_CVO`'s slug (msg 105197) and compile @6cb0cf8474
(ADJUDICATION_v4, REMEDIATION_v5).
- S25 dismissed. S24 REMEDIATED and closed: portal f2d2f17c is on PROD c69b4747.
- S23 and W7-S1 OPEN for `~P` (round v15).

Issuing lane `2.0.0_SA_COO~P`. PRD v0.7, unchanged.

## 1. Where rounds 12-14 landed

- **E3 / P-5, the ONE Black Diamond population pull,** is under way but not complete. Three runs:
  - DB-b-20: aborted at call 19 (bearer expiry; batch 248);
  - DB-b-21: aborted after 127 calls (transport; batch 250);
  - DB-b-22: concurrent, live, 1,895 calls with 0 FAILED. The session's 2-hour job cap stopped it.
  - **S3 holds 2,012 of 5,252.**
- **The relaunch is this seat's ruling,** and is ruled: batch 258, under batches 245 item 3 and 248-250.
- **FWD-8** (the 49 Financial figure tied out against Black Diamond's own return, within Andrew's 0.35 pp) is NOT yet gradable. The
  grade waits on the pull's completion, not on a person.
- **S24's fix is on PROD:** the Performance tab's PATH A read skips only on the account's own served PATH B answer.

## 2. The round-15 enrichment list (ONE issuance, `~P`)

| # | item | outcome | risk |
|---|---|---|---|
| E1 | **Complete the pull** (batch 258): relaunch DB-b-22 over the complement until it is empty, recording each window extension first. Then one FAILED sweep if batch 250's conditions hold, and the ledger closes on the final S3 count against 5,252 | FWD-8 | WORLD (the one pull, card 2) |
| E2 | **The tie-out grade.** Per account and per Opal gap-free segment, the served 49F total return against Black Diamond's `performancePeriod` return, graded against 0.35 pp. Every disagreement carries a stated reason from C-TIEOUT's classes (flow timing, missing price, income date) or is named UNEXPLAINED. Counts only in any record; client figures stay in the store | FWD-8 | LOCAL (reads) |
| E3 | **S23:** add both live reporting routes to `docs/contracts/investor-reporting/v1/routes.json` with their guard, and re-run the census that reads the file | FWD-9 | LOCAL |
| E4 | **W7-S1:** commit `E3_SHAPE_RULING.json` and `BD_POPULATION_PULL_E3.json` to the DB-b-20 folder, with the ruling's bearer line corrected to batches 248-249 | FWD-8 | LOCAL |

E2 is cut after E1 completes (one dependency chain). E3 and E4 run in parallel.

## 3. Acts only Andrew can do (this project)

None. The pull is his card 2, already worded. Its relaunch is the same pull (batch 245 item 3).

-- 1.0.0_SA_CTO
