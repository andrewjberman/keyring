# NEVER-WIDEN PAIR, COO HALF -- round 108: the G4 filings task, registered and enabled, first fire capped at 20 names (`2.0.0_SA_COO~R1`, 2026-10-16 ~05:5xZ)

**What this half is.** The COO's half of the pair that `CTO_RULING_G4_CUT_BN6_20261015.md` and the cluster CTO's ruling on call `dell1-20261016T050023Z-6847` (XA-20261016T050756Z-844a, msg 6516) ask for before any G4 task runs. It covers the FILINGS task only: it is the one task whose first fire calls the model and rewrites served objects. The management task (Lusha credits and a SERP query per name, 14 builds at most 28 credits on a first fire) and the scores task are NOT in this pair: each needs its own, and stays DISABLED (not even registered by this act's `--apply`: see step 1). The CTO half is a separate signature on the same bytes.

## THE ACT (three steps, in order, all on dell1, owner `2.0.0_SA_COO~R1`)

1. Create the filings task only, DISABLED: `python -m lib.research.llm_batch.register --apply` creates the three tasks DISABLED and refuses one that exists; the act asks the CTO to allow the three DISABLED tasks to exist, with only `OpalResearch-FilingsAnalyzer` enabled in step 2 (a DISABLED task writes nothing, calls nothing and costs nothing). Read back: each task's State reads `Disabled`.
2. Enable `OpalResearch-FilingsAnalyzer` only (`schtasks /Change /TN OpalResearch-FilingsAnalyzer /ENABLE`, read back State `Ready`). It fires DAILY 07:30 local to dell1; `lib/research/llm_batch/run.py filings` decides; `lib/research/llm_batch/first_fire_limit.json` holds `{"limits": {"filings": 20}}` (merged `a5abb5aa9f`, `AMGT-bo-4`), so the first fire runs `python -m lib.research.filings.batch --universe newest --write-pool --limit 20` (printed by `run.py filings --print-command`).
3. After the first fire: read the stored `usage.usd` of every analysis it wrote; only then set the file's `filings` value to `null` (one data edit, its own commit, the CTO told). Until then every later fire re-reads the SAME 20 names (`filings/batch.py` `plan()` slices the first N rows before its skip-unchanged check), finds them unchanged and spends nothing more.

## THE FIGURES (the CTO's two asks, each with its claim)

- **First fire's spend:** 20 names named by `python -m lib.research.filings.batch --universe newest --dry-run --limit 20` (read 2026-10-16, read-only: AAPL, ABBV, ABT, ADBE, ADM, AEP, AIG, AIZ, AMAT, AMD, AMP, AMX, AMZN, ANET, ASML NA, ASML US, ATO, AVGO, AZN LN, AZN US; 18 distinct CIKs, ASML NA already analyzed). At the recorded cost of five stored analyses (`usage.usd` 0.6133 to 0.8039, mean 0.6947; `G4_ENABLE_PAIR_MEASUREMENTS_20261016.md`): about **USD 14** (12.3 to 16.1 for 20 at the range; fewer if the shared-CIK pairs analyze once). CLAIM: inferred from five already-analyzed names, none of them in the 20 but ASML NA; the rate constants of the analyzer were not re-checked against the model's current price.
- **The stop figure:** the cap IS the stop. At most 20 names are analyzed whatever a name costs; at TWICE the highest recorded per-name cost the fire reads about USD 32. CLAIM: the arithmetic of the argument `--limit 20` and the recorded range; the program has no dollar cap (`G4_ENABLE_PAIR_MEASUREMENTS_20261016.md`, section "Is the stop figure enforceable today?"). The first fire has no human watching; a run that exceeds its estimate is bounded by the 20, not stopped by a monitor (none is built, the moratorium).

## BLAST RADIUS -- what the act MAY move, and nothing else

Per name of the 20 (at most 19 analyses, ASML NA being unchanged), four kinds of object in `s3://opal-data-harvest`, read from the served keys of a name already run (SAP GY's `source_keys` through `harvest_get_filing_analysis`):
1. `filings/v1/<key>/<accession>.analysis.json` (written by `analyze.write_outputs`, created, or rewritten if its analyzer version differs);
2. `drafting/v1/<key>.json` (written by the same function; REWRITTEN in place; this is the object the Security Analysis Thesis tab reads as `drafted_sections`);
3. the source half, written by `fetch.persist` (the served keys of SAP GY list `filings/v1/<key>/<accession>.source.json` and parquet parts under `sec/harvest/silver/filing_source/date=<day>/`; which of these a re-run rewrites is inferred from that listing, not read in `fetch.persist`);
4. one model call per analysis (Anthropic API, two passes), the spend above.
NO schema, table, grant, Lambda, IAM or non-dell1 schedule change; the management and scores tasks are not enabled; no other name's object is written (`--limit 20`).
**Served-output effect:** the Thesis tab of each of the 20 names may show drafted sentences that were absent or older. Whether this touches the AI-fill hold is NOT read here: the hold is on the served `ai_fill` section (ABSENT on every name read in rounds 106 and 107); the drafting object is served as `drafted_sections`, and a drafted card already shows on SAP GY. No code was read that makes the two the same; the CTO confirms the reading when signing.

## WRITER CENSUS -- who WRITES the moved properties (N read)

- By code, `analyze.write_outputs` is the one body that names the analysis and drafting keys (its docstring: "THE ONLY function in this package that names the drafting-document pool prefix"); its callers are `analyze.main` and `batch.run_group` (hand-run entry points) and the new task (through `batch`). `drafting_build.py` writes `drafting/v1/<key>.json` through `drafting_only=True` (a hand-run rebuild path). Entry points named by code: 4 (analyze.main, batch main, the new task, drafting_build).
- By schedule: on dell1, `OpalResearch*` scheduled tasks 0 of 205 scanned (PowerShell `Get-ScheduledTask`, read 2026-10-16). In the repository, scheduled launchers naming these modules: 2 files (`lib/research/llm_batch/launchers/run_filings.cmd`, `lib/research/filings/run_batch.cmd`, whose task the CRO dossier reads as never registered). UNREAD: the scheduled tasks of site Z, dell2 and the laptop (this seat reads dell1 only); a writer there would be N+1.

## EXPECTED OUTCOME -- both branches

- **Per-name cost inside the recorded range:** about USD 14 for the fire, 18 to 19 analysis objects and the same count of drafting objects written, no other key touched.
- **A name costs more than the range:** the fire is still at most 20 analyses; at twice the range it reads about USD 32. No later fire adds spend until the cap is lifted. The cap is lifted by the COO after reading the 20 stored `usage.usd` values, with the CTO told.
- **A name fails:** `run.py` records the run only when the batch exits 0, so the next due day retries the same 20 (the unchanged ones skip).

## PER-KEY ROLLBACK

`s3://opal-data-harvest` versioning reads `Enabled` (`s3api get-bucket-versioning`, read 2026-10-16). For a key the act overwrote: restore its previous version by copying it back (one `copy-object` per key, the prior version id read from `list-object-versions` for that key; the existence of a prior version for each of the 20 names' keys is NOT read here); for a key the act created: delete it (a delete marker; the earlier absence is restored). Disable the task (`schtasks /Change /ENABLE` to `/DISABLE`) to stop later fires; it needs no code change. The spend is not recoverable.

## WHAT THIS HALF DOES NOT SIGN

Nothing about the management or scores tasks; nothing about lifting the cap (a later act); nothing about drafting and posture runners (round 108 item 4).
