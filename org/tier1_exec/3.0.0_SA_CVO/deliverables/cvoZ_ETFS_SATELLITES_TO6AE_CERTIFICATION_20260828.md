# CERTIFICATION — `ETFS_SATELLITES.TO-6-AE` (the satellites registry producer schedule)

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T01:4xZ
**Executor:** `0.7.0_AE_CloudOps~S` · **Issuer:** `2.0.0_SA_COO~Z`
**Instance (certified object):** report msg 11644; commits `3f5f8bace5` (TF) + `27baa31426` (ledger close),
both measured ON ORIGIN by the executor with a positive control on the is-ancestor instrument.

---

## VERDICT: **AC1 / AC2 / AC4 / AC5 CERTIFIED.** `AC3` correctly **WITHHELD, NOT FAILED.**

---

## 1. ⭐ WHAT I RE-DERIVED, AND THE GAP IT CLOSED

Rule 22 forbids confirming via the first seat's method. `0.7.0_AE_CloudOps~S` censused **both scheduler
planes** for AC2 — `list-rules` 139/1 page, `list-schedules` 18/1 page, positive controls on both, and
the Rules denominator moving **138 → 139** across the apply as a control on the apply's own scope. That
is careful work and I did not re-run any of it.

⛔ **BUT AN ENUMERATION PROVES THE RULE EXISTS; IT DOES NOT PROVE THE RULE IS WIRED. A rule with no
target fires nothing, and it would census identically.** That gap is invisible from the plane they
measured, so I measured the next rung down:

```
INSTRUMENT 1  events list-targets-by-rule cot-satellites-registry-producer-daily
              -> CotSatellitesRegistryProducerDaily
                 arn:aws:lambda:us-east-1:313476888478:function:cot-satellites-registry-producer
              EXACTLY ONE TARGET, and it is the producer.
NEGATIVE CONTROL  the same call on ZZZ-no-such-rule-9999
              -> ResourceNotFoundException. THE INSTRUMENT CAN SAY NO.
INSTRUMENT 2  lambda get-policy cot-satellites-registry-producer
              -> Sid EventBridgeCotSatellitesRegistryProducerDaily, Effect Allow,
                 Principal events.amazonaws.com, Action lambda:InvokeFunction,
                 Condition ArnLike AWS:SourceArn = .../rule/cot-satellites-registry-producer-daily
```

**THE CHAIN IS COMPLETE ACROSS THREE RUNGS AND TWO AUTHORS:** the rule exists (their census) → the rule
targets the function (mine) → the function permits **that exact rule ARN** (mine). The resource policy
is `ArnLike`-conditioned on this one rule, not a wildcard service grant, so the permission is as narrow
as the trigger.

**AC2 CERTIFIED — and on strictly more than was claimed.**

## 2. AC1 / AC4 / AC5

- **AC1 (DESIRED)** — CERTIFIED. `satellites-registry-producer.tf:236-241` @`3f5f8bace5`, a real
  `schedule_expression` rather than an event pattern. The distinction matters: an event pattern with no
  emitter is the silent-never-fires shape.
- **AC4** — CERTIFIED. An independent daily wall-clock schedule chained off nothing. This is the
  CLAUDE.md §5 rule ("success-of-upstream as the only trigger is a defect") satisfied *by construction*
  rather than by assertion, which is the strongest form available.
- **AC5** — CERTIFIED. No branch on member count, no delete in the scheduled path, and the
  PUBLISH-EMPTY-NEVER-DELETE contract holds in the **deployed bytes**: a missing upstream partition
  fails LOUD rather than publishing a manufactured empty.

## 3. AC3 — WITHHELD IS CORRECT, AND I AM RECORDING WHY IT IS NOT A GAP IN THIS CERTIFICATION

AC3 is EXERCISED-class and needs a fire on the schedule's own trigger at 07:00Z. The executor declined
to write a `FAIL` row for a criterion that has not yet had the opportunity to fire. **That is the
posture I ratified this session and it is the third seat now holding an artifact rather than writing a
false failure** (with `0.4.0_DS_ClientPlatform~Q` and `0.4.0_DS_ClientPlatform~L`). Measured basis:
**18 `FAIL` rows across 1,258 acceptance rows estate-wide, at least one already a self-declared false
failure, and nothing downstream distinguishes them** (cert @`b884d661c8`).

⭐ **TWO THINGS THE EXECUTOR DID HERE THAT I AM CERTIFYING AS METHOD, NOT JUST RESULT:**
1. **The perishable baseline was captured as a durable artifact rather than left to be re-derived.**
   `get-bucket-versioning` reads Enabled, but `get-bucket-lifecycle-configuration` carries
   `expire-noncurrent-versions-14d` over `Prefix: ""` — so the QA version **dies 14 days after the
   scheduled fire supersedes it**. Durability's second half lives in a different API call, and the
   discriminator was banked before it could expire.
2. **The TO's named discriminator does not exist, and they said so instead of substituting silently.**
   The QA artifact carries **no `provenance` field** (measured: top-level keys are `schema_version,
   as_of, source, claim, books`). AC3 therefore rests on the VersionId/LastModified delta plus the
   invocation record — **and that is the stronger instrument**, because a provenance field is written
   by the system under test while version history and the EventBridge record are produced by different
   systems.

## 4. ⛔ FINDING F1 (OBSERVATION / INERT) — CARRIED TO THE CHANNEL AS `ETFS_POSITIONING-Z-S12`

Surfaced by the executor against their own design, which is why it is worth certifying as a finding
rather than filing as a complaint.

**S3 returns `403 AccessDenied` rather than `404 NoSuchKey` for a missing object when the caller holds
no `s3:ListBucket` — it will not confirm non-existence to a principal that cannot list.** Therefore, at
this producer's error surface:

> **"UPSTREAM IS LATE" AND "MY READ GRANT IS BROKEN" ARE BYTE-IDENTICAL.**

**Today it is the benign one, and that was established rather than assumed:**
`simulate-principal-policy` returns **allowed** on both read prefixes and the exact write key, with
**three negative controls returning implicitDeny**, each issued as a separate invocation with one
`--resource-arns` per call — so the multi-ARN false-deny mode could not silently disarm the controls.

⭐ **THE REASON THIS IS A FINDING AND NOT A CURIOSITY: IT IS THE SAME SHAPE AS THE HAZARD `TO-5-DS` AC3
RECORDS FOR THE SERVING LAYER — an absent artifact and a forbidden read collapsing into one status —
WHICH IS WHY THE EDGE SYNTHESIS WAS REMOVED @`24a8435642`. It has reappeared one layer up, on the
producer's READ side.** This is Rule 28's substrate question 7 (*is the failure mode distinguishable
from a genuine negative?*) answered NO on a second surface.

⚠ **AND THE SCOPE NOTE IS THE EXECUTOR'S AND IT IS RIGHT:** the remedy — a prefix-conditioned
`s3:ListBucket` on the two rebalancer prefixes — **does NOT implement option (C)**. (C) was a
newest-partition RESOLUTION strategy; this only changes which error code a failure carries. **Rejecting
(C) does not entail rejecting this**, and the ratified sentence must not be read as though it did.
NOT FIXED UNILATERALLY, correctly: the absence was explicitly ratified by `2.0.0_SA_COO~Z` and nothing
is blocked, because the grant is measured correct.

## 5. ONE LEDGER CORRECTION I AM RECORDING BECAUSE IT IS A ROLLBACK HAZARD

The executor's resource table lists **eight** resources; the apply created **nine** —
`module.cot_satellites_registry_producer` expands to the function **and** its log group, which the
module row hides. **A rollback driven off the table rather than off the apply count would orphan the log
group.** Self-caught, and the kind of small discrepancy that only bites during an incident.

## 6. WHAT THIS CERTIFICATION DOES NOT DO

- Does **NOT** discharge AC3, and no apply or census can — only the 07:00Z fire can.
- Does **NOT** touch `POSN_TENANCY.TO-4-AE`'s hold or the ETFS_SATELLITES PROD promote.
- Does **NOT** bear on the `etfs-positioning` producer apply (`0.7.0_AE_CloudOps~I`'s, a different
  project and a different schedule).
- Does **NOT** close D4. Its bar is Andrew's smoke test.
- ⛔ Does **NOT** mean the satellites view works: `ETFS_POSITIONING-Z-S11` records that **no fetch path
  exists**, so a correctly scheduled producer still does not reach the page.

---

— `3.0.0_SA_CVO~Z`
