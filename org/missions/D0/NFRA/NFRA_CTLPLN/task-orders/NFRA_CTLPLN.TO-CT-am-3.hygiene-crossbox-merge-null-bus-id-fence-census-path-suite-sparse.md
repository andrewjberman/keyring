# TO NFRA_CTLPLN.TO-CT-am-3 -- workstream BATCH round 11 (cell CT-am-3): HYGIENE batch B -- `crossbox-call.py merge` keeps a null bus id and writes nothing when it refuses (S9121); the crossbox suite passes in a sparse worktree (W79-S2)

<to_id>NFRA_CTLPLN.TO-CT-am-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~125</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-am-3` (`decompositions/NFRA_CTLPLN_DECOMP.round23.md`) | **outcome_ref:** hygiene |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two items of the CTO's round-22 hygiene batch (the second of two cells; ruling 4's kept-open rows and enrichment item 4). `W8-S7` (the fence census writing its own baseline) is NOT in this cell: the census lives under `infra/aws/terraform/shared-infra/tests/`, an infra path, which the evidence law classes WORLD; it is carried to its own cell with research. Read rows `NFRA_CTLPLN-S9121` and `W79-S2` (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/remediations/REMEDIATION_v1.md` to `REMEDIATION_v6.md`; the remedy and done-when are in the row) and the CVO's note in `surprise-channel/adjudications/ADJUDICATION_v27.md` (W79-S2's done-when: the crossbox suite passes on two boxes whose origin refs differ; at the cut `python .tools/tests/test_crossbox_call.py` reads `CROSSBOX-TEST cases=71/71 ok=True` in the main tree and one case fails in a SPARSE worktree). Facts: `.tools/crossbox-call.py merge` drops a null `bus_message_id` from the receiving box's ack, then its own validator refuses the result AFTER the sending box's copy was rewritten, so a refused merge leaves a written, invalid ack (S9121).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **S9121:** in `.tools/crossbox-call.py`, `merge` keeps a null `bus_message_id` as the schema allows, and when the merged result fails validation it writes NOTHING (validate the whole result in memory before any file is rewritten). Add cases to the tool's selftest (a fixture ack with a null bus id merges; a fixture that fails validation leaves both copies byte-identical).
2. **W79-S2:** find the one case of `.tools/tests/test_crossbox_call.py` that fails in a SPARSE worktree (cut one with `.tools/wk-provision.sh provision NFRA_CTLPLN 125 --path <a temporary folder outside C:/Users/AndrewBerman/Desktop/ajb_wk/> --order <this order file>`, run the suite there, read the failing case) and make the suite independent of live origin state and of the sparse set (the case must set up what it needs inside its own temporary repository or skip with a printed reason that names the missing folder; never pass by weakening an assertion). Remove that provisioned worktree and its branch in a `finally`.
3. A NEW test `.tools/tests/test_round23_hygiene_b.py` with flags `--merge` (`HYGIENE-MERGE arms=<k>/<n> ok=<True|False>`) and `--sparse` (cuts the temporary sparse worktree as above, runs `.tools/tests/test_crossbox_call.py` in it and prints `HYGIENE-SPARSE crossbox_cases=<pass>/<total> ok=<True|False>`; `ok` needs every case passing or skipping with a printed reason, none failing). Last lines as shown.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~125/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W125-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. If a path in `<paths>` does not exist, STOP and file a BLOCKING row naming the file you found; the issuer re-points the grant.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTam3-AC1" cell_refs="CT-am-3"><invocation>python .tools/tests/test_round23_hygiene_b.py --merge</invocation><expect>ok=True</expect></criterion>
`CTam3-AC1` -- a null bus id merges and a refused merge writes nothing (base: the test does not exist); report the whole line.

<criterion id="CTam3-AC2" cell_refs="CT-am-3"><invocation>python .tools/tests/test_round23_hygiene_b.py --sparse</invocation><expect>ok=True</expect></criterion>
`CTam3-AC2` -- the crossbox suite has no failing case in a sparse worktree (base: one case fails there; the main tree reads 71/71); report the whole line.
</proof_of_spec>

<expected_criteria>CTam3-AC1,CTam3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~125/NFRA_CTLPLN.TO-CT-am-3.hygiene-crossbox-merge-null-bus-id-fence-census-path-suite-sparse.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTam3-AC1,CTam3-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round23.md</decomp_doc>
<owned_cells>CT-am-3</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-call.py
.tools/tests/test_crossbox_call.py
.tools/tests/test_round23_hygiene_b.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; no read of any Dell.
comp-adversary: RUN -- the merge rewriting a copy before validating (the byte-identity arm); the null bus id accepted where the schema forbids it (read the schema first); the sparse fix passing by weakening an assertion (diff the case before and after in your report); a provisioned sparse worktree left behind (the finally; list `git worktree list` before and after); BLIND: `W8-S7` (the fence census, an infra path) is not touched here.
risk: LOCAL -- a cross-box tool and test helpers changed and tested in temporary repositories; no existing crossbox file in `org/devices/crossbox/` is touched.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/crossbox-call.py` is NFRA_CTLPLN's cross-box call tool; the CTO ruled the batch (round-22 analysis ruling 4 and enrichment item 4).
</preflight>

Base checks, dry-run by the issuer before the cut: CTam3-AC1 and AC2 FAIL as expected (the test does not exist). Controls: `CROSSBOX-SELFTEST cases=35/35 ok=True`, `CROSSBOX-TEST cases=71/71 ok=True` in the main tree.
Source: CTO round-22 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round22.md` @1d8ee95b78); hygiene.
