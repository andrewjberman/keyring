# NFRA_MCPORTAL task order -- `MP-t-4` -- HOP 4 (backend): the gateway's grant handlers, which invoke the writer and never write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface is written; the invoke grant is MP-t-3's.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: AWS READ-ONLY from this box (AC2's one read of the grant store). No write, no invoke.
</preflight>

## 1. THE CELL -- `MP-t-4` (round 1, decomposition s.2/s.3)

`MP-t-1` (your previous order) built the owner gate and the admin router `infra/aws/ec2/opal-gateway/app/admin_api.py`
(every handler behind the gate). It is merged at your HEAD. A separate grant-writer Lambda (another cell) is the ONLY
path that writes a grant. It takes `{"action": "narrow"|"widen"|"revoke", "tid", "oid", "candidate", "owner_header"}`
and answers `{"verdict": "WRITTEN"|"REFUSED", "reason"}`; its name is `lib/opal_naming.py`
`name('mcportal', None, 'grant-writer', 'lambda')` once its registry row lands. Build **`app/admin_grants.py`** (new):
- **`read_grant_state(tid, oid, table=None) -> str`** returns exactly `NO-PROFILE`, `PROFILED` or `STORE-UNAVAILABLE`,
  through the store's EXISTING read path (`app/access_state.py`, `app/data_entitlement.py`). `table=None` means the
  configured store.
- **`GET /api/admin/grants/{tid}/{oid}`**: the person's profile and active data grant (`data_entitlement` scope
  dimensions), read through the existing store.
- **`POST /api/admin/grants/{tid}/{oid}/narrow`** and **`.../widen`**: invoke the grant writer with the candidate and
  the REQUEST's own `x-amzn-oidc-data` header forwarded as `owner_header`, and return its verdict. **The gateway writes
  nothing itself**: no call to any store write API from this module.
- **`GET /api/admin/changes`**: the writer's audit records, newest first, each with before and after.
- **`tests/test_admin_grants.py`** (new), with stubs (no network, no `moto`), naming exactly:
  `test_get_grant_reads_store`, `test_narrow_invokes_writer_with_forwarded_header`,
  `test_gateway_never_writes_policy` (trap the store's write API: any call fails the test), and
  `test_changes_newest_first`.

The ONE line that registers these handlers in `app/admin_api.py` is a HOOKUP, and it is not yours: export your
routes (a list or a mount function) and name the line you need in your report. The issuer adds it at the merge.

## 2. BOUNDS

1. Nothing is deployed. Every existing route and guard is unchanged.
2. Standing: no push, no install, no vendor call, no AWS write. REFUSE a criterion you cannot meet as written, and report
   the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_grants.py
infra/aws/ec2/opal-gateway/tests/test_admin_grants.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `app/admin_api.py`, `app/owner_gate.py`, `app/access_state.py`, `app/data_entitlement.py`,
`app/config.py`, `ops/schwab_entitlement_admin.py` (under `infra/aws/ec2/opal-gateway/`).

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W2-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t4.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t4.AC2.sh; echo "exit=$?"</invocation><expect>live store: NO-PROFILE; bogus table: STORE-UNAVAILABLE -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/NFRA_MCPORTAL.TO-MP-t-4.grant-handlers.proof_of_spec.json`. Report once: what you changed and where, the commit hash, the hookup line you need, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S5 + S7 backend. Merge HELD with MP-t-1's until NFRA_OPALAI's OA-t-6 closes. Hookup at merge: the
router registration line in `app/admin_api.py`.

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
