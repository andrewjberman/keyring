# IR BK: YCharts session capture, REST serving, and bounded recovery

Author: **4.0.0_SA_CRO**. Andrew-directed experiments, September 10, 2026 Eastern; experiment timestamps cross into September 11 UTC. **Midstream L1 supplement to IRPT_BCKEND**, macro IRPT / D9. Consumer: CTO for the existing backend project's endpoint/PRD integration. This does not register another project or issue task orders.

The chosen direction is unchanged: use the **BDAPI Node/Playwright/Kimi runner on a transient, dedicated EC2 host** to acquire YCharts authentication; use ordinary REST workers for report operations when transport portability is proven. Carry forward Inflection's refresh-and-resume behavior with explicit session generations and bounded retries. This research produces runnable probes and failure-injection evidence; it does not claim a working cloud deployment.

**Current result, September 11 01:42 UTC:** Andrew corrected the credentials and explicitly requested Secrets Manager storage. The new version was saved and verified; login succeeded. Browser fetch, plain Node HTTP, and a subsequent separate process with the browser closed all retrieved the expected Overview template. The separate process also matched the expected account email in dashboard HTML; its session-free template control returned 403. See VI.4. Cloud portability, report creation and PDF output remain unproven.

**Earlier K3 amendment, September 10 Eastern / September 11 UTC:** Andrew selected `kimi-k3` and separate 2500-token read / 400-token action calls. That controller cleared live YCharts AWS WAF CAPTCHAs. Encrypted local cookies retained that clearance across fresh browser runs. Probe 09 correctly submitted the former stored credentials and received a rejection, subsequently resolved by the credential correction in VI.4. The original K2.6 failures remain dated baseline evidence.

## PART 0 - Midstream constraint and where it bent

No current task orders or project `phase` / `blocking` fields were read to formulate this supplement. Sources were Andrew's request, the existing IR briefs/design, actual runtime code, historical BDAPI/Inflection architecture and logs, and new experiments. The context leak is explicit: this seat previously reviewed the IR frontend/backend v0.4 PRDs and signed their brief coverage; their component vocabulary and ownership are already known. Scoped searches also surfaced new IR backend source directories. Those do not establish completion and are not ratified by this document.

## PART I - Outcome territory

### O1 - An advisor can obtain the requested analysis without supplying a YCharts session

An authorized advisor requests an Overview, Comparison, or Multi-Comparison analysis using resolved holdings and comparison inputs. A currently verified session serves it directly; a missing or unusable session causes a bounded acquisition attempt. The advisor does not copy cookies or manage a browser. The Analysis tab receives the same firm-authorized job/result contract already specified in IR FE and IR BK.

### O2 - An advisor can continue a request after session expiry or an Alyssa login

An advisor sees the request resume from its last verified stage after automation re-acquires authentication. Andrew explicitly accepts mutual displacement with Alyssa's shared login. This is not an invitation to an endless login contest: repeated displacement reaches a retryable or attention state with the original request preserved. It must not silently create duplicate portfolios or reports.

### O3 - An operator can distinguish a bad input, a blocked browser, and an expired session

An operator can identify which stage failed and take the appropriate action using sanitized request, refresh-attempt, SSM-command and session-generation evidence. A permission failure or malformed report is not reported as successful recovery. A WAF CAPTCHA, unavailable Kimi call, EC2 startup failure and invalid credentials are distinguishable conditions.

### O4 - An operator can recover concurrent requests without starting competing login runners

An operator can see one automation owner of the shared vendor login and the requests waiting on it. A verified new session can wake the appropriate waiters; old completion events cannot publish over the new session, wake the wrong request revision, release another owner's lease, or stop a newer attempt's host. Each firm's jobs and artifacts remain separately authorized even though the vendor login is shared.

### O5 - An analyst can trace a served report to the exact request and generation

An authorized analyst can inspect the report's input revision, template identity/version, effective settings, normalized holdings, vendor-object ownership, generation attempt, artifact validation and transformation provenance. A reported success means the expected output is available and validated, not simply that a vendor POST returned 201 or SSM returned Success.

## PART II - Boundary and owners

**IRPT_BCKEND owns** email/attachment ingestion, input analysis, firm/advisor authorization, the vendor session broker, browser capture, REST transport, durable generation state, reconciliation, report persistence and normalized sections. This supplement tightens that existing scope.

**IRPT_FNTEND owns** request/review interactions, the Analysis tab, useful progress/error presentation, Opal visual rendering and branded export presentation. FE receives sanitized state and authorized artifacts; it receives neither a YCharts password nor cookie bundle. No new UI flow is required merely to expose EC2/SSM implementation details.

**YALP_MDSRC is an existing shared-session consumer concern.** Its older market-data client reads `ycharts/credentials`. Its older capture Lambda expects a login at that same path. Do not overwrite that secret contract or create competing refresh schedules when connecting the new IR library. Coordinate a versioned adapter and a single refresh authority with the existing owner.

**ADVI_BDAPIMIG and ADVI_JWTRES are prior art**, not YCharts resource pools. Do not run YCharts work on BD49F instance `i-0fa1846f04ed7e337` or Inflection instance `i-081ae6aafb394fb1a`. CTO integrates these findings into the existing IR BK design and its normal review flow; CRO is not editing peer implementation or issuing deployment work here.

## PART III - Qualitative bar

### III.1 Verified authentication

Seeing a cookie, HTTP 200, a dashboard-shaped screenshot, EC2 Running, or SSM Success is insufficient. A session is usable only after the intended authenticated identity and an expected report-capable response shape are verified from the transport that will use it. The generic market-data probe alone does not prove report entitlement. An expired, absent, wrong-identity or unverified bundle must fail closed.

### III.2 Recovery preserves work

Recovery resumes the same authorized immutable request revision and checkpoint. Freshness is a verified new generation, not a timestamp that merely advanced. Read retries, authentication recovery, browser challenges, launch retries and ambiguous vendor mutations have distinct budgets and decisions. Proposed experiment limits are engineering configuration, not ratified latency or availability promises.

### III.3 Ordinary serving stays simple

A healthy session should avoid starting a browser host for each report. If live proof shows a YCharts WAF token cannot travel from capture host to the intended REST worker, that is a measured transport constraint. Retain the earlier annex's authenticated-page request option as a bounded fallback only for the affected operations; do not describe browser-mediated requests as proven Lambda REST serving.

### III.4 Credentials and tenant boundaries

Passwords stay in Secrets Manager and browser memory. Session cookies stay in a protected session bundle. Kimi receives only necessary public or masked login/challenge pixels; it does not receive client holdings, authenticated report pages, passwords or cookie values. Model output selects from constrained actions and never establishes success by assertion.

Firm/advisor claims are rechecked against the server's request ledger before vendor mutation and artifact delivery. Native vendor portfolio IDs are accepted only through a firm-scoped ownership mapping. A shared login or global template catalog does not confer access to another firm's request, portfolio or PDF.

## PART IV - Findings and proposed implementation contract

### IV.1 FINDING: BDAPI supplies the requested runner pattern

Measured source paths:

| Source | Reuse / adaptation |
|---|---|
| `docs/architecture/ADVI_BDAPIMIG_PRD.md` | Separate authentication capture from normal REST data requests; keep per-firm secrets and data planes explicit. |
| `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` | Node, Playwright/Chromium, Kimi state perception, bounded model retry, DOM fallback and verified cookie capture. The Kimi call has a 30-second socket-idle timeout; a hung call previously defeated retry. |
| `infra/aws/ec2/bd-49f-auto-login/run-bd-auto-login.sh` | Artifact deployment and invocation style. The checked-in wrapper uses native AWS egress; the JS header's always-on proxy statement is stale. |
| `infra/aws/terraform/bd-49f-auto-login/{main.tf,instance.tf,iam.tf}` | Dedicated host/role/profile/security-group pattern. Adapt privileges to YCharts. |
| `infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py` | Probe, start host, wait for Running and SSM Online, send a command, process completion, stop host and invoke the intended continuation. |
| `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` | REST consumer separation. BD's identity-to-DataMining-token exchange is provider-specific and must not be copied into YCharts. |

The BD controller's marker age/allowlist safeguards are useful, but a global marker and staggered cron do not supply concurrency control for interactive YCharts jobs. Preserve normal TLS verification. Do not inherit BD OTP/device-trust branches, broad source-account IAM grants or proxy/TLS exceptions.

### IV.2 FINDING: Inflection already has recovery-and-resume

`docs/architecture/ADVI_JWTRES.md` and `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-05-01/session_wrap_014.md` identify the implemented `recover_or_exit()` path. The historical log cites source `a63d76d51`, IAM change `e3325b6d4` and release `inf-pipeline-v1.7.12`; these are dated historical references, not a new live deployment measurement.

Current inspected code:

- `infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/jwt_freshness.py`: check freshness, invoke `inf-jwt-trigger`, wait for token metadata to advance, reload and recheck, then resume or fail explicitly.
- `infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py`: EC2/SSM refresh control; subsequent Eclipse-token derivation has its own success/failure boundary.
- `infra/aws/lambda/inf-pipeline/inf-ec2-retry-launch/lambda_function.py`: launch-failure-specific retry with a DynamoDB lock; not a generic retry of every vendor failure.

Adapt the behavior, not the JWT assumptions. YCharts cookies/WAF state are not Orion JWTs. Inflection's long polling loop is not a reason to occupy a report Lambda for its full lifetime; use durable waiting and a completion event. AWS can redeliver asynchronous Lambda events, and Run Command status changes can drive EventBridge, so continuation handlers must be idempotent. [Lambda asynchronous errors](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html), [SSM events](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-events.html).

### IV.3 FINDING: Kimi CAPTCHA prior art is a framework, not a YCharts proof

`tools/astn_wsjft/scripts/harvest_ft_session.js` contains a Kimi-guided hCaptcha tile loop. Its own status says synthetic localization passed and the live challenge selectors/geometry still need tuning. A different vendor's challenge is not a reusable solved YCharts puzzle. Keep the BDAPI model-health timeout/retry/fallback pattern, inspect the actual YCharts challenge, constrain actions to its visible controls, and verify the result using the vendor response.

The initial K2.6 browser experiments reached HTTP 405 and an AWS WAF script before any password submission. Waiting alone did not reveal the login form. AWS documents 405 for its CAPTCHA action and 202 for its automatic Challenge action; confirm `x-amzn-waf-action` and actual page state rather than classifying every 405 as authentication expiry. [AWS WAF action behavior](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-actions.html). The later K3 experiments in VI.3 provide actual YCharts puzzle-clearance evidence.

### IV.4 FINDING: existing YCharts code cannot be reused unchanged

`infra/aws/lambda/ycharts-session-capture/index.mjs` is a Puppeteer/container-Lambda implementation with provisional login selectors, not the requested EC2/Kimi runner. Its `LOGIN_SECRET_ID` is `ycharts/credentials`; the new runner's login input is `ycharts/login/credentials`. `infra/aws/terraform/ycharts-pipeline/{main.tf,lambdas.tf}` reflects that older arrangement.

The actual `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py` was exercised with injected HTTP responses and no network calls:

| Injection | Actual legacy behavior | Required behavior for IR |
|---|---|---|
| 200 with HTML login body | `freshness_probe()` returns true. | Reject unexpected content/schema; determine authentication from corroborating evidence. |
| 201 with JSON `report_url` | `_request()` omits parsed JSON. | Parse the expected successful creation response and verify it, then download/validate the artifact. |

This is evidence against copying the transport unchanged, not a claim that legacy market-data production returned those responses today. The legacy client's raw error-body logging also needs a sanitized adapter for client-report operations.

### IV.5 Proposed runtime and library boundary

Logical interfaces below belong in IR BK's implementation. Suggested homes are `infra/aws/ec2/ycharts-auto-login/` for the dedicated runner and the existing `infra/aws/lambda/investor-reporting/` package for the session/REST/job adapters; CTO should converge with its owner before choosing exact modules. This brief only adds research files under `docs/research/`.

```text
probeSession(sessionVersion, capability, transport) -> verified | classified_failure
ensureSession(accountKey, priorGeneration, reason, attemptId) -> ready | refresh_wait
captureSession(attemptId, fence, loginSecretRef) -> candidateVersion | classified_failure
completeRefresh(attemptId, fence, commandId, candidateVersion) -> published | rejected
resumeRequest(firmId, requestId, revision, checkpoint, generation) -> next_durable_state
```

`accountKey` identifies the single shared vendor login, not the tenant. `firmId` and request ownership remain mandatory in the job layer. Public response states should be useful equivalents of queued, preparing analysis, generating, input needed, retryable delay and ready; detailed auth/SSM states belong in operator evidence.

The controller uses the BD start/SSM/completion/stop pattern with an account-scoped durable conditional lease. Retain `attemptId`, monotonically advancing fence, lease expiry, host ID and SSM command ID. Bound each wait, retry and total attempt. Only the active owner may publish or control its host. The watchdog must use the same ownership checks. A stale cleanup must not stop a new owner's instance.

Use a durable job wait/event continuation rather than keeping Lambda busy through browser startup. Accept SSM Success only for the expected command and current attempt, then independently verify the candidate session. A successful capture must be usable by the intended report worker before waiting jobs proceed. An empty or missing secret is a capture requirement, not a reason to try an unauthenticated report POST.

**No OTP workflow.** An unexpected OTP/MFA prompt becomes a distinct unsupported-challenge outcome. Do not fake BD's `otpEntered` condition. Andrew's latest model choice is **`kimi-k3`**, replacing the initial K2.6/1500-token experiment. Use two calls: 2500 completion tokens for observation, then 400 for a constrained action, both with low reasoning effort in the final tested controller. K3 always reasons; its supported effort setting replaces a thinking-disable assumption. [K3 settings](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart). The budgets and retries remain versioned engineering inputs.

### IV.6 Proposed session record and publication

Read credentials from `ycharts/login/credentials`, read the model key from `astn/kimi/api-key`, and use `ycharts/session/current` as the intended session resource with an explicit versioned contract. Preserve `ycharts/credentials` for legacy consumers until a coordinated adapter is approved through the existing project.

The protected bundle includes schema version, generation/attempt/fence, capture timestamp, authenticated identity, browser/UA context, cookie jar with domain/path/expiry/secure attributes, CSRF/WAF state and successful probe metadata. Store no password there. Cookie age is advisory; a capability probe is authoritative. Maintain Set-Cookie updates and the headers observed in the HARs, including `X-CSRFToken` for mutations and `X-AWS-WAF-Token` where required; `credentials: include` does not add those custom headers.

**Fence publication as well as acquisition.** Proposed implementation: write an immutable candidate Secrets Manager version, then conditionally publish its exact VersionId/generation in the account coordinator only while the attempt owns the lease and all checks pass. Readers fetch that accepted VersionId. A stale candidate is never sufficient to resume work. Do not pretend that separate DynamoDB and Secrets Manager writes are one transaction. If compatibility requires AWSCURRENT, a single controlled publisher manages that label and consumers' migration explicitly; the coordinator's accepted version is authoritative.

Secrets Manager versions are immutable and `ClientRequestToken` can make the same candidate write idempotent. Omitting staging labels can move AWSCURRENT automatically; account for first-version behavior, candidate cleanup and version quotas. Repeated requests must not rewrite the secret merely to record probe timestamps. [PutSecretValue semantics](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html).

### IV.7 Proposed REST/retry decisions

| Observation | Decision |
|---|---|
| Expected authenticated response and schema | Continue from current checkpoint without starting EC2. |
| Explicit 401 or verified concurrent-login eviction | Coordinate one refresh attempt, require a new verified generation, then resume the safely retryable stage. |
| 200 HTML / wrong JSON shape | Never healthy; inspect redirect/login/WAF evidence. Unknown schemas are protocol failures, not permission to loop logins. |
| WAF action/header/interstitial | Browser challenge handling; do not treat as bad holdings, wrong password, or blanket authorization denial. |
| Unrelated 403 or invalid inputs | Preserve permission/input failure; no generic login retry. |
| 429 or transient read failure | Respect Retry-After where present and use bounded jitter/backoff; no auth-refresh storm. |
| EC2/SSM launch failure | Dedicated launch recovery with the same attempt/ownership controls; no vendor POST replay. |
| Timeout/disconnect/ambiguous 5xx during upload, portfolio creation or report generation | Mark outcome uncertain; reconcile the owned vendor object or artifact before any replay. |
| 201 report creation | Parse and validate expected URLs/status, then fetch and validate the PDF. Creation success is not delivery success. |
| Repeat eviction after the allowed refresh | Preserve request; surface retryable/attention state with evidence, not an endless automated contest. |

The harness's one-refresh rule and 20-waiter scenario are test bounds, not claims about throughput. HTTP class alone cannot prove an ambiguous mutation did not execute. Use a request/revision-derived opaque vendor name and stored returned IDs; never deduplicate across firms by a user's display name. No vendor idempotency guarantee was established in this research.

### IV.8 Report contract and evidence continuity

Carry forward `investor-reporting-ycharts-design-20260910.md` sections 3-6 and the supplied HAR fixtures. The captured template IDs are Overview `14141822`, Comparison `14141824` and Multi-Comparison `14141847`; validate current accessible templates and their report types before using them. These are discovered vendor identities, not permanent API guarantees.

Known flow: resolve securities/holdings; perform the actual upload; create the owned fixed portfolio; submit the versioned template payload to `POST /custom_pdf_reports/{id}`; process the synchronous 201 response; retrieve and validate the PDF; persist and transform it for the Opal section contract. The supplied HAR packet omits the holdings-upload multipart field name and output PDF bytes. **VI.5 closes those two gaps for a synthetic Overview flow:** the current vendor JavaScript declares field `holdings`, a live Lambda upload accepted it, and the subsequent generated PDF was downloaded and parsed. Comparison and Multi-Comparison still require their own live output proof.

Report generation is a job, not an advisor-facing synchronous Lambda request. Measure its real duration against the worker's configured budget. If it exceeds the normal Lambda budget, select an appropriate durable worker; do not assume a timeout licenses regeneration. Route artifact downloads only to observed/configured hosts, follow redirects under that allowlist, and never forward the YCharts session cookie to a signed object-storage URL. Validate complete PDF content, expected report variant and owned request association before declaring ready.

Preserve the existing settings and revisions, including the specified annual management fee and the distinction between captured July settings and the chosen August recipe. Do not mutate Alyssa's global preferences as part of a report job. Retain raw generation artifacts and normalized/report manifests under encrypted `opal-data-ycharts` firm/request/revision/attempt prefixes, following the existing IR BK contract. Cookie bundles do not belong in that bucket. The email poller remains every day, every 15 minutes between 08:00 and midnight Eastern; polling is not a login schedule.

## PART V - Preconditions without task-order sequencing

These dependencies are required evidence boundaries, not a new decomposition:

- A dedicated YCharts EC2 runtime, declared IAM/SSM/artifact deployment, native egress and browser package versions, with measured start/capture/stop behavior.
- The locally proven K3 YCharts CAPTCHA controller exercised on the dedicated cloud runtime; the FT hCaptcha framework alone is not sufficient proof.
- An authenticated identity/report-capability probe whose expected schema is verified, plus EC2-capture-to-Lambda-replay evidence. Local browser evidence cannot establish cloud portability.
- A durable lease/fence and request ledger implementation, fault-tested against duplicate starts, stale completion, partial secret publication, timeout and cleanup races.
- Coordination with existing YALP_MDSRC session consumers and schedules so they do not continually evict the new runner.
- Representative holdings attachments and the live upload field contract, output PDF examples for all three variants, template/settings fixtures and report-to-request ownership reconciliation.
- The existing mailbox grant, firm/advisor routing rules, artifact encryption/authorization, and an established operator destination for exhausted failures.

## PART VI - Status: NOT OUTCOME-BEARING

### VI.1 Initial K2.6 and offline experiments

Evidence lives in `docs/research/investor_reporting_ycharts_auth_20260910/`:

- `probe_session.cjs` is a bounded Node/Playwright/Edge experiment with explicit `--login-once`, `--kimi` and `--solve-captcha` options, public login/challenge perception and constrained actions, in-memory credentials/cookies and browser-versus-HTTP read probes. It does not publish a session, upload holdings, create reports or mutate AWS resources.
- `local_probe_01.json` through `local_probe_05.json` contain clocks, interim source hashes and sanitized observations, spanning **2026-09-11T00:22:16.520Z to 00:37:34.537Z**. Browser routes returned 405. Waits observed the AWS WAF script without a login form. No login credentials were submitted and no authenticated report read was reached. Probe 02 also hit a local AWS command-shim invocation defect; the final script invokes the canonical Windows `aws.cmd` through PowerShell rather than attempting direct Node execution.
- Probe 04 received a successful Kimi response classifying the public interstitial as **CAPTCHA**. Probe 05 enabled the bounded action controller, but both classification calls failed before a usable response was available; consequently **no CAPTCHA action executed**. This establishes neither a reliable Kimi transport nor a solved puzzle. The next implementation proof must cover both model failure/fallback behavior and actual challenge interaction. No raw model response or screenshot was retained.
- `recovery_contract.py` is an executable **in-memory research model**, not a deployed broker. `test_recovery.py` runs **14 passing offline tests**, including the two actual legacy-code findings, response classification, 201 parsing, unknown-mutation reconciliation, 20 concurrent waiters, stale-owner rejection and verified-generation resume. `recovery_results.json` records its clock and source hashes.
- `source_evidence.json` supplies measured source hashes and experiment inventory. Node syntax validation also passed. No claim is made that a generic repository gate exercised AWS or YCharts.

### VI.2 Existing secret state observed in this research

Safe `comp-secrets` inspection found `ycharts/login/credentials` with username/password fields, `astn/kimi/api-key` present, and no AWSCURRENT value available for `ycharts/session/current`. No secret value is included in these documents or probes. Presence is not proof that the vendor accepts the credentials. The initial tests stopped before credential submission; probe 09 in VI.3 reached an explicit rejection. A subsequent safe metadata check confirmed the then-stored username matched Andrew's originally requested account, both fields had no surrounding whitespace, and the password was nonempty. No credential guess or replacement was performed during those initial tests. Andrew's later correction and authorized secret update are recorded in VI.4.

### VI.3 K3 split-call experiments and former credential blocker

Current research modules: `kimi_split.cjs`, `probe_split_session.cjs`, `login_form.cjs`, `local_checkpoint.cjs`, `test_kimi_split.cjs`, and `test_login_form.cjs`, all under `docs/research/investor_reporting_ycharts_auth_20260910/`. `k3_evidence.json` pins the current modules, historical results and isolated test run. Earlier result hashes identify earlier revisions; they are not relabeled as the final source.

| Evidence | Measured result |
|---|---|
| `split_k3_probe_01.json` | The separate actor produced a usable action even after a reader exhausted its 2500-token allowance. The run was stopped to correct stale-image/single-tile behavior; it did not establish login. |
| `split_k3_probe_02.json` | A grid batch cleared the puzzle into the public dashboard. A missing sign-in transition caused the original blocked outcome; the separate reviewed observation preserves that distinction. |
| `split_k3_probe_03.json` | Two CAPTCHA actions, four K3 calls, and a verified transition to the login form. Its older credential selector was not yet correct. |
| `split_k3_probe_04.json` | Stopped after repeated image-change rejections with slower high-effort reads. Partial evidence does not count every rejected step. |
| `split_k3_probe_05.json` | Final low-effort 2500/400 configuration cleared the CAPTCHA with two actions and four calls. Saved an encrypted local pre-login cookie checkpoint. Its older form selector still prevents interpreting its login error as a correct credential test. |
| `split_k3_probe_06.json`, `split_k3_form_07.json`, `split_k3_probe_08.json` | Cookie restore avoided another CAPTCHA. Form inspection identified `auth-username` / `auth-password`. Earlier page-wide email and Sign In selectors were unsuitable. Probe 08 increments a counter before a click that times out; its counter is not a verified POST. |
| `split_k3_probe_09.json`, 01:25:26.128Z-01:26:02.482Z | Restored the solved challenge, submitted once through the actual login form, observed the POST, and verified both submitted fields exactly matched Secrets Manager. YCharts returned 200 on the login page with its incorrect-email/password message. No MFA, concurrent-session or CAPTCHA message was detected. No authenticated report GET was attempted. |

The reader describes every matching unselected tile and Confirm. The actor returns one bounded batch so repeated read latency does not leave a half-selected puzzle. The controller compares the full screenshot again before acting; a changed image rejects the plan. This is conservative and can reject cosmetic changes as well as puzzle changes. Reader/actor deadlines are 180/60 seconds, each with one retry; the controller permits at most 12 iterations. Empty or invalid actor output authorizes no click. Raw external reasoning stays in memory and can feed the separate actor when the reader's final text is exhausted; it is never logged or committed.

The model receives only the explicit public CAPTCHA page. Normal account pages are excluded. The login helper scopes fields to the form containing the visible password, captures field names before navigation, submits with Enter, and counts actual observed POSTs. Six isolated tests pass, including a real Edge fixture with a preceding newsletter email and hidden native submit; that test preserves the form's CSRF and wizard fields and verifies the transmitted credentials without logging them. This fixture is not a live successful login.

Research cookies are protected with Windows DPAPI CurrentUser at `.runtmp/ycharts-k3-probe.cookies.dpapi`; no plaintext cookie file, AWS session publication or production login runner was created. Cookie restore has been demonstrated for WAF/pre-login state only. Reuse of an already authenticated checkpoint still needs an identity/capability fast path and live proof. Do not promote a solved CAPTCHA cookie to a verified authenticated session.

**Probe 09's prerequisite was a vendor-accepted credential secret**, resolved in VI.4. Repeated identical rejected submissions were stopped until Andrew supplied the correction. The next transport boundary is dedicated EC2 capture to Lambda replay before report generation. No alternative CAPTCHA service is required by the evidence so far.

### VI.4 Corrected credential storage, accepted login and separate-process REST replay

Andrew supplied replacement credentials in this Codex session and explicitly authorized saving them. They were entered through hidden console input into an in-memory SDK update, preserving the existing secret's other fields. The exact resource is **`ycharts/login/credentials`, `us-east-1`**, new AWSCURRENT version **`e6b721ac-8d36-4042-9b85-e571fca68bc8`**. Readback verified both supplied values at **2026-09-11T01:39:16.145515+00:00**. `credential_update_20260911.json` contains this metadata and no credential values. No password was written to a source/evidence file or used as a command-line argument.

`split_k3_probe_10.json` covers **01:39:29.720Z-01:39:52.396Z**. The login POST returned **302**, both transmitted fields matched the updated secret, and the dashboard's inline scripts contained the expected account email. Browser fetch and ordinary Node HTTP each returned **200 JSON** for the market probe and the existing Overview template. Both template responses matched ID `14141822`, type `aggregate_security_overview`, and an array-valued `sections`. Correction from VI.5: the saved template legitimately returns an empty array, so the earlier phrase “populated sections” overclaimed. The runner's historical outcome label still says identity not yet verified; the recorded email match is corroboration, not a newly verified dedicated identity endpoint.

`probe_rest_checkpoint.cjs` then ran in a **separate Node process with no browser import**, restoring only the protected local cookie checkpoint. `rest_checkpoint_probe_11.json` covers **01:41:53.981Z-01:42:01.239Z**:

| Request | Observed result |
|---|---|
| Overview template with only WAF state, no authenticated session | 403 plain text; no template schema. |
| Same template with restored authenticated cookies | 200 JSON; expected ID/type/sections. |
| Dashboard with restored authenticated cookies | 200 HTML containing the expected account email read from the current credential secret. |

This run used Node's default user agent, not the browser user agent. It launched zero browsers, called Kimi zero times, submitted zero logins, and performed no cloud or business-data mutation. It proves the local browser-to-ordinary-HTTP handoff and an observed need for the authenticated session on that template route. It does not prove that a token captured on EC2 will work from Lambda's egress. Account email is corroborated in the authenticated response; a dedicated identity contract remains to be selected and verified.

Use the REST checkpoint probe first for a healthy local session. The login and REST probes remain separate research entry points; they do not implement a production lease/recovery orchestrator. The REST probe does not persist Set-Cookie updates, which the production transport must handle. No holdings upload, report POST or PDF download was performed. The credential secret is saved in AWS; the captured session remains local DPAPI research state and was **not published to `ycharts/session/current`**.

### VI.5 Andrew-directed EC2/Lambda and synthetic report proof

Andrew explicitly requested live testing of the boundaries listed after VI.4. The packet is **`docs/research/investor_reporting_ycharts_cloud_20260911/README.md`**, with exact source modules, sanitized per-stage evidence and cleanup receipt. It belongs to the existing **IRPT_BCKEND** project.

| Requested boundary | Live result on 2026-09-11 UTC |
|---|---|
| Session captured on EC2 works from Lambda egress | **Passed in isolation.** Dedicated EC2 `i-0167fd745ad906a66` captured fresh generation `a6ba5b05-456e-4120-9f12-c4659d375785` at 02:29:30-02:30:45; Lambda outside a VPC replayed it, without a browser, for authenticated template retrieval and all later operations. |
| Identity beyond email appearing in HTML | **Structured contract demonstrated.** Parse `window.USER` JSON: authenticated true, positive integer user ID matching the capture, expected credential email, no impersonation. Wrong-ID control rejects; production should pin the enrolled account ID. This is not a newly discovered documented identity API. |
| Cookie persistence | **Actual Set-Cookie/store/reload demonstrated in the test Lambda.** Later invocations read preceding secret versions. Live changes included a page-view counter and expiries; real auth-token value rotation and production concurrent-writer safety remain unproven. |
| Session publication | **Isolated publication/readback passed** in `ycharts/session/research-20260911`. The production `ycharts/session/current` remains untouched; its competing readers require a coordinated schema cutover. |
| Holdings upload and save | **Passed.** Multipart field `holdings` accepted SPY $60,000 + AGG $40,000 with no errors. Multipart JSON fields `portfolio`/`items` then created synthetic portfolio **2332060** (201). |
| Report creation | **Passed for Overview 14141822.** Full HAR-shaped generation state and current selected template returned 201 in a 26.76-second invocation. A smaller payload had returned 404; do not classify that response as automatic session expiry. |
| PDF download | **Passed.** Separate unauthenticated storage client downloaded 573,643 bytes; pypdf parsed 23 pages containing the synthetic title, SPY/AGG and 60%/40%. Cover visually checked. Encrypted S3 artifact retained. |

The second proper cloud CAPTCHA attempt succeeded using **Kimi K3 reader 2500 / actor 400, low effort**, two actions and four model calls. The first stopped safely and released its lease. This is functional evidence, not an availability estimate. Host runtime provisioning and the Node-to-CLI stdin adapter initially failed; the isolated runtime and Python boto3 SDK bridge resolved those prerequisites. Raw credentials, cookies, signed URLs and model reasoning are absent from committed evidence.

The synthetic portfolio initially rejected a zero annual management fee with 422 `invalid_management_fee`; using the captured 0.003 annual recipe succeeded. This does not change the approved report settings or establish a default for other advisors. The full generation request added `generationModalsState`, a current `selectedReport`, and its disclosure together; individual field necessity was not isolated.

Sources to carry: `capture_ec2.cjs`, `cloud_transport.py`, `package_experiment.py`, `test_cloud_transport.py`, `ec2_capture_02.json`, `lambda_probe_02.json`, `lambda_upload_01.json`, `lambda_create_02.json`, `lambda_generate_02.json`, `lambda_download_01.json`, `pdf_validation.json`, `lambda_deployment.json`, and `cleanup.json` in the new packet. The source-only packager places the already-proven K3/login helpers next to the EC2 entry point. The PDF is `s3://opal-data-ycharts/research/20260911/irpt-synthetic-20260911-6040/report.pdf`, SHA-256 `10465c26bde0d93e6f881e69c1c9c6940c9138d3670a4c1134f407232226c64a`.

Cleanup was measured at **02:52:47 UTC**: EC2 stopped, temporary Lambda and its role/policy absent, temporary EC2 secret-access policy absent, and no experiment-owned lease. Terraform `infra/aws/terraform/investor-reporting/ycharts-research-20260911/main.tf` defaults to `active=false`; safe-apply removed four temporary resources. The isolated secret, encrypted artifacts, seven-day log group, stopped-host research runtime and synthetic vendor portfolio remain as research state. No schedule or production cutover was created.

### VI.6 One Lambda, three deterministic report recipes: live middle-operation proof

Andrew clarified that the immediate deliverable is the operation between firm/advisor-scoped UI inputs and a generated report: one Lambda selects Overview, Comparison or Multi-Comp from the chosen comparisons. The implementation, source reconciliation, UI contract and live evidence are in **`docs/research/investor_reporting_ycharts_variants_20260911/README.md`**. The direct frontend handoff is `UI_CONTRACT.md`; the internal synthetic fixture is `manifest.example.json`; shared recipe and worker code are `recipe_contract.py` and `variant_worker.py` in that directory. This extends the existing IRPT_BCKEND/IRPT_FNTEND projects.

The UI selects client, account(s), immutable holdings snapshot and ordered comparisons, with optional title/profile overrides. The server derives firm/advisor scope from authentication, verifies entitlements, resolves typed securities and freezes the envelope. Zero comparisons selects Overview 14141822; one selects Comparison 14141824; two to five selects Multi-Comp 14141847. `resolved` is an internal server context, never an authorization claim accepted from the browser. Account numbers are display/internal references, not YCharts portfolio IDs.

| Actual Lambda output, 2026-09-11 UTC | Binding | Validated result |
|---|---|---|
| Overview, 03:48:59-03:49:13 | Synthetic portfolio 2332257 | 23 portrait pages; 573,677 bytes. Resumed an existing generated response after a dependency repair. |
| Comparison, 03:49:29-03:50:06 | Same portfolio + Opal Long-Term P:1728413 | 31 portrait pages; 820,984 bytes. |
| Multi-Comp, 03:50:22-03:50:53 | Same portfolio + Short-Term P:1728415, then Intermediate-Term P:1728315 | 35 landscape pages; 854,115 bytes. |

All three used SPY $60,000 / AGG $40,000 and the captured August 0.003 annual-fee recipe. Each verified title, selected comparison names, orientation, PDF structure/pages/hash; local parsing also found SPY/AGG and each cover was visually reviewed. The Lambda launched no browser or Kimi call. Three live duplicate requests reused their artifacts without retrieving a session or contacting YCharts. Changed inputs under an existing request ID and inconsistent account bindings rejected before vendor access. These checks prove the synthetic contract, not real tenant-directory authorization or an independent recalculation of every financial statistic.

The experiment exercised two useful resume boundaries. A WAF challenge after portfolio creation preserved the returned ID; an operator-triggered EC2 refresh using **Kimi K3, reader 2500 / actor 400, low effort** published a verified isolated session, and the same request resumed without another portfolio POST. The first capture stopped safely; the second succeeded. A missing AES parser dependency after report creation was repaired by packaging Linux PyCryptodome; the request resumed from the saved report URL without another generation POST. These are measured checkpoint resumes, **not an autonomous cloud recovery loop**.

The deployed package hash, source hashes, per-invocation results, PDF hashes, duplicate/negative controls and cleanup receipt are retained in the new packet. Exact ZIP SHA-256: `2826b9c946fe012f940048e7620f520649808350c23d324a195808a6782b6f5d`. The same isolated Terraform root now supports the recipe handler, reserved concurrency 1 and scoped S3 existence lookup; it still defaults to inactive. Cleanup readback at **03:54:10 UTC** confirmed EC2 stopped, Lambda/role and temporary capture policy absent, and no experiment-owned lease. Encrypted research artifacts, the isolated session, synthetic portfolio 2332257 and three reports remain. Production session/current, PRDs, peer task orders, API routes and schedules were not changed.

Use the new packet to replace the remaining assumption that each report needs browser interaction. Actual email/attachment normalization, firm/advisor cache resolution, queue/API connection, enrolled account identity, error-specific automatic recovery, session publication fencing and final Opal presentation remain integration work. Public-security comparisons, the five-comparison maximum and percent-unit uploads were not live tested in this proof. No custom downside controls were inferred from the HARs.

## PART VII - What this brief does not claim

VI.5 and VI.6 extend the earlier local evidence through **isolated EC2 capture, session publication, Lambda replay, cookie persistence, synthetic holdings/portfolio creation, all three report recipes and validated PDF retrieval**. They do not prove production session publication, coordinated legacy-consumer migration, real authentication-token rotation, autonomous cloud fault recovery, concurrent publication fencing, or exhaustive financial/PDF fidelity. Capture's lease check and the secret write are separate operations; the test Lambda's persistence has no production compare-and-swap. The scripts are a repeatable research starting point, not the completed sensitivity service.

The earlier “only credential-secret update” statement is superseded for the cloud experiment. Authorized mutations now also include dedicated EC2 start/runtime installation/stop, temporary Terraform resources and teardown, DDB lease/fence writes, isolated session versions, source/artifact S3 writes, and one synthetic vendor portfolio/report. No production reader, PRD, task order or peer implementation was replaced. Identity enrollment, tenant/advisor authorization, email intake, error-specific automatic recovery, production cookie coordination and custom Opal rendering remain existing project work.

The local HTTP 405 result does not prove AWS egress will fail or that a proxy is needed. The research did not validate MFA/OTP because Andrew chose no OTP workflow. It does not re-open the two-project product split, make the native vendor PDF viewer the finished Opal tab, ratify a new service-level target or assert that YCharts offers a stable public report API.

## REFS TO CARRY

- **BRIEF PATH:** `docs/briefs/investor-reporting-ycharts-session-recovery-brief-20260910.md`
- **PROJECT:** `IRPT_BCKEND`, macro IRPT / D9; **SIBLING:** `IRPT_FNTEND`; existing consumer coordination with `YALP_MDSRC`.
- **EXISTING PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; frontend counterpart `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`. Prior brief-coverage review referenced v0.4 at `62301f71e03a0725a7f4bebf0770a438dfc8b371`; this supplement does not assert the current PRD state.
- **UMBRELLA BRIEFS:** `docs/briefs/investor-reporting-ir-bk-brief-20260910.md` and `docs/briefs/investor-reporting-ir-fe-brief-20260910.md`, including their full four-brief/five-supporting-document maps.
- **YCHARTS SOURCE:** `docs/briefs/investor-reporting-ycharts-brief-20260910.md`; `docs/briefs/investor-reporting-ycharts-design-20260910.md`.
- **SOURCE EVIDENCE:** `docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_HAR_EVIDENCE_20260910.json`; `docs/briefs/sources/INVESTOR_REPORTING_YCHARTS_SOURCE_EVIDENCE_20260910.json`; `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`.
- **PRIVATE INPUTS:** `C:\Users\AndrewBerman\Desktop\YCharts Transcripts` (transcripts, manifest and HAR handoff). Read locally; do not attach raw HARs, secrets or client data to the CTO message.
- **PRIOR ART:** exact paths in IV.1-IV.4; dated Inflection log in IV.2. Source hashes and experiment clocks are in `docs/research/investor_reporting_ycharts_auth_20260910/source_evidence.json` and each result JSON.
