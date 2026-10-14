# NFRA_MCPORTAL task order -- `MP-pd-2` -- WORKSTREAM PC ROUND 2: the grant writer gains `set_person_access` (FWD-21 write half, F2, PRD C18)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~26</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a Lambda handler branch; invoked on demand by the gateway.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell: the writer already holds the POLICY# write the operator path uses; the release cell (MP-pd-7) carries the apply.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (no header, non-owner, stale header, bad shape, stale revision, a record kind the staged module does not know, a tombstone).
EGRESS CLASS, declared: none. Every store and changes-table call in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-pd-2` (workstream PC round 2, decomposition sections PD.1 and PD.2)

Your worktree is `C:/tmp/mp-pd-26` (branch `wk-NFRA_MCPORTAL-pd-26`). Work and commit only there.

Andrew wants to change, from the MC Portal page, what one person reaches through the gateway: switch a channel or a tool off
or on for that person, or stop and restore the person (PRD v0.8 FWD-21 and contract C18). The change is a new record kind,
`person_access`, written by the SAME grant writer that already writes grants, and read by the gateway on the next call (that
reader is another project's cell, NFRA_OPLGTW OG-cp-1; do not build it). This cell adds the WRITE to the Lambda at
`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py`. Read the whole file first, and its tests
(`tests/test_grant_writer.py`, `tests/test_register_tenant.py`, `tests/conftest.py`). `register_tenant` is your precedent: it is a
branch in `_decide` after the owner header is verified, it builds its own key (`_tenant_key`), it writes the record and an
`operator_audit` item in one `operator_transact`, and it fills `ctx["before"]` and `ctx["after"]` for the changes-table record.

THE RECORD (fixed; a parallel project reads exactly this):
- key: pk `POLICY#<tid>#<oid>`, sk `person_access`, record type `person_access` (the same partition as the person's
  `principal_profile`); one record per person, no revision part in the sort key;
- body: `status` (`active` | `revoked`), `revision` (int >= 1), `stopped` (bool), `tools_allow`, `tools_deny` (sorted unique lists
  of tool names), `channels_allow`, `channels_deny` (sorted unique lists of channel ids), `updated_at` (ISO Z), `updated_by`
  (the first 16 hex characters of the sha256 of the lower-cased approver string the writer already computes, which is the
  verified email or the claim name; never the owner key value).

THE EVENT: `{"action": "set_person_access", "tid", "oid", "change": {...}, "expect_revision": <int> | null, "owner_header"}`.
`change` may hold `stopped` (bool), `status` (`active` | `revoked`), `tools_allow`, `tools_deny`, `channels_allow`,
`channels_deny` (lists of strings). A key absent from `change` keeps its prior value; a key present REPLACES it. A first write
(no prior record) starts from `status` `active`, `stopped` false and four empty lists, applies `change`, and lands revision 1.

Build, in this order inside `_decide` (after the owner header is verified, exactly as `register_tenant` does):

1. **Refusals BEFORE any store call**, each `{"verdict": "REFUSED", "reason": R, "detail": ...}`:
   - `BAD-TID` when `tid` or `oid` is not a GUID (reuse the existing `_GUID_RE`);
   - `BAD-PERSON-ACCESS` when `change` is not a non-empty dict, holds a key outside the six, `stopped` is not a bool, `status` is
     not one of the two, a list is not a list of non-empty strings (each at most 128 characters, at most 64 entries), or
     `expect_revision` is neither null nor an int >= 1;
   - `RECORD-KIND-NOT-LIVE` when `"person_access"` is not in `acs.POLICY_RECORD_TYPES` of the module this Lambda imports. That
     tuple is closed, and the gateway release this Lambda stages from may not know the type yet. The refusal is the safe state.
2. **The key** is built the way `acs.policy_key(tid, oid, "person_access")` builds it. (Read `app/access_state.py` `policy_key`
   and `_expected_type` first.) If `acs.policy_key` refuses the type, that is the same state as `RECORD-KIND-NOT-LIVE`.
3. **The write**, in ONE `st.operator_transact([...])` with the person's `operator_audit` item (mirror the audit item
   `register_tenant` and `admin.activate` build: `approver`, `source_authorization` `"mcportal-grant-writer:set_person_access"`,
   `at`, `summary`; key `acs.Key(pk, "operator_audit#" + admin._audit_id(at), "operator_audit")`):
   - read the current record with `st.get(key)` first (a strong read);
   - no record: `expect_revision` must be null, else `STALE-REVISION`; the put carries condition `acs.IF_ABSENT`;
   - a record: `expect_revision` must equal its `revision`, else `STALE-REVISION` (before any write); the put carries a condition
     that the stored `revision` still equals the value read (look at how `admin.activate` and `access_state.Op` express an
     optimistic revision condition, and use that, not a new mechanism); the new `revision` is the prior + 1;
   - `acs.ConditionFailed` from the transaction -> `STALE-REVISION`.
4. **The changes-table record** (already written by `handle` for every outcome): set `ctx["before"]` to the prior body, or null,
   and `ctx["after"]` to the new body, so the existing record carries both. Change nothing in `handle` or `_record_item`.
5. **Revoking** is `change: {"status": "revoked"}`: it writes revision + 1 with `status` `revoked`. It is a tombstone. No code
   path in your branch issues a delete.
6. Answer `{"verdict": "WRITTEN", "reason": None, "detail": "", "result": {"tid", "oid", "revision": n, "record": <the body>}}`.

Do not change the four existing actions' behaviour, `handle`'s signature, `lambda_function`, `build_package.py`, Terraform or any
other file.

**Tests**, in the new file `tests/test_person_access.py`, by these exact names. The staged `app.access_state` does NOT know
`person_access` yet (it stages from the live gateway release), so tests that exercise a write plant the type into the staged
module's tuple with `monkeypatch.setattr(acs, "POLICY_RECORD_TYPES", acs.POLICY_RECORD_TYPES + ("person_access",))` (and undo
it per test). Use a fake store that records every call, and the injected test signing key and clock the other test files use:
- `test_person_access_first_write_creates_revision_1`: expect_revision null, change `{"channels_deny": ["m365"]}` lands revision 1
  with the audit item in the same `operator_transact`, `stopped` false, `status` active;
- `test_person_access_update_requires_current_revision`: with a record at revision 1, `expect_revision` 5 -> `STALE-REVISION`
  and ZERO writes; `expect_revision` 1 -> revision 2;
- `test_person_access_header_refusals_make_zero_store_calls`: no header, a non-owner and a stale header each REFUSED with the
  existing reasons and the fake store records zero calls of any kind;
- `test_person_access_bad_shape_refused_before_store`: an unknown change key, a non-bool `stopped`, a 65-entry list, a non-GUID tid
  and a bad `expect_revision` each refuse (`BAD-PERSON-ACCESS` or `BAD-TID`) with zero store calls;
- `test_person_access_stop_and_restore_round_trip`: `stopped` true then false: two revisions; the changes-table fake holds two
  records, the second's `before` equal to the first's `after`;
- `test_person_access_refused_when_record_kind_not_live`: WITHOUT the monkeypatch, `RECORD-KIND-NOT-LIVE` and zero store calls
  (this is the state the real staged module is in today);
- `test_person_access_revoke_is_a_tombstone_never_a_delete`: `{"status": "revoked"}` writes revision + 1 with status revoked, and
  the fake store records no `delete` action ever.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Nothing is applied, planned, built into a zip, packaged or invoked on AWS.
   `ops/schwab_entitlement_admin.py` and every file under `infra/aws/ec2/` stay unchanged (you may read them).
2. If a criterion cannot be met without editing a file outside section 3 (for example if `acs.Op` cannot express the revision
   condition, or `operator_transact` refuses the person_access key even with the type planted), REFUSE that criterion with what
   you measured and file a BLOCKING row. Never re-type a rule to make a test pass.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a).
   If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py
infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_person_access.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~26/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other file under `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`, `infra/aws/ec2/opal-gateway/app/access_state.py`,
`.../ops/schwab_entitlement_admin.py`, `.../app/admin_grants.py`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W26-S<k>` (the next free k for W26). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd2.AC1.sh; echo "exit=$?"</invocation><expect>writer person_access tests: 0 failed; named tests PASSED 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd2.AC2.sh; echo "exit=$?"</invocation><expect>writer suite: passed=31 or more failed=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~26/NFRA_MCPORTAL.TO-MP-pd-2.grant-writer-person-access.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- how you expressed the optimistic revision condition, and which existing function you mirrored;
- whether `operator_transact` accepted the person_access key with the type planted, and what it refused without it;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC round-2 issuance (decomposition v10) from PRD v0.8 C18 and the round-1 analysis ruling 3 (F2).
The record shape is NFRA_OPLGTW's OG-cp-1 draft's (`DRAFT_NOT_ISSUED_TO-OG-cp-1_person_record_reader.md`), which supersedes
PC.7's field names. Facts behind the cut (PD.0): the Lambda's tests stage the gateway closure from the LIVE release, so the real
`access_state` does not know `person_access` until OG-cp-1 is released; that is why one test is the NOT-LIVE refusal and why
MP-pd-7 is gated on that release. Checks dry-run at base 18:0xZ: AC1 FAIL (test file absent), AC2 FAIL (24 passed, needs 31).
Writes stay Andrew-only (C2): the header check is unchanged and runs first.

<status>complete</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
