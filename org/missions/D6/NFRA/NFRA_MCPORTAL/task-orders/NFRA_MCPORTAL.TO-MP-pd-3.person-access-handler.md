# NFRA_MCPORTAL task order -- `MP-pd-3` -- WORKSTREAM PC ROUND 2: the owner-gated per-person access handler, and the principal key on the People rows (F2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~27</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- request handlers; run when opened (PRD C8).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change here: the POST reuses the existing gateway-to-writer invoke grant (MP-t-3); the release cell carries any apply.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (bad shape, bad GUID, non-owner, a record kind the store does not know yet).
EGRESS CLASS, declared: none. Every writer invoke and store read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-pd-3` (workstream PC round 2, decomposition sections PD.1, PD.2 and PD.3)

Your worktree is `C:/tmp/mp-pd-27` (branch `wk-NFRA_MCPORTAL-pd-27`). Work and commit only there.

Andrew will change, from the MC Portal People page, what one person reaches through the gateway (PRD v0.8 FWD-21, contract C18).
A parallel cell extends the grant-writer Lambda with the action `set_person_access` (the record is in PD.2 below); another builds
the page against the shapes below. This cell is the gateway's admin handler between them. Read first, whole:
`infra/aws/ec2/opal-gateway/app/admin_grants.py` (your pattern: `invoke_grant_writer`, `_narrow_or_widen`, the owner-header read,
`_canonical_pair`, `get_grant`), `app/admin_people.py` (you edit it), `app/owner_gate.py`, `app/admin_api.py` (read only), and the
tests `tests/test_admin_people.py` and `tests/test_admin_grants*.py` for the stubbing approach.

THE RECORD (fixed): pk `POLICY#<tid>#<oid>`, sk `person_access`; body `status` (`active` | `revoked`), `revision` (int >= 1),
`stopped` (bool), `tools_allow`, `tools_deny`, `channels_allow`, `channels_deny` (sorted unique string lists), `updated_at`,
`updated_by`. The writer's event is `{"action": "set_person_access", "tid", "oid", "change": {...}, "expect_revision": <int> |
null, "owner_header"}`.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:

1. **`app/admin_people_access.py` (new)** with two handlers, both decorated with `owner_gate.owner_only`:
   - `access_get` -- `GET /api/admin/people/{tid}/{oid}/access`. Validate `tid` and `oid` as GUIDs (the way
     `admin_grants._canonical_pair` does); a bad one is 400. Read the record with ONE strong `access_state` get on the key
     `access_state.policy_key(tid, oid, "person_access")`. Answer 200 `{"tid", "oid", "record_kind": "live" | "not live", "record":
     <the body as stored, with the sets as lists> | null, "read_at": "<ISO Z>"}`. If `policy_key` or the get refuses because the
     module does not know the record type (`access_state.AccessStateRefused`), the answer is 200 with `record_kind` "not live" and
     `record` null, never a 500. A read failure of any other kind goes to the module's existing 503 arm (copy how `get_grant`
     does it). No record yet (the type is known, nothing stored) is `record_kind` "live" with `record` null. Run the blocking read
     in `run_in_threadpool`, as the other handlers do.
   - `access_post` -- `POST /api/admin/people/{tid}/{oid}/access`, body `{"change": {...}, "expect_revision": <int> | null}`.
     Validate the GUIDs (400) and the shape BEFORE any invoke (400, with a reason string): `change` a non-empty dict whose keys are
     among `stopped`, `status`, `tools_allow`, `tools_deny`, `channels_allow`, `channels_deny`; `stopped` a bool; `status` one of
     `active`, `revoked`; each list a list of at most 64 non-empty strings of at most 128 characters; `expect_revision` null or an
     int >= 1 (the key must be present). Read the verified owner header from the request exactly as `_narrow_or_widen` does, and
     call `admin_grants.invoke_grant_writer("set_person_access", tid, oid, <the payload>, owner_header)`. The payload argument is a
     dict `{"change": change, "expect_revision": expect_revision}`; READ `invoke_grant_writer` to see how it builds the Lambda event
     from its `candidate` argument, and if it cannot carry `change` and `expect_revision` as top-level event keys, build the event in
     your module by calling the same boto3 client function (`_lambda_client`, `GRANT_WRITER_FUNCTION_NAME` env) without editing
     `admin_grants.py`. The event the Lambda receives must have exactly the keys `action`, `tid`, `oid`, `change`, `expect_revision`,
     `owner_header`. Relay the verdict as the existing handlers do (the same status-code mapping).
   - `routes` -- a module-level list of the two Starlette `Route` objects, paths `/people/{tid}/{oid}/access` (GET and POST), for the
     release cell to splat into `app/admin_api.py` (`*admin_people_access.routes`), as `admin_refusals.routes` and `admin_tenants.routes` are.
2. **`app/admin_people.py` (edit, additive)**: every row of the body gains `"principal": {"tid": "<guid>", "oid": "<guid>"} | null`.
   It is non-null exactly for a row built from a principal that has a `principal_profile` in the grant store (those come from the
   breakdown's `_scan_principals`, which carries `tid` and `oid`); every other row is `null`, including the population row. A
   person who appears in several sources and has a profile gets the profile's `tid`/`oid`. Change nothing else in the body or in
   how rows are built or ordered.
   **AMENDMENT 1 (issuer, after your first report): the one existing assertion that pins the exact row key set moves with the
   added key.** In `tests/test_admin_people.py`, inside `test_people_lists_every_candidate_even_holding_nothing`, the line
   `assert set(p) == {"who", "kind", "how", "tier", "channels"}` becomes `assert set(p) == {"who", "kind", "how", "tier", "channels",
   "principal"}`. That is the ONLY edit to that test. Then re-run AC2: it must read named tests PASSED 4 of 4. Your two
   observations (the pinned `ROUND1_PEOPLE` literal in the never-leaks test, and the Lambda base not yet carrying the writer
   half) stand as filed and need no change.
3. **Do NOT edit** `app/admin_gateway_breakdown.py`, `app/admin_grants.py`, `app/admin_api.py`, `app/access_state.py`, or the
   writer Lambda. The two route lines and the import in `app/admin_api.py` belong to the release cell; name the line in your report.

**Tests**, by these exact names. `tests/test_admin_people_access.py` (new), mounted on a `Starlette` test app as the existing
handler tests do, with a fake Lambda client and a fake store:
- `test_access_post_invokes_writer_with_set_person_access_and_relays_verdict`: a valid POST makes exactly one invoke with action
  `set_person_access`, and the response relays a WRITTEN verdict and a REFUSED verdict with the same status mapping as narrow/widen;
- `test_access_post_payload_matches_pd2_event_shape`: the event the fake Lambda records has exactly the keys `action`, `tid`,
  `oid`, `change`, `expect_revision`, `owner_header`, with `expect_revision` null for a first write;
- `test_access_post_bad_shape_is_400_before_invoke`: an unknown change key, a non-bool `stopped`, a 65-entry list, a missing
  `expect_revision` key each give 400 and the fake Lambda records zero invokes;
- `test_access_post_non_owner_is_refused_and_no_invoke`: a non-owner gets 403 and zero invokes and zero store calls;
- `test_access_get_reads_record_when_live`: with the record type known (plant it into `access_state.POLICY_RECORD_TYPES` for the test)
  and a stored record, the GET answers `record_kind` "live" with the record; with the type known and no record, `record` null;
- `test_access_get_not_live_when_type_unknown`: WITHOUT planting the type, the GET answers 200, `record_kind` "not live", `record` null;
- `test_access_bad_guid_is_400`: a `tid` or `oid` that is not a GUID gives 400 on both verbs.
And in `tests/test_admin_people.py` (add two tests, keep the rest unchanged):
- `test_people_row_principal_is_set_only_for_profiled_principals`: a planted profiled principal's row carries its `{tid, oid}`; an
  email-only row and the population row carry null;
- `test_people_principal_never_leaks_into_other_fields`: difference control: with the new key removed from every row, the body
  equals the round-1 body for the same planted world (compare every other key).

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No other `app/` module, no Terraform, no manifest, nothing in `mcportal/`.
   Make no deploy and no AWS call.
2. If a helper cannot be reused without editing a file outside section 3, REFUSE that criterion with what you measured and file
   a BLOCKING row. Never re-type a rule to make a test pass.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a).
   If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_people_access.py
infra/aws/ec2/opal-gateway/app/admin_people.py
infra/aws/ec2/opal-gateway/tests/test_admin_people_access.py
infra/aws/ec2/opal-gateway/tests/test_admin_people.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~27/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `app/admin_grants.py`, `app/admin_gateway_breakdown.py`, `app/admin_api.py`, `app/owner_gate.py`, `app/access_state.py`, every other
`infra/aws/ec2/opal-gateway/app/` module, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W27-S<k>` (the next free k for W27). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd3.AC1.sh; echo "exit=$?"</invocation><expect>access handler tests: 0 failed; named tests PASSED 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd3.AC2.sh; echo "exit=$?"</invocation><expect>people rows tests: 0 failed; named tests PASSED 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~27/NFRA_MCPORTAL.TO-MP-pd-3.person-access-handler.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the route lines for the issuer (`*admin_people_access.routes` and its import in `app/admin_api.py`);
- whether `invoke_grant_writer` carried `change` and `expect_revision` as top-level keys or you built the event yourself, and why;
- any field of the contract you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC round-2 issuance (decomposition v10) from PRD v0.8 C18. `admin_people.py` is edited by this cell
only (round-1's MP-pc-2 is complete). `MP-pd-4` builds the page against PD.3, so do not rename a field. The release adds
`*admin_people_access.routes` to `app/admin_api.py` as its step 0. Checks dry-run at base 18:0xZ: AC1 FAIL (test file absent);
AC2 FAIL, named tests PASSED 2 of 4 (the two seam tests pass at base, the two new ones are absent: the bound arm holds).

<status>pending</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
