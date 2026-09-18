# TO IRPT_BCKEND.TO-IB-rtc-3 -- THE REFRESH BUILDS, EXERCISED FOR INFLECTION AND COTTONWOOD: the deployed dispatch fires the re-minted runner on the host for the two firms whose grants are in place, a directory artifact LANDS in each firm's own bucket with its hash recorded, the run record and the next fire's reconciliation read it back -- and the 49 Financial build reads BLOCKED on a named control, never on a missing grant

<to_id>IRPT_BCKEND.TO-IB-rtc-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>staged -- assigned to slot ~2; becomes pending when the COO hands it over after IB-rtc-2 is terminal and merged (the runner's closure must be aboard the bundle before any build).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 3 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (ADMITTED, both L4-R halves SIGNED) | **Round-2 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md` @cfe3a33a9b | **Round-2 slug:** L8/L9 @c1a8cd2543 (`3.0.0_SA_CVO`, msg 97752) | **Decomp cell:** `IB-rtc-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.3, s.R3) | **outcome_ref:** FWD-7 (own), FWD-1

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-3-2` on branch `wk-irpt_bckend-3-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-3-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed). Round-3 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Python:** `py -3.12` (bare `python` may resolve to 3.14 without PyYAML). AWS through `.tools/aws`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call, so read files with the Read/Grep tools and keep a gated read in its own call.

---

## THE CELL

**The PRD row, verbatim (v0.14 @b8e98d5a4d, candidate B4, unchanged since v0.13):** the refresh builds behind the enabled schedule -- one directory artifact per firm per business day in the FIRM's own bucket under `investor-reporting/directory/`, with `latest.json` revisions r -> r+1 and the previous revision retained.

**Where IB-rt-6 stopped (its VALID instance, RT6-AC1 recorded FAIL; rows W2-S49, W2-S51, S50, S53):** the DISPATCH half is built and deployed (the SSM dispatch Lambda, its least-privilege role, the dispatch/reconcile accounting, the zoned schedule ENABLED at `cron(0 9 ? * MON-FRI *)` America/New_York); the BUILD half never landed an artifact because (1) the host could not read 5 of 9 source prefixes and could not write 3 of 3 destinations and (2) the bundle lacked the runner's closure. Since then: MDPF_GLOBAL.TO-IAM1 (52986aca17, 585a9d24c0) granted the inf dimension reads, the 49f xref read and all three destinations (`comp-iam-usage reach-check` read the bd and cot destination writes ALLOWED on 2026-09-17 with a negative control implicitDeny); IB-rtc-2 carries the closure. What is NOT granted, by design: the five `opal-data-49financial/gold/advi/dimensions/` tables, behind that bucket's `DenyForeignFirmPrincipals` (a CONTROL, `infra/aws/terraform/mdpf-pipeline/iam.tf:598-603`), so the 49 Financial directory cannot be built by any `role/mdpf-*` principal.

**What L5 adds (decomposition v0.3 s.R3):**

- Re-measure BEFORE building, from the host by the host (the W2-S49 sweep, re-run read-only): each of the 9 source prefixes and 3 destinations READ-OK/READ-DENY/WRITE-OK, denominators printed, positive control in the same sweep. This is the ground truth the rest of the cell stands on; if inf or cot reads DENY, that arm reads BLOCKED with a row and the cell continues on the other firm.
- Fire the deployed dispatch (IB-rt-6's Lambda, invoked exactly as its schedule would -- the manual invoke path its face and result document; never a hand-run of the runner on the host that bypasses the dispatch) for `inf` and `cot`. Read back through the mechanism IB-rt-6 built: the run record, the command's invocation status, the NEXT reconciliation read (invoke the reconcile path or the Lambda's next-fire logic as the result doc describes), and the landed artifact: `list-objects-v2` under `s3://opal-data-inf/investor-reporting/directory/` and `s3://opal-data-cot/investor-reporting/directory/` BEFORE and AFTER, `latest.json` revision before/after (a FIRST MINT reads absent -> r1, and says so), the artifact's `ETag` and its `sha256` computed from the downloaded bytes (R-40), the previous revision retained where one existed.
- The 49 Financial arm: attempted ONCE through the same dispatch so the refusal is MEASURED on this vintage, expected to read BLOCKED at the source read with `AccessDenied` on the 49f dimensions; recorded as BLOCKED citing W2-S49/S53 and iam.tf:598-603, never worked around (no cross-firm widening, no re-mirroring of the dimensions -- both are NEVERs, s.8 item 3).
- Content sanity on what landed, with the real files as subject (bound 12): row counts per landed artifact, the firm named inside equals the destination bucket's firm, zero name- or e-mail-shaped path components, typed ids at the boundary (bound 13).

---

## DELIVERABLE

`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtc_3.py`, `IB-rtc-3_R33-AC1_battery_output.txt`, `the-refresh-builds-exercised.result.md`, the SSM sweep transcript (read-only), and the proof instance. No code home is written; the dispatch and the runner are exercised AS DEPLOYED.

---

## BOUNDS

- **Read-only on the host** except `/tmp` and what the RUNNER itself writes to its declared destinations; ONE `StartInstances` admitted if the host is stopped; **never** stop it. No IAM, no Terraform apply, no bundle mint (IB-rtc-2's). No cross-firm widening: a 49 Financial read that fails is a MEASUREMENT, not a task.
- The scheduled fire stays the acceptance for FWD-7; this cell's manual invoke is the QA exercise (CLAUDE.md: ad-hoc gold runs are permitted for QA).
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object` for a tracked file, `sha256sum` for a produced object, the service's own digest such as `ETag`/`CodeSha256` for a served one) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W2-S<k>` with k continuing that coordinate's numbering (read the file's highest `W2-S<k>` first; the file holds ONE fenced json array -- append your object inside it at the end, LF line endings, UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp like `2026-09-18T02:00:00Z`, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.

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

<criterion id="R33-AC1" cell_refs="IB-rtc-3"><invocation>timeout 1500 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtc_3.py</invocation><expect>IBR33-TWO-OF-THREE-DIRECTORIES-LANDED</expect></criterion>
**`R33-AC1` -- PASSES BY OUTPUT:** (a) the on-host sweep, `9` sources + `3` destinations each with a verdict and the positive control firing; (b) `inf` and `cot`: dispatch command id, status Success, artifact key, `ETag`, `sha256`, revision before -> after, previous revision retained-or-first-mint, row count -- `2 of 2` landed; (c) `49f`: attempted once, `BLOCKED` at the named read with the control cited -- `1 of 1` measured; (d) the reconciliation read names the same command ids and records `REFRESH_OK` for inf and cot; (e) key census `0 of N` name-shaped, firm-in-artifact equals bucket firm `2 of 2`. The token prints only when (a)-(e) hold with (b) at 2 of 2.

<criterion id="R33-AC2" cell_refs="IB-rtc-3" judgment="true"/>
**`R33-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the landed artifacts' contents are the runner's real output for the business date (which date, which sources, which counts) or a degenerate first mint; what FWD-7's DONE WHEN still lacks after this (the scheduled fire on a business day; the 49 Financial third); and whether the dispatch-to-reconcile loop closed on the mechanism IB-rt-6 built or on your manual reads. No verdict.

<expected_criteria>R33-AC1, R33-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.3, cell `IB-rtc-3` (s.R3.1 the rectangle; s.R3.2 the edges and the fence; s.R3.3 the seating; s.R3.4 the bounds carried; s.R3.5 what it does not decide).
<owned_cells>IB-rtc-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut -- the zoned schedule `cron(0 9 ? * MON-FRI *)` America/New_York is ENABLED (IB-rt-6 RT6-AC2, two instruments) and is NOT changed by this cell; the manual invoke is the QA exercise, the schedule stays the acceptance.
comp-iam: RUN at the cut -- `comp-iam-usage reach-check mdpf-daily-runner-ec2-role` 2026-09-17: s3:PutObject ALLOWED on opal-data-bd and opal-data-cot `investor-reporting/directory/`, implicitDeny on the negative control and on the 49f dimensions read. BLIND SPOT stated: the simulation cannot see a bucket policy; the on-host sweep (arm a) is the applied-plane read.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to its own lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R33-AC1, R33-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtc-3.the-refresh-builds-exercised-for-inflection-and-cottonwood.proof_of_spec.json R33-AC1,R33-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why). You cannot send or receive messages -- anything you would ask is a surprise row.
