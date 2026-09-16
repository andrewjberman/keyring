# TO NFRA_OPLGTW.TO-OG-i-3 -- the ALB's explicit browser paths

<to_id>NFRA_OPLGTW.TO-OG-i-3</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-i-3` | **outcome_ref:** FWD-1, FWD-4, FWD-7 | **depends_on:** `OG-i-2` (same state), `OG-x-1` (the paths) | **slot:** ~1, queue position 3

---

## WORKER FACE

### THE CELL

`OG-i-3` -- **the ALB's explicit browser paths** for the download page and its OIDC callback, in
`infra/aws/terraform/opal-gateway/alb.tf`, applied and read back.

The PRD, verbatim (C1): *"The download browser uses a separate Gateway-owned OIDC callback, secure HttpOnly SameSite
cookies, anti-CSRF state/nonce and exact issuer/audience/signature validation ... Browser OIDC endpoints bypass ALB login
only at those explicit paths; existing default browser authentication and unrelated routes remain intact."* And
(operator journey): *"S9's deployment operator verifies ... public IPv4 DNS with globally routable answers, no cross-host
redirect, and WAF/proxy preservation of MCP/OAuth headers and streaming responses."*

**The exact paths are not chosen here.** They are named in two merged records at your hand-off:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/BROWSER_PATHS.json` (the OIDC login and callback,
from `OG-a-3`) and `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/DOWNLOAD_PATHS.json` (the download
page and its exchange, from `OG-x-1`). If either is absent at HEAD, that is a BLOCKING row; never guess a path.

The baseline you compare against is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(`OG-p-1`'s ALB rule readback and WAF association).

**FIRST ACT -- rename three applied names to the builder's output (amended by `2.0.0_SA_COO~O` before hand-off, per
`1.0.0_SA_CTO` ruling R-OG-7, msg 97548, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md`
@af1cd9f7d6; rows W1-S9 and W1-S11).** `OG-i-2` applied three names that the naming grammar grades OUT-OF-PATTERN. No
registry row can make the builder emit a person's name, so they are renamed in this apply, before any runtime consumer
binds an ARN.
- **The three names.** Re-derive each with `lib/opal_naming.py`, print it, and use the printed value (never type it):
  - `opal-mcp-emp-menachem-schwab-read` -> `name("gateway", None, "schwab-read", "role")`, ruled as `gateway-schwab-read-role`;
  - `opal-mcp-schwab-catalog-read` -> `name("gateway", None, "schwab-catalog-read", "role")`, ruled as `gateway-schwab-catalog-read-role`;
  - `opal-gateway-assume-schwab-readers` -> `name("gateway", None, "assume-schwab-readers", "policy")`, ruled as `gateway-assume-schwab-readers-policy`.
  - If a printed value differs from the ruled one, that is a BLOCKING row and no apply.
- **Where the person binding goes.** The person a grant belongs to lives in each role's trust-policy ExternalId, in the
  application's entitlement record and in the role's tags, never in a name.
- **Move every consumer in this order, with no occurrence left behind.** At the ruling's measurement those are:
  - `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` (6 occurrences);
  - `infra/aws/ec2/opal-gateway/app/integrations/schwab/aws_roles.py` (1);
  - `org/standards/NFRA_OPLGTW_CONTRACT.json` (2), bumped to version 1.1 with `reader_role`, `catalog_role` and the
    policy name as builder output;
  - `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json`, rewritten with the new ARNs.
  - Re-count at your HEAD with an unscoped search of the three old strings, and print the denominator. Every hit outside
    this project's historical records (evidence, result files, rows, rulings, logs) is moved here or filed as a BLOCKING row.
  - Run the existing module `tests/test_schwab_catalog.py` after the `aws_roles.py` change; it must stay green.
- **Blast radius of the rename.** At most the destroy and create of the ten resources `OG-i-2` added (the two roles,
  their policies and trust, the Gateway statement, and the two secrets' resource policies where they name a role). The
  trust and ExternalId pairs re-key at create. No served key, no source object, no other resource.
  - The plan must show only those rows plus this cell's own.
  - Re-run the OG-i-2 live denial and assume arms against the new ARNs, and record them in this cell's result file.
    OG-i-2's proof and evidence stand at their vintage under the old names; do not edit them.

**The read-only host-command document (amended by `2.0.0_SA_COO~O` before hand-off, per `1.0.0_SA_CTO` ruling R-OG-6,
msg 97522, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @f81896bae3, extending
R-OG-2).** From this cell onward, every host read uses `ssm:SendCommand` only on a NAMED SSM document whose content is a
fixed set of read-only commands. Never use `AWS-RunShellScript`.
- **The document:** this cell creates it as ONE `aws_ssm_document` resource (document type `Command`) in the new file
  `infra/aws/terraform/opal-gateway/ssm_readonly_host.tf`, in the same apply as the listener rules.
- **Its name:** the output of `lib/opal_naming.py name()`, never typed. A builder refusal is a BLOCKING row naming the
  missing registry row.
- **Its content:** only the read commands later cells need (file digests under the Gateway app directory, the systemd
  unit's status, process RSS, and installed package versions), with no shell interpolation of a caller string.
- **The pin:** in the same file, the operator role `opal-gateway-access-admin` gains `ssm:SendCommand` pinned to exactly
  that document's ARN plus the Gateway instance's ARN. Nothing else is added to that role.
- **Disclosure:** a probe that still runs as the IAM user rather than assuming that role discloses the run as unpinned.
- **Record:** the document's name and ARN go in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json`.

**Read:** the PRD's "C1" and "Operator journey, audit and release"; `infra/aws/terraform/opal-gateway/alb.tf` and
`waf.tf`; the two path records and the baseline above.

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGI3-AC<n>` or `VERDICT: FAIL-OGI3-AC<n> <reason>`. The HTTP arm (AC4) makes unauthenticated GETs to
`https://mcp.opalinvest.dev` without following redirects and records status and Location only.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGI3-AC1" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC1(?![0-9])</expect></criterion>
`OGI3-AC1` -- the plan changes only listener rules for the exact download and OIDC-callback paths `OG-a-3` and `OG-x-1` name, and leaves the default action unchanged.

<criterion id="OGI3-AC2" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC2(?![0-9])</expect></criterion>
`OGI3-AC2` -- the apply runs through `safe-apply` under a ledger entry opened and committed before the act and closed before the reads.

<criterion id="OGI3-AC3" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC3(?![0-9])</expect></criterion>
`OGI3-AC3` -- every pre-existing rule reads back byte-equal to `OG-p-1`'s baseline.

<criterion id="OGI3-AC4" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC4(?![0-9])</expect></criterion>
`OGI3-AC4` -- (difference) an unauthenticated GET to an unrelated path still redirects to the ALB login, while the same request to an explicit path reaches the application (status and Location header recorded).

<criterion id="OGI3-AC5" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC5(?![0-9])</expect></criterion>
`OGI3-AC5` -- the `idle_timeout` is read back with its ARN and UTC time.

<criterion id="OGI3-AC6" cell_refs="OG-i-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i3.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGI3-AC6(?![0-9])</expect></criterion>
`OGI3-AC6` -- the WAF association equals `OG-p-1`'s baseline.

<expected_criteria>OGI3-AC1, OGI3-AC2, OGI3-AC3, OGI3-AC4, OGI3-AC5, OGI3-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-i-2` and `OG-x-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open the entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-i-3-alb-paths ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-i-3-alb-paths.json` and entry BEFORE the apply; close the legs and the entry and COMMIT BEFORE the grading reads.
- **Terraform.** Only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`. `.tools/terraform.exe` provisioned by the issuer; if absent, a BLOCKING row. One state, one slot.
- **Blast radius.** The R-OG-7 rename's replacement of `OG-i-2`'s ten resources (see FIRST ACT), new listener rules at the named paths, the one read-only `aws_ssm_document`, and the one statement pinning `opal-gateway-access-admin`'s `ssm:SendCommand` to that document and the Gateway instance (ruling R-OG-6). The default action, every existing rule, the WAF association, the listener certificates and the security groups stay unchanged. Any other plan row is a BLOCKING row and no apply.
- **No egress off Opal infrastructure.** Unauthenticated GETs to `https://mcp.opalinvest.dev` are Opal infrastructure; no call to Claude, Anthropic, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W1-S<k>`. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/terraform/opal-gateway/alb.tf
infra/aws/terraform/opal-gateway/ssm_readonly_host.tf
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
infra/aws/ec2/opal-gateway/app/integrations/schwab/aws_roles.py
org/standards/NFRA_OPLGTW_CONTRACT.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-i-3-alb-paths.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-i-3`, round 1 (section 3, S9).
<owned_cells>OG-i-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGI3-AC1` .. `OGI3-AC6` (6). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-3.alb-browser-paths.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGI3-AC1,OGI3-AC2,OGI3-AC3,OGI3-AC4,OGI3-AC5,OGI3-AC6` BEFORE the
`complete` flip. Result file `alb-browser-paths.result.md` beside it. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. Binding on this cell: the no-half-landed-deploy and safe-apply-only moratoria. No project gate holds it; it waits on OG-x-1's merge by an edge.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes listener rules only; it adds no IAM operation, policy, principal or role, so the lens would receive an empty input for it.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. comp-blast on the ALB (this seat, graph 2026-09-15 08:34:46): 1 downstream node, opal-gateway-alb-sg, a lower bound. comp-routes is blind to this ALB (it resolves the portal's CloudFront catch-all), so AC3 and AC4 read it live.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~1, queue position 3, handed after `OG-i-2` and `OG-x-1` merge. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
