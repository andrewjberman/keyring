# Andrew-direct GIPS-TWR feasibility: YES at DAILY tier -- the 49F archetype's third hard leg measured
**archetype:** TRACE + VALIDATE
**Window:** 0630-0645Z, Andrew-direct at this terminal.

## What happened

1. **ANDREW-DIRECT (verbatim in the deliverable):** assess GIPS-standard TWR feasibility from
   Schwab raw data against his GPT-produced standard doc (Desktop RTF -> text; THE spec, its
   provisions carried, never generic GIPS knowledge), via atom_decomp on the schwab fact tables.
2. **DELIVERED @e323c1cfac + view @5125943d3d** (third full run in the package ledger tonight:
   gips-twr-schwab-feasibility__20260811T0635Z, 15 entities from the standard's own discovery
   checklist + hard-stop sweep + FX boundary, 85/90 MEASURED, schema-VALID).
3. **VERDICT: YES -- DAILY TWR tier.** Both halves of the standard's deciding question
   MEASURED-YES: dim_balance = authoritative per-account daily fair-value series (525 trading days
   2024-07-08.., net_mv_plus_cash 100 percent, full decomposition -- the preferred-input branch);
   fact_trn = the classifiable ledger (100 percent dates/amounts/direction, 21-code universe,
   vendor categories near-1:1 onto external/internal). No source-computed return in all 20 tables
   (~A cited) -> canonical decision 2 = exactly instruction-5's grant, now GIPS-quality-barred.
   ZERO hard-stops; ONE conditional (code materiality = build task 1); five sized refinement cells
   (code table; fact_fam parse -- decoded as the account->family map; transfer pair-matching, swb
   sparse 3/1,961; accrued-income derivation for 112 rate-bearing assets from fact_sec coupon
   inputs; reversal specimen scan). USD-only boundary (zero FX cols); history floor stated.
4. **Instrument discipline, disclosed in-deliverable:** the package validator caught two authoring
   defects pre-commit (UNMEASURED-with-value; MEASURED-without-evidence); my own fixed-income probe
   mis-keyed on sentinel maturity dates and was discarded for interest_rate-nonzero; bare notna()
   on string columns read 100 percent and the empty-string correction INVERTED two cells before
   publication -- now mechanical constraint M2 in the rectangle itself.
5. **Folds landed downstream same-window:** CTO matrix -- the 49F performance-leg L4 cell
   DELIVERED, and with identity (map+zfill) + ingest (Model-B) + performance (this) the archetype's
   three hard legs are ALL MEASURED ("the strongest position any build in this program has started
   from"); ~A -- quality bar banked on the 49f=computed cell, both refinement cells adopted as
   archetype-spec rows, fact_fam's parse promoted from curiosity to named build task.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| aws s3 ls/cp (operational) | 20-table roster + cadence census (8,742 objs); 8 decisive tables pulled at date=2026-08-07 | daily cadence proven; schemas measured |
| pyarrow/pandas (scratchpad) | schema + content verification incl. empty-string-corrected counts | the verdict's cells |
| jsonschema | run conformance | 3 files VALID after 2 real catches |
| RTF->text converter (scratchpad) | the standard doc ingest | 12,346 chars, requirements extracted verbatim |

## Blockers

**None at me.** Build tasks route via COO at the archetype trigger (CTO's fold); CVO cert rides its
queue; the five refinement cells live in the deliverable as the natural TO seams. RECON-6 remains
my active critical-path item.
