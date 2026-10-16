# TO IRPT_DASHBD.TO-DB-f-2103 -- the FWD-5 DISPATCH TXN STEP, ONE CELL: `orion-gold-dispatch.sh` gains INF_G_01 as a BEST-EFFORT, POST-SENTINEL block beside the Eclipse block, by pure insertion

<to_id>IRPT_DASHBD.TO-DB-f-2103</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2103</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>135</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 9486 (the Inflection producer is a step in the Orion gold dispatch chain; the portal publish is never gated on a new, unserved table, Andrew directive 2026-05-15) | **Rows:** IRPT_DASHBD-D2-W2103-S<k> | **Decomp cell:** `DB-f-2103` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2103` (branch `wk-IRPT_DASHBD-2103`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2103/`. The folders `data/inf`, `lib`, `infra/logic` and `org/missions/D9/IRPT/IRPT_DASHBD/deliverables` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. Offline tests only. **You have NO AWS in this order: make no AWS call of any kind** (the script's `aws` calls are never executed by your tests except against a stub on PATH). No real id, no client figure, no security name anywhere.

**Why.** `data/inf/scripts/gold/orion-gold-dispatch.sh` is the Orion gold chain runner: a CATALOG of `ID|file|flags` rows (`{date}` marks a date-capable script), chain variables, a `--chain` case, and best-effort blocks that run AFTER the publish sentinel so a failure never blocks the portal (the Eclipse block is the pattern). The Inflection transaction launcher (`INF_G_01.account_transaction_gold.py`, a sibling order) must become such a step: its own catalog row, its own chain `txn`, and a TXN-BLOCK after the Eclipse block. It is in NONE of the full, incremental, compute or gold-stage chains.

**The inputs (read, never edited).** The pinned base copy `deliverables/2.0.0_SA_COO~F2/checks/r135/dispatch_base.sh.txt` (113,445 bytes; the checker compares your file against it: **the edit is a pure insertion, but for one error-message line that gains the word `txn`**); the Eclipse pattern in the script (the CATALOG near lines 239-318, the help near 1239, the `--chain` case entries near 1572-1580, the ECLIPSE-BLOCK near 1988-2040 at base); the existing tests `data/inf/scripts/gold/tests/test_aor_resolution.py` and `test_aor_fold_derivation.py`; the checker `deliverables/2.0.0_SA_COO~F2/checks/r135/p135_dispatch.py` (**read it first; it states every rule; it has a `--selftest`**).

**The cell (`DB-f-2103`), in this order; commit after step 2.**

1. **Insert, and only insert:**
   - The CATALOG row `INF_G_01|INF_G_01.account_transaction_gold.py|--upload --date {date}`, once, AFTER the `INF_E_00` row.
   - `CHAIN_TXN="INF_G_01"` beside the other chain variables. `INF_G_01` appears in no other chain variable.
   - `TXN_STEP_TIMEOUT="${TXN_STEP_TIMEOUT:-1800}"` and a function `run_txn_step()` modelled on the Eclipse step runner: it runs the script under `timeout -k 60 "$TXN_STEP_TIMEOUT"`, records its result in `TXN_RESULTS`, and ALWAYS `return 0` (never non-zero, never `exit`).
   - The `--chain` case entry `txn) SCRIPT_IDS="$CHAIN_TXN"; CHAIN_LABEL="chain:txn" ;;` (the checker pins its exact shape), its line in `show_help`, and the word `txn` in the unknown-chain error's `(valid: ...)` list (the one changed line).
   - The TXN-BLOCK (comment line `TXN-BLOCK (best-effort, post-sentinel)`) AFTER the ECLIPSE-BLOCK and BEFORE the line `# Auto-shutdown: fires after all modes`: it runs only for `MODE=chain` with `TARGET` full or incremental and `DRY_RUN=0`, loops `for _txn_id in $CHAIN_TXN`, calls `run_txn_step`, writes a status marker `gold/irpt_txn/_meta/dispatch_txn_status.json` the way the Eclipse block writes its marker, and says in a comment that it does NOT affect chain_exit.
2. **Tests** `data/inf/scripts/gold/tests/test_dispatch_txn_block.py`: at least 12 tests with names containing `catalog`, `chain`, `block`, `sentinel`, `shutdown`, `insertion`, `syntax` and `date`: the row exactly once and after INF_E_00; `CHAIN_TXN` set and in no other chain; the case entry and help line; the block's order (after the Eclipse block, before the auto-shutdown); the guard tokens; `run_txn_step` never returns non-zero; the diff against the pinned base is a pure insertion but for the error line; `bash -n` passes; every line the edit ADDS is ASCII (AMENDMENT 1: the pinned base holds 10 non-ASCII lines of its own, which stay; the test compares the added lines against the pinned base, never the whole file); `{date}` is on the row. Where a test needs the script's behaviour, extract the function text and run it under `bash` with a stub `timeout` on PATH; make no AWS call.
3. **Mutant** (temporary, reverted): make `run_txn_step` end with `return $rc`: at least one test fails. Say which.

<criterion id="DBF135-3-AC1" cell_refs="DB-f-2103" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r135/p135_dispatch.py" . DBF135-3-AC1</invocation><expect>DBF135-3-AC1 PASS</expect></criterion>
`DBF135-3-AC1` -- the dispatch edit in one verdict: the diff against the pinned base copy is a pure insertion but for the unknown-chain line gaining `txn`; the catalog row exactly once after INF_E_00; `CHAIN_TXN`; no other chain carries INF_G_01; `run_txn_step` and its timeout; the case entry and help line; the TXN-BLOCK between the ECLIPSE-BLOCK and the auto-shutdown with its guards and marker; `bash -n` passes; every added line ASCII; at least 12 tests with the named words, and those plus the three existing dispatch-related test files pass. Base: FAIL.

<expected_criteria>DBF135-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the pinned base copy, every other script, the launcher (a sibling order), the existing tests, every Terraform file.
- **AWS: none.** **NOT DEPLOYED.** Do not upload the script; the release pair does.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2103-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2103/
data/inf/scripts/gold/orion-gold-dispatch.sh
data/inf/scripts/gold/tests/test_dispatch_txn_block.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2103.fwd5-dispatch-txn-step-best-effort-post-sentinel-block.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md</decomp_doc> round 135, workstream ~F2 (F-SHIP), cell `DB-f-2103`.
<owned_cells>DB-f-2103</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: DBF135-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2103/IRPT_DASHBD.TO-DB-f-2103.fwd5-dispatch-txn-step-best-effort-post-sentinel-block.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF135-3-AC1 --governing-order <this order>` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the new test count and the three existing files' results; the mutant and which test failed; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a script edited in a branch and offline tests; nothing is uploaded, scheduled or run.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access in this order.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the chain's schedule is unchanged and the new step runs only after the release.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF135-3-AC1 FAILs at base and the checker's helpers are exercised by its self-test (7 arms).
lane: the <paths> block IS the grant.
</preflight>
