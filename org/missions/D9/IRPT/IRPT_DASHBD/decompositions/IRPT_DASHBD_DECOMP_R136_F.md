# IRPT_DASHBD round 136 -- workstream F-SHIP (~F2) decomposition: the 49 Financial transaction wiring (handler, Terraform write prefix, bundle members)

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~21:3xZ. Gate key: `<round>136</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 136**.

**Answers:** the CTO's round-135 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_135_20261016.md` @8d48df1751, msg 9837): round 135 CLOSES, no PRD addendum, "round 136 is your list in order". Its rulings carried here: (2) the applier for W4 is `0.7.0_AE_CloudOps~IB2` (DB2 is closed, rule 34); (3) the sid `WriteTheFiveGoldPrefixesOnly` stays and the packet says the plan changes the statement's prefix list only; (4) the Inflection bundle pin is re-cut and re-read at the Inflection release; (5) the two untagged seat-folder orders belong to their issuer. The enrichment list, with the state of each item at the cut:
1. **The 49 Financial transaction wiring** (the CTO's gate is met: `~D2`'s DB-b-300 ledger reads CLOSED 20261016T152240Z). Cut this round: **W1** the handler emission (`DB-f-2201`), **W2** the Terraform write prefix (`DB-f-2202`) and **W2b** the bundle members and pins (`DB-f-2203`, the source-map entry the plan names as the sibling). **Not a worker cell, after the drain:** **W3** the never-widen packet in `~D2`'s six-act shape (the issuer authors it from the merged bytes; the CTO and COO halves bind to its sha256) and **W4** the apply by `0.7.0_AE_CloudOps~IB2` after both halves are signed. At the cut the open ledgers were re-read in every live worktree (`git worktree list --porcelain`: 91 trees read, `ls-tree` of `org/critical_paths/.open_deploys/` in each; 50 distinct entry names matched `irpt-dashbd` or the IRPT family, each matched to its completion record on the trunk): no entry that reads OPEN names the 49 Financial `reporting-gold` root. The OPEN IRPT entries are `irpt-dashbd-cottonwood-landing-codeupdate-rewrite-r2-20261016` (DB-b-308, Cottonwood landing function, a different root: the CTO's own note), `irpt-holdings-exemption-mints-ib605-20261016` and `irpt-scope-feed-corrected-script-ibn2-20261016` (their titles name holdings exemptions and the scope-feed script; their targets were not opened). The 49 Financial ledgers that older branches still carry as files (hop 1, thresholds swap, the DB-b-300 listing grant) read CLOSED on the trunk.
2. **A fresh grade on the one snapshot (CVO):** attached to `DB-f-2201` as `DBF136-1-J1` (Inflection, the newest snapshot, denominators printed, the S6 print "N of 96") and `DBF136-1-J2` (49 Financial); the issuer draws both after the merge with `tools/sample_inflection_latest_snapshot.py` and `tools/sample_49f_producer_rows.py`.
3. **The Inflection pair** (after 49 Financial and Cottonwood) and 4. **the Cottonwood pair, then its transaction Income enrichment** (after DB-b-308's ten events close): NOT cut this round; each follows the 49 Financial pair's applied result, and the Inflection pair reads on the live runner whether the flat sync of `code/gold` copies the `.zip` beside the launcher.

## What was measured at the cut

Nothing new from the world: the wiring is code and text. Read: the handler (the guarded imports, `emit_classes`, the scheduled `run`, `run_backfill`), the gold root's `locals.tf`, `iam.tf` and `lambda.tf`, the source-map entry `irpt-49f-reporting-gold-lambda` (22 files, 21 pins), `account_transaction.py`'s imports (all members or the layer). **Found at the cut and carried as a stated fact, not a cell:** twelve tests in the gold Lambda's test directory fail at the base (`test_activity_lot_emission.py` 4, `test_class_catch_up.py` 3, `test_class_table_emission.py` 5; the fakes lack `as_of` after the class read was dated). They are pre-existing and outside every grant here; `DBF136-1-AC3` holds the line at "no failure beyond these twelve" (the ids are pinned in `checks/r136/handler_tests_base_failures.txt`).

## Cells (ONE issuance; WORLD floor by the `infra/` path)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| Handler: guarded `account_transaction` import, `transaction_frame`, `emit_transactions`, called LAST in `run` and `run_backfill`, two result keys, tests | `DB-f-2201` | FWD-5 | WORLD | none | R136-A |
| Terraform: the table constant, the prefix, the write list's last element (pure insertion in `locals.tf`) | `DB-f-2202` | FWD-5 | WORLD | none | R136-B |
| Source map: `account_transaction.py` and `transaction_words.json` as members of `irpt-49f-reporting-gold-lambda`, with their pins | `DB-f-2203` | FWD-5 | WORLD | none | R136-C |

**Decisions inside this decomposition (the issuer's, stated):** (a) the transaction stage runs LAST, after the filled-report stage, so a transaction failure can never delay the served filled report; it is guarded and never raises. (b) The stage reads the day's `fact_trn` partition through the reader `account_return_daily` already has: no new S3 listing code, and no read grant is added (the handler reads the silver the role already reads); the write grant is the only IAM change. (c) 49 Financial's transaction table is per-day, so the day is the partition day (unlike Inflection's cumulative snapshots). (d) The three files are disjoint, so the three cells run in parallel; the merge order is free, and the source map is shared with other lanes' re-pins (a conflicting merge is the issuer's to resolve). (e) The existing members' pins are NOT re-pinned (another lane's act); the packet's build step reads them. (f) `DB-f-2202` and `DB-f-2203` are `worker-light` (a few lines each), `DB-f-2201` is `worker`. (g) The twelve base failures are carried, not fixed: fixing them is a repair of tests the wiring does not touch, and a rider would widen the grant.

**Judgment criteria.** `DBF136-1-J1` and `DBF136-1-J2` on `DB-f-2201` (above). The Terraform and source-map cells are mechanical.

**Four-postulate record.** (i) Domain: the 49 Financial firm's account-transaction days the scheduled fire owes (the returns days it wrote), and the days a backfill rewrites. (ii) Same grain: one transaction partition per business day, as the producer's writer refuses a row under another day. (iii) One intent: the stage writes the table and nothing else, last, and cannot stop the stages before it. (iv) Not moved: the returns, class, lots and filled tables and their stages, the read grant and list pattern, the sid, the schedule, the layer, the function's size, the Cottonwood root and the Inflection path.

**Chain read.** M = 3 (R136-A, R136-B, R136-C), N = 3 cells, no dependency among them.

fanout: 3 of 3 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: three disjoint write surfaces (the handler and its tests, one Terraform file, one source-map entry) with no dependency among them. Workers `0.9.0_WK_IRPT_DASHBD~2201`, `~2202`, `~2203`.

| criterion | invocation | base reading |
|---|---|---|
| DBF136-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py . DBF136-1-AC1` | FAIL (no function) |
| DBF136-1-AC2 | `python -I .../checks/r136/p136_handler.py . DBF136-1-AC2` | FAIL (no wiring) |
| DBF136-1-AC3 | `python -I .../checks/r136/p136_handler.py . DBF136-1-AC3` | FAIL (no test file) |
| DBF136-1-J1, J2 | JUDGMENT: the CVO's 20-row comparisons (Inflection on the one snapshot; 49 Financial), fresh | not graded |
| DBF136-2-AC1 | `python -I .../checks/r136/p136_tf.py . DBF136-2-AC1` | FAIL (locals.tf unchanged) |
| DBF136-2-AC2 | `python -I .../checks/r136/p136_tf.py . DBF136-2-AC2` | FAIL |
| DBF136-3-AC1 | `python -I .../checks/r136/p136_sourcemap.py . DBF136-3-AC1` | FAIL (entry unchanged) |
| DBF136-3-AC2 | `python -I .../checks/r136/p136_sourcemap.py . DBF136-3-AC2` | FAIL (the members are not listed) |
