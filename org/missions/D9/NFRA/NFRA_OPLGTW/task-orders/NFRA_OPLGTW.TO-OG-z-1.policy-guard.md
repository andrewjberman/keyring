# TO NFRA_OPLGTW.TO-OG-z-1 -- the persistent policy model and its guard

<to_id>NFRA_OPLGTW.TO-OG-z-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-z-1` | **outcome_ref:** FWD-3, FWD-6, FWD-7 | **depends_on:** `OG-d-1`, `OG-a-2` | **slot:** ~3, queue position 5

---

## WORKER FACE

### THE CELL

`OG-z-1` -- **the persistent policy model and its guard** on discovery, dispatch and every REST route. A new module
`infra/aws/ec2/opal-gateway/app/data_entitlement.py` holds the `principal_profile` and `data_entitlement` records
(through `app/access_state.py`), and the guard is wired into every entry point.

What the source does today (certified L4 rectangle, S2-authorization, @5dd24300f7): *"All 35 native @mcp.tool functions
in tools.py call _run ... identity_scope restricts identities present in its map only. Unlisted identities pass through
... entitlements.py governs tier-to-write-class grants. It has no master/dataset/account/date/column policy"*; *"The
inspected gateway has global native/integration registration and no list_tools implementation or per-principal
discovery filter"*; *"REST /teams/poll and /query/v0 validate a bearer and blocklist but bypass both MCP tool allowlist
chokepoints. query_v0 derives opal-internal access from opalinvest.com/opalinvest.dev email domains and then reads
cataloged portal JSON with default boto3 credentials."* Re-ground each; count the tools and routes yourself.

What it must do -- the PRD's C2, verbatim:
- *"DynamoDB stores durable `principal_profile` and versioned `data_entitlement` records. Key grants by tid/oid, not
  email. Status is pending, active or revoked; use optimistic revision checks for operator updates. A revoked restricted
  profile is a tombstone, never deletion that reactivates the legacy unlisted-user path. Unknown users see no Schwab tools
  and direct Schwab calls fail. A newly added tool is denied until classified. Preserve existing users' current tool
  access through explicit regression, without granting new data tools by default."*
- *"Every request strongly reads the current profile/grant; an unavailable or malformed store denies restricted access.
  Scope includes master, dataset, account IDs, dates, columns and operations separately."*
- *"Enforce discovery and dispatch in the integration registry and native tool path. Inventory all 27 source-declared
  server routes and every non-MCP entry point, including /teams/poll and /query/v0. The new restricted profile is denied
  unrelated data tools and direct REST shortcuts before any credential fetch or read. Domain-suffix internality cannot
  bypass this policy ... Existing admin/Graph/portal routes retain their existing policy for other users, subject to
  regression coverage."*

Contract: `principal_key` = `tid`, `oid`; `profile_statuses` = pending, active, revoked; `operations` = list, describe,
query, download_filtered; `disabled_operations` = download_original, write. The principal comes from `OG-a-2`'s function
(merged at your hand-off).

**Read:** the PRD's "C2"; the contract; `app/identity_scope.py`, `app/tools.py`, `app/integrations/base.py`,
`app/integrations/registry.py`, `app/server.py`, `app/query_v0.py`, `app/entitlements.py`, `app/access_state.py`;
`tests/test_identity_scope.py` and `tests/test_min_tier_gate.py` (existing regressions that must stay as they are).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGZ1-AC1" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC1` (`test_ogz1_ac01`) -- profile and grant records are keyed by `tid`/`oid`, carry status pending, active or revoked and a revision, and a revoked record is a tombstone.

<criterion id="OGZ1-AC2" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC2` (`test_ogz1_ac02`) -- every request strongly reads the current profile and grant.

<criterion id="OGZ1-AC3" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC3` (`test_ogz1_ac03`) -- (difference) with the store unavailable or a record malformed, restricted access is denied, and with the store healthy it is served.

<criterion id="OGZ1-AC4" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC4` (`test_ogz1_ac04`) -- an unknown user sees no Schwab tool in discovery and a direct Schwab call fails.

<criterion id="OGZ1-AC5" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC5` (`test_ogz1_ac05`) -- a newly registered, unclassified tool is denied to the restricted profile.

<criterion id="OGZ1-AC6" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC6` (`test_ogz1_ac06`) -- the restricted profile's discovery lists only its allowed tools.

<criterion id="OGZ1-AC7" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC7` (`test_ogz1_ac07`) -- every other native and integration tool is denied to the restricted profile before any credential fetch, over all tools, denominator printed.

<criterion id="OGZ1-AC8" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC8` (`test_ogz1_ac08`) -- `/teams/poll`, `/query/v0` and every other non-MCP route are denied to the restricted profile before any credential or data read, over all route declarations, denominator printed.

<criterion id="OGZ1-AC9" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC9` (`test_ogz1_ac09`) -- a restricted principal with an `opalinvest.com` email is denied on `/query/v0`.

<criterion id="OGZ1-AC10" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC10` (`test_ogz1_ac10`) -- scope is enforced separately on master, dataset, account IDs, dates, columns and operations.

<criterion id="OGZ1-AC11" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC11` (`test_ogz1_ac11`) -- (difference) every existing identity-scope entry and an unlisted internal user keep exactly their current tool set, before against after.

<criterion id="OGZ1-AC12" cell_refs="OG-z-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py::test_ogz1_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ1-AC12` (`test_ogz1_ac12`) -- removing an overlay row does not reopen the unlisted path for a restricted profile.

<expected_criteria>OGZ1-AC1, OGZ1-AC2, OGZ1-AC3, OGZ1-AC4, OGZ1-AC5, OGZ1-AC6, OGZ1-AC7, OGZ1-AC8, OGZ1-AC9, OGZ1-AC10, OGZ1-AC11, OGZ1-AC12</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-a-3` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_data_entitlement_guard.py`; write exactly that name. Your criteria run offline against moto.
- **Existing users are regression, not scope.** AC11 proves their tool sets unchanged; you grant no existing user a new tool and remove none. `identity_tool_allowlist.txt` and `tests/test_identity_scope.py` are not yours: the one known red test there (row NFRA_OPLGTW-S1) stays red, and you never edit either file.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. No existing test is edited to make it pass.
- **Nothing deploys.**
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/query_v0.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-z-1`, round 1 (section 3, S2).
<owned_cells>OG-z-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGZ1-AC1` .. `OGZ1-AC12` (12). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-z-1.policy-guard.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGZ1-AC1,OGZ1-AC2,OGZ1-AC3,OGZ1-AC4,OGZ1-AC5,OGZ1-AC6,OGZ1-AC7,OGZ1-AC8,OGZ1-AC9,OGZ1-AC10,OGZ1-AC11,OGZ1-AC12`
BEFORE the `complete` flip. Result file `policy-guard.result.md` beside it, with the tool and route inventories and
their denominators. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE (query_v0.py:101 among them), 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell puts a deny before query_v0's ambient read for the restricted profile; it adds no AWS operation.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 5, handed after `OG-a-3` merges (its dependencies `OG-d-1` and `OG-a-2` precede it in
the same queue). Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1
@8768f46770. Row NFRA_OPLGTW-S1 sits on this cell's surface and is not its to fix.
