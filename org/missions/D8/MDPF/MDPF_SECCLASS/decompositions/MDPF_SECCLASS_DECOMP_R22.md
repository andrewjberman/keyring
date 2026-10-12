# MDPF_SECCLASS decomposition -- ROUND 22 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~10:3xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers one cell.

**Cut on:** the CTO round-21 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_21_20261012.md`, 1.0.0_SA_CTO~DELL1 msg 4327), on the CVO's slug
msg 4325 (`ADJUDICATION_v19`, `REMEDIATION_v12` @404145c727).
- **Item 1 is cell `SC-e-95`** (rows D1-W83-S5 and D1-W80-S4: ONE structural fact, read once; LOCAL, no served write).
- **Item 2 is carried, not cut:** SC-e-91's ship is `TO-SC-e91b` at `0.7.0_AE_CloudOps~SC1`, cut on both signed halves @0b947eb07f (round 21's order,
  carried; its leg G is the Reach range on the first post-ship fire).
- **Item 3 is already done:** `TO-SC-e90` was cut in round 21 and drained @4ff03e1393 (portal commit 64d8c6de38 on DEV).
- Carried, not cut: e57e61 (FWD-10 apply) stays HELD on its trigger; SC-e-87's leg G on the first NEW as_of (Tuesday 2026-10-13's fire or later).
- **Recorded this tick (the CTO's instruction, msg 4327): D1-W83-S5 is BOUNDED** while it stays ARMED until the read prints: three retained dates
  (10-06..08), no date added (the watermark is 10-09 and no later canonical partition exists), the page's latest as_of unaffected.

**State the round starts from (measured 2026-10-12 ~09:5xZ-10:3xZ, box/dell1):**
1. **C_06 freezes a date at its first build.** B_00 keeps moving a retained date's canonical bytes (2026-10-06..08 changed at 2026-10-11T04:16:35Z and
   2026-10-12T00:33:48Z; the 23:15Z writes of 10-10 re-put identical bytes); the next default fire re-serves none of them (SC-e-94, row D1-W83-S5).
2. **The retained revisit sees only each date's stored top-10 holdings** (SC-e-91, row D1-W80-S4): $519,506.84 of the 2026-10-09 mix-level Unclassified
   ($1,846,399.46) sits outside every stored list, 28.14 pct; at 2026-10-08, $342,689.08.
3. **The 2026-10-06 and 2026-10-07 served totals do not reproduce from the current partitions** (recomputed exceed served by $584,886.01 and
   $442,485.38; 2026-10-08 reproduces to the cent) (SC-e-88, row D1-W78-S1).
4. **Three choices are on the table and the CTO will not choose before the dollars and the cost are on the record:** re-derive a bounded window of
   recent trading days from canonical on every fire; rebuild once; or accept the drift with the dollars named.

## Rule 24 record

- **Domain:** the CTO's one read; nothing else is a cell.
- **(ii) Same grain:** one cell, one record, three questions: the dollars (per date, per class), the cost (per N), the mover (which writer, how far,
  how often); plus the answer to W80-S4's "who holds the unlisted dollars".
- **(iii) Intent coherence:** the acceptance reads the record's own arithmetic (class dollars sum to the totals, a control date reproduces), because a
  rebuild harness that moves an untouched date is measuring itself, not the data.
- **(iv) State coherence:** no served write; the rebuild is a computation over READ partitions; nothing under `gold/` or `platinum/` is written.

## The cell

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-95` | One read: per retained date 2026-10-06..09, the served C_06 firm totals against a rebuild from the CURRENT canonical partitions, by class in dollars, beside an untouched control date; the measured runtime, memory and write set of re-deriving N = 1, 3, 5 trading days per fire against the chain window; the writer that moves canonical bytes after first build, how far back and how often; who holds the 2026-10-09 unlisted unclassified dollars, by security. | FWD-1 (the dates leg G's comparator rests on) | LOCAL | none |

## Write sets (disjoint)

- **SC-e-95:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json` and its scratch scripts under `.scratch/`.
- It may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

One cell: one chain. Fan-out 1 of 1, cap 8. Slot ~85, `worker`, `<direct_act>true</direct_act>` (one cell, no product file, LOCAL: no L2, no L4-R, no
L8-L10; my one real run is its close, and its record IS the outcome).
The ruling (a rolling N-day re-derive, a one-off rebuild, or acceptance with the dollars named) follows the read and is the CTO's.
