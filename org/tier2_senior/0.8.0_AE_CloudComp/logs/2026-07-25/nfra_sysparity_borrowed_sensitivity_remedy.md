# Borrowed-sensitivity disclosure + immobile-assumption migration — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch 20260725T135933Z (L1b findings A+B, VERIFIED @43ce85dc67; off-main-fabric)
**Status:** COMPLETE
**Cycle wall:** ~13:59Z dispatch → ~14:10Z committed

---

## Objective

A: version_pin's sensitivity is BORROWED (ADD-without-bump is monotone-blind) — re-examine both units
for a derived_count migration (intrinsic beats borrowed), and disclose the borrowing in the check's own
output unconditionally. B: `inf-intraday-iam` is check-type `assumption` — IMMOBILE-BY-CONSTRUCTION —
migrate onto a predicate an estate change can move, durably checkable without live creds.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| population check | 06 metrics vs cse_schema enums / rulebank axes | determination: NO migration possible | `cse_measures` is a NEAR-MISS (counts served fedobs measures, not schema members — its own source field says so); no JSON report side for either unit's countables |
| `commit-gate` | on edited `system_parity.py` | PASS | clean |
| `system_parity.py` | `--self-test` | **29/29 rc=0** | cell 26 borrowing mutant + cells 27/28 grep_present firsts; negative renumbered 29 |
| `system_parity.py` | `--self-test-negative` | rc=1 | still reddens |
| `system_parity.py` | `--worktree --domain infrastructure` (before/after) | 4/4+1assu → **5/5+0assu** | inf-intraday-iam ASSUMPTION→PASS ("found in iam.tf") |
| `system_parity.py` | `--worktree --domain ontology` | both version_pin details carry the BORROWED line | rendered live, PASS and FAIL outcomes both |
| COMPRAIL HUD | denied one infra/.tf grep | rerouted | line-number lookup re-run with a rail-checked marker (comp-iam models grants, not source line numbers); policy body read via native Read |

**What worked:** checking the near-miss instead of assuming — `cse_measures` reads like a cse-schema
count and is a different population entirely (Verification Law 6); the honest no-migration determination
made A2 the whole remedy exactly as the dispatch anticipated.

**What failed:** nothing this cycle.

**Gap found (routed, not built):** intrinsic sensitivity on either version_pin unit needs a report side
that does not exist — 06's metrics gaining schema/rulebank counts is a comp-system change (base/~D's
compiler), routed as an enhancement suggestion in the memo.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. **A1:** per-unit determination table (memo) — countables exist source-side for BOTH units; no
   machine-readable report side exists for EITHER → version_pin remains, A2 is the whole remedy;
   enhancement routed.
2. **A2:** `_version_pin` appends the borrowing disclosure to EVERY outcome; future units inherit.
3. **B:** `inf-intraday-iam` migrated `assumption` → `grep_present` on `globgrph/iam.tf`, pattern
   spanning policy name AND a core describe action (hollow-policy-proof, cell 28); desc carries both
   planes (DESIRED-plane check per Rule 22a + CVO~Z's cycle-12 applied-plane measurement as
   point-in-time grounding).
4. **Battery:** cell 26 (ADD-without-bump must NOT move version_pin + disclosure present — the
   blindness recorded as a property, the RESEMANT discipline applied to our own check), cells 27/28
   (grep_present found / hollow-mutant), negative → 29. 29/29 green, reddens on --negative.

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/system/system_parity.py` | borrowing disclosure + 3 battery cells | This session, this lane |
| `infra/system/scope_contract.json` | inf-intraday-iam migration | This session, this lane |
| `.../NFRA_TOOLUNIFY_CENSUS/BORROWED_SENSITIVITY_REMEDY_C.md` | New memo | No — CTO~Z tree, on disk |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None.

## Current State

Both findings remedied: every version_pin outcome now states its own blind spot; the contract's last
unconditional-ASSUMPTION unit is a movable predicate with both planes disclosed. Reported to CTO~Z +
CVO~Z this turn.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify (its own filed corrections): the A1 near-miss is one JSON read; cell 26
   is the pair-table's ADD-without-bump made resident; B's cross-policy `[\s\S]*` edge stated for attack.
2. **[1.0.0_SA_CTO~Z]** The routed 06-metrics enhancement (schema/rulebank counts) if intrinsic
   sensitivity is wanted on those units.
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
