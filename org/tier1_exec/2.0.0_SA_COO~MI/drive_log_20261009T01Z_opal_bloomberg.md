# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-09 01:30Z -> 02:0xZ (host opal_bloomberg)

**archetype:** COORDINATE

## Tick 6 -- empty tick, so `/next-calls NFRA_MCPINDEX --drive` ran (keep-driving empty_tick=on, box sitez)

- **Limb:** L7, round 7, 6 of 7 orders terminal. MX-s-19 is gated on the A2 dates (Monday 10-12, Tuesday 10-13).
  Lease FULL.
- **Calls:** 0 open for NFRA_MCPINDEX on the open-calls queue (sitez-20261008T174201Z-f241 is CLOSED). None queued.
- **WHILE WAITING act:** amendment A5 @ba7f474c6e makes the A2 precondition one read,
  `round7/checks/s19.PRE.sh`.
  - Limbs per date: the sentinel OK line AND the object by head-object; the bd-silver-merge transactions and realized
    SUMMARY lines with failures=0; and silver objects written 00:00-03:00Z.
  - The last two limbs are the Z-W24-S8 discriminator, read before the disable rather than first on 10-19.
  - Controls: positive 10-08 and 10-09 -> 2 of 2 PASS. Negative 10-05 -> 0 of 1 FAIL.
  - The negative control exposed that the old code printed `OK: bronze sentinel emitted` on 10-05 while the object
    reads 404. That is why the head-object limb exists.
- **Re-assessment:** 0 FREE options. The round-7 rectangle is frozen mid-round. The armed rows Z-W8-S3, Z-W11-S2 and
  Z-W22-S1 are carried to the round-7 slug.
- **Row:** `NOTHING-LEFT: MX-s-19 event-gated on 2026-10-13 after 03:00Z (s19.PRE.sh); round-7 close gated on MX-s-19
  AC2 (2026-10-19/20); 0 calls queued`.
- **Msg 32229** (law edit: rule 30, the naming gate now refuses) read and acked. No act: this lane types no new
  resource names this round.

## Compiler Tools

- `open-calls.py mode get` -> empty_tick=on.
- `open-calls.py list`: 9 OPEN lines box-wide, 0 for NFRA_MCPINDEX.
- `s19.PRE.sh` x3. A harness heredoc unescaped `\\r` into a literal CR (line 16); caught by `od -c`, fixed and re-run.
- `safe-commit.sh`: refused once on a peer's open merge (MERGE_HEAD e9a9ed4f1b, a 0.9.0_WK_NFRA_OPLGTW~41 drain). It
  cleared in 84 s, and the retry landed.
