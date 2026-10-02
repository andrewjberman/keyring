# Never-widen sign-off packet -- the ingest mirror release: the membership-map writer's two files are an explained foreign class, and a second daily Inflection poll

Author `2.0.0_SA_COO~P`, 2026-10-02 ~23:1xZ; **RE-CUT ~23:2xZ** after CTO batch 190 refused the first cut. **Source:** @b7a2acb18c
(the re-cut) over @2e00498347, under CTO batch 63 item 6, batch 88 item 6 and batch 190, lane IRPT_BCKEND_FAST_P_MIRROR. **Rows:** IRPT_BCKEND-W99-S3, S216. **Sequenced** after the Inflection serving
packet, which is SERVED (ledger record 8c10791252). **Halves owed:** `1.0.0_SA_CTO` and `2.0.0_SA_COO~P`.

## Why

Every Inflection mirror run ends in an error while data still lands. Today's 13:05Z run (RequestId `083fbabe`) raised
`MirrorRaise: ALIEN SURPLUS on eclipse/inflection: 2 unexpected key(s) under eclipse/inflection/bronze/`. The two keys are another
writer's, both live today: `eclipse_membership_map/date=2026-09-24/manifest.json` and `.../membership_map.json`.
- The copies happen BEFORE the membership check raises. The data lands, the run reads as failed, and a real failure would read
  the same.
- A raw file that lands after 13:05Z waits a full day.

## The act (ONE ledger entry)

The opal-assets root, read ~23:0xZ: **3 to add, 1 to change, 0 to destroy, and nothing else.**

| leg | act | resource | before | after |
|---|---|---|---|---|
| M1 | targeted apply, the mirror's code | `module.mirror.aws_lambda_function.this` (`opal-assets-ingest-mirror`) | CodeSha256 `XYgkNk8q...` (S3 `JZBubUswuQJf`; the live bytes equal 97c22dc234, 2026-08-10) | **`V3oFb2ix4BKlxymtaIHOQRHdwx256KfX4mbuoEOQ838=`** (S3 `wep..7B7sOiUVchiKJu4TXpoREov3bTL`, 10,859 bytes) |
| M2 | targeted apply, the second schedule | `aws_cloudwatch_event_rule.mirror_inf_late`, its target, its permission | absent | `cron(5 17 * * ? *)` UTC, daily, input `{"firm":"inf"}`. A schedule, never an object trigger |

The first cut's artifact (`MJ/EfEjr`, S3 `NLE.I.KulB5r`) is superseded and is never applied.

**Members.** The zip has one member, `lambda_function.py`, equal to @b7a2acb18c's blob byte for byte (downloaded and compared), and
its map hash equals the S3 `content-sha256` metadata. Against the DEPLOYED code it moves three commits:
- **@b7a2acb18c** (behaviour, the re-cut): on the `eclipse/inflection` row only, keys matching
  `eclipse_membership_map/date=YYYY-MM-DD/(manifest|membership_map).json` are an EXPLAINED FOREIGN CLASS. They are printed on a
  `FOREIGN CLASS` line and counted as `foreign_membership_map_class`, and are never copied, overwritten or deleted. **Every other
  key no class explains still raises ALIEN SURPLUS**, and `alien_surplus` stays in the result (0 on a run that completes).
- **@2e00498347** (behaviour; its blanket SKIP is reverted by the re-cut):
  - the conservation check counts the row's OWN failures;
  - a failed copy is reported at cycle end, naming the key.
- **@97380d4869** (comment only): the DOOR 5 note now cites the lifted July hold (IB-pr-241).

## Blast radius, by the code's own rule

**What does not move:** which keys are copied, from where, and to where. The copy loop is unchanged.

**What STILL raises, unchanged:**
- ALIEN SURPLUS: any key under a row's prefix that no class explains, including any other file in the membership-map partition and
  the same file names under any other row's prefix;
- a missing landing;
- an unverified write;
- a size or digest mismatch;
- a key collision;
- a failed copy at cycle end;
- growth of the two baselined classes.

**What moves:**
1. An Inflection run whose destination holds ONLY the membership-map writer's two named files beyond its own ends OK, with a FOREIGN
   CLASS line and a count, instead of `MirrorRaise`.
2. A second Inflection cycle runs at 17:05 UTC every day, copying any raw file that landed after 13:05Z. The copy is idempotent:
   keys already landed are re-verified, not duplicated. The Cottonwood scheduler and the first Inflection rule (`cron(5 13 * * ?
   *)`) do not move. The first rule's comment says 15:05Z; that disagreement is left as found and named here.

**Writers of the destination prefix:** two -- the mirror, and the Eclipse membership-map writer whose two files are the 2 keys. The
mirror never writes or deletes that writer's keys; it now counts them. A third writer's key raises.

**Downstream:** Inflection's holdings producer (served today) fires at 14:00 UTC and reads the day's landed bronze. A file the 17:05
poll lands is read by the next day's fire, as a late file is today.

**Tests:** `infra/aws/lambda/opal-assets/tests/test_ingest_mirror_unknown_key_skip.py` passes 9 at @b7a2acb18c. Two are new and pin
the kept raise: an unexplained key inside the membership-map partition raises ALIEN SURPLUS naming it, and the same file name under
the orion row raises. The negative control against the unchanged mirror read 3 failed and 4 passed on 10-01.

## Rollback, per key

- **M1:** `s3api copy-object` of the prior artifact version `JZBubUswuQJfMBfIKeFlSvpaj0jjCjdg` (`XYgkNk8q`) over the key, then the
  same targeted apply.
- **M2:** destroying the three resources is a deletion and needs Andrew's word. Without it, a targeted apply sets the rule's
  `state` to DISABLED.

## Conditions (ledger legs)

1. The plan is exactly M1 and M2 (3 to add, 1 to change; re-read ~23:2xZ: the function's `s3_object_version` JZBubUsw ->
   wep..7B7s and `source_code_hash` XYgkNk8q -> V3oFb2ix, nothing else on it). The map hash equals the S3 metadata (row S278).
2. After M1, read the live CodeSha256 and run a re-plan, which must show No changes.
3. One `{"firm":"inf"}` invoke after M1 ends OK, with the copied and verified counts, `foreign_membership_map_class` = 2 and
   `alien_surplus` = 0 printed.
4. After M2, read the rule's schedule and its target input. The next 13:05Z fire (2026-10-03) and 17:05Z fire, read from the log,
   both end OK with no `MirrorRaise`. That is the A1 leg.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-02 ~23:1xZ; RE-SIGNED ~23:2xZ on the re-cut's bytes at the commit that carries it.
- The write set is one function's code (three commits, one of them comment-only) and three schedule resources.
- The copy set does not move.
- Every failure that must raise still raises, ALIEN SURPLUS included; the only class explained is the one batch 190 named.
- The rollback is per key.

## CTO half

REFUSED on the first cut (batch 190: the blanket SKIP removed the only tripwire). OWED on this re-cut.
