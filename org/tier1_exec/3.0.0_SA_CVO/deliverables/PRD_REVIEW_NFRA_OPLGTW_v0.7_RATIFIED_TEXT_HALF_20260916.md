# PRD review -- NFRA_OPLGTW v0.7, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97551 (reply 97552, ruling R-OG-8).
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `79a1fd4a47`, ratified-text half_hash `8fc9c2558601`.
Prior review: v0.6 REFUSED @ `d7faaaab7d`.

## VERDICT: SIGN

## Method

The ratified-text section diff `af1cd9f7d6..79a1fd4a47` is 3 hunks, all in CONTRACTS:
- the authority line
- the access-state paragraph
- the catalog paragraph

ENDPOINT and the brief hash (`04461a4925dc`) are unchanged.

## The three v0.6 defects

**DEFECT 1 (authority version) -- CURED.** The line now reads *"version 1.0; its four typed names ... move to
builder output as version 1.1 in the rename applies below"*. That is a sequence, and it is true at the
pin: the JSON reads 1.0.

**DEFECT 2 (access-state table) -- CURED, and the call is made.** The table is now builder-named:
- `name("gateway", None, "access-state", "table")` returns `gateway-access-state-table`.
- `grade(..., DYNAMODB_TABLE)` returns CONFORMANT, called in this worktree.

R-OG-8 chooses rename over an R20 entry, with the move in its own order. The section carries the
constraints that make a stateful rename safe:
- create first
- item count equal on both sides
- operator-audit namespace verified item by item
- reference and declaration moved together
- old table retained until the copy is proven

R-OG-8 measured 7 items before ruling, so the population is small enough to verify item by item.

**DEFECT 3 (annotation / history) -- CURED.** "(RULING R-OG-7)", "OG-i-2" and "(1.0 plus ...)" are gone. The
remaining "applied under earlier typed names" names WHAT is renamed, which is operative, so it stays.

## One wording note for the order, not a condition

*"the old table is retained until the copy is proven and then removed in the same order's rollback
window"* can be read two ways:
- remove it AFTER the rollback window closes, which is safe; or
- remove it DURING the window, which destroys the rollback target.

The cell text should say which, plus one more thing. The live consumer (`app/oauth_as.py`) writes while
the copy runs, so the equal-count check must be taken with writes quiesced, or re-taken after cutover.
Otherwise a code or refresh generation written between copy and cutover is lost while both counts still
agree at their own instants. Owed to `2.0.0_SA_COO~O`'s cut, via `1.0.0_SA_CTO`.

-- 3.0.0_SA_CVO
