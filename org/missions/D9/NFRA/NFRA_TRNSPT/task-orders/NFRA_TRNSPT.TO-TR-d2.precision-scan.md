# TO NFRA_TRNSPT.TO-TR-d2 -- the precision scan: the criterion's booleans for every message scanned

<to_id>NFRA_TRNSPT.TO-TR-d2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-d-2` (`decompositions/NFRA_TRNSPT_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** TR-f-2 (drained on your branch: `classify` reads the envelope, `load_tables` reads the ruled tables)

---

## WORKER FACE

### THE CELL

`TR-d-2`, the tool half of the CTO analysis's ruling 3b: the real run "prints the criterion's three booleans for every message it
scanned (the precision measurement C-CRITERION asks for, near misses included)". C-CRITERION (PRD): "Precision is a claim to MEASURE."
The issuer runs this tool over a recorded directory of real messages; you build and test it on synthetic input.

**Build (LOCAL):** `data/transcripts/scripts/outlook/precision.py --replay <dir> [--out <json>]`, reusing `criterion.load_tables` and
`criterion.classify` (import them; never re-implement the rule):
1. One line per `<id>.message.json` + `<id>.attachments.json` pair, sorted by received time:
   `SCAN <receivedDateTime> rid16=<first 16 hex of the record id> sender_ok=<0|1> client_recipient=<0|1> ycharts_pdf=<0|1> trade_update_excluded=<0|1> near_miss=<0|1> ingest=<0|1> basis=<ycharts_basis>`.
   NO subject, NO address, NO display name, NO body text on any line or in the `--out` file.
2. A final line: `PRECISION-SCAN scanned=N ingest=K near_miss=M excluded_trade_update=J not_author=L tables=<label>`.
3. `--out` writes the same rows and totals as JSON (`{"rows": [...], "totals": {...}, "tables": "<label>"}`).
4. Tests `data/transcripts/scripts/tests/test_outlook_precision.py` over `data/transcripts/scripts/tests/fixtures/outlook_replay_envelope/`
   (built by TR-f-2): the per-message booleans, the totals, and that no output line contains any `@`, any fixture subject or any
   fixture body word.

### ACCEPTANCE

<criterion id="TR2-d2-AC1" cell_refs="TR-d-2"><invocation>python -m pytest data/transcripts/scripts/tests/test_outlook_precision.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR2-d2-AC1` -- the booleans and totals, and no identifying text in the output.

<criterion id="TR2-d2-AC2" cell_refs="TR-d-2"><invocation>python data/transcripts/scripts/outlook/precision.py --replay data/transcripts/scripts/tests/fixtures/outlook_replay_envelope</invocation><expect>PRECISION-SCAN scanned=5</expect></criterion>
`TR2-d2-AC2` -- the entry the issuer's real run calls.

<expected_criteria>TR2-d2-AC1,TR2-d2-AC2</expected_criteria>

Dry-run at the base c31230ea02: AC1 "no tests ran" rc 4; AC2 precision.py absent rc 2 -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No bucket, no mailbox, no real email in the repository.
- **TR-x-2 is the next order in your queue** and will rewrite this module's imports to package-qualified form.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`, next unused), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/precision.py
data/transcripts/scripts/tests/test_outlook_precision.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md</decomp_doc> (round 2), cell `TR-d-2`.
<owned_cells>TR-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR2-d2-AC1, TR2-d2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-d2.precision-scan.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR2-d2-AC1,TR2-d2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the line formats, the totals over the fixture, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (Andrew's IAM user), 1 bucket policy with 2 Deny statements; BLIND: the live IAM plane outside this root (0 of the account's roles read). This cell reads and writes no bucket.
comp-adversary: DECLARED-NOT-APPLICABLE -- a read-only scan tool over recorded files.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @acd1033e60 ruling 3b and section 4 item 2; decomposition round 2 cell TR-d-2.
