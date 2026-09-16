# TO NFRA_OPLGTW.TO-OG-p-1 -- deployed parity and the pre-change baseline

<to_id>NFRA_OPLGTW.TO-OG-p-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-p-1` | **outcome_ref:** FWD-7, FWD-8 | **depends_on:** -- (head; spawned at issuance) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`OG-p-1` -- **deployed parity and the pre-change baseline, read only.** Every later cell compares against what you record
here: the release cell against your parity and error baseline, the query engine against your peak memory, the ALB cell
against your rule readback, the producer cell against your list of marker consumers, and the capacity cell against your
latency baseline. **You change nothing in AWS or on the host.** Every AWS call you make is a read verb.

Write `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json` (machine-readable, one key
per criterion below) and `BASELINE.md` beside it (human-readable, each value with its instrument, UTC time and
denominator). The probe for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py`,
which takes the criterion's short id (`AC1` .. `AC13`), prints its measurement with vintage and denominator, then exactly
one line `VERDICT: PASS-OGP1-AC<n>` or `VERDICT: FAIL-OGP1-AC<n> <reason>`.

**Facts to re-ground, not to trust** (from the certified L4 rectangle, `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/rectangle.final.certified.json`):
the Gateway instance is recorded as `i-07dccb1615503ac99`, t4g.nano, `deployed_commit` 7bd89b5d71 at 2026-09-09T19:08:11Z
(`infra/aws/ec2/EC2_MANIFEST.json` services.opal-gateway); the ALB is `arn:aws:elasticloadbalancing:us-east-1:313476888478:loadbalancer/app/opal-gateway/89166a68f337e5a4`
with a recorded 60-second idle timeout; the source bucket is `opal-data-assets`, recorded with versioning enabled, AES256
and all four public-access blocks on; the bucket carries an S3 notification `advi-49f-silver-complete-accelerator` on
`schwab/08335338/meta/complete/` (`infra/aws/terraform/opal-assets/silver.tf:756-759`). Each of these is a record or a
declaration; your reads are the measurement.

**Read:** the PRD's sections "Scope and evidence boundary", "C6 - AWS boundaries, state and rollback" and "Operator
journey, audit and release"; `infra/aws/ec2/EC2_MANIFEST.json`; `infra/aws/ec2/opal-gateway/app/audit.py` (what an audit
record carries); `infra/aws/ec2/opal-gateway/deploy/opal-gateway.service`. Host reads go through SSM
(`aws ssm send-command` with `AWS-RunShellScript`, then `get-command-invocation`) using `.tools/aws`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGP1-AC1" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC1(?![0-9])</expect></criterion>
`OGP1-AC1` -- the running Gateway's per-file source digests, read on the host by SSM, are compared file by file with the tree at `EC2_MANIFEST.json`'s `deployed_commit`; mismatches listed, denominator printed.

<criterion id="OGP1-AC2" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC2(?![0-9])</expect></criterion>
`OGP1-AC2` -- the host's instance type, architecture, process and worker count, Python version and installed package versions are read on the host.

<criterion id="OGP1-AC3" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC3(?![0-9])</expect></criterion>
`OGP1-AC3` -- the ALB's listener rules, priorities, default browser OIDC action, WAF association and `idle_timeout` are read back live, each with its resource ARN and UTC time.

<criterion id="OGP1-AC4" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC4(?![0-9])</expect></criterion>
`OGP1-AC4` -- `opal-data-assets` versioning, default encryption, the four public-access-block flags and the policy status are read back live.

<criterion id="OGP1-AC5" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC5(?![0-9])</expect></criterion>
`OGP1-AC5` -- `opal-gateway-role`'s trust and every inline and attached policy are read back live.

<criterion id="OGP1-AC6" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC6(?![0-9])</expect></criterion>
`OGP1-AC6` -- `GetRole` on `opal-mcp-emp-menachem-schwab-read` and on `opal-mcp-schwab-catalog-read` each return NoSuchEntity.

<criterion id="OGP1-AC7" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC7(?![0-9])</expect></criterion>
`OGP1-AC7` -- `DescribeTable` on `opal-gateway-access-state` returns ResourceNotFound.

<criterion id="OGP1-AC8" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC8(?![0-9])</expect></criterion>
`OGP1-AC8` -- the `meta/complete/` object count, newest key and schema field per master are printed.

<criterion id="OGP1-AC9" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC9(?![0-9])</expect></criterion>
`OGP1-AC9` -- the bucket's notification configuration is read live, and every `ObjectCreated` consumer whose prefix covers `schwab/*/meta/complete/` is listed.

<criterion id="OGP1-AC10" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC10(?![0-9])</expect></criterion>
`OGP1-AC10` -- the Gateway's peak RSS over a stated window is recorded with its instrument named.

<criterion id="OGP1-AC11" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC11(?![0-9])</expect></criterion>
`OGP1-AC11` -- the existing-user baseline records p95 latency from the ALB's `TargetResponseTime` (CloudWatch) over a stated window, per target group and overall, with its sample count printed; the probe states that the ALB does not know the tool, and claims no per-tool figure. *(Amended by `2.0.0_SA_COO~O` before re-hand, per `1.0.0_SA_CTO` ruling R-OG-2, msg 97499, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @d6583eab37; row W2-S1.)*

<criterion id="OGP1-AC12" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC12(?![0-9])</expect></criterion>
`OGP1-AC12` -- the OAuth client inventory is read from the Gateway's persisted OAuth client registrations, lists every registered client with counts, and states process-locality as measured. The audit record's missing `client_id` is a finding against FWD-8, carried to L10 on row W2-S2, and is not fixed here. *(Amended per ruling R-OG-2, msg 97499 @d6583eab37; row W2-S2.)*

<criterion id="OGP1-AC13" cell_refs="OG-p-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGP1-AC13(?![0-9])</expect></criterion>
`OGP1-AC13` -- every AWS call in the cell's command log is a read verb (Describe, Get, List, Head), except that an `ssm:SendCommand` call is admitted if and only if the probe prints its command text and that text is a read; the probe reads your own command log and prints its denominator. *(Amended per ruling R-OG-2, msg 97499 @d6583eab37; row W2-S3.)*

**RE-HAND SCOPE (issuer, amended with the three criteria above).** `OGP1-AC1`..`AC10` PASSED by output and were recorded on 2026-09-15 (`baseline.result.md`, proof instance VALID). Since then, by design, `OG-i-1` has created `opal-gateway-access-state` and `OG-i-2` is creating the two reader roles, so `AC6` and `AC7` cannot be re-run truthfully as a pre-change baseline. Do not re-run `AC1`..`AC10`; carry their recorded rows unchanged. Rebuild the probe arms for `AC11`, `AC12` and `AC13` as amended, run and record those three, update `BASELINE.json`/`BASELINE.md` and the result file for them, and re-validate the whole instance.

<expected_criteria>OGP1-AC1, OGP1-AC2, OGP1-AC3, OGP1-AC4, OGP1-AC5, OGP1-AC6, OGP1-AC7, OGP1-AC8, OGP1-AC9, OGP1-AC10, OGP1-AC11, OGP1-AC12, OGP1-AC13</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** After the tree check, build your own venv once: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Record `.venv-og/Scripts/python -m pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`. A package install into this venv is a build act this order grants; no other install is.
- **READ ONLY.** This cell changes nothing in AWS and nothing on the Gateway host: no apply, no deploy, no restart, no write. A read that would need a write is a BLOCKING row.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API. AWS account 313476888478 (us-east-1) and the Gateway at `https://mcp.opalinvest.dev` are Opal infrastructure.
- **No secret in evidence.** No token, cookie, secret value, raw account ID or customer value enters a committed file. Record digests, counts, names and ARNs; never a secret's value or an audit record's arguments.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W2-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-p-1`, round 1 (section 3, S9).
<owned_cells>OG-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGP1-AC1` .. `OGP1-AC13` (13). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/NFRA_OPLGTW.TO-OG-p-1.baseline.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGP1-AC1,OGP1-AC2,OGP1-AC3,OGP1-AC4,OGP1-AC5,OGP1-AC6,OGP1-AC7,OGP1-AC8,OGP1-AC9,OGP1-AC10,OGP1-AC11,OGP1-AC12,OGP1-AC13`
BEFORE the `complete` flip. Result file `baseline.result.md` beside it. **Flip `complete` only when every MECHANICAL
criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW; self-test PASS 6/6 on the second run (the first was killed at 120 s). This project registers G-A .. G-F and notice N-1 (decomposition s.6); none binds this read-only cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed (deny-blind). This cell reads the APPLIED plane the lens cannot see (AC5, AC6) and adds no operation.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); the deliverables folder is granted by convention.
</preflight>

Seating: slot ~2, queue position 1 (then `OG-r-1`, `OG-r-2`). Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`, seated
by `0.0.0_AB_MSTR` (msg 96971) on Andrew-direct ~07:5xZ 2026-09-15 (LD-0567). Decomposition v1 @8768f46770, merged @7921d898c0.
