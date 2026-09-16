# TO NFRA_OPLGTW.TO-OG-i-1 -- the opal-gateway-access-state table and its two grants

<to_id>NFRA_OPLGTW.TO-OG-i-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-i-1` | **outcome_ref:** FWD-1, FWD-3, FWD-4, FWD-6, FWD-7 | **depends_on:** -- (head; spawned at issuance) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`OG-i-1` -- **the `opal-gateway-access-state` DynamoDB table and its two grants**, in a new file
`infra/aws/terraform/opal-gateway/schwab_access_state.tf`, applied, read back and exercised. This is the durable store
for OAuth clients, pending authorizations, codes, refresh families, download tickets and catalog snapshots (`RUNTIME#`
keys) and for principal profiles, entitlements, approvals and operator audit (`POLICY#` keys). No cell before you writes
any record in it, and you write only isolated probe records.

The design you implement is the PRD's C6 and the contract's `state_store` block, verbatim in the PRD:
- *"The one new DynamoDB table uses encryption, point-in-time recovery, on-demand capacity, logical expiry and conditional
  transactions. Its operational role grant is limited to needed Get/Put/Update/TransactWrite operations on that exact
  table; operator administration has separate authorization."*
- *"The DynamoDB partition key separates POLICY#<tid>#<oid> records (profile, grant, approval, operator audit) from
  RUNTIME# namespaces (client, pending auth, code, refresh family, ticket, catalog). Runtime may strongly read POLICY keys
  but its write actions are conditioned through dynamodb:LeadingKeys to the RUNTIME prefix only; all transaction items
  must satisfy the restriction. The operator role alone may conditionally update POLICY records and append the matching
  operator audit in one transaction. Ordinary runtime and operator roles have no policy DeleteItem or table-admin
  permission. Profile, grant, approval and revocation tombstones have no TTL attribute; cleanup applies only to expiring
  RUNTIME records. A13 includes a runtime attempt to write POLICY and an operator revision race using isolated records."*

The runtime principal is the existing `opal-gateway-role` (the Gateway's instance role). The operator principal is a
new, separate role for the administration command a later cell builds; name it, and record its ARN.
Contract: table `opal-gateway-access-state`, region `us-east-1`, account `313476888478`, consistency
`strong_reads_and_conditional_transactions`, TTL `cleanup_only_never_authorization`.

**Read:** the PRD's "C6 - AWS boundaries, state and rollback"; `org/standards/NFRA_OPLGTW_CONTRACT.json` `state_store`;
`infra/aws/terraform/opal-gateway/main.tf` (provider, the role `opal-gateway-role`); an existing grant file in the
same root for its conventions (`infra/aws/terraform/opal-gateway/taxsma_gateway_iam.tf`).

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py`,
taking the short id (`AC1` .. `AC12`), printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGI1-AC<n>` or `VERDICT: FAIL-OGI1-AC<n> <reason>`. Save the plan as JSON (`terraform show -json`) in your
deliverables so AC1 reads a file, not memory. AC7's on-host arm runs through SSM on `i-07dccb1615503ac99` with
the instance's own role. AC8's operator race runs under the operator role, assumed from the operator identity,
because the runtime role cannot write `POLICY#` keys by design (row `NFRA_OPLGTW-W1-S2`). Both use probe keys
`RUNTIME#probe-og-i1-<utc>` and `POLICY#probe-og-i1-<utc>`.

**The WAF description backfill, as ruled (amended before re-hand-off, on `1.0.0_SA_CTO`'s /self-drive ruling msg
97237; rows `NFRA_OPLGTW-W1-S1`, `NFRA_OPLGTW-S3`).** Every plan of this root also carries two in-place `~ description`
backfills on `aws_wafv2_ip_set.opal_blocked_ips_regional_v4` and `_v6` (`waf.tf:261`, `:302`), declared by the closed
project NFRA_OPSEC202609. They are ADMITTED BY NAME into this apply, the root's first, on four conditions. Each
condition is a line in your change-management entry:
- the plan's out-of-cell changes are EXACTLY those two, `~ description` only, with `addresses` absent from the diff
  (AC10);
- `aws wafv2 get-ip-set` reads both sets' live address lists immediately before and after the apply, and they are
  identical, printed with their counts (AC11). WAF's UpdateIPSet sends the full list, so this readback is what proves
  the reconciler's list survived;
- plan and apply run in ONE safe-apply run, never from a stale saved plan, so the lock token is fresh. A
  `WAFOptimisticLockException` is a clean abort and a re-run, never a retry that forces;
- after the apply, a fresh plan of the root reads 0 changes on both sets (AC12).
Your first run's declaration is preserved at `59b567eed0`
(`git show 59b567eed0:infra/aws/terraform/opal-gateway/schwab_access_state.tf`). It uses the key names `pk`/`sk`/
`expires_at` that the merged adapter reads (row S2). It was removed from CLOUD unapplied (@716fffcba4), and it returns
only through this order's apply. Your first run's evidence is merged under your deliverables folder.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGI1-AC1" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC1(?![0-9])</expect></criterion>
`OGI1-AC1` -- the plan creates only the table, the runtime grant and the operator role and policy; the only changes to existing resources are the two admitted WAF `~ description` updates (AC10), and nothing is destroyed.

<criterion id="OGI1-AC2" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC2(?![0-9])</expect></criterion>
`OGI1-AC2` -- the apply runs through `safe-apply` under a ledger entry whose OPEN sentinel is committed before the act (the probe compares the sentinel's commit time with the apply's recorded start).

<criterion id="OGI1-AC3" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC3(?![0-9])</expect></criterion>
`OGI1-AC3` -- the ledger entry is closed and committed before the reads below (the probe compares the close commit's time with the first readback's).

<criterion id="OGI1-AC4" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC4(?![0-9])</expect></criterion>
`OGI1-AC4` -- `describe-table` reads SSE enabled, point-in-time recovery enabled, PAY_PER_REQUEST billing, the TTL attribute set and the designed key schema.

<criterion id="OGI1-AC5" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC5(?![0-9])</expect></criterion>
`OGI1-AC5` -- the runtime grant allows Get, Put, Update and TransactWrite on exactly the table ARN, with write actions conditioned on `dynamodb:LeadingKeys` matching `RUNTIME#*`, and no DeleteItem or table-admin action.

<criterion id="OGI1-AC6" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC6(?![0-9])</expect></criterion>
`OGI1-AC6` -- the operator principal is separate, may conditionally update `POLICY#` records and append `operator_audit` in one transaction, and holds no DeleteItem on `POLICY#` and no table-admin action.

<criterion id="OGI1-AC7" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC7(?![0-9])</expect></criterion>
`OGI1-AC7` -- (difference) from the Gateway host, an isolated runtime-principal write to a `POLICY#` key is AccessDenied, while the same write to a `RUNTIME#` key succeeds in the same harness (A13).

<criterion id="OGI1-AC8" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC8(?![0-9])</expect></criterion>
`OGI1-AC8` -- two concurrent operator revisions of one isolated `POLICY#` record yield exactly one success and one ConditionalCheckFailed (A13).

<criterion id="OGI1-AC9" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC9(?![0-9])</expect></criterion>
`OGI1-AC9` -- a probe `POLICY#` record carries no TTL attribute.

<criterion id="OGI1-AC10" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC10(?![0-9])</expect></criterion>
`OGI1-AC10` -- the saved plan's changes to resources outside this cell are exactly two `update` actions, on `aws_wafv2_ip_set.opal_blocked_ips_regional_v4` and `aws_wafv2_ip_set.opal_blocked_ips_regional_v6`, each changing only `description`, with `addresses` absent from the diff; no other existing resource changes and nothing is destroyed.

<criterion id="OGI1-AC11" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC11(?![0-9])</expect></criterion>
`OGI1-AC11` -- (discriminating) `aws wafv2 get-ip-set` read immediately before and immediately after the apply returns identical address lists for both sets, their counts printed, and both reads are recorded in the change-management entry.

<criterion id="OGI1-AC12" cell_refs="OG-i-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py AC12</invocation><expect>(?m)^VERDICT: PASS-OGI1-AC12(?![0-9])</expect></criterion>
`OGI1-AC12` -- after the apply, a fresh plan of the root reads 0 changes on both WAF IP sets and on the resources this cell created.

<expected_criteria>OGI1-AC1, OGI1-AC2, OGI1-AC3, OGI1-AC4, OGI1-AC5, OGI1-AC6, OGI1-AC7, OGI1-AC8, OGI1-AC9, OGI1-AC10, OGI1-AC11, OGI1-AC12</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** After the tree check, build your own venv once: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Record `.venv-og/Scripts/python -m pip freeze` in your result file. Never commit `.venv-og/` or `.scratch/`. A package install into this venv is a build act this order grants; no other install is.
- **Deploy discipline (spine L7).** Open the change-management entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-i-1-access-state --title "..." --author 0.9.0_WK_NFRA_OPLGTW~1 --leg "..."`, and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-i-1-access-state.json` and its entry under `org/critical_paths/change_management/` BEFORE the apply. After the apply, `close-leg` each leg with its proof and `close` the entry, and COMMIT that BEFORE the reads that grade the act. A death between the act and the commit leaves the world changed and the record silent -- so the order is open, commit, act, close, commit, read.
- **Terraform.** Only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`. `.tools/terraform.exe` is provisioned into your worktree by the issuer at spawn; if it is absent, that is a BLOCKING row -- never substitute a PATH `terraform`. The `infra/aws/terraform/opal-gateway` root is ONE state and only slot ~1 applies it; never from a second worktree.
- **Blast radius.** The plan creates and destroys nothing. The ONLY changes it may show to existing resources are the two `~ description` updates on the WAF IP sets admitted above (ruling 97237). The existing Tax SMA grant (`taxsma_gateway_iam.tf`), the `opal-gateway-assume-emp-roles` policy and every existing role in the root stay byte-unchanged. A plan that shows any other change, or any destroy, is refused: a BLOCKING row, no apply. Plan and apply run in ONE safe-apply run; a `WAFOptimisticLockException` is a clean abort and a re-run, never a forcing retry.
- **Probe records only.** You write only isolated `RUNTIME#probe-og-i1-*` and `POLICY#probe-og-i1-*` items. No profile, grant or client record for any real person.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.** No credential or secret value enters a committed file.
- **No new monitor, alarm, SNS or notification path.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W1-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/terraform/opal-gateway/schwab_access_state.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-i-1-access-state.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-i-1`, round 1 (section 3, S9).
<owned_cells>OG-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGI1-AC1` .. `OGI1-AC12` (12). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-1.access-state-table.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGI1-AC1,OGI1-AC2,OGI1-AC3,OGI1-AC4,OGI1-AC5,OGI1-AC6,OGI1-AC7,OGI1-AC8,OGI1-AC9,OGI1-AC10,OGI1-AC11,OGI1-AC12`
BEFORE the `complete` flip. Result file `access-state-table.result.md` beside it, naming the table ARN, the operator
role ARN and the `comp-iam` re-run over the root after the apply. **Flip `complete` only when every MECHANICAL
criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW; self-test PASS 6/6 on the second run. Binding on this cell: the no-half-landed-deploy and safe-apply-only moratoria. No project gate (G-A .. G-F) holds it.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed (deny-blind). This cell adds DynamoDB actions on one table for opal-gateway-role and a new operator role; its instance records the lens re-run after the apply, and AC5-AC8 read the APPLIED and EXERCISED planes the lens cannot see.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/terraform/** refuses a worker by lane and admits it only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 1 (then `OG-i-2`, `OG-i-3`, `OG-i-4`), the one holder of the `opal-gateway` Terraform
state. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
The issuer copies `.tools/terraform.exe` into the slot's worktree at spawn.

Amended 2026-09-15 ~21:0xZ, after the first run (refused at the plan, W1-S1) and before re-hand-off, by
`2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s /self-drive ruling msg 97237. The changes:
- the two WAF `~ description` backfills are admitted by name into this apply, the root's first, under four conditions;
- AC1 and the blast-radius bound are narrowed to exactly those two;
- AC10, AC11 and AC12 are added;
- the AC8 harness sentence is corrected to the operator role (W1-S2).
No criterion was removed.
