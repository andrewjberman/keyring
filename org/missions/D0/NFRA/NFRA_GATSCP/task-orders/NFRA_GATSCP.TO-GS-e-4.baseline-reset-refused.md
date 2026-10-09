# TO NFRA_GATSCP.TO-GS-e-4 -- round 2 GS-e-4: a commit that resets the known-errors list is refused, even when it stages nothing else

<to_id>NFRA_GATSCP.TO-GS-e-4</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~5</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-e-4` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

The surprise-channel "corpus pass" (`.tools/surprise-corpus-validate.py`) compares every channel document's schema failures with the
known-errors list `org/surprise_channel/.corpus-baseline.json` (`BASELINE_REL`, :49). Round 1 scoped it: with `--act PATH`, a NEW
failure outside the act's documents prints `STANDING <CODE> surprise-corpus ...` and does not refuse; inside them it refuses; a
RESOLVED tuple (in the list, no longer produced) always refuses. The row gate `.tools/surprise-row-gate.py` runs the pass only after
a dispatched path matches `CHANNEL_RE` (:61-66), passing `--act` for each such path (:3979-3996); otherwise `main` returns 0 early
(:3961-3965). The pre-commit hook hands the row gate the whole staged list as `STAGED`.

The defect: a commit that stages ONLY the baseline file matches no `CHANNEL_RE`, so nothing grades it. A reset that drops a tuple
would, if graded with `--act <baseline>`, surface the dropped failure as NEW in another project's document and print it STANDING.
Either way, the reset lands. The PRD requires: "deliberately resetting the known-errors list stays a refusal".

### THE CELL

`GS-e-4`. A commit that stages the corpus baseline runs the corpus pass with every finding in-act, so a reset refuses.

**Build:**
1. `surprise-row-gate.py`: a dispatched path equal to `org/surprise_channel/.corpus-baseline.json` triggers the corpus pass, with
   `--act` for it (and for any channel paths, as today). Change nothing else in the row gate: the per-row limbs never grade the
   baseline file as a document.
2. `surprise-corpus-validate.py`: when the baseline path is among the `--act` paths, every finding is in-act (no STANDING), so any
   NEW or RESOLVED tuple refuses. Without the baseline in the act: unchanged. `--write-baseline` (the deliberate re-baseline act)
   is unchanged.

### ACCEPTANCE

<criterion id="GE4-AC1" cell_refs="GS-e-4"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_baseline_reset.py"</invocation><expect>GS-E4-RESET ok=True</expect></criterion>
`GE4-AC1` -- with one baseline tuple dropped in a private index, the row gate given only the baseline refuses; given another
project's untouched document, it lands and prints the uncovered failure as STANDING with its own project (the difference control).

<criterion id="GE4-AC2" cell_refs="GS-e-4"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_corpus_scope.py"</invocation><expect>GS-T1-SCOPE ok=True</expect></criterion>
`GE4-AC2` -- round 1's corpus scope check still passes.

<expected_criteria>GE4-AC1,GE4-AC2</expected_criteria>

Each check plants in a private copy of the git index only. Read both before you build. Each prints its arms and ONE last line.
AC1 FAILs at the base. You do not edit the checks. Also run `python .tools/surprise-row-gate.py --self-test` once after your change
and report its last line (it must still report 0 failed arms).

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- No edit outside the grant. No change to the baseline file, the schemas or any channel document. No override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W5-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the check
  or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not
  block.

<paths>
.tools/surprise-corpus-validate.py
.tools/surprise-row-gate.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/` and `org/surprise_channel/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-4`.
<owned_cells>GS-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GE4-AC1, GE4-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~5/NFRA_GATSCP.TO-GS-e-4.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-4`, validated with `python .tools/proof-of-spec-check.py <instance> GE4-AC1,GE4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; the row gate self-test's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- AC1 arm 2 is the difference control (the same dropped tuple, a different act: STANDING, not a refusal); --write-baseline stays the deliberate path, so the CVO's re-baseline act is not blocked by this cell.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 3; decomposition round 2. Base dry-run (box/dell1 7611122124): GE4-AC1 FAIL as
expected (reset arm rc 0, early return); GE4-AC2 PASS as expected (a control).
