# TO IRPT_BCKEND.TO-IB-rt-7 -- THE HOLDINGS HANDLER: the declared authenticated route served by a real guarded handler over the revision-bound HoldingsSnapshot with normalized ids, and the attribution holdouts -- actual, assigned and target with missing attribution visible, signed custody totals never redistributed, distinct source clocks carried

<to_id>IRPT_BCKEND.TO-IB-rt-7</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged -- assigned to slot ~1; becomes pending when the COO hands it over after IB-rt-3 (this slot) is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 3(b) + 7 (attribution) | **Slug rows this cell closes:** C-S73 (holdings half), C-S75, W2-S11 (holdings half) | **Decomp cell:** `IB-rt-7` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-5 (contrib, the join/reconcile control), FWD-2 | **PRD candidate:** B12

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-2-1` on branch `wk-irpt_bckend-2-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** second in slot ~1, after IB-rt-3. IB-rtb-1 (this slot, last) replays this route.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B12 partner holdings joins (SmartX/49F, Eclipse/INF, BD Rebalancer/COT), taxonomy, denominators, `HoldingsSnapshot`
- **serves:** FWD-5 (contrib)
- **brief sections consumed:** O5; IV.5 both tables and the four paragraphs after
- **contracts (P=produces, C=consumes):** P `HoldingsSnapshot`
- **paths: reuse:** `runners_49f/b04_account_model_membership.py`; `opal-assets-silver-smartx/smartx_conversion.py`; `INF_E_00.eclipse_model_portfolios.py`; `build_dim_model_portfolio.py`; `build_cottonwood_mdpf_pair.py`; `mdpf_category_registry.py`; D1 / D3 PRDs as prior art
- **paths: new home:** `data/assets/scripts/gold/investor_reporting/` (holdings publisher)
- **fixtures / evidence:** 23 Parquet objects, 15,753,977 bytes (source-list.json, model-overlay evidence, `profile_snapshot.py`)
- **acceptance clause draft:** 49F universe 08335338 only, eight-to-ten-digit zero-pad join, 7,431 joined of 7,453; INF 658 of 663 assignments, 13 multi-account full portfolios not repeated per account; COT `external_id`-to-AccountID join, 946 of 950, custody x recursive weights is TARGET attribution; unique custody population is the denominator; observed / assigned / target bases never spliced; unknown classification is an explicit state, not Client; unique holdings reconcile before and after overlay; COT duplicates deduplicated only under a declared equal-value/null policy with units and dates checked, incompatible duplicates are explicit exceptions; recursive model expansion applies relative/absolute weights EXACTLY ONCE, detects cycles and missing nodes, retains unresolved mass, and never renormalizes only surviving Opal children -- an Opal WRAPPER or an Opal LEAF retains its own proper attribution, with a fixture where a wrapper holds non-Opal children and a leaf sits under a non-Opal wrapper (the old helper's empty-list cycle handling is invalid); SmartX roster, valuation and position rows are different grains -- missing positions are not zero, equity/cash/fees/accruals are reconciled not summed, parallel custody facts never unioned; Opal Supervised/Unsupervised and Advised/Residual are ALTERNATIVE partitions, not four additive children, vendor AccountSupervised is not Opal fee-taking status, and an older insurance-view exclusion removes nothing; Eclipse numeric ids get a declared canonicalization and `targetPercent` units stay uncertified until certified; source-date differences, managed/excluded meaning and assigned-account vs actual-sleeve bases preserved -- each with an adversarial fixture, because a total can reconcile while an allocation is economically wrong

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** WIRE THE THREE DECLARED PRODUCERS: (b) holdings: the handler at HEAD on the declared authenticated route. INTAKE AND ATTRIBUTION CONTROLS: actual/assigned/target and missing-attribution holdouts per firm source with distinct source clocks (C-S75).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/holdings/` (a new handler home; Lambda `irpt-holdings`, its root `infra/aws/terraform/investor-reporting/holdings/` with state key `investor-reporting/holdings/tfstate`): `GET /api/scoped/investor-reporting/holdings/{scope}` served through `guard()` + `FirmBinding`, reading the FIRM's `investor-reporting/holdings/<as_of>/snapshot.json` (the runner's output, ids normalized by IB-rt-3, no `:acct:` prefix), projecting to the resolved scope's permitted accounts, returning a `HoldingsSnapshot` slice that validates; the api root gains the integration for the route that read `NO-HANDLER-AT-HEAD` (applied under a ledger entry; the route table in `docs/contracts/.../v1/routes.json` updated to the handler with its status).
- The attribution holdouts (C-S75), per firm source, as fixtures AND as the runner's behaviour: actual / assigned / target bases each carried on its node with `basis`; an account with NO assignment stays VISIBLE under `unassigned` with its full custody value (never redistributed into sleeves, never dropped); the signed custody total before and after the overlay equal to the cent; two source clocks (custody as-of, overlay as-of) carried DISTINCT on the snapshot and on every node -- a snapshot that collapses them fails. One difference control: a deliberately redistributing build fails the reconcile.
- The three real firms' snapshots re-run in the worktree under QA prefixes after the normalizer, the round-1 numbers reproduced (49F 7,453; INF 790 of 845; COT 946 of 950) with denominators.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

the holdings runner with three real joins reconciled to the cent (IB-s-12); the round-1 attribution risks named in S12-AC2; IB-rt-3's normalizer; the route table with `NO-HANDLER-AT-HEAD` (IB-s-15); `guard()` and `FirmBinding`.

---

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~14:3xZ, before this order is handed; row W4-S15):** `irpt-common` (one S3 key, one terraform-managed layer version) is a shared write surface written by IB-rt-3, IB-rt-8 and IB-rt-4 from disjoint branches, last-writer-wins. FIRST ACT of this order, before any build or apply: rebuild the layer FROM THE TREE AT THIS ORDER'S CUT (the union of every cell's CONTRACTS/MODULES/DATA lists as merged), publish it as a new version, repoint `3 of 3` functions, and print the runtime capabilities read (`5 of 5` contracts, `ids.py`/`raw_keys.json` present). A layer built from any single cell's list is the defect, not the fix.

## DELIVERABLE

`infra/aws/lambda/investor-reporting/holdings/{handler.py,tests/}`; `infra/aws/terraform/investor-reporting/holdings/`; the api root integration for the holdings route; the runner's attribution holdouts + difference control in `holdings_snapshot.py` + tests; the ledger entries + sentinels; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rt_7.py` and `.result.md`.

---

## BOUNDS

- **Model targets never masquerade as observed holdings; a residual is never redistributed** (endpoint constraint; the difference control is the proof).
- **The handler serves; it never builds.** A missing snapshot is `UNAVAILABLE` with the as-of it looked for, never an inline run.
- **The api root's plan shows only the added integration and route target**; any other line is a STOP.

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

<criterion id="RT7-AC1" cell_refs="IB-rt-7"><invocation>timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rt_7.py</invocation><expect>IBRT7-HOLDINGS-SERVED</expect></criterion>
**`RT7-AC1` -- PASSES BY OUTPUT -- the route served and guarded, the holdouts held, the clocks distinct, the reconcile to the cent.**
**(a) SERVED.** `get-routes` shows the holdings route integrated to `irpt-holdings` with `naqxlm`; an in-process authorized request returns a schema-valid `HoldingsSnapshot` slice; six swapped-identifier requests refused with 0 protected bytes (`6 of 6`); `unguarded_routes()` over the real file still `0 of N`.
**(b) BASES NEVER SPLICED, HOLDOUTS VISIBLE.** Per firm: every node carries exactly one basis; unassigned accounts present with full value (count and value printed); the custody total before == after to the cent; a redistributing build FAILS the same check (printed).
**(c) TWO CLOCKS.** `custody_as_of` and `overlay_as_of` present and distinct on the snapshot and on `N of N` nodes; a fixture that collapses them is refused.
**(d) NORMALIZED.** 0 ids matching `:acct:`; ids resolve against the refreshed directory `N of M` per firm with the IB-rt-3 numbers (printed).
**(e) DEPLOYED.** `CodeSha256` equality; the holdings and api roots' post-apply plans `No changes`; ledgers CLOSED, sentinels committed.

<criterion id="RT7-AC2" cell_refs="IB-rt-7" judgment="true"/>
**`RT7-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which attribution can still reconcile to the cent and be economically wrong after these holdouts (the fixture that would catch it, built or not); which firm's overlay clock is furthest from its custody clock and what the snapshot says about it; and what the served slice cannot tell a reader about accounts the scope excludes. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT7-AC1, RT7-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-7.the-holdings-handler-and-the-attribution-holdouts.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/holdings/
infra/aws/terraform/investor-reporting/holdings/
infra/aws/terraform/investor-reporting/api/
docs/contracts/investor-reporting/
data/assets/scripts/gold/investor_reporting/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt7.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-7` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-7</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-holdings` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-holdings` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT7-AC1, RT7-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rt-7.the-holdings-handler-and-the-attribution-holdouts.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rt-7.the-holdings-handler-and-the-attribution-holdouts.proof_of_spec.json RT7-AC1,RT7-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
