# TO IRPT_BCKEND.TO-IB-rtd-3 -- THE HOLDINGS CONTRACT ABOARD THE BUNDLE AND S71's RE-ARM TRIGGER NAMED: `holdings_snapshot.py` reads `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, which is not a bundle member, so any holdings fire from the bundle dies at `load_contract()`; the member is declared into the closure (R-45), the bundle re-minted, `load_contract()` proven on the host, the two HoldingsSnapshot schemas' difference recorded, and the transition that would ARM S71 (the `irpt-holdings-snapshot` schedule flipping ENABLED) is guarded by a test that reads the live schedule state against the bundle's members

<to_id>IRPT_BCKEND.TO-IB-rtd-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T12:0xZ to the DS lane (its fifth order, first of round 4) on the CTO's round-3 analysis s.7/s.9 item 5: S71 is INERT only because a schedule is DISABLED and nothing watches that transition.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 4 (the CTO's round-3 analysis @5c59f68d70, msg 97944) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 3) | **Round-3 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md` @5c59f68d70 | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar (analysis s.4, ADOPTED) | **Decomp cell:** `IB-rtd-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.4, s.R4) | **outcome_ref:** FWD-5, FWD-7

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Worktree:** `/c/tmp/wk-irpt-4-ds6` on branch `wk-irpt_bckend-4-ds6`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-4-ds6/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention). Battery `battery_ib_rtd_3.py`.
- **Python:** `py -3.12`. AWS through `.tools/aws`. Capture `safe-commit.sh` and `safe-deploy.sh` output to files, never pipe them to `tail`, never pair with `$( )`. A recursive `grep`/`find` in Bash is DENIED by a rail hook; use the Read/Grep tools.

---

## THE CELL

**The finding (row S71, `0.4.0_DS_ClientPlatform~X`, 08:05Z; analysis s.7):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:109-110 @de4e176cc3` sets `CONTRACT_PATH = _REPO/docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` (blob `9ec70af2`, 34577 bytes) -- NOT the `_contracts/` copy (blob `95e4d500`, 26022 bytes; 391 vs 295 keys walked). The bundle's 9 members carry only `DirectoryEntry.schema.json`; a no-network probe shows the v1 schema is the ONLY file `holdings_snapshot.py` opens that the bundle lacks. The `irpt-holdings-snapshot` schedule is DISABLED, so no fire reaches it today -- **and it ARMS the moment anyone enables it.**

- (a) THE MEMBER: declare `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` into the `investor_reporting` closure by repo path (R-45: a member-level DISTRIBUTION flag; the contract is bundle-only, no loose leg -- say so), so `load_contract()` resolves at repo shape on the host. Do NOT change which file the runner reads and do NOT edit either schema; the DIFFERENCE between the two HoldingsSnapshot schemas is RECORDED (a keyword/`required`/`properties` diff, printed with its denominator) for the CVO and the CTO -- which one is the contract is L4's call, not this cell's.
- (b) RE-MINT through the guard under a change-management entry (as IB-rtc-8/9): `head-object` identity, closure `10 of 10` (or the count, with the diff against IB-rtc-9's 9), the negative control against IB-rtc-9's `0XLkiPt4wljdniLnF2fkPKN4qAIkjUbc` / ETag `4c942a76f990874838e33e37f24ed69a` DIFFERS, the new member's bytes in the tarball `==` the repo blob `9ec70af2...`, the three distribution legs `3 of 3` unchanged.
- (c) ON THE HOST (read-only, `/tmp`): extract at repo shape; `IMPORT-OK` all `.py` members; `holdings_snapshot.load_contract()` RETURNS the schema (`1 of 1`), and the POSITIVE CONTROL OF THE DEFECT: the pre-cell tarball's `load_contract()` raises `FileNotFoundError` naming the v1 path (`1 of 1`), same interpreter, same command. No holdings run, no source read.
- (d) THE RE-ARM TRIGGER, NAMED AND GUARDED (not a monitor -- a test in `data/assets/scripts/gold/investor_reporting/tests/`, run by the battery and by the suite): reads the live `irpt-holdings-snapshot` schedule state (`.tools/aws scheduler get-schedule`) and the SERVED bundle's member list (`head-object` `source-repo-paths`), and FAILS if the schedule is ENABLED while the bundle lacks every file `holdings_snapshot.py` opens (the probe list from S71, re-derived by the test with a no-network import). Print its verdict today (`DISABLED` + members present -> PASS) and the MUTANT (a member removed from the list -> the test FAILS when the schedule is ENABLED -- simulate the ENABLED read with a stub of the schedule reader only, the member list real).

---

## DELIVERABLE

the closure declaration; the ledger entry; the two-schema diff record; the trigger test; `battery_ib_rtd_3.py`, `IB-rtd-3_R43-AC1_battery_output.txt`, `the-holdings-contract-aboard.result.md`; the proof instance.

---

## BOUNDS

- **Rule 13 binds you:** the mint through `.tools/safe-deploy.sh`; never a bare `aws s3 cp`. NO apply, NO IAM, NO schedule change (the schedule stays DISABLED; enabling it is nobody's act this round), NO schema edit, NO holdings run.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
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

<criterion id="R43-AC1" cell_refs="IB-rtd-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rtd_3.py</invocation><expect>IBR43-HOLDINGS-CONTRACT-ABOARD-AND-TRIGGER-GUARDED</expect></criterion>
**`R43-AC1` -- PASSES BY OUTPUT:** (a) the member declared, the diff of the two schemas printed with denominator; (b) minted identity, closure count with diff, negative control DIFFERS, member bytes `==` blob, legs `3 of 3`; (c) host `load_contract()` `1 of 1` and the pre-cell `FileNotFoundError` `1 of 1`; (d) the trigger test PASS today and its mutant FAILING under a simulated ENABLED read. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R43-AC2" cell_refs="IB-rtd-3" judgment="true"/>
**`R43-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which of the two HoldingsSnapshot schemas is the contract the endpoint means (the diff says what differs; the answer is L4's), whether the trigger test is the right guard or the schedule's enable should itself be gated, and what else `holdings_snapshot.py` would need before a first enabled fire. No verdict. Every line citation carries `@<commit-ish>` (S56).

<expected_criteria>R43-AC1, R43-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-3.the-holdings-contract-aboard-the-bundle-and-the-re-arm-trigger-named.md
data/assets/scripts/gold/investor_reporting/
.tools/safe_deploy_core.py
.tools/bundles/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.4, cell `IB-rtd-3` (s.R4 -- the round-4 rectangle, edges, seating and bounds).
<owned_cells>IB-rtd-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut -- `irpt-holdings-snapshot` reads DISABLED (DS read at IB-rtc-9); BLIND SPOT: a description; the cell's trigger test re-reads it live.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted; the mint runs under the DS lane's existing grant through the guard.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R43-AC1, R43-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtd-3.the-holdings-contract-aboard-the-bundle-and-the-re-arm-trigger-named.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance, so no `PENDING-THIS-COMMIT` sentinel is needed); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rtd-3.the-holdings-contract-aboard-the-bundle-and-the-re-arm-trigger-named.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-3.the-holdings-contract-aboard-the-bundle-and-the-re-arm-trigger-named.md` BEFORE the complete flip; rc 0 AND R43-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
