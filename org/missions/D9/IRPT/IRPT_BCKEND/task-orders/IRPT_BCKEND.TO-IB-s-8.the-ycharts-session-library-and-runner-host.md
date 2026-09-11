# TO IRPT_BCKEND.TO-IB-s-8 -- THE YCHARTS SESSION LIBRARY AND RUNNER HOST: the BDAPI-with-Kimi runner style adapted to YCharts, lease and fencing, NO OTP branch, the host applied STOPPED

<to_id>IRPT_BCKEND.TO-IB-s-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-8` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-4 (contrib) | **PRD candidate:** B8

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-1-3` on branch `wk-irpt_bckend-1-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** first in slot ~3. Spawned after IB-s-17 is merged. IB-s-9 hangs off this cell.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B8 YCharts session library + browser runner
- **serves:** FWD-4 (contrib)
- **brief sections consumed:** O4 session paragraph; IV.4 session pattern and paths, Secrets paragraph
- **contracts (P=produces, C=consumes):** --
- **paths: reuse:** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js`, `run-bd-auto-login.sh`, `package.json`; `infra/aws/terraform/bd-49f-auto-login/{iam,instance,main}.tf`; `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py`; Secrets `ycharts/login/credentials` (existing), `ycharts/session/current` (proposed), `astn/kimi/api-key`
- **paths: new home:** separate YCharts host/role (never the BD host) under `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** six transcripts + manifest + three HARs (private packet, offline profile `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`)
- **acceptance clause draft:** BDAPI-with-Kimi runner style adapted: `getSession`/`probeSession`/`acquireSession`/`persistSession`/`withAuthenticatedPage` with lease/fencing; success predicate is identity/cookie/authenticated-probe, NO OTP branch; an unexpected challenge is an explicit failure; bounded reacquisition after eviction; no credential in any artifact

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Runner style is Andrew's word, not a build choice:** *"use the exact same style of runner, that strategy works very well. I do not believe they send OTP so dont need that part."* Adapt `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` (Node/Playwright with the Kimi DOM fallback, transient EC2/SSM execution, versioned artifacts, native AWS egress, normal TLS) into `infra/aws/ec2/investor-reporting-ycharts/` with the library surface the PRD row names -- `getSession`, `probeSession`, `acquireSession`, `persistSession`, `withAuthenticatedPage` -- lease/fencing for automation, the success predicate on identity/cookie/authenticated-probe evidence, an unexpected challenge an EXPLICIT FAILURE (never an invented OTP route), bounded reacquisition after an eviction (Alyssa and automation may evict each other), browser-managed CSRF/WAF rotation preserved.
- Secrets by NAME: `ycharts/login/credentials` (exists), `ycharts/session/current` (exists at the cut; the brief measured it without an AWSCURRENT version -- READ its version state at Phase 1 and record it), `astn/kimi/api-key` (exists); `ycharts/credentials` is legacy and UNTOUCHED. Coordinate compatibility with `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py` (assumes status 200; not a parser for 201).
- The host: `infra/aws/terraform/investor-reporting/ycharts/` -- a SEPARATE instance and role from the BD host (never the BD host), SSM document, the role's Secrets read on the three names only, applied and then held STOPPED (`aws_ec2_instance_state` = stopped); starting it and logging in is the qualified live arm on Andrew's per-use word.
- Proof of the library is OFFLINE: a local browser against the captured HAR flows (the private packet profiled by `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`; the HAR evidence JSON in `docs/briefs/sources/`) through a replay server; no request leaves the machine.

---

## DELIVERABLE

`infra/aws/ec2/investor-reporting-ycharts/` (`ycharts_session.js`, `run-ycharts-session.sh`, `package.json`, `README.md`) + `tests/`; `infra/aws/terraform/investor-reporting/ycharts/` (`instance.tf`, `iam.tf`, `ssm.tf`, `main.tf` completed); the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_8.py` and `.result.md`.

---

## BOUNDS

- **NO LIVE YCHARTS LOGIN.** The battery runs against a local replay; a request to any `ycharts.com` host from your worktree fails arm (e). The live arm is the CTO's L10 read on Andrew's word.
- **NO OTP BRANCH.** A code path that handles a one-time-code challenge fails arm (b).
- **The host is applied STOPPED and stays stopped.** Do not start it.
- **No secret value is printed, logged or committed.** `describe-secret` only.

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S8-AC1" cell_refs="IB-s-8"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_8.py</invocation><expect>IBS8-RUNNER-BUILT</expect></criterion>
**`S8-AC1` -- PASSES BY OUTPUT -- the library against the captured flows, the secrets by name, the host stopped.**
**(a) THE FIVE SURFACES WORK AGAINST THE REPLAY.** `probeSession` on a stale bundle -> not authenticated; `acquireSession` through the replayed login flow -> authenticated (identity/cookie/probe evidence printed, values redacted); `persistSession` writes a bundle; `getSession` returns it; `withAuthenticatedPage` runs a callback on an app page. `5 of 5`.
**(b) NO OTP BRANCH -- THE CENSUS.** Enumerate the runner's challenge handlers (denominator printed): 0 handle a one-time code; an injected unexpected challenge produces an EXPLICIT failure record, not a retry loop. Printed.
**(c) EVICTION IS BOUNDED -- THE DIFFERENCE CONTROL.** Inject an eviction mid-session: reacquisition happens at most N times (N declared) then stops with a failure; without the eviction, 0 reacquisitions. Both printed.
**(d) LEASE AND FENCING.** Two concurrent runners: exactly one holds the lease; the fenced one refuses to persist. Printed.
**(e) NOTHING LEFT THE MACHINE.** The replay server's request log shows every request; an outbound-network guard recorded 0 external connections. Printed.
**(f) SECRETS BY NAME, HOST STOPPED, LEDGER CLOSED.** `describe-secret` on the three names prints their version stages (no values); `describe-instances` prints `stopped` for the host; the ledger CLOSED and the sentinel committed (hash).

<criterion id="S8-AC2" cell_refs="IB-s-8"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S8-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S8-AC3" cell_refs="IB-s-8" judgment="true"/>
**`S8-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what the replay cannot show about the live site (WAF token minting, cookie rotation timing, an eviction by a person); the AWSCURRENT state you found on `ycharts/session/current` and what it implies for the first live run; and which part of the BDAPI runner you deliberately did NOT carry over and why. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S8-AC1, S8-AC2, S8-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-8.the-ycharts-session-library-and-runner-host.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/ec2/investor-reporting-ycharts/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s8.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-8` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-8</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-ycharts-runner` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S8-AC1, S8-AC2, S8-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-8.the-ycharts-session-library-and-runner-host.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-8.the-ycharts-session-library-and-runner-host.proof_of_spec.json S8-AC1,S8-AC2,S8-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
