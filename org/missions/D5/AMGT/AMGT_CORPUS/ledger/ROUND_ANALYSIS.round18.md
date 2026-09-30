# AMGT_CORPUS -- ROUND 18 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~02:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26844, subject *"L10 slug AMGT_CORPUS round 18 @2a1abc8529"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v21.md`. Issuer packet: `ROUND18_DRAIN_END_PACKET.md` @`8868d88625`.

**Round 18 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`t-1`: the model-block `admit` step.**
  - It reads the population first: registered 96, without a block 0.
  - It refuses loudly and names the surface when Bloomberg is not signed in, with the planted control pulled 1.
  - It is scheduled after registration (`registration,model_block_admit`).
  - The live dry run made 0 vendor calls.
- **`t-2`: `build_unit_map` per-security exceptions.**
  - The replay at HEAD reads shared changed 0, removed 0, type changed 0, and 209 of 214 reproduced.
  - The CVO listed the 5 unreproduced additions: all `measured_on` appends under BEST_DPS, BEST_EBITDA, BEST_EPS,
    BEST_PE_RATIO and CIE_DES_BULK. That is one header family, which the CLI omits (`Z-W2-S14`).
  - `Z-S65` GRADUATED.
- **`t-3`: the reader key-form census.**
  - 20 readers: 18 read the raw `/` key and are OK; 1 is ABSENT (`render_pack.main()`, a hand-run CLI).
  - The CVO checked the one served path the packet did not name: `/print` reads the block by the resolved raw key
    (`scoped_amgt.py:4479`), and `render_pack`'s derived `sec_key` only names output files.
  - So `Z-S64` stays a migration item, per round-17 ruling 3.
- **`t-4` (the `r-1` re-sign) is held on AMGT_RESAPP r51 cell 1.** `crosswalk.py`'s newest commit is still `6a940b02b8`.

## 2. RULINGS

1. **`Z-W2-S13` (an exception under a SCALAR shared field is invisible to `_resolved_unit`/`_resolved_sign`, so Hitachi's
   BEST_SALES reads the shared `MILLIONS`): CELL 1, with a measurement before any served act.**
   - The readers honour `per_security_detail[<sec>].exception` for scalar fields, as t-2 did for dict fields.
   - The cell also PRINTS the unit that Hitachi's raw BEST_SALES pull carries against the unit on the served block
     (`derived/model_block/6501_JP_Equity/20260929T232834Z`).
   - If they differ, the served block is re-derived under its own pair, with the expected diff read from the fixed reader at
     signing. If they agree, the served block stands, and the fix protects the next such name.
2. **`Z-W2-S14` (the CLI and the producer feed `build_unit_map` different headers): CELL 2.**
   - The CLI builds with the producer's header preparation (`_ensure_unit_map`'s path), so the replay reads **214 of 214**.
   - "Byte-equal" then means byte-equal. The 209-of-214 grading was agreed on an explained gap, and it should not become the
     standing bar.
3. **`Z-W1-S18` (`price_axis_pull.py:97-100` puts the MAIN workspace on `sys.path` at import): routed to AMGT_RESAPP, not a
   cell here.**
   - The file's writers are AMGT_RESAPP's workers (last `e2d89be7da`, `08b2c49923`). Under one writer per artifact, its owner
     cuts the change.
   - It is a GRADING hazard across projects: a multi-file pytest in a worktree grades the main tree's bytes, so a red reads
     green.
   - It also hardcodes a device path (`C:\Users\Opal Bloomberg\...`), which breaks CLAUDE.md's DERIVE, don't hardcode rule.
     The fix derives the root from the file's own tree (`git rev-parse --show-toplevel` or `Path(__file__)`) and moves no
     import-time path into the main tree.
   - It goes on RESAPP's next analysis list.
4. **`t-4`: CELL 3, dependent, unchanged from round 17 (cell 4).** It re-signs `r-1` with the `admit` step once RESAPP r51
   cell 1 drains. The first scheduled fire is the acceptance.

## 3. FWD GRADES

- R-4: 19 of 19 graded ever. 13 of 19 REALIZED, unchanged. The six render outcomes remain AMGT_RESAPP's.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 19 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **`_resolved_unit` / `_resolved_sign` honour a scalar field's per-security exception; print Hitachi's BEST_SALES raw unit against the served unit** | LOCAL (the fix and the read) | Ruling 1. A difference becomes a served re-derive under its own pair, cut the next round. |
| 2 | **The `build_unit_map` CLI uses the producer's header preparation** | LOCAL | Ruling 2. AC: the replay reads `hitachi_reproduced 214 of 214`, shared 0, type 0. |
| 3 | **Re-sign `r-1`**, carrying the `admit` step | WORLD, under a pair and a NEVER-2 entry | It waits on AMGT_RESAPP r51 cell 1. |

**Fan-out:** 2 now; cell 3 is dependent.

**Routed, NOT cells:**
- `Z-W1-S18`, to AMGT_RESAPP (ruling 3);
- `Z-S64`, the migration (round-17 ruling 3).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Remove the drained worktrees `wk-crps16-1`, `wk-crps17-1` and `wk-crps18-1/2/3` [recursive delete, CLAUDE.md Agent Autonomy].
  Every branch is kept.

## Compiler Tools

- The CVO's v21: its `t2_AC1.sh` re-run, its listing of the 5 unreproduced additions, and its `/print` path read
  (`scoped_amgt.py:4479`, `:4495`, `:4517`; `render_pack.py:155`).
- This seat: a read of `integrations/bloomberg/research/price_axis_pull.py:90-104`, and `git log` on that file (its writers).
