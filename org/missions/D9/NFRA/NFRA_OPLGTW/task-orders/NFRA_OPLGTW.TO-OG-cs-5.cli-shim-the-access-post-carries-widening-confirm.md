# NFRA_OPLGTW task order -- `OG-cs-5` -- the owner-gated access POST carries an optional boolean `widening_confirm` into the grant-writer event (cli-shim workstream, wave 1; COO~MP's finding of 2026-10-21 15:15Z, named in PRD v3.19 FWD-24's gateway work)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-5</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~181</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reuses the grant-writer function and env already configured.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is COO~MP's measured finding (ferry 2026-10-21 15:15Z): the deployed grant writer (`lambda_function.py` line 418) refuses any change that adds to `tools_allow` or `channels_allow` unless the event carries `widening_confirm: true`, and the gateway's `invoke_set_person_access` drops it; the carry is the one missing piece, accepted by the issuer and named in the CTO's FWD-24 work.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cs-5` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-A)

WHY. `POST /api/admin/people/{tid}/{oid}/access` (owner-gated) invokes the grant-writer Lambda with `{action, tid, oid, change, expect_revision, owner_header}`. The writer refuses any change that ADDS to `tools_allow` or `channels_allow` unless the event also carries `widening_confirm: true` (the owner's explicit confirmation of a widening). The gateway's POST never forwards that flag, so every widening is refused. Deny-list adds (narrowings) need no flag and must stay exactly as they are.

DO, in two files and nothing else (under `infra/aws/ec2/opal-gateway/`):

1. `app/admin_people_access.py`, a SMALL edit (3 to 14 lines added, at most 6 removed, against the blob `65f9faa4a9`):
   - `shape_refusal(body)`: accept an OPTIONAL top-level key `widening_confirm` in the body. When present it must be a real boolean (`True` or `False`); a string, the integer `1`, `None` or anything else is refused with a reason that names `widening_confirm` (say "widening_confirm must be a bool"). When absent, behaviour is exactly as today (a valid body returns `''`; the existing refusals are unchanged).
   - `invoke_set_person_access(tid, oid, change, expect_revision, owner_header, client=None, widening_confirm=False)`: add the keyword argument `widening_confirm` (default False). The event gets the extra key `"widening_confirm": True` ONLY when the argument is `True`; when it is `False` or omitted the event holds EXACTLY the six old keys, no `widening_confirm` key at all (the event must be byte-identical to today's for every caller that does not send the flag).
   - `access_post`: read `body.get("widening_confirm")` (a bool or absent after `shape_refusal` passes) and pass it to `invoke_set_person_access` as `widening_confirm=<that bool or False>`.
   Touch no other line and no other function; do not edit any other file under `app/`.
2. NEW `tests/test_cs5_widening_confirm.py`, at least FOUR tests, offline, fakes only, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import (model on `tests/test_admin_people_access.py`: read how it stubs the owner identity, the access-state store and the lambda client, and copy that mechanism, do not invent one): `shape_refusal` accepts `widening_confirm` true and false and refuses `"yes"`, `1` and `None` naming `widening_confirm`; a POST through the app with `widening_confirm: true` reaches the fake lambda client with an event holding `"widening_confirm": true`; a POST without it, and one with `false`, reach it with an event of exactly the six old keys; an old-style narrowing body (a `tools_deny` add) still returns the writer's verdict unchanged.

## 2. BOUNDS

- Write only the two files above, `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call (the lambda client is a fake in every test).
- Counts and hashes only: no e-mail address, account number or token in any file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_people_access.py
infra/aws/ec2/opal-gateway/tests/test_cs5_widening_confirm.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~181/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W181-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)widening_confirm true and false are well formed .*: ok.*a non-bool widening_confirm is refused naming widening_confirm .*: ok.*control: a body without widening_confirm is well formed; unknown key and missing expect_revision still refused: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)widening_confirm=True: the event holds widening_confirm true and the six old keys .*: ok.*false and omitted: the event holds EXACTLY the six old keys .*: ok.*the route reads widening_confirm from the body and hands it to the invoke .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cs-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs5.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/admin_people_access\.py against the pin: (?:[3-9]|1[0-4]) added, [0-6] removed .*: ok.*files under app/ that differ from HEAD: \['admin_people_access\.py'\] .*: ok.*tests/test_cs5_widening_confirm\.py: [4-9]\d* test functions.*: ok.*new file tests/test_cs5_widening_confirm\.py: [4-9]\d* passed, 0 failed.*neighbours \(2\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the body shape, `AC2`: the writer event, both graded by issuer-written probes independent of your tests. `AC3`: the footprint (a bound, against the pinned blob and the base commit) and your tests plus two neighbours.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-5.cli-shim-the-access-post-carries-widening-confirm.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-5.cli-shim-the-access-post-carries-widening-confirm.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-A, wave 1, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`. Source: COO~MP's ferry 2026-10-21 15:15Z; accepted by the issuer (ferry 15:36Z). It also lets Andrew's confirm write a WIDENING `person_access` add through the People route once the cli-shim release is live.
- Widening, plainly: none by this order (a flag the owner sends is forwarded; the writer, not the gateway, decides; deny adds are untouched). The release that carries it is a later order with its own never-widen halves.
- Pre-cut: `AC1` base FAIL as expected (a non-bool `widening_confirm` is accepted); `AC2` base FAIL as expected (the keyword is unexpected); `AC3` base FAIL as expected (0 added, the new test file absent). Pin: `admin_people_access.py` blob `65f9faa4a9`.

<status>pending</status>
<round>48</round>
<workstream>CLISHIM-A</workstream>
<slot>~181</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
