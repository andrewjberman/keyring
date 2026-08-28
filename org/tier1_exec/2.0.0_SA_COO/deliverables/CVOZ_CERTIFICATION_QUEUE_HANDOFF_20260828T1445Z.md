# `3.0.0_SA_CVO~Z` CERTIFICATION QUEUE — HAND-OFF LIST, NOT THE REGISTER

**Cut by `2.0.0_SA_COO~Z` (issuer of most of these) 2026-08-28 ~14:4xZ, on Andrew's reopening of the
CVO seat: *"bring CVO~Z on"*. Spawn is `0.0.0_AB_MSTR~Z`'s act.**

> ## ⛔ READ THIS LIST. DO NOT READ `to-check` AND STOP.
> **The register shows 9. The true queue is 12.** Three items are structurally INVISIBLE to the
> register and a fresh certifier working from `to-check` alone will believe it is done at 9.

## THE QUEUE — 12 items

**VISIBLE on the register (`token[0]` = `queued` → PENDING) — 9**
```
D1_CATVIEWS.TO-I1-DS.path-to-live-channel-enumeration
ETFS_INGEST.TO-6.gics-industry-group-per-security-field
ETFS_INGEST.TO-8.publisher-carries-the-industry-group-key
ETFS_POSITIONING.TO-1.etf-positioning-producer-and-subassetclass-vocabulary
ETFS_POSITIONING.TO-2.etf-serving-route-artifact-contract-and-iam
ETFS_POSITIONING.TO-3.positioning-models-etfs-flip-and-five-hardcoded-sites
ETFS_POSITIONING.TO-5.etf-producer-lambda-and-schedule
ETFS_POSITIONING.TO-7.per-fund-as-of-all-four-etfs-every-day
ETFS_POSITIONING.TO-11-DE.int-default-for-first-visit
```
**INVISIBLE to the register (`token[0]` = `complete` → drops OFF the board) — 3**
```
ETFS_SATELLITES.TO-6-AE.registry-producer-schedule
ETFS_SATELLITES.TO-8-DE.consumer-seam-fetch-the-registry
ETFS_SATELLITES.TO-9-DE.internal-viewer-firm-selection
```

## ⛔ WHY THE THREE ARE INVISIBLE — AND THE AUTHORS ARE NOT WRONG
`to-check._classify_status()` reads **`token[0]` only**. `complete` maps to COMPLETE and the row leaves
the board. **`complete` is TRUE of the EXECUTION and FALSE of the LIFECYCLE**, and the field offers only
one axis — so each author reported accurately on the only axis available.
**Root (`1.0.0_SA_CTO~Z`): Rule 24 (ii) SAME GRAIN.** Certification state is a **PER-CRITERION VECTOR**
(`TO-6-AE` is simultaneously *certified* on AC1/2/4/5 and *pending* on AC3); the board reads a **PER-TO
SCALAR**. ⛔ **Minting `partially-certified` does not fix it — that summarises a vector into another
scalar.** No vocabulary was minted tonight, deliberately.
⚠ **DIRECTION MATTERS:** this defect makes the register **over-OPTIMISTIC**, and an over-optimistic
register **cannot announce itself** — a row that leaves the board is indistinguishable from one that is
done.

## ⚠ THIS COUNT IS A FLOOR, NOT A CEILING
The probe matches **three known wordings** (`queued -- for …CVO`, `Awaiting …CVO`,
`CERTIFICATION PENDING at …CVO`). **A fourth phrasing would be invisible to it too** — the same
enumeration weakness, one level up. ⛔ **Do not treat 12 as certified-complete coverage of the queue.**
**Corroborate against the lanes, not against this list alone.**

## ⚠ CORRECTION TO THE NUMBER IN CIRCULATION
`1.0.0_SA_CTO~Z` (13220) told `0.0.0_AB_MSTR~Z` **ten**. That was correct **when measured** — it
predates this seat disposing `ETFS_INGEST` TO-6/TO-8 to `queued` after the 13:00Z fire. **The live count
is 12.** Neither number was wrong at its own vintage; **this one carries its measurement time.**

## WHAT EACH ITEM'S FACE ALREADY CARRIES
Every face states its own evidence and its own bounds. ⛔ **Two specifically constrain a certificate:**
- **`ETFS_INGEST` TO-6 / TO-8** — all three rungs PASS on the 13:00Z scheduled fire; the falsifiable
  prediction held (`ABSENT_FROM_SOURCE` = 1 = ABT; `NOT_APPLICABLE_NON_EQUITY` = 8 = the run's own FI
  count). ⚠ **This seat measured the EXERCISE only.** `TO6-AC1/AC2/AC4/AC5` are SOURCE/DATA-class,
  discharged by a lane that has since died. **No "6 of 6" is claimed and a certificate must not assert
  one.**
- **`ETFS_SATELLITES.TO-6-AE`** — its face states `CERTIFICATION PENDING at 3.0.0_SA_CVO~Z` for **AC3
  only**; AC1/AC2/AC4/AC5 are already **CERTIFIED @`324330f5f2`**. **A certificate must read
  criterion-wise, never a bare 5/5.**

## NOT IN THIS QUEUE
`D1_CATVIEWS.TO-P1-AE` — `TP1AE-AC1` discharged 13:52Z (category-views SERVED, 4 firms, 13:50:50Z,
provenance `written_by` stated) and its deploy ledger is **CLOSED, 5 legs proven**. **AC2–AC6 are
separate and unclaimed.** Not queued for certification by this seat.
