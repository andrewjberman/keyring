# CLOSURE HANDOFF, written for a successor who was not here -- 0.7.0_AE_CloudOps

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

**Written:** 2026-08-30 ~18:30Z, on the Andrew-direct edict relayed by `1.0.0_SA_CTO` at 88950.
**This closes a CONTEXT, not any work.** Nothing below is cancelled, wound down, or narrowed. No
project is marked complete because of this document. Every open item stays open at its stated point.

**Companion:** the session log for this window is
`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-30/session_close_0303-1820Z.md` @`e5fd5a2ad1`.
That one is written for this fabric and assumes context. THIS one assumes none.

---

## 0. Who this seat is, in plain terms

`0.7.0_AE_CloudOps` -- the cloud-operations engineering seat on the laptop device. Base serial (no
`~lane` suffix). Its surfaces:

- **AWS infrastructure changes via Terraform**, always through `.tools/safe-apply.sh` (a wrapper
  that runs an authorization gate and an inbox checkpoint before the irreversible apply). A bare
  `terraform apply` is prohibited.
- **AWS Lambda function deploys.** Lambda code reaches AWS ONLY through Terraform. Never through
  `aws lambda update-function-code`.
- **CI tooling under `infra/aws/lambda/ci/`** -- the scripts that build Lambda zip packages, upload
  them to S3, and record which code version is deployed where.
- **EC2 batch-runner code deploys**, which go local -> S3 -> the instance pulls at run time. Code is
  never written directly onto a VM.

Working branch is `CLOUD`. Commits go through `.tools/safe-commit.sh` under the seat's own author
line. Pushes are NOT done by this seat -- an integrator seat (`0.0.0_AB_MSTR`) opens and closes
"integration windows" and pushes everything in range. So a commit sitting LOCAL is normal and not
an error; it rides the next window.

---

## 1. DONE -- closed and verified, with the pin and the instrument

### 1a. INF-ONEWRITER

**What it is in plain terms:** a Lambda function named `inf-silver-chain` was running code that had
not been rebuilt in 111 days, and nobody could tell, because no instrument compared the deployed
bytes to the source record. Separately, TWO different programs were writing the SAME output file
each day (a "billing" data table). The cell fixed both: redeploy the stale function, then retire
the second writer so exactly one program writes that file.

**DONE, both halves:**

- **The redeploy.** Applied 2026-08-30T09:54:24Z. Verified on the live function, not on the apply
  report: `CodeSha256 = y7hEGWshBrgT84AAiA+Pggod9XBy1fg8twnVTG1+8l8=` with
  `LastModified = 2026-08-30T09:54:24Z` (both together -- either alone can be a stale read). The
  deployed package was DOWNLOADED and all four declared source modules were confirmed byte-identical
  (after normalising line endings) to the committed source at pin
  `0ae699e57b4f689f3598d7e3c4607de7568d45e6`, AND confirmed to contain zero carriage-return bytes.
  Commit `71a3e7f839`.
- **The retirement.** The second writer was a step named `INF_API_SILVER_BILLING` inside a shell
  dispatch script, `data/inf/scripts/gold/orion-gold-dispatch.sh`. Removed from the chain that runs
  it (line 341, `CHAIN_PULL`, 20 entries -> 19). The definition at line 303 was DELIBERATELY KEPT so
  that rolling back is re-adding one word. Commits `09ffccc6ef` + `6fc3f50b64`.
  **The commit was not the retirement.** Two EC2 machines read that script from S3 at run time, so
  the change only took effect when the file was uploaded to
  `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` at 2026-08-30T14:03:13Z. Verified two ways:
  the object's ETag equalled the md5 of the committed blob, AND the object was downloaded and read
  (19 chain entries, the retired name appearing once as the kept definition, zero carriage returns).
  Commit `ec49f41e58`.

### 1b. INF-RECORDER-SCOPE -- commit `14346d1f09`

**What it is:** `infra/aws/lambda/ci/record-terraform-deploy.sh` records "which source commit is
deployed" for each Lambda. It selected EVERY Lambda under a pipeline's Terraform directory, so
deploying one function wrote deploy records for others. Measured: 25 rows matched, 7 written, 6 of
them for functions that deploy never touched.

**Now:** a new helper `infra/aws/lambda/ci/record-deploy-scope.py` takes `--plan <file>` (reads the
applied addresses out of `terraform show -json`) or `--function <names>`; a bare pipeline-wide call
with a saved plan present is REFUSED with exit code 2 and prints three numbers. Four falsification
arms live in `infra/aws/lambda/ci/test_record_deploy_scope_arms.py` and re-run on a scratch copy.

### 1c. INF-DRIFTCENSUS -- commit `9fffb68061`

**What it is:** a census asking, for every Lambda in the `inf-pipeline` group, whether the code
actually deployed matches the commit its record names. Tool:
`infra/aws/lambda/ci/deployed-drift-classify.py`, plus
`infra/aws/lambda/ci/source-map-staleness-census.py`. Both WRITE NOTHING.

**Result:** 8 of 25 rows had deployed code differing from their record. **Zero were cases of the
record lagging behind a good deploy.** Seven were running OLDER code than the record claimed; one
was a member-set difference.

### 1d. INF-REDEPLOY -- commits `0ff092b97c` (six rows) + `5c89cfb052` (one row)

**What it is:** the remedy for 1c. It was originally cut as SEVEN production redeploys. I measured
what the differences actually were and it came back as documentation only -- docstrings, code
comments, and log message text, from a mechanical find-and-replace commit on 2026-06-11 that
renamed paths from `data/orion/...` to `data/inf/...`. The issuer re-sized it.

**Result: ZERO deploy legs. Seven RECORD corrections.** Nothing served moved -- each function's
`CodeSha256` and `LastModified` were read live before and after, all identical. Each row's new value
was verified by downloading the deployed package and confirming EVERY member matched that commit.

### 1e. ETFS_POSITIONING.TO-14-AE -- commits `bf393fcd4e` + `3bc842e7ae`

**What it is:** a deploy-completion ledger opened 2026-08-29 by `0.7.0_AE_CloudOps~N` (a temporary
lane of this seat, now ended) that sat OPEN 23.8 hours with two unproven legs, because the lane's
session ended before the scheduled runs that were its acceptance.

**DONE:** both legs measured at the artifacts and closed. The discriminating evidence was a
before/after: a holding ticker "ABT" carried 0 of 8 return-window values in the pre-apply data and
8 of 8 after, and the population of 0-of-8 rows fell 6 -> 5 with ABT being the entire difference.
`3bc842e7ae` separately commits the sentinel-file removal the first close left uncommitted.

---

## 2. IN FLIGHT -- started, not finished, and exactly where it stops

**NOTHING IS MID-ACT AT THIS SEAT.** No apply is half-landed, no upload is partial, no ledger is
open on an act that has begun. If nobody touches anything, nothing breaks and nothing rolls back.

Two ledgers are OPEN BY DESIGN. "Open" here means the record is waiting on a future scheduled run,
not that work is unfinished:

| Ledger | What it waits for | If nobody touches it |
|---|---|---|
| `s1-bd49finsurance-silver-family` | the 04:35Z scheduled run (see section 4) | stays open; harmless. It is a record awaiting evidence, not a stalled deploy. |
| `freshguard-leg4-writer-wiring-finish` | Andrew's decision on an alarm-building moratorium dated 2026-07-28 | stays held. This is CORRECT and is not drift. Do not "resolve" it. |

Find them with `python .tools/deploy_ledger.py list` from the workspace root.

---

## 3. OWED BY THIS SEAT -- what another seat is waiting on

**NOTHING IS OWED TO ANY SEAT RIGHT NOW.** Every request made of this seat today was answered, and
the last cell (INF-REDEPLOY) was acknowledged closed by its issuer `2.0.0_SA_COO` at message 88513.

One item is HELD BY CHOICE and a successor should know why rather than discover it:

- **`record-deploy-scope.py` should RESOLVE its `--deploy-ledger` argument from git rather than
  trust the string passed on the command line.** This is this seat's own tool and a short change.
  It is NOT built because it is the remedy for a defect class that `3.0.0_SA_CVO` declared at
  message 88834 and whose OWNER HAS NOT BEEN NAMED yet. Building it now would pre-empt that.
  If a successor is told to build it, that is the shape.

---

## 4. CLOCK / EVENT-GATED -- fire time, what it proves, what failure looks like

### 4a. 04:35Z daily -- the 49F insurance silver family (ledger `s1-bd49finsurance-silver-family`)

- **Fires:** 04:35Z every day, on an S3 object-created event.
- **What it proves:** that a newly-created Lambda family (`bd49finsurance`) picks up that day's
  insurance data files and writes them out as silver-tier parquet. Acceptance requires the NEW
  family's own log showing the run, AND a second family named `cottonwood` showing NO invocation on
  those same files -- that second half is the negative control proving the routing is correctly
  scoped and not firing everything.
- **What failure looks like:** the new family's log shows no invocation for the day's keys; or
  `cottonwood` ALSO fires on them (routing too wide); or the family fires but writes nothing.
- **Also read at the first fire:** the function's actual `MaxMemoryUsed`. Its 1024 MB size rests on
  a 23.5 MB estimate that measured Python object allocation only -- it EXCLUDES the interpreter,
  native buffers, and the attached layer. That is a floor, not a measured peak, and it is unverified.
- STOP: **A manual invocation is NOT the acceptance.** Do not run it ad hoc to close the ledger faster.

### 4b. ~11:18Z daily -- the first single-writer day for billing (INF-ONEWRITER Step 2)

- **Fires:** the `inf-silver-chain` Lambda's normal daily run.
- **What it proves:** that retiring the second writer worked. The served file
  `s3://opal-data-inf/silver/api_dims/billing/snapshot_date=<date>/data.parquet` must carry exactly
  ONE new version that day, timestamped at the chain's run (~11:18Z), with content equal to what was
  certified on 2026-08-30.
- **What failure looks like:** TWO versions again on that key (the retirement did not take, or
  somebody ran the retired step by hand); or one version whose content differs from the certified
  content.
- **Whose read it is:** `0.4.0_DS_ClientPlatform~V`, not this seat.
- STOP: **Hazard, written into the dispatch script at line 303:** the retired step's definition was
  kept so rollback is cheap. Running it by hand on a production date RE-CREATES a second writer for
  that day and destroys this acceptance read. Do not run it without the issuer's word.

---

## 5. UNVERIFIED -- read this section before trusting anything above

A closure log that reads uniformly clean is the one to distrust. These are the soft spots.

1. **`inf-etf-ownership-daily` -- the one case I did not fully resolve.** Its deployed package is
   MISSING two modules (`dedup_core.py`, `trading_calendar.py`) that its current source imports. The
   deployed code does NOT import them and runs cleanly (0 import errors over 7 days), so nothing is
   broken today. **But if anyone redeploys it, the build MUST include all three modules or the
   function will fail on its first run.** This is recorded as a gate on that leg. The leg is OPTIONAL
   and was not taken.
2. **`inf-portal-advisor-publisher`'s drift verdict rests on ONE comparison with no control.** It
   declares exactly one source file and that file differed, so there was no second matching file to
   prove the comparison method was working. The tool printed "cannot self-control" itself. It was
   CLASSIFIED, not certified. It also has no enabled schedule.
3. **The MECHANISM behind the 2026-06-11 false deploy records is well-supported but not proven.**
   Measured: the commit is a mechanical path sweep, it touches all six functions, and none of them
   was redeployed after it. Not measured: the actual invocation of the recorder that wrote those
   rows. Nobody watched it happen.
4. **The INF-DRIFTCENSUS "impact" reading is about the REACHABLE code surface only.** For
   `inf-api-txn` I computed which modules the handler can actually reach and found 3 of 6 packaged
   modules unreachable. That closure is STATIC -- a dynamic import would overturn it. Two other
   seats checked that on different axes and found none, but it remains a static argument.
5. **Push state is perishable.** Measured by `git ls-remote` plus `merge-base --is-ancestor` per
   commit at 18:25:14Z: `origin/CLOUD = 89edf8efc1c8de6d105f822c742bdbdccdbbd1a5`, and
   `14346d1f09`, `9fffb68061`, `0ff092b97c`, `5c89cfb052` are ALL ON ORIGIN. The session log commit
   `e5fd5a2ad1` and this file are **LOCAL** and ride the next integration window. Re-measure before
   relying on any of it.
6. **Four figures I stated today were wrong and were corrected.** They are corrected in the record,
   but a successor reading older messages will meet the wrong numbers: "25 rows stamped with HEAD"
   (truth: 7), "nine functions" (truth: 8, of which 7 matched the predicate), "+39 lines of real
   code" (truth: 39 comment lines, 0 code), and "14 other sends" (truth: uncounted; 95 per-recipient
   deliveries carried an id). In every case the instrument was right and my reading of its output
   was wrong. **If an older message and a newer one disagree on a number, the newer one is the
   correction.**
7. **The messaging fabric is silently dropping delivery records right now.** `org/mcp/server.py`
   swallows broker errors, so a send can report DELIVERED while writing no delivery row and stamping
   no message id in the delivered file. A file with no `**Msg-ID:**` header does NOT mean the row is
   missing -- it means the SENDER never learned the id. Owner is `1.0.0_SA_CTO`; a fix is
   deliberately deferred. **Practical effect for a successor: trust the inbox DIRECTORY for what
   arrived, not the delivery-state query.**

---

## 6. Current State (the one-screen version)

Everything this seat touched today is committed and, except the two log files, on origin at
`89edf8efc1`. No AWS change is half-applied. No ledger is open on a started act. Two ledgers await
scheduled evidence, one awaits Andrew. `inf-silver-chain` runs current code and is the sole writer
of the billing table. Six inf-pipeline deploy records that falsely claimed a deploy now honestly
say the deployment is behind the source -- **the estate's "stale" count rose from 6 of 25 to 13 of
25, and that rise is the repair, not a regression.** Do not "fix" it back.

---

## 7. Next Steps

1. **[0.4.0_DS_ClientPlatform~V]** the ~11:18Z single-writer read (section 4b).
2. **[0.7.0_AE_CloudOps]** the 04:35Z insurance-family read (section 4a), including the memory
   figure.
3. **[1.0.0_SA_CTO]** two queued items in that seat's lane: `commit-gate.sh` must exit non-zero when
   it checks nothing on a file class its own header claims to cover, and the `org/mcp/server.py`
   broker-error fix.
4. **[gate or issuer, owner unnamed]** the NON-AUTHORITATIVE IDENTIFIER class (message 88834). This
   seat disclosed the seventh instance against itself and cannot own the class it is in.
