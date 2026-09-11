# TO IRPT_BCKEND.TO-IB-s-13 -- THE NARRATIVE PACKET: deterministic events on the verified daily cumulative TWR, dated topic evidence with the future excluded, missing history as an answer, prose that states contemporaneity and never a cause

<to_id>IRPT_BCKEND.TO-IB-s-13</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-13` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-8 (contrib) | **PRD candidate:** B13

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-1-4` on branch `wk-irpt_bckend-1-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** second in slot ~4, after IB-s-11.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B13 event detection + dated news/topic retrieval + prose validation (`NarrativePacket`)
- **serves:** FWD-8 (contrib)
- **brief sections consumed:** O6 narrative paragraph; IV.6 event paragraph, history paragraph, prose paragraph
- **contracts (P=produces, C=consumes):** P `NarrativePacket`
- **paths: reuse:** `infra/aws/lambda/news_layer3_curation/lambda_function.py`, `news_trending_analysis/lambda_function.py`, `keyword_drilldown_generator/lambda_function.py`; DynamoDB `opal-news-trending-daily`, `opal-news-articles`; `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json`
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (narrative adapter -- the new seam named at L5)
- **fixtures / evidence:** export/narrative evidence
- **acceptance clause draft:** events on verified daily cumulative TWR (growth, running peak, drawdown, peak/trough/recovery), overlapping episodes merged, declared materiality policy; same series + same history select the same moments twice; publication/cutoff timezone verified; a window predating the history renders MISSING HISTORY; prose cites selected evidence ids only, states contemporaneity, never causation; news text is data, not instruction; events detected on the verified daily cumulative TWR BEFORE any display downsampling; no MWR, annualized or cash-flow-driven substitution and no zero-filled days; FUTURE information excluded by date; syndicated context deduplicated; a prefilter archive is used as the final historical Topic Cloud only after proof that it is; secondary signals (RSI, regime, Fear & Greed, best/worst) admitted only with historical date and universe evidence, and a current neutral or fallback value is never a historical observation -- each exclusion with a failure fixture, because a deterministic replay reproduces the same wrong story twice if the input policy admits a future article

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **The new seam the endpoint said L5 names is THIS project's:** `infra/aws/lambda/investor-reporting/narrative/` (Lambda `irpt-narrative`) reads the news producers' outputs -- DynamoDB `opal-news-trending-daily` and `opal-news-articles` (both PRESENT at the cut), `s3://opal-data-news-v2/trending_reports/YYYY/MM/DD/trending_report_HHMMSS.json` -- READ-ONLY, and changes nothing in `news_layer3_curation`, `news_trending_analysis` or `keyword_drilldown_generator`; ownership of the producers stays where it is.
- Events on the verified daily cumulative TWR from `PerformanceReport` (IB-s-11) BEFORE any display downsampling: growth `1 + cumulativeReturn`, running peak, drawdown `growth / peak - 1`, peak/trough/recovery dates; overlapping episodes merged; a DECLARED materiality policy (`event_policy.json`, versioned); no MWR, annualized or cash-flow substitution; no zero-filled days.
- Evidence: dated Trending Topic / Topic Cloud terms for each event window with the publication/cutoff timezone VERIFIED from the producer's own bytes (a writer's local path date is not proof of ET); FUTURE information excluded by date; syndicated context deduplicated; the prefilter archive used as the final historical Topic Cloud only after proof that it is; secondary signals (RSI, regime, Fear & Greed, best/worst) admitted only with historical date and universe evidence, and a current neutral/fallback value never becomes a historical observation. Coverage printed: a window predating the history renders MISSING HISTORY, never an empty list.
- **THE SHARED LAYER `irpt-common` (row `IRPT_BCKEND-W4-S3`, an issuer amendment before this order was handed).** The deployed `irpt-performance-adapter` cannot carry two of its runtime dependencies: `jsonschema` (not in the python3.12 runtime; no layer in `infra/aws/lambda/ci/lambda-layer-map.json` provides it) and the bounded Black Diamond helpers it reuses from `opal-assets-bd49f-reporting-pull` (a source copy would be two definitions of one vendor request body). This order builds ONE shared layer at `infra/aws/lambda/layers/irpt-common/` -- `jsonschema` (pinned) plus a `bd_helpers` module ASSEMBLED AT BUILD TIME from the reporting-pull Lambda's source at a pinned commit (the estate's `build_package.py` shape: `git show <pin>:<path>`, never a hand copy), the pin recorded in the layer's `BUILD_MANIFEST.json` -- registers it in `lambda-layer-map.json`, declares it in the `performance` root (same slot as IB-s-11: no second worktree touches that state) and re-applies that root to attach it to `irpt-performance-adapter` under its own ledger entry (`irpt-bckend-s13-layer`), and attaches it to `irpt-narrative` in the narrative root. The deployed performance function then validates contracts (`contract_validated=true`) and no BD cell degrades to UNCERTIFIED for want of a helper.
- Prose: a constrained step that cites selected evidence ids only, validated for dates, quantities and citations; states contemporaneity; a validator REJECTS causal phrasing; news text is data, never instruction. `NarrativePacket` schema-valid with generation/model/prompt versions where a model is used (the prompt and model are pinned in the packet; no call is made to any external model API in this cell -- the prose step runs a deterministic template in this round unless an Opal-owned model route exists, and says which).

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/narrative/` (`events.py`, `evidence.py`, `prose.py`, `event_policy.json`) + `tests/` + `fixtures/`; `infra/aws/terraform/investor-reporting/narrative/` (`lambda.tf`, `iam.tf` read-only on the two tables and the bucket prefix, `main.tf` completed); the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_s_13.py` and `.result.md`.

---

## BOUNDS

- **Not a BI surface.** A bounded read of dated signals for the selected account's own periods; no free query capability.
- **No external model API call.** If a prose model is used it is an Opal-owned route; otherwise a deterministic template, stated.
- **The news producers are read, never written; their ownership is unchanged.**

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S13-AC1" cell_refs="IB-s-13"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_s_13.py</invocation><expect>IBS13-NARRATIVE-DETERMINISTIC</expect></criterion>
**`S13-AC1` -- PASSES BY OUTPUT -- determinism, exclusion of the future, missing history, contemporaneity.**
**(a) DETERMINISTIC.** One known drawdown window replayed twice against the same dated history selects the SAME moments (diff empty, printed); events computed on the pre-downsample series (assert the input length equals the daily series length).
**(b) THE FUTURE IS EXCLUDED -- THE DIFFERENCE CONTROL.** A fixture history carrying an article dated after the window: excluded (0 future ids in the packet); a deliberately broken policy that admits it FAILS the arm. Both printed.
**(c) MISSING HISTORY IS AN ANSWER.** A window predating the history renders `MISSING HISTORY` with the coverage bounds, never an empty topic list. Printed.
**(d) THE TIMEZONE IS VERIFIED FROM THE PRODUCER.** Print the cutoff/timezone evidence you read from the producer's own output or code (file and line), and the live read of `opal-news-trending-daily` (item count in a 30-day window, denominator printed) and the S3 prefix (object count) that established the usable coverage.
**(e) SECONDARY SIGNALS GATED; SYNDICATION DEDUPED.** A current neutral value is refused as a historical observation; two syndicated copies collapse to one evidence id. Printed.
**(f) CONTEMPORANEITY, NEVER CAUSE.** The prose validator ACCEPTS a contemporaneous sentence and REJECTS three causal phrasings (fixtures printed); every citation resolves to a selected evidence id (`N of N`).
**(h) THE SHARED LAYER IS BUILT, PINNED AND ATTACHED (issuer amendment, row W4-S3).** The layer zip imports `jsonschema` and `bd_helpers` in a clean Python (printed); `BUILD_MANIFEST.json` names the reporting-pull pin and the helper functions vendored (`N of N` named in IB-s-11's face); `get-function-configuration` on `irpt-performance-adapter` AND `irpt-narrative` prints a `Layers[].Arn` containing `irpt-common` (2 of 2); the performance root's ledger `irpt-bckend-s13-layer` CLOSED (entry hash); an invocation of the deployed performance function with its offline fixture event (no vendor transport) returns `contract_validated: true`.
**(g) SCHEMA-VALID, READ-ONLY, LEDGER CLOSED.** The packet validates; the role's policy carries no write on the news resources (printed from `iam.tf`); `get-function-configuration irpt-narrative` `CodeSha256` equals the built zip's; sentinel committed (hash).

<criterion id="S13-AC2" cell_refs="IB-s-13"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/narrative plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S13-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S13-AC4" cell_refs="IB-s-13"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/performance plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S13-AC4` -- THE PERFORMANCE ROOT IS CONVERGED after the layer is attached (issuer amendment, row W4-S3).**
Run after the layer apply and after its ledger closes.

<criterion id="S13-AC3" cell_refs="IB-s-13" judgment="true"/>
**`S13-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: how much usable history you measured (first and last dated topic, gaps) versus the 'almost a full year' the brief requested; whether the prefilter archive IS the final Topic Cloud (what you read to decide); and where a reader of the page would still read causation despite the wording. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S13-AC1, S13-AC2, S13-AC4, S13-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-13.narrative-events-dated-evidence-contemporaneity.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/narrative/
infra/aws/terraform/investor-reporting/narrative/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
infra/aws/lambda/layers/irpt-common/
infra/aws/lambda/ci/lambda-layer-map.json
infra/aws/lambda/investor-reporting/performance/
infra/aws/terraform/investor-reporting/performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s13.json
org/critical_paths/.open_deploys/irpt-bckend-s13-layer.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-13` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-13</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-narrative` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S13-AC1, S13-AC2, S13-AC3; S13-AC4 added by issuer amendment before hand-off. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-s-13.narrative-events-dated-evidence-contemporaneity.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-s-13.narrative-events-dated-evidence-contemporaneity.proof_of_spec.json S13-AC1,S13-AC2,S13-AC4,S13-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
