# AMGT_CORPUS round 34 -- `CRPS-aj-2` never-widen pair, CTO half (re-pin `amgt-induction-daily` to a864e82a5c + one on-demand fire)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~23:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND34_AJ2_SERVED_ACT.md`
@5454d04761 (msg 29059). **Authority:** Andrew ~20:3xZ card 3, "yes to all recommendations" (@9fe6e6f111). This is the per-use vendor
word for one daily Bloomberg pull covering earnings dates, the V3 fields and a long name.

## What I read

- **The pins:** old `33c1d096a3` is an ancestor of new `a864e82a5c`. The pinned checkout serves ONLY this task, and other jobs run
  from the working tree. Its served writer is `model_block_pull.stage_derive` (ONE rule; three callers). Between the pins, the code
  that moves served blocks is `model_block_pull.py` (+542/-34: the `refresh` stage and the 52 appended mnemonics) and
  `induction_scheduled.py` (+20/-5). `field_map.json` at the new pin is the map the served blocks were already derived under: the act
  writes it 0 times.
- **The branches, read from the producer at the base dry runs:**
  - **A (DAPI up):** about 768 Bloomberg calls; 96 new write-once blocks become the newest served; 0 Seeking Alpha calls.
  - **B (signed out):** rc 4; served UNCHANGED.
  - **C (partial):** a failed name keeps its prior block.
- **The blast radius per key and the rollbacks** are in the half. A served block rolls forward from the prior raw stamp, and no
  delete is used. The task's action rolls back by re-registering the old pin.
- READ_HERE sets no data-volume threshold; its budget is sign-in attempts. A REFUSED fire stops, and the sign-in goes to Andrew (his
  login).

## Conditions

1. **Gate leg 0 as written:** the plan prints Python311, or STOP before `-Register`.
2. **Leg v in full:**
   - the run log's refresh line;
   - the 96-name served census with its denominator, naming every name not at the run date;
   - the per-mnemonic field-error census of the 52;
   - 3 routes plus BA's Model tab screenshot.
3. **Added by this seat:** on BA's Model tab, the 52 new mnemonics must not surface their pointer unit ("SEE field_map.json ... not
   yet built") or a raw list value. A count of that text on the rendered tab must read 0. A non-zero count is the half's "broken
   Model tab" STOP: forward-roll-back the moved names, re-pin to the old pin, and file a row.
4. **The standing daily fire at 13:00Z** recurs under card 3's word. A REFUSED or partial day is recorded, never retried in a loop.

**CTO HALF: SIGNED** for legs 0, r, f and v at pin a864e82a5c, covering branches A, B and C.
