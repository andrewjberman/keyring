# TO NFRA_OPLGTW.TO-OG-z-3 -- the keyed account alias

<to_id>NFRA_OPLGTW.TO-OG-z-3</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-z-3` | **outcome_ref:** FWD-2, FWD-3 | **depends_on:** `OG-z-1` | **slot:** ~3, queue position 6

---

## WORKER FACE

### THE CELL

`OG-z-3` -- **the keyed account alias**: a new module `infra/aws/ec2/opal-gateway/app/account_ref.py` that turns a raw
Schwab account ID into the `account_ref` every Schwab response and CSV shows, and resolves it back only for the
principal's current authorized account set.

The PRD's C2, verbatim: *"Accounts are raw IDs internally only. Expose a versioned, keyed HMAC account_ref over master
plus account ID; keep its key in the existing approved secret mechanism, and never log raw IDs. The same numeric account
ID in two masters yields different aliases. An alias is usable only after resolution against the current authorized
account set."* Acceptance row A5: *"Same account ID in two masters gives different aliases; requests/caches/cursors/
tickets cannot mix masters."*

The key lives in the secret `OG-i-2` provisions; its NAME (never its value) is in
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json` once that cell merges. Read
the key through the Gateway's existing secret path (`app/integrations/base.py`, the `secretsmanager:GetSecretValue`
call). Your tests use a locally generated test key and never touch the real secret. The authorized account set comes
from `OG-z-1`'s entitlement records (merged at your hand-off).

State the retired-key rule you choose in your result file (reject, or re-resolve under the current version), and prove
it (AC5).

**Read:** the PRD's "C2"; the contract's `fields` (`account_ref` in `dim_position` and `dim_balance`) and
`forbidden_field_classes`; `app/data_entitlement.py`, `app/integrations/base.py`, `app/audit.py`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGZ3-AC1" cell_refs="OG-z-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_account_ref.py::test_ogz3_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ3-AC1` (`test_ogz3_ac01`) -- `account_ref` is a versioned keyed HMAC over master and account ID, with its key read through the secret `OG-i-2` provisions.

<criterion id="OGZ3-AC2" cell_refs="OG-z-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_account_ref.py::test_ogz3_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ3-AC2` (`test_ogz3_ac02`) -- one account ID in two masters yields two different references (A5).

<criterion id="OGZ3-AC3" cell_refs="OG-z-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_account_ref.py::test_ogz3_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ3-AC3` (`test_ogz3_ac03`) -- a reference outside the current authorized account set returns ENTITLEMENT_DENIED without revealing whether the account exists.

<criterion id="OGZ3-AC4" cell_refs="OG-z-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_account_ref.py::test_ogz3_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ3-AC4` (`test_ogz3_ac04`) -- a raw account ID appears in no log or audit line the harness captures.

<criterion id="OGZ3-AC5" cell_refs="OG-z-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_account_ref.py::test_ogz3_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ3-AC5` (`test_ogz3_ac05`) -- a reference under a retired key version is handled by the stated rule.

<expected_criteria>OGZ3-AC1, OGZ3-AC2, OGZ3-AC3, OGZ3-AC4, OGZ3-AC5</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-z-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_account_ref.py`; write exactly that name. Tests use a locally generated key; the real secret is never read in this cell.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.** No key, no raw account ID.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W3-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/account_ref.py
infra/aws/ec2/opal-gateway/tests/test_account_ref.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-z-3`, round 1 (section 3, S2).
<owned_cells>OG-z-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGZ3-AC1` .. `OGZ3-AC5` (5). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/NFRA_OPLGTW.TO-OG-z-3.account-alias.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGZ3-AC1,OGZ3-AC2,OGZ3-AC3,OGZ3-AC4,OGZ3-AC5` BEFORE the `complete`
flip. Result file `account-alias.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES
by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE (secretsmanager:GetSecretValue at integrations/base.py:204 among them), 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell reuses that existing secret read; OG-i-2 owns the grant on the new secret.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~3, queue position 6, handed after `OG-z-1` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
