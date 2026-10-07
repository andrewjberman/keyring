#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-24 (criterion SC8-e24-AC2): the census of every screen that shows a mix by class.

READ-ONLY by default. Walks <WS>/portal/src (.ts/.tsx/.js/.jsx, test files excluded) plus the producer files named in SCREENS,
derives each screen's groups FROM THE SOURCE (a literal list, a colour-table key set, a producer funnel), and checks that every
file in the portal that carries a class-list vocabulary is accounted for: it is a screen's file, or it is listed in EXCLUDED
with its reason. A file that is neither is printed UNACCOUNTED, never dropped.

  python screen_group_census.py            census + compares SCREEN_GROUP_MAPPING_20261007.json (groups must equal derived)
  python screen_group_census.py --write    also (re)writes SCREEN_GROUP_MAPPING_20261007.json from this script's tables

The last stdout line is  SCREEN-GROUP-CENSUS files_scanned=<n> screens=<n>  (n = portal source files + producer files read).
Exit 0 when every derived group list matches the declared one, nothing is UNACCOUNTED, and the geography list is read; else 1.

basis: `measured` = the code states the mapping (a fold, a funnel, a one-to-one list); `inferred` = a proposal, the CVO grades it.
"""
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SRC = ROOT / "portal" / "src"
OUT = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_20261007.json"
SIX = ["cash", "fixed_income", "equity", "structured", "alternatives", "commodities"]
LABEL = {"cash": "Cash", "fixed_income": "Fixed Income", "equity": "Equity", "structured": "Structured",
         "alternatives": "Alternatives", "commodities": "Commodities", "multi_asset": "Multi-Asset",
         "unclassified": "Unclassified", "other": "Other"}
EXTS = {".ts", ".tsx", ".js", ".jsx"}
P = "portal/src/"
PA = P + "pages/AdvisorIntelligence/"
POS = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/"
GEO_FILE = POS + "yang-generate-positioning/lambda_function.py"


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def strings_in_array(text, start_rx):
    m = re.search(start_rx, text)
    if not m:
        return None
    i = text.index("[", m.end() - 1) if text[m.end() - 1] != "[" else m.end() - 1
    j = text.index("]", i)
    return re.findall(r"['\"]([^'\"]+)['\"]", text[i:j])


def labels(tokens):
    return None if tokens is None else [LABEL.get(t, t) for t in tokens]


def d_treemap_order():  # Positioning's class list (ASSET_CLASS_ORDER, the ratified five in canonical order)
    return strings_in_array(read(P + "components/holdings/HoldingsTreemapChart.tsx"), r"ASSET_CLASS_ORDER[^=]*=\s*\[")


def d_layout(firm):
    return labels(strings_in_array(read(PA + f"_partners/{firm}/layout.ts"), r"ordered:\s*\["))


def d_canonical(with_cash=False, with_other=False):
    t = read(PA + "_shared/lib/composition.ts")
    name = "CANONICAL_CLASSES_WITH_CASH" if with_cash else "CANONICAL_CLASSES"
    toks = strings_in_array(t, r"const " + name + r"\s*=\s*\[")
    if toks is None:
        return None
    return labels(toks + (["other"] if with_other else []))


def d_ir_class_keys():  # ASSET_CLASS_COLOR key set, in CLASS_RANK order, from the IR registry
    t = read(P + "pages/InvestorReporting/tabs/holdings/assetClass.ts")
    m = re.search(r"const CLASS_RANK[^{]*\{(.*?)\}", t, re.DOTALL)
    if not m:
        return None
    pairs = re.findall(r"^\s*['\"]?([A-Za-z -]+?)['\"]?:\s*(\d+)", m.group(1), re.MULTILINE)
    return [k for k, _ in sorted(pairs, key=lambda kv: int(kv[1]))]


def d_ir_table_groups():
    toks = d_treemap_order()
    ex = strings_in_array(read(P + "pages/InvestorReporting/tabs/holdings/SecurityList.tsx"), r"extraClasses=\{\[")
    return None if toks is None or ex is None else toks + ex


def d_positioning_summary():
    t = read(P + "pages/Positioning/panels/PositioningSummary.tsx")
    m = re.search(r"const ASSET_CLASSES:.*?\n\]", t, re.DOTALL)
    return re.findall(r"label: '([^']+)',\s+rowLabel", m.group(0)) if m else None


def d_aua_segments():
    t = read(PA + "_shared/components/AdvisorAnalytics.tsx")
    m = re.search(r"const allSegments.*?\n\s*\]", t, re.DOTALL)
    return re.findall(r"label: '([^']+)'", m.group(0)) if m else None


def d_cma():
    t = read(P + "pages/CapitalMarketAssumptions/tabs/ExpectationsTab.tsx")
    m = re.search(r"CATEGORY_COLORS[^{]*\{(.*?)\}", t, re.DOTALL)
    if not m:
        return None
    keys = re.findall(r"^\s*'([^']+)':", m.group(1), re.MULTILINE)
    return keys


def d_inflection_legend():
    t = read(PA + "_partners/inflection/InflectionInsightsPanel.tsx")
    return re.findall(r"MIX_PIE\.\w+ \}\} />([A-Za-z -]+)</span>", t[t.index("Asset Class:"):][:1500])


def d_perfrp():
    t = read(PA + "_shared/perfrp/PerfrpAllocation.tsx")
    m = re.search(r"const CLASS_LABELS.*?\n\}", t, re.DOTALL)
    named = re.findall(r":\s*'([^']+)'", m.group(0)) if m else None
    return named


def d_attrib_funnel(rel):  # the producer's two-way funnel: cash + fixed_income -> Fixed Income, every other class -> Equity
    t = read(rel)
    ok = re.search(r"in \('fixed_income', 'cash'\):\s*\n\s*asset_class = 'Fixed Income'\s*\n\s*else:\s*\n\s*asset_class = 'Equity'", t)
    return ["Fixed Income", "Equity"] if ok else None


# ---------------------------------------------------------------------------------------------------------------------
# The screens. `mapping_over` = {class: (target group, basis, why)}; every other class maps one-to-one onto the group of the
# same label (basis measured) when the screen carries that group. `dropped` = classes of the six the code does not draw today.
# ---------------------------------------------------------------------------------------------------------------------
CASH_TO_FI_INFERRED = ("Fixed Income", "inferred", "cash is not drawn here today; proposed to fold into Fixed Income, the fold Positioning states (HoldingsTab.tsx)")
SCREENS = [
    {"screen": "Positioning > Holdings (treemap, legend and table)",
         "files": [P + "components/holdings/HoldingsTreemapChart.tsx", P + "components/holdings/HoldingsBreakdownTable.tsx",
                P + "pages/Positioning/tabs/HoldingsTab.tsx", P + "pages/Positioning/constants/etf-categories.ts",
                P + "pages/Positioning/shared/etfAdapter.ts", P + "pages/Positioning/shared/satelliteAdapter.ts",
                P + "pages/Positioning/shared/satelliteSet.ts", P + "pages/Positioning/shared/bookSet.ts", P + "api/portal-proxy.ts"],
         "producers": [GEO_FILE], "derive": d_treemap_order,
         "mapping_over": {"cash": ("Fixed Income", "measured", "HoldingsTab.tsx: 'Cash' FOLDS TO 'Fixed Income'; legendClassesFor(foldCash=true)")},
         "note": "Five groups; Cash folds into Fixed Income (stated in code). Multi-Asset, Hedge, Other, Unclassified are not drawn here."},
    {"screen": "Positioning > Summary (allocation by class rows)",
         "files": [P + "pages/Positioning/panels/PositioningSummary.tsx"], "producers": [GEO_FILE], "derive": d_positioning_summary,
         "mapping_over": {"cash": ("Fixed Income", "measured", "PositioningSummary.tsx ASSET_CLASSES: Fixed Income row served: ['fixed_income','cash'], blurb 'Bonds & Cash'")},
         "note": "Five groups; Cash is summed into the Fixed Income row (stated in code)."},
    {"screen": "Investor Reporting > Holdings (treemap and legend)",
         "files": [P + "pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx", P + "pages/InvestorReporting/tabs/holdings/assetClass.ts",
                P + "components/holdings/HoldingsTreemapChart.tsx", P + "pages/InvestorReporting/contracts/adapt.ts",
                P + "pages/InvestorReporting/contracts/index.ts", P + "pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts"],
         "producers": ["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"], "derive": d_ir_class_keys, "mapping_over": {},
         "note": "Nine groups, the six one-to-one plus Multi-Asset, Other, Unclassified. Multi-Asset is a group this screen shows today; cell SC-e-23 removes it."},
    {"screen": "Investor Reporting > Holdings (class-mix bar in the drill tree)",
         "files": [P + "pages/InvestorReporting/tabs/holdings/DrillTree.tsx", P + "components/CategoryViewTree.tsx",
                P + "pages/InvestorReporting/tabs/holdings/assetClass.ts"],
         "producers": ["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"], "derive": d_ir_class_keys, "mapping_over": {},
         "note": "CLASS_BAR_ORDER is the key set of ASSET_CLASS_COLOR in rank order: the same nine groups as the treemap. Multi-Asset: SC-e-23 removes it."},
    {"screen": "Investor Reporting > Holdings (securities table grouped by class)",
         "files": [P + "pages/InvestorReporting/tabs/holdings/SecurityList.tsx", P + "components/holdings/HoldingsBreakdownTable.tsx",
                P + "pages/InvestorReporting/tabs/holdings/assetClass.ts"],
         "producers": ["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"], "derive": d_ir_table_groups,
         "mapping_over": {"cash": ("Fixed Income", "measured", "HoldingsBreakdownTable.tsx: displayClass 'Cash' -> 'Fixed Income' (PRD s.3 class 1)")},
         "note": "ASSET_CLASS_ORDER (five) plus extraClasses Multi-Asset, Other, Unclassified. A cash row sits under Fixed Income in this table while the treemap and class bar draw Cash as its own group. Multi-Asset: SC-e-23 removes it."},
    {"screen": "Investor Reporting > Holdings (held positions by asset class totals)",
         "files": [P + "pages/InvestorReporting/tabs/holdings/classTotals.ts", P + "pages/InvestorReporting/tabs/holdings/assetClass.ts"],
         "producers": ["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"], "derive": d_ir_class_keys, "mapping_over": {},
         "note": "One line per served class in the page's class order (Cash first): the nine groups of the class-mix bar. Multi-Asset: SC-e-23 removes it."},
    {"screen": "Attribution > Holdings",
         "files": [P + "pages/Attribution/constants/etf-categories.ts", P + "pages/Attribution/constants/holdings-shared.tsx",
                P + "pages/Attribution/components/HoldingsCustomTreemapContent.tsx", P + "pages/Attribution/tabs/SelectionTab.tsx"],
         "producers": [POS + "yang-generate-holdings-attribution/lambda_function.py"],
         "derive": lambda: d_attrib_funnel(POS + "yang-generate-holdings-attribution/lambda_function.py"),
         "mapping_over": {"cash": ("Fixed Income", "measured", "producer funnel: fixed_income and cash -> Fixed Income"),
                       "structured": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "alternatives": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "commodities": ("Equity", "measured", "producer funnel: every other class -> Equity")},
         "note": "Two groups by Andrew-direct 2026-10-06 (attribution funnel); source_asset_class keeps the registry class. S23: etf-categories.ts still carries a static Cash / Fixed Income / Equity / Hedge category list (surface for the later round)."},
    {"screen": "Attribution > Asset Allocation Summary",
         "files": [P + "pages/Attribution/components/AssetAllocationSummary.tsx", P + "pages/Attribution/constants/holdings-shared.tsx", P + "pages/Attribution/Attribution.tsx"],
         "producers": [POS + "yang-generate-allocation-summary/lambda_function.py"],
         "derive": lambda: d_attrib_funnel(POS + "yang-generate-allocation-summary/lambda_function.py"),
         "mapping_over": {"cash": ("Fixed Income", "measured", "producer funnel: fixed_income and cash -> Fixed Income"),
                       "structured": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "alternatives": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "commodities": ("Equity", "measured", "producer funnel: every other class -> Equity")},
         "note": "Two groups (Fixed Income, Equity); the producer's benchmark table also carries Structured, Commodities, Alternatives at 0.0 'no benchmark'."},
    {"screen": "Attribution > Style vs Policy comparison",
         "files": [P + "pages/Attribution/components/StylePolicyComparison.tsx", P + "pages/Attribution/constants/holdings-shared.tsx"],
         "producers": [POS + "yang-generate-allocation-summary/lambda_function.py"],
         "derive": lambda: d_attrib_funnel(POS + "yang-generate-allocation-summary/lambda_function.py"),
         "mapping_over": {"cash": ("Fixed Income", "measured", "producer funnel: fixed_income and cash -> Fixed Income"),
                       "structured": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "alternatives": ("Equity", "measured", "producer funnel: every other class -> Equity"),
                       "commodities": ("Equity", "measured", "producer funnel: every other class -> Equity")},
         "note": "Same two groups and producer as the Asset Allocation Summary."},
    {"screen": "Capital Market Assumptions > Expectations (columns grouped by class)",
         "files": [P + "pages/CapitalMarketAssumptions/tabs/ExpectationsTab.tsx", P + "pages/CapitalMarketAssumptions/types.ts"],
         "producers": ["infra/aws/lambda/v2_portal/yang_pipeline/cma/yang-generate-cma/lambda_function.py"], "derive": d_cma,
         "mapping_over": {"fixed_income": ("Fixed Income", "measured", "category 'Fixed Income'"),
                       "equity": ("Equities", "measured", "category 'Equities'"),
                       "structured": ("Equities", "inferred", "no Structured category; proposed Equities, the side the attribution funnel (Andrew-direct 2026-10-06) puts structured on")},
         "note": "Groups expected return and volatility by class: a class grouping, not a weight mix. Five categories, no Structured."},
    {"screen": "Advisor Intelligence > Partner Analytics > AUA mix (49 Financial and Demo)",
         "files": [PA + "_partners/49financial/layout.ts", PA + "_partners/demo/layout.ts", PA + "_shared/components/PartnerAnalytics.tsx",
                PA + "_shared/types/TenantLayoutConfig.ts", PA + "_shared/hooks/useTenantLayout.ts"],
         "producers": ["data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py"], "derive": lambda: d_layout("49financial"),
         "mapping_over": {"cash": CASH_TO_FI_INFERRED},
         "note": "includesCash false: the cash slice is filtered out today. Multi-Asset is shown today; SC-e-23 removes it. Demo's `ordered` list is the same."},
    {"screen": "Advisor Intelligence > Partner Analytics > AUA mix (Inflection)",
         "files": [PA + "_partners/inflection/layout.ts", PA + "_shared/components/PartnerAnalytics.tsx"],
         "producers": ["data/inf/scripts/gold/INF_D_03.composition_artifacts.py"], "derive": lambda: d_layout("inflection"), "mapping_over": {},
         "note": "Seven groups; the six one-to-one plus Multi-Asset (SC-e-23 removes it)."},
    {"screen": "Advisor Intelligence > Partner Analytics > AUA mix (Cottonwood)",
         "files": [PA + "_partners/cottonwood/layout.ts", PA + "_shared/components/PartnerAnalytics.tsx"],
         "producers": ["data/cot/scripts/gold/C_06.client_mix_timeseries.py"], "derive": lambda: d_layout("cottonwood"), "mapping_over": {},
         "note": "Nine groups; the six one-to-one plus Multi-Asset (SC-e-23 removes it), Unclassified, Other."},
    {"screen": "Advisor Intelligence > Books, Advisor book and Profile mix donut (49 Financial and Demo)",
         "files": [PA + "_shared/lib/composition.ts", PA + "_shared/tabs/ClientsTab.tsx", PA + "_shared/AdvisorBookView.tsx",
                PA + "_shared/panels/ConsolidatedOverviewPanel.tsx", PA + "_shared/panels/CanonicalBookView.tsx", PA + "_shared/AdvisorBookClientDetail.tsx"],
         "producers": ["data/black_diamond/scripts/gold/D_03.composition_artifacts.py"], "derive": lambda: d_canonical(),
         "mapping_over": {"cash": CASH_TO_FI_INFERRED},
         "note": "normalizeMixTo4Class without includeCash: a cash row is dropped from the donut today. Multi-Asset is shown today; SC-e-23 removes it."},
    {"screen": "Advisor Intelligence > Books, Advisor book and Profile mix donut (Inflection)",
         "files": [PA + "_shared/lib/composition.ts", PA + "_shared/tabs/ClientsTab.tsx", PA + "_shared/AdvisorBookView.tsx",
                PA + "_shared/panels/ConsolidatedOverviewPanel.tsx", PA + "_shared/panels/CanonicalBookView.tsx", PA + "_shared/AdvisorBookClientDetail.tsx"],
         "producers": ["data/inf/scripts/gold/INF_D_03.composition_artifacts.py"], "derive": lambda: d_canonical(with_cash=True), "mapping_over": {},
         "note": "includeCash true: eight groups, the six one-to-one plus Multi-Asset (SC-e-23 removes it) and Unclassified."},
    {"screen": "Advisor Intelligence > Books, Advisor book and Profile mix donut (Cottonwood)",
         "files": [PA + "_shared/lib/composition.ts", PA + "_shared/tabs/ClientsTab.tsx", PA + "_shared/AdvisorBookView.tsx",
                PA + "_shared/panels/ConsolidatedOverviewPanel.tsx", PA + "_shared/panels/CanonicalBookView.tsx", PA + "_shared/AdvisorBookClientDetail.tsx"],
         "producers": ["data/cot/scripts/gold/D_03.composition_artifacts.py"], "derive": lambda: d_canonical(with_cash=True, with_other=True), "mapping_over": {},
         "note": "includeCash and includeOther true: nine groups, the six one-to-one plus Multi-Asset (SC-e-23 removes it), Unclassified, Other."},
    {"screen": "Advisor Intelligence > Advisor Analytics > AUA mix bars",
         "files": [PA + "_shared/components/AdvisorAnalytics.tsx"], "producers": ["data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py"],
         "derive": d_aua_segments, "mapping_over": {},
         "note": "Draws every class a served mix carries (nine possible groups, a class absent from every bar draws nothing). Multi-Asset: SC-e-23 removes it."},
    {"screen": "Advisor Intelligence > Performance reporting > Allocation card",
         "files": [PA + "_shared/perfrp/PerfrpAllocation.tsx"], "producers": [], "derive": d_perfrp,
         "mapping_over": {"structured": ("structured", "measured", "classLabel(): an unlabelled class renders the producer's token verbatim"),
                       "commodities": ("commodities", "measured", "classLabel(): an unlabelled class renders the producer's token verbatim")},
         "groups_declared": ["Equity", "Fixed Income", "Alternatives", "Cash", "structured", "commodities"],
         "note": "Four classes carry a label; Structured and Commodities render as the raw lower-case token, a group named differently from the shared list."},
    {"screen": "Advisor Intelligence > Inflection Insights > basket tile legend",
         "files": [PA + "_partners/inflection/InflectionInsightsPanel.tsx"], "producers": [], "derive": d_inflection_legend,
         "mapping_over": {"structured": ("Alternatives", "inferred", "legend has no Structured entry; MIX_PIE once shared one colour between structured_notes and alternatives"),
                       "commodities": ("Alternatives", "inferred", "legend has no Commodities entry; the old `hedge` colour was Alternatives' orange"),
                       },
         "note": "Tiles are coloured by the served class through mixPieColor, but the legend lists four. A structured or commodities tile wears its own colour with no legend entry."},
]

# Files that carry a class-list vocabulary and are NOT a screen's file: reason by path prefix.
EXCLUDED = {
    P + "lib/chartColors.ts": "colour registry (ASSET_CLASS, MIX_PIE): colours only, the groups come from each caller",
    P + "lib/dataLoader.ts": "market-instrument grouping for performance heat maps, not a mix by class of a book",
    P + "lib/tickerRegistry.ts": "market-instrument registry, not a mix",
    P + "lib/periodResolution.ts": "period maths, names asset class in a comment",
    P + "components/market-performance/": "Market Performance tab: instrument heat maps and RSI by instrument class, not a mix",
    P + "components/PerformanceHeatMap.tsx": "market heat map, not a mix",
    P + "hooks/useRSIValues.ts": "market RSI hook, not a mix",
    P + "pages/MarketPerformance/": "Market Performance tab (market view)",
    P + "api/endpoints/advisor-intelligence.ts": "API client for AI payloads: types and fetch, draws no group",
    P + "api/endpoints/aum.ts": "AUM by model asset-class code (UST, INT, LT ...), a different axis",
    P + "api/endpoints/market.ts": "market data client, not a mix",
    P + "pages/AdvisorIntelligence/_shared/types.ts": "AI payload types, draws no group",
    P + "pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx": "prose, no class list",
    P + "pages/CapitalMarketAssumptions/tabs/OpalViewsTab.tsx": "allocation views by pair/class position (-2..+2), not a mix by class",
    P + "pages/Correlation/": "correlation matrix of instruments, not a mix",
    P + "pages/SecurityAnalysis/": "security ranking and chatter, not a mix",
    P + "pages/SecurityScanner/": "scanner types, not a mix",
    P + "pages/InvestorReporting/tabs/holdings/AllocationBars.tsx": "bars coloured by model code, not by class",
    PA + "_shared/perfrp/contract.ts": "perfrp data contract (dim_asset_classification partitions): a dimension name, draws no group",
    P + "pages/InvestorReporting/tabs/holdings/palette.ts": "colour picker, no class list drawn",
}
ASSET_WORD = re.compile(r"asset[ _-]?class|assetClass|AssetClass", re.IGNORECASE)
FAMILIES = [re.compile(p, re.IGNORECASE) for p in (r"fixed[ _]?income", r"equit", r"alternatives", r"commodit", r"structured", r"\bcash\b")]


def is_test(rel):
    return "/__tests__/" in rel or ".test." in rel or ".spec." in rel


def main(argv):
    write = "--write" in argv
    portal_files = [p for p in sorted(SRC.rglob("*")) if p.suffix in EXTS and p.is_file() and "node_modules" not in p.parts
                    and not is_test(p.as_posix())]
    screen_files = {f for s in SCREENS for f in s["files"]}
    producers = sorted({f for s in SCREENS for f in s["producers"]})
    candidates, unaccounted, excluded_hit = [], [], []
    for p in portal_files:
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")
        fam = sum(1 for r in FAMILIES if r.search(text))
        if not (fam >= 4 or ASSET_WORD.search(text)):
            continue
        candidates.append(rel)
        if rel in screen_files:
            continue
        reason = next((why for k, why in EXCLUDED.items() if rel == k or (k.endswith("/") and rel.startswith(k))), None)
        if reason:
            excluded_hit.append((rel, reason))
        else:
            unaccounted.append(rel)
    missing = [f for f in sorted(screen_files | set(producers)) if not (ROOT / f).exists()]

    doc_screens, problems = [], []
    for s in SCREENS:
        derived = s["derive"]()
        declared = s.get("groups_declared")
        groups = declared if declared is not None else derived
        if derived is None:
            problems.append(f"{s['screen']}: groups not derivable from source")
            continue
        if declared is not None and [g for g in derived if g not in declared]:
            problems.append(f"{s['screen']}: derived {derived} not within declared {declared}")
        mapping, mbasis, why = {}, {}, {}
        for c in SIX:
            if c in s["mapping_over"]:
                tgt, b, w = s["mapping_over"][c]
            elif LABEL[c] in groups:
                tgt, b, w = LABEL[c], "measured", "one-to-one: the screen carries a group of the same name"
            else:
                tgt, b, w = None, "inferred", "no group"
            if tgt is None or tgt not in groups:
                problems.append(f"{s['screen']}: no target group for {c}")
                continue
            mapping[c], mbasis[c], why[c] = tgt, b, w
        entry = {"screen": s["screen"], "files": s["files"], "producers": s["producers"], "groups": groups,
                 "mapping": mapping, "mapping_basis": mbasis, "mapping_why": why,
                 "basis": "inferred" if "inferred" in mbasis.values() else "measured", "note": s["note"]}
        doc_screens.append(entry)

    # S26: the geography list in yang-generate-positioning, read by ast so the line and the values are the file's own
    gtext = read(GEO_FILE)
    geo = {}
    for node in ast.walk(ast.parse(gtext)):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "ETF_GEOGRAPHY_MAPPING" for t in node.targets):
            vals = [v.value for v in node.value.values]
            geo = {"source": f"{GEO_FILE}:{node.lineno}", "values": sorted(set(vals)), "tickers": len(vals),
                   "default_for_unlisted": "Other" if "ETF_GEOGRAPHY_MAPPING.get(ticker, 'Other')" in gtext else "ABSENT"}
    geo["placed"] = ("PROPOSED, not decided (the CTO decides): a new field `geography` on the shared list (the etf-classifications table), "
                     "one of the four values above, 'Other' where a row has none. Not an existing field: sub_asset_class carries a different "
                     "grain (US Large Cap, Developed, International, EM ... for equity only; none of its fixed-income values is a region) and the "
                     "list holds 3,493 rows against this dict's tickers. OPEN: which of the listed tickers have a row today, and who fills the field "
                     "for the rest, is the placing round's act.")
    doc = {"denominator": {"files_scanned": len(portal_files) + len(producers),
                           "how": "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_census.py --write: portal/src .ts/.tsx/.js/.jsx minus tests "
                                  f"({len(portal_files)} files) + {len(producers)} producer files; {len(candidates)} files carry a class-list vocabulary or the words "
                                  f"'asset class', {len(candidates) - len(excluded_hit) - len(unaccounted)} are a screen's file, {len(excluded_hit)} are excluded with a reason, "
                                  f"{len(unaccounted)} unaccounted"},
           "six_classes": SIX, "screens": doc_screens, "geography": geo,
           "excluded": [{"file": f, "reason": r} for f, r in excluded_hit]}
    if write:
        OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        print(f"WROTE {OUT.relative_to(ROOT).as_posix()}")
    elif OUT.exists():
        have = json.loads(OUT.read_text(encoding="utf-8"))
        same = [a["groups"] for a in have.get("screens", [])] == [b["groups"] for b in doc_screens]
        if not same:
            problems.append("SCREEN_GROUP_MAPPING_20261007.json groups differ from the groups derived now")
    for s in doc_screens:
        print(f"SCREEN groups={len(s['groups'])} basis={s['basis']} :: {s['screen']} :: {', '.join(s['groups'])}")
    for f, r in excluded_hit:
        print(f"EXCLUDED {f} ({r})")
    for f in unaccounted:
        print(f"UNACCOUNTED {f}")
        problems.append(f"unaccounted: {f}")
    for f in missing:
        problems.append(f"missing file: {f}")
    print(f"GEOGRAPHY source={geo.get('source')} values={geo.get('values')} tickers={geo.get('tickers')} default={geo.get('default_for_unlisted')}")
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"SCREEN-GROUP-CENSUS files_scanned={len(portal_files) + len(producers)} screens={len(doc_screens)}")
    return 0 if not problems and geo.get("values") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
