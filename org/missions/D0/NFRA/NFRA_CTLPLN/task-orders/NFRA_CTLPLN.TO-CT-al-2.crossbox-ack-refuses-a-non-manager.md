# TO NFRA_CTLPLN.TO-CT-al-2 -- workstream OUTCOME round 13 (cell CT-al-2): FWD-3 -- `crossbox-call.py ack` refuses any serial that is not the receiving box's MSTR lane, with one non-manager ack refused and one manager ack admitted

<to_id>NFRA_CTLPLN.TO-CT-al-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~120</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-al-2` (`decompositions/NFRA_CTLPLN_DECOMP.round22.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD v0.31 FWD-3 (`prd/NFRA_CTLPLN_PRD.md` line 48 and the v0.31 addendum): box-to-box messages go fabric manager to fabric manager; the receiving manager acknowledges. CTO round-21 ruling 2: the managers are each box's `0.0.0_AB_MSTR` lane, and an acknowledgement by a CTO or CloudOps lane is not a manager acknowledgement. At the cut, today's matrix holds 8 acknowledgements by non-manager serials (`1.0.0_SA_CTO~DELL1`, `1.0.0_SA_CTO~Z`, `0.7.0_AE_CloudOps~CA2`). The tool is `.tools/crossbox-call.py` (subcommand `ack`; its `send-pending` already refuses any acting serial that is not a `0.0.0_AB_MSTR` serial or lane: read how it decides, and reuse that function). Its selftest `python .tools/crossbox-call.py --selftest` reads `CROSSBOX-SELFTEST cases=35/35 ok=True` at the cut.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. In `.tools/crossbox-call.py`, make `ack` REFUSE (non-zero exit, nothing written, a message that names the rule and the right serial) when the acting serial is not the receiving box's manager: a `0.0.0_AB_MSTR` serial or lane whose box equals the file's `to_device` (base `0.0.0_AB_MSTR` is the laptop's manager; `~Z` is site Z's, `~DELL1` dell1's, `~DELL2` dell2's: derive the mapping from `org/devices/DEVICES.json` and the existing aliases, never type a box list). Everything else about `ack` stays as it is.
2. Add cases to the tool's own selftest for the refusal and the admission (so the selftest count grows from 35).
3. A NEW test `.tools/tests/test_round22_manager_ack.py` (standard library; a temporary repository with a temporary crossbox folder; no network): arms (a) a CTO serial of the receiving box acks: REFUSED, file unchanged; (b) a CloudOps serial: REFUSED; (c) the receiving box's manager acks: ADMITTED, file shows the ack; (d) the SENDING box's manager acks: REFUSED (wrong box); (e) the base laptop manager acks a call to the laptop: ADMITTED. Last line `MANAGER-ACK arms=<k>/<n> ok=<True|False>`.
4. Do not touch any existing crossbox file in `org/devices/crossbox/`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~120/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W120-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTal2-AC1" cell_refs="CT-al-2"><invocation>python .tools/tests/test_round22_manager_ack.py</invocation><expect>ok=True</expect></criterion>
`CTal2-AC1` -- a non-manager ack is refused and a manager ack is admitted, per box (base: the test does not exist); report the whole last line.

<criterion id="CTal2-AC2" cell_refs="CT-al-2"><invocation>python .tools/crossbox-call.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTal2-AC2` -- the tool's own selftest passes with the new cases (base: `CROSSBOX-SELFTEST cases=35/35 ok=True`; the count must grow); report the whole last line.

<criterion id="CTal2-AC3" cell_refs="CT-al-2"><invocation>python .tools/crossbox-matrix.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTal2-AC3` -- the matrix reader still passes its own selftest (base: record its last line in your report first; a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTal2-AC1,CTal2-AC2,CTal2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~120/NFRA_CTLPLN.TO-CT-al-2.crossbox-ack-refuses-a-non-manager.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTal2-AC1,CTal2-AC2,CTal2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round22.md</decomp_doc>
<owned_cells>CT-al-2</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-call.py
.tools/tests/test_round22_manager_ack.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network.
comp-adversary: RUN -- the refusal blocking the manager's own ack (arms c and e); the refusal trusting a typed box list (the mapping is derived from the register); the refusal reaching `receive`, `close` or `send-pending` (their behaviour must not change: run the selftest); a CTO of the receiving box being refused where the ruling intends it (arm a); every box's CTOs ack through this tool today, so after the merge their acks are refused and the managers must ack: that is the CTO's ruling, the cell does not soften it; BLIND: acks already recorded in `org/devices/crossbox/` by non-managers are not rewritten (the CVO re-reads them).
risk: LOCAL -- a cross-box tool changed and tested in a temporary repository; no existing crossbox file is touched.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/crossbox-call.py` is NFRA_CTLPLN's cross-box call tool (C-TRUNK/crossbox cells t-2, w-6, y-1); the CTO ruled this change (round-21 analysis ruling 2).
</preflight>

Base checks, dry-run by the issuer before the cut: CTal2-AC1 FAIL as expected (the file does not exist); CTal2-AC2 base `CROSSBOX-SELFTEST cases=35/35 ok=True` (the criterion passes at the base on the substring; the new cases are the proof, report the count); CTal2-AC3 base to be recorded by the worker.
Source: CTO round-21 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round21.md` @a558191b7c), msg 109483; FWD-3.
