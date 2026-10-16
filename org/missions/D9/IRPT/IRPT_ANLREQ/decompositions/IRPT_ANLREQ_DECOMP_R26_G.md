# IRPT_ANLREQ round 26, workstream ~G (ENGINE) -- decomposition: the release-33 build record and the release-34 pool input

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO ADDENDA 3 to 6 (msgs 8658, 8693, 8711, 8714, 8723): r33 is the `irpt-ycharts-generate` leg (and the `irpt-status` words) under its own pair; r34 is the resident release that carries the swap and the dated pool snapshot (no IAM change). Round 24 merged release 33's source (`927337a741`: six re-pinned staged rows, the new `ticket_confirmation.py` member, the ticket-table variable and its one-statement GetItem policy) and round 25 the resident installer's swap-pool binding. The release-census on the merged tree prints `changed_members=8` for `irpt-ycharts-generate` against the live zip.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The build is a cell of its own, like `AR-g-92`.** `AR-g-103` builds BOTH Lambda packages at the fixed pin `927337a741f40a83e7daa9e09154436a813b05dd` (the merge of `AR-g-102`, the last commit that changes a member of either package) with the repository's own builder in `BUILD_ONLY` mode, twice each, and records the zips, their CodeSha256 values and member tables. It uploads nothing and makes no AWS call. The issuer's verifier re-derives every number from the zips and the git objects and, in addition, requires the two CodeSha256 values to equal those of the ISSUER'S OWN trial build of the same pin (a second, independent build must be byte-identical), so the applier's `BUILD_ONLY` digest check has a value to be signed against.
- **The baseline for "what changed" is the last build commit, not the live zip.** The live zip is the applier's census. The record's delta is against each function's build commit: for `irpt-ycharts-generate` the map's `last_deployed_commit` (`06d1597652`), for `irpt-status` the release-31 map commit `af51e37a29` (the map's own `last_deployed_commit` for it is the last commit touching the source directory and is not the build commit; measured: the delta against it adds three members R31L already shipped). The expected deltas are exactly 8 members (five re-pinned, two native, one added) and exactly `status.py`.
- **The pool input is a read of one table under an applier order.** `AR-g-106`: the CloudOps seat scans `etf-classifications` (three projected attributes), writes the export, and builds the dated snapshot with the merged builder; the snapshot is committed so the r34 release tooling can pin it by `git show`. Read-only; a denied scan is a STOP (no second principal). The pool's row count, class count, largest class and per-holding Yahoo request bound come out of that read and go into the r34 packet.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-103` | the two Lambda zips (`irpt-ycharts-generate`, `irpt-status`) in a stage folder outside the repo, and `RESIDENT`-style record `R33_BUILD.json` in the worker's folder | the worker's `deliverables` folder, the order, the channel file | WORLD (floor of an infrastructure path; nothing deployed, no AWS call) |
| `AR-g-106` | the classification table export, the pool snapshot and the result file, committed; one table read | the applier's `deliverables/irpt_anlreq_r34/` folder | WORLD (an AWS read under an applier order; no write) |

## Edges and chains

- TWO independent chains. `AR-g-103` depends on `AR-g-102` (merged); it feeds the r33 pair packet and the applier order. `AR-g-106` depends on `AR-g-98` (the builder, merged); it feeds the r34 release tooling.

## Four-postulate record

(i) Domain: two Lambda packages (107 and 49 members); one table's three columns. (ii) One pin, one baseline rule, one verifier. (iii) One intent per cell. (iv) What this cut does NOT move: any deployed byte, the Terraform root, the resident, the map.

fanout: 1 of 2 chains, cap 8, reason: one worker cell (the build, slot 204); the second chain (AR-g-106) is an applier order to `0.7.0_AE_CloudOps~AQ2`, not a worker.
