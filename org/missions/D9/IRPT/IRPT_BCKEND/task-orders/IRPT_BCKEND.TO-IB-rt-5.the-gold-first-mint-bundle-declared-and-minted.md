# TO IRPT_BCKEND.TO-IB-rt-5 -- THE GOLD FIRST-MINT: the investor_reporting bundle declared in the deploy guard's one declaration table and the two runners minted to the shared home through the guard's own explicit mechanism, verified by the served artifact -- a Rule 13 DS act, the gate opened by the CTO

<to_id>IRPT_BCKEND.TO-IB-rt-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~X</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 3(c) | **Slug rows this cell closes:** W1-S8, W2-S5 | **Decomp cell:** `IB-rt-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-1, FWD-5, FWD-7 (the producers' dependency) | **PRD candidate:** B1

---

## IDENTITY AND WORKTREE

- **Serial:** `0.4.0_DS_ClientPlatform~X` -- a DS-lane seat of `0.4.0_DS_ClientPlatform`, seated by the issuer for this order (spawn != dispatch; this face is the dispatch). Every Bash call begins `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- **Home:** `org/tier2_senior/0.4.0_DS_ClientPlatform~X/`; a pointer to this face sits in its `task_orders/`. **Worktree:** `/c/tmp/wk-irpt-2-ds` on branch `wk-irpt_bckend-2-ds`, cut by the issuer from `HEAD` of `CLOUD`. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-ds/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`. The issuer merges your branch at the drain.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** the DS lane's only order this round; nothing before it. IB-rt-6 (slot ~2) waits on this cell's merge AND its minted artifacts.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B1 directory ingestion + viewer-scoped projection + search service
- **serves:** FWD-1 (contrib), FWD-7 (own)
- **brief sections consumed:** O1; IV.2 identity table, daily-movement paragraph, business-date paragraph
- **contracts (P=produces, C=consumes):** P `DirectoryEntry`
- **paths: reuse:** `data/assets/scripts/silver/silver_registry.py`, `mirror_schemas.py`, `rebalancer_schemas.py`, `bd49f_dim_conversion.py`; `runners_49f/a01_dim_relationship.py`, `a06_dim_identity_crosswalk.py`, `d08_firm_ownership_map.py`, `bd49f_dim_portfolio_group.py`; `runners_inf/a00_dim_account.py`, `a01_dim_relationship.py`, `runner_common.py`; `runners_cot/a01_dim_relationship.py`; `data/firm_registry.json`; `lib/trading_calendar.py`
- **paths: new home:** `data/assets/scripts/gold/investor_reporting/` (directory runner); publisher output to `<FIRM bucket per FIRM_BUCKET_MAP>/investor-reporting/...`, served ONLY through this project's scoped handlers after `ResolvedScope` (v0.5, L5 finding `IRPT_BCKEND-S1`: `opal-data-portal-v2` is the origin of CloudFront behavior 19 with NO auth Lambda, so a directory or holdings object there is reachable without the edge validator; the firm-scoped AdvisorIntelligence data is the precedent)
- **fixtures / evidence:** split evidence manifest; 49F crosswalk `match_method`/`match_as_of`/`in_0833_universe`; INF 874-of-953 identity fixture
- **acceptance clause draft:** duplicate names, account-only entry, multiple relationships, terminated-but-entitled client resolve to the expected authorized set; provider calls during search = 0; as-of and source completion date carried on every entry

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** The gold first-mint (W1-S8): .tools/safe_deploy_core.py CODE_TREES must carry the two runners' bundle -- a Rule 13 DS act on a shared tool the IRPT grant cannot touch; the CTO opens the gate here: 0.4.0_DS_ClientPlatform (or the DS instance the COO seats) declares the bundle and mints; until then the row stays an unresolved dependency, never a deployed runner.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `.tools/safe_deploy_core.py` `CODE_TREES` (the ONE declaration, INFRA.TOOLS per its own header; the CTO's ruling 3(c) opens the gate for this act) gains a bundle `investor_reporting` under the assets tree: members `directory_runner.py` and `holdings_snapshot.py` (repo paths under `data/assets/scripts/gold/investor_reporting/`, `sha_metadata_key: script-sha256`), bucket `opal-data-mdpf`, `s3_key` under `code/scripts/assets_gold/investor_reporting/` in the shape the `accrual_bridge` bundle uses (read it; copy its shape; change only the members and keys) -- tests excluded from the bundle. The guard's own self-test and `.tools/tests/` pass after the edit (print the run).
- The mint: `.tools/safe-deploy.sh --mint-bundle investor_reporting` (the explicit first-mint mechanism the guard documents), NEVER a bare `aws s3 cp`; then the ARTIFACT verified: `head-object` on each landed key prints size and ETag/`script-sha256` metadata equal to the built file's; the ordinary push path on a later commit to those files then reads MEMBER (not SKIP-NOT-MEMBER) -- proven by a no-op commit's gate output, printed.
- The DS lane's own change-management entry for the mint (`irpt-bckend-rt5-mint`), OPEN sentinel committed before the act, CLOSED and committed before the grading reads.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

the two runners committed at HEAD (`data/assets/scripts/gold/investor_reporting/directory_runner.py`, `holdings_snapshot.py`, IB-s-1/IB-s-12) with 404 on the served prefix; the guard's refusal `ERROR: no bundle named ... declared (declared: ['accrual_bridge'])` (rows W2-S5, W1-S8); the `accrual_bridge` bundle as the shape to copy; the round-1 finding that COMMITTED is not SERVED.

---

## DELIVERABLE

The `CODE_TREES` edit in `.tools/safe_deploy_core.py`; the guard's tests green; the two minted keys under `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/`; the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py` and `.result.md`.

---

## BOUNDS

- **Declare and mint; do not edit the runners.** A defect in a runner is a row for the IRPT lane (IB-rt-3 / IB-rt-6 own them), never a fix here.
- **The guard's other bundles and trees are untouched**; the self-test run is the control.
- **No production run of either runner in this cell**; the mint lands code, the schedule (IB-rt-6) runs it.

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

<criterion id="RT5-AC1" cell_refs="IB-rt-5"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py</invocation><expect>IBRT5-FIRST-MINT-SERVED</expect></criterion>
**`RT5-AC1` -- PASSES BY OUTPUT -- the bundle declared, the guard green, the artifacts served and verified.**
**(a) DECLARED.** `.tools/safe-deploy.sh --mint-bundle nonexistent` prints the declared list and it contains `investor_reporting` (printed); the guard's self-test and `.tools/tests/` pass (counts printed).
**(b) MINTED THROUGH THE GUARD.** The mint invocation's output printed verbatim; `head-object` on each of the 2 keys prints size and the sha metadata equal to `sha256sum` of the repo file (`2 of 2`).
**(c) MEMBER NOW.** A no-op change to a runner committed on the branch runs the push gate and reads MEMBER / deployed or verified, never SKIP-NOT-MEMBER (the gate's own line printed) -- the gate's own run is the authority, not a resolver call.
**(d) LEDGER.** The entry CLOSED; the sentinel's OPEN commit hash and its removal commit hash printed.

<criterion id="RT5-AC2" cell_refs="IB-rt-5" judgment="true"/>
**`RT5-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the bundle's member list is the whole runner (imports it needs at run time on the host) or only the two files; which host will execute them and whether that host's tree already carries their dependencies (pandas, the silver registry); and what the served artifact proves and does not prove about a scheduled run. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT5-AC1, RT5-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
.tools/safe_deploy_core.py
data/assets/scripts/gold/investor_reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt5-mint.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-5` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-5</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE for IAM; the S3 write is the guard's under the DS lane's credentials -- the guard's own gate line at push time is the authority (LD-0549 shape). BLIND SPOT: the resolver function is an estimate, never the ceiling.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT5-AC1, RT5-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json RT5-AC1,RT5-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
