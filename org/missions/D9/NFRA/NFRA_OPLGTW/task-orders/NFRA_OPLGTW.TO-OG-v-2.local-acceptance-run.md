# TO NFRA_OPLGTW.TO-OG-v-2 -- the local integrated acceptance run

<to_id>NFRA_OPLGTW.TO-OG-v-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-2` | **outcome_ref:** FWD-2 .. FWD-7 | **depends_on:** `OG-v-1`, `OG-x-1`, `OG-z-2` | **slot:** ~6, queue position 2

---

## WORKER FACE

### THE CELL

`OG-v-2` -- **the local integrated acceptance run**, before anything reaches production. Write
`infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py` and run it against the integrated Gateway at your
base (every Gateway code cell merged), graded against `OG-v-1`'s independent expectations. The first release (`OG-r-1`)
is not handed until every row you run passes.

The PRD's C1 paragraph this run discharges: *"Inventory active client registrations and test the migration before
cutover."* And the acceptance rule: *"The test author must construct independent expected fixtures rather than calculate
expectations with the query under test. CVO's validation compares that full set before trusting any green test exit
code."*

**The harness, and its seams named so they can be argued with:** the Gateway's ASGI app runs in process; DynamoDB, S3
(versioning on) and STS are moto; the S3 fixture objects are `OG-v-1`'s `fixtures/`, loaded into moto; the upstream
identity provider is a local test issuer with a locally generated key; the Schwab integration's enablement is on for
the test process only. Each A-row that `A_ROWS.json` marks `operated_by: machine` and whose instrument is the local
harness becomes one test `test_ogv2_a<nn>` (for example `test_ogv2_a03`), compared against `expected/`. Rows whose
instrument is the host (`OG-r-2`) or a person (`OG-v-4`, `OG-v-5`) are listed in your result file as out of scope here,
with their denominator.

**Read:** `infra/aws/ec2/opal-gateway/tests/acceptance/A_ROWS.json`, `WALKTHROUGH_PROTOCOL.md`, `expected/`, `fixtures/`
(from `OG-v-1`); the PRD's "Acceptance matrix and independent proof"; `app/server.py` (how the app is built) -- you read
the app to drive it, never to derive an expectation.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV2-AC1" cell_refs="OG-v-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py::test_ogv2_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGV2-AC1` (`test_ogv2_ac01`) -- the integrated application runs locally against the emulated state store and the fixture objects.

<criterion id="OGV2-AC2" cell_refs="OG-v-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py -q -p no:cacheprovider --color=no -k "test_ogv2_a"</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGV2-AC2` -- each machine-operated A-row of `OG-v-1`'s census is run against its expectation and passes; the result file prints the denominator (rows run of rows marked machine-and-local).

<criterion id="OGV2-AC3" cell_refs="OG-v-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py::test_ogv2_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGV2-AC3` (`test_ogv2_ac03`) -- (difference) a legacy refresh token returns invalid_grant, and a freshly registered loopback client connects and survives a restart (A2, machine half).

<criterion id="OGV2-AC4" cell_refs="OG-v-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests -q -p no:cacheprovider --color=no -m "not live" -k "not test_scoped_deny_by_default"</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGV2-AC4` -- the whole `infra/aws/ec2/opal-gateway/tests/` suite passes, count printed, with the one known red test of row NFRA_OPLGTW-S1 deselected by name.

<expected_criteria>OGV2-AC1, OGV2-AC2, OGV2-AC3, OGV2-AC4</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **You grade; you do not fix.** A failing row is a FAIL recorded with its output and a surprise row naming the cell whose surface it lands on. You never edit `app/`, `OG-v-1`'s expectations or any other cell's test to make a row pass.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after every Gateway code cell merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Local only.** Nothing in this cell reaches AWS, the Gateway host or any user.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1) and is deselected by name in AC4. Never edit it or `identity_tool_allowlist.txt`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W6-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py
infra/aws/ec2/opal-gateway/tests/acceptance/conftest.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-2`, round 1 (section 3, S10; section 5 distinct-worker constraint).
<owned_cells>OG-v-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV2-AC1` .. `OGV2-AC4` (4). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-2.local-acceptance-run.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV2-AC1,OGV2-AC2,OGV2-AC3,OGV2-AC4` BEFORE the `complete` flip.
Result file `local-acceptance-run.result.md` beside it, with one line per A-row: run here, host, or person. **Flip
`complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell; OG-r-1 is not handed until it passes.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell runs the integrated build locally against emulators; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~6, queue position 2, handed after `OG-x-1` and `OG-z-2` merge (every Gateway code cell is then at HEAD);
a slot that authored no `app/` code. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567).
Decomposition v1 @8768f46770.
