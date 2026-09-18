# TO IRPT_BCKEND.TO-IB-rtc-4 -- INSTRUMENT HYGIENE, FOUR ROUND-2 RULINGS EXECUTED: W4-S28's disarm act performed as a BYTES comparison (served CodeSha256 against the zip built from the fix's source); S32's two stale round-1 batteries RETIRED rather than satisfied; W4-S23's bar re-cut to ZERO VENDOR connections with the vendor list enumerated; and rt2_verify_deployed.py made to fetch the layer it needs so a fresh worktree reads 7 of 7 (W1-S17)

<to_id>IRPT_BCKEND.TO-IB-rtc-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T01:45Z to slot ~3 (cold start) at the issuance; a head, no cross-slot wait.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Round-2 slug:** L8/L9 @c1a8cd2543 (`3.0.0_SA_CVO`, msg 97752) | **Decomp cell:** `IB-rtc-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3) | **outcome_ref:** FWD-4, FWD-3, FWD-8 (instrument repairs on their evidence), FWD-2 (W4-S23)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-3-3` on branch `wk-irpt_bckend-3-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-3-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed). Round-3 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Python:** `py -3.12` (bare `python` may resolve to 3.14 without PyYAML). AWS through `.tools/aws`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call, so read files with the Read/Grep tools and keep a gated read in its own call.

---

## THE CELL

**The rulings this cell executes (IRPT_BCKEND_ROUND2_ANALYSIS.md @cfe3a33a9b, verbatim):**
- W4-S28: "the row's own disarm act is a served-CodeSha256-against-built-zip read, and nobody has performed it. A TIMESTAMP ORDERING IS NOT A BYTES COMPARISON. It stays ARMED on a measurement, not on an assumption, and R-40's bar is exactly what that row has been missing all along." The fix is in source at `56a6e07e8f` (2026-09-12T00:03:03Z); the deployed `irpt-ycharts-generate` was last modified 2026-09-12T05:21:01Z.
- S32: "both round-1 batteries are now STALE INSTRUMENTS reporting FALSE RED after a correct bundle mint. Any citation of their deploy leg is invalid at HEAD. What must NOT happen is re-minting per-file keys to satisfy a stale battery -- that is repairing the world to match a broken instrument."
- W4-S23: "'0 external connections' is unachievable against the portal as built (12 requests, 2 foreign, both Google Fonts, 0 vendor with the vendor list enumerated). Re-cut to '0 VENDOR connections', which is the number the bar exists to protect."
- W1-S17 (rows W1-S17 and S54, this seat's disarm carried the remedy here): `rt2_verify_deployed.py` prints `NOT VERIFIED` for the four layer-attached functions when its gitignored `.scratch/layer/` cache is absent, while the three-way sha256 chain reads EQUAL on 7 of 7 in the same run; the candidate remedy is that the verifier DOWNLOADS the layer zip when the cache is absent.

**What L5 adds (decomposition v0.3 s.R3):**

- (a) **W4-S28, the bytes comparison.** Build the `irpt-ycharts-generate` deployment zip from the fix's source exactly as its Terraform root builds it (read the root under `infra/aws/terraform/investor-reporting/ycharts/` for the build path and hash method -- `CodeSha256` is base64(sha256(zip bytes)) and a zip's bytes depend on the archive's file order and timestamps, so build with the ROOT'S OWN mechanism, never an ad-hoc `zip`), compute its `CodeSha256`, read the served function's `CodeSha256` (`.tools/aws lambda get-function-configuration`), and print EQUAL or DIFFER with both values. NEGATIVE CONTROL: a sibling function's served `CodeSha256` printed beside it and shown to DIFFER. If the root's build is not reproducible byte-for-byte from a worktree (a plausible finding), the arm prints that as the measurement with the two hashes and the reason, and the row stays ARMED with a named next act -- never a PASS by timestamp.
- (b) **S32, retire.** The two round-1 batteries whose deploy leg reports false red (named in row S32; read it) each gain a header line in their `.result.md` reading `SUPERSEDED AT <pin> BY <row S32>: the deploy leg reads FALSE RED after the correct bundle mint; not an instrument at HEAD` -- and NOTHING is minted, moved or re-keyed to make them green.
- (c) **W4-S23, the re-cut bar** applied to the battery that carries it (IB-rt-8's export arm, `deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_8.py`, or wherever the census lives -- read S23 and RT8's result to find it): the arm's bar becomes `0 VENDOR connections` over an ENUMERATED vendor host list (printed, with its count), the foreign-but-not-vendor hosts (the two Google Fonts) printed as a separate line, and the re-run prints `VENDOR 0 of N requests` with N the request denominator. The bar's TEXT change is recorded verbatim in your result.
- (d) **W1-S17, the layer fetch.** `deliverables/0.9.0_WK_IRPT_BCKEND~2/rt2_verify_deployed.py` gains ONE behaviour: when `.scratch/layer/` lacks the `irpt-common` layer zip it needs, it downloads the published layer version's zip (`.tools/aws lambda get-layer-version` -> the `Content.Location` URL) into that cache and proceeds; then IB-rt-2's terminal battery is re-run FROM YOUR FRESH WORKTREE and prints `7 of 7` on arm (e). Nothing else in the verifier or the battery changes; the sha256 chain must still read EQUAL 7 of 7.

---

## DELIVERABLE

`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rtc_4.py` (one battery, four arms, each printing its denominator), `IB-rtc-4_R34-AC1_battery_output.txt`, `instrument-hygiene.result.md`; the two SUPERSEDED header lines; the W4-S23 bar edit; the verifier edit; the proof instance.

---

## BOUNDS

- **Deploys nothing; mints nothing; applies nothing.** The zip is built LOCALLY for comparison only. Read-only against the deployed plane.
- **Never re-mint keys to satisfy a stale battery** (S32's own NEVER).
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object` for a tracked file, `sha256sum` for a produced object, the service's own digest such as `ETag`/`CodeSha256` for a served one) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W3-S<k>` with k continuing that coordinate's numbering (read the file's highest `W3-S<k>` first; the file holds ONE fenced json array -- append your object inside it at the end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp like `2026-09-18T02:00:00Z`, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R34-AC1" cell_refs="IB-rtc-4"><invocation>timeout 1200 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rtc_4.py</invocation><expect>IBR34-FOUR-ARMS-MEASURED</expect></criterion>
**`R34-AC1` -- PASSES BY OUTPUT -- four arms, each a measurement with its denominator:** (a) `served CodeSha256 <x> vs built <y> -> EQUAL|DIFFER|NOT-REPRODUCIBLE(reason)` with the sibling control printed and DIFFERING; (b) `2 of 2` result docs carry the SUPERSEDED header and `0` keys minted or moved; (c) the vendor list `N` enumerated, `VENDOR 0 of M requests`, foreign-non-vendor hosts listed; (d) rt-2's battery from the fresh worktree prints `7 of 7` on arm (e) and the sha256 chain `EQUAL 7 of 7`. The token prints when all four arms have PRINTED THEIR MEASUREMENT -- arm (a) may read DIFFER or NOT-REPRODUCIBLE and the token still prints, because the criterion is that the comparison was PERFORMED as bytes; the reading itself is R34-AC2's.

<criterion id="R34-AC2" cell_refs="IB-rtc-4" judgment="true"/>
**`R34-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether arm (a)'s reading DISARMS W4-S28 (EQUAL -> the fix is aboard; DIFFER -> it is not, and what is served instead; NOT-REPRODUCIBLE -> what read would settle it); whether the S32 retirement leaves any round-1 claim citing those batteries' deploy leg uncorrected; and whether the W4-S23 vendor list is complete against the estate's vendor set (YCharts, Black Diamond, Orion, Eclipse, SmartX, Bloomberg, Schwab, Microsoft Graph). No verdict.

<expected_criteria>R34-AC1, R34-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-4.instrument-hygiene-served-bytes-stale-batteries-vendor-bar-layer-cache.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/rt2_verify_deployed.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.result.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_8.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_8.result.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-4` (s.R3.1 the rectangle; s.R3.2 the edges and the fence; s.R3.3 the seating; s.R3.4 the bounds carried; s.R3.5 what it does not decide).
<owned_cells>IB-rtc-4</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted or applied; the reads run under the launching seat's credentials (stated, not measured).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R34-AC1, R34-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rtc-4.instrument-hygiene-served-bytes-stale-batteries-vendor-bar-layer-cache.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rtc-4.instrument-hygiene-served-bytes-stale-batteries-vendor-bar-layer-cache.proof_of_spec.json R34-AC1,R34-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why). You cannot send or receive messages -- anything you would ask is a surprise row.
