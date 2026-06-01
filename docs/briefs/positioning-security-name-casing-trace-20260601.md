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

## Compiler Tools
- `comp-platinum page Positioning` — ran (FE component had no directly-resolved fetch; getPositioningData traced manually to /api/general/positioning/positioning_data.json). comp-pipescript io applies if/when AE touches a gold script (this fix is in a Lambda, not data/*/scripts/gold). Decomposition + all-caps scope read directly from the live serving artifact.
