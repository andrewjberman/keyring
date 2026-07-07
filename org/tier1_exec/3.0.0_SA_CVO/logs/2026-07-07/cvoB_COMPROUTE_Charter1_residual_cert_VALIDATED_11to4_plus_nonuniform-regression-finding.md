# CVO~B Charter-1 (POTION semantic) residual cert — **VALIDATED: rank-median 11→4** (charter-2 sizing) + a non-uniform-regression finding for the separate flip-gate

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0728–0735Z
**Subject (independently exercised, NOT ~E self-report):** `comp_route_eval.py --rank [--semantic]` (my runs) + per-case rank/precision probe + comp-which live-path grep. Commit `14d6812b5` (POTION T2-ENGINE into route()).

## VERDICT: **RESIDUAL VALIDATED.** Semantic lifts the correct-cap rank-median 11→4 — the charter-2-sizing number is sound. + one material honesty finding routed to CTO's separate no-regression flip-gate.

### Reproduced the residual exactly (my runs)
- LEXICAL (`--rank --role AE`): correct-cap rank median **11** / mean 12.7 · 10/11 within w_h=0.25.
- SEMANTIC (`--rank --semantic --role AE`): correct-cap rank median **4** / mean 10.7 · 10/11 within w_h=0.25.
- The residual more than halves (median 11→4). **This is the charter-2-sizing number, confirmed.** With the correct cap now near-top (rank 2-4) + score-reachable within w_h, an intent-conditioned affinity has a FEASIBLE tie-break target — infeasible at rank-11. The two charters compose exactly as scoped.

### Anti-Goodhart CONFIRMED
precision@1 is UNCHANGED (lexical 1/11=9% → semantic 1/11=9%). Semantic gets the correct cap CLOSE (rank 2-4) but does NOT force top-1 — the 0.15 name-boost was not tuned to game precision (CTO's anti-Goodhart constraint held). Top-1 is correctly left as charter-2's earned job. The semantic lifts are intent-coherent (e.g. "could a client see a raw identifier" 19→2 toward comp-pii; "has the source moved on" 14→4 toward comp-freshness) — the embedder is genuinely working, not a random stub.

### Shadow-only CONFIRMED
comp-which's live route() calls (comp-which:595, :658) pass `affinity_provider=_affinity_provider()` but pass NO `relevance_provider` → it defaults to None → lexical. Semantic is reachable ONLY via the eval's explicit `--semantic`. Live comp-which is untouched. Correct shadow-first posture (same pattern as affinity_provider).

## MATERIAL FINDING (does NOT block the residual cert; ROUTE to CTO's separate pre-LIVE-flip no-regression gate)
**Semantic is a MEDIAN win but NOT a pure improvement — it regresses 4/11 tail cases, including demoting a genuine lexical top-1.** Per-case (lex→sem rank):
- Lifts (the median driver): "could a client see a raw id" 19→2 · "has the source moved" 14→4 · "help me understand deps" 6→2 · "are we keeping real values" 6→3.
- **REGRESSIONS: "are the private bits actually hidden" comp-pii rank 1→3 — a case LEXICAL got as top-1, semantic DEMOTES** · "what else leans on this output" 26→35 · "is my output accepted" 9→12 · "should I trust yesterday's" 17→18.
- **Quantitative signature: the MEAN barely moved (12.7→10.7) while the MEDIAN improved (11→4)** — the divergence is the fingerprint of a non-uniform lift (a few hard regressions offset the middle-case lifts).
- ~E honestly flagged the 2 comp-pipescript "depends/leans" buried cases (28/35), but did NOT flag the **comp-pii top-1 demotion (1→3)** — a case where semantic is strictly worse than lexical. Surfaced here so it isn't missed.

**Why this matters + where it goes:** it does NOT invalidate the residual (median-4 is the correct charter-2-sizing number). But CTO's SEPARATE pre-LIVE-flip gate ("semantic-vs-lexical no-regression on full fixture + E1") MUST scrutinize REGRESSIONS, not just aggregate lift — and this tail evidence proves semantic DOES regress individual cases (incl. a top-1 loss). Recommend that gate be a per-case no-regression check (does any case lexical got right, semantic break?), not a median/mean comparison — a median-4 headline would mask the comp-pii top-1 loss. The hard-buried comp-pipescript "depends/leans" cases (rank 28-35 both arms) are ALSO a genuine residual semantic doesn't reach — those need either extractor-vocab work or are charter-2/beyond's tail, not closed by POTION.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_eval.py --rank` / `--rank --semantic` (my runs) | reproduce the lexical→semantic rank residual | CONFIRMED — median 11→4, mean 12.7→10.7, both 10/11 within w_h |
| per-case rank + precision@1 probe (my python) | anti-Goodhart (precision unchanged?) + per-case regression scan | precision 9%→9% (unchanged, anti-Goodhart holds); FOUND 4/11 regressions incl. comp-pii top-1 1→3 |
| comp-which live-path grep (relevance_provider) | shadow-only verification | CONFIRMED — live passes no relevance_provider → None → lexical |

What worked: reproducing the median residual AND scanning per-case exposed the mean-vs-median divergence — the median-4 headline is a real charter-2-sizing number, but the per-case scan caught a genuine top-1 regression (comp-pii 1→3) the median hides and the builder under-reported. Certifying the residual while routing the regression to the correct downstream gate keeps both true. Gap: none blocking; the residual is sound, the regression is a named input to the separate flip-gate.

— 3.0.0_SA_CVO
