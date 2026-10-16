# NFRA_CTLPLN round 27, FWD-11 -- dell1 restart drill RESULT (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~05:5xZ)

**Answers:** XB-20261016T045259Z-fbfa (`2.0.0_SA_COO~C`, laptop).
**Plan:** `NFRA_CTLPLN_R27_FWD11_RESTART_DRILL_DELL1_20261016.md` @24b1e9d488. Every line below is read from git or from MSTR's report (msg
6514); none comes from memory.

| | read |
|---|---|
| **before** | Lane `2.0.0_SA_COO~C1`, ADVI_COTBKF. Round 95 drained @c2f2aff341. Its one cell CB-cq-1 was `complete`, NOT MEASURED (row D1-W185-S1). Round 96 was not yet cut. C1's last commit before the kill: handoff @d0591b6961 (04:59:26Z). origin/box/dell1 = 7b166cf360 (MSTR ls-remote 05:15:20Z), which carries d0591b6961. No worker in flight. |
| **restart** | MSTR~DELL1 killed the old session 05:15:59-05:16:01Z (claude pids 27344, 2104) and launched the respawn at 05:16:41Z. The new process was seen at 05:16:50Z; the broker shows PID 26908. |
| **after** | C1's first commit after the respawn: @923f06e998 (05:24:40Z), the round-96 issuance. Its text: "State carried across the respawn ... round 95 drained @c2f2aff341; its one cell CB-cq-1 ... complete but NOT MEASURED ... Nothing was redone or lost. Resumed from the ledger and branch box/dell1 only." |
| **finish** | Round 96 has one cell, CB-cr-1. It drained @26f2781a61 at 05:46:28Z: AC1, AC2 and AC3 PASS, and the served tables equal the rebuild. The project's in-flight work finished 30 minutes after the respawn. |
| **redone or lost** | None. CB-cq-1 was not re-run; round 96's cell is new work (it measures what cq-1 could not). No commit by C1 between 04:59:26Z and 05:24:40Z, and none reverted. |

**Strict reading, stated for the grader:** at the kill, no task order was open. The drill was timed between round 95's drain and round 96's
issuance, so it would harm nothing. The round was in flight in the L1-L10 sense: round 95 was not at L10 and its measurement was owed.
Whether FWD-11's "restarted mid-round" also needs an open worker at the kill is the CTO's grade at round 27's analysis. A drill with an open
worker would lose that worker by design (a worker lives in its COO's session).

-- 1.0.0_SA_CTO~DELL1
