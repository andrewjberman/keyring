# NFRA_OPLGTW task order -- `OG-en-30` -- the client tools' served notes claim only what the source can back: `client_get_fees` stops telling a calling model that an empty fee list is "a true zero" (round 42; the CVO's row `Z-S385`, half `NEVER_WIDEN_HALF_CVO_OG-ap-39_20261018.md`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-30</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-30</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~150</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- docstring text only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CVO's finding on the notes of `OG-en-28` ("a value must carry its claim").
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-30` (decomposition addendum R3-T.119 amendment A6, round 42, workstream ENRICH-R42-D)

THE DEFECT. `OG-en-28` documented the `absent_reason` codes in the docstrings of the five `client_*` functions in `infra/aws/ec2/opal-gateway/app/tools.py` (served as tool descriptions). The note of `client_get_fees` for `no_fee_rows_in_window` reads: "the window holds no fee row for this account; the empty list is a true zero, not an error, so report zero or widen the window". The code fact is narrower: `app/client_adapter_bd49f.py` (near line 764) emits the code when the account has no fee row IN THE SOURCE'S PARTITIONS READ. Whether the source is COMPLETE for the window is an open question (rows `Z-S355`, `Z-S368`, `Z-S369`: 109 fee partition rows firm-wide over 2026-08-17..09-15 and a pending REST-versus-silver probe). A calling model that reads "a true zero ... report zero" would report a client's fees as zero with confidence. The answer body and the reach are unchanged; the DESCRIPTION is the claim.

THE EDIT (docstring text only, in `app/tools.py`; you write only that file):
1. Reword the `no_fee_rows_in_window` note of `client_get_fees` so that it says: the account has no fee row in the SOURCE for this window; this does NOT establish a total (the source's completeness for the window is not measured), so a caller should say that no fee rows were found in the source, not that the fees were zero, or widen the window. Keep it in the same docstring line as it is now (the same sentence slot), the same style (`code: what it means; what the caller does next`), and add no word "zero" to this note.
2. AUDIT the other eleven notes `OG-en-28` wrote (read every `client_*` docstring in `app/tools.py`): any sentence that asserts a completeness, a certainty or an absence of error that the code does not establish gets the same treatment (reword to say what was measured). Do not touch a note that only says what the code did. List what you changed, or "none", in your report.
3. THE LINE-COUNT RULE, as in `OG-en-28`: `app/tools.py` is cited by LINE NUMBER in `app/refs/DATA_CATALOG.yaml`, so add NO lines and delete NO lines: the file keeps its newline count of 1896. Lengthen or replace existing docstring text only.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no behaviour change (the syntax tree of `tools.py` stays EQUAL to its present one once docstrings are blanked), no IAM, no env key, no catalog edit.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/tools.py` (docstring text only); the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~150/`. Rows: id `NFRA_OPLGTW-Z-W150-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-30"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/en30.AC1.sh; echo "exit=$?"</invocation><expect>(?s)banned completeness phrases in the client_\* docstrings: none \(want none\); the no_fee_rows_in_window note names the source, says no fee row there, does not claim a total and has no bare 'zero': yes; tools\.py newline count 1896 \(want 1896\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-30"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~150 '^infra/aws/ec2/opal-gateway/app/tools\.py$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~150: files touched [1-9]\d*; product files 1; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-30"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh en30set tests/test_og_en9.py tests/test_og_sv1.py tests/test_og_sv2.py tests/test_og_cl2.py tests/test_og_en24.py; echo "exit=$?"</invocation><expect>(?s)en30set forward: passed (\d+); failed 0.*en30set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: no client docstring carries "true zero", "report zero" or "zero fees"; the fee note names the source, says no fee row there, does not claim a total and has no bare "zero"; `tools.py` keeps its 1896 newlines. `AC2`: your commits touch only `tools.py`. `AC3`: the five catalog, tool and client test files pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-30.round-42-fee-note-claims-only-what-is-measured.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the fee note's new text, the eleven notes audited and what changed). Also state whether the syntax tree of `tools.py` is equal to the one at your branch base once docstrings are blanked.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-D (decomposition addendum R3-T.119 amendment A6; one issuance per workstream). The CVO signed `OG-ap-39` with the wording as a carried condition ("reword the fee claim in the next release"); the issuer rules it BEFORE the release instead: `OG-ap-39` is the documentation release, so shipping a description the CVO has graded as an unmeasured completeness claim, then a second release to correct it, costs more than re-cutting once. `OG-ap-39` is re-cut on trunk after this cell drains (amendment A4: new `release_sha`, new ask, the three halves re-sign on the one changed docstring line; the page size, the db3 test, the harvest blob and the conditions are unchanged).
- The check's sentence slicing stops the fee note at the next code word; the bare-"zero" rule is on the note only (other notes may use the word where it is true, for example a count).
- Pre-cut: `AC1` base FAIL as expected (the base reads "true zero", "report zero"); the dry-run controls (a banned phrase re-added, a bare "zero" in the note, a line added) read NO, the corrected copy reads PASS; `AC3` passes at the base.

<status>staged</status>
<round>42</round>
<workstream>ENRICH-R42-D</workstream>
<slot>~150</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
