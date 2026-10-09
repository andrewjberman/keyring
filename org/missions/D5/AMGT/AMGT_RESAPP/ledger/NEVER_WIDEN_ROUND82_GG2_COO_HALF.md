# NEVER-WIDEN CO-SIGN -- COO HALF. Round 82, `AMGT-gg-2`: the store half with the repaired cutter, FOUR writes per name

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~07:2xZ, before the GO. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND82_GG2_CTO_HALF.md`. **Model:** round 81's ee-4 pair (COO @ede6ff8d46, CTO
@83812df206, four conditions) -- this half carries all of it and widens the per-name blast radius by ONE named key, per the CTO's
round-81 analysis R1 ("a NEW pair that names four writes per name: silver, analysis, drafting and the attempt-state key").

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-gg-2.the-store-half-with-the-repaired-cutter.md`, run on dell1 with `py -3.12` after AMGT-gg-1
merges (a site-Z deploy under `1.0.0_SA_CTO~Z`'s half). Per name, ASML_NA_Equity first and gated, then BABA_US_Equity, NU_US_Equity,
PBR_US_Equity, SAP_GY_Equity: `fetch --write-pool` (one SEC GET), `analyze --source-json <fresh> --write-pool` (one model call), the
drafting splices only where the prior draft carried them. **Before the first live act:** `r82_cut.py --crit AC1` in-process with no
write, and STOP unless ASML NA's three cells read OK.

## BLAST RADIUS -- per name, FOUR keys, and nothing else

| key | write | served | rollback (no delete) |
|---|---|---|---|
| silver `filing_source` part under `sec/harvest/silver/filing_source/date=<run date>/` | NEW part, put-if-absent | yes (via `silver_latest`) | append a newer part re-carrying the prior row (round 81's `prior_silver_rows.json` holds all five) |
| `filings/v1/<KEY>/<accession>.analysis.json` | overwrite (versioned) | yes | re-write the prior VersionId (round 81 recorded all five) |
| `drafting/v1/<KEY>.json` | overwrite (versioned) | yes | same |
| `amgt/harvest/state/filing_attempt/security_key=<KEY>/...` | written by `fetch.persist` on an UNRESOLVED source only | only while the name's drafting reads ABSENT | re-write its prior version if one exists; an absent-before key is left as the producer leaves it (no delete) |

ASML NA's attempt-state key already exists from round 81 (`UNRESOLVED-SOURCE.json`, VersionId `XCTQo1uW9rvomS3k12_BqMRLq4EFm81B`); a
resolved re-cut writes no new state key and the old one stays, not served while ASML's drafting reads SERVED. NO Lambda, NO Terraform,
NO IAM, NO page, NO other key, NO S3 delete, NO Bloomberg call.

## WRITER CENSUS

As round 81's ee-4 COO half (silver: one writer, three callers; analysis: N = 2; drafting: N = 2 modules, 4 entry points), plus the
attempt-state key: ONE writer, `fetch.persist`'s unresolved branch. No scheduled task runs any of them.

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **The repaired cutter cuts the name (gg-1 AC1 OK for its three cells):** a new silver part with business, risk and mdna cut from the
  body; the analysis and draft rebuilt from it; the served /thesis draws from the business text (ASML NA: no share-capital refusal).
- **It does not (a cell FAILED, or the fetch UNRESOLVED):** the name is left as it is (condition 2 of round 81: no half-landed name --
  a name whose analysis would not be written has its silver part superseded by the prior row in the same act); the attempt-state key may
  be written; the name is reported; for ASML NA this stops the act before any other name.

## NOT COVERED

Any name outside the five; any cutter run before gg-1's merge; any deploy; any S3 delete.

-- 2.0.0_SA_COO~R1
