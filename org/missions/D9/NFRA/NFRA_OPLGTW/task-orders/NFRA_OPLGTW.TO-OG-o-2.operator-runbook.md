# TO NFRA_OPLGTW.TO-OG-o-2 -- the operator runbook and its status summary

<to_id>NFRA_OPLGTW.TO-OG-o-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-o-2` | **outcome_ref:** FWD-6, FWD-8 | **depends_on:** `OG-z-2`, `OG-x-1` | **slot:** ~5, queue position 7

---

## WORKER FACE

### THE CELL

`OG-o-2` -- **the operator runbook and its status summary**: `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md`
and a status command `infra/aws/ec2/opal-gateway/ops/schwab_status.py`. The walkthroughs that grade FWD-1, FWD-6 and
FWD-8 are performed by following this runbook, so it must be executable by an operator with nothing else in hand.

The PRD's "Operator journey, audit and release", verbatim where it binds:
- *"A CloudOps operator begins onboarding by reading the current deployment parity/health record, resolving the immutable
  principal with the identity administrator, and validating the proposed scope against an actual authorization record. Use
  the existing organization connector where compatible; otherwise the supplied prefilled Claude connector form names Opal
  Gateway and its MCP URL. The form grants no data access. An owner adds/enables the custom connector; Menachem connects
  his work identity, enables it in chat, asks a sample single-master/date question, opens the link (including Claude
  external-link confirmation), signs into the browser and clicks Download CSV. Do not silently recreate shared connector
  credentials or headers; plan and test any required reconnect migration. Managed Enterprise Auth is future work and is
  not implied by DCR or Entra login. During onboarding, the operator tells Menachem that selected results enter the
  organization's Claude chat environment and its retention settings. Commercial training defaults do not mean zero
  transfer; this disclosure accompanies the existing limitation that returned data and downloaded bytes cannot be
  recalled."*
- *"Named readers and moments: the assigned CloudOps operator reads health/closure/error summaries before each onboarding
  or grant change, on each support incident and immediately after every rollout/rollback. The deployment operator reads
  the parity/negative-policy and regression reports before enablement. The identity/data administrator reads the exact
  scope diff at every grant revision. CVO reads A1-A20 and its expected-ID census at every project validation. COO reads
  the admitted PRD/run at L5 and runtime evidence at round close."*
- From C6: *"Rollback disables the integration and keeps the restricted-profile denial and durable token revocation shim
  active; do not roll back to a binary that reopens the email-only path or accepts legacy refresh tokens ... Source
  ingesters and source contents remain intact. No source delete, rewrite or bucket-policy broadening is part of rollback."*
  And the A15 readbacks: versioning, AES256, the four public-access blocks (BlockPublicAcls, IgnorePublicAcls,
  BlockPublicPolicy, RestrictPublicBuckets) and the non-public bucket policy, before and after.

The grant commands are `OG-z-2`'s (`GW/ops/schwab_entitlement_admin.py`), the download journey `OG-x-1`'s, the audit
fields `OG-o-1`'s -- all merged at your hand-off. Every command the runbook names must exist at HEAD (AC2).

**Read:** the PRD's "Operator journey, audit and release" and "C6"; `GW/ops/schwab_entitlement_admin.py`,
`app/schwab_audit.py`, `app/download_routes.py`; `infra/aws/ec2/safe-ec2-deploy.sh` (the rollback's release path).

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGO2-AC<n>` or
`VERDICT: FAIL-OGO2-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGO2-AC1" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC1(?![0-9])</expect></criterion>
`OGO2-AC1` -- the runbook carries onboarding, connector add or reuse, member connection, troubleshooting, audit read, grant change and revocation, rollback and disclosure sections.

<criterion id="OGO2-AC2" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC2(?![0-9])</expect></criterion>
`OGO2-AC2` -- every command the runbook names exists at HEAD.

<criterion id="OGO2-AC3" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC3(?![0-9])</expect></criterion>
`OGO2-AC3` -- troubleshooting distinguishes authentication failure, terminal entitlement denial and data unavailability.

<criterion id="OGO2-AC4" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC4(?![0-9])</expect></criterion>
`OGO2-AC4` -- the rollback section disables the integration and keeps the restricted-profile denial and the revocation shim.

<criterion id="OGO2-AC5" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC5(?![0-9])</expect></criterion>
`OGO2-AC5` -- the rollback section forbids restoring a binary that reopens the email-only path or accepts legacy refresh tokens.

<criterion id="OGO2-AC6" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC6(?![0-9])</expect></criterion>
`OGO2-AC6` -- the rollback section preserves source objects and ingesters and carries the source-bucket readbacks.

<criterion id="OGO2-AC7" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC7(?![0-9])</expect></criterion>
`OGO2-AC7` -- the disclosure states the chat-environment and retention exposure, that commercial training defaults do not mean zero transfer, and that delivered data cannot be recalled.

<criterion id="OGO2-AC8" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC8(?![0-9])</expect></criterion>
`OGO2-AC8` -- the runbook names its readers and their consuming moments.

<criterion id="OGO2-AC9" cell_refs="OG-o-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_o2.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGO2-AC9(?![0-9])</expect></criterion>
`OGO2-AC9` -- the status summary prints health, closure and error summaries with no customer value (the probe runs it against moto fixtures and scans the output).

<criterion id="OGO2-J1" cell_refs="OG-o-2" judgment="true"/>
`OGO2-J1` -- graded at L9 by 3.0.0_SA_CVO: an operator can execute each section at its named moment without other context. RECORD; NO VERDICT.

<expected_criteria>OGO2-AC1, OGO2-AC2, OGO2-AC3, OGO2-AC4, OGO2-AC5, OGO2-AC6, OGO2-AC7, OGO2-AC8, OGO2-AC9, OGO2-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-z-2` and `OG-x-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **The runbook describes; it performs nothing.** You run no rollback, grant change, connector act or deploy while writing it. Its commands are exercised by the walkthroughs, not here.
- **No new monitor, alarm, SNS or notification path.** The status summary is a command an operator runs.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/ec2/opal-gateway/ops/schwab_status.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-o-2`, round 1 (section 3, S8).
<owned_cells>OG-o-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGO2-AC1` .. `OGO2-AC9`, `OGO2-J1` (10). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-o-2.operator-runbook.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGO2-AC1,OGO2-AC2,OGO2-AC3,OGO2-AC4,OGO2-AC5,OGO2-AC6,OGO2-AC7,OGO2-AC8,OGO2-AC9,OGO2-J1`
BEFORE the `complete` flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a
`status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`operator-runbook.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. The no-new-monitor moratorium binds the status command.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes a runbook and a read-only status command over existing modules; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 7, handed after `OG-x-1` drains and `OG-z-2` merges. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
