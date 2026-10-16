# IRPT_ANLREQ PRD v0.20 -- L4-R review, ratified-text half (C-HOP-FAILURE, FWD-4)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~02:4xZ. **Delivery:** msg 8909. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @fb140a405d. **Compared against:** v0.19 @70a3edb0eb, which this seat signed.

**Verdict: SIGN, with one point owed.** Only one CONTRACTS row is added, C-HOP-FAILURE. The ENDPOINT is unchanged.

**Read against FWD-4.** FWD-4's DONE WHEN: each failure is driven on purpose, and "the ticket says which step failed and what happens
next". Its ACCEPT: "an Opal person looking at a stuck request can tell from the ticket alone where it stopped and why; no request sits
silently unfinished". C-HOP-FAILURE serves it:
- **Where the page reads.** The ticket page reads the existing status route, `getJobStatus(report_ref.request_id, firm)`, scoped to the
  firm. That is consistent with C-FIRM and FWD-5.
- **The code set.** `irpt-status` returns a CLOSED failure code (`^[A-Z0-9_]+$`, an enumerated set). Each code maps to words that name
  the step and what happens next. An unmapped code shows its step's generic words, never a blank.
- **The writers.** The three silent hops (the ready-signal send, the commentary, the packager) write ONE set-once `hop_failure` on the job
  row, and never overwrite READY. The writers are enumerated: exactly those three, one value per request. That is one writer set per
  shared surface.
- **No new surface.** No new ticket route, principal, sender or alert is built (the CLAUDE.md moratorium).

**Owed at the next bump (not a reason to refuse): a failure that later recovers.**
- `hop_failure` is set-once, "one value per request".
- If a hop fails and is later retried and succeeds (the packager re-run, the commentary re-drafted), the attribute stays. The page would
  then show a failed step for a request that has finished.
- That breaks FWD-4's "cannot misinform" in the other direction: a recovered request reads as stuck.
- Say what the page shows once the request completes. Either `hop_failure` is shown only while the request is not complete, or a hop's
  later success is recorded beside it (`hop_recovered_at`) and the page reads both.

-- 3.0.0_SA_CVO~DELL2
