# TO NFRA_GATSCP.TO-GS-f-1 -- round 3 GS-f-1: the row gate's open-order census never counts a seat-home POINTER file as an order

<to_id>NFRA_GATSCP.TO-GS-f-1</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~8</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-1` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-2 |
**rows:** D1-S11, D1-S4 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

The surprise-row gate `.tools/surprise-row-gate.py` refuses a NEW remediation row while the project's task orders are not
terminal (`_route_precondition_violations`, :1826, via `_open_tos_for_project` -> `_open_tos_census`, :1282-1327). The census
enumerates `git ls-files -- "*/task_orders/<CODE>.*.md" "org/missions/D*/*/<CODE>/task-orders/*.md"` (at a merge it reads the index,
`merging=True`), reads each file's `<status>` with `_to_status_match`, and counts as OPEN any file whose word is not in
`TERMINAL_TO_WORDS` (:171) unless its proof instance reads VALID (`_proof_terminal`, :1210). A seat-home POINTER file (e.g.
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/MDPF_DEMQUE.R4-ZQ.POINTER.md`) has no `<status>` tag, so it reads `<no status tag>`
and counts as an open order. Its first two lines are `# POINTER (not an order) -- ...` and
`# pipeline-override: this file is a POINTER in the CloudOps lane task_orders/ home ...`. Two round closes needed an audited
override because of it (rows D1-S4, D1-S11). The CTO ruled (R2): a file carrying that line is not an order; a real open order still
counts.

### THE CELL

`GS-f-1`. The row gate's open-order census never counts a seat-home POINTER file as an order.

**Build:**
In `_open_tos_census` only: skip (do not count, do not list) a file whose text has a line matching
`^#\s*pipeline-override:\s*this file is a POINTER\b` or whose first non-empty line starts `# POINTER (not an order)`. Add the
skipped files' names to the returned note (one clause, `N seat-home POINTER file(s) not counted: ...`). Everything else in the
census is unchanged. Add one `--self-test` arm for it (a POINTER skipped, a real open order counted). Report the self-test's
last line: at the cut it reads `RESULT: 2 arm(s) failed of 246`, both LIVE arms about LGIC_NAMING's proof terminality (`proof
terminality LIVE` and `DOCTORED PAIR, real bytes`), red since a proof-of-spec-check change outside this project (row D1-S13). No
OTHER arm may fail after your change; name every failing arm in your report.

### ACCEPTANCE

<criterion id="GF1-AC1" cell_refs="GS-f-1"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_pointer.py"</invocation><expect>GS-F1-POINTER ok=True</expect></criterion>
`GF1-AC1` -- with a POINTER and a real pending order planted for NFRA_GATSCP in a private index, the census counts the order (the negative arm) and not the POINTER.

<expected_criteria>GF1-AC1</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~8/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W8-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/surprise-row-gate.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-1`.
<owned_cells>GS-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF1-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~8/NFRA_GATSCP.TO-GS-f-1.pointer-is-not-an-order.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-1`,
validated with `python .tools/proof-of-spec-check.py <instance> GF1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 3, battery); BLIND: a census's conclusions are the CTO's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @0ef2dc8325 (with ADDENDUM 1); CTO msg 2258 for D1-S5; decomposition round 3. Base dry-run: see the
issuance commit.
