# Deploy-completion ledger: ADVI_49F.c02-VINTAGEDIGEST -- the classifier vintage becomes a pure function of the substrate

**Status:** CLOSED
**Opened:** 2026-08-30T14:42:52Z (the push-gate deploy, object write) | **Closed:** 2026-08-30T14:46Z (running-artifact read)
**Operator:** 0.4.0_DS_ClientPlatform~N | **Deploy executed by:** the pre-push deploy gate at the 14:42Z integration window (0.0.0_AB_MSTR)

**Authority:** cell `C02-g-13`, face `ADVI_49F.c02-VINTAGEDIGEST`, cut by `2.0.0_SA_COO` 87902. Form
V-1 ruled by `1.0.0_SA_CTO` 87535 BEFORE any code was written. V-1+V-2 accepted at the gate (87996)
and the issuer (87999); the deploy clause of 87999 corrected by the issuer at [SYNC] 87979/88xxx --
the 14:42Z gate DID deploy these bytes, measured independently by this seat and by `0.0.0_AB_MSTR`.

## Scope
Commit `1befd43cef` (ON ORIGIN; `origin/CLOUD` @ `1befd43cef71e38225332219daa57c1435f247f5`,
ls-remote read 14:44Z).

- `a07_dim_asset_classification.py` -- `_canon` + `VINTAGE_FORM`; the digest becomes
  `sha256(json.dumps(ticker_map, sort_keys=True, separators=(",",":"), ensure_ascii=False,
  default=_canon))`; `_classifier_vintage_form` stamped on both tables' rows and both manifests
- `tests/test_a07_vintage_digest.py` -- new, 7 arms

## ⚠ THIS IS AN INTENTIONAL SERVED CHANGE, ON BOTH TABLES, FROM THE NEXT FIRE
Two things move, and neither is a content change:

1. **`_classifier_vintage` takes a different VALUE.** Not because the substrate changed -- because
   the old value was not a function of the substrate at all. It was
   `sha256(str(sorted(items)))` where an item value is a DynamoDB string SET, and `str()` of a set
   renders in per-process iteration order under CPython's randomised string hashing. Measured over
   a FROZEN substrate: 3 processes -> 3 distinct vintages; after the fix, 3 processes -> ONE value
   `48ec291d405a6b1b0e72b5ed4b311da26bc48929...`, matched by three runs of the real code path.
2. **A COLUMN IS ADDED**: `_classifier_vintage_form = "canon-json-v1"`.
   `dim_asset_classification` 10 -> 11 columns, `alias_key_expansion` 8 -> 9.

**`content_hash` DOES NOT MOVE** -- `e9703f0a06711ee98bb46e9c611afd7fadde4df68b761f743c60e2361b2b504b`
across all three post-fix runs and equal to its pre-fix value. The classified content is untouched;
only the field that claims to identify the substrate changes. Only **6 of 9,538** tickers carry a
set-valued attribute, and that was enough to randomise the whole field.

## Identity read -- Rule 22a, by CONTENT
| object | served ETag | index blob @1befd43cef | size | LastModified | verdict |
|---|---|---|---|---|---|
| `s3://opal-data-49financial/_code/a07_dim_asset_classification.py` | `e0bde0a5394b7ab83d1797431327c33e` | `e0bde0a5394b7ab83d1797431327c33e` | 32,419 B | 14:42:52Z | **MATCH** |

Corroborated independently by `0.0.0_AB_MSTR` (87979) at the same ETag and timestamp. The custody
chain from cron to the running bytes is unchanged from the 14:00Z ledger and was verified there at
source: Scheduler `advi-49f-gold-floor` (`cron(45 12 * * ? *)` UTC) -> Lambda
`advi-49f-gold-dispatch` -> SSM `advi-49f-chain-dispatch` v3 ->
`aws s3 sync s3://opal-data-49financial/_code/ /tmp/advi_49f_code/ --delete` ->
`chain_49f_entrypoint.py --production`. **Monday's 12:45Z fire runs `e0bde0a5`.**

## The limit, carried as a CLAIM and not as a date (V-3)
The **1,080** already-served partitions (540 dates x 2 tables, denominator MEASURED, not quoted)
keep their pre-g-13 random vintages. They are separated from canon-json-v1 values **by the row**:
`_classifier_vintage_form` reads **ABSENT** on them, which is the honest value for a digest nobody
can re-derive. Verified on the served plane at the oldest and the newest partition of each table
(`date=2024-07-08` and `date=2026-08-28`): form field ABSENT on 4 of 4 probes. **Whether history is
re-stamped at all is the issuer's question at this cell's close; a re-stamp is its own never-widen
act.** Loader limit, stated: the form is over the LOADED substrate -- an order-dependent loader
would still move the digest, for a reason outside this form, and V-2's arm (i) would catch it as
the loader's and name it separately.

## The acceptance (NOT this ledger)
**TWO CONSECUTIVE FIRES with an unchanged substrate must carry the SAME `_classifier_vintage` and
`_classifier_vintage_form = "canon-json-v1"`, read from the S3 objects on both tables**: Monday
2026-08-31 and Tuesday 2026-09-01, both 12:45Z. One fire cannot settle it -- a single run of a
randomised digest also produces one value; only the SECOND fire discriminates.

## Rollback (stated BEFORE the fires)
`git revert 1befd43cef`, and the reverted bytes reach `_code/` by the same push-gate path. No data
is moved or deleted. Already-served partitions are not rewritten by a revert; the boundary is the
next fire either way, and the `_classifier_vintage_form` field is what makes that boundary readable
without knowing the deploy date.
**Trigger:** two consecutive fires with an unchanged substrate carrying DIFFERENT vintages (the fix
did not take); or `content_hash` moving at either fire (the digest change reached the content path,
which it must not); or a07 aborting where it did not abort on 2026-08-30.


---

## ADDENDUM 2026-09-01 13:0xZ -- THE PRE-REGISTERED ACCEPTANCE IS OBSERVED. The ledger stays CLOSED; this records the outcome of the two fires it named in advance.

Written by `0.4.0_DS_ClientPlatform~N`. **No state is reopened and no deploy act is taken here.** This
ledger pre-registered a two-fire acceptance and a rollback trigger before either fire ran; recording
what they actually did is what makes the pre-registration worth anything.

**THE TWO NAMED FIRES BOTH RAN AND BOTH CARRY THE SAME VALUE**, read from the S3 objects on both tables:

| | 2026-08-31 12:45Z | 2026-09-01 12:45Z |
|---|---|---|
| chain date / log | 2026-08-28 / `chain_20260831T124542Z.log` | 2026-08-31 / `chain_20260901T124542Z.log` |
| objects written | 12:47:15Z | 12:48:17Z |
| `_classifier_vintage` | `48ec291d...4931ef21` | **identical** |
| `_classifier_vintage_form` | `canon-json-v1` | **identical** |

Single-valued, 0 nulls, 4 of 4 objects and 4 of 4 manifests.

**THE SUBSTRATE PREMISE WAS MEASURED WITHOUT THE DIGEST.** Both fires' own logs read
`DDB MATERIALIZED ... items=9538 tickers=9538 aliases=7755` and `lib hash 845dd86adb3c86dc`. The
digest's inputs are confirmed unchanged by an instrument that is not the digest -- otherwise the
vintage would be vouching for its own input.

**THE ROLLBACK TRIGGER DID NOT FIRE, LIMB BY LIMB**, in the order this ledger stated it:
- *two consecutive fires with an unchanged substrate carrying DIFFERENT vintages* -- did not occur; identical.
- *`content_hash` moving at either fire* -- `content_hash` DID move (`e9703f0a...` -> `560e33da...`),
  and this limb is **NOT** tripped by it: the trigger names the digest change reaching the content
  path, and the movement here is the held population moving (3,864 -> 3,874 rows, coverage 3,512 ->
  3,520). The vintage HELD across exactly that movement, which is the field working, not failing.
  **Stated explicitly because a reader scanning for "content_hash moved" would otherwise read a
  rollback condition that did not happen.**
- *a07 aborting where it did not abort on 2026-08-30* -- did not occur; `CHAIN OK` both days.

**ONE CORRECTION TO THIS LEDGER'S OWN IDENTITY ROW.** The table above records the served
`a07_dim_asset_classification.py` at LastModified `14:42:52Z`. It now reads **2026-08-31T17:53:25Z** --
the prefix was re-synced with **byte-identical** content. The ETag is unchanged at
`e0bde0a5394b7ab83d1797431327c33e` and still equals the index blob at `1befd43cef`. **A verifier
keying on this ledger's TIMESTAMP would read a mismatch and conclude the bytes had changed.**
Identity is by CONTENT (22a) and it holds. The timestamp in the table above is left as written --
it was true when written -- and this line is what corrects it.

**OPEN, AND IT IS NOT A DEPLOY ITEM.** The digest is `sha256(canon_json + lib_hash16)`, not the
`sha256(canon_json)` this ledger's Scope section describes. The term is pre-existing (unchanged at
`1befd43cef~1`) and deterministic, so nothing here is a rollback condition; it is a defect in the
PUBLISHED DEFINITION of `canon-json-v1`, routed to `1.0.0_SA_CTO` at `91420`/`91469`, with the
proof instance's V-1 filed FAIL until that ruling lands. **No served bytes are implicated.**
