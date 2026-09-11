# TO IRPT_BCKEND.TO-IB-s-12 -- THE HOLDINGS SNAPSHOT: three partner joins with printed denominators, observed / assigned / target bases never spliced, unique holdings reconciled before and after the overlay

<to_id>IRPT_BCKEND.TO-IB-s-12</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S12-AC1 PASS-by-output (rc=0, IBS12-HOLDINGS-RECONCILED, 6 of 6 arms); S12-AC2 RECORDED for 3.0.0_SA_CVO at L9, no worker verdict; proof-of-spec-check rc=0; 3 resources applied, ledger closed at 0ab73203c2; 3 real QA snapshots landed; the rule-13 code deploy leg is BLOCKED (row W1-S8 filed, does not gate S12-AC1); row W1-S7 filed.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-12` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-5 (contrib) | **PRD candidate:** B12

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** RE-SEATED: fourth in slot ~1, after IB-s-5 (depends on IB-s-1 for identity and scope keys -- merged at f1aac99b66). IB-s-4 (slot ~2) shares the directory root and is handed only after this cell merges.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B12 partner holdings joins (SmartX/49F, Eclipse/INF, BD Rebalancer/COT), taxonomy, denominators, `HoldingsSnapshot`
- **serves:** FWD-5 (contrib)
- **brief sections consumed:** O5; IV.5 both tables and the four paragraphs after
- **contracts (P=produces, C=consumes):** P `HoldingsSnapshot`
- **paths: reuse:** `runners_49f/b04_account_model_membership.py`; `opal-assets-silver-smartx/smartx_conversion.py`; `INF_E_00.eclipse_model_portfolios.py`; `build_dim_model_portfolio.py`; `build_cottonwood_mdpf_pair.py`; `mdpf_category_registry.py`; D1 / D3 PRDs as prior art
- **paths: new home:** `data/assets/scripts/gold/investor_reporting/` (holdings publisher)
- **fixtures / evidence:** 23 Parquet objects, 15,753,977 bytes (source-list.json, model-overlay evidence, `profile_snapshot.py`)
- **acceptance clause draft:** 49F universe 08335338 only, eight-to-ten-digit zero-pad join, 7,431 joined of 7,453; INF 658 of 663 assignments, 13 multi-account full portfolios not repeated per account; COT `external_id`-to-AccountID join, 946 of 950, custody x recursive weights is TARGET attribution; unique custody population is the denominator; observed / assigned / target bases never spliced; unknown classification is an explicit state, not Client; unique holdings reconcile before and after overlay; COT duplicates deduplicated only under a declared equal-value/null policy with units and dates checked, incompatible duplicates are explicit exceptions; recursive model expansion applies relative/absolute weights EXACTLY ONCE, detects cycles and missing nodes, retains unresolved mass, and never renormalizes only surviving Opal children -- an Opal WRAPPER or an Opal LEAF retains its own proper attribution, with a fixture where a wrapper holds non-Opal children and a leaf sits under a non-Opal wrapper (the old helper's empty-list cycle handling is invalid); SmartX roster, valuation and position rows are different grains -- missing positions are not zero, equity/cash/fees/accruals are reconciled not summed, parallel custody facts never unioned; Opal Supervised/Unsupervised and Advised/Residual are ALTERNATIVE partitions, not four additive children, vendor AccountSupervised is not Opal fee-taking status, and an older insurance-view exclusion removes nothing; Eclipse numeric ids get a declared canonicalization and `targetPercent` units stay uncertified until certified; source-date differences, managed/excluded meaning and assigned-account vs actual-sleeve bases preserved -- each with an adversarial fixture, because a total can reconcile while an allocation is economically wrong

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Destination re-homed (row `IRPT_BCKEND-S1`):** the snapshot lands in the FIRM's bucket under `investor-reporting/holdings/<as_of>/snapshot.json` (+ `latest.json`), QA under `investor-reporting/qa/holdings/`; served only through this project's scoped handler.
- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: per firm, the join the PRD row fixes (49F: Schwab custody universe 08335338 only, SmartX by the eight-to-ten-digit zero-pad grammar, allocation id links the model; INF: Orion positions + Eclipse simple portfolios / model catalogue with declared canonical integer ids, 13 multi-account full portfolios never repeated per account; COT: BD custody + Rebalancer `external_id`-to-AccountID, custody x recursively composed weights is TARGET attribution, the old overlay date visible), the canonical taxonomy from `mdpf_category_registry.py`, the denominators (unique actual custody population per resolved scope), remainders and unknowns explicit, `HoldingsSnapshot` objects schema-valid with the classification partitions (Opal Supervised/Unsupervised and Advised/Residual as ALTERNATIVE partitions; vendor AccountSupervised is not Opal fee-taking; UNKNOWN never Client).
- The adversarial fixtures the v0.4 row names, one test each: COT duplicate policy (equal-value/null with units and dates; incompatible duplicates are exceptions); recursive expansion applies weights EXACTLY ONCE, detects cycles and missing nodes, retains unresolved mass, never renormalizes only surviving Opal children (a wrapper over non-Opal children; a leaf under a non-Opal wrapper); SmartX roster / valuation / position grains not summed, missing positions not zero; the alternative partitions; Eclipse `targetPercent` units UNCERTIFIED until certified; managed/excluded meaning preserved.
- Production schedule in `infra/aws/terraform/investor-reporting/directory/schedule.tf` (same root as IB-s-4, same slot). The rule-13 deploy hazard of row `IRPT_BCKEND-S4` applies here as to IB-s-1.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~00:2xZ, before this order was handed -- a cut defect of the issuer, surfaced on a worker's row):**
- **FIRST-MINT IS EXPLICIT, AND THE EXIT CODE IS NOT THE DELIVERY (row `IRPT_BCKEND-W2-S5`).** `.tools/safe-deploy.sh` on a shared home whose prefix carries 0 members emits `SKIP-NOT-MEMBER` and exits rc=0 with `OK: safe-deploy gate PASS` -- a GATE verdict with NOTHING deployed, and the disclaiming lines sit below the OK where a tail-read misses them. The production code deploy of this cell's runner is that FIRST-MINT: read `.tools/safe-deploy.sh`'s own header for the explicit first-mint mechanism it names and use it (never a bare `aws s3 cp`); then verify the ARTIFACT on the served prefix (`head-object` on the landed key: size and ETag/sha printed beside the built file's), never the guard's exit code. If the guard names a lane this serial cannot satisfy for the first-mint, that is a BLOCKING row on the deploying arm, not an override.

---

## DELIVERABLE

`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` + `tests/` (the adversarial fixtures); the schedule addition; the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_12.py` and `.result.md`; QA snapshots in each firm bucket.

---

## BOUNDS

- **Parallel position/assets tables are never unioned into duplicate custody facts.**
- **No model's global AUM is a client's holding; target constituents are not observed sleeve holdings.**
- **An older MDPF insurance-view exclusion removes nothing from this product.**
- **Reuse the join/status logic of `b04_account_model_membership.py` and `smartx_conversion.py` exactly; do not invent missing advisor attribution.**

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

<criterion id="S12-AC1" cell_refs="IB-s-12"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_12.py</invocation><expect>IBS12-HOLDINGS-RECONCILED</expect></criterion>
**`S12-AC1` -- PASSES BY OUTPUT -- the joins with their denominators, the reconcile, and the adversarial fixtures.**
**(a) THE JOINS, LIVE, WITH DENOMINATORS.** Per firm print joined / total (49F mappings joined of valid keys; INF assignments resolved of total and the multi-account count; COT assignments joined of total and accounts with no map) beside the PRD row's dated figures (7,431 of 7,453; 658 of 663; 946 of 950) as CONTEXT, not as the bar -- the bar is that every count carries its denominator and every gap a reason.
**(b) RECONCILE BEFORE AND AFTER.** Per firm: unique custody total before the overlay == after (printed, to the cent); coverage and join exceptions carry denominators.
**(c) BASES NEVER SPLICED.** Every node carries exactly one of observed / assigned / target and the snapshot refuses a pie that mixes them (fixture printed).
**(d) THE ADVERSARIAL FIXTURES, ONE ARM EACH, N OF N.** COT duplicate policy; exactly-once recursive expansion; cycle; missing node; unresolved mass retained; Opal wrapper over non-Opal children; Opal leaf under non-Opal wrapper; SmartX grains not summed; missing positions not zero; alternative partitions not additive; AccountSupervised not fee-taking; `targetPercent` UNCERTIFIED; managed/excluded preserved. Print passed/total.
**(e) UNKNOWN IS EXPLICIT.** A node with no classification reads UNKNOWN, never Client, never false; printed.
**(f) LANDED.** `head-object` on each firm's QA `latest.json`; the ledger CLOSED and the entry committed (hash); the rule-13 deploy attempted ONCE through the guard's explicit first-mint mechanism -- the ARTIFACT verified by `head-object` (size + ETag/sha beside the built file's), never the exit code; a refusal is printed verbatim, filed as a BLOCKING row, and this arm reads BLOCKED.

<criterion id="S12-AC2" cell_refs="IB-s-12" judgment="true"/>
**`S12-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which attribution can reconcile to the cent and still be economically wrong (name the fixture that would catch it and whether you built it); which source clocks were mixed (SmartX intraday vs prior-day custody) and how the snapshot states it; and what a reader cannot learn from the snapshot alone. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S12-AC1, S12-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-12.holdings-snapshot-three-partner-joins-reconciled.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/investor_reporting/
infra/aws/terraform/investor-reporting/directory/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s12.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-12` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-12</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread. This cell ADDS one schedule (irpt-holdings-snapshot) to the directory root.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-holdings-snapshot` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S12-AC1, S12-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-12.holdings-snapshot-three-partner-joins-reconciled.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-12.holdings-snapshot-three-partner-joins-reconciled.proof_of_spec.json S12-AC1,S12-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
