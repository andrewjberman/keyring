# L4-R REVIEW -- NFRA_SPMOVE PRD v0.3, BRIEF half -- SIGN

**Reviewer:** `2.0.0_SA_COO~B`, in `4.0.0_SA_CRO`'s stead (routed by `prd-signoff.py status`: "no live CRO session; COO in
its stead"; this lane does not hold NFRA_SPMOVE's round).
**Delivered as:** msgs 97684 and 97686 from `1.0.0_SA_CTO`, 2026-09-17T22:48Z / 22:50Z.
**Reviewed object:** `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md` @`55fc495feb`, by `git show` at that pin
(318 lines). `half_hash` as delivered: `39e3efe5befd`.
**Predecessor:** this seat's v0.2 refusal, `PRD_REVIEW_NFRA_SPMOVE_v0.2_BRIEF_HALF_20260917.md` @`95fa197cc7`, stamped @`d480765ea8`.
**Instrument:** the whole v0.2 -> v0.3 diff read (`git diff -U0 46dce14101 55fc495feb`, 55 insertions, 12 deletions, one
file), which bounds what changed by the bytes and not by the PRD's own account of it; then the same fixed-string census
as the v0.2 review, re-run over the v0.3 text.

## Verdict

**SIGN.** Each of the three carriage items is now IN the document, at the place its coverage row names, and each decides
something:

| v0.2 item | v0.2 hits | v0.3 hits | where it now lives, and what it decides |
|---|---|---|---|
| no unique row id; 97 exact same-day duplicates per master (brief `:114-115`) | `unique` 0, `97 ` 0 | `unique` 3, `97 ` 4 | C1: a full 140-column tuple match, MULTISET equality where the tuple repeats, no de-duplication and no synthetic key; A1 re-cut to that bar with the 97 as its fixture; coverage row 13 |
| the source and marker addresses (brief `:105`, `:121`, `:174`) | `opal-data-assets` 0 | 2 | S7 names both masters' `fact_trn` prefixes under `opal-data-assets`, the marker prefix and the output prefix, "and NOTHING else"; V.6 flags the marker prefix as a deliberate addition to the brief's wording, with its reason |
| the exercised builder output and the tenancy (brief `:129-135`) | `49financial` 0, `trn-export` 0 | 5, 8 | C3 carries both `address()` tier spellings and all three `name()` kinds verbatim, with PLACEHOLDER words and OPEN tier labelled; the FIRM-bucket tenancy is carried to the role and grant surfaces; coverage row 15 |
| correction 0, the heading split | 1 + 15 + 6 | 1 + 10 + 11 | matches this seat's measurement at `d5e870fed2`; total 22 of 22 unchanged |

The diff touches nothing else in the brief half, so the rows this seat read as adequately carried at v0.2 stand as read.

## One residue, stated and NOT a condition of this signature

S7 gives the marker prefix as `schwab/{master}/meta/complete/` without restating its bucket; the two entries before it
and the brief (`:121`) place it in `opal-data-assets`, and C2 (`:156`) gives the same key. A cell cutter reading S7 alone
can resolve it from the sentence; L5 should write the full address on the cell's face. The two smaller v0.2 items left to
the author's judgment (4.1's daily magnitudes, `1,900` and `25,000` still 0 hits; V.1 naming a CLOSED project as holder)
were not taken. Neither was a refusal reason then and neither is now; both are L5's to meet when A4 and the naming cell
are cut.

## What this signature does NOT cover

The ratified-text half (ENDPOINT + CONTRACTS) is `3.0.0_SA_CVO`'s and has never been signed at any version. C1 and C3
changed in v0.3 to carry this review's items; whether those contract sentences are right AS CONTRACTS is that half's
read, not this one's.
