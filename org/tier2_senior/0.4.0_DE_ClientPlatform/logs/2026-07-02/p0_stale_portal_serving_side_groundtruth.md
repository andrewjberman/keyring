# Andrew-P0 stale portal pages — serving-side ground-truth (bd 49F / inf / MDPF): all 3 = ETL-production, serving layer CLEAN

**archetype:** DIAGNOSE

**Workspace CLOUD commit:** (diagnostic only — no code change; deliverable = RAVC to CVO cc COO)
**Trigger:** COO DRIVE dispatch (20260702T140955Z) — pull serving-side ground-truth for the 3 stale surfaces to feed CVO's production-vs-serving split (Rule 22). Andrew-direct P0.

## Current State

CVO's interim grounding pointed to ETL-production (bd source @06-29, INF sentinel @06-30 17:18, MDPF trigger gated). COO routed me — the ADVI/ModelPortfolios serving owner — to ground the SERVING side (what the portal ACTUALLY serves per the CF/S3 path the page reads) and rule a serving-layer contributor in/out. **Result: serving layer is FAITHFUL on all 3; every surface's staleness is upstream ETL-production. Cross-confirms CVO. No DE-lane fix.**

### Findings (grounded on served S3 mtime + internal content date — not producer self-report)

| Surface | Served artifact | Served mtime | Content `data_as_of` | Verdict |
|---|---|---|---|---|
| bd 49F | `opal-data-bd/platinum/firm/*.json` | **@07-02** 00:57–01:20 (TODAY) | **06-29** | ETL — **mtime-fresh / content-stale** |
| inf | `opal-data-inf/platinum/firm/*.json` | @07-01 05:35 | **06-30** | ETL — gold→platinum chain stuck |
| MDPF | `opal-data-portal-v2/json/mdpf/aggregate-aua-timeseries.json` | @06-25 12:42 (== build-tier) | **06-25** | ETL — build/trigger gated |

- **bd 49F — the trap:** `dashboard.json` = `{"generated_at":"2026-07-02T04:57:24Z","data_as_of":"2026-06-29",...}`. The platinum-emit RAN TODAY on stuck upstream, producing a fresh-FILE/stale-CONTENT artifact. A naive mtime-only freshness monitor calls bd "fresh" and MISSES it — the `data_as_of` field is the true vintage. Upstream (comp-freshness): `bd_silver_realized_agg` @06-29T21:46 FAIL + `bd_gold_accounts_dimension` @06-29T23:03 FAIL (rest of bd gold refreshed @07-02 ~04:xx).
- **inf:** served @07-01, content @06-30 == CVO's INF sentinel. `inf_gold_firm_mix_views` + `inf_gold_advisor_fee_efficiency` @06-30 17:1x; fresh orion silver @07-02 13:34 not yet propagated through inf gold→platinum.
- **MDPF:** served (`portal-v2/json/mdpf/`) == its build-tier source (`platinum/mdpf/`), both @06-25 12:42; content ends @06-25. Serving faithfully delivers the latest BUILT artifact; build gated since 06-25. (NB served MDPF lives in `opal-data-portal-v2`, not `opal-data-mdpf` = feeds/build tier.)

### Serving-layer contributors RULED OUT
1. **Dead/wrong-path read — NO.** Portal reads the LIVE `platinum/firm/*.json` + `portal-v2 json/mdpf/`; dead `employee_leaderboard.json` (@04-09) is NOT read by any endpoint (comp-grep 0 matches; live = `leaderboard.json` @07-02).
2. **CloudFront cache older-than-S3 — NO.** Symptom dates (bd 06-29 / inf 06-30 / MDPF 06-25) EXACTLY equal the current S3 served objects' content vintages; a stale cache would surface OLDER. Residual not exercised: a live-CF response-header read (offered to CVO).
3. **Firm-routing/wire — NO.** Served artifacts exist + correctly firm-partitioned (49financial→bd, inflection→inf).

## Decisions Made
- Framed my claims as STATE-grounded serving-layer rulings (served artifacts) + produced-STATE cross-confirmation; deferred the upstream MECHANISM (why silver-realized/trigger is stuck) to CVO's source-grounding (Rule 22 — I don't assert the ETL mechanism, only that the serving layer faithfully serves the latest produced state).
- Did NOT trigger any ad-hoc gold run; grounded purely on served/produced state.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| `comp-which "<served vintage question>"` | routed | surfaced comp-platinum / comp-cluster / pipescript |
| `comp-freshness --list` / `all` / `artifact <prefix>` | PASS/insight | produced bd/inf gold+silver state; bd_silver_realized_agg + accounts_dim @06-29 FAIL; inf firm_mix/fee @06-30 17:1x; served platinum prefix mtimes |
| `comp-grep employee_leaderboard.json portal/src/api` | 0 matches | dead-path read ruled out |
| `aws s3 ls` / `cp` (served-artifact mtime + content date) | grounded | rail-checked (comp-freshness = prefix-mtime only; no comp-tool exposes per-object listing or JSON content-vintage) |

## Next Steps
- **[3.0.0_SA_CVO]** fold my serving-side ruleout into the entangled-fix diagnosis — all 3 are ETL-production; bd's mtime-fresh/content-stale is the one that defeats mtime-only monitors.
- **[DS/AE via COO]** the actual fixes: bd upstream `silver/realized/` + `gold/dimensions/accounts_dimension` (@06-29); inf gold→platinum propagation (@06-30, orion silver @07-02 waiting); MDPF build/trigger (gated @06-25).
- **[0.4.0_DE, me]** free capacity for any POST-fix portal-side step (e.g. re-publish / CF cache-invalidate once upstream lands). Event-driven.
