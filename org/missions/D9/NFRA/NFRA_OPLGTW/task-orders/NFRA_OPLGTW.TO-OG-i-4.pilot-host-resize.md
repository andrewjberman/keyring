# TO NFRA_OPLGTW.TO-OG-i-4 -- the pilot host: t4g.nano to t4g.small

<to_id>NFRA_OPLGTW.TO-OG-i-4</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-i-4` | **outcome_ref:** FWD-7 | **depends_on:** `OG-p-1`, `OG-i-3` (same state); **HELD on gate G-A** | **slot:** ~1, queue position 4

---

## WORKER FACE

### THE CELL

`OG-i-4` -- **the pilot host**: change `aws_instance.gw`'s `instance_type` in `infra/aws/terraform/opal-gateway/main.tf`
from `t4g.nano` to `t4g.small`, apply, and re-take the existing-user baseline on the new host.

The PRD, verbatim: *"The declared existing t4g.nano/one-worker deployment is not presumed to have capacity for this
workload. S9 targets t4g.small (ARM64, 2 GiB) for the pilot, still on the existing Gateway service ... this is a design
target, not a deployed measurement."* Contract `capacity`: `target_instance_type` t4g.small, `target_architecture` arm64,
`target_memory_mib` 2048.

**Gate G-A, stated here because it decides whether you act at all.** Changing an EC2 instance type stops and starts the
instance, and CLAUDE.md's Agent Autonomy section requires human confirmation for stopping EC2. You are spawned only
after that confirmation exists as a recorded Andrew-direct under
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/` or `org/tier1_exec/*/deliverables/`, and your ledger entry cites it by
path@commit (AC1). **If you cannot find that record at HEAD, do nothing to the instance: file a BLOCKING row and stop.**

Baseline to compare against: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(`OG-p-1`'s instrument and window rule for the existing-user baseline).

**Read:** the PRD's "Operator journey, audit and release" (capacity paragraph); `infra/aws/terraform/opal-gateway/main.tf`
(`aws_instance.gw`); the baseline above; `infra/aws/ec2/opal-gateway/deploy/opal-gateway.service`.

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGI4-AC<n>` or `VERDICT: FAIL-OGI4-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGI4-AC1" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC1(?![0-9])</expect></criterion>
`OGI4-AC1` -- the ledger entry cites the Andrew-direct record authorizing this stop and start of the Gateway instance, by path@commit, and that record exists at the cited commit.

<criterion id="OGI4-AC2" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC2(?![0-9])</expect></criterion>
`OGI4-AC2` -- the plan changes only `instance_type` on `aws_instance.gw` and does not replace the instance.

<criterion id="OGI4-AC3" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC3(?![0-9])</expect></criterion>
`OGI4-AC3` -- the apply runs through `safe-apply` under a ledger entry opened and committed before the act and closed before the reads.

<criterion id="OGI4-AC4" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC4(?![0-9])</expect></criterion>
`OGI4-AC4` -- the instance reads t4g.small, arm64, running.

<criterion id="OGI4-AC5" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC5(?![0-9])</expect></criterion>
`OGI4-AC5` -- after the restart, the Gateway's systemd unit is active and an unauthenticated `/mcp` returns 401 with the resource challenge.

<criterion id="OGI4-AC6" cell_refs="OG-i-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i4.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGI4-AC6(?![0-9])</expect></criterion>
`OGI4-AC6` -- the existing-user baseline is re-taken on the new host with `OG-p-1`'s instrument and window rule.

<expected_criteria>OGI4-AC1, OGI4-AC2, OGI4-AC3, OGI4-AC4, OGI4-AC5, OGI4-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **G-A.** No stop, start, resize or apply on the instance without the recorded Andrew-direct at HEAD. Its absence is a BLOCKING row and a stop.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Deploy discipline (spine L7).** Open the entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-i-4-pilot-host ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-i-4-pilot-host.json` and entry BEFORE the apply; close and COMMIT BEFORE the grading reads. A death after the stop and before the commit is the expensive shape: if the instance is not running when you resume, restoring it is your first act and a row.
- **Terraform.** Only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`. `.tools/terraform.exe` provisioned by the issuer; if absent, a BLOCKING row. One state, one slot.
- **Blast radius.** One attribute on one resource. A plan that replaces the instance, or changes any other attribute or resource, is a BLOCKING row and no apply.
- **No code change.** This cell changes the host, not the Gateway's code or configuration.
- **No egress off Opal infrastructure.** No call to Claude, Anthropic, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W1-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/terraform/opal-gateway/main.tf
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-i-4-pilot-host.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-i-4`, round 1 (section 3, S9; section 6 G-A).
<owned_cells>OG-i-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGI4-AC1` .. `OGI4-AC6` (6). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-4.pilot-host-resize.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGI4-AC1,OGI4-AC2,OGI4-AC3,OGI4-AC4,OGI4-AC5,OGI4-AC6` BEFORE the
`complete` flip. Result file `pilot-host-resize.result.md` beside it. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell is HELD on project gate G-A (CLAUDE.md Agent Autonomy: stopping EC2 needs human confirmation); the no-half-landed-deploy and safe-apply-only moratoria bind it.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes one instance attribute; it adds no IAM operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. comp-blast (L4, EC2, 47 of 47 traversal) lists the instance's downstream; a stop affects every existing Gateway user for its duration, which is why G-A exists.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~1, queue position 4, handed only after `OG-i-3` merges AND the G-A record is at HEAD. Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
