# CTO Session — Compiler Toolchain Round 2 (Incident-Driven)

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-14
**Project:** Cross-project infrastructure (compiler tools)

---

## Objective

Analyzed 2 weeks of session logs (2026-04-01 to 2026-04-14) to identify bugs, errors,
and manual workarounds that could be caught by compiler tools. Designed and built 5 new
capabilities based on the root causes found.

---

## Root Cause Analysis

27 incidents extracted from logs. Three dominant root cause categories:

**Category 1: "No crash" ≠ "correct output" (4 critical production incidents)**
Every data bug had a defensive guard that swallowed failure silently:
- D_00: `if 'client_city' in adim` → skipped → geo_drill absent → state drill broken
- D_02: `if split_col in snap_latest.columns` → SPLIT_COLS not loaded → fee_earning_aua = $0
- B_00: accepted sparse canonical_prices → Easter $1.6B→$100M AUA collapse
- build_canonical_prices_v2: no post-step declared → inject_scoped_overrides not called → $22M phantom

**Category 2: Pipeline post-step dependencies never declared**
build_canonical_prices_v2 + inject_scoped_overrides have an implicit ordering constraint
that was never encoded anywhere. Breaking it caused a $22M phantom value incident.

**Category 3: IAM permission cascades not modeled**
bd-exporter-ec2-role lacked s3:DeleteObject. Gold runner watchdog silently failed to
delete the shutdown marker, looped for 57+ extra minutes per cycle. No tool connected
"script calls s3.delete_object" to "role doesn't grant s3:DeleteObject."

Plus: CloudFront custom_error_response blocks intercept 403s from Lambda auth denials,
returning HTML. comp-routes behaviors didn't show this, requiring manual TF reading.

---

## Implementations

### Fix 1: comp-pipescript io COLUMN GAPS (extract_pipeline.py + pipeline_cli.py)

Added `_extract_column_gaps(py_file)` — static analysis that:
- Parses every `_load_parquet(KEY, columns=[...])` call (including pool.submit pattern)
- Finds all column accesses (bracket, attribute, .get()) on the returned variable
- Flags columns accessed but NOT in the columns= list

Output in `comp-pipescript io`:
```
  COLUMN GAPS (1) -- columns accessed but not in _load_parquet columns= list:
    !! adim.client_city
       accessed at line 956, not in _load_parquet(ACCOUNTS_DIMENSION, columns=[...]) at line 886
       FIX: add 'client_city' to the columns= list at line 886
```

Would have caught BOTH geo_drill and fee_earning_aua incidents at commit time.

### Fix 2: comp-pipescript postdeps (pipeline_cli.py + gold_pipeline_deps.yaml)

New `postdeps` subcommand reads `data/black_diamond/scripts/gold/gold_pipeline_deps.yaml`.
Initial config declares:
- build_canonical_prices_v2.py → BLOCKING post-step: inject_scoped_overrides.py (with incident note)
- B_00 precondition: canonical_prices.parquet must exist + pricing coverage > 80%
- D_01 / D_00b precondition: dim_advisor_office.csv must be on S3

Smoke test confirms correct output with incident annotation for the Apr 6 override wipe.

### Fix 3: comp-validate (extract_validate.py + validate_cli.py + .tools/comp-validate)

New tool. Checks declared invariants against a local artifact before S3 upload.
Config at `data/black_diamond/scripts/gold/gold_validate_config.yaml`.
Initial invariants from 4 production incidents:

| Script | Check | Incident |
|--------|-------|---------|
| D_00 | geo_drill key present (ERROR) | geo_drill absent → state drill broken |
| D_00 | geo AUA nonzero (ERROR) | Easter pricing dropout |
| D_04 | leaderboard count >= 5 (ERROR) | gold run failure detection |
| D_04 | fee_paying.aua > 0 for large advisors (ERROR) | SPLIT_COLS not loaded |
| D_01 | views.geo + views.adv present (ERROR) | aggregation failure detection |
| D_01 | views.ofc present (WARN) | ADVI_OFFICE W1 deployment check |

Exit code 1 if any ERROR fails — can gate S3 upload in build-and-upload.sh.
Supports: key_present, count_min, field_nonzero, sum_approx, no_null_numeric, threshold_pct.

Smoke test:
```
comp-validate --list  -> 4 scripts, 10 checks loaded correctly
```

### Fix 4: comp-routes custom_error_response (extract_routes.py + routes_cli.py)

Added `CustomErrorResponse` dataclass and parser for `custom_error_response {}` blocks
in cloudfront-distribution.tf. `comp-routes behaviors` now shows:
```
CUSTOM ERROR RESPONSES (2):
  !! These intercept HTTP status codes -- Lambda/S3 errors may be hidden from browser
  HTTP 403 -> 200 /index.html  (ttl: 0s)
  !! WARN: Lambda 403 auth-denials will be swallowed -- browser gets 200 /index.html not the Lambda error
  HTTP 404 -> 200 /index.html  (ttl: 0s)
```

`comp-routes auth-map` now warns when 401/403 codes are intercepted with fix guidance.

Would have caught the Lambda 403→HTML incident (DE~A reported HTML, COO had to manually read TF).

### Fix 5: comp-iam (extract_iam.py + iam_cli.py + .tools/comp-iam)

New tool. Scans Lambda/EC2 sources for boto3/AWS CLI operations, cross-references against
Terraform IAM policy documents, flags permission gaps.

Output format:
```
PERMISSION GAPS (1 found)
  bd-gold-runner (EC2)  (role: bd-exporter-ec2-role)
    !! MISSING: s3:DeleteObject
       Called via: s3.delete_object at data/black_diamond/.../shutdown.py:847
       Fix: add 's3:DeleteObject' to bd-exporter-ec2-role policy in iam.tf
```

Covers: s3:GetObject/PutObject/DeleteObject/ListBucket/CopyObject, ssm:SendCommand/GetParameter,
dynamodb:PutItem/GetItem/Query, and AWS CLI (aws s3 rm, aws s3 cp, aws ssm send-command).
Sources: lambda-source-map.json + infra/aws/terraform/*/iam.tf + gold/*.py.

---

## Smoke Tests

| Test | Command | Result |
|------|---------|--------|
| py_compile all 6 modules | python -m py_compile ... | ALL OK |
| column gap (no false positives on D_00) | comp-pipescript io D_00 --no-portal | PASS — no spurious gaps |
| postdeps full output | comp-pipescript postdeps | PASS — 4 entries, incident annotations shown |
| validate list | comp-validate --list | PASS — 4 scripts, 10 checks |
| custom_error_response | comp-routes behaviors | PASS — 2 CF error rules, 403 WARN shown |

---

## Files Created / Modified

Modified:
- `org/modules/graph/extract_pipeline.py` — added `_extract_column_gaps()`
- `org/modules/graph/pipeline_cli.py` — column gaps in cmd_io + cmd_postdeps + postdeps subparser
- `org/modules/graph/extract_routes.py` — CustomErrorResponse dataclass + parser + RoutingTable field
- `org/modules/graph/routes_cli.py` — behaviors + auth-map + stats updated
- `org/modules/graph/comp-tools.yaml` — comp-validate, comp-iam, comp-tooltip, postdeps, column gap docs

Created:
- `org/modules/graph/extract_validate.py` — invariant check engine
- `org/modules/graph/validate_cli.py` — comp-validate CLI
- `org/modules/graph/extract_iam.py` — IAM op scraper + TF parser
- `org/modules/graph/iam_cli.py` — comp-iam CLI
- `.tools/comp-validate` — shell wrapper
- `.tools/comp-iam` — shell wrapper
- `data/black_diamond/scripts/gold/gold_validate_config.yaml` — initial invariant config
- `data/black_diamond/scripts/gold/gold_pipeline_deps.yaml` — post-step dependency config
- `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-14/compiler_toolchain_improvements_round2.md` — this file

---

## Compiler Tools (Meta)

| Tool | Command | Result |
|------|---------|--------|
| py_compile gate | python -m py_compile on all 6 modules | PASS |
| comp-pipescript io smoke | io D_00 --no-portal | PASS |
| comp-pipescript postdeps | postdeps (all) | PASS |
| comp-validate list | validate_cli.py --list | PASS |
| comp-routes behaviors | routes_cli.py behaviors | PASS (2 custom_error_responses shown) |

---

## Open Items

- comp-diff --staged in portal submodule: not yet investigated (deferred from round 1)
- comp-iam full validation pending final agent completion
- comp-validate gold_validate_config.yaml: additional scripts (D_02, D_00b, B_00 coverage check) can be added as DS identifies invariants during session work
