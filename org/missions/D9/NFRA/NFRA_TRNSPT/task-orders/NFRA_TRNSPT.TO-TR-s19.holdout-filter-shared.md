# TO NFRA_TRNSPT.TO-TR-s19 -- W1-S8 (ARMED): read_meeting.py and research_read.py share ONE holdout filter

<to_id>NFRA_TRNSPT.TO-TR-s19</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-s-19` (`decompositions/NFRA_TRNSPT_DECOMP_R19.md`) | **outcome_ref:** FWD-5, FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-s-19` (CTO ADDENDUM 8, row NFRA_TRNSPT-D2-W1-S8, ARMED, disarm owner `2.0.0_SA_COO~T2`): `data/transcripts/scripts/teams/read_meeting.py`
prints held-out Research rows that `data/transcripts/scripts/teams/research_read.py` withholds (`research_read.py` skips `held_out` rows, :62-65).
Ruling: both readers call ONE shared holdout filter (the one `research_read.py` uses); a held-out row is never printed.

**Build:**
1. Move the held-out rule into one function (e.g. `data/transcripts/scripts/teams/holdout.py` `visible_rows(rows) -> (rows, held_count)`); make
   `research_read.py` call it with NO behavior change, and make `read_meeting.py` call it before printing anything: a held-out row is counted, never
   printed, its text never reaches stdout.
2. `data/transcripts/scripts/tests/test_holdout_filter_shared.py` (new, synthetic rows only): `test_both_readers_use_one_filter` (both modules
   import the same function object); `test_held_out_row_never_printed` (a planted held-out row's text never appears in read_meeting's captured stdout,
   its count does); `test_research_read_unchanged` (company_turns on a synthetic table returns exactly what it returned before).

### ACCEPTANCE

<criterion id="TR19-s19-AC1" cell_refs="TR-s-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py s8</invocation><expect>R19-S8-OK</expect></criterion>
`TR19-s19-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR19-s19-AC1</expected_criteria>

Dry-run at the base (box/dell2 6ab360052a): `R19-S8-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/teams/holdout.py
data/transcripts/scripts/teams/read_meeting.py
data/transcripts/scripts/teams/research_read.py
data/transcripts/scripts/tests/test_holdout_filter_shared.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R19.md</decomp_doc> (round 19), cell `TR-s-19`.
<owned_cells>TR-s-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR19-s19-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-s19.holdout-filter-shared.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR19-s19-AC1` BEFORE the flip. Commit code first, then pin.
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

Source: CTO msgs 2938, 2946 (ADDENDUM 8, 8.1); decomposition round 19 cell TR-s-19.
