# TO NFRA_OPLGTW.TO-OG-a-3 -- the download browser's own OIDC login

<to_id>NFRA_OPLGTW.TO-OG-a-3</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-a-3` | **outcome_ref:** FWD-4 | **depends_on:** `OG-a-2` | **slot:** ~3, queue position 4

---

## WORKER FACE

### THE CELL

`OG-a-3` -- **the download browser's own OIDC login**, in a new module `infra/aws/ec2/opal-gateway/app/browser_oidc.py`
with its routes in `app/server.py`. The export cell (`OG-x-1`) sends a signed-in browser here before it redeems a
download ticket; the ALB cell (`OG-i-3`) opens exactly the paths you name.

What the source does today (certified L4 rectangle, S1-auth): *"The existing ALB browser identity path validates ES256
against the regional key selected by kid, disables JWT audience validation, does not check an expected ALB
signer/client/issuer in that function, and returns email only. Reusing it does not by itself establish the proposed
immutable browser-to-MCP identity binding."*

What it must do -- the PRD's C1, verbatim: *"The download browser uses a separate Gateway-owned OIDC callback, secure
HttpOnly SameSite cookies, anti-CSRF state/nonce and exact issuer/audience/signature validation. It establishes the same
tid/oid principal independently. Do not infer that match from the existing ALB email-only helper. Browser OIDC endpoints
bypass ALB login only at those explicit paths; existing default browser authentication and unrelated routes remain
intact."*

Write `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/BROWSER_PATHS.json`: the exact login and
callback paths this cell serves, one entry per path with its HTTP methods. `OG-i-3` reads that file and nothing else to
decide the ALB rules. The principal function is `OG-a-2`'s (merged at your hand-off): reuse it, never a second one.

**Read:** the PRD's "C1" and "C5" (the download journey this login serves); `app/identity.py`, `app/server.py`,
`app/context.py`, and `OG-a-2`'s principal function at HEAD.

**Amended after your first run, on `1.0.0_SA_CTO`'s ruling msg 97203 (rows `NFRA_OPLGTW-W3-S16`, `NFRA_OPLGTW-W3-S17`,
`NFRA_OPLGTW-S13`).** Your first run (this branch at `06a9aec60d`) passes AC1..AC7, but two tests pin the whole route
table.
- `tests/test_principal_cutover.py::test_oga2_ac04` requires `set(ROUTE_CLASS) == set(routes)` (`:540`), and your two
  paths are not in `ROUTE_CLASS`.
  - That file is now granted to you, ENTRIES ONLY: add `/schwab/download/login` and `/schwab/download/callback` to
    `ROUTE_CLASS` as `"public"`. That is their true class, because a login and its OIDC callback are reachable
    without a session.
  - Change no assertion and no other line. AC9 runs the module; AC10 checks the file's diff.
- Your own `test_oga3_ac07` pins the table exactly (`tuple(rest) == BASE_ROUTES`, and head-minus-base equal to your two
  routes), so the next cell that adds a route breaks it.
  - AC7 is restated as a superset: rewrite `test_oga3_ac07` so it holds at any later HEAD.
  - The exact fact, the base plus exactly these two routes at this cell's HEAD, moves to AC8, a one-time probe recorded
    in your proof.
Your AC1..AC6 code stands. Re-run all ten criteria and rebuild the proof instance and result file.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGA3-AC1" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC1` (`test_oga3_ac01`) -- the Gateway-owned OIDC callback and download paths are listed exactly, for `OG-i-3`: the test asserts the served routes equal `BROWSER_PATHS.json`.

<criterion id="OGA3-AC2" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC2` (`test_oga3_ac02`) -- a mismatched state or nonce is refused.

<criterion id="OGA3-AC3" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC3` (`test_oga3_ac03`) -- an ID token with a wrong signature, issuer or audience is each refused.

<criterion id="OGA3-AC4" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC4` (`test_oga3_ac04`) -- the session cookie is Secure, HttpOnly and SameSite, scoped to the download paths.

<criterion id="OGA3-AC5" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC5` (`test_oga3_ac05`) -- the same user fixture yields the same `tid`/`oid` principal through this login as through MCP OAuth.

<criterion id="OGA3-AC6" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC6` (`test_oga3_ac06`) -- the cell's code neither imports nor calls `identity.py`'s ALB email helper (a static check of `browser_oidc.py`).

<criterion id="OGA3-AC7" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py::test_oga3_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC7` (`test_oga3_ac07`) -- (superset) every route at the cut base `7459929520` is still served, unchanged and in order; the two browser routes are served; the middleware is unchanged; and the existing browser authentication still guards `/login`, `/sprint` and `/sprint/archive`.

<criterion id="OGA3-AC8" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/probes/og_a3.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGA3-AC8(?![0-9])</expect></criterion>
`OGA3-AC8` -- (one-time record) at this cell's HEAD, the served route table equals the table at the cut base `7459929520` plus exactly the paths in `BROWSER_PATHS.json`, none removed or changed; the probe prints the counts and `VERDICT: PASS-OGA3-AC8` or `VERDICT: FAIL-OGA3-AC8 <reason>`.

<criterion id="OGA3-AC9" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py -q -p no:cacheprovider --color=no -m "not live"</invocation><expect>(?m)^11 passed(?![^\n]*(failed|error))</expect></criterion>
`OGA3-AC9` -- `tests/test_principal_cutover.py` passes, 11 of 11, with the two browser paths classed in `ROUTE_CLASS`.

<criterion id="OGA3-AC10" cell_refs="OG-a-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/probes/og_a3.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGA3-AC10(?![0-9])</expect></criterion>
`OGA3-AC10` -- (discriminating) the diff of `tests/test_principal_cutover.py` against the cut base `7459929520` is exactly two added `ROUTE_CLASS` entries, `/schwab/download/login` and `/schwab/download/callback`, each `"public"`, and no other line; the probe prints `VERDICT: PASS-OGA3-AC10` or `VERDICT: FAIL-OGA3-AC10 <reason>`.

<expected_criteria>OGA3-AC1, OGA3-AC2, OGA3-AC3, OGA3-AC4, OGA3-AC5, OGA3-AC6, OGA3-AC7, OGA3-AC8, OGA3-AC9, OGA3-AC10</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-a-2` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_browser_oidc.py`; write exactly that name. The upstream provider is a local test issuer with a locally generated key, never Entra. AC8 and AC10 are probes and AC9 a module run; `tests/test_principal_cutover.py` is yours for its two `ROUTE_CLASS` entries only.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. The ALB is not yours (`OG-i-3`); nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/browser_oidc.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-a-3`, round 1 (section 3, S1).
<owned_cells>OG-a-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGA3-AC1` .. `OGA3-AC10` (10). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-a-3.browser-oidc.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGA3-AC1,OGA3-AC2,OGA3-AC3,OGA3-AC4,OGA3-AC5,OGA3-AC6,OGA3-AC7,OGA3-AC8,OGA3-AC9,OGA3-AC10`
BEFORE the `complete` flip. Result file `browser-oidc.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell adds no AWS operation, policy, principal or role; it adds a browser login inside the Gateway process.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 4, handed after `OG-a-2` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.

Amended 2026-09-15 ~19:1xZ, after the first run and before re-hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling
msg 97203 (rows `NFRA_OPLGTW-W3-S16`, `NFRA_OPLGTW-W3-S17`, `NFRA_OPLGTW-S13`). The changes:
- `<status>` returns to pending;
- `tests/test_principal_cutover.py` is granted, ROUTE_CLASS entries only;
- AC7 is restated as a superset;
- AC8 (a one-time exact-diff record), AC9 and AC10 are added.
No criterion was removed.
