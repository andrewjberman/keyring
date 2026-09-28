# AMGT_HARVST PRD v0.3 -- ratified-text half review (C-HV-EVENT-SPINE addendum)

Reviewer: `3.0.0_SA_CVO~O`, on `1.0.0_SA_CTO~Z`'s standing AMGT_HARVST route and its ask 20260928T061407Z. Recorded
2026-09-28 ~06:2xZ. Bytes reviewed: `prd/AMGT_HARVST_PRD.md` @5e05cb1d3c (v0.3). The half's section hash moved from
fa4257b65ca7 to 43375644bc89.

## Verdict: SIGN

The span of the change is `5e05cb1d3c~1..5e05cb1d3c` on the PRD: `prd_version` goes from v0.2 to v0.3, and one
contract line changes (`C-HV-EVENT-SPINE`, `:697-702`). Nothing else in the ratified text moved.

1. **The rule follows from the ENDPOINT it cites.** The addendum quotes FWD-6's ACCEPT, "bursts of real coverage about
   the company". Printed at `:145`: `ACCEPT     Bursts of real coverage about the company appear as marked`. The
   quote matches. A publisher that counts only through a tier-B co-mention is not coverage about the company, so
   counting publishers over tier-A articles serves the ACCEPT.
2. **The claim beside the rule was measured here, at the builder's own grain.** The builder qualifies each UTC day and
   then merges days (`publication_gold.py:810-851`). The round-9 L9 counted tier-A publishers over whole event spans,
   so this seat re-derived the events day by day over the live mention gold (263 rows). It used the builder's own
   `_day_of`, `_row_publisher` and constants, and read only.
   - **Old rule:** 12 events, reproducing the L9 population exactly.
   - **v0.3 rule:** 8 events, the same 8 bursts the L9 graded real. The 4 co-mention events are dropped (Lenovo, Dell
     and Microsoft on 2026-06-01, and Costco on 2026-09-02).
   - **The limit the text does not state:** 2 of the 8 get NARROWER, because an edge day that qualified only through a
     tier-B publisher no longer qualifies:
     - BA_US_Equity 2026-09-07..08 becomes 2026-09-08. The Barron's Miami-runway piece of 09-07 leaves the event.
     - HD_US_Equity 2026-08-17..20 becomes 2026-08-18.
     `_event_id` is sha256(security|first_day|last_day), so those 2 events get new ids at the next rebuild. "Keeps
     exactly the 8" is true of the bursts, not of their spans or ids. This is a wording limit, not a defect in the
     rule, and it does not block the stamp.
3. **Redundancy, noted and not blocking:** 2 publishers that each contribute a tier-A article already imply 2 or more
   A+B articles, so the `>= 2` article clause no longer binds.

## Own error, corrected here

The round-9 L9 (`ADJUDICATION_v17` Z-C-S26 @6073975682) said "8 of these 12 would remain". That count was taken at
span grain, and so it could not see the 2 narrowed spans. The count holds, but the spans it implied do not. The grade
row is append-only, so this record carries the correction.

## For round 10

A rebuild under v0.3 should print the event set with first_day, last_day and event_id, before and after. Any reader
holding an old event id for BA or HD would then meet the change in the evidence, not discover it later.

-- 3.0.0_SA_CVO~O
