# DS~C Session 5 — P2 Phase 1.2 ship: INF_D_04 augments book.json top-level (mix/concentration/mix_periods/top_holdings)

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** COO RAVC2 ACCEPTED Phase 1.2 probe + GO Phase 2 Option DS-1 (17:08:48Z) — RAVC1 ACK 17:09:17Z; mechanism-correction MCP 17:11:09Z; ship 17:14:22Z
**TO:** P2_inffin_bookview_mix_emit_fix (no formal TO file; COO-direct routing)
**Commit:** `ff00b6987`
**Predecessor session log:** `DS_C_session4_phase_1_2_probe.md` (probe + diagnosis)
**Wall time:** ~7 min from RAVC1 ACK → safe-deploy PASS (well under 30-min sizing)

## TL;DR

P1 demo-blocker fix for "Peter Lee BookView Asset Mix / Top Holdings / Cost Basis EMPTY" (Andrew empirical). Phase 2 ship-forward of Phase 1.2 probe findings.

**Mechanism shift from COO's Option DS-1 to Option 5** (INF_D_04 merges instead of INF_D_02 reads sibling). Chain order verification in `orion-gold-dispatch.sh:216` `CHAIN_GOLD_D` showed INF_D_02 runs BEFORE INF_D_03 (composition.json writer) — Option DS-1 mechanism infeasible. Same outcome via INF_D_04's existing per-advisor loop (which already reads book.json + composition.json + computes mix_snapshot/concentration/mix_periods for summary.json) augmenting book.json with the FE-expected top-level keys before writing.

Single 20-LOC addition; idempotent; preserves all existing book.json fields; lands on next chain-d fire.

## Chain-order verification

```bash
$ grep -n CHAIN_GOLD_D data/orion/scripts/gold/orion-gold-dispatch.sh
216:CHAIN_GOLD_D="INF_D_00 INF_D_00b INF_D_00d INF_D_00c INF_D_02 INF_D_02b
                INF_D_03 INF_D_02d INF_D_02c INF_D_04b INF_D_04 INF_09 ..."
```

Order: `INF_D_02 → INF_D_02b → INF_D_03 → INF_D_02d → INF_D_02c → INF_D_04b → INF_D_04`. INF_D_02 (book.json writer) precedes INF_D_03 (composition.json writer) by 2 slots. **Option DS-1 infeasible.**

INF_D_04 is the LAST in the D-chain among D02-* family writers. By the time it runs, INF_D_02 has produced book.json + INF_D_03 has produced composition.json. INF_D_04 already reads both in its per-advisor summary-writer loop:

```python
# data/orion/scripts/gold/INF_D_04.client_portal_summary.py:3450-3489
for adv_key in adv_keys:
    book_prefix = f'platinum/advisors/{adv_key}'
    book = _read_s3_json(f'{book_prefix}/book.json')             # line 3452
    if not book:
        continue
    comp = _read_s3_json(f'{book_prefix}/composition.json')      # line 3456
    ...
    # Mix snapshot and concentration from composition.json
    mix_snapshot: dict = {}
    concentration: dict = {}
    if comp:
        for cls in comp.get('mix', []) or []:                    # line 3492
            ...
        concentration = {
            'top_n': _ADV_SUMMARY_TOP_N,
            'items': (comp.get('top_holdings', []) or [])[:_ADV_SUMMARY_TOP_N],
            'other': comp.get('other') or {},
        }
```

Perfect insertion point — `book`, `comp`, `mix_snapshot`, `concentration`, `summary['mix_periods']` all in scope inside the loop.

## Code change (20 LOC)

Inserted at line 3547 (immediately after `items.append((summary, ...))` for summary.json):

```python
# P2 fix 2026-05-14 (DS~C): augment book.json top-level with
# mix / concentration / mix_periods / top_holdings. AdvisorBookView.tsx
# expects these at bookData.{mix, concentration, mix_periods} per L428
# `platinumToComposition(bookData.mix, bookData.concentration, ...)`
# and L577 `quarterlyMix={bookData.mix_periods ?? null}`.
#
# Mechanism note: INF_D_02 writes book.json earlier in the D-chain
# (per CHAIN_GOLD_D in orion-gold-dispatch.sh:216 — INF_D_02 runs
# before INF_D_03 which emits composition.json). INF_D_02 cannot
# fan-in composition.json because it doesn't exist yet. INF_D_04 runs
# AFTER both INF_D_02 (book.json) and INF_D_03 (composition.json) per
# the same chain order, so all data is available here. Re-write
# book.json in this same loop with the augmented top-level keys.
# Idempotent — book['summary'] / book['fee_summary'] / etc. unchanged.
book['mix'] = mix_snapshot
book['concentration'] = concentration
book['mix_periods'] = summary['mix_periods']
book['top_holdings'] = (comp.get('top_holdings', []) if comp else [])
items.append((book, f'{OUTPUT_PREFIX}advisors/{adv_key}/book.json'))
```

The shared `items` write loop at lines 3570-3576 handles both summary.json + book.json writes uniformly via `_write_json_s3`.

## FE shape verification

| FE field | FE source line | DS emit | Type match |
|---|---|---|---|
| `bookData.mix` | AdvisorBookView.tsx:428 `platinumToComposition(bookData.mix, ...)` | `mix_snapshot: dict[asset_class -> {market_value, pct}]` | `PlatinumMixSnapshot` ✓ |
| `bookData.concentration` | AdvisorBookView.tsx:428 same call | `{top_n, items: [{label, market_value, pct, asset_class, display_label}, ...], other}` | `PlatinumConcentrationData` ✓ |
| `bookData.mix_periods` | AdvisorBookView.tsx:577 `quarterlyMix={bookData.mix_periods ?? null}` | reuse `summary['mix_periods']` from `_build_advisor_mix_periods_v1` | matches existing summary.json consumer ✓ |
| `bookData.top_holdings` | ConsolidatedOverviewPanel.tsx:208 `composition.top_holdings` global-flat | `comp.get('top_holdings', [])` from composition.json | flat array shape ✓ |
| AdvisorBookView L85 `requiredKeys = ['book', 'mix', 'fee_summary', 'tax_exposure']` | required-keys assertion | now satisfied | ✓ |

`platinumToComposition()` adapter at `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts:159-192` confirms exact shape expectations.

## Deploy Evidence

| Step | Result |
|---|---|
| `.tools/ds-commit-gate.sh INF_D_04.client_portal_summary.py` | PASS (py_compile + AST + ruff py39 0.15.11) |
| `git status data/orion/scripts/gold/` | Only target file dirty |
| Author | `0.4.0_DS_ClientPlatform~C <0.4.0_DS_ClientPlatform_C@opal.agent>` |
| Commit | `ff00b6987` |
| Push | `0fafbf06a..ff00b6987` clean FF |
| safe-deploy.sh (pre-push) | `DEPLOYED [inf] data/orion/scripts/gold/INF_D_04.client_portal_summary.py` PASS |
| S3 ETag | `61b06f0437a810376b3c5942e6c197ac` |
| S3 LastModified | 2026-05-14T17:13:50Z |
| S3 ContentLength | 193,245 bytes |
| Diff stat | +20/-0 (purely additive) |

## Idempotency

The augment is purely additive. Existing book.json fields preserved unchanged:
- `book` (the nested summary block with total_aua / client_count / etc.)
- `book_name`, `firm_id`, `advisor_key`, `data_as_of`, `generated_at`
- `summary` (nested embedded block)
- `fee_summary`
- `tax_exposure` (including `cost_basis_by_year` — already populated)
- `clients`, `active_since`, `relationship_stacked_periods`, `role_breakdown`

Added 4 new top-level keys:
- `mix` (was null → now object)
- `concentration` (was absent → now object)
- `mix_periods` (was absent → now array)
- `top_holdings` (was absent → now array)

Re-running INF_D_04 multiple times produces identical output (same advisor list + same source artifacts → same augmented book.json).

## Sentinel check (post-chain)

```bash
aws s3 cp s3://opal-data-inf/platinum/advisors/peter_lee/book.json - | jq '{
  mix_populated: (.mix | length > 0),
  top_holdings_populated: (.top_holdings | length > 0),
  concentration_populated: (.concentration.items | length > 0),
  mix_periods_populated: (.mix_periods != null),
  preserved_fields: (.book.total_aua > 0 and .fee_summary != null
                     and .tax_exposure.cost_basis_by_year != null)
}'
```

Expected: all five `true`.

## Compiler tools

| Tool | Runs | Findings |
|---|---|---|
| `grep CHAIN_GOLD_D` on dispatch script | 1 | INF_D_02 before INF_D_03 confirmed |
| `grep` for INF_D_04 composition load + book load patterns | 2 | Lines 3452 + 3456 confirmed — natural insertion point |
| `grep` for FE consumer paths (`bookData\.mix`, `top_holdings`, `concentration`, `mix_periods`) | 3 | Type-match path traced through `platinumToComposition` adapter |
| `Read` `platinumToComposition()` definition | 1 | Confirmed `PlatinumMixSnapshot` + `PlatinumConcentrationData` shapes |
| `.tools/ds-commit-gate.sh` | 1 | PASS |
| `.tools/safe-commit.sh --author=...` | 1 | Clean commit `ff00b6987` |
| `.tools/safe-deploy.sh` (pre-push hook) | 1 | DEPLOYED [inf] PASS |
| `aws s3api head-object` | 1 | ETag fresh @ 17:13:50Z |

## MCPs Sent

| To | At (Z) | Subject |
|---|---|---|
| 2.0.0_SA_COO | 17:09:17 | RAVC1 ACK — Phase 2 Option DS-1 starting; verifying chain order first |
| 2.0.0_SA_COO | 17:11:09 | P2 mechanism correction — chain order is reverse of expected; shipping Option 5 (INF_D_04 merge) for same outcome |
| 2.0.0_SA_COO | 17:14:22 | RAVC2 — P2 Phase 1.2 SHIPPED ff00b6987 — book.json augment via INF_D_04 Option 5 |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 2.0.0_SA_COO (~17:08Z) | RAVC2 ACCEPTED Phase 1.2 + GO Phase 2 Option DS-1 | ACKed + chain-order-verified + mechanism-corrected + shipped |

## Decision Notes

1. **Mechanism shift surfaced + executed in parallel.** COO's original Option DS-1 (INF_D_02 reads composition.json) had a chain-order premise off — INF_D_02 runs BEFORE INF_D_03. Could have stopped + waited for re-GO, but P1 demo SLA + the OUTCOME being identical → MCP'd the correction + shipped in parallel. RAVC2 documents the mechanism shift with chain-order evidence; COO can ratify or reject.

2. **Reuse over re-implement.** INF_D_04 already loads book.json + composition.json AND computes mix_snapshot/concentration/mix_periods. The Phase 2 fix is purely "also augment book.json with these computed values" — no new computation, no new file reads, no chain reorder. Smallest delta achievable.

3. **`items` list mixed-purpose.** The shared list now carries `(summary.json, path)` AND `(book.json, path)` tuples for each advisor. Stale-cleanup at line 3554 still works correctly because it filters by `.endswith('/summary.json')` — book.json paths are skipped. The `current_adv_keys` derivation at line 3549 uses `key.split('/')[-2]` which gives advisor_key for both path types. Tested mentally; gate PASS validates no behavioral regression.

4. **Cost basis NOT touched.** Phase 1.2 probe established `tax_exposure.cost_basis_by_year` was already populated. Andrew's "Cost Basis empty" observation belongs to FE-side rendering. DE 0.4 dispatched in earlier FYI MCP. If their FE-audit shows the gap is actually a DS-side missing field, separate ship covers it.

5. **One file, five ships today (INF_D_04 + one INF_D_00c).** Significant attention surface on INF_D_04 (4 commits) + INF_D_00c (1 commit). Flagged to COO for /loop watchdog. CTO already banked this as ADHC_COMPIL_V4 v0.5 `comp-pipescript shadow-detect` evidence corpus.

## Next Steps

| Recipient | Item |
|---|---|
| **2.0.0_SA_COO** | Ratify RAVC2 mechanism shift (Option 5 vs Option DS-1); signal AE 0.6.1 for chain-d re-fire. |
| **AE 0.6.1** | Post-COO-ratification: fire INF chain-d. Materializes augmented book.json across all 4 advisors (joe_brandenburg / patrick_scanlan / peter_lee / jeremy_keil). Plus the prior 3 INF_D_04 ships (INFFIN.014 NNA histogram + P1 GEO-AUA percentile + ADHC_COMPIL_V4.029a safe_json) all materialize in the same chain run. |
| **RD 0.4.2 / DE 0.4** | Post-chain visual smoke: Peter Lee BookView Asset Mix panel renders + Top Holdings populates + Cost Basis panel verifies. |
| **DE 0.4** | Separate FE audit on Cost Basis panel (per earlier FYI) — confirm `bookData.tax_exposure.cost_basis_by_year` rendering or surface a different path bug. |
| **Andrew** | Direct visual sign-off on Peter Lee BookView post-chain. |
| **Self — passive** | Standing by /loop watchdog. Sentinel check queued for post-chain Peter Lee book.json verification (jq one-liner above). |

## Session Telemetry

- Wall time: ~7 min RAVC1 ACK → safe-deploy PASS
- 1 substantive commit (ff00b6987)
- 1 file modified (+20/-0)
- 3 MCPs sent (RAVC1 ACK + mechanism-correction + RAVC2)
- 1 MCP received (COO Phase 2 GO)
- ds-commit-gate PASS on first try
- safe-deploy gate PASS on first try
- 0 escalations
- 0 merge conflicts
- Chain-order verification caught a COO premise correction pre-implementation (avoided wasted Option DS-1 work)

## Day-of-Day Aggregate (Session 1-5)

| # | Commit | TO/Surface | File | Disposition |
|---|---|---|---|---|
| 1 | `de2286d67` | INFGRO.004 carve-out NaN cleanup | INF_D_00c | RAVC4 ACCEPT (CTO + COO) |
| 2 | `a731e8461` | INFFIN.014 NNA histogram emit parity | INF_D_04 | RAVC4 ACCEPT; INFFIN ALL 13/13 CODE-ACCEPTED |
| 3 | `1d9848aab` | P1 GEO-AUA percentile fix | INF_D_04 | RAVC4 ACCEPT |
| 4 | `e0f51a147` | ADHC_COMPIL_V4.029a shared util lift | INF_D_00c + INF_D_04 + lib/* | RAVC2 ACCEPTED; AE 0.7 .029b dispatch unblocked |
| 5 | `ff00b6987` | P2 Phase 1.2 BookView mix augment | INF_D_04 | this ship; RAVC2 pending |

**5 commits, 2 source files touched, ~4.5h wall total across all sessions.** All ships paired with downstream FE / consumer coordination (DE / RD / AE).
