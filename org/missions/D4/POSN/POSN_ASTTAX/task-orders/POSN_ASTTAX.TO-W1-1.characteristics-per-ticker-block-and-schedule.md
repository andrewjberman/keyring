# TO POSN_ASTTAX.TO-W1-1 -- `characteristics.json` GAINS THE PER-TICKER `tickers` BLOCK (every ticker any satellite holds, once, with its source; GLD's returns from the estate's ONE returns rule); the rule moves to `cron(30 12 * * ? *)`; deployed through Terraform, then DRIVEN with an explicit `bbg_as_of` (AT6-s-1, B6; FWD-7 served, C-HOLDING-MEASURES, C-B4-SCHEDULE)

<to_id>POSN_ASTTAX.TO-W1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~24</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.11** @`ab2ee8052a` (s.0 ADDENDUM
v0.9 + v0.10 + v0.11: FWD-7, C-HOLDING-MEASURES, C-B4-SCHEDULE, C-HOLDING-IDENTITY; the returns rule for a Bloomberg-sourced ticker;
AMENDED ~04:1xZ on v0.11 -- the identity pair and the table read, Z-S139 / Z-S141) - **Decomp cell:** `AT6-s-1` -
**Issuance:** round 6, wave 1, slot `~24`. **GATES `AT6-s-2` (F4)**, which attaches what you serve.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~24`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~24;`. Your worktree is
`/c/tmp/wk-posn-6-24` (branch `wk-posn_asttax-6-24`, a sparse cone cut by the COO; do NOT re-create it). First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit ONLY via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~24 <0.9.0_WK_POSN_ASTTAX~24@opal.agent>" -F <msgfile> -- <paths>` (the
msgfile written by the Write tool or python, never a shell heredoc). Never push, merge, rebase, `checkout --`, `clean`. Every `.py`
edit passes `.tools/commit-gate.sh`. **Immediately before EVERY `safe-apply`:** write your serial into the halt-gate session file in
BOTH roots -- `printf '%s' 0.9.0_WK_POSN_ASTTAX~24 > org/mcp/sessions/c880f6b2-bdc0-4941-86d5-8ba8c531349a.serial` in the worktree
(create `org/mcp/sessions/` there; the file is gitignored) and in `/c/Users/Opal Bloomberg/Desktop/ajb_workspace/` -- the file is
LAST-WRITER-WINS across this COO's workers. Environment for every recorder or python call: `PYTHONUTF8=1`, and a space-free `python3`
shim directory first on PATH (the recorder's unquoted python path splits on this device's space; W23-S4).

## THE CELL

Andrew ~02:1xZ: *"no characteristics or performance in the 'Holdings Breakdown' panel"*; ~02:3xZ: *"just fix it completely, we're not
waiting for the next day"*; ~03:0xZ: *"vendor change approved go get it"* (GLD's return history, a CTO act you READ, never land).
**PRD C-HOLDING-MEASURES:** `characteristics.json` ALSO publishes, once per artifact, a `tickers` block keyed by ticker for every ticker
any satellite holds: `fee, aum, active, yield, duration, credit, beta, returns, source`. Precedence is the producer's existing PER-TICKER
rule, unchanged. Every existing field of the artifact is unchanged for the same inputs. **C-B4-SCHEDULE:** `cron(30 12 * * ? *)` UTC,
never success-of-upstream; deploy, then a DRIVEN run with an explicit `bbg_as_of`; the scheduled fire is the organic leg (the COO's).

**Measured at HEAD (the issuer, ~03:1xZ) -- read it back, never trust this text:** `data/assets/scripts/gold/build_satellites_characteristics.py`
(499 lines): `build()` :355-405 is PURE (:357-362); `resolve_ticker` :270-282 (Yang row -> `positioning_data`; else bbg -> `bbg`; else
`none`), called per holding at `aggregate_satellite` :305; `yang_index` :204-232 keeps ONLY `SCALAR_FIELDS` (:113) + `returns` (:225-226)
and DROPS `aum`, `active`, `credit` that a Yang `current_holdings` row carries (the row type: `portal/src/api/portal-proxy.ts:1062-1109`
at `dd1d33c6db` -- `aum` in millions, `active` 0|1); `bbg_index` :234-257 over `BBG_SCALAR_COLUMNS` :117-122 and `BBG_RETURN_COLUMNS = {}`
:125; the envelope :373-405 (`schema_version` 1, `inputs` :377-386, `method` :387-399, `satellites` :404); `publish` :429-434; `main`
:452-495 (`--as-of`, `--bbg-as-of`, `--dry-run`, `--out`). The handler `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py:72-96`
forwards `dry_run` (:80) and `bbg_as_of` (:82-83) only. `build_package.py` :93-102 lists the members at the repo-mirroring layout, pinned
by `--pin` (:105-136, immutable only). The `.tf` `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`: rule :272-277,
target :279-283, module :222-243 (512 MB, 120 s, layer `pandas-pyarrow-requests-layer:1`), policy :95-150 (Sids at :103, :109, :119,
:132), deny :152-170; the module `infra/aws/terraform/modules/yang-lambda/main.tf:17-20, :36-39` reads the artifact's `version_id` and
`metadata["content-sha256"]` -- UPLOAD BEFORE PLAN. **The returns rule** (v0.10; the estate's ONE): `data/etfs/scripts/gold/etf_positioning_gold.py`
`load_history(as_of, bucket)` :731-830 (every `bbg/<date>/history_topup.parquet` inside `HISTORY_LOOKBACK_DAYS` 400 :320, listed on
`bbg/` :746, plus `_load_backfill_history` :675-729 listing `bbg-testpull/tickers/` :690-693 and reading each `history.csv`) and
`compute_returns(tkr, as_of, hist)` :855-921 (`RETURN_WINDOWS` :319; frontier ON `as_of`; start coverage; a NaN disqualifies). It is
import-safe (`_s3()` :361 lazy; `sys.path` :77-78 resolve under the mirrored layout; pandas from the layer). **You READ it by pin as a
zip member at its repo path; you never edit it** (its lane is ETFS).

**Your act, in this order:**
1. `build_satellites_characteristics.py`: (a) `yang_index` ALSO keeps `aum`, `active`, `credit` per ticker (a separate per-ticker map,
   so `aggregate_satellite`'s inputs and every existing field are byte-for-byte the same computation); (b) `bbg_index` ALSO keeps
   `aum <- FUND_TOTAL_ASSETS` per ticker (same unit as Yang's `aum`, measured 5 of 5 by the CTO; print your own 5-of-5 read in W1-AC4);
   (c) a NEW pure function builds `tickers`: for every DISTINCT ticker across `holdings.json`'s rows, once: source by `resolve_ticker`;
   a `positioning_data` row supplies all seven scalars and its `returns` verbatim; a `bbg` row supplies `fee, yield, duration, beta`
   (`BBG_SCALAR_COLUMNS`), `aum`, `active` NULL, `credit` NULL, and `returns` = `compute_returns(ticker, bbg_as_of, hist)` where `hist =
   load_history(bbg_as_of)` (imported from `etf_positioning_gold`; loaded ONCE per run and only if any `bbg`-sourced ticker exists);
   `none` -> every field NULL; (d) the envelope gains `tickers` and ONE new key `method.tickers_block` (`bbg_aum_column`, `returns_rule`,
   `returns_as_of`, `history_partitions_read`, `backfill_tickers_read`, `identity_source`, `identity_missing`); **`schema_version` stays 1;
   nothing else changes.** (e) **THE IDENTITY PAIR (v0.11 C-HOLDING-IDENTITY):** every `tickers` entry ALSO carries `name` and
   `management_style`, read for every DISTINCT ticker through the estate's one classifier module
   `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (`ETFClassifier(table_name).get_classification(ticker)` -- one
   `get_item` per distinct ticker, ~25 reads per run, the same call `build_satellites_registry.py:312-347 load_classifier` already makes),
   INDEPENDENT of the measures' source precedence (unchanged); a ticker the table does not carry publishes both NULL and is COUNTED in
   `method.tickers_block.identity_missing` (`identity_source` names the table). Measured basis (the CTO, ~04:0xZ, full scan 285 items): all 25
   satellite tickers carry both; Yang's `name` and `active` agree with the table 23 of 23.
   `validate()` additionally checks each satellite ticker appears in `tickers` exactly once.
2. `build_package.py`: the member `data/etfs/scripts/gold/etf_positioning_gold.py` at its repo path (read by pin like the others), AND the
   member `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` mapped FLAT at the zip root, exactly as the registry
   producer's `build_package.py:117-121` does (the `_shared` path is not an importable package name), imported by its module name.
   `lambda_function.py`: unchanged unless the import path needs `data/etfs/scripts/gold` on `sys.path` (state it).
3. The `.tf`: the rule's cron; the policy's READ grant widened EXACTLY as both never-widen halves name (`s3:ListBucket` on
   `arn:aws:s3:::opal-data-etfs` with `s3:prefix` conditioned to `bbg/*` and `bbg-testpull/tickers/*`; `s3:GetObject` on
   `opal-data-etfs/bbg/*/history_topup.parquet` and `opal-data-etfs/bbg-testpull/tickers/*/history.csv`); NO new write, the deny
   unchanged; AND (v0.11) a READ grant on the table -- Sid `ReadEtfClassifications`, `dynamodb:GetItem` ONLY on
   `arn:aws:dynamodb:<region>:<account_id>:table/etf-classifications` (NARROWER than the registry producer's
   `satellites-registry-producer.tf:145-152` precedent, which also grants BatchGetItem: the module's per-ticker path calls `get_item`
   only, and BOTH never-widen halves name exactly that one action -- CTO half A1 @2c6b7d8887, COO half R1; no `BatchGetItem`, no
   `Scan`, no `Query`, no write). Memory: keep 512 MB unless W1-AC4 prints a peak above
   384 MB, then 1024 MB and say so.
4. Deploy (W1-AC5..W1-AC11), then the DRIVEN run (W1-AC12), the rule read (W1-AC13), the record (W1-AC14).

**The never-widen halves (NEVER#1):** `org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND6_COO_HALF.md` and
`org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND6_CTO_HALF.md`. **You reach W1-AC7 (the first world write) only if BOTH exist at
HEAD and name this act (the key, the rule, the READ widening INCLUDING the table read -- COO half R1 AMENDMENT, CTO half amended likewise --
and the driven run); otherwise REFUSE the leg with a row and stop there** --
W1-AC3..W1-AC6 still run (nothing is written). **Rollback (from the halves):** the key's prior VersionId (printed in W1-AC1) restored by
`copy_object`; the function re-pointed to artifact version `sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml`; the `.tf` reverted and re-applied.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route. A
producer that REFUSES (a partition absent, a read denied) is the measured act of that criterion: record it, file the row, keep going.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W24-S<k>` (start at S1), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="W1-AC1" cell_refs="AT6-s-1"><invocation>timeout 120 bash -c "python3 .tools/prd-signoff.py status POSN_ASTTAX; git log -1 --format=%h -- org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND6_COO_HALF.md; git log -1 --format=%h -- org/missions/D4/POSN/POSN_ASTTAX/ledger/NEVER_WIDEN_ROUND6_CTO_HALF.md; .tools/aws s3api head-object --bucket opal-data-cot --key platinum/satellites/characteristics.json --query '{v:VersionId,lm:LastModified,len:ContentLength}' --output json; .tools/aws s3api list-objects-v2 --bucket opal-data-etfs --prefix bbg/ --delimiter / --query 'CommonPrefixes[].Prefix' --output text | tr '\t' '\n' | sort | tail -3"</invocation><expect>ADMITTED at the pinned PRD hash with BOTH halves SIGNED current; two non-empty commit hashes (both never-widen halves exist at HEAD -- absent = REFUSE the deploy leg at W1-AC7); the served key's VersionId printed as <PRIOR_CHARACTERISTICS_VERSIONID> (the rollback); the newest bbg partition printed as <NEWEST_BBG_PARTITION> (its characteristics.parquet head-object 200 in the same reading).</expect></criterion> `W1-AC1` -- THE PRECONDITIONS, READ BACK; THE ROLLBACK AND THE PARTITION PINNED.

<criterion id="W1-AC2" cell_refs="AT6-s-1"><invocation>timeout 60 python3 .tools/deploy_ledger.py open --slug posn-round6-b6-characteristics-tickers --title "POSN_ASTTAX B6: characteristics.json gains the tickers block; rule to cron(30 12 * * ? *); driven run" --author 0.9.0_WK_POSN_ASTTAX~24 --window-hours 4 --leg "L1|git|SITEZ commit of producer + build_package + tf|hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip|VersionId + content-sha256 read back" --leg "L3|verify|targeted plan|0 add / 3 change / 0 destroy" --leg "L4|activation|safe-apply|summary + HALTGT" --leg "L5|verify|unscoped 0-diff|No changes" --leg "L6|verify|driven invoke with explicit bbg_as_of lands the tickers block|VersionId moved + block read back" --leg "L7|verify|rule cron(30 12 * * ? *) ENABLED with the function as target|describe-rule + list-targets" --leg "L8|verify|first scheduled 12:30Z fire lands organically (the negative arm; recorded by the COO, not waited on here)|s3api head after the fire" --leg "L9|git|deploy recorded: source map + CHANGELOG entry by hand|git show --stat"</invocation><expect>the entry created under org/critical_paths/change_management/ with 9 legs; L8 stays OPEN by design.</expect></criterion> `W1-AC2` -- THE LEDGER, OPENED FIRST.

<criterion id="W1-AC3" cell_refs="AT6-s-1"><invocation>timeout 900 bash -c "PYTHONUTF8=1 python3 <DIFFERENCE_CONTROL_PURITY> --bbg-as-of <NEWEST_BBG_PARTITION>"</invocation><expect>the script (in your deliverables) loads the three inputs ONCE, read-only, from the live keys (holdings.json, positioning_data.json, the bbg partition's characteristics.parquet + run_manifest.json), runs build() from HEAD's module (extracted with `git show HEAD:data/assets/scripts/gold/build_satellites_characteristics.py` to a temp path) and from your working module over the SAME objects, strips exactly `tickers` and `method.tickers_block` from yours, and prints DEEP-EQUAL True with the leaf count compared (> 200) and the two stripped keys named; POSITIVE CONTROL: with one leaf perturbed the same compare prints False. The live bucket is never written.</expect></criterion> `W1-AC3` -- PURITY: EVERY EXISTING FIELD UNCHANGED FOR THE SAME INPUTS.

<criterion id="W1-AC4" cell_refs="AT6-s-1"><invocation>timeout 900 bash -c "PYTHONUTF8=1 python3 data/assets/scripts/gold/build_satellites_characteristics.py --bbg-as-of <NEWEST_BBG_PARTITION> --dry-run --out <LOCAL_OUT> && PYTHONUTF8=1 python3 <LOCAL_DRY_RUN_TICKERS> <LOCAL_OUT>"</invocation><expect>rc 0, nothing written to S3 (the dry-run SKIP line); the reader script prints from <LOCAL_OUT>: the tickers block's count EQUALS the distinct-ticker count across holdings.json's rows (25 expected; both numbers printed) and no ticker twice; sources by name (23 positioning_data expected, GLD bbg, CASH none -- printed, not assumed); for every ticker both sources carry, Yang aum vs FUND_TOTAL_ASSETS printed side by side with the count equal (5 of 5 expected); GLD: active NULL, credit NULL, fee/yield/duration/beta from the bbg columns, returns per window -- a value where load_history found GLD's series with an observation ON <NEWEST_BBG_PARTITION> and start coverage, else null with the rule's reason (frontier absent / start coverage / no series) printed per window: BOTH branches are the measured act; CASH all NULL; the identity pair (name, management_style) present for 25 of 25 tickers (the count printed; identity_missing 0 expected, a NULL pair counted, never guessed); the satellites block of <LOCAL_OUT> parse-identical to the served artifact's when the inputs triple is unchanged (both triples printed), else stated; peak RSS printed.</expect></criterion> `W1-AC4` -- THE LOCAL DRY RUN: THE BLOCK, READ AND COUNTED.

<criterion id="W1-AC5" cell_refs="AT6-s-1"><invocation>timeout 300 bash .tools/commit-gate.sh data/assets/scripts/gold/build_satellites_characteristics.py infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/build_package.py infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf</invocation><expect>clean for 4 of 4 named files (py_compile + ds-precommit + ruff); the cross-firm limb quoted as NOT FIRING (opal-data-etfs is in no foreign list; the producer's home dir matches none).</expect></criterion> `W1-AC5` -- THE GATE, ON EVERY EDITED FILE.

<criterion id="W1-AC6" cell_refs="AT6-s-1"><invocation>timeout 300 bash -c "cd infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer && python3 build_package.py --pin <COMMITTED_HASH> --out /c/tmp/wk-posn-6-24/.scratch/b6.zip && python3 build_package.py --pin HEAD --out /c/tmp/wk-posn-6-24/.scratch/never.zip; echo rc=\$?"</invocation><expect>the first build lists every member at the mirroring layout INCLUDING data/etfs/scripts/gold/etf_positioning_gold.py with its sha256, the in-zip BUILD_MANIFEST and the sidecar written; the second (a moving ref) is REFUSED non-zero -- the positive control that the pin is immutable.</expect></criterion> `W1-AC6` -- THE PACKAGE, PINNED; A MOVING REF REFUSED.

<criterion id="W1-AC7" cell_refs="AT6-s-1"><invocation>timeout 300 bash -c ".tools/aws s3api put-object --bucket opal-313476888478-lambda-artifacts --key cot-pipeline/cot-satellites-characteristics-producer.zip --body /c/tmp/wk-posn-6-24/.scratch/b6.zip --metadata content-sha256=<ZIP_SHA256_B64> --output json && .tools/aws s3api head-object --bucket opal-313476888478-lambda-artifacts --key cot-pipeline/cot-satellites-characteristics-producer.zip --output json"</invocation><expect>ONLY after W1-AC1 read both halves at HEAD; the head-object READ BACK (never the put response) prints the new VersionId, ContentLength equal to the zip's bytes and Metadata content-sha256 equal to the base64 sha256 you computed; the PRIOR version printed as the rollback (sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml expected -- read, not assumed).</expect></criterion> `W1-AC7` -- THE ARTIFACT UPLOADED, READ BACK, PRIOR VERSION KEPT.

<criterion id="W1-AC8" cell_refs="AT6-s-1"><invocation>timeout 300 comp-iam gaps infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf</invocation><expect>the policy reads exactly: the three existing input GetObjects, the ONE pinned PutObject, plus the READ widening the halves name (ListBucket on opal-data-etfs conditioned to the two prefixes; GetObject on history_topup.parquet and bbg-testpull/tickers/*/history.csv; GetItem ONLY on table/etf-classifications) -- no wildcard bucket, no new write, no BatchGetItem, no Scan, the cross-firm deny present; the DESIRED-plane caveat quoted.</expect></criterion> `W1-AC8` -- THE GRANT, EXACTLY THE HALVES' LIST.

<criterion id="W1-AC9" cell_refs="AT6-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan -target=module.cot_satellites_characteristics_producer -target=aws_iam_role_policy.cot_satellites_characteristics_producer_s3 -target=aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily -out=C:/tmp/wk-posn-6-24/.scratch/b6.tfplan</invocation><expect>Plan: 0 to add, 3 to change, 0 to destroy -- exactly the function (s3_object_version + source_code_hash to W1-AC7's values, memory if changed), the policy (the READ widening) and the rule (schedule_expression cron(20 7 * * ? *) -> cron(30 12 * * ? *)); each change named from the plan text; the plan path ABSOLUTE (-chdir re-bases a relative one, W19-S2).</expect></criterion> `W1-AC9` -- THE PLAN: THREE CHANGES, NAMED.

<criterion id="W1-AC10" cell_refs="AT6-s-1"><invocation>timeout 900 .tools/safe-apply.sh -chdir=infra/aws/terraform/cot-pipeline apply C:/tmp/wk-posn-6-24/.scratch/b6.tfplan</invocation><expect>the halt-gate serial file written in both roots immediately before; Apply complete! Resources: 0 added, 3 changed, 0 destroyed; the HALTGT output pasted; then `aws lambda get-function-configuration` prints CodeSha256 EQUAL to W1-AC7's content-sha256 and LastModified after the apply (the live plane, a second instrument).</expect></criterion> `W1-AC10` -- THE APPLY, CORROBORATED ON THE LIVE PLANE.

<criterion id="W1-AC11" cell_refs="AT6-s-1"><invocation>timeout 600 terraform -chdir=infra/aws/terraform/cot-pipeline plan</invocation><expect>No changes. Your infrastructure matches the configuration. (unscoped, the whole root).</expect></criterion> `W1-AC11` -- THE 0-DIFF, UNSCOPED.

<criterion id="W1-AC12" cell_refs="AT6-s-1"><invocation>timeout 600 bash -c ".tools/aws lambda invoke --function-name cot-satellites-characteristics-producer --cli-binary-format raw-in-base64-out --payload '{\"bbg_as_of\": \"<NEWEST_BBG_PARTITION>\"}' /c/tmp/wk-posn-6-24/.scratch/b6_invoke.json --output json && cat /c/tmp/wk-posn-6-24/.scratch/b6_invoke.json && .tools/aws s3api head-object --bucket opal-data-cot --key platinum/satellites/characteristics.json --query '{v:VersionId,lm:LastModified,len:ContentLength}' --output json && PYTHONUTF8=1 python3 <LOCAL_DRY_RUN_TICKERS> --served"</invocation><expect>StatusCode 200, NO FunctionError, body rc 0 (a refusal -- partition absent, a read denied -- is recorded verbatim as the measured act with a row; nothing written); the served VersionId MOVED off <PRIOR_CHARACTERISTICS_VERSIONID>; the served artifact read with get-object: its tickers block DEEP-EQUAL to <LOCAL_OUT>'s over the same inputs triple (printed; name and management_style included), its satellites block equal to the pre-deploy served block when the triple is unchanged; the edge copy is not asserted here (DefaultTTL 60 s; F4 reads it).</expect></criterion> `W1-AC12` -- THE DRIVEN RUN, READ BACK AGAINST THE DRY RUN.

<criterion id="W1-AC13" cell_refs="AT6-s-1"><invocation>timeout 120 bash -c ".tools/aws events describe-rule --name cot-satellites-characteristics-producer-daily --query '{state:State,expr:ScheduleExpression}' --output json && .tools/aws events list-targets-by-rule --rule cot-satellites-characteristics-producer-daily --query 'Targets[].[Id,Arn]' --output json"</invocation><expect>ENABLED, cron(30 12 * * ? *); one target, the function's ARN. L8 (its first fire, 2026-09-15 12:30Z) is the COO's organic read, not yours.</expect></criterion> `W1-AC13` -- THE SCHEDULE, AFTER ITS INPUT.

<criterion id="W1-AC14" cell_refs="AT6-s-1"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh --plan C:/tmp/wk-posn-6-24/.scratch/b6.tfplan</invocation><expect>the record commit VERIFIED by `git show --stat` listing infra/aws/lambda/ci/lambda-source-map.json (never by the script's stdout); its CHANGELOG helper cannot run here (W23-S4: a hardcoded bun path) -- write the CHANGELOG.json entry YOURSELF in the helper's exact shape (record-terraform-deploy.sh:600-700: version, deployed_at, deployed_commit, deployed_commit_short, previous_commit, branch, agent, functions_updated, commits, artifacts -- scoped to this ONE function) at the HEAD of entries, json.dump(ensure_ascii=False, indent=2) + trailing newline in UTF-8, the file's non-ASCII count UNCHANGED (print len(b) - len(b.decode('utf-8')) before and after), committed under your grant; the other two device defects worked around by ENVIRONMENT only (PYTHONUTF8=1; the space-free python3 shim), never by editing the script; legs L1-L7 and L9 closed with proofs; L8 OPEN by design.</expect></criterion> `W1-AC14` -- THE RECORD, GIT-VERIFIED; THE LEDGER LEGS CLOSED.

<criterion id="W1-AC15" cell_refs="AT6-s-1" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether precedence BY TICKER (a whole Yang row before any Bloomberg column) is the honest reading for a page reader when the two sources agree on aum and fee but only one carries active and credit; and whether serving GLD's returns from the ETF gold rule beside Yang's windows (start-inclusive, 1Q 91 vs 90 days -- disclosed in the PRD) is a difference a reader must be told on the page or only in the artifact. Record the readings and offer NO verdict.</expect></criterion> `W1-AC15` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>W1-AC1, W1-AC2, W1-AC3, W1-AC4, W1-AC5, W1-AC6, W1-AC7, W1-AC8, W1-AC9, W1-AC10, W1-AC11, W1-AC12, W1-AC13, W1-AC14, W1-AC15</expected_criteria>

<placeholders>COMMITTED_HASH, DIFFERENCE_CONTROL_PURITY, LOCAL_DRY_RUN_TICKERS, LOCAL_OUT, NEWEST_BBG_PARTITION, PRIOR_CHARACTERISTICS_VERSIONID, ZIP_SHA256_B64</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-W1-1.characteristics-per-ticker-block-and-schedule.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~24/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/build_satellites_characteristics.py
infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/
infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf
infra/aws/terraform/cot-pipeline/CHANGELOG.json
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round6.md</decomp_doc> round 6, cell `AT6-s-1`.
<owned_cells>AT6-s-1</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-2` (holdings.json, the ticker set), `AT5-s-4` (the producer you extend), the ETF gold module
(read by pin), the Bloomberg backfill (a CTO act; you read whatever exists at the run). DOWNSTREAM: `AT6-s-2` (F4) attaches the block.
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-15 ~03:2xZ -- 5 of 5 carriers within budget (C1=23 sentinel lines, C2=9 open deploy ledgers, C3=12 NEVER clauses, C4=21 scope guards, C5=334 blocking fields); GATES ARMED 2, neither a POSN gate; the B4 ledger `posn-round5-b4-satellites-characteristics` is OPEN at L8 (its organic arm) and this cell supersedes that arm with the rescheduled rule's first fire: close its L8 SUPERSEDED with a pointer to your ledger, stated in W1-AC14.
comp-iam: RUN 2026-09-15 ~03:2xZ -- DESIRED plane, 474 .tf files, 404 policy blocks attached, 26 NOT ATTACHED, deny overlay 2 unparsed; `comp-iam service cot-satellites-characteristics-producer` reads "No AWS operations detected" -- BLIND BY CONSTRUCTION (the calls are vendored by pin, the trigger carries no call site), so the grant is graded by W1-AC8 (`comp-iam gaps` on the .tf) and by the live apply (W1-AC10); the deny's parse silence is not "allowed".
comp-adversary: RUN on the decomposition (5 complement sources run / 0 deferred / 4 declared-excluded, 12 digests). NOT covered, stated: (1) the issuer has not run load_history inside the Lambda's 512 MB / 120 s envelope -- a peak or a wall that exceeds it is a row and a sizing change, stated in the .tf; (2) whether etf_positioning_gold's import under the layer resolves `trading_calendar` the way the producer already does is unread -- the dry run is the instrument; (3) the issuer has not read how many tickers the backfill prefix lists (a full list of every ticker's history.csv for one GLD read is a cost, not a defect -- print the count).
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~24/POSN_ASTTAX.TO-W1-1.characteristics-per-ticker-block-and-schedule.proof_of_spec.json
</proof_of_spec>
