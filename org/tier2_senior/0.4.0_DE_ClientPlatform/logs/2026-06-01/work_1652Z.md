# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1652Z (Positioning name-casing trace)

**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE

## Dispatch
CTO [TO Andrew-direct] (CC COO): VUG renders ALL-CAPS "VANGUARD GROWTH ETF" on Positioning page; trace to source + fix at the cleaning layer (NOT a one-off FE patch). COO GO'd as my fresh item (no re-lane).

## Trace (FE -> source) — brief: docs/briefs/positioning-security-name-casing-trace-20260601.md
1. FE HoldingsTab.tsx:597 `name: ETF_NAME_FALLBACKS[h.ticker]?.name || h.name` — VUG not in FE map -> falls to API name; no casing transform.
2. getPositioningData -> /api/general/positioning/positioning_data.json -> S3 json/positioning/positioning_data.json.
3. SERVING (confirmed empirically, gzip): VUG="VANGUARD GROWTH ETF"; 29 all-caps names total, all also TRUNCATED.
4. Producer = yang-generate-positioning Lambda: `name = ETF_NAME_OVERRIDES.get(ticker, etf_meta.get('name'))`. ETF_NAME_OVERRIDES = 6-entry manual dict; VUG absent -> all-caps passthrough.
5. Source = model PKL etf_characteristics <- Black-Diamond (BD stores ~28-char ALL-CAPS names; security_ticker_mapping_final.py:80).

## Key findings
- The "cleaning tables" Andrew expects = the per-ticker override maps (backend ETF_NAME_OVERRIDES + FE ETF_NAME_FALLBACKS). VUG slipped BOTH; it's the ONLY one of the 29 serving all-caps missing from the FE map -> only ticker all-caps on FE.
- **A `.title()` proper-case transform is INSUFFICIENT** — source is all-caps AND truncated ("PTFDR FOCD OPP ETF" can't be un-truncated by re-casing). Cleaning must be a per-ticker FULL name. (Corrects the TO's "proper-case transform" premise.)

## Fix layer + lane
- Layer = backend ETF_NAME_OVERRIDES (Lambda) — the correct cleaning layer (cleans the serving artifact; FE needs no per-ticker entry).
- LANE = AE (Lambda = infra/aws/lambda/, DT/AE; DE can't edit/deploy). Handing to AE.
- Option A (now): add 'VUG':'Vanguard Growth ETF' to ETF_NAME_OVERRIDES. Option A+ (follow-on): sweep the other 28 + retire FE map. NOT .title(), NOT FE one-off.
- Visual smoke = human (Andrew) post-deploy (headless blocked).

## Commits
- CLOUD `<pending>` — brief + this log

## Comms
- RAVC2 -> CTO (1.0.0_SA_CTO) + COO (2.0.0_SA_COO): trace + recommendation + A-vs-A+ ruling ask + AE-handoff confirm.

## Next
- [CTO] rule Option A vs A+ (sweep) + confirm AE as implementer.
- [AE] (pending CTO confirm) implement ETF_NAME_OVERRIDES fix in yang-generate-positioning Lambda + redeploy + rollup re-run. I author the exact entry/diff on GO.
- Held: DS~B Schwab re-derive continuity re-verify; RD~B SMA-fold (103f623a DEV) rendered-math verify. /work cron live.
