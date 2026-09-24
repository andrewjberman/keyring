# AMGT_HARVST -- current state

Seat `2.0.0_SA_COO~Y` (Claude, site Z). Mandate `COO_Y_HARVST.md` as amended by the ADDED SCOPE ITEM
(`2b`) at `98edbe915d`. Worktree `C:/tmp/coo-y-harvst-2b-20260924`, branch `harvst-2b-y-20260924`.
Trunk `CLOUD`; this lane commits, `0.0.0_AB_MSTR~Z` pushes.

## `2b` -- THE GRADED `chatter_daily` GOLD FOR THE AMGT UNIVERSE: BUILT, AND THE SUCCESS BUCKET IS EMPTY

**THE ONE SENTENCE THE MANDATE ASKS FOR: 0 of 191 identities -- and 0 of 50,997 rows -- carry a
non-empty success bucket, because `COMPLETE` requires all five `ENABLED_PUBLISHERS` to cover the day
and FOUR OF THE FIVE have ZERO retained `listing_hit` rows.** That is a COLLECTION fact, not a reader
fact: the reader works, and this build is what proves it works over the whole universe rather than
over six hand-written names.

**THE TABLE, read back from S3 rather than taken from the producer's summary:**
`s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-09-24/part-20260924T105051Z.parquet`,
83,030 bytes (`ContentLength` == bytes read), 50,997 rows = **191 securities x 267 days**
(2026-01-01 backfill floor -> 2026-09-24). The predecessor snapshot covered **6** securities x 266
days = 1,596 rows; the universe it should have covered is **191 of 250 names** (59 carry no
`security_key`, are counted, and are dropped -- C-ONE-IDENTITY forbids inventing one).

**EVERY ROW NOW CARRIES ITS DENOMINATOR, which is the mandate's own test of a graded row.**
`data_status` was a CLASS and a class is not a denominator. Two columns were added to
`GOLD_DAILY_SCHEMA` and are populated on every row: `publishers_covered` / `publishers_enabled`.
Measured on the served bytes: 0 rows missing either, `publishers_enabled` == 5 on all 50,997, and
**0 rows where the class disagrees with the fraction**.

| measured on the 2026-09-24 snapshot | value | denominator |
|---|---|---|
| `data_status = COMPLETE` | **0** | 50,997 rows / 191 securities |
| `data_status = PARTIAL` | 1 (`992_HK_Equity`, 1 of 5 publishers) | 50,997 rows |
| `data_status = DENIED` (0 of 5) | 50,996 | 50,997 rows |
| securities with >=1 article day | **55** | 191 |
| rows carrying >=1 article | 201 | 50,997 |
| retained `listing_hit` rows | **20, ALL `wsj`, ALL one query "Lenovo Group", ONE day (09-23)** | 20 |
| publishers with ZERO `listing_hit` rows | **4** (`barrons`, `bbg`, `ft`, `sa`) | 5 enabled |

⛔ **THE SHAPE THAT MATTERS MOST AND IS EASY TO MISREAD: 201 rows carry articles while reading
`DENIED`.** Mentions come from silver `article`; the coverage grade comes from silver `listing_hit`.
The two are different tables and the second is nearly empty, so the table can hold real chatter for a
name and still grade it 0 of 5. That is the grade being HONEST, not wrong -- but a consumer ranking on
`mention_score` without reading `publishers_covered` would be ranking over ungraded water.

**THE UNIVERSE -> `securities` STEP IS NOW CODE, NOT A HAND-WRITTEN FILE.**
`lib/research/harvest/universe_securities.py` (new) reads the pool universe object and emits the list
the `publication_gold` builders take. It resolves NOTHING: `security_key` is read straight off the
universe, which is the crosswalk's output. The one derived field is the alias set (the universe
carries no alias or company column), by two stated rules -- ticker-tail strip and repeated
corporate-suffix stripping -- with every rule's touch count printed: 250 names read, 191 securities,
59 without identity, 27 ticker tails stripped, 162 suffix aliases added, 11 aliases dropped as
unusable, 0 securities with no alias, 0 `composite_figi` (the crosswalk holds none: 0 of 254 records).
Artifact: `universe_securities_2026-09-16.json` beside this file, named for the universe vintage it
was built from.

**TWO CONTROLS RAN BEFORE ANYTHING WAS WRITTEN, and both are cases that were FREE to differ:**
1. **Alias fidelity.** Of the six hand-curated names earlier rounds built gold from, **4 of 6**
   reproduce exactly from the universe (`Boeing`, `Costco`, `Home Depot`, `Lenovo`). The two misses
   are SOURCE-DATA facts, not rule defects: the universe misspells `Haliburton` (row
   `AMGT_HARVST-Z-S19`), and it carries the legal name `Valero Energy` where the curated file carries
   the short common name. Both are asserted in the test file in the shape the universe actually
   carries, so a later fix shows up as a test change rather than as drift.
2. **No regression on the mention table.** The 2026-09-24 mention build reproduces **every** row of
   the 09-23 snapshot: 0 pairs present there and absent here. 21 extra pairs appear on those same four
   securities, and the discriminator says why -- **21 of 21 come from articles ABSENT from the 09-23
   snapshot (silver grew 94 -> 118 article keys), and 0 come from a matching change.** Mention gold:
   `date=2026-09-24/part-20260924T105025Z.parquet`, 263 rows, 55 securities, 118 articles read.

**BOUNDS HELD.** No vendor call, no deploy, no delete, no promotion, no new notifier, no publisher
access, no backfill. Both builds read RETAINED silver only. `write_gold` puts with
`IfNoneMatch="*"`, so neither write could overwrite an existing part; the prior 09-22/09-23 snapshots
are untouched. The gold table is NOT served today -- the deployed `amgt-resapp-chatter-axis` reads
`CHATTER_AXIS_SOURCE=legacy` (read live at 10:4xZ: `CodeSha256 Xdwp7Ir...`, 512 MB, 120 s), so this is
not a served-output write and needs no never-widen pair.

⚠ **WHAT THIS DOES NOT DO, stated because a populated table invites the opposite reading: it does not
keep itself populated.** The gold build has NO schedule -- both builds in this table's history were
manual runs, and this one is a third. Ad-hoc gold runs are permitted for QA; a production table needs
its own scheduled producer, which is a deploy act and is not this lane's. Owner: `1.0.0_SA_CTO~Z` to
route. Until then the table's vintage is the date of the last hand-run.

## H03 step 2a -- LANDED AND CLOSED BY THE AE LANE, nothing owed by this lane

Applied `2026-09-24T05:09:00Z` by `0.7.0_AE_CloudOps~A` (msg 25266): 1 imported, 0 added, 3 changed, 0
destroyed; `CodeSha256 Xdwp7Ir...`, 512 MB, 120 s, `CHATTER_AXIS_SOURCE=legacy`; never-widen held (2
`chatter_daily` entries, 0 removals); `plan -detailed-exitcode` rc=0. The 10:00Z scheduled fire closed
leg `daily` (msg 25403): `rows_written=2`, both days' pointers present, **`payload_hash` IDENTICAL
across 09-23 and 09-24** -- a fresh generation with unchanged content, which is R-19's nonpublishing
claim measured. Ledger `amgt-h03-leadpanel-y-20260924`: `baseline`, `artifact`, `pair`, `tf`, `daily`
CLOSED; **`served` is the only open leg and is CVO-owned.**
⭐ That identical payload hash is the same fact this file's `2b` section measures from the other end:
the chatter water was stale because `chatter_daily` held six names, and it now holds 191.

## Parked (one line each, owner, un-park condition)

- **Scheduled producer for the gold chatter tables** -- `1.0.0_SA_CTO~Z` to route; un-parks when a
  schedule exists or the table is ruled QA-only. ⚠ R-55 @`7dda0c24ab` sharpens this from a preference
  to a NAMED DEFECT: ad-hoc gold runs are QA-only while production pipelines must be scheduled, so an
  unscheduled production table is off-law, and the owner it needs is **not Andrew**.
- **`listing_hit` collection for the four silent publishers** (`barrons`, `bbg`, `ft`, `sa`) -- this is
  the ONLY thing standing between this table and a non-empty success bucket. ⭐ **R-55 MEASURED WHAT THIS
  LINE ASSUMED, and the answer came back the other way from what the check expected:** the constraint is
  not stale but the question was **NEVER PUT TO HIM** -- R-21's whole seven-row card table names no
  publisher access, and `publisher access` / `listing_hit` / `barrons` / `ENABLED_PUBLISHERS` return
  ZERO hits across the rulings file. Neither granted nor withheld, just unaddressed. The wider reading
  of "all the egress you want for vendors" is REFUSED as a silent widening (a word is relayed, never
  adjudicated wider). So this is now a **third reserved card at Andrew**, carried by `1.0.0_SA_CTO~Z`;
  un-parks on his answer to the card, not on an inference from R-21.
- **`AMGT_HARVST-Z-S19`** (universe misspells "Haliburton") -- routed to the `universe/v1` producer's
  owner; INERT (HAL has 0 mention rows today), un-parks if that name is ever ranked.
- **`lib/research/price/**` explicit-state migration** rides in `6e9868b903` for coherence --
  `2.0.0_SA_COO~Z` may overwrite; un-parks on that seat's word.
- **Arrow writer/reader tuple binding** (R-15/R-17) -- `4.0.0_SA_CRO~Z` holds the design; the 05:0xZ
  dry-run invoke (Arrow 15.0.2 read Arrow-24 parquet, no error) is the first target-runtime read.
- **The `org/XXX.md` 1b-F row for this lane** still scopes a 20-minute loop to IRPT Analysis, while
  this lane was re-seated onto AMGT by mandate at 02:46Z and the IRPT `~Y` instance is dead. NOTHING
  WAS ARMED this session. Owner `1.0.0_SA_CTO` (the row's landing seat); un-parks when that row is
  re-scoped or stood down.
