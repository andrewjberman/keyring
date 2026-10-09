# TO NFRA_TRNSPT.TO-TR-e19 -- FWD-4: a listing snapshot per pull, so the expired cause is reachable

<to_id>NFRA_TRNSPT.TO-TR-e19</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-e-19` (`decompositions/NFRA_TRNSPT_DECOMP_R19.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-e-19` (CTO ADDENDUM 8 item 4): FWD-4's "expired" cause is unreachable: `data/transcripts/scripts/teams/completeness.py` reaches `expired`
only through `inputs["previously_listed"]` (:71, :82), and no pull stores a listing, so that input is always empty (coverage row FWD-4).

**Build:**
1. Each Teams pull run stores its Microsoft listing (meeting ids + dates + series, no content) as one snapshot object at an address from
   `lib/opal_naming.py address()` (a state/listing path in the transcripts tier; a builder refusal = a row). Add the write to
   `data/transcripts/scripts/teams/pull.py` behind the existing apply flag, and a loader (`listing_snapshot.py`) that turns all prior snapshots
   into `previously_listed`.
2. `completeness.py` takes `previously_listed` from that loader when the caller passes none, so asking about one missing meeting reaches `expired`
   when a meeting was listed before and is absent now.
3. `data/transcripts/scripts/tests/test_listing_snapshot_expired.py` (new, fakes): `test_snapshot_written_per_pull`; `test_expired_cause_reached`
   (listed in snapshot 1, absent from the current listing, no bronze -> `expired`); `test_never_recorded_still_distinct`.

### ACCEPTANCE

<criterion id="TR19-e19-AC1" cell_refs="TR-e-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R19_CHECKS/r19_checks.py e4</invocation><expect>R19-E4-OK</expect></criterion>
`TR19-e19-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR19-e19-AC1</expected_criteria>

Dry-run at the base (box/dell2 6ab360052a): `R19-E4-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W3-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/teams/pull.py
data/transcripts/scripts/teams/completeness.py
data/transcripts/scripts/teams/listing_snapshot.py
data/transcripts/scripts/teams/NAMES.json
data/transcripts/scripts/tests/test_listing_snapshot_expired.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R19.md</decomp_doc> (round 19), cell `TR-e-19`.
<owned_cells>TR-e-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR19-e19-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-e19.listing-snapshot-expired.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR19-e19-AC1` BEFORE the flip. Commit code first, then pin.
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

Source: CTO msgs 2938, 2946 (ADDENDUM 8, 8.1); decomposition round 19 cell TR-e-19.
