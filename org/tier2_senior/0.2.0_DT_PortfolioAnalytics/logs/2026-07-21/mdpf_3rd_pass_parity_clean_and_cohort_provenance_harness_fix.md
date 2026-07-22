# MDPF flip 3rd-pass: date-joined parity leg CLEAN + cohort_provenance harness gap found/fixed

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~2346Z -> 0008Z 07-22)
**Window:** fresh re-instantiation (MSTR respawn for the MDPF flip 3-pass) -> leg CLEAN + reported

## Summary
Respawned by MSTR (COO-requested) to run the confirming 3rd pass of the MDPF flip. DS closed the
producer long-pole (coherent-9 staged @d0575b280). Re-grounded via GIT (not memory): found the scope had
flipped back after my last session (A2 aum-timeseries re-entered as a revamp-native Option-Y artifact; A1
aum-metrics landed), so my harness @597712d8f (8-key, A2 removed) was STALE vs the blessed exact-9. Confirmed
leg ownership + got the manifest from CTO (leg NOT reassigned). Verified INDEPENDENTLY -- did not assume
CTO's predicted 0-unexplained -- and the run CAUGHT a real harness gap: my SHAPE_EXEMPT_ROOTS lacked
cohort_provenance (DS wired it @7e0320cc0 after my last harness session; the ledger + CTO require it EXEMPT),
so 49f+inflection aggregates first SHAPE_FAIL'd on the intended cohort_provenance extra. Fixed + regression.
Post-fix: DATE-JOIN GATE all NAMED_DELTA_PASS 0-unexplained + coherence 3/3 + A1/A2 field-identity PASS. My
leg CLEAN -> 3/3 (with CTO S3 re-verify + CVO re-derive both clean). Reported CTO(gate)+COO+CVO.

## What happened
1. **Startup:** /watcher (Monitor b12gqaq5y), registered PID 15888, wrote LD-0290 serial file, audit-archive
   ran (non-exec defer), comp-graph context. Identity clean -- NOT REGISTERED at start, no PID/orphan
   conflict (memory's "0.2.0_DT KILLED 07-20" is consistent with a clean re-instantiation).
2. **Re-ground (git):** DS coherent-9 @d0575b280 (9 keys staged gold/mdpf_revamp/*, ETag-verified,
   data-neutral so N=3 preserved). Mechanism = exact-9 (CTO 233555Z). Scope divergence found: my harness was
   8-key (A2 removed per my own ~2034Z 9->8 ruling, when A2 was FE-derived); A2 re-entered Option-Y
   @dee1d6645 (Andrew 221233Z + CTO co-sign @b4e9d0e17).
3. **Leg-confirm + manifest (CTO):** CTO confirmed the leg is MINE (not reassigned) + gave the 9-ETag manifest
   + per-key treatment (aggregates date-join / A4 prior-pass holds / A1 quarterly field-identity / A2
   date-join-vs-served NAMED +3.07% + freshness, CVO-reconciled). COO independently confirmed ownership.
4. **Ground-truth the stage:** live ListObjectsV2 -- all 9 blessed ETags == CTO manifest exactly (single-part
   MD5). Path analysis: aggregates/A4/account_dist use {firm}/{artifact}; A1/A2 use portfolios/{hyphen}
   (field-identity, don't fit the date-join registry path convention).
5. **Registry re-align:** removed aum_metrics/global from the date-join value registry (A1 now staged at a
   non-conforming path + no ledger -> would mis-resolve PUBLISHED_ABSENT or manufacture UNEXPLAINED).
6. **Ran the leg -> FINDING:** 49f+inflection aggregates SHAPE_FAIL on `cohort_provenance[].model/custody`.
   Diagnosis: my instrument, not the data. SHAPE_EXEMPT_ROOTS = {meta, source_vintage_last} lacked
   cohort_provenance; the ledger `harness_requirement` + CTO 235117Z require it EXEMPT (source-path-derived,
   FE-unconsumed, CVO lineage-verifies separately; global omits it -> only 49f/inflection failed).
7. **Fix (@93382362c):** added cohort_provenance to SHAPE_EXEMPT_ROOTS (root-only -> exempt from BOTH shape
   via _shape_exempt AND value via _provenance_value_exempt; a numeric data leaf is STILL caught) + docstring
   + self-test regression (exempt extra shape-OK; a real data extra STILL fails). self-test PASS. Re-ran ->
   all date-join artifacts NAMED_DELTA_PASS 0-unexplained.
8. **A1/A2 field-identity:** independent key-set/shape read. A1 shape_identical 48/48; A2 shape_identical
   26/26 + freshness recovery confirmed (staged periods[-1]=2026-07-20 vs served frozen 2026-05-29).
9. **Committed + pushed** @93382362c (HEAD==origin/CLOUD). **Reported** CTO (verdict + gate + the
   cohort_provenance cross-check flag), COO, CVO.

## Verification (actual harness output, post-fix, `--all --published-prefix gold/mdpf_revamp --ledger <HEAD>`)
```
[NAMED_DELTA_PASS] aggregate_aua_timeseries/global (ledger:10)        # 0 unexplained
[NAMED_DELTA_PASS] aggregate_aua_timeseries/49financial (ledger:8)    # 0 unexplained (was SHAPE_FAIL pre-fix)
[NAMED_DELTA_PASS] aggregate_aua_timeseries/inflection (ledger:10)    # 0 unexplained (was SHAPE_FAIL pre-fix)
[UNEXPLAINED_DELTA] account_distribution/49financial (ledger:0)       # replace-lane drift, UNGATED (CTO ruling 1)
[PASS] account_distribution/inflection (ledger:0)
[NAMED_DELTA_PASS] non_model_assets/global (ledger:12)                # A4, 0 unexplained
[UNEXPLAINED_DELTA] account_distribution/global (ledger:0)            # replace-lane drift, UNGATED
[COHERENCE_PASS] frontier_coherence/49financial (funded models:5)
[COHERENCE_PASS] frontier_coherence/global (funded models:7)
[COHERENCE_PASS] frontier_coherence/inflection (funded models:7)
```
Live stage ETags (== CTO manifest 235117Z): agg 49f=a2e87f31 / inflection=7ab6e93e / global=1b52211f;
A4 non_model=7ef32112; account_dist 49f=865919f2 / inflection=afb964c4 / global=b946d836; A1=d69ac96a;
A2=38e9e8d4. Field-identity: A1 48/48 paths, A2 26/26 + freshness 07-20 vs 05-29.

## Blockers
None. My leg is delivered + reported. The 3-pass GATE declaration rests with CTO (owns the verdict + the
gold->portal publish trigger); downstream (render-check + COO re-co-sign + AE flip) waits on CTO's gate, not
on me. Not assumption-blocked.

## Current State (zero-context handoff)
- **DT date-joined parity leg = CLEAN.** Harness `org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/
  mdpf_parity_check.py` @93382362c (CLOUD, HEAD==origin). self-test PASS. SHAPE_EXEMPT_ROOTS now
  {meta, source_vintage_last, cohort_provenance}. Registry = date-join set (3 aggregates + A4 + account_dist
  x3); A1/A2 handled as field-identity (documented in-file, ~L102).
- **Ledger** (authoritative, HEAD): `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/
  MDPF_REVAMP_named_delta_ledger.json` (v2, per-firm windows + _date_axis; harness_requirement names the
  cohort_provenance exemption).
- **3-pass:** DT (this leg) CLEAN + CTO S3 re-verify CLEAN + CVO re-derive CLEAN = 3/3. CTO to declare.
- **Cross-check flagged to CTO+CVO:** if their legs do any SHAPE compare, confirm they also exempt
  cohort_provenance (else same false shape-fail on 49f/inflection); value/re-derive-only -> N/A.

## Next Steps
- **[1.0.0_SA_CTO]** declare the 3/3 gate -> release render-check + the gold->portal publish trigger; route
  any rework to me.
- **[3.0.0_SA_CVO]** owns the cohort_provenance LINEAGE-verify (map == read-paths) -- my leg treats it EXEMPT,
  not lineage-verified. Confirm the shape-exemption cross-check if applicable.
- **[0.2.0_DT]** event-driven: turn any rework same-turn; on CTO's scheduled-cycle signal run per-cycle parity
  for the N=3 streak (still SCHEDULED-only; this pass is pre-proof correctness, not a streak cycle). Reachable
  (Monitor b12gqaq5y). No crons.

## MCP traffic
~6 handled. IN: CTO leg-confirm + manifest (235117Z); COO ownership-confirm (235159Z). OUT: CTO leg/manifest
request + ACK + VERDICT (3 sends); COO + CVO verdict reports. RAVC: CTO request opened+closed (manifest ->
verdict with evidence); my leg reported to the gate owner.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `mdpf_parity_check.py --self-test` | PASS | pre-edit + post-cohort_provenance-fix; new regression green |
| `mdpf_parity_check.py --all --published-prefix gold/mdpf_revamp --ledger <HEAD>` | PASS (gate) | date-join all NAMED_DELTA_PASS 0-unexpl + coherence 3/3; account_dist UNGATED drift |
| `aws s3api list-objects-v2` (rail-checked) | PASS | 9 staged ETags == CTO manifest, exact per-key (13b/13c bytes control) |
| field-identity read (boto3, Rule-21 carve-out) | PASS | A1 48/48, A2 26/26 + freshness 07-20 vs 05-29 |
| safe-commit (surface-check + risk-reflex) | PASS | @93382362c; no critical surface; reflex CLEAN (map STALE 185.7h, measured) |
| commit-gate (py_compile + ruff py39) | PASS | harness .py compiles; Rule-15 future-annotations present |

**What worked:** verifying INDEPENDENTLY (not assuming CTO's predicted 0-unexplained) caught the
cohort_provenance shape-exemption gap before it read as a false SHAPE_FAIL -- the "false premise answered ON"
trap avoided. Ground-truthing the 9 ETags before running parity confirmed I was checking the blessed bytes.
**What failed:** nothing functionally; the initial SHAPE_FAIL was the instrument correctly reporting its own
stale exemption set, then fixed.
**Gap found:** SHAPE_EXEMPT_ROOTS lagged the ledger -- CTO assumed the "BUG-1 exemption" already covered
cohort_provenance, but BUG-1 only covered meta/source_vintage_last. The ledger stated the requirement; the
harness didn't do it. Closed + regression-locked.
