# L4-R review: NFRA_OPLGTW PRD v2.0, brief half -- SIGNED

**Reviewer:** 4.0.0_SA_CRO~Z. **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @e43ee663be, half `brief`,
half_hash f10198b22b29. **Delivered:** 1.0.0_SA_CTO~O msgs 31967 and 31969. **Read:** the pinned bytes, in full for
ENDPOINT (lines 47-167), BRIEF COVERAGE (345-364) and the v2.0 addendum (645-707).

**The brief for v2.0** is this seat's assessment,
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPLGTW_SCHWAB_USABILITY_AND_TAX_MASTER_ASSESSMENT_20261008.md` @139c8d018e, and
Andrew's four answers on it, `ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md` @116d52009d.

## Coverage of the assessment's plan, item by item

| Assessment item | Where the PRD carries it | Content carried, not just pointed at | Verdict |
|---|---|---|---|
| G1 account identity, widened by answer 2 | FWD-10 (:129-137); addendum item 1 (:656-665) | the column class, "every name and title field", the four classes kept forbidden, `account_ref` kept as the join key, audit with counts only, grants for Andrew and Alyssa only | carried, and his widening is applied at the width he stated |
| G2 history, answer 3 | FWD-12 (:149-157); addendum item 4 (:674-680) | 13 months, month-end clamp, unavailable-not-guessed | carried. It adds a fact my assessment lacked: only 27 completion markers (2026-08-31 to 10-07) qualify dates today, so the metadata backfill is the precondition. My "560 to 690 days in silver" counted partitions, not qualified dates; the PRD's reading is the right one for serving |
| G3 datasets from existing silver | FWD-11 (:139-147); addendum item 2 (:666-671) | `fact_acc` as `dim_account`, open lots `fact_uln`/`fact_ult`, closed lots `fact_rld`/`fact_rly`/`fact_rty`, grain and semantics recorded from the source, closure rule kept | carried. Not carried: `fact_upn`/`fact_upt` (position-level cost). Not a defect: open lots carry the same cost and can be summed; noted for the round that writes the field lists |
| G4 flow labels | FWD-11; addendum item 3 (:672-673) | a code table in the contract, `unclassified` for an unlisted code | carried |
| G5 Tax SMA master, answer 1 | FWD-13 (:159-167); addendum item 5 (:681-686) | the list-only run against a control master, same shape, same structure, the zero-files stop, never-widen halves for the infrastructure | carried, with his condition ("same shape") made checkable |
| Answer 4, write tools later | not in this PRD | correct: write tools are NFRA_MCPINDEX/NFRA_OPALAI territory and deferred; the inventory is `docs/briefs/opal-gateway-write-tools-inventory-20261008.md` | correctly outside |
| I1-I4 (NFRA_MCPINDEX items) | not in this PRD | correct boundary | correctly outside |

## The heading denominator

The BRIEF COVERAGE section (:345-364) enumerates the original commission's ten headings at @45ce4e5b73. It does not
enumerate the v2.0 brief's headings. The addendum states that the brief half is "accepted as written by the CRO" under
rule 27's proportionate sign-off. My assessment has seven numbered sections; the table above maps the ones that bear
outcomes (sections 3 to 6) and the calls (section 7). Section 1 is a summary, section 2 restates Alyssa's report, which
FWD-10 to FWD-13 answer. I take that as the denominator met, without asking for a re-enumeration in the BRIEF COVERAGE
table.

## One correction returned by pinned line

None that blocks. One note for the CTO, not a refusal: :133 says staff "see every account's number and every name and
title field Schwab records for it". The forbidden list at :660 is by named class; a source column that is a name but
also personal data (for example a primary-contact field) needs its class decided in round 32 item 4. The addendum
already says an undecided column is forbidden (:661), so the safe direction holds.

## Row NFRA_OPALAI-Z-S61

1.0.0_SA_CTO~O reports it exercised live by row Z-S62 @a81c2dcfd8, with its fix (R54) in release r29. Not this half's
subject; recorded here so the Alyssa sitting's Teams test is read against r29.

## Verdict

**SIGN.** G1 to G5 read as my plan and as Andrew's four answers, at the width he stated.
