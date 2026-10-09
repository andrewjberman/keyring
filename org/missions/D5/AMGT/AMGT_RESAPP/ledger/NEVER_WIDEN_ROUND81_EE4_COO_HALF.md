# NEVER-WIDEN CO-SIGN -- COO HALF. Round 81, `AMGT-ee-4`: re-cut and re-analyze the five stored 20-F names (ASML NA first)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~04:5xZ, before the GO. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND81_EE4_CTO_HALF.md`. Grounding: `deliverables/2.0.0_SA_COO~R1/round81_prep/GROUP_STORE_NOTES.md`
@2a2b247b7c. Order: `task-orders/AMGT_RESAPP.TO-AMGT-ee-4.the-store-half-five-20f-names.md`.

## THE ACT

Per name, in this order, ASML_NA_Equity first and checked (AC1, AC2) before the other four (BABA_US_Equity, NU_US_Equity,
PBR_US_Equity, SAP_GY_Equity), run on dell1 with `py -3.12` after AMGT-ee-3 is merged (fetch and analyze import):
1. `python -m lib.research.filings.fetch --security-key <KEY> --form 20-F --cik <CIK from the stored filing_identity> --write-pool`
   (one SEC EDGAR GET; one silver part appended).
2. `python -m lib.research.filings.analyze --security-key <KEY> --source-json <the fresh source.json> --write-pool`, with
   `ANTHROPIC_API_KEY` exported in the same call from `comp-secrets get anthropic-api-key --reveal` (one model call).
3. The drafting splices re-run on the new draft only if they had run on the prior one (notes section 1.3), said in the record.

## BLAST RADIUS -- what the act MAY touch, and nothing else (per name: three keys)

| key | write | served by | rollback (no delete, R2) |
|---|---|---|---|
| `s3://opal-data-harvest/sec/harvest/silver/filing_source/date=<run date>/part-<stamp>.parquet` (builder `store.address_of` -> `opal_naming.address`) | NEW part, put-if-absent | `scoped_amgt._read_filing_source_object` (via `silver_latest`, newest `fetched_at` per security_key+accession) | append a newer part carrying the prior row's content, so `silver_latest` reads the prior row again; the new part is never deleted |
| `s3://opal-data-harvest/filings/v1/<KEY>/<accession>.analysis.json` | overwrite (versioned) | segment rows, passage map | re-write the prior VersionId's bytes as the newest version (copy-object from that VersionId); ASML NA's prior: `WIU.oSeIh8NKMhy2DfqsJmRwGOusYTxs` |
| `s3://opal-data-harvest/drafting/v1/<KEY>.json` | overwrite (versioned) | `/thesis` drafted sections, driver chart | same; ASML NA's prior: `FWeloN5.zr6pvN1NWUXScK5RakjwF1qV` |

The other four names' prior VersionIds are read fresh at the act and recorded in the change-management entry before the first write.
NO Lambda, NO Terraform, NO IAM, NO page, NO other key. NO S3 delete. NO Bloomberg call.

## WRITER CENSUS (rules read, notes section 4)

- silver `filing_source` (sec): ONE writer function (`fetch.persist` -> `harvest.filings.write_filing_source_silver` -> `store.silver_append`),
  three callers (`fetch.main`, `batch.run_group`, `battery.py`'s EDGAR leg); appends only.
- `filings/v1/*.analysis.json`: `analyze.write_outputs` and `analyze.reverify_stored_thesis_driver` (N = 2).
- `drafting/v1/*.json`: `analyze.write_outputs` and `drafting_build` (N = 2 modules, 4 entry points).
- No scheduled task runs any of them (`-FilingsAnalyzer` disabled; census @6a308cd424). A dell1 RUN is not a change to a site-Z producer
  path (CTO~DELL1 analysis R1: the store half runs on dell1); the keys are the same a site-Z run would write.

## EXPECTED OUTCOME -- both branches, read from the producer's rule

- **The filing has an Item 4.B Business overview heading:** the new stored source's excerpt carries `business` (cap 60000), risk and
  mdna cut by today's patterns (no bare-fallback risk); the analysis and draft are rebuilt from it; the served /thesis for the name
  draws from the business text and the share-capital refusal no longer applies (ASML NA: AC2).
- **The filing has no such heading:** `business` reads FAILED with its reason in the stored source; risk / mdna as today's patterns cut
  them; the served page names no business section for that name. The act is covered on this branch: the rollback below applies unchanged.
- **The model call fails or the analysis refuses:** nothing is written to the analysis or drafting key for that name (write_outputs runs
  after the call); the silver part alone stands and `silver_latest` serves it; the name is reported and the next name proceeds only
  after ASML NA's AC1/AC2 read YES.

## NOT COVERED (a new act, a new pair)

Any name outside the five; any 10-K re-cut; any drafting splice the prior draft did not carry; any deploy; any S3 delete.

-- 2.0.0_SA_COO~R1
