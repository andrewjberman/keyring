# TO NFRA_TRNSPT.TO-TR-t5 -- thread hop 6: the trace, hops 3-5 end to end on one real meeting with no person

<to_id>NFRA_TRNSPT.TO-TR-t5</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-t-5` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TR-t-4 (drained; `read_meeting.py` on your branch); `land_bronze.py` from chain A is
NOT on your branch -- see the bound below

---

## WORKER FACE

### THE CELL

`TR-t-5`, thread hop 6 (PRD section 2): "Trace -> every step ran without a person; the run's record shows the pull, the landing
and the parse with their timestamps." Round 1 (PRD section 2, last paragraph): hops 3 to 6 are built and exercised against a
pull run under a fresh sign-in -- the 2026-09-29 pull -- while hops 1-2 wait on the gateway tools. The COO's one real run of
FWD-1 for this round is THIS script's run, kept as an artifact.

**Build:** `data/transcripts/scripts/teams/thread_trace.py --series <s> --transcript <ID> --date YYYY-MM-DD --negative-date YYYY-MM-DD --out <json>`:
1. hop `land-probe`: verify the bronze objects are held and byte-true -- read the sidecar and the `.vtt`, recompute sha256, compare
   (do it inside this script with boto3; chain A's `land_bronze.py --probe-held` is the same check but is not on your branch);
2. hop `parse`: `python data/transcripts/scripts/teams/parse_silver.py --series <s> --transcript <ID> --apply` as a subprocess
   (`timeout 120`); capture its `SILVER-WRITTEN` line;
3. hop `read`: `python data/transcripts/scripts/teams/read_meeting.py --series <s> --date <date>` as a subprocess; capture the
   `MEETING` header only (count the turn lines; never store them);
4. negative arm: `read_meeting.py --series <s> --date <negative-date>` (a date with no meeting) -> expect `NOT-HELD ... cause=...`;
5. write `<out>` = `{"transcript_id","series","date","no_person": true,"started_utc","ended_utc","hops":[{"hop","ran_by":
   "data/transcripts/scripts/teams/thread_trace.py","cmd","started_utc","ended_utc","exit","s3_keys":[...],"summary_line"}],
   "negative_arm":{"date","result":"NOT-HELD","cause"}}` with every `s3_keys` entry an `s3://opal-data-transcripts/teams/transcripts/...`
   address, and print `THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD`. No cue text anywhere in the artifact.

### ACCEPTANCE

<criterion id="TR1-t5-AC1" cell_refs="TR-t-5"><invocation>python data/transcripts/scripts/teams/thread_trace.py --series monday_meeting --transcript MM-20260928-0858 --date 2026-09-28 --negative-date 2026-09-27 --out org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R1_THREAD_TRACE_MM-20260928-0858.json</invocation><expect>THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD</expect></criterion>
`TR1-t5-AC1` -- the three hops run by the script on the real Monday meeting, and the negative arm answers with a cause.

<criterion id="TR1-t5-AC2" cell_refs="TR-t-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_thread_trace_check.py org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R1_THREAD_TRACE_MM-20260928-0858.json</invocation><expect>TRACE-VALID</expect></criterion>
`TR1-t5-AC2` -- the issuer's validator: three hops, monotonic timestamps, exit 0 each, addresses under the builder's prefix,
the negative arm with a cause, no person, no text.

<expected_criteria>TR1-t5-AC1,TR1-t5-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "No such file", AC2 TRACE-INVALID unreadable -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED.** The parse hop re-writes the same silver parquet (idempotent, same bytes or a versioned overwrite of the same
  content); nothing else is written to the bucket.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W2-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/teams/thread_trace.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-t-5`.
<owned_cells>TR-t-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-t5-AC1, TR1-t5-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-t5.thread-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-t5-AC1,TR1-t5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the THREAD-TRACE line, per-hop durations, the negative arm's cause, the trace path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (arn:aws:iam::313476888478:user/Andrew_Berman, the var.reader_principal_arns default), 1 bucket policy with 2 Deny statements (TLS-only, key-only); BLIND: the live IAM plane outside this root was not scanned (0 of the account's roles read). The trace runs under that one grantee; this cell adds no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hop 6 (S22 FWD-1 part); decomposition round 1 cell TR-t-5.
