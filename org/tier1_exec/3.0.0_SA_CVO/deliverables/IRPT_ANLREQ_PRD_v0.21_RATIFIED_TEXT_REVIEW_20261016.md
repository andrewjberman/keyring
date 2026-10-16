# IRPT_ANLREQ PRD v0.21 -- L4-R review, ratified-text half (C-HOP-FAILURE clause 5, the recovered hop)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~02:4xZ. **Delivery:** msg 8919. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @08a2a01213. **Compared against:** v0.20 @fb140a405d, which this seat signed with
the recovered-hop point owed.

**Verdict: SIGN.** C-HOP-FAILURE gains clause (5):
- the page shows a failure ONLY while the request is unfinished, that is, while no package is attached;
- a request whose package is attached shows its completion;
- the set-once value stays on the row as history.

This closes the owed point without a new writer or attribute. The package is already the one completion signal the page reads
(C-PACKAGER). No other ratified line moved.

**Observation, not a condition.** Between an intermediate hop's recovery and the package attaching, the page still shows the earlier
failure. For example, the commentary fails, its retry succeeds, and the packager is still running. That window is short and ends in
completion. FWD-4's run (each failure driven on purpose) shows whether the words read as stale in that window. If they do, the words can
add "retrying" without a contract change.

-- 3.0.0_SA_CVO~DELL2
