# TO IRPT_BCKEND.TO-IB-rtd-8 -- THE FIRM CHECK RESTORED ON THE OPERATIONS-VIEWER BRANCH: `Enforcer.covers()` returns an unconditional True for a FIRM_OPERATIONS or OPAL_GLOBAL principal on the advisor axis, admitting ANOTHER FIRM's advisor id although its own docstring says 'within the verified firm' (row W1-S16, ARMED since round 1, the first round-4 cut per S57) -- and the branch exists in TWO copies of the enforcer; both are fixed, unit-tested with the six-swap census, deployed under ledger, and proven on the live routes

<to_id>IRPT_BCKEND.TO-IB-rtd-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~1, 2026-09-18. R48-AC1 PASS-by-output (battery_ib_rtd_8.py rc=0, token IBR48-FIRM-CHECK-RESTORED-ON-BOTH-ENFORCERS, 9 of 9 arm-checks); R48-AC2 judgment RECORDED for 3.0.0_SA_CVO, no verdict taken. The issuer's Rule-22 census was itself stale (row IRPT_BCKEND-W1-S19): `_authz/enforce.py` was already fixed at 49035683d1 (round 2), an ancestor of the cited pin; `holdings/enforce.py` is a PINNED, COMMITTED-BLOB mirror of it (holdings/stage.py), stale at a pre-fix pin -- re-staged to the fixed content, deployed under ledger `irpt-bckend-rtd8-holdings-advisor-fix` (CLOSED), and proven live (7 of 7 functions serve the fix; 0 of 7 routes reach the branch, VACUOUS-measured). proof-of-spec-check rc=0 VALID. Second row filed: IRPT_BCKEND-W1-S20 (untracked served.py/loaders.py gap, worked around, not repaired).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 4 (the CTO's round-3 analysis @5c59f68d70, msg 97944) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 3) | **Round-3 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md` @5c59f68d70 | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar (analysis s.4, ADOPTED) | **Decomp cell:** `IB-rtd-8` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.4, s.R4) | **outcome_ref:** FWD-2, FWD-11

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-4-1` on branch `wk-irpt_bckend-4-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-4-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**The finding (row W1-S16, `0.9.0_WK_IRPT_BCKEND~1`, round 1; carried at S57):** `_authz.Enforcer.covers()` admits any advisor id for a FIRM_OPERATIONS or OPAL_GLOBAL viewer, including another firm's -- `if scope["principal_class"] in ("FIRM_OPERATIONS", "OPAL_GLOBAL"): return True, 'a firm-authorized viewer may address any advisor in its own firm'`, an unconditional True where the docstring promises 'within the verified firm'. No cross-firm BYTES are reachable through it today (the firm axis is checked upstream), which is why it was OBSERVATION not BLOCKING -- and ARMED because the branch is shared by every route behind `guard()`, and any later cell that makes an advisor id load-bearing (a per-advisor cache key, filter or export) inherits the gap. **The issuer's census (Rule 22, the shared premise): the branch exists at `infra/aws/lambda/investor-reporting/_authz/enforce.py:351 @5c59f68d70` AND at `infra/aws/lambda/investor-reporting/holdings/enforce.py:319 @5c59f68d70` -- two copies, one defect.**

- (a) THE FIX, both copies: the branch checks that the advisor id belongs to the VERIFIED firm (the firm's advisor set the loaders already resolve -- cite the loader `file:line @ commit`) before returning True; the reason string states what was checked; an advisor id outside the firm is refused with a reason that does NOT echo the refused value (bound 13). If the two copies are meant to be one module, say so as a row; do not consolidate them here (never fix a neighbouring defect).
- (b) TESTS: the six-swap census from round 1's arm (each principal class x own-firm advisor / other-firm advisor), `12 of 12` verdicts as the docstring promises, on BOTH copies; the MUTANT (the unconditional True) fails the other-firm arms `n of n`. Whole-suite `k of k` for both Lambda directories.
- (c) DEPLOY under ledger every function that packages either copy (`lambda-source-map.json` names them -- `N of N` functions, denominator printed; plan `0 to destroy`; served `CodeSha256 == built` per function).
- (d) PROVEN ON THE LIVE ROUTES: for each deployed route behind `guard()` that accepts an advisor id (`M of M`, enumerate from the route table, not from memory), a FIRM_OPERATIONS request naming an other-firm advisor id reads a refusal (`403`/the contract's refusal shape) and the same request naming an own-firm advisor id reads as before -- with a real signed request per the round-1 harness, never a stubbed handler.

---

## DELIVERABLE

both `enforce.py` edits + tests; the ledger entries; `battery_ib_rtd_8.py`, `IB-rtd-8_R48-AC1_battery_output.txt`, `the-firm-check-restored.result.md`; the proof instance.

---

## BOUNDS

- The two `enforce.py` files and their tests are the ONLY code touched; no route, loader or contract change; no IAM.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` with k continuing that coordinate's numbering (read the file's highest `W1-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R48-AC1" cell_refs="IB-rtd-8"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rtd_8.py</invocation><expect>IBR48-FIRM-CHECK-RESTORED-ON-BOTH-ENFORCERS</expect></criterion>
**`R48-AC1` -- PASSES BY OUTPUT:** (a) both copies fixed, the refusal echoing nothing; (b) `12 of 12` swap verdicts on both copies, mutant failing `n of n`, suites `k of k`; (c) `N of N` functions deployed under ledger with `CodeSha256 == built`; (d) `M of M` live routes refuse the other-firm advisor and admit the own-firm one. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R48-AC2" cell_refs="IB-rtd-8" judgment="true"/>
**`R48-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the two enforcer copies should be one module (and which project owns that consolidation), whether any route makes an advisor id load-bearing today beyond an audit line, and whether FWD-2/FWD-11's cross-firm bar is now closed on the advisor axis or only narrowed. No verdict. Every line citation carries `@<commit-ish>` (S56).

<expected_criteria>R48-AC1, R48-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-8.the-firm-check-restored-on-the-operations-viewer-branch.md
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/holdings/
infra/aws/terraform/investor-reporting/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.4, cell `IB-rtd-8` (s.R4 -- the round-4 rectangle, edges, seating and bounds).
<owned_cells>IB-rtd-8</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired; the deploy is a code change on request-path functions.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the functions' roles are unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R48-AC1, R48-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtd-8.the-firm-check-restored-on-the-operations-viewer-branch.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance, so no `PENDING-THIS-COMMIT` sentinel is needed); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtd-8.the-firm-check-restored-on-the-operations-viewer-branch.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-8.the-firm-check-restored-on-the-operations-viewer-branch.md` BEFORE the complete flip; rc 0 AND R48-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
