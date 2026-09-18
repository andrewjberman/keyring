# TO IRPT_BCKEND.TO-IB-rtd-6 -- THE DIRECTORY DESTINATION DECLARED AT ITS LGIC ADDRESS AND THE MOVE PACKETED: the three firms' directories land under legacy `s3://opal-data-bd/investor-reporting/directory/` (D14's move owed, analysis s.9 item 2); the LGIC address for each firm's directory comes from `lib/opal_naming.py address()` (a builder REFUSAL is a registry row to add, never a typed path -- Rule 30), the readers and writers of the legacy destination are censused across BOTH projects, the move is planned as a direct port with a same-window rollback (no dual-write, no shadow), and the never-widen packet for the new write grant is written -- it DECLARES and does NOT apply

<to_id>IRPT_BCKEND.TO-IB-rtd-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-18T12:0xZ to slot ~4 (cold start) on the CTO's round-3 analysis s.9 item 2. The move itself is IB-rtd-7, gated on both halves and on IRPT_FNTEND's reader.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 4 (the CTO's round-3 analysis @5c59f68d70, msg 97944) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 3) | **Round-3 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md` @5c59f68d70 | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar (analysis s.4, ADOPTED) | **Decomp cell:** `IB-rtd-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.4, s.R4) | **outcome_ref:** FWD-1, FWD-7, FWD-10 (the firm-bound destination)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-4-4` on branch `wk-irpt_bckend-4-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-4-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` is provisioned by the issuer. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`.

---

## THE CELL

**What the analysis owes (s.9 item 2) and what law binds it:** Rule 30 -- every S3 address is `lib/opal_naming.py address()` output; a builder refusal is a missing registry row under `infra/logic/registry/`, never a hand-typed workaround; tier homes and tenancy per `infra/logic/02_DOCTRINE.md` R1-R21 (firm-attributable gold/platinum/state in the FIRM bucket). NEVER-1: served output moves only under never-widen sign-off (CTO+COO); NEVER: no shadow pipeline, no duplicate output path, no standing parity comparator -- build correctly, port directly, same-window rollback. Today: all three directories at `s3://opal-data-bd/investor-reporting/directory/<date>/directory.json` (+ `_refresh/<date>/manifest.json`), written by the host under `mdpf-daily-runner-ec2-role` (the legacy 49 Financial destination until D14, as the rtc-6 packet states), read by the directory Lambda (`infra/aws/lambda/investor-reporting/directory/handler.py`, `_authz/loaders.py`), the holdings Lambdas, and IRPT_FNTEND's API surface.

- (a) THE ADDRESS, BUILT: for each firm, call `address(source, scope, tier, table, partition)` for the directory (and its `_refresh` manifest) -- print the exact call and its output, or the builder's REFUSAL verbatim and the registry row (`infra/logic/registry/*.json`) it needs, drafted in your result (NOT committed to the registry -- that is the CTO's L4 act under Rule 30; a row, not an edit). State the tier you chose and the doctrine rule that places it (`02_DOCTRINE.md` R<n> @commit). Three firms, `3 of 3` addresses or refusals.
- (b) THE CENSUS of the legacy destination, unscoped over the corpus and then scoped (Rule 24): every reader of `investor-reporting/directory` (`comp-find` over the repo, denominator printed; the Lambda source map's functions; `portal/` and IRPT_FNTEND's tree home) and every writer (the host role, the DS's writer census instrument re-run: `N of M` principals). Split readers by PROJECT: this project's, IRPT_FNTEND's, other.
- (c) THE MOVE, PLANNED (not performed): the direct port -- the runner writes the LGIC address; the readers read it; the legacy prefix is retired (not mirrored) in the same window; rollback = the reader/writer config reverted in one apply and the legacy objects still present (they are not deleted by this project). Name every artifact the port touches (runner destination constant, `FirmDestinationPolicy`, the Lambda env/config, `.tools/ds-precommit-check.py`'s `_CROSS_FIRM_FOREIGN_*` enumerations if a bucket name changes), and the IRPT_FNTEND cell the reader change requires (a named hand-off to `2.0.0_SA_COO~F`, not this project's edit).
- (d) THE PACKET for the write grant (K-keys, as rtc-6's): the host role (or the assumed principal) gains `PutObject` on each firm's directory address in its FIRM bucket; the fence (`DenyForeignFirmPrincipals`, per-bucket Deny) re-read for the new keys; plans printed for every root touched; writers census before; negative control designed (the host cannot write another firm's directory address; the 49f principal cannot write at all). For `1.0.0_SA_CTO` + `2.0.0_SA_COO~B`. NOTHING APPLIED.

---

## DELIVERABLE

`battery_ib_rtd_6.py`, `IB-rtd-6_R46-AC1_battery_output.txt`, `the-directory-destination-declared.result.md` (the addresses or refusals, the registry-row draft, the census tables, the port plan), `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtd-6.md`; the proof instance.

---

## BOUNDS

- READ-ONLY on every live plane and on the registry: no apply, no registry commit, no runner edit, no policy edit, no object written or copied; `terraform plan` only. A registry row you need is DRAFTED in the result and is a row in the channel, never committed by you.
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

<criterion id="R46-AC1" cell_refs="IB-rtd-6"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtd_6.py</invocation><expect>IBR46-DESTINATION-DECLARED-AT-LGIC-ADDRESS-AND-PACKETED</expect></criterion>
**`R46-AC1` -- PASSES BY OUTPUT:** (a) `3 of 3` firms with a built address or the builder's refusal + drafted row, the tier's doctrine rule cited with vintage; (b) readers censused unscoped then per project with denominators, writers `N of M`; (c) the port plan naming every touched artifact and the FNTEND hand-off; (d) the packet written with K-keys, plans, fence re-read, writers-before and the negative control design. The token prints only when every arm holds; the battery re-derives every count from the real world each run and never reads its own earlier output.

<criterion id="R46-AC2" cell_refs="IB-rtd-6" judgment="true"/>
**`R46-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the move is this project's own conformance (the directory is a NEW pipeline built to LGIC) or a D14 rider that must wait for the full-name migration (memory: legacy bd/inf/cot buckets are the active channels until D14); which registry rows the builder needs and whether any is an R20 departure; and what the port costs IRPT_FNTEND. No verdict. Every line citation carries `@<commit-ish>` (S56).

<expected_criteria>R46-AC1, R46-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-6.the-directory-destination-declared-at-its-lgic-address-and-the-move-packeted.md
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/mdpf-pipeline/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.4, cell `IB-rtd-6` (s.R4 -- the round-4 rectangle, edges, seating and bounds).
<owned_cells>IB-rtd-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled, changed or fired; this cell declares and plans only.
comp-iam: RUN at the cut by the issuer's read of the rtc-6 packet -- the host role has NO grant on any firm bucket's directory address today (the 49f dimensions read goes through the assumed principal); BLIND SPOT: identity policies only; the packet's census is arm (b)/(d) with the live fence re-read.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `.tools/**`, `data/**` and `lib/**` path resolves to its own lane at HEAD and is admitted ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R46-AC1, R46-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtd-6.the-directory-destination-declared-at-its-lgic-address-and-the-move-packeted.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced or served artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance, so no `PENDING-THIS-COMMIT` sentinel is needed); a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtd-6.the-directory-destination-declared-at-its-lgic-address-and-the-move-packeted.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtd-6.the-directory-destination-declared-at-its-lgic-address-and-the-move-packeted.md` BEFORE the complete flip; rc 0 AND R46-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
