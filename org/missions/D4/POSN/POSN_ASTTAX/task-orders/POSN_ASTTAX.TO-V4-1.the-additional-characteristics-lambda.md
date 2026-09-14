# TO POSN_ASTTAX.TO-V4-1 -- BUILD AND DEPLOY the additional lambda: per-satellite weighted characteristics (fee, yield, duration, beta, returns) from `holdings.json` weights x per-ticker inputs, NULL disclosed and never renormalised, on its OWN schedule (AT5-s-4, B4; C-SATELLITE-SOURCE)

<to_id>POSN_ASTTAX.TO-V4-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~20</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-SATELLITE-SOURCE: *"aggregated server-side by an additional lambda"*) - **Decomp cell:** `AT5-s-4` - **Issuance:** round 5,
wave 2, same slot as `TO-V2-1` -- **you start this order only after your `TO-V2-1` is `complete` at HEAD.** **GATES `AT5-s-7`, `AT5-s-8`.**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~20`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~20;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit only via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~20 <0.9.0_WK_POSN_ASTTAX~20@opal.agent>" -F <msgfile> -- <paths>`,
msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`.

## THE CELL

Andrew ~17:2xZ, verbatim: *"Satellites simply need to have an additional lambda to do weighted characteristics aggregates."*
A SEPARATE function, per his word -- not a second output of the registry producer.

**Inputs (all READ-only for you):**
- `s3://opal-data-cot/platinum/satellites/holdings.json` -- YOUR OWN `TO-V2-1` artifact; its schema is the one you committed
  (`satellites.<code>.holdings[].{ticker, weight, asset_class, sub_asset_class, sleeves}`), read it back from HEAD, never from memory.
- `s3://opal-data-portal-v2/json/positioning/positioning_data.json` -- Yang's served models (gzip body; top-level `current_holdings`
  carries per-ticker fee / yield / duration / beta / returns for every ticker a Yang book holds).
- `s3://opal-data-etfs/bbg/<asof>/characteristics.parquet` (+ `run_manifest.json`) -- the Bloomberg ETF daily pull
  (`integrations/bloomberg/pipeline/etf_daily_pull.py:37-38`, `:330-350`). GLD and VXX enter it as `EXTRA_SECURITIES` from the
  2026-09-15 07:00 ET fire (@`ac3e03a317`); the latest partition today is `bbg/2026-09-11/` with GLD/VXX ABSENT. Resolve `<asof>`
  from the clock and `lib/trading_calendar.py` (T-1 business day), never by listing (no `s3:ListBucket`).

**Output:** `s3://opal-data-cot/platinum/satellites/characteristics.json` (a NEW key, zero writers today):
```
{as_of, inputs: {holdings_as_of, positioning_data_as_of, bbg_as_of},
 satellites: {<code>: {fee, yield, duration, beta, returns: {...the fields the inputs carry...},
                       coverage: {weight_with_value, weight_null}}}}
```
Each aggregate = sum over the satellite's holdings of (weight x per-ticker value) over the tickers that HAVE a value, divided by
100 (weights are percent). A ticker with no value in either source contributes NOTHING to the numerator and its weight to
`coverage.weight_null`; **NEVER renormalise** to the covered weight -- the null share is DISCLOSED, not hidden. Source precedence
per ticker: Yang's `current_holdings` where present, else the Bloomberg pull, else NULL.

**Build shape -- the registry producer's, mirrored:** `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/
{lambda_function.py (the TRIGGER, passes no date), build_package.py (--pin REQUIRED, repo-mirroring layout)}`; the LOGIC at
`data/assets/scripts/gold/build_satellites_characteristics.py` (vendored by pin). Terraform
`infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`: role with `s3:GetObject` on EXACTLY the three input
keys (holdings.json; `json/positioning/positioning_data.json` on `opal-data-portal-v2`; `bbg/*/characteristics.parquet` + `bbg/*/
run_manifest.json` on `opal-data-etfs`), `s3:PutObject` on EXACTLY `platinum/satellites/characteristics.json`, the cross-firm
deny MIRRORED from the registry producer's, `AWSLambdaBasicExecutionRole`; memory/timeout MEASURED from a local run; an
EventBridge rule `cron(20 7 * * ? *)` UTC (20 minutes after the registry producer's 07:00Z fire, its own clock, NEVER
success-of-upstream); target + permission. **NO alarm, NO SNS, NO monitor** (the standing moratorium).

**The cross-firm gate, read at the cut so you do not re-derive it:** `.tools/ds-precommit-check.py:68-70` keys on a script's
HOME DIR (`data/cot/`, `data/black_diamond/`) and bans `opal-data-bd|inf|49financial` / `opal-data-cot`; `opal-data-portal-v2` and
`opal-data-etfs` are in NO foreign list and neither `data/assets/` nor `infra/aws/lambda/cot-pipeline/` matches a home dir. The
gate does not fire on your reads. If it DOES fire, that is a row and a STOP -- a gate edit is not yours.

### NEVER-WIDEN: NON-APPLICATION, STATED

`characteristics.json` has zero writers today; no existing served output moves. Both halves
(`org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` @`f381f6f402`, `.../NEVER_WIDEN_ROUND5_CTO_HALF.md`
@`af667548d1`) state the non-application. What still binds: the ledger entry, `safe-apply`, `comp-iam gaps`, the deny, the schedule.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W20-S<k>` (continue your own S-sequence from TO-V2-1), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="V4-AC1" cell_refs="AT5-s-4"><invocation>timeout 60 grep -o -m1 "<status>[^<]*</status>" org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V2-1.holdings-json-beside-registry-json.md</invocation><expect>the status line reads `complete` at HEAD, and `s3api head-object` on platinum/satellites/holdings.json returns 200. Otherwise this order STOPS with a row: its premise is your own prior cell.</expect></criterion> `V4-AC1` -- THE DEPENDENCY, READ BACK, NOT ASSUMED.

<criterion id="V4-AC2" cell_refs="AT5-s-4"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-round5-b4-satellites-characteristics --title "POSN_ASTTAX B4: cot-satellites-characteristics-producer (new function)" --author 0.9.0_WK_POSN_ASTTAX~20 --leg "L1|git|SITEZ commit of producer + trigger + build_package + tf|hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip|sha256" --leg "L3|verify|plan (new function + role + policies + rule + target + permission)|summary" --leg "L4|activation|safe-apply|summary" --leg "L5|verify|0-diff|No changes" --leg "L6|verify|QA invocation lands characteristics.json|s3api head + content read" --leg "L7|verify|schedule enabled with the function as target|describe-rule + list-targets" --leg "L8|verify|next scheduled 07:20Z fire lands organically (the negative arm; recorded by the COO)|head after the fire"</invocation><expect>the entry path with 8 legs OPEN; L8 is the organic arm, left OPEN by design and named in your report.</expect></criterion> `V4-AC2` -- THE LEDGER.

<criterion id="V4-AC3" cell_refs="AT5-s-4"><invocation>timeout 600 python <LOCAL_DRY_RUN_BUILD></invocation><expect>nine satellites; for `Opal Satellite 15`, `coverage.weight_null` is >= 8.34 (GLD has no value in either source today) and `weight_with_value + weight_null` equals that satellite's total holdings weight to 0.01; every aggregate printed with the ticker set that fed it; no aggregate is computed over a renormalised base (print the formula you used once).</expect></criterion> `V4-AC3` -- THE ARITHMETIC, WITH THE NULL SHARE VISIBLE.

<criterion id="V4-AC4" cell_refs="AT5-s-4"><invocation>timeout 300 python <DIFFERENCE_CONTROL_SAME_RUN></invocation><expect>Sat 15's `coverage.weight_null` DROPS by 8.34 and its fee/yield aggregates MOVE, while the run without the synthetic value leaves them where V4-AC3 read them -- the two arms DIFFER. If they do not, the control is not discriminating: report that, not the result. The live bucket is never written.</expect></criterion> `V4-AC4` -- THE CONTROL THAT SHOWS WHAT CHANGES WHEN THE INPUT EXISTS (the 2026-09-15 pull, simulated on scratch).

<criterion id="V4-AC5" cell_refs="AT5-s-4"><invocation>timeout 180 bash .tools/commit-gate.sh</invocation><expect>clean on every changed/new .py and .tf, output cited; both ASCII limbs read; ds-precommit's cross-firm limb quoted as NOT FIRING with the home-dir line it printed.</expect></criterion> `V4-AC5` -- THE GATE, INCLUDING THE CROSS-FIRM LIMB'S OWN VOICE.

<criterion id="V4-AC6" cell_refs="AT5-s-4"><invocation>timeout 600 python infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/build_package.py --pin <COMMITTED_HASH></invocation><expect>the zip built from git at your pin with its member list printed at the repo-mirroring layout (lib/trading_calendar.py included if the builder imports it); a moving ref REFUSED.</expect></criterion> `V4-AC6` -- THE PACKAGE, PINNED.

<criterion id="V4-AC7" cell_refs="AT5-s-4"><invocation>timeout 300 comp-iam gaps</invocation><expect>the new role's statements GRANTED to exactly the three input keys and the one output key; no wildcard bucket resource; the cross-firm deny present; the DESIRED-plane caveat quoted.</expect></criterion> `V4-AC7` -- THE GRANTS, NARROW, DESIRED PLANE.

<criterion id="V4-AC8" cell_refs="AT5-s-4"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan -target=module.cot_satellites_characteristics_producer -target=aws_iam_role.cot_satellites_characteristics_producer -target=aws_iam_role_policy.cot_satellites_characteristics_producer_s3 -target=aws_iam_role_policy.cot_satellites_characteristics_producer_cross_firm_deny -target=aws_iam_role_policy_attachment.cot_satellites_characteristics_producer_basic -target=aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily -target=aws_cloudwatch_event_target.cot_satellites_characteristics_producer_daily -target=aws_lambda_permission.events_cot_satellites_characteristics_producer -out=.scratch/b4.tfplan</invocation><expect>N to add, 0 to change, 0 to destroy, with N printed and every added resource named -- all of them yours; any change or destroy is a STOP with a row.</expect></criterion> `V4-AC8` -- THE PLAN: ADDS ONLY, ALL YOURS.

<criterion id="V4-AC9" cell_refs="AT5-s-4"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/cot-pipeline apply .scratch/b4.tfplan</invocation><expect>Apply complete! Resources: N added, 0 changed, 0 destroyed (N equal to V4-AC8's); HALTGT output pasted.</expect></criterion> `V4-AC9` -- THE APPLY.

<criterion id="V4-AC10" cell_refs="AT5-s-4"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan</invocation><expect>No changes. (Unscoped this time: the new resources must not perturb anything else in the stack.)</expect></criterion> `V4-AC10` -- 0-DIFF, UNSCOPED.

<criterion id="V4-AC11" cell_refs="AT5-s-4"><invocation>timeout 300 .tools/aws lambda invoke --function-name cot-satellites-characteristics-producer --payload '{}' .scratch/b4_invoke.json</invocation><expect>StatusCode 200; then `s3api head-object` on platinum/satellites/characteristics.json returns 200 and its body's nine coverage pairs EQUAL V4-AC3's local run (same inputs, same day). QA proof on demand, never production evidence.</expect></criterion> `V4-AC11` -- THE KEY EXISTS BECAUSE YOU MADE IT EXIST.

<criterion id="V4-AC12" cell_refs="AT5-s-4"><invocation>timeout 120 .tools/aws events describe-rule --name cot-satellites-characteristics-producer-daily --query '{state:State,expr:ScheduleExpression}' --output json</invocation><expect>ENABLED, cron(20 7 * * ? *); list-targets-by-rule names the function. L8 (the organic fire) is the COO's to record.</expect></criterion> `V4-AC12` -- THE SCHEDULE, ITS OWN CLOCK.

<criterion id="V4-AC13" cell_refs="AT5-s-4"><invocation>timeout 300 bash infra/aws/lambda/ci/record-resource-deploy.sh cot-pipeline</invocation><expect>recorded per that script's contract (or record-terraform-deploy.sh --plan .scratch/b4.tfplan, stated); legs L1-L7 closed with proofs; L8 OPEN by design.</expect></criterion> `V4-AC13` -- RECORDED.

<criterion id="V4-AC14" cell_refs="AT5-s-4" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether the null-share disclosure is honest for a reader of the page -- a 91.66%-covered fee for Sat 15 shown beside an 8.34% null share -- and whether the source precedence (Yang first, Bloomberg second) is the right one for a ticker both carry. Record the readings and offer NO verdict.</expect></criterion> `V4-AC14` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V4-AC1, V4-AC2, V4-AC3, V4-AC4, V4-AC5, V4-AC6, V4-AC7, V4-AC8, V4-AC9, V4-AC10, V4-AC11, V4-AC12, V4-AC13, V4-AC14</expected_criteria>

<placeholders>COMMITTED_HASH, DIFFERENCE_CONTROL_SAME_RUN, LOCAL_DRY_RUN_BUILD</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V4-1.the-additional-characteristics-lambda.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~20/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/build_satellites_characteristics.py
infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/
infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf
infra/aws/terraform/cot-pipeline/CHANGELOG.json
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-4`.
<owned_cells>AT5-s-4</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-2` (your own TO-V2-1: holdings.json and its schema, read back at HEAD). DOWNSTREAM:
`AT5-s-7` (F3) binds your schema line verbatim; `AT5-s-8` (R1) reads the served key.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut -- the NEVER clauses bind: no monitor, safe-apply, own schedule; your ledger entry is opened at V4-AC2.
comp-iam: RUN -- 474 .tf files scanned, 404 policy blocks attached, 26 NOT ATTACHED; BLIND on the sibling producer (0 boto3 call sites in its trigger, logic vendored by pin) and BLIND on this NEW function until its .tf exists; V4-AC7 grades YOUR .tf on the DESIRED plane and V4-AC11 exercises the grants on the APPLIED plane.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not read the Bloomberg characteristics parquet's
column names -- the returns fields are whatever it carries, printed by V4-AC3, never invented; (2) the issuer has not measured the
function's memory with pandas/pyarrow loaded -- your dry run is the first; (3) the cron offset 07:20Z is the issuer's proposal from
the registry producer's measured 07:00Z; if V2's run measures longer than 20 minutes, widen the offset and say so in a row.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~20/POSN_ASTTAX.TO-V4-1.the-additional-characteristics-lambda.proof_of_spec.json
</proof_of_spec>
