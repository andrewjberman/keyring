# CTO never-widen half -- MDPF_SECHIST SH-t-4, `etf_daily_pull.py` @8d21f46533 at site Z (run record prints the draw beside the ledger remainder; FWD-7)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~13:4xZ (msg 926). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_SH_T4_SITEZ_DEPLOY_20261008.md` @cf0cd79497.

## VERDICT: SIGNED on the technical half, NOT ACTIONABLE until Andrew's word on the no-modify order. Site Z's own pair governs the act.

## Read by this seat

- **Blast radius:** `bbg/<asof>/run_manifest.json` gains `spent_after` and `remainder`, and the leg's log gains one line. N = 1 writer of
  the manifest (`main()`). No row requested, drawn, written or recorded changes. The refusal rule, the ledger format and the production
  pull are untouched, pinned by the 5 existing plan/budget tests plus the new one.
- **Both branches** are read from the new code's own rule: the re-read succeeds (two numbers and one line), or it raises (two nulls,
  one WARN, exit code unchanged). Where the budget block was never reached, nothing is added.
- **Rollback:** site Z restores blob 0e399c9523 (fad25b1527). The two manifest fields have no reader, so they may stay.
- **The file is under Andrew's standing no-modify order.** `integrations/bloomberg/pipeline/` is the Positioning/ETFS-view pipeline
  (Andrew-direct 2026-10-06 ~20:1xZ, `ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md`:
  "The order still stands for the Positioning and ETFS-view files (`integrations/bloomberg/pipeline/`, the vehicle and the sign-in").
  SH-t-1's change to this same file landed on his explicit merge word to site Z (~13:3xZ 10-07). A pair cannot substitute for that.

## Conditions

1. **Andrew's word on this change** (an act only he can do: lifting a hold he set by name). It goes to him through site Z's CTO, which
   owns the vehicle, or the laptop. Without it, nothing lands.
2. **Site Z's pair** (`1.0.0_SA_CTO~Z` and its COO) governs the act on site Z's tree. This half is dell1's technical read only.
3. **Order:** the deploy lands only after the FWD-1 acceptance pull (earliest 2026-10-09 07:00 ET) has run on the round-1 bytes, and
   outside the 07:00 ET window.
4. After the first run: the manifest carries both keys (or two nulls with one WARN), and the rows drawn equal the ledger's
   `backfill` line for the day.
