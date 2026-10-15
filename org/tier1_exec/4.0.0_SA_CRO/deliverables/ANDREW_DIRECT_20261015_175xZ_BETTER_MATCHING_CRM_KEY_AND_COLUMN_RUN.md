# ANDREW DIRECT -- do better at Cottonwood account matching: a CRM-derived intermediary key, and a run through both sides' columns (2026-10-15 ~17:5xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering this seat's read of the crosswalk:
- R1 (the same normalized account number) matched 0;
- R2 (the in-kind holdings fingerprint) matched all 471 of 1,533 Commonwealth accounts;
- 387 of 860 active Black Diamond accounts have no predecessor.

**Verbatim:**

> No we need to do better at matching. There should be a "CRM" upload in the aws cloud, likely somewhere in a cottonwood-named bucket, but maybe opal-data-assets, that has a ton of CRM PII, im wondering if there could be an intermediary key fashioned from something in there. Beyond that I would briefly run through the various column fields on both the BD side and the Cottonwood side to see if there is another viable key somewhere, need some options/ideas.

## What it sets (surfaced, not adjudicated)

This seat researches, read-only, and reports options:
1. find the CRM upload and test whether it yields an intermediary key between Commonwealth and Black Diamond accounts;
2. run through the identity-bearing columns on both sides for another viable key.

**PII handling:** counts and join rates only. No PII value goes into a file, the repo or a message.

-- recorded by 4.0.0_SA_CRO~DELL2

## Follow-up, minutes later (verbatim)

> The name is also a very obvious match mechanism if nobody tried that already to push stuff over the line.

**Sets:** the account name is a candidate match key, to be tested alongside the CRM bridge. This seat checks whether any prior seat tried it.
