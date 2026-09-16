# TO NFRA_OPLGTW.TO-OG-o-1 -- the acknowledged Schwab audit entry point

<to_id>NFRA_OPLGTW.TO-OG-o-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-o-1` | **outcome_ref:** FWD-6, FWD-8 | **depends_on:** -- (head; spawned at issuance) | **slot:** ~5, queue position 1

---

## WORKER FACE

### THE CELL

`OG-o-1` -- **the acknowledged Schwab audit entry point**, a new module `infra/aws/ec2/opal-gateway/app/schwab_audit.py`.
Every Schwab data release (query result, download start) awaits its audit receipt through this module first.

What the source does today (certified L4 rectangle, S6-operations): *"audit: Local JSONL plus best-effort S3 copy. New tool
args are omitted unless declared in metadata-safe allowlist. Separate detail string is copied up to 500 chars and requires
sanitization. Master/dataset/policy/version/count fields need explicit safe audit schema."*

What it must do -- the PRD's "Operator journey, audit and release", verbatim:
- *"Audit fields: timestamp/correlation, hashed principal identifier, operation/tool, master/dataset/date, grant revision,
  opaque snapshot/version reference, input/output counts and bytes, duration, policy decision/outcome/error code, and
  operator change actor/reference. Exclude raw account IDs, customer values, prompts, OAuth credentials, cookies, ticket
  secrets and complete URLs. Use the existing audit sink; add bounded classifications, not another general alarm service.
  If the durable authorization audit write cannot be acknowledged, deny a new data release and return
  DEPENDENCY_UNAVAILABLE; auth availability for unrelated Gateway users must not depend on a Schwab sink."*
- *"Implement a Schwab-specific acknowledged audit entry point: await successful PutObject of the sanitized
  authorization/denial record under the existing opal-mcp-audit sink's dedicated Schwab prefix and retain the response
  receipt/correlation before releasing data. The existing best-effort audit._emit/log_call return is not this
  acknowledgment. Name events release_authorized and delivery_finished separately; record planned versus actually
  delivered counts, and cancellation/failure, without claiming that authorization proves delivery."*

Contract: `audit_acknowledgment` = *"successful awaited S3 PutObject receipt in opal-mcp-audit Schwab prefix before data
release"*; `audit_event_types` = release_authorized, delivery_finished, denied, cancelled, failed, operator_revision.
**Prefix, decided at the cut:** `audit/schwab/`, inside the Gateway's existing grant
(`infra/aws/terraform/opal-gateway/audit-lake.tf:186-187`: `s3:PutObject` on `${aws_s3_bucket.audit.arn}/audit/*`), so no
IAM change is needed. Your tests use moto.

**Read:** the PRD's "Operator journey, audit and release"; the contract; `app/audit.py`; `infra/aws/terraform/opal-gateway/audit-lake.tf`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGO1-AC1" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC1` (`test_ogo1_ac01`) -- the entry point awaits a successful PutObject under `opal-mcp-audit` `audit/schwab/` and returns its receipt before any data release, by a call-order assertion.

<criterion id="OGO1-AC2" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC2` (`test_ogo1_ac02`) -- (difference) with the sink failing, a new data release returns DEPENDENCY_UNAVAILABLE and no data, and with it healthy the data is released.

<criterion id="OGO1-AC3" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC3` (`test_ogo1_ac03`) -- the event types are exactly release_authorized, delivery_finished, denied, cancelled, failed and operator_revision.

<criterion id="OGO1-AC4" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC4` (`test_ogo1_ac04`) -- release_authorized and delivery_finished record planned and delivered counts separately.

<criterion id="OGO1-AC5" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC5` (`test_ogo1_ac05`) -- a fixture record holds no raw account ID, customer value, prompt, OAuth credential, cookie, ticket secret or complete URL.

<criterion id="OGO1-AC6" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC6` (`test_ogo1_ac06`) -- (difference) with the sink failing, an unrelated legacy authentication still succeeds.

<criterion id="OGO1-AC7" cell_refs="OG-o-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py::test_ogo1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGO1-AC7` (`test_ogo1_ac07`) -- the prefix sits inside the Gateway's existing grant (`audit-lake.tf:186-187`, `audit/*`), so no IAM change is made: the test reads the Terraform file and the module's prefix constant.

<expected_criteria>OGO1-AC1, OGO1-AC2, OGO1-AC3, OGO1-AC4, OGO1-AC5, OGO1-AC6, OGO1-AC7</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** After the tree check, build your own venv once: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Record `pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`. A package install into this venv is a build act this order grants; no other install is.
- **Tests.** Each criterion names one test function in `tests/test_schwab_audit.py`; write exactly that name. Your criteria run offline against moto.
- **No new monitor, alarm, SNS or notification path.** Bounded classifications in the audit record only.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. `app/audit.py` keeps its current behaviour for every existing caller. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/schwab_audit.py
infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-o-1`, round 1 (section 3, S8).
<owned_cells>OG-o-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGO1-AC1` .. `OGO1-AC7` (7). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-o-1.acknowledged-audit.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGO1-AC1,OGO1-AC2,OGO1-AC3,OGO1-AC4,OGO1-AC5,OGO1-AC6,OGO1-AC7`
BEFORE the `complete` flip. Result file `acknowledged-audit.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. The no-new-monitor moratorium binds this cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE (s3:PutObject at audit.py:48 among them), 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell's PutObject stays under the audit/* grant at audit-lake.tf:186-187; AC7 proves it.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 1 (then `OG-q-1`, `OG-k-1`, `OG-q-2`, `OG-q-3`, `OG-x-1`, `OG-o-2`). Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
