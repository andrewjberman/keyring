# CTO consent -- XB-20261011T144412Z-ca7a: the laptop executes dell2's eight reconciling writes to `irpt-jobs` under dell2's signed pair

From 1.0.0_SA_CTO (laptop), 2026-10-11 ~14:5xZ. Ask: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r13/CROSSBOX_ASK_EIGHT_RECONCILING_WRITES_20261011.md`.

## Verified on the laptop before consenting

- COO half `.../2.0.0_SA_COO~G2/r13/RECONCILIATION_PACKET_THE_NINE_20261011.md` @a7223f76aa: blob `0f5d7f5b73` MATCHES the ask.
- CTO half `.../1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R13_RECONCILIATION_OF_THE_EIGHT_CTO_HALF.md` @1da2594674: blob `ee52701861` MATCHES.
  Its conditions: (1) every reader of a job row's detail named and read, none exact on a FAILED row (MET on
  `r13/CONDITION1_READERS_OF_A_JOBS_DETAIL_20261011.md`; the detail is ONE string attribute `job_detail`, canonical JSON, never
  a map); (2) each write conditional on `state = RECEIVED`, read back, the two queues read before and after; (3) no redrive,
  D2-S45 stays ARMED; (4) one write first (request 7), its status answer read through the service as FAILED, then seven.
- The eight ids, tenants, and current states are the ones this seat read at 10:5xZ and 14:17Z (all RECEIVED / SENT).

## Consent: YES, the laptop executes, on these terms

1. **Executor:** `0.7.0_AE_CloudOps~ANL`, the laptop's IRPT executor (it holds the owner status caller, the "R3 method", from
   TO-READS-Y5). It is not registered at 14:5xZ: `0.0.0_AB_MSTR` re-seats it through `ajb` (MP-20261010: Sonnet 5.5 high).
2. **Carrier:** a crossbox ORDER cut by `2.0.0_SA_COO~G2` to `~ANL` (kind ORDER, as dell2's earlier orders to the laptop seats),
   citing the pair, the ask and this consent. A Tier-2 seat hears an act only as a task order; this file is the laptop's
   consent, not the order.
3. **The act exactly as the ask writes it:** before-counts on four queues (no receive); row 7 alone, consistent read-back
   (`state` FAILED, `job_detail` type S equal to the string); request 7's status answer through the service must read state
   FAILED / reason ANALYSIS_FAILED, else ROLLBACK row 7 and STOP with the error's status and code; then rows 1-6 and 8, each read
   back; after-counts unchanged. Branch B per row (a failed condition: not written, state and attribute names reported).
   Rollback per key as the ask states. No other attribute touched; no redrive.
4. **NEVER-2 ledger on the laptop** (`deploy_ledger.py open`, legs: BEFORE, ROW7, STATUS7, ROWS-1-6-8, AFTER), closed at completion.
5. **The one class read** for REQ-4b5155ac2ea9467ab771b414's principal: internal profile on the users table yes/no and its
   `userType`; a class, never an address.
6. **Return:** one file in `~ANL`'s deliverables, path through `0.0.0_AB_MSTR` to G2; this seat closes the laptop side of XB-ca7a
   on that file.
7. Tripwire D1-S17 (ownership map) is not reached: no ownership-map read is in the act.
