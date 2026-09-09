# TO ETFS_GUARDRAIL.TO-EG-s-7 -- the remediation ladder, rungs 0-2 unattended: probe, re-run the firm-scoped producer, re-check; NO rung may fabricate; and the one IAM grant that lets the reporter box invoke the three producers

<to_id>ETFS_GUARDRAIL.TO-EG-s-7</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- proof-of-spec instance `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-7.the-remediation-ladder-rungs-1-2-and-the-invoke-grant.proof_of_spec.json` VALID (rc=0). All 7 criteria PASS by output (S7-AC5/AC6 amended by the issuer's ruling @`2baa6af162` to plan/apply BY TARGET to `aws_iam_role_policy.reporter`, re-run and PASSED after the issuer copied the estate's pinned `.tools/terraform.exe` v1.9.8 into this worktree; the grant is APPLIED and confirmed on the live plane via `get-role-policy`, targeted 0-diff `rc=0`). Ledger `etfs-guardrail-eg-s-7-reporter-invoke-grant` OPENED then CLOSED. Rows `ETFS_GUARDRAIL-W1-S6` and `-S7` filed, both dispositioned by the issuer's ruling. Flip made by the assignee per the tree-convention grant. Prior: pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance (s.6a); Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S7a; s.7.4 the home; s.6 rulings 4 and 6; s.4 property 9; brief s.5) | **Decomp cell:** `EG-s-7` | **outcome_ref:** FWD-8 | **verb:** wire | **depends_on:** `EG-s-4` (your previous order), `EG-s-12` (your earlier order; its answer binds rung 2 for Inflection)

---

## THE CELL

`EG-s-7` (PRD s.7.2 S7a): NEW `data/etfs/scripts/coverage/remediate.py` -- rungs 1-2, unattended. Bound: *"No rung may fabricate. Rung 1 re-runs the producer; rung 2 re-checks upstream."* Ruling 4: *"Rungs 1-2 unattended; rung 3 STOPS AND ASKS."* Ruling 6: *"Egress is the THIRD fallback and should almost never fire -- in the only real instance, all five days were already in our own bucket."* Property 9: *"No rung, under any failure, writes a value that was not measured. If all three fail, the day stays missing and is reported as missing."*

**The ladder, as decided at L5 (decomposition v0.1.1 s.6a):**

- **rung 0 -- PROBE.** For each non-covered trading day, ask the firm-scoped producer, without writing: invoke `<producer>` with `{"date": d, "probe": true}` where the producer has a probe mode (`cot-etf-ownership-daily`, `bd-49f-etf-ownership-daily` -- added by `EG-s-1`/`EG-s-2` in another queue; until they land, a probe invoke returns the producer's ordinary dated behaviour, which for those two WRITES a slice -- so rung 0 is SKIPPED for a producer whose probe mode is not yet deployed, detected by the response shape, and the day goes to rung 1). The answer classifies: `partition False` -> D; `priced 0` -> B (STOP: expected, no rung 1); `priced > 0` -> C.
- **rung 1 -- RE-RUN THE PRODUCER** for C and UNKNOWN days: invoke `<producer>` with `{"date": d}` (the dated backfill path every producer already has; it LOUD-fails on an absent partition = D, skips an unpriced day = B, writes the slice = C recovered). The producer is the only writer; the ladder writes nothing. Producers by partner: cottonwood -> `cot-etf-ownership-daily`; 49financial -> `bd-49f-etf-ownership-daily` (the twin `EG-s-11` confirmed as the served writer; if that order's result named the `-canonical` twin instead, the map follows it -- read the result file); inflection -> `inf-etf-ownership-daily` (relied-on, not modified; its own answer is the discriminator).
- **rung 2 -- RE-CHECK.** Re-read `opal-data-etfs/daily/<partner>/<d>.json` (the slice may have landed since); for Inflection ALSO record what `EG-s-12`'s result says the deployed producer reads, so a D verdict for Inflection is stated against the bucket the running code uses, not the repo's.
- **rung 3 -- STOP AND ASK** is `EG-sb-7`, your NEXT order: this order leaves an unresolved day as `UNRESOLVED` with its class and returns; it does not ask, and it never calls a provider.

**The one IAM change.** The ladder runs inside the renderer's precondition on the reporter box (`EG-s-6`), whose instance role `etfs-reports-reporter-role` (`infra/aws/terraform/etfs-reports/iam.tf:24-59`) holds no `lambda:InvokeFunction`. Add ONE statement, `Sid = "InvokeProducersForRemediation"`, `Action = ["lambda:InvokeFunction"]`, `Resource` = exactly the three producer ARNs (`arn:aws:lambda:us-east-1:313476888478:function:cot-etf-ownership-daily`, `...:function:bd-49f-etf-ownership-daily`, `...:function:inf-etf-ownership-daily`) -- an invoke grant, not a data grant; no bucket, no prefix. Applied through `safe-apply` under a NEVER-2 ledger entry, plan read BEFORE apply, 0-diff after.

## DELIVERABLE

1. `data/etfs/scripts/coverage/remediate.py` -- ASCII, stdlib + boto3. API: `remediate_month(partner, month, classes, *, invoke=None, s3=None, dry_run=False) -> dict` returning `{"resolved": [...], "expected_empty": [...], "unresolved": [{"date", "class", "reason"}...], "rungs": {"probe": n, "rerun": n, "recheck": n}}`; `invoke(function_name, payload) -> dict` injected (boto3 `lambda.invoke` in production; a stub in tests); `dry_run=True` classifies and PLANS the invokes without making them. CLI: `python data/etfs/scripts/coverage/remediate.py --partner <p> --month YYYY-MM --dry-run` printing `LADDER: partner=<p> month=<m> holes=<n> rung0=<n> rung1=<n> rung2=<n> unresolved=<n> dry_run=True` (the only live mode this order exercises). The module carries NO HTTP client and NO provider call (rung 3 is a STOP by construction).
2. `data/etfs/scripts/coverage/tests/test_remediate.py` -- ZERO AWS calls; arms: (a) a C day -> invoke called exactly once with `{"date": d}`, the stub then reports the slice present -> resolved; (b) a B day (probe says priced 0) -> invoke NEVER called, day in `expected_empty`; (c) a D day (invoke raises the producer's "no ... partition" RuntimeError shape) -> `unresolved` with class D, no retry storm (exactly one invoke); (d) an UNKNOWN day with no probe mode -> rung 1 once, then re-check; (e) the ladder never calls `put_object` (assert on the stub s3); (f) `dry_run=True` makes zero invokes and returns the plan.
3. The IAM edit in `infra/aws/terraform/etfs-reports/iam.tf`, its plan, apply and 0-diff (BY TARGET, per S7-AC5 as amended), under the ledger entry `etfs-guardrail-eg-s-7-reporter-invoke-grant` (`python .tools/deploy_ledger.py open --slug etfs-guardrail-eg-s-7-reporter-invoke-grant --title "EG-s-7: lambda:InvokeFunction on the three ETFS producers for etfs-reports-reporter-role" --author 0.9.0_WK_ETFS_GUARDRAIL~1 --leg "iam|activation|etfs-reports-reporter-role|get-role-policy shows Sid InvokeProducersForRemediation with the three producer ARNs"`; then `close-leg --slug ... --leg-id iam --proof "<the get-role-policy output line>"`; then `close --slug ...`). The entry and its sentinel are COMMITTED (a staged sentinel dies with a forced teardown).
4. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/the-remediation-ladder-rungs-1-2-and-the-invoke-grant.result.md` -- every criterion's invocation and output verbatim with rc and denominator; the plan summary line; the ledger entry's path.

## ACCEPTANCE

<criterion id="S7-AC1" cell_refs="EG-s-7"><invocation>python -m pytest data/etfs/scripts/coverage/tests/test_remediate.py -q</invocation><expect>passed</expect></criterion>
`S7-AC1` -- the six-arm battery is green (record N passed).

<criterion id="S7-AC2" cell_refs="EG-s-7"><invocation>python -c "import re; s=open('data/etfs/scripts/coverage/remediate.py').read(); print('HTTP_CLIENT_IMPORTS=%d PUT_OBJECT_CALLS=%d' % (len(re.findall(r'^\s*(?:import|from)\s+(?:requests|urllib|http)\b', s, re.M)), len(re.findall(r'put_object\(', s))))"</invocation><expect>HTTP_CLIENT_IMPORTS=0 PUT_OBJECT_CALLS=0</expect></criterion>
`S7-AC2` -- the module carries no HTTP client and no S3 write: no rung can egress and no rung can fabricate, as a property of the bytes.

<criterion id="S7-AC3" cell_refs="EG-s-7"><invocation>python data/etfs/scripts/coverage/remediate.py --partner cottonwood --month 2026-08 --dry-run</invocation><expect>dry_run=True</expect></criterion>
`S7-AC3` -- the live DRY RUN over August cottonwood plans without invoking (record the counts; `holes=0` is the expected state after the 09-01 repair, and any other number is a real finding).

<criterion id="S7-AC4" cell_refs="EG-s-7"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/coverage/remediate.py data/etfs/scripts/coverage/tests/test_remediate.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S7-AC4` -- the commit gate is clean.

<criterion id="S7-AC5" cell_refs="EG-s-7"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false -target=aws_iam_role_policy.reporter</invocation><expect>1 to change</expect></criterion>
`S7-AC5` -- the TARGETED plan after the edit changes EXACTLY the reporter role policy (`aws_iam_role_policy.reporter`): `0 to add, 1 to change, 0 to destroy`. Run `.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports init -input=false` first if `.terraform/` is absent. If the targeted plan shows ANY other resource, do NOT apply: BLOCKING row, stop this criterion. (AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W1-S7: the `etfs-reports` directory carries a PRE-EXISTING `aws_instance.reporter` `user_data` drift (deferred as benign by NFRA_TERRAFORM-P2 @`1502fdd6f9`, 2026-07-08; found by row ETFS_GUARDRAIL-W1-S7) that is NOT this order's and is NOT applied -- a `user_data` change on `aws_instance` is applied by the provider through a STOP and START of the reporter instance, a confirm-with-Andrew act. The RULING: plan and apply BY TARGET to `aws_iam_role_policy.reporter`, state the target in the ledger entry, and record the FULL untargeted plan's summary and its `aws_instance.reporter` line VERBATIM in the result as the honest state of the directory. The drift itself is routed by the issuer, not by you.)

<criterion id="S7-AC6" cell_refs="EG-s-7"><invocation>.tools/aws iam get-role-policy --role-name etfs-reports-reporter-role --policy-name etfs-reports-reporter --query "PolicyDocument.Statement[?Sid=='InvokeProducersForRemediation'].Action" --output text</invocation><expect>lambda:InvokeFunction</expect></criterion>
`S7-AC6` -- the APPLIED plane carries the grant (read after `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-reports apply -input=false -auto-approve -target=aws_iam_role_policy.reporter`, which you run only after AC5's TARGETED plan read exactly one resource; then the 0-diff read is the TARGETED plan with `-detailed-exitcode` (rc=0), recorded in the result beside the full plan's remaining drift line -- AMENDED on row ETFS_GUARDRAIL-W1-S7).

<criterion id="S7-AC7" cell_refs="EG-s-7" judgment="true"/>
`S7-AC7` -- graded by the CVO at L9: rungs 0-2 are unattended and never fabricate; the invoke grant names exactly three functions and no bucket; rung 3 is a STOP left to `EG-sb-7`; the Inflection re-check is stated against the deployed producer's bucket per `EG-s-12`'s answer. RECORD; NO VERDICT.

<expected_criteria>S7-AC1, S7-AC2, S7-AC3, S7-AC4, S7-AC5, S7-AC6, S7-AC7</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override.
- **NEVER-2 / NEVER-9:** Terraform through `.tools/safe-apply.sh` ONLY (never bare `terraform apply`); the ledger entry opened BEFORE the apply and closed with proof after; the plan read BEFORE the apply; a plan touching anything but `aws_iam_role_policy.reporter` is NOT applied. `HALT_ACK=1` acknowledges the routine halt-gate surface after you have read it.
- **No firm bucket, no firm prefix, no data grant.** The Sid grants `lambda:InvokeFunction` on three ARNs and nothing else.
- **No live invoke in this order** except through `--dry-run` (which invokes nothing). The live ladder is exercised by the renderer's gate (`EG-s-6`) and the scheduled fire.
- **No provider call, no HTTP client, no standing egress grant** (ruling 4).
- **EVERY invocation is bounded.** `timeout 120`; a timeout is RECORDED AS THE OUTPUT (terraform init may need the retry).
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **THE TERRAFORM BINARY (AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W1-S6):** `.tools/terraform.exe` (v1.9.8) is the estate's terraform and it is GITIGNORED, so a fresh worktree lacks it; the issuer provisions a copy into your worktree's `.tools/` at hand-off (confirm `.tools/terraform.exe version` before any plan). NEVER substitute the PATH `terraform` (v1.14.5) for an apply: a newer CLI re-pins the remote state's `terraform_version` and the estate's binary can no longer read that state. If the copy is absent, that is a BLOCKING row, not a substitution.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
data/etfs/scripts/coverage/
infra/aws/terraform/etfs-reports/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-7`.
<owned_cells>EG-s-7</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL, etfs-reports or the reporter role.
comp-iam: RUN at L5 on etfs-reports-orchestrator -- 16 calls / 9 statements, 2 GRANTED, 4 GRANTED-BROAD, 1 UNGRANTED, 9 UNRESOLVABLE-RESOURCE; the reporter INSTANCE role was read at source (iam.tf:24-59, 5 statements, no lambda:InvokeFunction) -- the delta this order adds is exactly one statement; `comp-iam gaps` is re-run by the worker after the edit and recorded.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); the ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED, not merely staged.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S7-AC1` .. `S7-AC7`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-7.the-remediation-ladder-rungs-1-2-and-the-invoke-grant.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S7-AC1,S7-AC2,S7-AC3,S7-AC4,S7-AC5,S7-AC6,S7-AC7` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
