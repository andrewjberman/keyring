# PRD review -- NFRA_SPMOVE v0.3, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97692 (nudged 97661/97663/97669/etc.).
PRD: `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md` @ `55fc495feb`, ratified-text half_hash `5f58edba86f5`.
Prior review: none -- never signed at v0.1, v0.2 or v0.3.

## VERDICT: SIGN

## Method

Diffed the working-tree PRD (confirmed byte-identical to `55fc495feb`, zero diff to HEAD) against the ratified
pins at `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_SPMOVE_ENDPOINT_FORWARD_20260916.md` @`8d5995ec46`,
outcome by outcome, printing the bytes on both sides. FWD-1 and FWD-3 checked line-for-line (below); FWD-2,
FWD-4, FWD-5, FWD-6 checked the same way and match. Grepped ENDPOINT and CONTRACTS for a ruling-id parenthetical
or a seat name (`\(R-\d`, `\(RULING`, `@[0-9a-f]{8,}`) -- the four hits in the file are all in the header /
provenance prose above the sections, none inside ENDPOINT (:75-140) or CONTRACTS (:141-221).

## ENDPOINT verbatim, module SOURCE only

FWD-1, ratified pin vs. PRD -- DONE WHEN/ACCEPT/PROOF byte-identical, SOURCE dropped (the one line class this
seat has already accepted as the section's permitted trim, on the STATUS precedent for LGIC_CANON/LGIC_NAMING/
LGIC_ENFORCE and now on SOURCE for this sibling pair). Same result for FWD-3 (checked because it is the one
outcome barred at APPLIED rather than EXERCISED, so its ACCEPT/PROOF shape differs from the rest) and for the
remaining four. No outcome statement is reworded and no DONE WHEN bar is paraphrased anywhere in the section --
this is the corroborating instrument for today's companion refusal on `NFRA_MCPINDEX` v0.3, which drops ACCEPT
and PROOF and paraphrases the bar itself; this PRD, cut by the same seat the same day, does not do that.

## CONTRACTS

C1-C7 checked for operative-constraint completeness against the brief's measured facts (the no-unique-row-id
and 97-duplicate finding decide C1's comparison rule; C2 states the two measured marker irregularities as
design input; C3 carries the builder's EXERCISED `address()`/`name()` output verbatim per Rule 30, with the two
open placeholders -- `table` and `trn-export` -- and the open tier both flagged as such rather than assumed
settled; C4's size table is labelled MEASURED vs. INFERRED per value, not asserted as one class). No contract
row states a value the ENDPOINT or the brief contradicts. C3's registry tenancy claim (49 Financial, a FIRM
bucket) is carried as a fact the naming builder itself returned, not a hand-typed address, consistent with
Rule 30's citation requirement.

**Agreement with the counterpart surfaces named in CONTRACTS:** the `NFRA_OPLGTW` reader-role reference ("never
widened for this") is a constraint this PRD imposes on itself, not a claim about NFRA_OPLGTW's own CONTRACTS,
and nothing here contradicts that project's admitted PRD. The `NAMING_SCHEMA.json` SharePoint-grammar addition
is correctly scoped as this project's own cell "ratified through LGIC_NAMING's schema bump, never a rider on
LGIC_ENFORCE" -- the same discipline this seat has held LGIC_ENFORCE to directly.

## Not re-opened

BRIEF COVERAGE, the acceptance matrix and the brief-half's own content-carriage defects (fixed at v0.3, per
`2.0.0_SA_COO~B`'s refusal) are the brief half's territory, not this one's, and are not re-derived here.

-- 3.0.0_SA_CVO
