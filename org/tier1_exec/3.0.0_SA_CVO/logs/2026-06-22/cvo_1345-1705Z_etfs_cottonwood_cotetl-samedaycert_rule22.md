# CVO 2026-06-22 ~13:45-17:05Z — ETFS research brief + Cottonwood migration assessment + COTETL same-day fix-drive & full cert + Rule 22 (grounding doctrine)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, TRACE

Afternoon delta after the morning log (55084d21a). All Andrew-direct. Four arcs, each grounded against live/served artifacts (never self-report); the COTETL cert was the first artifact under the new Rule 22, applied to its own origin pipeline.

## 1. ETFS macro / ETFS_AVGCAP -- PRD-enabling research brief (shipped to CTO)
Andrew-direct: monthly AVERAGE ownership VALUE per Opal ETF {DIVZ,IDVZ,PFDE,PFOE} per partner {49F,Inflection,Cottonwood}. Built the CTO research brief (org/tier1_exec/3.0.0_SA_CVO/ETFS_AVGCAP_cto_research_brief_20260622.md, commit 6d4441c00), CTO-validated + COO-handed-off for setup/decomp.
- CANONICAL SOURCES (live-verified, all 4 ETFs present at ticker+market_value+date+account): 49F=Schwab RPS/BDRECPOS (silver/RPS EMPTY, build via /49-schwab-conv); Inflection=Orion gold/holdings (clock PINNED 2026-05-15 = Eclipse start; Eclipse model-data cross-ref); Cottonwood=BD gold/canonical/holdings.
- KEY CORRECTION (Andrew-caught): v1 used silver/ULN ($274.2M) -- the UNREALIZED-lot SUBSET, WRONG artifact. RPS/BDRECPOS full positions = $529.9M @05-08 (trailer-validated: T1 control 92,848 records == my parse). bd $508.6M ~= RPS (no 2x double-count; bd ~4% low = lags). Resolved via the wrong-artifact catch.
- ARCH: no-cross-firm-bucket (NEVER#1) => per-partner compute -> new IAM'd opal-data-etfs aggregation bucket. 8 open PRD decisions + phasing (P1 Inflection+skeleton -> P2 49F silver/RPS -> P3 Cottonwood). CTO authors PRD (gated on Andrew priority); COO owns setup.

## 2. Cottonwood BD transaction / Opal-model migration assessment (Andrew-direct)
Read silver/transactions (15 files). Earliest trade_date = 2026-04-22 (BD backfill ceiling). Activity uptick: Apr $1M -> May $1.09B/61.6k txns -> Jun $1.81B/56k. MIGRATION INTO Opal ETFs CONFIRMED: $7.07M, 101 buys (zero sells), first 2026-05-29, accelerating (May $0.79M -> Jun $6.28M). 4 relationships (Lesnik $4.29M / Beecherl $1.50M / Rubottom $0.79M / Henderson $0.49M). Internal reallocation (external_flow=None), no "Opal model" object in BD (direct ETF buys), advisor unattributed. Frozen holdings ($194.5K@06-09) badly UNDERSTATE it -> measure from txn-flow.

## 3. COTETL same-day fix-drive + FULL CERT (Andrew same-day mandate; $24M AUA close)
Andrew: fix all breaks + run bronze->silver->gold e2e + validate end-to-end no-issues TODAY (no observation period); stick bronze->silver-file (not REST-direct). Drove via COO(marshal DS+AE)+CTO(fix).
- TRIAGE: 2 break-points framed (silver-06-18 + canonical-seal-06-09). CTO/DS code-read refined: #1 = benign D-1 window (06-18 last-complete-biz-day; corroborated by my AM bd-A_00 finding); #2 = MIS-LOCALIZATION (my "stuck seal" was build-timing, not a seal -- see arc 4).
- RUN-1 partial: ground-truthed only HOLDINGS+positions_cube advanced; nna+account_gains+served still 06-09 (caught it broader than CTO's "likely PASS"). Cert HELD (#1/#3/#5 fail).
- RUN-2 BINDING CERT: $24M AUA-FREEZE CERTIFIED CLEARED -- served data_as_of 06-09->06-18, total.aua $373.16M->$395.30M (+$22.14M), holdings/nna/cube/account_performance contiguous 04-22->06-18, backfill full. Triple-grounded (me+DS+AE). Caught NEW residual #1 (account_gains STILL 06-09, never rebuilt, upstream of perf/composition per comp-blast) that NEITHER AE nor DS reported.
- FULL-FREEZE RE-CERT CLEARED: DS source-grounded account_gains = BENIGN-UNCONSUMED (C_03 snapshot-wired, C_02 fallback-unused, served grep-clean); CVO corroborated via the decisive served-state (ALL 7 platinum/firm @06-18, zero-stuck) + served-chain-ADVANCED-despite-account_gains@06-09 (reference != live-consumption). Andrew "no issues" bar MET. Open = non-correctness future-cleanup (dead account_gains/C_00/C_02 path; the 13-unmapped firm-headline decision for Andrew; fee-side L6).
- SELF-CORRECTION: my "aua_overrides doesn't exist" was a PARTIAL-SEARCH artifact (scanned config/ not code/gold/); ground-truthed -> it EXISTS -> RETRACTED before it corrupted a correct banked memory.

## 4. Rule 22 / mechanism-grounding doctrine (my mis-inference -> institutionalized LAW)
My COTETL canonical "separate stuck seal, won't self-heal" was a MIS-INFERENCE -- I inferred a MECHANISM from an OUTPUT date-pattern without reading B_00 (snapshot-rebuild, build-timing staleness). Owned it cleanly; DS code-read corrected it. CTO institutionalized it as CLAUDE.md Rule 22 + docs/architecture/NFRA_COMPRAIL_GROUNDING_DOCTRINE.md (53919cb32) -- the CONCLUSION-layer of NFRA_COMPRAIL. Validated it sound (the two-grounding-modes split: STATE->served, MECHANISM->source/graph). Updated memory (feedback_two_grounding_modes_state_vs_mechanism + MEMORY.md pointer). MY authoring lane (CTO ratifies, ratified-in-advance): the grounding: field (CAUSAL claims only) into molecule/seams/verify-channel + the TO-5 coverage-audit backstop -- POST-CERT pass (pending). Applied Rule 22 correctly on the very next occasions (the account_gains state-vs-mechanism split + the aua_overrides retraction).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-freshness all | AM estate freshness (carried) | (AM) |
| pipescript advi-bd/inf/cot, --resource nna/rps/schwab, --list | ETFS canonical-source lineage + cot transaction/holdings producers | source map established |
| comp-blast account_gains | COTETL residual #1: account_gains consumers (load-bearing check) | upstream of C_00/C_03/D_00/D_03 (edges); state showed not-gating |
| comp-which (ETFS served artifact; account_gains consumers) | routing (rail) | -> pipescript --resource / comp-pipescript io |
| comp-grep / comp-glob (rail) + Grep (account_gains refs) | aua_overrides existence (full S3+repo) + account_gains consumer files | aua_overrides EXISTS code/gold/; account_gains ref'd by C-tier |
| comp-which-rail.log (TO-5 baseline) | first post-enforce coverage-audit cut | 1 HIGH false-positive (aws_freshness on local tail blocks /49-schwab-conv) + 1 mis-route -> CTO |
| boto3 served/parquet reads (operational) | ETFS RPS parse + trailer-validate; cot txn aggregation; COTETL cert served-state | all STATE claims grounded vs served |

**What worked:** grounding STATE vs the served artifact + NOT inferring MECHANISM -- the discipline caught a holdings-only partial-advance, a still-stuck account_gains (twice, that producers missed), the wrong-Schwab-artifact ($274M vs $530M), and my OWN partial-probe over-claim. **What failed:** the canonical "stuck seal" mis-inference (owned, corrected, institutionalized as Rule 22). **Rail:** comp-which/comp-grep/comp-glob used per the now-LIVE Rule 21 gate; boto3 = operational data reads (free); the one false-positive deny surfaced to CTO as the TO-5 first cut.

## Current State (handoff)
- COTETL: FULLY CERTIFIED CLEARED ($24M AUA + full freeze, end-to-end, zero taint). COO co-reporting Andrew; CTO formal cert-record. AUAFIX-L5 now unblocked (freeze cleared).
- ETFS_AVGCAP: research brief shipped; CTO authors PRD (gated on Andrew priority); COO owns setup/decomp.
- Rule 22 authoring (grounding: field + TO-5 backstop): MY post-cert pass, NEXT; CTO ratifies same-pass.
- TO-5 (comp-rail post-enforce): accumulating; first coverage-audit cut delivered (1 false-positive + 1 mis-route).
- Future-gated: SS4c synthetic (post-06-24 Wed run); the 13-unmapped firm-headline decision (Andrew); fee-side L6; the dead account_gains/C_00/C_02 cleanup TO.

## Next Steps
- **[3.0.0_SA_CVO]** Rule 22 authoring pass (grounding: field into molecule/seams/verify-channel + TO-5 coverage-audit backstop) -> ping CTO to ratify.
- **[3.0.0_SA_CVO]** TO-5 coverage-audit continues (rail-log telemetry); SS4c synthetic post-06-24.
- **[1.0.0_SA_CTO]** ETFS_AVGCAP PRD (per Primary Path) + the COTETL formal cert-record + the Rule-22 grounding-field ratify.
- **[2.0.0_SA_COO]** ETFS_AVGCAP setup/decomp; track the 3 COTETL non-correctness open items.
- **[0.4.0_DS_ClientPlatform]** COTETL deploy-ledger close-leg; the dead account_gains/C_00/C_02 cleanup + confirm-the-13 attribution.

— 3.0.0_SA_CVO
