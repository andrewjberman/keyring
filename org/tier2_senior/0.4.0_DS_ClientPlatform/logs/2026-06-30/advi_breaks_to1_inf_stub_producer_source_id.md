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

## Addendum — trigger trace tail (post-acceptance, CTO+COO requested; READ-ONLY)

Both RAVCs ACCEPTED (CTO 131322Z, COO 131327Z); PRD §2 corrected, TO-1 cert-eligible, TO-2 recommendation
endorsed-but-gated. Both asked for the remaining read-only trace tail. Source-side grounding (AE owns the
live CloudTrail/CW confirm):

- **Item #2 (no 06-30 chain fire) — TEMPERED, premature to call broken.** `infra/aws/terraform/inf-pipeline/eventbridge.tf`:
  inf morning gold trigger = PRIMARY event-driven (INFETL.SILVER-AGGREGATOR ~13:00 UTC, gated on 06-30 bronze)
  + FALLBACK `inf_canonical_prices_daily` `cron(0 14 * * ? *)` (14:00 UTC, ENABLED, target inf-gold-trigger, DLQ
  inf-gold-trigger-dlq). My S3 check was ~13:14 UTC — BEFORE the 14:00 fallback; prior-day rich writes land
  ~14:29-14:34Z (after the trigger). So "zero 06-30 writes" was not yet conclusive of a broken trigger (Rule 22).
  Served staleness now is real, but the morning window is still open. AE to confirm post-14:00Z.
- **Item #1 (what kicked the 3 INF_D_00-only evening runs) — NARROWED.** No committed code path invokes
  `--single INF_D_00` / `--from INF_D_00` (grep data/ + infra/ = doc-comment hits only). Not a scheduled inf
  rule → AE's principal hunt targets manual SSM/console runner exec or a non-inf (canonical/SSOT 06-29-eve)
  job kicking an inf partial. Runner pulls orion-gold-dispatch.sh from `s3://opal-data-inf/code/gold/` (EC2_MANIFEST.json:307).
- **Net:** a normal 06-30 chain fire self-corrects served to rich (stub-then-rich, rich wins); the durable risk
  is the off-cadence INF_D_00-only re-runs, which TO-2 (remove the stub emit) kills regardless.

Addendum RAVC'd to COO + AE (131557Z / 131607Z).

## TO-1 CLOSE — both legs converged (DS source + AE forensic)

AE infra forensic (0.7.0_AE 132129Z) fully converges with the DS source map:
- **No-06-30-break — RESOLVED:** primary event-path fired 06-30 13:01Z (runner i-0ed5 launched; dispatch-lock
  `mode=full source=aggregator`); chain in ~88-min compute; D_00/D_04 header writes DUE ~14:29-14:34Z. NOT a
  trigger break — my temper confirmed and upgraded (didn't even need the 14:00 fallback).
- **06-29-eve clobber principal:** CloudTrail excludes the scheduled inf-gold path AND in-instance SSM; only
  Andrew-local boto3 write-then-readback in-window during his own 06-29-eve canonical/SSOT bootstrap (3
  canonical-schwab-runner instances 20:17-20:32Z). → STRONGLY-INDICATED manual `INF_D_00 --upload` one-off,
  NOT recurring automation. Rule-22 caveat: PutObject principal UNVERIFIABLE-by-log (org trail S3 data-event
  selector = ReadOnly + S3 server-access-logging OFF on opal-data-inf) — decisively excludes scheduled, can't
  positively name principal → TO-6 observability-gap input (a data-event-selector/access-logging fix).
- **Net:** inf daily chain is HEALTHY and self-corrects served→rich ~14:30Z today (stub-then-rich, rich wins).
  The 06-29 freeze was a transient one-off. TO-2 (emit-removal + shape gate) remains the DURABLE fix — kills
  the manual-re-clobber class.

## TO-2 — STAGED + READY (CTO arch-approved 131626Z; HELD for Andrew-GO via COO)

Full validated diff: `scratchpad/ADVI_BREAKS_TO2_inf_staged_patch.md`. Two files:
- INF_D_00.portal_aggregates.py: REMOVE the header_metrics emit (thin dict L885-891 + write L898 + dry-run-log
  + comment unused const) → INF_D_04 sole/authoritative writer.
- INF_D_04.client_portal_summary.py: ADD served-key shape gate before the PUT (require firm_name + nested
  total{aua} + dates; ValueError on thin/stub) — defense-in-depth.
- Consumer-safety VERIFIED (comp-pipescript io): consumer = getHeaderMetrics→ClientsTab; INF_D_04 rich header
  preserves the legacy flat mirrors (total_aua/client_count/account_count L1276-1281) → ClientsTab reads a
  SUPERSET of the stub, ZERO regression.
- On-GO: apply → ds-commit-gate → comp-pipescript io re-confirm → safe-commit → `aws s3 cp` both to
  s3://opal-data-inf/code/gold/ → validate on next nightly (NO ad-hoc run) → CVO re-sweep B/C/E/F.
- Background watch `babvs3fbd` on the served key independently confirms the ~14:30Z rich write.

## inf VALUE DEFECT (COO new-priority -> Andrew INGESTION reframe -> Andrew-CONFIRMED downstream)

COO dispatched the +$1.72M inf AUA over-statement (served 06-29 $202,711,894.29 vs Orion $200.99M).
Andrew then reframed to "ingestion froze ~Friday"; I ground-truthed live and Andrew CONFIRMED the result.

GROUNDED (live S3 sums; content-as-of via the VALUE test, which beats mtime per the cot trap):
- silver/api_dims/positions_mv per snapshot_date = DISTINCT daily values, each ties Orion:
  06-27/06-28 $202,582,215.84 (weekend carry, expected identical) | 06-29 $200,987,115.59 (=Orion 06-29)
  | 06-30 $202,125,678.08 (=Orion 06-30 $202.13M). A frozen-Friday file would sum ~$203.0M; it does NOT.
  => positions ingestion CONTENT is FRESH + CORRECT, not frozen. **Andrew-confirmed** ("getting to
  202.13m today = we are pulling the correct data").
- THE DEFECT is DOWNSTREAM: served 06-29 $202,711,894.29 = gold/canonical/holdings_2026-06-27 AND _06-28
  BYTE-IDENTICAL (11480 rows, pre-short-fix = silver +$129,678 from the 8 dropped shorts). INF_D_04
  load_latest_holdings() (L401) picks the MAX-date GOLD holdings partition; on the 06-29 run no fresh
  06-29 GOLD partition existed at D-stage, so it computed off the stale 06-28 weekend partition. The
  GOLD-canonical-holdings layer did not advance on that scheduled path — NOT ingestion.
- Old +$1.72M decomposition: ~$1.59M stale-gold-partition (06-28 vs 06-29) + ~$0.13M pre-fix short-drop
  (already fixed 07bc375d2; takes effect on the next clean build).
- FRAGILITY (latent): load_latest_holdings picks the GLOBAL max-date partition, so if a day's B-stage
  fails but D-stage still runs, D publishes a STALE partition with a fresh generated_at = false freshness
  (exactly the 06-29 pattern). Worth a freshness/as-of assert (TO-6 class).
- TODAY: silver 06-30 fresh ($202.13M); gold holdings_06-30 PENDING (chain fired 13:01Z, due ~14:30Z).
  Once it builds, load_latest picks 06-30 -> served self-corrects to ~$202.13M. VERIFYING at ~14:30Z
  (bg watch babvs3fbd on the served key + a value sum on gold holdings_06-30).
- Open (partly unrecoverable — my 06-29 manual 21:26Z pull overwrote the scheduled silver partition):
  whether the 06-29 SCHEDULED 12:50Z pull/B-stage failed to land a 06-29 gold partition (freeze-day),
  which is why load_latest fell back to 06-28. Today's run is the recurrence test.
- Pre-existing separate: inf_silver_accounts_dim FAIL (stale 2026-04-29, read by INF_D_00) — noted, predates Friday.

RAVC'd COO + CVO (CC CTO). Pairs with CVO's Andrew-commissioned 3-pipeline ingestion->served /draw.

### Freeze-day root (partition forensic — LastModified + per-partition market_value.sum)
- The 06-29 SCHEDULED chain rewrote gold holdings for 06-20..06-28 in ONE 14:03:3x-42Z batch; MAX-date =
  holdings_06-28 ($202,711,894.29, 11480 rows). It produced NO holdings_06-29. The only 06-29 partition is
  MINE (LM 21:39:41Z, the manual 21:26Z pull; $200,987,115.59, 11416 rows, post-short-fix).
- => at the 14:34Z D-stage, INF_D_04.load_latest_holdings() picked 06-28 (stale) = served $202,711,894.29.
- ROOT: no 06-29 silver positions_mv partition existed at the 14:03Z gold build -> INF_B_00 (builds one gold
  partition per silver snapshot_date it finds) maxed at 06-28. The scheduled 12:50Z pull did not land a
  06-29-dated silver partition that day (the exact pull failure = runner/CW logs, AE lane).
- RECURRENCE: recurs ANY day the scheduled pull fails to land a current-day silver partition. Durable defect
  (flagged 0.8.0~B + CTO): load_latest_holdings SILENTLY serves the prior partition as fresh -> fail-loud /
  alarm on a missing current-day partition (TO-6 guard).
- Per-date sums are all DISTINCT/plausible (06-24 $202.32M, 06-25 $202.38M, 06-27/28 $202.71M weekend,
  06-29 $200.99M) -> content is not frozen; a current-day partition was MISSING.
- SELF-HEAL (in progress): today silver 06-30 landed ($202.13M); gold holdings_06-30 due ~14:30Z; once built,
  load_latest picks 06-30 -> served ~$202.13M. Verifying via bg watch babvs3fbd + a value sum at the D_04 write.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which "..."` | route to find the data_contract + header_metrics writers | routed to on-rails comp-grep; located targets |
| `comp-grep header_metrics` / `platinum/firm/header_metrics.json` | enumerate every writer of the served key | found INF_D_00:898 + INF_D_04:2495 (inf), plus BD/COT analogues; the draft brief named INF_D_00 as the flat stub (line-drifted but claim true) |
| `pipescript advi-inf` | inf chain map / writers of the served key | confirmed inf-portal-publisher writes `header_metrics_fresh` (distinct key), narrowing the plain-key writers to INF_D_00 + INF_D_04 |
| raw `aws s3api get-object`/`list-object-versions` | independently ground LIVE served object + version-size forensic | rail-checked marker (version-byte history is not a comp surface); confirmed 132B stub current + the daily-race + 06-29-eve flip + zero-06-30 |
| `comp-pipescript io INF_D_00` / `INF_D_04` | DS-mandated pre-edit check for TO-2 staging | surfaced the consumer (getHeaderMetrics→ClientsTab) + confirmed INF_D_00 writes the key as `(terminal)` and INF_D_04 also writes it — the two-writer race; drove the consumer-safety verdict |

DS `comp-pipescript io` run on both gold scripts as part of TO-2 staging (consumer + column-gap surface). Diagnosis phase (TO-1) was read-only — `pipescript advi-inf` carried the chain map there.
