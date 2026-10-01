# IRPT_BCKEND round 26 (~P) -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~18:5xZ. **Input:** `2.0.0_SA_COO~P`'s slug 103376 and drain-end
`deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUND26_P_DRAIN_END_20260930.md` @299d57ca4d (three cells terminal: pr-261 drained
@18518f52d4, pr-262 applied 16:19Z under both halves, pr-263 superseded on S236). Rows read from the channel at HEAD: W97-S3, W97-S4,
S237. The analysis this round answered: `ROUND_ANALYSIS.round25P_sweep3_4.md` @dd4c69b696.

## 1. What round 26 proved

- **W86-S1 is DISARMED.** The INF gold chain passes step 3 and reached the raw writers for the first time since 09-28 (run
  `chain_full_20260930_145412`: bronze positions and transactions for 09-30 landed). The ship went flat beside its importer because the
  runner flattens by basename and has no `lib/` on its path (the worker's two readings, `RESOLUTION_READINGS.json`). That finding is
  the reason for the deployed-layout issuer rule sent to all laptop issuers today (103370-103374).
- **S216 stays ARMED, on its own condition.** `fact_positions` still ends at 2026-09-27; the chain broke in a second place (the ingest
  mirror and `opal-assets-silver-orion`, which logged only START on 09-28/29). The frontier read remains the disarm.
- **pr-262 is applied;** W86-S2 disarms on the held observation of the next real stop event (the a1 ledger, by 2026-10-01 11:20Z).
- **S219 is closed by S236:** the two gap partitions are zero-OK by the engine's own rule; no schema bump. Accepted.

## 2. Rulings

1. **W97-S3, the NNA coverage guard (BLOCKING): no blind excusal; a conditional ruling so the record is immediate on read.** The guard
   refuses because three served NNA rows for partition 2026-09-24 would drop: account 866 -20,000, 769 +10,000, 1096 +10,000, signed
   net $0.00, gross $40,000. A signed net of zero across three accounts is the shape of an internal transfer re-read as INTERNAL on
   today's raw, which NNA is right to exclude, but that is an inference until read. Round 27 cell (read-only, first): compare the 09-24
   transactions for the three accounts between the last raw that produced the served rows and today's raw; print each row's
   classification before and after and whether the three accounts share a household or client.
   - **Branch A (the rows are one transfer among related accounts, now INTERNAL):** the drop is a correction of served NNA. It still
     moves served output, so it lands as a small never-widen packet (the three literal keys, before and after, the reason, rollback by
     re-emitting the prior values) with both halves; this seat signs on read of the packet if the diagnosis shows Branch A. The excusal
     in `lib/nna_coverage_excusals.json` names the packet as its decider record. The guard is never disabled.
   - **Branch B (anything else):** no excusal. The input regressed; the repair is upstream and is its own cell.
   While the guard holds, INF_C_02..INF_D_11 do not run. INF's served gold has been stale since 09-27 on S216 anyway, so a one-round
   hold costs nothing that is not already lost, and moving served NNA unread would.
2. **S216's second break:** round 27 cell, read-only diagnosis first (why the mirror and silver-orion did not move `fact_positions` on
   today's raw), then the repair under its own ledger. The disarm is the frontier read past 2026-09-27, unchanged.
3. **W97-S4, the two raw days that will not backfill (09-28, 09-29):** the daily pull is a snapshot, so those days are a declared gap.
   Under PRD v0.20-v0.21 they are NOT COMPUTABLE days for INF holdings-basis performance, and each voids the next trading day; that is
   the served behaviour until a backfill exists. The round-27 diagnosis cell also reads (from the Orion API's own documentation, no
   call) whether the positions endpoint accepts an as-of date. If it does, the backfill is a vendor use no word of Andrew's names yet
   and is listed for him with that citation; if not, the gap is permanent and says so on the page.
4. **S237 / S239, the retiring engine's skipped-day flow error (a $1.125M deposit served as +56.10% on 2025-01-10, 44 accounts):
   measure the blast radius before any remedy.** The row's own open question decides it: does the error reach a served PERIOD return?
   Round 27 cell (read-only): read the served 49F since-inception and 3Y answers for account 0093614544 and two other affected
   accounts through the live adapter, and name which reader shape the served path uses (partition listing, which refuses the non-OK
   window, or calendar enumeration, which hides it).
   - **If it propagates:** the remedy is the 49F holdings-basis re-switch (the planned port that retires the engine for serving), moved
     up to a round-27 cell under the sweep-2 every-period rule and its own halves. The retiring engine is NOT patched: a fix to `c02`
     would be a second path for a figure that is being retired.
   - **If it does not:** the harm stays at the daily grain of a table no client reads, and the re-switch retires it on its schedule.
   IRPT_DASHBD already carries the correct skipped-day rule (DB-b-1's face @51c05d1530), and its tie-out oracle is Black Diamond's own
   return, not this table, so the dashboard is not exposed.
5. **S235, the Schwab silver miss for 2026-09-29 (a trading day):** the 49F r3 ledger's A1 stays open until a scheduled fire finds its
   silver, as the packet says. The miss itself belongs to the Schwab ingest lane (AE PartnerETL, the `/49-schwab-conv` owner): ~P cuts
   it as an AE-lane order; if that seat is dark, the order is parked with its owner and the condition that un-parks it (the pattern
   ruled for MDPF_SECCLASS SC-e-12 today).
6. **Top cell stands:** `_authz/served.py` enforces a service principal's `allowedFirmIds` (403 on a foreign `selected_tenant`, with a
   test; ~Y's patch candidate @4a3cabe67d), SERVED under a packet and both halves, then ~Y's live negative control; S238 disarms on my
   read of both prints; W27 opens after.

## 3. Outcome read

No FWD is REALIZED by round 26. FWD-3's INF arm moved from "chain dead at step 3" to "raw lands, silver does not"; its served figure
is unchanged. FWD-3's 49F arm waits on the re-switch (ruling 4 may move it up).

## 4. Enrichment for round 27 (~P; one issuance)

1. The `_authz/served.py` enforcement (ruling 6).
2. The read-only diagnosis cell covering three reads: the NNA 09-24 transfer (ruling 1), the mirror and silver-orion no-op (ruling 2),
   the Orion as-of documentation (ruling 3).
3. The S237 blast-radius read (ruling 4); the 49F re-switch joins round 27 only if it propagates.
4. The S235 AE-lane order, parked if the seat is dark (ruling 5).
5. Carried: S132 least privilege on the edge role; the INF adapter switch after S216 disarms and the INF holdings producer fires on its
   schedule.

Every cell that changes an import in deployed code carries the deployed-layout criterion (103370).

-- 1.0.0_SA_CTO
