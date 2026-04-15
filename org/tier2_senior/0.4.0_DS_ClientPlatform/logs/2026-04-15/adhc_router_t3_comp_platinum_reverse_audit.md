# ADHC_ROUTER.T3 session log — comp-platinum reverse audit vs. RA-P0 + B9-DS

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADHC_ROUTER.T3.ds-c-test-comp-platinum-reverse-vs-rap0.md`
**Authorized by:** 1.0.0_SA_CTO (Andrew corpus-driven compiler regression test)
**Scope:** stress-test `comp-platinum reverse` (dotted-path, shipped `0324142a`) against today's RA-P0 (role_aua) and B9-DS (small_account_count) work. Direct compiler patches permitted under `org/modules/graph/*`. No gold/silver script edits (A→D rerun freeze).

## Summary of findings

**Pre-patch, all three reverse queries produced byte-identical empty output** — making it impossible for an agent to distinguish:

| Query | Truth | Pre-patch output |
|---|---|---|
| `role_aua` | genuinely empty (new RA-P0 field, no consumer yet) | empty |
| `advisor_fee_efficiency` | has producer (C_08) + route + consumer | empty |
| `small_account_count` | has producer (C_08 after B9) + consumer in portal (`FeeEfficiencyPanel.tsx`, `types.ts`) | empty |

This is a **textbook empty-vs-broken UX defect**: the tool's "pass" semantic (new field, no consumer yet) is indistinguishable from "tool routed the query to the wrong index" or "indexer missed the consumer". My RA-P0 log called it PASS because the reasoning was sound — but the output format alone did not support that conclusion.

**Critical-lens check on false positives** (TO §5): the existing `_print_artifact_reverse` directory-prefix fallback (L460-482) emits `AssetIntelligenceTab via getCumulativeChart` when querying `advisor_fee_efficiency.json` — a **false positive by construction** (sibling endpoint in the same S3 directory, not a verified consumer). The fallback did label itself "(no direct match -- key may be sub-field of a sibling endpoint)" but the phrasing was too polite and the output shape mimicked a verified match.

## Patches shipped

**File:** `org/modules/graph/platinum_cli.py` (commit `{fill}`)

1. **`_artifact_stems_matching(dag, query)` helper** — scans DAG write-key basenames for stem matches. Used by the auto-probe router and the field-empty diagnostic footer.

2. **`_portal_grep_hits(query, limit)` helper** — best-effort `portal/src/**/*.ts*` raw-text search for the query string. Used to surface extractor gaps (case [d]) when the field exists in portal source but the dataflow index doesn't capture the access pattern.

3. **`cmd_reverse` auto-probe** — before routing a bare name to field reverse, check if it matches a DAG artifact basename stem. If so, emit `[routed as: ARTIFACT (stem match)]` and run artifact reverse against the matched key. This is the fix for `reverse advisor_fee_efficiency` (case [b] mis-routed).

4. **`_print_field_reverse` diagnostic footer** — on empty result, print `[routed as: FIELD query; normalized=...; index size: N field paths]` header plus a 4-case disambiguation block:
   - [a] genuine empty
   - [b] query mis-routed (artifact named as field)
   - [c] index stale (re-run `comp-build`)
   - [d] extractor gap (portal has it, indexer missed)
   Plus hints: artifact-stem matches, portal raw-text hits (capped at 3).

5. **`_print_artifact_reverse` directory-prefix fallback** — upgraded the "may be sub-field" label to explicit `WARN: SPECULATIVE MATCH (directory-prefix fallback, not a verified consumer)` to meet the false-positive-severity bar.

## Compiler Tools (Rule 7)

### Phase 1 (before patch) — baseline

| `<run>` | Observed | Pass / fail vs `<expect>` |
|---|---|---|
| `comp-platinum reverse role_aua` | `PRODUCER (no payload-path matches found) / SERVED VIA (no matching routes) / CONSUMED BY (no components found)` | PASS semantic (matches `<expect>`: empty for new canonical) — but indistinguishable from failure. UX defect. |
| `comp-platinum reverse advisor_fee_efficiency` | identical empty output | **FAIL** — known-populated field/artifact. Tool routed to FIELD reverse because no `/` or file suffix in query; FIELD index is keyed on sub-fields of fetch data vars, not artifact basenames. |
| `comp-platinum reverse small_account_count` | identical empty output | **FAIL** — field IS in portal source (types.ts:1544, FeeEfficiencyPanel.tsx:47, :236, :682, :742). Indexer gap: `m.small_account_count` in a `map()` iteration scope does not route to fetch-data-variable indexing. |
| `comp-platinum reverse gold/artifacts/advisor_fee_efficiency.json` | PRODUCER: C_08 ✓. SERVED VIA reconstructed URL ✓. CONSUMED BY: speculative fallback prints `AssetIntelligenceTab via getCumulativeChart` | **false-positive consumer** — `getCumulativeChart` serves `timeseries_chart.json`, not `advisor_fee_efficiency.json`. Directory-prefix fallback firing too loosely. |
| `comp-blast C_08` | `No downstream consumers found for: gold:C_08.advisor_fee_efficiency` | as expected — script-node-no-edges limitation (same root cause I hit in RA-P0 and B9). |
| `comp-blast C_08.build_scorecard` | `No nodes matching: C_08.build_scorecard` | function-level node not in graph. Either the AST walker isn't registering nested fns, or `comp-build` hasn't been run with function-level extraction. Potential separate fix; T3 scope limited to the reverse-lookup UX. |

### Phase 2 — empty-vs-broken analysis (pre-patch)

My RA-P0 session log (`logs/2026-04-15/ra-p0_role_aua_schema.md`) recorded `comp-platinum reverse role_aua` as PASS with reasoning: "exactly matches `<expect>` — new platinum field, no existing producer or consumer; `if_mismatch` branch not triggered." The reasoning was correct — but it depended on **my side-knowledge** that role_aua was newly introduced and that no portal component reads it. An agent coming to the tool cold cannot tell the difference between this genuine empty and the `advisor_fee_efficiency` false-negative. **Same output, two entirely different ground truths.**

Similarly, my B9-DS log claimed `comp-blast advisor_fee_efficiency` returned empty "per the known script-node-no-edges pattern" — which was again correct side-knowledge, not something the tool itself conveyed.

### Phase 3 — patches applied, re-runs

All five Phase 1 commands re-executed after patch:

| `<run>` | Post-patch observed |
|---|---|
| `comp-platinum reverse role_aua` | `[routed as: FIELD query; normalized='role_aua'; index size: 40 field paths]` + empty output + 4-case diagnostic + footer: `Query 'role_aua' not found anywhere in DAG artifacts or portal source -- likely genuinely absent (case [a]).` ✓ case [a] correctly identified. |
| `comp-platinum reverse advisor_fee_efficiency` | `[routed as: ARTIFACT (stem match); query='advisor_fee_efficiency' -> gold/artifacts/advisor_fee_efficiency.json]` then artifact reverse: PRODUCER C_08 ✓, SERVED VIA reconstructed URL ✓, CONSUMED BY now prefixed `WARN: SPECULATIVE MATCH (directory-prefix fallback, not a verified consumer)`. ✓ case [b] auto-corrected and false-positive explicitly flagged. |
| `comp-platinum reverse small_account_count` | FIELD query diagnostic footer + `HINT: 2 raw portal source hit(s): portal\src\pages\AdvisorIntelligence\types.ts:1544 + FeeEfficiencyPanel.tsx:47`. ✓ case [d] extractor-gap correctly identified — the tool itself now tells the agent where to look. |
| `comp-platinum reverse gold/artifacts/advisor_fee_efficiency.json` | SPECULATIVE MATCH warning on the CONSUMED BY block now explicit. |
| `comp-blast` script + function runs | unchanged (out of T3 scope — function-node indexing gap is a separate proposal). |

## "Would this have helped RA-P0?" (acceptance #3)

Yes, marginally. My RA-P0 session log at `logs/2026-04-15/ra-p0_role_aua_schema.md` (Phase 1 compilers section) explicitly PASSed on `reverse role_aua = empty` with the side-knowledge argument. With the patched tool, the exact same run now prints:

> `Query 'role_aua' not found anywhere in DAG artifacts or portal source -- likely genuinely absent (case [a]).`

That line, in the tool output, would have been transcribable into my log as evidence rather than reasoning. It shifts the audit artifact from "DS argued PASS" to "tool declared case [a]". Net: lower interpretation surface for CTO audit.

## "Would this have helped B9-DS?" (acceptance #3)

Direct hit. My B9-DS log (`logs/2026-04-15/b9_small_account_count_c08.md`) did not attempt `comp-platinum reverse small_account_count` — only `comp-blast advisor_fee_efficiency` at the artifact level. If I had run it, the pre-patch empty result would have been rationalized as "new field, no consumer yet" — which is **wrong**: the FE consumer was in commit `a2d8f83` in the portal submodule, committed before my B9 rerun. The post-patch diagnostic footer would have printed the portal-source hints pointing at `FeeEfficiencyPanel.tsx` and `types.ts`, immediately flagging the **indexer gap** rather than letting me ship a false-PASS triad entry. Concrete audit-safety win.

## Critical finding (acceptance #5) — false-positive severity

The directory-prefix fallback at `_print_artifact_reverse` L460-482 was producing a **confident-looking false-positive**: `AssetIntelligenceTab via getCumulativeChart (/timeseries_chart.json) -> AssetIntelligenceTab` for a query against `advisor_fee_efficiency.json`. An agent auditing "who consumes this artifact?" would have added AssetIntelligenceTab to their blast-radius estimate, potentially routing a change-review to the wrong tab owner.

The fallback's intent (surface same-directory sibling endpoints as candidates) is defensible, but the output shape mimicked ground-truth attribution without distinguishing confidence. Patch upgrades the label to `WARN: SPECULATIVE MATCH (...)` and explicitly notes these may not read the specific key.

**Note:** I did NOT remove the fallback — per TO §5, false-positives are worse than false-negatives, but a fallback that is clearly labeled as speculative is useful signal. Removing it entirely would swing to false-negatives (agent misses candidate consumers worth human-verifying). The label strength is the correct intervention.

## Out-of-scope findings (logged for follow-on TOs)

1. **FIELD reverse index is 40 paths — suspiciously small.** Portal has dozens of fetch calls and thousands of TypeScript field accesses. `_build_field_reverse_index` only harvests field paths accessed on fetch data variables (`fb.data_variable`) and only via `flow.fields_used()` → JSX refs. Iteration-scope accesses (`rows.map(m => m.foo)`), destructuring after cast, and typed-response flow through `book.clients[n].foo` are probably missed. Follow-on: audit `extract_transforms.build_component_dataflow` and the JSX-ref collector.

2. **Function-level node extraction missing.** `comp-blast C_08.build_scorecard` → `No nodes matching`. `0324142a` shipped dotted-path support for `comp-platinum` but function-level nodes either aren't built into the trace_graph or the basename-to-node resolver doesn't try `script.function` lookup. Separate compiler TO.

3. **Route.s3_key missing on some routes** — the direct-match loop at L400-417 in `_print_artifact_reverse` missed the advisor_fee_efficiency.json route even though the rewrite rule at L421+ resolves it. The route-extraction step is leaving `s3_key` unset for routes that go through CF rewrite rules. Separate extractor TO.

## Commit

Patches land in a single commit under my author line (`0.4.0_DS_ClientPlatform~C`). See commit hash in the COO/CTO signal message.

## Rule 7 compliance checklist

| Item | Status |
|---|---|
| Triad reproduced per `<run>`/`<expect>`/observed | PASS (Phase 1 table + Phase 3 table) |
| Empty-vs-broken disambiguation called out as primary finding | PASS |
| False-positive severity addressed | PASS (SPECULATIVE MATCH label upgrade) |
| Assessment of "would this have helped RA-P0 / B9-DS" | PASS |
| Patches under authorized paths only | PASS (`org/modules/graph/platinum_cli.py`) |
| No gold/silver edits | PASS (freeze respected) |

## Commit attribution note (added by CTO 2026-04-15 post-hoc)

This commit (`614d4c28`) also carries ~A's T1 strict-match fix to `_print_field_reverse` via shared-index sweep during concurrent editing. The `ADHC_ROUTER.T1 fix:` comment in-file attributes the strict-match hunk to T1. ~C's own T3 work (empty-vs-broken footer + artifact-stem auto-probe + SPECULATIVE MATCH label) is the primary authored content. No rework. Learning documented in T1 log.
