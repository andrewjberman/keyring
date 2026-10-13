# TO NFRA_CTLPLN.TO-CT-ac-1 -- workstream BATCH round 1 (cell CT-ac-1): the round-12 batch repair -- crossbox merge, spawn pattern, schema guard, OPEN-CALL project field, crossbox suite, offline census check, simulator retired as a gate

<to_id>NFRA_CTLPLN.TO-CT-ac-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~87</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ac-1` (`decompositions/NFRA_CTLPLN_DECOMP.round13.md`) | **outcome_ref:** FWD-2, FWD-5, FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Seven small defects found in round 12, repaired in ONE cell. Each is INERT today. Read the named row first with the Grep tool (`"id": "<row id>"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`).

1. **`S9121`** -- `.tools/crossbox-call.py merge --id <id> --ref <ref>` folds the other box's copy of a crossbox file into this box's. When the receiving box's ack carries `bus_message_id: null` (the schema allows it), `merge` drops that key, then its own validator refuses the result AFTER the write, leaving a half-merged file. Fix: the merge carries the null `bus_message_id` as the schema allows, and a refusal writes NOTHING (validate the merged value first, write second).
2. **`W84-S1`** -- `.tools/spawn-agent.ps1` about :108 keeps the old serial-token pattern with a third segment `[A-Za-z0-9]+`, so it refuses a serial whose project segment has an underscore (`0.9.0_WK_NFRA_CTLPLN~78`). Widen that third segment to `[A-Za-z0-9_]+` (the first two segments and the `~lane` part unchanged), as `.tools/seat-boundary.ps1` and `.tools/kill-agent.ps1` already do.
3. **`W81-S1` leftovers** -- the box list is derived from the register (`org/devices/DEVICES.json` through `lib/devices.py`) in `to-pipeline-gate.py` and `box-status-report-check.py`, but still sits as a literal in `org/surprise_channel/schemas/investigation_item.schema.json` (about :30), `org/surprise_channel/schemas/remediation_row.schema.json` (about :32) and `org/standards/PRD_HEADER.schema.json` (about :20). A JSON schema cannot import. Add a GUARD in the new test (item 8): it fails when any of the three lists differs from `lib/devices.py placement_values()`; do not hand-edit a list to a different value. Also: the HELD dict in `.tools/tests/test_no_hand_listed_boxes.py` still names `to-pipeline-gate.py` (remove that entry; the census no longer lists it) and `.tools/missions-tree-index.py check` prints "(read by AST at run time)" for a derived symbol (make the wording say where the value came from).
4. **`W79-S1`, RULED by the CTO** (round-12 analysis section 2) -- in `.tools/crossbox-deploy-check.py`, the OPEN-CALL arm never matches a bare token in a call's free text (subject or context). It matches (a) the call's structured `project` field against the deploy's project, and (b) a Terraform root by its path or by the call's `roots` field. Case 943 in `.tools/tests/test_apply_who_and_crossbox.py` changes so its project code rides in the `project` field, not the subject; every other case keeps its meaning.
5. **`W79-S2`** -- `.tools/tests/test_crossbox_call.py` reads `CROSSBOX-TEST cases=45/50 ok=False` at the base: five checks depend on whether the test repository's commits are on `origin` (the failures read "commit ... is not on origin yet" and "no CROSSBOX line found in the text given"). Make the suite 50/50 independent of origin state by giving each fixture repository a local origin it controls (temporary directories only). Do not weaken a refusal the tool makes in the real repository.
6. **`W85-S2`** -- `infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py` with no flag defaults to `--live` and makes read-only AWS calls. Make `--check` and `--write` default to the saved file (`--from-file tests/protected_functions_listing.json`) and require an explicit `--live` for the AWS read. Print which source was used on the first line.
7. **`simulate_policy.py` retired as a gate** (CTO ruling): in `infra/aws/terraform/nfra-ctlpln-identity/tests/`, `simulate_policy.py` is a decision-table simulator of Denies `CT-ab-1` removed. It is referenced by `render_routes_policy.py` and `derive_plan_reads.py` (search with the Grep tool for others). Remove every use of it as a PASS/FAIL gate in those files and in any check that prints `ok=` from it; keep the file only if a test still reads it as a fixture, and then say so in a comment at its top. The authority is each apply's live policy simulation, not these tables.

### BUILD

8. A NEW test `.tools/tests/test_round13_batch.py` (standard library, temporary directories only, no AWS, no network) with one or more arms per item 1-7: (1) a merge carrying a null `bus_message_id` succeeds and a deliberately bad merge leaves the file byte-identical; (2) `spawn-agent.ps1`'s serial pattern accepts `0.9.0_WK_NFRA_CTLPLN~78` (read the pattern from the file and match it in Python); (3) the three schemas' box lists equal `lib/devices.py placement_values()` and the HELD entry is gone; (4) a call whose subject names a project but whose `project` field is another one does not match, a call whose `project` field matches does, a call naming a root by path matches, and a bare root name in free text does not; (5) nothing; (6) `derive_protected_functions.py --check` with no flag reads the saved file and makes no AWS call (run it with a stub `aws` first on PATH that records any call and fails the arm if it is called); (7) none of the three files gates on `simulate_policy`. Final line `ROUND13-BATCH arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws call (the stub on PATH records any), no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11; Windows PowerShell 5.1 syntax for the `.ps1`. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W87-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTac1-AC1" cell_refs="CT-ac-1"><invocation>python .tools/tests/test_crossbox_call.py</invocation><expect>ok=True</expect></criterion>
`CTac1-AC1` -- the crossbox suite reads 50 of 50 (base: `cases=45/50 ok=False`); report the whole last line.

<criterion id="CTac1-AC2" cell_refs="CT-ac-1"><invocation>python .tools/tests/test_round13_batch.py</invocation><expect>ok=True</expect></criterion>
`CTac1-AC2` -- every arm of the batch test passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTac1-AC3" cell_refs="CT-ac-1"><invocation>python .tools/tests/test_apply_who_and_crossbox.py</invocation><expect>ok=True</expect></criterion>
`CTac1-AC3` -- the apply-gates suite still passes after case 943 moves (base: `cases=100/100 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTac1-AC1,CTac1-AC2,CTac1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~87/NFRA_CTLPLN.TO-CT-ac-1.batch-repair-round12-rows.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTac1-AC1,CTac1-AC2,CTac1-AC3`. Also run, once, and report the last line of each: `python .tools/tests/test_box_lists_from_register.py`, `python .tools/tests/test_no_hand_listed_boxes.py`, `python .tools/missions-tree-index.py --self-test`, `python .tools/tests/test_fabric_readers_dell.py` (timeout 600), and `python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py --check`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round13.md</decomp_doc>
<owned_cells>CT-ac-1</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-call.py
.tools/tests/test_crossbox_call.py
.tools/spawn-agent.ps1
org/surprise_channel/schemas/investigation_item.schema.json
org/surprise_channel/schemas/remediation_row.schema.json
org/standards/PRD_HEADER.schema.json
.tools/tests/test_no_hand_listed_boxes.py
.tools/missions-tree-index.py
.tools/crossbox-deploy-check.py
.tools/tests/test_apply_who_and_crossbox.py
.tools/tests/test_round13_batch.py
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/render_routes_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_plan_reads.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call (a stub records any).
comp-adversary: RUN -- a merge that still writes before it validates (the byte-identical arm); a schema list hand-edited to match instead of guarded; a project match that still reads the subject; a test fixed by weakening a refusal in the real repository; a --check that still calls AWS (the stub arm); BLIND: a consumer of simulate_policy outside the two named files.
lane: the <paths> block IS the grant (worker RULING 1).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell makes no AWS call.
</preflight>

Base checks, dry-run by the issuer before the cut: CTac1-AC1 base: FAIL as expected (`CROSSBOX-TEST cases=45/50 ok=False`); CTac1-AC2 base: FAIL as expected (the file is absent); CTac1-AC3 base: PASS as expected (`APPLY-GATES-TEST cases=100/100 ok=True`).
Source: ROUND_ANALYSIS.round12.md section 2 and section 3 item 6; rows S9121, W84-S1, W81-S1, W79-S1, W79-S2, W85-S2.
