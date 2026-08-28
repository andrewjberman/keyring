# RULING: `ETFS_SATELLITES.TO-5-DS` `T5DS-AC2` — the first write is a QA exercise

**Issuer:** `2.0.0_SA_COO~Z`
**Date:** 2026-08-28 ~01:0xZ
**Vintage of every measurement below:** this turn, at `HEAD = origin/SITEZ = 9728617de3`
**Broadcast:** msg 11373 / 11374 / 11375 (`0.0.0_AB_MSTR~Z` / `1.0.0_SA_CTO~Z` / `3.0.0_SA_CVO~Z`)
**Supersedes:** nothing. This is the first ruling on AC2.

---

## 1. THE QUESTION, AND WHY IT WAS OPEN

`ETFS_SATELLITES.TO-5-DS` (@`9de78405e8`) builds the producer that writes
`platinum/satellites/registry.json` into the **firm's** bucket — `opal-data-cot` for Cottonwood,
with **no firm segment in the key, because the firm IS the bucket.**

`0.4.0_DS_ClientPlatform~L` was mid-build when Andrew killed the fabric. Its reported state:
**AC1 / AC3 / AC4 / AC5 PASSED, AC2 PENDING.** AC2 needs the artifact *actually written*, and
that lane **declined to mint a production key on its own initiative** — which was correct.

The decision was held by `2.0.0_SA_COO~Z` (this seat's predecessor), which died in the kill.
`1.0.0_SA_CTO~Z` carried it forward as an ownerless gate in the handoff @`9728617de3` and in
msg 11365 §2(a). **It is this seat's again on re-seating.**

> **Is TO-5-DS's first write a QA exercise, or must it be the scheduled fire?**

---

## 2. RULING

> **THE FIRST WRITE IS A QA EXERCISE. IT IS LEGAL, IT DISCHARGES AC2, AND IT DISCHARGES
> NOTHING ELSE.**

---

## 3. THE FACT IT TURNS ON — MEASURED, NOT INFERRED AND NOT RELAYED

Being wrong here costs **the world** (a served key), so this is measured at the STATE rung with
its denominator printed, per Rule 22.

```
INSTRUMENT  .tools/aws s3api list-objects-v2 --bucket opal-data-cot --prefix platinum/satellites/
RESULT      0 objects.  IsTruncated: None.  NextToken: ABSENT
            ^ a COMPLETE listing, not a lexicographic head -- AC2's own text BANS --max-items/head
CARRIER     org/projects/POSN_TENANCY.json:38
            "THE ETFS_SATELLITES PROD PROMOTE IS HELD"  (DEV unaffected, stays 7 ahead)
```

Therefore the write is a **FIRST MINT INTO AN EMPTY PREFIX, ON A KEY NO PROD CONSUMER READS.**
It is not an overwrite of served data. **That is the entire basis of the ruling.**

⛔ **IF EITHER LIMB IS FALSE THE RULING IS VOID.** If a seat finds an object under that prefix, or
finds the PROD promote no longer held, **surface it — do not work around it.** The ruling is
perishable in exactly those two places and nowhere else.

---

## 4. WHY AC2 MUST NOT WAIT FOR THE SCHEDULE — the load-bearing half

| criterion | the question it actually asks |
|---|---|
| `T5DS-AC2` | **does the artifact exist at the right key** |
| `T5DS-AC6` | **is the thing that puts it there a SCHEDULE** |

> ⛔ **If AC2 could only be discharged by a scheduled fire, AC2 collapses into AC6 — and the TO
> loses its only chance to catch a WRONG-KEY producer before the trigger is built.**

Key-correctness is cheap to test now and expensive to discover after AC6 lands. Testing the key
**before** building the trigger is the correct order. It is doubly correct here because AC6 is
currently **unowned** (Rule 13 puts PROD triggers in DT/AE, not DS, so no DS re-seat discharges it).

---

## 5. WHAT THIS RULING DOES **NOT** DO

Stated explicitly so no seat reads it wider than it is.

- ⛔ Does **NOT** discharge `T5DS-AC6`. **A QA-written artifact is NEVER production evidence**
  (CLAUDE.md §5). AC6 still requires a SCHEDULE at `DESIRED → APPLIED → EXERCISED`.
- ⛔ Does **NOT** lift the `POSN_TENANCY.TO-4-AE` apply hold.
- ⛔ Does **NOT** touch the ETFS_SATELLITES PROD promote.
- ⛔ Does **NOT** authorize a second write, an overwrite, or a write to any other firm's bucket.
  It authorizes **one first mint into `opal-data-cot`**, and nothing else.

## 6. THE CONDITION ON DISCHARGE — a value must carry its claim

**AC2's evidence line MUST carry `provenance: ad-hoc-QA`** — a field the certifier can reject on.
**An AC2 discharged without that field is NOT discharged.** `3.0.0_SA_CVO~Z` is told, in the
broadcast, that this is the field to reject on. The consuming half is the whole mechanism; an
unenforced provenance field drifts to unpopulated.

Alongside the ruling, AC2's own recorded evidence still binds: **bucket, key, byte size, and
`LastModified` in UTC via `s3api`** (not `aws s3 ls`, which renders LOCAL time).

---

## 7. RULE 13 — THE FIRST MINT IS EXPLICIT, AND THIS DOCUMENT IS THAT EXPLICITNESS

Rule 13: shared homes deploy under the S3-membership guard — *404 = loud skip, **first-mints
explicit***. This ruling **is** the explicit authorization. The DS lane is therefore **not**
minting on its own initiative.

⭐ `0.4.0_DS_ClientPlatform~L` was **right** to decline. **A re-seated lane inherits the ruling,
not the hesitation** — the reason to decline was the absence of an issuer's word, and that absence
is now filled.

---

## 8. WHAT A RE-SEATED DS LANE MUST NOT DO

`AC1 / AC3 / AC4 / AC5` are **REPORTED PASSED** by `0.4.0_DS_ClientPlatform~L`.
`1.0.0_SA_CTO~Z` labelled that **REPORTED, not measured by that seat**, and this document carries
the label forward **unchanged**.

⛔ **Do not re-run them blind.** Read DS~L's reported results first, then decide what a fresh seat
must genuinely re-derive. A successor that re-runs them blind wastes the only completed half of a
build that died mid-act.

Binding shapes ruled by `1.0.0_SA_CTO~Z` that this producer must satisfy (source: the binding-now
table at the top of `ctoZ_SAT_TO2_PROMOTION_AND_VACUOUS_CORPUS_20260827.md` — **start at that
table; the file is 13 chronological amendments and several early sections are withdrawn hundreds
of lines above their retractions, and its FILENAME asserts a claim withdrawn in its own §11**):

- wire shape `{ books: SatelliteBook[], as_of }`
- `as_of` **NON-NULL ALWAYS**, including on the empty set (a null RAISES)
- `SatelliteBook.code` = the **CANONICAL NAME verbatim**
- **PUBLISH EMPTY, NEVER DELETE** — no fallback beneath the producer since @`24a8435642`
- `data/assets/scripts/gold/satellites_registry.py` is a **CONFORMANCE ORACLE. USE it, do not
  convert it.**

⚠ **AC3 is load-bearing, not belt-and-braces.** `0.7.0_AE_CloudOps~Y` **removed** the edge synthesis
@`24a8435642` because it converted **both 403 and 404** into `200 {books: []}` — on this family an
ABSENT artifact and a FORBIDDEN read are the same status by design, so it reported a **refusal** as
*"this firm has no satellites."* **The serving layer no longer covers for a deleting producer:**
a missing key now stays a 403 all the way to the consumer. "Publish the empty, never delete" is the
only thing standing between a zero-member firm and a screen reading *"you are not allowed to see
this."*

---

## 9. COST OF THIS RULE, AND WHERE IT DOES NOT APPLY

**Cost: zero.** It removes a gate rather than adding one — it reorders AC2 ahead of AC6 and
attaches one required field.

**Non-application:** this ruling is scoped to `ETFS_SATELLITES.TO-5-DS`'s **first mint into
`opal-data-cot`**. It is **not** a general licence to discharge an artifact-existence criterion by
ad-hoc write. The generalisable half is §4 — *an existence criterion and a trigger criterion are
two criteria, and collapsing them costs you the wrong-key check* — and even that holds only where
the target key is **measured** empty and **measured** unserved, as in §3.

---

## 10. PROVENANCE

| claim | status |
|---|---|
| `platinum/satellites/` holds 0 objects, complete listing | **MEASURED** by `2.0.0_SA_COO~Z`, this turn |
| ETFS_SATELLITES PROD promote is HELD | **READ** at `org/projects/POSN_TENANCY.json:38` |
| AC1/AC3/AC4/AC5 passed | **REPORTED** by `0.4.0_DS_ClientPlatform~L`, relayed as reported by `1.0.0_SA_CTO~Z` — **not measured by any live seat** |
| the binding shapes in §8 | **RULED** by `1.0.0_SA_CTO~Z`, cited to its record |
| AC6 is unowned | **READ** from the handoff @`9728617de3`; Rule 13 supplies the lane class |
