# TO NFRA_TRNSPT.TO-TR-c22 -- the FWD-3 census: every transcript fetchable on a cutoff date, landed or missing with its cause

<to_id>NFRA_TRNSPT.TO-TR-c22</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-c-22` (`decompositions/NFRA_TRNSPT_DECOMP_R22.md`) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-c-22` (CTO ADDENDUM 13 item 1): FWD-3 says "no meeting fetchable on 29 September is later found missing". The issuer will run ONE live
census; you build it on fakes. Existing pieces you READ and reuse:
- `data/transcripts/scripts/teams/gateway_client.py`: `GatewayTransport.list_meeting_transcripts(meeting_id)` returns `{"count", "rows"}`.
  Read a row's shape from the fixtures under `data/transcripts/scripts/tests/`.
- `data/transcripts/scripts/teams/meeting_allowlist.py` `load()` gives the rows with `online_meeting_id` and `series`.
- `data/transcripts/scripts/teams/completeness.py`: `CAUSES` and `build()`/`live_inputs()`. A missing entry's cause comes from it, never a
  new vocabulary.

**Build:** `data/transcripts/scripts/teams/census.py`:
1. `census(listings, silver_keys, cutoff)`. `listings` is `{series: [transcript rows]}`, and `silver_keys` is the set of silver object
   keys. It returns:
   - `fetchable`: every listed transcript whose created time falls on or before `cutoff` 23:59:59Z. Its length is the DENOMINATOR.
   - for each one, `landed` (a silver key exists for that series and meeting date) or `missing` with a `completeness` cause.
   - A series whose listing call was refused (e.g. 502) contributes ONE `refused` entry, so it is counted, not dropped.
2. CLI `python -m data.transcripts.scripts.teams.census --live --cutoff 2026-09-29`. It reads the gateway through `GatewayTransport` (bearer
   via `gateway_client.read_bearer`) and S3 silver keys through paginated `list_objects_v2`, both read-only. It prints ONE JSON line: the
   denominator, per-series counts, landed and missing counts, and each missing entry as (series, date, cause). No transcript text and no
   titles.
3. `data/transcripts/scripts/tests/test_census.py` uses fakes that RECORD calls:
   - `test_cutoff_denominator_counts_only_on_or_before`: rows after the cutoff are excluded; the denominator equals the count.
   - `test_missing_entries_carry_a_completeness_cause`: every missing entry's cause is in `completeness.CAUSES`, and a refused series is
     counted.
   - `test_live_reads_only_and_prints_no_text`: no put, copy or delete is called, and no planted text or title appears in the output.

### ACCEPTANCE

<criterion id="TR22-c22-AC1" cell_refs="TR-c-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py c22</invocation><expect>R22-C22-OK</expect></criterion>
`TR22-c22-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR22-c22-AC1</expected_criteria>

Dry-run at the base (box/dell2 7b2f529975): `R22-C22-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes only; no AWS or HTTP. The issuer runs the live CLI. No transcript, email or client content anywhere.

<paths>
data/transcripts/scripts/teams/census.py
data/transcripts/scripts/tests/test_census.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R22.md</decomp_doc> (round 22), cell `TR-c-22`.
<owned_cells>TR-c-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR22-c22-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-c22.fetchable-vs-landed-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR22-c22-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the module and CLI, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local build.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call in the build; the issuer's live run is read-only under the dell2 agent identity.
comp-adversary: RUN -- sources: CTO ADDENDUM 13 @d1f23acf0c, completeness.py, gateway_client.py; BLIND to live data. Traps: dropping a refused series from the denominator, a new cause vocabulary, content in output; the three tests fix each.
lane: the paths block.
</preflight>

Source: CTO msg 3796 (ADDENDUM 13); decomposition round 22 cell TR-c-22.
