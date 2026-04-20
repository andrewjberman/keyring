# 1.0.0_SA_CTO — Session 33 Log

**Date:** 2026-04-20 (Mon)
**Scope:** ADVI_STAUDT project registration + PRD authoring + 4-lane TO dispatch + layer ~A/~B/~C findings acceptance + ~D in flight
**Continuity from:** session 32 (2026-04-17, log `startup_session32.md`)

---

## 1. Session startup (ground-truth reconciliation)

- Registered `1.0.0_SA_CTO` (PID 31848), broker connected, inbox-watch live.
- Inbox at startup: 3 messages — DS ack on drop-step-1 (201925Z), AE SSM d83a1d11 COMPLETE (205356Z), COO 4-bug portal audit (213111Z).
- AE SSM d83a1d11 SUCCESS at 20:48:50Z on 2026-04-17: C_08 + Group D clean, D_04 spot-check sane, `cd177553` prefix swap held (`client_state` Unknown = 1.4%), D_04 `comp-validate` 2 ERRORs confirmed validator-config-bug not data-bug (`windows[0].entries` vs dict `windows.{QTD,YTD,MAX}.entries`) — separate small DS TO, not on critical path.
- COO's 4-bug audit: Travis $82M vs $434M Leaderboard AUA, Leaderboard No-Fee missing, `aua_growth_pct` -79%, NNA daily-vs-cumulative modal gate. COO traced to D_00c/D_02 `tagged_aua` schism + layered band-aids 2026-04-09 → 2026-04-15. Needed architectural call.
- Dashboard drift audit: no stale pending-TO findings this session (dashboard current through session 31; session 32 was state-preserving).

---

## 2. ADVI_STAUDT registered

**Macro:** ADVI | **Project code:** ADVI_STAUDT | **Commit chain:** `1472d1b7` (PRD) → `3f9effe2` (§3.3 Group D 14 sites) → `65945fbf` (§3.0 two-class headline + invariant) → `8dd2f32f` (§3.4 Group B+C) → `ec9c7020` (§4 layer-scoped restructure).

**Artifacts:**
- `docs/architecture/ADVI_STAUDT.md`
- `org/projects/ADVI_STAUDT.json`
- Row added to `org/projects/REGISTRY.md` Active Projects

**Problem statement:** On 2026-04-17 Andrew surfaced 4 live ADVI portal bugs; on 2026-04-20 asked for a deterministic reconstruction of gold+portal state at four checkpoints to attribute what regressed between Wednesday-accepted baseline and current state. Framing: "upstream B→D definitions may have been mishandled, downstream blast larger than it should be; systematic and collaborative, rule out from the source."

**PRD structure after 5 amendment passes:**
- §2.3 Live NNA-path split surfaced during PRD research: after session-32 `cd177553` revert, D_00c+D_02 still on `CANONICAL_NNA_ATOMIC_PREFIX` while D_04+D_00b+D_01+C_08 reverted to `CANONICAL_NNA_PREFIX`. Unreconciled live schism — not just a historical artifact.
- §3.0 Two primary failure classes (Andrew: lead every TO with this):
  - **Class 1 NNA definition change** — grain (CN-P2 `b3f6b1ee`/`ebd737e3` per-advisor cumulative → per-(date, advisor, role) daily-grain) + path (`nna/` vs `nna_atomic/` split after `cd177553`)
  - **Class 2 Group D mapping ambiguity** — tagged_aua source-of-truth (D_00c vs D_02 vs D_04 override, no shared canonical module) + role-split (`D_00c._weighted_aua` L881 + C_08 RA-P5 `d9ab1719`) + fee-split (`D_00c:565` silent clip + D_04 top-level `fee_breakdown.no_fee.aua` NOT swept by B1.fix `5114984b`)
- §3.0 mandatory per-advisor invariants: `sum(role_breakdown[*].aua) == tagged_aua` AND `fee_paying.aua + no_fee.aua == tagged_aua`.
- §3.1 Four checkpoints: **T0** `544877cc` (Wed 2026-04-15 ~20:40 ET), **T1** `f177240b` (Thu 2026-04-16 ~22:30 ET post-polars+perf-war-room), **T2** `ae759bbb` (Fri 2026-04-17 ~07:00 ET post-council+cusip), **T3** `cd177553` (Mon 2026-04-20 current).
- §3.3 Group D PRIMARY focus — 14 production sites enumerated with file:line (D_00c:528/565/580/881, D_02 `build_advisor_books`/`_nna_since`/RA-P2b, D_04:2325-2340 override, C_08 RA-P5 + defensive backfill).
- §3.4 Group B + C material-change scope — every touched script gets a line (B_00, B_01 [21+ commits], B_01b, B_02/B_03; C_00, C_01 [CN-P1/P1b], C_02/C_04/C_05/C_06, C_03 [phantom outflow], C_07, C_08).
- §4 layer-scoped decomposition (Andrew clarification: "rule out from the source"): each lane owns one layer across all 4 checkpoints; findings-write sequencing gate is upstream MCP, not data collection.

---

## 3. COO TO authoring + shape review

COO staged 4 TOs on first pass using time-scoped model (pre-§4 amendment); rewrote to layer × 4-checkpoint model after my URGENT amend MCP. Shape review (20260420T125111Z) returned CONDITIONAL APPROVE with 1 blocking REWORK:

- **REWORK:** add `comp-build` to Phase 0 inside each scratch worktree before first `comp-pipescript io` call. Rationale: `.comp-graph/graph.json` is per-worktree and gitignored; scratch worktree has no graph at start.
- Non-blocking polish: ~C polars probe should pin silver partition version; ~B cusip probe should disclaim T0/T1 expected-low; T0 `544877cc` baseline already contains pre-window regressions (W6-005 `0804b377` + DE `9f6faf9` 2026-04-13) — lanes should report those as "pre-window at T0" not "introduced at T0."

COO committed rework and dispatched GOs to ~A/~B/~C/~D. All 4 TOs opened with §3.0 verbatim, inherited §3.3 (to ~D) + §3.4 (to ~B/~C) verbatim, split compiler mandate into Phase 0 (parallel data collection) + Phase 1 (findings-write gated on upstream MCP) + Phase 2 (handoff), acceptance-criteria rule-out discipline ("clean-bill OR N-findings with evidence; neither without layer-specific evidence").

---

## 4. Layer findings accepted

### ~A (Silver + Group A) — commit `0d34f025`, well under 6h SLA

**Conclusion:** A-group scripts (A_00-A_04) IDENTICAL at all 4 checkpoints — CLEAN-BILL. 3 silver material changes.

- **A-1** (T1→T2): `silver/transactions.cusip` ADDED via `80917a1e` (`merge-daily-incremental.py` + one-shot backfill). Schema 73→74 cols, 97.75% non-null. Primary downstream consumer: B_01 RPS correction keying.
- **A-2** (T2→T3): `silver/ULN/` NEW in `opal-data-schwab` via `6c80c5ed`. 350 partitions, 213,253 rows/partition, 17 cols. **NOT yet consumed by production** — future B_01 position authority source.
- **A-3** (T2→T3): `c270a9b2` rolling-key refresh SHIPPED then `32fbb0d6` REVERTED same day by Andrew. Net zero. B_01 at T3 bypasses via `2a69b97e` dated resolution.

**Group D upstream clean-bill:** A_01/A_02/A_04 (advisor_assignments/fee_rate/client_dimension) artifacts identical across checkpoints. Any Group D tagged_aua / role-split / fee-split discrepancy is **NOT** attributable to upstream dimension changes.

### ~B (Group B) — commit `fd857154`, well under 8h SLA

**7 material findings + 4 clean-bills.**

- **B-1** bond-100x pricing introduced T3 only (`d45fc0dc`+`fd6f362d`) — 152,192 bond cohort, 100x MV inflation at T0/T1/T2
- **B-2** confidence-tiered cap + `market_value_uncapped` T3 only (`cb6d78e2`)
- **B-3** snapshot_date silver/allocations auto-detect at T2 (`ec2c1efc` GOLD-DATE-FIX)
- **B-4** CP-DS1 cusip-keyed rework at T2 (`1db831aa`+`f5f19e77`+`c4ebde9a`+`ae759bbb`) — causally downstream of A-1, chain confirmed clean
- **B-5** synth-inject PIVOT 2/5/6 + Gate 3 silent-close at T3 (`5438de6e`..`d39c4dff`) — **$390M+ synth reduction, largest holdings_lots → tagged_aua propagation path** (primary row for ~D's 2B propagation matrix)
- **B-6** `df.attrs` serialization crash bug at T0/T1 (fixed `52b78c0d`+`b320426b` between T1 and T2) — **T0/T1 B_01 output may be partial/stale**, relevant interpretive caveat for ~D's sample reading
- **B-7** B_02‖B_03 dispatcher race at T1 only (~4h window, fixed `20776727` Thu 23:22)

**Clean-bills:** B_00 (perf-only), B_01b (compiler-visibility), B_02 (zero commits), B_03 (zero commits).

**T3 parquet sanity anchor:** 1,011,807 rows / firm MV $1,646.4M / cusip 98.30% / `market_value_uncapped` present — reproduces COO session-32 closure figures.

**Methodology finding (NEW, important):** `comp-graph` caches at workspace root, NOT per-worktree. `comp-pipescript io` in a scratch worktree reflects T3 state regardless of CWD. My pre-dispatch REWORK (comp-build inside worktree) was INSUFFICIENT. ~B worked around via direct source reads from worktree files. Forwarded proactively to ~C and ~D before they hit the same issue.

### ~C (Group C) — commit `b687ff47`, well under 10h SLA

**5 material findings + 5 clean-bills. Headline is C-3.**

- **C-1 (Class 1 path evidence):** `nna/` 14 cols vs `nna_atomic/` 22 cols. `aua_current` + `growth` ABSENT from `nna_atomic/` — direct cause of C_08 KeyError at T2 that triggered the `cd177553` partial revert. Universe delta: 5,987 → 9,581 accounts (+3,970). `c01_nna_schema_diff.md` is THE authoritative Class 1 path document.
- **C-2 (Class 1 partition gap):** `2026-04-14.parquet` MISSING from both `nna_atomic/` and `role_aua/` at all checkpoints. Backfill `c962ddb3` stopped at Apr 13, never wrote Apr 14. D_00c + D_02 (still on `nna_atomic/` at T3) will silently miss Apr 14 data.
- **🚨 C-3 (Class 2 HIGH-IMPACT):** `role_aua/` backfill (`c962ddb3` Thu 12:42 ET) used **pre-phantom-fix** `account_performance.parquet` — bakes 68,759 cum_* violations into all 2,294 `role_aua/` partitions. **Backfill was never re-run after `85bb2daa` C_03 fix. Corruption persists at T2/T3.** Every D-group script reading canonical `role_aua/` at T2/T3 (D_02 via RA-P4, D_00c via RA-P3, C_08 via RA-P5) is deriving role-level AUA from corrupted daily cum_inflows/cum_outflows. Live pipeline defect.
- **C-4 (Class 1+2):** C_08 CN-P5 flip → crash → revert chain confirmed. Live schism at T3 documented per §2.3.
- **C-5 (Class 2):** Phantom outflow reset bug — 68,759 violations at T0/T1/T2, 0 at T3 post-`85bb2daa`. All D-group scripts reading `account_performance` at T0/T1/T2 received corrupted cum_* values.
- **C-6 C_00 polars port:** CLEAN-BILL, logical equivalence confirmed.

**Clean-bills:** C_02/C_04/C_05/C_06/C_07 (empty git-log in window).

**Directive issued to ~D:**
- C-3 gets dedicated section in `bug_attribution.md`, layer-of-origin = **C (not D)**
- `coo_handoff.md` recommendation: RA-P1c-style re-backfill of `role_aua/` post-C_03-fix is a required fix TO independent of any D-script change
- C-2 Apr 14 gap: test whether any advisor's NNA timeseries has a visible gap at 2026-04-14

---

## 5. Pipeline picture so far

The four-bug portal symptom + live NNA schism decompose into a layered causal tree. Layer assignments per lane findings:

| Layer | Verdict | Key evidence |
|---|---|---|
| Silver / Group A | CLEAN-BILL on A-scripts + 3 additive silver changes (cusip, ULN, rolling-key ship+revert) | ~A 0d34f025 |
| Group B | 7 material findings — bond-100x + cap + cusip rework + PIVOT synth-inject (B-5 biggest lever) + df.attrs crash T0/T1 + race | ~B fd857154 |
| Group C | 5 material findings — Class 1 path producer confirmed (C_01 schema split), Apr 14 partition gap, **role_aua/ backfill carries phantom corruption at T2/T3 (C-3)**, C_08 live schism, phantom outflow T0-T2 | ~C b687ff47 |
| Group D | In flight (~D) | — |

**Cross-layer causal chains already visible:**
- A-1 (silver cusip) → B-4 (B_01 cusip-keyed rework) — CLEAN propagation
- B-1/B-2/B-4/B-5 (B_01 output shifts) → C-3 input — **entangled with** C-5 phantom outflow fix; ~D must disentangle at synthesis
- C-1 (nna_atomic schema split) → C-4 (C_08 flip/crash/revert) → live D-group schism — CLASS 1 complete chain
- C-3 (role_aua backfill corruption) → all D-consumers of `role_aua/` at T2/T3 — LIVE CLASS 2 fault line

---

## 6. ~D in flight right now

**Scope:** Group D layer audit (D_00, D_00b, D_00c, D_01, D_02, D_03, D_04 × 4 checkpoints) + 5 SYNTHESIS deliverables.
**Commits chain so far:** `0d34f025` (~A) → `fd857154` (~B) → `b687ff47` (~C) → **~D synthesis commit pending**.
**Timeline:** 12h SLA from ~C MCP (20260420T132933Z). ETA ~20260421T01:29Z (9:29 PM ET tonight), likely well under given ~A/~B/~C pace.

**Already flagged by ~D during Phase 0:** `comp-blast _weighted_aua` and `comp-trace tagged_aua` return "No nodes matching" — function-level nodes are not indexed in comp-graph. ADHC_ROUTER Phase 2 backlog item confirmed. ~D will fall back to manual file:line evidence using PRD §3.3 14-site table as the authoritative enumeration. Annotating in `bug_attribution.md` as "GRAPH COVERAGE GAP — ADHC_ROUTER Phase 2".

**~D deliverables pending:**
- `layer_D/layer_d_findings.md` — Group D layer verdict (clean-bill OR N-findings) citing ~A/~B/~C upstream
- `SYNTHESIS/group_d_tagged_aua_decomposition.md` (2A — PRIMARY per §3.3: master 4-checkpoint × 14-production-site table with 5-advisor sample and divergence class)
- `SYNTHESIS/group_bc_propagation_matrix.md` (2B — every B/C change → C artifact → D artifact → platinum → portal component; C-3 role_aua corruption and B-5 synth-inject $390M+ lever are the two primary rows)
- `SYNTHESIS/delta_table.md` + `.json` (2C)
- `SYNTHESIS/bug_attribution.md` (2D — one section per COO bug + NNA-path split + C-3 + any sum-invariant violation; layer-of-origin tagged per §3.4)
- `SYNTHESIS/coo_handoff.md` (2E — restore-T0 / keep-T1-2-3 / hybrid per field/bug with per-call fix-TO sketch)

**~D final MCP fires to CTO + COO + Andrew** on commit.

---

## 7. ADHC_ROUTER Phase 2 backlog — promoted items this session

Session surfaced two new ADHC_ROUTER Phase 2 priorities (promoted based on live STAUDT impact):

1. **Function-level blast nodes** (confirmed by ~D live encounter). Current graph only indexes script-level nodes; `comp-blast D_00c._weighted_aua` / `comp-trace tagged_aua` return "No nodes matching" and force manual grep fallback.
2. **`.comp-graph/` worktree-scoped cache** (confirmed by ~B live encounter). Cache at workspace root means `comp-pipescript io` in a scratch worktree returns T3 state regardless of CWD. Forces lanes to fall back to direct code reads for per-checkpoint I/O audits — a significant manual overhead.

Existing Phase 2 items retained:
- `.sh` corpus indexing (from 2026-04-16 PROD incident root cause)
- FIELD index ~40 paths undersized
- `route.s3_key` unset on CF-rewrite routes
- SyntaxWarning line 91 `\$` escape fix
- Default-to-short empty output

---

## 8. Open items + next steps

**Active (self-driving):**
- ~D synthesis in flight; will MCP CTO+COO+Andrew on completion.

**Gated on ~D synthesis:**
- COO authors fix-TO wave from `coo_handoff.md`. Expected high-priority fix TOs based on current evidence:
  - `role_aua/` re-backfill post-phantom-fix (C-3 layer-of-origin = C, RA-P1c-style)
  - `nna_atomic/` Apr 14 partition gap close (C-2)
  - NNA-path-split resolution (D_00c+D_02 vs D_04+D_00b+D_01+C_08) — architectural call between re-land-atomic (requires schema expansion to include `aua_current`/`growth`/`client_state`) and unwind-atomic (revert CN-P2/P3)
  - Group D tagged_aua source-of-truth unification (COO's Option A vs Option B architectural call — NOW grounded in 4-checkpoint evidence from ~D's 2A/2E)
  - D_04 override block L2325-2340 disposition
  - `fee_breakdown.no_fee.aua` top-level sweep (post B1.fix miss)
- Andrew review of `SYNTHESIS/coo_handoff.md` before COO fix-TO dispatch.

**Parked / non-blocking:**
- D_04 `comp-validate` path bug (`windows[0].entries` vs `windows.{QTD,YTD,MAX}.entries`) — separate small DS TO. Out of STAUDT scope.
- BDPL_NNA.S1 state-vs-client_state schema-alignment TO (DS drafting from session 32 directive).
- AE SSM d83a1d11 post-run validator evidence logging — completion verified in inbox, session log by AE still pending.
- Cap-timing-rule brief disposition — CTO dispatch MCP 20260417T174410Z pending Andrew reply.
- `silver/ULN/` wiring into production (A-2 artifact not yet consumed).

---

## 9. Compiler Tools (this session)

| Date | Agent | TO | Tool | Command | Result | Note |
|---|---|---|---|---|---|---|
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-build | `comp-build` | PASS | 1,162 nodes / 940 edges, 2.7s |
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-pipescript | `comp-pipescript io D_00c` | PASS | Confirmed reads `CANONICAL_NNA_ATOMIC_PREFIX`, no D_02 reads (9 reads, 0 from D_02) |
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-pipescript | `comp-pipescript io D_02` | PASS | Confirmed reads `CANONICAL_NNA_ATOMIC_PREFIX`, writes `canonical_role_aua_key` → D_01 |
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-pipescript | `comp-pipescript io D_04` | PASS | **Confirmed reads `CANONICAL_NNA_PREFIX`** (NOT atomic) — live schism evidence §2.3 |
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-platinum | `comp-platinum reverse platinum/firm/leaderboard.json` | PASS | Producer D_04, 11 upstream feeders, 3 portal consumers (AdvisorIntelligence, AdvisorsTab, ClientsTab) |
| 2026-04-20 | 1.0.0_SA_CTO | (PRD research) | comp-pipescript | `comp-pipescript io data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | FAIL | Full path rejected — use short ID only |

(Additional comp-* runs in `org/compiler-tools-log.md` auto-appended.)

**Methodology note discovered by ~B and confirmed this session:** `comp-pipescript io` in a scratch worktree reflects workspace-root graph, not worktree-local. Direct source-file reads are the correct fallback for per-checkpoint I/O audits. Promoted to ADHC_ROUTER Phase 2.

---

## 10. Commits this session

| SHA | Author | Description |
|---|---|---|
| `1472d1b7` | 1.0.0_SA_CTO | ADVI_STAUDT PRD v1 + project JSON + REGISTRY row |
| `3f9effe2` | 1.0.0_SA_CTO | §3.3 Group D 14 production sites + function-level compiler-mandate delta |
| `65945fbf` | 1.0.0_SA_CTO | §3.0 two primary failure classes headline + mandatory per-advisor invariants |
| `8dd2f32f` | 1.0.0_SA_CTO | §3.4 Group B + Group C material-change scope (every touched script enumerated) |
| `ec9c7020` | 1.0.0_SA_CTO | §4 layer-scoped decomposition — upstream-first rule-out discipline |
| (COO commits) | 2.0.0_SA_COO | 4 TO authoring + shape rework per CTO review |
| `0d34f025` | 0.4.0_DS_ClientPlatform~A | Layer A findings — silver/A inventory + 3 material + clean-bill |
| `fd857154` | 0.4.0_DS_ClientPlatform~B | Layer B findings — 7 material + 4 clean-bill + methodology finding |
| `b687ff47` | 0.4.0_DS_ClientPlatform~C | Layer C findings — 5 material + 5 clean-bill + C-1 Class 1 path evidence + C-3 role_aua corruption |
