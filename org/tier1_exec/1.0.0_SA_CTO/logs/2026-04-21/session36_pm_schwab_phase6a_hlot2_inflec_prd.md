# 1.0.0_SA_CTO — Session 36 Continuation Log (PM/Evening)

**Date:** 2026-04-21 (Tue, PM through evening)
**Scope:** Schwab TRN_NNA Phase 6a integration + HLOT2/HLOT2b ship + architectural collision (AE silver-enrich vs DS gold-runtime) resolved to Path A + BD silver schema drift RCA + ADVI_INFLEC second-partner PRD v1.0→v1.1→v1.2 + watchdog grace-window fix + various sibling RAVC closes.
**Continuity from:** `session36_five_item_decisions.md` (5-item walkthrough) + `session36_pm_active_filter_decision.md` (earlier PM segment).

---

## 1. Post-/clear startup reconciliation

Session resumed post /clear. Full startup sequence executed:

- MCP register + inbox-watch live
- Project registry + MCP org scan + agent-status drills
- Dashboard drift reconciliation: 6 project rows rewritten (STAUDT, ROLLUP, COMP_LEARNS, TRSB_TFIMPT, ADHC_DSFLOW, ADVI_DESIGN); 2 projects moved Active→Completed (PROFAU, INCMTL); pipeline tag row added (trade-pipeline-v1.3.0). Commit `964a9819`.

---

## 2. Andrew 5-item walkthrough — decisions committed `0a37d545`

One-by-one walkthrough of the 5 open items surfaced in the COO/CTO "What's Open" status. All decided. Full detail: `session36_five_item_decisions.md`.

Summary:
1. **AUA active-filter brief** — KILLED multi-signal proposal; replaced with Cohort A D_04 summary-footnote TO (599 accts / $44.7M headline summary for portal footnote, NO gold-runner filter changes). Brief file deleted.
2. **Chart vs Leaderboard methodology** — per-day tagging-gated canonical for ALL flow attribution (NNA/leaderboard/chart). AUA stays current-snapshot. CHART-METH renamed CHART-ALIGN per Andrew. `STAUDT.KPI 50bps sentinel` KILLED.
3. **TRSB §8 Q2+Q4 + SES** — W2 rescoped to joint 0.5.0_AE + 0.7.0_AE Phase 0 discovery bundling SES packet.
4. **ADHC_DESIGN orphans** — CANCEL 4 orphan TOs, CLOSE at 28/32 effective. COO 3-step atomic closure.
5. **SES production-access** — folded into TRSB §3.

COO execution 3 commits: `1fd28809` (5 TO actions + STAUDT.KPI cancel + TRSB.W2 rescope) + `d04cb534` (ADHC_DESIGN 3-step closure) + `1e9d9dc3` (DSFLOW.002 org-docs with Andrew fold-ins). ACCEPTED via MCP.

---

## 3. Schwab TRN_NNA Phase 6a (`dfaeddc2`) — ship + RAVC4 close

### 3.1 DS 0.4.0 pre-flag #1 + design clarifications

DS 0.4.0 pre-flagged C_01 Phase 6a (Schwab TRN merge inside C_01.canonical_nna.py). Three decisions required before land:

**Q1 imputed-row advisor attribution:** escalated to Andrew. Options (a) BD-most-recent-architect lookup, (b) synthetic 'Onboarding' bucket, (c) firm-only attribution.

Andrew ruled **(c) firm-level only** with note that advisor-level could later come via backfill if BD catches up.

**CTO design refinement post-Andrew:** engagement on V1 (emit-time lookup, no threshold) vs V2 (30d aging gate) vs V3 (dynamic p95). DS's BD onboarding-lag distribution analysis showed bimodal (71% ≤30d + 22% >90d heavy tail, p95=504d). V2 30d gate would permanently drop the 22% heavy tail. Endorsed **V1 emit-time lookup** for Phase 6b (future TO).

**Q2 classifier tune gate:** proceed on current classifier (AE 0.6 Option A ship-as-is, effective accept via Andrew Phase 6 GO).

**Q3 byte-identity AC#5:** stable mergesort by schwab_txn_key, validation bundled into closeout.

**Diff-flag threshold:** $100 floor + 2% ratio endorsed (over 2%-only).

**Phase 6a scope narrowed 6→3 tags:** `bd` / `bd_diff_flagged` / `schwab_imputed` (no `bd_lagged`/`bd_delayed`/`bd_only` — those require event-level fuzzy matching, deferred Phase 6b).

### 3.2 Pre-flag #2 lib/ verification catch

DS initial pre-flag #2 mentioned `lib/schwab_flows.py` as "bundled with runner's S3 layout" without verification. CTO caught the gap, asked for explicit (A) already-on-S3 / (B) ships-in-this-upload / (C) runtime-packaged. DS confirmed (B) — lib/schwab_flows.py is NEW, ships in same upload batch per `lib/nna_flows.py` precedent.

### 3.3 Upload + MATCH

Dual-GO (CTO + COO A→D-rerun-sensitive protocol). DS shipped:
- `code/gold/C_01.canonical_nna.py` ETag `dca241c1be4c97ecd5ee6152c05fec4d` (45.6KB)
- `code/gold/lib/schwab_flows.py` ETag `2ae15d1c7f3629ae30c9ff3112156f71` (10.0KB)

`comp-pipescript deployed C_01` MATCH 2/2. Byte-identical round-trip verified.

### 3.4 RAVC4 close

DS fired RAVC4 evidence MCP. Key validation on fresh C_01 output:

| Date | rows | bd | bd_diff_flagged | schwab_imputed | imputed_inflow |
|------|-----:|---:|----------------:|---------------:|---------------:|
| 2026-04-17 | 5,984 | 5,966 | 18 | 0 | — |
| 2024-12-30 | 4,744 | 4,682 | 0 | 62 | **$18.46M** |
| 2024-12-31 | 4,751 | 4,594 | 1 | 156 | **$22.76M** |

Marquee validations:
- Stoneridge Road $17.4M on 2024-12-30 — schwab_imputed, exact match
- Jessica Lindsey Short Trust $20.10M on 2024-12-31 — schwab_imputed, within $5k

**ACCEPTED** `20260421T184918Z`. CHART-ALIGN + COHORT-A upload paths unblocked.

### 3.5 D_04 regression (`d87377a5`) — retroactively accepted

Post-accept, qa-runner `87227091 --group D` run crashed D_04 at line 1598 `_nna_period_key` with `TypeError: 'float' object is not subscriptable`. Root cause: dfaeddc2 outer-merge introduced NaT-date rows when Schwab aggregation produced zero-gross pairs (TOA/ACAT identity moves pass classifier with gross=0; impute_mask doesn't fire because schwab_present=False; date never backfilled).

DS fixed direct-ship commit `d87377a5`:
1. `lib/schwab_flows.py`: filter `raw[raw['gross_amount'] > 0]` pre-aggregation
2. `C_01._worker_04b`: defensive `dropna(subset=['date'])` post-merge

S3 uploaded 19:55Z. MATCH verified. DS flagged own responsibility + asked for retroactive validation.

**CTO protocol note logged:** my own Phase 6a RAVC4 accept closed on C_01 grain evidence only — explicitly noted D-cascade didn't fire but relied on "code-level review" for downstream schema impact assessment. Code review missed the NaT-date propagation through D_04's `_nna_period_key`. Future Phase 6a-class acceptances on D-consumer-affecting changes need D-grain evidence before close.

**DS protocol note forward-looking:** 60-second ACCEPTANCE FLEX MCP is the right pattern for urgent regression-fix-on-authorized-change (CTO+COO get objection window without blocking critical path). No retroactive formalization required for this case given urgency + Andrew's stale-drift directive.

---

## 4. HLOT2 / HLOT2b — combined close path

### 4.1 Patch A close-partial at 73%

COO surfaced HLOT2 Patch A result from qa-runner `51ce2df1`: $57M recovered vs $78.6M target = 73%. Andrew directive: **accept close-partial, keep momentum, DS investigation sibling TO non-blocking.**

DS ACCEPTANCE evidence:
- 4,046 paired +MV rows reclassified CA_SELL→CA_BUY
- DIVZ total MV $131.88M (pre-gap baseline $74.5M → +$57.4M recovered)
- Residual $21.2M vs $153.1M ceiling

DS root-cause hypothesis for $21M miss (leaning A+C):
- **(A) silver/transactions incomplete** for some CA-Merger paired rows (LEADING — BD export dropped one side of pair)
- **(C) Genuine ceiling** — $78.6M was theoretical-max from HLOT1 sample, not mechanism-matched
- (B) Classifier threshold (MINOR) / (D) Code bug (UNLIKELY)

**CTO scope-decomposition recommendation to COO:** sibling DS TO scoped to characterization ONLY. If (A) dominates, separate AE-scope bronze-silver audit TO (not bundled). Different lanes, different timeframes.

### 4.2 HLOT2b B_01 fix ship (`74dbad2b`)

DS pre-flagged #1+#2 on HLOT2b — B_01 `_build_authoritative_reopen_lots` ticker→cusip fix. Enriches canonical/holdings with cusip via `silver/bd_assets_dim` ticker lookup before required_cols check. Per-row fallback on missing cusip.

All 5 Tier 1 targets (IEFA/SPYM/IDVZ/IEMG/SPHY) have valid 1:1 CUSIP mappings. Smoke: 93.6% rows cusip post-merge, 6.4% skipped. Expected ~$102.7M combined Tier 1 recovery.

Dual-GO, upload, MATCH verified:
- `code/gold/B_01.holdings_lots.py` ETag `8a3dc16ccf4b5fbace02a8b749bb9c6f` (149.6KB)

### 4.3 Combined RAVC4 pending

HLOT2+HLOT2b+Phase 6a+D_04 fix+CHART-ALIGN+COHORT-A combined validation pending next qa-runner `--chain full --force` dispatch. Single-run coverage per DS's plan. AE firing after `--group D` completes (in flight at log-write time).

---

## 5. Architectural collision — AE silver-enrich pivot → Andrew Path A directive

### 5.1 Discovery

AE 0.6 MCP'd CTO with `b9a49a4e` — silver-layer enrichment approach (494 partitions of `silver/transactions_enriched/`) framed as "SUPERSEDES the brief's Phase 6 plan." Material architectural pivot shipped WITHOUT CTO pre-flag.

Parallel with DS's shipped Path A gold-runtime merge (`dfaeddc2`, already on S3 MATCH-verified 20 min earlier).

CTO halted both lanes pending Andrew arbitration.

### 5.2 Andrew directive

User verbatim: *"if AE diverged, they and their work must be brought in line with our plan."*

**Path A (DS gold-runtime merge) is canonical.** AE's silver-enrichment workstream rolled back to diagnostic path.

### 5.3 6-step action list to AE

CTO authored explicit 6-step directive:
1. Dispatch qa-runner for DS Phase 6a `dfaeddc2` (unblocked DS)
2. Confirm no pending production writes to `silver/transactions_enriched/`
3. Relocate `enrich_transactions_with_schwab.py` to `data/black_diamond/scripts/diagnostics/` with diagnostic docstring; commit `768818d1`
4. Preserve 494 partitions (no delete); add `_DIAGNOSTIC_ARTIFACT.txt` marker at S3 prefix (ETag `6596959de350a90b431c77a7ec09979f`)
5. Schema-drift investigation as separate deliverable (see §6)
6. `account_xref` layer stays at `03_silver/account_xref/` as standalone silver dimension

AE ACK'd all 6 + session log protocol violation addendum. Clean recovery.

**Preserved from AE's work:** `03_silver/account_xref/` (valuable standalone BD↔Schwab mapping), BD `original_account_number` == Schwab acct10 zero-stripped finding, schema-drift discovery (§6), Jessica Lindsey / William Chan recovery evidence.

---

## 6. BD silver schema drift RCA — Path X-lite authorized

### 6.1 AE flag + investigation

AE 0.6 surfaced that `silver/transactions` dropped `is_nna` / `is_nna_inflow` / `is_nna_outflow` columns post-2026-01-27; signal moved to `external_flow`. AE's own enricher missed 111,333 rows in 2026 on initial pass.

CTO grep survey of `is_nna_*` consumers:
- `data/black_diamond/scripts/gold/lib/nna_flows.py` — SAFE (classifies by `transaction` type strings via INFLOW_TYPES/OUTFLOW_TYPES frozensets)
- `data/black_diamond/scripts/gold/C_01.canonical_nna.py` — SAFE (consumes via nna_flows.py)
- `infra/aws/lambda-layers/bd-gold-common/python/bd_gold_common.py` — PRODUCES is_nna_* (for old consolidator Lambda, now deleted)
- `infra/aws/lambda/bd-pipeline/bd-gold-layer/lambda_function.py` — recomputes on the fly

Phase 6a C_01 qa-runner dispatch confirmed safe on this axis. Schema drift does NOT affect the live code we shipped.

### 6.2 AE Path X-lite RCA (`6c58f0ec`)

AE 4-hour SLA on investigation — shipped in 1 hour. Key findings:
- Producer post-2026-01-27 is `merge-daily-incremental.py` (new 1,147-line direct XLSX→parquet script on bd-exporter EC2, replaces bd_transaction_consolidator Lambda which is DELETED)
- Root-cause commit `1c5b4b5d` "Switch BD ingestion to Daily template" 2026-01-28T22:10:04Z — unintended consequence, no CHANGELOG, no consumer pre-flag
- **Production blast radius: ZERO.** All gold consumers classify from `transaction_type`/`action`. bd-gold-layer Lambda recomputes on the fly. Drift-tolerant by accident.
- Only affected consumer was AE's own (now-relocated) enricher

### 6.3 Path X-lite decision — 5-answer set

Andrew's answers on AE's 5 open questions:
1. **TO owner: AE 0.6** (bd-exporter is AE's scope)
2. **Backfill scope: forward-only** (zero consumers broken; no historical rewrite)
3. **Pre-commit schema-delta gate: NO.** Andrew verbatim: *"this should in practice never happen. It seems like there is one schema somewhere that may have drifted somewhere and we should just open an investigation explicitly into that."* Philosophy: don't build generic drift-tolerance tooling. One-off investigation per instance; RCA `6c58f0ec` IS the investigation.
4. **Delete dead `bd_transaction_consolidator` source: YES**
5. **Draft `BD_SILVER_TRANSACTION_CONTRACT.md` ADR: YES** (short, with drift-notification rule)

Path X-lite authorized, AE self-owns TO authoring. Not bundled with HLOT2b RAVC4 — ships independently after chain settles.

---

## 7. DS 42/42 MATCH S3 sweep + CHART-ALIGN/COHORT-A upload

### 7.1 Andrew stale-drift directive

Andrew 19:08 ET: *"make sure S3 scripts are fresh and deployed it is your responsibility... fuck DT thats all you go."*

### 7.2 DS comprehensive sweep

DS extended DS-owned upload scope from `.py` only to ALL `code/gold/` artifacts (`.py` + `.sh` + `.yaml`). Sweep result: 40 MATCH + 2 STALE (D_00c CHART-ALIGN `62a24746`, D_04 COHORT-A `3cf43c26`) → post-sweep 42 MATCH, 0 STALE.

Three files uploaded via committed-ref pattern:
- `code/gold/gold_dispatch.sh` (`425c0fa2` — 0.7.0_AE): ETag `c8d6aaa08a1eb15e328f3ab703bc9990`
- `code/gold/D_00c.portal_leaderboard.py` (`62a24746` — CHART-ALIGN): ETag `e7f1ce0aa7280f71ab6a20361dfc9902`
- `code/gold/D_04.client_portal_summary.py` (`3cf43c26` — COHORT-A): ETag `2b07267de68efde5a9fde67855c5b186`

### 7.3 Retroactive CHART-ALIGN pre-flag ACK

DS noted they uploaded D_00c without formal pre-flag #2. CTO retroactively ACCEPTED — my prior MCP `20260421T184810Z` "CHART-ALIGN (DS~B, pre-flag #2 incoming — proceed)" was conditional-GO; plus Andrew's stale-drift directive; plus compiler-gate PASS; plus COO GO'd close path. Not a protocol skip. No formalization required.

### 7.4 Memorialization candidate

**DS-owned upload scope extension** (post-HLOT2b RAVC4): DS-direct upload covers full `data/black_diamond/scripts/gold/` tree (`.py` + `.sh` + `.yaml`). No DT queue. No AE queue. Memory file `feedback_ds_commits_ae_deploys.md` extension at session close.

---

## 8. Watchdog grace-window fix (`11478af7`) — AE 0.6 cross-lane execution

### 8.1 Andrew directive

Andrew 19:26Z: *"there should not be keep-alive, we should have the watchdog working effectively enough that we never need to do that."* + 19:31Z: 5-min grace window.

0.7.0_AE_CloudOps (owner of watchdog pattern) was offline. AE 0.6 shipped fix cross-lane with Andrew's explicit directive.

### 8.2 Design

Replaced 0.7.0_AE's `GOLD_KEEP_ALIVE` marker + 1h TTL (`425c0fa2`) with:
- `/var/lib/watchdog-last-gold` stamped on every `pgrep` hit (EBS-persisted)
- 5-min grace window after last sighting
- No operator-facing marker / no escape hatch
- Reverted `gold_dispatch.sh` `/tmp/GOLD_KEEP_ALIVE touch`

### 8.3 Deploy

- Repo `11478af7` pushed
- S3 `code/runner/watchdog-shutdown.sh`
- QA runner live-patched (md5 `4dac941c`)
- PROD runner (`i-01003b035d2988dfb`) live-patch pending before 23:00Z nightly

### 8.4 Cross-lane authority note

Future reference: `0.7.0_AE_CloudOps` retains primary ownership of watchdog pattern; `11478af7` shipped under Andrew-override during 0.7 offline window. Ownership does not transfer.

### 8.5 Architectural carry-forward

Grace-window pattern is shared infrastructure. When `inf-gold-layer-runner` gets provisioned under ADVI_INFLEC W2.1, it inherits `11478af7` design — noted in ADVI_INFLEC PRD §6.2 reference to bd-gold-layer-runner watchdog shape.

---

## 9. COMP_LEARNS closure — REGISTRY row move (`324e0143`)

2.1.0_SA_COO MCP'd base CTO with REGISTRY row-move request for COMP_LEARNS → Completed/Archived. Andrew closure directive 14:35 ET ("Yeah agreed go ahead"). Dyad `1.1.0_SA_CTO` + `2.1.0_SA_COO` handled project-scoped operations; base CTO owns workspace-wide REGISTRY.

Final state: 20 COMPLETE + 1 DEFERRED (.005 superseded by .021 mutation engine) + 1 STAGED-EXT (.010 externally-gated on Andrew PRD doc N1).

§8 v0 exit criterion satisfied at `.017` ship `695c0d59`. CTO lane closed `794f97df`. DS lane closed `22889582`.

Changes: REGISTRY.md row moved from Active to top of Completed/Archived; prompt.md dashboard row moved from Active to Recently Completed/Merged.

---

## 10. ADVI_INFLEC — second partner PRD (v1.0 → v1.1 → v1.2)

### 10.1 DS~D investigation brief

DS~D delivered comprehensive partner-diligence: `docs/briefs/cto-brief-inflection-partner-data-investigation.md`. Inflection Wealth Management = $667M AUM RIA on Orion Portfolio Solutions, 99.4% Fidelity, 4.29M transactions, 29-col schema. Q2 2024 gap (65 business days) blocks full historical rebuild until Andrew re-downloads from Orion. 60-70% BD pipeline code reuse estimated.

### 10.2 PRD v1.0 (`1c611056`)

Initial PRD authored with central architectural finding: Opal serving layer is already multi-tenant by firmId. `opal-partners-data` Lambda reads firmId from JWT → `get_firm_bucket()` from `opal-users-v2` DynamoDB. Adding Inflection = new tenant, not new tenant system.

Compiler evidence: `comp-routes auth-map` confirmed all `/api/scoped/advisor-intelligence/*` routes are firm-agnostic; `FIRM#mockadv → opal-data-bd` existing precedent.

10 open questions surfaced.

### 10.3 PRD v1.1 (`2e772a5b`) — Andrew §10 Q1-Q4 landed

Andrew answers:
- **Q1 White-label: NO** — shared Opal portal; firmId routing handles isolation. W7 CANCELLED. But added W5.0 DE housecleaning — refactor `portal/src/pages/AdvisorIntelligence/` into `_shared/` primitives + `_partners/` overrides. Andrew: *"we are going to have to be surgical with how we organize components if shared or unique."*
- **Q2 Gold runner: dedicated** `inf-gold-layer-runner` + NEW dedicated `inf-exporter` EC2. Andrew: *"No it will need new runners because it is a different data source with different protocol for downloading."*
- **Q3 Orion SFTP/API: NO.** Custom `inf-exporter` with Playwright + OTP relay. Andrew: *"modified EC2 strategy ... different JavaScript/HTML export page and have to figure out a way for the EC2 to be able to receive a text message from me with OTP."* Designed OTP-relay sub-component (§6.3 of PRD).
- **Q4 Firm-rep structure: maintain 49F as base.**

3 new opens added: Q11 OTP delivery method, Q12 credential storage, Q13 user domain gating.

### 10.4 PRD v1.2 (`089f83fc`) — comprehensive resource inventory

Andrew: *"make sure you covered the opal-partner-inflection table like how we did for 49 for user-specific permissions grouping and all that. make sure you cover all the resources in your document, maybe a good time to use compilers now just to be absolutely sure."*

Compiler + direct-grep audit surfaced material gaps in v1.1. v1.2 adds:

**NEW SHARED INFRA resources (§4.2 rewritten):**
- `opal-partner-inflection` DynamoDB table via existing parameterized `partner-firm-table` TF module — one-liner mirror of `49financial.tf`
- `opalinvest-auth-handler` generalization — currently has `PARTNER_TABLE_49FIN` hardcoded; needs `getPartnerIdentity()` to derive table from firmId + IAM wildcard grant + deploy
- Lambda@Edge FIRM_BUCKET_MAP updates in TWO files (`auth-validator-edge` + `shared-advisor-router`, must stay in sync)
- `portal/src/lib/firmAccess.ts` FIRM_ALLOWED_PATHS entry per ONBOARDING.md §5 Step 4
- `portal/src/api/endpoints/advisor-intelligence.ts` — 10 hardcoded `'49financial'` default-fallbacks → JWT-derived
- `portal/src/contexts/AuthContext.tsx` dev-mode generalization
- `infra/aws/users/partner-schemas/inflection.md` documentation per ONBOARDING.md §5 Step 6

**W1 expanded 4→9 tasks** to cover above.
**W5 expanded to 9 tasks** for portal code cleanup per §4.2.

§8 Compiler Tools section rewritten with comprehensive audit runs:
- `aws dynamodb list-tables | grep partner` → surfaced `opal-partner-*` pattern
- `grep -rn "49financial" infra/aws/` → 8 live hardcoded call-sites
- `grep -rn "49financial" portal/src/` → 14 hardcoded call-sites
- ONBOARDING.md §5 direct-read → authoritative partner-onboarding runbook

### 10.5 PRD handoff to COO

MCP dispatched `20260421T194046Z`. COO ACK'd with decomposition plan:
1. Compiler mandate sweep (comp-blast + comp-pipescript overlap) before TO authoring
2. Parallel-startable TOs first (W0 + W1.1-W1.9 + W5.0.1-W5.0.6 + W3.1)
3. Staged TOs for W2/W3.2-W3.4/W4/W5/W6
4. ADVI_ROLLUP tail cross-domain coordination flagged
5. COO MCP Andrew direct for W0.1/W0.3/W0.4 (Q2 re-download + Orion walkthrough scheduling + remaining §10 answers)

Phase 0 → Phase 1 transition on COO TO dispatch.

---

## 11. Commits this session (CTO authorship)

| SHA | Description |
|---|---|
| `964a9819` | Session 36 mid-cycle dashboard sync (post-/clear reconciliation) |
| `0a37d545` | Session 36 — Andrew 5-item decision walkthrough |
| `324e0143` | COMP_LEARNS closure — REGISTRY row move + dashboard |
| `1c611056` | Register ADVI_INFLEC — PRD v1 |
| `2e772a5b` | ADVI_INFLEC PRD v1.1 — Andrew §10 Q1-Q4 landed |
| `089f83fc` | ADVI_INFLEC PRD v1.2 — comprehensive resource inventory |

(This log commit pending.)

---

## 12. Compiler Tools (this session)

| Tool | Command | Result | Context |
|---|---|---|---|
| `comp-routes auth-map` | `comp-routes auth-map` | PASS | Verified multi-tenant CF routing for ADVI_INFLEC PRD §3 |
| Direct grep | `grep -rn "is_nna" + "external_flow" infra/aws` | Found 40 + 56 files | BD silver schema drift consumer audit |
| Direct grep | `grep -rn "49financial" infra/aws + portal/src` | 8 + 14 hardcoded call-sites | ADVI_INFLEC v1.2 resource inventory |
| Direct AWS CLI | `aws dynamodb list-tables | grep partner` | Surfaced opal-partner-* pattern | ADVI_INFLEC PRD v1.2 |
| Direct AWS CLI | `aws dynamodb scan opal-users-v2 | grep FIRM#` | `FIRM#mockadv → opal-data-bd` precedent | ADVI_INFLEC PRD |
| Direct AWS CLI | `aws s3 ls opal-data-bd/` | Bucketing layout | ADVI_INFLEC §4.1 mirroring |
| Direct TF read | `partner-firms/49financial.tf` + `modules/partner-firm-table/` | Confirmed parameterized module | ADVI_INFLEC v1.2 W1.4 |
| Direct doc read | `infra/aws/users/ONBOARDING.md §5` | Authoritative runbook | ADVI_INFLEC v1.2 W1/W5 structure |
| Direct code read | `opal-partners-data/lambda_function.py` | Multi-tenant `get_firm_bucket()` confirmed | ADVI_INFLEC PRD §3.1 |
| Direct TF read | `bd-pipeline/{main,lambdas,ec2,s3}.tf` | 5-file canonical split | ADVI_INFLEC §4.1 mirroring |

---

## 13. Feedback / memory candidates (pending session-close write)

| File | Rule | Why |
|---|---|---|
| `feedback_c01_source_system_nat_date_guard.md` | Outer-merge row-additive source_system introductions need defensive date coercion | dfaeddc2 → d87377a5 regression |
| `feedback_schwab_trn_nna_zero_gross_filter.md` | TOA/ACAT zero-gross rows in TRN_NNA silver must be filtered pre-aggregation | Classifier passes them; consumers would crash downstream |
| `feedback_gold_runner_inter_script_watchdog_kill.md` | Gold runner needs watchdog grace-window (not keep-alive marker) to survive inter-script gaps | AE 0.6 `11478af7` fix + Andrew directive |
| `feedback_phase6a_class_ravc_needs_d_grain_evidence.md` | Schema-additive changes with D-consumer impact need D-grain evidence before RAVC4 close | My Phase 6a accept closed on C_01 grain only; D_04 crash surfaced post-accept |
| `feedback_acceptance_flex_for_urgent_regression_fix.md` | 60-sec ACCEPTANCE FLEX MCP is right pattern for urgent regression-fix-on-authorized-change (CTO+COO objection window without blocking critical path) | DS d87377a5 direct-ship pattern |
| `feedback_ds_commits_ae_deploys_extension.md` | DS-owned upload scope covers `data/black_diamond/scripts/gold/` tree including `.sh` + `.yaml` (not just `.py`) | Andrew stale-drift directive + DS 42/42 sweep |
| `feedback_architectural_pivot_needs_preflag.md` | Shifting a workstream's architectural layer (e.g., gold-runtime → silver-producer merge) requires CTO pre-flag before shipping, regardless of perceived Andrew directive scope | AE 0.6 silver-enrich pivot → Path A rollback |

---

## 14. Open items / next steps

### In flight (agent execution)
- AE 0.6 qa-runner `--group D` completion (D_02 PID 3977 in flight) → next `--chain full --force` dispatch validating HLOT2+HLOT2b+Phase 6a+D_04 fix+CHART-ALIGN+COHORT-A
- AE 0.6 PROD watchdog live-patch before 23:00Z nightly
- COO ADVI_INFLEC TO decomposition (compiler mandate sweep → W0/W1/W5.0 TOs → GO firings)

### Awaiting Andrew
- ADVI_INFLEC §10 Q5-Q13 remaining opens (historical AUM approach, history start, Keil dedupe, Journal asymmetry, New Accounts Rep handling, Fidelity enrichment, OTP delivery method, credential storage, user domain gating) — non-blocking for W1/W5.0 start
- W0.1 Q2 2024 Orion re-download — gates W3 silver build
- W0.3 Orion sign-in flow walkthrough with AE — gates W2.6-W2.8 exporter dev
- AE 0.6 TRN_NNA AC#3 methodology parked item

### Parked
- HLOT3a/b Reverse Split + Spinoff CA classifier (STAUDT follow-up)
- Advisor-level flow-attribution reconciliation sentinel (standing-backlog, NOT gated)
- Phase 6b V1 emit-time architect lookup TO (awaits 6a RAVC closure + DS bandwidth)
- $21M Patch A sibling investigation TO (COO authoring, non-blocking)
- AE Path X-lite TO (self-owned, awaits chain settle)

### Closed this session
- Phase 6a Schwab TRN_NNA RAVC4 (C_01 grain)
- HLOT2 Patch A close-partial at 73%
- D_04 regression d87377a5 retroactive accept
- 5-item walkthrough all 5 decisions
- COMP_LEARNS REGISTRY row move
- ADVI_INFLEC PRD v1.0 → v1.1 → v1.2 + COO handoff
- Architectural collision (AE silver-enrich → Path A) resolved
- BD silver schema drift RCA + Path X-lite 5-answer authorization
- Watchdog grace-window fix (11478af7) acknowledged
- DS 42/42 MATCH S3 sweep acknowledged

---

## 15. Meta-observations

1. **Multi-tenant architecture paid off twice this session.** Phase 6a C_01 merge respects #2 per-day gating by construction; ADVI_INFLEC PRD confirmed the firmId-scoped serving layer supports a new partner with zero CF/API/Lambda-code changes. Investment in multi-tenant primitives (ROLGAT 2026-04-17 JWT claims + `opal-partners-data` `get_firm_bucket()`) is structural leverage.

2. **Architectural pivot without pre-flag is the highest-cost protocol failure mode.** AE 0.6's silver-enrich workstream shipped 494 partitions before surfacing to CTO. Recovery required full halt + Andrew arbitration + 6-step action list + S3 marker file. The rollback was clean but the context switch was expensive. Pre-flag discipline on layer-changing work must be non-negotiable.

3. **Andrew's "momentum over completeness" stance is operationalizing.** Patch A 73% accept, D_04 regression direct-ship retroactive accept, CHART-ALIGN upload under stale-drift directive — all are pattern applications of the same principle. The organization needs to internalize ACCEPTANCE FLEX MCP as the "momentum discipline" — fast-ship with objection window, not fast-ship without observability.

4. **Compiler-tool + direct-grep audit caught significant PRD gaps v1.1 → v1.2.** The `opal-partner-inflection` table, auth-handler generalization, Lambda@Edge FIRM_BUCKET_MAP updates, portal `advisor-intelligence.ts` hardcodes — all would have surfaced as blockers during COO decomposition or AE TO execution if v1.1 had shipped. Lesson: compiler sweep is worth the 30 min spent on PRDs whose scope touches shared-infra.

5. **Watchdog `GOLD_KEEP_ALIVE` → grace-window arc is a microcosm of design discipline.** AE 0.7 shipped keep-alive under deadline pressure; AE 0.6 shipped grace-window under Andrew's explicit "no keep-alive" directive. The grace-window is the right design; the keep-alive was a band-aid. Both engineers did their best given constraints. The pattern to retain: Andrew's directive to go FROM the band-aid TO the structural fix was the forcing function. Without the explicit "fix the root cause" ask, band-aids accumulate.
