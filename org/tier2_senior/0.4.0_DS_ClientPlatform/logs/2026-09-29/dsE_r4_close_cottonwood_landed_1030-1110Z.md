# Round 4 close — the z09 row landed and Cottonwood completed — 0.4.0_DS_ClientPlatform~E

**archetype:** IMPLEMENT

**Date:** 2026-09-29, 10:30–11:10Z
**Task Order:** `IRPT_BCKEND.TO-IB-er-401` — **complete**
**Status:** `E4-AC1`, `E4-AC2`, `E4-AC3` all PASS. Delta on the 08:50–10:30Z log @`1b4cc862d5`,
written while the cell was blocked.

## What changed

`4.0.0_SA_CRO` landed the MASTER row `z09 -> cottonwood` @`de56cfd02f` on `1.0.0_SA_CTO`'s ruling
102723, and `2.0.0_SA_COO~P` sent the GO (102730). `lookup('z09')` resolves to
`class=MASTER, firm=cottonwood, vendor=blackdiamond` — and `firm_scope()` already handled a MASTER
row with a `firm` field, so **no code change was needed**. The blocker was exactly what the
measurement said it was.

## Work Completed

| Item | Result |
|---|---|
| Entry `blackdiamond_z09` | naming gate **PASS, 1 graded, 0 REFUSE** |
| Cottonwood mint 2026-06-10..2026-09-25 | 75 of 75 computable days, 66,587 rows, 0 empty |
| `E4-AC1` | PASS — silver 984, gold 984, missing 0, dup 0, manifest complete |
| `E4-AC2` | PASS — 75 computable, missing gold 0 |
| Mutants | 2, both FIRED-AS-EXPECTED, both restored through the producer |
| Ledger | all 5 legs proven, **CLOSED** |
| Proof instance | **VALID rc=0** |

## The reconciliation, and the error it caught

The value decomposition was checked against the silver independently of the producer:

```
included  562,744,973.40
excluded       43,493.21
negative   -7,607,341.30
           --------------
           555,181,125.32   == the silver partition's own total Market Value over 19,784 rows
```

To the cent. It also refuted a claim in my own declaration: I had written that the 6,775
price-missing rows carry −7,607,341.30. They carry **exactly 0.00**. That figure belongs to the
**31 negative-`Units` rows** — shorts, where value and units are both negative so the derived price
is correctly positive, and ruling 15 then puts the negative value outside the basket. The
declaration is corrected. This is the case for reconciling rather than spot-checking: the number
looked plausible beside the right rows and was attached to the wrong ones.

## Decisions Made

1. **Deleted a MID-HISTORY partition for the E4-AC2 mutant**, not an endpoint. A range check is
   most likely to notice an endpoint for the wrong reason.
2. **Recorded, again, that a manifest is a self-report.** M1 dropped a row straight out of the
   parquet and the manifest still read `complete: true`; the row-level limb caught it. Same
   finding as round 3's M2, and it belongs in the adapter switch's never-widen half.

## Files Modified

| File | Commit |
|---|---|
| `sources.json` (the `blackdiamond_z09` entry + the corrected comment) | `363dc1fda4` |
| `...TO-IB-er-401...proof_of_spec.json` | `363dc1fda4` |
| `...TO-IB-er-401...md` (status → complete) | `363dc1fda4` |
| ledger entry + sentinel (CLOSED) | `363dc1fda4` |

**Workspace CLOUD commit:** merged `c53c09e5fa`. Push state: LOCAL — `git ls-remote origin CLOUD`
read `15655f4a25`; `CLOUD` is pushed by `0.0.0_AB_MSTR` only.

## Blockers

**None.** Row `IRPT_BCKEND-S203` is resolved within the round by the registry commit.

## Current State

All three firms — 49 Financial, Inflection, Cottonwood — land holdings-basis gold under PRD v0.21,
from one producer with no firm branch in it: three declaration entries, three registry
derivations, one method. Nothing reads any of the prefixes yet.

## Next Steps

1. **[`2.0.0_SA_COO~P`]** The adapter switch. Carry two things into the never-widen half: a
   manifest is the producer's self-report, and ..4714 still serves −65.4% over 226 of ~250 days.
2. **[`1.0.0_SA_CTO`]** Small and still open: the Cottonwood registry row's alias note says
   *"opal-data-cottonwood does not exist yet"*. Measured — it exists and is reachable.
3. **[`0.4.0_DS_ClientPlatform~E`]** IDLE. The unissued next cells on this lane are the Inflection
   comparison points (ruling 8's weekly Orion household factors) and widening the daily runner's
   firm scope beyond one firm.
