# NFRA_OPLGTW task order -- `OG-ed-1` -- the legacy `/callback` consent branch exempts the MASTER-ADMIN tier from the email deny record, and nobody else (round 47; the CTO half of `OG-gv-1` names `email_deny` handling option 2, msg 36207 @31e0a20c20; the CVO concurs @48d273c72b)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ed-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ed-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~175</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the CTO's signed half of `OG-gv-1` (message 36207, 2026-10-20 13:37Z): "exempt the master-admin tier only; a test proving a non-admin with a deny record still gets a 403". The browser routes already exempt a master admin (`OG-en-14`); this is the same exemption, one guarded check, on the legacy consent branch.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ed-1` (decomposition addendum R3-T.124, amendment A10, round 47, workstream ENRICH-R47-J)

WHY. `app/data_entitlement.py::email_denial(email, store=None, route_class=None)` returns 403 when an `email_deny` record exists for the email. `OG-en-14` added a route class: with `route_class == INTERNAL_PAGE` and `_master_admin_email(email)` true (the email is EXACTLY one `MASTER_ADMIN_EMAILS` entry; fails closed) it returns `None` before the store is read. The legacy GUI consent flow (`app/server.py`, the `/callback` branch after `token_broker.read_state`, about line 681) and the second check inside `app/token_broker.py::redeem_consent` (about line 393) pass NO class, so a master admin with a deny record would be refused 403 there. `OG-gv-1` will write that record for the owner (`activate()` re-creates it), so this branch must exempt the master-admin tier first.

DO, in these files and nothing else:
1. `infra/aws/ec2/opal-gateway/app/data_entitlement.py`:
   - add `CONSENT = "consent"` on the line after `INTERNAL_PAGE = "internal_page"`;
   - in `email_denial`, change the exemption test from `route_class == INTERNAL_PAGE and _master_admin_email(email)` to `route_class in (INTERNAL_PAGE, CONSENT) and _master_admin_email(email)`;
   - update the comment on the `"/callback": "consent"` entry of `BROWSER_ROUTE_CLASSES` (it currently says "no exemption") to say the master-admin tier is exempt (OG-ed-1) and every other email gets the record verdict, and extend the `email_denial` docstring's last sentence the same way. No other change; `_master_admin_email` is not touched.
2. `infra/aws/ec2/opal-gateway/app/server.py`: in the legacy consent branch, change `denial = await _email_denied(email)` (about line 681, right after the comment naming row W3-S22) to `denial = await _email_denied(email, route_class=data_entitlement.CONSENT)`. Update the docstring of `_email_denied` only where it says the `/callback` branch passes none. Touch no other call of `_email_denied`.
3. `infra/aws/ec2/opal-gateway/app/token_broker.py`: in `redeem_consent`, change `data_entitlement.email_denial(principal.email)` to `data_entitlement.email_denial(principal.email, route_class=data_entitlement.CONSENT)`. One line.
4. NEW `infra/aws/ec2/opal-gateway/tests/test_og_ed1.py`, at least FOUR tests, modelled on `tests/test_og_en14.py` (read it: it imports `_FakeTable` and `_seed_deny` from `tests/test_email_deny.py`, monkeypatches `cfg.MASTER_ADMIN_EMAILS` to one admin email, and uses ADMIN `andrew@opalinvest.com`, NON_ADMIN `alyssa@opalinvest.com`). Offline, fakes only:
   - `test_oged1_ac01`: a master admin WITH an active deny record is not denied on class `data_entitlement.CONSENT` (None) and the fake store records ZERO `get_item` reads; positive control: the same record refuses her with no class (403).
   - `test_oged1_ac02`: a NON-admin WITH a deny record gets 403 on class CONSENT and the record was read; the same non-admin against an unreadable store gets 503; a lookalike of the admin (`xandrew@opalinvest.com`) with a record gets 403.
   - `test_oged1_ac03`: `token_broker.redeem_consent` with `_exchange_code`, `verify_upstream_id_token`, `oidc_nonce`, `_consent_scope_list`, `_write_cache`, `_principal_owner` and `_email_owner` stubbed: for the admin with a deny record it RETURNS the principal; for the non-admin with a record it raises `token_broker.EmailDenied` with `status == 403`.
   - `test_oged1_ac04`: `inspect.getsource(server)` (import `app.server` as `tests/test_og_en14.py` does) shows the legacy consent branch passes `route_class=data_entitlement.CONSENT` to `_email_denied`, and `asyncio.run(server._email_denied(ADMIN))` with no class is still 403 for the admin with a record.
   Do not edit `tests/test_og_en14.py`, `tests/test_email_deny.py` or any test other than the two named in item 5.
5. (AMENDED 2026-10-20 ~14:2xZ, ruling on worker row Z-W175-S1) Two EXISTING tests stub the function you changed with a one-argument lambda, which now raises `TypeError` at the new `route_class=` call: `tests/test_scoped_consent_r253.py` (about line 117) and `tests/test_login_admit_r24.py` (about line 162) both read `monkeypatch.setattr(tb.data_entitlement, "email_denial", lambda email: None)` (r24 spells it `h.mp.setattr(...)`). In each, change ONLY that lambda to `lambda email, route_class=None: None`. No other line of either file changes.

## 2. BOUNDS

- Write only the files above (the four of items 1 to 4 and the two stubs of item 5), `W/` and, if a row is needed, the channel. No other product file, no other test, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/tests/test_og_ed1.py
infra/aws/ec2/opal-gateway/tests/test_scoped_consent_r253.py
infra/aws/ec2/opal-gateway/tests/test_login_admit_r24.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~175/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W175-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ed-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ed1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)class consent: not denied, store reads 0: ok.*non-admin with a deny record, class consent: 403 and the record was read: ok.*unreadable store, class consent: 503: ok.*NO class keeps today's verdict: 403: ok.*lookalike of the admin, class consent: 403: ok.*redeem_consent for the master admin with a deny record returns: ok.*redeem_consent for the non-admin with a deny record denied: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ed-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ed1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_ed1\.py: (?:[4-9]|[1-9]\d+) passed, 0 failed.*neighbours \(5\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ed-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ed1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/data_entitlement\.py against the pin:.*: ok.*app/server\.py against the pin:.*: ok.*app/token_broker\.py against the pin:.*: ok.*tests/test_og_ed1\.py: (?:[4-9]|[1-9]\d+) test functions.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the behaviour, graded by a script of the issuer's, independent of your tests. `AC2`: your tests and the five neighbours pass (the one carried red, `test_ogz1_ac08`, is allowed). `AC3` (a bound): the edit is the exemption and its two call sites, against the pinned blobs.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ed-1.round-47-the-master-admin-exemption-on-the-legacy-callback-consent-branch.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-J, amendment A10 of R3-T.124. Source: the CTO's half of `OG-gv-1` (msg 36207): option 2, "exempt the master-admin tier only; a test proving a non-admin with a deny record still gets a 403; its own never-widen ask, riding `OG-rl-18` if that release is not yet cut". `OG-gv-1` Phase B runs only when `OG-rl-18` AND this exemption are live.
- Widening, plainly: a master admin whose email has an `email_deny` record can complete the legacy `/callback` consent sign-in (before: 403); no other email's verdict changes; no tool, grant or scope changes.
- `<risk>WORLD</risk>` is the gateway-path floor. Pre-cut: `AC1` base FAIL as expected (admin denied, reads 2; `redeem_consent` denies the admin); `AC2` base FAIL as expected (new test file absent); `AC3` base FAIL as expected (0 lines changed, no test file). Arm: the three product edits applied in the shared tree read `AC1` PASS and `AC3` PASS on the three bounds (the test-file count read 0, as expected), then were reverted by edit. The four neighbours read 32 passed and 1 failed (`test_ogz1_ac08`, the carried red) at the base.
- Pins: `data_entitlement.py` blob `aff1cf560f`, `server.py` blob `9d740ed043`, `token_broker.py` blob `e5df633a37`. `server.py` and `token_broker.py` equal the live ref (`13917ef993`) at the issuance, so `OG-rl-18`'s take list gains them whole.
- AMENDED 2026-10-20 ~14:2xZ (2.0.0_SA_COO~O, ruling on worker row NFRA_OPLGTW-Z-W175-S1): the worker found that two existing tests stub `email_denial` with a one-argument lambda (my dry-run of the neighbours at the base ran four files and missed `test_login_admit_r24.py`, which also stubs it). Item 5 and two `<paths>` entries added; `ed1.AC2` gains `tests/test_login_admit_r24.py` as a fifth neighbour (7 passed at the base). Gate limb: none graded (an existing tree order that declares no placeholders).

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-J</workstream>
<slot>~175</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
