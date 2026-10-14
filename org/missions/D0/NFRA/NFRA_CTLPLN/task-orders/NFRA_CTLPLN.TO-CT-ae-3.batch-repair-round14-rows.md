# TO NFRA_CTLPLN.TO-CT-ae-3 -- workstream BATCH round 3 (cell CT-ae-3): the round-14 batch repair -- one roots rule for fork and act rows in files mode, an ENFORCE refusal unstages everything it staged, the checkpoint ignore rule, stale simulator comments in the identity root

<to_id>NFRA_CTLPLN.TO-CT-ae-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~99</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ae-3` (`decompositions/NFRA_CTLPLN_DECOMP.round15.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Four small defects from round 14, repaired in ONE cell. Each is INERT today. Read the named row or note first (Grep the id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`).

1. **Files-mode equality (CTO round-14 ruling 3; the `CT-ad-5` close note).** `.tools/crossbox-deploy-check.py` `measure_open_call` (about :189-260). In FILES MODE (`narrow`: a non-Terraform root with carried files) the loop over open-calls rows applies `roots_field_hit` to an `act` row but skips it for a `fork` row (`if not narrow`), so a roots-named `fork` row does not match through its own `roots` field there while a roots-named `act` row does. Make them equal: in files mode a row of ANY kind also matches through `roots_field_hit(row, rel)`. Everything else is unchanged: the `act` rule of `CT-ad-5` (an act row matches ONLY through its roots), the Terraform-root behaviour, closed rows ignored, the crossbox call FILES loop, the `calls_scanned` denominator. Update the module docstring sentence about files mode.
2. **`W93-S1`.** `.tools/safe-commit.sh`, the naming stage (about :1052-1115 plus the unstage in its ENFORCE refusal path): an ENFORCE refusal of the stage unstages only the eight graded extensions it graded, so a non-graded file staged beside them (for example the project `.md` deliverable) stays in the index after the refusal. Make the ENFORCE refusal unstage EVERY file this call staged (every path in `IN_SCOPE`), like the other refusing stages of the script do. WARN mode is unchanged: the stage still never changes the script's exit code there.
3. **`W95-S1`.** `infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py --check-fresh` writes `reached_roles_census.fresh_checkpoint.json` next to the saved census; no ignore rule covers it, so a stray checkpoint could be staged. Add ONE ignore rule for that file name to `infra/.gitignore` (read the file's existing layout and follow its style; do not reorder or remove any rule). Verify with `git check-ignore -v` on a path of that name under the tests folder.
4. **The `routes.tf` follow-up.** Round 14's `CT-ad-1` reworded the two `routes.tf` comments that named the deleted `simulate_policy.py`. Search the identity root `infra/aws/terraform/nfra-ctlpln-identity/` (all file types; Grep tool) for any OTHER comment or docstring that still names `simulate_policy` or says a deleted test reads or gates something, and reword each the same way (comment or docstring text only). A mention that is CODE (an import, a call, a path read) is NOT yours to change: report it by file and line. If the search finds nothing more, say so with the files searched.

### BUILD

5. A NEW test `.tools/tests/test_round15_batch.py` (standard library, temporary directories only, no AWS, no network) with arms: (1) in files mode a roots-named `fork` row matches (`matched=1`), a no-roots `fork` row against the same non-Terraform root does not match through its project alone when the files do not name it (keep the existing text/project behaviour for fork rows exactly as the base prints for the same fixture; compare against the base by importing `git show HEAD:.tools/crossbox-deploy-check.py` from a temporary file), an `act` row with no roots still matches nothing; (2) the naming stage extracted from `safe-commit.sh` the way `.tools/tests/test_safe_commit_derivation.py` does it, in a temporary repository with ENFORCE on and a stub gate that refuses: after the refusal the staged `.md` AND the graded `.json` are both unstaged; with WARN the exit code is unchanged and both stay staged; (3) `git check-ignore` reports the checkpoint name ignored by `infra/.gitignore` and a neighbour name (`reached_roles_census.json`) NOT ignored; (4) a text search of the identity root's comments and docstrings reports no remaining `simulate_policy` mention outside code. Final line `ROUND15-BATCH arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. The identity-root edits are comment and docstring text only (a `git diff` of those files shows only comment lines; anything else is a finding). Cell 2 edits the commit path every seat uses: run the naming gate with its LIVE LIMB SWITCHED OFF in every experiment (the way `.tools/tests/test_safe_commit_derivation.py` does), and make no AWS call. No aws, no network, no push, no `terraform` command. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W99-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTae3-AC1" cell_refs="CT-ae-3"><invocation>python .tools/tests/test_round15_batch.py</invocation><expect>ok=True</expect></criterion>
`CTae3-AC1` -- every arm of the batch test passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTae3-AC2" cell_refs="CT-ae-3"><invocation>python .tools/tests/test_open_call_act_roots.py</invocation><expect>ok=True</expect></criterion>
`CTae3-AC2` -- the act-row suite still passes after item 1 (base: `OPEN-CALL-ACT-ROOTS arms=8/8 ok=True`, a control); report the whole last line. If an arm of that file asserted the old files-mode fork behaviour, update it in this cell and name the arm.

<criterion id="CTae3-AC3" cell_refs="CT-ae-3"><invocation>python .tools/tests/test_safe_commit_derivation.py</invocation><expect>ok=True</expect></criterion>
`CTae3-AC3` -- the derivation suite still passes after item 2 (base: `SAFE-COMMIT-DERIVATION cases=17/17 ok=True`, a control, about 52 seconds); report the whole last line.
</proof_of_spec>

<expected_criteria>CTae3-AC1,CTae3-AC2,CTae3-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 300`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~99/NFRA_CTLPLN.TO-CT-ae-3.batch-repair-round14-rows.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTae3-AC1,CTae3-AC2,CTae3-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round15.md</decomp_doc>
<owned_cells>CT-ae-3</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-deploy-check.py
.tools/tests/test_open_call_act_roots.py
.tools/safe-commit.sh
.tools/tests/test_safe_commit_derivation.py
infra/.gitignore
infra/aws/terraform/nfra-ctlpln-identity/
.tools/tests/test_round15_batch.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the identity-root edits are comment text and nothing is applied.
comp-adversary: RUN -- the act rule of CT-ad-5 weakened by the equality edit (CTae3-AC2 and arm 1 keep it); an ENFORCE refusal that now unstages a file it did not stage (arm 2 stages only the call's own paths); a WARN-mode exit code changed (arm 2 checks it); the ignore rule ignoring the census itself (arm 3 checks the neighbour); a comment edit that changes code (the diff rule); BLIND: a second `.gitignore` deeper in the tests folder that overrides the new rule (the worker runs `git check-ignore -v` and reports the matching file).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths (the identity root, infra/.gitignore); this cell makes no AWS call and applies nothing.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/safe-commit.sh` is on every seat's commit path.
</preflight>

Base checks, dry-run by the issuer before the cut: CTae3-AC1 base: FAIL as expected (the file does not exist); CTae3-AC2 and CTae3-AC3 base: see the issuer's dry-run note in the issuance commit.
Source: CTO round-14 analysis section 3 rulings 3-5 and section 4 item 3 (`ledger/ROUND_ANALYSIS.round14.md` @affd2fab43); rows W93-S1, W95-S1; the `CT-ad-5` close note.
