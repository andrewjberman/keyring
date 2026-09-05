# NFRA_COMPEFFICACY -- ROUND-6 ANALYSIS (L10, the CTO's read of the slug; the project's close under Andrew's "a") -- 2026-09-04 ~07:3xZ

**Reader:** `1.0.0_SA_CTO` (the single router; L4 owner). **Slug:** `3.0.0_SA_CVO` message 94126 -- record @f4b41b1c20 (adjudications
C-S1..C-S6, S39, REMEDIATION_v1.md S31/S35/S36 in v3 form) and @22388f7195 (the closing cells: `deliverables/3.0.0_SA_CVO/CE-q-1.seven-answers.md`,
`CE-pass-1.rollup.md` v2, `CE-g-4.codex-rail-design.md`; `ledger/STEP_LOG.3.0.0_SA_CVO.round6.json`). **Precondition, the gate's own line:**
25 task orders at HEAD on both roots, 0 open; 37 investigation items across 3 channel files, 0 undispositioned. **Word:** Andrew at the
`2.0.0_SA_COO` terminal ~07:0xZ, "a" (@6d1e252f3c): no v3 issuance, no worker spawn; the project closes on its CVO limbs, then this
analysis. **CTO adjudication @6b21ce6010:** CE-g-4 HELD on ruling 2(b), non-blocking; FWD-9 grades NOT_EVALUATED until a Codex seat
exercises the rail. **Answer:** the ROUND-N ANALYSIS, not an addendum -- no outcome is unserved by a cell and no cell is invalidated. Under
"a" there is no recut: what cannot close here is CARRIED with its owner named, and the close's grades say so.
**Push state at write:** LOCAL; origin/CLOUD @351f309e0a (ls-remote read this session).

## 1. Per outcome (PRD v0.7 FWD-1..10): the expectation, what the run delivered, what the channel says, and what the close will read

The grade itself is the second read (`ledger/COMPLETION_GRADES.round6.json`, after the COO's `COMPLETION_REPORT.round6.json`), against the
exercised artifact, never this table. This table states the expectation the grade is read against.

| outcome | DONE WHEN | delivered at HEAD | channel / adjudications | the close will read |
|---|---|---|---|---|
| FWD-1 the list | APPLIED | PRD s.7 T-1..T-24 + G-1..G-4; the two non-tools recorded as such | -- | REALIZED on the PRD |
| FWD-2 one account per tool, one shape | EXERCISED | 25 orders terminal; every per-tool deliverable in the `deliverables/<serial>/` shape; the CVO read each at L9 | CE-pass-1 v2 read 11 deliverables at full width | REALIZED if the CVO's read of the last account is on the record (it is, C-S5 and the roll-up) |
| FWD-3 what it counted, what it could not see | EXERCISED | T-cells' disclosure lines; G-2's VINTAGE line on comp-blast and comp-trace (G2-AC1..AC7); comp-find's denominator/floor lines | G2-AC1 PASS, G2-AC3 PASS | REALIZED on a real run's output read against its disclosure (G-2's instance @65a85beb44) |
| FWD-4 every tool in one of three states, read by Andrew | EXERCISED | every tool's state is on the record (cleared / retired / short-listed candidates) | CE-mrq-1 in flight at Andrew (PRD s.5) | **NOT_EVALUATED** -- "read by Andrew" is his act at the sitting; the record is ready for it |
| FWD-5 his seven questions answered | APPLIED | CE-q-1.seven-answers.md @22388f7195 (CVO authors) | -- | REALIZED once the CTO LANDS the text in the PRD (this seat's act, PRD v0.8; section 3) |
| FWD-6 the passcraft findings used up | EXERCISED | CE-pass-1 v2: 48 findings, FIXED 9 / NOT-FIXED-owner-named 24 / RECORDED 11 / ROUTED-TO-ROW 9, UNCLEAR 0; the last disposition read by the CVO, which fixed nothing | -- | REALIZED (the non-fixer read is on the record) |
| FWD-7 the cloud-compile brief addressed, not parked | APPLIED | G-2/G-3 carried to NFRA_CLDGRPH's CG-s-8/CG-s-9/CG-x-7 at PRD v0.7; the rest of the brief IS NFRA_CLDGRPH | -- | REALIZED (each ask has an owner in the plan) |
| FWD-8 the short list, ratified, a seat started from it | EXERCISED | the draft @ac52464f82; v2 against s.7's dispositions owed by the CVO after the sitting | -- | **NOT_EVALUATED** -- ratification is Andrew's (PRD s.5), and no seat has started from an unratified list |
| FWD-9 a cleared tool stays cleared from any seat; the fix on the shared branch | EXERCISED | comp-blast's budgeted contract exercised from the CVO's seat (C-S1, a seat other than the fixer); every fix LOCAL under the push hold (LD-0522); CE-g-4's design half landed, exercise HELD | C-S1 GRADUATED and CLOSED; CE-g-4 per @6b21ce6010 | **NOT_EVALUATED** -- two limbs no artifact covers: "on the shared branch" (the push is Andrew's word) and the Codex rail's exercise (a Codex seat is Andrew's word) |
| FWD-10 a verdict-bearing tool never returns clean from a partial run | EXERCISED | T-24's Rule-T form (AC2/AC5 UNCOMPUTABLE-BY-CONSTRUCTION, disclosed); comp-blast rc 3 at budget on a BEHIND graph (C-S1); comp-heat has no budget at all (T20-AC4 FAIL) | C-S5 grade record | **NOT_EVALUATED** -- the ACCEPT clause's denominator is "every marquis tool whose rc carries a verdict", and the marquis list is not ratified (FWD-8); and the one measured failure (comp-heat) stands unfixed under "a" |

**Coverage verdict:** 10 of 10 outcomes have a cell; none is unserved; no `DECOMP_INVALIDATING` row. The close will read six REALIZED and
four NOT_EVALUATED -- FWD-4, FWD-8, FWD-9, FWD-10 -- and every NOT_EVALUATED waits on an act only Andrew can make (his read at the
sitting, the marquis ratification, the push word, a Codex seat), not on any seat's queue. `CLOSED` is mechanical on every grade
REALIZED and therefore does not follow; `ROUND_CLOSE` stands. That is the honest end-state of "a", not a stall.

## 2. The six things the slug names, each routed

1. **S35 (C-S3, GRADUATED, ARMED, owner `2.0.0_SA_COO` on this route) -- `comp-trace` accepts `--budget` and ignores it; a caller expecting
   comp-blast's contract gets an unbounded local rebuild (66.9 s measured).** Under "a" no cell is cut here. **Route: CARRIED to
   `NFRA_CLDGRPH` CG-s-8**, as G-2/G-3 were at PRD v0.7 -- the local rebuild path's retirement makes the flag honest by construction, and
   CG-s-8 is in `2.0.0_SA_COO~A`'s round-4 issuance (last, per R7). The row's disarm lands with CG-s-8's instance; the help string's
   INERT disclosure (cli.py:1802-1809) is the interim. The CVO's row act: `DISMISSED_WITH_REASON` here naming CG-s-8, or the ARMED
   row carried with its owner re-seated to `2.0.0_SA_COO~A` -- the CVO's choice of form.
2. **T20-AC4 FAIL -- `comp-heat freshness` with no path scores the whole repo (an 8.3 MB snapshot) and accepts no `--budget`.** The T-20
   lane is dead and "a" cuts nothing. **Route: NOT-FIXED, owner `0.8.0_AE_CloudComp` (the tool's home), waits for a pass** -- and one
   REC for Andrew's FWD-4 read at the sitting: comp-heat has 0 runs and its only consumer returns `{}` before reaching it (CE-q-1);
   RETIRE is the cheaper true state, and it removes this FAIL from FWD-10's denominator by his ruling rather than by a fix.
3. **S39 (C-S6, DISMISSED_WITH_REASON, owner named) -- a dead rebuild winner's empty mkdir-mutex beside a 6.5 MB `.rebuild.tmp.wal`,
   the steal path (`_canonical.py:204-217`, 1800 s) unexercised.** The engine and its mutex are `0.8.0_AE_CloudComp`'s via NFRA_CLDGRPH
   CG-s-8. **Route: CARRIED to CG-s-8** -- the local seam this lock belongs to is what CG-s-8 retires; the steal path's wait on an
   unbudgeted default query is a fact CG-s-8's worker records before the retirement. No row is filed here; the CVO's S39 names it.
4. **comp-which F2 (a syntactically valid, non-existent gold-script id routed with a confident 2.00 score) and comp-find F1 (`--version`
   becomes a search pattern).** One-flag fixes on the two tools every seat uses; "a" cuts nothing. **Route: NOT-FIXED, owner
   `0.8.0_AE_CloudComp`, FIRST TWO ITEMS of the next pass** (a maintenance issuance outside this project, or this project's next round if
   Andrew reopens it); F2 is a wrong-object hazard on the router itself and is named to Andrew in the report of this analysis.
5. **S34 (C-S2, DISMISSED_WITH_REASON) -- a fresh worktree carries no gitignored runtime graph (217 MB), so a graph-touching order's
   worker starts TOOL-FAILED.** **Route: `/dispatch`, `2.0.0_SA_COO`** -- the spawn step names or copies the gitignored runtime state a
   graph-touching order needs, or the order's worker face says the state is absent and what the criterion reads instead. Procedure at
   the COO; carried in the message that hands this analysis over.
6. **CE-mrq-1 stays at Andrew** (PRD s.5); the CVO's draft v2 against s.7's dispositions after his sitting. Nothing routed.

## 3. The CTO's own acts this analysis names

- **FWD-5's landing:** CE-q-1's seven answers are the CVO's text; the CTO lands them in the PRD (v0.8, section 5 "the questions answered",
  header `prd_version` bumped, the L4 notifier to the COO) -- this seat's act now, no outcome or manifest row changed.
- **The decomposition's CE-q-1 text** ("trace is a subset of BLAST", the superseded v0.4 read) and the stale `status now` column (v0.2.8's own
  note) are `2.0.0_SA_COO`'s L5 bookkeeping, named, not routed.
- **The close:** `2.0.0_SA_COO` writes `ledger/COMPLETION_REPORT.round6.json` (one row per outcome, cells, instances, COVERED/UNCOVERED with
  denominators -- CE-g-4's exercise reads UNCOVERED per @6b21ce6010); `1.0.0_SA_CTO` then reads the exercised artifacts and writes
  `ledger/COMPLETION_GRADES.round6.json` as section 1 expects. `dep_stage: ROUND_CLOSE` on this commit.

## 4. Handoff

This file and `surprise-channel/remediations/REMEDIATION_v1.md` (@f4b41b1c20) go to `2.0.0_SA_COO` in the CTO's one message of the round.
No issuance follows (Andrew's "a"); the COO's next act on this project is the completion report.
