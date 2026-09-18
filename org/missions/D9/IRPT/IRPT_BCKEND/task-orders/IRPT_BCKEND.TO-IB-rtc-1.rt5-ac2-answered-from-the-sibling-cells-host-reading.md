# TO IRPT_BCKEND.TO-IB-rtc-1 -- RT5-AC2 ANSWERED FROM THE SIBLING CELL'S HOST READING: the one-paragraph repair the round-2 analysis ordered, carried with its citation and its content hash, so the judgment row states a FACT measured on the host rather than an inference from a precedent

<to_id>IRPT_BCKEND.TO-IB-rtc-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T01:45Z to slot ~1 (cold start) at the issuance; a head, no cross-slot wait.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Round-2 slug:** L8/L9 @c1a8cd2543 (`3.0.0_SA_CVO`, msg 97752) | **Decomp cell:** `IB-rtc-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3) | **outcome_ref:** FWD-1, FWD-5, FWD-7 (the outcomes IB-rt-5 served)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-3-1` on branch `wk-irpt_bckend-3-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-3-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed). Round-3 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Python:** `py -3.12` (bare `python` may resolve to 3.14 without PyYAML). AWS through `.tools/aws`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call, so read files with the Read/Grep tools and keep a gated read in its own call.

---

## THE CELL

**The CTO's ruling this cell executes (IRPT_BCKEND_ROUND2_ANALYSIS.md @cfe3a33a9b, verbatim):** "RT5-AC2's FAIL stands and the repair is ONE PARAGRAPH. The bar asked a direct, non-conditional question -- which host executes the bundle, does its tree carry pandas and the silver registry -- and the record answered 'UNDETERMINED BY ANY READ THIS CELL MADE' while printing its own denominator as 0 hosts identified, 0 runner lines executed, then substituted a precedent and an inference. A judgment criterion is not satisfied by an inference where the question asked for a fact, and the printed zero is the honest tell that nothing was measured. IB-rt-6 already measured that host DIRECTLY in this same project: ModuleNotFoundError for 'ids', with boto3, pandas, jsonschema and trading_calendar all resolving. Carry that with its citation and re-grade. The cell does not need to go back to the host; it needs to stop answering from its own bounds when a sibling cell holds the reading."

**What L5 adds (decomposition v0.3 s.R3):**

- The sibling reading lives in `IB-rt-6`'s record: row `IRPT_BCKEND-W2-S49` (`world_is`: SSM command `fb070815-519e-4699-9a6b-193267476d25` on `i-02448edb624a7a7cf`, caller `mdpf-daily-runner-ec2-role`, python 3.9.25, boto3 1.42.97, pandas 2.3.3, jsonschema 3.2.0, pyarrow 21.0.0, numpy 2.0.2) and row `IRPT_BCKEND-W2-S44` (the on-host `ModuleNotFoundError: No module named 'ids'`), plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_6.result.md` and the `IB-rt-6` proof instance in that same home. READ them; quote the deciding lines verbatim; do not paraphrase a measurement.
- The repair is an APPEND to IB-rt-5's proof instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json`: the RT5-AC2 judgment row gains the sibling's host reading as `output_evidence`, with its citation (row ids, the SSM command id, the result file and its `git hash-object` at HEAD -- R-40) and a `status_reason` that names `3.0.0_SA_CVO` as the grader. The row's verdict field is NOT set by you: a judgment criterion is graded at L9. Nothing else in that instance changes; the instance must still validate with its governing order bound.
- The "silver registry" half of the question is answered the same way: what IB-rt-6's on-host reads say about `trading_calendar` and the runner's silver reads (W2-S49 lists which silver prefixes the host could read), quoted with denominators; where the sibling's record does not answer a sub-question, the row SAYS SO with the words "not measured by any sibling cell" and names which read would answer it -- never an inference.

---

## DELIVERABLE

The appended RT5-AC2 row in IB-rt-5's proof instance (a modification of a DS-lane deliverable admitted by `<paths>` below); `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IB-rtc-1_R31-AC1_output.txt` printing the appended row and the validator's run; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/rt5-ac2-repaired.result.md`; your own proof instance.

---

## BOUNDS

- **Read-only** against every plane but the two files named in `<paths>` and your own deliverables home; **no host command is dispatched** (the sibling holds the reading; a fresh SSM read is expressly NOT this cell's, per the ruling).
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object` for a tracked file, `sha256sum` for a produced object, the service's own digest such as `ETag`/`CodeSha256` for a served one) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` with k continuing that coordinate's numbering (read the file's highest `W1-S<k>` first; the file holds ONE fenced json array -- append your object inside it at the end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp like `2026-09-18T02:00:00Z`, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R31-AC1" cell_refs="IB-rtc-1"><invocation>py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md</invocation><expect>VALID \(rc=0\)</expect></criterion>
**`R31-AC1` -- PASSES BY OUTPUT -- IB-rt-5's instance still validates with the order bound after the append.**

<criterion id="R31-AC2" cell_refs="IB-rtc-1"><invocation>py -3.12 -c "import json;d=json.load(open('org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json',encoding='utf-8'));r=[x for x in d['acceptance'] if x.get('criterion_id')=='RT5-AC2'][0];e=json.dumps(r);print('SIBLING-CITED' if ('W2-S49' in e and 'fb070815-519e-4699-9a6b-193267476d25' in e and 'ModuleNotFoundError' in e and 'pandas' in e and '3.0.0_SA_CVO' in e) else 'SIBLING-ABSENT')"</invocation><expect>SIBLING-CITED</expect></criterion>
**`R31-AC2` -- PASSES BY OUTPUT -- the RT5-AC2 row carries the sibling's host reading, its SSM command id, the on-host import failure, the pandas reading and the CVO as grader.** (If the instance's acceptance rows use a different key than `criterion_id` for the id, read the schema at `org/standards/PROOF_OF_SPEC.schema.json` and adjust the SELECTOR only, recording the exact command you ran; the five substrings are the bar.)

<criterion id="R31-AC3" cell_refs="IB-rtc-1" judgment="true"/>
**`R31-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which of RT5-AC2's sub-questions (the host; pandas; the silver registry) the sibling's record answers as a FACT and which it does not; and whether anything in IB-rt-5's own record contradicts the sibling's reading. No verdict.

<expected_criteria>R31-AC1, R31-AC2, R31-AC3</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-1.rt5-ac2-answered-from-the-sibling-cells-host-reading.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-1` (s.R3.1 the rectangle; s.R3.2 the edges and the fence; s.R3.3 the seating; s.R3.4 the bounds carried; s.R3.5 what it does not decide).
<owned_cells>IB-rtc-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, rule or trigger is created, changed or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied; no policy, role or trust document is written.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R31-AC1, R31-AC2, R31-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtc-1.rt5-ac2-answered-from-the-sibling-cells-host-reading.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtc-1.rt5-ac2-answered-from-the-sibling-cells-host-reading.proof_of_spec.json R31-AC1,R31-AC2,R31-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why). You cannot send or receive messages -- anything you would ask is a surprise row.
