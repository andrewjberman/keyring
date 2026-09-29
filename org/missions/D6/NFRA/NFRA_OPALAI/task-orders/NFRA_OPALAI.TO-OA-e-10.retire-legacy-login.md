# NFRA_OPALAI task order -- `OA-e-10` -- ROUND 2, E10: census the legacy /login GUI consent, then retire or narrow it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~16</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a census and a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only SSM reads of the host's journal and cache directory listing through existing access; no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the change REMOVES or NARROWS a surface; AC3 is the control that the email-deny guard stands.
EGRESS CLASS, declared: AWS READ on Opal's own plane (SSM reads of journald lines and file names; no secret, token or cache content is read). Development downloads are covered by Andrew-direct record @f8d1103a38. No vendor call.
</preflight>

## 1. THE CELL -- `OA-e-10` (round 2, decomposition section R2.1; row NFRA_OPLGTW-Z-S7)

The gateway `infra/aws/ec2/opal-gateway/` still serves a legacy GUI consent route. It predates the MCP `/authorize`
sign-in:
- `Route("/login", login)` at `app/server.py:923`, handler `login()` at `:450-459`;
- its access-layer arm at `:199` (the `path == "/login" or sprint_view.is_sprint_path(path)` branch);
- the legacy branch of the shared `callback()` at `:464`: a non-bridge Fernet state redeems a Graph consent that
  `app/token_broker.py` caches under the caller's EMAIL.

For a restricted profile that cache reaches no usable tool, so the route is inert, but nothing needs it. **Census first.
Remove it only on ZERO dependents; otherwise narrow it.**

1. **The census.** Write `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~16/E10_LOGIN_CENSUS.md`.
   - `LOGIN_USES:` the number of `/login` requests in the gateway's own request log since the MCP `/authorize`
     sign-in went live. The service runs uvicorn with its default access log (`deploy/opal-gateway.service:16`), so
     read `journalctl -u opal-gateway` over SSM on `i-07dccb1615503ac99`. Count only; print no email.
   - `WINDOW: <first-date>..<last-date>`: the span the journal ACTUALLY covers, measured, never assumed. Name the
     go-live date of `/authorize` from git (the commit that registered it) and say whether the journal reaches back to
     it.
   - `SOURCE:` the exact command.
   - `DEPENDENTS:` the number of SERVER-HELD identities that still read the email-keyed cache `/login` writes. Check
     each of `/otp/*`, `/ms/*` (`MS_INGEST_IDENTITY`, `app/config.py:209`) and any other caller of
     `token_broker.get_token(email)` for a server-held identity. For each one, decide whether its token cache can be
     (re)minted ONLY through `/login` + the legacy callback, or also through another path (a bridge sign-in, a bootstrap
     exchange). Read the code, and the host's cache FILE NAMES (never contents).
   - Name each dependent: which identity, which route, and why.
   - `BRANCH: REMOVE` when `DEPENDENTS` is 0, else `BRANCH: NARROW`. Each of these five keys starts its own line.
2. **The build, on the census's branch** (gateway code only; nothing is released here):
   - **REMOVE:** delete the `/login` route, `login()`, the `"/login"` half of the `:199` condition (the `/sprint*` arm
     STAYS, byte-equivalent in behaviour), and the legacy non-bridge branch of `callback()`. After the change:
     - a legacy-state `/callback` is refused with a plain 4xx, and `redeem_consent` is never called;
     - the bridge branch (Claude's MCP connect) is unchanged.
   - **NARROW:** `/login` admits only the server identities the census named (a config list, fail closed when empty),
     and refuses any other caller with 403 BEFORE any consent URL is built.
   - Either way, the OG-e-2 email-deny guard stays. `tests/test_email_deny.py` keeps its four `/sprint*` denial arms.
     You may drop `("GET", "/login")` from its `_ROUTES` table and adapt `test_legacy_callback_403_redeem_consent_never_called`
     ONLY on the REMOVE branch, and ONLY so the removed route is asserted gone. Never weaken a `/sprint*` arm.
   - New tests in `tests/test_login_retire.py`, including the one named for your branch:
     - `test_login_removed`: `/login` answers 404, and a legacy-state `/callback` is refused without `redeem_consent`;
     - `test_login_narrowed`: a non-listed identity gets 403 with no consent URL built, and a listed one is redirected.
     Use the fixtures `tests/test_email_deny.py` already uses (a fresh app process, a stubbed ALB identity, no network).

## 2. BOUNDS

1. Nothing is deployed. The release of this change is NOT this round's: it needs never-widen halves, and it is cut at
   round 2's L10 or rides E9's move.
2. `app/browser_oidc.py` is edited ONLY if the census names it as part of the `/login` path; say so in the census.
   `app/token_broker.py`, `app/oauth_as.py` and every `/otp`, `/ms` route are READ, never edited.
3. No token, cache content, secret or email is printed, committed or put in the census.
4. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/browser_oidc.py
infra/aws/ec2/opal-gateway/tests/test_login_retire.py
infra/aws/ec2/opal-gateway/tests/test_email_deny.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~16/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `app/token_broker.py`, `app/oauth_as.py`, `app/otp.py`, `app/config.py`, `app/identity.py`,
`deploy/opal-gateway.service`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W16-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-10"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e10.AC1.sh; echo "exit=$?"</invocation><expect>login_uses, window, source, dependents named; branch consistent=yes (REMOVE iff dependents=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-10"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e10.AC2.sh; echo "exit=$?"</invocation><expect>the test named for the census's branch passed>=1; failed/errored=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-10"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e10.AC3.sh; echo "exit=$?"</invocation><expect>sprint routes asserted=4; email-deny suite 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~16/NFRA_OPALAI.TO-OA-e-10.retire-legacy-login.proof_of_spec.json`.
Report once:
- the census's five lines;
- each dependent named;
- the branch taken;
- what you changed, with file:line;
- the commit hashes;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E10 (row NFRA_OPLGTW-Z-S7). WORLD by the infra floor; nothing deploys. The write surface adds
`tests/test_email_deny.py` beyond the decomposition's R2.1 list, because the REMOVE branch changes what that suite's
`/login` arm can assert. AC3 is the control that the OG-e-2 guard's `/sprint*` arms stand.

SPAWN ONLY WHEN: at the cut (slot `~16`).

Dry-run at base (CLOUD `c8df03c408`, ~20:5xZ):
- e10.AC1 base: FAIL as expected (census not committed).
- e10.AC2 base: FAIL as expected (no BRANCH in a committed census).
- e10.AC3 base: PASS as expected (control: 4 sprint routes asserted; 11 passed, 0 failed).

<status>complete</status>
<round>2</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
