# L4-R review, NFRA_MCPINDEX PRD v0.10, ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-14 ~00:3xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 33841 and 33842 (both acked). **Bytes reviewed:**
`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @301af339c7, which the working tree equals. Read whole:
`git diff e581c26ab4 301af339c7` -- the version bump, FWD-20's ACCEPT, FWD-21's ACCEPT and PROOF, and the v0.10
addendum. Half hash at review: `be6514742258`. Prior: v0.9 SIGNED @552de8f694.

## What changed, and against what

- **FWD-20 ACCEPT.** Depth is now read at answer time from the served artifact, the same rule as freshness. It comes
  from a first-date field or the dated series' first element. A snapshot's depth is its one as-of. "absent" is said only
  where no served artifact carries any date. This is the remedy of row Z-W33-S1 (REMEDIATION_v8 @e660242ac7), carried
  without change. The addendum's "a live-queried row's depth is its served window, `inferred` where not read" is also
  that remedy's.
- **FWD-21 ACCEPT and PROOF.** These are re-pinned to list v4 @7e0da2dfee: all 24 prefixes serve to Opal principals.
  This rests on Andrew's call 8 ("Yes that is available for opal users only for now ... no undue holds"; record
  `ANDREW_DIRECT_20261013_200xZ_..._HARVEST.md:5`, read at the v2.6 OPLGTW review). v0.9 item 1's V1 line is
  superseded for Opal principals, as call 8 requires. The text now agrees with its counterpart, NFRA_OPLGTW FWD-21 v2.8:
  Opal-only admission, non-Opal refused on every prefix, and this project catalogs the prefixes. That resolves the lag
  this seat flagged at the OPLGTW v2.6 review.

## Verdict: SIGN

Both changes close findings this seat recorded, and they follow Andrew's words at their width. No seat name appears in
the ENDPOINT section's new text.

## Carried (not grounds)

1. **FWD-21's denominator grain.** PROOF counts "the catalog's harvest rows against list v4's 24 prefixes". ACCEPT names
   row 8's gold tables by table prefix. v4 also serves everything else under `amgt/`: the seven research-* gold tables
   and bronze, silver and state. A row count will therefore not equal 24. A census that reads "24 of 24 prefixes" can
   pass while `amgt/`'s other contents have no row. The decomposition should state the denominator as the 24 top-level
   prefixes, each covered by at least one row. It should also list `amgt/`'s sub-prefixes explicitly: covered, or out
   of scope with a reason.
2. **Non-data prefixes.** v4 itself notes that `lib/` (a code archive) and `social/v1/_measurement/` (a vendor cost
   record) are not research data. Their catalog rows should say so in `meaning`, so that discover does not route a
   research question to them.

-- 3.0.0_SA_CVO~Z
