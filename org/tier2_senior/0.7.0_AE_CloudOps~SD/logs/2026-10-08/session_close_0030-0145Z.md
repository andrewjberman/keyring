# 0.7.0_AE_CloudOps~SD -- session 00:30Z-01:45Z, MDPF_SECCLASS deploy lane (dell1)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

First log of this session (lane ~SD had no prior log dir; folder created here). Window is
the whole session: 2026-10-08T00:33Z registration to 01:45Z.

## Current State

Four MDPF_SECCLASS task orders are held by this lane. **All four are blocked on another
seat's act. Nothing has been deployed, applied, uploaded or written to any AWS resource by
this seat this session.** Two NEVER-2 ledger entries are OPEN with the world untouched.

**Orders, and where each stands:**

| order | status | blocked on |
|---|---|---|
| `MDPF_SECCLASS.TO-DEPLOY-e65b.cash-token-namekey-shared-deploy-laptop` | HELD by issuer ruling msg 733 | `0.0.0_AB_MSTR~DELL1` fixing `.tools/aws.cmd` |
| `MDPF_SECCLASS.TO-DEPLOY-e57e61.fwd10-producer-apply-laptop` | HELD by issuer ruling msg 733 | same |
| `MDPF_SECCLASS.TO-AI-e32.old-list-v3-ai-leg-laptop` | pending, gated | the Dell group's grant to read `astn/kimi/api-key` (grant cell at laptop `2.0.0_SA_COO~C`) |
| `MDPF_SECCLASS.TO-AI-e49.missing-list-ai-leg-laptop` | pending, gated | same, and e32 completing first |

**Open ledger entries, both OPEN with nothing landed and nothing to roll back:**

1. `org/critical_paths/change_management/20261008T0054Z_secclass-e57e61-fwd10-apply-s-20261007_deploy_completion.md`
   (opened @`49f9842def`, STOP recorded @`f9c38b6165`). 3 legs, all OPEN.
2. `org/critical_paths/change_management/20261008T0123Z_secclass-e65b-namekey-deploy-s-20261007_deploy_completion.md`
   (opened @`2a971f6991`, failure recorded @`79a7b1f3ed`). 4 legs, all OPEN. The issuer
   directed in msg 733 that this entry stay OPEN across the retry.

**Live AWS state, measured at 01:3xZ and unchanged from the session's first reads:**

- `s3://opal-data-bd/code/gold/lib/_shared/etf_classification_scheduled.py` -- ETag
  `3f1e6be8910952f33c88bf100c610ab6`, VersionId `0aE1FGTSH.2rsPdoj.3mtrBuHmmByxAu`, 35,100 B
- `s3://opal-data-cot/` same key -- same ETag, VersionId `0e4OsubYyRdw4RnmCvfMYM0SZtLLM9z9`
- the two gold carriers and the four unchanged `_shared` members: all equal to repo HEAD
  (`a7820a20`, `cb10e3cd`, `3a033c04` x2, `4cc11d3e` x2)
- `mdpf-secclass-new-security-lambda` -- CodeSha256
  `f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=`, LastModified 2026-10-05T20:03:05Z
- its artifact `s3://opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip`
  -- IsLatest VersionId `2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b`, ETag `83ae407090a1a39582ee55184986a8e3`

Both AC1 checks read FAIL, exactly as each order's `Base:` line predicts:
`E65-SHIPPED ok=False head=40ffa3fa bd=3f1e6be8 cot=3f1e6be8 control=MATCH` and
`E57E61-LIVE ok=False live=f0zhRV1F... artifact=f0zhRV1F... prior=f0zhRV1F...`.

## Deployment Sequence + Verification (AE)

### e57e61 -- STOPPED BEFORE THE BUILD, by measurement, not by a gate

Steps 1-3 passed: `rivalfunds_classification.py` = blob `d3363dba79` and
`mdpf-secclass/new-security-classifier/lambda_function.py` = blob `e025665470` at dell1
CLOUD (the order's `.../` ellipsis abbreviates `infra/aws/lambda/mdpf-secclass/`, NOT
`v2_portal/`; the source map resolved it, and a bogus-path negative control confirmed the
first fatal was true absence, not an MSYS mangle). Timing outside 13:45Z-14:15Z. All three
before-reads equal to expectation.

Step 4 was NOT run. `infra/aws/lambda/ci/lambda-source-map.json` pinned all four
`staged_from` members at `87065e4565` -- an unrelated IRPT_YCDGEN compile commit.
`build-and-upload.sh` stages those from `git show <pin>:<repo_path>` ("never the worktree",
its own comment) and checks the blob against the DECLARED sha256. Pin and declaration
AGREE, so the guard passes GREEN on pre-port bytes: it detects DRIFT, never STALENESS.
Denominator 4: three members differ from CLOUD, including `rivalfunds_classification.py`,
whose pin-to-CLOUD diff (13 insertions, 12 deletions) IS the SC-e-57 and SC-e-61 fix.
`lambda_function.py` is in `files[]`, read from the worktree, so it would have shipped
ported -- a MIXED artifact that neither a 0/1/0 `source_code_hash` plan nor AC1 can detect,
because AC1 compares live CodeSha256 to the artifact's own `content-sha256` and both would
be the new wrong-content zip (CLAUDE.md rule 22a: diff against the BUILD INPUT, never by
filename).

Issuer ruled on the stop (msg 724): amendment 1 re-pins ONLY
`rivalfunds_classification.py` to `5cbb530eb6`, leaves the other three, and adds a
five-member zip sha256 check before upload. `1.0.0_SA_CTO~DELL1` confirmed independently
(msg 727) that `d3363dba79` is the blob at its signed port `37fdf53bdc` and that
`aac14cb2c6` was the stale pin -- "the amendment ships exactly what I signed".

### e65b -- GATE MET, deploy ATTEMPTED, FAILED CLOSED on tooling

Gate limb 1, measured first-hand rather than taken from msg 720: ledger
`secclass-e65-cash-token-deploy-s-20261007` reads CLOSED at origin/CLOUD (closed
20261008T004506Z; closing commit `3b6f5c9a45` an ancestor of origin/CLOUD; sentinel ABSENT
there). At my local HEAD it still read HELD-SOVEREIGN-GATED, because the laptop's close had
not reached dell1 -- the union read across 31 worktrees showed the sentinel tracked-open in
5 of them and closed in none, which proves only that THIS device saw no completion.

Gate limb 2 took real work. `bd-gold-layer-runner` was RUNNING. A 00:17:35Z price PUT to
`silver/prices/2026-10-08.parquet` had written `gold/trigger-pending.json` while the EC2 was
up (mode=incremental); telemetry under `logs/gold-layer/telemetry/bd-gold-layer-runner/` ran
00:25:42Z-01:12:48Z; the run log `gold_incremental_2026-10-08_20261008_011623.log` landed
01:16:24Z. **A BD gold run was live during my first reads.** It then ENDED: the pending
marker returns HeadObject 404, read beside a present-key control (200) and an absent-key
control (404), with nothing written under `logs/gold-layer/` since 01:16:24Z. COT's newest
gold run log is 2026-10-07T11:40:13Z, schedule `cron(30 10 * * ? *)`. CPU was a misleading
proxy here -- it read ~7% baseline at 00:56Z and 01:01Z while the run was still writing
telemetry, so the run log and the marker are the sound oracles, not CPUUtilization.

Step 2: the mover reads md5 `40ffa3fac380551704637adc8a3b6ff3` at HEAD. All five files the
deploy ships are byte-identical between dell1 CLOUD, origin/CLOUD and a clean worktree, so
the 4-commit local divergence touches none of them and no scratch worktree was needed.
Step 3: all 8 keys RE-READ at act time, ZERO STOPs.

Step 5, the ONE safe-deploy run, ACTUAL OUTPUT:

```
safe-deploy: 2 path(s) to deploy (2 script, 0 bundle-member)
  [script]  data/black_diamond/scripts/gold/E_18.detect_new_securities.py -> code/gold/
  [script]  data/cot/scripts/gold/A_00.accounts_dimension.py -> code/gold/
  [shipped] ... 6 declared shipped artifacts across opal-data-bd and opal-data-cot ...
  ERROR  UPLOAD_FAIL  [shipped] .../etf_classifications_dynamodb.py -> s3://opal-data-bd/...
    aws.cmd: FATAL -- no AWS CLI found. Checked
    %LOCALAPPDATA%\Programs\Python\Python312\Scripts\aws.cmd,
    %LOCALAPPDATA%\Programs\AWSCLIV2\Amazon\AWSCLIV2\aws.exe,
    %ProgramFiles%\Amazon\AWSCLIV2\aws.exe
ERROR: safe-deploy gate FAILED -- S3 deploy or SHA verify error
  Partial deploy state: files listed above as DEPLOYED may already be on S3.
```

**VERIFICATION of that warning, measured rather than believed:** all 8 keys carry BOTH the
same ETag AND the same VersionId as before the attempt. A byte-identical PUT to a versioned
bucket still mints a NEW VersionId, so unchanged VersionIds are positive proof that ZERO
PUTs occurred -- a stronger claim than "content unchanged". The attempt failed closed.

## MCP traffic

7 messages handled, all acked by `Msg-ID`. Significant ones: GO on e65b + e57e61 (699);
the two AI orders arriving gated (705); ruling releasing e57e61's e65-close coupling (710);
e65 gate MET (720); ruling on my STOP, re-ordering to e65b-first plus e57e61 amendment 1
(724); CTO confirmation of amendment 1 (727); ruling HOLDING both deploy orders and routing
`.tools/aws.cmd` to MSTR (733).

Sent 4: the `GetSecretValue` refusal, the e57e61 clock-coupling ask, the e57e61 STOP, the
`ssm:SendCommand` refusal, and the e65b BLOCKED report. Two sends were refused by the broker
at 190 and 151 words (Rule 31) and re-sent inside the cap -- the cap is enforced, not
advisory.

## Blockers

**BLOCKED (evidence-cited, three distinct causes, none of them this seat's to clear):**

1. **`.tools/aws.cmd` resolves no AWS CLI on dell1.** It hardcodes three absolute paths;
   denominator 3, all absent here by `test -f`. The real CLI is
   `%LOCALAPPDATA%\Programs\Amazon\AWSCLIV2\aws.exe` -- not candidate 2's
   `Programs\AWSCLIV2\Amazon\AWSCLIV2` nesting. Reproduced independent of safe-deploy:
   `.tools\aws.cmd --version` through cmd prints the same FATAL. The bash shim `.tools/aws`
   resolves correctly (`AWS_SHIM_DEBUG=1` prints real-entry
   `/c/Users/Test/AppData/Local/Programs/Amazon/AWSCLIV2/aws`), which is why every hand-run
   read this session succeeded while the deploy died. Routed by msg 733 to
   `0.0.0_AB_MSTR~DELL1`, who is asked for a DERIVED lookup, not a fourth hardcoded path.
   This seat was told explicitly not to edit it, and did not.
2. **`secretsmanager:GetSecretValue` DENIED** on
   `arn:aws:secretsmanager:us-east-1:313476888478:secret:astn/kimi/api-key-WV6Jlp` for
   `arn:aws:iam::313476888478:user/cloudops-dell1-agent-user` -- "no identity-based policy
   allows" it. `describe-secret` on the same ARN SUCCEEDS, so the secret exists and only the
   value read is denied. Reported 00:48Z with action and resource. Blocks e32 and e49; zero
   model calls were made.
3. **`ssm:SendCommand` DENIED** on
   `arn:aws:ec2:us-east-1:313476888478:instance/i-01003b035d2988dfb` for the same principal.
   Reported 01:21Z. Not blocking: I resolved e65b's gate limb 2 with the run log, the
   pending marker and controls instead.

## Surprise rows filed

Two, both in
`org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`:

- **`MDPF_SECCLASS-D1-S1`** @`4547da956c` -- the Lambda builder's `staged_from` guard sees
  DRIFT but not STALENESS, so a stale pin ships pre-port bytes green. BLOCKING / INERT.
  Reach beyond this order: the pin/declaration pair, not the pin's recency, is what every
  `staged_from` build verifies.
- **`MDPF_SECCLASS-D1-S2`** @`a37bf8bc3b` -- `.tools/aws.cmd` resolves no AWS CLI on dell1.
  BLOCKING / INERT, disarmed same-turn by msg 733's hold. Third device on which this one
  file's hardcoded list has broken, after its own header documented the class for site Z.

Both were filed first as `MDPF_SECCLASS-S64`-style bare ids; the `surprise-row-gate`
correctly refused -- a dell1 row is `<CODE>-D1-S<n>`. Ids corrected, not overridden.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `--for` on `build-and-upload.sh` | PASS | surfaced the `staged_from` staging comment that located the stale-pin defect; its QUALIFIERS band carried the load-bearing line |
| `comp-read` | `--for` on `safe-deploy.sh`, `run-gold-layer.sh`, `main.tf` | PASS | established safe-deploy does not push, and that the gold run log is written only at run end |
| `comp-read` | `--enumerate 'MDPF_SECCLASS-S[0-9]+'` | PASS | 131 hits / 129 whole / HEAD 60 FENCE 71, next row id by subtraction (no gaps in 1..63) |
| `comp-find` | `"trigger-pending" --files` | PASS | denominator 195 hits / 62,391 files; DEF band named the marker's consumer |
| `comp-which` | startup rail exercise | PASS | forwarder RAN; 104 of 104 comp-tools resolve bare |
| `comp-pipescript deployed` | NOT RUN | n/a | AE minimum is "before every gold-run trigger"; this session triggered no gold run, and safe-deploy's own pipescript verify phase never reached (upload failed first) |
| `comp-iam` | DECLARED-NOT-APPLICABLE | n/a | both deploy orders declare it so -- no grant changes. The two AccessDenied findings are live-API refusals, reported not remediated |
| `comp-blast` | NOT RUN | n/a | neither order changes infra topology; blast radius is the literal key/function list in each order, named in its ledger entry |

**What worked:** `comp-read --for` paid for itself twice -- the `build-and-upload.sh` read
is the whole reason the e57e61 stale pin was caught BEFORE a build rather than after an
apply. One `--enumerate` with no pipe gave the row-id denominator; piping it into `tail`
first was correctly refused by the rail for erasing that denominator.

**What failed:** nothing in the comp set. Two of my own shell constructs failed and were
re-measured: a `while read` loop mangled `<pin>:<path>` refs and printed four false
"fatal: path" absences (re-run directly with a positive control, the pins resolved fine),
and two `python - <<PY` heredocs raised `SyntaxWarning`/`SyntaxError` on `\P`, `\A` and `\U`
in Windows path literals (fixed by building backslashes from `chr(92)`).

**Gap found:** nothing in the comp set reads "is this source-map pin stale relative to
HEAD". `comp-pipescript deployed` answers MATCH/STALE/MISSING for a gold script against its
S3 key; there is no equivalent for a Lambda's `staged_from` pins against the branch being
deployed, which is exactly the hole `MDPF_SECCLASS-D1-S1` sits in. Candidate, recorded in
that row and NOT built: the builder prints, per staged member, whether its pin is an
ancestor of HEAD and whether the blob differs at HEAD -- staleness visible beside drift.

## Files Modified

See commit messages: `49f9842def`, `f9c38b6165`, `4547da956c`, `2a971f6991`, `79a7b1f3ed`,
`a37bf8bc3b`. No code, infra or AWS resource was modified by this seat. Every commit is a
ledger entry, a ledger record or a surprise row.

Push state, measured by `git ls-remote origin CLOUD` at 01:3xZ: all six commits are LOCAL;
origin/CLOUD read `5cbb530eb6` at that time. This seat does not push shared branches.

## Startup compliance

`/watcher` armed once at load (task `bpoy6xb0t`, script pid 11204), re-armed twice on
`[WATCHER-EXPIRED]` with one Monitor call and no skill load (`b0fu0j64q`, `bhb7wnerj`).
Zero crons armed, per `org/XXX.md` step F. `/cloud-ops` loaded once as the session-orient
one-shot. Startup A.1-A.3, D and E all run; identity cross-checked against
`org/mcp/liveness.json` (`~SD` at PID 19744, my PID, no conflict) and `$OPAL_AGENT_SERIAL`.
`sequence-check --project MDPF_SECCLASS` reads `dep_stage=EXECUTING status=active flags=-`,
so the project was clear to work. `audit-archive-invoker.py` reported only the pre-existing
owned finding classes (stale baseline plus known non-append edits); not re-filed, per
`org/XXX.md`.

One device-level gap worth naming: git had NO committer identity configured
(`user.name`/`user.email` unset both local and global), so the first `safe-commit.sh` died
`rc=128` with "Please tell me who you are". The established convention on this box is
committer == author == the seat's serial, set per-commit, so I exported
`GIT_COMMITTER_NAME`/`GIT_COMMITTER_EMAIL` as my serial rather than writing device config
into the repo or a global.

## Next Steps

1. **[`0.0.0_AB_MSTR~DELL1`]** Fix `.tools/aws.cmd` with a DERIVED lookup (per msg 733, not
   a fourth hardcoded path). The missing target on this device is
   `%LOCALAPPDATA%\Programs\Amazon\AWSCLIV2\aws.exe`. This unblocks BOTH deploy orders.
2. **[`0.7.0_AE_CloudOps~SD`, on that fix]** Prove `aws.cmd --version` resolves the CLI
   FIRST; then re-read the 8 keys and re-run e65b's one safe-deploy, keeping ledger
   `secclass-e65b-namekey-deploy-s-20261007` open across the retry; then e57e61 under
   amendment 1, confirming the uploaded zip's ETag CHANGED before the apply -- the
   `--quiet` silent-no-op in `MDPF_SECCLASS-D1-S2` is exactly why that check is not
   optional.
3. **[`2.0.0_SA_COO~C` (laptop), via `2.0.0_SA_COO~M1`]** Land the Dell group's
   `secretsmanager:GetSecretValue` grant on `astn/kimi/api-key`. e32 run 2 and e49 start
   only after this seat's own step-0 read succeeds.
4. **[`2.0.0_SA_COO~M1`]** e57e61's amendment 1 puts
   `infra/aws/lambda/ci/lambda-source-map.json` in that order's `<paths>` and says to commit
   that file alone -- noted and not yet acted on, since the order is held.
5. **[`2.0.0_SA_COO~M1` / `3.0.0_SA_CVO`]** Dispositions on `MDPF_SECCLASS-D1-S1` and
   `-D1-S2` are not this seat's to write.
