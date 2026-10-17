# TO IRPT_BCKEND.TO-IB-pr-617 -- BUILD: the export reads the CURRENT filled-report object (no VersionId) and refuses, with a worded state, when its sha256 or size differs from what the export recorded at submit; the tests move with it (IB-pr-551 ADDENDUM 3, XA-20261017T010553Z-d493 RULED (B))

<to_id>IRPT_BCKEND.TO-IB-pr-617</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~481</issued_to>
<issued_by>2.0.0_SA_COO~S2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed ADDENDUM 3 of the pair IB-pr-551 (COO half `deliverables/2.0.0_SA_COO~S2/NEVER_WIDEN_IB_pr_551_ADDENDUM_3_GETOBJECT_ONLY_SHA256_REFUSAL_COO_HALF.md`, blob `87a46d9cf370c293dae46a413cba213db721b5ef`; CTO half signed in `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_551_SERVE_PATH_HOPS_2_4_CTO_HALF.md`).

---

## WORKER FACE

**Cell `IB-pr-617` (inlined).** The export function reads the filled report (a platinum JSON object, one per client) twice: at SUBMIT the server pins it (`server_pinned_body` reads the current object and records its sha256 and size in the frozen record), and at RENDER and again at the freeze it re-reads it through `read_pinned_filled` (file `infra/aws/lambda/investor-reporting/export/retained_export.py`, function `read_pinned_filled`). Today that second read passes the pinned S3 VersionId to the reader, which makes S3 require `s3:GetObjectVersion`; the S3 fence validator forbids that action, so the export role will be granted `s3:GetObject` only. **Change `read_pinned_filled` so it reads the CURRENT object (call the reader with the client id and NO version_id), no longer requires the reply's version to equal the pin, and keeps the refusal when the bytes' sha256 or size differ from the pin, with a worded state.** An overwritten report is therefore REFUSED, never exported from other bytes. The frozen record keeps the VersionId the server saw at submit as a record only.

**Exactly this change** in `retained_export.py` (touch no other function in that file, no other file but the three test files):

```python
def read_pinned_filled(reader, pin):
    """THE ONE READ of a pinned filled report: the freeze and the render both use it. `reader(client_id)` answers
    `{key, version_id, body}` for the CURRENT object (no VersionId is passed: the export role holds no GetObjectVersion).
    Bytes whose sha256 or size differ from the pin are refused and never rendered."""
    found = reader(pin["client_id"])
    key = found.get("key") if isinstance(found, dict) else None
    if not isinstance(key, str) or not key.strip():
        raise FilledReportUnavailable("the filled report object could not be read; resubmit")
    data = found.get("body")
    if (not isinstance(data, bytes) or len(data) != pin["size"]
            or hashlib.sha256(data).hexdigest() != pin["sha256"]):
        raise FilledReportUnavailable("the filled report for this client changed after this export was submitted (its "
                                      "sha256 or size no longer matches the pin); open the report again and resubmit")
    return key, data
```

Do NOT edit `filled_reader_installed.py` (it already reads the current object when no version is named), `render.py`, `bundle.py`, `server_pinned_body`, `parse_filled_report_source` or any other file. Update the docstrings or comments in `retained_export.py` that say the pinned VersionId is always passed or that the current object is never consulted, only where they would now be false (the module head near line 34 and `read_pinned_filled`'s own docstring); change nothing else.

**Tests (three files under `infra/aws/lambda/investor-reporting/export/tests/`: `test_filled_report_server_pin.py`, `test_filled_report_freeze_scope.py`, `test_filled_report_source.py`).** Run the three files first and read every failure: each failure is one of (a) a test that asserted the OLD behaviour (a read under the pinned VersionId, `store.calls[-1] == (CLIENT, VID)`, calls `[(CLIENT, None), (CLIENT, VID)]`, `test_reply_under_another_version_is_refused`): move it to the new behaviour (the reader is called as `(CLIENT, None)`), or (b) a defect of your change (fix the code, not the test). The known ones: `test_overwritten_version_still_exports_pinned_bytes` (server_pin), `test_valid_filled_report_pin_is_frozen_with_version_sha_and_size`, `test_pin_without_its_version_id_is_frozen_at_the_current_version`, `test_page_sent_version_is_ignored_and_the_current_version_is_frozen`, `test_reply_under_another_version_is_refused`, `test_render_read_returns_the_pinned_bytes_and_round_trips_the_bundle` (source). Then add or rename EXACTLY these two behaviour tests (the checker looks for the names):

1. `test_overwritten_object_is_refused_at_render` (in `test_filled_report_server_pin.py`, replacing `test_overwritten_version_still_exports_pinned_bytes`): freeze against a store whose current object is DATA1; overwrite the object with DATA2 (the store's `overwrite`); `filled_render_read(store, item)` raises `FilledReportUnavailable`, and the last reader call was `(CLIENT, None)`.
2. `test_changed_object_is_refused_with_a_worded_state` (in `test_filled_report_source.py`, replacing `test_reply_under_another_version_is_refused`): PLANT a changed object: a reader whose first answer (the server's pin read) is the document and whose later answers are the same document with one byte flipped; `freeze_filled_report` raises `FilledReportUnavailable`, and the exception text contains both the words `changed` and `resubmit`. Also assert a changed SIZE (a longer body) is refused the same way.

Keep every other test's intent; do not delete a test without moving it. The whole of the three files must pass at the end.

**Do, in this order. A STOP is reported to the issuer and writes nothing further.**
1. Read `retained_export.py` lines 300 to 480 and the three test files; run them (`python -I -m pytest -q -p no:cacheprovider tests/<file>` from `infra/aws/lambda/investor-reporting/export/`) and record the count BEFORE.
2. Make the change above and the test moves; run the three files to green. Record the count AFTER and the list of tests you moved or renamed.
3. Run the three criteria below from the repository root; record each output and exit code verbatim in `IB248-1_criteria_output.txt` under your deliverables folder. AC3 puts the base file back in place for a moment and restores yours; if it reports your file was not restored, restore it with `git checkout -- <file>` ONLY if the repo's HEAD copy is the base, otherwise STOP.
4. Write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~481 <0.9.0_WK_IRPT_BCKEND~481@opal.agent>" -F <msgfile> -- <explicit paths>` (the message file written with a file-writing tool, not the shell), flip this order to `complete` only if all three criteria PASS (otherwise leave it `pending` and say which failed). Report once, under 150 words.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB248-1-AC1" cell_refs="IB-pr-617"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r248/p248_cells.py" . IB248-1-AC1</invocation><expect>IB248-1-AC1 PASS</expect></criterion>
<criterion id="IB248-1-AC2" cell_refs="IB-pr-617"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r248/p248_cells.py" . IB248-1-AC2</invocation><expect>IB248-1-AC2 PASS</expect></criterion>
<criterion id="IB248-1-AC3" cell_refs="IB-pr-617"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r248/p248_cells.py" . IB248-1-AC3</invocation><expect>IB248-1-AC3 PASS</expect></criterion>

<expected_criteria>IB248-1-AC1, IB248-1-AC2, IB248-1-AC3</expected_criteria>

What the checks grade: AC1 the three export filled-report test files pass and the two named tests exist and pass; AC2 the seam: `read_pinned_filled` passes no `version_id` to the reader, keeps the sha256 and size comparison, its refusal says the report changed and to resubmit, and `filled_reader_installed.py` is byte-equal to the base commit `bba05481507a`; AC3 the difference control: with the BASE `retained_export.py` put back, both named tests FAIL.

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/export/retained_export.py` and the three test files named above; read anything in the repo; write your deliverables folder, the surprise channel and this order's status. **NO** edit of any other file, **NO** AWS call, **NO** deploy, **NO** push, **NO** edit of `filled_reader_installed.py`, `render.py`, `bundle.py`, any Terraform file or the source map.
- **Refusal clause:** STOP and report if: a failing test is neither a moved old-behaviour assertion nor a defect of your change; a change outside the two named functions or the stated docstrings would be needed; AC3 leaves the built file unrestored and the HEAD copy is not the base.
- **Row ids** `IRPT_BCKEND-D2-W481-S<k>`; file a row for anything odd and keep working. `surfaced_at` = `date -u +%FT%TZ` at filing. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_server_pin.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_freeze_scope.py
infra/aws/lambda/investor-reporting/export/tests/test_filled_report_source.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-617.export-reads-the-current-filled-object-and-refuses-on-sha256.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 243 (round 8, workstream ~PS), cell `IB-pr-617`.
<owned_cells>IB-pr-617</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB248-1-AC1, IB248-1-AC2, IB248-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/IRPT_BCKEND.TO-IB-pr-617.export-reads-the-current-filled-object-and-refuses-on-sha256.proof_of_spec.json` (the file stem of this order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: Code and tests in one file of one Lambda package (WORLD only because the gate floors every infra/ path at WORLD, spine v3.19 L6; nothing is deployed or changed in the cloud by this cell); the function reaches the cloud only through the later bundle apply (TO-IB-pr-618, WORLD, its own preflight).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed here; the export role's grant is ADDENDUM 3's IAM leg (TO-IB-pr-616 Step 6), GetObject only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p248_cells.py IB248-1 dry-run at the base `bba05481507a` on dell2 2026-10-17 ~01:5xZ: AC1, AC2, AC3 each FAIL (AC1: the named tests do not exist; AC2: read_pinned_filled still passes version_id; AC3: with nothing built the named tests select nothing). AC2 also run against a reference copy of the change in a scratch tree and PASSES. The file p248 puts the base file back and restores the built bytes in a finally clause.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~481` in its own worktree. Class WORLD by the path floor (the work is a repo-only build of about 20 code lines plus tests, no cloud call), full limbs, not the direct-act path.
</preflight>
