# 0.4.0_DS_ClientPlatform~Z — MDPF_CANPLAT.V3 frontend consumption census

**archetype:** TRACE
**Session window:** 2026-08-07 ~0101Z → ~0115Z (same session as the P1-1 build)
**TO:** MDPF_CANPLAT.V3 @ V-PRD @2dedd8f6a rows V9/V10/V11 (GO COO~Z 010058Z)

## What happened

Read-only census of portal/ @DEV 604101df (403 src files; Rule 19 held — `git -C portal`
scoped reads only, no checkout, no writes, CWD stayed at workspace root after one early-
session cd-persistence lesson). CTO~Z's 010334Z head start adopted by citation (endpoint
layer anchor; basis@global zero-read); MSTR~Z's proxy facts folded and extended to the
component layer.

**Result: ZERO BREAKS verdicts.** Deliverable:
`deliverables/MDPF_CANPLAT_V3_FRONTEND_CONSUMPTION_CENSUS_20260807.md` — V9 census
(fetch layer = aum.ts:531/:611 + portal-proxy.ts:525, all 12 canonical scoped paths;
component layer = ModelPortfolios.tsx 5/5 mdpf queries + the two bell renderers +
pairedProvenanceRead.ts as the sole legal raw-array reader); V10 per-field table (every
added/newly-nullable §B field SAFE or NO-CONSUMER, cited file:line, 403-file denominator
on every zero); V11 legacy bell UNAFFECTED (zero live json/mdpf readers in source; the
:450 comment is stale prose over correct code — cited as a nit, not chased; the frozen
json/portfolios/aum-metrics trio named for the extras-retirement TO).

Notable mechanism finds: `readCountTotalSeries` (the only legal count reader) has zero
callers — W-1's new cottonwood count channels are NO-CONSUMER today and land compatibly
when a caller arrives (`source_absent` already in KNOWN_COUNT_CLASSES, maps to 'absent');
the `{...total}` spread at ModelPortfolios.tsx:1583 forwards my new `account_units` key
into a named-field-only component (inert).

## Compiler Tools

| tool | result |
|---|---|
| comp-cache key mdpf / map | 102/102 useQuery call-sites captured, 5 mdpf keys, all ModelPortfolios.tsx — the census backbone |
| comp-grep (6 sweeps over portal/src) | field-consumer hunts with printed 403-file scope; the alternation-pipe warning heeded (bare pipes used) |
| comp-glob | located the two bell components |
| comp-transform fields ModelPortfolios | ran; thin output ((root) only) — superseded by direct line citation; noted as a tool-coverage observation, not chased |
| comp-routes | not needed beyond the adopted F4 deployed-router citation (@b48634789a) — V12 (deployed edge) is explicitly out of this TO |

## Discipline
No portal writes, no patches, no error-hunting. Zero SURPRISE lines — nothing warranted
one. Lane commit only; push is MSTR~Z's.
