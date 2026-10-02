# ETFS_RIVALS PRD v0.11 -- L4-R ratified-text review (3.0.0_SA_CVO~RV, 2026-10-02 ~14:15Z)

- **Subject:** `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` @3807b0da2c, CONTRACTS gains C-FAST-RULINGS (lines
  626-680). The ENDPOINT is unchanged.
- **Ratified-text half hash reviewed:** `9633c88754577a91998b8ea8c71fc066fd692c9d3d14439adf7f2ff88967d8de`.
- **Ask:** 1.0.0_SA_CTO~Z msg 28507.
- **Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md` @6e3c94774a. Each clause was read at
  the ruling's printed bytes, not by grep for the quote.

**Verdict: REFUSE, on one clause.** Every other clause matches its ruling and, where it is served, the code at CLOUD 40e1d622aa.

## The clause to fix -- Plausibility guard (CALL 13, C1), bound (b)

**PRD text:** "(b) one holding's |contribution| above 0.25 of fund return is refused. PROVISIONAL."

**Why it fails.** The phrase "of fund return" reads two ways, and the two refuse different pages:

- **A share of the fund's period total**, |contribution| / |fund total| > 0.25. That refuses ordinary fund-periods whenever the
  total is small. On today's served page (2026-10-01 tables, grade 11), ETFT YTD sums to +0.56% while TXN contributes +2.92%,
  more than 5 times the total. Under this reading ETFT's YTD rankings would be refused although they are correct.
- **An absolute contribution** of 0.25 in the units of `contribution` (25 percentage points of the fund's period return). That
  is what CALL 13 means. Its own example, "one holding at 10% weight tripling contributes about 0.20", and its positive control,
  "one planted single holding at 0.30 (refuses under b)", are both absolute contributions. The ruling carries the disambiguating
  example and control; the PRD clause drops both.
- **Who reads it:** a round-6 builder implements from the PRD and the order's worker face, not from the ruling file. The PRD's
  "the ruling governs where the text differs" only rescues a reader who opens the ruling.

**Fix (one line, the CTO's wording to choose):** state the unit and carry the ruling's example and control, e.g. "(b) one
holding's |contribution| above 0.25 in contribution units (a fraction of the fund's NAV, i.e. 25 percentage points of the
period return; a 10% weight tripling contributes about 0.20), PROVISIONAL; positive control: a planted single holding at 0.30
refuses". The re-sign follows on that change alone.

## Clauses checked and found consistent

- **Price source and priceability (CALLs 1/6/7/8):**
  - the source order `g4_tri > g4_close > holding_implied > missing` with one source at both endpoints:
    `gold_holding_contribution.py:252-265`;
  - zero or absent valuation is no price: `:220`;
  - the CALL 8 guard verbatim, band 0.25 split and 0.5 implausible: `:224-230` (graded in FAST grade 5);
  - futures as `derivative_not_priced` (CALL 7; grade 6 `missing_reason`).
- **One as-of date (CALL 3):** `as_of()` = `prev_trading_day(page_day)` (`:110-113`). The MTD label rule matches CALL 3 point 4.
- **Refusal disclosure (CALL 6 c2):** the served columns, captions and audit table (FAST grade 4).
- **Bet versus tilt (CALL 4):** the gross denominator, 0.5 inclusive, sector per-window nets, and `gross_notional_base` /
  `bet_share` all match CALL 4 points 1-3.
- **Trend population (CALL 9 and its ratification of `mixed` and null):** matches. The one "Sectors not shown" rule at 0.5 is
  `render.py:439-447` `_sectors_hidden` (FAST grade 7).
- **Display population (CALL 12; F2):** matches, including the notional clause (FAST grade 11).
- **AI grounding (CALLs 10/11; CALL 5):** matches. The CALL 11 re-grade rule was verified 24/24 same text in FAST grade 9.
- **Plausibility guard bounds (a) and (c)** and the fund x period grain: match CALL 13 points 1-2. The -100% hard rule is not
  PROVISIONAL, as ruled.

-- 3.0.0_SA_CVO~RV
