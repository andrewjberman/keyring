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
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T19:57:36Z",
    "one_line": "TO-B1-1 cell AF1-s-13 hands `internal` to the HoldingsTab mount and merges the aggregate 'into the Positioning data object the tab reads', but at portal edf85ce503 HoldingsTab declares no `internal` prop (passing it fails the portal typecheck, TS2322, measured) and in Models mode the tab renders its OWN getPositioningData fetch, not the page's object; both limbs need HoldingsTab.tsx, which TO-B1-1's <paths> do not hold, while TO-B2-1's <paths> hold HoldingsTab.tsx and not Positioning.tsx.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/Positioning/tabs/HoldingsTab.tsx @edf85ce503 :599-626: the HoldingsTab props are customBlend, mode, etfData, satelliteData, bookStatus -- no internal prop and no models-data prop.",
        "same file @edf85ce503 :637 `const [modelsData, setModelsData] = useState<PositioningDataResponse | null>(null)`, :648-653 `dataByMode = { models: modelsData, etfs: etfData, satellites: satelliteData }`, :727-737 the tab's own `getPositioningData()` inside a useEffect: in Models mode the tab reads its own fetch and never the page's positioningData.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b1_mount_internal_prop_typecheck_measure.txt (committed with this row): with `internal={internal}` on the mount, `tsc -b --noEmit` EXIT=2, `src/pages/Positioning/Positioning.tsx(670,11): error TS2322 ... Property 'internal' does not exist on type 'IntrinsicAttributes & { customBlend: CustomBlendState; mode?: ...; bookStatus?: ... }'`.",
        "org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-B1-1.portal-fetch-viewer-gate-and-remembered-choice.md @ed1db8f1db <paths>: portal-proxy.ts, Positioning.tsx, bookSet.ts, README.md, and the act says 'HoldingsTab.tsx is NOT yours in this order'; POSN_AGGFIX.TO-B2-1.holdings-tab-restores-the-aggregate-book.md @ed1db8f1db <paths>: HoldingsTab.tsx and no Positioning.tsx, while its 'Your inputs from TO-B1-1' lists '`internal` handed to the `HoldingsTab` mount'.",
        "portal 63edeeeb51 on wk-aggfix-1-3-portal (LOCAL): landed the fetch, the internal-and-Models query, mergeOpalAggregate feeding the page's dataByMode.models (Positioning.tsx :369-384, :471 at that commit), and the book-set helpers; the HoldingsTab mount carries no internal prop."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AF1-s-13 (decomposition @605c03f81f, TO-B1-1 verbatim): `internal` (:267) is passed to the `HoldingsTab` mount (:642); on status OK with holdings its current_holdings.AGG is merged into the Positioning data object the tab reads. TO-B2-1 lists the mount hand-over among its inputs from TO-B1-1.",
    "world_is": "Neither limb can land inside TO-B1-1's grant with B1-AC7 at exit 0. The tab's prop type rejects `internal`, and the tab's Models data is its own fetch, so a page-side merge reaches PositioningSummary (which reads current_holdings only where SUBCATEGORY_SOURCE is current_holdings: etfs and satellites) and not the Holdings tab. TO-B1-1 landed the page-side fetch, gate and merge and the pure helpers, and did NOT pass internal to the mount. The hand-over -- an `internal` prop plus either a models-data prop or the tab applying mergeOpalAggregate to its own fetch -- needs a HoldingsTab.tsx edit and a Positioning.tsx edit in one typechecking commit, and no single order's <paths> holds both files.",
    "notes": "Form only; significance not judged. No B1 criterion grades the mount, so B1-AC1..AC8 are recorded as run. For 2.0.0_SA_COO~Z: TO-B2-1's grant or a re-cut."
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T19:57:36Z",
    "one_line": "TO-B1-1 has the render harness read AuthContext.tsx 'for the claim shape of an advisor and a client', but AuthContext has NO client class: Claims carries only firmId, userType, advisorId, firmRole, advisorRole, and the one non-Opal shape it mints is devBypass's partner advisor; the client claim set was therefore CONSTRUCTED (a partner firmId with every other claim at its parseClaims deny-floor) and recorded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/contexts/AuthContext.context.ts @edf85ce503 :31-43: interface Claims { firmId, userType: 'Dev' | null, advisorId, firmRole: 'admin' | 'user' | null, advisorRole } -- no client member.",
        "portal src/contexts/AuthContext.tsx @edf85ce503 :110-142 parseClaims (userType kept only when exactly 'Dev'; firmRole only admin|user; advisorRole only the four RCU roles, else null); :686-697 devBypass(advisorRole) mints the partner advisor (firmId VITE_DEV_FIRM_ID, userType null, advisorId 'dev-advisor-id', firmRole 'user'); a case-insensitive read of 'client' over the same file: 10 hits, every one queryClient / QueryClient / api-client, 0 naming a user class.",
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs @ed1db8f1db :159-169: the tier notion (x-user-tier, x-user-type request headers) lives at the edge, not in the portal's claims.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b_five_books_dom.mjs VIEWERS (committed with this row): advisor {firmId 49financial, userType null, advisorId b-harness-advisor, firmRole user, advisorRole architect}; client {firmId 49financial, userType null, advisorId null, firmRole null, advisorRole null}; both printed on every run's CLAIMS lines."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-B1-1 fixtures paragraph: 'vary the SESSION's user claims per viewer class, reading AuthContext.tsx for the claim shape of an advisor and a client'; decomposition @605c03f81f :311-312: the portal worker builds the advisor and client claim sets from AuthContext.tsx and records them.",
    "world_is": "The portal claims cannot tell a client from any other non-Opal, non-advisor partner user; the page predicate (firmId opal-capital OR userType Dev) treats both as non-internal, so for this page the two classes render identically. Whether a real client session carries a claim the portal does not model (an edge-derived tier) is not readable from the portal."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:44:00Z",
    "one_line": "TO-C1-1 drives a 'client' viewer class in its unit and live arms, but the live signer never mints one: generateAccessToken sets tier 'internal' for firmId opal-capital and 'advisor' for every other firm, and no other claim marks a client. The worker constructed the class (tier 'client', firmId 49financial, no advisor identity) and signed it with the live key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts @240fe36222 :168 (generateAccessToken, :162): const tier = user.firmId === 'opal-capital' ? 'internal' : 'advisor' -- the payload's only tier source.",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/types.ts @240fe36222 :63: the access payload's tier is commented 'Vestigial -- kept for portal-authorizer compat'.",
        "portal src/contexts/AuthContext.tsx @edf85ce503 :122-140 parseClaims: firmId, userType, advisorId, firmRole, advisorRole; advisorRole levels architect/consultant/local_ops/implementor; no client class.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~2/c1_classes.mjs: the client claim set used; printed with the token redacted in C1-AC3's output."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 AF1-s-4 and AF1-s-11: exercise /api/general/positioning/model.json live with a client token, and drive four viewer classes (Opal staff, Dev, advisor, client).",
    "world_is": "The signer's tier space is {internal, advisor}; no real login produces a client-class token. The worker's client class carries tier 'client' (the value the proxy docstring names), firmId 49financial and no advisor identity. The gate's predicate reads only firmId and userType, so the class's tier value cannot move a gate row.",
    "notes": "Form only. Not read: portal-authorizer, or any other identity source that might carry a client notion."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:44:00Z",
    "one_line": "The portal proxy docstring for getModelData says the Lambda 'Checks X-User-Tier header (blocks client tier)' on /api/general/positioning/model.json. Exercised live, a client-tier token is NOT refused there: the request reaches S3, which answers 403 AccessDenied because the key is absent, byte-identical to Opal staff's answer. MODEL-ROUTE CLIENT REFUSAL: FALSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/portal-proxy.ts @edf85ce503 :1419-1426 (getModelData docstring): 'Lambda: Checks X-User-Tier header (blocks client tier)'; 'Access: Internal + Advisor tiers only'.",
        "C1-AC3 live run 2026-09-15T19:41:33Z, node .../deliverables/0.9.0_WK_POSN_AGGFIX~2/c1_live_tier_arms.mjs --phase pre: unauthenticated 401 {error: Missing or invalid Authorization header}; client token 403 len=263 S3 XML <Error><Code>AccessDenied</Code> sha256 b3c16307d6e569c8...; Opal-staff token 403 with the same sha256.",
        "Same run: s3api head-object opal-data-portal-v2 json/positioning/model.json -> 404 Not Found.",
        "C1-AC2 (c1_edge_tier_read.py) at git objects @b29fe4bf48: public-data-router 0 tier/role/firm/userType branches; auth-validator-edge's branches scoped to /api/scoped/advisor-intelligence/ and the advisor/account/relationship scoping regexes; shared-advisor-router not associated with /api/general/*."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 AF1-s-4 / C1-AC3: record whether the proxy docstring's 'blocks client tier' for /api/general/positioning/model.json is true by exercising that URL live with a client token; FALSE is recorded and filed as an OBSERVATION row.",
    "world_is": "No function on the /api/general/* path reads the tier: any verified token is forwarded to S3. The URL serves nothing today only because json/positioning/model.json does not exist; were that key written, every signed-in viewer could read it.",
    "notes": "INERT while the key is absent (404 at the run). Not measured: whether anything writes json/positioning/model.json. The docstring describes a check that is not on the path."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S3",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:55:00Z",
    "one_line": "C1-AC8 asks for infra/aws/lambda/ci/lambda-source-map.json 'restored to PURE ASCII with only the changed values', but the map at HEAD is not pure ASCII: it carries 23 non-ASCII characters (detector 28) on 8 lines, several of them mojibake, so a pure-ASCII restore also rewrites those 8 unrelated lines as backslash-u escapes. The JSON values are identical; the one semantic change the build made is auth-validator-edge artifact_sha256.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @9633bb9e7e (last commit touching it; unchanged at b29fe4bf48): 197884 bytes, detector len(b)-len(b.decode('utf-8')) = 28; 23 non-ASCII characters U+009D U+00A2 U+00A7 U+00AC U+00C3 U+00E2 U+2014 U+201A U+20AC; json.dumps(indent=2, ensure_ascii=False) reproduces it byte-for-byte.",
        "A pure-ASCII write (ensure_ascii=True) of the UNCHANGED base differs from it on lines 175, 223, 238, 253, 268, 287, 419, 549 of 3281.",
        "After build-nodejs-lambda.sh portal-auth auth-validator-edge (2026-09-15T19:50Z): 1 semantic leaf change, /functions/auth-validator-edge/artifact_sha256 wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic= -> fekWqHP2cWuewpfFOnlxa2S5jBhxmKKs8eB4/QccRxs=; the pure-ASCII restore was 197971 bytes, detector 0, differing from the base on 9 lines (the 8 above plus 1503)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC8: lambda-source-map.json restored to PURE ASCII with only the changed values (detector 0 printed).",
    "world_is": "The base already carries non-ASCII bytes, so PURE ASCII and 'only the changed values' cannot both hold byte-wise: a pure-ASCII write leaves exactly one semantic change and eight escape-only line changes on other functions' entries.",
    "notes": "Form only. The worker's pure-ASCII restore was then returned to the base bytes, because the artifact it described was rolled back under Branch B (row POSN_AGGFIX-Z-W2-S4); the map at the worker's HEAD equals the base. Not measured: which commit introduced the non-ASCII characters, or whether any consumer reads the map in a non-UTF-8 text mode."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S4",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T20:00:00Z",
    "one_line": "C1-AC9's targeted plan cannot come out as the order expects: -target=aws_cloudfront_distribution.portal pulls in the distribution's dependency aws_wafv2_web_acl.opal_cloudfront_protection (its web_acl_id), so the plan reads 'Plan: 0 to add, 3 to change, 0 to destroy' with the pre-existing WAF drift inside it. Branch B: the worker stopped before C1-AC17 and C1-AC10, applied nothing, and restored the artifact's prior bytes as the latest object version.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/portal-auth/cloudfront-distribution.tf @638492cd7e :117: web_acl_id = aws_wafv2_web_acl.opal_cloudfront_protection.arn inside resource aws_cloudfront_distribution.portal -- Terraform's -target includes a targeted resource's dependencies.",
        "C1-AC9, 2026-09-15T19:52:43Z, the order's invocation verbatim: init succeeded; 'Plan: 0 to add, 3 to change, 0 to destroy.'; terraform show -json of .scratch/c1.tfplan: 14 resource_changes, 3 with an action -- aws_cloudfront_distribution.portal update (25 lambda_arn paths, every before-value auth-validator-edge:19, 0 non-association leaf changes), aws_lambda_function.auth_validator_edge[0] update (s3_object_version GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> zNqzzAOFvq1LnTji4BV2_OymHRfr.bXI), aws_wafv2_web_acl.opal_cloudfront_protection update (rule[3], rule[4], rule[5] managed_rule_group_statement version '' -> null).",
        "Rollback per the COO half's artifact row, 2026-09-15T19:58Z: s3api copy-object CopySourceVersionId GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> latest VersionId 7AkZ0zQ1ETC.wcttDTxnk3t2s5QT9rh2, metadata content-sha256 wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic=; get-object of the latest re-hashed to that value (21096 bytes) and its bundle carries aggregate_denied 0 times.",
        "Live re-read 2026-09-15T19:58:26Z (c1_live_association_read.py --before-apply): AUTH-VALIDATOR ASSOCIATIONS 25 -- AT VERSION 19 25 of 25, config ETag E1XYSDYC8UB18L, the same ETag C1-AC1 read at 19:33Z.",
        "Targeted re-plan after the rollback, 2026-09-15T19:59:38Z: still 'Plan: 0 to add, 3 to change, 0 to destroy'; the function now plans s3_object_version GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> 7AkZ0zQ1ETC.wcttDTxnk3t2s5QT9rh2 (identical bytes)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC9 and decomposition s.1.2: the plan -target'ed to the function and the distribution reads 'Plan: 0 to add, 2 to change, 0 to destroy' with aws_wafv2_web_acl absent (the whole-root WAF drift 'kept out of your targeted plan'); anything else is Branch B -- STOP, BLOCKING row, the COO half's rollback.",
    "world_is": "While the WAF drift stands, no plan targeted to the distribution can exclude it, so C1-AC9 as written cannot pass. Not run: C1-AC17, C1-AC10, C1-AC11, C1-AC12, C1-AC13, C1-AC14, C1-AC15. The live function and all 25 associations are at version 19; ledger entry posn-aggfix-r1-edge-gate stays OPEN with L1 and L2 closed.",
    "notes": "INERT: left alone, nothing serves differently. Residual of rolling back by copy: the latest artifact VersionId (7AkZ0z...) differs from the one in state (GUSk3...), so the NEXT portal-auth apply by any seat publishes a new version carrying the OLD code, re-points all 25 associations to it, and applies the WAF drift with it. Restoring the exact prior latest version would need a delete of object versions zNqzz... and 7AkZ0z..., an S3 delete this worker does not make without human confirmation. How the plan is re-cut is the issuer's."
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S6",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T21:10:10Z",
    "one_line": "A2-AC13 cannot hold as written. main() --upload now writes both keys with the put shape, but its payloads cannot equal the handler's in every field except generated_at: main() passes generate_positioning_data no ETF returns and a YYYY-MM-DD data_date, while the handler passes etf_returns_df/etf_returns_lookup and a YYYYMMDD data_date. The same differences exist at 605c03f81f.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @166ca71b85 :2603 (main): generate_positioning_data(model_data, date_formatted, data_pkl_data); :2761 (lambda_handler): generate_positioning_data(model_data, data_date, None, data_as_of, etf_returns_df, etf_returns_lookup). The same two calls @605c03f81f at :2461 and :2615.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a2_ac13.out.txt @166ca71b85 (a2_producer_harness.py --cli-upload, 2026-09-15T21:05Z, event execution 20260914_v1-9dbd2129; the model PKL benchmarks/model_20260914_v1.pkl at VersionId V7LdxQzGOdxGv6KulE48xjPDATbu0A4T for both runs; main() return 0): EXACTLY TWO PUTS True, both with ContentType application/json, ContentEncoding gzip, CacheControl no-cache. positioning_data.json DIFFERS on 161 leaf paths in 11 shapes: 160 holdings[*].returns present only in the handler's capture (portfolios and the five books), plus $.data_date. opal_aggregate.json DIFFERS on 30 paths, all $.current_holdings.AGG.holdings[*].returns.",
        "Same output, CONTROL at 605c03f81f: the CLI shared file against the handler shared file DIFFERS on 191 paths in 12 shapes, the same classes plus the AGG holdings returns the base still carried in the shared file (30).",
        "Captured data_date values, read from the .scratch captures: handler runs '20260914' (BEFORE and AFTER); CLI runs '2026-09-14' (BEFORE and AFTER). data_as_of is '2026-09-14' in all four."
      ]
    },
    "spec_asserts": "TO-A2-1 A2-AC13: main() run with --upload under the capturing wrapper on the same model PKL: exactly two puts captured, each with ContentType application/json, ContentEncoding gzip and CacheControl no-cache, and each decompressed payload equal to the handler AFTER run's capture of the same key in every field except generated_at.",
    "world_is": "The two write sites built different payloads before this order touched them. The CLI path carries no per-holding returns (in portfolios, in the five books, and now in the aggregate's holdings), and its data_date is YYYY-MM-DD. Making the payloads equal means changing how main() calls generate_positioning_data (load etf_returns from the model PKL and pass the YYYYMMDD date), which the order does not name. Refused under the refusal clause, not repaired.",
    "notes": "A2-AC13 is recorded FAIL. Its other limbs hold: two puts, the put shape, the same model PKL, main() return 0. The harness sets AWS_LAMBDA_FUNCTION_NAME for the CLI run as for the handler runs; without it, main() takes load_aum_data's local branch and writes no current_holdings. Whether A2-AC13 is re-cut to exclude returns and data_date, or main() is widened, is the issuer's call.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S7",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T21:10:10Z",
    "one_line": "The shared file is not byte-stable across processes for the same source and the same inputs. The key order of portfolios.<code>.benchmark.spread.segment.{sector,geography,maturity} follows set iteration, which Python's per-process hash randomization reorders. To make A2-AC3's byte comparison meaningful, the harness pins PYTHONHASHSEED=0 for every run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @605c03f81f :1265, :1272, :1279 (calculate_benchmark_comparison): all_sectors, all_geographies and all_maturities = set(...) | set(...), iterated to fill spread['segment'][...]; the same lines @166ca71b85.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a2_ac3.unpinned_hash_seed.out.txt @166ca71b85 (seed unpinned, 2026-09-15T20:58Z): BOOKS NON-AUM IDENTICAL 5 of 5; 'TOP-LEVEL DIFFERS on: portfolios' with 0 differing leaf paths. A diagnostic read of those captures found 14 dicts whose key order differs, all under benchmark.spread.segment, with json.dumps(sort_keys=True) EQUAL.",
        "Discriminating read in the same session: two runs of the BEFORE source at 605c03f81f with the seed unpinned (.scratch/a2/diag_runs/before-rep1 and before-rep2): portfolios bytes DIFFER and sorted-keys EQUAL; data_as_of, note, benchmarks, current_holdings and data_date bytes EQUAL.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a2_ac3.out.txt @166ca71b85 (PYTHONHASHSEED=0 for both arms): TOP-LEVEL IDENTICAL, BOOKS NON-AUM IDENTICAL 5 of 5, CONTROL FIRED."
      ]
    },
    "spec_asserts": "TO-A2-1 AF1-s-8 and A2-AC3: the handler run at the base commit and at the branch HEAD against the SAME inputs, with every top-level key other than generated_at and current_holdings byte-identical.",
    "world_is": "portfolios is byte-identical only while the hash seed is held equal. The deployed Lambda runs with a random seed, so the served shared file's segment key order can change from run to run with no data change. Consumers that read by key are unaffected; any byte or hash comparison of two served files would see a change that is not one.",
    "notes": "Form only. The producer's key order is outside this order's cells and is untouched. The harness's first comparator was also blind to key order (it printed 0 differing leaf paths for a real byte difference); it now reports key-order differences.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S8",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T21:10:10Z",
    "one_line": "A2-AC6 asks the hand re-derivation to match the producer to 6 decimals, but the producer serves each aggregate weight rounded to 4 decimals (round(total_weight, 4)). The 6-decimal MATCH is therefore of the hand value rounded to 4 places the producer's way; the unrounded hand values differ from the served weights in the 5th decimal.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @166ca71b85 :1675 (calculate_aggregated_holdings): 'weight': round(data['total_weight'], 4); @605c03f81f :1607. The books' weights that feed the sum are rounded to 4 at :1894 @166ca71b85.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a2_ac6.out.txt @166ca71b85, unrounded hand value / hand rounded to 4 / producer weight: IEFA 0.1351988140 / 0.135200 / 0.135200; DIVZ 0.1262441538 / 0.126200 / 0.126200; IDVZ 0.1042665386 / 0.104300 / 0.104300. HAND RE-DERIVATION MATCH 3 of 3."
      ]
    },
    "spec_asserts": "AF1-s-7 and A2-AC6: the exercise re-derives the aggregate weight of three named holdings by hand from the model books and the member AUM, and matches the producer's output to 6 decimals.",
    "world_is": "The served weight has 4 decimals, so an unrounded re-derivation cannot agree with it at 6. The harness prints the unrounded value, the value rounded to 4, and the producer's weight, and grades MATCH on the rounded value.",
    "notes": "Form only. The rounding is unchanged by this order.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S9",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T21:10:10Z",
    "one_line": "A2-AC11 cannot print one file. git diff --stat 605c03f81f HEAD -- infra/ lists 8 files at HEAD 166ca71b85, because the SITEZ fast-forward the order's first act requires brought in 7 infra files that other orders changed after the anchor (POSN_AGGFIX TO-C1-1's edge gate, AMGT_RESAPP rj-10's harvest files). This order's own commit changes exactly one infra file.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a2_ac11.out.txt, the invocation verbatim at HEAD 166ca71b85: 8 files changed -- infra/aws/lambda-edge/auth-validator-edge/aggregate_gate.mjs, infra/aws/lambda-edge/auth-validator-edge/index.mjs, the producer lambda_function.py, and infra/aws/terraform/harvest/{build-and-upload-scoped-amgt.sh, chatter-axis-schedule.tf, lambda_src/build_zip.py, lambda_src/lambda_function.py, scoped-amgt-api.tf}; rc=0.",
        "Same file, labeled SUPPLEMENTARY: git diff --stat 0c4650dc1c HEAD -- infra/ (0c4650dc1c = the SITEZ tip fast-forwarded to before any edit) lists 1 file, the producer, 197 insertions and 47 deletions.",
        "Same file: git log 605c03f81f..HEAD -- infra/ names 240fe36222 (0.9.0_WK_POSN_AGGFIX~2), a30a75d74a and d3e9dc909b (0.9.0_WK_AMGT_RESAPP~19), drains 5445eee97e and 0c4650dc1c, and this order's 166ca71b85."
      ]
    },
    "spec_asserts": "TO-A2-1 A2-AC11: timeout 60 git diff --stat 605c03f81f HEAD -- infra/ shows exactly one file under infra/: infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py. The first act brings SITEZ into the branch.",
    "world_is": "The anchor is fixed, and HEAD includes every SITEZ commit up to 0c4650dc1c, so the diff counts other orders' files. The one-file result holds only against the base this order's work started from.",
    "notes": "Recorded FAIL by output; the supplementary read is not substituted for the criterion. The fixed anchor is right for the before-arm read, but as the base of this diff it picks up every drain merged in after it. How the criterion is re-cut is the issuer's call.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S10",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T21:19:52Z",
    "one_line": "The proof schema defines acceptance[].expect as the Python regex the evidence must match, 'Carried from the task order's <expect>'. TO-A2-1's <expect> clauses are prose, so carrying them verbatim makes proof-of-spec-check refuse every PASS row: 10 violations, 9 no-match and 1 uncompilable pattern. The instance omits expect, so it is graded as self-report (the pre-v3 state).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/PROOF_OF_SPEC.schema.json @49607de3fb, acceptance.items.properties.expect.description: 'spine v3.0 L6/L7 (one clause per criterion): the PATTERN (Python regex, searched with DOTALL) the deciding output must match; the checker grades a mechanical criterion by this match, not by the worker. Carried from the task order's <expect>. OPTIONAL'.",
        ".tools/proof-of-spec-check.py @49607de3fb conditional_checks: re.search(exp, output_evidence, re.S | re.M); a PASS row that does not match is a violation, and a pattern that does not compile is a violation.",
        "org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-A2-1.producer-reads-current-weights-and-writes-the-opal-only-key.md @49607de3fb, A2-AC1: <expect>legacy 0; platinum 1 or more; opal_aggregate 1 or more.</expect>; every <expect> in the order is an English clause.",
        "proof-of-spec-check run in worktree wk-posn_aggfix-1-1 at HEAD 49607de3fb, with each order <expect> carried verbatim into the instance: 'violations=10', 'INVALID (rc=1)'; e.g. \"acceptance[A2-AC1]: status=PASS but output_evidence does NOT match expect 'legacy 0; platinum 1 or more; opal_aggregate 1 or more.'\" and 'acceptance[A2-AC7]: expect is not a valid pattern (unterminated character set at position 263)'."
      ]
    },
    "spec_asserts": "org/standards/PROOF_OF_SPEC.schema.json acceptance[].expect: the regex the deciding output must match, carried from the task order's <expect>, so that the checker, not the worker, grades a mechanical criterion.",
    "world_is": "The order's <expect> clauses are sentences (backticks, semicolons, parentheses, square brackets), not patterns. Verbatim they match no evidence, and A2-AC7's does not even compile. For this order, carrying cannot engage the checker's grading of PASS rows; only a worker writing its own patterns could, and the schema does not describe that.",
    "notes": "Form only. The instance's criterion_verbatim carries each prose expectation, and PASS rests on verbatim output against it. TO-A1-1's instance carries no expect either.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S3",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T20:57:22Z",
    "one_line": "TO-B2-1 grounds the re-authoring on 'the canvas is light; ink on white panels; the removed orange-on-dark classes render near-invisible today', but both Holdings tab panels are Panel variant=\"chart\", which renders the dark BAND with the .dark-band ink context, where the neighbouring columns' light idioms are legal and legible; the restored group was authored in the band's own ink token with the four named classes kept out, and its legibility is left to B2-AC6's measurement rather than to the premise.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/pages/Positioning/tabs/HoldingsTab.tsx @edf85ce503 (unchanged at 63edeeeb51) :1103 and :1195 -- Portfolio Composition and Holdings Breakdown are each `<Panel variant=\"chart\">`.",
        "portal src/ui/components/panels/Panel.tsx @63edeeeb51 (not touched since edf85ce503) :63 `chart: 'bg-[hsl(var(--bg-band))]', // inverted band -- white-text idiom legal inside` and :90 `(variant === 'chart' || variant === 'mixed') && 'dark-band'`.",
        "portal src/index.css @63edeeeb51 :363-379 body sets --layer-body 221 45% 18% and --semantic-background-contentPanel: var(--layer-body); :406-413 `.dark-band { color: hsl(var(--palette-white)) }` (mode-stable band ink).",
        "portal CLAUDE.md @63edeeeb51 :44 (the 'Known divergence' paragraph): Panel variant chart/mixed resolve to the band and stay dark because 4,887 light-on-dark idioms in src/pages/ depend on a dark container; portal DESIGN.md C3 names the band ink palette.white #E8ECF5.",
        "HoldingsTab.tsx @edf85ce503 :1303-1374 -- the columns beside the restored group render text-green-300 and text-white on that band today."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-B2-1 cell AF1-s-14 and 'The canvas law': the Model Breakdown group is 're-authored in today's light-canvas tokens (no text-white, text-orange-300, bg-white/10, bg-orange-500/5)'; 'the canvas is light; ink on white panels; the removed orange-on-dark classes render near-invisible today'.",
    "world_is": "The page canvas is light, but the Holdings tab's two panels are band-valued containers (the portal's own recorded divergence from DESIGN.md C3), so the group sits on the band's panel body, not on a white panel. The worker kept the four named classes out (counted by B2-AC1), set the group's ink to the band's ink token hsl(var(--palette-white)) as a value, laid the orange tint over the opaque panel base the way the neighbouring headers are, and measured contrast on the rendered ground (B2-AC6). A navy-on-white re-authoring, which the premise implies, would have measured illegible on this ground.",
    "notes": "Form only; significance not judged. Whether the Holdings panels should move to a white panel is DSGN_REBRND's (rows DSGN_REBRND-W1-S9 / W2-S5 named in portal CLAUDE.md), not this order's."
  },
  {
    "id": "POSN_AGGFIX-Z-W3-S4",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~3",
    "surfaced_at": "2026-09-15T21:23:05Z",
    "one_line": "proof-of-spec-check's count-bar limb refused TO-B2-1's B2-AC8 row because the shared typecheck runner printed an exit code directly before the noun ('RUN 1: EXIT=0  error TS lines=0' in the bar; 'EXIT=2  error' and 'exit=2 errors=1' in the control arm's lines), which the limb reads as a zero count beside a nonzero count of errors; TO-B1-1's committed B1-AC7 bar matched the same wording written as `EXIT=0[ ]{2}error` and was never recognized as a bar, so the same evidence shape passed one instance and failed the next on the regex spelling alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/proof-of-spec-check.py @f247f24c13 :1384 `_BAR_ZERO_RE` accepts `0` followed by [ \t]+, a literal backslash-s or backslash-t, or `[ \t]` before a noun, so `0[ ]{2}error` is not read as a zero-count bar while `0  error` is; :1405 `_nonzero_counts` reads any `<digits><space>noun`, so an exit code printed before the noun counts; :1380-1382 NON-APPLICATION names key=value bars (`rc=0`) as outside the rule.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b2_proof_check.txt (this order, first check): 'VIOLATION: count-bar[B2-AC8] ... asserts ZERO of 'error' ... NONZERO count for that noun: '2  error'; '2 errors'' -> INVALID (rc=1); every other row's bar read clean.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/POSN_AGGFIX.TO-B1-1.portal-fetch-viewer-gate-and-remembered-choice.proof_of_spec.json @0741530d35, row B1-AC7 expect `RUN 1: EXIT=0[ ]{2}error TS lines=0\b` over evidence carrying 'RUN 2: EXIT=2  error TS lines=1'; b1_proof_check.txt @0741530d35: 'count-bar-frame: 0 PASS row(s) carry a zero-count bar' and VALID (rc=0).",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~3/b2_ac8_typecheck.attempt1.txt (the refused record, kept) and b_typecheck_run.sh (committed with this row): the runner now prints `exit_code=N; error_TS_line_count=M`; the computed values are unchanged."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The agent definition: 'Validate: python .tools/proof-of-spec-check.py <instance> <ids> -- ONLY the exit code is the verdict', and RULING M(ii) as quoted by the limb: a PASS whose zero-count bar matches evidence that also carries a nonzero count of the same noun is refused, key=value bars being out of scope.",
    "world_is": "The B2-AC8 evidence is a key=value record (an exit code and an error-line count per run, with a deliberate-error control arm whose count is 1 by design); the limb classifies it by adjacency, so whether it refuses depends on how the bar's whitespace is spelled and on whether the instrument prints a number before the noun. The worker did not respell the bar to pass the detector; it changed the runner's wording to key=value fields, re-ran the same invocation once, kept the refused record as attempt1, and rebuilt.",
    "notes": "Form only; significance not judged. Whether the limb should also recognize `[ ]{n}` / `\\s{n}` spellings, or skip exit-code adjacency, is the checker owner's."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S5",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T21:14:00Z",
    "one_line": "The order's serial-file line writes org/mcp/sessions/<session>.serial in the MAIN workspace, but safe-apply run from the linked worktree roots the halt gate at the worktree (.tools/..), which has no org/mcp/: C1-AC10 refused rc=3 IDENTITY UNRESOLVED. The same root sets the inbox the gate scans, and an absent inbox reads as no messages. The worker set HALT_GATE_REPO_ROOT to the main workspace; the gate then admitted the worker, scanned issuer 2.0.0_SA_COO~Z, refused rc=1 on 182 routine messages, and passed with HALT_ACK=1 after the worker reviewed all 182.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh @31995abe76 :38 HALT_GATE_REPO_ROOT defaults to the directory above .tools/ (the worktree); :39 HALT_GATE_INBOX_ROOT = <root>/org/mcp/inbox; :57 the serial file is <root>/org/mcp/sessions/<session>.serial; :248-250 halt_gate_unread_for returns no files when the inbox directory is absent; :400 an empty scan passes silently; :439 HALT_ACK set -- messages acknowledged.",
        "C1-AC10 run 1, 2026-09-15T20:43:18Z (serial written to the main workspace path, as the order says): 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)', safe-apply rc=3; list-versions after: 19 versions, nothing applied.",
        "C1-AC10 run 2, 2026-09-15T20:46:35Z, HALT_GATE_REPO_ROOT=/c/Users/Opal Bloomberg/Desktop/ajb_workspace (main HEAD 0c4650dc1c, order <status>staged</status> there): 'worker 0.9.0_WK_POSN_AGGFIX~2 has no inbox; scanning its issuer 2.0.0_SA_COO~Z', 'HALT-GATE: 182 pending message(s)', 'blocked ... re-run with HALT_ACK=1', rc=1 at 20:50:57Z; nothing applied.",
        "Review of the 182 (parsed from the gate's own listing, cross-checked by a direct subject count over org/mcp/inbox/2.0.0_SA_COO/*.md: 182 unread, 0 subjects starting [STOP] or [HALT]): 171 from deploy_ledger.py (automated RED/WARN/HELD-STALE ledger scans, 16 to 39 days old, 12 distinct ledger slugs, none naming posn, aggfix, portal, auth, edge, waf or cloudfront); 11 from 4.0.0_SA_CRO~W (Andrew-direct harvest items); 0 word-bounded subject hits for POSN, AGGFIX, portal-auth, auth-validator, edge, WAF, cloudfront, STOP, HALT or freeze.",
        "C1-AC10 run 3, 2026-09-15T20:55:12Z, HALT_ACK=1 with the same root: 'HALT-GATE: HALT_ACK set -- messages acknowledged. Proceeding.', comp-tagauthz gate PASSED, tombstone gate CLEAN, 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.' rc=0 at 21:05:00Z.",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/rj10.apply.txt @0c4650dc1c :1 then :30: the issuer-scan line for 2.0.0_SA_COO~W, then 'Apply complete!' with no pending-message block, although that issuer's base inbox is the same 2.0.0_SA_COO."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 IDENTITY AND THE FIRST ACT: immediately before the first safe-apply, printf the serial to /c/Users/Opal Bloomberg/Desktop/ajb_workspace/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial; C1-AC10 runs .tools/safe-apply.sh from the worktree with the halt-gate checkpoint output pasted above the apply summary.",
    "world_is": "From a linked worktree the gate reads its serial, its worker-admission tree and its inbox under the worktree unless HALT_GATE_REPO_ROOT is set. With the serial in the main workspace it refuses; a serial copied into the worktree would give the gate an identity and an absent inbox, so it would pass without reading any STOP. The worker's runs 2 and 3 set the root to the main workspace; run 3 also set HALT_ACK=1 after the review above. The invocation and the plan file were unchanged.",
    "notes": "Form only. Not measured: which root the AMGT_RESAPP~19 gate used, or whether any other worker's safe-apply from a worktree passed on an absent inbox. HALT_ACK moves no inbox file; the 182 messages remain unread in the issuer's inbox."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S6",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T21:14:00Z",
    "one_line": "C1-AC11 cannot read 'No changes': after the apply, the targeted re-plan still reads 'Plan: 0 to add, 1 to change, 0 to destroy', the one change being the same three WAF managed_rule_group_statement version '' -> null leaves the apply carried. The live WebACL did not move (same LockToken, every rule field equal), so the provider re-plans this normalization on every plan of the portal-auth root.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C1-AC11, 2026-09-15T21:05:42Z, the order's invocation verbatim, rc=0: '# aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place', 'Plan: 0 to add, 1 to change, 0 to destroy.'; the text diff removes and re-adds the rules common-rule-set, ip-reputation and known-bad-inputs with '(1 unchanged attribute hidden)' in managed_rule_group_statement.",
        "Supplementary saved re-plan, same targets, 2026-09-15T21:10:12Z, terraform show -json .scratch/c1_replan_after.tfplan: 14 resource_changes, 1 with an action (aws_wafv2_web_acl.opal_cloudfront_protection update); exactly 3 changed leaves /rule/3|4|5/statement/0/managed_rule_group_statement/0/version from \"\" to null; each of the three rules equal before and after once version is masked; aws_lambda_function.auth_validator_edge[0] and aws_cloudfront_distribution.portal no-op.",
        "C1-AC10 apply 2026-09-15T20:55Z..21:05Z: 'aws_wafv2_web_acl.opal_cloudfront_protection: Modifications complete after 22s' inside 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.'",
        "C1-AC19 (20:42:21Z) and C1-AC20 (21:06:16Z), wafv2 get-web-acl: LockToken 848a6d0b-d69f-40e0-876a-cfc0ce40b6b2 on both reads; 'WAF RULES UNCHANGED 6 of 6'; the three managed rules' Version absent on both sides.",
        "infra/aws/terraform/portal-auth/waf-cloudfront.tf @31995abe76 :183-185, :202-204, :221-223: each managed_rule_group_statement sets vendor_name and name and no version."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC11: the targeted re-plan after the apply reads 'No changes. Your infrastructure matches the configuration.'; AMENDMENT 2 treats the WAF normalization as a one-time in-place change inside the act.",
    "world_is": "The apply changed nothing on the live WebACL and the normalization does not converge: while the config leaves version unset and the API returns none, every plan that includes this WebACL (targeted to the distribution, or whole-root) shows the same 1 change. C1-AC11 as written cannot pass. C1-AC12 (25 of 25 at version 20), C1-AC13 (30 of 30) and C1-AC20 (6 of 6) read as expected, so the served act is Branch A under both halves and was not rolled back.",
    "notes": "Form only. INERT: re-applying it moved no live WAF field on this run. Not measured: the provider version's handling of an absent Version, or whether a whole-root plan shows anything else. How C1-AC11 is re-cut is the issuer's. After this finding the issuer re-cut C1-AC11 (TO-C1-1 AMENDMENT 3 @b2628856f5, on 1.0.0_SA_CTO~Z msg 23255) to accept exactly this one-address, three-leaf residual; the worker records C1-AC11 against that expectation."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S7",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T21:20:00Z",
    "one_line": "C1-AC14's recorder refused rc=2 on its first run on this device: record-terraform-deploy.sh:511 runs the scoping tool through an UNQUOTED $SCOPE_PY, and command -v python3 resolves to /c/Users/Opal Bloomberg/bin/python3, so the path splits at the space ('/c/Users/Opal: Is a directory'). The worker re-ran the identical invocation once with the 8.3 form /c/Users/OPALBL~1/bin first on PATH; the record then committed (5419bca04f).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/record-terraform-deploy.sh @31995abe76 :493 SCOPE_PY=\"$(command -v python3 || command -v python)\"; :511 'if ! $SCOPE_PY \"$SCOPE_TOOL\" \"$PIPELINE\" --terraform \"$TF_LOCAL\" --timestamp \"$TIMESTAMP\" $SCOPE_ARGS; then' -- $SCOPE_PY unquoted.",
        "C1-AC14 run 1, 2026-09-15T21:12:11Z, the order's invocation verbatim: 'record-terraform-deploy.sh: line 511: /c/Users/Opal: Is a directory', 'ERROR: scoped source-map record refused or failed', rc=2; git show --stat HEAD still 31995abe76 (1.0.0_SA_CTO~Z's commit), the auth-validator-edge row unchanged (26ffa22b79).",
        "Device read 2026-09-15T21:15Z: command -v python3 -> /c/Users/Opal Bloomberg/bin/python3; cygpath -d of its directory -> C:/Users/OPALBL~1/bin (printed with backslashes), which lists python3.",
        "C1-AC14 retry 1 of 1, 2026-09-15T21:15:31Z, PATH=/c/Users/OPALBL~1/bin:$PATH, same invocation: 'SCOPED DEPLOY RECORD ... + auth-validator-edge 26ffa22b79 -> 240fe36222', 'stamped 1 of 7 rows under portal-auth'; committed [wk-posn_aggfix-1-2 5419bca04f] 'ci: record deploy portal-auth @ 31995abe [skip ci]'; git show --stat HEAD lists infra/aws/lambda/ci/lambda-source-map.json only.",
        "Same run: the CHANGELOG helper is JavaScript handed to python3 ('SyntaxError: unterminated string literal (detected at line 18)', 'Note: CHANGELOG.json write failed'), the defect row POSN_ASTTAX-Z-W23-S4 already carries; the entry was written by hand."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC14: timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh portal-auth --plan <c1.tfplan> --author <worker>; the recorder's commit verified by git with auth-validator-edge's last_deployed_commit moved.",
    "world_is": "On this device the recorder cannot reach its scoping step while python3 resolves under the spaced user profile, so it refuses before writing anything. With PATH rooted at the 8.3 short name the same invocation records the deploy. The recorder's code was not changed.",
    "notes": "Form only. Not measured: whether any other call site in record-terraform-deploy.sh expands an interpreter path unquoted, or how other devices resolve python3."
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S11",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T22:12:00Z",
    "one_line": "A3-AC5's safe-apply passed the halt gate on its first run without listing the issuer's unread inbox, so the order's OPERATING FACT 2 (read every listed subject, paste the census, re-run with HALT_ACK=1) had nothing to act on; the apply ran once, without HALT_ACK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-A3-1.deploy-the-producer-and-read-the-served-result.md @33dad02f79 OPERATING FACT 2: 'The gate then lists the ISSUER's unread inbox (routine messages, measured 182 at TO-C1-1's apply). Read every listed subject, paste the census into your evidence, and if none begins [STOP] or [HALT], re-run the same safe-apply with HALT_ACK=1 as the gate instructs.'",
        "A3-AC5 run 1, 2026-09-15T22:08:49Z, serial files written to both the worktree and main-workspace session paths immediately before, the order's invocation verbatim: the only halt-gate line printed is 'HALT-GATE: worker 0.9.0_WK_POSN_AGGFIX~1 has no inbox; scanning its issuer 2.0.0_SA_COO~Z (a [STOP] to the issuer halts its workers)'; the tagauthz and tombstone gates follow, then 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.', rc=0 (org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a3_ac5.attempt1.out.txt).",
        ".tools/safe-apply.sh @84fe842e09 :263 '# Checkpoint passed (empty inbox, or routine acked, or audited STOP override).'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-A3-1 OPERATING FACT 2 and A3-AC5: the halt gate lists the issuer's unread inbox, the worker pastes the subject census, and re-runs safe-apply with HALT_ACK=1 when no subject begins [STOP] or [HALT].",
    "world_is": "The gate listed no subjects and asked for no acknowledgment; it passed and the apply completed on the first run. No subject census exists to paste, and HALT_ACK=1 was not used.",
    "notes": "Form only. Not measured: the issuer inbox's unread count at 22:08Z, or which branch of the checkpoint (empty inbox or otherwise) passed it."
  },
  {
    "id": "POSN_AGGFIX-Z-W1-S12",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~1",
    "surfaced_at": "2026-09-15T22:15:00Z",
    "one_line": "yang-invalidate-cloudfront, invoked with its recorded event, invalidates only ONE of the two distributions it names: E2LPCXXBLDGWXY returns NoSuchDistribution and is caught inside the function, so the run reports no FunctionError. The recorded pipeline execution 20260914_v1-9dbd2129 got the same error at 07:08 EDT, so this predates the deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/outputs/invalidate-cloudfront/lambda_function.py @84fe842e09 :28-31 DISTRIBUTION_IDS ['E2LPCXXBLDGWXY', 'EVTSA9VEHNZVH']; :43-52 create_invalidation Paths ['/*']; :60-65 any exception is logged and appended as {'distribution_id', 'error'}, never raised.",
        "A3-AC8 driven invoke 2026-09-15T22:12:21Z, recorded input sha256 031b8fff6f2dbc87: StatusCode 200, FunctionError none, payload {'invalidations': [{'distribution_id': 'E2LPCXXBLDGWXY', 'error': 'An error occurred (NoSuchDistribution) when calling the CreateInvalidation operation: The specified distribution does not exist.'}, {'distribution_id': 'EVTSA9VEHNZVH', 'invalidation_id': 'I7UYBELUPGGXFNJ66T7RKNKEYA', 'status': 'InProgress'}]} (org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/a3_ac8.out.txt).",
        "get_execution_history of arn:aws:states:us-east-1:313476888478:execution:YangDataPipeline:20260914_v1-9dbd2129 (166 events): InvalidateCloudFront TaskStateEntered event 154; LambdaFunctionSucceeded event 157 at 2026-09-15 07:08:06 -04:00 carries the same NoSuchDistribution error for E2LPCXXBLDGWXY and invalidation I1YKVUAI19FE94Z83JXRPD5P3O InProgress for EVTSA9VEHNZVH."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-A3-1 A3-AC8 and the producer COO half's permitted set: yang-invalidate-cloudfront invoked once with its recorded event removes the cache entries for the paths that event names, and the invoke shows no FunctionError.",
    "world_is": "The invoke shows no FunctionError, and one of the function's two hardcoded distributions no longer exists, so only EVTSA9VEHNZVH is invalidated. Every pipeline run does the same: the recorded execution carries the identical error.",
    "notes": "Form only. Not measured: which distribution serves the portal's /api/general/positioning/ paths, whether E2LPCXXBLDGWXY was deleted or renamed, or when the error first appeared."
  }
]
```
