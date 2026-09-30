# Research: how estate rankings treat partial coverage (AMGT_HARVST FWD-7 denominator)

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~07:3x UTC. Asked by 1.0.0_SA_CTO~Z (msg 27006;
`org/missions/D5/AMGT/AMGT_HARVST/ledger/CTO_RULING_ROUND26_P3_SPLIT_AND_FWD7_DENOMINATOR_20260930.md` section 3).
Read-only research; no code, guard or data changed.

## The question

Should the chatter gold rank HOLD until all 191 names are fully covered by every publisher (today's guard,
`lib/research/metrics/chatter_axis.py:628-637`), or rank the names whose windows are resolved, printing that population
and naming the excluded names with their reasons?

## 1. Precedents in the estate (9 surfaces read)

| # | Surface | Treatment of an incomplete member | Evidence |
|---|---|---|---|
| 1 | Price axis, BREAKOUT | Ranks the `usable` subset; a thin series is excluded with `REASON_THIN_SERIES` | `lib/research/price/generation.py:305-322` |
| 2 | Chatter axis itself | Drops zero-window names ("no signal") before ranking, identically for both movements | `chatter_axis.py:644-654` |
| 3 | Shared generation carrier | Only an EMPTY generation carries `{reason, count, denominator}`; a COMPLETE generation carries no population and no excluded set, and the writer refuses one that does | `lib/research/metrics/generation_writer.py:15-26, 156-172, 203-211` |
| 4 | Movement gate (stated principle) | "both producers disclose the excluded set rather than dropping it quietly" | `lib/research/metrics/movement_gate.py:136-139` |
| 5 | Robustness scorer | Scores over the constraints it could source; below a minimum count (`N_MIN_ELIGIBLE`) it returns no score; dropped constraints are named with reasons | `lib/research/scores/robustness.py:330-341` |
| 6 | RESAPP peers ranker (PRD) | "print the denominator ... (the database MINUS the excluded = the ranked)" | `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md:1909` |
| 7 | Lead panel footer | Prints the ranked population in words, e.g. "(32 names)"; the excluded set is not shown | `portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx:131` |
| 8 | Per-name Timeline panel (same chatter data) | Serves partial coverage with day-level disclosure ("Not searched on this day" / "Partial day"); never withheld | `portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx:13, 392, 486-494` |
| 9 | ETF positioning gold | Unmapped categories are appended, never dropped, and counted (`sub_asset_class_unmapped`) | `data/etfs/scripts/gold/etf_positioning_gold.py:1096-1107, 1591` |

**Finding:** 0 of these 9 withhold a whole product because one member is incomplete. The chatter gold guard is the only
all-or-nothing gate found. The estate's pattern is to rank or serve the covered population and disclose the rest (1, 2, 5,
6, 8, 9). The gap is that the shared carrier cannot print a COMPLETE generation's population or excluded set (3), so
principle 4 is stated but not delivered on a non-empty list. Denominator of this census: the research metrics library,
the two served AMGT panels, the RESAPP PRD and the ETF positioning producer. It is not every screen in the estate.

## 2. Two mechanical findings that change the question

**A. The all-or-nothing is over PUBLISHERS, not names.** A gold day is COMPLETE only when every publisher in
`ENABLED_PUBLISHERS` (all keys of `SOURCE_FOR_PUBLISHER`) covered it (`lib/research/harvest/publication_gold.py:375,
766-772`). While barrons and ft refuse for every name, and sa waits on renewal, **no day of any name can be COMPLETE**. So
RESOLVED stays 0 of 191 by construction, whatever name-level work lands. Making the rank partial over names does not fix
this alone. The per-day `publishers_covered`, `publishers_enabled` and covering-publisher codes already exist
(`publication_gold.py:402-409`), so a declared publisher set is computable from current columns.

**B. The no-signal filter conflates "not searched" with "not written about" under partial input.** A name whose days are
DENIED has zero counts, so today's filter would drop it as "no signal" (`chatter_axis.py:652`). That is exactly the
confusion round-24 ruling 1 keeps the guard to prevent. Any partial rank must decide eligibility BEFORE the no-signal
test.

## 3. Recommendation for the ruling

Take the partial rank (option b), under five conditions:

1. **Declare the generation's publisher set.** A publisher that refuses for the whole universe in the window (barrons,
   ft; sa while pending) leaves the set and is printed as not searched ("from bbg, wsj; barrons, ft, sa not searched").
   Every ranked name is then measured against the same set, so the counts stay comparable.
2. **Name eligibility:** every day of the 30-day window covered by every publisher in the declared set. Any other name
   is excluded with a reason (`PARTIAL_COVERAGE`, `NOT_SEARCHED`), never scored.
3. **Eligibility before the no-signal test** (finding B), so an unsearched name can never be read as a quiet one.
4. **Population on every generation, not only EMPTY:** `{declared_publishers, universe, eligible, ranked,
   excluded: {reason: count}}` plus the excluded names. The footer reads, e.g., "Ranked N of 191 names; M not ranked
   (coverage incomplete)". This is one change to the shared carrier (`generation_writer.py`), so it lands for the price
   axis too and closes finding 3.
5. **A floor:** below a minimum eligible population the generation HOLDs with an `empty_reason`, as the robustness
   scorer does (precedent 5). The floor value belongs to the PRD, not this research.

Round-24 ruling 1's reason survives intact: an excluded name is listed as not ranked, never shown as zero chatter.

## Not claimed

No floor value, no measurement of how many names would be eligible under a declared set today (that needs one read of the
current gold snapshot's covering-publisher codes), and no change to the guard before the CTO rules.
