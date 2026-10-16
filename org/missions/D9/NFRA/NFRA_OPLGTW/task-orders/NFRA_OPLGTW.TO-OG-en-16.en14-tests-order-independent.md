# NFRA_OPLGTW task order -- `OG-en-16` -- repair: the `OG-en-14` tests must not depend on test order (round 39 repair of a merged cell; the issuer's drain check found `test_ogen14_ac03` red after `test_og_en4.py` or `test_og_en12.py`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-16</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-16</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~128</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- offline tests only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- a repair of the issuer's own drain finding on the merged `OG-en-14` (merge `6510ce187f`); no behaviour of the gateway changes.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-16` (decomposition addendum R3-T.99 A1, round 39 repair, workstream ENRICH-R39-B)

THE DEFECT. Run `cd infra/aws/ec2/opal-gateway && python -m pytest -q tests/test_og_en4.py tests/test_og_en14.py` (or `tests/test_og_en12.py` then `tests/test_og_en14.py`): `tests/test_og_en14.py::test_ogen14_ac03` fails with `RuntimeError: Missing required env var: TENANT_ID` raised at `app/config.py:17` when its fixture `mods` runs `importlib.import_module("app.config")`. Run alone, or after `test_og_en13.py`, `test_og_en15.py`, `test_og_cl2.py` or `test_og_en8.py`, it passes. The file sets `os.environ.setdefault("MOCK_GRAPH", "1")` once at import; an earlier test file in the run leaves `MOCK_GRAPH` unset or changed by the time `app.config` is first imported, and `app/config.py` then demands the real tenant variables. A test must not depend on what ran before it.

THE FIX (tests only). In `tests/test_og_en14.py`, make the `mods` fixture set its own environment before the first import of `app.config`: use `monkeypatch.setenv("MOCK_GRAPH", "1")` as the FIRST line of the fixture (the `setdefault` at import time may stay). If `app.config` or `app.data_entitlement` may already be imported by an earlier file in a state that breaks, make the fixture robust to that too (for example read what `app/config.py` does with `MOCK_GRAPH` and `get_config()` and do the smallest thing that makes all three files pass in either order); do NOT change any file under `app/`, and change no other test file. Do not weaken or remove any assertion of `OG-en-14`.

## 2. BOUNDS

- Write only the files in `<paths>`. No code under `app/`. No release, no deploy, no IAM, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_og_en14.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~128/`. Rows: id `NFRA_OPLGTW-Z-W128-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-16"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/en16.AC1.sh; echo "exit=$?"</invocation><expect>(?s)forward order en4, en12, en14: passed (\d+); failed 0.*reverse order en14, en12, en4: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-16"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~128 '^infra/aws/ec2/opal-gateway/tests/test_og_en14\.py$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~128: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three files pass in both orders with the same count. `AC2`: the commits of this serial touch only `tests/test_og_en14.py`.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-16.en14-tests-order-independent.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, what you changed).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39 repair, workstream ENRICH-R39-B. Found at the drain: `test_ogen14_ac03` passes alone and in the worker's own run and fails after `test_og_en4.py` or `test_og_en12.py` (the full-suite order). Risk WORLD by the L6 floor (a gateway infrastructure path); tests only.
- Pre-cut: `en16.AC1` base FAIL as expected (forward order: 10 passed, 1 failed; reverse: 11 passed, 0 failed); `AC2` base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>39</round>
<workstream>ENRICH-R39-R</workstream>
<slot>~128</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
