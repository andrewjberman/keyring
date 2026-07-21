# MDPF_REVAMP -- crash-recovery: cohort_provenance finished (the stall) + A2 built + coherent-9 STAGED (DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, DEPLOY, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-21 | **Window:** hard-close restart (~22:33Z) -> ~23:37Z

## Summary
Andrew hard-closed the prior session mid-stall and reloaded me to assess + finish. Grounded in GIT
(not memory): the hard-close stranded exactly ONE uncommitted change -- the cohort_provenance helpers
were added to the aggregate producer but NEVER WIRED (lines 687/845 still `[None]*len(dates)`). Finished
it (source-path-derived per Andrew 205026Z), then built the not-started A2 aum-timeseries producer, then
re-staged the full coherent-9 with a DATA-NEUTRALITY proof so the N=3 vintage/streak is preserved. All 9
served keys staged + ETag-verified. Producer long-pole CLOSED; 3-pass now in motion (CTO S3 re-verify +
CVO re-derive; DT respawn via COO/MSTR). Andrew was actively watching cutover readiness throughout.

## Work done
- **Startup + reorient:** /watcher (Monitor bm9586ict), registered (PID 42116), wrote the LD-0290 serial
  file (caught by the pre-push VALGATE -- I'd skipped it jumping into the assessment). Grounded the stall
  in git: `dim_mdpf_aggregate_aua_timeseries.py` modified +31 lines UNCOMMITTED (cohort_provenance helpers
  defined, not wired) = the ONLY stranded work. A1/A4 survived committed (@19d3a606d / @6a9fe4f77).
- **#4 cohort_provenance FINISHED (@7e0320cc0 + ledger @bf3ca6205):** SOURCE-PATH-DERIVED -- each cohort's
  provenance == the opal-data-assets `{source}` segment it READS FROM. Wired both firm sites: 49F
  model=SmartX(fact_model_aum_daily)/custody=Schwab(fact_rps_s2); inflection model=Eclipse(fact_portfolios_
  full)/custody=Orion(fact_assets); global omits (served does too). None only on fully-absent dates.
  Unit-verified (map exact + honest-None; ASSERTS PASS). docstring + meta note + still_pending + ledger
  _meta updated for coherence. Grounded the exact ruling from the CVO census @386e3717a first (I was
  stalling when I wrote the helpers -> re-confirmed the spec before wiring, did not trust pre-crash code).
- **#2 A2 aum-timeseries BUILT (@dee1d6645):** new `dim_mdpf_aum_timeseries.py`, sibling of A1 -- thin
  projection off the GLOBAL aggregate. Retires the self-frozen legacy clobber (served stuck at 2026-05-29;
  revamp fresh to 07-20). Grounded the served shape from the live sample: `{aggregate, by_model, periods}`,
  by_model = 5 CORE ONLY (NO SMA/blend -- verified aggregate.{aum,account_count}==sum(by_model) to the
  cent), aggregate = MODEL total (not enterprise). Built aggregate BY CONSTRUCTION as the 5-core sum to
  preserve the served internal identity. --verify-served: ALL key sets IDENTICAL (field-identity PASS);
  named value delta +3.07% @ last-common 05-29 (D-1 family). --self-test PASS.
- **#5 COHERENT-9 STAGED + verified:** re-ran the aggregate --firm all, DIFFED new DATA arrays vs the
  N=3-blessed stage BEFORE staging -> all 3 firms BYTE-IDENTICAL (no partition moved; only cohort_provenance
  + timestamps changed) = streak-neutral PROOF. Staged 3 aggregates (put_object, ETag==MD5 verified) +
  regen A1/A4 off fresh global + A2. All 9 keys present + ETag/Size verified (ListObjectsV2).
- **Reported:** CTO (coherent-9 manifest + exact-8/9 reconcile + DT-liveness flag), CVO (cohort_provenance
  source-map for lineage-verify + A2 decouple), COO (Andrew readiness). CTO CONFIRMED exact-9 + running S3
  re-verify + signaled CVO re-derive; COO resolving DT respawn via MSTR. ~A closed A4 3/3 (nothing needed).

## MCP traffic (~12 handled)
Significant: COO x3 (post-reload status check-in [Andrew "are we ready"], hygiene tip [commit incrementally],
long-pole-closed ACK + DT respawn); CTO CONFIRM exact-9 + running S3 re-verify + CVO signal; CVO carried
2 future-verifies (cohort_provenance lineage + A2/A4 decouple-survives-repoint) -- source-map reported;
~A "A4 closed 3/3, nothing needed from you". Sent: status, 4 landing reports, ACK.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| safe-commit (surface-check + risk-reflex) | 4 commits | PASS | no critical surface; reflex CLEAN each (map STALE 184h, measured) |
| commit-gate (py_compile + ds-precommit + ruff py39) | every .py edit | PASS | producers compile; Rule-15 future-annotations present |
| comp-system-gate | ledger commit | OVERRIDE (audited) | build-alongside/FE-unconsumed leaf/data-neutral; regen deferred to coherent-9 |
| aws s3api list-objects-v2 (13b, rail-checked) | coherent-9 landing verify | PASS | ETag==MD5 single-part all 9; key+ETag+Size |
| boto3 data-plane reads (served/staged JSON) | shape/neutrality grounding | n/a | off-rail per Rule 21 carve-out (no comp-tool fits served-JSON reads) |

**What worked:** the data-neutrality diff (new aggregate vs staged, DATA arrays only) PROVED the N=3 vintage
holds before staging -- the right control. **What failed:** none functionally. **Gap found:** the
comp-system-gate reads its override ONLY from `-m` argv (never the `-F` file), while the CLAUDE.md Git
PreToolUse gate DENIES `-m` carrying `$(`/backtick -- and the override must be its OWN-LINE `-m` paragraph
(sed `^` anchor). Resolved: split the commit (producer .py path doesn't trigger comp-system-gate -> clean
`-F`; ledger via a literal 2nd `-m` paragraph). Banked for the fabric.

## Files Modified
see commit messages: **7e0320cc0** (cohort_provenance wiring), **bf3ca6205** (ledger map + exempt note),
**dee1d6645** (A2 producer, new file). All authored 0.4.0_DS_ClientPlatform, pushed origin/CLOUD.

## Deployment / staging + verification (DS gold artifact -- coherent-9, one data-vintage)
| # | Key (gold/mdpf_revamp/) | ETag | Size | Staged |
|---|---|---|---|---|
| 1 | 49financial/aggregate_aua_timeseries.json | a2e87f311fd0 | 177330 | 23:30Z (cohort_provenance) |
| 2 | inflection/aggregate_aua_timeseries.json | 7ab6e93e3f3a | 151243 | 23:30Z (cohort_provenance) |
| 3 | global/aggregate_aua_timeseries.json | 1b52211f6443 | 165630 | 23:30Z (cohort_provenance) |
| 4 | global/non_model_assets.json (A4) | 7ef321124087 | 82101 | 23:30Z |
| 5 | portfolios/aum-metrics.json (A1) | d69ac96ab99a | 5079 | 23:30Z |
| 6 | portfolios/aum-timeseries.json (A2 NEW) | 38e9e8d46678 | 277985 | 23:24Z |
| 7 | 49financial/account_distribution.json | 865919f2be40 | 11451 | 19:19Z (unchanged, CTO ruled keep) |
| 8 | inflection/account_distribution.json | afb964c4d67f | 14914 | 19:19Z |
| 9 | global/account_distribution.json | b946d8364ca3 | 14953 | 19:19Z |

ETag==local MD5 verified (single-part) on the 3 aggregates staged this window. account_dist x3 kept as-is
(CTO 233555Z: coherence is by the meta-map/stable model_key, not timestamp; a re-run risks a needless
data-move).

## Blockers
None. Producer lane complete. Downstream (CTO S3 re-verify + CVO re-derive + DT respawn + AE mechanics +
render + COO re-co-sign) is in others' hands and in motion; NOT a blocker on me.

## Current State (zero-context handoff)
- **Producer long-pole CLOSED.** All 9 served keys staged + ETag-verified (table above), one DATA-vintage
  (proved byte-identical to the N=3-blessed stage; only cohort_provenance + timestamps moved).
- **cohort_provenance:** source-path-derived, LIVE. `dim_mdpf_aggregate_aua_timeseries.py`
  `_provenance_of`/`_cohort_provenance` @7e0320cc0. Map: 49F model=SmartX/custody=Schwab; inflection
  model=Eclipse/custody=Orion; global omits. Populated 49F 427 / inflection 424 (3 fully-absent -> None).
- **A2:** `data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py` (@dee1d6645). Reads ONLY the global aggregate
  (NO legacy emitter, NO portal-v2). CLI: --self-test / --verify-served / --out / --upload. 5-core,
  aggregate==sum(by_model). Staged portfolios/aum-timeseries.json.
- **Mechanism = exact-9** (CTO 233555Z): aggregate x3 + non_model(A4) + aum-metrics(A1) + aum-timeseries(A2)
  + account_distribution x3. AE builds exact-9 diffs against this set.
- **3-pass in motion:** CTO running S3 re-verify on the 9 ETags + CVO re-derive parallel; the DATA verify
  from N=3 @e17a28141 largely HOLDS (byte-identical arrays) -> the NEW surface = cohort_provenance lineage
  (CVO) + A1/A2 field-identity (CTO). DT (0.2.0) not live -> COO requesting respawn via MSTR / CTO may
  reassign the leg.

## Next Steps
- **[1.0.0_SA_CTO]** finish the pre-publish S3 re-verify on the 9 ETags; rule the DT parity leg; drive the
  cutover co-sign (CTO+COO+Andrew) when 3-pass + render clear.
- **[3.0.0_SA_CVO]** lineage-verify cohort_provenance (map reported 233405Z) + re-derive the coherent-9 +
  confirm A2/A4 decouple survives repoint.
- **[2.0.0_SA_COO]** resolve DT respawn (MSTR); relay readiness to Andrew; drive re-co-sign.
- **[0.7.0_AE_CloudOps / AE]** on CTO clear: build the exact-9 diffs + flip (repoint json/portfolios/* +
  the aggregate/account_dist served keys) + wire the parallel nightly schedule so the streak accrues.
- **[me / 0.4.0_DS_ClientPlatform]** event-driven: turn any 3-pass finding same-turn (producers are
  --self-test + validate gated; rework = fast fix + data-neutral re-stage). Rollback-ready.
- Reachable, event-driven (Monitor bm9586ict). No crons.
