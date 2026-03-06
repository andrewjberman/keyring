# ADVI_NNAVAR Investigation Closure — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 23:55
**End Time:** 23:59

## Objective

Close the ADVI_NNAVAR investigation. The -$119M total volume gap vs Schwab is fully
explained. Cancel Phase 5b. Document the definitive finding.

---

## The Finding

Phase 5 desc_audit identified "Holding market value withdrawn" — 4,106 Transfer Out rows,
$119.3M — as 81.9% of Transfer Out gross volume. This matches the gap to $0.3M.

**We were computing it correctly.** This is NOT a bug.

"Holding market value withdrawn" records assets leaving 49F's management when a client
departs to another advisor — who also custodies at Schwab. The assets never leave the
Schwab platform. From Schwab's perspective: no TOA outflow, NNA unchanged. From 49F's
perspective: real AUM departed, correct to count as an NNA outflow.

**The gap is a definitional split, not a data error:**

| System | NNA Definition |
|--------|---------------|
| 49F / BD | Flows into and out of 49F's managed book |
| Schwab | Flows into and out of the Schwab custodial platform |

When a 49F client fires 49F and moves to another Schwab-custodied advisor:
- 49F sees an outflow (correct for 49F's NNA)
- Schwab sees nothing — assets stayed on platform (correct for Schwab's NNA)

The $119M represents approximately one year of 49F client departures to other
Schwab-platform advisors. It will persist structurally and is not fixable or worth fixing.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Do NOT add "Holding market value withdrawn" to canonical exclusions | These are real outflows from 49F's perspective. Excluding them would overstate 49F's NNA. |
| Cancel Phase 5b (`diag_nnavar_phase5b_hmv_exclusion.py`) | No EC2 run needed. The finding is resolved analytically — the gap is correct behavior. |
| Close the volume gap investigation | All hypotheses tested. Gap explained. No production change warranted for the gap itself. |

---

## Investigation Summary (All Phases)

| Phase | Finding | Status |
|-------|---------|--------|
| Phase 1 | Velocity cap dominant lever; cap impl diverged from production | Complete |
| Phase 2 | Cap tuning ceiling: r=0.448 (vel_w120_t1p00, 13/13) | Complete |
| Phase 3 | External flow null finding; settlement marginal; BI unavailable | Complete |
| Phase 3b | VARIABLE TIMING — BD settlement vs Schwab initiation date; r=0.726 at N=-30 | Complete |
| Schwab vector correction | SCHWAB_NNA was reversed in all scripts; corrected | Complete |
| Phase 4 | No missing types; no sign errors | Complete |
| Phase 5 | "Holding market value withdrawn" = $119.3M — correct behavior, gap explained | Complete |

**Gap status: EXPLAINED AND CLOSED. Not a defect.**

---

## What Remains Actionable (Production Bundle)

The volume gap is closed. The correlation gap (production r=0.329 vs ceiling r=0.448)
is still improvable via cap tuning. Pending CEO go/no-go:

| Change | Impact | Gate |
|--------|--------|------|
| Cap tuning: vel_w120_t1p00 (window=120d, threshold=1.0×) | r: 0.329 → 0.448, sign_agr: 13/13 | COO rebuild authorization |
| Settlement date: use settle_date where non-null | +1 sign_agr, near-zero cost | Same rebuild |
| JNL/sweep canonical fix (9bfb289b + b4f2d7a7) | Cleaner exclusions | CEO go/no-go |
| ACAT integration (ONBOARDING_DAYS=30, BURST=3, MIN=0) | +$45.98M gap reduction | CEO go/no-go |

**Corrected best cap: vel_w120_t1p00** (not aua_t1p50+vel_w120_t2p00 from prior incorrect analysis).

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/briefs/coo-memo-nnavar-investigation-complete.md` | Updated with closure finding | Yes — this commit |
| This session log | Closure log | Yes — this commit |

---

## Current State

**Status: COMPLETE**
**Active branch:** `CLOUD`

ADVI_NNAVAR investigation is complete. The -$119M gap is explained: it is the structural
difference between 49F's NNA definition (flows in/out of 49F's book) and Schwab's NNA
definition (flows in/out of the Schwab platform). Correct behavior. No production fix
warranted for the gap. Production bundle (cap tuning + settlement + canonical + ACAT)
remains pending COO authorization and CEO go/no-go.

---

## Next Steps

1. **[2.0.0_SA_COO] Review updated COO memo** — `docs/briefs/coo-memo-nnavar-investigation-complete.md`
2. **[COO/CEO] Go/no-go on JNL/sweep canonical fix + ACAT** — gates the rebuild
3. **[COO] Authorize gold rebuild window** — single rebuild with cap tuning + settlement + canonical + ACAT
4. **[Separate ACAT task]** Fix reversed SCHWAB_NNA in `diag_acat_param_grid.py` and `diag_acat_correlation_summary.py`

**Do NOT:**
- Run Phase 5b EC2 suites — cancelled
- Add "Holding market value withdrawn" to script 05 exclusions — it is correct behavior
