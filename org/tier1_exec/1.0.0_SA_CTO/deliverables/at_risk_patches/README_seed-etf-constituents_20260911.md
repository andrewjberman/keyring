# AT-RISK WORK PRESERVED, NOT APPLIED -- `seed-etf-constituents.py`, uncommitted 17 days

**Preserved by** `1.0.0_SA_CTO~Z`, 2026-09-11 ~17:2xZ. **Surfaced by** `2.0.0_SA_COO~Z` (msg 21492).
**Patch:** `seed-etf-constituents_UNCOMMITTED_20260911T1725Z.patch` (37 lines).

⛔ **NOTHING WAS APPLIED, COMMITTED TO THE PRODUCER, OR DEPLOYED. The working-tree file is UNTOUCHED
and still ` M`.** This directory holds a COPY so the reasoning cannot evaporate; it is not a fix and
it does not change what any pipeline runs.

## Why this exists

`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` has carried a substantive
UNCOMMITTED edit -- 13 insertions, 6 deletions -- that **survived the 2026-09-11T14:10:36Z reboot**
and was already dirty at this session's opening `git status`. Site Z's shared tree loses uncommitted
work. This was one `git checkout` or one crash from gone, and the MEASUREMENT inside it would have
gone with it.

Last committer on the file: `b3d830094c`, `1.0.0_SA_CTO~Z`, 2026-08-25 -- **this seat**, and the edit
quotes an Andrew-direct of the SAME DATE, so on the evidence it is most likely this seat's own
work-in-progress left uncommitted across 17 days. That is why this seat preserved it rather than
routing it onward.

## What the edit does -- read from the diff, not from its description

1. **Collapses the two cash rows onto ONE canonical line.** `CASH` -> "Cash & Cash Equivalents",
   and `CASH&OTHER` is deleted from `NAME_CORRECTIONS`. The comment carries Andrew-direct 2026-08-25
   VERBATIM: *"it should always be managed the same way: Fixed Income for Asset Class, Ultra Short
   Duration for Sub Asset, CASH for ticker, and Cash & Cash Equivalents for Name"*, and states that
   the producer normalises both the derived residual row and the issuer sentinel onto the one ticker.
   ⚠ It REPLACES a distinction the prior comment defended on purpose ("one is a row we were given,
   the other one we derived, and the ticker is the only thing that still says which"). Andrew's word
   is the later authority; **that the edit overrides a deliberate prior distinction is the thing a
   reviewer should look at first.**
2. **Drops EMPTY values, not just `None`**, on the batch write: `if v is not None` becomes
   `if v is not None and v != ""`. Its stated basis is a MEASUREMENT: `sub_asset_class` backs the
   `sub-asset-class-index` GSI and DynamoDB REFUSES an empty string for an indexed key attribute --
   *"measured: ValidationException on the first real write"*.

## What is NOT established, and it is the whole reason this is preserved rather than committed

- ⛔ **THIS SEAT DID NOT RE-MEASURE THE ValidationException.** The claim is the diff comment's, and
  verifying it needs a real write against the live table. **An in-comment "measured:" is the author's
  assertion, not this seat's measurement** -- the exact distinction this seat got wrong three times
  today and is not repeating on a production write path.
- **It is untested here**, and it changes a PRODUCER's write behaviour. Committing untested bytes
  into a branch someone may deploy from is an outward act; copying them into a deliverable is not.
- **It does NOT fix `POSN_ASTTAX-Z-W8-S2`** (ARMED, disarm_owner `1.0.0_SA_CTO~Z`). That row is about
  three registry rows blank for 17 days because the seeder **writes only on CREATE and preserves
  existing rows**. This edit changes the empty-value FILTER, not the create-only behaviour.
  ⚠ **But whoever disarms W8-S2 must know these bytes exist and are NOT at HEAD**, or they will
  measure the committed producer and reason about a version someone has already partly revised.
  `2.0.0_SA_COO~Z` is right that this is the load-bearing consequence.
- ⭐ **AN UNEXPLAINED COINCIDENCE, recorded rather than resolved:** the fix sat uncommitted ~17 days
  and W8-S2 measured the blank values stale for ~17 days. That is suggestive, NOT causal, and the
  two mechanisms do not obviously connect (an empty-string write should have RAISED under the old
  filter, not silently persisted). **Nobody should treat the coincidence as a diagnosis.**

## Who decides what happens to it

Not this seat, not tonight. Applying or committing the producer change wants (a) a re-measurement of
the ValidationException claim, (b) a read of whether collapsing `CASH&OTHER` changes any served
artifact, and (c) whoever owns that Lambda's deploy path. Andrew's 2026-09-11 ~15:4xZ scope word is
AMGT_RESAPP and POSN_ASTTAX only; **preserving an at-risk artifact that bears on an in-scope ARMED row
is inside that word, and revising a production producer is not.**

**Verification of this artifact:** `git apply --check --reverse` against the working tree SUCCEEDS,
so the saved patch is EXACTLY the current delta rather than an approximation of it.
