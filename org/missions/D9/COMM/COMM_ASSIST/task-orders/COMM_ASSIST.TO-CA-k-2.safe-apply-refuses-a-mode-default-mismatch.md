# TO COMM_ASSIST.TO-CA-k-2 -- round 19 CA-k-2: safe-apply refuses a module.ldo_001 apply when the trunk's mode default differs from the live INGRESS_MARK_MODE

<to_id>COMM_ASSIST.TO-CA-k-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~28</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-k-2` (`decompositions/COMM_ASSIST_DECOMP.round19.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none (CTO round-18 analysis ruling 3, msg 109267; PRD v0.10 ADMITTED)

---

## WORKER FACE

### THE CELL

The assistant's mark mode (`INGRESS_MARK_MODE`, `off`/`record`/`enforce`) is set in Terraform by the variable `chat_assist_ingress_mark_mode` in `infra/aws/terraform/transcripts/chat_assist.tf`. Two seats apply `module.ldo_001`: this project and NFRA_CTLPLN. If the trunk's default ever differs from what is live, the next apply by either seat silently flips the mode (the mark's enforcement) with no one having decided it. You add a GATE, not an alert: before a `safe-apply` that covers `module.ldo_001`, compare the trunk's default with the live value and REFUSE the apply on a difference. It reads one value and builds no notification, no scheduler and no AWS resource.

### THE CONTRACT (fixed by the issuer; the issuer's check pins every point)

Your whole interface is the header docstring of `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l2_gate.py` (it is in your worktree at HEAD; READ it first and do not edit it). In short:

1. A NEW script `.tools/ldo001-mode-default-check.py [--tf PATH] [--live-json PATH]`. Its LAST stdout line is `LDO001-MODE verdict=<OK|REFUSED|NO-VERDICT> default=<v> live=<v>`; exit 0 only for OK. The default is read from the variable `chat_assist_ingress_mark_mode` in the `.tf`. The live value is `INGRESS_MARK_MODE` of the handler and the ingress Lambda functions, read-only (`lambda get-function-configuration` through the `.tools/aws` shim; resolve the function names from the module, do not invent them). `--live-json` is the test seam: a JSON file holding a dict or a list of dicts each shaped like that call's output. Equal everywhere is OK; a difference (default against live, or between the two functions) is REFUSED; anything unreadable (file, JSON, key, variable, default, the AWS call) is NO-VERDICT, which also refuses.
2. ONE block in `.tools/safe-apply.sh`, placed BEFORE the seat-gates block: when the apply covers `module.ldo_001` (a `-target` of `module.ldo_001` or below, written `-target=X` or `-target X`, after the `apply` word; or no `-target` and the `-chdir` tree declares `module "ldo_001"`), run the script with `--tf <tree>/chat_assist.tf`, print `safe-apply: [ldo001-mode] <its last line>` to stderr, and on a non-zero result exit 10 with `BLOCKED` on stderr, terraform never called. `LDO001_MODE_OVERRIDE="reason"` lets the apply go on and writes ONE audit line naming `LDO001_MODE_OVERRIDE`, the actor and the reason to the same override audit file the seat gates use. `LDO001_MODE_LIVE_JSON` is the seam that feeds the live JSON to the script from the environment. `SAFE_LDO001_MODE_CHECK_ONLY=1` makes a covered apply exit 0 right after the check. An apply that does NOT cover the module runs nothing of this and prints no `[ldo001-mode]` line.
3. Exit code 10 is new (2 to 9 are taken). Follow the shape of the existing blocks in that file; change nothing else in it.

### HAZARDS (measured by the issuer before the cut)

- `.tools/safe-apply.sh` is edited by other projects' workers (NFRA_CTLPLN, NFRA_MCPMSP, LGIC_BLANKFIX). Start from the HEAD file in your worktree and insert only this one block, so a later merge is a clean add.
- Every safe-apply arm in the issuer's check passes `--dry-seat-gates`; without it a run proceeds into the halt gate and the naming plan and takes minutes. Run your own safe-apply trials the same way and never run a real `terraform`.
- The check cleans up the audit file `org/git-author-override-audit.l2chk.log`; use that device name in your own trials too, so no stray audit file is left.
- Do NOT run `safe-apply` against the real tree for an apply. The live read inside the script is read-only and fine to run once, to see `verdict=OK` against the real file.

### RULES

- Edit nothing but the files in `<paths>`. No non-ASCII.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAk2-AC1" cell_refs="CA-k-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l2_gate.py"</invocation><expect>L2-GATE ok=True arms=13 of 13</expect></criterion>
`CAk2-AC1` -- the issuer's check (read it; do not edit it): the script's verdicts on a match, a mismatch, an unreadable live value and an unparsable default; the hook refuses a covered mismatch before terraform is reached, lets a covered match through, never runs on an apply that does not cover the module, and the override applies and writes its audit line. It prints 2 of 13 at the base (only the two never-runs arms hold, trivially).

<criterion id="CAk2-AC2" cell_refs="CA-k-2"><invocation>bash .tools/tests/test_safe_apply_scoped_gates.sh</invocation><expect>RESULT: PASS</expect></criterion>
`CAk2-AC2` -- the bound, a control that PASSES at the base: the scoped-apply gate tests.

<criterion id="CAk2-AC3" cell_refs="CA-k-2"><invocation>python .tools/tests/test_apply_who_and_crossbox.py</invocation><expect>APPLY-GATES-TEST cases=100/100 ok=True</expect></criterion>
`CAk2-AC3` -- the bound, a control that PASSES at the base: the seat gates' 100 cases.
</proof_of_spec>

<expected_criteria>CAk2-AC1,CAk2-AC2,CAk2-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 280`: the issuer's check finds the repository from the current directory, so running it by an absolute path to the shared tree would test the trunk and not your work. Commit the script and the hook FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~28/COMM_ASSIST.TO-CA-k-2.safe-apply-refuses-a-mode-default-mismatch.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~24/COMM_ASSIST.TO-CA-j-12.assistant-keeps-mention-and-mail-records.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAk2-AC1,CAk2-AC2,CAk2-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the exit code and the seam names, the one live read you made, and the passed/failed count of every test you ran. Your surprise rows are `COMM_ASSIST-W28-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round19.md</decomp_doc>
<owned_cells>CA-k-2</owned_cells>
</decomp_ref>

<paths>
.tools/ldo001-mode-default-check.py
.tools/safe-apply.sh
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-k-2.safe-apply-refuses-a-mode-default-mismatch.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~28/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the gate runs inside an apply someone starts.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the live read (`lambda get-function-configuration`) is a read the applying seat's identity already makes (the issuer's own `check_j5_live` reads the same call).
comp-adversary: RUN -- the check running on every apply and slowing or blocking unrelated work (refused: AC1 never-runs arms; that negative control reads 11 of 13); an unreadable live value read as a match (refused: AC1 `live-unreadable-no-verdict`, `tf-unparsable-no-verdict`, `apply-with-no-verdict-blocks`; the OK-on-unreadable controls read 10 of 13 and 12 of 13); a gate that cannot be passed when the mismatch is intended (refused: the audited override, AC1 override arm); the existing gates moving (refused: AC2 and AC3). BLIND: the real Lambda environment is read once by the issuer after the merge (a match reads `verdict=OK default=enforce live=enforce` today); a real apply through the hook is not exercised here, because an apply is the thing the gate protects.
naming: the new file `.tools/ldo001-mode-default-check.py` is a tool file, not a pipeline name (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1). The CTO ruled the shape (ROUND_ANALYSIS.round18 ruling 3: a gate, not an alert).
</preflight>

Base: CAk2-AC1 base: FAIL as expected (2 of 13). CAk2-AC2 base: PASS as expected (control, `RESULT: PASS`). CAk2-AC3 base: PASS as expected (control, 100/100). AC1 green arm: PASS as expected (13 of 13) against a scratch reference in a throwaway worktree (since removed), whose script also read the live value: `LDO001-MODE verdict=OK default=enforce live=enforce`; the existing `test_safe_apply_targeted.sh` stayed PASS there.
Source: CTO round-18 analysis ruling 3 (`ledger/ROUND_ANALYSIS.round18.md` @5e4395ae5c, msg 109267); the standing second-writer hazard recorded in CTO call C2 of the R18D half; `.tools/safe-apply.sh` (the seat-gates block and `SAFE_NAMED_COMMIT_CHECK_ONLY` as the seam pattern).
