# POSN_AGGFIX -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~Z` at L6, in the round-1 issuance commit, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the
gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only during the
round.** Every row goes inside the ONE fenced json array below, per `org/surprise_channel/schemas/investigation_item.schema.json`; a
worker's id is `POSN_AGGFIX-Z-W<slot>-S<k>`, a seat's `POSN_AGGFIX-Z-S<k>`.

```json
[
  {
    "id": "POSN_AGGFIX-Z-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-15T18:48:41Z",
    "one_line": "PRD v0.2 C-NO-SILENT-EMPTY describes the five books' failure fallback as 'writes aum 0 into each book' (:1798), but on a WHOLLY failed weight read the producer writes no current_holdings at all (load_aum_data returns {} at :1475-1477, and generate_positioning_data's `if aum_data:` gate at :2374-2381 with :2392-2395 omits the block and data_date); aum 0 arises only on a PARTIAL read. TO-A2-1 keeps both arms exactly, so no behaviour moves; the PRD sentence under-describes today's fallback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md @cbd85e5cff :192-195 (C-NO-SILENT-EMPTY): 'The five model books keep their current failure fallback, which writes `aum` 0 into each book (`:1798`)'.",
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @605c03f81f :1475-1477: `except Exception as e:` prints WARN and `return {}` (the success return is :1474).",
        "same file @605c03f81f :2374-2381, inside generate_positioning_data (def at :2117): `aum_data = load_aum_data(data_date)`; `if aum_data:` extracts current_holdings, else `current_holdings = None`; :2392-2395 adds current_holdings and data_date to the output only when current_holdings is truthy.",
        "same file @605c03f81f :1796-1799: `'aum': aum_data.get(model_code, 0)` -- the 0 is reached only when aum_data is non-empty but lacks a code (a partial read)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "C-NO-SILENT-EMPTY (PRD v0.2 :192-195): a failed weight read leaves the five books with their current fallback, aum 0 in each book.",
    "world_is": "Two arms: a wholly failed read serves the shared file with NO current_holdings key and no data_date (every Models-mode book disappears for every viewer); a partial read writes aum 0 into the missing book only. The decomposition's AF1-s-6 parenthesis repeated the PRD's one-arm wording; TO-A2-1 states both arms and its A2-AC7/A2-AC8 prove each, and the producer's never-widen COO half names the wholly-failed arm as Branch B with a rollback.",
    "notes": "Carried for 1.0.0_SA_CTO~Z's round analysis: a PRD touch to C-NO-SILENT-EMPTY's sentence would align the text with the measured fallback; nothing in this round waits on it. Filed by the issuer at L6; it also opens this channel, which the row gate refuses to open empty."
  },
  {
    "id": "POSN_AGGFIX-Z-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-15T19:10:49Z",
    "one_line": "The shared positioning file has THREE writers, not one: besides the producer, yang-time-machine (Dev-triggered portal restore) and rollback-protocol.sh restore prior S3 versions of every key under json/ by prefix. After TO-A3-1's Branch A, a restore to any execution before the change re-serves current_holdings.AGG and July book aum to every signed-in viewer until the next pipeline run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py @SITEZ HEAD :4-10 restores all captured JSON outputs of the latest execution at or before a target date by CopyObject with CopySourceVersionId; restore_outputs :197-239; only json/portfolios/ is skipped (:52-58).",
        "infra/aws/lambda/v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py :22 JSON_PREFIX = 'json/' and :62 paginate over that prefix: every key under json/, including json/positioning/positioning_data.json and, once written, json/positioning/opal_aggregate.json, is captured per execution.",
        "infra/aws/lambda/data_refresh/lambda_function.py :1756 POST /data-refresh/time-machine, Dev-gated (:24, :140-192); infra/aws/lambda/data_refresh/portal_time_machine/lambda_function.py :4-8 fans out to yang-time-machine.",
        "infra/aws/lambda/v2_portal/yang_pipeline/scripts/rollback-protocol.sh :24-35 lists json/positioning/ among restored prefixes; :170-176 copy_object from a prior VersionId.",
        "Census: comp-find 'positioning/positioning_data.json' over infra and data, 25 hits across 8,112 files, names only the producer as a writer by literal key; the two restore writers address the key by prefix."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The producer never-widen COO half @ed1db8f1db prints 1 writer for json/positioning/positioning_data.json, and PRD v0.2 FWD-7 with C-OPAL-ONLY-DATA asserts the aggregate's figures reach Opal viewers only once the change lands.",
    "world_is": "Two further writers restore that file by prefix. A Dev-triggered time-machine restore, or an operator rollback, to a date before the change puts current_holdings.AGG and July book aum back into the file every signed-in viewer receives, until the next pipeline run. It is not part of TO-A3-1's act and neither half signs it.",
    "notes": "INERT until TO-A3-1 lands Branch A. Carried for 1.0.0_SA_CTO~Z's round analysis: whether a cell carries it (for example, the restore set skipping json/positioning/opal_aggregate.json and a restore of the shared file dropping AGG, or a named operating rule). The CTO halves @ this commit name it: ledger/NEVER_WIDEN_ROUND1_PRODUCER_CTO_HALF.md."
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T19:42:53Z",
    "one_line": "The served platinum/mdpf/global/aum-metrics.json (VersionId OVcFBOpgjFywfYJGYjowX2VSVwLdiyez, period 2026-09-14) carries total.model_aum 1,800,437,987.06 over by_model rows summing to 1,792,113,521.90; the 8,324,465.16 gap is exactly opal_fixed_income, a cohort 'model' key the global fold counts in model_aua and that dim_mdpf_aum_metrics.py's fixed seven-key MODEL_ORDER never rows. DEFECT against that producer's own stated contract; producer owner 0.4.0_DS_ClientPlatform; POSN_AGGFIX edits nothing there.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a1_gap_explain.py run at ed1db8f1db: 'GAP served 8,324,465.16 vs GAP gold 8,324,465.16 |diff| = 0.00 -> REPRODUCED within 0.01'; 'cohort model keys OUTSIDE MODEL_ORDER: 1 -> opal_fixed_income (Fixed Income) 8,324,465.16'; 'GAP gold - their sum = 0.00'; 'sum of ALL cohort model keys at frontier = 1,800,437,987.06; model_aua - that = 0.00'; control arm moved the gap by exactly 1.00.",
        "gold fold s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json VersionId .UzblTWLJpsPRnUPs067bC5KuoRhP648 (LastModified 2026-09-15T13:31:07Z, as_of_last 2026-09-14): 10 by_model keys; opal_fixed_income cohort_class model, 8,324,465.16 at the frontier row.",
        "data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py @ed1db8f1db :31-32 by_model is cohort_class=='model' ONLY; :27-28 total.model_aum = model_aua frontier; :94-102 MODEL_ORDER lists 7 keys and not opal_fixed_income; :497 the by_model loop walks MODEL_ORDER only; last changed at 4707880967 (2026-08-06).",
        "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py @ed1db8f1db :126-140 GLOBAL_MODEL_KEYS gained opal_fixed_income at 2d5f8a7f74 (2026-08-26) and its same-commit file list does not name dim_mdpf_aum_metrics.py; data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py @ed1db8f1db :130-137 'model_aua already carries these dollars -- by_model was the SHORT side'."
      ]
    },
    "spec_asserts": "TO-A1-1 cell AF1-s-1: reproduce the gap total.model_aum - sum(by_model[].aum) (8,324,465.16 on the 2026-09-14 file) from the file and from the gold fold input, and state whether it is a defect; a defect is a surprise row naming the MDPF producer's owner.",
    "world_is": "The gap is the Fixed Income model to the cent. model_aua is the sum of every cohort 'model' key the fold carries; the served rows come from a fixed tuple that did not grow when the fold's key set grew on 2026-08-26, so the rows fall short of the total by Fixed Income, and any later cohort 'model' key would be left out the same way without a signal. Note: org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/AF1_S1_GAP_EXPLANATION.md.",
    "notes": "Producer owner 0.4.0_DS_ClientPlatform (dim_mdpf_aum_metrics.py:39 Author; gate 1.0.0_SA_CTO). disarm_owner is 2.0.0_SA_COO~Z by the task order's rule for ARMED rows; the disarm is routing this to that owner, since this project edits nothing in MDPF. For C-MEMBERS: Fixed Income is neither a primary model nor a blend of primaries, so its 8,324,465.16 belongs with the assets the aggregate reports as left out; org/standards/POSN_AGGREGATE_MODEL_SET.json measured_against.rows_outside_the_rule 0 counts served rows and cannot see it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T19:42:53Z",
    "one_line": "A1-AC6's invocation cannot print the four result lines its expectation names: simulate-principal-policy given two resource ARNs returns ONE EvaluationResult per action with EvalResourceName templated as arn:aws:s3:::${BucketName}/${KeyName}, and the per-ARN decisions sit in ResourceSpecificResults, which the criterion's --query never selects. The run printed 2 lines, both 'allowed', naming no ARN; A1-AC6 is recorded FAIL by output.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "A1-AC6 invocation verbatim, run 2026-09-15 in /c/tmp/wk-aggfix-1-1 at ed1db8f1db, rc=0, output exactly two lines: 's3:GetObject arn:aws:s3:::${BucketName}/${KeyName} allowed' and 's3:PutObject arn:aws:s3:::${BucketName}/${KeyName} allowed'.",
        "Diagnostic read on the same live evaluator with the same arguments and --output json without --query: each of the 2 EvaluationResults carries 2 ResourceSpecificResults; GetObject platinum/mdpf/global/aum-metrics.json allowed, GetObject json/positioning/opal_aggregate.json allowed, PutObject platinum/mdpf/global/aum-metrics.json allowed, PutObject json/positioning/opal_aggregate.json allowed; every MatchedStatement SourcePolicyId role_yang-pipeline-lambda-role_yang-pipeline-lambda-permissions.",
        "A1-AC7 (one resource ARN) printed the ARN itself: 's3:PutObject arn:aws:s3:::opal-data-bd/posn-aggfix-negative-control.json implicitDeny', so the template appears only when more than one ARN is passed."
      ]
    },
    "spec_asserts": "A1-AC6 expect: 'four result lines; s3:GetObject on the platinum aum-metrics ARN reads allowed and s3:PutObject on the opal_aggregate ARN reads allowed', from --query EvaluationResults[].[EvalActionName,EvalResourceName,EvalDecision] --output text.",
    "world_is": "The query yields one line per action (2 lines) with a templated resource name, so the expectation cannot be met by the criterion's own invocation. The per-ARN decisions the cell needs exist, both needed pairs 'allowed', under EvaluationResults[].ResourceSpecificResults[] (or with one ARN per invocation); by the refusal clause this worker did not substitute either route for the criterion.",
    "notes": "Re-cut shapes available to the issuer: --query 'EvaluationResults[].ResourceSpecificResults[].[EvalResourceName,EvalResourceDecision]' per action, or one invocation per (action, ARN) pair.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S3",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T19:42:53Z",
    "one_line": "yang-pipeline-lambda-role evaluates 'allowed' for s3:PutObject on arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json (the MDPF served file this project only reads) and for s3:GetObject on json/positioning/opal_aggregate.json, from the same policy that grants the two needed actions; A1-AC7's negative control is in another bucket and does not bound the grant inside opal-data-portal-v2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Live iam simulate-principal-policy for arn:aws:iam::313476888478:role/yang-pipeline-lambda-role, actions s3:GetObject s3:PutObject over both ARNs, --output json, 2026-09-15: all 4 ResourceSpecificResults 'allowed', SourcePolicyId role_yang-pipeline-lambda-role_yang-pipeline-lambda-permissions.",
        "A1-AC7 output: 's3:PutObject arn:aws:s3:::opal-data-bd/posn-aggfix-negative-control.json implicitDeny' (bucket opal-data-bd)."
      ]
    },
    "spec_asserts": "TO-A1-1 AF1-s-9 (C-NEVER-WIDEN): the producer role already holds s3:GetObject on platinum/mdpf/global/aum-metrics.json and s3:PutObject on json/positioning/opal_aggregate.json; A1-AC7: an 'allowed' negative control means the role is wider than the PRD read.",
    "world_is": "The role is allowed PutObject on the MDPF served aum-metrics key too, so the Positioning producer can already overwrite the file its new code will read. The negative control's implicitDeny, on opal-data-bd, shows the evaluator can deny but does not bound the grant's width within opal-data-portal-v2. Nothing was changed; this project widens nothing.",
    "notes": "Measured only on the live evaluator; iam.tf was not re-read (outside this cell's instrument).",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S4",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T19:42:53Z",
    "one_line": "The shared key json/positioning/positioning_data.json has TWO write sites in code, both in the producer file: the Lambda handler's put_object (lambda_function.py:2623-2630, Key=OUTPUT_KEY :2529) and main()'s --upload branch (put_object :2501-2508, Key=s3_key_output :2496). The order's L5 read named one writer at :2529/:2627; A1-AC2 prints WRITERS 2 and is recorded FAIL by output.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a1_census.py --writers at ed1db8f1db (34,828 tracked workspace files; 837 portal files under src at edf85ce503): 'WRITER ws:infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:2501 put_object (Key=s3_key_output at :2503, constant at :2496) inside def main()'; 'WRITER ws:infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:2623 put_object (Key=OUTPUT_KEY at :2625, constant at :2529) inside def lambda_handler()'; 'WRITERS 2'; 'AGG WRITERS 1'.",
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @ed1db8f1db :2398-2405 main() parses --upload and --bucket (default opal-data-portal-v2); :2494-2508 'if args.upload:' then s3_client.put_object(Bucket=args.bucket, Key=s3_key_output, ...); :2642-2643 the __main__ guard calls exit(main()).",
        "git diff 605c03f81f HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py is empty (rc 0), so the order's :2627-2634 is not a vintage difference: the handler's put_object call spans :2623-2630 at both commits.",
        "a1_deployed_vs_source.py: the deployed bundle's lambda_function.py sha256 b4114f5c...1bdc18 equals the file at dbe34de7b0 and at HEAD, so the running bundle carries both entry points."
      ]
    },
    "spec_asserts": "TO-A1-1 AF1-s-2 (a) and A1-AC2: 'L5 read: one, the producer :2529/:2627'; expect 'a line WRITERS 1 for the shared key naming the producer's put_object (lambda_function.py:2627-2634, OUTPUT_KEY :2529), which is the positive control'.",
    "world_is": "Two code paths write the key: the deployed handler (the scheduled path) and the file's own __main__ CLI with --upload (a manual path that writes to the same bucket and key by default). A change to what the handler writes leaves the CLI path writing the old shape unless it changes too. The handler's put_object is found (the positive control) at :2623, four lines above the order's citation.",
    "notes": "Whether a manual CLI entry point counts as a writer for C-NEVER-WIDEN is the issuer's to rule; this census counts code that writes the key.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S5",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T19:42:53Z",
    "one_line": "The order says 'The served objects are gzip-encoded: decompress before parsing'; only json/positioning/positioning_data.json is (ContentEncoding gzip). platinum/mdpf/global/aum-metrics.json and json/portfolios/aum-metrics.json carry no ContentEncoding and are plain JSON.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head_object on opal-data-portal-v2, 2026-09-15: json/positioning/positioning_data.json VersionId aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou ContentEncoding gzip; json/portfolios/aum-metrics.json VersionId 2xsIhWJmoBR96Qy5NzsEpT8ZG5daawKe ContentEncoding None; platinum/mdpf/global/aum-metrics.json VersionId OVcFBOpgjFywfYJGYjowX2VSVwLdiyez ContentEncoding None."
      ]
    },
    "spec_asserts": "TO-A1-1 'Measured by the issuer at L5': 'The served objects are gzip-encoded: decompress before parsing.'",
    "world_is": "One of the three named objects is gzip-encoded; the two aum-metrics objects are not, so a reader that always gunzips them fails. This worker's scripts detect the gzip magic bytes instead. Every other L5 figure read back as stated (the five books equal the legacy file's rows 5 of 5 and no platinum row 0 of 5).",
    "notes": "Form only; nothing in this order depends on it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-S3",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-15T20:09:23Z",
    "one_line": "DISARMS POSN_AGGFIX-Z-W1-S1 for this project (owner 2.0.0_SA_COO~Z): the 8,324,465.16 gap is opal_fixed_income, and Andrew-direct ~19:0xZ ruled Opal Fixed Income not needed for POSN_AGGFIX, so the aggregate never counts it and its reconciliation block reports the gap with the explanation ref; the MDPF producer's fixed seven-key MODEL_ORDER defect stays UNDER_INVESTIGATION for its own owner, 0.4.0_DS_ClientPlatform, routed through the round's slug and round analysis.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/AF1_S1_GAP_EXPLANATION.md @11f402ef1e: the gap reproduced to 0.00 from the gold fold and attributed to opal_fixed_income (A1-AC1 PASS).",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_190xZ_POSN_AGGFIX_NO_OPAL_FIXED_INCOME_PRIMARY_MODELS_ONLY.md @fc8cdf1a1e: 'We do not need Opal Fixed Income for any of this, please note that.'",
        "org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md @605c03f81f s.1.1: the payload's reconciliation block carries file_total_model_aum, members_sum, gap and gap_explanation_ref."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "POSN_AGGFIX-Z-W1-S1"
    ],
    "spec_asserts": "W1-S1 as filed: ARMED, disarm owner 2.0.0_SA_COO~Z; C-GAP-EXPLAINED requires the gap explained before the aggregate is read as current.",
    "world_is": "Explained by measurement and outside this project's members by Andrew's word, so no POSN_AGGFIX act can be harmed by it; the defect it names lives in data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py and belongs to that producer's owner, which this project does not edit.",
    "notes": "Investigation-plane disarm by the named owner. Routing of the MDPF defect to 0.4.0_DS_ClientPlatform rides the round's slug (3.0.0_SA_CVO~Z) and round analysis (1.0.0_SA_CTO~Z); no remediation is this project's."
  }
]
```
