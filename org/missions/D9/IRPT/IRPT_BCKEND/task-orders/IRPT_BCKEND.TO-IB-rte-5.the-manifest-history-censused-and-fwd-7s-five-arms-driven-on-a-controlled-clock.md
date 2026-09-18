# TO IRPT_BCKEND.TO-IB-rte-5 -- THE MANIFEST HISTORY CENSUSED AND FWD-7's FIVE ARMS DRIVEN ON A CONTROLLED CLOCK: W2-S57 stays open from round 3 (analysis s.8 item 6) -- IB-rtd-2 made the no-op branch fire, and what remains is rtd-2's own Q2 (whether any pre-fix manifest misstates previous state -- a project-wide census no worker could run inside its grant) and FWD-7's stated PROOF, a controlled-clock exercise of ALL FIVE arms (an added client, a changed eligibility, a MISSED trigger, a FAILED refresh, an OVER-AGE request) against the CURRENT deployed code, each arm's reason code bound by hash

<to_id>IRPT_BCKEND.TO-IB-rte-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~2 2026-09-18T21:3xZ: R55-AC1 PASS-by-output (16 of 16 graded checks, token IBR55-MANIFESTS-CENSUSED-AND-FIVE-ARMS-DRIVEN); rtd-2's Q2 CLOSED at k=0 of 5 via the full un-purged S3-version history; five arms driven 5 of 5 distinct against the current deployed CodeSha256; fresh-dispatch case measured, named-blocked (0 of 1), not driven. R55-AC2 recorded for the CVO, no verdict. proof-of-spec-check.py rc=0 VALID.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 5 (the CTO's round-4 analysis @561d6e1cc9, msg 98036) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 4) | **Round-4 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md` @561d6e1cc9 | **Andrew-direct:** 2026-09-18 ~17:3xZ "Approved" (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @af794c77e3) | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30 | **Decomp cell:** `IB-rte-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.5, s.R5) | **outcome_ref:** FWD-7

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-5-2` on branch `wk-irpt_bckend-5-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-5-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**Where W2-S57 stands:** IB-rtd-2 (@2c0c8746d6) fixed `last_manifest()` and two siblings (`_last_recorded_business_date`, `_last_dispatched_cid`), deployed three times under ledger (served `CodeSha256` `q7O3GGjK2PBHkNo6KfJOAVaJhUW4cwxtWQFZgTqSO/o=`), and drove `REFRESH_NOOP_SAME_FRONTIER` for 2 of 2 unchanged-frontier firms. Its judgment record left Q2 NOT RUN: *"whether any pre-fix historical manifest needs a one-time reconciliation"* -- the two `previous_entry_count=0` manifests captured as negative controls may be a firm's genuine first build or a pre-fix-masked prior one. And FWD-7's own PROOF line (PRD @b8e98d5a4d) is *"controlled-clock / source-fixture exercise driving ALL FIVE arms ... with NO REAL-CALENDAR WAIT anywhere in it"* -- round 1 built the controlled-clock instrument (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_4_controlled_clock.py`, read it); no round has driven all five arms against the code as deployed AFTER rtd-2.

- (a) THE CENSUS (rtd-2's Q2): every `_refresh/<date>/manifest.json` under each firm's directory destination (`s3://opal-data-bd/...`, `opal-data-inf/...`, `opal-data-cot/...` -- IB-rtc-3/rtd-1/rtd-2's results name the exact prefixes), `M of M` manifests listed with `reason_code`, `as_of_business_date`, `previous_entry_count`, `current_entry_count`, the landed artifact's ETag and its `as_of`; for each firm, the chain re-derived under the FIXED previous-state rule -- which manifests, if any, MISSTATE previous state (a `previous_entry_count=0` beside an earlier COMPLETED manifest for the same firm is the signature). Print `k of M` misstating. A reconciliation, if any is needed, is a served-output WRITE: DECLARE it (the exact keys, before -> after, the rollback) in your result and do NOT perform it -- it is a never-widen act for a later cell; if `k = 0`, say so and Q2 closes.
- (b) THE FIVE ARMS, driven on the controlled clock against the CURRENT deployed function (`CodeSha256` read at T0 and bound): (1) an ADDED client in the source fixture becomes visible within the declared window; (2) a CHANGED eligibility ceases to be offered; (3) a MISSED trigger reads DIFFERENTLY from a completed one (`missed_business_dates` / the reason code); (4) a FAILED refresh reads differently from both; (5) an OVER-AGE directory request hits the declared expiry/fallback (`expiry.py`'s closed set) rather than a silent answer. Each arm: the clock value driven, the invocation (the deployed function or the instrument's harness -- say which plane each arm runs on and why; an arm that can only run in-process against the deployed BYTES is stated as such), the reason code produced, the artifact hash. `5 of 5` arms with the reason codes DISTINCT where the endpoint says they must differ. No real-calendar wait; no vendor call; no source bucket written.
- (c) THE FRESH-DISPATCH CASE, named: every fire since IB-rtc-7 found prior commands landed (rtd-1). State what a scheduled fire needs to perform a FRESH SSM dispatch (a frontier advance in the source set), whether the controlled clock can drive it WITHOUT writing to a source or destination bucket, and if it can, drive it (`1 of 1` new command id, its build outcome by hash); if it cannot, say exactly which write it would need and STOP there -- that is a measurement.

---

## DELIVERABLE

`battery_ib_rte_5.py`, `IB-rte-5_R55-AC1_battery_output.txt`, `the-manifest-history-and-five-arms.result.md` (the `M of M` manifest table and the declared reconciliation, if any); the proof instance.

---

## BOUNDS

- READ-ONLY on every served bucket: no manifest rewritten, no directory written, no source fixture placed in a live source prefix (fixtures live in the instrument's own scratch/fixture plane); no apply, no deploy, no IAM. A reconciliation is DECLARED, never performed here.
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

<criterion id="R55-AC1" cell_refs="IB-rte-5"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rte_5.py</invocation><expect>IBR55-MANIFESTS-CENSUSED-AND-FIVE-ARMS-DRIVEN</expect></criterion>
**`R55-AC1` -- PASSES BY OUTPUT:** (a) `M of M` manifests censused per firm with `k of M` misstating (and the declared reconciliation if `k > 0`); (b) `5 of 5` arms driven on the controlled clock against the deployed `CodeSha256`, reason codes distinct where required, each artifact hashed; (c) the fresh-dispatch case driven `1 of 1` or the exact blocking write named. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R55-AC2" cell_refs="IB-rte-5" judgment="true"/>
**`R55-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether FWD-7's DONE WHEN (EXERCISED on a controlled clock, all five arms, no real-calendar wait) is now met as written or what remains; whether the manifest history is sound as the missed-trigger detector's input; and whether the fresh-dispatch case needs a design change (a driven reset) or only patience. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R55-AC1, R55-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-5.the-manifest-history-censused-and-fwd-7s-five-arms-driven-on-a-controlled-clock.md
infra/aws/lambda/investor-reporting/directory/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.5, cell `IB-rte-5` (s.R5 -- the round-5 rectangle, edges, seating and bounds).
<owned_cells>IB-rte-5</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the schedule is neither changed nor relied on; the clock is controlled.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted; read-only on every bucket.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R55-AC1, R55-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rte-5.the-manifest-history-censused-and-fwd-7s-five-arms-driven-on-a-controlled-clock.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rte-5.the-manifest-history-censused-and-fwd-7s-five-arms-driven-on-a-controlled-clock.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-5.the-manifest-history-censused-and-fwd-7s-five-arms-driven-on-a-controlled-clock.md` BEFORE the complete flip; rc 0 AND R55-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
