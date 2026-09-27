# 0.6.2_AE_PartnerETL~S -- 2026-09-27 1745-1910Z -- IRPT_BCKEND.TO-IB-s158

## The COT Black Diamond session auto-login succeeds again; the per-day cause does not survive
**archetype:** DIAGNOSE

Row `IRPT_BCKEND-S158`, cell `IB-sr-1`, round 19, `<risk>WORLD</risk>`, issued by `2.0.0_SA_COO~P`.

### Outcome

The session refresh is live and the whole COT chain has run green for the first time since 09-24.
`blackdiamond/cot/session` AWSCURRENT moved from `e9259045-d182-42e9-ac0c-e03c090c9d8c`
(2026-09-16T11:33:35.346Z, 11 days stale) to `9da4e781-7f11-4cf0-b2dd-2980e56db1db`
(2026-09-27T18:42:27.771Z). Reaching that Success released the chain the session gates:
`opal-cot-bronze-run` (590ed628) Success, `opal-cot-silver-run` (907f9f8e) Success,
`opal-cot-gold-run` (4fad5c7a) Success rc 0.

**AC2 MET, AC3 MET, AC1 REFUSED AS WRITTEN.** AC1 asks for the cause per failed day from the box's own
log. Those logs do not exist on any carrier, and the failure did not reproduce once the fix was live, so
there is no failing line to quote. The test was NOT weakened to pass: every `failed_days` row carries an
ABSENT cause, so the order's own AC1 invocation prints `MISSING`, which is the true answer.

### What was actually wrong, and what was not

MEASURED: `ssm.tf:49` ran `set -e`; `:65` ran the wrapper bare. A non-zero wrapper exit killed the shell
AT that line, so `EXIT_CODE=$?`, `tail -25` and the `aws s3 cp` were UNREACHABLE. `EXIT_CODE=$?` was dead
code. The document still reported Failed rc 1, which is why the failure was visible as a status and
invisible as a reason. The live document was byte-identical to repo HEAD at 876 bytes before the change,
so this was a defect in the build input, not drift away from it.

NOT MEASURED, and deliberately not asserted: the proximate login failure on each of 09-24..09-27. The
cold-start hypothesis is plausible -- each failure ran on a box `cot-bd-session-trigger` had started
seconds earlier (StartInstances 11:30:16Z, command requested 11:30:32Z) while my run had a box warm for
~25 minutes -- but testing it needs a box STOP, which CLAUDE.md puts behind human confirmation. Not asked
as a blocking question: tomorrow's `cron(30 7) America/New_York` run IS that cold-boot test and it now
runs with the log-on-failure document in place, so the evidence arrives without spending Andrew's word.

### The premise that failed

The order's build step 1 asserts "the box keeps `/tmp/cot-session-autologin-*.log`". It does not. `/tmp`
on `i-0643a5bee8a8feabf` is **tmpfs** (`findmnt /tmp` -> `tmpfs tmpfs rw,nosuid,nodev,seclabel`;
`df -h /tmp` -> `3.9G 0 3.9G 0%`), the trigger Lambda starts the box per run, and
`ec2-auto-shutdown-enforcer` stops it at `IDLE_CEILING_HOURS=3.0`. Every session-fetch log dies within
hours of being written. Absence proven on THREE carriers with printed denominators, plus a positive
control so the zero discriminates:

| carrier | denominator | result |
|---|---|---|
| box `/tmp` | 0 of `/tmp/cot-session-autologin-*.log`; 0 of `/tmp/*.log` | EMPTY (tmpfs) |
| `s3://opal-data-cot/logs/cot-exporter/session-fetch/` | 12 objects, newest `20260916-113031` | nothing for 09-24..09-27; the 09-16 object is the POSITIVE CONTROL that the upload works on a Success |
| box persistent SSM orchestration dirs | 42 dirs, all 4 failed command ids present | stdout AND stderr EMPTY in 4 of 4 |

Fourth carrier ruled out rather than left as a maybe: `bd_49f_auto_login.js:434` gates screenshots behind
`BD_DEBUG_SHOTS=1`; `grep -c BD_DEBUG_SHOTS` on the box's `secret-ids.env` returns 0.

### The change

`infra/aws/terraform/cot-pipeline/ssm.tf` @`de68b15717`; document version 5 applied
2026-09-27T18:37:47.998Z; targeted plan 0 add / 1 change / 0 destroy; `safe-apply` with comp-tagauthz
PASSED and tombstone CLEAN, zero override.

```
EXIT_CODE=0
./run-bd-auto-login.sh > $LOG_FILE 2>&1 || EXIT_CODE=$?
tail -25 $LOG_FILE || true
aws s3 cp $LOG_FILE s3://opal-data-cot/logs/cot-exporter/session-fetch/$(basename $LOG_FILE) || true
exit $EXIT_CODE
```

`|| EXIT_CODE=$?` keeps the failure inside a `||` list, which `set -e` does not act on, so the captured
code survives to the final `exit`. `tail` gained `|| true` so a missing log cannot re-abort before the
upload -- the same class of bug being fixed. Blast radius checked against the LIVE consumer, not assumed:
`aws events describe-rule cot-session-complete` returns pattern
`{document-name:[opal-cot-bd-session-fetch], status:[Success]}` -> `cot-bd-session-trigger`. Name
unchanged and the step still exits non-zero on failure, so that rule still fires on Success only.

**The failure branch is NOT yet exercised.** The upload leg is proven on the Success branch only
(`cot-session-autologin-20260927-184053.log`, 1172 B). ABSENT is not EXERCISED-AGAINST; the next failed
run is what proves it end to end.

### Surprise rows

The order prescribes id `IRPT_BCKEND-S158-S<k>`, which the gate's own schema REFUSES
(`investigation_item.schema.json` pins `^[A-Z0-9_]+-(Z-)?(W[0-9]+-|C-)?S[0-9]+$`). Used the channel's
documented seat grammar instead and flagged it for the issuer.

- **S164** -- the tmpfs premise; OBSERVATION, INERT, GRADUATED into this order's own fix.
- **S165** -- the cot box carries NO in-run login retry. `/opt/bd-cot-auto-login/secret-ids.env`
  (md5 `9b55e03c`, 1200 B) sets neither `BD_MAX_LOGIN_ATTEMPTS` nor `BD_LOGIN_BACKOFF_MS`; the repo copy
  (md5 `3c429837`, 1660 B) sets both and marks them CTO-gated. One transient failure is terminal for the
  day and silent -- how a 1-day glitch became an 11-day-stale session. ARMED, `disarm_owner`
  `1.0.0_SA_CTO`. Named, NOT remediated: `secret-ids.env` is in my grant but the retry needs the newer
  `.js`, which is not, and env vars the running `28dd27a0` ignores are inert at best.
- **S166** -- the running login script has no build input in the cot tree.
  `infra/aws/ec2/bd-cot-auto-login/` holds only the wrapper and env file; box `bd_49f_auto_login.js`
  `28dd27a0` (35049 B) vs repo 49F copy `15fd5ef9` (46900 B). The box DOES match the hash
  `secret-ids.env` itself declares canonical, so a versioning gap, not proven drift. ARMED.

### Deployed-bytes audit (rule 22a -- md5 of the RUNNING path, never by filename)

| asset | box | repo | verdict |
|---|---|---|---|
| `run-bd-auto-login.sh` | `a10ac98ada74e0539b987cb30c8fd979` | same | MATCH |
| `secret-ids.env` | `9b55e03c...` (1200 B) | `3c429837...` (1660 B) | DIFFER -> S165 |
| `bd_49f_auto_login.js` | `28dd27a0...` (35049 B) | `15fd5ef9...` (46900 B) | DIFFER -> S166 |

### Status

TO left `pending`, NOT flipped to `complete`: AC1 is FAIL. `proof-of-spec-check` **VALID (rc=0)** on
`IBS158-AC1,IBS158-AC2,IBS158-AC3` -- 3/3 criteria carry a cell_ref, 1/1 cell resolves, 3/3 recorded
invocations match the TO verbatim, 3/3 surprises resolve to channel rows. Deploy ledger
`irpt-bcknd-s158-cot-session-autologin` CLOSED, all 5 legs proven (L4 closed as VACATED: no act, nothing
landed on the box). The COO owns the re-cut or a `superseded` disposition.

### Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-blast` | `comp-blast opal-cot-bd-session-fetch` | Rule-20 graph read before the infra change, QUERY not rebuild; provenance read (projection built 2026-09-27T12:17:16Z, 28526 nodes / 61180 edges). `PRESENT_WITH_ZERO_RESULTS` and it says so itself -- "no EXTRACTED edge -- NOT provably zero" -- so it did NOT clear the blast radius and was not treated as if it had. The real control was the live `describe-rule`. The pre-commit risk reflex also could not clear the diff: danger map 73.3h STALE, `ANSWER STATE: PARTIAL_OR_BLIND`. |
| `comp-read` | `.tools/safe-commit.sh --for "<only the paths after -- or the whole index>"`; `bd_49f_auto_login.js --enumerate 'screenshot\|trace\|s3://\|window_seconds'` | Decided a lane question and closed a carrier. The safe-commit read found `git commit --only` at :1078 plus its lock, which established that a shared-tree commit cannot sweep another seat's staged files -- the index held another seat's staged `INVESTIGATION_v1.md` at that moment. The `.js` enumerate (11 hits / 604 lines) found the S3 screenshot uploader and, decisively, that :434 gates it behind `BD_DEBUG_SHOTS=1`. |
| `comp-find` | `'screenshot\|trace\.zip\|putObject' --files --limit 25 -- infra/aws/ec2/`; `'proof_of_spec' --files -- org/standards/` | Located the canonical login script off a printed denominator (343 hits / 464 files scanned; 148 ephemeral-floor and 124 binary declared unsearched) -- which is how the cot tree's MISSING `.js` became visible (S166). FAILURE MODE: an unscoped whole-repo census for the instance id blew the 120s foreground budget and had to be backgrounded; a pathspec made it answer in seconds. |
| live scheduler / Lambda reads | `aws scheduler get-schedule --name cot-bd-session-daily-et`; `aws lambda get-function-configuration --function-name ec2-auto-shutdown-enforcer` | Established the operating envelope BEFORE acting. The enforcer read (`MAX_RUNTIME_HOURS=0`, `IDLE_CEILING_HOURS=3.0`, `IDLE_CPU_THRESHOLD=1.0`) proved a box started for diagnosis would not be stopped out from under the work, and is half the mechanism behind the tmpfs finding. |
| `deploy_ledger.py` | `open` (5 legs, 6h window); `close-leg` x5; `close` | The complete manifest declared at deploy-START, before the first live act, so the leg that turned out inapplicable (L4) had to be dispositioned explicitly instead of forgotten. It also printed the required commit pathspec for its own sentinel pair, which kept the OPEN state from being destroyed by the shared-tree commit. |
| `proof-of-spec-check.py` | `<instance> IBS158-AC1,IBS158-AC2,IBS158-AC3` | The authority, run BEFORE any flip. A bare first invocation graded the wrong object (INVALID, 13 schema violations), which forced reading a known-valid instance rather than inventing the shape. Then caught two real defects: `decomp_ref.owned_cells` is not a property, and my AC3 `invocation` had a second command appended -- the recorded invocation must be the criterion's VERBATIM, with extra legs in `output_evidence`. Also surfaced that the TO lives in `task-orders/` while discovery globs `*/task_orders/*.md`, so an explicit `decomp_ref.to_ref` is required for alignment to resolve at all. |
| comp-tool rail | 3 census-into-pager pipes | GATED THREE TIMES, every one correct -- my own habit of reaching for `head`/`tail` on a census tool, which erases the denominator the tool exists to print. Re-run with native `--limit`/`--files`. The whole-call abort did not bite because each gated read was its own call. |

### What I did not do

- Did not run `./run-bd-auto-login.sh` directly on the box. It was the fastest route to a log and is
  FORBIDDEN: vendor sign-in only through the document (CTO 101946, 101977). Every sign-in this session
  went through `opal-cot-bd-session-fetch` via its own trigger Lambda.
- Did not stop the box to force a cold-boot reproduction (human confirmation required).
- Did not deploy the retry env vars, and did not touch the `.js` versioning gap. Both are named as ARMED
  rows with `disarm_owner 1.0.0_SA_CTO`.
