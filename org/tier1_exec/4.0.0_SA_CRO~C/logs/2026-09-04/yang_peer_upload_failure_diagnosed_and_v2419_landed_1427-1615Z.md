# Yang's peer-ranking upload failure: diagnosed, parser fixed, yang-v2.4.19 landed, upload replayed -- 4.0.0_SA_CRO~C

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE

**Date:** 2026-09-04
**Task Order:** ad-hoc -- Andrew-direct (terminal, ~14:2xZ and ~15:2xZ)
**Status:** COMPLETE (push state LOCAL; the shared-branch push is 0.0.0_AB_MSTR's)
**Window:** 2026-09-04 14:27Z (session start, /watcher) -> 16:15Z

---

## Objective

Andrew, verbatim: "Look at Yang's message on MS Teams. Afterwards, check the execution logs for
"Data Refresh" pipeline from the opalinvest.dev portal. It would appear Yang's upload of the Peers data
failed for some reason." Then: "LTA is now ULT and LTC is now LT, see if they have that in the fields
where previously LTA and LTC were expected/housed." Then: "you can land it, i authorize the deployment
according to procedures. then afterward, i want you to find the file he uploaded in the cloud (because i
suspect it made it into the bucket even if the process didnt run) and run it again. ping me when all of
the above is done."

Yang Liu, Teams 1:1 2026-09-04T14:23:24Z: "good morning, Andrew. The peer ranking upload seems not to
work any more. the source data is in the same format"

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "where is the portal data-refresh pipeline (yang-pipeline) defined..." | PARTIAL | 3-way tie (comp-estate / comp-routes / comp-transform), none the answer; routed to comp-find |
| comp-find | -i 'yang-pipeline\|yang_pipeline\|data-refresh' --files --limit 60 | PASS | 14,583 hits / 149,056 files; HEAD band surfaced the peer-performance config + lambda dir on page 1. >120s wall, backgrounded |
| comp-find | 'PipelineExecutionFailed' --files | PASS | 3 hits -> the two state-machine definition JSONs; located YangDataPipeline |
| comp-find | 'validate_peer_output' --files | PASS | 12 hits, DEF band = the one lambda source; also surfaced the 06-26 guard deploy ledger + DS closeout log (the design intent) |
| comp-find | --hidden portal 'peer_performance' (misused) | FAIL | my error: passed the pattern as the path; "NO MEASUREMENT". Fell back to native Grep on portal/src |
| comp-read | lambdas.tf --enumerate 'peer.performance' | PASS | found module block :214 and warned every hit was a substring (correct) |
| comp-read | .owned-paths.yaml --enumerate 'infra/aws/lambda\|...' | PASS | lane for yang lambda source :1794 -> CLOUD_OPS_OR_ETL; recorder files -> YANG_PIPELINE_DEPLOY |
| comp-read | trigger/lambda_function.py --enumerate 'start_execution\|...' | PASS | execution naming `{version}-{uuid[:8]}` |
| comp-aws | yang-generate-peer-performance | FAIL | wrong verb (it wants derive/score/...); graph check for Rule 20 not obtained via comp-aws; the change was code-only in one Lambda with a 0-change baseline plan, so the blast radius was read from the plan |
| commit-gate.sh | lambda_function.py | PASS | py_compile + ds-precommit + ruff clean |
| deploy_ledger.py | open / close-leg x4 / close | PASS | ledger yang-peer-perf-rename-v2.4.19 CLOSED |
| deploy_ledger.py | check | FAIL | crashes mid-sweep: UnicodeEncodeError cp1252 on U+26D4 printing a BYPASS line (surfaced to COO+CTO 94207) |
| safe-apply.sh | -chdir=... apply tfplan-peer-v2419.bin | PASS | comp-tagauthz PASS, tombstone CLEAN, 0/1/0 |
| build-and-upload.sh | yang-pipeline yang-generate-peer-performance | PASS | single-function mode; sha verified by an independent head-object |
| record-terraform-deploy.sh | --version yang-v2.4.19 --function ... | PARTIAL | source-map row correct; CHANGELOG entry "0 commit(s), 0 function(s)" (known writer issue per /cloud-ops). First run refused (lane), second under YANG_PIPELINE_DEPLOY override |
| audit-archive-invoker.py | startup A.2 | PASS | 6 findings; 3 NON-APPEND-EDIT shrinks beyond the owned classes -> one row to CVO (94210) |
| openpyxl raw-cell read | 4 archived workbooks | PASS | THE decisive instrument: parser-independent oracle for labels + 1Y values |

**What worked:** comp-find's HEAD band put the right lambda dir and its config on page 1; comp-read on
.owned-paths.yaml answered the lane question in one call; a raw-cell openpyxl oracle (same pattern the
06-26 DS closeout banked) discriminated source-drift from code-drift and verified the served artifact
independently of the parser.
**What failed:** comp-which tied three unrelated tools for a "where is pipeline X defined" question;
comp-aws has no per-function edge lookup verb; deploy_ledger.py check crashes on non-ASCII output under
cp1252; the aws shim is CLI v1 (v2 flags refused).
**Gap found:** no comp-tool answers "which Step Functions state machine / log group does portal feature X
run through" -- the same portal-chart-to-data-path gap the 06-26 DS log banked, still open.

---

## Work Completed

### 1. Startup (/watcher + org/XXX.md)
Registered `4.0.0_SA_CRO~C` (broker PID 46996), armed the persistent inbox Monitor (task b3d9ug6hq,
bash child 951060), wrote the session serial file, acked 7 stale Aug-25 broker messages
(69581,70843,71027,71046,71075,71158,71383). A.2/A.3/B.0/B.1 ran AFTER the incident (16:07Z): PATH
104/104 + forwarder exercised; delivery ledger 0 rows since 09-03; no TO held by this lane.

### 2. Diagnosis (EXERCISED)
- Step Functions `YangDataPipeline`: `20260904_v1-06273296` (14:20:27Z) and `-3c6fdaa5` (14:22:12Z)
  FAILED at `GeneratePeerPerformance` only; `20260804_v1-74331a80` had failed the same way on
  2026-08-04, unnoticed.
- CloudWatch `/aws/lambda/yang-generate-peer-performance`: `ValueError ... missing expected models:
  ['LTA', 'LTC']` from the 2026-06-26 fail-closed guard `validate_peer_output` (lambda_function.py:135).
- Live Lambda CodeSha256 `uhHb2esvNIC/...` == the 06-26 deploy: code unchanged, SOURCE changed.
- Raw cells, Peer Table block 4 (col AA): 08-03 upload of the July file = "Aggressive growth daily
  returns" (1Y 18.5667) / "Conservative growth daily returns" (1Y 17.2745), SUCCEEDED; 08-04 re-upload
  of the same file = "Long term daily returns" (1Y 17.2745) / "Ultra long term daily returns"
  (1Y 18.5667), FAILED. Today's 20260831 file carries the new labels. Values tie LT=old LTC,
  ULT=old LTA, as Andrew stated.
- Portal FE already aliases ULT->LTA, LT->LTC (`portal/src/lib/modelPortfolioColors.ts:371-372`) and
  renders the JSON `name` (`PeersTab.tsx:440`).

### 3. Fix + harness
`MODEL_MAP` gains `'ultra long term': 'LTA'` (before `'short term'`) and `'long term': 'LTC'` (last);
old labels retained; `MODEL_NAMES` LTC='Long-Term', LTA='Ultra Long-Term'. Harness over 20260630,
20260731 (08-03), 20260731 (08-04), 20260831 with a raw-cell 1Y oracle: HEAD parser 3/5+RAISE on the two
renamed files and 5/5 on the older two; patched parser 5/5 on all four, zero mismatches.

### 4. Deploy (see Deployment Sequence) and replay
Yang's file was in the bucket (`uploads/Models Performance vs Peers 20260831.xlsx`, 558,689 B,
14:22:11Z) with `uploads/manifest.json`. Replayed via the production trigger (`aws lambda invoke
yang-pipeline-trigger` with the S3 Records event for that manifest) -> `20260904_v1-33c4dc7a`
SUCCEEDED 15:51:11Z-15:51:53Z, 89 events, 0 failures, `InvalidateCloudFront` entered.

### 5. Records + comms
Andrew-direct record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260904_1423Z_PEER_UPLOAD_FAILED_LTA_IS_ULT_LTC_IS_LT.md`
@9ba7dfe9f6, updated with the executed path @b337b17e8f. Two memory entries (the rename fact; the
aws-shim-is-CLI-v1 trap). Broadcasts: 94198/94199/94200 (diagnosis, before the GO), 94207/94208/94209
(landed), 94210/94211 (audit-log shrink observation to CVO+CTO). PushNotification sent per "ping me".

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | deploy_ledger.py open yang-peer-perf-rename-v2.4.19 (4 legs, 4h) | `a51251338b` |
| 1 | Commit source (GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL, audited) | `beac7179dd`, commit-gate PASS |
| 2 | build-and-upload.sh yang-pipeline yang-generate-peer-performance | SHA256 `OGIdaw7yRfdc8PYT/Eq4O+32pQsceBm4Lh/86V+HK8k=` size 5335; head-object version `e_fvjPt0nNk_X7kbnqlafqf_9SnMLHev`, metadata match |
| 3 | terraform init + baseline targeted plan (before upload) | init OK; "No changes" -> no pre-existing drift on the module |
| 4 | targeted plan -out tfplan-peer-v2419.bin | 0 add / 1 change / 0 destroy (s3_object_version + source_code_hash only) |
| 5 | safe-apply.sh -chdir=infra/aws/terraform/yang-pipeline apply tfplan-peer-v2419.bin | tagauthz PASS, tombstone CLEAN; "0 added, 1 changed, 0 destroyed" |
| 6 | 0-diff plan (targeted) | "No changes" |
| 7 | record-terraform-deploy.sh --version yang-v2.4.19 --function ... (GIT_COMMIT_AUTHOR_OVERRIDE=YANG_PIPELINE_DEPLOY, audited) | `34263765d7`; source-map last_deployed_commit=beac7179dd |
| 8 | git tag -a yang-v2.4.19 -> 34263765d7 | tag LOCAL; push NOT performed (shared-branch law) |
| 9 | replay via yang-pipeline-trigger | `20260904_v1-33c4dc7a` SUCCEEDED |
| 10 | deploy_ledger.py close (4/4 legs proven) | `b337b17e8f` |

## Verification

```
LIVE: CodeSha256=OGIdaw7yRfdc8PYT/Eq4O+32pQsceBm4Lh/86V+HK8k= LastModified=2026-09-04T15:44:03.000+0000 LastUpdateStatus=Successful State=Active CodeSize=5335 Runtime=python3.11 Timeout=240
TERMINAL: status=SUCCEEDED start=2026-09-04T15:51:11Z stop=2026-09-04T15:51:53Z name=20260904_v1-33c4dc7a
TOTAL EVENTS: 89  failures: 0
served json/peers/peer_performance.json size=8506 lastmod=Fri, 04 Sep 2026 15:51:22 GMT
generated_at: 2026-09-04T15:51:21Z data_as_of: 2026-08-31 periods: ['1M', 'QTD', '1Q', 'YTD', '1Y', 'Since Inception']
  INT  name='Intermediate-Term'    1Y=12.0723 raw=12.0723 MATCH periods=6/6 nulls=[]
  LTA  name='Ultra Long-Term'      1Y=16.6039 raw=16.6039 MATCH periods=6/6 nulls=[]
  LTC  name='Long-Term'            1Y=15.6316 raw=15.6316 MATCH periods=6/6 nulls=[]
  ST   name='Short-Term'           1Y=3.6215 raw=3.6215 MATCH periods=6/6 nulls=[]
  UST  name='Ultra Short-Term'     1Y=3.3901 raw=3.3901 MATCH periods=6/6 nulls=[]
MODELS: 5 /5 -> SERVED VERIFIED
json/latest/peer_excel.json: latest_version=20260904_v1 data_as_of=2026-08-31 pipeline_execution_id=33c4dc7a-8ecc-414c-8184-b3625dd5820b
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep internal codes LTA/LTC; rename only the display names | The FE keys every chart on LTA/LTC and already aliases ULT/LT to them; changing codes would need a portal deploy for a data fix |
| Accept BOTH label generations in MODEL_MAP | Archived workbooks re-run cleanly; the guard still fires on a third rename |
| Replay via the production trigger, not `start-execution` | The trigger mints ids, writes `json/latest/peer_excel.json`, and is the exact path a portal retry takes |
| Targeted apply with a saved plan | Baseline plan proved zero module drift; a whole-root apply was un-planned blast radius for a one-function fix |
| Two audited overrides rather than a lane edit | One-off on Andrew's word; the standing lanes (CLOUD_OPS_OR_ETL, YANG_PIPELINE_DEPLOY) are correct for the seats that normally deploy |
| Do not push CLOUD or the tag | LD-0367/0368: shared-branch push is MSTR's on Andrew's word; the deployed Lambda does not depend on it |

---

## Files Modified

See commit messages: `9ba7dfe9f6`, `beac7179dd`, `a51251338b`, `34263765d7`, `b337b17e8f`. Extra context:

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-peer-performance/lambda_function.py` | MODEL_MAP + MODEL_NAMES (+15/-3) | Yes -- `beac7179dd` (lane override CLOUD_OPS_OR_ETL) |
| `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | deploy record | Yes -- `34263765d7` (lane override YANG_PIPELINE_DEPLOY) |
| `infra/aws/terraform/yang-pipeline/tfplan-peer-v2419.bin` | saved plan (untracked, consumed) | No -- local artifact |
| `~/.claude/.../memory/reference_yang_peer_workbook_renamed_long_term_pair_lta_is_ult_ltc_is_lt.md`, `..._the_tools_aws_shim_is_cli_v1_...md`, `MEMORY.md` | memory | n/a (agent memory dir) |

---

## Blockers

None owned by this seat. Sequence state with its holder:
- **[0.0.0_AB_MSTR]** push of CLOUD (5 commits) + tag `yang-v2.4.19` -- on Andrew's word. Not a blocker for the deployed fix.

---

## Current State

> For a reader with zero prior context.

`yang-generate-peer-performance` (Lambda, us-east-1, account 313476888478) is LIVE at CodeSha256
`OGIdaw7yRfdc8PYT/Eq4O+32pQsceBm4Lh/86V+HK8k=` (source `beac7179dd`, tag `yang-v2.4.19` ->
`34263765d7`, Terraform state `yang-pipeline/tfstate` 0-diff on the module). It now parses Yang's
renamed long-term rows ("Ultra long term" -> LTA, "Long term" -> LTC) and the older labels. Yang's
2026-08-31 workbook was replayed as `YangDataPipeline:20260904_v1-33c4dc7a` (SUCCEEDED); the served
`s3://opal-data-portal-v2/json/peers/peer_performance.json` (generated 15:51:21Z, data_as_of 2026-08-31)
carries 5 models x 6 periods with every 1Y value equal to the raw workbook cell, and CloudFront was
invalidated by the run. Deploy ledger `org/critical_paths/change_management/20260904T1531Z_yang-peer-perf-rename-v2-4-19_deploy_completion.md`
is CLOSED. Push state LOCAL: origin/CLOUD `fa82d6b93c` (ls-remote); commits `9ba7dfe9f6`,
`beac7179dd`, `a51251338b`, `34263765d7`, `b337b17e8f` and the tag exist only on this device.

---

## Next Steps

1. **[0.0.0_AB_MSTR] push CLOUD with `--follow-tags`** on Andrew's word -- carries the source, the deploy record and `yang-v2.4.19`.
2. **[Andrew] tell Yang** the Peers tab now labels the pair "Ultra Long-Term" / "Long-Term"; uploads work as before.
3. **[2.0.0_SA_COO / 0.7.0_AE_CloudOps] `deploy_ledger.py check` crash** (cp1252 on U+26D4) -- surfaced in 94207; `/drive`'s `check --red` may be exiting on the traceback.
4. **[3.0.0_SA_CVO] audit-log NON-APPEND-EDIT shrinks** (mass-deletion, safe-deploy-bypass, rcg-sweep) -- surprise row 94210; not investigated here.
5. **[4.0.0_SA_CRO~C]** back to event-driven: inbox Monitor b3d9ug6hq live; no loop armed.
