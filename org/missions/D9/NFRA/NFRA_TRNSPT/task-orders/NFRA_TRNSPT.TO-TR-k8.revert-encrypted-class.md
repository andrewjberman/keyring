# TO NFRA_TRNSPT.TO-TR-k8 -- revert the ENCRYPTED_UNVERIFIED class; prove internal encrypted mail does not land

<to_id>NFRA_TRNSPT.TO-TR-k8</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-k-8` (`decompositions/NFRA_TRNSPT_DECOMP_R8.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-k-8` (CTO ruling msg 1519): "revert TR-g7's class change in criterion.py, pull.py, land_bronze.py, silver.py and gold.py; no env flag
... The work stays recoverable at ff7846f9f7. (1) a fake-route test showing an internal encrypted author email does not land; (2) the
bundle import check passes and the five modules equal their pre-ff7846f9f7 behavior." Why: every encrypted-only author email in 120 days
went to Opal itself (368 of 368, 0 to a client), so the class would land nothing, and it ships in the Lambda bundle switched on.

**Build:**
1. Restore EXACTLY these six files to their bytes at commit `8394179dec` (the first parent of merge `ff7846f9f7`), e.g.
   `MSYS_NO_PATHCONV=1 git show 8394179dec:<path> > <path>` for each (in Git Bash; never add `2>/dev/null`; an empty result is an error):
   `data/transcripts/scripts/outlook/criterion.py`, `pull.py`, `land_bronze.py`, `silver.py`, `gold.py` (all under
   `data/transcripts/scripts/outlook/`), and `data/transcripts/scripts/tests/test_outlook_silver.py`.
2. Delete `data/transcripts/scripts/tests/test_encrypted_class.py` (`git rm`).
3. New `data/transcripts/scripts/tests/test_internal_encrypted_not_landed.py` with `test_internal_encrypted_author_email_not_landed`: an
   author sender (from the real author table via `criterion.load_tables()`, or a synthetic author injected the way the existing outlook
   tests do), ONE recipient at `opalinvest.com`, ONE non-inline attachment named `report.asc` with `contentType`
   `application/octet-stream` and size 13,500,000, run through `pull.run(source, fake_s3, kms_key_arn=..., apply=True, run_id=...,
   admitted_only=True)` with a stub source (the pattern in `test_outlook_bronze.py` / `test_gateway_mail.py`). Assert nothing was put to
   the fake s3, `ingest` is 0 and `not_landed_not_admitted` is 1. Synthetic local parts only; no real person's address.

### ACCEPTANCE

<criterion id="TR8-k8-AC1" cell_refs="TR-k-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R8_CHECKS/r8_checks.py k8-notland</invocation><expect>R8-K8-NOTLAND-OK</expect></criterion>
`TR8-k8-AC1` -- the internal encrypted author email does not land.

<criterion id="TR8-k8-AC2" cell_refs="TR-k-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R8_CHECKS/r8_checks.py k8-revert</invocation><expect>R8-K8-REVERT-OK</expect></criterion>
`TR8-k8-AC2` -- the six files equal `8394179dec`, `test_encrypted_class.py` is gone, and the bundle import check passes.

<expected_criteria>TR8-k8-AC1, TR8-k8-AC2</expected_criteria>

Dry-run at the base (CLOUD 9787a68b10): AC1 `FAIL absent`, AC2 `FAIL ... 6 files differ` -- FAIL as expected. Also run
`python -m pytest data/transcripts/scripts/tests -q -p no:cacheprovider -k "outlook or mail or internal_encrypted" --ignore=data/transcripts/scripts/tests/test_eod_voice.py`
(0 failed expected; the ignore is an unrelated collection error).

## BOUNDS

- **Grant.** The eight paths in the block below, this order's file, your deliverables folder. Nothing else.
- **LOCAL.** No AWS, gateway or HTTP call; no deploy. Do not edit any other order's proof instance or any `PENDING-THIS-COMMIT` value.
- **Refusal clause.** If a restored file breaks a test outside this grant, stop and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`,
  next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/outlook/criterion.py
data/transcripts/scripts/outlook/pull.py
data/transcripts/scripts/outlook/land_bronze.py
data/transcripts/scripts/outlook/silver.py
data/transcripts/scripts/outlook/gold.py
data/transcripts/scripts/tests/test_outlook_silver.py
data/transcripts/scripts/tests/test_encrypted_class.py
data/transcripts/scripts/tests/test_internal_encrypted_not_landed.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R8.md</decomp_doc> (round 8), cell `TR-k-8`.
<owned_cells>TR-k-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR8-k8-AC1, TR8-k8-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-k8.revert-encrypted-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR8-k8-AC1,TR8-k8-AC2` BEFORE the flip. Pin each artifact to a commit that
actually contains it; if the final commit's hash is not yet known, commit the code first and the instance second.
</proof_of_spec>

**REPORT:** the two check lines, the suite line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a revert in code and tests; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 6 files compared against 8394179dec (all differ at the cut), 1 merge (ff7846f9f7) read; BLIND to the served Lambda (not redeployed; it never carried the class). Traps: a partial revert, an empty git show read as success, a false artifact pin; AC2 compares bytes and the face orders code before instance.
lane: five outlook modules, two test files, one new test, the investigation file.
</preflight>

Source: CTO ruling msg 1519; decomposition round 8 cell TR-k-8.
