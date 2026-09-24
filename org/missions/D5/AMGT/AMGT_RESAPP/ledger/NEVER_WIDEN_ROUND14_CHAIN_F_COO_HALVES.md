# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain F (filings). One co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_F_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; the worker reads BOTH before its first live act and STOPS with a
BLOCKING row if either is absent or lacks the `AMGT-rk-41` section. `rk-38`, `rk-39`, `rk-40`, `rk-42` write only
validation-name pool objects that no served route resolves (the three keys are not in the crosswalk) or nothing at all,
and are NOT co-signed; `rk-42`'s one device act (re-registering a DISABLED scheduled task from its own XML, `Enabled
false` before and after) is a device-plane act with no served surface and is covered by its own change-management
entry, not by a pair.

## `AMGT-rk-41` -- C-VERBATIM-GATE = HOLD applied by rebuilding the served drafting objects (R14-F4; FWD-9, FWD-18, V6/D18)

**THE ACT.** `python -m lib.research.filings.drafting_build --rebuild-pool --population crosswalk/v1/2026-09-15.json
--pre-act-dir .scratch/drafting_v1_preact` -- ONE rebuild, through the ONE writer, of every `drafting/v1/<key>.json`
whose key is in the MEASURED population AND carries an analysis object (12 at the cut; AC5 re-measures the denominator
at spawn). NO model call (the rebuild applies the gate to sentences already drafted -- it holds an unanchored sentence,
it writes none). NO Lambda redeploy (AC7 is a read-only invoke before and after).

**BLAST RADIUS (narrowed on CTO msg 23833 D4, the issuer's reading with its basis):** LIVE, only the validation keys
`CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` that carry an analysis object (`--only-keys`; 0 to 3, each absence
NOT ATTEMPTED with its reason); the twelve covered keys are DRY-RUN ONLY this round -- their rebuild is a producer
re-run over covered names, barred by Andrew's standing word until end-to-end validation, re-opened then under a fresh
pair. Where the live set is non-empty: up to 3 keys under `drafting/v1/`, each REWRITTEN IN PLACE (this prefix is keyed by
name, not stamped -- the one served prefix in this round whose rollback is a RE-PUT, not a delete). Served: YES, every
one -- the thesis/drafting routes serve these objects for every crosswalk name that has one. Nothing else moves: no
analysis object, no filings source object, no adapter.

**WRITER CENSUS of `drafting/v1/<key>`: N = 2 writers at HEAD** -- `analyze.py:1215` and `batch.py:150` (PRD v0.13 :918
names both; CTO msg 23830 re-verified). `drafting_build.py` is the COMPOSER, not a writer: at HEAD it has no `main()`, no
argparse, no `__main__` guard and no S3 write. `AMGT-rk-42` (sequenced BEFORE this cell) collapses the two writers into ONE,
`analyze.write_outputs(...)`, and `rk-41`'s new CLI (its step 3) writes ONLY through that function -- so at the time of THIS
act N = 1, and the order's AC8 proves the entry point exists and refuses a bad call before any pool read. No schedule
writes the prefix (`OpalResearch-FilingsAnalyzer` is DISABLED; `comp-schedule` at the cut: 0 on `drafting`). Rule read: a
rebuild replaces the whole object for a key from its analysis object under the current gate.

**EXPECTED OUTCOME, both branches (read from the HOLD rule as the order inlines it, section 1), with the D3 bind: the
rebuilt document ships ONLY `PASS` sentences in `sections[].sentences`, every held sentence in a top-level block, and no
`verbatim_check` value outside {PASS, REFUSE} reaches the adapter -- the branch that would take every document INVALID
against the deployed validator while the shrink check reads GREEN is closed by the order's bind and printed per key.** A sentence with a
verbatim span anchored in its source: SERVED unchanged. A sentence with no anchoring span: HELD -- present in the
object under `held_no_span` with its reason, `served_no_span` = 0 for EVERY rebuilt key (AC6 prints both counts per
key). The 11 objects derived from pre-driver-point analyses (analysis s.3.8, carried as data): rebuilt under the gate
LIKE THE OTHERS -- the gate re-apply is NOT the content rebuild s.3.8 defers, and the order says so; if `1.0.0_SA_CTO~Z`
reads s.3.8 as barring even the gate re-apply, AC6/AC7 are struck (the census names them) and this half then covers
nothing. AC7's planted read on BA_US_Equity before and after: the route still `200`; the served sentence set for BA
shrinks or is equal, NEVER grows (that is the never-widen on this axis).

**PER-KEY ROLLBACK, from the live pre-act bytes.** Pre-act: for EVERY key in the measured set, `get_object` bytes
saved to `.scratch/drafting_v1_preact/<key>.json` with sha256 recorded in the change-management entry (AC5) BEFORE the
rebuild. Rollback = re-put each saved file to its key (`put_object`, same key, then `head_object` read-back of the
sha256). The `.scratch/` copies are the rollback INPUT and are named in the entry; they are never committed.

**NOT COVERED:** any model call; a rebuild of a key outside the measured population; a change to the adapter's own
validator (`scoped_amgt.py:1483-1514`, chain B's file -- the order names it OUT of scope); a switch that would make
HOLD anything but HOLD (card 4 answered HOLD; no switch exists).

**Change-management:** entry opened with `.tools/deploy_ledger.py open` before AC5's snapshot, sentinel COMMITTED;
legs closed with AC5's sha table, AC6's rebuilt count and AC7's before/after.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.
