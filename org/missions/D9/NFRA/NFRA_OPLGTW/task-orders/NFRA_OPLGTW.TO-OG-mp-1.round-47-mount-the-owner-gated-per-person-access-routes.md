# NFRA_OPLGTW task order -- `OG-mp-1` -- mount `admin_people_access.routes` in `app/admin_api.py` behind the owner gate (round 47; the CTO's ferry 2026-10-20 17:30Z for NFRA_MCPORTAL PRD v0.10 @ee76bb0bfc: "mount admin_people_access.routes behind owner_only in your next batched release, under never-widen"; the served People panel's API answers 404 today, CRO~Z brief F3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mp-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mp-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~176</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this order (the handlers reuse `admin_grants`' grant-writer function and env, already configured for the grant routes).
comp-adversary: DECLARED-NOT-APPLICABLE -- the CTO's ferry of 2026-10-20 17:30Z naming this seat's next batched release; the module `app/admin_people_access.py` (PD.3) already exists on trunk with its own tests and states in its docstring: "Mount (the release cell adds it in app/admin_api.py; this module does not edit that file): *admin_people_access.routes".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-mp-1` (decomposition addendum R3-T.124, amendment A12, round 47, workstream ENRICH-R47-K)

WHY. `app/admin_people_access.py` defines `routes` (two `Route` objects on `/people/{tid}/{oid}/access`, GET and POST, each decorated with `owner_only`), but `app/admin_api.py` never mounts them, so the API answers 404. The mount is the only missing piece.

DO, in two files and nothing else (under `infra/aws/ec2/opal-gateway/`):
1. `app/admin_api.py`: add the import line `from . import admin_people_access` directly after the line `from . import admin_people` (about line 24), and add the entry `    *admin_people_access.routes,` to the `routes = [...]` list directly after the line `    *admin_tenants.routes,` (about line 68). Two added lines, none removed. Do not touch any other line, and do not edit `app/admin_people_access.py`.
2. NEW `tests/test_og_mp1.py`, at least THREE tests, offline, fakes only, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import (model on `tests/test_admin_people_access.py` and `tests/test_owner_gate.py`: read how they stub the owner identity and the access-state store; copy that mechanism, do not invent one):
   - `test_ogmp1_ac01`: with a starlette `TestClient(admin_api.admin_app)` and NO identity header, `GET` and `POST` on `/people/t1/o1/access` answer `401` with `no verified identity` (the owner gate refuses; before the mount they answered 404), and `GET /whoami` also answers 401 (the control).
   - `test_ogmp1_ac02`: the route table `admin_api.routes` holds the two new paths exactly once each (GET with HEAD, and POST), the total count is 18, and every `Route` object of `admin_people_access.routes` is the same object that is mounted.
   - `test_ogmp1_ac03`: with the owner stub of `tests/test_admin_people_access.py`, `GET /people/{tid}/{oid}/access` through `admin_api.admin_app` reaches the handler (a seeded `person_access` record is answered with the module's own shape; read the module and its tests for that shape); an unseeded person answers what the module answers for an absent record.

## 2. BOUNDS

- Write only the two files above, `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/tests/test_og_mp1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~176/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W176-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mp1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the new GET and POST answer 401 no verified identity with no owner header: ok.*controls: /whoami 401, /people 401, an unmounted path 404: ok.*the route table holds the two new routes exactly once each; count 18 \(want 16 \+ 2 = 18\): ok.*every Route object of admin_people_access\.routes is the one mounted: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mp1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_mp1\.py: (?:[3-9]|[1-9]\d+) passed, 0 failed.*neighbours \(5\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-mp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/mp1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/admin_api\.py against the pin: 0 removed, [2-4] added.*: ok.*app/admin_people_access\.py byte-equal to HEAD: ok.*tests/test_og_mp1\.py: (?:[3-9]|[1-9]\d+) test functions.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the mount, graded by a script of the issuer's, independent of your tests. `AC2`: your tests and the five admin neighbours pass (31 passed at the base). `AC3` (a bound): the edit is the two mount lines, against the pinned blob.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mp-1.round-47-mount-the-owner-gated-per-person-access-routes.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-mp-1.round-47-mount-the-owner-gated-per-person-access-routes.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-K, amendment A12 of R3-T.124. Source: the CTO's ferry 17:30Z (NFRA_MCPORTAL PRD v0.10). The mount rides `OG-rl-18` (batch17): `OG-rl-17` is frozen at its signed bytes; the module `admin_people_access.py` is already in batch16's take list, the mount is the one line batch16 does not carry.
- Widening, plainly: two new OWNER-GATED routes answer where they answered 404 (GET reads one person's `person_access` record; POST invokes the grant-writer Lambda, which writes the record: the gateway writes nothing itself). No new tool, no `tools/list` change, no IAM change in this order. A person_access record cannot admit the `client_*` tools (row Z-S432), so the panel the routes serve cannot widen a principal's tool reach by itself.
- FWD-29 ("person_access and the data grant admit through one rule", same ferry) is NOT this order: it changes `decide()` and joins the round-48 per-firm client grant cell.
- Pre-cut: `AC1` base FAIL as expected (GET 404 POST 404; count 16); `AC2` base FAIL as expected (new test file absent; the five neighbours read 31 passed); `AC3` base FAIL as expected. Arm: the two mount lines applied in the shared tree read `AC1` PASS and `AC3`'s first two lines PASS, then were reverted by edit. Pin: `admin_api.py` blob `2fb26985d9` (equal to the live ref `13917ef993`).

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-K</workstream>
<slot>~176</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
