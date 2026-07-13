# Deploy Completion Record
**Date opened:** 2026-07-13T12:35:47.687543+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260713T124017Z
**Deploy:** inf-accounts-v2-daily 0-row roster guard (fail-closed before the write) + sentinel status derived not asserted
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit f06215520 (guard + both-arm harness) | hash on origin/CLOUD via git branch -r --contains | CLOUD f06215520 (guard at the call site + test_zero_row_roster_guard.py both-arm harness), author 0.7.0_AE_CloudOps, safe-commit -F. | CLOSED 20260713T124017Z |
| L2 | s3-prefix | inf-accounts-v2-daily.zip -> lambda-artifacts | build-and-upload write-VERIFY (size + content-sha256 metadata match) | build-and-upload write-VERIFIED: s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-accounts-v2-daily.zip size=38398, Metadata.content-sha256 match (gate da5af3c8c). New sha Sx7BN++cU0zFRJ2QEhWe2P++wj/84MLuAWPjtQm6zMI=; baseline was klb5p7rY86avZ7ZmRELZJ8GA45jioDOMtYCybzWNGlA= -- the object DEMONSTRABLY changed, so TF did not hash a stale zip. | CLOSED 20260713T124017Z |
| L3 | activation | safe-apply: live CodeSha256 == new artifact sha | 0-diff replan + live get-function-configuration | safe-apply (HALT_ACK=1, -target=module.inf_accounts_v2_daily): 0 added, 1 changed, 0 destroyed. Untargeted 0-diff replan: 'No changes. Your infrastructure matches the configuration.' APPLIED-TRUTH GATE: live get-function-configuration CodeSha256 = Sx7BN++cU0zFRJ2QEhWe2P++wj/84MLuAWPjtQm6zMI= == the artifact sha, != the pre-apply baseline. The guard IS the deployed code. | CLOSED 20260713T124017Z |
| L4 | verify | REACHABILITY FROM THE RUNNER: download the DEPLOYED zip from AWS and confirm the guard is in the code AWS actually runs -- not the repo, not a commit hash, not a green test suite | guard string present in the deployed package + both-arm harness green | REACHABILITY FROM THE RUNNER (CVO's bar: 'Landing is not the property that matters -- reachability from the runner is'). DOWNLOADED THE DEPLOYED PACKAGE FROM AWS (aws lambda get-function -> presigned Code.Location, 38,398 B) and read the code AWS actually runs -- not the repo, not a commit hash, not a green test suite. (a) GUARD PRESENT in the deployed lambda_function.py ('REFUSING to write an empty roster'; '0-ROW ROSTER IS AN INSTRUMENT BREAK'). (b) SENTINEL GUARD PRESENT ('REFUSING to stamp a silver-complete sentinel ... rows=0'). (c) ORDER ASSERTED, not assumed: guard at line 168, write_silver_api_dim_parquet at line 178 -- THE GUARD PRECEDES THE WRITE in the deployed bytes. (d) POSITIVE CONTROL on the retrieval: the same grep returns 0 for a string that is not in the file, so it discriminates and the presence is a REAL presence, not a broken read. BEHAVIOUR EXERCISED, BOTH ARMS, ON THE REAL HANDLER (test_zero_row_roster_guard.py drives the actual lambda_handler with deps stubbed; it does NOT re-implement the guard and assert on the copy): EMPTY roster -> RAISES + NO parquet + NO sentinel; REAL 3-row roster -> WRITES + sentinel status=ok rows=3. FAILING ARMS 0. The REAL-roster arm is the POSITIVE CONTROL and it is what makes the empty arm mean anything: it proves the handler genuinely REACHES the parquet write, so an always-raising stub could not have passed. HONEST LIMIT, STATED: I did NOT invoke the DEPLOYED lambda with an empty roster -- I cannot force a 0-row roster without corrupting the real feed. The behavioural proof is hermetic-on-the-real-handler; the deployed proof is byte-presence + an unbroken sha chain (tested source -> zip -> S3 content-sha256 -> live CodeSha256, all four matching). That is the strongest available without manufacturing the very corruption the guard exists to prevent. | CLOSED 20260713T124017Z |

## Log

- 20260713T123547Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260713T124017Z LEG L1 closed: CLOUD f06215520 (guard at the call site + test_zero_row_roster_guard.py both-arm harness), author 0.7.0_AE_CloudOps, saf
- 20260713T124017Z LEG L2 closed: build-and-upload write-VERIFIED: s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-accounts-v2-daily.zip size=383
- 20260713T124017Z LEG L3 closed: safe-apply (HALT_ACK=1, -target=module.inf_accounts_v2_daily): 0 added, 1 changed, 0 destroyed. Untargeted 0-diff replan
- 20260713T124017Z LEG L4 closed: REACHABILITY FROM THE RUNNER (CVO's bar: 'Landing is not the property that matters -- reachability from the runner is').
- 20260713T124017Z CLOSED -- all 4 legs proven
