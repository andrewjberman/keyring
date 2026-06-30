# ADVI_BREAKS TO-1 (INFLECTION) — stub producer source-ID

**archetype:** DIAGNOSE

**Serial:** 0.4.0_DS_ClientPlatform~A · **Date:** 2026-06-30 · **TO:** ADVI_BREAKS.TO-1 (inf, DIAGNOSE, READ-ONLY, P0)
**GO:** 2.0.0_SA_COO 20260630T130509Z · **PRD:** docs/architecture/ADVI_BREAKS_PRD.md

## Mandate
Source-confirm the THIRD writer (132B flat stub) of `s3://opal-data-inf/platinum/firm/header_metrics.json`,
why it re-fired off-cadence 06-29 eve, why no 06-30 refresh, and whether it should write this key at all.
READ-ONLY — TO-2 fix is CTO+COO-gated; not applied.

## Findings (SOURCE + LIVE-S3 grounded)

1. **STUB PRODUCER — SOURCE-CONFIRMED (refutes PRD §2):** `data/inf/scripts/gold/INF_D_00.portal_aggregates.py`
   - L71 `HEADER_METRICS_KEY = {OUTPUT_PREFIX}firm/header_metrics.json` (OUTPUT_PREFIX default `platinum/`)
   - L885-891 builds the exact flat shape `{firm_id, generated_at, data_as_of, total_aua, client_count}` —
     no `total` nest, no NNA windows, no `account_count`, no `firm_name`
   - L898 `_write_json_s3(header_metrics, HEADER_METRICS_KEY)` — `separators=(',',':')` compact + AES256 → ~132 B
   - **PRD §2 is WRONG** where it states INF_D_00:898 emits the RICH shape / has NO stub path and calls the
     stub a "distinct THIRD writer." L898 IS the stub write; the stub is INF_D_00's own `main()` `--upload` path.

2. **RICH (intended) writer of the same key:** `INF_D_04.client_portal_summary.py` L1136 `build_header_metrics`
   → L1287 write = `HeaderMetricsResponse` (28830 B). So the key has TWO in-chain writers (INF_D_00 stub +
   INF_D_04 rich). `inf-portal-publisher` writes `header_metrics_FRESH.json` (different key) — NOT this key.

3. **Daily race — SOURCE-CONFIRMED, structural:** `orion-gold-dispatch.sh` chains (FULL/INCREMENTAL/GOLD_D)
   all order `...INF_D_00...INF_D_04 INF_09...` — INF_D_00 always BEFORE INF_D_04. Normal full run: stub
   ~14:29 then rich ~14:34 LAST → rich wins. Live versions confirm 132→28830 each day 06-25..06-29.

4. **Why the stub won 06-29 eve:** stub becomes last-writer ONLY when INF_D_00 runs WITHOUT a trailing
   INF_D_04. Dispatch supports exactly that (`--single INF_D_00` / `--from INF_D_00`, dispatch L18/L971/L1064).
   Live `list-object-versions`: three 132B writes 21:29:20 / 21:40:30 / 22:07:10Z, no rich after → three
   INF_D_00-only invocations. EXACT invocation principal/source = 0.7.0_AE CloudTrail lane (paired; INFERRED
   on my side these were single/partial INF_D_00 runs).

5. **No 06-30 refresh:** ZERO writes after 06-29 22:07 → the 06-30 morning gold chain did not fire at all;
   producer not at fault for content (never invoked). Trigger-health (F-axis) = AE lane. Served frozen on
   the 06-29 22:07 stub (`total_aua` 202,582,215.84 / `data_as_of` 2026-06-29 — confirmed via live get-object;
   live body = `{"firm_id":"inflection","generated_at":"2026-06-29T22:07:08Z","data_as_of":"2026-06-29","total_aua":202582215.84,"client_count":300}`).

6. **Should INF_D_00 write this key? NO** (TO-2 recommendation): its header_metrics is a degenerate flat
   5-key subset of INF_D_04's rich response on the same served key; only effect is a clobber hazard. Clean
   fix = REMOVE the INF_D_00 header_metrics emit (L885-891 dict + L898 write); INF_D_00 keeps clients_tab +
   filters/dimensions. Plus PRD's size/shape gate as defense-in-depth + INF_D_04 authoritative-last.

## Disposition
RAVC'd to COO (primary) + CTO (CC, PRD §2 amend). AE paired on CloudTrail principal + 06-30 trigger-health.
Rule 22: stub identity SOURCE-CONFIRMED; re-fire principal + no-06-30-trigger root remain AE-lane (INFERRED until AE confirms). No prod write fired.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which "..."` | route to find the data_contract + header_metrics writers | routed to on-rails comp-grep; located targets |
| `comp-grep header_metrics` / `platinum/firm/header_metrics.json` | enumerate every writer of the served key | found INF_D_00:898 + INF_D_04:2495 (inf), plus BD/COT analogues; the draft brief named INF_D_00 as the flat stub (line-drifted but claim true) |
| `pipescript advi-inf` | inf chain map / writers of the served key | confirmed inf-portal-publisher writes `header_metrics_fresh` (distinct key), narrowing the plain-key writers to INF_D_00 + INF_D_04 |
| raw `aws s3api get-object`/`list-object-versions` | independently ground LIVE served object + version-size forensic | rail-checked marker (version-byte history is not a comp surface); confirmed 132B stub current + the daily-race + 06-29-eve flip + zero-06-30 |

DS minimum `comp-pipescript io` not run: this TO is READ-ONLY diagnosis, no gold script was edited/run — used `pipescript advi-inf` for the chain map instead.
