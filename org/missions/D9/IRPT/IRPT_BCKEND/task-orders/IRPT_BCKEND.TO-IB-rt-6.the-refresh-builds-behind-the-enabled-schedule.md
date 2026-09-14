# TO IRPT_BCKEND.TO-IB-rt-6 -- THE REFRESH BUILDS: a real build_fn behind the ENABLED directory schedule -- the minted runner executed on the estate's scheduled-gold host pattern -- with source completion, new revision, expiry and missed trigger proven by before/after artifacts for all three firms

<to_id>IRPT_BCKEND.TO-IB-rt-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-12T05:48:29Z. Its gate ('after IB-rt-2, IB-rt-3 and IB-rt-5 are terminal and merged') is SATISFIED on all three, each proof-of-spec instance re-graded VALID rc=0 at HEAD by the issuer rather than taken from a report. Third order of slot ~2.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 3(a) | **Slug rows this cell closes:** C-S73 (refresh half) | **Decomp cell:** `IB-rt-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-7 (own), FWD-1 | **PRD candidate:** B4

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-2-2` on branch `wk-irpt_bckend-2-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** third in slot ~2, after IB-rt-1 and IB-rt-2; cross-slot waits on IB-rt-3's normalizer and IB-rt-5's minted runner. IB-rtb-1 replays the served directory after this cell.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B4 directory refresh schedule, expiry/fallback, controlled-clock harness
- **serves:** FWD-7 (own)
- **brief sections consumed:** O1 refresh; O7 clocks/manifests; IV.2 business-date paragraph
- **contracts (P=produces, C=consumes):** P `DirectoryEntry.revision`; P `StatusEnvelope` (stale)
- **paths: reuse:** `lib/trading_calendar.py`; each source's completion manifest
- **paths: new home:** `infra/aws/terraform/investor-reporting/` (scheduler)
- **fixtures / evidence:** source fixtures for the five arms
- **acceptance clause draft:** all five arms driven on a controlled clock: added client, changed eligibility, MISSED trigger, FAILED refresh, OVER-AGE request -- each reads differently; no real-calendar wait

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** WIRE THE THREE DECLARED PRODUCERS. (a) directory refresh: a real build_fn behind the ENABLED schedule, source completion / new revision / expiry / missed-trigger proven with before/after artifacts for all three firms.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- The mechanism is the ESTATE's, not invented: `infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py` is the pattern -- a trigger Lambda issues an SSM command to the mdpf daily-runner host (`infra/aws/ec2/mdpf-daily-runner/`, `EC2_MANIFEST.json`) that pulls the minted script from `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/` and runs it with the host's own python and dependencies. `directory/refresh.py`'s `build_fn` becomes exactly that: dispatch the minted `directory_runner.py` for one firm on one business date via SSM, wait bounded for completion, read the runner's completion manifest, and record COMPLETED / FAILED / MISSED as the round-1 envelope already does. `build_dispatch: NOT_WIRED` becomes a real value on every manifest.
- Before/after artifacts for 3 of 3 firms under the PRODUCTION prefixes (`<firm bucket>/investor-reporting/directory/<as_of>/`), each run under a change-management entry: the `latest.json` revision advances, the new revision carries the normalized ids of IB-rt-3, and the previous revision is retained (immutable revisions).
- The four arms on the deployed schedule, driven (no real-calendar wait): source completion (a firm's manifest date advances -> the next fire builds), new revision (artifact hash differs, revision +1), expiry (an over-age read hits the declared fallback), missed trigger (the schedule's fire skipped -> MISSED in the envelope) -- the controlled-clock harness of IB-s-4 re-run against the real build path.
- The runner's own dependencies on the host are measured, not assumed: the first SSM run prints the host's python and the import check of the runner's modules.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`irpt-directory-refresh` live with `build_fn=None` recording `NOT_WIRED` honestly; the ENABLED schedule `cron(0 9 ? * MON-FRI *)` America/New_York; `expiry.py`; the controlled-clock harness (IB-s-4); the runner (IB-s-1) and its first-mint (IB-rt-5); the mdpf trigger pattern and the daily-runner host.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~13:2xZ, at IB-rt-5's report, before this order was handed -- three facts the DS lane measured that this cell builds on; recorded in the commit and on the channel after the DS re-mint merges):**
- **THE MINT IS ONE TARBALL, NOT TWO LOOSE KEYS.** `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` (26,935 bytes at the mint; per-member sha metadata `directory-runner-sha256`, `holdings-snapshot-sha256`, each equal to the repo file's) is the served artifact; the loose per-file keys are permanent 404s BY DESIGN of the ratified bundle mechanism. The SSM dispatch pulls the tarball and unpacks it (the `mdpf-accrual-trigger` shape: `tar -xzf` on the host), never a per-file `s3 cp`. The round-1 batteries `battery_ib_s_4.py` and `battery_ib_s_12.py` grade "served" on the loose keys and probe a bundle name that does not exist -- they are FROZEN round-1 evidence and say the opposite of the world now; this cell does not re-run them as evidence (DS row on the channel after the re-mint).
- **THE RUNNERS IMPORT FIRST-PARTY CODE BY REPO SHAPE.** Both runners reach `lib/trading_calendar.py` through `_REPO = Path(__file__).resolve().parents[4]` then `sys.path.insert(_REPO/"lib")`, and import `boto3`, `jsonschema`, `pandas`. Unpacked FLAT into `/opt/mdpf/scripts/gold/` the way `accrual_bridge` is, `parents[4]` is not a repo root and the import raises before any runner logic runs. The SSM run therefore unpacks into a repo-shaped path on the host (or the host's tree carries `lib/` at the expected depth) and arm (d) prints the import check's stdout -- the runner's modules, `pandas` and `trading_calendar` each resolved -- BEFORE the first build; a missing dependency on the host is a BLOCKING row and arm (d) reads BLOCKED. No runner is edited to change its import shape here (a change to the runners is a row for the IRPT lane's L10, since the minted bytes and the repo bytes must stay equal).
- **NOTHING CONSUMES THE TARBALL YET** (the DS lane's census: 9 hits across 31,208 files, none a consumer): this cell is the first consumer, and the ledger entry of the first real build names the tarball's ETag it ran.

---


---

## ISSUER AMENDMENT -- 2026-09-12T05:48:29Z (`2.0.0_SA_COO~B`): THE HAND-OFF. Governs over every line above it.

### G1. YOUR GATE IS SATISFIED ON ALL THREE AND THIS ORDER IS PENDING.
`IB-rt-2`, `IB-rt-3` and `IB-rt-5` are all terminal and merged, each instance re-graded `VALID rc=0` at HEAD by the
issuer rather than taken from its report. Round 2 stands at 10 of 12. **Begin immediately.** `IB-rtb-1` -- the last
cell of the round -- is gated on THIS order, so nothing else in the round moves until it closes.

### G2. NEW WORKTREE. Whatever IDENTITY names above, it is not where you work.
- **Worktree:** `/c/tmp/wk-irpt-2-2c` on branch `wk-irpt_bckend-2-2c`, cut from CLOUD at `3dce524340`.
- Every path in this face is relative to that root; prefix `/c/tmp/wk-irpt-2-2c/` to make one absolute.
- ⛔ **`/c/tmp/wk-irpt-2-2b` IS GONE** -- IB-rt-2 is terminal and its worktree and branch are removed. Do not look
  for it.
- First act: `git rev-parse --abbrev-ref HEAD`, then `test -d org && test -d .tools && echo TREE-OK`.

### G3. YOU CARRY IB-rt-2's CONTEXT, AND THAT CUTS BOTH WAYS.
You are the subagent that ran IB-rt-2, so you are not cold. What transfers:
- **The deploy discipline you just executed three times**: one root at a time, each function verified on SERVED
  bytes by extract-and-import in the flat `/var/task` layout in a fresh interpreter with the repo off `sys.path`,
  three-way hash equality, ledger opened only with room to close it and its OPEN sentinel committed BEFORE the act.
- **Your own five hard-won rules**, all of which apply here: a duplicated fact is a defect whose latency ends at the
  next grant, and the fix is to DELETE a copy rather than sync it; a post-apply `No changes` is PERISHABLE in two
  directions (another cell's commit, or your own stale worktree over a shared state) and the plan output is
  identical either way; `git log -- <path>` answers *what last touched this path*, never *what changed this thing*
  (use `-S<token>`); a green arm is not licence for the prose beside it; and print `0 subject file(s) differ from
  HEAD` beside your token.
⛔ **What does NOT transfer is any grant.** IB-rt-2's `<paths>` retired when it went terminal. **This order's
`<paths>` block is the whole of your write surface** -- read it, and if a path you need is missing, that is a
BLOCKING row to me and NOT a prose sentence you can act on. I made exactly that mistake on IB-rt-2 (amendment 3's
C1 granted `holdings/` in prose the gate cannot read) and it cost you a blocked commit. **A grant is only real in
the surface the enforcer reads.**

### G4. THE CELL'S OWN LAW: THE SCHEDULE IS ENABLED, SO THE BUILD MUST BE TRUE BEFORE IT FIRES.
This cell is about the refresh building BEHIND an enabled schedule. Two things follow and both are measured, never
asserted:
- **Read the trigger state LIVE, never from the `.tf`.** `aws events describe-rule` is the instrument; a rule's
  declared state and its live state are different claims. This round has already paid for that twice -- the
  ycharts probe rule reads ENABLED while its function serves a retired predicate, and a capture rule reads DISABLED
  while its source still carries the legacy body.
- **An ENABLED schedule means the world can fire your code before you are finished.** If any step of this cell
  leaves a window where the scheduled run would produce a wrong artifact, that window is a BLOCKING row before it
  is a design choice. Say which steps have one.

### G5. STANDING MECHANICS, UNCHANGED.
Prove each criterion by RUNNING the invocation the face names and showing the expectation met by OUTPUT. **The
acceptance token enters the battery output ONLY in the edit that makes every arm pass, never negated** -- the
`<expect>` is a REGEX and a "NOT ASSERTED" line MATCHES. `PENDING-THIS-COMMIT` is ONE-SHOT; pin each artifact row to
the commit that CARRIES it. A judgment criterion gets its output and NO verdict, with a `status_reason` naming
`3.0.0_SA_CVO`. **The flip is the LAST act** -- after it, re-run the invocation and read `git status --porcelain`,
because two cells tonight flipped on a run that did not reproduce. Rows are `IRPT_BCKEND-W2-S<k>`; re-read the
channel at HEAD immediately before minting (176 rows and moving). `safe-commit.sh` with explicit FILE paths and a
Write-tool message file; your branch only; never push, merge, rebase, `checkout --` or `clean`. A rail denial aborts
the WHOLE Bash call and silently no-ops every later segment.


## DELIVERABLE

`infra/aws/lambda/investor-reporting/directory/refresh.py` with the real `build_fn` (SSM dispatch) and its IAM (`ssm:SendCommand` on the named host, least privilege, in `infra/aws/terraform/investor-reporting/directory/`); the runner's completion-manifest contract; the three production builds and their before/after records; the ledger entries + sentinels; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_6.py` and `.result.md`.

---

## BOUNDS

- **The host is the estate's scheduled-gold host; no new EC2, no container, no pandas layer in a Lambda.**
- **A production build writes ONLY under the firm's own `investor-reporting/directory/` prefix**; the previous revision is never deleted.
- **The schedule stays ENABLED; its first REAL fire is observed, not waited for**: the battery drives the trigger's handler directly with a controlled clock and reads the same artifacts the scheduled fire would produce.

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

<criterion id="RT6-AC1" cell_refs="IB-rt-6"><invocation>timeout 1500 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_6.py</invocation><expect>IBRT6-REFRESH-BUILDS</expect></criterion>
**`RT6-AC1` -- PASSES BY OUTPUT -- three firms built for real, four arms on the real path, revisions immutable.**
**(a) WIRED.** `refresh.py` calls the SSM dispatch (source census: `build_fn=None` = 0 sites); the deployed function's manifest after one driven fire reads `build_dispatch: SSM` with the command id (printed, secrets none).
**(b) THREE OF THREE, BEFORE/AFTER.** Per firm: the `latest.json` revision before and after (r -> r+1), the artifact hash differs, the previous revision object still present (`head-object`), the entry count with its denominator, 0 ids carrying `:acct:` (census).
**(c) FOUR ARMS.** Source completion, new revision, expiry, missed trigger -- each reads its own distinct envelope value on the real build path (`4 of 4`, pairwise distinct).
**(d) THE HOST CAN RUN IT.** The SSM run's stdout shows the runner's import check passing on the host (module names printed) -- or a BLOCKING row naming the missing dependency and this arm reads BLOCKED.
**(e) LEDGERS.** Every entry CLOSED, sentinels committed (hashes); the directory root's post-apply plan `No changes`.

<criterion id="RT6-AC2" cell_refs="IB-rt-6" judgment="true"/>
**`RT6-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what a scheduled fire can do that the driven fire did not (the host's own state, a concurrent mdpf run, a stopped host); how a failed SSM dispatch is distinguished from a failed build in the envelope; and what the as-of an advisor reads now measures. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT6-AC1, RT6-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-6.the-refresh-builds-behind-the-enabled-schedule.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/directory/
infra/aws/terraform/investor-reporting/directory/
data/assets/scripts/gold/investor_reporting/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt6.json
infra/aws/lambda/ci/lambda-source-map.json
.tools/safe_deploy_core.py
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-6` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the round-1 cut (5 of 5 carriers, 25 gates ARMED, 0 naming IRPT); this cell CHANGES a schedule's target or a function behind one -- `comp-schedule` is re-run by the assignee at Phase 1 and recorded in the instance. BLIND SPOT: a ledger of gates, not prose obligations.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-directory-refresh` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-directory-refresh` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT6-AC1, RT6-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-6.the-refresh-builds-behind-the-enabled-schedule.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-6.the-refresh-builds-behind-the-enabled-schedule.proof_of_spec.json RT6-AC1,RT6-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.

---

## ISSUER AMENDMENT H -- 2026-09-12T06:38:56Z (`2.0.0_SA_COO~B`). Governs over every line above it. **FOUR RULINGS AND A REDIRECT.**

Your G4 reading is accepted and it is the kind of thing that should never be inferred: the trigger is an EventBridge
**Scheduler schedule**, not a Rule, so `describe-rule` returns `ResourceNotFoundException` -- **a false absence if
read carelessly** -- and `scheduler get-schedule` reads ENABLED, `cron(0 9 ? * MON-FRI *)` America/New_York. You also
said the right thing about the 55-hour window: **that is calendar luck, not a property of any plan.** Do not build on
it.

### H1. ⛔ THE FOURTH OPTION IS REFUSED. You were right not to take it, and it is refused by LAW, not by preference.
Having the host extract `ids.py` out of an existing Lambda artifact zip is **a shadow distribution channel** --
bytes reaching a runtime by a route nothing declares. CLAUDE.md carries Andrew's COMPLETE VETO on shadow and
build-alongside channels. **Never raise it again and do not let a later cell rediscover it as clever.** That you
named it and handed it up instead of taking it is the correct handling of an option you can see is out of bounds.

### H2. THE BLOCKER IS MINE TO CLEAR AND I AM CLEARING IT IN THE `<paths>` BLOCK, NOT IN PROSE.
**Your lane reading was wrong, and the error is understandable:** you said the member list in
`.tools/safe_deploy_core.py` is out of lane. **Measured at `.owned-paths.yaml:2003-2009`: `.tools/**` is lane `ANY`**
-- "Shared .tools/ -- any agent may contribute tooling" -- and the only narrower entries under `.tools/` are
`git-hooks/**`, `tests/**`, `surprise-row-gate.py` and `to-pipeline-gate.py`, none of which match. So
`safe_deploy_core.py` was never out of LANE. It was out of **this order's `<paths>`**, which is a different thing.

**GRANTED, in the block, in this amendment's commit:**
```
.tools/safe_deploy_core.py
```
I put it in the BLOCK because I granted `holdings/` to IB-rt-2 in a PROSE SENTENCE the gate cannot read and it cost
that order a blocked commit on four finished files. **A grant is only real in the surface the enforcer reads.**

### H3. ⛔ AND DECLARING `ids.py` AS A BUNDLE MEMBER IS **NOT** A SECOND COPY. This is the distinction the cell turns on.
You declined to copy `ids.py` into the in-lane bundle directory because that would be a second copy of THE ONE
opaque-id normalizer, which `irpt-holdings`' own BUILD_MANIFEST forbids in those words. **Correct -- a FILE COPY
would be a second definition.** But adding `ids.py` to the member list so the packager RESOLVES IT FROM `_ids/ids.py`
at build time is a **DISTRIBUTION**, not a definition. There is one source of truth and the bundle carries a copy of
it the way every zip does.
**Two precedents, both already in this estate and one of them inside this very bundle:**
- `lambda-source-map.json` declares `ids.py` as a FLAT BUILD INPUT for three functions -- that is the mechanism I
  ruled on for IB-rt-2, and it is the same shape.
- **`trading_calendar` already resolves from its real distribution on that host**, which you measured yourself. The
  bundle already carries a module it does not define.
So: **declare the member, resolve it from `_ids/`, copy no file.** If the packager cannot resolve it from `_ids/`
without a copy, that is a BLOCKING row -- not a copy you make anyway.

### H4. W2-S46 IS RESOLVED BY READING THIS FACE'S OWN SOURCE, NOT BY CHANGING A TIMEOUT. **SEND AND RETURN.**
You found the named pattern does not wait -- `mdpf-accrual-trigger` sends and returns -- and that a bounded wait
cannot fit a 60s function. **The face agrees with you and against the wait**, in its own words:
- line 36: *"no real-calendar wait"*
- line 127: *"The schedule stays ENABLED; its first REAL fire is OBSERVED, NOT WAITED FOR: the battery drives the
  trigger's handler directly with a controlled clock and reads the same artifacts the scheduled fire would produce."*

**RULING: the dispatch SENDS AND RETURNS, exactly like the pattern the face names. Build no in-function wait and do
not raise the timeout.** Completion is OBSERVED by reading the artifacts, which is what line 127 already requires.
⛔ And do not let "observed" become "polled on a real clock" -- the controlled clock is the instrument.

### H5. ⭐ W2-S45 IS THE CELL'S REAL WORK, IT IS IN LANE, AND IT IS WHAT YOU DO NOW.
You called it that yourself and you are right. `refresh.py` calls the manifest *"the ONLY memory this cell has
between fires"* and contains **0 hits across 1 file** for `put_object|boto3|s3` -- all five hits in the package are
in the SEARCH handler. `last_manifest_as_of` has exactly one caller and it is a TEST, so **the MISSED-trigger
detector is unreachable in production**, `_refresh/` is empty in all three buckets though the function has run, and
the IAM grants a write NO CODE PERFORMS.
**That is a cell whose central claim -- it remembers between fires -- is false today, and it needs no external
dependency to fix.** Build it while H2's grant lets you clear the import. A MISSED-trigger arm that cannot detect a
missed trigger in production is the false green this round has been finding all night, and this one is findable
before it ships.

### H6. W2-S47 ACCEPTED, AND SAY IT ON THE ARM RATHER THAN AROUND IT.
All three production `latest.json` read 404 with only `qa/` present, positive-controlled. So arm (b)'s `r -> r+1` is
a **FIRST MINT**, *"previous revision retained"* is **VACUOUS until a second build**, and the revision is a STRING
(`irpt-dir/<firm>/<date>/1.0`) and not an integer. **Write all three facts onto the arm.** An arm that reads PASS on
a vacuous condition is exactly what `W4-S28` caught in round 1.

### H7. ⛔ THE HOST YOU LEFT RUNNING: DO NOT STOP IT, AND DO NOT START IT AGAIN WITHOUT TELLING ME FIRST.
`i-02448edb624a7a7cf` is `running` because you started it at 06:07Z for the import check. **Stopping EC2 requires
human confirmation and is NOT yours or mine to take** -- you were right to leave it. The mdpf chain's own 15:00Z run
self-stops it, so it is bounded rather than indefinite, and I am surfacing it to Andrew rather than acting. **Record
the start, the reason and the self-stop in your report.** Any further start is a line to me BEFORE you take it, not
after -- a started host is a cost nobody else can see.
