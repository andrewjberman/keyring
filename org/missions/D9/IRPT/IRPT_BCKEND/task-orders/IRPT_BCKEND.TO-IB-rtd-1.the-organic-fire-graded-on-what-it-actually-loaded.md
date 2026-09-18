# TO IRPT_BCKEND.TO-IB-rtd-1 -- THE 13:00Z ORGANIC FIRE GRADED ON WHAT IT ACTUALLY LOADED: the negative arm of FWD-7's driven exercise -- the schedule's own fire, read back by the artifacts it produced and bound to the bundle VersionId and Lambda CodeSha256 at invocation, never to what a criterion predicted it would find

<to_id>IRPT_BCKEND.TO-IB-rtd-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~2, 2026-09-18. T0 armed 12:48:46Z-12:57:44Z (before the 13:00:00Z fire); the fire observed at 13:00:29Z (request id 986aad35-d0ab-4b76-9161-0ac88e100734, invoker scheduler.amazonaws.com via CloudTrail AssumeRole on irpt-directory-refresh-scheduler-role); 3 of 3 firms accounted for (REFRESH_COMPLETED_WITH_ADDITIONS on byte-identical bytes, row IRPT_BCKEND-W2-S57's pattern, now confirmed organic). R41-AC1 PASS (battery token IBR41-ORGANIC-FIRE-READ-BY-ITS-ARTIFACTS, 23/23 arms, rc 0). R41-AC2 judgment recorded (UNVERIFIABLE-BY-INSTRUMENT, CVO at L9). proof-of-spec-check rc=0, VALID. HANDED by 2.0.0_SA_COO~B at 12:45Z (@406f1bf79b, fifteen minutes before the 13:00Z fire); drained by the issuer.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 4 (the CTO's round-3 analysis @5c59f68d70, msg 97944) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 3) | **Round-3 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md` @5c59f68d70 | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar (analysis s.4, ADOPTED) | **Decomp cell:** `IB-rtd-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.4, s.R4) | **outcome_ref:** FWD-7 (the organic arm), FWD-1

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-4-2` on branch `wk-irpt_bckend-4-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-4-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**What the analysis rules (s.2, s.4, s.9 item 1):** FWD-7's organic case is the NEGATIVE ARM of a driven exercise, correctly shaped and not a wait-defect; but a criterion certifying what that fire WILL find is the defect R38-AC2 fell into. **So this cell grades the fire on what it ACTUALLY LOADED**, at the bundle's `VersionId` at invocation, and EventBridge `Invocations` certifies nothing (bind the proof to the ARTIFACT the fire produced).

The schedule: `irpt-directory-refresh`, `cron(0 9 ? * MON-FRI *)` America/New_York, ENABLED, next fire 13:00Z 2026-09-18 (DS read at IB-rtc-8; re-read it, print the state and the next-fire time). The fire dispatches all three firms through IB-rt-6's mechanism (SSM to `i-02448edb624a7a7cf`, the host pulls the bundle, the NEXT fire reconciles).

- (a) BEFORE the fire (your first act, timestamped): the served identities the fire WILL meet, read now and recorded as READ-AT-T0, not as predictions -- Lambda `irpt-directory-refresh` `CodeSha256` (`get-function-configuration`), the bundle key's current `VersionId`/`ETag` (`head-object` on `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`), the env keys (4 + `IRPT_DIRECTORY_SOURCE_ROLE_MAP`), the three firms' newest manifest under `.../_refresh/<date>/manifest.json` and landed directory ETags. These are the T0 row; nothing here is a claim about the fire.
- (b) THE FIRE, observed: poll the Lambda's CloudWatch log group / the run record the dispatch writes (IB-rt-6's result names the exact carriers) until the invocation whose start time is >= 13:00:00Z appears, bounded by `timeout 1800`; record the request id, the invocation's `CodeSha256` (from the log stream's version or `get-function` at that moment), and the THREE SSM command ids it dispatched. The host's command stdout (`get-command-invocation`) names the bundle it pulled -- record the `VersionId`/sha256 it printed and compare to (a): EQUAL or DIFFERENT, stated, either is a measurement.
- (c) THE ARTIFACTS the fire produced, by hash: per firm, the SSM command status, the landed key's `ETag`/`sha256` and revision (before -> after), row count, the manifest the reconciliation writes and its `reason_code` -- `REFRESH_OK`/`REFRESH_COMPLETED_WITH_ADDITIONS`/`REFRESH_NOOP_SAME_FRONTIER`/failure, per firm, `3 of 3` firms accounted for whatever each read. A firm whose build FAILED is recorded with its stderr excerpt; that is a measurement, not a stop. **Know W2-S57 going in:** the no-op branch cannot fire today, so a same-frontier firm will read `REFRESH_COMPLETED_WITH_ADDITIONS` on unchanged bytes -- record it as the row predicts, without grading it.
- (d) THE NEGATIVE ARM stated: the difference between this fire and the driven fires of IB-rtc-3/IB-rtc-7 -- who invoked (the scheduler principal, from the invocation's event source / CloudTrail `Invoke` with `eventSource` `scheduler`), the payload (the schedule's own, no override), and whether anything the driven fires did NOT exercise happened here (a missed-trigger or over-age path). `EventBridge Invocations` may be read and printed but is NOT the evidence for any arm.

---

## DELIVERABLE

`battery_ib_rtd_1.py`, `IB-rtd-1_R41-AC1_battery_output.txt`, `the-organic-fire-graded-on-what-it-loaded.result.md` (with the T0 row and the per-firm artifact table, every hash), the run-record / SSM transcripts; the proof instance.

---

## BOUNDS

- READ-ONLY everywhere: no apply, no deploy, no invoke, no re-fire, no host write beyond nothing (this cell touches no host); the fire is the scheduler's. A manual `invoke` here would destroy the discriminator this cell exists to read.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W2-S<k>` with k continuing that coordinate's numbering (read the file's highest `W2-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R41-AC1" cell_refs="IB-rtd-1"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtd_1.py</invocation><expect>IBR41-ORGANIC-FIRE-READ-BY-ITS-ARTIFACTS</expect></criterion>
**`R41-AC1` -- PASSES BY OUTPUT:** (a) the T0 row read and timestamped before 13:00Z; (b) the invocation observed with request id, `CodeSha256` at invocation and 3 SSM command ids, the host-printed bundle identity compared to T0; (c) `3 of 3` firms accounted for by hash with each manifest `reason_code`; (d) the scheduler principal named as the invoker. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R41-AC2" cell_refs="IB-rtd-1" judgment="true"/>
**`R41-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the organic fire exercised any path the driven fires did not (missed trigger, over-age, the no-op branch) or merely repeated them; whether the bundle/Lambda the fire loaded are the ones round 3 certified (T0 == invocation, or not, and what moved between); what FWD-7's five arms still lack after this fire. No verdict. Every line citation carries `@<commit-ish>` (S56).

<expected_criteria>R41-AC1, R41-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-1.the-organic-fire-graded-on-what-it-actually-loaded.md
infra/aws/lambda/investor-reporting/directory/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.4, cell `IB-rtd-1` (s.R4 -- the round-4 rectangle, edges, seating and bounds).
<owned_cells>IB-rtd-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut -- the schedule `irpt-directory-refresh` is ENABLED at cron(0 9 ? * MON-FRI *) America/New_York (DS read 06:4xZ at IB-rtc-8, next fire 13:00Z); BLIND SPOT: the read is a description of the schedule, not of the fire -- the fire is this cell's measurement.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; read-only.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R41-AC1, R41-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtd-1.the-organic-fire-graded-on-what-it-actually-loaded.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance, so no `PENDING-THIS-COMMIT` sentinel is needed); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtd-1.the-organic-fire-graded-on-what-it-actually-loaded.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-1.the-organic-fire-graded-on-what-it-actually-loaded.md` BEFORE the complete flip; rc 0 AND R41-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
