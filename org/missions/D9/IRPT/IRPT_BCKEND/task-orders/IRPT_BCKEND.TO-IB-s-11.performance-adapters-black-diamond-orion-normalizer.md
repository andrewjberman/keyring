# TO IRPT_BCKEND.TO-IB-s-11 -- THE PERFORMANCE ADAPTERS: Black Diamond for 49F and Cottonwood on separate tenant routing, Orion for Inflection, one normalizer -- units are part of a number's meaning and a normalizer that treats decimal and percentage as one unit fails

<to_id>IRPT_BCKEND.TO-IB-s-11</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-11` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-3 (contrib) | **PRD candidate:** B11

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-1-4` on branch `wk-irpt_bckend-1-4`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** first in slot ~4. Spawned after IB-s-18 is merged. IB-s-13 and IB-s-15 hang off this cell.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B11 performance adapters: Black Diamond (49F, COT separately), Orion (INF); normalizer
- **serves:** FWD-3 (contrib)
- **brief sections consumed:** O2; IV.3
- **contracts (P=produces, C=consumes):** P `PerformanceReport`
- **paths: reuse:** BD `POST /portfolioreporting/api/performance/performancePeriod` + `performanceSeries`; Orion `POST /api/v1/Reporting/Scope`; `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` (bounded helpers); `inf-performance-daily/pull_inflection_performance_dim.py` (prior art only)
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (adapters)
- **fixtures / evidence:** `docs/research/investor_reporting_performance_20260910/probe_performance.py` (offline); BD/Orion teardowns; nine-outcome September 10 evidence
- **acceptance clause draft:** native date/cumulative arrays preserved; one hierarchy chosen, overlapping levels never summed; period `timeWeightedReturns.return` decimal; Orion units per FWD-3 constraint; nodes identified by group path + `$type` + calculation id together; `startValue + valueChange` is NOT a dollar-history shortcut; compact `cumulative=false` shape; missing facts stay absent with reasons

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/performance/` (Lambda `irpt-performance-adapter`): adapters per PRD row B11 and IV.3 -- Black Diamond `POST /portfolioreporting/api/performance/performancePeriod` and `performanceSeries`, 49F and COT on SEPARATE tenant routing; Orion `POST /api/v1/Reporting/Scope` with native household/account scopes and the compact `cumulative=false` daily breakdown; native date/cumulative arrays preserved; ONE hierarchy chosen (`levels` or `combinedLevels`), overlapping levels never summed; BD period `timeWeightedReturns.return` DECIMAL; Orion summary `calculated-performance.performance` DECIMAL and daily `performance` PERCENTAGE, daily `factor` linked as product-minus-one; response nodes identified by group path + `$type` + calculation id TOGETHER (ids repeat); `startValue + valueChange` REFUSED as a dollar-history shortcut; missing or unsupported facts stay ABSENT with reasons; the normalizer to `PerformanceReport` with explicit units, method, fee/accrual, annualization, dates, currency, scope, benchmark and coverage -- and it never changes a provider's methodology to make two numbers look comparable.
- Input: a `ResolvedScope` FIXTURE (this cell does not wait on IB-s-2); the exact selected account set is what is requested -- relationship return is a VENDOR calculation for that set, never a sum or average of account returns.
- Bounded helpers from `opal-assets-bd49f-reporting-pull/lambda_function.py` are reused (name the functions); `pull_inflection_performance_dim.py` is prior art only.
- Proof is OFFLINE: `docs/research/investor_reporting_performance_20260910/probe_performance.py` in its offline mode over the captured evidence (`INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json`: nine HTTP outcomes, two 401s, seven successes); the live calls are the qualified arm.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/performance/` (`bd_adapter.py`, `orion_adapter.py`, `normalize.py`, `handler.py`) + `tests/` + `fixtures/`; `infra/aws/terraform/investor-reporting/performance/` (`lambda.tf`, `iam.tf`, `main.tf` completed); the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_s_11.py` and `.result.md`.

---

## BOUNDS

- **NO LIVE BLACK DIAMOND OR ORION CALL.** The adapters run against the captured evidence through a transport stub; an outbound call to either vendor host fails arm (g).
- **No fabricated aggregate.** Summing or averaging account returns into a relationship return fails arm (d).
- **Proposed TWR/net/YTD defaults are explicit in the report, never source rewrites.**

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

<criterion id="S11-AC1" cell_refs="IB-s-11"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_s_11.py</invocation><expect>IBS11-PERFORMANCE-NORMALIZED</expect></criterion>
**`S11-AC1` -- PASSES BY OUTPUT -- the adapters and the normalizer against the captured evidence, the unit arm as the difference control.**
**(a) THREE TENANTS, THREE ROUTES.** 49F and COT resolve to DIFFERENT BD tenant routes; INF resolves to Orion; printed.
**(b) THE CAPTURED EVIDENCE REPLAYS.** `probe_performance.py` offline over the evidence JSON: the seven successful outcomes parse into `PerformanceReport` objects that validate; the two 401s produce ABSENT-with-reason, never a value. `9 of 9` accounted.
**(c) UNITS ARE MEANING -- THE DIFFERENCE CONTROL.** Orion summary decimal and daily percentage normalize to ONE declared unit with the conversion recorded; a deliberately unit-blind normalizer produces a figure 100x off and FAILS the arm; daily `factor` product-minus-one ties to the cumulative series (printed for the fixture's rows).
**(d) NO FABRICATED AGGREGATE.** A relationship of two accounts: the report carries the vendor's relationship calculation for the exact set; a build that sums the account returns FAILS the arm. Printed.
**(e) HIERARCHY, IDENTITY, SHORTCUT.** One hierarchy chosen and overlapping levels never summed (fixture printed); nodes identified by the triple, with a fixture where the calculation id repeats; `startValue + valueChange` refused (printed).
**(f) ABSENT STAYS ABSENT.** Annualized / MWR / benchmark facts the evidence lacks are absent with reasons in the report (census printed).
**(g) NOTHING LEFT THE MACHINE; THE LEDGER CLOSED.** 0 external connections; `get-function-configuration irpt-performance-adapter` `CodeSha256` equals the built zip's; sentinel committed (hash).

<criterion id="S11-AC2" cell_refs="IB-s-11"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/performance plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S11-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S11-AC3" cell_refs="IB-s-11" judgment="true"/>
**`S11-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which scope/method cases the evidence does NOT establish (49F live-tenant parity, multi-account BD aggregation, Orion subset exclusion, annualization/accrual/currency/benchmark, full history) and which the normalizer therefore marks UNSUPPORTED rather than PARTIAL; and what the first live call would need to show before the report is advertised for a tenant. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S11-AC1, S11-AC2, S11-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-11.performance-adapters-black-diamond-orion-normalizer.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/performance/
infra/aws/terraform/investor-reporting/performance/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s11.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-11` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-11</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-performance-adapter` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S11-AC1, S11-AC2, S11-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-s-11.performance-adapters-black-diamond-orion-normalizer.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-s-11.performance-adapters-black-diamond-orion-normalizer.proof_of_spec.json S11-AC1,S11-AC2,S11-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
