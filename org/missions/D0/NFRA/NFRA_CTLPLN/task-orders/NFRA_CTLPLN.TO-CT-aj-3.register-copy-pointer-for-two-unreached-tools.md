# TO NFRA_CTLPLN.TO-CT-aj-3 -- workstream OUTCOME round 8 (cell CT-aj-3): point the two unreached box-listing tests at a register copy, so the fixture-box read becomes 8 of 8 (FWD-2)

<to_id>NFRA_CTLPLN.TO-CT-aj-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~114</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in wk-NFRA_CTLPLN-114 @363731326b (merged at the drain): FWD2-BOX-ADDED tools=8/8 not_reached=0 named=8 ok=True; BOX-LISTS-FROM-REGISTER gate=derived status_report=derived ok=True; proof VALID. fabric_value_census.py exits 1 at the base (W114-S1, pre-existing); the reach rule ignores its exit code, declared in the proof.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aj-3` (`decompositions/NFRA_CTLPLN_DECOMP.round20.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-2 (`prd/NFRA_CTLPLN_PRD.md` line 41). Round 19's `.tools/tests/test_round19_register.py --fwd2` adds a fixture box `fixbox` to a copy of `org/devices/DEVICES.json` and requires each box-listing tool to name it: 6 of 8 listed tools were reached; two were not, because they cannot be pointed at a register copy: `.tools/tests/test_box_lists_from_register.py` (it prints PASS/FAIL arms, no box name) and `.tools/tests/fabric_value_census.py` (it reads no box list). Rows `NFRA_CTLPLN-W106-S6` and `S7`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. Give `.tools/tests/test_box_lists_from_register.py` a `--register <path>` option (default the real register) and make its output print the box names it read from that register in a line `BOXES-READ <names>`; keep its last line and exit code unchanged for the default run.
2. Give `.tools/tests/fabric_value_census.py` the same `--register <path>` option and make it print the box names its census compares against in a line `BOXES-READ <names>`. Read the file first: if it truly reads no box list, say so in the report and make the line print the register's box names it is given, so the fixture read can see them.
3. Update `.tools/tests/test_round19_register.py` so `--fwd2` points both at the temporary register copy and counts them as reached when `fixbox` appears in `BOXES-READ`. Last line must read `FWD2-BOX-ADDED tools=8/8 not_reached=0 named=8 ok=True`. The real register is never written; the real register's sha1 is compared before and after, as in the round-19 test.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~114/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W114-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaj3-AC1" cell_refs="CT-aj-3"><invocation>python .tools/tests/test_round19_register.py --fwd2</invocation><expect>tools=8/8</expect></criterion>
`CTaj3-AC1` -- all eight listed tools name the fixture box (base: `tools=6/8 not_reached=2`); report the whole last line.

<criterion id="CTaj3-AC2" cell_refs="CT-aj-3"><invocation>python .tools/tests/test_box_lists_from_register.py</invocation><expect>ok=True</expect></criterion>
`CTaj3-AC2` -- the default run of the register-derived box-list test still reads ok (base: `BOX-LISTS-FROM-REGISTER gate=derived status_report=derived ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaj3-AC1,CTaj3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~114/NFRA_CTLPLN.TO-CT-aj-3.register-copy-pointer-for-two-unreached-tools.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaj3-AC1,CTaj3-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round20.md</decomp_doc>
<owned_cells>CT-aj-3</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_box_lists_from_register.py
.tools/tests/fabric_value_census.py
.tools/tests/test_round19_register.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a default run changing its verdict (the control criterion); the option pointed at the real register by mistake and the test writing it (sha1 before and after); a tool reading the box list from somewhere other than the file given (the fixture box must appear in its output); BLIND: a real box added through the register is a qualified wait, none is in sight.
risk: LOCAL -- test files only.
lane: the <paths> block IS the grant (worker RULING 1). Three test files under `.tools/tests/`; no gate or hook is touched.
</preflight>

Base checks, dry-run by the issuer before the cut: CTaj3-AC1 FAIL as expected (`tools=6/8 not_reached=2` at the cut); CTaj3-AC2 base `BOX-LISTS-FROM-REGISTER gate=derived status_report=derived ok=True` (a control).
Source: CTO round-19 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round19.md` @2009d89478), msg 109424; FWD-2.
