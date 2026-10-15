# TO IRPT_DASHBD.TO-DB-c-7 -- BUILD the Cottonwood `holdings_performance_daily` FUNCTION in the repo: a third copy of the Inflection (IB-er-501) function, role, policy, scheduler role and schedule (created DISABLED) in the 49 Financial Terraform root, plus the handler change (a refused gold listing FAILS the fire loud) with its planted test; repo files only; nothing is planned, applied, built into a zip, uploaded or invoked

<to_id>IRPT_DASHBD.TO-DB-c-7</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~404</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>116</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the never-widen pair for DB-c-5, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_DB-c-5_R115_COTTONWOOD_HOLDINGS_PERFORMANCE_CTO_HALF.md` and COO half `deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_DB-c-5_R115_COTTONWOOD_HOLDINGS_PERFORMANCE_COO_HALF.md`, both at blob `ad049d506c`; the packet `deliverables/0.9.0_WK_IRPT_DASHBD~403/NEVER_WIDEN_PACKET_DB-c-5_R115.md` is the design | **Rows:** IRPT_DASHBD-D2-W404-S<k> | **Decomp cell:** `DB-c-7` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 3) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-404`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~404/`. Never push. No client data is read or written by this cell. A raw `aws` command in a shell call is denied by the repo's rail and this cell needs none.

**Why.** The CTO and the issuer signed the pair that lets an applier create, in order, the Cottonwood function, its principal, a 12-date catch-up and the schedule. The function does not exist, so this cell BUILDS it as repo files; the applier's later order plans and applies them. The 49 Financial Terraform root already holds a firm-isolated copy for Inflection (cell `IB-er-501`), which reuses the 49 Financial function's packaged zip (one `artifact_key`) and gives each firm its own function, execution role, scheduler role and schedule. Cottonwood is the third copy. The CTO also ruled that a refused gold listing must FAIL the fire loud, not fall back to one day (row `IRPT_DASHBD-D2-W403-S4`).

**Where things are (read each before editing).** Terraform root `infra/aws/terraform/investor-reporting/holdings-performance/`: `lambda.tf` (the 49 Financial module `irpt_holdings_performance` and the Inflection copy `irpt_holdings_performance_inf_lambda_name`/`irpt_holdings_performance_inf`), `iam.tf` (the Inflection role/policy blocks from line 134, `irpt_holdings_performance_inf_*`), `schedule.tf` (the Inflection scheduler role and schedule from line 122, `irpt_holdings_performance_inf_*`), `locals.tf` (the Inflection local set from line 89, `irpt_hp_inf_*`). Handler `infra/aws/lambda/investor-reporting/holdings-performance/handler.py` (`_days_to_compute` around line 100) and its tests `infra/aws/lambda/investor-reporting/holdings-performance/tests/test_catch_up.py`. The channel declaration is `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (key `blackdiamond_z09`); the producer is `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (`firm_scope()`/`resolved_prefix()` derive a channel's firm and prefixes; mirror them as the Inflection locals do). The design is `deliverables/0.9.0_WK_IRPT_DASHBD~403/NEVER_WIDEN_PACKET_DB-c-5_R115.md` (Change set, Function) and its facts `PACKET_FACTS_R115.json`.

**The cell (`DB-c-7`).**
1. **Locals** (`locals.tf`, appended, nothing existing edited): a Cottonwood local set `irpt_hp_cot_*` modelled one for one on the Inflection set `irpt_hp_inf_*`: the source key `blackdiamond_z09`, its declaration entry, the firm derived the way the producer derives it (no firm token typed), the read bucket and the Black Diamond silver `fact_holdings` prefix, the firm's gold bucket, `irpt_hp_cot_gold_write_arns` (exactly the two gold tables `holdings_performance_daily` and `holdings_performance_manifest` under `irpt/<firm>/gold/`, and nothing else), and the read/list ARNs: read and list on the Black Diamond silver prefix AND list-and-read on the principal's OWN daily gold table (so the scheduled path can list the newest landed day), as in the packet's grants. Where the declaration for this channel differs in shape from `orion` (for example it carries a `master` or a balance prefix), follow what `sources.json` and `holdings_performance.py` say and state it in your report.
2. **Function** (`lambda.tf`, appended): `module "irpt_holdings_performance_cot_lambda_name"` (the opal_name builder with the derived firm as scope, function `holdings-performance`, kind `lambda`) and `module "irpt_holdings_performance_cot"` (yang-lambda), the same artifact key, handler, runtime, timeout, memory and layer as the Inflection copy, its tags naming this cell; outputs for its name and ARN.
3. **Role and policy** (`iam.tf`, appended): the Lambda trust policy, `aws_iam_role "irpt_holdings_performance_cot"` (name from the opal_name builder, kind `role`), `data "aws_iam_policy_document" "irpt_holdings_performance_cot"` and `aws_iam_role_policy "irpt_holdings_performance_cot"`: PutObject ONLY on `irpt_hp_cot_gold_write_arns`; GetObject and ListBucket on the Black Diamond silver prefix; ListBucket (with the prefix condition) and GetObject on its own daily gold prefix; logs on its own log group; NO delete action, NO wildcard action, no other table or firm. Outputs for the role ARN.
4. **Scheduler role and schedule** (`schedule.tf`, appended): `aws_iam_role "irpt_holdings_performance_cot_scheduler"` with a policy allowing `lambda:InvokeFunction` on the Cottonwood function only, and `aws_scheduler_schedule "irpt_holdings_performance_cot"`: name from the opal_name builder (kind `daily`, function `holdings-performance`), `state = "DISABLED"`, `schedule_expression = "cron(15 8 ? * MON-FRI *)"`, `schedule_expression_timezone = "America/New_York"`, flexible window OFF, target the Cottonwood function with input `{"kind":"irpt_holdings_performance_daily","note":"...","source":"blackdiamond_z09"}`; outputs for its name and state. The state stays `DISABLED`: the CTO ruled it is enabled only after the catch-up's after-read, by a later one-line change the applier makes.
5. **Handler** (`handler.py`, ONLY inside `_days_to_compute`): when `lister(...)` raises, the function raises (a `RuntimeError` naming the exception type and message, chained with `from exc`), so a refused listing FAILS the fire; the print of `WARN: gold listing failed ... computing the single day` goes. The other three branches stay exactly as they are: an event with a `date` is that day; an empty landed list is `[T]`; a newest landed day at or after `T` is `[]`; a gap is the oldest `MAX_DAYS_PER_FIRE` days after the newest landed day through `T`. Do not touch any other function in the file.
6. **Tests** (`tests/`): add `test_refused_listing_fails_loud.py` with `def test_refused_listing_fails_loud` that plants a lister raising `PermissionError("AccessDenied")` and expects `_days_to_compute` to raise (load the handler the way `test_catch_up.py` does, with the producer stubbed); and UPDATE the two existing cases in `test_catch_up.py` that encode the old fallback (the unreadable-listing branch of `test_catch_up_an_empty_or_unreadable_gold_listing_keeps_the_single_day`, and `test_S297_listing_failure_and_empty_landed_still_plan_the_single_day`): the unreadable-listing assertion now expects the raise, the empty-landed assertion stays `[T]`. Edit nothing else in that file.
7. **Do NOT**: run `terraform init`, `plan` or `apply`; build, zip or upload the Lambda package (`build-and-upload.sh`); call any AWS API; edit any existing Terraform block (this is additive; `DBC116-3-AC1` rejects a removed line); edit the producer, the declaration or `lambda-source-map.json`. The handler is SHARED: the 49 Financial and Inflection functions run the same zip, so they carry the change only when the applier later rebuilds and applies; say so in your report.

<criterion id="DBC116-1-AC1" cell_refs="DB-c-7"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r116/p116_bcw.py" . DBC116-1-AC1</invocation><expect>DBC116-1-AC1 PASS</expect></criterion>
`DBC116-1-AC1` -- the handler no longer holds the single-day fallback print and `_days_to_compute` raises; calling it with a lister that raises raises; the manual-date, no-landed-day, already-landed and gap branches return exactly what they did before; the planted test exists and pytest passes on it and on `test_catch_up.py`. Base: FAIL.

<criterion id="DBC116-2-AC1" cell_refs="DB-c-7"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r116/p116_bcw.py" . DBC116-2-AC1</invocation><expect>DBC116-2-AC1 PASS</expect></criterion>
`DBC116-2-AC1` -- the Terraform root holds the Cottonwood name module, function module, role, policy document, role policy, scheduler role and schedule under the labels `irpt_holdings_performance_cot*`; the schedule block is `DISABLED`, `cron(15 8 ? * MON-FRI *)`, `America/New_York`, targets the Cottonwood function and names `blackdiamond_z09`; the policy document grants no delete and no wildcard action and its PutObject uses the Cottonwood write-arn local; `terraform fmt -check` reports no unformatted file when the binary is present. Base: FAIL.

<criterion id="DBC116-3-AC1" cell_refs="DB-c-7"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r116/p116_bcw.py" . DBC116-3-AC1</invocation><expect>DBC116-3-AC1 PASS</expect></criterion>
`DBC116-3-AC1` -- against the tree this round was cut on, the four `.tf` files have added lines and no removed line; `handler.py` changes only inside `_days_to_compute`; no file outside the four `.tf` files, `handler.py` and the two test files under `holdings-performance/tests/` changed in the two `holdings-performance` folders (Terraform and Lambda) or the producer's folder, against the commit this round was issued at (`7f16db08c3`; the first cut named an earlier commit and counted other seats' later changes elsewhere under `infra/aws`, the issuer's defect, worker row `IRPT_DASHBD-D2-W404-S1`). Base: FAIL (no added line).

<expected_criteria>DBC116-1-AC1, DBC116-2-AC1, DBC116-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, the producer, the declaration, every contract and every other Terraform root.
- **Reads and writes.** Reads: repo files. Writes: the files in `<paths>`, your folder and your private folder. No AWS call, no Terraform command that touches state or a provider, no zip, no upload, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A shape you cannot mirror from the Inflection copy (for example a declaration key with no counterpart) is a row and a report, never a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W404-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~404/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-7.cottonwood-holdings-performance-function-build-repo-files-only.md
infra/aws/terraform/investor-reporting/holdings-performance/iam.tf
infra/aws/terraform/investor-reporting/holdings-performance/lambda.tf
infra/aws/terraform/investor-reporting/holdings-performance/locals.tf
infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf
infra/aws/lambda/investor-reporting/holdings-performance/handler.py
infra/aws/lambda/investor-reporting/holdings-performance/tests/test_catch_up.py
infra/aws/lambda/investor-reporting/holdings-performance/tests/test_refused_listing_fails_loud.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 3, cell `DB-c-7`.
<owned_cells>DB-c-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC116-1-AC1, DBC116-2-AC1, DBC116-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~404/IRPT_DASHBD.TO-DB-c-7.cottonwood-holdings-performance-function-build-repo-files-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC116-1-AC1 DBC116-2-AC1 DBC116-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the Cottonwood firm token the locals derived (a registry scope key) and the read/gold buckets; any place the channel's declaration differed from `orion` and what you did; the names the opal_name modules will produce; the two existing tests you changed and how; the statement that the handler is shared and nothing was rebuilt or uploaded; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: repo files only; nothing is planned, applied, uploaded or invoked. The blast of the later apply (36 keys, one function, two roles, one disabled schedule) is bounded in the signed pair at blob ad049d506c.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the order writes the TEXT of a role and its policy; no principal or grant is created. The CTO half read the grants against both bucket policies.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is written as text in state DISABLED; none is created.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the three criteria FAIL at base and DBC116-1-AC1 was exercised on a scratch tree (fallback restored: FAIL; refusal patched without the updated old tests: FAIL).
</preflight>
