# TO NFRA_TRNSPT.TO-TR-g18 -- one evidence row per ungraded FWD (round 18 coverage)

<to_id>NFRA_TRNSPT.TO-TR-g18</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-g-18` (`decompositions/NFRA_TRNSPT_DECOMP_R18.md`) |
**outcome_ref:** FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-g-18` (CTO ADDENDUM 6 @7558d41da5): "one evidence row per ungraded FWD (1-6, 8, 9). Each row names the act that exercises it now, on demand,
with its invocation and its read. Where no act exists, it names the missing hop. Output: `R18_COVERAGE.md`." The CTO grades each row from it.

**Read (do not edit):** the PRD `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` (each FWD's DONE WHEN and ACCEPT), the project record
`org/missions/D9/NFRA/NFRA_TRNSPT/STATUS.md`, every close record `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R*_CLOSE.md` and
`R*_READBACK*.json` / `R*_TRACE*.json` / `R*_COMPLETENESS*.json`, and the code under `data/transcripts/scripts/` (teams/, outlook/,
commentary/) and `infra/aws/terraform/transcripts/`.

**Build:** `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R18_COVERAGE.md`: a short header, then ONE ```json block holding a list
of exactly 8 objects, one per FWD in `FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-8, FWD-9`, each:
`{"fwd", "done_when" (quoted from the PRD), "act" (what a person or seat does now to exercise it), "invocation" (the exact command, script or
page), "read" (what is looked at and what it must show), "evidence_so_far" (record paths with commit pins, or ""), "missing_hop" (the hop that
does not exist yet, or "")}`. Either act + invocation + read are all non-empty, or missing_hop is non-empty; never both empty. Cite paths and lines;
quote no transcript, email or client content. Do not run any AWS command or served act: name it.

### ACCEPTANCE

<criterion id="TR18-g18-AC1" cell_refs="TR-g-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R18_CHECKS/r18_checks.py g18</invocation><expect>R18-G18-OK</expect></criterion>
`TR18-g18-AC1` -- the file holds exactly the 8 FWD rows, each complete.

<expected_criteria>TR18-g18-AC1</expected_criteria>

Dry-run at the base (box/dell2 c2d3f143d3): `R18-G18-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Read-only of the repo; no AWS, HTTP or model call; no content quoted.
- **Refusal clause.** A FWD whose PRD text and record disagree: write the row from the PRD, and file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`,
  next unused across every document under `surprise-channel/`).

<paths>
org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R18_COVERAGE.md
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R18.md</decomp_doc> (round 18), cell `TR-g-18`.
<owned_cells>TR-g-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR18-g18-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-g18.coverage-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR18-g18-AC1` BEFORE the flip. Commit the file first, then pin.
</proof_of_spec>

**REPORT:** the 8 rows in one line each (fwd: act-or-missing-hop), the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only coverage record.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- sources: the PRD v0.3, STATUS.md, close records R5-R17 and their read-backs; BLIND to live state (named, not run). Traps: a row graded by the worker (grading is the CTO's), quoted content, an empty row passed off as complete; the face and check fix each.
lane: one deliverable file and the investigation file.
</preflight>

Source: CTO msg 2894 (ADDENDUM 6); decomposition round 18 cell TR-g-18.
