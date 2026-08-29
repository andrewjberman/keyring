# DEPLOY LEDGER -- D1_CATVIEWS reland + refire (chain steps 2 and 3)

**Status:** CLOSED -- COMPLETE, ACCEPT
**Opened:** 2026-08-28T22:15Z
**Closed:** 2026-08-28T22:19Z
**Executor:** `0.7.0_AE_CloudOps~Z`
**TO:** `D1_CATVIEWS.TO-R1-AE`
**Authority:** Andrew-direct verbatim *"yes reland once all fixes are in"* (relayed `1.0.0_SA_CTO~Z`
14134). Gate discharged: GO from `1.0.0_SA_CTO~Z` (14277) and issuer GO from `2.0.0_SA_COO~Z` (14289).

## THE ACT

Two steps, run back to back and deliberately NOT separated by a report:

1. `mdpf_refresh.py --reland --confirm` -- RESERVED-CATEGORY S3 DELETE of 16 conflict-held dated
   gold keys under `s3://opal-data-assets/portal/gold/mdpf/`.
2. `mdpf_refresh.py gold` -- floor -> accrual -> publisher. The floor REBUILDS the deleted keys;
   the publisher projects them to `s3://opal-data-portal-v2/platinum/mdpf/`.

## PRE-FIRE CONTROL -- RUN AND PASSED BEFORE THE DELETE

`latest_run_manifest()` (`mdpf_refresh.py:205`) resolves the delete set AT CALL TIME via
`max(LastModified)`, while Andrew's word names a FROZEN enumeration from the 21:3xZ dry-run. Those
are two different objects sharing one name, so they were diffed mechanically immediately before the
confirm:

```
  MANIFEST   live resolves portal/gold/mdpf/_manifests/2026-08-27/20260828T211849Z.json
             authorized    portal/gold/mdpf/_manifests/2026-08-27/20260828T211849Z.json    MATCH
  KEY SET    authorized 16 · live 16 · diff -u IDENTICAL, zero added, zero removed
```

## THE WINDOW -- CREATED BY THIS ACT, ANNOUNCED BY THIS SEAT

`reland()` at `:331-333` DELETES ONLY; the rebuild is step 3's floor run. So between step 2 and
step 3 the 16 dated gold keys DO NOT EXIST -- gold is ABSENT, not wrong.

```
  before      gold PRE-FIX    platinum PRE-FIX     consistent
  WINDOW      gold ABSENT     platinum PRE-FIX     any cross-plane read is INDETERMINATE
  after       gold CORRECT    platinum CORRECT     consistent
```

**Nobody scores inside the window** (`1.0.0_SA_CTO~Z` 14277 s3). `WINDOW OPEN` and `WINDOW CLOSED`
are broadcast by this seat.

**THE STATE THAT IS WORSE THAN DOING NOTHING:** if step 3 fails or is interrupted mid-window, the 16
gold keys stay DELETED and platinum keeps serving stale bodies with no gold behind them. This is why
step 2 was not fired until step 3 could be carried immediately after. **If step 3 fails, this entry
stays OPEN and the failure is escalated loud to `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z` -- it is not
closed on a partial.**

## ACCEPTANCE -- WHAT COUNTS

Read out of the SERVED BODIES, all 4 scopes, denominator printed:

```
  STRUCTURAL   SMA.aum > 0 + absent_reason ABSENT   at global + 49financial
               SMA.aum == 0.00 + absent_reason PRESENT at cottonwood + inflection
  LITERAL      SMA.aum == 22,794,766.25 -- valid ONLY because tonight's as_of IS 2026-08-27
```

**DOES NOT COUNT:** `mdpf_refresh`'s own VERIFY block (1 artifact type of 4, timestamps only --
14212); the object's `LastModified` (already advanced 13:50:51Z -> 21:19:23Z tonight from the ad-hoc
QA publisher leg, with PRE-FIX content -- 14298); conservation and global==49financial (both pass on
the un-relanded plane -- consistency invariants, printed never scored).

Instruments: this seat's `verify_step3_served_category_views.py` @`a4e16bc65f`, and independently
`3.0.0_SA_CVO~Z`'s ratifier and `1.0.0_SA_CTO~Z`'s cross-plane check. Agreement on the READ is
corroboration; agreement on the CRITERIA is repetition, since all three derive from 14213.

## PROVENANCE

All 16 relanded objects will carry `_provenance.trigger` = **adhoc**. That is HONEST and REQUIRED.
Forging `{"source":"aws.events"}` is forbidden (`1.0.0_SA_CTO~Z` 14134, `3.0.0_SA_CVO~Z` 14150 s3 --
refusal of ratification outright). This entry records the ad-hoc stamp as expected, not as a defect.

## CLOSE-OUT -- 2026-08-28T22:19Z

### The window, measured

```
  OPEN    22:16:5xZ   16 dated gold keys DELETED
  CLOSED  22:17:37Z   floor rebuilt them -- green, a4_objects_built 16, conflicts=0
  duration ~40s. Nothing scored inside it by this seat.
```

### Step 2 -- the delete

16 keys deleted, identical to the pre-fire authorized set (manifest match + `diff -u` identical,
zero added, zero removed). The authorized enumeration and the live resolution were the same object
AT THE MOMENT OF THE ACT.

### Step 3 -- rebuild and publish

```
  22:17:37Z  mdpf-gold-lambda      {"status":"green","errors":[],"a4_objects_built":16}
             manifest ...20260828T221739Z.json   conflicts=0
  22:17:40Z  mdpf-accrual-trigger  SSM 9124d754 -> Success
  22:17:55Z  publisher             published 18, unchanged 0, failed [], missing_pairs []
```

The publisher still reports `unexpected_pairs: [all four category-views]` -- EXPECTED. The
`CATVP-c` enumeration fix is committed (`84fda0fd04`) and deliberately NOT applied per 14197, so
the live function is still the 2026-08-07 build and still blind to the 4th type. It served them
regardless, which is the narrowed behaviour.

### Acceptance -- VERDICT: ACCEPT

```
  SCORED 11 PASS / 0 FAIL over 11 assertion(s); 0 NA_BY_DATE; 0 INDETERMINATE

  global       SMA.aum 22794766.25          absent_reason ABSENT   Client.aum 267632047.22
  49financial  SMA.aum 22794766.252499998   absent_reason ABSENT
  cottonwood   SMA.aum 0.0                  absent_reason PRESENT      <- Direction B intact
  inflection   SMA.aum 0.0                  absent_reason PRESENT      <- Direction B intact
  L2 members carrying aum: 8 of 15   (0 of 15 pre-reland)
  CONTROL conservation 267,632,047.22 + 22,794,766.25 = 290,426,813.47 -- PRINTED, NOT SCORED
```

Body `as_of` 2026-08-27 on all four, read from the BYTES (platinum keys are undated).
NOT cited as acceptance: `mdpf_refresh`'s VERIFY block (it printed PASS x4; it reads 1 artifact type
of 4 on timestamps only) and `LastModified` (already advanced tonight for an unrelated reason).

### Stop conditions -- all four checked, none tripped

```
  gold SMA.aum > 0 at global + 49financial       MET
  gold vs platinum disagreement after publisher  NONE -- both 22,794,766.25
  cottonwood/inflection gained a non-zero SMA    NO
  bundle filename                                0.4.0_DT_ClientPlatform~Z's leg, not this one
```

### Provenance -- honest, and NOT what was predicted

All four relanded objects carry `_provenance.trigger = "manual"`, not `"adhoc"`. Confirmed at
source: `mdpf_gold_consolidator.py:1398` writes `trigger.get("kind")` into the ARTIFACT, while
`:1148` writes the whole dict into the RUN MANIFEST -- so `detail.source = "adhoc"` lives in the
manifest and never reaches the artifact. `manual` is the honest kind for a hand-invoked run and is
not `scheduled`, which is the claim that was forbidden. Nothing forged. Surfaced as 14329 because a
ratifier asserting `"adhoc" in trigger` against the artifact would refuse a correct reland.

**NOTHING HALF-LANDED.** Both steps completed; gold and platinum agree; the ledger closes on a
measured acceptance, not on rc=0.
