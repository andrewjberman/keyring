# Andrew-direct ~21:4xZ 2026-09-18 -- AMGT_RESAPP data conforms to the canon NOW, not through a later migration

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, before any act on it. **Context:** his ~21:1xZ words made
`opal-data-harvest` the designated home for all AMGT_RESAPP data and pipelines; `1.0.0_SA_CTO~Z` read that as an R20
declared departure from R4 (bronze and silver belong in `opal-data-assets`); this seat measured the canon and narrowed
it to bronze alone, because R4's own non-application and R8 scope the mandatory form to CLIENT-CONFIDENTIAL data
(`infra/logic/02_DOCTRINE.md:367`, `:414-421`, `:503`).

## Verbatim, in order

> Actually, my apologies, we should follow the nomenclature and structure for all new buckets, that is my error.

Then, answering the one question this seat put to him -- scope it to new work (R19's own-migration route), or conform
AMGT_RESAPP's live keys now:

> If we do not do so, it is just gong to cause more problems than its worth downstream

> so even though its more effort, might as well just establish this early and up front

## Reading, narrow

1. **The declared departure is WITHDRAWN.** No R20 exception is recorded for AMGT_RESAPP's tier homes. The canon's
   nomenclature and tier structure are followed.
2. **AMGT_RESAPP conforms NOW, option (b) of the question as put** -- not through a later migration project, and not
   scoped only to future buckets. He chose the more effortful route deliberately, to avoid downstream cost.
3. **What that means, per the canon as measured:** BRONZE (raw vendor bytes as delivered) lands in `opal-data-assets`
   (R4); SILVER and above may live in the product bucket `opal-data-harvest` under R8's free axis WITH A DECLARED
   REASON (an R20 reason, not an exception); every address comes from `lib/opal_naming.py address()` and every resource
   name from `name()` (Rule 30); a key's tier is readable from its prefix.
4. **It is a MIGRATION of live keys, and it is not free:** every AMGT reader keys on today's prefixes
   (`raw/bloomberg/**`, `filings/v1/**`, `universe/v1/**`, `crosswalk/v1/**`, `derived/model_block/**`,
   `drafting/v1/**`, `management/v1/**`, `peers/v1/**`, `posture/v1/**`, `scores/v1/**`). Which prefix is which TIER is
   an L4 classification, and the cut-over must keep every reader serving throughout. Nothing moves on this record.
5. **Not decided here:** where it is placed (its own project under Rule 30 R19, or a chain of round 14) -- that is
   `1.0.0_SA_CTO~Z`'s to route and `2.0.0_SA_COO~Z`'s to cut; and the round-14 issuance already in flight is not
   re-opened by this seat.

## Addendum ~21:5xZ -- no cross-bucket move: bronze and silver stay in `opal-data-harvest`

Verbatim, minutes after the words above:

> With that in mind, i want you to do a deep dive on teh shapes of the data we're pulling from the various sources for
> RESAPP, and review the LGIC_NAMING system standards, and come up with a plan on how to manage this properly. We can
> run bronze and silver inside the opal-data-harvest bucket, that is fine, it does not need to be in opal-data-assets,
> which i believe should exclusively be for client assets.

**Reading, narrow -- this supersedes item 3 and item 4 of the reading above:**
1. **No cross-bucket migration.** Bronze and silver stay in `opal-data-harvest` with every other AMGT tier. The "live-key
   migration to `opal-data-assets`" this seat relayed in msg 23794 is WITHDRAWN.
2. **What remains is the STRUCTURE inside the bucket:** `lib/opal_naming.py` `address()` and `name()`, tier readable from
   the prefix (Rule 30), which is his ~21:4xZ "follow the nomenclature and structure".
3. **`opal-data-assets` is CLIENT ASSETS ONLY**, in his words -- a statement about the CANON, whose R4 as written says
   "every source, every scope, every time". Placing that reading in the doctrine or its registry is the laptop fabric's
   work under his word, not this seat's here.
4. **A task to this seat:** the shapes of the data RESAPP pulls from every source, a review of the LGIC naming standards,
   and a plan to manage it properly. That plan carries the tier classification per prefix, measured.

## Addendum ~22:0xZ -- the doctrine placement, chosen

`0.0.0_AB_MSTR~Z` put two shapes to him (msg 23815), because `_home_bucket` (`lib/opal_naming.py:249-261`) resolves
through `tiers.json.homes[tenancy][tier]` and every existing tenancy sends bronze and silver to `opal-data-assets`, so
no scope row alone can make `address()` return an `opal-data-harvest` bronze address: (i) a new tenancy whose bronze and
silver are scope-homed, or (ii) place his "opal-data-assets is client assets only" reading into the doctrine itself.
Both this seat and `0.0.0_AB_MSTR~Z` recommended (ii). Verbatim:

> yes 2 is the move

**Reading, narrow:**
1. **Option (ii) is chosen: the doctrine records what he said** -- `opal-data-assets` is for CLIENT data; general and
   product data is homed by scope at every tier, bronze and silver included. It is a change to the one file every
   address in the estate resolves through, which is why it was his call.
2. **The placement is `0.0.0_AB_MSTR~Z`'s**, on the laptop fabric (`infra/logic/**` is lane PLATFORM_LOGIC_DOCS, which
   excludes this lane), and the answer goes to `1.0.0_SA_CTO~Z` as that seat asked.
3. **It is estate-wide, not AMGT-only** -- and the hazard this seat names for whoever writes it: changing the homes
   table must NOT silently re-home another scope's live bronze or silver. Every existing general pipeline keeps the
   address its own registry row states until its own migration project moves it (Rule 30 R19); the doctrine change
   states the rule, and per-scope homes record where each pipeline actually is.
4. **Client-confidential data is untouched:** R4-R7 bind there with no free axis.

## Addendum ~22:0xZ (2) -- what `opal-data-assets` is FOR, in his words

Immediately after choosing option (ii), verbatim:

> opal-data-assets is very specifically for client/partner custodial information

**Reading, narrow:** the bucket's purpose is **client and partner CUSTODIAL information** -- narrower than "client
data" as this seat and the CTO had been relaying it. The doctrine wording placed under option (ii) carries HIS words:
`opal-data-assets` holds client/partner custodial information; every other scope is homed by scope at every tier,
bronze and silver included. **This seat does not define "custodial" further than he said it** -- the placement quotes
him, and any narrower reading (for example whether a firm-attributable derivation of custodial data is also custodial)
is a question for him, not an inference.
