# TO NFRA_OPLGTW.TO-OG-z-2 -- the operator's entitlement administration command

<to_id>NFRA_OPLGTW.TO-OG-z-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-z-2` | **outcome_ref:** FWD-6, FWD-8 | **depends_on:** `OG-z-1` | **slot:** ~3, queue position 7

---

## WORKER FACE

### THE CELL

`OG-z-2` -- **the operator's entitlement administration command**, a repository command at
`infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, never an MCP tool. An authorized operator uses it to
create, revise and revoke a principal's grant; nothing else in the Gateway writes a `POLICY#` record.

The PRD's C2 and C6, verbatim:
- *"Entitlement updates are operator-only, through an audited repository/release-operated administration command using
  an authorized operator AWS identity. Validate a candidate, show the exact scope diff, then conditionally activate it
  against the old revision. Store approver, timestamp and source authorization reference. Reject empty/unknown identity,
  unapproved accounts/fields or malformed dates. Provide no MCP tool to mutate grants."*
- *"The operator role alone may conditionally update POLICY records and append the matching operator audit in one
  transaction. Ordinary runtime and operator roles have no policy DeleteItem or table-admin permission. Profile, grant,
  approval and revocation tombstones have no TTL attribute."*

The operator role is `OG-i-1`'s (its ARN in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/access-state-table.result.md`
once merged); the record shapes are `OG-z-1`'s (`app/data_entitlement.py`, merged at your hand-off). Contract fields
the command validates against: `fields`, `forbidden_field_classes`, `grant_date_modes`, `operations`,
`disabled_operations`.

**This cell builds the command; it activates no grant.** Your tests run against moto. No real person's profile is
created, revised or revoked here (gate G-E is a separate, later act by an authorized operator).

**Read:** the PRD's "C2" and "C6"; the contract; `app/data_entitlement.py`, `app/access_state.py`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGZ2-AC1" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC1` (`test_ogz2_ac01`) -- a candidate with an empty or unknown identity is refused.

<criterion id="OGZ2-AC2" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC2` (`test_ogz2_ac02`) -- a candidate with an unapproved account or field is refused.

<criterion id="OGZ2-AC3" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC3` (`test_ogz2_ac03`) -- a candidate with a malformed date is refused.

<criterion id="OGZ2-AC4" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC4` (`test_ogz2_ac04`) -- the command prints the exact scope diff before activation.

<criterion id="OGZ2-AC5" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC5` (`test_ogz2_ac05`) -- (difference) activation against a stale revision is refused, and against the current revision succeeds.

<criterion id="OGZ2-AC6" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC6` (`test_ogz2_ac06`) -- one transaction writes the `POLICY#` record and its `operator_audit` with approver, timestamp and source authorization reference.

<criterion id="OGZ2-AC7" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC7` (`test_ogz2_ac07`) -- revocation writes a tombstone and deletes nothing.

<criterion id="OGZ2-AC8" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC8` (`test_ogz2_ac08`) -- no registered MCP tool writes a `POLICY#` record, over all tools, denominator printed.

<criterion id="OGZ2-AC9" cell_refs="OG-z-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py::test_ogz2_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ2-AC9` (`test_ogz2_ac09`) -- the command runs under an operator AWS identity and refuses to run under the runtime role (the test drives the caller-identity check with both ARNs).

<expected_criteria>OGZ2-AC1, OGZ2-AC2, OGZ2-AC3, OGZ2-AC4, OGZ2-AC5, OGZ2-AC6, OGZ2-AC7, OGZ2-AC8, OGZ2-AC9</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-z-3` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_entitlement_admin.py`; write exactly that name. Your criteria run offline against moto.
- **No grant is activated.** The command is never run against the live table in this cell.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-z-2`, round 1 (section 3, S2).
<owned_cells>OG-z-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGZ2-AC1` .. `OGZ2-AC9` (9). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-z-2.entitlement-admin.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGZ2-AC1,OGZ2-AC2,OGZ2-AC3,OGZ2-AC4,OGZ2-AC5,OGZ2-AC6,OGZ2-AC7,OGZ2-AC8,OGZ2-AC9`
BEFORE the `complete` flip. Result file `entitlement-admin.result.md` beside it, with the command's usage. **Flip
`complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. The command it builds is what gate G-E's activation later uses; G-E does not hold the build.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. The command runs under OG-i-1's operator role, outside the Gateway process; the lens re-run is recorded in the instance.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 7, handed after `OG-z-3` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
