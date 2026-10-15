# TO COMM_ASSIST.TO-CA-k-3 -- round 19 CA-k-3: ONE batch repair -- the stale mail test arms, one test import, and two reader texts; no product change

<to_id>COMM_ASSIST.TO-CA-k-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~29</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-k-3` (`decompositions/COMM_ASSIST_DECOMP.round19.md`) | **outcome_ref:** none (hygiene: CTO round-18 analysis ruling 4; no outcome of its own) |
**depends_on:** CA-k-1 MERGED. This order is STAGED: it edits `test_inbound_mail_draft.py` and `refresh.py`, which CA-k-1 also edits. The issuer flips it to `pending` and cuts the worktree from the trunk AFTER the CA-k-1 merge.

---

## WORKER FACE

### THE CELL

Five pieces of hygiene, repaired together, with NO behaviour change: the product code is not touched. Only test files and two text lines of the reader change.

(a) **CA-j-18, the stale mail test arms.** `data/transcripts/scripts/tests/test_inbound_mail.py` prints `cases=11/15`. Four cases use invented firm keys (`invented-firm`, `invented-house`, `second-firm`) in the party registry, but `firm_domains` now returns only the `FIVE_PARTIES` keys, so it returns `{}` for them. Repair the TEST so those cases register their invented parties the way the code now reads them (for example widen `mail_requests.FIVE_PARTIES` per case inside the test with a context manager or decorator that restores it), never by editing the code. `data/transcripts/scripts/tests/test_inbound_mail_draft.py`: the arm `client_no_request` expects the text to end `Reply #dev [notes] to open a job / 0 drop`; the text now ends `... notes to redraft / 0 drop / #dev [notes] to open a job`. Make the assertion state the current, correct tail.
(b) **W19-S5.** `data/transcripts/scripts/tests/test_teams_chat_natural.py` imports a sibling test module by a bare name, so pytest run on it ALONE from the repo root fails to collect. Make it import the way the passing sibling tests do (for example put the tests directory on `sys.path` first), so it passes alone from the repo root and still passes in one run with `test_teams_chat_tenant.py`.
(c) **W25-S3.** `data/transcripts/scripts/muse_reader/refresh.py`: the CLI help text says "the four files" although the reader writes six sources, and every table scan logs `READ drafts` whatever source it read. Make the help name the sources from `refresh.SOURCES` and make the scan log line name the source actually read (for example `SCAN table=...`). The data written to the folder must stay byte-identical.

### THE CONTRACT

Your interface is the header of `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l3_batch.py` (in your worktree at HEAD; READ it first, do not edit it). Its arms: `mail_cases`, `mail_draft_arms`, `natural_alone`, `natural_in_set`, `help_sources`, `scan_log_truth`, `refresh_same` and `no_product_change`. The last two bite in your worktree: against the merge-base with the trunk, nothing under `data/`, `infra/` or `.tools/` may change except the four allowed files (the three test files and `refresh.py`), and `refresh.py` must write a byte-identical folder on a fixed stub.

### RULES

- Edit nothing but the files in `<paths>`. No non-ASCII. Do NOT edit `mail_requests.py`, `tenant.py` or any other product file: if a test cannot pass without a product change, STOP and report the refusal with its measurement.
- Refuse a criterion you cannot satisfy as written and report the refusal; do not repair or widen it.
- Three other tests (`test_teams_chat_jobs.py`, `test_teams_chat_eod_republish.py`, `test_teams_chat_stale_eod.py`) have the same bare-import defect. They are NOT in this cell; leave them.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAk3-AC1" cell_refs="CA-k-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l3_batch.py"</invocation><expect>L3-BATCH ok=True arms=8 of 8</expect></criterion>
`CAk3-AC1` -- the issuer's check: the two mail test scripts print every case passing; the natural test passes alone from the repo root and in one run with the tenant test; the help names the six sources and not "four"; a scan of a non-drafts source never logs `READ drafts`; the reader writes the same bytes; nothing else changed. It prints 2 of 8 at the base in the trunk checkout (six arms fail; the last two pass trivially there).

<criterion id="CAk3-AC2" cell_refs="CA-k-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAk3-AC2` -- the bound, a control that PASSES at the base: the assistant's flow tests.

<criterion id="CAk3-AC3" cell_refs="CA-k-3"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k2_reader.py"</invocation><expect>K2-READER ok=True arms=7 of 7</expect></criterion>
`CAk3-AC3` -- the bound, a control that PASSES at the base: the reader's six sources.
</proof_of_spec>

<expected_criteria>CAk3-AC1,CAk3-AC2,CAk3-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 250`: the issuer's checks find the repository from the current directory, so running one by an absolute path to the shared tree would test the trunk and not your work. Commit the edits FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~29/COMM_ASSIST.TO-CA-k-3.batch-repair-stale-tests-and-reader-text.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~24/COMM_ASSIST.TO-CA-j-12.assistant-keeps-mention-and-mail-records.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAk3-AC1,CAk3-AC2,CAk3-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names each changed line and the passed/failed count of every test file you ran. Your surprise rows are `COMM_ASSIST-W29-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round19.md</decomp_doc>
<owned_cells>CA-k-3</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/tests/test_inbound_mail.py
data/transcripts/scripts/tests/test_inbound_mail_draft.py
data/transcripts/scripts/tests/test_teams_chat_natural.py
data/transcripts/scripts/muse_reader/refresh.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-k-3.batch-repair-stale-tests-and-reader-text.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~29/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made.
comp-adversary: RUN -- a test "repaired" by changing the product code to match it (refused: AC1 `no_product_change`; the control that edits `mail_requests.py` instead reads that arm FAIL); a reader that changes its output while only its text was to change (refused: AC1 `refresh_same`; a data change inside `refresh.py` fails that arm); a repair that hides a real defect by weakening an assertion to nothing (named: the issuer measured each stale assertion against the live code before the cut, so each is a stale expectation and not a defect: the party-registry cases read keys the code no longer accepts; the text tail moved when the reply menu was reordered); a repair that breaks the flow tests (refused: AC2 and AC3). BLIND: the arms that compare against the merge-base bite only in a worker's worktree; in the trunk checkout both pass trivially.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAk3-AC1 base: FAIL as expected in the trunk checkout (2 of 8; the six real arms fail). CAk3-AC2 base: PASS as expected (control, 64 passed). CAk3-AC3 base: PASS as expected (control, 7 of 7). AC1 green arm: PASS as expected (8 of 8) against a scratch reference in a throwaway worktree (since removed), with the flow set at 64 passed and 112 passed in the five-test pytest run.
Source: CTO round-18 analysis ruling 4 (`ledger/ROUND_ANALYSIS.round18.md` @5e4395ae5c, msg 109267); issuer rulings W19-S5, W24-S1..S3, W25-S3 (`deliverables/2.0.0_SA_COO~CA/r18/ISSUER_RULINGS.md`).
