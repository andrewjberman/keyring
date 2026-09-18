# TO IRPT_BCKEND.TO-IB-rtc-8 -- THE BUNDLE RE-MINTED WITH THE 49 FINANCIAL SOURCE SET ABOARD: the investor_reporting bundle is re-minted through the guard after IB-rtc-6's runner edit merged, so the host runs the Firm49F that reads through an assumed session when handed a role ARN and behaves exactly as today without one; verified on the served object and on the host -- a Rule 13 DS act, the K5 mint the sign-off packet names

<to_id>IRPT_BCKEND.TO-IB-rtc-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.4.0_DS_ClientPlatform~X, 2026-09-18: R38-AC1 PASS 4 of 4 (token printed, fresh detached checkout at f5005ea933); R38-AC2 recorded for 3.0.0_SA_CVO, not self-graded; the bundle minted at VersionId q8myxeHdNw48w1uDb7YTcBh8DHV9TzU2 / ETag 479af04c under the ledger entry irpt-bckend-rtc8-k5-mint (opened a1f09a51dd, closed 84349a3a19); row IRPT_BCKEND-S70 (INERT). Its merge is one of IB-rtc-7's three cell preconditions.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 (AMENDMENT 1 on R-44/R-45 @57bc083d45; this cell added ~06:4xZ on the packet's step 5) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d | **Rulings:** R-44 / R-45 @57bc083d45 | **Decomp cell:** `IB-rtc-8` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3.6) | **outcome_ref:** FWD-1, FWD-7 (the 49 Financial third)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-3-ds4` on branch `wk-irpt_bckend-3-ds4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-3-ds4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention). Battery `battery_ib_rtc_8.py`.
- **Python:** `py -3.12`. AWS through `.tools/aws`. Capture `safe-commit.sh` and `safe-deploy.sh` output to files, never pipe them to `tail`, never pair with `$( )`. A recursive `grep`/`find` in Bash is DENIED by a rail hook; use the Read/Grep tools.

---

## THE CELL

**The packet's own step (NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md, "How IB-rtc-7 applies it", step 5, verbatim):** "Mint the `investor_reporting` bundle through `.tools/safe-deploy.sh --mint-bundle investor_reporting` so the host runs the K5 runner (a DS-lane act)." And K5: "`directory_runner.py` `Firm49F`: the five dimension reads go through a lazily assumed session ... It is a member of the `investor_reporting` bundle, so it reaches the host through a bundle mint (Rule 13, DS lane). Without the env variable it behaves exactly as today."

**What L5 adds:** the mint is exactly IB-rtc-2's arms (d) and (e), re-run on the tree that now carries IB-rtc-6's runner edit (merged @119fda050a). The runner is a DISTRIBUTION-flagged member of no leg (it is bundle-only); the three `runner_common.py` distribution members are unchanged since IB-rtc-2's mint, so their loose legs must read UNCHANGED (the consistency control from R-45, run read-only: no real commit is made to a distribution member here).

- (a) The closure re-derived at the branch tip: still `8 of 8` declared by repo path (print the diff against IB-rtc-2's list; IB-rtc-6 edited `directory_runner.py` in place and added a test file that is NOT a runtime member -- say so).
- (b) Re-mint: `.tools/safe-deploy.sh --mint-bundle investor_reporting` under a change-management entry (OPEN sentinel committed before the act, closed before the grading reads); `head-object` printing `ETag`, `VersionId`, `source-repo-paths`, and the tarball `sha256` from downloaded bytes (R-40); the NEGATIVE CONTROL against the PRE-CELL object (IB-rtc-2's mint, ETag `0020e7afc760b827a6adb7c0ad538903`) DIFFERS, and the member `directory_runner.py`'s bytes inside the new tarball equal the repo blob at your branch tip (`git hash-object` and sha256 both printed).
- (c) Consistency, read-only: the three distribution members' loose legs `ETag == repo md5` and their bundle bytes `== repo bytes`, `3 of 3`, with NO commit made to them.
- (d) On the host (`i-02448edb624a7a7cf`; ONE `StartInstances` admitted if stopped, never a stop): the read-only SSM extract at repo shape into `/tmp` as IB-rtc-2 did; `IMPORT-OK 3 of 3`; and ONE more line: with `IRPT_SOURCE_READ_ROLE_ARN` UNSET, instantiating `Firm49F` prints the K5 WARN note and uses the host session (the "behaves exactly as today" claim, measured, `0` network events); with it SET to a syntactically valid but NON-EXISTENT role ARN, `Firm49F`'s lazy assumption is NOT attempted at construction (`0` STS calls, your counter) -- the assume happens at first read, which this cell never triggers.

---

## DELIVERABLE

The ledger entry + sentinel commits; the re-minted key's identity; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_8.py`, `IB-rtc-8_R38-AC1_battery_output.txt`, `the-bundle-re-minted-49f-aboard.result.md`; the proof instance.

---

## BOUNDS

- **Rule 13 binds you:** the mint goes through `.tools/safe-deploy.sh`; never a bare `aws s3 cp` to a served key. **NO apply, NO IAM, NO real commit to a distribution member, NO runner execution end-to-end** (IB-rtc-7's).
- Read-only on the host except `/tmp`; never a stop.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-D-S<k>` with k continuing that coordinate's numbering (read the file's highest `D-S<k>` first; the file now holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R38-AC1" cell_refs="IB-rtc-8"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtc_8.py</invocation><expect>IBR38-BUNDLE-REMINTED-49F-ABOARD</expect></criterion>
**`R38-AC1` -- PASSES BY OUTPUT:** (a) `8 of 8` declared, diff printed; (b) the minted identity, `source-repo-paths` `8 of 8`, sha256 recorded, negative control against `0020e7af` DIFFERS, `directory_runner.py` bytes in the tarball `==` the branch-tip blob; (c) distribution legs consistent `3 of 3`, `0` commits made to them; (d) host extract `8 of 8`, `IMPORT-OK 3 of 3`, the UNSET case prints the WARN and `0` network events, the SET case makes `0` STS calls at construction. The token prints only when (a)-(d) hold.

<criterion id="R38-AC2" cell_refs="IB-rtc-8" judgment="true"/>
**`R38-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the bundle the host will run at IB-rtc-7's fire is byte-identical to the tree IB-rtc-7's applies are cut from (name the commit and the hashes), and whether anything in the mint moved a firm's served module. No verdict.

<expected_criteria>R38-AC1, R38-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-8.the-bundle-re-minted-with-the-49-financial-source-set-aboard.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-8` (s.R3.6 AMENDMENT 1, the K5 mint added on the packet's step 5).
<owned_cells>IB-rtc-8</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired; one StartInstances is admitted and is not a schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; the mint runs under the DS lane's existing grant through the guard. BLIND SPOT stated: the guard's S3-membership check is the control, arm (b).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). The mint writes no repo path; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R38-AC1, R38-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-8.the-bundle-re-minted-with-the-49-financial-source-set-aboard.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtc-8.the-bundle-re-minted-with-the-49-financial-source-set-aboard.proof_of_spec.json R38-AC1,R38-AC2` BEFORE the complete flip; rc 0 AND R38-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.
