# ROUND-1 ANALYSIS -- MDPF_SECCLASS (D8), 1.0.0_SA_CTO, 2026-09-30 ~03:0xZ

**On:** the CVO's L10 slug 103113 (`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md` @a7fcb28d57) and the COO's drain packet
(`DRAIN_END_R1_20260930.md` @ee54196616, read via the CVO's summary, not opened by me). The COO recuts round 2 from the ENRICHMENT LIST below in ONE issuance.
**Evidence base:** the CVO's live reads at 02:4xZ (one scan page of 2,309 rows of `etf-classifications`; PHYS and GLD get-items), my own reads of the two signed halves, and the PRD's FWD text.
I did not re-run any scan. Grades below are what those reads support; a FWD with no cell in round 1 is graded NOT YET SERVED, not NOT_REALIZED.

## 1. The decision asked: C-WRITER (the 238 rows with no `classified_by`)

**RULING.** Both: name the constituents seeder in the contract AND label the 238.
1. `classified_by` becomes a four-value set: `seed`, `scheduled`, `constituents`, `legacy`. `seed` still always wins. `scheduled` and `constituents` write only where no row exists.
   The constituents seeder (`seed-etf-constituents.py`, my ruling 103050) now sets `classified_by = constituents` on every row it writes; its condition stays "the row does not exist or carries no label".
2. The 238 unlabelled rows get `classified_by = legacy` by ONE additive conditional update (`attribute_not_exists(classified_by)`), touching no other attribute. `legacy` means "written before this contract; provenance not recorded"; it is not a claim about which seeder wrote it.
3. The label update writes to existing rows, so it carries its own never-widen halves (CTO and COO). It is not a rider on another cell.
4. Until it lands, FWD-4's census reports any row with no label as a finding, and "seed always wins" reads a missing label as `legacy` (loses to `seed`, wins against `scheduled`). One rule, stated in the contract.
**WHY.** A provenance field that admits "none" cannot discriminate; the CVO is right that the census has no value to read on those rows. Labelling does not change any served class.
**Not decided here:** whether any of the 238 is wrong. That is FWD-2's job once they carry a label.

## 2. Grades (FWD-1..8)

| FWD | grade | basis |
|---|---|---|
| FWD-1 thread | NOT_REALIZED | thread orders t1-t4 complete, but the thread halves predate the backfill (3,699 unclassified BD holdings were read before it) and the CVO signs none whose figures were read before 02:2xZ. No live run of the BD chain to the page has been done. |
| FWD-2 one answer everywhere | NOT YET SERVED | no round-1 cell exercised it. PHYS reads commodities/Metals/seed/fund and GLD the same (CVO reads), which is a start, not the acceptance. |
| FWD-3 one edit | NOT YET SERVED | the CVO's note stands: exercise it with a ticker the fork had wrong. |
| FWD-4 no second definition | NOT_REALIZED | a fourth classify site exists (W3-S3: served positions.json is coarse), so the check does not read zero. |
| FWD-5 old copy deleted | NOT YET SERVED | waits on FWD-4 reading zero; the delete is Andrew's act. |
| FWD-6 declared exceptions | NOT YET SERVED | no cell in round 1. |
| FWD-7 scheduled classification | NOT_REALIZED | the backfill wrote 1,934 rows, but per the PRD a one-off catch-up is test evidence only; the ordinary scheduled run has not happened, and the E_18 IAM change is unsigned. |
| FWD-8 fund vs stock | NOT_REALIZED | `instrument_kind` is absent on 2,163 of 2,309 rows (fund 135, single_security 11). |
Nothing is REALIZED, so the project stays open. Round 1 did what round 1 is for: the table exists with a writer rule, the seed run and the backfill landed under signed halves, and the thread is traced.

## 3. ENRICHMENT LIST (round 2; the COO cuts one issuance)

| # | cell | serves | notes |
|---|---|---|---|
| E1 | Contract amendment + the `legacy` label update (section 1) | FWD-4, FWD-7 | contract `MDPF_SECCLASS_CONTRACT.json` v0.2.0; halves for the label write; PRD addendum by me after the CVO signs the contracts half |
| E2 | Populate `instrument_kind` on the 2,163 rows; add the `instrument_kind`-only update mode | FWD-8 | the input source (Schwab, GICS) is not wired: the first act is to name it. W2-S3 |
| E3 | Re-census the BD thread after the backfill, then fresh halves, then the thread deploy (release step 3) and one live run to the page | FWD-1 | the CVO will not sign a stale-figure half |
| E4 | A ticker-keyed source for Cottonwood | FWD-2 | S2, ARMED; IB-mr-251 waits on it |
| E5 | The fourth classify site (served positions.json) folds into the one list | FWD-4, FWD-2 | W3-S3 |
| E6 | FWD-3 exercise: pick one ticker the fork had wrong, correct it in the seed source once, read it on every screen | FWD-3 | shows `seed` beats `scheduled` |
| E7 | The ordinary scheduled run and its IAM half (PutItem on `etf-classifications` for E_18's principal; removal of the `bd-securities` PutItem grant) | FWD-7 | needs its own halves; the trigger is the schedule, never upstream success alone |
| E8 | The 884 unresolved names (bd 207, 49financial 601, inflection 76) | FWD-2, FWD-7 | listed by name in the census; a named class or a stated reason each |
Build TOs carry at most three mechanical criteria; repo-wide hygiene runs at the drain.

## 4. What I am NOT changing
The PRD text, the endpoint and the DONE WHEN lines are unchanged. The C-WRITER edit rides E1 and a PRD addendum after the contracts half is signed, so no signed half is re-opened by this analysis.
