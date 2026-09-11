# TO IRPT_BCKEND.TO-IB-rt-8 -- THE EXPORT WORKER RENDERS: a cloud renderer on the estate's existing browser-host pattern executing the counterpart's versioned RenderPackage, the layer carrying all five contracts, the frozen ExportBundle persisted before render, a stable logical export identity with an explicit attempt id, submit-to-ready-to-download on the served service -- and the four synthetic PDFs inventoried and segregated, never deleted

<to_id>IRPT_BCKEND.TO-IB-rt-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- GO paired at the round-2 issuance (the hand-off is the GO). First and only order of slot ~4.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 5 | **Slug rows this cell closes:** W4-S9, W4-S10, W4-S12, W4-S13, C-S76 | **Decomp cell:** `IB-rt-8` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-8 (contrib, the worker), FWD-3, FWD-4 (the Analysis PDF) | **PRD candidate:** B14

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-2-4` on branch `wk-irpt_bckend-2-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** the only order of slot ~4 this round (the same subagent that built performance, narrative and export). IB-rtb-1 (slot ~1, last) replays the export and download routes after this cell.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B14 asset ingestion, `ExportBundle` freeze, render worker executing the counterpart's `RenderPackage`, `ExportReceipt`, protected download
- **serves:** FWD-8 (contrib), FWD-3 (contrib), FWD-4 (contrib: the Analysis PDF)
- **brief sections consumed:** O6 export paragraph; IV.6 logo/bundle paragraph and execution paragraph
- **contracts (P=produces, C=consumes):** C `RenderPackage`; P `ExportBundle`, `ExportReceipt`
- **paths: reuse:** brand sources `deck_generation/brand/opal_brand_guidelines.pdf`, `brand_spec/brand.json`, `engine/brand.py`, official logo SVG
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (export job + browser runtime); protected artifact storage
- **fixtures / evidence:** `docs/research/investor_reporting_export_20260910/{profile_export_capture.py,build_export_review.py,performance-export-review.pdf,FONT_LICENSE.txt}`; **(v0.11, CRO R2)** the three SYNTHETIC vendor PDFs + receipts from the variants packet as the Analysis-export INPUT specimens (available); STILL MISSING: the native-section / Opal-rendered export certification is B14's own work with the counterpart's `RenderPackage`, never marked complete on generator success, and real-client specimens remain the proof gap
- **acceptance clause draft:** bundle pins scope, report, asset, renderer/template/disclosure and narrative policy versions; retry reuses the bundle, no vendor call during render; branding change = new export revision without recalculation; logos verified for binding, type, dimensions, checksum, safe SVG, resolved before render, no arbitrary URL fetch; download reauthorized even when the artifact exists; the ANALYSIS export renders the counterpart's certified section layout in its own orientation under the same brand, at the same input, configuration and artifact revision as the native preview, and never inherits the performance narrative; actual three-variant PDFs remain a proof gap, not a field to invent

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** THE EXPORT WORKER RENDERS. A cloud renderer executing the counterpart's versioned RenderPackage in a browser runtime (the FNTEND slug's W2-S4: runtime 'browser'), the deployed layer carrying all five contracts, the frozen ExportBundle persisted before render, a stable logical export identity (bundle/version) with an explicit attempt id, submit-to-ready-to-download proven on the served service with stored-object hash equality (W4-S9/S10/S12, C-S76). The four synthetic PDFs under firms/49financial/generations/GENIBS14SYN/: the evidence-surface owner inventories the four keys and segregates them or proves production readers exclude them; deletion is a separately authorized owner act (W4-S13) -- carried to Andrew as the human word it names.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- THE RUNTIME, WITH ZERO EGRESS: a python3.12 Lambda has no browser and fetching one is refused egress (rows W3-S1/S2, W4-S9). The estate ALREADY OPERATES browser hosts: the BD auto-login pattern (`infra/aws/ec2/bd-49f-auto-login/`, `infra/aws/lambda/bd-pipeline/bd-49f-session-trigger` start/SSM/completion/stop controller) and the stopped YCharts host (`infra/aws/ec2/investor-reporting-ycharts/`, IB-s-8) carry Playwright + Chromium. Phase 1 reads both and the render worker becomes a controller Lambda (`irpt-export-render` re-purposed: it freezes the bundle, persists it, and dispatches the render to the export host via SSM; the host runs the counterpart's `RenderPackage` print entry point in Chromium and writes the PDF to the bound firm's `exports/<revision>/attempts/<a>/report.pdf`; the controller validates the PDF, writes the receipt, stops the host) -- the transient-host STYLE the endpoint fixes for YCharts, reused. If no existing host carries a usable browser without egress, that is ONE row and the render arm reads `HUMAN-GATED` naming the operator's act (a one-time image build on Opal infra), never a silent skip.
- THE LAYER: `irpt-common` rebuilt to carry all five IRPT contracts the deployed functions need (`RenderPackage`, `ExportBundle`, `ExportReceipt` added; W4-S10), validated by an import/read INSIDE the runtime (`aws lambda invoke` of a capabilities action reading each schema from `/opt/python/irpt_contracts`), the performance and narrative functions re-pointed to the new version.
- THE COUNTERPART'S REAL RenderPackage: read from the primary checkout's `portal/` (gitlink; print which checkout answered) at the counterpart's HEAD -- its versioned package with `runtime: 'browser'` (the FNTEND slug's W2-S4); the fixture package is RETIRED as evidence; an unsupported package version is REFUSED with the public reason `RENDER_PACKAGE_VERSION`.
- IDENTITY: `export_id` = the logical identity derived from (`bundle_sha256`, `contract_version`) -- stable across a byte-identical retry; `attempt_id` explicit per render; the receipt carries both plus the raw artifact digest; an identical-input retry REUSES the logical export (the receipt found by `export_id`, attempt +1 only if the artifact is absent) and a changed input does not (W4-S12).
- THE FOUR SYNTHETIC PDFs (W4-S13): inventory the four keys under `firms/49financial/generations/GENIBS14SYN/attempts/1/exports/` (`list-objects-v2`, sizes, metadata printed), then EITHER move them under `investor-reporting/qa/synthetic/` in the same bucket (a copy + a delete of the source key is a delete -- NOT taken) OR prove ordinary production readers exclude them: the holdings/directory/export handlers' key filters reject `GENIBS14SYN` and any object carrying `irpt-synthetic=true` metadata (a test per reader, printed). This cell PROVES EXCLUSION and does not move or delete; deletion stays Andrew's word, carried on the instance.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`irpt-export-render` live and reporting renderer absence explicitly, `iam.tf` without a write grant (IB-s-14); `ExportBundle` freeze, receipt, reauthorized download route, asset verification (IB-s-14, 9 of 9 arms on the estate's local Edge path); the shared layer at 2 of 5 contracts (IB-s-13); the counterpart's RenderPackage at its round-1 HEAD and its round-2 recut on the same slug; the BD auto-login and YCharts transient-host patterns.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/export/` (the controller, the host dispatch, `identity.py`, the exclusion filters) + tests; the export host entry under `infra/aws/ec2/investor-reporting-export/` (or the documented reuse of the YCharts host with a second SSM document, state which); `infra/aws/terraform/investor-reporting/export/` with the write grant scoped to the bound firm's exports prefix and the SSM grant on the named host; the layer rebuild (`irpt-common:<n>`, 5 of 5 contracts); the ledger entries + sentinels; the inventory record `deliverables/0.9.0_WK_IRPT_BCKEND~4/RT8_synthetic_pdfs_inventory.md`; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_8.py` and `.result.md`.

---

## BOUNDS

- **No egress off Opal infrastructure** for a browser or any dependency; the estate's existing hosts or a HUMAN-GATED arm.
- **No vendor call during render or preview** (an outbound-network guard on the host's render run, printed with its denominator).
- **Nothing under `GENIBS14SYN` is deleted or moved by this cell**; exclusion is proved, deletion carried.
- **The performance revision is immutable across export revisions**; the receipt's `artifact_hash` names the bytes that exist.

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

<criterion id="RT8-AC1" cell_refs="IB-rt-8"><invocation>timeout 1800 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_8.py</invocation><expect>IBRT8-EXPORT-RENDERS</expect></criterion>
**`RT8-AC1` -- PASSES BY OUTPUT -- a real PDF from the real package on the served service, five contracts in the runtime, stable identity, exclusion proved.**
**(a) SUBMIT TO READY TO DOWNLOAD, ON THE SERVED SERVICE.** Through the deployed controller: a bundle frozen and persisted BEFORE render (`head-object` on the bundle key with its hash), the render dispatched to the host, the PDF landed under the bound firm's exports prefix, the receipt's `artifact_hash` equal to the stored object's (`head-object`), the download route returning an Opal-signed URL after reauthorization; every step's timestamp printed; 0 external connections during the render (host guard log, denominator printed). If the host arm is `HUMAN-GATED`, the record is printed verbatim and this arm reads `HUMAN-GATED`, admitted by this criterion as the arm's own rule.
**(b) THE REAL PACKAGE, VERSIONED.** The counterpart's `RenderPackage` at its HEAD (checkout printed) rendered; an unsupported version refused `RENDER_PACKAGE_VERSION`; the fixture package absent from the render path (census).
**(c) FIVE OF FIVE IN THE RUNTIME.** `aws lambda invoke` capabilities output lists 5 of 5 contracts read from `/opt/python/irpt_contracts` with their `contract_version`; `get-layer-version` prints the version; 3 of 3 functions reference it.
**(d) STABLE IDENTITY.** Identical-input retry: same `export_id`, receipt reused, attempt count printed; changed input: different `export_id`; printed side by side with the raw digests.
**(e) EXCLUSION PROVED.** The inventory of the 4 keys printed (sizes, metadata); per production reader (directory, holdings, export status, download) a test shows objects under `GENIBS14SYN` or with `irpt-synthetic=true` are excluded (`N of N` readers); 0 deletes issued (CloudTrail-free assertion: the 4 keys still `head-object` 200 after the battery).
**(f) LEDGERS AND PLANS.** Every entry CLOSED, sentinels committed; export, performance and narrative roots' post-apply plans `No changes`.

<criterion id="RT8-AC2" cell_refs="IB-rt-8" judgment="true"/>
**`RT8-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which host rendered and what its lifetime, cost and concurrency limits are; which fonts the PDF actually embedded versus the package's requirement; what changed in the PDF between two renders of one bundle and why the content hash is the identity; and what the exclusion proof does not cover (a reader added later). No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT8-AC1, RT8-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-8.the-export-worker-renders.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/export/
infra/aws/ec2/investor-reporting-export/
infra/aws/ec2/investor-reporting-ycharts/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/lambda/layers/irpt-common/
infra/aws/lambda/ci/lambda-layer-map.json
infra/aws/terraform/investor-reporting/performance/
infra/aws/terraform/investor-reporting/narrative/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt8.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-8` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-8</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-export-render` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-export-render` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT8-AC1, RT8-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rt-8.the-export-worker-renders.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rt-8.the-export-worker-renders.proof_of_spec.json RT8-AC1,RT8-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
