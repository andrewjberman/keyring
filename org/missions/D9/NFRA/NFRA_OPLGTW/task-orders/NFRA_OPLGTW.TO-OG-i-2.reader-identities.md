# TO NFRA_OPLGTW.TO-OG-i-2 -- the Schwab data-plane AWS identities

<to_id>NFRA_OPLGTW.TO-OG-i-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-i-2` | **outcome_ref:** FWD-3 | **depends_on:** `OG-i-1` (the same Terraform state) | **slot:** ~1, queue position 2

---

## WORKER FACE

### THE CELL

`OG-i-2` -- **the Schwab data plane's AWS identities**, in a new file `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf`:
two reader roles, one statement letting the Gateway assume exactly those two, and the secret that keys the account alias.
Applied, read back, and exercised from the Gateway host.

The design is the PRD's C6, verbatim:
- *"All silver reads use the dedicated assumed role `opal-mcp-emp-menachem-schwab-read` with trust restricted to
  opal-gateway-role plus its dedicated ExternalId. Allow GetObject/GetObjectVersion on the six exact prefixes and
  ListBucket only for those approved prefix forms. Attach explicit denies for other data paths/actions to this reader,
  not to the operational Gateway role. No fallback to Gateway instance credentials, broad opal-assets-read role, role
  selected by model, or role chaining. Application policy enforces the narrower dates/accounts/fields because IAM's
  prefix scope admits more."*
- *"Use a separate Gateway-assumable `opal-mcp-schwab-catalog-read` role for the two exact completion prefixes, with its
  own exact trust/ExternalId and deny-outside policy. Catalog metadata remains server-side. The data role does not gain
  metadata access. Current AES256 observations do not justify a new KMS grant; if deployment discovers another
  encryption mode, prove an exact-key permission and return the changed condition through the normal workflow. Existing
  wildcard employee-role trust uses the Tax SMA ExternalId and must not be broadened or reused."*
- The alias key (PRD C2): *"Expose a versioned, keyed HMAC account_ref over master plus account ID; keep its key in the
  existing approved secret mechanism, and never log raw IDs."* Provision that secret here, with the Gateway's read grant
  on exactly it; the alias code is another cell's.

Contract values: bucket `opal-data-assets`; `data_prefixes` = `schwab/08242234/silver/dim_position/`,
`schwab/08242234/silver/dim_balance/`, `schwab/08242234/silver/dim_asset/`, `schwab/08335338/silver/dim_position/`,
`schwab/08335338/silver/dim_balance/`, `schwab/08335338/silver/dim_asset/`; `completion_prefixes` =
`schwab/08242234/meta/complete/`, `schwab/08335338/meta/complete/`.

**One trap, measured at the cut.** The Gateway already holds `opal-gateway-assume-emp-roles`, which lets it assume
`arn:aws:iam::313476888478:role/opal-mcp-emp-*` with the Tax SMA ExternalId `opal-mcp-taxsma-pt2`, and two roles
`opal-mcp-emp-alyssa-*` already sit under it. The new data role's NAME matches that wildcard. Its TRUST must therefore
key on its own ExternalId, so the existing wildcard grant cannot assume it. AC6 proves exactly that.

Record in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json`: both role ARNs,
where each ExternalId and the alias key live (secret or parameter NAMES, never values), and the Gateway statement's
Sid. Later cells read that file.

**The alias-key secret's SHAPE (amended before hand-off by `2.0.0_SA_COO~O`, on row `NFRA_OPLGTW-W3-S25`;
`OG-z-3` merged to `CLOUD`).** `OG-z-3`'s `app/account_ref.py` is now on `CLOUD` and reads the alias key from ONE
secret whose id comes from the environment variable `SCHWAB_ACCOUNT_REF_SECRET_ID` and whose value is a JSON object
`{"current_version": "v<n>", "keys": {"v<n>": "<base64 of at least 32 bytes>"}}`. Provision the secret with THAT
shape (AC1 already covers the Gateway's read grant on it) and record its NAME, never its value, in
`SCHWAB_IDENTITIES.json` beside the role ARNs. That module is fail-closed in all six of its arms: a missing name, a
missing secret, a non-JSON value, a short key, no key for `current_version` or a non-base64 key all answer
`UNAVAILABLE` and never an unkeyed alias. So a secret of another shape does not degrade -- every account reference
on the live Gateway reads `UNAVAILABLE`.

**Read:** the PRD's "C2" and "C6"; the contract; `infra/aws/terraform/opal-gateway/taxsma_gateway_iam.tf` and
`secrets.tf` (conventions); `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914/reader-role-policy.proposed.json`
(the proposed data-role policy; a proposal, not a measurement).

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGI2-AC<n>` or `VERDICT: FAIL-OGI2-AC<n> <reason>`. On-host arms run through SSM on `i-07dccb1615503ac99`
with the instance's role. The silver key AC7 reads is named in your result file; no object bytes are kept.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGI2-AC1" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC1(?![0-9])</expect></criterion>
`OGI2-AC1` -- the plan creates exactly two roles with their policies, one statement on `opal-gateway-role` allowing `sts:AssumeRole` on exactly those two ARNs with each one's dedicated ExternalId, and the alias-key secret with the Gateway's read grant on it.

<criterion id="OGI2-AC2" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC2(?![0-9])</expect></criterion>
`OGI2-AC2` -- the plan shows zero changes to `taxsma_gateway_iam.tf`'s resources, to `opal-gateway-assume-emp-roles` and to the `opal-mcp-emp-alyssa-*` roles.

<criterion id="OGI2-AC3" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC3(?![0-9])</expect></criterion>
`OGI2-AC3` -- the data role allows GetObject and GetObjectVersion on the six data prefixes and ListBucket conditioned on those prefix forms, with explicit denies outside them (`meta/*` included) and no write action.

<criterion id="OGI2-AC4" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC4(?![0-9])</expect></criterion>
`OGI2-AC4` -- the catalog role allows GetObject and GetObjectVersion on the two completion prefixes and ListBucket conditioned on them, with explicit denies outside them.

<criterion id="OGI2-AC5" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC5(?![0-9])</expect></criterion>
`OGI2-AC5` -- each role trusts only `opal-gateway-role`, with its own ExternalId.

<criterion id="OGI2-AC6" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC6(?![0-9])</expect></criterion>
`OGI2-AC6` -- (difference) from the Gateway host, assuming each new role with the Tax SMA ExternalId fails, while assuming it with its dedicated ExternalId succeeds.

<criterion id="OGI2-AC7" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC7(?![0-9])</expect></criterion>
`OGI2-AC7` -- from the Gateway host, the data role's GetObject on a silver object of a listed prefix succeeds.

<criterion id="OGI2-AC8" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC8(?![0-9])</expect></criterion>
`OGI2-AC8` -- from the Gateway host, the data role's GetObject on a `meta/complete/` key is denied.

<criterion id="OGI2-AC9" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC9(?![0-9])</expect></criterion>
`OGI2-AC9` -- from the Gateway host, the data role's GetObject on a key outside the six prefixes is denied.

<criterion id="OGI2-AC10" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC10(?![0-9])</expect></criterion>
`OGI2-AC10` -- from the Gateway host, the data role's PutObject on a key under a listed prefix is denied.

<criterion id="OGI2-AC11" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC11(?![0-9])</expect></criterion>
`OGI2-AC11` -- from the Gateway host, the data role's ListBucket outside its prefix forms is denied.

<criterion id="OGI2-AC12" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC12(?![0-9])</expect></criterion>
`OGI2-AC12` -- from the Gateway host, assuming any role from a data-role session is denied.

<criterion id="OGI2-AC13" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC13(?![0-9])</expect></criterion>
`OGI2-AC13` -- from the Gateway host, the catalog role's GetObject on a `meta/complete/` key succeeds.

<criterion id="OGI2-AC14" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC14</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC14(?![0-9])</expect></criterion>
`OGI2-AC14` -- from the Gateway host, the catalog role's GetObject on a silver key is denied.

<criterion id="OGI2-AC15" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC15</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC15(?![0-9])</expect></criterion>
`OGI2-AC15` -- the source bucket policy's hash before the apply equals its hash after.

<criterion id="OGI2-AC16" cell_refs="OG-i-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i2.py AC16</invocation><expect>(?m)^VERDICT: PASS-OGI2-AC16(?![0-9])</expect></criterion>
`OGI2-AC16` -- policy-simulation results and live exercised results are recorded in separate, labelled sections.

<expected_criteria>OGI2-AC1, OGI2-AC2, OGI2-AC3, OGI2-AC4, OGI2-AC5, OGI2-AC6, OGI2-AC7, OGI2-AC8, OGI2-AC9, OGI2-AC10, OGI2-AC11, OGI2-AC12, OGI2-AC13, OGI2-AC14, OGI2-AC15, OGI2-AC16</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off (after `OG-i-1` merged). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** Your venv `.venv-og` (built by the command: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Record `pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open the change-management entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-i-2-reader-identities ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-i-2-reader-identities.json` and its entry BEFORE the apply; close each leg and the entry and COMMIT that BEFORE the reads that grade the act.
- **Terraform.** Only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`. `.tools/terraform.exe` is provisioned into your worktree by the issuer; if absent, a BLOCKING row -- never a PATH `terraform`. One state, one slot.
- **Blast radius.** The plan creates, and adds exactly one statement to the Gateway role's inline policies; it changes no existing statement and destroys nothing. Any other change is a BLOCKING row and no apply. No bucket policy, no KMS grant (if the measured encryption mode needs one, a row), no change to any Tax SMA or `opal-mcp-emp-alyssa-*` resource.
- **Denial probes never write.** A write-denial arm (AC10) targets a key that does not exist and records AccessDenied; if a probe write were ever to succeed, stop and file an ARMED row naming yourself as disarm owner.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.** No ExternalId value, alias key, credential or object content enters a committed file.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W1-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-i-2-reader-identities.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-i-2`, round 1 (section 3, S9).
<owned_cells>OG-i-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGI2-AC1` .. `OGI2-AC16` (16). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-2.reader-identities.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGI2-AC1,OGI2-AC2,OGI2-AC3,OGI2-AC4,OGI2-AC5,OGI2-AC6,OGI2-AC7,OGI2-AC8,OGI2-AC9,OGI2-AC10,OGI2-AC11,OGI2-AC12,OGI2-AC13,OGI2-AC14,OGI2-AC15,OGI2-AC16`
BEFORE the `complete` flip. Result file `reader-identities.result.md` beside it, with the `comp-iam` re-run after the
apply. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW; self-test PASS 6/6 on the second run. Binding on this cell: the no-half-landed-deploy and safe-apply-only moratoria. No project gate holds it.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed (deny-blind: it cannot answer "is this denied?"). This cell is the deny side the lens cannot read; AC6-AC14 exercise it live, and the instance records the lens re-run.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as the PRD's neighborhood. comp-blast (L4, EC2, 47 of 47 traversal) lists opal-gateway-assume-emp-roles and the two opal-mcp-emp-alyssa-* roles downstream of the Gateway: the reason for AC2 and AC6.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~1, queue position 2, handed after `OG-i-1` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
