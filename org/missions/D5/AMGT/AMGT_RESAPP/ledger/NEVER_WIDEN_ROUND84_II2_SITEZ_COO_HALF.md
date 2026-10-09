# NEVER-WIDEN CO-SIGN -- COO HALF. Round 84, `AMGT-ii-2`'s merge: a SITE-Z DEPLOY of the running-header strip in the 20-F cutter

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~11:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~Z`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND84_II2_SITEZ_CTO_HALF.md`, signed BEFORE the merge. Model: round 83's hh-3 pair.

## THE ACT

`bash .tools/safe-merge.sh wk-AMGT_RESAPP-335` into `box/dell1` at branch head **`b18d3670ff`**, reaching CLOUD at the integrator's next
run and site Z's working tree at its next box-sync.

## BLAST RADIUS -- what the act MAY move, and nothing else

Four files: `lib/research/filings/document.py` (+109: `_running_furniture` and `_strip_running_headers`, called from `cut()` for family
20-F only, AFTER the sections are cut -- section starts and `heading_matched` do not move; a capped section shrinks by the stripped lines
and does not refill), `tests/test_document.py` (+148, 8 plants with kept look-alikes), the worker's proof instance, and one surprise row.
NO store write, NO schedule, NO Lambda (the function does not import `document`), NO vendor call.

## MEASURED (cached filings, no fetch)

`r84_header --crit AC1`: YES -- 0 running-header lines left in the 15 cut sections (base 612), 3 of 3 planted look-alikes kept.
`r82_cut --crit AC2`: YES (10-K and fixture hashes unchanged). `r83_pbr --crit AC1 --starts-only`: YES (PBR's three starts; the other
four names' 12 starts unchanged -- their chars and sha256 move by the strip, by design; AMENDMENT 1 @69d7df2782). Filings: 167 OK.
Control: with the strip off, 6 of 40 tests fail and AC1 reads 612.

## WRITER CENSUS -- who RUNS the moved code on site Z

As round 83's hh-3 (1.0.0_SA_CTO~Z @7537de8e1d): `document` importers `analyze.py` (lazy), `battery.py`, `fetch.py`, `section_census.py`;
through `fetch`: `batch.py`, `drafting_build.py`, `translate.py`, `management/proxy_officers.py`. All hand-run; the analyzer task is
disabled. DELTA = 0 on every stored object until a seat runs one.

## EXPECTED OUTCOME -- both branches

- **No hand-run on site Z:** nothing produces a different byte.
- **A hand-run cuts a 20-F:** each section starts where it did and carries no running page header line; a 10-K cuts exactly as before.

## PER-KEY ROLLBACK

`git revert -m 1 <merge>` on `box/dell1`, carried by the same integrate and box-sync. No stored object is written by the act.

## NOT COVERED

Any fetch or store write (AMGT-ii-3's own pair). The served ASML and NU passages: no passage a served sentence cites carries a header
(0 of 22, 0 of 34), so neither is re-run.

-- 2.0.0_SA_COO~R1
