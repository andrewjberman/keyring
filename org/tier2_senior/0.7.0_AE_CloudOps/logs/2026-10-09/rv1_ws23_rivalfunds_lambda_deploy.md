# 0.7.0_AE_CloudOps~RV1 -- ETFS_RIVALS WS2/WS3: the rivalfunds Lambda deploy at pin b48273e3d0

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Session: 2026-10-09 ~14:23Z - 15:0xZ. Lane `0.7.0_AE_CloudOps~RV1`, box dell1, branch `box/dell1`, workspace root
`C:/dev/ajb_workspace`. First log for this lane; window is the whole session.

## What was done

Startup (`/watcher`, then `org/XXX.md` 1b A-F), then the one task order this lane was seated for, start to finish:
`ETFS_RIVALS.TO-APPLY-WS2WS3.rivalfunds-lambda-deploy-dell1` -- the code-only deploy of the five rivalfunds
Lambdas at pin `b48273e3d0`, under two signed never-widen halves (COO @`683b767406`, CTO @`20bd5c33db`), both read
in full before any act. Steps 1-8 ran in order; nothing was skipped and nothing was applied outside the graded plan.

**THE DEPLOY IS LIVE AND VERIFIED.** 14:48:39Z-14:49:03Z.

## Deployment Sequence

| # | act | instrument | result |
|---|---|---|---|
| 1 | STOP 1, pin | `git worktree add --detach C:/tmp/rv-ws23-dell1 b48273e3d0` | HEAD `b48273e3d0a9083d85b8a6f05cfd4c828d62091c`, 0 porcelain lines |
| 1a | condition 7 reproduced | `git diff --stat` both pins | TF root + lambda dir: 0 files; seven STAGED paths: 19 files +5027 -95 (the COO half's number exactly) |
| 1b | pre-package control | raw bytes vs `git cat-file blob` | 82 of 82 identical, 0 missing, 0 different; negative control live |
| 2 | package then plan | `rivalfunds_package.py`, then `plan -out C:/tmp/rv_apply_ws23.tfplan` | 5 staged; `Plan: 0 to add, 5 to change, 0 to destroy` |
| 3 | STOP 3, per attribute | `terraform show -json` + own grader | BRANCH A, 0 failures (see Verification) |
| 4 | snapshot | `coverage_snapshot.py take ... 2026-10-09 20` | `SNAPSHOT: 19 of 20 keys saved`; manifest committed @`a66006c2e4` |
| 5 | env key sets BEFORE | `get_function_configuration`, names only | 5 of 5 read |
| 6 | windows + ledger | clock read; `deploy_ledger.py open` | 14:47:26Z, outside both brackets, 1197 min to deadline; slug `etfs-rivalfunds-ws23-dell1-20261009`, 2 legs |
| 7 | apply | `.tools/safe-apply.sh -chdir=<tree> apply <saved planfile>` | `Apply complete! Resources: 0 added, 5 changed, 0 destroyed`, rc=0 |
| 8 | AFTER + AC1 + re-plan | live reads; `ws23_deploy_check.py`; `plan -detailed-exitcode` | all pass (see Verification) |

## Verification (actual output)

STOP 3, graded per attribute and not from the summary line:
```
resource_changes in the plan: 45
  actions ['no-op']: 40
  actions ['update']: 5
SUMMARY GRADED FROM THE CHANGE SET: 0 to add, 5 to change, 0 to destroy
  [each of 5] attributes DIFFERENT: ['last_modified', 'source_code_hash']
  [each of 5] memory_size before=3008 after=3008
forbidden-attribute denominator checked per mover: 20 names
environment before==after on all movers: True
STOP 3 RESULT: BRANCH A 0 failures
```
AC1 and the re-plan:
```
WS23 DEPLOY RESULT: PASS 0 failures
No changes. Your infrastructure matches the configuration.   (-detailed-exitcode rc=0)
APPLIED==GRADED: 5 of 5    (live CodeSha256 == the plan's own declared after-hash)
```
BEFORE -> AFTER per function, all five `State Active` / `LastUpdateStatus Successful` / `MemorySize 3008`:
daily `6Z77vxU0`->`Gn5el43F` 14:48:51Z; fetch-holdings `cXi5kINK`->`co0WQL/I` 14:49:03Z; build-silver
`DLqulrgw`->`rl8rvn08` 14:48:45Z; canonical-shape `5ZTAg5Km`->`dgF/rCz3` 14:48:39Z; publish-page
`/ZD6nH7g`->`5R61Tu7/` 14:48:57Z. Environment key sets identical before and after (daily
`['RIVALFUNDS_AI_ENABLE','RIVALFUNDS_OPENAI_SECRET']`, the other four `[]`), corroborated on the declarative plane:
`generated.auto.tfvars.json` carries identical key sets, memory and timeouts at BOTH pins.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `--files 'STALE-BASELINE\|audit-archive-invoker' ... --limit 12` | PASS after a WARN | first run used a BRE-escaped pipe; the tool WARNED that `\|` is literal and that a 0 may be the pattern. Corrected to a bare pipe: 0 hits became **13 hits across 2361 files**. The warning prevented a false absence. |
| rail (`comp_rail_direct.py`) | two denials | PASS (worked as designed) | F1 denied a blind recursive grep and named the replacement; F4 then denied `comp-find ... \| tail -12` because a pipe can cut the denominator line. Re-ran with `--limit`. Both denials were correct and cost one round trip each. |
| `deploy_ledger.py` | `open` / `close-leg` / `hold` / `list` | PASS | L1 closed with proof; entry HELD on a named external gate so the issuer's open L2 reads KNOWN-HELD rather than half-landed RED. |
| `safe-apply.sh` | `-chdir=<tree> apply <saved planfile>` | PASS | `comp-tagauthz` gate PASSED (0 of 0 candidates overwrite an access-granting tag); `tombstone-gate` CLEAN (0 creates vs 7 tombstones). HALTGT passed silently and is NOT cited as evidence (ADHC_HALTGT). |
| `safe-commit.sh` | 3 commits | PASS (1 correct refusal) | owned-paths clause 4 refused `deliverables/0.7.0_AE_CloudOps~DELL1/` for this lane; re-landed under `~RV1`. |
| `surprise-row-gate.py` | at commit | PASS | `1 new row(s) of 23 total checked`, all step-7/step-10 fields present. |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~RV1` | PASS | `total=1 scanned=5337` -- the one order, left `pending` for the issuer to close. |
| `audit-archive-invoker.py` | startup A.2 | WARN | STALE-BASELINE (1210.6h) plus NON-APPEND-EDIT / ERROR-FAILCLOSED rows. Already OWNED and recorded (LD-0553/LD-0554, `0.0.0_AB_MSTR` under the CTO's D0-row-12 ruling), so NOT re-filed; `mkdir org/audit/archive/<device>/` is expressly banned. |
| PATH shims | startup A.3 | PASS | 101 of 102 comp-tools resolve bare; a forwarder RAN. |

**What worked:** grading the plan per attribute from `show -json` rather than trusting `Plan: 0 to add, 5 to
change`; packaging before planning (`archive_file` zips at plan time); applying the SAVED planfile so applied bytes
are graded bytes; checking live hashes against the plan's own declared after-values as a second, AC1-independent
oracle.
**What failed:** nothing in the deploy. Two rail denials and one owned-paths refusal, all correct.
**Gap found:** `coverage_snapshot.py compare` prints `was absent, now PRESENT` for a key that had no pre-image and
does NOT count it as a stop line -- so CTO condition 8's "each of the 20 keys is printed as unchanged or changed"
is unmeetable for `date=2026-10-09`. Filed as row `ETFS_RIVALS-D1-S12`, not patched (the script is the issuer's).

## Files Modified

See commit messages: `a66006c2e4`, `ba032e078a`, `8ad8b51083`. Beyond those: nothing. No `.py` in the repo was
edited (the three helper scripts I wrote live in the session scratchpad, outside the checkout).

## MCP traffic

5 messages total. Significant: msg 2546 IN, the GO (acked READ); msg 2554 OUT, my tc-1 state ask to
`0.0.0_AB_MSTR~DELL1`; msg 2564 IN, the issuer's PROCEED citing AMENDMENT 2 @`6c73509684` (acked READ, bytes
verified at the pin); the DONE report to `2.0.0_SA_COO~V1` (1068 B, verified by `wc -c`); an owner-notice to
`2.0.0_SA_COO~S1` (890 B) about a `deploy-stale-s3` finding my ledger close triggered on ITS surface.

## Blockers

None. Nothing this lane owns is blocked. Two items are open and owned elsewhere, both named with their owner:
- Ledger L2 + AC2 -- `2.0.0_SA_COO~V1`, gated on its 2026-10-10 11:00Z chain and 13:00Z sweep reads. Held, dated,
  not stranded.
- `deploy_stale_20261009T144908Z.json` / `...150211Z.json` (same class, same script) -- `2.0.0_SA_COO~S1`,
  `data/assets/scripts/silver/rebalancer_schemas.py` STALE/MISSING on S3. Out of my lane; owner notified; I did not
  act and did not re-file.

## Current State

Written for a reader with zero prior context.

- Lane `0.7.0_AE_CloudOps~RV1` LIVE on dell1, PID 31808, registered, broker summary current. One inbox watcher,
  Monitor task `b3u6eoh4m` (re-armed at the 30-minute expiry, same turn, one call). ZERO crons (`CronList`: "No
  scheduled jobs"); no row in `org/ref/LIVE_ARMS.md`, so this lane arms nothing.
- **Live in the world:** the five rivalfunds Lambdas (`etfs-rivalfunds-daily-lambda`,
  `etfs-rivalfunds-fetch-holdings-lambda`, `rivalfunds-build-silver-lambda`,
  `rivalfunds-build-canonical-shape-lambda`, `rivalfunds-publish-page-lambda`) now run the `b48273e3d0` package.
  Code only -- no IAM, schedule, memory, timeout or environment change; no function invoked, no test event, no S3
  object written, no environment variable set.
- **Terraform:** root `infra/aws/terraform/etfs-rivalfunds/`, backend `s3://opal-313476888478-terraform-state`
  key `etfs-rivalfunds/tfstate`. A re-plan at the pin reads no changes.
- **Trees:** `C:/tmp/rv-ws23-dell1` is the deploy tree (detached at `b48273e3d0`, built zips under
  `.runtime/rivalfunds-build/zips/`) -- KEEP, AC1 reads those zips. `C:/tmp/rv-r28-dell1` is the ROLLBACK tree,
  still HEAD `39889dd4d7`, 0 porcelain lines, five rollback zips intact -- read-only, do not change.
  `C:/tmp/rv-ws23-covsnap` holds 19 parquet pre-images plus `manifest.json` -- KEEP until L2 closes.
- **Rollback path:** re-apply the `39889dd4d7` package from `C:/tmp/rv-r28-dell1` through `safe-apply`; for G2,
  put back the snapshot bytes per key (no pre-image exists for `date=2026-10-09`).
- **Ledger:** `org/critical_paths/change_management/20261009T1447Z_etfs-rivalfunds-ws23-dell1-20261009_deploy_completion.md`,
  L1 CLOSED with proof, L2 OPEN and HELD (`HELD-SOVEREIGN-GATED`, gate=external).
- **Order:** `org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-APPLY-WS2WS3.rivalfunds-lambda-deploy-dell1.md`,
  report section written and committed @`8ad8b51083`, `<status>` deliberately left `pending` for the issuer to
  close (the aw-1 model's convention; AC2 is a judgment criterion and is never self-graded).
- **Push state, MEASURED:** LOCAL @`8ad8b51083`; `origin/box/dell1` read `593af697c3` by `git ls-remote` at
  14:5xZ. This box does not push `box/dell1` -- under `org/XXX.md`'s shared-branch law that branch is pushed only
  by an MSTR or the box's scheduled `box-sync`, so these three commits travel by `box-sync`.

## Next Steps

1. `[2.0.0_SA_COO~V1]` Reads the 2026-10-10 11:00Z chain and 13:00Z sweep against the writers table, grades AC2,
   runs `coverage_snapshot.py compare C:/tmp/rv-ws23-covsnap 10` for CTO condition 8, and closes L2. Grade 19 keys
   unchanged-or-changed and `date=2026-10-09` separately as created-or-still-absent (row `ETFS_RIVALS-D1-S12`).
   A changed key OUTSIDE the last 10 trading days is a STOP and a same-day restore from the snapshot.
2. `[2.0.0_SA_COO~V1]` Closes the order's `<status>`, and notes the step-4 manifest path landed under
   `deliverables/0.7.0_AE_CloudOps~RV1/` because owned-paths refused `~DELL1` for this lane.
3. `[2.0.0_SA_COO~S1]` Owns the `deploy-stale-s3` findings on `rebalancer_schemas.py`; notified, untouched here.
4. `[0.0.0_AB_MSTR]` Owns the audit-archive STALE-BASELINE class for dell1 per LD-0553/LD-0554; surfaced only.
5. `[0.7.0_AE_CloudOps~RV1]` Event-driven hold: act on the next `[INBOX]` event the same turn; re-arm the Monitor
   on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load. Keep all three `C:/tmp/rv-*` trees and the
   covsnap directory until L2 closes.
