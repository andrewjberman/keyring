# ROUND 12 -- CELL SKETCH (scratch, 2.0.0_SA_COO~W, written 22:3xZ while round 11 sits at L9)

**NOT A CUT.** No round-12 order exists until `3.0.0_SA_CVO~W` files the round-11 slug and `1.0.0_SA_CTO~W` answers it with a
ROUND_ANALYSIS or a PRD addendum (LD-0521: a cut before the slug deadlocks round 11's L10). The decomposition is this lane's at L5
and is written against that analysis, not against this sketch. Every chain below may be re-shaped or dropped by it.

Sources already in hand: ROUND11_PACKET.md section 5 (items 1-11, 8b-8e), the CTO's L10 pre-read candidates 1-16, card 16
(msg 23266), and the browser half's findings.

## Chain D -- the deployed plane catches up with HEAD (sequenced; every act needs a fresh never-widen co-sign)

1. **D1 adapter redeploy from HEAD.** Z-S107: the served adapter was built from `5ae785828e`, before rj-12's `read_posture` landed,
   so the Posture tab prints the comparable's key and "packs are not carried". The cell rebuilds from HEAD and re-reads live,
   asserting `comparable_name` and per-key `packs` present on the served object, and the tab's coverage lines rendered from them.
2. **D2 the Model tab reads model blocks from the pool.** W19-S13 and packet 8b: `MODEL_BLOCK_ROOT` is repo-relative and absent in
   Lambda, while the pool already holds `derived/model_block/<key>/<timestamp>/model_block.json`. The cell adds the adapter read of
   the newest block per key AND the `derived/model_block/` prefix on the adapter role, under the same co-sign; the live read asserts
   fiscal and header figures non-zero for a name that has a block, and ABSENT-explicit for one that does not.
3. **D3 Divergence D, per card 16.** Bloomberg only: `F_cons` from BEST_ESTIMATE_FCF, dispersion per tick-1 ruling 3. Needs D2's
   model NTM FCF on the served plane. Seeking Alpha is display-and-flag beside the Bloomberg analyst count, never a score input.

## Chain M -- C-TAB-METRIC, one headline metric per tab (Andrew-direct, ruled principle)

4. **M1 the metric record and its store.** `{metric_id, definition, unit, absolute, percentile, pool_n, pool_vintage, state, reason}`;
   append-only in `s3://opal-data-harvest` at `metrics/v1/{metric_id}/{security_key}/{as_of}.json` with a dated pool snapshot at
   `metrics/v1/{metric_id}/_pool/{as_of}.json`. The pool is the companies ANALYZED in the Security Analysis database that carry the
   metric. Below a declared floor the percentile is ABSENT with `pool too small (N)` and the absolute still renders. NOTE: the write
   prefix is a new grant on whichever role writes it -- co-sign, and it is a WRITE to the harvest bucket, so the cell states that the
   harvest COLLECTION mechanism and cadence remain Andrew's and are untouched.
5. **M2 management tenure as the first metric.** The absolute exists (BA 2.58, COST 5.06, HD 4.68, SAP 4.04; BABA none). The pool
   file carries only `pool_avg_tenure_years` 4.08 and no distribution, and its denominator says `names_with_roster 5` where 4 names
   contribute -- the cell counts CONTRIBUTORS and stores the distribution, so a percentile is recomputable.
6. **M3 Peers V, the peer-relative valuation z-score.** Blocked behind CSC values: W18-S13 measured 5 of 17 columns mapped and only
   1 carrying per-member values. The cell lands the values R-1 can carry and states which columns stay ABSENT and why.
7. **M4 Thesis/Risk Robustness.** The CTO measured 0 of 6 constraint inputs computable at the 8-quarter frequency from a fiscal-year
   model block. The cell either lands the six inputs from Bloomberg at that frequency or records the metric ABSENT with the
   per-input reason. It does not compute a score from inputs it does not have.

## Chain F -- the frontend, cut WIDE (Andrew asked for parallel frontend production)

8. **F1-F5, one cell per tab component:** each tab renders the headline slot as absolute plus pool percentile, with ABSENT and its
   reason when either half is missing. Five disjoint write surfaces now that the five tabs exist, so five workers can run at once.
9. **F6 the exact-input exercise over FIVE routes** (W18-S20): rankings, thesis, overlay, peers, coverage, so the header and the
   Peers tab are actually driven. The browser half already captures all five from the deployed adapter.

## Chain P -- producers and contracts still open

10. **P1 the Price producer writes no generation** (W18-S11 / Z-S105): every Price list reads ABSENT on the deployed readers.
11. **P2 the comparable's packs** (W20-S11 / Z-S104): the contract choice is the CTO's -- draft the comparable, restrict ordering to
    complete packs, or write the verdict absent.
12. **P3 the thesis route's as-of day** (W18-S19): it carries `generated_at` and `crosswalk_vintage` only. Whether the bundle should
    carry an `as_of_date`, and from which input, is a contract call for `1.0.0_SA_CTO~W`.

## Fan-out shape, if the analysis keeps these chains

Four or five dependency-independent chains (D sequenced, M partly sequenced, F wide, P independent). `fanout: N of M chains, cap 8`
with the frontend chain taking several slots at once. Cells 3, 6 and 7 are the ones most likely to be re-cut by the analysis.

## What the coming slug is reported to carry (REPORTED, NOT LANDED -- do not cut on it)

Quoted by `0.0.0_AB_MSTR~Z` (msg 23275) from a screenshot of `3.0.0_SA_CVO~W`'s own TUI at 22:40Z, the in-flight commit line reads:
`AMGT_RESAPP round 11 CVO L8-L10: 250 dispositions, AC5 fail, one remediation slug`.

- **AC5 FAIL matters most to this lane.** rj-3 AC5 is the round's ONE judgment criterion, and the browser half
  `ROUND11_BROWSER_EXERCISE.md` is what it grades. If the landed adjudication carries that grade, a round-12 cell re-cuts the
  exercise against whatever the CVO names as unmet, and chain F item F6 (the five-route exact-input exercise) is the natural home
  for it. The grade's REASON is not known and is not guessable from the commit subject.
- **250 dispositions** covers the whole channel at HEAD, so the round-11 rows this lane filed (Z-S107, W18-S19, W18-S20 and the
  rest) should come back dispositioned. The goal's DONE WHEN needs every row dispositioned, so the slug is also the read that tells
  this lane which rows remain open.
- **STATUS OF THIS NOTE:** a TUI line read through another seat's screenshot is the weakest carrier in this file. Nothing here is
  cut, cited or planned against until `REMEDIATION_v11.md` and the adjudication land at HEAD and this lane reads them directly.

## What card 19 means for THIS lane's COMPLETION_REPORT (1.0.0_SA_CTO~W, msg 23284, record @339699021e, ledger row 17)

Census taken by the CTO while preparing its L10 outcome-coverage read, from the PRD v0.8 outcomes own DONE WHEN lines:
- **19 outcomes declared. 18 are EXERCISED BY A PERSON** (an analyst, Adam, Lauren, a PM). **Exactly 1 is APPLIED: FWD-9.**
- **0 of 19 REALIZED after eleven rounds**, and every round analysis that states a count says 0.
- No COMPLETION_REPORT and no COMPLETION_GRADES exist anywhere in the repo for this project; `project.json` reads status active,
  dep_stage ROUND_CLOSE.

**Consequence for the close this lane owes, and it is a shape, not a narrowing:**
- FWD-9 is the ONE outcome this lane can grade REALIZED from an artifact with nobody present. Everything else needs the promote
  (Andrew, under PORTAL FROZEN: COMMIT YES / PROMOTE NO) and one session where named people work the page.
- So COMPLETION_REPORT, when round 12 is drained, grades FWD-9 against its exercised artifact and names the other 18 HELD-AT-STOP
  with the Andrew-reserved act each waits on. **The outcome set is never narrowed to make the report close** -- the goal's own
  words.
- **Nothing in the round changes on this card** (the CTO says so explicitly): round 12 still lands the four tab scores, the Model
  tab pool path and the peer-set repair, so the page is worth exercising when that session happens.

## A commit-time hazard this lane will meet on its own round-12 drains (1.0.0_SA_CTO~W, msg 23292, measured 23:16-23:27Z)

`3.0.0_SA_CVO~W`'s SECOND commit attempt was refused by the missions-tree-check hook reading `flat index rows=0
(generated=0, hand-written=0, parse-errors=0)` with 12 INDEX-MISSING violations and 2 R6 rows unreadable -- 14 violations.

**THE OBVIOUS READING IS FALSE and the CTO tested it before relaying:** it is NOT a sparse cone missing `org/projects/`. In that
seat worktree `core.sparseCheckout=false`, 367 index rows present, and `missions-tree-index.py check` run INSIDE that worktree
reads 0 violations with 367 rows; the shared tree control reads the same; no commit touched `org/projects/`, DIRECTIVES.yaml or
MACROS.yaml in the window.

**THE READ:** the hook reads the WORKTREE, not the staged index, and the shared tree was busy with POSN_AGGFIX drains at 23:1x-23:2x.
`rows=0 with parse-errors=0` is not "rows failed to parse", it is "no rows seen at all" -- the shape of a read taken MID-WRITE. Not
reproducible in either tree afterwards.

**WHY IT MATTERS HERE:** every round-12 drain this lane runs fires that same hook against that same shared tree while other seats
commit. If a drain refuses with `rows=0`, the act is **re-run the check in this tree and print its denominator** before touching
anything -- a transient refusal and a real INDEX-MISSING read identically in the banner and differently in the denominator. Do not
widen a cone, do not regenerate the index, and do not force past it on that banner alone. If it reproduces, it is a gate finding
and the gate belongs to `1.0.0_SA_CTO`'s lane, not this one.
