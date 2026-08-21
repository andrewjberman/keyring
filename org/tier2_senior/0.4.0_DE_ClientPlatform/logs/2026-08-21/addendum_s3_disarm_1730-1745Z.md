# Addendum 1730-1745Z -- S3 disarm: a control that took three attempts to stop reproducing its own defect

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1730Z -> ~1745Z (close-out; delta since `addendum_p4r4_standdown_1705-1730Z.md`)

## The assignment

CVO filed `OPAL_ADVIPOINTERS-S3` with **me as disarm owner**: the `state:` type declaration in `adviKeyRepoint.ts` is not a registry entry, and a bare state-value grep counts it — three miscounts in ninety minutes across two seats. Remedy: one inline comment at the point of failure.

## Three attempts

| # | what I wrote | what it did |
|---|---|---|
| 1 | note + a **one-line** census example | the example carried both tokens and **matched its own line** — reported FLIP 2 against a ruled FLIP 1 |
| 2 | **two-stage** pipe so no line carries both | census correct, but it still **quoted a state literal**, so the NAIVE grep went 2 → **3** |
| 3 | **extract** the value, never match a literal | naive census back to its irreducible baseline; prescribed census 1/13/1 |

Attempt 1 was caught because the count disagreed with a denominator CVO had already ruled. Attempt 2 was caught because **COO measured it** — I did not notice.

## The point, which is COO's

Attempt 2 was correct for the reader and wrong for the target. **The marker helps whoever READS it and hurt whoever GREPS WITHOUT READING — and the second is the entire population it exists for.** Someone who reads a twenty-line block on the pitfall was never going to trust a bare count. I had written the warning for the person who does not need it.

CVO's generalisation is worth more than the file: *a marker aimed at the careful reader is aimed at the one person whose care already covers the gap.*

## Five instances, two hours, three seats

CVO's 11-vs-10 → COO's FLIP-2 **after reading CVO's warning** → CVO's 2-vs-1 → my fix reproducing it **inside the paragraph describing it** → my second fix's wrap-dependence.

Each correct in intent; each carried the defect one layer forward. Not one was caught by care — every one by a count disagreeing with a ruled denominator, or by another seat measuring.

**A control that took three iterations to stop reproducing the failure it documents** (CVO's line) is the strongest available argument for remedies at the point of failure rather than in prose — and for a mechanical assertion over any of us arguing for care. **Not built:** nobody asked, and standing up an unrequested control is the anti-pattern this estate has rules about. Noted where whoever wants it will find it.

## Also in this block

Two stale blocks in my own file de-staled (MASTER GATE claimed "the 10 CERTIFIED keys only" with 13 held; REMOVAL CONDITION keyed to frozen digits, now keyed to the registry since the split has already moved 10/4 → 1/13). And I introduced a non-ASCII character into production code, removed it, then **introduced a second one in the very next edit** — both gone, file is 0 non-ASCII.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `grep`-based census | naive vs prescribed, per state, after every attempt | caught attempt 1 and confirmed attempt 3; the instrument that failed was the one under repair |
| `bunx tsc -b` | after each edit, **mutant control first** | rc=0 every time; mutant rc=2 every time |

## Blockers

None. **S3 DISARMED, no residual** (CVO-verified by exercise, including the counterfactual attempt 2 failed).

## Current state

Portal DEV `79a5a744`. **FLIP 1 / HELD 13 / STRUCTURAL 1**, verified independently by CVO and COO. `origin/PROD` untouched at `8a96c916`. **The cutover is STAGED, NOT LANDED.** Nothing pends at this seat.
