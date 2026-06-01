# Positioning Security-Name Casing — End-to-End Trace + Fix Recommendation

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-06-01
**archetype:** TRACE
**secondary_archetypes:** DIAGNOSE
**Dispatch:** CTO [TO Andrew-direct] — VUG renders ALL-CAPS "VANGUARD GROWTH ETF" on the Positioning page (should be "Vanguard Growth ETF"); trace to source + fix at the cleaning layer, not a one-off FE patch.
**Outcome:** Fix layer identified = the **backend cleaning table** (`ETF_NAME_OVERRIDES` in the `yang-generate-positioning` Lambda). Lambda = **AE lane** (infra/aws/lambda/); I (DE) cannot edit/deploy it -> handing the concrete fix to AE, CC CTO+COO. **Key correction to the TO premise:** a proper-case `.title()` transform is INSUFFICIENT because the source names are all-caps AND truncated.

## End-to-end trace (FE field -> endpoint -> S3 -> producer -> ultimate source)
1. **FE render** — `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:597` (+642/669/691/835): `name: ETF_NAME_FALLBACKS[h.ticker]?.name || h.name`. A FE per-ticker fallback map (`ETF_NAME_FALLBACKS`, line 68, "Maps truncated API names to full, properly capitalized names"). **VUG is NOT in this map** -> falls through to `h.name` (the API value). No casing transform is applied to `h.name`.
2. **Endpoint** — `Positioning.tsx` -> `getPositioningData()` (`portal/src/api/portal-proxy.ts:1053`) -> `GET /api/general/positioning/positioning_data.json` (DEMO public, no auth) -> S3 `json/positioning/positioning_data.json`.
3. **Serving artifact** — `s3://opal-data-portal-v2/json/positioning/positioning_data.json` (gzip). Confirmed empirically: `ticker=VUG name="VANGUARD GROWTH ETF"`. **29 all-caps security names total**, all also TRUNCATED (e.g. `PFOE`="PTFDR FOCD OPP ETF", `VUSB`="VANGUARD ULTRA SHORT BOND ET", `SPYM`="STE STR SPDR PT S&P 500 ETF").
4. **Producer** — `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`. Name assignment: `name = ETF_NAME_OVERRIDES.get(ticker, etf_meta.get('name', ticker))` (lines 1444/1587; line 2070 uses `etf_meta.get('name')` with NO override). `ETF_NAME_OVERRIDES` (line 122, "Clean names for specific ETFs") is a **6-entry manual dict** (PFDE, PFOE, JAAA, DIVZ, IDVZ, PCHI). **VUG is NOT in it** -> `etf_meta.get('name')` (all-caps) passes through.
5. **Ultimate source** — `etf_meta`/`name` comes from `model_pkl_data.get('etf_characteristics')` (line 1529/1994) — the model PKL's ETF-characteristics frame. The all-caps+truncated names originate in **Black-Diamond** securities data (`data/black_diamond/.../security_ticker_mapping_final.py:80` `'VANGUARD GROWTH ETF': 'VUG'`; BD stores ~28-char ALL-CAPS asset names) and flow into the PKL.

## Root cause
- The "intermediary tables designed to clean exactly this" that Andrew expects ARE the two per-ticker override maps: backend `ETF_NAME_OVERRIDES` (6 entries) + FE `ETF_NAME_FALLBACKS` (~50 entries). Neither is a systematic transform.
- VUG slipped **both** tables. Cross-referencing the 29 serving all-caps tickers against the FE map: **VUG is the only one missing from the FE fallback** -> the only ticker that renders all-caps on the FE (the other 28 are rescued on FE render, but the **backend still serves all 29 all-caps**).
- **A `.title()` proper-case transform does NOT solve this** — the source is all-caps AND truncated. `.title()` on "PTFDR FOCD OPP ETF" -> "Ptfdr Focd Opp Etf" (still wrong). Correct cleaning requires a per-ticker FULL proper name. (`ETF_NAME_OVERRIDES` also corrects genuinely-WRONG source names, e.g. `DIVZ` source "ELEVATION SERIES TRUST - POL" -> "TrueShares Low Volatility Equity Income ETF" — so it's a full-name map by design, not a re-caser.)

## Fix — layer + options (surfacing before change per CTO instruction)
**Layer = backend cleaning table `ETF_NAME_OVERRIDES`** (the CTO/Andrew-intended cleaning layer; fixing here cleans the *serving artifact* so the FE needs no per-ticker entry). This is in the **yang-generate-positioning Lambda = AE lane** (infra/aws/lambda/, terraform-deployed). DE cannot edit/deploy it.

- **Option A (minimal, in-pattern — recommended now):** add `'VUG': 'Vanguard Growth ETF'` to `ETF_NAME_OVERRIDES`. One entry, matches the existing pattern, fixes the flagged bug at the correct layer. After redeploy + rollup, the serving artifact carries the clean name and the FE renders it clean with no FE change.
- **Option A+ (sweep — recommended follow-on):** while in the file, populate `ETF_NAME_OVERRIDES` with proper full names for the other all-caps serving tickers (the 28 currently masked only by the FE map) from a canonical securities-name source, so the backend serves clean names for ALL tickers (not just those the FE happens to map). Lets the FE `ETF_NAME_FALLBACKS` be slimmed/retired later (de-dupes the dual maps).
- **NOT recommended:** a `.title()`/proper-case transform (truncation makes it wrong); a one-off FE `ETF_NAME_FALLBACKS['VUG']` add (the FE patch the CTO explicitly excluded).

## Lane + hand-off
- The fix is a **Lambda code change** (`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`) -> **AE (0.7.0_AE_CloudOps, yang pipeline owner)** implements + deploys (terraform per LAMBDA_DEPLOYMENT_PROTOCOL; comp-pipescript / source-map per the deploy rules). I (DE) author the exact proposed change; AE applies + deploys.
- After deploy: the positioning rollup must re-run so `positioning_data.json` re-emits with the clean name (AE).
- **Visual smoke is human** (headless Chrome/Playwright blocked fabric-wide) — flag Andrew to confirm the rendered "Vanguard Growth ETF" on the Positioning Holdings tab post-deploy.

## RESOLUTION (CTO GO Option A — verified, 2026-06-01)
CTO ruled (165454Z): GO Option A now (DE authors diff -> AE deploys); A+ follow-on gated on a canonical name source. Pre-handoff verification settled two things:

1. **The FE-read path DOES apply the override.** The serving artifact has TWO holdings sections: `portfolios/{model}/holdings` (NO override — all all-caps) and `current_holdings/{model}/holdings` (override APPLIED — PFDE/DIVZ clean). The FE Holdings tab (Current period) reads `positioningData.current_holdings[selectedPortfolio].holdings` (HoldingsTab.tsx:592). VUG in `current_holdings` is all-caps ONLY because it's absent from `ETF_NAME_OVERRIDES` -> **adding VUG to the dict fixes the FE Current view.** Confirmed VUG's current_holdings entry carries the attribution columns (fee/aum/beta/returns) matching the CTO reference row.
2. **The QTD/YTD/1Y/SI view is already clean.** It reads a SEPARATE Lambda (`yang-generate-holdings-attribution` -> `holdings_attribution_data.json`), whose serving artifact ALREADY shows VUG = "Vanguard Growth ETF". So (a) the defect is isolated to the Current view / yang-generate-positioning, and (b) **the proper name "Vanguard Growth ETF" is confirmed by a live artifact, not guessed** — and that attribution source is the canonical clean-name source A+ needs.

**EXACT DIFF (Option A) — handed to 0.7.0_AE_CloudOps to apply + deploy:**
File `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`, in the `ETF_NAME_OVERRIDES` dict (lines 122-129), add one entry:
```python
     'PCHI': 'Polen High Yield ETF',  # NOT MSCI China (that's MCHI)
+    'VUG': 'Vanguard Growth ETF',   # all-caps "VANGUARD GROWTH ETF" from BD PKL source (Andrew-flagged 2026-06-01)
 }
```
AE deploy: terraform via safe-apply (Rule 1) -> re-run the positioning rollup so `positioning_data.json` re-emits -> CloudFront-invalidate the positioning path. Post-deploy verify: `current_holdings.*.holdings` VUG name = "Vanguard Growth ETF"; visual smoke = Andrew (headless blocked).

**A+ canonical source (follow-on):** the 22 of 28 remaining all-caps tickers have provider names in the FE `ETF_NAME_FALLBACKS`; ALL of them (and the rest) have clean names in the `holdings_attribution_data.json` source — that attribution source is the canonical full-name reference for the sweep (satisfies the CTO's "pull from a reference, don't un-truncate"). Scope A+ with AE.

## DEPLOYED + VERIFIED (2026-06-01)
AE (0.7.0_AE_CloudOps) deployed Option A: code `f981f6ae6` (yang-v2.4.10), safe-apply HALTGT 0-diff, positioning rollup re-emitted (`generated_at 2026-06-01T17:05:24Z`), CloudFront invalidation `I20LMCX2L11PR0E1EEHNLNC86F`.
- **DE independent serving-verify (RAVC validate) = PASS:** re-pulled `json/positioning/positioning_data.json` (gen 17:05:24Z — the re-emitted artifact); `current_holdings.{INT,LTC,LTA,AGG}.holdings` VUG = "Vanguard Growth ETF" (4 clean, 0 all-caps). The FE Current Holdings target path is FIXED. Rendered visual = Andrew (CF inval was InProgress; headless blocked).
- **`portfolios.*.holdings` all-caps (AE flag) = LATENT, NOT a visible defect.** That section's `name` field is NOT rendered by any live FE component: `PositioningSummary` consumes `positioningData.portfolios[code]` only for portfolio-level metrics (no holdings `.name`); HoldingsTab renders names from `current_holdings` (Current, fixed) + `attributionData` (QTD/YTD, already clean). Recommendation: apply the same override to the `portfolios`-section name path as part of **A+** (data-cleanliness + de-risk future consumers), not a blocking fast-follow.

## Compiler Tools
- `comp-platinum page Positioning` — ran (FE component had no directly-resolved fetch; getPositioningData traced manually to /api/general/positioning/positioning_data.json). comp-pipescript io applies if/when AE touches a gold script (this fix is in a Lambda, not data/*/scripts/gold). Decomposition + all-caps scope read directly from the live serving artifact.
