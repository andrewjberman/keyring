# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-10-01 00Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 00:19Z | L8 | 26 | ab-4 leg d at 17/19; the 23Z log committed |
| 00:2xZ | L8 | 26 | ab-4 leg d: 19/19 written, 0 errors; S3 structure one new each, as below |
| 00:33Z | L8 | 26 | session log `dc97dc2259` (rounds 19-26) |
| 00:4xZ | L8 | 26 | leg d `inputs_equal_now` 19/19; BP's dossier names `BP-SLASH-.../20260930T231718Z`, NG's `NG-SLASH-.../190147Z`; ledger closed, as below |
| 00:43Z | L8 | 26 | the round-26 packet `aa35ffcdca` to `3.0.0_SA_CVO~Z` (msg 27458) |
| 00:51Z | L10 | 26 | the CTO's round-26 analysis `3a758833b7` (msg 27460); round 27 = 3 cells; ruling 2: commit each sentinel after every leg close |
| 00:5xZ | L6 | 27 | ac-3 direct act, as below |

**Leg d structure:** 0 other names; the changed keys are `model_rows`, `inputs` and `content_sha256`, plus `as_of` on 8 (the build date
crossed midnight UTC).

**The ledger close:** legs b and c were found re-opened (the sentinel's working copy had reverted to its committed state) and were
re-closed with the same evidence. Ledger `amgt-corpus-r26-ab4` CLOSED.

**ac-3 direct act:** owner rows `Z-S72` (the code census reads `induction_scheduled.py:109` / `:111` UNRESOLVED; owner `~X`) and `Z-S73`
(REGISTRY_HASH stale; owner `~Z`, told), committed `32894174c0`.

## Compiler Tools

- `d25.py structure|inputs`, `deploy_ledger.py`, and `readonly_proof.main(['--code-census'])` (the Z-S72 cause).
- Gaps: a ledger sentinel's working copy reverted between two leg closes (cause not found). The remedy is to commit the sentinel
  after each close (round-26 ruling 2).
