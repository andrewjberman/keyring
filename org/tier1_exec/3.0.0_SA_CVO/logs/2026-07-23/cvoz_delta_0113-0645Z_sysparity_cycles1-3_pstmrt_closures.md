# CVO~Z delta log — SYSPARITY ticks 1–13 (three full cycles) + PSTMRT s.7-i1 closure arc

**archetype:** VALIDATE
**Serial:** `3.0.0_SA_CVO~Z` · **Window:** 2026-07-23 0113–0645Z · continues `cvoz_session_0047-0056Z`

## NFRA_PSTMRT (after the first log)

s.7-i1 went through TWO full verify→adopt→re-verify cycles, both clean, then a third contested
round: CTO~Z's RE-GROUND ask on F3 (live firmAccess.ts disagreed with the comp-constants
canonical). Adjudicated on both planes: firmAccess.ts values are ANDREW RULINGS (portal
@4d08170c 05-28, @21f2178d 06-29); the canonical froze pre-ruling placeholders; auth plane has
NO domain primitive (per-email DDB allowlists, 4 tables / 23 rows all read) so ONE field
suffices. My own original F3 verdict had bound to the stale canonical — corrected on the record
(same vintage class as CTO~Z's F1; symmetric ownership). Amendment @d5e69c8cc re-verified
verbatim-clean. **s.7 item 1 FULLY CLOSED @03f4de5da.** Items 2–4 build-gated. Residuals routed:
comp-constants re-canonization → 0.8.0; stale allowlist rows incl. user@cottonwood.com
(Rule-23-adjacent) → main CTO via CTO~Z.

## SYSPARITY loop (cron 952ef5bb, 13 ticks, 3 complete 4-domain cycles — ALL AT PARITY)

| Tick | Domain | Verdict + exercised evidence |
|---|---|---|
| 1 | sweep | NEW finding: untracked `sdk/tenants/acme/` carried evidence for tracked CONFIRMED verdicts → routed 0.8.0, landed @07fefc060, re-verified (15/15, citations at vintage) — CLOSED same-hour |
| 2 | comp-tools | registration invariant PASS 63/63 tools, 84/84 ledger (comp-manifest-check live) |
| 3 | infra | graph-infra claim falsified-then-restored BY EXERCISE: dead legacy-mode kuzu rebuild winner (~0222Z, empty lock) → 900s backstop steal exercised → pin==HEAD restored 0245Z. NO defect; honest served-stale header + backstop + large-delta gate all behaved per design |
| 4 | eng+loops | 1/1 MATERIALIZED recognizer, cross-manifest consistent (near-miss: wrong-manifest axis caught by Law-6). code_heat 144h observation → 0.8.0: dispositioned NEVER-SCHEDULED (dev-box producer, no scheduler; rides open Andrew/CTO nightly-full pattern decision as instance #2) |
| 5 | ontology | drift-gate RULE_BANK coverage MUTANT-PROVEN (touch → STALE rc2 → regen → CURRENT rc0; LD-0314 hole closed AND exercised); cse_schema 0.5 == live import. 06 regen @dfdb7b017 |
| 6 | comp-tools | comp-which routing 3/3 (2 rank-1 + 1 honest near-tie with tied-banner) |
| 7 | infra | FEDOBS artifact 7/7 measures; warrant SHA spot-resolves as real portal commit (8-of-45 sample carrier noted) |
| 8 | eng+loops | audit-archive MINT PATH exercised for real: due-window fired, snapshot @618821137 + baseline @09ac016fd, author resolved via LD-0290 serial file, pushed |
| 9 | ontology | rule-bank/catalog label coherence 6/6 EXACT both directions; registry_binding correctly absent = clean pre-P2 baseline |
| 10 | comp-tools | auto-log control exercised (+1 append / dedupe correct / attribution beats foreign .agent_context). NEW Law-11 instance: log's LOCAL date column false-undercounted my own verify → 0.8.0 fixed same-hour @cd8a728fa (Z-suffixed self-labeling stamps), re-verified source+live — CLOSED |
| 11 | infra | pin==HEAD held unattended (tick-3 recovery durable); two-producer pattern live; cadenced tables in bounds |
| 12 | eng+loops | never-rules gate battery 67/67 incl. real-DENY bite-tests + F-020 audit-log integrity |
| 13 | ontology | consumer-exercised: summary_corpus._load_variance_catalog() returns dims{firm} + the 6 coherent labels — the pre-P2 zero-diff baseline THROUGH the live consumer |

Standing observations (no action owed by me): graph_contracts 875h no-declared-cadence;
FEDOBS artifact restates integrity claim whose SHA evidence lives one hop away (sample 8/45).

## Compiler Tools

comp-system --check (every tick, all CURRENT; 2 regens committed @529f7f6b5 @dfdb7b017) ·
comp-manifest-check (63/63) · comp-kuzu ×4 (incl. the backstop-steal exercise) · comp-which ×4 ·
comp-glob/comp-grep throughout (on-rails) · never-rules test battery 67/67 · audit-archive-invoker
(minted @618821137). Gap found + fixed by 0.8.0: comp_log_auto LOCAL date stamp (@cd8a728fa).

## Open

1. SYSPARITY loop continues (rotation restarts comp-tools).
2. PSTMRT s.7 items 2–4 on build lands (0.8.0 gates + P2 YAML) — pre-P2 baselines banked (ticks 9, 13).
3. Content-eval answer key: Andrew+~Z joint review (queued at Andrew's word).
