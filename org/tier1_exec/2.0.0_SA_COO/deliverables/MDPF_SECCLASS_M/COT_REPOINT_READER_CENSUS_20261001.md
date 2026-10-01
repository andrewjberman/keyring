# MDPF_SECCLASS, the Cottonwood re-point -- every reader of the mix, and what it does with a class it has not seen (CTO rulings batch 99 item 3)

By `2.0.0_SA_COO~M`, 2026-10-01 17:4xZ. Read-only, code at CLOUD HEAD (portal working copy for `portal/src`). The new classes the
re-point publishes in Cottonwood's mix: `commodities`, `structured`, `unclassified` (batch 99). Method: the in-tree readers by
`comp-pipescript consumers C_06 --pipeline cot-gold` and a read of each; the portal, Lambda and edge readers by a read-only sweep
(a search agent, from the published file names to the components), with its two highest-impact findings re-read here at the
cited lines. The rule of item 3: a reader that would silently drop a class blocks the re-point unless it changes in the same act.

## Producers in the gold tree that drop or mislabel before any reader sees the class (change in the same act)

| file:line | what it does with a new class | evidence |
|---|---|---|
| `data/cot/scripts/gold/D_04.client_portal_summary.py:525` (and :561-568) | builds the firm mix snapshot over four classes, then drops any composition class not in it -- the new classes never reach `platinum/firm/mix_summary.json` (`other` is dropped the same way today) | `for ac in ('equity', 'fixed_income', 'alternatives', 'cash'):`; "asset classes not in C_06 (e.g. 'other') are excluded" |
| `data/cot/scripts/gold/lib/mix_views.py:19`, :84-95 | builds the period views (`firm_mix_views.json`, the client and advisor views) over three classes and puts everything else into an `unclassified` residual described as "settlement float" -- commodities, structured and cash would read as unclassified (cash and `other` do today) | `MIX_ASSET_CLASSES = ['equity', 'fixed_income', 'alternatives']` |

## Readers (portal, Lambda, edge)

| file:line | reads | a new class | Cottonwood-reachable |
|---|---|---|---|
| `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx:633-644` (`firmMixChartData`) | `platinum/firm/timeseries_overview.json` `.mix` | **DROPS** structured, commodities, other, unclassified: only `equity`, `fixed_income`, `alternatives`, `cash` are mapped (re-read here) | **YES, every Cottonwood user**: `_partners/cottonwood/index.tsx:161` renders it unconditionally (re-read here) |
| `.../_shared/components/AdvisorAnalytics.tsx:399-406`, :657-662 | advisor `mix.json` | **DROPS** the same four | probably, admins (advisor profile); not checked live |
| `.../_shared/lib/composition.ts:117-118` (`normalizeMixTo4Class`) | any composition mix | renders structured and commodities; **DROPS** unclassified (`if (!classes.includes(item.asset_class)) continue`) and re-scales the rest | yes, through the callers below |
| `.../_shared/tabs/ClientsTab.tsx:356` | `platinum/firm/mix_summary.json` `.composition` | **DROPS** other and unclassified (only cash opted in) | yes, firm admins (Books tab) |
| `.../_shared/tabs/ClientsTab.tsx:457` | platinum client summary `.mix` | **DROPS** cash, other, unclassified (no options) | not determined (client with no advisor) |
| `.../_shared/AdvisorBookView.tsx:915-917`, :802-804 | advisor and client summaries `.mix` | **DROPS** unclassified (through :117) | yes, admins (advisor drill) |
| `.../_shared/panels/ConsolidatedOverviewPanel.tsx:391` (legend) | normalized composition | **DROPS from the legend** structured, commodities, unclassified (the slice is still drawn) (re-read here) | yes |
| `ConsolidatedOverviewPanel.tsx:353-356` (donut), :78-82 (quarterly bar), :463/:478 (dots) | same / `mix_periods` / concentration | renders (grey fallback; generic key lookup) | yes |
| `.../_shared/lib/composition.ts:186-193` (`platinumToComposition`) | platinum `mix` dict | renders every key (title-case fallback label) | yes |
| `PartnerAnalytics.tsx:97-103` (`resolveMixClassMeta`) | class key | renders, but is only called for `layout.assetClasses.ordered` (cottonwood `layout.ts:128`, which has no `unclassified`) | yes |
| `portal/src/lib/chartColors.ts:597-623` | colour map | renders; structured and commodities have colours, unclassified falls back to grey | yes |
| `infra/aws/lambda-edge/shared-advisor-router/index.mjs:289-315` | path rewrite only | passes through | yes |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:1423-1555` | serves the files verbatim | passes through | not determined (bucket from a DynamoDB firm row) |
| `infra/aws/lambda/bd-pipeline/bd-incrparity-trigger/incrparity_cli.py:34` | byte hash of `mix_daily_summary.json` | ignores classes | not determined (Black Diamond tooling) |
| `AdvisorBookView.tsx:826-832`; `contexts/AuthContext.tsx:51,67` | computed, never rendered; cache warm-up | n/a | n/a |

**Totals:** 2 producers that drop or mislabel; 18 readers, of which **7 drop at least one new class**, 0 crash, 7 render or pass
through, 3 reachability not determined.

## What this means for the packet

The re-point cannot ship alone. Shipped as built, Cottonwood's firm Mix chart (every user) would lose structured, commodities and
unclassified, and the Books donut would never receive them. The same act carries: `D_04` and `lib/mix_views.py` over the ruled
class list; the seven dropping readers rendering every class they receive (labels and colours for the three, including an
`unclassified` colour); a page walk at Cottonwood after the deploy. The portal changes land on DEV under a FAST lease (portal law);
PROD promotion is Andrew's.

Not measured: the three undetermined reachabilities; `ClientsTab.tsx:457` live.
