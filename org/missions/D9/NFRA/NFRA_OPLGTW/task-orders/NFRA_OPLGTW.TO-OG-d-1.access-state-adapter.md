# TO NFRA_OPLGTW.TO-OG-d-1 -- the access-state adapter

<to_id>NFRA_OPLGTW.TO-OG-d-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-d-1` | **outcome_ref:** FWD-1, FWD-3, FWD-4, FWD-6, FWD-7 | **depends_on:** -- (head; spawned at issuance) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`OG-d-1` -- **the access-state adapter**: one new module, `infra/aws/ec2/opal-gateway/app/access_state.py`, through which
every later Gateway module reads and writes `opal-gateway-access-state`. OAuth, the policy guard, the catalog and the
export all build on it, so its guarantees are the project's guarantees.

The contract's `state_store` block and the PRD's C6, verbatim where it binds:
- record types: `principal_profile`, `data_entitlement`, `oauth_client`, `oauth_code`, `oauth_refresh_family`,
  `download_ticket`, `catalog_snapshot`, `oauth_pending_authorization`, `operator_audit`;
- consistency `strong_reads_and_conditional_transactions`; TTL `cleanup_only_never_authorization`;
- key namespaces: `POLICY` = *"profile/grant/approval/operator audit; operator writes only; no TTL or ordinary delete"*,
  `RUNTIME` = *"client/pending-auth/code/refresh/ticket/catalog; runtime conditional writes and expiring records"*;
- *"runtime_policy_access": "strong read only; write actions require all LeadingKeys match RUNTIME#*"*;
- PRD C1: *"check logical expiry even if TTL deletion is late"*; *"Failure of durable state fails new/refresh exchanges
  closed; it must not silently select an old stateless branch."*

The table itself is another cell's (`OG-i-1`, applied in parallel). Your tests run offline against **moto** in your venv,
which implements DynamoDB's ConditionExpression and TransactWriteItems semantics; name its version in your result file.
The IAM `LeadingKeys` condition cannot be tested in moto -- that is `OG-i-1`'s live arm. Your adapter enforces the same
rule in code BEFORE any AWS call (AC4), so the two controls are independent.

You also own `infra/aws/ec2/opal-gateway/tests/conftest.py`: register a `live` marker there (tests that reach AWS carry
`@pytest.mark.live` and are skipped unless `OG_LIVE=1`), so later cells share one registration.

**Read:** the PRD's "C1" (state paragraphs) and "C6"; the contract's `state_store`; `infra/aws/ec2/opal-gateway/app/revocation.py`
and `app/audit.py` (how the Gateway already reads AWS and fails closed).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGD1-AC1" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC1` (`test_ogd1_ac01`) -- every read is strongly consistent.

<criterion id="OGD1-AC2" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC2` (`test_ogd1_ac02`) -- every write is conditional, and every multi-item change is one transaction.

<criterion id="OGD1-AC3" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC3` (`test_ogd1_ac03`) -- keys use the `POLICY#<tid>#<oid>` and `RUNTIME#<kind>#...` namespaces.

<criterion id="OGD1-AC4" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC4` (`test_ogd1_ac04`) -- (difference) the runtime write API refuses a `POLICY#` key before any AWS call, and accepts the same call on a `RUNTIME#` key.

<criterion id="OGD1-AC5" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC5` (`test_ogd1_ac05`) -- (difference) an expired-but-present record reads as absent, and the same record unexpired reads as present.

<criterion id="OGD1-AC6" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC6` (`test_ogd1_ac06`) -- an unavailable or malformed store returns DEPENDENCY_UNAVAILABLE and never a default or stateless fallback.

<criterion id="OGD1-AC7" cell_refs="OG-d-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_access_state.py::test_ogd1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGD1-AC7` (`test_ogd1_ac07`) -- the tests run against an emulator that implements ConditionExpression and transaction semantics, named with its version (the test proves a failed condition raises ConditionalCheckFailed and prints the emulator's version).

<expected_criteria>OGD1-AC1, OGD1-AC2, OGD1-AC3, OGD1-AC4, OGD1-AC5, OGD1-AC6, OGD1-AC7</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** After the tree check, build your own venv once: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Record `.venv-og/Scripts/python -m pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`. A package install into this venv is a build act this order grants; no other install is.
- **Tests.** Each criterion names one test function; write exactly that name. Your criteria run offline; nothing in this cell reaches AWS.
- **The known red test.** `infra/aws/ec2/opal-gateway/tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised; `requirements.txt` is not yours to edit.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/tests/test_access_state.py
infra/aws/ec2/opal-gateway/tests/conftest.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-d-1`, round 1 (section 3, S3).
<owned_cells>OG-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGD1-AC1` .. `OGD1-AC7` (7). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-d-1.access-state-adapter.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGD1-AC1,OGD1-AC2,OGD1-AC3,OGD1-AC4,OGD1-AC5,OGD1-AC6,OGD1-AC7`
BEFORE the `complete` flip. Result file `access-state-adapter.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell's code adds DynamoDB call sites the lens will trace once they land; OG-i-1 owns the grant they need.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 1 (then `OG-a-1`, `OG-a-2`, `OG-a-3`, `OG-z-1`, `OG-z-3`, `OG-z-2`). Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770. The cut's
interpreter census: Python 3.12.10 carries starlette 0.52.1, PyJWT 2.11.0, boto3 1.42.54, httpx 0.28.1, cryptography
48.0.1, pytest 9.0.2, PyArrow 18.1.0 and DuckDB 1.5.0, and lacks msal, uvicorn and moto -- hence the venv.
