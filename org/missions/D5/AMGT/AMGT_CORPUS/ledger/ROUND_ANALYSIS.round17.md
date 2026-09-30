# AMGT_CORPUS -- ROUND 17 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~01:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26818, subject *"L10 slug AMGT_CORPUS round 17 @db10a16583"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v20.md`. Issuer packet: `ROUND17_DRAIN_END_PACKET.md` @`1d85152810`.

**Round 17 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`s-1` is terminal VALID.** The census found 95 of 96 names with a model block and Hitachi absent.
  - Under the pair (this seat's half, with ruling (b) at section 2a), Hitachi's block is SERVED:
    `derived/model_block/6501_JP_Equity/20260929T232834Z/model_block.json`, 11 FY rows. The CVO re-read it on S3 with a
    positive control.
  - The live census reads 96 of 96.
  - `field_map.json` at `ead621d685` adds only Hitachi: 1 + 176 + 37 = 214 additions, 0 changed or removed. The CVO diffed it
    element by element.
- **`s-2` (the `r-1` re-sign) is held at the issuer on `Z-S66`.** Nothing is registered. The CVO measured this and AGREED.
- **The L9 residue attribution is AGREED.** The CVO strengthened it: the residue's two recorded puts never reached S3 (0 of
  2,958 objects written 05:40-05:46Z), which fits `substrate.py`'s stub client.

## 2. RULINGS

1. **The model-block admission (`admits_new_registrations False`): CELL 1.**
   - The producer exists (`integrations/bloomberg/research/model_block_pull.py`), so under the build ladder only its
     POPULATION is missing. The fix is not a new producer.
   - The mode's population is registered names with no block. It reads the crosswalk or registrations and the S3 listing,
     and prints the list with its denominator before any pull.
   - It fires as a STEP of `r-1`'s scheduled induction, after the registration step. That makes one schedule, not a second
     task, and puts it under `r-1`'s re-sign.
   - Vendor calls stay scripted under R-21 @`b390c36444`.
   - When the Bloomberg terminal is not signed in, the step must REFUSE loudly and name the surface
     (`integrations/bloomberg/READ_HERE.md`). A skip that looks like an empty population is not acceptable.
   - This is not a design fork: the estate holds one producer and one schedule, and the cell only joins them.
2. **`Z-S65` (`build_unit_map` downgrades shared fields on one ambiguous name): CELL 2, as ruled at the round-17 half
   (section 2a).**
   - When one name disagrees with a MEASURED shared field, `build_unit_map` records a per-security exception.
   - It never changes a shared field's status or type.
   - The acceptance is Hitachi's own input replayed at HEAD: the committed map is reproduced byte for byte, with 0 shared
     changes.
3. **`Z-S64` (the model-block writer bypasses `slash_safe_key`; `BP/` is stored under a literal `/`): a READ-ONLY census in
   CELL 3, not a re-key.**
   - Re-keying would move 6 served objects. Under CLAUDE.md rule 30, an existing pipeline reaches key conformance through its
     own migration, never as a rider.
   - The only question this round is whether any READER uses a different key form than the writer and so reads BP as
     ABSENT. If one does, that is a served defect and the next round cuts it. If none does, the row stays INERT and is
     carried as a migration item.
4. **`s-2` / the `r-1` re-sign: CELL 4, dependent.**
   - It waits on AMGT_RESAPP round 51's first cell: the `write_pool` union, moved into `write_pool` itself
     (`ROUND_ANALYSIS.round49.md` follow-up @`1b2294bbd6`).
   - The fork test is run through `add_security` on both sides.
   - This seat's CTO half re-grades branch 2, and it now also covers cell 1's step.

## 3. FWD GRADES

- 13 of 19 REALIZED, unchanged. No FWD's grade moves on this round: Hitachi's block is a served repair, not an endpoint
  outcome.
- The six render outcomes remain AMGT_RESAPP's.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 18 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **Registered names with no block get pulled.** A population mode on `model_block_pull.py`, run as a step of `r-1`'s induction. | LOCAL (the build); the fire is under cell 4's pair | Proven with a refusing transport: it prints the population (96 registered, 0 without a block, as of now) and refuses loudly when not signed in. |
| 2 | **`Z-S65`: per-security exceptions in `build_unit_map`** | LOCAL | Replay 6501 at HEAD: `field_map.json` byte-equal to `ead621d685`'s; 0 shared-field status or type changes. |
| 3 | **`Z-S64`: census of the key form used by model-block readers** | LOCAL, read-only | Every reader of `derived/model_block/`, and its key form, with the denominator printed. BP is read OK or ABSENT on each. |
| 4 | **Re-sign `r-1`** (including cell 1's step) once AMGT_RESAPP r51's `write_pool` union drains | WORLD, under a pair and a NEVER-2 entry | The first scheduled fire is the acceptance. |

**Fan-out:** 3 now (cells 1-3 are independent). Cell 4 waits on AMGT_RESAPP r51 cell 1 and on cell 1 here.

**NOT cells:**
- re-keying the model block (ruling 3);
- widening the evidence rule (round-16 ruling 2 stands).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None new. The removal of the drained worktrees `wk-crps16-1` and `wk-crps17-1` is a recursive delete (CLAUDE.md Agent
  Autonomy). It goes on his next worktree word, as before.

## Compiler Tools

- The CVO's v20: its S3 read with a positive control, its element-by-element `field_map` diff, and its 2,958-object put
  window scan.
- This seat: the round-17 CTO half's section 2a and the worker's `MODEL_BLOCK_CENSUS_ROUND17.md` producer section (4 callers,
  0 triggers).
