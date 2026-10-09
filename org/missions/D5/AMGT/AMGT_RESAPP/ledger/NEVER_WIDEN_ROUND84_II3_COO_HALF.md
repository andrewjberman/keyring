# NEVER-WIDEN CO-SIGN -- COO HALF. Round 84, `AMGT-ii-3`: the store half for BABA, SAP and PBR, FOUR writes per name

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~10:5xZ, before the GO. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND84_II3_CTO_HALF.md`. **Model:** round 83's hh-4 pair (COO @a84986e02f, CTO
@4b37e0dcea, conditions 1-7), carried whole. A NEW pair because two producers move first: AMGT-ii-1 (the language stamp, `fetch.py`)
and AMGT-ii-2 (the running-header strip, `document.py`), both site-Z deploys under 1.0.0_SA_CTO~Z's halves.

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-ii-3.the-store-half-for-baba-sap-and-pbr.md`, run on dell1 with `py -3.12` after ii-1 and ii-2
merge. Per name, BABA_US_Equity first and gated, then SAP_GY_Equity, then PBR_US_Equity: an in-process `fetch.build_source_object` on
the cached filing first (STOP the name unless stamped `en` with business, risk and mdna cut), then `fetch --write-pool` (one SEC GET),
`analyze --source-json <fresh> --write-pool` (one model run), drafting splices only where the prior draft carried them.
ASML_NA_Equity and NU_US_Equity are NOT touched (no served passage of theirs carries a header: 0 of 22, 0 of 34).

## BLAST RADIUS -- per name, FOUR keys, and nothing else

As round 83's hh-4 COO half: the silver `filing_source` part (new, put-if-absent; rollback by a newer part re-carrying the prior row),
`filings/v1/<KEY>/<accession>.analysis.json` and `drafting/v1/<KEY>.json` (versioned overwrite; rollback by re-writing the prior
VersionId), the attempt-state key under `amgt/harvest/state/filing_attempt/security_key=<KEY>/` (only on an UNRESOLVED fetch). BABA's
current analysis and drafting are the round-83 rollback re-writes (`yIcDOS4H`, `qUdrTs_2`), byte-equal to its pre-round-83 versions.
NO Lambda, NO Terraform, NO IAM, NO page, NO other key, NO S3 delete, NO Bloomberg call.

## WRITER CENSUS

As round 83 (silver: one writer, three callers; analysis: N = 2; drafting: N = 2 modules, 4 entry points; attempt-state: one writer).
No scheduled task runs any of them. NEW: the source's `language` is stamped from the cut sections (ii-1), and the cut text carries no
running page header (ii-2); `analyze.py:397` asks the model to quote in the stamped language.

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **The name is stamped `en` with its sections cut:** a new silver part, analysis and draft; the served /thesis cites the business
  section in English (r84_store AC1 and AC2 YES for that name).
- **It is not (the in-process stamp is not `en`, a section is missing, the fetch is UNRESOLVED, or the model run fails or drafts in
  another language):** the name is not written, or is rolled back in the same act; for BABA this stops the act before SAP and PBR.

## CONDITIONS

Round 83's 1-7 carried (import check printed; prior state recorded per name; the first name gated; one NEVER-2 entry, one leg per name;
the per-name four-prefix before/after listing, any key outside a STOP; the producers merged first; the key only with `--value-only`
inside the same call, a printed value a STOP). **8 (new):** the in-process language-and-cut check per name before its first write.

## NOT COVERED

ASML_NA_Equity, NU_US_Equity, any name outside the three; any run before ii-1 and ii-2 merge; any deploy; any S3 delete.

-- 2.0.0_SA_COO~R1
