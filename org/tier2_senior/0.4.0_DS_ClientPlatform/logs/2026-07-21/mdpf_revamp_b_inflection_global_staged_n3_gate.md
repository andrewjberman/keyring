# MDPF_REVAMP -- (b) inflection+global serve-real history BUILT + STAGED, N=3 gate in motion (DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-21 | **Window:** fabric-crash recovery (~14:20Z) -> ~15:53Z

## Summary
Post-crash recovery from origin/CLOUD @399e44fc6. Closed CTO gate item (a) [19/20 published-only date
enumeration], recorded+broadcast an Andrew-direct inflection ruling, then BUILT + VERIFIED + STAGED the
full (b) deliverable: inflection + global serve-real HISTORY. All 3 firms date-joined-parity clean
(0 unexplained) + internal identities PASS + @07-17 last-common ties EXACT. Staged to gold/mdpf_revamp/*,
pinged CTO -> 3-pass gate now running (DT independent parity + CTO S3 re-verify + AE publish).

## Work done
- **Recovery + startup:** /watcher (Monitor bgszef4p4), registered (PID 42464), LD-0290 serial file, read
  CTO gate verdict 135429Z FIRST (per launcher), ACK'd (CTO closed the "resend" loop on my ACK).
- **GATE ITEM (a) -- CLOSED:** enumerated the 49F aggregate date-set symmetric diff (served 429 vs my
  serve-real axis). All published-only are real NYSE trading days w/ real aum_daily data; all served-only
  are synthetic holiday-fills. Committed 4fcbef1ab. CTO ACCEPTED (0 unexplained). Surfaced the re-anchor
  catch: latest-tie must be at LAST-COMMON date, not [-1] (my frontier 07-20 > served 07-18) -- CTO
  RULED verify-at-common-date + corrected his own locked criteria.
- **ANDREW-DIRECT ruling (recorded+broadcast same turn):** "Yes it was 0, 5-15 was the beginning" (for
  inflection). Grounded independently in orion (Opal model ~$0 through 05-01 -> $97.7M @05-14). Memory
  project_mdpf_inflection_model_zero_until_may15_launch.md + broadcast CTO/COO/MSTR.
- **(b) BUILD -- inflection + global full serve-real history** (data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py):
  * inflection: model = eclipse Opal (0 pre-2026-05-15 launch per Andrew; real after), custody = deep
    orion fact_assets.currentValue, non_model = custody-model. Launch seam CLEAN (0@05-14 -> $94.5M@05-15).
  * global: date-JOINED firm-sum (not index) of 49F + inflection; opal_aggregate = 49F(model+non_model)
    + inflection(model). Shape-matched served global (dropped partner_custody_total/cohort_provenance/
    partner_name -- served global lacks them).
  * 49F axis wired to EXPLICIT canonical NYSE trading-day axis via the local _trading_day_calendar shim
    (NOT lib/ -- CTO 145638Z: lib not on runner path) + a PARITY-NEUTRAL GUARD that caught aum_daily
    carrying 2025-01-09 (Carter National Day of Mourning, NYSE CLOSED) -> axis 428->427, diff refined to
    407 common / 22 served-only / 20 published-only.
  * feed gaps emit None (D1, no interpolation): 05-21 eclipse-feed gap (bronze+silver both lack it ->
    served's value is legacy-IMPUTED; revamp honest-None is MORE correct; CTO-endorsed).
- **VERIFICATION:** internal identities PASS all i (3 firms); @07-17 ties EXACT (49F custody
  $1,665,338,126.76; inflection custody $202,375,944.55 + model $137,773,262.95 to the cent); 49F model
  @07-17 -0.093% (F2 drift, in D-3 band).
- **LEDGER v2** (MDPF_REVAMP_named_delta_ledger.json): empirical PER-LEAF bands (covering aggregate +
  by_model.*.model_value -- the miss that left 750/2653/5026 value-unexplained on first pass), inflection
  full entries, account_count None-placeholder (FLAG-2 all firms), global feed-gap/blend null_ok,
  non_model latest (workaround for a harness substring bug), _date_axis + n_dates for DT. Validated with
  DT's OWN compare() @e2bb91b4e: ALL 3 FIRMS 0 UNEXPLAINED + DATA-shape clean.
- **STAGED + verified** (ListObjectsV2 ETag==local MD5, single-part): gold/mdpf_revamp/{49financial,
  inflection,global}/aggregate_aua_timeseries.json. Pinged CTO + DT.
- **Riders:** _trading_day_calendar.py docstring honesty fix (CTO 151204Z; marked INTERIM DIVERGENT COPY);
  TO-2 scope call to CTO (spec-omits-vs-harness-includes conflict); confirmed ~A's A4 contract + merged
  A4 non_model_assets/global into the ledger.

## MCP traffic
~30+ messages, all base CTO (gate) + 0.4.0_DS~A (A4 seam/contract) + 0.2.0_DT (harness) + COO/MSTR
(Andrew-direct broadcast). Significant: CTO gate item (a) CLOSED + re-anchor RULED + (b) ACCEPTED + 05-21
ENDORSED + 4 inflection gate conditions; Andrew-direct inflection=0-until-05-15 (recorded+broadcast);
Andrew-direct trading-days-only-axis-is-fine (via ~A); DT ACK LIVE + fixing 2 harness bugs I surfaced;
~A A4 built + contract confirmed.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| safe-commit (surface-check + risk-reflex) | 6 commits | PASS | no critical surface; reflex clean each |
| commit-gate (py_compile+ds-precommit+ruff) | every .py edit | PASS | caught unused calendar_source import -> wired to meta provenance |
| comp-system-gate | 4 doc/build commits | OVERRIDE | audited system-current-override (build-alongside + ledger/deliverables, no infra/pipeline state) |
| DT mdpf_parity_check.compare() @e2bb91b4e | 3 firms x ~6 iterations | 0 UNEXPLAINED | ran DT's OWN date-joined harness on staged artifacts+ledger; caught 2 real DT-harness bugs (meta-shape false-fail + model_aua-substring-in-non_model_aua) |
Grounding via boto3 data-plane reads (silver/served/bronze provenance -- off-rail per Rule 21 carve-out;
no rich comp-tool fits parquet/served-JSON reads) + lib/_trading_day_calendar canonical NYSE axis. The
parity-neutral guard (canonical-vs-implicit axis) caught a non-trading day in the source. Gap: DT-harness
_shape_diff over-compares meta/source_vintage_last + _spec_field_hit substring-matches -- both flagged to DT.

## Files Modified
See commit messages: **4fcbef1ab** (date enum), **b0aafa8b6** (inflection+global history build),
**eb96d0549** (ledger v1 + enum refresh), **e3b2c8f6b** ((b) parity-final: account_count None + global
shape + ledger v2), **c983589f5** (Andrew-ruled axis notes), **9d21de589** (calendar docstring honesty).
Files: data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py + _trading_day_calendar.py + the ledger
+ enumeration deliverables.

## Blockers
None. (b) staged + parity-clean. N=3 verification is in others' hands: CTO S3 re-verify (pending) + DT
independent parity (running, fixing the 2 harness bugs first) + AE publish (CTO-gated). TO-2 parked on a
CTO scope ruling (non-blocking).

## Current State
- **STAGED (LIVE):** s3://opal-data-assets/gold/mdpf_revamp/{49financial,inflection,global}/aggregate_aua_timeseries.json
  (ETags 6e072745.../a9778de4.../7d574a2d...). 427 canonical trading days [2024-11-01..2026-07-20].
- **Producer:** dim_mdpf_aggregate_aua_timeseries.py (--firm all --out-dir): 49F real aum_daily model +
  full-envelope rps_s2 custody; inflection eclipse model (0 pre-05-15) + orion custody; global date-joined
  firm-sum. Feed gaps -> None (no interp). Local build ~32s (427 orion + 427 rps_s2 + ~44 eclipse partitions).
- **Ledger:** MDPF_REVAMP_named_delta_ledger.json (c983589f5) -- 3 firms date-joined 0-unexplained +
  non_model_assets/global (~A's A4, TBD ranges ~A finalizes at stage).
- **DT:** harness mdpf_parity_check.py @e2bb91b4e (date-joined); fixing BUG-1 (meta-shape exempt) + BUG-2
  (substring field-hit) then running independent parity on the staged artifacts.

## Next Steps
- **[1.0.0_SA_CTO]** run S3 re-verify (identities/ties) + trigger AE publisher (gold/mdpf_revamp/* ->
  portal/*) + rule TO-2 scope. The 3-pass gate = N=3 all 3 firms same cycle.
- **[0.2.0_DT_PortfolioAnalytics]** fix the 2 harness bugs + gate-report the independent date-joined parity
  (pointing at gold/mdpf_revamp/ via --stage-gold until AE publishes).
- **[0.4.0_DS_ClientPlatform~A]** A4 dry-run against the staged global aggregate -> finalize the TBD
  enterprise/non_model ranges -> send me to lock the ledger.
- **[me / 0.4.0_DS_ClientPlatform]** available for TO-5 (source_vintage_last from DDB, resolves the meta
  source_vintage_last shape gap) pending CTO's TO-2 ruling; respond to any CTO/DT verification findings.
- Reachable, event-driven (Monitor bgszef4p4). No crons.
