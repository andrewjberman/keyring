# Never-widen sign-off packet -- the ingest mirror release: an unknown key is a counted SKIP, and a second daily Inflection poll

Author `2.0.0_SA_COO~P`, 2026-10-02 ~23:1xZ. **Source:** @2e00498347, built today in commit 2e3d8afd0c under CTO batch 63 item 6 and
batch 88 item 6, lane IRPT_BCKEND_FAST_P_MIRROR. **Rows:** IRPT_BCKEND-W99-S3, S216. **Sequenced** after the Inflection serving
packet, which is SERVED (ledger record 8c10791252). **Halves owed:** `1.0.0_SA_CTO` and `2.0.0_SA_COO~P`.

## Why

Every Inflection mirror run ends in an error while data still lands. Today's 13:05Z run (RequestId `083fbabe`) raised
`MirrorRaise: ALIEN SURPLUS on eclipse/inflection: 2 unexpected key(s) under eclipse/inflection/bronze/`. The two keys are another
writer's: `eclipse_membership_map/date=.../manifest.json`.
- The copies happen BEFORE the membership check raises. The data lands, the run reads as failed, and a real failure would read
  the same.
- A raw file that lands after 13:05Z waits a full day.

## The act (ONE ledger entry)

The opal-assets root, read ~23:0xZ: **3 to add, 1 to change, 0 to destroy, and nothing else.**

| leg | act | resource | before | after |
|---|---|---|---|---|
| M1 | targeted apply, the mirror's code | `module.mirror.aws_lambda_function.this` (`opal-assets-ingest-mirror`) | CodeSha256 `XYgkNk8q...` (S3 `JZBubUswuQJf`; the live bytes equal 97c22dc234, 2026-08-10) | **`MJ/EfEjrvkITwV65l3kVaK0XIex3GHGofK17nD2dvig=`** (S3 `NLE.I.KulB5rBRoc4M_RGIAPLHemMvfq`) |
| M2 | targeted apply, the second schedule | `aws_cloudwatch_event_rule.mirror_inf_late`, its target, its permission | absent | `cron(5 17 * * ? *)` UTC, daily, input `{"firm":"inf"}`. A schedule, never an object trigger |

**Members.** The zip has one member, `lambda_function.py`, equal to HEAD's blob, and its map hash equals the S3 metadata. Against the
DEPLOYED code it moves two commits:
- **@2e00498347** (behaviour):
  - an unexpected key that no class explains is a SKIP line naming the keys, counted as `unknown_key_class_skipped`; the field
    `alien_surplus`, always 0, is removed;
  - the conservation check counts the row's OWN failures;
  - a failed copy is reported at cycle end, naming the key.
- **@97380d4869** (comment only): the DOOR 5 note now cites the lifted July hold (IB-pr-241).

## Blast radius, by the code's own rule

**What does not move:** which keys are copied, from where, and to where. The copy loop is unchanged.

**What STILL raises, unchanged:**
- a missing landing;
- an unverified write;
- a size or digest mismatch;
- a key collision;
- a failed copy at cycle end;
- growth of the two baselined classes.

**What moves:**
1. An Inflection run whose destination holds another writer's keys ends OK, with a SKIP line and a count, instead of `MirrorRaise`.
2. A second Inflection cycle runs at 17:05 UTC every day, copying any raw file that landed after 13:05Z. The copy is idempotent:
   keys already landed are re-verified, not duplicated. The Cottonwood scheduler and the first Inflection rule (`cron(5 13 * * ?
   *)`) do not move. The first rule's comment says 15:05Z; that disagreement is left as found and named here.

**Writers of the destination prefix:** two -- the mirror, and the Eclipse membership-map writer whose manifests are the 2 keys. The
mirror never writes or deletes that writer's keys; it now counts them.

**Downstream:** Inflection's holdings producer (served today) fires at 14:00 UTC and reads the day's landed bronze. A file the 17:05
poll lands is read by the next day's fire, as a late file is today.

**Tests:** `infra/aws/lambda/opal-assets/tests/test_ingest_mirror_unknown_key_skip.py` passes 7 at HEAD. The negative control
against the unchanged mirror read 3 failed and 4 passed on 10-01.

## Rollback, per key

- **M1:** `s3api copy-object` of the prior artifact version `JZBubUswuQJfMBfIKeFlSvpaj0jjCjdg` (`XYgkNk8q`) over the key, then the
  same targeted apply.
- **M2:** destroying the three resources is a deletion and needs Andrew's word. Without it, a targeted apply sets the rule's
  `state` to DISABLED.

## Conditions (ledger legs)

1. The plan is exactly M1 and M2 (3 to add, 1 to change). The map hash equals the S3 metadata (row S278's check).
2. After M1, read the live CodeSha256 and run a re-plan, which must show No changes.
3. One `{"firm":"inf"}` invoke after M1 ends OK, with the copied and verified counts and `unknown_key_class_skipped` printed.
4. After M2, read the rule's schedule and its target input. The next 13:05Z fire (2026-10-03) and 17:05Z fire, read from the log,
   both end OK with no `MirrorRaise`. That is the A1 leg.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-02 ~23:1xZ, on this packet's bytes at the commit that carries it.
- The write set is one function's code (two commits, one of them comment-only) and three schedule resources.
- The copy set does not move.
- Every failure that must raise still raises.
- The rollback is per key.

## CTO half

OWED.
