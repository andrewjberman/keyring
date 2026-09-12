# ANDREW-DIRECT 2026-09-12 ~01:5xZ -- all nine noncurrent versions approved (IRPT_BCKEND W4-S20 / S41)

**Received at:** the 1.0.0_SA_CTO terminal, in-session, 2026-09-12 ~01:5xZ.
**Recorded by:** 1.0.0_SA_CTO. **Broadcast:** same turn, per `org/XXX.md`.
**Class:** authorization for an **UNRECOVERABLE** act.

## VERBATIM AND ENTIRE

> "Approved all 9"

## WHAT HE WAS ANSWERING -- the corrected card, so "all 9" has exactly one referent

The re-ask of 01:5xZ, after his ~01:2xZ approval was found to rest on a falsified count:

> **"The four synthetic export PDFs hold NINE noncurrent versions, not four. (a) delete all nine
> (b) delete only the four named (c) leave them"** -- REC (a) all nine.

So: **(a). The NINE noncurrent versions of the FOUR synthetic-export PDF keys.** The number nine is
not a target to be reached by other means; it is the measured population of one specific set.

## THE AUTHORIZED SET, ENUMERATED BY SUBTRACTION FROM A PRINTED DENOMINATOR

⛔ **Written this way deliberately.** The first authorization failed because it was a FORWARD LIST of
four remembered VersionIds. Rule 24: write the enumeration as *the printed denominator MINUS what is
excluded*, never as a forward list of what you thought of.

**DENOMINATOR** -- `aws s3api list-object-versions --bucket opal-data-ycharts --prefix
firms/49financial/generations/GENIBS14SYN/attempts/1/exports/`, re-measured at `1.0.0_SA_CTO` 01:44Z,
rc=0, 8808 bytes, `IsTruncated: None` (the page IS the population):
**10 versions, 5 delete markers, 5 distinct keys.**

| | |
|---|---|
| **10** | all versions under the prefix |
| **-1** | `probe/probe.txt` (1 version, 5 B) -- **NOT an export PDF, named nowhere in the row, EXCLUDED** |
| **= 9** | **THE AUTHORIZED SET**: every noncurrent version of the four `report.pdf` keys |

Which is `r1/report.pdf` **3**, `v0-11-overview/report.pdf` **2**, `v0-11-comparison/report.pdf` **2**,
`v0-11-multicomp/report.pdf` **2**. Every version of those four keys is noncurrent -- each key's
current state is a delete marker from the earlier act.

## ⛔ NOT AUTHORIZED, named because an unrecoverable act invites exactly this drift

- `probe/probe.txt` -- any version of it, and its delete marker. **Reported, left alone.**
- Any other object, prefix or key in `opal-data-ycharts`.
- The five **delete markers** themselves. Removing a delete marker RESTORES a current object; that is
  the opposite of the intent and is not covered by "delete the versions".
- Any bucket-level change: versioning state, lifecycle rule, policy, or replication.
- Any "while we are here" cleanup of any kind.

## ⚠ THE COUNT IS PERISHABLE AND HAS ALREADY MOVED ONCE

Nine is the count at 01:44Z. It was four at the time of the row, because `IB-rt-8` re-ran the render
and each key accumulated versions. **`2.0.0_SA_COO~B` re-reads the prefix IMMEDIATELY BEFORE acting.**
If the live denominator is not 10/5/5 with nine noncurrent PDF versions, that is a NEW population and
the act STOPS AGAIN -- the authorization is over a measured set, not over a number to be matched.

## EVIDENCE SHAPE REQUIRED (unchanged from 96041, widened to nine)

The nine VersionIds read BEFORE; the deletes; then a **by-VersionId** read returning `NoSuchVersion`
on **9 of 9**, with a **POSITIVE CONTROL** on an object that must still resolve. ⛔ A 404 on the
ordinary key proves nothing here -- that was already true before the act, which is the entire reason
this call existed.

## WHAT THIS CLOSES

Channel row `IRPT_BCKEND-S41` (BLOCKING, ARMED, disarm_owner `1.0.0_SA_CTO`) is **DISARMED** by this
ruling: its disarm text required carrying the corrected count back to Andrew and reporting his answer
on the corrected number. Done. The hazard it names -- acting on a count wrong by five -- cannot occur,
because the authorization is now over the measured nine.

After the act lands and the 9-of-9 read returns, **"the four synthetic export PDFs are gone" is
sayable without a qualifier.** Until then the qualifier stands.

## SCOPE -- NOT WIDENED

He answered one card. Untouched: the portal freeze; the `CLOUD -> SITEZ` merge leg; `0.0.0_AB_MSTR`'s
separate `/kill storage` 3.4 GB recursive delete, which is its own lane's call and still owed his own
word.
