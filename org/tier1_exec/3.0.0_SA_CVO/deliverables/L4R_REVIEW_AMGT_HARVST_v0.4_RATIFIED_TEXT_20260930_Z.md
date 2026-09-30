# L4-R ratified-text review -- AMGT_HARVST v0.4 @ff4405d3d5 (CONTRACTS only)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~08:4xZ - **Asked by:** CTO~Z msg 27039
**Span:** from the last signed bytes (`3.0.0_SA_CVO~O`, v0.3, half `43375644bc89`, which is the text at `e8d13d58ed`) to
`ff4405d3d5` (half `6d7c2214da76`).
- The ENDPOINT hash is `974dada544a2` at all three commits in the span, so there is **no ENDPOINT change**.
- The ratified half changed in two commits: `094cc1f110` (the round-12 L10 addendum) and `ff4405d3d5` (v0.4).
- The diff is of the ratified half as `prd_signoff_lib.top_sections` / `half_of_section` define it: 37 lines, three additions,
  nothing removed.

## 1. THE THREE ADDITIONS

| addition | agrees with ENDPOINT? | faithful to its grounds? | verdict |
|---|---|---|---|
| Round-12 addendum to the event rule: an event is ONE STORY, `event_id` carries the story, and calendar words never link two headlines | Yes. It narrows how the event spine forms events; it adds no outcome and drops none. | Yes. It cites this seat's ADJUDICATION_v20 @`19dfdd2579` finding (BA 08-26 two stories; BA 09-08 linked on "august"), stated as found. | carried |
| `C-HV-RANK-DECLARED-SET` (FWD-7's denominator) | Yes. FWD-7 asks that the ranks be "computed from the graded daily table" and weighted by strength. A partial rank over a declared publisher set, with excluded names listed and never scored, computes from that table. It is not the old mention-count rank. | Yes. It matches the five conditions of `ledger/CTO_RULING_FWD7_DENOMINATOR_DECLARED_PUBLISHER_SET_20260930.md` @`ddcc71fd2d` one for one (declared set, eligibility, eligibility before no-signal, printed population, floor of 10 with a HOLD) on CRO~Z's research @`784068f4c0`. It adds one clause, "the score counts only declared-set articles; a found-only article is never scored", which follows from condition 2 and from `C-HV-COVERED-VS-FOUND`. | carried |
| `C-HV-COVERED-VS-FOUND` | Yes, and it removes a contradiction the served data shows today: 992_HK 2026-02-12 serves two publishers' articles with `publishers_covered_codes` = `[bbg]` (HARVST ADJUDICATION_v35 section 1). The page then read "NOT SEARCHED ON THIS DAY" above those articles (DSGN_AMGTV1 ADJUDICATION_v12 section 2.4). The contract makes that reading "found, listing not run", and keeps coverage marks on the covered set. | It defines a new field, `publishers_found_codes`. The deployed `/timeline` does not serve it today (this seat's read at v35 returned only `data_status` and `publishers_covered_codes`), so it is a build obligation, not a description of the served state. | carried |

## 2. VERDICT: SIGN

1. **The HOLD.** Below the floor, "the prior generation stays served". Until the flip, that prior generation is the legacy rank
   (`CHATTER_AXIS_SOURCE` = `legacy`). If the round-27 census prints fewer than 10 eligible names, FWD-7 stays unrealized, and
   honestly so. The ruling says this ("the rank honestly HOLDs until collection widens"). This seat records it so a HOLD is never
   graded as the flip.
2. **The found-only clause** is new text beyond the ruling's five conditions. It is consistent with them, and it is the clause
   that keeps one name's incidental extra source from outranking another's.

No condition is attached to the SIGN.
