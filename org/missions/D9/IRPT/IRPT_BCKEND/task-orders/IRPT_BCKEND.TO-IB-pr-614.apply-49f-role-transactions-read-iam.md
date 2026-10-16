# TO IRPT_BCKEND.TO-IB-pr-614 -- APPLY the signed IAM pair: the 49 Financial holdings-performance role reads its own split-adjust transactions prefix (list + get on `schwab/08335338/silver/fact_trn/` only), by one Terraform plan of 1 change; then ONE recovery invoke with the schedule's own input (completes IB-pr-612 Act 1; row `IRPT_BCKEND-D2-S217`; packet blob 03cd6e9d46; CTO half signed @334655f31b)

<to_id>IRPT_BCKEND.TO-IB-pr-614</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair: packet and COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_49F_PERF_ROLE_TRANSACTIONS_READ_IAM_PAIR_PACKET_AND_COO_HALF.md` (git blob `03cd6e9d4618a0c46c36bc8adb8e2cfb9485fa86`; READ IT ALL: section 2 the exact edit, 3a the battery, 4 the branches and stop rule) and the CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_49F_PERF_ROLE_TRANSACTIONS_READ_IAM_CTO_HALF.md` (SIGNED, conditions 1 to 4) | **Decomp cell:** `IB-pr-614` (decomposition section 240) | **outcome_ref:** FWD-21 | **DEADLINE: the grant applied AND the recovery invoke read by 13:00Z today (2026-10-16); else the CTO's fallback, Branch B of IB-pr-612 Act 1 (all three functions back to `o9UugRAV...`, the same session), which is the issuer's call to order, not yours.**

---

## WORKER FACE

**Cell `IB-pr-614` (inlined).** IB-pr-612 Act 1 put `LiDXhN74...` on the three holdings-performance functions at 05:15:36Z. The 49 Financial function's first scheduled run (11:30Z plus two retries) errored 3 of 3 with `AccessDenied s3:ListBucket on opal-data-assets`: its role `irpt-49f-holdings-performance-role` has no grant for the new split-adjust transactions read (`infra/aws/terraform/investor-reporting/holdings-performance/locals.tf` derives the grants from `positions_prefix` and `balance_prefix` only). This order adds that one grant, derived from the declaration and not typed, then recovers the failed scheduled day with ONE invoke. **IB-pr-612's ledger stays OPEN (this is its completion); you do not close it. Act 2 (IB-pr-613) is NOT started.** Paths you post are `file:///` absolute URIs or markdown links, with the repo-relative form for another box. No account, holding name or value in any record: counts and hashes only.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**

1. **Gates (READ ONLY).** (a) `git hash-object` of the packet equals `03cd6e9d4618a0c46c36bc8adb8e2cfb9485fa86`; the CTO half reads SIGNED and names `03cd6e9d46`. (b) IB-pr-612's ledger reads OPEN and is the only ledger or marker naming the root `holdings-performance` or any of its three functions (same worktree-union read as IB-pr-612 step 1c; print `worktrees_read` and `marker_files_read`); no other apply runs on the root while you work (CVO rule, msg 8750). (c) `get-function-configuration` CodeSha256 of the 49F function equals `LiDXhN74TsATYhoQKzs+Oy1qtNn3hDJxxjkLa0ZlfLg=`. Any disagreement: STOP.
2. **Simulate battery BEFORE** (packet 3a; `aws iam simulate-principal-policy` on `arn:aws:iam::313476888478:role/irpt-49f-holdings-performance-role`). Arms: ALLOWED-after (2): `s3:ListBucket` on `arn:aws:s3:::opal-data-assets` with `s3:prefix` `schwab/08335338/silver/fact_trn/date=2026-10-14/`, and `s3:GetObject` on `arn:aws:s3:::opal-data-assets/schwab/08335338/silver/fact_trn/date=2026-10-14/data.parquet`. DENIED-always (8): the Inflection and Cottonwood silver prefixes resolved from `sources.json` (list + get each = 4), `smartx/platform/silver/fact_allocation_account_map/` (list + get = 2), `schwab/08335338/silver/fact_acc/` (list + get = 2). UNCHANGED (4): `schwab/08335338/silver/dim_position/` and `.../dim_balance/` (list + get). BEFORE must read the two ALLOWED-after arms implicitDeny, the 8 denied arms implicitDeny and the 4 unchanged arms allowed; anything else: STOP. Record counts only.
3. **The edit.** Make exactly the `locals.tf` edit of packet section 2 (the two locals `irpt_hp_read_object_arns` and `irpt_hp_read_list_conditions` gain the `try(v.split_adjust.transactions_prefix, null)` term) and nothing else; commit that ONE file (`.tools/safe-commit.sh`, your own author, `-F`). Name the pre-edit blob for Branch B.
4. **Plan, apply.** `terraform plan` to a planfile; it must read **exactly 1 to change, 0 to add, 0 to destroy, the one being `aws_iam_role_policy.irpt_holdings_performance`** (an output change is not a resource); any other resource or any destroy: STOP and revert the edit. Then `bash .tools/safe-apply.sh` on that planfile. Never a console edit, never `put-role-policy`.
5. **After-read.** Re-plan reads 0 changes. Simulate battery AFTER: the 2 ALLOWED arms allowed, the 8 DENIED arms implicitDeny, the 4 UNCHANGED arms allowed. A denied arm allowed or an allowed arm still denied: STOP and Branch B of the grant (revert the one edit, `safe-apply`, read the battery back equal to BEFORE) and report at once.
6. **The recovery invoke, ONCE.** Read the schedule's own input (`aws scheduler get-schedule`, `Target.Input`; expect `{"kind":"irpt_holdings_performance_daily","note":"scheduled fire; handler.py resolves the target trading day itself","source":"schwab_08335338"}`). `lambda invoke` `irpt-holdings-performance-lambda`, RequestResponse, with EXACTLY that payload (no `date` key), once. It recovers the failed scheduled day; it is not a new run. Read: status 200, no `FunctionError`, the days written (only those the handler resolves), the run manifest's `split_adjust.declared` true, and `run_ok`. A `FunctionError`, a day outside what the handler resolves, or a need for a second invoke: STOP and report (no second invoke). Confirm from the schedule the next fire: Monday 2026-10-19T11:30:00Z.
7. **Do NOT close any ledger** (the issuer closes IB-pr-612's after reading your record). **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB245-1_iam_record.json`:
`{"gates":{"packet_blob":"03cd6e9d4618a0c46c36bc8adb8e2cfb9485fa86","both_halves_signed":true,"act_1_ledger_open":true,"function_code_sha256":"LiDXhN74TsATYhoQKzs+Oy1qtNn3hDJxxjkLa0ZlfLg=","one_change_at_a_time":true},"change":{"files_changed":["infra/aws/terraform/investor-reporting/holdings-performance/locals.tf"],"plan":{"add":0,"change":1,"destroy":0,"resources":["aws_iam_role_policy.irpt_holdings_performance"]},"path":"terraform-safe-apply","safe_apply_rc":0,"replan_changes":0},"simulate_before":{"allowed_arms_implicit_deny":2,"denied_arms_implicit_deny":8,"unchanged_arms_allowed":4},"simulate_after":{"allowed_arms_allowed":2,"denied_arms_implicit_deny":8,"unchanged_arms_allowed":4},"recovery":{"invokes":1,"event":{"kind":"irpt_holdings_performance_daily","note":"scheduled fire; handler.py resolves the target trading day itself","source":"schwab_08335338"},"status_code":200,"function_error_absent":true,"manifest_split_adjust_declared":true,"run_ok":true,"days_written":<n>,"next_scheduled_fire_utc":"2026-10-19T11:30:00Z"},"rollback_performed":false,"act2_started":false,"ledger_closed_by_applier":false,"counters":{"lambda_invokes":1,"iam_changes":1,"artifact_uploads":0,"schedule_changes":0,"files_deleted":0,"markers_closed":0,"served_keys_written_by_me":0}}`.
8. **Run the three criteria below from the repository root** (record every output and exit code verbatim in `IB245-1_criteria_output.txt`), write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths. Report once, under 150 words; report each STOP at once.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB245-1-AC1" cell_refs="IB-pr-614"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r245/p245_cells.py" . IB245-1-AC1</invocation><expect>IB245-1-AC1 PASS</expect></criterion>
<criterion id="IB245-1-AC2" cell_refs="IB-pr-614"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r245/p245_cells.py" . IB245-1-AC2</invocation><expect>IB245-1-AC2 PASS</expect></criterion>
<criterion id="IB245-1-AC3" cell_refs="IB-pr-614"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r245/p245_cells.py" . IB245-1-AC3</invocation><expect>IB245-1-AC3 PASS</expect></criterion>

<expected_criteria>IB245-1-AC1, IB245-1-AC2, IB245-1-AC3</expected_criteria>

What the checks grade: AC1 the packet blob, the CTO half signed at it, IB-pr-612's ledger still open, the function at the candidate; AC2 one file edited, the plan 1/0/0 on the one policy through safe-apply, re-plan 0, the simulate battery before and after as counts; AC3 one recovery invoke with the schedule's own input, no FunctionError, the manifest declares split_adjust, the next fire, no rollback, Act 2 not started, the counters. Do not edit the checks.

## BOUNDS

- **Grant:** `locals.tf` of `infra/aws/terraform/investor-reporting/holdings-performance` (the one edit), `safe-apply` on one saved plan of 1 change, `iam simulate-principal-policy`, reads of the schedule, the function and its logs, ONE `lambda invoke` of `irpt-holdings-performance-lambda` with the schedule's own input, your record folder. **NO second invoke; NO `date` key in the event; NO invoke of the siblings; NO other IAM change; NO change to any schedule, layer, environment or code; NO artifact upload; NO deletion; no Act 2; no ledger closed.**
- **Refusal clause:** STOP on any of: a packet or half byte that differs; an unexpected open ledger or marker on the root; the function not at `LiDXhN74...`; a BEFORE battery that differs; a plan that is not exactly the one policy; an AFTER arm that differs (Branch B of the grant); a `FunctionError` or a second invoke needed. A bound in a CTO half is raised only by a CTO half.
- **Row ids** `IRPT_BCKEND-D2-IB2-S<k>` or the next free `D2-S<k>` the gate accepts. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
infra/aws/terraform/investor-reporting/holdings-performance/locals.tf
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-614.apply-49f-role-transactions-read-iam.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 240 (round 4, workstream ~PM), cell `IB-pr-614`.
<owned_cells>IB-pr-614</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB245-1-AC1, IB245-1-AC2, IB245-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-614.apply-49f-role-transactions-read-iam.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the artifact moved is ONE inline IAM policy document (`aws_iam_role_policy.irpt_holdings_performance`, role `irpt-49f-holdings-performance-role`): two read statements gain one prefix of the role's own custodian master; ONE writer (`safe-apply`, one saved plan of 1 change); the other two roles, the functions' code, schedules and every S3 object are untouched; the rollback is the one-edit revert and one `safe-apply` (packet section 4). The ONE recovery invoke writes only the day the handler resolves for the scheduled fire it recovers.
comp-iam: RUN -- the change IS the grant: list (prefix-conditioned) and get on `arn:aws:s3:::opal-data-assets/schwab/08335338/silver/fact_trn/*` for the 49F role; proven by the 14-arm simulate battery before and after (packet 3a).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- the schedule is READ (its input and next fire), never changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p245_cells.py IB245-1 dry-run at base on dell2 2026-10-16 ~11:58Z: AC1, AC2, AC3 FAIL (no record). Positive control (control245.py): the three positives PASS and 29 negatives (a wrong packet blob, an unsigned or absent CTO half, a closed ledger, a moved function digest, two files edited, a plan of 2 changes or with a destroy or another resource, a non-safe-apply path, a re-plan above 0, a gap not shown before, a denied arm allowed, an allowed arm still denied, a lost unchanged arm, two invokes, a `date` key in the event, a FunctionError, an undeclared or failed run, no day written, a wrong next fire, a rollback, Act 2 started, the applier closing the ledger, a schedule change, a deletion) each fail their own arm (0 unexpected). NOT measured by me: the live role policy now, the simulate arms' real answers (the denied arms' exact prefixes are resolved by you from `sources.json`), the day the handler will resolve.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD.
</preflight>
