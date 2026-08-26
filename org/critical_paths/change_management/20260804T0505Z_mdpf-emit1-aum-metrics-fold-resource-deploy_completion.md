# Deploy completion — EMIT-1: aum-metrics builder, fold re-source (code-plane; chain wiring pends AE)

**Status:** HELD-VERIFY-PENDING -- owner: 0.2.0_DS_PortfolioAnalytics -- re-read: the next SCHEDULED v3-window run

> Re-stamped 2026-08-26 by `2.0.0_SA_COO`. This entry carried **no `**Status:**` line at all**, so a status-classifying reader found none and reported it OPEN for 530h. **Its own body gives the state: `CLOSE 20260804T1552Z -- artifact plane 4/4`, all four scopes serving, live-verified -- and *"acceptance leg 1 (SCHEDULED run) remains the one open leg."* APPLY COMPLETE, ONE VERIFY LEG PENDING** on a named event under a named owner. `0.4.0_DT_ClientPlatform~C` identified this exact shape at 72599 and it is the entry that motivated the `HELD-VERIFY-PENDING` value (@67dc16081a). **Nothing is half-landed; this was never a stranded deploy.**

**Deployer:** 0.2.0_DS_PortfolioAnalytics · 2026-08-04 04:55–05:05Z · **Authority:** EMIT-1 TO @859ff461b + spec @90db23580 + fold re-source ruling CTO 045548Z (5 conditions).
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aum_metrics.py` → repo HEAD @5ee67e2f3 (MATCH).

## THE TIE-LAW PRINT (condition 5: both figures, never rounded; condition 1: this is a BY-CONSTRUCTION GUARD, never cross-validation)

| state | global `total.model_aum` | timeseries headline @2026-07-30 | delta |
|---|---|---|---|
| PRE-fix (two derivation rules) | $1,687,104,377.82 | $1,687,095,883.86 | **+$8,493.96** — 100% the cot leg (pair-current @07-24 $125,132,212.03 vs slice-carried @07-27 $125,123,718.07) |
| POST-fix (fold re-source) | $1,687,095,883.86 | $1,687,095,883.86 | **0.00** — BY CONSTRUCTION (shared derivation; the check survives as a plumbing/regression guard that fires only if a second derivation is ever reintroduced). THE VALUE is verified upstream by the fold's own gate battery (450-date gates, W-2b, parity) — one truth, verified once, at its source |

## The five conditions, evidenced

1. Tie reclassified — ledger cites it as BY-CONSTRUCTION GUARD (above); spec amendment CTO-side in parallel.
2. Components decompose from the SAME fold values at the frontier date; cent-exact reconcile kept (genuine internal check) — observed: 49F full $1,696,469,951.41 @07-30 + INF $142,064,669.67 @07-30 + COT $125,123,718.07 **carried@07-27** = the headline to the cent.
3. Cot component cites the slice-carried value with as_of + `carried: true` label.
4. R-4 `_assert_measured_frontier` stays the refusal path; the stale "PERMANENTLY interpolated_estimate-tainted" comments corrected in the same hunk (taint = pre-first-measured backfill window only; the guard, not the comment, is the control).
5. Both-figures discipline: this table.

**Also:** `scope` additive on all emitted docs; count law unified to the fold's `account_count_total` frontier + `count_as_of`; forced-absent honest-null leg PASS (synthetic short-history spine: q1–q3 all-None + `series_start` reason — never a zero); per-firm docs unchanged in values (49F/INF logs byte-matched the pre-edit run's figures).

## Remaining to acceptance (not this ledger's legs)

- **Chain wiring (AE/DT lane):** nothing RUNS this builder in the chain yet — one dispatch stage (`dim_mdpf_aum_metrics.py --firm all --upload`, after 6a) wires it; accrual (DECLARED aum-metrics, as_of=period) + publisher already bridge to the four platinum keys. Routed to AE sequenced with their executing wave.
- **Acceptance leg 1** (four keys from a SCHEDULED v3-window run) + **leg 5** (DE /frontend-dev on real served artifacts) follow the wiring + next fire.
- Cottonwood's own `scope` field: additive one-liner on the PAIR (my DC1 family) — rides its next touch or EMIT-2 coordination; DE reads scope gracefully-absent meanwhile.

---

## ADDENDUM 20260804T1510Z — P0 DIRECT-INVOCATION PRODUCTION FIRE (Andrew-direct 1408Z, CTO relay; COO dispatch 141156Z + serve-ruling addendum 142936Z)

**Authority:** Andrew-direct at CTO terminal ~1408-1410Z (*"push that generation end to end and water test it end to end"* + *"we cannot wait for a schedule"*) — operator-ordered direct invocation as PRODUCTION legs, superseding the schedule wait. CTO ruling 142446Z: SERVE mixed vintages; artifacts are **PRODUCTION INTERIM off the 07-31 spine**, superseded by a same-day fresh re-run after the Orion 401 fix (AE root-causing).

**What fired (this seat's legs — global + inflection; 49financial = 0.4.0_DS EMIT-2; cottonwood = the pair's, already served):**

| step | invocation | observed result |
|---|---|---|
| emitter | `dim_mdpf_aum_metrics.py --firm global --upload` (repo @1ba9301bfd = S3-deployed MATCH) | 14:53:36Z OK — `gold/mdpf_revamp/global/aum_metrics.json` + legacy `portfolios/aum-metrics.json` (dual by design) |
| emitter | `--firm inflection --upload` | 14:53:39Z OK — `gold/mdpf_revamp/inflection/aum_metrics.json` |
| accrual | `build_portal_gold_accrual.py --only portal/gold/mdpf/global/aum-metrics/2026-07-30.json` | 14:56:03Z wrote 7,766B md5 2022e7816b2b, errors=0 |
| accrual | `--only portal/gold/mdpf/inflection/aum-metrics/2026-07-30.json` | 14:56:07Z wrote 5,894B md5 76590bcaa0b8, errors=0 |
| publisher | `aws lambda invoke opal-assets-mdpf-portal-publisher` (direct; hand-run self-labels per D2/PIN-4) | rc 200 — **13/13 published, all_present=true, unrecognized=0** |

**WATER TEST (independent content reads of the SERVED artifacts, never the publisher rc):**

| leg | served key (s3://opal-data-portal-v2/) | written | size/ETag | content |
|---|---|---|---|---|
| GLOBAL | `platinum/mdpf/global/aum-metrics.json` | 2026-08-04T14:59:06Z | 5,908B / d4674de756a6d71f6e126408f2646235 | period=2026-07-30, scope=global, total.aum=$1,963,658,339.15, model_aum=$1,687,095,883.86, non_model=$276,562,455.29, accounts=8,099, q0–q3 all populated (series_start 2024-11-01), by_model=7, `_provenance` TRUE (publisher stamp, source key + vintage 2026-07-30) |
| INFLECTION | `platinum/mdpf/inflection/aum-metrics.json` | 2026-08-04T14:59:07Z | 4,306B / e881074efcd542a2dee465aa63de5d74 | period=2026-07-30, scope=inflection, total.aum=$204,775,547.30, model_aum=$142,064,669.67, non_model=$62,710,877.63, accounts=561, q0–q3 populated, by_model=7, `_provenance` TRUE (vintage 2026-07-30) |

**TIE LAW (BY-CONSTRUCTION GUARD framing per condition 1 — exercised on the SERVED pair):**
- global `model_aum` $1,687,095,883.86 == served `aggregate-aua-timeseries.model_aua` @2026-07-30 $1,687,095,883.86 — **0.00**; `total.aum` == `opal_aggregate_aua` — **0.00**; counts tie (8,099).
- inflection `model_aum` $142,064,669.67 == `model_aua` — **0.00**; `total.aum` == `partner_custody_total` $204,775,547.30 — **0.00**; counts tie (561).

**VINTAGE (COO addendum condition):** both legs period=2026-07-30 (T-1 frontier of the 07-31-built spine; spine staging keys unmodified since 2026-07-31 15:00Z). PRODUCTION INTERIM per CTO 142446Z; the post-Orion-fix fresh run supersedes.

**NEVER#4 note:** these artifacts are production by Andrew's word; **acceptance leg 1 (SCHEDULED v3-window run) remains OPEN** — this fire does not satisfy it and is not cited as schedule evidence.

**Why the 09:50 fire emitted 1-of-4 (seat-visible observables; runner-log confirmation = CTO forensics):**
1. At 09:50, `gold/mdpf_revamp/{global,inflection}/aum_metrics.json` did NOT exist (created 14:53Z by this fire; 49f staged 14:23Z by EMIT-2's hand leg) and the accrual tree carried aum-metrics ONLY for cottonwood (2026-07-24) → the publisher's listing-derived set had one aum-metrics pair → **published 1-of-4 CORRECTLY GIVEN ITS INPUTS. The publisher is not the defect.**
2. Stage 6e was wired + deployed pre-fire (dispatch on S3 01:13 ET, `--firm all --upload` at `mdpf-daily-dispatch.sh:559`) yet nothing staged — and the emitter runs GREEN NOW off the same spine inputs that existed at 09:50, so the emitter's own computation was not the blocker.
3. Spine staging keys show NO write today (07-31 15:00Z mtimes) → 6d's step-(3) global re-stage never landed either. **INFERRED mechanism (not runner-log-confirmed): the revamp chain failed AT/BEFORE its fatal 6a–6d stages (Orion-401-stale feeders) and never reached 6e; 6e's WARN-not-fatal soft-launch is designed to leave exactly the observed state if it fired and failed.** Discriminator between "chain died pre-6e" and "6e ran+failed" lives in the runner's dispatch log — CTO's lane.

**CLOSE 20260804T1552Z — artifact plane 4/4.** AE's publisher fire 15:44Z (their one-invoker leg, on my 49f stage-confirm): 14/14 published, live-verified — `platinum/mdpf/49financial/aum-metrics.json` 15:44:29Z, 4,138B, ETag c2cc3b26, period 2026-07-30, provenance in content (AE 154850Z). Orion 401 root cause per AE: overnight token 6h past its 10h TTL; fresh token landed 13:01:27Z, exp 23:02:19Z. All four scopes serve; DE Leg-4 render unblocked fabric-wide; acceptance leg 1 (SCHEDULED run) remains the one open leg.
