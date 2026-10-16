# IRPT_ANLREQ round 24, workstream ~G (ENGINE) -- decomposition: the producer runs the swap, release 33's Lambda source, and the six-object delete

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** CTO msgs 8658, 8693, 8711, 8714, 8723 (ADDENDA 3 to 6 of `CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md`): r32 (applied 22:09Z), then the swap compose and the r33 door cell, then r33 (the `irpt-ycharts-generate` leg), then resident r34, then FWD-1 run 3; and the relay of Andrew's approval of call 2106 (MSTR msgs 8768, 8770). Round 23 merged the swap pass, its pool builder and the Yahoo history port (`8540b8449c`, `a6bcac3875`), round 22 the door's decision tree (`78e28b386b`).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The producer is the one consumer of the swap.** `opal_producer.py` gains an OPTIONAL `swap` store; with none, nothing changes (an UNRESOLVED holding refuses the run as it does today), so this cell moves no resident byte until round 25 supplies the store. The swap runs inside `_read_stage`, so `produce`, `produce_package` and `produce_commentary_pdf` all see the same effective rows. A run with nothing analysable left refuses before any write (`NO_ANALYSABLE_HOLDINGS`).
- **The report names every substitution first.** One `SWAP` disclosure per record (the pass's own sentence: the replacement, or "<SYM> is not analysed; Opal Staff will manage the replacement."), before the pricing disclosures and the weighting one; the settings carry the pool's vintage and the counts; the run record carries the records (no amounts).
- **Release 33's source is a map-and-Terraform cell, separate from every code cell.** `AR-g-102` re-pins exactly the staged rows whose files the ENGINE cells changed since each row's old pin, adds the `ticket_confirmation.py` member, and DECLARES the ticket-table variable and its one-statement GetItem policy. The shared-zip lesson (R42) is applied: the issuer read `git log` for each re-pinned path since its old pin, and one foreign commit rides in (`acceptance.py`, IB-pr-478, IRPT_BCKEND), stated in the order for the pair to sign. The other 26 stale rows of the function (other lanes' merged work) are NOT re-pinned. The r33 pin is taken after the last cell that touches these files merges; no later cell in this plan does.
- **The delete is Andrew's, carried by an order.** Call 2106 (the six release-29 synthetic objects, every version) was approved by Andrew (record `ANDREW_DIRECT_20261015_203xZ_A252_...`); the Dell identities are denied that act on purpose, so the CTO relays it to the laptop CloudOps seat `0.7.0_AE_CloudOps~U7` as an order that reads its six keys from the pinned list file (never retyped) and STOPS on a denial. `TO-DELETE-C449-U7` is `~Y2`'s to flip (MSTR msg 8770); this seat does not touch it.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-100` | `ycharts/research/opal_producer.py` (the optional swap store, `_swap_stage`, the effective rows, the run record's swaps, the `SWAP` disclosures and settings), eight named tests in one file | the two files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |
| `AR-g-102` | `infra/aws/lambda/ci/lambda-source-map.json` (six re-pinned rows and one new row of `irpt-ycharts-generate`, one re-pinned row of `irpt-status`, one files entry) and `infra/aws/terraform/investor-reporting/ycharts/generate.tf` (`IRPT_TICKETS_TABLE`, one inline policy of one GetItem statement) | the two files named in the order + the worker's folder | WORLD (an IAM declaration and a source map; nothing applied) |
| `AR-g-105` | the delete of every version of the six release-29 objects, a result file and a closed ledger | `0.7.0_AE_CloudOps~U7`'s folder and ledger; six S3 keys | WORLD (an S3 delete under Andrew's recorded approval) |

## Edges and chains

- THREE chains, no shared file: `AR-g-100` (producer), `AR-g-102` (map and Terraform), `AR-g-105` (an applier order to another seat on another box). `AR-g-101` (round 25: the resident assembly, the builder flag and the bindings pin for the pool) follows `AR-g-100`; the r33 pair follows `AR-g-102` and an applier order (`AR-g-103`), the r34 pair follows `AR-g-101`.

## Four-postulate record

(i) Domain: the producer's three entry points over the read stage; the map's two functions; the six listed objects. (ii) One swap store contract, one record shape, one pin rule (the last commit touching the path). (iii) One intent per cell. (iv) What this cut does NOT move: the resident bindings and builder, the door, `swap_pass.py` and the history port, any deployed byte, and `TO-DELETE-C449-U7`.

fanout: 2 of 3 chains, cap 8, reason: two worker cells (producer, map and Terraform) with no shared file; the third chain (AR-g-105) is an applier order to `0.7.0_AE_CloudOps~U7`, not a worker; slots 201 and 202.
