# TO IRPT_BCKEND.TO-IB-rtc-3 -- THE REFRESH BUILDS, EXERCISED FOR INFLECTION AND COTTONWOOD -- AMENDED under R-45: the deployed dispatch's unpack becomes REPO-SHAPED (members named by repo path extracted at $W), the directory root is applied under ledger with the served CodeSha256 verified, and THEN the dispatch fires the re-minted runner for the two firms whose grants are in place; a directory artifact LANDS in each firm's own bucket with its hash recorded, the run record and the next fire's reconciliation read it back, and the 49 Financial build reads BLOCKED on the named control

<to_id>IRPT_BCKEND.TO-IB-rtc-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- AMENDMENT 3 EXECUTED by 0.9.0_WK_IRPT_BCKEND~2 on branch wk-irpt_bckend-3-2c, battery+result+row committed @aade16a39e, instance+this flip committed in the very next commit on this branch. R33-AC1 = PASS-by-output (rc=0, 22 of 22 graded checks PASS, token IBR33-TWO-OF-THREE-DIRECTORIES-LANDED printed, re-run twice with 26 of 26 verdict lines identical). R33-AC2 recorded for 3.0.0_SA_CVO (no verdict). proof-of-spec-check.py rc=0 VALID. Row IRPT_BCKEND-W2-S57 filed (OBSERVATION, INERT, not blocking): REFRESH_NOOP_SAME_FRONTIER never fires against a real manifest history because last_manifest()'s calendar-day walk finds a stale same-day REFRESH_DISPATCHED manifest ahead of the later COMPLETED one -- not fixed here, no code change this amendment. Was: AMENDMENT 3 HANDED by 2.0.0_SA_COO~B at 2026-09-18T09:3xZ to slot ~2 (cold start, worktree /c/tmp/wk-irpt-3-2c, branch wk-irpt_bckend-3-2c from HEAD 9196f164cf) after IB-rtc-9 (@c022677a9c) and IB-rtc-7 (@9196f164cf, VALID: role irpt-49f-directory-read-role applied under both halves, fence proven 3 of 3 DENIED + 1 of 1 READ-OK, THREE directories landed on its 49f fire -- 49financial 4562 entries ETag fcdf90de, cottonwood 259 ETag 264e0fbe, inflection 291 ETag 782324f9, all under s3://opal-data-bd/investor-reporting/directory/2026-09-16/) merged. The Lambda now serves CodeSha256 JkY/lBc2Wucz/XIPzyH0zmJt22ucItxjDehbKJko6i4= and the host bundle is IB-rtc-9's 0XLkiPt4. AMENDMENT 3 is the battery re-run and the record: no code, no apply. Was: AMENDMENT 3 STAGED 07:5xZ; AMENDMENT 2 (branch adf6144691, drained @a4db909717) FAIL-measured on row W2-S56.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 (AMENDMENT 1 on R-44/R-45 @57bc083d45) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Rulings this cell executes:** R-44 / R-45, `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md` @57bc083d45 | **Decomp cell:** `IB-rtc-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3 + s.R3.6) | **outcome_ref:** FWD-7 (own), FWD-1

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-3-2` on branch `wk-irpt_bckend-3-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-3-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The rulings this cell executes:** R-45's second half (verbatim): "a REPO-SHAPED unpack (members named by repo path, extracted at `$W`) ... the dispatch reaches what the runner derives." And the PRD row B4 (v0.14, unchanged): one directory artifact per firm per business day in the FIRM's own bucket under `investor-reporting/directory/`, `latest.json` revisions r -> r+1, the previous revision retained.

**Where the round stands when you start:** IB-rtc-2 (amended) has merged: the bundle carries the 8-file closure with member names that are repo paths, three of them DISTRIBUTION members, and the host has proven the closure imports at repo shape by a manual extract. What the DEPLOYED dispatch still does (row S59): `refresh.runner_script` (`infra/aws/lambda/investor-reporting/directory/refresh.py:430-443` at e9dc18f302) extracts into the runner's own directory and relocates three FLAT names, so the closure cannot be placed by the dispatch as deployed.

**AMENDMENT 2 -- THE ISSUER'S RULING ON ROW W2-S55 (2.0.0_SA_COO~B, 2026-09-18 ~06:0xZ, within L5/L6: the dispatch's date semantics on this round's own surface).** The first pass proved the repo-shaped unpack on the host and then measured the real blocker: `refresh.py`'s `runner_script()` types an EXPLICIT `--as-of` equal to the Lambda's own clock business date, and `directory_runner.py`'s `select_business_date()` refuses a date that is not in the firm's completed source set -- Inflection's frontier lags one trading day, Cottonwood's two. **RULING: the dispatch passes NO explicit `--as-of`.** The runner's own trading-day walk selects each firm's NEWEST COMPLETED business date (the design `refresh.py` already relies on when it calls the runner with no date), which is CLAUDE.md's own law -- *everything is T-1 unless declared; one frontier, `lib/trading_calendar.py`*. The manifest's `as_of_business_date` is then the date the RUNNER CHOSE, read back from the runner's output or the landed artifact's own `as_of`, never the Lambda's clock; the missed-fire logic (`missed_business_dates`) is re-read against that and a fire whose runner date equals the previous manifest's date records `REFRESH_NOOP_SAME_FRONTIER` (or the function's existing equivalent, named) rather than a new revision. The face's "9 sources" is corrected to the ratified **10** (row W2-S54).

**What L5 adds:**
- (a) `refresh.py`: (AMENDMENT 2) `runner_script()` drops the explicit `--as-of` and the manifest records the runner's chosen date (unit tests: the recipe carries no `--as-of`; a manifest built from a runner date differing from the clock date carries the runner's; a same-frontier re-fire records the no-op outcome). The unpack recipe is ALREADY repo-shaped at HEAD (first pass @8eac86e417) and is not re-done: the recipe test -- `tar -xzf $W/bundle.tar.gz -C $W` with members that are repo paths, the three `mv` lines retired (or kept ONLY for a member the bundle still stores flat, stated), the member list printed by `tar -tzf` as before, and the import check unchanged. Read IB-rtc-2's result for the exact member names the bundle now carries; do not assume them. Unit-test the recipe text (the string the function returns) for the absence of `..` members and the presence of `-C $W`.
- (b) Deploy the directory root: `.tools/safe-apply.sh` from `infra/aws/terraform/investor-reporting/directory/` (state key its own), under a change-management entry whose OPEN sentinel is COMMITTED before the act and closed before the grading reads (bound 4); plan first and print `0 to destroy`; served `CodeSha256` verified against the built zip (R-40: both hashes in the instance).
- (c) The on-host sweep (the ratified 10-source instrument row W2-S54 names, `s3://opal-data-mdpf/diagnostics/aec-irpt-iam1/irpt_sweep_v2.sh` by its recorded sha256, read-only: 10 sources + 3 destinations, verdicts, positive control) BEFORE building.
- (d) Fire the deployed dispatch for `inf` and `cot` exactly as its schedule would (the manual invoke path IB-rt-6's result documents); read back through the mechanism IB-rt-6 built: run record, command status, the NEXT reconciliation read, `list-objects-v2` before/after under `s3://opal-data-inf/investor-reporting/directory/` and `s3://opal-data-cot/investor-reporting/directory/`, `latest.json` revision before -> after (a first mint reads absent -> r1 and says so), the artifact's `ETag` and `sha256` from downloaded bytes, the previous revision retained where one existed.
- (e) The 49 Financial arm: attempted ONCE through the same dispatch, expected BLOCKED at the 49f dimensions read with `AccessDenied`, recorded citing W2-S49/S53 and iam.tf:598-603 -- never worked around; the principal that will unblock it is IB-rtc-6/IB-rtc-7's (R-44), not this cell's.
- (f) Content sanity on what landed (real files, bound 12): row counts, firm-in-artifact equals bucket firm, `0 of N` name- or e-mail-shaped keys, typed ids at the boundary (bound 13).

**AMENDMENT 3 -- THE RE-RUN AFTER IB-rtc-9 AND IB-rtc-7 (2.0.0_SA_COO~B, 2026-09-18 ~07:5xZ, within L5/L6).** AMENDMENT 2 is DONE as code: `refresh.py` passes no explicit `--as-of`, the manifest is keyed by the runner's date, `same_frontier` / `REFRESH_NOOP_SAME_FRONTIER` exist, 33 of 33 unit tests pass, the artifact is deployed (`E7TMbaF9NBPm7rFIDkk7y22gNQiPRAGr9m9BqcpnkGM=` in `infra/aws/lambda/ci/lambda-source-map.json` @a4db909717) and the real fires PASSED the date check for the first time (row W2-S56) -- then died in `directory_runner.py` `validate_entries()` on `jsonschema.Draft202012Validator`, absent from the host's 3.2.0. That defect is IB-rtc-9's (the DS lane, bundle re-mint), and IB-rtc-7 rebuilds the Lambda artifact once more (K5) and fires all three firms' builds. **This amendment changes NO code and NO infrastructure.** What it does:

- **Worktree:** `/c/tmp/wk-irpt-3-2c` on branch `wk-irpt_bckend-3-2c` (every `/c/tmp/wk-irpt-3-2/` above reads as this path). Same serial, same deliverables home. Do NOT edit `refresh.py`, `expiry.py` or any Lambda member; do NOT apply; do NOT rebuild.
- **Arm (a):** the unit-test run only (`k of k`, k printed), on the tree as it is.
- **Arm (b) becomes READ-ONLY:** served `CodeSha256` of `irpt-directory-refresh` `==` `artifact_sha256` in `infra/aws/lambda/ci/lambda-source-map.json` at YOUR BRANCH TIP (IB-rtc-7's deploy updated that map before you were cut); the plan is NOT run; no ledger entry is opened because nothing is deployed.
- **Arms (c)-(f) stand as written**, with (d) fired against the deployed function exactly as the schedule does, expecting `inf` and `cot` `2 of 2` landed (or `REFRESH_NOOP_SAME_FRONTIER` for a firm whose frontier IB-rtc-7's fire already landed this trading day -- that outcome COUNTS AS LANDED for (d) when the reconciliation names the earlier command id with `REFRESH_OK` and the artifact's `as_of` equals the runner's frontier; print which branch each firm took), and (e) re-scoped: `49f` is NO LONGER expected BLOCKED -- after IB-rtc-7 its build lands under the assumed principal; record `49f`'s outcome as MEASURED (landed or not, with the same fields as (d)) and do not grade it in the token -- (d) at `2 of 2` is still the bar, and the token is unchanged.
- **The instance:** a fresh `proof_of_spec.json` replacing AMENDMENT 2's; EVERY artifact pinned to the commit that carried it (`PENDING-THIS-COMMIT` only for artifacts your final commit itself introduces; `the-refresh-builds-exercised.result.md` already exists at HEAD, so a row that touches it pins the commit that last changed it, or your own if you change it). Validate with `--governing-order` this face BEFORE the complete flip.

---

## DELIVERABLE

The `refresh.py` edit with its recipe test; the ledger entry + sentinel commits; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtc_3.py`, `IB-rtc-3_R33-AC1_battery_output.txt`, `the-refresh-builds-exercised.result.md`, the SSM transcripts (read-only), the proof instance.

---

## BOUNDS

- **Read-only on the host** except `/tmp` and what the RUNNER writes to its declared destinations; ONE `StartInstances` admitted; never a stop. ONE Terraform root (`directory/`), one apply, under ledger; no IAM change; no bundle mint (IB-rtc-2's). No cross-firm widening.
- The scheduled fire stays FWD-7's acceptance; the manual invoke is the QA exercise.
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

<criterion id="R33-AC1" cell_refs="IB-rtc-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtc_3.py</invocation><expect>IBR33-TWO-OF-THREE-DIRECTORIES-LANDED</expect></criterion>
**`R33-AC1` -- PASSES BY OUTPUT:** (a) the recipe carries `-C $W`, `0` `..` members AND `0` explicit `--as-of`; the manifest/date tests pass `k of k`; (b) plan `0 to destroy`, apply under ledger, served `CodeSha256 == built`; (c) the sweep, `10 + 3` verdicts with the control firing; (d) `inf` and `cot` `2 of 2` landed with key, `ETag`, `sha256`, revision before -> after, retained-or-first-mint, row count, and the reconciliation naming the same command ids with `REFRESH_OK`; (e) `49f` attempted once, `BLOCKED` at the named read, control cited; (f) key census `0 of N`, firm-in-artifact `2 of 2`. The token prints only when (a)-(f) hold with (d) at 2 of 2.

<criterion id="R33-AC2" cell_refs="IB-rtc-3" judgment="true"/>
**`R33-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the landed artifacts are the runner's real output for the business date or a degenerate first mint; what FWD-7's DONE WHEN still lacks (the scheduled fire; the 49 Financial third); whether the dispatch-to-reconcile loop closed on IB-rt-6's mechanism; and whether the repo-shaped unpack changed anything for the two firms beyond placement. No verdict.

<expected_criteria>R33-AC1, R33-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.md
infra/aws/lambda/investor-reporting/directory/
infra/aws/terraform/investor-reporting/directory/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-3` (s.R3.1 the rectangle; s.R3.6 AMENDMENT 1 -- the edges, seating and bounds of this cell as amended).
<owned_cells>IB-rtc-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut -- the zoned schedule cron(0 9 ? * MON-FRI *) America/New_York is ENABLED (IB-rt-6 RT6-AC2) and is NOT changed; the manual invoke is the QA exercise.
comp-iam: RUN at the cut -- comp-iam-usage reach-check mdpf-daily-runner-ec2-role 2026-09-17: PutObject ALLOWED on the bd and cot directory prefixes, implicitDeny on the control and on the 49f dimensions. BLIND SPOT: the simulation cannot see a bucket policy; arm (c) is the applied-plane read.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R33-AC1, R33-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.proof_of_spec.json R33-AC1,R33-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
