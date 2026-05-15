# Session — Inflection live-portal data-drift incident (Andrew-direct)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-15
**Type:** Incident investigation — Andrew watching the live (opalinvest) Inflection portal
**Co-investigator:** 0.4.0_DS_ClientPlatform~A (gold-side root causes)
**Status:** Root causes identified; gold fixes pending DS~A + a co-landing chain re-run. No DE code shipped this session.

---

## Incident

Andrew on the LIVE Inflection portal reported, ~2:54pm ET:
1. Segment Analytics showing 204M AUA vs main view 205M.
2. Washington accounts jumped 685 -> 744.
3. Subsequently: "slippage between snapshot / radial / header" surfaces — internally inconsistent counts/totals — "not acceptable."

## Trigger

On-demand full Inflection gold chain `chain_full_20260515_175733` ran 17:57:34Z -> ~18:56Z
(full A->D rebuild, started INF_S_00 canonical-prices rebuild, synced 156 gold scripts). It
regenerated every `platinum/firm/` artifact on `opal-data-inf` at 18:53-18:54Z. That is the
"updated 2:54pm ET" stamp.

## Findings (verified)

### F1 — "204M vs 205M" = a real $787K backend inconsistency, NOT cache
The same chain emitted the firm's current AUA as two different numbers:
- **Snapshot family** (`header_metrics.json`, `partner_analytics.json`, geo donut total) = **$203,845,242.41** — canonical (Andrew-confirmed correct).
- **Timeseries family** (`timeseries_overview.json` aua.{monthly,quarterly,annually}[-1]; `cumulative_chart.json` geo.data[-1]) = **$204,632,759.83** — wrong, +$787,517.42.

The Continuous-view Segment Analytics panel + the Assets Overview header AUA read the
timeseries family -> they show "205M". Snapshot donut reads the snapshot family -> "204M".
Confirmed not cache: Andrew tested incognito + AE 0.6.1 ran CloudFront invalidation
`IBM4YGAK0CJZ6ADS4MGADDM49U` (Completed 19:31:52Z) — 205M persisted because the wrong
number is *inside* the fresh artifact.

Root (DS~A): the 06:00 cron produced a **defective short holdings build**
(`gold/canonical/holdings_2026-05-15.parquet` v1 = 801 accts, mv $204,632,760); the 17:57Z
full chain produced the correct holdings (865 accts, $203,845,242). The timeseries family is
sourced from the defective 06:00-derived value; the snapshot family from the 17:57Z rebuild.

### F2 — Washington 685 -> 744: 744 is CORRECT
DS~A S3 object-version evidence: 685 came from the defective 06:00 short holdings; 744 from
the correct 17:57Z holdings. INF_D_04 geo-emitter code unchanged today. 744 = account-grain
canonical. Not drift, not a methodology change.

### F3 — WA state (744) != Σ cities (515): top-N city cap
`INF_D_04.client_portal_summary.py` `_build_geo_view` (L120 `GEO_TOP_N_CITIES_PER_STATE=10`,
L2200 `.head(top_n_cities)`) emits only the top-10 cities per state by AUA. WA has ~55 city
strings; 45 cities / 229 accounts ranked #11+ are dropped from the city breakdown but still
counted in the state total. WA is the only state affected (only state with >10 cities).
Secondary: city strings are not normalized ("Snohomish"/"SNOHOMISH", "Lynnwood"/"Lynwood").

### F4 — count-reconciliation defects in INF_D_04 (DS~A classified)
- **A** (city cap, = F3): real bug — fix = emit city-grain "Other Cities" remainder bucket.
- **B** (histogram $1K floor, 865 accts -> 770 plotted): floor intentional; silent exclusion is the bug — fix = emit `plotted_count` + `excluded_count` (DE field-name sign-off given).
- **C** (client_count 321 geo-merge vs 307 accounts_dim): real bug, dual source of truth — 307 canonical; needs a CTO ruling.
- **D** (radial_12m AUA sums $2.2M short of total): not a bug — structural 12m-lifecycle partial decomposition; relabel.

## Postmortem — DE error this session

I reported the WA 229-account gap as "definitively null-city-but-WA-state" — it was an
**inference from the artifact** (saw 10 cities, no no_city key) labelled as verified. I did
not check the top-N cap and did not verify at account level. DS~A's account-level merge
reproduction disproved it (0 null-city accounts; the 229 are in 45 real cities past the
top-10 cap). Corrected to Andrew. Lesson: artifact-shape inference != account-level
verification; do not present an inference as "definitive." (Sister to the audit-completeness
and docstring-constraint memories.)

## Coordination ledger

| Dir | Agent | Item |
|-----|-------|------|
| DE -> AE 0.6.1 | CloudFront invalidation — fired + Completed 19:31:52Z (`IBM4YGAK0CJZ6ADS4MGADDM49U`) |
| DE <-> DS~A | Co-investigation; DS~A owns gold root causes + INF_D_04 patch; flip-flopped top-N->null-city->top-N, final = top-N (account-level verified) |
| DE -> COO | ADVI_BIWNDW.001 GO acked — pickup confirmed, queued behind this incident |

## Current State

| Item | Status |
|------|--------|
| Incident | Root-caused; gold fixes pending DS~A + co-landing chain re-run |
| Canonical firm AUA today | $203,845,242.41 (204M) — snapshot family correct |
| 205M surfaces | Timeseries family carries defective 06:00-holdings value; fix pending |
| WA 744 | Correct |
| INF_D_04 defects A/B/C/D | Classified; DS~A surfacing a TO to COO |
| ADVI_BIWNDW.001 (DE FE window-coverage) | GO received; not started — queued behind incident |
| Watcher | LIVE |

## Next Steps

- **[DS~A]** Pin the gold script that builds `timeseries_overview.json` + `cumulative_chart.json`
  current-period AUA point; fix it to source the 17:57Z-class holdings rebuild, not the
  06:00-cron value. This is the live "205M" fix.
- **[DS~A]** INF_D_04 `_build_geo_view` patch: (A) city-grain "Other Cities" remainder bucket
  so state == Σ cities; (B) histogram `plotted_count`/`excluded_count` emit; city-string
  normalization. One low-risk patch.
- **[AE 0.6.1 / 0.7.0]** Own a separate item: the 06:00 cron systematically under-builds
  `gold/canonical/holdings_{date}.parquet` (05-14 + 05-15 both short, corrected only by a
  later full chain). Recurring defect — root-cause the cron chain-mode.
- **[CTO]** Rule Defect C — canonical firm `client_count`: 307 (accounts_dim) vs 321
  (geo holdings-merge). DE + DS~A both recommend 307.
- **[COO]** Author the INF_D_04 count-reconciliation patch TO (DS~A to take); co-sequence the
  gold fixes into the INFGRO/BIWNDW co-landing chain run so one cycle ships everything.
- **[DE — me]** (1) Execute ADVI_BIWNDW.001 (FE-1 max:'MAX' / FE-2 Inflection window-lift /
  FE-4 explicit unavailable-window state) once the incident stabilizes — FE-only, unblocked.
  (2) Build the FE surface->field map (which panel reads which count field) for the
  count-reconciliation work. (3) After the co-landing chain re-runs with the gold fixes,
  re-verify the live portal reconciles (snapshot == timeseries == header == radial).
- **[DE -> Andrew]** Converge the single joint incident writeup with DS~A once the
  timeseries-source script is pinned.
