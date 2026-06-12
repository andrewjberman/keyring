# Critical Path Change Record
**Date:** 2026-06-12T20:24Z
**Surface:** advisor_intelligence (SEV1, firms: bd/inf/cot)
**Class:** approval
**Authored by:** 0.4.0_DT_ClientPlatform
**Verified by:** 3.0.0_SA_CVO (RAVC4, 20260612T202436Z)

---

## Change

**File:** `portal/src/pages/AdvisorIntelligence/_shared/components/AdvisorAnalytics.tsx`
**Commit:** bb2c93b8 (portal DEV) — CLOUD 85acc2433

Diff: added `canonicalWindowKey` to the `nnaPeriodData` `useMemo` dependency array.

```diff
- }, [canonicalNna, advisorId, interval, cutoff, timeseriesData, pickInflowsCanon, pickOutflowsCanon, pickNnaCanon])
+ }, [canonicalNna, advisorId, interval, cutoff, timeseriesData, pickInflowsCanon, pickOutflowsCanon, pickNnaCanon, canonicalWindowKey])
```

## Surface detail

`advisor_intelligence` — the NNA flow chart in `AdvisorAnalytics` is rendered for all firm partners (bd/inf/cot) on the Advisor Intelligence page. The `nnaPeriodData` memo computes the windowed NNA period series shown in this chart.

## Why the change was made

`canonicalWindowKey` is derived from the active `window` prop (`'1Y' | '3Y' | 'max'`). It is used inside the memo to look up `canonicalNna.window_bounds?.[canonicalWindowKey]` — the window boundaries that filter the canonical NNA series to the correct date range.

Without `canonicalWindowKey` in the deps: if the user switches the window (e.g. 1Y → 3Y), `canonicalWindowKey` changes but the memo does NOT recompute. The NNA chart continues to display the old window's bounds — stale data rendered on the SEV1 surface.

With the fix: memo correctly reruns on window change; canonical NNA bounds are always fresh.

## Risk assessment

**No render-loop risk:** `canonicalWindowKey` is a string derived from a finite-valued enum (`'1Y' | '3Y' | 'max'`). It is stable within a given window selection — only changes when the user actively switches the window toggle.

**Behavior direction:** bug-fix (stale→correct). Previously the chart showed stale NNA for the window the user just left; now it shows the correct NNA for the current window.

**SEV1 justification:** CVO verified at diff level — minimal correct fix, no broader logic change. Surface-check ran in ADVISORY mode (ramp not flipped); fix approved via RAVC chain.

## Evidence

- Sweep finding: NFRA_DEBTSCAN.TO-D5 ESLINT-02 (exhaustive-deps, case B)
- RAVC2 analysis (DT, 20260612T202326Z): identified as REAL BUG, not routine lint
- CVO RAVC4 (20260612T202436Z): "canonicalWindowKey addition is the minimal correct fix (memo recomputes on window change, stale-bounds bug closed)"
- Commit: `bb2c93b8` (portal DEV `67bd09f2` → `bb2c93b8`)

## Follow-up

Visual confirm queued: window-switch behavior (1Y/3Y/max toggle on NNA chart) to be smoke-tested when bb2c93b8 rides the next PROD promote. Confirm NNA series changes correctly on window toggle.
