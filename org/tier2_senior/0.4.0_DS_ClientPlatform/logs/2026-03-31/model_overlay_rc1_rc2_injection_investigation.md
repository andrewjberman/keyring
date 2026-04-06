# Model Overlay RC1/RC2 Injection Investigation -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-31 (session 2)
**Start Time:** 11:30 PM ET
**End Time:** 2:30 AM ET (2026-04-01)
**Project:** ADVI_PRICES (model overlay accuracy)

---

## Objective

Continue from earlier session. After ticker fixes and gold rerun confirmed the model overlay
gap ($244M), Andrew directed fast iteration cycles (RC1 -> RC2 -> RC2 tuning) to close the
gap between Opal Positioning weights and BD gold layer holdings.

---

## Work Completed

### 1. DIVZ AUM Scope Established

Andrew confirmed $150-160M of DIVZ should be in 49F ($238M total ETF AUM).
Gold shows $47-49M. Gap = ~$100M.

Key calibration:
- 3,539 accounts hold DIVZ per BD unrealized but have zero DIVZ in gold
- Their combined silver AUA: $868M
- Expected DIVZ at 13%: $113M
- Combined with existing gold ($47M): $160M -- matches Andrew's estimate

### 2. RC1: DIVZ Asset Name Aliasing

**Root cause identified:** BD renamed "OPAL DIVIDEND INCOME ETF" to "POLEN DIVIDEND
INCOME ETF" on Feb 17, 2026. Script 02 keys FIFO on (account_id, asset_name). This
created two independent FIFO chains that never net against each other.

**Fix:** Added `NAME_ALIASES` normalization before FIFO groupby in both:
- `02_build_positions_cube.py` (line before cumsum groupby)
- `03_build_holdings_lots.py` (after load_transactions returns)
- Also added "EVENTIDE HIGH DIVIDEND ETF" -> "POLEN DIVIDEND INCOME ETF"

**Result:** DIVZ consolidated to single asset name. No MV change because split
names weren't causing unit undercounting -- they were just labeling two separate
FIFO chains that happened to sum correctly.

**Commits:** db591a12, 56b7726b

### 3. RC2: Per-Position Buy Injection Redesign

**Root cause identified:** 3,539 accounts confirmed by BD unrealized as holding DIVZ
but our FIFO has zero buy transactions for them. Original injection was blocked by:
- 1,425 accounts: negative residual (phantom positions inflate gold > silver)
- 310 accounts: truly zero residual
- 124 accounts: not in allocations

**Fix in script 02:** Redesigned `_load_synthetic_buy_events` to use unrealized lot
count as proportional weighting instead of price-weighting. Removed account-level
residual gate. Used max(residual, 10% silver) as injectable floor.

**Result:** Tier degradation -- the 10% floor caused gold_mv to exceed silver_mv
for accounts that previously matched (A->D migrations).

**Fix in script 02 (second pass):** Removed 10% floor, reverted to positive-residual
only for cube injection. This preserves 05f tier accuracy while still improving
injection for genuinely underrepresented accounts.

**Commits:** 9b4cac4a, 967e3a2f

### 4. RC2: Synthetic Lot Injection in Script 03

**Key insight:** Script 02 and script 03 are independent. 02's injected positions
live in the positions cube; 03 builds holdings lots from raw transactions only.
Injecting in 02 does not affect the portal's Books tab top holdings (which reads
holdings_lots).

**Fix in script 03:** Added `_build_synthetic_lots()` function that:
1. Loads BD unrealized report
2. Finds (account, asset) pairs confirmed by BD but absent from FIFO
3. Creates synthetic lots with units estimated from injectable_mv / price
4. injectable_mv = positive residual only (silver > gold accounts)
5. Distributes across missing positions proportional to unrealized lot count

**Result:** DIVZ $49M -> $92M. R-squared 0.47 -> 0.81. Total lot MV: $2.12B.

**Problem flagged by Andrew:** $2.12B vs $1.59B silver -- $510M overshoot. Even
pre-injection holdings_lots was $1.98B vs $1.59B silver ($390M pre-existing overshoot).

**Commits:** 0395ecb2, 5a484091

---

## Key Finding: Pre-Existing $390M FIFO Overshoot

**Andrew's direction (via AE message 20260331T190357Z):** STOP iteration. The $390M
overshoot in holdings_lots BEFORE any injection is a fundamental FIFO reconstruction
fidelity problem. This is not an injection problem.

BD's unrealized report IS the ground truth for open lots. Our FIFO reconstructs
$1.98B when BD says $1.59B. That $390M divergence must be traced from raw files:
transactions -> allocations -> unrealized -> realized.

RC injection is patching symptoms. The reconstruction itself needs to be correct first.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep RC1 (name aliasing) | Proven correct, no downsides, confirmed by AE |
| STOP RC2 injection iteration | Pre-existing FIFO overshoot makes injection results unreliable |
| Next step: raw data trace | Andrew's direction -- trace every step from raw BD files |

---

## Final State of Deployed Code

| Script | Change | Status |
|--------|--------|--------|
| `02_build_positions_cube.py` | RC1 name aliasing + RC2 positive-residual cube injection | Deployed to S3 |
| `03_build_holdings_lots.py` | RC1 name aliasing + RC2 synthetic lot injection (positive residual) | Deployed to S3 |

**The RC2 injection code is on S3 but should be considered experimental until the
fundamental FIFO reconstruction fidelity is resolved.**

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `gold/02_build_positions_cube.py` | RC1 name aliasing, RC2 injection redesign, floor removal | Yes -- db591a12, 9b4cac4a, 967e3a2f |
| `gold/03_build_holdings_lots.py` | RC1 name aliasing, RC2 synthetic lot injection | Yes -- 56b7726b, 0395ecb2, 5a484091 |

---

## Current State

**Status:** BLOCKED (fundamental investigation needed)
**Active branch:** `CLOUD`

RC1 (name aliasing) is solid and should stay. RC2 (injection) produced R²=0.81 and
DIVZ $92M but at the cost of total MV diverging further from silver ($2.12B vs $1.59B).
The pre-existing $390M FIFO overshoot (pre-injection) is the root issue.

Andrew's direction: trace from raw BD files (transactions, unrealized, allocations,
realized) to understand where FIFO diverges from BD's own lot data.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Raw data trace** -- Compare BD unrealized lot data
   against our FIFO-reconstructed positions account by account. Find where and why
   our cumulative unit counts exceed what BD reports. Is it: missing sells? Wrong
   transaction types? Ghost positions from corporate actions?

2. **[0.4.0_DS_ClientPlatform] Quantify overshoot sources** -- How much of $390M
   is from specific account categories (phantom accounts vs genuine overshooting)?

3. **[0.4.0_DS_ClientPlatform] Fix reconstruction before injection** -- Once FIFO
   fidelity is established, RC2 injection should be accurate and bounded.

**Do NOT:**
- Dispatch more fast EC2 cycles until raw data trace is complete
- Remove RC1 (name aliasing) -- it is correct
- Add the 10% injectable floor back to 02 or 03 -- it causes tier degradation
- Trust injection results until the base FIFO overshoot is understood

**Key question for raw trace:**
The BD unrealized report has 402,623 lots across 7,244 accounts. Our gold layer
open positions total $1.98B. BD allocations say $1.59B. Where do 91,453 cube
positions aggregate to $400M more than BD says those accounts are worth?
