# TO NFRA_GATSCP.TO-GS-x-1 -- direct act GS-x-1: the close gate grades the round being closed

<to_id>NFRA_GATSCP.TO-GS-x-1</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~17</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-x-1` (`decompositions/NFRA_GATSCP_DECOMP.directact-x1.md`) | **outcome_ref:** row
D1-S15 (1.0.0_SA_CTO~DELL1 msg 2776) | **rows:** D1-S15 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

`.tools/git-hooks/missions-tree-check.sh` close_gate (:81-130) runs when a commit moves a project row's `dep_stage` to ROUND_CLOSE or CLOSED. It calls
`python .tools/round-close-check.py --project "$code" --staged` (:101) with NO `--round`, so it grades every round of the project:
a fully graded round 14 of LGIC_BLANKFIX reads `orders=69 judgment=14 graded=14 ... verdict=REFUSED` through the gate, while
`python .tools/round-close-check.py --project LGIC_BLANKFIX --round 14 --staged` reads `orders=3 ... verdict=MAY-CLOSE`. It passes
today only because the gate is in WARN mode. round-close-check takes `--round <n>` together with `--staged`. A project row
carries no round field and a close commit stages only the row and `org/projects/<CODE>.json`, so the round must come from the
index. 1.0.0_SA_CTO~DELL1 msg 2776: the close-gate passes the round being closed; an ungraded judgment in that round still refuses.

### THE CELL

`GS-x-1`. The close gate grades the round being closed.

**Build:** in close_gate, before the round-close-check call, derive `n` = the highest integer in a `<round>N</round>` tag among the
project's task-order files IN THE INDEX (the directory `$(dirname "$p")/task-orders/`; one call such as
`git -C "$ROOT" grep --cached -h -o -E '<round>[0-9]+</round>' -- "<that dir>"` is enough). If `n` is found, pass `--round "$n"`
and keep the rest of the call as is. If none is found, print one `WARN: missions-tree-check close-gate -- <code>: no <round> in
the staged task orders; grading all rounds.` and run the call as today. Change no verdict logic, no mode, no exit code, and no
other limb of the hook. ASCII only.

### ACCEPTANCE

<criterion id="GX1-AC1" cell_refs="GS-x-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round4_prep/checks/r4x_closegate_round.py"</invocation><expect>GS-X1-CLOSEGATE ok=True</expect></criterion>
`GX1-AC1` -- a real round close (LGIC_BLANKFIX round 14, 96a8832de7) replayed in a private git dir reads `orders=3` and MAY-CLOSE
through the gate; with one ungraded judgment criterion planted in a round-14 order it reads REFUSED (the negative arm).

<expected_criteria>GX1-AC1</expected_criteria>

Read the check before you build. It prints its arms and ONE last line, which the expectation is matched against. You do not edit
the check. The check takes about two minutes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~17/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- Do NOT read, grep, copy, quote or attach any `org/**/W73_S*_EVIDENCE.json`, anything under
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`, the IRPT_DASHBD tie-out files, or any cottonwood
  manifest; do not `git show` commits 1ba8eafcda, f5645bb6e9, cb16f8b2f9, d2eb7316f2 (client account data; 0.0.0_AB_MSTR~DELL1
  msgs 2718, 2745, 2764). Search only inside named paths.
- **Proof instance.** Fill `decomp_ref.vintage_commit` and every `commit_or_etag` with a real 7-40 hex commit or
  `PENDING-THIS-COMMIT`; never `HEAD` or a bare `PENDING`.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W17-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/git-hooks/missions-tree-check.sh
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.directact-x1.md</decomp_doc> (direct act), cell `GS-x-1`.
<owned_cells>GS-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GX1-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~17/NFRA_GATSCP.TO-GS-x-1.close-gate-grades-the-round-being-closed.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-x-1`,
validated with `python .tools/proof-of-spec-check.py <instance> GX1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the criterion's last line whole; the row ids; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- the criterion carries its negative arm (an ungraded judgment in the round still refuses); BLIND: a next round cut before the close reads the newer round.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msg 2776; row D1-S15; decomposition directact-x1. Base dry-run: see the issuance commit.
