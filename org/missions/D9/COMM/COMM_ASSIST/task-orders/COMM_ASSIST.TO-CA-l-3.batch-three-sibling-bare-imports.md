# TO COMM_ASSIST.TO-CA-l-3 -- round 20 CA-l-3: ONE batch repair -- the three sibling tests with the bare-import defect; no product change

<to_id>COMM_ASSIST.TO-CA-l-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~31</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>SIBLINGIMPORT</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-l-3` (`decompositions/COMM_ASSIST_DECOMP.round20.md`) | **outcome_ref:** none (hygiene: CTO round-19 analysis ruling 4; no outcome of its own) |
**depends_on:** none (the round-19 batch CA-k-3 merged `93a3f55d25`)

---

## WORKER FACE

### THE CELL

Three test files under `data/transcripts/scripts/tests/` import another test module by a BARE name (`test_teams_chat_tenant`), so `python -m pytest <file>` run on one of them ALONE from the repo root fails to collect (`ModuleNotFoundError: No module named 'test_teams_chat_tenant'`): `test_teams_chat_jobs.py`, `test_teams_chat_eod_republish.py`, `test_teams_chat_stale_eod.py`. Round 19's cell CA-k-3 repaired the same defect in a fourth sibling, `test_teams_chat_natural.py`. You repair these three the same way, and change nothing else.

### THE FIX (look at commit `8454482177` for the shape)

In each of the three files, put the tests directory on `sys.path` BEFORE the sibling import: add `import os` and `import sys` if absent, then `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))`, and mark the sibling import line `# noqa: E402`. Keep every test function, name and assertion exactly as it is.

### THE CONTRACT

Your interface is the header of `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m3_batch.py` (in your worktree at HEAD; READ it, do not edit it). Its arms: each of the three files passes pytest ALONE from the repo root; the five siblings (`tenant`, `natural`, and these three) pass together in ONE run; no `def test_` name is lost from any of the three; and nothing under `data/` (except the three files), `infra/` or `.tools/` differs from the merge-base with the trunk.

### RULES

- Edit nothing but the files in `<paths>`. No non-ASCII. Do NOT edit any product file: if a test cannot pass without a product change, STOP and report the refusal with its measurement.
- Refuse a criterion you cannot satisfy as written and report the refusal; do not repair or widen it. Do not add, delete or weaken a test.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAl3-AC1" cell_refs="CA-l-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m3_batch.py"</invocation><expect>M3-BATCH ok=True arms=6 of 6</expect></criterion>
`CAl3-AC1` -- the issuer's check: each of the three files collects and passes alone from the repo root (14, 12 and 14 tests on the issuer's reference), the five siblings pass in one run (112), no test name is lost, and no product file changed. It prints 2 of 6 at the base (the three `alone` arms and `combined` fail).

<criterion id="CAl3-AC2" cell_refs="CA-l-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAl3-AC2` -- the bound, a control that PASSES at the base (64 passed): the assistant's flow tests.

<criterion id="CAl3-AC3" cell_refs="CA-l-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k2_reader.py"</invocation><expect>K2-READER ok=True arms=7 of 7</expect></criterion>
`CAl3-AC3` -- the bound, a control that PASSES at the base (7 of 7): the reader's six sources. (AMENDED 2026-10-15 by the issuer: this criterion first named round 19's `check_l3_batch.py`, whose `no_product_change` arm allows only that cell's four files and so grades the three files THIS cell must edit as stray changes; a control that cannot pass was the issuer's defect, found by worker ~31, which refused it and filed COMM_ASSIST-W31-S1.)
</proof_of_spec>

<expected_criteria>CAl3-AC1,CAl3-AC2,CAl3-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 280`. Commit the edits FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~31/COMM_ASSIST.TO-CA-l-3.batch-three-sibling-bare-imports.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~29/COMM_ASSIST.TO-CA-k-3.batch-repair-stale-tests-and-reader-text.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it. Flip `<status>` to `complete` only when all three pass. Validate with the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAl3-AC1,CAl3-AC2,CAl3-AC3`; its LAST line must be `VALID (rc=0)` at the final head. Your final report names each changed line and the pass count of each test file. Your surprise rows are `COMM_ASSIST-W31-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial; write the commit message file with your Write tool (never a shell heredoc), ending with the attribution line the harness gives you.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round20.md</decomp_doc>
<owned_cells>CA-l-3</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/tests/test_teams_chat_jobs.py
data/transcripts/scripts/tests/test_teams_chat_eod_republish.py
data/transcripts/scripts/tests/test_teams_chat_stale_eod.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-l-3.batch-three-sibling-bare-imports.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~31/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made.
comp-adversary: RUN -- a test "repaired" by deleting or weakening it (refused: AC1 `names` compares each file's `def test_` set with the base; the control that renames one test fails that arm); a repair that edits product code (refused: AC1 `no_product_change`); a repair that breaks a sibling (refused: AC1 `combined`, 112 together; AC2; AC3); a path hack that makes one file pass alone and break the combined run (refused: `combined`). BLIND: the `no_product_change` arm bites only in a worker's worktree (against the merge-base with the trunk); in the trunk checkout it passes trivially.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAl3-AC1 base: FAIL as measured (2 of 6; `alone:test_teams_chat_jobs`, `alone:test_teams_chat_eod_republish`, `alone:test_teams_chat_stale_eod` and `combined` fail with `ModuleNotFoundError: No module named 'test_teams_chat_tenant'`); green arm 5 of 5 against a scratch reference in a non-git mirror (since removed; `no_product_change` is skipped there and bites in a worktree), negative control (a renamed test) fails `names`. CAl3-AC2 base: PASS as measured (control, 64 passed). CAl3-AC3 base: PASS as measured (control, K2-READER arms=7 of 7).
Source: CTO round-19 analysis ruling 4 (`ledger/ROUND_ANALYSIS.round19.md` @b4f6d499d0, msg 109356); issuer ruling W19-S5 and the round-19 packet's enrichment item 4; commit `8454482177` as the shape.
