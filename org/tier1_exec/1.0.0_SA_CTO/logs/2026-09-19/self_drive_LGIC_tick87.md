# /self-drive LGIC -- tick 87 (2026-09-19 ~13:0xZ-13:2xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## Sequence and scope

Clean; CAPACITY **AT CAP 3/3**. **0 open of 162, 0 NOT-MEASURABLE**, re-derived at write time.
**COMPLETION TEST: NOT DONE -- 1 of 4. No open calls in LGIC scope.** ⭐ **Both LGIC projects drained to ZERO
in one tick** -- `LGIC_ENFORCE` round 15's retired-discriminator sweep (`EN-d-1-r15`, my r14 recut) and
`LGIC_LGCTFM` round 7's `LT-g-1-r7` are both `complete`.

## THE ACT -- `IRPT_BCKEND-S94` RULED INTO RATIFIED TEXT, v0.15 @`c0a1466be5`

**RULING: `platinum/<firm_id>/ownership_map.json` EXISTS FOR EVERY CLIENT FIRM THE REGISTRY ENABLES** -- an
EMPTY map where a firm has no advisors, never an absent key.

### ⛔ AND THE PROBLEM IS A CONSEQUENCE OF MY OWN RULING

`S90` bars `ListBucket` -- correctly; on a platinum prefix the key names are themselves firm-attributable.
**But WITHOUT `ListBucket` a MISSING key returns `AccessDenied`, not `NoSuchKey`**, and
`_authz/loaders.py:106-114` re-raises anything but `NoSuchKey`. ⛔ **So an ABSENT map and a GENUINE DENIAL
became indistinguishable to the loader, both surfacing as `UNEXPECTED`.** Measured by `2.0.0_SA_COO~B`:
`inflection` has no map (404), so its advisors stay `UNEXPECTED` **even with the grant in place.**
⭐ **MY NARROWEST-GRANT RULING CREATED A NEW INDISTINGUISHABILITY, and the honest framing is that this clause
REPAIRS it -- not that it improves something.**

⭐ **WHY THIS AND NOT A MITIGATION: IF THE MAP ALWAYS EXISTS, "ABSENT" NEVER HAPPENS, AND `AccessDenied`
UNAMBIGUOUSLY MEANS DENIED. The ambiguity is ELIMINATED, not reduced** -- which is why it beats anything that
teaches the loader to guess.

**Two alternatives refused BY NAME so neither is re-proposed:** a key-scoped `ListBucket` (the one `S90` bars),
and ⛔ **a loader that reads `AccessDenied` as "no map" -- which MASKS A REAL DENIAL**, the same false-clean
class as the holdings carve-out. **The loader's behaviour does not change under this clause.**

**Routing stated, not inferred:** the producer is **DS-owned**, and ⛔ **the PRODUCTION is NOT a rider on an
IRPT round** -- it is cut in the producer's own lane. **What this PRD owns is the INVARIANT IT CONSUMES, and
it went into ratified text precisely because cells are cut from ratified text and not from a channel.**
**Acceptance shape: `n of N` registry-enabled firms, `N` READ FROM THE REGISTRY, never a typed list.**

## Not signed, on instruction -- and that is the mechanism working

`2.0.0_SA_COO~B`: *"do not sign 609fbba9de"* -- the `rtf-10` packet was re-cut twice (`S93`/`S95`, then `S96`'s
manifest `staged_from` gap). ⭐ **A superseded blob named unprompted is blob-binding doing its job, and it has
saved a signature on a stale object twice today.** My half waits for the third-pass blob.

**And on `2.0.0_SA_COO~B`'s explicit question:** I do **NOT** read the build-store restore as needing its own
never-widen half. ⭐ **It restores an artifact key to the bytes ALREADY SERVING -- the served plane does not
move, which is the verified-DELTA=0 case CLAUDE.md's own NEVER line exempts.** `S93` (K-DIR to four of the
seven serving roles) is squarely inside my condition (3); no widening.

## Carried into the round-6 analysis

⚠ **The live `irpt-directory-search` zip carries the seam file as a CRLF HAND COPY** -- 197,344 bytes / 6,224
CR against the committed blob's 191,120 -- and **the 05:22Z build has NO REPRODUCING TREE STATE.** R-40's class
**on a whole function.** `K-CODE`'s rebuild replaces it; **the analysis will say so rather than leave a reader
wondering whether it was ever reconciled.**

## Owed by this seat

1. **`IRPT_BCKEND` round-6 analysis** -- the binding check with BOTH classes and its `.tools/` home; `rt-7`'s
   `_no_grant` decision read before anything is cut against `FWD-5`; and the CRLF-hand-copy carry above.
2. **`IB-rtf-10` CTO half** -- on the THIRD-pass blob, not `609fbba9de`.

## Open calls at Andrew -- 5, card 1 ROUTE RULED / act OPEN (@`3948ba37d9`; not re-swept this tick)

## Compiler Tools

`sequence-check.py` - `_open_tos_census` (None-aware) - `git rev-parse HEAD:<packet>` (the blob I did NOT sign)
- `.owned-paths.yaml` lane resolution (`ANY_CTO`) - `prd-signoff.py status` before and after -
`safe-commit.sh` - `send_message` (2 recipients, 2 DELIVERED).

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `4290315df9` (`ls-remote`). **state: ARMED**
