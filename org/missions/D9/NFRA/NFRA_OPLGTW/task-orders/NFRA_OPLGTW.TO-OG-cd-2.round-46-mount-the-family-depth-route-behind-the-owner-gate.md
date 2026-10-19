# NFRA_OPLGTW task order -- `OG-cd-2` -- mount the `family_depth` route in `app/admin_api.py` behind the owner gate: two added lines and one test file (round 46; round-45 analysis A1 item 3; PRD v2.6 FWD-20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cd-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cd-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~163</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the read grant the route needs is the separate order `OG-cd-3` (`family_depth_read_iam.tf`).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-45 analysis amendment A1, list item 3 (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round45.md` @6018fc83fd): "mount the `family_depth` route".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cd-2` (decomposition addendum R3-T.123, amendment A1, round 46, workstream ENRICH-R46-B)

WHY. `infra/aws/ec2/opal-gateway/app/family_depth.py` (cell `OG-cd-1`, live in the eleventh release) defines `async def families(request)` (the JSON of `read()`), but nothing mounts it, and the handler is NOT decorated with the owner gate (every sibling handler is). The admin router `app/admin_api.py` lists its routes in the `routes` list and already imports `owner_only` (`from .owner_gate import owner_only`). FWD-20 needs the read reachable, and reachable only by the dashboard owner. Read `app/family_depth.py` lines 395 to the end, `app/admin_api.py`, `app/owner_gate.py` (`owner_only`), and `tests/test_admin_gateway_breakdown.py` (how a test stubs the ALB identity) first.

DO, in `infra/aws/ec2/opal-gateway/app/admin_api.py` ONLY (plus the new test file), by the smallest change that works. The diff against the base blob is EXACTLY TWO ADDED LINES and no removed line:
1. After the line `from . import admin_people` add `from . import family_depth`.
2. In the `routes` list, after the line `Route("/people", admin_people.people, methods=["GET"]),` add, with the same indentation: `Route("/gateway/families", owner_only(family_depth.families), methods=["GET"]),`.
   Do NOT edit `app/family_depth.py` (it is already live and must stay byte-equal), `app/owner_gate.py` or any other file.
3. **The new test file `infra/aws/ec2/opal-gateway/tests/test_og_cd2.py`** with EXACTLY these three tests (names fixed). Build the app from the REAL `app.admin_api.admin_app` (not a hand-built Starlette), `TestClient(admin_app, base_url="http://localhost", raise_server_exceptions=False)`, `DASHBOARD_OWNER_EMAILS` set to `("andrew@opalinvest.com",)` through `monkeypatch` on `app.config.get_config()`, and the identity stubbed as `tests/test_admin_gateway_breakdown.py` does it (`monkeypatch.setattr(app.owner_gate, "_alb_oidc_identity", fake)`; `fake` raises `app.identity.IdentityError` for "no identity" and returns an email otherwise). Replace `app.family_depth.read` with a stub that records each call and returns `{"denominator": 1, "families": []}`. Restore everything after each test.
   - `test_ogcd2_ac01`: `app.admin_api.routes` holds exactly one route whose `path` is `/gateway/families`; its methods include GET; and its `endpoint` is NOT `app.family_depth.families` itself (the gate wraps it).
   - `test_ogcd2_ac02`: `GET /gateway/families` with no identity answers 401; with a verified non-owner (`someone.else@opalinvest.com`) answers 403; and the stubbed `read` was called ZERO times by those two requests.
   - `test_ogcd2_ac03`: with the owner (`andrew@opalinvest.com`) the answer is 200 and the JSON body equals the stub's return value.
   (A reference of this exact test shape passed `cd2.AC1` in the issuer's dry run; write your own from the sibling test.)

## 2. BOUNDS

- Write only `infra/aws/ec2/opal-gateway/app/admin_api.py`, `infra/aws/ec2/opal-gateway/tests/test_og_cd2.py`, `W/` and, if a row is needed, the channel. NO other product file, no other test, no release, no deploy, no Terraform, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address other than the two test addresses above, or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/tests/test_og_cd2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~163/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W163-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/cd2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/cd2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)added lines 2 \(want 2\), removed lines 0 \(want 0\); import line 1 \(want 1\); owner-gated Route line 1 \(want 1\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the route is mounted behind the owner gate: no identity 401, a non-owner 403 with the read never called, the owner 200 with the read's body. `AC2`: the mount is the smallest change, two added lines, none removed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cd-2.round-46-mount-the-family-depth-route-behind-the-owner-gate.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, workstream ENRICH-R46-B, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-45 analysis amendment A1 (msg 35923), item 3, first half. The IAM half is `OG-cd-3`; the release is `OG-ap-50`.
- READING DISCLOSED TO THE CTO: (1) the mount is `owner_only(family_depth.families)` in `admin_api.py`, not a decorator inside `family_depth.py`, so the live module stays byte-equal and the release takes two files. (2) `app/admin_api.py` belongs to NFRA_MCPORTAL; the line is the "release cell adds it" hookup `family_depth.py`'s docstring and `OG-cd-1` already name, two added lines and nothing else, and its owner is told in the ask. (3) The three fixed test names are `test_ogcd2_ac01` to `ac03`.
- Base blob of `app/admin_api.py` at the issuance: `c1885ec0404f45714616addeec961923ff549ed0`. Pre-cut: `AC1` base FAIL as expected (no test file); `AC2` base FAIL as expected (0 added lines). Arms fed to the checks: the issuer's reference implementation (two lines plus a three-test file) passed both and was reverted; a bare `family_depth.families` (no gate), a third added line and a removed import each failed `AC2` as they should.

<status>pending</status>
<status>complete</status>
<round>46</round>
<workstream>ENRICH-R46-B</workstream>
<slot>~163</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
