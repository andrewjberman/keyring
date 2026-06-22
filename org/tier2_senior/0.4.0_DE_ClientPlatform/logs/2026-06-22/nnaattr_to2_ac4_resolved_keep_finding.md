# NNA.TO-2 AC4 RESOLVED -- override RETAINED load-bearing + P2 finding routed (delta since 7e0c8681b)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Agent:** 0.4.0_DE_ClientPlatform · **Window:** 2026-06-22 ~13:40Z (delta since the W3-OFC verify log `7e0c8681b`) · **TO:** ADVI_NNAATTR.TO-2 · Portal DEV commit `c02809b6`, 1 portal commit, ~2 significant MCP.

## Current State
The AC4 (c) totals-equality verdict I requested from CVO landed (`134012Z`) -- resolving the one held item on my TO-2 DE-leg. DE producer-leg now verified-COMPLETE.

**AC4 verdict: DIVERGENT -> KEEP the INFMVP.F5 override (load-bearing). Do NOT remove.** CVO ground-truthed both served artifacts (gzip-decoded, 49financial):
- Legacy `partner_analytics_quarterly.json` views.nna['current'].adv.donut = "NNA by Architect", 54 segments, total 102,458,685.37 == EXACTLY canonical firm QTD nna -> ARCHITECT-scoped + ADDITIVE (Sigma segments == firm).
- Canonical `advisor_nna_canonical.json` advisors[adv].windows.QTD.nna = ALL-ROLES + NON-ADDITIVE (Sigma advisors = 405.8M; reconciliation.advisors_additive=false by F-1a design).
- Population: 52 advisors both, 49 DIVERGENT / 3 EQ (pure-architect). Per-advisor delta = exactly the non-architect role credit (Travis 6.81M arch vs 8.90M all-roles; Tim Rodgers 17.84M vs 31.10M).
- MECHANISM (why load-bearing): the override (DistributionTab ~L2601-2611, sets seg value/aua = w.nna) is what makes the ADV donut show ALL-ROLES canonical per advisor instead of ARCHITECT-only legacy. That IS the F-1 cross-route unification at the donut layer. Remove it -> donut reverts to architect-scope -> re-opens the per-advisor route divergence ADVI_NNAATTR exists to fix.

**Action taken:** upgraded the `b24cd040` deferral comment -> RETAINED-load-bearing (portal DEV `c02809b6`): documents the DIVERGENT verdict + the mechanism + logs the P2 finding inline. `tsc --noEmit` clean; comment-only (10/6 within the block).

**P2 FINDING (routed to COO; CVO flagged for me+CTO -- NOT my build):** the override injects ALL-ROLES (non-additive ~405M) values into a donut whose declared whole is ARCHITECT-additive (102.5M) -> parts-don't-sum-to-whole representational tension (F-1a non-additivity surfacing in a parts-of-whole widget). The FE override is the correct STOPGAP; the clean fix is DATA-layer (DS/AE): migrate the partner_analytics views.nna.adv donut SOURCE to emit canonical all-roles + decide whole-semantics, retiring the override. RAVC2'd to COO to decompose a DS/AE refactor TO.

**TO-2 DE-leg vs ACs:** 1 (read canonical) DONE; 2 (cross-route identity served) VERIFIED to the cent by CVO #9 independent re-derive; 3 (Continuous 60%-loss) FIXED (CVO clarified it's the cumulative_chart path, already landed P2.W2; donut total reconciles to the cent); 4 (override) RETAINED-load-bearing per the outcome-gated DIVERGENT resolution (correct disposition, not a miss); 5 (F-3 fee-split) DONE; 6 (vocab/labels) DONE; 7 (log+RAVC2) DONE. CVO confirms all other #9 legs PASS -> producer-leg #9-clear.

## Blockers
None. TO-2 DE-leg done + #9-clear. Project close = COO lane (gated on DS TO-1 re-verify + formal CVO #9 re-cert). P2-1 still event-pending on AE0.7 P2-2.

## Next Steps
- **[2.0.0_SA_COO]** decompose the P2 DS/AE donut-source-migration refactor TO; flip TO-2 + project close on DS TO-1 re-verify + CVO #9 re-cert.
- **[0.4.0_DE]** fire my TO-2 producer-side served-verify on DS TO-1 re-verify; P2-1 close-verify on AE0.7 P2-2 materialize. Event-driven.

## Compiler Tools
None NEW this delta (verdict-resolution + comment-upgrade; the live-graph + transform checks are in `7e0c8681b`). `bunx tsc --noEmit -p tsconfig.app.json` re-run on the comment edit -> exit 0 (the only gate a comment-only portal commit owes). No comp tool answers a "verdict-accept + doc-upgrade" step.

## MCP traffic (this window)
~2 significant: CVO AC4 verdict received (`134012Z` -- DIVERGENT/KEEP+finding) -> my RAVC-close accept to CVO (`134317Z`); RAVC2 to COO (`134327Z` -- DE-leg complete + P2 refactor to queue).
