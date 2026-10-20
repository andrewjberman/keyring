# NFRA_MCPORTAL task order -- `MP-zo-3` -- WORKSTREAM OGW ROUND 1: the grant writer -- a WIDENING needs the verified owner's confirm; the stale test repaired (FWD-26 writer side, CVO note)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zo-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zo-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~43</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Lambda source and tests; nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no AWS call (the tests use fakes).
comp-adversary: DECLARED-NOT-APPLICABLE -- one test presents a non-owner master_admin header for a widening confirm and asserts zero store calls; that is its own adversary arm.
EGRESS CLASS, declared: none. Make no AWS or network call.
</preflight>

## 1. THE CELL -- `MP-zo-3` (workstream OGW round 1, decomposition section OGW1.3)

You have one worktree: `C:/tmp/mp-ogw-43`, branch `wk-NFRA_MCPORTAL-43` (a sparse checkout that carries `infra/aws/lambda/` and `infra/aws/ec2/`). Begin each shell call with `cd C:/tmp/mp-ogw-43 &&`. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~43 <0.9.0_WK_NFRA_MCPORTAL~43@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push. Make NO AWS or network call.

**The code.** `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`. Its action `set_person_access` is `_set_person_access(event, ctx, owner, *, store)`; the caller has ALREADY verified the owner header (`_verify_owner_header`), so only the verified owner reaches it; a non-owner principal, including a `master_admin` that is not the owner, is refused by that check before any store call. The change body is `event["change"]` with the keys `stopped`, `status`, `tools_allow`, `tools_deny`, `channels_allow`, `channels_deny` (a key present REPLACES that field; see `_person_access_shape_error` and `_person_access_body`). Tests are in `.../tests/` (`test_person_access.py` has the fakes `FakeStore`, `FakeChangesClient`, `_event`, `_plant`, `_kw`).

**The rule to add (PRD v0.10 FWD-26, the writer's side).** A WIDENING is a change that ADDS at least one entry to `tools_allow` or `channels_allow` compared with the prior record (a first write counts against an empty prior). A subtract (adding to a deny list), a restore (removing from a deny list), a stop, a restore-person and a revoke are NOT widenings. A widening requires `widening_confirm` true in the EVENT (not inside `change`):
- absent or not exactly `True` -> REFUSED with reason `WIDEN-NO-CONFIRM`, before any store call (zero store calls), after the shape check and the owner check you already have;
- present, with the verified owner header -> proceeds as today, and the written record and the `operator_audit` item both carry `widening_signoff` = `{"confirmed_by": <the approver string the code already computes>, "at": <the write time>}` so the audit shows who confirmed and when (the existing before/after already shows the change). Never write the owner-key value anywhere.
Do not build the three-halves path: a non-owner can never reach this code, and no other principal may widen in this build.

**The stale test.** `test_person_access_refused_when_record_kind_not_live` fails at base (35 passed, 1 failed): it assumes the staged live-gateway closure does not know `person_access`, but the live gateway now does (OG-cp-1 landed), so the writer writes. Repair it IN PLACE, keeping its name: use `monkeypatch` to make the writer's view of `acs.POLICY_RECORD_TYPES` exclude `person_access` for this test only, then assert the same REFUSED `RECORD-KIND-NOT-LIVE` with zero store calls. Report the old and new body.

**FIVE named tests** in `.../tests/test_person_access.py` (names are read from the sources by the check; each is a top-level `def` with exactly this name; fakes only; synthetic GUIDs):
- `test_person_access_refused_when_record_kind_not_live` (the repaired one)
- `test_widening_without_confirm_is_refused_before_any_store_call` (a change adding a `channels_allow` entry, no `widening_confirm`: REFUSED `WIDEN-NO-CONFIRM`, `store.calls == []`; repeat for `tools_allow`)
- `test_widening_with_the_verified_owners_confirm_is_written_and_recorded` (with `widening_confirm: True`: WRITTEN, revision as today, `widening_signoff` present on the record and on the audit item, no key value anywhere)
- `test_subtract_restore_and_stop_need_no_widening_confirm` (a deny addition, a deny removal, `stopped` true then false: each WRITTEN with no confirm; a prior record with allow entries that stay unchanged is not a widening)
- `test_widening_confirm_from_a_non_owner_master_admin_is_refused_before_any_store_call` (an otherwise valid widening with `widening_confirm: True` but a header for a DIFFERENT principal than the owner: REFUSED by the existing owner check, `store.calls == []`; read how `test_person_access_header_refusals_make_zero_store_calls` builds a wrong-principal header and follow it)
All existing tests keep their names and pass. The whole tests directory now reads 40 passed and 0 failed.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not touch the gateway source, Terraform, `build_package.py`, the function map or the manifest. No deploy, no AWS call, no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof line are the issuer's.
4. Standing rules: no push and no vendor call. The tests take about a minute (they stage the closure once); run them under `timeout 115`.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~43/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py`, `infra/aws/ec2/EC2_MANIFEST.json`, `infra/aws/ec2/opal-gateway/`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W43-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zo-3"><invocation>cd C:/tmp/mp-ogw-43 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo3.AC1.sh; echo "exit=$?"</invocation><expect>named tests present in sources 5 of 5.*failed=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~43/NFRA_MCPORTAL.TO-MP-zo-3.grant-writer-widening-confirm.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1;
- the commit hash;
- the old and new body of the repaired test, and every other existing assertion you changed, or none;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the OGW round-1 issuance (decomposition v20) from PRD v0.10 FWD-26 (the writer refuses a widening that has no recorded sign-off; the verified owner's confirm IS the sign-off; everyone else needs the three halves, not built here) and the CVO's note (a test that the writer REFUSES a WIDENING confirm from a non-owner master_admin principal). `portal_channels` in the change shape is NOT in this cell: the grant's `ScopeChange` lives in the gateway source the Lambda stages from the live release (NFRA_OPLGTW). The writer is deployed through Terraform by `MP-pd-7` Act A after this order drains. Risk is WORLD only because the to-pipeline-gate's path floor says a Lambda source path is infrastructure (spine v3.19 L6); this order deploys nothing and calls no AWS API.
zo3.AC1 base: FAIL as expected (pytest 35 passed, 1 FAILED -- the stale test; named tests present in sources 1 of 5; min 40 passed), run in the provisioned slot-43 worktree, 2026-10-20 ~18:3xZ.

<status>pending</status>
<round>1</round>
<workstream>OGW</workstream>
<slot>~43</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
