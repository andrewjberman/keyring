# H03 2a infra apply LANDED: the memory bump was load-bearing, and the census that nearly lied -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Date:** 2026-09-24, 04:25Z-05:25Z (00:25-01:25 local, UTC-4)
**Task Order:** NONE DISPATCHED. Acted on the MANDATE LETTER at `f47642479c`
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/AE_CLOUDOPS_H03_2A_APPLY.md`),
authored by `1.0.0_SA_CTO~Z`, routed by `0.0.0_AB_MSTR~Z` under the RK122 precedent, addressed to this
lane. Letter bytes at the pin equal HEAD bytes (6648), so the artifact read is the artifact cited.
**Status:** APPLY COMPLETE AND VERIFIED. Ledger leg `tf` CLOSED. Commit `6fdfe5b25e` LOCAL.

## Objective

Startup (`/watcher` + `org/XXX.md` Step 1b A-F), then the H03 2a infra apply: land code, packaging and
configuration on `amgt-resapp-chatter-axis` with `CHATTER_AXIS_SOURCE=legacy`, without publishing,
without touching the schedule, and without altering the apply to satisfy a stale proof clause.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-find` (content, `--all`) | locate orders naming this seat | PARTIAL -- 502 hits / 72,198 files, 424 DOC band; too broad, fell back to a scoped `<issued_to>` parse |
| `comp-read --enumerate` | AE rows in `org/XXX.md` | PASS -- 3 hits / 869 lines, WARN every hit a fragment; settled that NO Step 1b-F loop row exists for this seat |
| `comp-which` (A.3 exercise) | prove a forwarder RAN, not just resolved | PASS -- 104 of 104 resolve bare, forwarder executed |
| comp-tool rail (`comp-tool-hud.sh`) | gate raw searches | FIRED TWICE, CORRECTLY -- once on a `| tail` after `comp-find`, once on a `.tf` grep |
| `owned-paths-validate.py --check-agent` | path authority, both arms | PASS -- rc=0 / 0 violations for `~A`; rc=1 / 5 VIOLATIONs for `2.0.0_SA_COO~Y` |
| `deploy_ledger.py close-leg` | close leg `tf` | PASS -- "OK: leg tf closed. Remaining open: ['daily', 'served']" |
| `commit-gate.sh` | Rule 14 | PASS -- 3 of 3 py, then 5 of 7 at commit |
| `safe-apply.sh` | Rule 18 gated apply | PASS -- tagauthz gate PASSED, tombstone-gate CLEAN, apply complete |

**What worked:** the NEGATIVE CONTROL discipline, three times, and each one was load-bearing rather than
ceremonial. Pulling the REFUSED patch `@442e839d89` beside the authorized `@523f62b92e` proved the hash
DISCRIMINATES rather than merely agreeing. Feeding `owned-paths-validate` the builder's serial produced
rc=1 with five VIOLATION lines, which is the only thing separating a real pass from that tool's known
VACUOUS no-stdin rc=0. And the `--is-ancestor` push-state read carried a control commit, without which an
ON-ORIGIN and a broken ancestry test read identically.

**What failed -- all three were MY OWN instruments, and every one returned a clean, plausible result:**
1. **`git worktree list --porcelain | awk '/^worktree /{print $2}'` SPLIT ON WHITESPACE** and silently
   dropped 7 of 43 worktrees, **including the MAIN one** -- which was the only tree whose answer I needed.
   It printed `C:/Users/Opal` seven times and `fatal: not a git repository`, which reads like a broken
   worktree rather than a broken census. Had I not re-run it, I would have reported the H03 ledger ABSENT
   from the main tree with a confident denominator. Redone in python: 43 read, 0 failures, ledger found in 3.
2. **Native Windows python cannot open an MSYS `/tmp` path.** `aws ... > /tmp/h03_pol.json` succeeded
   (rc=0, `wc -c` = 3024) and `json.load(open('/tmp/h03_pol.json'))` raised FileNotFoundError on a file
   that demonstrably existed. Fixed by piping through `cat` instead of passing a path.
3. **`send_message` refused on `from_serial`/`to_serial`/`message`** -- the correct names are
   `from_agent`/`to_agent`/`body`. The tool now FAILS LOUD; it used to drop unknown params silently.

**Gap found:** the `/watcher` skill's PowerShell census regex `inbox-watch\.sh {serial} stream` read
`script rows: 0` for a LIVE watcher on this device, for the SECOND time (first surfaced by this lane
2026-09-23). The workspace path contains a space, so the Monitor command quotes the script path and a `"`
sits between `.sh` and the serial. The failure direction is the dangerous one: the skill's own text says
zero means NO WATCHER and instructs the seat to ARM, so the defect drives toward DOUBLE-ARMING -- the exact
orphan-theft condition that section exists to prevent. `inbox-watch\.sh"? {serial} stream` matches.
Confirmed live at pid 40776, then pid 51100 after the 30-minute expiry re-arm. Not edited by this seat.
**Also measured, contra both `org/XXX.md` and the skill: `/cygdrive/c` DOES NOT EXIST on this device.**
Both documents present `/c` and `/cygdrive/c` as co-mounted and instruct a `test -d /cygdrive/c` preference;
here that test is false and `/c` is the only mount.

## Deployment Sequence

1. Verified patch `@523f62b92e` = 41,525 b, sha256 `41c1a2ac...`; worktree and HEAD byte-identical. Pulled
   refused `@442e839d89` = 41,198 b, sha256 `4cffba6d...` as negative control. Read the VALUE directly:
   authorized `:121` `chatter_axis_source = "legacy"` vs refused `:117` `"gold"`.
2. `head-object` both S3 VersionIds; `get-function-configuration` pre-state. Rollback artifact confirmed
   byte-identical to the RUNNING `CodeSha256` -- the CVO claim re-derived on a second instrument.
3. `git apply` (5 files), `commit-gate.sh` 3 of 3 py clean.
4. `terraform init` (new module ref), `terraform plan -out`.
5. RAVC1 to CTO~Z / COO~Y / MSTR~Z with the plan diff.
6. `.tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply <plan>` -- Rule 18, never bare.
7. Post-apply verification, 0-diff plan, ONE `dry_run` invoke.
8. `deploy_ledger.py close-leg --leg-id tf`; `safe-commit.sh`; RAVC2.

**NOT in this act:** no pool write, no generation, no pointer move, no schedule change (the ENABLED
`cron(0 10 * * ? *)` stands), no portal, no vendor call, no egress off Opal infrastructure.

## Verification

```
Apply complete! Resources: 1 imported, 0 added, 3 changed, 0 destroyed.
```

```
get-function-configuration:
{ "sha": "Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=", "size": 55418293,
  "mem": 512, "to": 120, "env": { "CHATTER_AXIS_SOURCE": "legacy" },
  "rev": "2c917823-4409-4528-a8ca-aecdff3562df", "mod": "2026-09-24T05:09:00.000+0000" }
```

```
get-role-policy (live, parsed): statements: 4 | total resource/prefix entries: 21
chatter_daily occurrences: 2
   Resource   [ReadThePoolPrefixesTheProducerReads] arn:aws:s3:::opal-data-harvest/amgt/harvest/gold/chatter_daily/*
   s3:prefix  [ListOnlyThePoolPrefixesTheProducerReads] amgt/harvest/gold/chatter_daily/*
gold-but-NOT-chatter_daily entries: 0 (expect 0)
```

```
0-diff: terraform plan -detailed-exitcode -> "No changes. Your infrastructure matches the
configuration."  PLAN rc=0
```

```
dry_run invoke, RequestId 10fbaa9c-95be-4f4c-9a15-e5d9e15aa128, StatusCode 200, FunctionError null:
OK: chatter axis as_of=2026-09-24 source=legacy dry_run=True tickers_considered=191 rows_ranked=2
  rows_written=0 names_read=250 names_with_links=3
PRODUCT TRENDING_CHATTER state=COMPLETE rows_ranked=2 rows_written=0 pointer_written=False
  failed_marker_written=False reason_code=None
PRODUCT BREAKOUT_CHATTER state=EMPTY rows_ranked=0 rows_written=0 pointer_written=False
  failed_marker_written=False reason_code=None
REPORT Duration: 10362.44 ms  Memory Size: 512 MB  Max Memory Used: 112 MB  Init Duration: 102.28 ms
```

**THE MEASUREMENT THIS ACT PRODUCED: Max Memory Used 112 MB against a PRIOR CEILING OF 128 MB.** The
function was running at 87.5% of its limit. The 128 -> 512 resize was load-bearing, not cosmetic, and that
figure did not exist before this run. It is also the first target-runtime evidence that **Arrow 15.0.2
reads Arrow-24-written parquet** without error, which R-15/R-17 left REQUIRED.

## Decisions Made

1. **Did not reconcile the five stale proof clauses.** They were written for `gold`; the CTO half refused
   `gold`; under `legacy` they are FALSE BY CONSTRUCTION. Nothing was altered to make one pass.
2. **Did not treat the dry-run `pointer_written=False` as a contradiction.** A dry run writes nothing; the
   letter's `pointer_written=True` expectation is about the 10:00Z fire.
3. **Carried the output delta rather than acting on it.** The plan added five keys to the
   `scoped_amgt_route_keys` OUTPUT, which the letter's blast radius did not name. Surfaced in RAVC1 and
   RAVC2. `1.0.0_SA_CTO~Z` answered (msg 25267): N=1 writer, N=0 consumers over 72,224 files, plus TWO
   pre-existing negative controls (AMGT-rk-59 proof_of_spec `:74`, AMGT_EXPERIENCE C1_EXECUTION `:11`)
   dispositioning the same delta identically. **INSIDE the signed radius; the limit is that this covers
   those five keys and nothing else.**
4. **Took the audited `# rail-checked:` marker ONCE**, for the live `get-role-policy` read, because
   `comp-iam` models `(action)` and never `(action, resource)` and is explicitly a FLOOR -- it structurally
   cannot answer WHICH resource prefix was added, which is the never-widen question the letter names.
5. **Did not commit two pre-existing untracked files** (`20260904T*_bbgtml_*_deploy_completion.md`) that sat
   in `org/critical_paths/change_management/` at session start. Not mine.

## Files Modified

See commit message: `6fdfe5b25e` (7 files, 559 insertions, 60 deletions -- per-file detail is in the body).
Five are the letter's patch targets under `infra/aws/terraform/harvest/`; two are the ledger
(`.open_deploys/amgt-h03-leadpanel-y-20260924.json` + its `change_management` entry).

## Blockers

**None.** Nothing is owed by this seat and nothing is waiting on it.

## Current State

`amgt-resapp-chatter-axis` (us-east-1, 313476888478) now runs `CodeSha256`
`Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=` at 55,418,293 bytes, **512 MB / 120 s**, with
`CHATTER_AXIS_SOURCE=legacy`, RevisionId `2c917823-4409-4528-a8ca-aecdff3562df`, LastModified
2026-09-24T05:09:00Z. Code is served from
`s3://opal-313476888478-lambda-artifacts/harvest/amgt-resapp-chatter-axis.zip` VersionId
`lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9`. **ROLLBACK is VersionId `PUSLcUMaAwg.oPLW0ZdH6nO8t7ylo_eY`, 669,924 b,
content-sha256 `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`, verified byte-identical to what was running
before this apply.** The role policy `amgt-resapp-chatter-axis-lambda-policy` gained exactly one prefix,
`amgt/harvest/gold/chatter_daily/`, in the two read-scoped statements. The log group
`/aws/lambda/amgt-resapp-chatter-axis` is now Terraform-managed (tags only; `retention_in_days 0`
never-expire UNCHANGED). Terraform is 0-diff.

Ledger `amgt-h03-leadpanel-y-20260924`: `baseline`, `artifact`, `pair`, `tf` CLOSED; **`daily` and `served`
OPEN**. Window 12h from 2026-09-24T02:51:28Z. Read across ALL 43 live worktrees, found in 3.

Commit `6fdfe5b25e` is on local `CLOUD` and **LOCAL, not pushed** -- `origin/CLOUD` reads
`4359367feef887a11da92433e25fdc59e6c84920` by `ls-remote`, and `6fdfe5b25e` is NOT an ancestor of it while
control commit `f47642479c` IS, so the negative is a real read.

Separately: startup A.2 produced 14 audit-archive findings in classes OUTSIDE the two `org/XXX.md`
documents as known-owned. Five audit logs left this device in ONE window on 2026-09-11 (18 -> 13 files
between `sitez/2026-09-11T103259Z` and `T224403Z`; 7 later snapshots stable at 13). Content survives on the
laptop, one log still growing there (72 lines vs this device's last 29). Classified **EXPOSURE, not
incident**; surfaced to `1.0.0_SA_CTO~Z`, who accepted the classification. Two genuinely uncovered logs
(`org/commit-msg-ascii-override-audit.log`, `org/opal-ipblock-audit.log`, 0 of 49 snapshots on any device)
are parked behind `rv0057-f001`.

## Next Steps

1. **[SCHEDULED, no owner act]** The `cron(0 10 * * ? *)` fire at 10:00Z is the `daily` leg. Grade it
   against the letter's control: the 09-23 pointers (`20260923T100026Z-d09ee37a8f3b` /
   `20260923T100028Z-25147d66b259`) stay BYTE-IDENTICAL to `3.0.0_SA_CVO~Z`'s pre-apply pins @`2f4f39c66e`
   **WHILE** a fresh `#2026-09-24` `_CURRENT` appears with `row_count 2`. A fresh same-day `_CURRENT` is
   EXPECTED, not a regression.
2. **[`3.0.0_SA_CVO~Z`]** The `served` leg -- Lead Panel chatter route review and served-row reconciliation.
   E0 is separately owned.
3. **[`0.0.0_AB_MSTR~Z`]** The push. `6fdfe5b25e` is LOCAL; this seat commits and never pushes.
4. **[`1.0.0_SA_CTO~Z`]** 2a is explicitly NONPUBLISHING (R-19) and claims no acceptance id. It does NOT fix
   the chatter water -- 1,596 gold rows for six securities, 1,595 DENIED, replay resolving 0 of 191. That is
   `2b`, upstream, unowned, and at Andrew.
