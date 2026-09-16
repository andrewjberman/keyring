# TO NFRA_OPLGTW.TO-OG-a-1 -- durable OAuth

<to_id>NFRA_OPLGTW.TO-OG-a-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-a-1` | **outcome_ref:** FWD-1, FWD-3, FWD-7 | **depends_on:** `OG-d-1` | **slot:** ~3, queue position 2

---

## WORKER FACE

### THE CELL

`OG-a-1` -- **durable OAuth** in `infra/aws/ec2/opal-gateway/app/oauth_as.py` and the token/registration routes of
`app/server.py`: client registration with exact redirects, resource binding, one-use codes and refresh families, all
stored through `app/access_state.py` (`OG-d-1`, merged at your hand-off).

What the source does today (certified L4 rectangle, S1-auth, source read @5dd24300f7): *"DCR and authorize accept HTTP
exact-host loopback redirects only; S256 PKCE is required. Authorization codes are popped under a process lock before
checking redirect, optional client_id and verifier. Clients, pending requests and codes are process-local"*; *"Hosted
Claude HTTPS callback is rejected. Unknown client_id is accepted for loopback authorize; redemption checks client_id only
when nonempty"*; *"Authorize and token handlers do not consume or validate resource parameters"*; *"Refresh validates the
incoming JWT but neither consumes it nor compares the request's client_id/resource. The token handler always issues
configured scope ... there is no atomic rotation/replay/family store."* Re-ground each against the file before you change it.

What it must do -- the PRD's C1, verbatim, the paragraphs this cell owns:
- *"Register and exactly match `https://claude.ai/api/mcp/auth_callback`. Preserve existing Code loopback redirects only
  for registered clients, with RFC loopback port handling and no arbitrary hosted redirects. Require the issued client ID
  in authorization-code redemption; remove the current unregistered-loopback/optional-client behavior through an explicit
  reconnect migration. DCR is JSON; token exchange is form encoded. Metadata must advertise the same resource, issuer,
  endpoints, scope and S256 behavior actually enforced. Discovery, registration and ordinary token/auth responses have a
  10-second budget; refresh has 30 seconds."*
- *"Store client registration, authorization codes and refresh families durably in `opal-gateway-access-state`. Codes are
  single use; refresh tokens are cryptographically random, stored only as hashes, bound to immutable
  principal/client/resource/scope and family. A conditional DynamoDB transaction consumes the current generation and
  installs the next. Reuse revokes the family; a concurrent loser receives invalid_grant and cannot mint a second valid
  successor. No grace period that leaves a replay usable. Logout/revocation invalidates the family. Use 15-minute access
  tokens, 30-day absolute and 7-day idle refresh expiry; check logical expiry even if TTL deletion is late. Record expiry
  explicitly and scope reductions on refresh; never remint a broader configured scope."*
- *"Persist client records so restarting a worker does not forget clients. Failure of durable state fails new/refresh
  exchanges closed; it must not silently select an old stateless branch."*
- *"Persist the pending upstream authorization state with a short logical expiry, state/nonce and client/resource
  bindings; a restart between authorize and callback either resumes that exact bound transaction or returns an explicit
  restart-login error, never guesses identity."*

Contract limits: `access_token_seconds` 900, `refresh_absolute_seconds` 2592000, `refresh_idle_seconds` 604800,
`auth_endpoint_seconds` 10, `refresh_endpoint_seconds` 30. The immutable principal (tid/oid) and the legacy cutover are
the NEXT cell's (`OG-a-2`); here, bind families to whatever principal key the current code carries, behind one function
`OG-a-2` will change.

**Read:** the PRD's "C1 - identity, OAuth and migration"; `app/oauth_as.py`, `app/server.py` (routes and metadata),
`app/access_state.py`; `tests/test_jwt_cve_lock.py` (existing token tests, which must stay green).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGA1-AC1" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC1` (`test_oga1_ac01`) -- registration (JSON) accepts exactly `https://claude.ai/api/mcp/auth_callback` and registered loopback redirects with RFC 8252 port handling.

<criterion id="OGA1-AC2" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC2` (`test_oga1_ac02`) -- registration refuses an arbitrary hosted redirect.

<criterion id="OGA1-AC3" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC3` (`test_oga1_ac03`) -- (difference) code redemption without the issued `client_id` is refused, and the same redemption with it succeeds.

<criterion id="OGA1-AC4" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC4` (`test_oga1_ac04`) -- authorization with an unregistered `client_id` is refused.

<criterion id="OGA1-AC5" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC5` (`test_oga1_ac05`) -- a requested resource other than the advertised one is refused at authorize and at token exchange.

<criterion id="OGA1-AC6" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC6` (`test_oga1_ac06`) -- PKCE S256 is required and `plain` is refused.

<criterion id="OGA1-AC7" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC7` (`test_oga1_ac07`) -- a second redemption of one authorization code returns invalid_grant.

<criterion id="OGA1-AC8" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC8` (`test_oga1_ac08`) -- a refresh rotates the family's generation by one conditional transaction.

<criterion id="OGA1-AC9" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC9` (`test_oga1_ac09`) -- reuse of a consumed refresh token revokes the family, so the newest token then fails too.

<criterion id="OGA1-AC10" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC10` (`test_oga1_ac10`) -- N concurrent refreshes of one token yield exactly one success, and every loser gets invalid_grant with no second valid successor.

<criterion id="OGA1-AC11" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC11` (`test_oga1_ac11`) -- a refresh never returns a broader scope than the family's, and a narrower requested scope is recorded.

<criterion id="OGA1-AC12" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC12` (`test_oga1_ac12`) -- access tokens last 15 minutes and refresh families 30 days absolute and 7 days idle, with logical expiry enforced while records are present.

<criterion id="OGA1-AC13" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac13 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC13` (`test_oga1_ac13`) -- (difference) a restart between authorize and callback resumes the bound transaction or returns an explicit restart-login error, and never guesses an identity.

<criterion id="OGA1-AC14" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC14` (`test_oga1_ac14`) -- client registrations survive a process restart.

<criterion id="OGA1-AC15" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac15 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC15` (`test_oga1_ac15`) -- (difference) with the state store failing, new and refresh exchanges fail closed, and with it healthy they succeed.

<criterion id="OGA1-AC16" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac16 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC16` (`test_oga1_ac16`) -- the advertised metadata equals the enforced configuration field by field.

<criterion id="OGA1-AC17" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac17 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC17` (`test_oga1_ac17`) -- token exchange is form encoded.

<criterion id="OGA1-AC18" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py::test_oga1_ac18 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC18` (`test_oga1_ac18`) -- under the harness load, discovery, registration and token responses stay under 10 seconds and refresh under 30 seconds of server time.

<criterion id="OGA1-AC19" cell_refs="OG-a-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests -q -p no:cacheprovider --color=no -m "not live" -k "not test_scoped_deny_by_default"</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGA1-AC19` -- the whole `infra/aws/ec2/opal-gateway/tests/` suite passes, count printed, with the one known red test of row NFRA_OPLGTW-S1 deselected by name.

<expected_criteria>OGA1-AC1, OGA1-AC2, OGA1-AC3, OGA1-AC4, OGA1-AC5, OGA1-AC6, OGA1-AC7, OGA1-AC8, OGA1-AC9, OGA1-AC10, OGA1-AC11, OGA1-AC12, OGA1-AC13, OGA1-AC14, OGA1-AC15, OGA1-AC16, OGA1-AC17, OGA1-AC18, OGA1-AC19</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-d-1` merged). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_oauth_durable.py`; write exactly that name. Your criteria run offline against moto; an upstream identity provider is a local test issuer with a locally generated key, never Entra.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1) and is deselected by name in AC19. Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. No existing test is edited to make it pass.
- **Nothing deploys.** This cell changes source; the release is `OG-r-1`'s.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.** Test keys are generated at test time and never committed.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/oauth_as.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-a-1`, round 1 (section 3, S1).
<owned_cells>OG-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGA1-AC1` .. `OGA1-AC19` (19). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-a-1.durable-oauth.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGA1-AC1,OGA1-AC2,OGA1-AC3,OGA1-AC4,OGA1-AC5,OGA1-AC6,OGA1-AC7,OGA1-AC8,OGA1-AC9,OGA1-AC10,OGA1-AC11,OGA1-AC12,OGA1-AC13,OGA1-AC14,OGA1-AC15,OGA1-AC16,OGA1-AC17,OGA1-AC18,OGA1-AC19`
BEFORE the `complete` flip. Result file `durable-oauth.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell; its code reaches users only through OG-r-1, which notice N-1 precedes.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell's state calls go through OG-d-1's adapter under OG-i-1's grant; it adds no new AWS service.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path, the RFC 9700 citation in C1). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 2, handed after `OG-d-1` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770. The suite baseline at the cut: 76 passed, 1 failed (row
NFRA_OPLGTW-S1), 34 subtests passed on Python 3.12.10.
