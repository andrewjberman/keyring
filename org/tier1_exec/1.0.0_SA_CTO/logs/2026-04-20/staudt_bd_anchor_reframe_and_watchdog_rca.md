# 1.0.0_SA_CTO — Session 34 Log

**Date:** 2026-04-20 (Mon, PM)
**Scope:** ADVI_STAUDT pivot from internal-universe-unification to BD-anchored engine accuracy + QA-runner watchdog incident RCA + FIX wave PROD ship + BFIX wave reshape under Andrew's "we don't track that" directive.
**Continuity from:** session 33 (`advi_staudt_prd_and_layer_audit_progress.md`) — SSM d749a6b2 was firing as that log closed; this session picks up mid-flight.

---

## 1. Session startup

- Registered 1.0.0_SA_CTO (PID 35160), broker connected, `inbox-watch` live, compiler context set.
- Inbox at start: 2 AE messages on QA-runner SSM d749a6b2 dispatch (16:57:51Z).
- COO not registered at startup. Sent state-request MCP; COO came online shortly after with a full FIX-wave picture (all 7 fixes + cancellations + qa-runner d749a6b2 in flight, ETA 17:24Z).
- Session 33 dashboard was current; no stale-TO findings to reconcile.

---

## 2. Andrew reframe — BD is the ground truth (not internal universes)

**Turn 1:** COO's brief carried the "Penfield $400M-vs-$434M = universe truncation (3,608 acct delta)" framing forward from earlier sessions. I relayed it to Andrew in the oriented summary as if it were a concluded finding. Andrew corrected: *"Universe truncation is not an appropriate conclusion to come to, that was a theory that may not even be relevant."*

**Turn 2:** Andrew elaborated the north star: *"Black Diamond is our ultimate source of truth with regard to currently active accounts, of which there is something like 6500 of them at this moment. I understand that different accounts have phased in and out of existence over the last 6 years but I think we need to be clear on what we're ultimately trying to accomplish here which is to create a system that is accurate in the present, tracking all active accounts and the holdings therein."*

**Memory saved:**
- `project_bd_is_ground_truth.md` — BD is authoritative for active accounts (~6,554 at 2026-04-16); system goal is present accuracy; don't compare internal-A vs internal-B, compare against BD.
- `feedback_no_unverified_theories_as_conclusions.md` — don't carry causal hypotheses forward as facts; decompress COO's compressed shorthand when forwarding to Andrew.

**Immediate impact:**
- OPB (Option B scoping) TO put on HOLD — the A-vs-B internal-universe binary is a false choice when neither universe is anchored to BD. MCPed AE + COO to park OPB pending DS~A investigation.
- DS~A's ad-hoc BD investigation re-framed as the ground-truth path.

---

## 3. QA-runner watchdog incident (d749a6b2 → 9139086d → RCA complete)

**17:16Z:** AE alert — QA runner `i-0090b823a4a0997e3` unexpectedly STOPPED mid-D_02 at 17:06:55Z. Shutdown reason `Client.InstanceInitiatedShutdown`.

**17:22Z:** AE RCA candidate = watchdog-shutdown.timer (commit `50dc0f7d` shipped 12:07 ET today) missed manual-SSM process names. Widened regex commit `9139086d` (`run_gold_layer|gold_rebuild|build_gold|gold_dispatch|gold_prof|gold_layer_scripts/`) and re-dispatched as SSM `b5ad3829` at 17:21:22Z.

**17:47Z:** `b5ad3829` Group D complete 26m07s clean. Widened regex proven in 5 consecutive active-run SKIP cycles.

**Andrew flagged (verbatim):** *"We had a canonical one that worked quite well. Did 0.6.0_AE just make a totally new watchdog with new rules on the spot or something?"* Escalated to structural post-mortem.

**Post-mortem (Q1-Q6) returned by AE (commit `9a700351`):**
- Q1 (pre-enable audit): NO audit. AE treated canonical-as-shipped as trusted-by-pedigree; should have re-verified regex against QA's manual-SSM invocation surface. Fuck-up admitted.
- Q2 (validation window): NO 30-sec `pgrep -f` smoke test in the 4h50m between enable and first real workload. Admitted.
- Q3 (PROD exposure history): **CTO-owned audit.** Log pulled from PROD via SSM `910c0fbb`:
  ```
  [2026-04-11T02:18:12Z] SKIP: uptime 5m < 30m threshold
  [2026-04-11T02:33:19Z] SKIP: uptime 20m < 30m threshold
  ```
  PROD's 2026-04-11 manual SSM `e99ecf29` did NOT misfire because the uptime threshold was **30m at the time**. Run completed in ~29m; `shutdown -h +2` fired before the 30m mark. Pure threshold luck — the regex was broken the whole time. Commit `af9f40a0` (2026-04-09) dropped threshold 30m→10m, opening an 11-day latent-vulnerability window (2026-04-09 → 2026-04-20) where PROD would have misfired on any manual SSM > 10m. No PROD manual SSM was run in that window, so no misfire was observed; pure luck, not design.
- Q4 coverage test: `scripts/test_watchdog_regex_coverage.sh` to enumerate gold entry points + assert `pgrep` non-empty. GO'd, this week.
- Q5 GOLD_KEEP_ALIVE lifecycle: AE removes post-run + verifies `marker_missing`. No future dispatch prepends the marker. Verified closed post-b5ad3829.
- Q6 structural: process-tagging TO staged (`exec -a "[opal-gold] $0"` → regex collapses to `\[opal-gold\]`). Author now, execute post-STAUDT.

**PROD live-patched** via SSM `910c0fbb`: pre-hash `3520122ffa8b6e3dabfca8c03b1f0db7` → post-hash `f3a20c836c899957b7275b9d3c390e84` (matches CLOUD `9139086d`). Persists on EBS across reboots. PROD `i-01003b035d2988dfb` clean-stopped 17:51:48Z.

**Q3 addendum appended to RCA** file `infra/aws/ec2/bd-gold-qa-runner/RCA_20260420_watchdog_shutdown.md` with full evidence and PROD live-patch receipts.

---

## 4. FIX wave PROD deploy complete

**COO GO'd** AE for `bd-gold-trigger` at 19:17:31Z after all 4 RAVC4 closures landed:
- FIX7 (~A `e0550693`) — D_00b RA-P5 disable, firm ADV-AUA $1.651B
- FIX3A (~A `43c3693a` + `c25afc6c`) — D_00c+D_02 nna/ revert, structural PASS
- FIX6 Phase 2 (~D `b7a75374`) — 3-yr NNA gate, 1,092 entries oldest 2023-04-21
- FIX2 (~B `c25afc6c`) — D_00c L569 explicit no_fee WARN + $35M sentinel

**PROD SSM `3e06059f`** 19:23:12Z → 19:49:33Z (26m21s), all 7 scripts clean. AE closed FIX-wave RAVC loop at 19:58Z, QA reverted c6i→c6a.16xlarge.

**Wave outcome:** FIX7 is the user-visible win — firm NNA chart line went from $330M (pre-wave) to $1.649B (matches current gold canonical/holdings). Already live on PROD before this session started; this session's PROD ship is the platinum-layer commit of FIX1/FIX2/FIX6/FIX7 together.

---

## 5. DS~A engine_accuracy briefing — the $46M gap

**`data/black_diamond/diagnostics/STAUDT/BRIEFING_aua_engine_accuracy_2026-04-20.md`**

DS~A's ad-hoc BD investigation produced two independent AUA confirmations that agree within $1M:

1. **Andrew's identity check:** EOP 2025 AUA $1,446M + 2026 YTD NNA $123M + 2026 YTD GRO $123M = **$1,696M implied**.
2. **BD silver/allocations direct sum on 2026-04-16:** **$1,697,678,133**.

Portal/gold canonical firm AUA: **$1,649,375,328**. Gap: **-$46M / -284bps** (5.6× over 50bps target).

**Key takeaway:** flow path (NNA+GRO) is correct against BD; snapshot path (canonical/holdings) is the outlier. Flows derived from raw transactions are accurate; the gap lives in B_00.canonical_holdings.py + upstream.

**Three bugs per briefing:**
- Bug 1: `bd_stale` overreach → $38.6M / 111 accts (PCRA/AQR/Fidelity-401k/Schwab-Trust-Bank)
- Bug 2: Schwab cash deficit → $18.8M / 4,950 accts (BD cash not reaching canonical)
- Bug 3: non-Schwab dropped → $18.5M / 62 accts (truly-non-Schwab never admitted)

**The `aua_residual` silent absorber:** $50M YTD 2026 drift hidden in the reconciliation field, ±$30-46M daily swings, never alarmed. Andrew's identity check was the first thing to surface this.

---

## 6. BFIX wave authoring + 3 diagnostic probes

COO authored BFIX1/BFIX2/KPI TOs (Andrew-approved in chat). ~A committed **`081223b5`** (B_00.canonical_holdings.py +102/-6):
- **BFIX1:** new `build_persistent_rps_accts()` + `reconcile_date()` param for Direction 2 (persistent multi-day RPS predicate). Recovers ~$6.6M / 25 accts.
- **BFIX2:** bd_only re-injection after reconcile for accts in `bd_df` missing from `holdings`. Recovers ~$14.2M / 54 newly-opened accts.
- Phase 0 mechanism note caught the briefing's $38.6M attribution error (only $6.6M is B_00's surface); remaining $32M lives upstream in A_03.positions_cube.

**CTO 3-question diagnostic probes (per silver-A→D-rerun-sensitive pre-flag ACK):**
- **Q1 BFIX2 re-inject filter:** 92-acct re-inject set decomposes to 58 intended + 28 BFIX1-overlap (dissolves post-deploy) + 6 fp_dust. Bug 2 absorption risk: NONE (cash deficit affects accts INSIDE canonical, not dropped ones — disjoint populations). **GREEN.**
- **Q2 bd_only downstream NaN handling:** Direct B_00 consumers (B_02, B_03, C_02) don't read `ticker`/`schwab_units`; bd_only rows with `NaN`/`empty` flow silently. NaN price drags `pct_priced` metric (feature, not crash). Post-deploy spot-check: ≥80% re-injected priced via canonical_prices, else BFIX2b. **GREEN.**
- **Q3 BFIX1 outage boundary:** Persistent set 5,450 accts (77.6% of 7,027 mapped). 1-5 day outage robust (0-0.3% drop); 7-day full dark = cliff but inherits same failure mode as current code (L423-431 short-circuit). Real loss in 7d full outage: $200. No circuit-breaker needed. Optional WARN log `if persistent_set < 50% mapped` staged as follow-up. **GREEN.**

---

## 7. Combined deploy plan — Andrew's "keep pushing to full fix"

At 19:42Z Andrew: *"I think we should just keep pushing to try and get the full fix sorted."*

Pivoted from staged BFIX1/2 → BFIX3 → BFIX4 to **combined deploy**:
- BFIX3 (Schwab cash investigation) starts immediately on ~A in parallel with FIX-wave PROD fire
- BFIX4 TO authored proactively against A_03 positions_cube $32M signal
- DT holds B_00 S3 upload until all 4 BFIX patches commit
- Single pre-flag, single upload, single qa-runner --group ABCD, combined PROD deploy
- Branch-point: if BFIX3 or BFIX4 surfaces as multi-file/architectural, pivot back to staged

---

## 8. BFIX3 Phase 0 — branch point triggered

~A closed BFIX3 Phase 0 in 25 min (commit note, file `BFIX3/cash_flow_trace.md`). **Root cause was NOT what the briefing said.**

- Not Schwab (Schwab RPS has 1 cash row firmwide, $19K)
- Not a B_00 filter bug (cash handling L390-396 / L471-472 / L520-525 all correct given input)
- **Real cause:** BD has two incompatible cash models:
  1. Allocations model: account-level `cash_market_value` from BD accounting (sweep + settled balances)
  2. Transactions model: cash only arrives via transaction side-effects
- A_03.positions_cube reads model 2 → only 14% of accts (853/5,919) have cash in cube; other 5,397 accts ($27.95M) have BD-reported cash that never enters cube.

**Branch point triggered.** Two paths proposed:
- **Path Alpha:** A_03 synthesizes cash from alloc where transactions don't deliver. DS lane, 1-2h, ships in combined deploy. BFIX3b+BFIX4b collapse into one A_03 patch. Closes gap to +50bps overshoot. **Cost:** non-transactional position in cube, diverges from FIFO purity.
- **Path Beta:** Fix BD bronze ingestion at source. AE lane, slow, forces staged pivot.

~A + COO both leaned Path Alpha. I recommended Path Alpha + direct injection with `source='bd_cash_synth'` tag (over the cleaner-but-heavier overlay-parquet variant).

---

## 9. Silver-allocations deep dive — 62 partitions, per-acct distribution

Pulled `s3://opal-data-bd/silver/allocations/*.parquet` (62 dates, 2026-01-16 → 2026-04-16).

**Firm-level cash across the full window:**

| Metric | Min | Median | Mean | Max | First | Last |
|---|---:|---:|---:|---:|---:|---:|
| Accounts | 6,147 | 6,338 | 6,341 | 6,554 | 6,147 | 6,554 |
| Firm AUA | $1.534B | $1.599B | $1.604B | $1.698B | $1.550B | $1.698B |
| Firm cash (net) | $25.1M | **$31.2M** | $31.7M | $43.7M | $27.1M | $33.6M |
| Cash as % AUA (bps) | 157 | **194** | 197 | 274 | 175 | 198 |

**Per-account distribution (6,687 unique accts × 62 dates = 393K rows):**
- Median per-acct cash: $624 (typical account has a few thousand at most)
- Top 56 accts (≥$100K median cash) carry ~$21M of the firm's $31M cash
- Median cash as % of own AUA: **1.11%** (steady-state)
- 502 accts (7.5%) are fully-invested (always $0 cash); 5,715 (85.5%) have positive cash every day; 184 (2.8%) go margin-debit at some point

**Key insight:** cash has been $25-44M every single day since silver ingestion turned on. Not a drift, not a new bug — a **systemic $27-44M structurally absent** from our canonical view for the entire period. Consistent with Bug 2 framing in the briefing.

---

## 10. Silver-vs-canonical diff — the real gap attribution

Pulled `gold/canonical/holdings/2026-04-16.parquet`. Direct per-account diff against silver allocations 2026-04-16:

| Population | Accts | AUA contribution |
|---|---:|---:|
| Silver only (accts we drop) | 599 | -$44,715,940 |
| Canon only (over-includes) | 12 | +$2,007,201 |
| Overlap (in both) | 5,955 | -$3,523,024 |
| **Total firm gap** | | **-$46,231,763** |

**Overlap reconciliation is nearly perfect:** canon MV $1,649.4M vs silver AMV $1,653.0M = **-21bps** on the 5,955 accts we track. Per-account: median delta $0.08, mean delta $4K, p99 $142K.

**97% of the firm-level gap is the 599 dropped accounts.** Not bugs — accounts we structurally don't see.

**Methodology gap caught by ~A:** DS~A correctly counted 654 untracked (599 absent + 55 in-canonical-but-effective-$0). My analysis missed the 55 "effectively zero in canonical" cohort ($7.76M of BD-reported AUA sitting invisible in portal). ~A's 654 / $52.47M is the correct number.

**Top 20 untracked named accts:** BRYAN DAVID GRUNDHOEFER $5.08M, Craig Smith Rollover IRA $2.59M, CRAIG M SMITH TTEE $2.50M, David Victor Rollover IRA $2.47M, CHARLES SCHWAB TRUST BANK $2.32M, Buck NCF DAF $2.30M, Stephanie Bourland PCRA $2.26M, Lyndon Cook Retirement Plan $2.05M, Silverthorne Home $2.00M, Austin Home $1.75M, Fisher JT AQR brokerage $1.50M, Christopher Taylor PCRA $1.40M, Chad Marek PCRA $1.19M, DONALD WAYNE CRABBE $1.10M, Patterson JT AQR $1.00M, LAURENCE COLE $1.00M, GLENN BRIAN CALLISON $1.00M, Tracey Hopper $950K, David Siu LTC IRA $947K, McLeod Jeff PCRA $876K.

Pattern: PCRA / AQR / Fidelity 401k / Schwab Trust Bank / real estate / DAFs — custodied outside Schwab RPS.

---

## 11. Andrew's strategic call — "we don't track that"

Andrew decision: **don't pass-through the 654 untracked accounts.** We can't reliably track their position-level detail (no holdings breakdown, no lots, no NNA attribution path, no drill-down); injecting $52M of black-box AUA with no composition would be worse than not showing them. Clean "we don't track that" is honest.

**Revised BFIX wave scope (pending MCP dispatch to COO + ~A, awaiting Andrew go):**

| TO | Status | Rationale |
|---|---|---|
| BFIX1+BFIX2 (`081223b5`) | **PROCEEDS** — ships as planned | Real engine bug fixes on accts we DO track; $20.8M recovery from newly-opened + bd_stale overreach |
| BFIX3 (cash synthesis Path Alpha) | **CANCELLED** | Would inject values for accounts we can't reliably track |
| BFIX4 (A_03 cash + absent_from_cube) | **CANCELLED** | Same — non-trackable cohort |
| KPI (~C sentinel) | **RESHAPED** | From "hard-fail if >50bps from BD" to "track untracked-cohort size, alert on material growth / drop-in" |
| B_00 mini-PRD | **AUTHOR NOW** | Documents ~654/$52M untracked cohort as known architectural limitation; post-STAUDT initiative |

**Post-BFIX1/2 firm AUA target:** -284bps → ~-160bps (the $20.8M recovery). The remaining ~$26M gap stays as documented untracked-cohort limitation, not treated as a bug to close.

---

## 12. Ops-infra observations (non-blocking)

- D_00 + D_02 + D_04 were all found stale on S3 during the session (3-script deploy gap). DT + ~D + AE pushed routine uploads + qa-runner --group D dispatch. B_00 stays PARKED per BFIX combined-deploy plan.
- Watchdog timer now proven end-to-end on both PROD and QA runners across systemd-nightly AND manual-SSM paths. Fix persists on EBS; next nightly inherits widened regex.
- Q4 coverage test + Q6 process-tagging TO both queued for AE this week.

---

## 13. Compiler Tools (this session)

| Tool | Command | Result | Context |
|---|---|---|---|
| `comp-build` | N/A — graph cache still current from session 33 | skip | No file changes warranting rebuild this session |
| — | direct `pd.read_parquet` over 62 silver/allocations partitions | N/A | Bulk data probe, not compiler surface |
| — | `git show 9a700351 -- RCA*.md` | OK | Verified RCA file contents |
| — | `git log --oneline --format=... -- infra/aws/ec2/**/watchdog*` | OK | Traced watchdog commit lineage for Q3 audit |
| ~A direct | `comp-pipescript io B_00` (via ~A probes) | GREEN | Confirmed no COLUMN GAPS on BFIX1/2 surface |
| ~A direct | `comp-pipescript deployed D_00 / D_02 / D_04` | STALE → MATCH | Deploy-gap diagnosis |
| ~A direct | `comp-pipescript io D_04` | no column gaps | Widening check pre-upload |

Note: the session's primary surface was data-level reconciliation (parquet reads), not graph-level compiler surface. Compiler tools live on the agents actually modifying scripts (~A/~D).

---

## 14. Commits (this session's direct CTO authorship)

| SHA | Author | Description |
|---|---|---|
| Q3 addendum append on `RCA_20260420_watchdog_shutdown.md` | (AE `0.6.0_AE_PartnerETL` committed on my write) | Q3 PROD exposure audit findings + PROD live-patch receipts + validation receipts |

(Other commits observed this session authored by other agents, for the record:)

| SHA | Author | Subject |
|---|---|---|
| `9139086d` | 0.6.0_AE_PartnerETL | fix(watchdog): widen regex to match manual-SSM gold dispatch paths |
| `9a700351` | 0.6.0_AE_PartnerETL | RCA file creation |
| `d9a419aa` | 0.6.0_AE_PartnerETL | RCA update (Q3 addendum) |
| `081223b5` | 0.4.0_DS_ClientPlatform~A | feat(B_00): BFIX1+BFIX2 — bd_stale predicate tightening + bd_only re-injection |
| `3e06059f` | — (SSM command ID, not git) | PROD Group D FIX-wave deploy |
| `1c62e25c` / `910c0fbb` | — (SSM command IDs) | PROD watchdog state probe + live-patch |
| `b5ad3829` | — (SSM command ID) | QA Group D re-run with widened regex |

---

## 15. Open items / next steps

**Awaiting Andrew go:**
- MCP COO + ~A with revised BFIX scope (BFIX1/2 ship as planned; BFIX3/BFIX4 cancelled; KPI reshaped; B_00 mini-PRD authored).
- Once dispatched: DT uploads `081223b5` to S3 → AE qa-runner full --group ABCD → DT comparison pack → combined PROD deploy of BFIX1+BFIX2 (no BFIX3/BFIX4 bundled).

**Self-driving:**
- None — all lanes either idle or in-flight on non-STAUDT work.

**Parked:**
- OPB (Option B scoping TO) — held pending BD-anchored investigation evidence. Given the untracked-cohort decision, OPB likely gets re-scoped or cancelled entirely post-session.
- EOP2025 (~B) $32M intra-portal inconsistency diagnostic — queued, P3, non-blocking.
- B_00 architectural mini-PRD — author next session as the home for the "don't track that" documentation.
- Q4 watchdog coverage test (AE, this week).
- Q6 process-tagging TO (AE, post-STAUDT).
- Session 33 log's open items remain valid where not superseded here.

---

## 16. Feedback / memory updates

**New memories:**
- `project_bd_is_ground_truth.md` — BD authoritative for active accounts; system goal is present accuracy.
- `feedback_no_unverified_theories_as_conclusions.md` — label theories as theories; decompress shorthand before forwarding.

**No updates needed** to the following (still accurate as written):
- `feedback_prod_runner_eventbridge_only.md` — manual-SSM was a pattern for 0.7.0_AE on 2026-04-10 and 0.6.0_AE today for FIX wave; the memory rule is about scheduled/nightly runs, not ad-hoc coordinated runs.
- `feedback_ec2_gold_runner_sizing.md` — c6i temp-swap was justified by us-east-1d capacity, reverted post-wave.

---

## 17. Notable architectural insights surfaced (carry forward)

1. **`aua_residual` is a silent absorber** of snapshot-vs-flow drift ($50M YTD 2026, ±$30-46M daily swings). KPI sentinel (1b) — `abs(sum(aua_residual)) / sum(aua_current) < 50bps` — formalizes Andrew's identity check as an automated gate. Ship post-wave.
2. **BD has two cash models** (allocations / transactions) that never reconcile. This is a BD-ingestion architectural gap, not a B_00 bug. Path Beta (bronze ingestion fix) remains the correct long-term answer even though we're not pursuing Path Alpha.
3. **Overlap tracking is effectively perfect** (21bps firm-level miss on 5,955 accounts in both silver and canonical). The 599 dropped accts and 55 effective-zero accts together account for ~97% of the firm gap — they are structurally invisible to our pipeline, not bugs in what we track.
4. **ADHC_ROUTER Phase 2** — coverage test from watchdog Q4 feeds the same class of tooling (enumerate all invocation points, assert tool coverage). Worth bundling into the Phase 2 backlog alongside function-level blast nodes + `.sh` corpus indexing + worktree-scoped graph cache.
