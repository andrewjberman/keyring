# AMGT_CORPUS round 27 -- `CRPS-ac-2` never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~05:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND27_AC2_SERVED_ACT.md` @e4b31a6f28 (msg 27531).

## What I read myself (not taken from the COO half)

1. **Dry run evidence** (`deliverables/2.0.0_SA_COO~X/evidence/r27_ac2_dryrun.txt`):
   - `ac2 keys 100 move_blocks 1 map_entries 1 unit 10 sign 10 currency 0 value 0 case_blocks 0 top 0 other 0 errors 0 writes_per_block {1: 100}`;
   - the single map entry is `CAPITAL_EXPEND BBSE3 BZ Equity`.
2. **Code lineage:**
   - `b239301bb1` and the ac-1 merge `3a7cf75c4f` are both ancestors of HEAD.
   - `29d87a966a..HEAD` over `integrations/bloomberg/research/` + `lib/research/` touches exactly `build_unit_map.py`
     (+49/-4) and its new round-27 test, matching the COO half.
3. **Live before-state of the exact key** (boto3, bucket `opal-data-harvest`, prefix `derived/model_block/BBSE3_BZ_Equity/`):
   - 11 block stamps; the newest is `20260930T231715Z/model_block.json`;
   - in it, `CAPITAL_EXPEND` appears 20 times, `UNRESOLVED` 20 times (10 unit + 10 sign) and `ZERO-DOMINATED` 0 times.
   - This agrees with the half's "units 10 UNRESOLVED -> ZERO-DOMINATED; signs 10 reason text only".
4. **Writers of the moved properties:**
   - `field_map.json` has one writer, `build_unit_map.main`.
   - The block has one writer, `model_block_pull.stage_derive`. It writes a NEW stamp and refuses to overwrite
     (`model_block_pull.py:428-440`).
   - The dossier has one writer, `dossier.write_one`.
   - N = 3 writers, all three named in the COO half.

## Blast radius (what the act may touch) and rollback per key

| key | act | rollback |
|---|---|---|
| `field_map.json` | one commit, one entry (BBSE3 `CAPITAL_EXPEND`) | revert that commit plus ac-1 |
| `derived/model_block/BBSE3_BZ_Equity/<new stamp>/model_block.json` | one new object; no overwrite, no delete | the prior stamp `20260930T231715Z` stays; re-derive forward |
| BBSE3 dossier | at most one new object, only if its inputs changed | the prior dossier stays |
| every other key of 100 | nothing | -- |

## Both branches

- **The act runs as dry-run-predicted:** the served `/thesis` for BBSE3 carries the ZERO-DOMINATED unit text in place
  of the UNRESOLVED reason. Values, currency, case and top-level are byte-unchanged. `modelSheet.ts` reads no unit
  field, so the Model tab rows do not move.
- **Any leg differs from its capture:** the COO half's STOP limbs 1-3 apply. Nothing past the failing leg runs, and
  the map commit is reverted.

## Conditions

1. Leg v's negative arm is mandatory and printed: TSM `CURR_ENTP_VAL` stays UNRESOLVED, and BA `EQY_DPS` keeps its unit
   byte-unchanged.
2. The NEVER-2 sentinel is committed after every leg close (round-26 ruling 2).

**CTO HALF: SIGNED** for gate, (a), (b), (c) (one block) and (d) (at most one dossier object), at HEAD >= `b239301bb1`.
