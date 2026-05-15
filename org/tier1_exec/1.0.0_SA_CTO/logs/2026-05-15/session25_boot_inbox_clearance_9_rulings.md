# Session 25 — Boot + 9-ruling inbox clearance (INFGRO / RUNDATE / OWNPTH.010 / TXNAMG v0.2 / INFDRF / governance)

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-05-15 ~19:30Z..~20:05Z
**Frame:** Boot prompt "1.0.0_SA_CTO. Boot up." → MCP startup surfaced a 23-message inbox (18 + 3 + 2) of CTO-gating rulings + a COO throughput-prioritized 5-item list + 1 mid-session add (ADVI_INFDRF Defect C). Cleared the full decision queue.

---

## Session arc

One contiguous exec-coordination session. Boot startup surfaced ~9 distinct CTO rulings gating ADVI throughput across INFGRO, INFETL/RUNDATE, ADHC_OWNPTH, ADVI_TXNAMG, governance — plus a mid-session add (ADVI_INFDRF Defect C). No PRD authored from scratch; output was architectural rulings + one PRD amendment (TXNAMG v0.2) + a governance-file edit. The `data/smartx/` lane ruling was rendered moot mid-session by an Andrew-direct call — caught via an inbox re-check **before** I edited `.owned-paths.yaml` (the inbox-check-before-landing discipline held).

No CTO-COO architectural divergence; one COO framing was refined (the INFGRO "one bug subsumes" — see ruling 3).

---

## Rulings (chronological)

### 1. RUNDATE-DISPATCH (iii) — ratified
AE 0.7.0 brief `cef13f998`. **Element 2** (reject-incoherent-combination guard) ratified as specified — the actual defect fix. **Element 1**: ruled **Option 1b** (derive date-capability from `{date}`-token presence), NOT 1a (a separate `date_param` catalog column). Reasoning: for a safety guard the classification signal must BE the substitution signal so it cannot fail open — the `{date}` token literally controls substitution, so "step honors --run-date" ≡ "row carries `{date}`" tautologically. A separate column introduces a desync surface (column says capable + token absent → guard passes + substitution silently doesn't happen = exactly the mixed-date run the guard exists to prevent). **§3.4**: YES — add an inf-gold-trigger Lambda hard-refuse of `snapshot_date` for `mode ∈ {full, incremental}` (structurally always-mixed), scoped to those two modes only. Implementation = separate gated TO via COO. MCP to AE 0.7.0 (CC COO).

### 2. ADHC_OWNPTH.010 AC10 — Option (a) ACCEPT
My .010 design sketch's premise — a git `pre-reset` hook, "Git 2.34+" — was **factually wrong**. AE 0.5.0's synthetic-repo Phase-1 probe empirically confirmed no `pre-reset` hook exists in any git version. `reference-transaction` is the only structural hook that fires on `git reset`; it is command-blind; topology (`merge-base --is-ancestor`) is the only discriminator and necessarily catches rebase + amend too. Ruled **(a)**: reframe .010 as a unified destructive-HEAD-move guard — that coverage is correct, matches the TO title verbatim, net-positive. (b) leaky (amend is topologically identical to reset), (c) cultural (a wrapper contradicts ADHC_OWNPTH's own structural-over-cultural thesis) — both rejected. COO rewrites scope-step-1 + AC10. MCP to AE 0.5.0 (CC COO); ACK received (FORCE-RESET→FORCE-HEADMOVE token accepted).

### 3. INFGRO firm_return_pct_twr — window-TWR aggregation defect (COO #1, highest)
Brief: `docs/briefs/infgro-window-twr-aggregation-ruling-20260515.md` (commit `9ca076f15`).
`INF_D_00c._aggregate_gro_{firm,per_advisor}_window` (L606-705) compute an AUA-weighted **arithmetic mean** over all (household × date) in-window rows — not a window TWR. Confirmed by DE 0.4's 3 empirical tells (inverted monotonicity, %-vs-$ inconsistency, return-% uncorrelated with avg_twr_pct). Ruling: a window TWR has **two aggregation axes** — cross-sectional AUA-weighting (correct, keep) + temporal geometric chain-link (the fix; the code averages where it must compound). Phase 0 confirms the grain of `return_pct_twr`; the exact compounding formula is grain-dependent. **Finding A (return_pct_twr, INF_D_00c) explicitly decoupled from Finding B (epsilon-dominance, INF_C_02 + perf-coverage)** — corrected COO's "one bug subsumes" framing: `epsilon_$` is a straight `.sum()` of an INF_C_02 column, so the Axis-2 fix does not touch it; they can only share a root upstream in INF_C_02. Both gate .005 partner-facing. INFGRO.005 HOLD upheld (portal code verified correct, zero rework); .006 gates the same fix.

### 4-6. ADVI_TXNAMG PRD v0.2 — three rulings (commit `1da63834a`)
- **§4.1 RULED UNION** — TO-1 §1.2 found 31,726 of 1,179,785 Custom-Report transaction ids (~2.7%) are on accounts closed before the REST pull date, absent from the REST spine. This is new empirical evidence falsifying the v0.1 "Custom Report ⊂ REST" subset premise. A pure left-join silently drops legitimate transaction history — a business-semantic row filter, which CLAUDE.md Rule 17 prohibits in silver, and counter to Andrew's preservation directive. → TO-7 (DS~D, UNION extension; CR-only rows schema-mapped into canonical camelCase, NOT a NULL-spine concat). Additive — does not reopen shipped TO-3.
- **§4.4 INF_D_02 reclassified** SHIELDED → masked-bronze-fallback. Its `load_buy_lot_acquisitions` path carries the same masked bronze-fallback as INF_D_00; the "8 shielded" count was off by one (7 shielded + 2 masked-fallback). TO-2 shipped (`61ff21102`) without it (identified post-scoping). → TO-8 (DS, low-urgency hygiene). Auto-Rule #6 class miss (a consumer characterized by one of two read sites).
- **fkTradeStatus ratified ALIAS** — TO-1 classified it an encoding variant of REST `status`; CTO ratifies not-carried. TO-3 shipped on this default; no rework.

### 7. ETFS_NETAST governance (commit `cc1604d49`)
`.owned-paths.yaml`: added `etf_netassets_watch/** → POD4`. Path was UNDEFINED — DS~C's `da4931c85` ETF-probe commit needed an audited override. AE 0.7.0's ETFS_NETAST infra work is in `infra/aws/**` (already AE-laned).

### 8. data/smartx/ lane — MOOT
Andrew ruled directly: "smartx (backend) is a 0.5.0_AE lane." AE 0.5.0 applied `data/smartx/** → SHARED_OPAL_ETL` and shipped SXPL_RESTIN.002 (`smartx-v2.2.0`). Dropped from my queue — caught by an inbox re-check before I touched `.owned-paths.yaml`.

### 9. ADVI_INFDRF Defect C — canonical firm client_count (ruled, then AMENDED)
Mid-session COO add (URGENT Inflection live-portal drift, DS~A BE-root-caused). 307 (`accounts_dim`) vs 321 (geo view's `nunique(household)` on a holdings merge). **Initial ruling: 307 canonical** — dedicated dimension > incidental merge-derived count; NOT a product call. One empirical premise pinned for DS~A, with the explicit caveat that if the 14-HH delta were genuine missing clients the ruling inverts.
**AMENDED** (after DS~A's verification): the premise partially inverted. 11 of the 14 confirm it (phantom double-counts), but 3 (households 1353/1366/1367, May-created) are genuinely new clients `accounts_dim` is missing — that artifact is STALE, frozen 2026-04-29 (17 days). A third number, 298, comes from the FRESH `accounts_v2`. Amended ruling: "307 canonical" **WITHDRAWN**; 321 still out (geo phantom-pseudo-household artifact — geo-derivation fix proceeds off a fresh real household mapping); the canonical client_count is **BLOCKED on a dimension-freshness bug** (accounts_dim 04-29 + household_dim 04-28 refresh path frozen); do NOT re-designate `accounts_v2` canonical either (298 < the stale 307 + bidirectional disagreement = its own coverage gap, candidate closed-account exclusion). Re-decide canonical post-freshness-fix; if a real disagreement survives → CTO+Andrew client-definition product call. The pinned-premise discipline worked — the caveat caught the inversion. MCP: amended ruling to DS~A (ACK'd), consolidated to COO.

### 10. ADVI_INFINC.006 — Option A (account-level windowed pull)
DS~D's probes killed both alternative endpoints: firm-level = 11-column bronze-contract gap; client-level = Complete-status-ONLY (drops 144,453 non-Complete rows — all Pending / Reversed / Rejected). The account endpoint accepts date windows (the "no date params" docstring was wrong — 3rd docstring-as-assumption correction in the INFINC arc). Ruled **Option A — account-level windowed pull**: full status fidelity, current schema, zero bronze-contract change, TO-3's shipped amalgamated silver untouched. A Complete-only bronze is a business-semantic row filter at ingestion (Rule-17 family); with the firm-endpoint call-count win dead, Option B (client-level) buys nothing. INFINC.006 stays P2/gravy. (My first reply confirmed client-over-firm before DS~D's 144K finding landed — superseded by the Option-A ruling; crossed-messages clarification sent.)

### 11. RUNDATE-DISPATCH — implementation-TO scope augmentation
AE 0.6.1's ADVI_INFDRF.002 root-cause surfaced that the silver-aggregator (the documented PRIMARY gold-chain trigger) dispatches `--chain full --run-date {date}` and has been FAILING — the system runs on a mis-timed fallback cron with the primary path dead. Architectural call: the RUNDATE-DISPATCH implementation TO must ALSO include the layer-1 aggregator-trigger fix (the aggregator triggers plain `{mode:full}`, no snapshot_date, like the cron) — the guards alone make the primary path fail LOUD, not revive it. Routed to COO as a scope note for the impl TO (AC: "primary aggregator path runs green"). Separately flagged to COO: the accounts_dim/household_dim freshness-freeze (ruling #9) is likely the SAME root as the INF_C_02/C_03 append-only-gate P0 — verify before routing a separate freshness item.

---

## Commits

| Commit | Scope |
|---|---|
| `9ca076f15` | `docs/briefs/infgro-window-twr-aggregation-ruling-20260515.md` (new) |
| `cc1604d49` | `.owned-paths.yaml` — `etf_netassets_watch/** → POD4` |
| `1da63834a` | `docs/architecture/ADVI_TXNAMG.md` — PRD v0.2 |
| (this commit) | session log + CTO dashboard header refresh |

Note: the INFGRO-brief commit hit concurrent index contention twice (AE 0.5.0 SXPL_RESTIN.002 deploy staged files; once a stale `.git/index.lock`) — resolved per CLAUDE.md Rule 14a (`git reset HEAD -- <extras>` is non-destructive; `git commit --only` reads the working tree). `git commit --only` does NOT commit a brand-new untracked file — `git add` is required first.

## Outbound MCP

~14 outbound: COO ×6 (master ruling sweep; INFDRF Defect C; the 3-item consolidated; INFINC/Defect-C/RUNDATE-aggregator; append-gate shared-root connect; "all crossed" confirm). AE 0.7.0 ×1 (RUNDATE ratify). AE 0.5.0 ×1 (OWNPTH.010). DS~D ×3 (TXNAMG fkTradeStatus + §4.1 UNION + INFINC.006 firm/client confirm; INFINC.006 Option A ruling; crossed-messages clarification). DS~A ×2 (INFDRF Defect C initial; amended). DE 0.4 ×1 (INFGRO defect CC). All inbound RAVC loops closed.

## Compiler Tools

No comp-* tools run this session. Reasoning: this was an exec-coordination + ruling session — architectural rulings on TO-scope / PRD decisions, one PRD amendment (TXNAMG v0.2), one governance-file edit (`.owned-paths.yaml`). No gold-script edit, no portal component, no PRD authored from scratch, no 4xx/auth debug — none of the comp-* triggers applied. The INFGRO ruling cited `INF_D_00c` code (L606-705) read directly; the defect is structural-visible (an arithmetic mean), not a graph-trace question. The fix-TOs COO authors (INFGRO, TXNAMG TO-7/TO-8, RUNDATE-DISPATCH impl) carry `comp-pipescript io` mandates per the normal TO protocol.

## Carry-forward

- **COO TO-authoring queue**: INFGRO fix-TO (DS~C, Phase-0-first — the throughput unlock, author first); RUNDATE-DISPATCH impl TO (AE 0.7.0); TXNAMG TO-7 (DS~D, UNION) + TO-8 (DS, INF_D_02); ADHC_OWNPTH.010 scope-step-1 + AC10 rewrite.
- INFGRO.005 + .006 HELD pending the corrected leaderboard.json + DE 0.4 re-validation. Co-lands with ADVI_BIWNDW.002 (one INF chain run, both to DS~C).
- **ADHC_VALGATE PRD v0.1** authoring — still unauthored (carried from sessions 23/24). CTO bandwidth item.
- **ADHC_COMPIL_V4 Task #22 + TO-017** — triggers the 3-step project closure when shipped.
- **ADVI_INFGRO PRD v0.4 amendment** — the window-TWR ruling brief folds into it when that amendment is authored.
- **ADVI_INFDRF Defect C** — canonical client_count re-decided AFTER the dimension-freshness fix; if a real accounts_dim-vs-accounts_v2 disagreement survives, it is a CTO+Andrew client-definition product call. The freshness bug (accounts_dim/household_dim frozen 04-28/29) is likely the same root as the INF_C_02/C_03 append-gate P0 — confirm via the append-gate patch verification before routing a separate item.
- **RUNDATE-DISPATCH impl TO** must carry the layer-1 aggregator-trigger fix (revives the primary gold-chain path) — flagged to COO with a "primary aggregator path runs green" AC.

## Session boundaries

- Started ~19:30Z (boot prompt). Closed ~20:05Z (commits + log).
- Commits authored: `9ca076f15`, `cc1604d49`, `1da63834a` + this log commit.
- Watcher: clean Bash-tool `run_in_background` relaunches after each delivery; ~23 inbox messages cleared across 3 pulls.
