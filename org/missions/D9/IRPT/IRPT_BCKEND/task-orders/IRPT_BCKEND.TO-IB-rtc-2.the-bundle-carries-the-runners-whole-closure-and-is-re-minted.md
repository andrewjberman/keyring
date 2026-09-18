# TO IRPT_BCKEND.TO-IB-rtc-2 -- THE BUNDLE CARRIES THE RUNNER'S WHOLE CLOSURE AND IS RE-MINTED: the seven repo files directory_runner.py reaches by derivation are declared as members of the investor_reporting bundle, the bundle is re-minted through the guard's own mechanism, and the host proves it can import every member -- a Rule 13 DS act, the same gate the CTO's round-1 ruling 3(c) opened

<to_id>IRPT_BCKEND.TO-IB-rtc-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>staged -- assigned to the DS lane; becomes pending when the COO hands it over at the issuance (a head; no cross-slot wait). Its merge releases IB-rtc-3.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Round-2 slug:** L8/L9 @c1a8cd2543 (`3.0.0_SA_CVO`, msg 97752) | **Decomp cell:** `IB-rtc-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3) | **outcome_ref:** FWD-1, FWD-7 (dependency), FWD-5

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-3-ds` on branch `wk-irpt_bckend-3-ds`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-3-ds/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention; no `<paths>` entry needed). Round-3 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Python:** `py -3.12` (bare `python` may resolve to 3.14 without PyYAML). AWS through `.tools/aws`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call, so read files with the Read/Grep tools and keep a gated read in its own call.
- **You are a Tier-2 DS seat under a v3 round:** register on the broker under this full serial, arm `/watcher`, and take this order as your GO -- the hand-off message names it. You may send information-only messages; a question about the spec is a surprise row, not a message.

---

## THE CELL

**The row this cell closes (`IRPT_BCKEND-W2-S51`, worker ~2, 2026-09-12, verbatim one-line):** "THE MINTED BUNDLE CANNOT CARRY WHAT THE RUNNER ACTUALLY NEEDS. directory_runner.py reaches ELEVEN repo paths by derivation; the bundle declares four of them ... three of the remaining five are per-firm runner_common.py modules imported by repo path."

**The measurement it stands on (row `IRPT_BCKEND-W2-S49`, verbatim excerpt):** "the host has NO copy of any firm's runner_common.py (bounded find over /opt /home /srv -> 0 hits), and directory_runner.py instantiates one per firm BY REPO PATH in SourceSet.__init__ (data/assets/scripts/gold/runners_49f, data/inf/scripts/gold/runners_inf, data/cot/scripts/gold/runners_cot); the minted bundle investor-reporting.tar.gz carries exactly three members (directory_runner.py, holdings_snapshot.py, ids.py -- tar -tzf printed on the host) and none of them is a runner_common."

**What L5 adds (decomposition v0.3 s.R3):**

- The denominator is derived, not recalled: the SET of repo files `data/assets/scripts/gold/investor_reporting/directory_runner.py` reaches by import or by repo-path load (its own `_import_runner(...)` calls, module-level imports of first-party modules, and any file the three `runner_common.py` modules themselves import from the repo -- the transitive closure, printed as a list with its count). Row W2-S51 counted eleven references to seven distinct files at its vintage; you print YOUR count at HEAD and the diff against seven.
- Each member is declared in `.tools/safe_deploy_core.py` `CODE_TREES` bundle `investor_reporting` exactly as IB-rt-5 declared the first members (read that cell's face and result under this deliverables home first; copy its shape, not its list). The bundle is re-minted with `.tools/safe-deploy.sh --mint-bundle investor_reporting` -- NEVER a bare `aws s3 cp` -- under a change-management entry whose OPEN sentinel is committed before the act and whose close is committed before the grading reads (bound 4).
- Verification on the SERVED artifact and on the HOST, never on the report: `head-object` on the minted key printing `ETag` and `source-repo-paths`; the members listed by `tar -tzf` ON the mdpf daily-runner host by an SSM `AWS-RunShellScript` that is READ-ONLY and writes only under `/tmp` (the pattern rows W2-S49/W2-S53 used; the host `i-02448edb624a7a7cf` must be RUNNING -- if it is stopped, ONE `StartInstances` is admitted exactly as IB-rt-6 did, and NEVER a stop, bound: the mdpf daily chain owns that lifecycle); then an on-host `python3 -c` import of `directory_runner` that instantiates `SourceSet` for all three firms, printing `IMPORT-OK <firm>` per firm or the exception verbatim. R-40: the minted tarball's `sha256` (computed from the downloaded bytes on the host) recorded beside its `ETag`, and each member's `git hash-object` at your branch tip recorded in the instance.
- A member the closure needs that is NOT under a `data/*/scripts/gold/**` or `lib/**` path this order's `<paths>` admits is a BLOCKING row, not an override.

---

## DELIVERABLE

The `CODE_TREES` edit; the guard's tests green (counts printed); the re-minted key and its `ETag`+`sha256`; the ledger entry + sentinel commits; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_2.py` with its `.result.md` and `IB-rtc-2_R32-AC1_battery_output.txt`; the proof instance.

---

## BOUNDS

- **Rule 13 binds you as the DS lane:** the mint is yours; no worker and no other seat may take it. The QA-deploy is through `.tools/safe-deploy.sh` only.
- **Read-only on the host** except `/tmp`; **never** `StopInstances`/`TerminateInstances`; no runner is EXECUTED end-to-end here (IB-rtc-3 does that, after your merge) -- the import check instantiates and returns.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object` for a tracked file, `sha256sum` for a produced object, the service's own digest such as `ETag`/`CodeSha256` for a served one) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-D-S<k>` with k continuing that coordinate's numbering (read the file's highest `D-S<k>` first; the file holds ONE fenced json array -- append your object inside it at the end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp like `2026-09-18T02:00:00Z`, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R32-AC1" cell_refs="IB-rtc-2"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_2.py</invocation><expect>IBR32-CLOSURE-MINTED-AND-IMPORTS-ON-HOST</expect></criterion>
**`R32-AC1` -- PASSES BY OUTPUT -- every arm prints its denominator:** (a) the closure `N of N` members declared in `CODE_TREES` (N printed, the list printed, the diff against W2-S51's seven printed); (b) the guard's own tests pass (`k of k`); (c) the minted key's `head-object` prints `ETag`, `source-repo-paths` naming every member, and the tarball `sha256`; (d) `tar -tzf` ON THE HOST lists `N of N` members; (e) the on-host import prints `IMPORT-OK` for `3 of 3` firms; (f) the NEGATIVE CONTROL: the PREVIOUS tarball (its `ETag` from IB-rt-5's instance) is shown to have carried `3` members, so the arm can tell a re-mint from a no-op. The token prints only when (a)-(f) all hold.

<criterion id="R32-AC2" cell_refs="IB-rtc-2" judgment="true"/>
**`R32-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which members the closure needed beyond W2-S51's seven and why; whether any member's presence in a shared DS-lane bundle widens what the mdpf host can execute in a way the cross-firm bound (s.8 item 3) should hear about; and whether the host's import succeeded for the 49 Financial firm's module without reading any 49 Financial DATA (it must -- an import is not a read). No verdict.

<expected_criteria>R32-AC1, R32-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.md
.tools/safe_deploy_core.py
.tools/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-2` (s.R3.1 the rectangle; s.R3.2 the edges and the fence; s.R3.3 the seating; s.R3.4 the bounds carried; s.R3.5 what it does not decide).
<owned_cells>IB-rtc-2</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, rule or trigger is created, changed or fired; one StartInstances is admitted and is not a schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; the mint runs under the DS lane's own existing grant through the guard. BLIND SPOT stated: the guard's S3-membership check is the control, measured by arm (c).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R32-AC1, R32-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-2.the-bundle-carries-the-runners-whole-closure-and-is-re-minted.proof_of_spec.json R32-AC1,R32-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why). You cannot send or receive messages -- anything you would ask is a surprise row.
