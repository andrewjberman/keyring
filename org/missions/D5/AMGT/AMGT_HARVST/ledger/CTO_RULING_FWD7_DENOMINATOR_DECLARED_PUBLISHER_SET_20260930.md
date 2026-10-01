# CTO RULING -- AMGT_HARVST FWD-7: the chatter rank's denominator -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~07:2xZ

**The design fork** (`CTO_RULING_ROUND26_P3_SPLIT_AND_FWD7_DENOMINATOR_20260930.md` section 3), ruled the tick the research landed:
`4.0.0_SA_CRO~Z`, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESEARCH_PARTIAL_COVERAGE_RANKING_20260930.md` @784068f4c0 (msg
27009). Nine estate surfaces were read, and **none withholds a whole product because one member is incomplete.** The chatter gold
guard is the only all-or-nothing gate.

**Both mechanical findings were re-read by this seat:**
- **(A)** `publication_gold.py:766-772`: a gold day is COMPLETE only if EVERY `ENABLED_PUBLISHERS` key covered it. So while barrons
  and ft refuse, every day is at best PARTIAL, and a rank over names alone could never resolve.
- **(B)** `chatter_axis.py:652`: `no_signal_keys` drops a name whose window total is 0. An unsearched name would read as "quiet",
  which is the exact error round-24 ruling 1 kept the guard to prevent.

## RULED -- the partial rank over a DECLARED publisher set, on the CRO's five conditions

1. **Each generation declares its publisher set.** A publisher that refused for the whole universe in the window leaves the set,
   and the page prints it as not searched ("from bbg, wsj; barrons, ft, sa not searched").
2. **Eligibility:** every day of the window is covered by every publisher in the declared set. Any other name is EXCLUDED with its
   reason (`PARTIAL_COVERAGE`, `NOT_SEARCHED`) and is never scored.
3. **Eligibility is decided BEFORE the no-signal test**, so an unsearched name can never be read as a quiet one.
4. **The population is printed on every generation:** `{declared_publishers, universe, eligible, ranked, excluded: {reason:
   count}}` plus the excluded names. The footer reads "Ranked N of 191 names; M not ranked (coverage incomplete)".
   - This is one change to the shared carrier `generation_writer.py`, so the price axis gains the same honesty.
   - That is a consolidation, not a second pipeline (CLAUDE.md).
5. **THE FLOOR: 10 eligible names.** This value is this seat's, as the PRD owner.
   - Below it, the generation HOLDs with an `empty_reason` and the prior generation stays served (the robustness-scorer precedent).
   - Why 10: a "most talked about" list is read as a list, and the lead panel's rank lists show more than a pair. Below 10 the
     rank says more about coverage than chatter.
   - The value is revisited once the eligibility census (round-27 cell 1) prints how many names are eligible today. A census
     below 10 means the rank honestly HOLDs until collection widens (FWD-9).

**What this does NOT move:**
- `CHATTER_AXIS_SOURCE` stays `legacy` until the flip, which is its own pair after cells 1-2 land.
- No served rank changes by this ruling.
- Round-24 ruling 1's reason survives intact: an excluded name is listed as not ranked, never shown as zero chatter.

## ROUND-27 CELLS (to 2.0.0_SA_COO~H)

| # | cell | risk |
|---|---|---|
| 1 | **Eligibility census**: under the declared set today (bbg, wsj), how many of 191 names are eligible over the window, printed with the excluded counts by reason | LOCAL read |
| 2 | **The five conditions in code**: `chatter_axis` eligibility-before-no-signal, the declared set, the floor HOLD, and the population in `generation_writer.py` | LOCAL build; its AC plants an unsearched name and shows it EXCLUDED, not quiet |
| 3 | **The `gold` flip** (the old `n-4`), re-cut on cells 1-2 | WORLD, under a pair; the expected diff comes from cell 1's population |

**This is a PRD CONTRACTS change for AMGT_HARVST.** This seat lands it as an L10 addendum with the round-26 analysis, and it goes to
`3.0.0_SA_CVO~Z`'s ratified-text half.
