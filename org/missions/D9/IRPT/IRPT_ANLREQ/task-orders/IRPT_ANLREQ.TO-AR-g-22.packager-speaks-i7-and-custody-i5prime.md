# TO-AR-g-22 -- the packager reads `commentary_ref` and writes `pdf_ref` as I7, and sends I5' for a custody-lane request (rows D2-W62-S3, D2-W62-S4)

<to_id>IRPT_ANLREQ.TO-AR-g-22</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~65</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-22` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-12 is merged).

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md`, section "Interface added this round", rows I7 and I5'.
Then `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json`, the ONE sample every lane's I7 contract test
round-trips.

### THE CELL

The packager is `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`, built in round 1. Its handler is
`handle_commentary_ready`; its package render is `opal_producer.produce_package`.

1. **I7 in.** The acceptance record's `commentary_ref` is the structured `{"artifact_id", "sha256", "version_id"}`. Read it as that
   dict.
   - Refuse `COMMENTARY_REF_MALFORMED` when a key is missing, when there is any extra key, or when `sha256` is not 64 lowercase hex.
   - Read the bytes by its `artifact_id` through the live repository reader, and check them against its `sha256`. A mismatch refuses
     `COMMENTARY_SHA_MISMATCH`.
   - Round 1 also took a bare string. Drop it, and refuse `COMMENTARY_REF_MALFORMED`.
2. **I7 out.** `pdf_ref` (the stored `package.pdf`) is the same structured shape, taken from what the artifacts port returns.
   - On the I5 call, `commentary_ref` and `pdf_ref` each travel as canonical JSON: `json.dumps(x, sort_keys=True, separators=(",", ":"))`.
   - Each must be at most 512 characters (`infra/aws/lambda/ticket_center/lambda_function.py:129` `PACKAGE_REF_MAX_CHARS`). Over the
     limit refuses `PACKAGE_REF_TOO_LONG` before any call.
   - If the stores lack an `artifacts` port, so no version or sha exists, refuse `PDF_REF_UNSTRUCTURED`. Never send a bare key.
3. **I5' (custody lane).** A request filed on a CUSTODY basis has no original upload. Its I5 carries `original_ref: null`; the other
   three refs stay required.
   - Decide the lane from the acceptance record. Read how `ycharts/generate/submission.py` `validate_public_request` (:45) tells a
     custody basis from a prospect `input_id` basis, and what the stored record keeps of it.
   - A PROSPECT request with no `original_ref` still refuses `ORIGINAL_REF_ABSENT`, as in round 1.
   - If the record cannot tell the lanes apart, file a row and refuse.
4. **Wired reader.** `2.0.0_SA_COO~T2` registered `svc-irpt-packager` for `ANALYSIS_COMMENTARY` in `reports/repository.py`
   `SERVICE_READERS` (decomposition AMENDMENT 5).
   - `live_read_artifact` now reads through `ArtifactRepository` as that subject, and no longer raises `COMMENTARY_READER_UNWIRED`
     when the subject is registered.
   - Update `research/tests/test_opal_packager.py` test (h), which pinned the reader as unwired and is red at base. It now asserts
     the registered subject and the repository read, using a fake repository. Keep its refusal arm for an unregistered subject.
   - Keep every other test in that file green.
5. **Test.** Add `research/tests/test_packager_i7.py`, offline with fakes. It must prove:
   - (a) THE SAMPLE: load `I7_SAMPLE.json`. `sample` -> canonical equals its `canonical` field; canonical -> `json.loads` equals
     `sample`. Assert both directions.
   - (b) a valid structured `commentary_ref` is read by `artifact_id` and sha-checked; a wrong sha refuses `COMMENTARY_SHA_MISMATCH`;
   - (c) a bare-string or extra-key `commentary_ref` refuses `COMMENTARY_REF_MALFORMED`, with no render and no attach;
   - (d) the attach payload's `commentary_ref` and `pdf_ref` are canonical-JSON strings of at most 512 chars;
     `json.loads` of each gives the three-key dict;
   - (e) a custody-lane record sends `original_ref: null` with the other three present; a prospect record without an original still
     refuses `ORIGINAL_REF_ABSENT`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR22-g-AC1" cell_refs="AR-g-22"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g22</invocation><expect>^AR1-G2-G22-OK</expect></criterion>

<criterion id="AR22-g-AC2" cell_refs="AR-g-22"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR22-g-AC1,AR22-g-AC2</expected_criteria>

- AC1 runs `test_packager_i7.py` AND `test_opal_packager.py`: at least 5 passed and 0 failed across both. At base it FAILs
  (`test_packager_i7.py` is absent and test (h) is red).
- AC2: no file newly red. At base this reads OK. Allow at least 600 s.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs. Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W65-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below.
  Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~65" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~65@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~65 <0.9.0_WK_IRPT_ANLREQ~65@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_i7.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-22.packager-speaks-i7-and-custody-i5prime.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> round 2, workstream ~G, cell `AR-g-22`.
<owned_cells>AR-g-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR22-g-AC1, AR22-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/IRPT_ANLREQ.TO-AR-g-22.packager-speaks-i7-and-custody-i5prime.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-22`.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR22-g-AC1,AR22-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~62/IRPT_ANLREQ.TO-AR-g-12.package-pdf-with-commentary-and-attach.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the I7 read and sha check;
- where `pdf_ref`'s three fields come from;
- how the lane is decided;
- the test (h) change;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the packager's two ref shapes and one lane branch; I5's wire stays four string fields (canonical JSON per I7), with original_ref null only on the custody lane (I5', ~V2's AR-v-21 admits it). Ships in the resident release (AR-g-23); nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- the repository read uses ~T2's SERVICE_READERS entry (AMENDMENT 5); no permission here.
comp-routes: DECLARED-NOT-APPLICABLE -- the I5' route change is ~V2's AR-v-21.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the packager runs on the I4 message (AR-g-13 poll).
comp-adversary: RUN -- read the R2 decomposition (I7, I5'), ticket_center lambda_function.py :129 and :1389-1392, and the base failure of test_opal_packager.py test (h) (assert not ['svc-irpt-packager'], after ~T2's AMENDMENT 5 entry). Published I7_SAMPLE.json (179 canonical chars). Traps: an unstructured pdf_ref, a ref over 512, an unchecked commentary sha, a prospect request slipping into I5', the bare-string read kept.
lane: ~G (ycharts/research/*).
</preflight>

Source: IRPT_ANLREQ decomposition round 2 cell AR-g-22 (@cff0872f0f, 2.0.0_SA_COO~Y2 msg 2780); rows D2-W62-S3, D2-W62-S4; AMENDMENT 5.
