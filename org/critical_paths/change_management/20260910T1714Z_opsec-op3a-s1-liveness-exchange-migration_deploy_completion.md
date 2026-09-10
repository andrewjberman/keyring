# DEPLOY-COMPLETION LEDGER -- NFRA_OPSEC202609 OP3A-s-1 / FWD-12: the two IN-LANE liveness callers move onto the gateway's capability-token EXCHANGE endpoint

**Status:** **OPEN 2026-09-10T17:14Z** by `0.9.0_WK_NFRA_OPSEC202609~5` (L7, TO-OP3A-S-1).
**Opened BEFORE any apply**, per CLAUDE.md s.5 NEVER-2 and the task order's own bound.
⛔ **STILL OPEN AT 17:2xZ -- THE APPLY WAS REFUSED BY A GATE AND NOTHING WAS DEPLOYED. NOTHING IS
HALF-LANDED. Read "THE APPLY WAS BLOCKED" below before treating this entry as an in-flight deploy.**
**This entry is deliberately NOT closed:** a CLOSED ledger entry for a deploy that did not happen is
a worse artifact than an open one.

**Closes when:** BOTH Lambda functions read a `source_code_hash` equal to the value the targeted plan
predicted, AND a manual invocation of each returns `{"ok": true, "cred_path": "exchange"}` with the
function's own CloudWatch log carrying a `cred_path=exchange` line for that RequestId.
NOT on `LastModified`, NOT on the apply's own rc, NOT on the plan text -- on the deployed function's
configuration and its own executed log.

## What is being deployed

Two `aws_lambda_function` resources in `infra/aws/terraform/opal-gateway`, and nothing else:

| function | tf resource | packaged source |
|---|---|---|
| `opal-otp-liveness` | `aws_lambda_function.otp_liveness` | `infra/aws/lambda/m365-otp-liveness/lambda_function.py` |
| `opal-ms-ingest-liveness` | `aws_lambda_function.ms_ingest_liveness` | `infra/aws/lambda/m365-ms-ingest-liveness/lambda_function.py` |

**The change, in one sentence:** each probe now presents its long-lived static bearer ONCE, to the
gateway's exchange endpoint, and probes `/{otp,ms}/health` with the short-TTL (300 s) capability
token it receives -- so the credential that crosses the wire on the probe call EXPIRES instead of
being a held secret.

Source edit per file (3 behaviour lines + one helper):
- `TOKEN_URL = os.environ.get("{OTP,MS}_TOKEN_URL", HEALTH_URL.rsplit("/", 1)[0] + "/token")`
- `_capability(static_bearer)` -- `POST` to `TOKEN_URL` with the static bearer, no body, returns
  `capability_token`; prints `cred_path=exchange url=... aud=... ttl=...s`.
- in the handler: `bearer = _capability(bearer)` INSIDE the probe's EXISTING `try`, and the probe
  `Request` moved inside that same `try`.
- success return gains `"cred_path": "exchange"`.

Declaration edit per file: one new environment variable, `OTP_TOKEN_URL` / `MS_TOKEN_URL`.

## What this deploy deliberately does NOT do

- **The static bearer is NOT retired and neither secret is revoked.** Three cross-lane callers
  (`bd-49f-auto-login` / OpalETL, `bd-cot-auto-login` / PartnerETL, the globgrph `NFRA_MSGRAPH`
  derive / CloudComp) still depend on dual-accept, and they migrate through their own lanes by
  Andrew's ruling `@9382d107a3` s.1. Their code is untouched here.
- **No alarm, monitor, notification, subscription or checker is created, changed or added.** The
  standing moratorium is untouched. The exchange runs inside the probe's ALREADY-EXISTING `try`
  precisely so that a failed exchange reaches the alert path that already exists rather than adding
  a new trigger site. **The number of `_alert()` call sites is unchanged at 2 in each file.**
- **No gateway-side (app) edit.** That surface is `0.7.0_AE_CloudOps`'s lane. The exchange endpoint
  was consumed exactly as it already behaves.

## THE APPLY IS `-target`ed, AND THAT IS NOT ROUTINE -- HERE IS WHY

A baseline `terraform plan` of `infra/aws/terraform/opal-gateway` taken at 2026-09-10T17:0xZ, BEFORE
any edit of mine, was **not empty**:

```
Plan: 0 to add, 2 to change, 0 to destroy.
  # aws_wafv2_ip_set.opal_blocked_ips_regional_v4   ~ + description = "NFRA_OPSEC202609 C-2: ..."
  # aws_wafv2_ip_set.opal_blocked_ips_regional_v6   ~ + description = "NFRA_OPSEC202609 C-2: ..."
```

Those two resources are declared in `waf.tf` and belong to `0.7.0_AE_CloudOps`'s cells
(`TO-OP-S-4-18` @`37c4bde812`, `TO-OP-S-15-19` @`3758b14afc`) -- **not to this order.** An untargeted
apply from this seat would have silently landed another lane's pending change. Recorded as surprise
row `NFRA_OPSEC202609-Z-W5-S1`. The apply is therefore scoped:

```
-target=aws_lambda_function.otp_liveness -target=aws_lambda_function.ms_ingest_liveness
```

which plans **exactly** `Plan: 0 to add, 2 to change, 0 to destroy` over those two functions only.

## Rollback -- named, and measurable

Restore both sources to their pre-change bytes and drop the two env vars, then re-apply with the
SAME two targets:

```
git show c9c6600e95:infra/aws/lambda/m365-otp-liveness/lambda_function.py
git show c9c6600e95:infra/aws/lambda/m365-ms-ingest-liveness/lambda_function.py
git show c9c6600e95:infra/aws/terraform/opal-gateway/otp-liveness.tf
git show c9c6600e95:infra/aws/terraform/opal-gateway/ms-ingest.tf
```

**The rollback's success oracle is an exact pair of strings, measured before the apply, not a
description:**

| function | pre-deploy `source_code_hash` | pre-deploy package `lambda_function.py` sha256 / bytes |
|---|---|---|
| `opal-otp-liveness` | `hot3riLNhAoNfPYJhQPI/z/TW5Cd4BjfaQ73Q5oZbMU=` | `fd13b4905476d692...` / 3947 B |
| `opal-ms-ingest-liveness` | `eJivS8spnzrkj5eCovTF5BWU22kclsEMabGOrQYQ6UI=` | `8f2b0aca27da5032...` / 3301 B |

Rollback is complete when `get-function` reads those two `source_code_hash` values back.
**Blast radius of a rollback is the same two functions**; nothing else is in the target set.
**Rollback is CHEAP and the failure is LOUD:** the probes are read-only liveness checks on a 6 h
cadence that fetch no mail, no OTP code and no file content. A broken probe degrades to a false
alert, not to a data loss.

## Pre-deploy state, MEASURED not assumed (2026-09-10T16:57Z-17:12Z)

1. **Dual-accept intact TODAY.** `GET /otp/health` with the current static bearer -> **200**
   `{"ok":true}` at 16:57:16Z. Junk bearer on the same path -> **401** `{"error":"unauthorized"}`.
2. **The exchange endpoint answers a real exchange, not a Microsoft OIDC 302.** `POST /otp/token`
   with the static bearer, no body -> **200** `{"capability_token": ..., "token_type":"Bearer",
   "expires_in":300, "aud":"gw:otp"}`, `server: uvicorn`, `cache-control: no-store`. RS256,
   `kid ac4c49e6c8bec6d4`, `iss https://mcp.opalinvest.dev`, `sub 49f`, `typ capability`,
   `exp-iat = 300`. `POST /ms/token` is the same with `sub ms`, `aud gw:ms`.
3. **The minted token is accepted, and NOT because any JWT is accepted.** `gw:otp` token on
   `/otp/health` -> 200; `gw:ms` token on `/ms/health` -> 200; **cross-audience controls BOTH
   directions: `gw:ms` on `/otp/health` -> 401, `gw:otp` on `/ms/health` -> 401.**
4. **Running bytes were the repo bytes before this change.** The deployed package was downloaded and
   its single member compared to the repo source: `fd13b4905476d692` / 3947 B and
   `8f2b0aca27da5032` / 3301 B, IDENTICAL on both.
5. **The patched handlers were exercised LOCALLY against the live gateway before any deploy**, with
   `_alert` hard-stubbed to abort the process rather than publish: both returned
   `{"ok": true, "cred_path": "exchange", "detail": "status=200"}`.
6. **IAM needs no change** -- the exchange path reads the SAME secret the probe reads today.
   (`simulate-principal-policy`, one `--resource-arns` per call, re-run below.)

⚠ **BOUND, stated rather than buried:** every live number in this entry was taken inside a single
short window on 2026-09-10. It supports *"the exchange worked and dual-accept was intact at that
moment"* and supports **no claim about stability across the 6 h probe cadence.**

## Steps

| # | Step | State |
|---|---|---|
| 1 | Grounding re-taken from source + live endpoint (AC1/AC2/AC3) | **DONE** 16:57Z-17:01Z |
| 2 | Sources patched; `py_compile` clean; `terraform validate` Success; `terraform fmt -check` rc=0 | **DONE** |
| 3 | Patched handlers exercised locally with alerting stubbed | **DONE** 17:12Z |
| 4 | Baseline plan read; foreign drift found; apply scoped by `-target` | **DONE**, row `Z-W5-S1` |
| 5 | Gateway health confirmed IMMEDIATELY BEFORE the apply, so no alert branch can fire | **DONE** 17:16:46Z -- `/otp/health` 200, `/ms/health` 200 |
| 6 | `safe-apply` (targeted) | ⛔ **BLOCKED** -- gate refusal, rc=3, twice. See below. |
| 7 | `get-function` reads the predicted `source_code_hash` on both | **NOT REACHED** |
| 8 | Manual invoke of both; result + own log carry `cred_path=exchange` | **NOT REACHED** |
| 9 | Commit the change under this serial | ⛔ **BLOCKED** -- owned-paths lane gate, rc=1, 6 of 9 paths. Same `<issued_to>` cause. Row `Z-W5-S3`. |
| 9a | Commit the RECORD (this entry, the rows, the proof instance, the patch) under this serial | **DONE** -- the 3 of 9 `org/` paths were admitted |
| 10 | Push state stated as MEASURED | **DONE** -- see Push state |

## ⛔ THE APPLY WAS BLOCKED, AND THE GATE WAS RIGHT

`safe-apply` runs `.tools/halt-gate-check.sh` first. It refused this seat **twice**, `rc=3`:

1. **17:17:39Z** -- `HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)`. No session serial file
   existed in this fresh worktree. Remedied as the banner instructs (the file is under
   `org/mcp/sessions/`, which `.gitignore:423` ignores -- runtime state, not a repo edit, and
   worktree-local because `HALT_GATE_REPO_ROOT` resolves to the worktree root).
2. **17:2xZ** -- `HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)`, verbatim:
   `Resolved serial: 0.9.0_WK_NFRA_OPSEC202609~5` ... *"a spine-v3 worker (0.9.0_WK_<CODE>~<n>) is
   admitted only while a NON-TERMINAL task order under <CODE> at HEAD is issued_to it."*

**The cause, measured unscoped:** the task order was amended @`775e6cf20a` to widen `<paths>`, but its
`<issued_to>` still reads `0.9.0_WK_NFRA_OPSEC202609~4`. A census of every task order under this
project at HEAD returns **`issued_to ~5`: 0 of 35**. `halt_gate_worker_issuer` (`:146-153`) therefore
finds no order for this serial and fails closed.

**THE REFUSAL IS CORRECT AND WAS NOT OVERRIDDEN.** The gate exists so a worker's deploy halts on its
issuer's STOP messages; a worker with no order has no issuer inbox to scan, and admitting it would
mean deploying blind. The `rc=3` identity branch carries **no** override by design (`HALT_OVERRIDE`
at `:415` sits inside the STOP-message branch, which is only reached after identity resolves -- read
from source, deliberately NOT exercised: a test whose failure mode is "performs the deploy I declined
to authorise myself for" is not a safe test). Editing `<issued_to>` to admit myself would be
manufacturing my own admission past a safety gate, and is an issuer act, not a worker's.

Recorded as surprise row `NFRA_OPSEC202609-Z-W5-S2` (BLOCKING, ARMED, disarm owner `2.0.0_SA_COO~Z`).

### NOTHING LANDED -- MEASURED ON THE LIVE PLANE, 17:23:16Z, AFTER the refusal

```
opal-otp-liveness        CodeSha256 hot3riLNhAoNfPYJhQPI/z/TW5Cd4BjfaQ73Q5oZbMU=
                         LastModified 2026-08-15T02:32:24.425+0000   OTP_TOKEN_URL ABSENT
opal-ms-ingest-liveness  CodeSha256 eJivS8spnzrkj5eCovTF5BWU22kclsEMabGOrQYQ6UI=
                         LastModified 2026-08-15T02:32:30.583+0000   MS_TOKEN_URL  ABSENT
```

Byte-identical to the pre-deploy values recorded above, on both the code hash and the timestamp, and
neither new environment variable is present. **Terraform was never invoked** -- the gate exits before
`exec`. NEVER-2 is not engaged: there is no half-landed deploy to finish or roll back, and the
rollback recipe above is consequently UNUSED, not failed.

## ⛔ AND THE SAME DEFECT ALSO BLOCKED THE COMMIT -- CORRECTING THIS ENTRY'S OWN EARLIER TEXT

The section above says "the committed change". **That was written before the commit was attempted and
it is WRONG.** `.tools/safe-commit.sh` refused rc=1 with six owned-paths lane violations, one per
`infra/` path, each reading:

```
agent=0.9.0_WK_NFRA_OPSEC202609~5 not in permitted_agents -- WORKER: no NON-TERMINAL task order
at HEAD issued_to this serial names this path in its <paths> block
(ADHC_OWNPTH.005: the order is the grant; a missing path is a cut defect, never an override)
```

**The owned-paths lane gate resolves a worker's WRITE grant through the same `<issued_to>` field the
halt gate resolves ADMISSION through.** One stale field disables both. The `<paths>` block does name
these directories -- the @`775e6cf20a` amendment added them for exactly this purpose -- but no gate
can read a grant for a serial no order is issued to.

**Split by plane, measured on the one invocation:** 9 dispatched paths, **6 REFUSED** (both
`lambda_function.py`, both `.tf`, both `.build` zips -- all under `infra/`), **3 ADMITTED** (this
ledger entry, the surprise channel, the proof-of-spec instance -- all under `org/`). Every other gate
in that run passed first. Recorded as row `NFRA_OPSEC202609-Z-W5-S3`, BLOCKING/ARMED, same disarm
owner and same one-line disarm.

**`GIT_COMMIT_AUTHOR_OVERRIDE` was NOT used.** CLAUDE.md 14a names it as the audited escape for a lane
refusal; a `<paths>` entry the gate cannot reach is a cut defect and a blocking row, never an override.

⭐ **THE WORK IS NOT LOST.** The four edited text files are intact and unstaged in worktree
`C:/tmp/wk-opsec-3a-5` on branch `wk-NFRA_OPSEC202609-3A-5`, and a git-format patch of all four is
committed as a RECORD (never a source, never a build input, referenced by nothing) at
`org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~5/OP3A-s-1.exchange-migration.WORKTREE-ONLY.patch`
-- 140 lines, 8003 bytes, sha256 `a5bf2999bcbf7c1125eecd83ed28f0bbb41734786ba8e18b8ec6d9be0c9d8c24`.
Apply it back onto the four canonical paths with `git apply`.

### WHAT THIS ENTRY LEAVES BEHIND, STATED SO IT IS NOT DISCOVERED LATER

⚠ **The change is DESIRED-not-APPLIED on BOTH planes -- not committed AND not applied.** Once it IS
committed, `infra/aws/terraform/opal-gateway` will carry **three** pending in-place changes: the two
`aws_wafv2_ip_set` descriptions that were already there (`0.7.0_AE_CloudOps`'s, row `Z-W5-S1`) and
these two Lambda functions. **Anyone applying this root untargeted lands all of them.** The
remaining act, once `<issued_to>` is corrected, is: `git apply` the patch (or use the worktree), one
scoped commit, then a single command by an admitted principal:

```
terraform -chdir=infra/aws/terraform/opal-gateway plan -input=false \
  -target=aws_lambda_function.otp_liveness -target=aws_lambda_function.ms_ingest_liveness -out=<plan>
.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -input=false <plan>
```

then steps 7 and 8. **Whoever performs it must re-read `/otp/health` and `/ms/health` immediately
before invoking**, because both functions carry an SNS + SES alert branch and a probe run against an
unhealthy gateway fires it.

## Push state

**LOCAL** on worktree branch `wk-NFRA_OPSEC202609-3A-5` -- a MEASURED value, read as
`git rev-parse HEAD` on the branch with no push attempted and none permitted: a worker never pushes,
and the integrator's merge and push are downstream of this entry. **This branch is not on origin.**
The claim is perishable and ages the moment an integrator runs.

## Escalation

Step 6 was blocked and is escalated by the artifact rather than quietly retried: row
`NFRA_OPSEC202609-Z-W5-S2`, BLOCKING/ARMED, disarm owner `2.0.0_SA_COO~Z` (the order's own
`<issued_by>`). If steps 7 and 8 are later performed and fail, roll back to the two
`source_code_hash` values above and escalate loud with the apply's own output.

-- `0.9.0_WK_NFRA_OPSEC202609~5`
