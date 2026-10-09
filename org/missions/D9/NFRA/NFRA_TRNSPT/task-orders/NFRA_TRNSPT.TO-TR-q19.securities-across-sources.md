# TO NFRA_TRNSPT.TO-TR-q19 -- FWD-9: one read-only question across meetings, mail updates and commentary

<to_id>NFRA_TRNSPT.TO-TR-q19</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~5</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-q-19` (`decompositions/NFRA_TRNSPT_DECOMP_R19.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-q-19` (CTO ADDENDUM 8 item 6; PRD FWD-9 "an analyst asks which securities were discussed this quarter and gets one answer covering all
three"): no act exists (coverage row FWD-9).

**Build:**
1. `data/transcripts/scripts/query/securities_across.py` (new package `query/`): `securities_discussed(quarter, *, readers) -> {security:
   {"meetings": n, "mail_updates": n, "commentary": n}}` over three injected read-only readers (Teams + Research silver non-held-out turns, outlook
   analysis_commentary silver, commentary DRAFTs), matching tokens from the existing securities allowlist
   (`data/transcripts/scripts/teams/securities_allowlist.json`). Counts only; no text in the output. A CLI prints the table.
2. `data/transcripts/scripts/tests/test_securities_across_sources.py` (new, synthetic readers): `test_one_answer_three_sources` (one call returns
   per-security counts from all three); `test_counts_only_no_content` (no input text appears in the output); `test_quarter_bounds` (a row outside the
   quarter is not counted).

### ACCEPTANCE

<criterion id="TR19-q19-AC1" cell_refs="TR-q-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py q9</invocation><expect>R19-Q9-OK</expect></criterion>
`TR19-q19-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR19-q19-AC1</expected_criteria>

Dry-run at the base (box/dell2 6ab360052a): `R19-Q9-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W5-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/query/__init__.py
data/transcripts/scripts/query/securities_across.py
data/transcripts/scripts/tests/test_securities_across_sources.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R19.md</decomp_doc> (round 19), cell `TR-q-19`.
<owned_cells>TR-q-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR19-q19-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~5/NFRA_TRNSPT.TO-TR-q19.securities-across-sources.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR19-q19-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local build, no schedule created.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant change.
comp-adversary: RUN -- sources: CTO ADDENDUM 8 @c592051597 (+ 8.1 @3cbbddbe24), R18_COVERAGE.md @ed84ea7977 and the modules named in the face; BLIND to live data (fakes only). Traps: content in output or fixtures, a typed address, a behavior change in an existing reader; the face and the three named tests fix each.
lane: the paths block.
</preflight>

Source: CTO msgs 2938, 2946 (ADDENDUM 8, 8.1); decomposition round 19 cell TR-q-19.
