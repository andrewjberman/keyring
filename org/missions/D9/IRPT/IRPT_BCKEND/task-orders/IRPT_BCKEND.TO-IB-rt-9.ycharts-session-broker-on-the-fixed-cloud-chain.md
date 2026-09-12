# TO IRPT_BCKEND.TO-IB-rt-9 -- YCHARTS ON THE v0.9 MECHANISM: IB-s-8 recut to the fixed cloud chain -- the session broker built on the CRO's packet (K3 capture on the dedicated host, fenced publication of a versioned session, the production ycharts/session/current cutover with every competing reader migrated and the legacy non-403 probe retired), proven on recorded fixtures; the live capture stays the qualified arm

<to_id>IRPT_BCKEND.TO-IB-rt-9</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- RE-OPENED by 0.9.0_WK_IRPT_BCKEND~3 at 2026-09-12T04:0xZ. The complete flip at 076bdb0973 rested on a run that no longer reproduces: arm (e)'s "gone from the tree" check took its baseline from HEAD~2, which was the pre-deletion commit on the run that passed and had become the DELETION commit itself two commits later, so a fresh run at HEAD read "down from 0" and FAILED. The WORLD is correct -- the absorption, the closed ledger and every other check still pass -- but RT9-AC1 PASSES BY OUTPUT and the output at HEAD did not. A relative ref as a baseline is a moving target. Fixed to self-locate: the deleting commit is found with git log --diff-filter=D and the baseline is that commit's parent, which cannot drift. Re-flips only on a run that reproduces at HEAD.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 6 (mechanism) | **Slug rows this cell closes:** W3-S1, W3-S2 | **Decomp cell:** `IB-rt-9` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-4 (contrib) | **PRD candidate:** B8

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-2-3` on branch `wk-irpt_bckend-2-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** second in slot ~3, after IB-rt-4. IB-rt-10 follows in this slot.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B8 YCharts session library + browser runner + the SESSION BROKER (v0.5)
- **serves:** FWD-4 (contrib)
- **brief sections consumed:** O4 session paragraph; IV.4 session pattern and paths, Secrets paragraph; **SUPP** O1, O2, O4; III.1, III.3, III.4; IV.1, IV.2, IV.3, IV.4, IV.5, IV.6; V
- **contracts (P=produces, C=consumes):** P `session bundle` (server-only, never a browser contract)
- **paths: reuse:** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js`, `run-bd-auto-login.sh`, `package.json`; `infra/aws/terraform/bd-49f-auto-login/{iam,instance,main}.tf`; `infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py` (probe, start host, wait Running + SSM Online, send command, process completion, stop host, invoke continuation); `infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py` (REST-consumer separation only -- BD's identity-to-token exchange is NOT copied); `infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/jwt_freshness.py`, `inf-jwt-trigger/lambda_function.py`, `inf-ec2-retry-launch/lambda_function.py` (recover-or-exit BEHAVIOR adapted; YCharts cookies/WAF state are not Orion JWTs; launch-failure retry is not a generic vendor retry); `tools/astn_wsjft/scripts/harvest_ft_session.js` (Kimi challenge FRAMEWORK only, another vendor's puzzle is not a solved YCharts one); `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py` (NOT reusable unchanged: accepts a 200 HTML login body as fresh, discards the 201 JSON -- both measured); `infra/aws/lambda/ycharts-session-capture/index.mjs` (Puppeteer container Lambda, provisional selectors, reads `ycharts/credentials` -- the legacy arrangement, not the runner); Secrets `ycharts/login/credentials` (login input), `ycharts/session/current` (the session resource, versioned contract), `astn/kimi/api-key`, `ycharts/credentials` (legacy, preserved for YALP_MDSRC); `docs/research/investor_reporting_ycharts_auth_20260910/{probe_session.cjs,recovery_contract.py,test_recovery.py,source_evidence.json}` (research model + 14 offline tests; a starting point, not the service)
- **paths: new home:** dedicated transient YCharts runner host + role + SSM document under `infra/aws/ec2/` (supplement suggests `ycharts-auto-login/`; L5 named `investor-reporting-ycharts/`) and `infra/aws/terraform/investor-reporting/`; the broker/session adapters in `infra/aws/lambda/investor-reporting/`; NEVER the BD49F instance `i-0fa1846f04ed7e337` or the Inflection instance `i-081ae6aafb394fb1a`
- **fixtures / evidence:** six transcripts + manifest + three HARs (private packet, offline profile `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`); the five local probes `local_probe_01..05.json` (2026-09-11 00:22-00:37Z: browser routes 405 with the AWS WAF script, no login form reached, no credential submitted; Kimi classified the interstitial CAPTCHA once, the action-enabled attempt exhausted classification retries, no action executed); `recovery_results.json` (14 of 14 offline tests)
- **acceptance clause draft:** BDAPI-with-Kimi runner style adapted: `probeSession(sessionVersion, capability, transport)`, `ensureSession(accountKey, priorGeneration, reason, attemptId)`, `captureSession(attemptId, fence, loginSecretRef)`, `completeRefresh(attemptId, fence, commandId, candidateVersion)` with `accountKey` = the ONE shared vendor login (never the tenant); NO OTP branch -- an unexpected OTP/MFA prompt is a distinct unsupported-challenge outcome and BD's `otpEntered` condition is never faked; VERIFIED AUTHENTICATION: usable only after the intended identity AND an expected report-capable response shape are verified from the transport that will use it (the generic market-data probe does not prove report entitlement); a 405/202 is classified by `x-amzn-waf-action` and actual page state, never as authentication expiry; Kimi receives only public or masked login/challenge pixels (never holdings, authenticated pages, passwords or cookie values), selects from constrained actions, never establishes success by assertion, and keeps the BD model-health timeout/retry/DOM-fallback pattern (the 30-s socket-idle timeout is load-bearing); the controller uses the BD start/SSM/completion/stop pattern under an ACCOUNT-SCOPED DURABLE CONDITIONAL LEASE carrying attemptId, a monotonic fence, lease expiry, host id and SSM command id; every wait, retry and total attempt bounded; ONLY the active owner publishes or controls its host, the watchdog uses the same ownership checks, a stale cleanup never stops a newer owner's instance; durable job wait / completion event instead of a Lambda busy through browser startup; SSM Success accepted only for the expected command and current attempt, then the candidate independently verified and usable by the intended report worker BEFORE waiters proceed; continuation handlers idempotent (async Lambda redelivery, SSM status events); the protected SESSION BUNDLE carries schema version, generation/attempt/fence, capture timestamp, authenticated identity, browser/UA context, cookie jar with domain/path/expiry/secure attributes, CSRF/WAF state and probe metadata -- NO password, cookie age advisory, capability probe authoritative; `X-CSRFToken` on mutations and `X-AWS-WAF-Token` where required are explicit headers (`credentials: include` does not add them); FENCE PUBLICATION: write an immutable candidate Secrets Manager version (idempotent via `ClientRequestToken`), then conditionally publish its exact VersionId/generation in the account coordinator only while the attempt owns the lease and every check passes; readers fetch the accepted VersionId; a stale candidate never resumes work; DynamoDB and Secrets Manager writes are never pretended to be one transaction; if AWSCURRENT compatibility is needed a single controlled publisher moves that label and consumer migration is explicit; probe timestamps never rewrite the secret; staging-label, first-version, candidate-cleanup and version-quota behavior accounted for; `ycharts/credentials` preserved for legacy consumers and ONE refresh authority coordinated with YALP_MDSRC so consumers do not evict the runner; an empty or missing secret is a capture requirement, never permission for an unauthenticated report POST; the BD OTP/device-trust branches, broad source-account IAM grants and proxy/TLS exceptions are NOT inherited, normal TLS verification preserved; no credential in any artifact, log, fixture or commit; **(v0.6, SUPP VI.3 + IV.5 K3 amendment)** the tested controller is `kimi-k3` with TWO calls per step -- a 2500-token READ that describes every matching unselected tile and Confirm, then a 400-token ACTION returning one bounded batch -- both at low reasoning effort, reader/actor deadlines 180/60 s; the controller re-compares the full screenshot before acting and a CHANGED IMAGE REJECTS THE PLAN (conservative by design; cosmetic changes may also reject); the model receives ONLY the explicit public CAPTCHA page, never an account page; the login helper scopes to the form containing the visible password (`auth-username` / `auth-password`), captures field names before navigation, submits with native Enter and counts OBSERVED POSTs (a pre-click counter is not wire proof); these are versioned implementation inputs, never product requirements; a solved-CAPTCHA checkpoint is NEVER promoted to an authenticated session without an identity/capability proof, and the DPAPI-protected local research cookies are research-only, never a production checkpoint; PREREQUISITE RESOLVED (v0.7, SUPP VI.4): Andrew supplied corrected credentials and authorized their storage; `ycharts/login/credentials` (us-east-1) AWSCURRENT version `e6b721ac-8d36-4042-9b85-e571fca68bc8`, readback verified 2026-09-11T01:39:16Z, no value in any artifact; probe 10 (01:39Z): login POST 302 with both transmitted fields matching the secret, dashboard scripts carry the account email, browser fetch AND plain Node HTTP each returned 200 JSON for the market probe and Overview template `14141822` (`aggregate_security_overview`, populated sections); probe 11 (01:41Z, a SEPARATE Node process, zero browser launches, zero model calls, zero login submissions): the template with only WAF state returned 403 plain text, with the restored authenticated cookies 200 JSON, the dashboard 200 HTML with the account email -- the LOCAL browser-to-ordinary-HTTP handoff is PROVEN and the template route's need for the authenticated session is OBSERVED; **(v0.8, SUPP VI.5, cloud packet @f06c1951e1) THE CLOUD FLOW IS PROVEN IN ISOLATION on Andrew's live-test word:** dedicated EC2 `i-0167fd745ad906a66` captured a fresh session by the K3 controller (second cloud CAPTCHA attempt, two actions / four calls; the first attempt stopped safely and released its lease); IDENTITY is a structured contract -- parse `window.USER` JSON for authenticated true, a positive integer user id matching the capture and the credential email, wrong-id control rejects; production PINS the enrolled account id; the session was published and read back in the ISOLATED secret `ycharts/session/research-20260911` (production `ycharts/session/current` untouched); a Lambda OUTSIDE a VPC replayed it with NO browser for template retrieval, persisted and reloaded actual Set-Cookie changes across invocations (page-view counter and expiries moved; real auth-token VALUE rotation is NOT what was observed), uploaded synthetic holdings, created an owned synthetic portfolio, generated the Overview and downloaded the PDF. STILL UNPROVEN, named: the production `ycharts/session/current` cookie-schema cutover with its competing readers (cookie-string vs cookie-array consumers; the legacy session-probe accepts any non-403 as authenticated), real authentication-token rotation, concurrent/stale-writer publication safety (the research capture checks the lease before the secret write but the two stores are not atomic; the research Lambda's persistence has no compare-and-swap), live cloud eviction / self-healing fault arms, and Comparison / Multi-Comparison outputs. Research state retained and enumerated in the packet's `cleanup.json`: the isolated secret, encrypted artifacts under `s3://opal-data-ycharts/research/20260911/`, a seven-day log group, the stopped host runtime and one synthetic vendor portfolio; `infra/aws/terraform/investor-reporting/ycharts-research-20260911/main.tf` defaults `active=false` (four temporary resources removed by safe-apply; landed under the audited CLOUD_OPS_OR_ETL exception on Andrew's live-test instruction) -- **(v0.9, Andrew-direct 03:1xZ) B8 ABSORBS that root as the seed of its production root and BUILDS ON `capture_ec2.cjs` (the EC2 entry point) and the packet's K3/login helpers; the proven chain is the mechanism, fixed; B8's acceptance arms, in order: (1) the production `ycharts/session/current` cutover -- one versioned schema, every competing reader migrated or adapted, the legacy non-403-is-authenticated probe retired; (2) concurrent publication fencing -- two capture attempts driven against one account, exactly one publishes, the loser's SSM completion cannot publish, a stale candidate cannot resume a waiter; (3) real token-value rotation observed and survived; (4) eviction / self-healing driven on the deployed jobs -- a displaced session recovers the same request revision and checkpoint, repeated displacement parks the request in a retryable state with the request preserved**

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** YCHARTS ON THE v0.9 MECHANISM. IB-s-8 recut to the fixed cloud chain; no live vendor call (the CTO's qualified read on Andrew's per-use word stands). PRD v0.9/v0.13 FWD-4 CONSTRAINT: the five boundaries VI.5 names unproven are acceptance arms of the cells, in order: the production session-secret cutover with its competing readers, concurrent publication fencing, real token-value rotation, cloud eviction / self-healing, Comparison and Multi-Comparison live proof.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- BUILD ON THE PACKETS, never a parallel implementation: `docs/research/investor_reporting_ycharts_cloud_20260911/{capture_ec2.cjs,cloud_transport.py}` and the auth packet's K3/login helpers become the production modules under `infra/aws/lambda/investor-reporting/ycharts/session/` (the broker: `publish`, `lease`, `fence`, `evict`, `current`) and `infra/aws/ec2/investor-reporting-ycharts/` (the capture controller on the dedicated host, K3 split controller, NO OTP branch); the research root `infra/aws/terraform/investor-reporting/ycharts-research-20260911/` (`active=false`) is ABSORBED into the ycharts root as its seed and retired (a plan showing its resources moving under the ycharts root's state, `state mv` under the ledger, then the research root deleted from the tree).
- THE FOUR ARMS OF v0.9, ON FIXTURES: (1) the cutover of `ycharts/session/current` to the versioned bundle shape with EVERY competing reader migrated (census the readers of that secret across the estate -- `comp-find` over infra and tools, denominator printed -- and each reader's parse updated to the new shape or its own contract left untouched where the PRD names it, `YALP_MDSRC`'s `ycharts/credentials` never touched); the legacy any-non-403 probe RETIRED (census 0 remaining); (2) concurrent publication fencing driven with two capture attempts on the fixture: one wins the fence, the other refuses without overwriting; (3) token-value rotation survived on fixtures: a new session version published, the replay transport picks it up on its next invocation, the old version refused; (4) eviction / self-healing driven on the deployed jobs: a 401 mid-job triggers ONE refresh through the broker and the job resumes its checkpoint; a repeat eviction reaches `retryable/attention`, never a loop. Arm (5), live Comparison / Multi-Comparison, is the CTO's qualified read at L10 on Andrew's per-use word and is NOT this order's.
- Every arm runs against RECORDED fixtures through the transport stub with a difference control; a capture on the host is a live login and is not run by this order (bound 1). The capture controller's deploy lands on the STOPPED host (code in place, instance not started).

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

the stopped runner host and its root (IB-s-8, the v0.4 mechanism, superseded by Andrew's word at v0.9); the generation Lambda's transport built on `cloud_transport.py` (IB-s-9) reading the session by name; the research packets and the research root (`active=false`); the recovery contract with the WAF-header fix (IB-s-9, W3-S8).

---

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~17:3xZ, at the drain of this slot's report -- row W3-S23 read at 3ed2c79443; the order stays OPEN):**
- **W3-S23 GRANTED, NOT SCOPED OUT.** `<paths>` now carries `infra/aws/lambda/ycharts-session-probe/` and `infra/aws/lambda/ycharts-session-capture/`, the two legacy ycharts-pipeline readers of `ycharts/session/current`. The probe's predicate (`status is not None and status != 403` reads a 400 as an authenticated session) is the false green the v0.9 cutover exists to remove, so naming it out of scope would leave it live: arm (a) reads `4 of 4` readers on the versioned bundle shape OR retired, with the probe's predicate replaced by a read of the versioned session's fence (a 400 is NOT authenticated), and a retired reader's function is left deployed only if its trigger is DISABLED and its source says why. Bound 1 stands: no live YCharts call rides on any of this.
- **W2-S21's YCHARTS HALF IS THIS ORDER'S.** `irpt-ycharts-generate` declares 25 build inputs in `lambda-source-map.json` of which 7 have never existed in the tree: register the truth (a build input absent from the tree is REMOVED, never invented), rebuild from the tree, and print `artifact_sha256` == S3 `content-sha256` == live `CodeSha256` for every ycharts function you deploy. The closed ledger entry that claimed a byte-identical rebuild at a commit lacking the inputs is a RECORD defect carried to L10 by name; do not edit it.
- **W4-S21 NOTED FOR THE YCHARTS ROOT.** The export root (IB-rt-8) declares `aws_iam_role_policy.render_host_export_evidence` BY NAME onto `irpt-ycharts-runner-role`, so the ycharts root's `iam.tf` no longer enumerates everything that role can reach. This order does NOT move that policy (a cross-root move is a destroy-and-create on a live role); it records the cross-root attachment in the ycharts root's `iam.tf` header as a comment naming the export root, and the fold is carried to L10.
- **W3-S20 IS CLOSED BY THE MERGE:** the export root's live state at f20bebd15d is declared (IB-rt-8's arm (a) landed); a plan of that root from this cut reads `No changes` or files a row.
- Arm (e) (the research root absorbed into the ycharts root by `state mv` under the ledger) proceeds once arm (a) is measured; NEVER-2 stands -- open the ledger only with the room to close it in-session.

**ISSUER CORRECTION (2.0.0_SA_COO~B, 2026-09-11 ~18:2xZ, at the drain of the wind-down branch e021ddcdfd -> 22f2238cd7; for the SUCCESSOR run):**
- **THE 'ABSENT BUILD INPUTS' PREMISE IS CONTESTED BY TWO INSTRUMENTS AND THE FACE NO LONGER ASSERTS IT.** Slot ~2 measured (W2-S21) that irpt-ycharts-generate declared 7 of 25 inputs that never existed and irpt-status 5 of 7; slot ~3 measured at a later tip (W3-S24) 26 declared, 26 resolving, 0 absent -- the 8 outside `source_dir` are flat-packaged SHARED libraries (`enforce`, `gate`, `keys`, `resolve`, `firm_registry.json`), and removing them strips the function's imports. The drain resolved irpt-status's file list in `lambda-source-map.json` as the UNION of both sides (the shared libraries slot ~3 declares plus the `entry.py` slot ~2 added), which is the non-destructive reading. RULE FOR THE SUCCESSOR: before removing ANY declared build input, resolve it the way the builder does (`source_dir` first, then the flat-packaged shared library roots), print `N of N resolve`, and remove only what resolves NOWHERE; an input that resolves outside `source_dir` is a shared library, not an absence.
- **A DEPLOY IS OWED (W3-S25), first act of the successor run that holds the functions:** `_scope/resolve.py` gained `import ids` and the packaging followed only in the declaration -- the three functions shipping `resolve.py` are REBUILT from the tree and deployed under a ledger; `CodeSha256` equality cannot see this defect by construction, the import-closure check in the `/var/task` + `/opt/python` layout can.
- **THE LIVE PROBE STILL RUNS THE RETIRED PREDICATE** (`ycharts-session-probe`, LastModified 2026-05-22, rule ENABLED, every 6 hours): the rewrite is in the tree at 22f2238cd7, not in the world. Its redeploy rides IB-rt-9's arm (e) ledger; until then `SessionFresh=1` from that probe is not evidence of anything.

---

## ISSUER AMENDMENT -- 2026-09-11 ~22:5xZ (`2.0.0_SA_COO~B`, post-reboot re-entry). THIS BLOCK GOVERNS OVER EVERY LINE ABOVE IT.

**Authority:** Andrew-direct ~22:25Z at the `1.0.0_SA_CTO` terminal, VERBATIM AND ENTIRE: *"load up and get
/canonical-flow driving for COO~B (IRPT_BCKEND) and COO~F (IRPT_FNTEND)."* Relayed as msg 96019; recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_2225Z_RESUME_AFTER_REBOOT_DRIVE_BOTH_IRPT_LANES.md`
@4a90ec8d2f. It lifts exactly ONE thing: MSTR 95994's instruction 2, "start nothing new". **The round stays FROZEN
(Rule 27)** -- no re-cut, no PRD re-open; an off-spec finding is a surprise ROW and you keep working.

### A1. YOU ARE A COLD START. The IDENTITY section's *"the same subagent as round 1, continued with its context intact"* is FALSE and is STRUCK.
This device rebooted at ~22:0xZ. **Every worker subagent of this round is DEAD and cannot be resumed.** You carry no
prior context and must assume none. Your whole context is: THIS FACE (the newest amendment governs), and the WIP hand-off written for exactly this moment: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/WIP_IB-rt-9_winddown.md`. **READ THAT FILE BEFORE YOU READ ANYTHING ELSE IN THIS FACE'S BODY** -- its own opening line is that three sentences of this task order are no longer true, and it says which.

### A2. NEW WORKTREE -- the pair named in IDENTITY IS GONE.
- **Worktree:** `/c/tmp/wk-irpt-2-3b` on branch `wk-irpt_bckend-2-3b`, cut by the issuer from CLOUD HEAD `7d6db9bcfa`.
- The old pair (`/c/tmp/wk-irpt-2-3 on wk-irpt_bckend-2-3`) was REMOVED after its branch was verified an ancestor of the tip. Do not look for it, and
  **never spawn into an old worktree.**
- **Every path in this face is relative to the NEW worktree root**; make it absolute by prefixing `/c/tmp/wk-irpt-2-3b/`.
- First act unchanged: `git rev-parse --abbrev-ref HEAD`, then `test -d org && test -d .tools && echo TREE-OK`.

### A3. FRESH-WORKTREE TRAPS THIS ROUND HAS ALREADY PAID FOR -- none of these is yours to rediscover.
- **`.tools/terraform.exe` is gitignored and therefore ABSENT here.** Four roots read `rc 1` for want of
  `terraform init`, and **an rc is not a reading.** Resolve the binary by path; `init` each root before any plan.
- **`safe-apply.sh` has TWO identity gates.** `export OPAL_AGENT_SERIAL=...` satisfies only the commit-lane one; the
  halt gate reads `org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial`, gitignored per-session state **you must write
  yourself BEFORE any apply** (row W4-S2). Write it before you need it.
- **A rail denial ABORTS THE WHOLE BASH CALL**, so every later segment of an `&&` chain is a SILENT no-op --
  including your commit. Put a gated read in its own call, or verify the later segment's EFFECT.
- **`safe-commit.sh` force-adds gitignored files under a DIRECTORY pathspec** (it once staged a 685 MB provider
  binary). Always pass explicit FILE paths.
- **Heredoc backslashes arrive HALVED** in the Bash tool. Write scripts and commit messages with the Write tool.
- A raw `grep`/`find` over a directory is denied and routed to `comp-find`; a `cmd | grep` pipe RECEIVER is free.

### A4. YOUR FIRST LEDGERED ACT IS THE OWED DEPLOY (row `IRPT_BCKEND-W3-S25`), AND YOU ARE FIRST IN LINE FOR IT.
`_scope/resolve.py:81` carries `import ids as _ids` at module scope, and the DECLARATION fix is already committed
(`d3397434d5`) for `irpt-export-render`, `irpt-status` and `irpt-ycharts-generate`. **The deploy was never taken --
the wind-down forbade it.** The three live functions serve OLDER bytes and work today; the ARMED part is that the
next rebuild of any of them, by anyone, for any reason, would build, upload, register, match its hash three ways and
then die at cold start on `ModuleNotFoundError`.

- **Slot ~2 (IB-rt-2) is working the SAME `lambda-source-map.json` and three of its six functions are YOURS.**
  Sequencing is ruled: **you deploy these three FIRST**; slot ~2 is held off them until I confirm your deploy landed.
  Report to me the moment it has.
- Verify with an EXTRACT-AND-IMPORT in the flat `/var/task` layout, repo stripped from `sys.path`, in a FRESH
  interpreter -- `CodeSha256` cannot see a missing module by construction. Your own `.scratch/verify_ycharts_inputs.py`
  was scratch and did not survive; rewrite it.
- Print `artifact_sha256 == S3 content-sha256 == live CodeSha256` for every function (W3-S18). NEVER-2: the ledger
  opens only with the room to close it in-session; OPEN sentinel committed BEFORE the act, CLOSE before the grading
  reads.

### A5. ARM (a) IS DONE AND MUST NOT BE RE-DONE; ARMS (b)-(f) REMAIN.
Re-run the battery once to confirm the cutover still passes (~40 s), then leave arm (a) alone. The WIP's sections 1
and 2 are the order of work: (b) fencing, (c) rotation, (d) eviction/self-healing, (f) egress, and **(e) absorbed /
stopped / converged LAST and only with room to finish.**

- **THE ACCEPTANCE TOKEN STAYS ABSENT FROM THE BATTERY'S OUTPUT IN EVERY FORM, INCLUDING NEGATED.** `RT9-AC1`'s
  `<expect>` is graded as a REGEX over that output, so a line reading `<token>: NOT ASSERTED` would MATCH and the
  criterion would read PASS on a run that proved one arm of six. Add the token to the final line ONLY in the same
  edit that makes all six arms pass. This is the single easiest way to turn this hand-off into a false green.
- **Write NO proof-of-spec instance until arms (b)-(f) pass in ONE run.** `PENDING-THIS-COMMIT` is a ONE-SHOT
  sentinel: writing the instance now burns it on five arms that do not exist. `RT9-AC2` is `judgment="true"` -- it
  gets its output and NO verdict, under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.

### A6. THE THREE STALE SENTENCES YOU ALREADY IDENTIFIED STAY STRUCK, AND W3-S24 IS RULED.
The *"25 build inputs of which 7 have never existed"* premise is FALSE (26 declared, 26 resolve; the 8 outside
`source_dir` are flat-packaged shared libraries). **The `irpt-status` file list is the UNION of both slots' readings
-- resolve the way the builder does, print `N of N`, remove only what resolves NOWHERE.** Acting on the naive check
would strip `enforce`, `gate`, `keys`, `resolve` and `firm_registry.json` out of the zip and be GREEN at every
deploy-time rung.

The grant of `ycharts-session-probe/` and `ycharts-session-capture/` is SPENT and does **not** reach
`infra/aws/terraform/ycharts-pipeline/`. If retiring the capture properly needs a change there, that is a BLOCKING
row to me, never an override.

### A7. THE LIVE PROBE STILL RUNS THE RETIRED PREDICATE. That is a disclosure, not an emergency.
`ycharts-session-probe-schedule` is ENABLED, `cron(0 */6 * * ? *)`, and the live function `LastModified 2026-05-22`.
The old predicate is OVER-permissive: it does not false-ALARM, it false-REASSURES. **So `SessionFresh=1` is not
evidence of anything until arm (e) redeploys it** -- do not cite it as evidence in the meantime, and say so in any
row that touches session freshness.


## DELIVERABLE

`infra/aws/lambda/investor-reporting/ycharts/session/` + tests; `infra/aws/ec2/investor-reporting-ycharts/` (the capture controller from `capture_ec2.cjs`); the ycharts root absorbing the research root (`state mv` under the ledger; the research directory removed); the reader census and migrations; the ledger entries + sentinels; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_9.py` and `.result.md`.

---

## BOUNDS

- **NO LIVE YCHARTS CALL, NO LOGIN, NO CAPTURE RUN** in this order; the host stays STOPPED; the qualified live arm is L10's.
- **`ycharts/credentials` (legacy, `YALP_MDSRC`'s) is never overwritten; `ycharts/login/credentials` is read by NAME only; no value in any artifact.**
- **ONE automation owner of the shared vendor login**: the broker's fence is the mechanism, proven on fixtures.

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="RT9-AC1" cell_refs="IB-rt-9"><invocation>timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_9.py</invocation><expect>IBRT9-BROKER-FENCED</expect></criterion>
**`RT9-AC1` -- PASSES BY OUTPUT -- the four v0.9 arms on recorded fixtures, the readers migrated, the research root absorbed.**
**(a) THE CUTOVER, EVERY READER.** Census of readers of `ycharts/session/current` and of the legacy probe across the estate (denominator printed): `N of N` migrated to the versioned bundle shape or explicitly out of scope by PRD name; legacy any-non-403 probes remaining: 0.
**(b) FENCING.** Two capture attempts on the fixture: 1 wins, 1 refuses, the published version unchanged by the loser (printed).
**(c) ROTATION.** A new version published; the replay transport's next invocation uses it; the old version refused; printed.
**(d) EVICTION / SELF-HEALING.** On the deployed generation job with the replay transport: a 401 mid-job -> ONE broker refresh -> resume at the checkpoint (no resubmit, the difference control); a repeat eviction -> `retryable/attention`; printed.
**(e) ABSORBED, STOPPED, CONVERGED.** The research root gone from the tree, its resources under the ycharts root (`state list` printed), the host STOPPED (`describe-instances`), the ycharts root's post-apply plan `No changes`; ledgers CLOSED, sentinels committed.
**(f) NOTHING LEFT THE MACHINE.** 0 external connections across the battery (guard log, denominator).

<criterion id="RT9-AC2" cell_refs="IB-rt-9" judgment="true"/>
**`RT9-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which readers you migrated and which you left untouched by PRD name, with the line each parses; what the fixture fence cannot show about two real hosts racing; and what the first real capture on Andrew's word would measure that nothing here does. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT9-AC1, RT9-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-9.ycharts-session-broker-on-the-fixed-cloud-chain.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/
infra/aws/ec2/investor-reporting-ycharts/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/terraform/investor-reporting/ycharts-research-20260911/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt9.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ycharts-session-probe/
infra/aws/lambda/ycharts-session-capture/
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-9` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-9</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-ycharts-generate and the capture host role` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-ycharts-generate and the capture host role` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT9-AC1, RT9-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-9.ycharts-session-broker-on-the-fixed-cloud-chain.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-9.ycharts-session-broker-on-the-fixed-cloud-chain.proof_of_spec.json RT9-AC1,RT9-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
