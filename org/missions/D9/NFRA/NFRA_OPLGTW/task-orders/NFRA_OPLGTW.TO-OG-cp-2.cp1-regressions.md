# NFRA_OPLGTW task order -- `OG-cp-2` -- repair the two gateway tests that OG-cp-1 turned red (the contract's byte form; a premise that is no longer true)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cp-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cp-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~97</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- tests and a contract file's byte form only; nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- a regression found by `2.0.0_SA_COO~MI`'s catalog run on the unchanged catalog (msg 34340) and traced by the issuer to `OG-cp-1` (merged `fa9d18e692`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cp-2` (decomposition addendum R3-T.66, workstream R37-PERSON, FWD-22)

`OG-cp-1` added the record kind `person_access` to the closed record set and to both contract copies (`org/standards/NFRA_OPLGTW_CONTRACT.json` and its byte copy `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json`; `GW` = `infra/aws/ec2/opal-gateway`). Two gateway tests were not in its regression run and now fail on trunk:

1. (DROPPED by A1) `GW/tests/test_schwab_host_inputs.py::test_grant_writer_stages_the_contract_only_from_the_standard` compares the contract staged from the deployed commit with the working standard; it is release-anchored and not yours to repair. Change neither contract file.
2. `GW/tests/test_admin_people_access.py::test_access_get_not_live_when_type_unknown`. Its premise ("the store refuses the record type, so the answer is not live") used `person_access` as the UNKNOWN type; since `OG-cp-1` the type is known, and the same file's other test already asserts the known-type case (`record_kind` live). FIX the test, keeping its intent (a deployment whose closed record set does not contain the type answers "not live" and never reads the store): make the unknown-type condition explicit for that one test by monkeypatching the closed set the app consults (`app_mods.acs.POLICY_RECORD_TYPES`, or whatever name the app reads; read `app/access_state.py` and `app/admin_people_access.py`) to a tuple WITHOUT `person_access`, then assert exactly what it asserted before. Do not change any other test or any app code.

## 2. BOUNDS

- The files in `<paths>` only. No release, no deploy, no app code change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/tests/test_admin_people_access.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~97/`. Rows: id `NFRA_OPLGTW-Z-W97-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cp-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cp2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)failing ids not in the baseline \(the release-anchored one excluded\): 0 \(want 0\); test_access_get_not_live_when_type_unknown passed: 1 of 1.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cp-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cp2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)contract copies byte-equal: yes; person_access in record_types 1 time\(s\) \(want 1\).*person_access fields declared 8 of 8; missing \[\]; tier field present: no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both tests pass and the four suites add no failing id beyond the baseline. `AC2`: the contract copies are byte-equal and declare `person_access` once.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cp-2.cp1-regressions.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream R37-PERSON (decomposition addendum R3-T.66). Found by `~MI` (msg 34340: "two gateway tests fail on the UNCHANGED catalog"), traced here: both failed only after `OG-cp-1` merged. `OG-cp-1`'s regression run named bd-2, bd-3, family, guard and admin; these two suites were outside it. They would fail `OG-ap-21`'s test run, so this cell merges before that release is cut.
- Pre-cut: cp2.AC1 base FAIL as expected (the two named tests fail on trunk); cp2.AC2 passes at base (the copies are byte-equal; the byte FORM differs from the packager's).

- A1 (issuer, 2026-10-15 ~06:0xZ, worker row Z-W97-S1): the worker measured that `build_package.py` copies the contract VERBATIM from `git show <deployed_commit>` (the manifest's pin, today `ee23dd004c`, whose contract has no `person_access`), so the staged member cannot equal the working standard until a release carries the new contract: part 1 of the cell's premise (re-serialise the files) was wrong and is DROPPED; the contract copies stay as `OG-cp-1` left them. `test_grant_writer_stages_the_contract_only_from_the_standard` is therefore RELEASE-ANCHORED: red between the merge of `OG-cp-1` and the release that deploys it, green again when that release lands; `OG-ap-21`'s Phase A runs it and must read it green at the new deployed commit. Part 2 (`test_access_get_not_live_when_type_unknown`) stands and is merged. cp2.AC1 grades part 2 and zero NEW failing ids with that one test excluded and named; the order is re-seated to re-record. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>R37-PERSON-FIX</workstream>
<slot>~97</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
