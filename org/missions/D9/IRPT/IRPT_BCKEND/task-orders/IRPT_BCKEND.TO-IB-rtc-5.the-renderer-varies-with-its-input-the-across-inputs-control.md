# TO IRPT_BCKEND.TO-IB-rtc-5 -- THE RENDERER VARIES WITH ITS INPUT, THE ACROSS-INPUTS CONTROL: two known-different bundles rendered through the real renderer produce outputs that DIFFER on raw and normalized hashes and on content, the same bundle twice produces outputs that AGREE on the normalized hash, and the real-path arm stands HUMAN-GATED on the session exactly as W4-S25 recorded it -- the control W4-S19 said every render arm must carry before FWD-3, FWD-4 or FWD-8 can be narrowed again

<to_id>IRPT_BCKEND.TO-IB-rtc-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T01:45Z to slot ~4 (cold start) at the issuance; a head, no cross-slot wait.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Round-2 slug:** L8/L9 @c1a8cd2543 (`3.0.0_SA_CVO`, msg 97752) | **Decomp cell:** `IB-rtc-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3) | **outcome_ref:** FWD-8, FWD-3, FWD-4

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-3-4` on branch `wk-irpt_bckend-3-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-3-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention; no `<paths>` entry needed). Round-3 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Python:** `py -3.12` (bare `python` may resolve to 3.14 without PyYAML). AWS through `.tools/aws`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call, so read files with the Read/Grep tools and keep a gated read in its own call.

---

## THE CELL

**The ruling this cell executes (IRPT_BCKEND_ROUND2_ANALYSIS.md @cfe3a33a9b, verbatim):** "Round 1's renderer produced ONE document from THREE distinct bundles: three raw sha256, one normalized content hash, an identical 71,944-byte decompressed content stream. IB-s-14's v0.11 arm PASSED because it compared each PDF only to ITSELF. A renderer whose output does not vary with its input cannot evidence that the input was rendered ... FWD-3, FWD-4 and FWD-8 are NOT NARROWED by that arm. Any round-3 cell that re-evidences them carries a control that compares ACROSS inputs, never each artifact to itself -- render two known-different bundles and require the outputs to DIFFER. A test that cannot fail on identical output is not a test of rendering."

**Where the render path stands (rows W4-S25, W4-S19; IB-rt-8's instance under this deliverables home):** the render controller and host dispatch are built (IB-rt-8); the REAL path is SESSION-GATED -- Chromium reached `https://opalinvest.dev/investor-reporting/print` and was answered with a SIGN-IN SCREEN, so `render_export.cjs` refused `SESSION_ABSENT` (W4-S25). The non-interactive session is the test principal RT2 recorded HUMAN-GATED; W4-S25 is re-owned to `2.0.0_SA_COO~B` under R-42 and its card is at Andrew. So the real-path arm of this cell is HUMAN-GATED, verbatim from RT2's record, and the CONTROL runs on the post-authorizer plane against the REAL renderer code.

**What L5 adds (decomposition v0.3 s.R3):**

- The subject is the real renderer: the export root's render controller/renderer as deployed and as in the repo (read IB-rt-8's result and `battery_ib_rt_8.py` here for its entry points, the `RenderPackage` contract in `docs/contracts/investor-reporting/v1/`, and the counterpart's real package if IB-rt-8 pinned one). Two KNOWN-DIFFERENT bundles are constructed from the contract (a real package with one material field changed -- a different client display block, a different holdings table -- so the difference is CONTENT, not metadata), rendered through the same renderer invocation IB-rt-8 exercised on the browser-host pattern (or, if that host is not reachable non-interactively, the renderer's in-process path with the SAME code, the plane named), and the outputs compared: raw `sha256` differ, the normalized content hash (IB-s-14's own normalizer) differs, the decompressed content streams differ at a printed byte offset. Then the IDENTICAL-INPUT control: the same bundle rendered twice -> normalized content hashes EQUAL (raw may differ by timestamps; say which).
- The real-path arm: `render_export.cjs` against the print route WITH a session is HUMAN-GATED; the record is quoted verbatim from RT2's `RT2_test_principal_human_gated.md` and W4-S25, and the arm prints `HUMAN-GATED: <the operator's exact act>`. It is not skipped silently and it is not simulated.
- R-40: every rendered output's `sha256` and normalized hash recorded in the instance beside the bundle's `sha256`; the bundles themselves committed under your deliverables home as fixtures (scrubbed, bound 6).

---

## DELIVERABLE

`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtc_5.py`, the two bundle fixtures and their renders' hashes (the PDFs themselves are NOT committed if over 1 MB; their hashes are), `IB-rtc-5_R35-AC1_battery_output.txt`, `renderer-across-inputs.result.md`, the proof instance. No code home is written.

---

## BOUNDS

- **Read-only against the deployed plane; deploys nothing; no vendor call** (a YCharts render input is a FIXTURE, never a live pull); the browser host is used only as IB-rt-8 used it and is never stopped.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object` for a tracked file, `sha256sum` for a produced object, the service's own digest such as `ETag`/`CodeSha256` for a served one) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W4-S<k>` with k continuing that coordinate's numbering (read the file's highest `W4-S<k>` first; the file holds ONE fenced json array -- append your object inside it at the end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp like `2026-09-18T02:00:00Z`, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R35-AC1" cell_refs="IB-rtc-5"><invocation>timeout 1200 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtc_5.py</invocation><expect>IBR35-RENDER-VARIES-WITH-INPUT</expect></criterion>
**`R35-AC1` -- PASSES BY OUTPUT:** (a) two bundles, `sha256` differ, the differing field named; (b) two renders on the same plane, raw `sha256` DIFFER, normalized hash DIFFER, content streams DIFFER at byte offset `<n>` of `<len>`; (c) identical-input control: normalized hashes EQUAL `1 of 1`; (d) the plane named (browser host or in-process) and the real-path arm printed `HUMAN-GATED: <act>` verbatim; (e) the round-1 defect REPRODUCED first as the positive control for the detector: the three round-1 bundles' renders (or their recorded hashes from W4-S19) shown to collapse to one normalized hash, so the detector is proven to fire on the bad case before it is trusted on the good one. The token prints only when (a)-(e) hold.

<criterion id="R35-AC2" cell_refs="IB-rtc-5" judgment="true"/>
**`R35-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the plane the control ran on is the plane FWD-8's DONE WHEN names, and what the real-path arm still lacks; whether the two bundles differ in a way a client would see (content) rather than in metadata; and whether anything in the renderer's behaviour explains W4-S19 (why three bundles rendered one document) rather than merely no longer exhibiting it. No verdict.

<expected_criteria>R35-AC1, R35-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-5.the-renderer-varies-with-its-input-the-across-inputs-control.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-5` (s.R3.1 the rectangle; s.R3.2 the edges and the fence; s.R3.3 the seating; s.R3.4 the bounds carried; s.R3.5 what it does not decide).
<owned_cells>IB-rtc-5</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; the reads run under the launching seat's credentials (stated, not measured).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R35-AC1, R35-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtc-5.the-renderer-varies-with-its-input-the-across-inputs-control.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtc-5.the-renderer-varies-with-its-input-the-across-inputs-control.proof_of_spec.json R35-AC1,R35-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why). You cannot send or receive messages -- anything you would ask is a surprise row.
