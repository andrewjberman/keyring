# TO NFRA_OPLGTW.TO-OG-a-2 -- the immutable principal, the legacy cutover and the challenge semantics

<to_id>NFRA_OPLGTW.TO-OG-a-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-a-2` | **outcome_ref:** FWD-1, FWD-3, FWD-7 | **depends_on:** `OG-a-1` | **slot:** ~3, queue position 3

---

## WORKER FACE

### THE CELL

`OG-a-2` -- **the immutable principal, the legacy cutover and the challenge semantics.** Carry Entra's validated `tid`
and `oid` through the signed access token and the request context; reject every legacy token at every protected route;
check family status on every request; and fix the 401/403 behaviour.

What the source does today (certified L4 rectangle, S1-auth): *"Entra login is coupled to Graph authorization.
token_broker requests GRAPH_SCOPES and returns preferred_username/email/upn; context stores only email. No immutable
tenant/object identity propagates in the gateway token or request context."*; *"insufficient_scope is raised with status
403, but _mcp_unauthorized renders every OAuthError as HTTP 401."* Re-ground each before changing it.

What it must do -- the PRD's C1, verbatim, the paragraphs this cell owns:
- *"Use the existing Gateway authorization-server issuer and resource. Entra is the upstream identity provider, not an
  alternative MCP audience. Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata
  only. Validate token signature, issuer, audience, expiry, authorized tenant, nonce/state, client, PKCE S256, redirect
  and requested resource at every applicable exchange. Never accept caller-supplied email, identity headers, role or
  tenant as the authorization identity. Authentication must not require Graph mail/file consent; retain delegated Graph
  acquisition only for tools that use it."*
- *"At cutover, every protected MCP and REST route rejects legacy access JWTs lacking the new token-version and immutable
  principal claims, even while their old exp is still valid ... Access tokens carry a family identifier; every protected
  request checks family status and principal revocation with the current grant. Family logout/reuse revocation therefore
  prevents later use of previously issued access tokens as well as refresh."*
- *"A missing or invalid MCP credential gets 401 with the advertised resource challenge. A valid token lacking an OAuth
  scope gets the specified 403 insufficient_scope response, not the current conversion back to 401. A denied data
  entitlement is a terminal tool authorization error, not an OAuth escalation or a login loop."*

The route census (AC4) is over every route declaration in `app/server.py` at your base (the L4 read counted 27
Route/Mount entries @5dd24300f7; count them yourself and print the denominator). `OG-a-1` (merged at your hand-off)
bound refresh families behind one principal-key function; this cell changes that function to `(tid, oid)`.

**Read:** the PRD's "C1"; `app/token_broker.py`, `app/context.py`, `app/identity.py`, `app/oauth_as.py`, `app/server.py`,
`app/revocation.py`; `tests/test_oauth_durable.py` (the previous cell's tests, which must stay green).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGA2-AC1" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC1` (`test_oga2_ac01`) -- the signed access token and the request context carry the validated Entra `tid` and `oid` and a token-version claim, and email is display metadata only.

<criterion id="OGA2-AC2" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC2` (`test_oga2_ac02`) -- authentication completes without Graph mail or file scopes.

<criterion id="OGA2-AC3" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC3` (`test_oga2_ac03`) -- a Graph-using tool still acquires its delegated Graph token in the harness.

<criterion id="OGA2-AC4" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC4` (`test_oga2_ac04`) -- every protected MCP and REST route rejects an access token lacking the new token-version and principal claims while its `exp` is still valid, over all route declarations, denominator printed.

<criterion id="OGA2-AC5" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC5` (`test_oga2_ac05`) -- a legacy refresh token returns invalid_grant.

<criterion id="OGA2-AC6" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC6` (`test_oga2_ac06`) -- (difference) an access token of a revoked family is rejected, and one of a live family is accepted.

<criterion id="OGA2-AC7" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC7` (`test_oga2_ac07`) -- a caller-supplied email, identity header, role or tenant never becomes the authorization identity.

<criterion id="OGA2-AC8" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC8` (`test_oga2_ac08`) -- a principal with the same email and a different `oid` is denied (A3).

<criterion id="OGA2-AC9" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC9` (`test_oga2_ac09`) -- a token from an unauthorized tenant is rejected.

<criterion id="OGA2-AC10" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC10` (`test_oga2_ac10`) -- (difference) a missing or invalid credential returns 401 with the resource challenge, while a valid token lacking a scope returns 403 insufficient_scope.

<criterion id="OGA2-AC11" cell_refs="OG-a-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py::test_oga2_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA2-AC11` (`test_oga2_ac11`) -- a denied data entitlement returns a terminal tool error and never a 401 or an OAuth escalation.

<expected_criteria>OGA2-AC1, OGA2-AC2, OGA2-AC3, OGA2-AC4, OGA2-AC5, OGA2-AC6, OGA2-AC7, OGA2-AC8, OGA2-AC9, OGA2-AC10, OGA2-AC11</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-a-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_principal_cutover.py`; write exactly that name. The upstream identity provider is a local test issuer with a locally generated key, never Entra. `tests/test_oauth_durable.py` stays green.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. No existing test is edited to make it pass.
- **Nothing deploys.** The cutover reaches users only through `OG-r-1`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/token_broker.py
infra/aws/ec2/opal-gateway/app/context.py
infra/aws/ec2/opal-gateway/app/identity.py
infra/aws/ec2/opal-gateway/app/oauth_as.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/revocation.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-a-2`, round 1 (section 3, S1).
<owned_cells>OG-a-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGA2-AC1` .. `OGA2-AC11` (11). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-a-2.principal-cutover.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGA2-AC1,OGA2-AC2,OGA2-AC3,OGA2-AC4,OGA2-AC5,OGA2-AC6,OGA2-AC7,OGA2-AC8,OGA2-AC9,OGA2-AC10,OGA2-AC11`
BEFORE the `complete` flip. Result file `principal-cutover.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell; its cutover reaches users through OG-r-1, which notice N-1 precedes.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell adds no AWS operation; it narrows Graph acquisition to the tools that use it.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 3, handed after `OG-a-1` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
