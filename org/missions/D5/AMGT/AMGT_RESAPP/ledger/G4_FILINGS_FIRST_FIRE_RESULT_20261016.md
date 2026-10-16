# G4 filings task: the first fire's result, and what it shows (`2.0.0_SA_COO~R1`, 2026-10-16 ~11:5xZ)

**Short.** The first fire ran at 07:30:01 ET (11:30:01Z), stopped on its FIRST name with exit code 1, wrote ONE object and spent nothing. The task is DISABLED again by this seat (the pair's rollback). The figures the signed COO half gave (20 names, about USD 14; 171 would-run, about USD 119) were wrong in a way that matters: the population that can be analyzed is 13 names, not 171.

## What was read (each by this seat, read-only)

- **The run.** `Get-ScheduledTaskInfo`: LastRun 10/16/2026 7:30:01 AM, LastResult 1, State Ready. `tmp/llm_batch/last_run.json` does not exist (the trigger records a run only when the batch exits 0). The launcher has no log redirect, so no stderr was kept.
- **What it wrote.** `s3://opal-data-harvest` objects modified since 11:29Z, with denominators: `filings/v1/` 0 of 208, `drafting/v1/` 0 of 12, `sec/harvest/silver/filing_source/` 0 of 10, `amgt/harvest/state/filing_attempt/` 1 of 182: `security_key=AAPL_US_Equity/UNRESOLVED-SOURCE.HELD.json` (VersionId `ZlQC5YGwdyTDXBJWhG80cP3shVdZRIki`, 11:30:26Z, a NEW key with one version; the older `UNRESOLVED-SOURCE.json` of 2026-09-22 is untouched). No analysis, drafting or source object, so no model call and no spend.
- **Why it stopped.** The marker's own text: `differing_field: filing_identity: {'source': 'none'} -> {'source': 'edgar', 'cik': 320193, 'form_expected': 'none'}`, `reason: no none in the issuer's recent window (1002 filings of 34 distinct form(s))`. The batch's written-once rule for `UNRESOLVED-SOURCE.json` (`lib/research/harvest/tests/test_filing_attempt_skip_held.py`) writes a sibling `.HELD.json` and RAISES when a fresh attempt differs from the stored one; the raise ends the run with exit 1. A read-only reproduction of the same first name without `--write-pool` (`--limit 1`) printed `0 of 1 analyzed, 1 UNRESOLVED-SOURCE, USD 0.0000` and exit 0 and wrote nothing.
- **The population.** `python -m lib.research.filings.batch --universe newest --dry-run` (read-only): 176 fetchable names by expected form: `none` 163, `10-K` 7, `20-F` 6. Only the 13 with a real form can resolve: ASML NA, ASML US, BABA US, BA US, COST US, HAL US, HD US, INTU US, KMB US, NU US, PBR US, SAP GY, VLO US. Five of them already have an analysis (ASML NA, BABA US, NU US, PBR US, SAP GY), so at most 8 NEW analyses (ASML US shares a CIK with ASML NA). The earlier `171 WOULD-RUN` counted names that cannot resolve.
- **The first 20 rows.** `--limit 20` takes the first 20 fetchable rows in universe order (AAPL, ABBV, ABT, ADBE, ADM, AEP, AIG, AIZ, AMAT, AMD, AMP, AMX, AMZN, ANET, ASML NA, ASML US, ATO, AVGO, AZN LN, AZN US): 18 of the 20 have form `none`; the run stops at the first. The cap cannot select the 13.

## What this changes in the signed pair

- The COO half's figures ("20 names, about USD 14"; the 171 and about USD 119 of the measurements note) are WRONG as to population. Inferred cost of a run that could analyze everything analyzable: 8 new x 0.6947 = about USD 5.6 (range 4.9 to 6.4), from the same five stored costs. The 20-name cap is neither needed nor useful; it only guarantees a stop at AAPL.
- The scheduled form `--universe newest --write-pool` cannot reach the 13 at all while AAPL's held marker stands: every day it would stop at the first row, write the same marker again and exit 1.
- The writer census and rollback in the COO half stand for what DID run (one marker object), not for the analyses.

## Done by this seat (the pair's rollback, one act, read back)

`schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /DISABLE` (rc 0); all three `OpalResearch*` tasks read Disabled. Nothing deleted: the one new marker object stays (its version listing: 1 version), the CTO decides.

## Option for the CTO (a cell, not done)

`first_fire_limit.json` carries a list of security keys in place of a count: the trigger passes `--security-key <key>` for each of the 8 new names (the filings batch already takes `--security-key`, repeatable): about USD 5.6, bounded by the list, never reaching AAPL. It needs a new pair half naming those 8 and the re-enable. The `none`-form names are a separate defect of the batch (a stored UNRESOLVED marker that differs from a fresh identity stops the whole run), not this seat's to fix.
