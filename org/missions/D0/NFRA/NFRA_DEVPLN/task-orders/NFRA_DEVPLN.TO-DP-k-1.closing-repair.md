# TO NFRA_DEVPLN.TO-DP-k-1 -- round 9 ENRICHMENT DP-k-1: the closing repair -- the gate's `walk =git(` spacing and the closer-drive example's hard-coded project code

<to_id>NFRA_DEVPLN.TO-DP-k-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-k-1` (`decompositions/NFRA_DEVPLN_DECOMP.round9.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two one-line repairs to the output of an earlier order. Your worktree is a linked worktree of the workspace; the portal repo is not needed.

### BUILD

1. `.tools/portal-hooks/dev_push_payload_gate.py` line 162 reads `    walk =git(portal, "rev-list", "--first-parent", "--reverse", "%s..%s" % (remote, local))`. Put one space after the equals sign: `walk = git(`. Change nothing else on that line or in the file.
2. `.claude/skills/closer-drive/SKILL.md` step 5, line 35, reads `` `python .tools/open-calls.py approval-lease --project NFRA_DEVPLN --branch cand/<box>/<slug> --box <box> ``. This skill serves every project, so replace the hard-coded `NFRA_DEVPLN` with `<CODE>` (the phrase becomes `approval-lease --project <CODE> --branch cand/<box>/<slug> --box <box>`). Change nothing else in the file.

### RULES FOR THIS CELL

Edit with the Edit tool; keep each file's existing line endings (do not rewrite a whole file). Python standard library only; ruff clean on the Python file; no non-ASCII added. No push, merge or rebase. Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path. Run every command under `timeout 120` or less.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, next unused k after the highest `W1-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working. Copy the shape of an existing `W1-S` row in that file (`class` OBSERVATION or BLOCKING, `hazard_standing` ARMED or INERT, `disposition` UNDER_INVESTIGATION).

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPk1-AC1" cell_refs="DP-k-1"><invocation>grep -c "walk = git(" .tools/portal-hooks/dev_push_payload_gate.py</invocation><expect>^1$</expect></criterion>
`DPk1-AC1` -- the spacing repair (the count is 0 at the base).

<criterion id="DPk1-AC2" cell_refs="DP-k-1"><invocation>grep -c "approval-lease --project .CODE." .claude/skills/closer-drive/SKILL.md</invocation><expect>^1$</expect></criterion>
`DPk1-AC2` -- the example takes the project code as a placeholder (the count is 0 at the base).

<criterion id="DPk1-AC3" cell_refs="DP-k-1"><invocation>python .tools/tests/test_dev_push_payload_gate.py</invocation><expect>cases=21/21 ok=True</expect></criterion>
`DPk1-AC3` -- a third criterion, with its reason: the gate file was edited, and its suite must stay green (it reads 21/21 at the base).

<expected_criteria>DPk1-AC1,DPk1-AC2,DPk1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-k-1.closing-repair.proof_of_spec.json` (copy the shape of an existing proof instance in that folder), validate it with
`python .tools/proof-of-spec-check.py <instance> DPk1-AC1,DPk1-AC2,DPk1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID. Commit with safe-commit under your serial. Report once at the end: criteria with output, commit hashes, rows.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round9.md</decomp_doc>
<owned_cells>DP-k-1</owned_cells>
</decomp_ref>

<paths>
.tools/portal-hooks/dev_push_payload_gate.py
.claude/skills/closer-drive/SKILL.md
org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-k-1.closing-repair.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations and the base measurements; BLIND to the filesystem around the cited paths. Finding inlined: the skill already carries `--project <CODE>` twice, so AC2 greps the exact `approval-lease --project <CODE>` phrase.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round8.md` @8cc3f585e7 section 3 (1.0.0_SA_CTO msg 109157). Its drain closes the project (analysis section 3). No portal worktree is needed.
