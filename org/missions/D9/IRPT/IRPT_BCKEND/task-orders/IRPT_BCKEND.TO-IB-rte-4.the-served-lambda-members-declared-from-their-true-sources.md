# TO IRPT_BCKEND.TO-IB-rte-4 -- THE SERVED LAMBDA MEMBERS DECLARED FROM THEIR TRUE SOURCES: four production members (`holdings/served.py`, `holdings/loaders.py`, `directory/errors.py`, `directory/trading_calendar.py`) are served but not tracked at the path the build reads -- their sources are tracked ELSEWHERE (`_authz/`, `lib/`) as undeclared copies with no vintage (rows W1-S20, W2-S59; the CTO's correction: NOT code with no source, so NOT a third copy); the build manifest's `files[]` is made to declare the true source (or stage from a pinned blob), every served zip member is verified against its declared source by hash (the CVO's INFERRED made VERIFIED), and every investor-reporting function builds from a CLEAN checkout with no manual staging

<to_id>IRPT_BCKEND.TO-IB-rte-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>superseded -- CLOSED for round 5 by 2.0.0_SA_COO~B at 2026-09-19T03:4xZ: its FAIL (2 of 9 functions with no-source members) is round 6's FIRST cell, IB-rtf-1, on the CTO's L4 ruling @457cf494c6; the 48 declarations and the pinned-blob mechanism stand at HEAD. Was: pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T19:0xZ to slot ~4 (cold start) on the round-4 analysis s.8 item 4 and rows W1-S20 / W2-S59 (ARMED, disarm_owner 2.0.0_SA_COO~B).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 5 (the CTO's round-4 analysis @561d6e1cc9, msg 98036) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 4) | **Round-4 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md` @561d6e1cc9 | **Andrew-direct:** 2026-09-18 ~17:3xZ "Approved" (record `org/tier1_exec/2.0.0_SA_COO~B/deliverables/ANDREW_DIRECT_20260918_173xZ_TWO_OPEN_CALLS_APPROVED_IRPT_BCKEND.md` @af794c77e3) | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30 | **Decomp cell:** `IB-rte-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.5, s.R5) | **outcome_ref:** FWD-1, FWD-7 (the served functions' provenance)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-5-4` on branch `wk-irpt_bckend-5-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-5-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The finding, corrected by the CTO (analysis s.5/s.8 item 4):** W1-S20 and W2-S59's rows are right -- `build-and-upload.sh` fails out of the box on `irpt-holdings` (`served.py`, `loaders.py`) and `irpt-directory-refresh` (`errors.py`, `trading_calendar.py`) because those paths under the functions' `source_dir` are tracked at no revision; both workers rebuilt by copying from the live zip / canonical sources and did not commit the copies. **But the hand-off summary "committed at NO revision" was WIDER than the rows:** `served.py` and `loaders.py` are tracked at `_authz/`, `errors.py` at `_authz/` and `holdings/`, `trading_calendar.py` at `lib/` plus three Lambda-local copies. *"It is SERVED CODE WHOSE SOURCE IS AN UNDECLARED COPY WITH NO VINTAGE. THE REMEDY IS TO DECLARE THE TRUE SOURCE IN files[] OR STAGE FROM A PINNED BLOB -- NOT TO COMMIT A THIRD COPY."* The build reads `infra/aws/lambda/ci/lambda-source-map.json` `functions[<name>].files[]` relative to `source_dir` (`build-and-upload.sh:173-174, :195, :209-240 @HEAD` -- the parity check ADHC_DRIFTD.002 and its `BAU_PARITY_SKIP` override, row W2-S58).

- (a) THE CENSUS, unscoped then scoped: for every function in the investor-reporting family (`N of N` from the source map), every member of its SERVED zip (download, list, hash) against the source map's `files[]` and against the repo: per member, one of TRACKED-AT-PATH / TRACKED-ELSEWHERE (where, blob hash, equal or not) / UNTRACKED-ANYWHERE. Print the table with its denominators. The four named members are the known cases; the census says whether there are more (W1-S20's class named a memory pattern -- read `memory/feedback_structural_over_cultural_pattern.md` item 6 and say whether this is the same instance).
- (b) THE REMEDY, the CTO's: make `files[]` (or the builder) declare each served member's TRUE SOURCE -- a source path outside `source_dir` (e.g. `../_authz/served.py`, `../../../../lib/trading_calendar.py`) staged at build time, with the builder change MINIMAL in `build-and-upload.sh` if `files[]` cannot already express an out-of-dir source (read the script first; cite the line that resolves a file; a pinned-blob form `path@<commit>` is admissible if the builder verifies the blob hash). No third copy is committed. The parity check must still pass WITHOUT `BAU_PARITY_SKIP` for every function (W2-S58's false-flag on a shared `source_dir` is fixed or explained by the same change -- say which).
- (c) VERIFIED, NOT INFERRED: for every function, the zip built from a CLEAN checkout (`git stash -u` is banned; use a fresh `git worktree add --detach` of your branch tip) equals the SERVED zip member-for-member by sha256 -- `N of N` functions, `m of m` members; where a member differs, print which and why (a build-time timestamp is not a content difference -- compare members, not the zip). Expect `0` functions needing a deploy; if any differs in content, deploy it under ledger (`0 to destroy`, served `CodeSha256 == built`) and say so.
- (d) THE CONTROL: with the four declarations removed (a mutant manifest, in scratch only), the build FAILS for both functions exactly as W1-S20/W2-S59 recorded; with them present it SUCCEEDS from the clean checkout with `0` manual staging steps.

---

## DELIVERABLE

the source-map / builder change; `battery_ib_rte_4.py`, `IB-rte-4_R54-AC1_battery_output.txt`, `the-served-members-declared.result.md` (the census table); the proof instance.

---

## BOUNDS

- NO third copy of any member is committed; the ONLY code paths touched are `infra/aws/lambda/ci/` (the builder + source map) and, if a function's content genuinely differs from its served zip, that function's deploy under ledger. `BAU_PARITY_SKIP` is never set in the graded run. The served functions are not redeployed when their content is unchanged.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W4-S<k>` with k continuing that coordinate's numbering (read the file's highest `W4-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R54-AC1" cell_refs="IB-rte-4"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rte_4.py</invocation><expect>IBR54-SERVED-MEMBERS-DECLARED-FROM-TRUE-SOURCES-VERIFIED</expect></criterion>
**`R54-AC1` -- PASSES BY OUTPUT:** (a) the census `N of N` functions x `m of m` members with each member's class and hashes; (b) the true sources declared with no third copy, parity passing without the override `N of N`; (c) clean-checkout builds equal the served zips member-for-member `N of N`, or the differing functions deployed under ledger with `CodeSha256 == built`; (d) the mutant manifest FAILS both builds and the real one SUCCEEDS with `0` manual steps. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R54-AC2" cell_refs="IB-rte-4" judgment="true"/>
**`R54-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the family has other undeclared-copy members beyond the four (the census says), whether `_authz/` should be a shared package rather than copied into each function (a shape question for L4), and whether the builder change is the estate's to keep (`infra/aws/lambda/ci/` serves every Lambda family, not this project's alone -- name the owner). No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R54-AC1, R54-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-4.the-served-lambda-members-declared-from-their-true-sources.md
infra/aws/lambda/ci/
infra/aws/lambda/investor-reporting/
infra/aws/terraform/investor-reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.5, cell `IB-rte-4` (s.R5 -- the round-5 rectangle, edges, seating and bounds).
<owned_cells>IB-rte-4</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; a deploy, if any, runs under the functions' existing roles.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R54-AC1, R54-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rte-4.the-served-lambda-members-declared-from-their-true-sources.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rte-4.the-served-lambda-members-declared-from-their-true-sources.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rte-4.the-served-lambda-members-declared-from-their-true-sources.md` BEFORE the complete flip; rc 0 AND R54-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
