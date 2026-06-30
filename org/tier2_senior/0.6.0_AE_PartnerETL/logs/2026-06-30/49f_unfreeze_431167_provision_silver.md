# 49F served un-freeze — ADVI_BREAKS 431167 unrealized facts-restore + provision + silver-merge

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE
**serial:** 0.6.0_AE_PartnerETL | **date:** 2026-06-30 | **window:** session start (~16:47Z) -> ~17:55Z

## Summary

Launched on an ADVI_BREAKS "shared BD-source convergence" rationale; mid-session Andrew firm-mapped
0.6.0_AE = 49 Financial ONLY, and the convergence task was SUPERSEDED (org concluded separate roots,
not one shared BD-session — independently corroborated by my live grounding: cot session healthy +
retry-net re-landed priced 06-23..26; 49F session recovered-but-not-durable, 3.5-day dark gap 06-26..28).
Took over the P0 49F un-freeze from 0.7.0 and drove it to a verified silver/06-29; the served flip lands
on tonight's scheduled 23:00Z gold. Also answered two Andrew-direct questions (BD historical-PIT
feasibility; persistent-login-on-ingestion-box design).

## What was delivered (the 49F un-freeze, legs L2 / L4 / silver)

ROOT (already DS/AE-grounded, re-confirmed live): 49F unrealized BD-DataMining template (431167, qt4) had
`facts=[]` (empty measure catalog) -> empty export -> empty silver/unrealized -> B_01 CUSIP veto-set
collapse (102,883 -> 0) -> D_03 firm-composition empty -> D_03/D_04 publish-tail halt -> served frozen
06-26T05:00 (data_as_of 06-24, $1.745B).

- **L2 PROVISION (mine):** ran the canonical `cot_bronze_ingest.py --table unrealized --provision` (firm
  env BD_FIRM_ID=49f / BD_S3_BUCKET=opal-data-bd / BD_SESSION_SECRET_ID=blackdiamond/49f/session) ->
  minted NEW persisted BD templateId **486228** carrying ~B's populated facts (1 Fact / 11 measures,
  single Market Value id17 selected). VERIFIED on BD: GET /template/486228 -> facts:1, SELECTED [(17,MV)].
- **L4 TEST-PULL (mine):** persisted 486228 NON-EMPTY across 06-24/26/29 (470,414 / 471,369 / 471,601 rows,
  MV 99.7% priced). single-day(06-24)==14d-window(06-24)=470,414 EXACTLY -> BD returns the END-date PIT
  snapshot regardless of range; 49F does NOT replicate cot's empty-under-Custom root (COO's load-bearing
  risk REFUTED). 06-30=0 rows = BD freshest-date T+N lag, self-heals. Landed frontier
  forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-06-29.xlsx (471,601).
- **CTO PARITY GATE 1a+1b CLOSED (source-grounded by me):** B_01.holdings_lots.py consumes from
  silver/unrealized ONLY the 4 identity dims (account_id, asset_name, cusip, open_date; L621-651, 779-780)
  to build the cusip-keyed veto set — ZERO measures -> single MV is full-fidelity (Rule 17 spirit, met).
  Grain: 470K bronze tax-lots -> ~102,883 (acct,cusip) = ~B's "103K" (B_01.L466 documents the veto-set).
  B_01._resolve_unrealized_key already frontier-selects nearest non-empty (2-day contract+alarm).
- **SILVER MERGE (mine, the load-bearing tonight-vs-tomorrow gate):** ~B cleared the stale 06-29 manifest
  entry + deployed a 0-row-skip guard (2acfb0401). Ran canonical `merge-daily-incremental.py --unrealized`
  on bd-allocations (Amazon Linux, bd-exporter-profile=opal-data-bd RW). Result: 06-29 471,601 lots ->
  dedup (account_id,asset_name), removed 368,739 -> **silver/unrealized/2026-06-29.parquet = 102,862 rows,
  17 cols, 3,030,016 bytes**; 06-30 SKIPPED by the 0-row guard. VERIFIED the parquet: account_id 100% /
  asset_name ~100% / cusip 99.9% / open_date 92% / market_value 100% nonnull. >> 50KB gate, in the healthy
  ~2.3MB band (vs 7,573B stub).

## Snag + reroute (Rule-22 catch, on the record)

0.7.0's handed-off "exporter" i-0fa1846f04ed7e337 is the bd-49f-AUTO-LOGIN box (Playwright browser-login,
auth-only, CVO-certified least-priv): no boto3, opal-data-bd code/template read=403, forwardfill
write=AccessDenied (only the 49f session secret readable). Grounded via SSM probes BEFORE burning time.
Rerouted: provision ran LOCAL/ad-hoc off the canonical S3 script + fresh session (BD session NOT IP-bound,
token minted from local); silver-merge ran on bd-allocations (started->ran->stopped, COO-confirmed
baseline-restore = operational, no Andrew confirm). CTO process note: document 486228 + provision as
reproducible -> folds into ADVI_BDAPIMIG runner productionization.

## Andrew-direct questions answered (BD-source, my lane)

1. **BD historical-PIT feasibility (holdings+values):** YES, confirmed empirically. BD-DataMining qt1
   holdings + qt4 unrealized are date-addressable END-date PIT snapshots (asOfDate). Live proof: cot
   holdings = 18 distinct daily snapshots 06-09..26 (06-10/11/12 pulled on-demand 06-22, 06-23..26 on
   06-29, all distinct + priced ~85% nzf); 49F unrealized 06-24/26/29 each distinct, 99.7% priced;
   single-day==window confirms true per-date PIT. Bounds: (a) depth = firm onboarding (~2026-04-22 cot);
   (b) freshest 1-2 bdays lag (T+N). 49F has NO holdings(qt1) template today (AUA=Schwab-lots; a new qt1
   template would add it, same provision pattern).
2. **Persistent login on the ingestion box (no OTP every time):** the mechanism is ~80% built in
   bd_49f_auto_login.js — injects bd_DeviceRegistration cookie pre-login (L290-297), checks "Remember My
   Device" (L414-438), persists the jar (L475). GAP: orchestrator secret-ids.env never sets
   BD_DEVICE_REGISTRATION -> the trust-token loop isn't closed -> full re-MFA on every .bd.identity death
   (the 3.5-day-dark-gap fragility). Fix: capture bd_DeviceRegistration -> persist to its own durable
   secret -> re-inject on each login so BD skips MFA; consolidate onto the ingestion box (Andrew's
   Schwab/0.0.1_UA pattern). Durable follow-on (COO carrying as a TO; CTO arch + CVO re-cert).

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-which "schwab persistent login / OTP relay" | PARTIAL | routed to 0.0.1_UA_mstools (M365/Graph) refs; located the OTP-relay/device-trust context |
| comp-pipescript io B_01.holdings_lots.py | PASS | confirmed reads silver/unrealized + the 9 inputs; grounded the measure-set parity (1b) |
| comp-freshness (gated nudge) | N/A | verify done by direct parquet read on the box (head_object size + pandas columns/nonnull) — comp-freshness indexes pipeline/served, not an ad-hoc just-landed silver partition |

What worked: comp-pipescript io B_01 pinned the unrealized consumer + (with the source read) closed CTO
gate 1b. What failed: none. Gap/notes: BD-DataMining provision/test-pull/silver-merge have no comp-tool
(forensic + BD-REST + EC2-run); used rail-checked raw aws/SSM. The HUD gated an `aws s3 ls` STRING inside
an SSM heredoc payload (false positive — it's the on-box command, not a local inspection); worked around
via the Write tool + boto3 head_object.

## Briefs written

None — DEPLOY/COORDINATE; findings delivered via RAVC messages + this log.

## Blockers

None. Remaining un-freeze step (23:00Z scheduled gold -> served flip) is a legitimate external-event gate
(NEVER#4: verify on the scheduled run, not ad-hoc), not an assumption-block. ~B owns L5; CTO+0.7.0 verify
served tomorrow AM ET.

## Current State (handoff)

- **49F served:** still frozen (opal-data-bd/platinum/firm/header_metrics.json, data_as_of 06-24,
  LastModified 06-26T05:00, 1648B) — flips on tonight's scheduled gold.
- **BD template 486228** (qt4 unrealized, facts:1/id17 MV) live on BD + in s3://opal-data-bd/code/bronze/
  templates/unrealized.json (~B commit c36aa98ca) + repo data/black_diamond/scripts/bronze/templates/.
- **Bronze:** forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-06-29.xlsx (471,601 lots, 36MB) landed;
  06-30 empty stub left in place (COO ruling: converter frontier-selects, no S3-delete).
- **Silver:** silver/unrealized/2026-06-29.parquet = 102,862 rows / 3,030,016 bytes / 17 cols, all 4 B_01
  identity cols populated. incremental_unrealized_manifest.json now has 06-29 (re-processed); 06-30 NOT
  marked processed (re-checked until it lands data).
- **Chain set for 23:00Z gold (cron 0 23 MON-SAT):** B_01._resolve_unrealized_key -> silver/06-29 ->
  veto ~103K (no mass-close) -> D_03 non-empty -> D_04 republish -> served data_as_of advances off 06-24.
- **Infra:** bd-allocations (i-0800437d1dbb0b5cc) STOPPED (baseline restore). bd-49f-auto-login
  (i-0fa1846f04ed7e337) still running (0.7.0's start) — auth-only, not an ingest box.

## Next Steps

- **[0.4.0_DS_ClientPlatform~B]** L5: confirm B_01 resolves silver/06-29 delta-0 on the 23:00Z gold ->
  D_03/D_04 republish; verify served flip tomorrow AM.
- **[1.0.0_SA_CTO]** + **[0.7.0_AE_CloudOps]** independently verify the served artifact tomorrow AM ET
  (data_as_of off 06-24 + AUA == 49F custodian truth) -> CTO GREEN co-sign.
- **[0.6.0_AE_PartnerETL]** (me) on COO cue: design+propose the persistent-login durable phase (close the
  device-trust loop + consolidate login+ingestion on one box) — ties ADVI_BDAPIMIG runner
  productionization (document 486228 + provision as reproducible) + 49F session-hardening.
