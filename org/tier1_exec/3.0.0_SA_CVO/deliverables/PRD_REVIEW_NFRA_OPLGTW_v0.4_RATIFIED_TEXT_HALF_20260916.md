# PRD review -- NFRA_OPLGTW v0.4, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97504.
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `8bfc074be7`, half_hash `984595906620`.
Prior review: v0.3 REFUSED, `PRD_REVIEW_NFRA_OPLGTW_v0.3_RATIFIED_TEXT_HALF_20260916.md` @ `bec64dea66`.

## VERDICT: SIGN

## Method (the one the v0.3 refusal promised)

1. **Re-hash.** `prd_signoff_lib.half_hashes` at `8bfc074be7`: ratified-text `984595906620`,
   brief `04461a4925dc`. The brief hash is unchanged from v0.3, so the brief half did not move.
2. **Diff only the cured places.** `git diff d6583eab37 8bfc074be7` on the PRD is 3 hunks, 6 lines:
   - the header `prd_version`
   - FWD-9's SOURCE line
   - C6's FWD-9 paragraph

   No other byte of the half moved.
3. **Re-run the per-card census.** Seat serials / version notes:
   - FWD-1..FWD-8: 0 / 0 each.
   - FWD-9: **1 / 0**. The one serial is the prior-art path, which the v0.3 review expressly allowed.
   - CONTRACTS: 0 seat serials, no `(v0.N)` annotation.

## Cure 1 -- DONE

FWD-9's SOURCE no longer carries "at the ... terminal", "asked by ...", or the "Added at v0.3 ...
RULING R-OG-3 ..." clause. Andrew's verbatim words, the prior-art path, and all five qualified inputs
remain.

The words were checked in both carriers:
- **The PRD:** still present, byte-exact.
- **The rulings record** (`RULINGS_NFRA_OPLGTW_20260916.md` @ `8bfc074be7`): now present, byte-exact.

So the tracked carrier did not disappear when the prose moved.

## Cure 2 -- DONE, form (b)

C6 now states that FWD-9's export surface is outside `NFRA_OPLGTW_CONTRACT.json` v1.0's enumeration.
That surface is its reader role, its two prefixes and its SharePoint delivery. C6 also says the
surface is enumerated into the contract at FWD-9's cell, with the role name from builder output,
before any code consumes it. So "closed there as data" is true again for everything v1.0 claims.

The "(v0.3)" annotation is gone.

## Carried forward, not a condition

FWD-9's cell must bump the contract JSON before code consumes the export surface. That is now a
PRD-stated obligation of the cell. At that cut, it is a gradeable criterion the adjudicator will
look for.

-- 3.0.0_SA_CVO
