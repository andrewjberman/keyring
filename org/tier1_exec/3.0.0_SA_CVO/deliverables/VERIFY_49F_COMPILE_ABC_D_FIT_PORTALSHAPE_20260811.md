# GROUND-TRUTH VERIFY (Andrew-direct ~1005Z): compile? A/B/C fit D? D holds portal shape?

**3.0.0_SA_CVO 2026-08-11 ~1008Z · archetype: VALIDATE.** Not spec-reasoning -- run + measured.

## Q1 COMPILE -- YES
All 33 runners_49f/*.py + tests py_compile clean. Zero failures.

## Q2 DOES A/B/C SHAPE FIT INTO D -- YES (column-verified, not just wired)
d01_firm_header_metrics (the archetype emitter) reads FIVE columns from the A/B/C canonicals;
every one is WRITTEN by its producer (name-exact, not just path-wired):
- nna["nna_headline"]      <- c01_nna_canonical:58  ✓
- val["fair_value"] / ["account_id"] <- b00_canonical_valuation:62 (grain account_id)  ✓
- led["final_class"]       <- c00_flow_ledger:119  ✓
- rel["relationship_id"]   <- a01_dim_relationship:74  ✓
A producer writing `nna_head` under a consumer reading `nna_headline` would compile and be a
broken seam; measured, the names MATCH. The seam is real.

## Q3 DOES D MAINTAIN PORTAL OUTPUT SHAPE -- YES (byte-schema identical to the LIVE served artifact)
d01 payload vs the DEPLOYED s3://opal-data-bd/platinum/firm/header_metrics.json (read-only GET,
the live FE read): **0 key-path differences across the full nested tree -- BYTE-SCHEMA IDENTICAL.**
fit_harness self-test (the built parity instrument): PASS -- 368 fields compared, undeclared
mutant FAILED loud at firm_id, declared-domain mutant routed DESIGN. Read-only by construction.

## HONEST CAVEATS (two, neither changes the YES)
1. SCOPE: d01 is ONE emitter of 16 D families (fit_harness FAMILIES). d00 is the census, not an
   emitter. So the fit + portal-shape is PROVEN byte-exact for the ARCHETYPE emitter; the other
   ~14 families are the remaining port-forward, each gated by the SAME fit_harness parity that
   just passed. The pattern is proven; the instances are not all built.
2. VALUES vs SHAPE: d01's STRUCTURE is byte-identical, but some VALUES are backfill-pending zeros
   (nna_qtd/ytd/12m, by_architect array, new/existing splits) until the 525-partition backfill
   (P2+). The portal gets STRUCTURALLY-CORRECT data with some windows zeroed, never wrong-shaped
   data. Shape proven now; full values at backfill.

-- 3.0.0_SA_CVO
