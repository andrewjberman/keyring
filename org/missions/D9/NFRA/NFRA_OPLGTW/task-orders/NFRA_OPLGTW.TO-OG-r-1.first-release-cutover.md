# TO NFRA_OPLGTW.TO-OG-r-1 -- the first release: the integrated build, the OAuth cutover, the Schwab flag off

<to_id>NFRA_OPLGTW.TO-OG-r-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-r-1` | **outcome_ref:** FWD-1, FWD-7, FWD-8 | **depends_on:** `OG-p-1`, `OG-i-1`, `OG-i-2`, `OG-v-2` (and notice N-1 before the spawn) | **slot:** ~2, queue position 2

---

## WORKER FACE

### THE CELL

`OG-r-1` -- **the first release.** Deploy the integrated Gateway build at your worktree's base (every Gateway code cell
merged, the local acceptance run `OG-v-2` all PASS) through `infra/aws/ec2/safe-ec2-deploy.sh`, with the Schwab
integration's enablement OFF and no principal profile active. This release carries the OAuth cutover the PRD requires.

The PRD, verbatim:
- *"Legacy refresh tokens cannot be safely upgraded without a new authenticated connection. Cutover rejects them with
  invalid_grant, preserves registered Code client callbacks, and tells existing users to reconnect once."*
- *"Feature flag defaults off and new grants default pending. Before rollout, record existing Gateway release/config
  digests and client journeys. Enable a controlled identity first, then the approved employee profile. Rollback disables
  the integration and keeps the restricted-profile denial and durable token revocation shim active; do not roll back to a
  binary that reopens the email-only path or accepts legacy refresh tokens."*
- *"Pin Terraform, dependency lock and EC2 release artifacts using the existing Gateway release manifest/process. Measure
  declared/deployed parity on-instance via the normal SSM inspection."*

The baselines you compare against are `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(your own queue's first cell, `OG-p-1`: parity method, error baseline, client inventory). The table and the reader roles
are live (`OG-i-1`, `OG-i-2`); `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json`
names them. The runbook's rollback section (`infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md`, `OG-o-2`) is
what AC10 checks the recorded previous release against.

**You do not enable anything.** No Schwab tool is reachable after this release, for any principal. Enabling a controlled
identity is a later act, under gate G-C.

**The authority check before the deploy (amended before hand-off, on `1.0.0_SA_CTO`'s ruling msg 97114; rows
`NFRA_OPLGTW-W3-S9` and `NFRA_OPLGTW-S8`).** The pre-existing tier, per-identity tool allowlist and integration
min-tier gate still resolve by email; re-keying them is a round-2 cell. This release ships in round 1 only if:
- the Schwab data path's authority is the tid/oid-keyed grant (`OG-z-1`), and
- the email-keyed min-tier gate can only ADD a restriction, never grant alone.
AC11 proves it on your release base, locally, BEFORE the deploy. Run it with the Schwab integration enabled in the
probe's own process only, against emulated AWS. An identity carrying a predecessor's email and that email's tier,
but no tid/oid grant, is denied every Schwab tool; the same request under an active tid/oid grant is allowed. If AC11
fails, nothing deploys: file a BLOCKING row and stop.

**The browser-login withholding (amended before hand-off, on `1.0.0_SA_CTO`'s ruling msg 97251; row
`NFRA_OPLGTW-W3-S22`).** Five browser routes (`/login` and the four `/sprint` paths) and the legacy-consent branch of
`/callback` still authorize by the ALB login email, not by tid/oid; closing that is a round-2 cell. So in this
release, no principal whose email can complete the ALB browser login (the Entra app's assignment) holds a restricted
profile. AC12 prints the set of principals holding a restricted profile at release and, for each, whether its email
can complete that login. Every one that can is withheld, so the printed count is 0.

**Read:** the PRD's "C1", "C6" and "Operator journey, audit and release"; `infra/aws/ec2/safe-ec2-deploy.sh` and
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (the release process); `infra/aws/ec2/EC2_MANIFEST.json`; the baseline.

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGR1-AC<n>` or `VERDICT: FAIL-OGR1-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGR1-AC1" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC1(?![0-9])</expect></criterion>
`OGR1-AC1` -- the ledger entry is opened and its sentinel committed before the deploy.

<criterion id="OGR1-AC2" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC2(?![0-9])</expect></criterion>
`OGR1-AC2` -- the deploy runs through `infra/aws/ec2/safe-ec2-deploy.sh` with the Schwab feature flag off.

<criterion id="OGR1-AC3" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC3(?![0-9])</expect></criterion>
`OGR1-AC3` -- no principal profile is active in the state store after the deploy.

<criterion id="OGR1-AC4" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC4(?![0-9])</expect></criterion>
`OGR1-AC4` -- on the host, every deployed file's digest equals the build input's, file by file, denominator printed.

<criterion id="OGR1-AC5" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC5(?![0-9])</expect></criterion>
`OGR1-AC5` -- an unauthenticated `/mcp` returns 401 with the advertised resource challenge (asserted, not printed).

<criterion id="OGR1-AC6" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC6(?![0-9])</expect></criterion>
`OGR1-AC6` -- the discovery metadata advertises exactly the resource, issuer, endpoints, scope and S256 behaviour the running configuration enforces.

<criterion id="OGR1-AC7" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC7(?![0-9])</expect></criterion>
`OGR1-AC7` -- on the host, the registry loaded with the live configuration enumerates zero Schwab tools.

<criterion id="OGR1-AC8" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC8(?![0-9])</expect></criterion>
`OGR1-AC8` -- the ledger entry is closed and committed before the grading reads.

<criterion id="OGR1-AC9" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC9(?![0-9])</expect></criterion>
`OGR1-AC9` -- the Gateway's error count over the first stated window after the deploy does not exceed `OG-p-1`'s baseline for the same window length.

<criterion id="OGR1-AC10" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC10(?![0-9])</expect></criterion>
`OGR1-AC10` -- the previous release artifact is recorded and restorable by the runbook's rollback section.

<criterion id="OGR1-AC11" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC11(?![0-9])</expect></criterion>
`OGR1-AC11` -- (difference) on the release base, locally and before the deploy, an identity carrying a predecessor's email and tier but no tid/oid grant is denied every Schwab tool, while the same request under an active tid/oid grant is allowed; the Schwab tool count is printed.

<criterion id="OGR1-AC12" cell_refs="OG-r-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGR1-AC12(?![0-9])</expect></criterion>
`OGR1-AC12` -- at release, the set of principals holding a restricted profile is printed and, for each, whether its email can complete the ALB browser login (the Entra app's assignment); the count of principals that hold a restricted profile AND can complete that login is 0.

<expected_criteria>OGR1-AC1, OGR1-AC2, OGR1-AC3, OGR1-AC4, OGR1-AC5, OGR1-AC6, OGR1-AC7, OGR1-AC8, OGR1-AC9, OGR1-AC10, OGR1-AC11, OGR1-AC12</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off, after every Gateway code cell and `OG-v-2` merged. Deploy exactly that base. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open the entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-r-1-first-release ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json` and entry BEFORE the deploy; close the legs and the entry and COMMIT BEFORE the grading reads. NEVER leave the deploy half-landed: finish it in-session, or roll back by the runbook and file an ARMED row naming yourself as disarm owner.
- **The Gateway only through `infra/aws/ec2/safe-ec2-deploy.sh`.** No hand copy, no direct SSM install, no `aws lambda update-function-code`, no Terraform in this cell.
- **Nothing enabled.** The Schwab integration stays disabled and no profile is activated. No grant for any person. AC11's local arm enables the integration in the probe's own process only, against emulated AWS; it reaches neither the host nor the live state store.
- **No egress off Opal infrastructure.** Unauthenticated GETs to `https://mcp.opalinvest.dev` are Opal infrastructure; no call to Claude, Anthropic, an interactive Entra sign-in or any vendor API. You do not reconnect any client.
- **No secret in evidence.** No token or secret value enters a committed file.
- **`mcp==1.28.0` is not raised.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W2-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-r-1`, round 1 (section 3, S9; section 6 N-1).
<owned_cells>OG-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGR1-AC1` .. `OGR1-AC12` (12). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/NFRA_OPLGTW.TO-OG-r-1.first-release-cutover.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGR1-AC1,OGR1-AC2,OGR1-AC3,OGR1-AC4,OGR1-AC5,OGR1-AC6,OGR1-AC7,OGR1-AC8,OGR1-AC9,OGR1-AC10,OGR1-AC11,OGR1-AC12`
BEFORE the `complete` flip. Result file `first-release-cutover.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. Binding on this cell: the no-half-landed-deploy moratorium. Notice N-1 (the cutover's client inventory to 0.0.0_AB_MSTR and 1.0.0_SA_CTO) precedes the spawn; it is a notice, not a gate.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This release is the first time the Gateway's code carries the new operations (DynamoDB, sts:AssumeRole twice); the instance records the lens re-run over the released source.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. comp-blast (L4, EC2, 47 of 47 traversal): every existing Gateway client is downstream of this release, which is why N-1 precedes it.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~2, queue position 2, handed after `OG-v-2`, `OG-i-1` and `OG-i-2` merge AND the issuer has sent notice
N-1 with `OG-p-1`'s client inventory. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567).
Decomposition v1 @8768f46770.

Amended 2026-09-15 ~14:5xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling msg 97114. W3-S9 is
disposed "in scope, round-2 cell", and the release is guarded by AC11. The hand-off hold of row `NFRA_OPLGTW-S8`
resolves into AC11. No criterion was removed.

Amended again 2026-09-15 ~22:1xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling msg 97251: AC12
adds the browser-login withholding line, which is W3-S22's round-1 disarm; its fix rides the round-2 email-keyed
cell. No criterion was removed.
