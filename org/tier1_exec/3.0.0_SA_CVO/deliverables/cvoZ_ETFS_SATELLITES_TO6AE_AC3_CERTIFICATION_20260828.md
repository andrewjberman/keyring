# CERTIFICATION — `ETFS_SATELLITES.TO-6-AE` · `T6AE-AC3` (the scheduled fire)

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28 ~15:1xZ**
**Completes:** `cvoZ_ETFS_SATELLITES_TO6AE_CERTIFICATION_20260828.md` @`324330f5f2`, which certified
`AC1/AC2/AC4/AC5` and recorded `AC3` as **WITHHELD, NOT FAILED** — waiting on a clock, not on work.
**Instance (certified object):** `0.7.0_AE_CloudOps~S`'s AC3 evidence report (msg 13073), filed
@`bae0325e89`; runbook @`28c465b93b`.

---

## VERDICT: **`T6AE-AC3` CERTIFIED — EXERCISED.**

`ETFS_SATELLITES.TO-6-AE` now stands at **5 of 5 CERTIFIED, read CRITERION-WISE and never as a bare
5/5**: `AC1/AC2/AC4/AC5` @`324330f5f2`, `AC3` here. The two certificates are the whole set; neither
alone discharges the TO.

**`T5DS-AC6` — RELOCATED-AND-DISCHARGED.** It was relocated into this TO and is met **by `AC3`, not by
the relocation**. The condition this seat committed to withholding on is satisfied by measurement, and
this is the PASS branch — the FAIL/non-fire obligation the lane carried does not arise.

---

## 1. THE CRITERION, AND WHY IT NEEDS TWO LIMBS

> `T6AE-AC3` — **EXERCISED, it FIRED ON ITS OWN SCHEDULE.** An ad-hoc invocation does not discharge
> this, and neither does a successful apply. Evidence must distinguish a scheduled fire from a manual
> one — the artifact's `LastModified` (UTC, `s3api`) aligned to the schedule, **plus the invocation
> record.**

The criterion names **two** limbs deliberately, and the reason is visible in the evidence: the
artifact limb alone cannot separate a scheduled write from a manual one, because **both produce a
write.** The invocation record is what carries the attribution.

## 2. ⛔ THE DIVISION OF INSTRUMENTS, STATED RATHER THAN BLURRED

**Rule 22: a second seat's confirmation via the FIRST seat's method is REPETITION, not corroboration.**
So the two limbs are held by two different seats on two different instruments, and this certificate
says which is which.

| Limb | Instrument | Whose | Rung |
|---|---|---|---|
| The artifact changed **at the cron boundary** | `s3api list-object-versions` — version history | **MINE**, run at this seat | measured |
| The fire was **SCHEDULED, not ad-hoc** | CloudWatch invocation record (`argv` / `event_keys`) | **`0.7.0_AE_CloudOps~S`'s**, CITED as theirs | measured, carried |

**MY LIMB, measured at ~15:1xZ — a DIFFERENT instrument from the peer's log read:**

```
s3api list-object-versions  s3://opal-data-cot/platinum/satellites/registry.json
  2026-08-28T07:00:19Z   2196 B   VersionId 9EnoqfgmUV...   IsLatest=True    <- the scheduled fire
  2026-08-28T01:38:46Z   2196 B   VersionId xLcuAW7VMbG...
  2026-08-28T01:09:51Z   2182 B   VersionId D1iVAJ4LJOq...
  DeleteMarkers: key ABSENT from the response  ->  ZERO delete markers
  Versions: 3    IsTruncated: None
```

`07:00:19Z` sits **19 seconds past the `cron(0 7 * * ? *)` boundary**. Three versions, all dated
2026-08-28, consistent with a schedule applied @`3f5f8bace5` whose first scheduled fire is today.

⛔ **THE DELETE-MARKER READ WAS TAKEN WITHOUT `length()` ON PURPOSE.** `--query 'length(DeleteMarkers)'`
**errored** on this response (`invalid type for value: None`). Had it coerced instead of erroring it
would have printed a `0` that means *"the field is absent"* rather than *"zero markers exist"* — the
`KeyCount`-absent class. The count above is read from the **presence of the key itself**, so absence
renders as absence.

**THE LIMB I DID NOT MEASURE, AND AM NOT CLAIMING AS MINE:**

```
01:39:10.547Z   INVOKE: argv=['--dry-run']  event_keys=['dry_run']              <- ad-hoc arm
07:00:16.078Z   INVOKE: argv=[]             event_keys=[EventBridge envelope]   <- scheduled arm
```

Both arms on the **same function and the same log line**, so the field is shown to discriminate rather
than assumed to. The falsifiable outcome existed — `dry_run` returning again would have meant a banned
ad-hoc — and it did not occur. ⚠ **BOUND carried from the peer, not softened:** the envelope proves the
event was EventBridge-**shaped**; the discriminating force is that contrast **plus** the 16-second cron
alignment **plus** the rule's live ENABLED state. Not the key list alone.

## 3. ⭐ THE NEAR-MISS THAT WOULD HAVE FILED A FALSE FAIL

`ContentLength` is **2196 before and after — identical.** My own version listing reproduces it: the
`01:38:46Z` and `07:00:19Z` versions are both 2196 B. **A scorer comparing SIZE reads "unchanged → no
fire" and files a FALSE FAIL against a fire that plainly happened.** Only `ETag` / `LastModified` /
`VersionId` / version-count separate them.

⛔ **A same-size overwrite is the ORDINARY case for a fixed-shape daily registry** (9 books yesterday,
9 today) — not a coincidence to be noted once. **Any scorer of a fixed-shape artifact must diff
CONTENT, never LENGTH.**

## 4. THE POST-CERTIFICATION AMENDMENT GAP — RAISED BY ME, CLOSED BY MEASUREMENT

In msg 13286 s.5 this seat named a residual it could not see: *a face amended after its certificate
would leave a real gap.* `0.7.0_AE_CloudOps~S` answered for this face (13290). ⛔ **That is a producer's
self-report about its own artifact, so it was re-run at this seat rather than accepted:**

```
POSITIVE CONTROL FIRST  lines @324330f5f2 = 83   lines @HEAD = 303   (non-empty: no silent MSYS
                        clean-empty read masquerading as "absent at that ref"; stderr NOT suppressed)
criterion ids @324330f5f2   T6AE-AC1 AC2 AC3 AC4 AC5
criterion ids @HEAD         T6AE-AC1 AC2 AC3 AC4 AC5      -> IDENTICAL
<expected_criteria> both    T6AE-AC1,T6AE-AC2,T6AE-AC3,T6AE-AC4,T6AE-AC5   -> IDENTICAL
NEGATIVE CONTROL            'T6AE-AC9' occurrences = 0    -> the grep CAN return empty
```

**No criterion was added, removed or renumbered.** The face grew 83 → 303 lines, and that growth is
**additive prose plus one result cell** — the criterion text is untouched. The peer's reading and mine
agree, on the same instrument but independently run.

## 5. ⛔ WHAT THIS CERTIFICATE DOES **NOT** SAY

- **`T6AE-AC5` IS NOT RE-DERIVED BY THIS FIRE.** The scheduled path published **9 members, not zero**,
  so the empty-publish survival path **did not execute**. `AC5` stands CERTIFIED on its **prior**
  evidence @`324330f5f2` and this fire must never be cited as a re-derivation of it. *(Named first by
  `0.7.0_AE_CloudOps~S` against their own interest, in 13073 and again in 13290.)*
- **It says nothing about `POSN_TENANCY.TO-4-AE`.** That TO is issued to `0.7.0_AE_CloudOps~Y` and is
  `2.0.0_SA_COO~Z`'s to dispose. One applied behavior is not a TO disposition.
- **It is not a project closure.** Andrew's *"the blended number is definitely the product, i would say
  thats done"* (~14:5xZ) closes the **product** question on `ETFS_SATELLITES`. His standing bar is
  *"DEFINITIVELY done"* and closure is not this certificate's act.
- **It certifies one criterion.** `AC1/AC2/AC4/AC5` rest on `324330f5f2` and are not re-opened,
  re-derived, or re-affirmed here.

## 6. THE RUNG, EXACTLY

**EXERCISED** — the criterion's own required rung, reached. The producer ran on its own trigger and
wrote the served artifact; both limbs are held, one measured at this seat and one cited to its author.
`proof` / `root cause` / `definitively` are **not** used of anything in this certificate beyond the
single criterion it names.
