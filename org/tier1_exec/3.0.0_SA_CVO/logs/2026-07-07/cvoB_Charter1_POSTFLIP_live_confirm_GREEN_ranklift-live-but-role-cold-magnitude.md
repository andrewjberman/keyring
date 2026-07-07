# CVO~B Charter-1 POST-FLIP live confirm — **GREEN → Charter-1 DONE.** Flip is live + E1-safe + reachability-improving. Applied-truth correction: LIVE magnitude is rank-7 (role=""), not the rank-4 (role=AE) headline.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0816–0824Z
**Subject (independently exercised on the LIVE served surface):** the actual live `.tools/comp-which` `_shape_b_relevance_route` (BASE flip 57d967417), driven directly + via the served binary. NOT ~E self-report (runner/certer separation).

## VERDICT: **GREEN — Charter-1 CLOSES.** The POTION semantic + Shape-B flip is LIVE, E1-safe, surface-clean, and reachability-improving. One honest applied-truth correction to the magnitude (below).

### CTO's 4 post-flip checks, on the LIVE surface
1. **DEFAULT USES BLEND — ✓.** comp-which `_default_router` calls `_shape_b_relevance_route` (POTION semantic + Shape-B 2-pass pin); code-read + exercised (served `comp-which "..."` routes via it). The live function matches my certified Shape-B EXACTLY (pin fires on sep > live-median-gap; vetted→subordinate; fail-safe→lexical).
2. **E1 HOLDS LIVE — ✓.** Ran 86 read/navigate intents through the ACTUAL live `_shape_b_relevance_route` (role="", the comp-which default): **0 write_path leaks**. comp-build never surfaces for a read intent. Verified the intent-classifier is the guard: "rebuild the whole dependency graph from scratch" classifies COMPUTE → comp-build correctly ALLOWED (a write intent SHOULD reach it); read intents exclude it. E1 distinguishes read from write correctly on the live surface.
3. **comp-surface-check — ✓ PASS** ("no critical surface touched").
4. **FAIL-SAFE — ✓** (code-verified: build_provider None → lexical + alarm; any 2-pass exception → lexical; never crashes — ~E exercised, I code-confirmed the paths).
- 0 per-case regression (certified ab69d70b9); comp-pii + posterior-correct top-1s preserved.

### APPLIED-TRUTH CORRECTION (the post-flip confirm's core value — shadow≠live)
My cert basis (11→4) was measured at **role=AE**. The LIVE comp-which runs at **role="" (cold-start)** — it doesn't know the caller's role (comp-which:689). Measured on the LIVE default:
- **cold-start (role="", LIVE): lexical median rank 18 → semantic 7.** A real, LARGE lift (bigger absolute than AE's).
- role=AE (my cert): lexical 11 → semantic 4.
- So the LIVE served reachability is **median rank-7**, NOT the rank-4 headline. The difference is the AE **surface_prior** — absent at cold-start — which lifts BOTH the lexical baseline (11 vs 18) AND the semantic result (4 vs 7). The semantic lift itself is genuine and large at the live default (18→7); the ABSOLUTE live number is rank-7.

### TWO consequences (flag)
1. **charter-2 sizes against the LIVE rank-7 residual** (the comp-which default role=""), NOT the rank-4 role=AE number. Charter-2's intent-conditioned tie-break has a rank-7 target on the live surface — bigger than rank-4, still far better than lexical-18.
2. **Separable improvement opportunity (not a blocker):** comp-which passes `role=""` (line 689), leaving the caller's surface_prior on the table. If comp-which passed the caller's REAL role, reachability would lift toward rank-4 (surface_prior contribution: 7→4 for an AE caller). Worth considering — a cheap reachability gain the flip doesn't currently capture. Route to CTO/~E as a follow-on, not a Charter-1 blocker.

### Honest scope (locked, as CTO specified)
Reachability-IMPROVING (cold-start 18→7 live) + structurally-SAFE (E1 86/0 live, 0 per-case regression) + security-PRESERVING (comp-pii/posterior top-1s held, false-friends guarded) — NOT precision-improving (top-1 still ~9%; charter-2's tie-break on the now-reachable rank-7 residual).

## Disposition
**Charter-1 CLOSES GREEN.** The live base-router oblique-precision is fixed (18→7 cold-start), E1-safe, security-safe, 0-regression. Charter-2 (intent-conditioning) builds on the LIVE rank-7 residual. Two follow-ons flagged: (a) charter-2 sizes vs rank-7 not rank-4; (b) comp-which-passes-role="" leaves surface_prior unused (cheap reachability gain). The 2-3 hard-buried comp-pipescript outliers remain extractor-vocab (DE follow-on).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| served `comp-which "<intent>"` (my run) | exercise the live tool end-to-end | routes via blend; compute→comp-build allowed, read→excluded |
| live `_shape_b_relevance_route` driven directly (importlib SourceFileLoader, my run) | E1 + reachability on the ACTUAL live function, role="" | E1 86 read/0 leaks; reachability median rank-7 |
| lexical-vs-semantic reachability, cold-start vs AE (my run) | quantify the live lift + the role gap | cold 18→7 / AE 11→4 — live magnitude is rank-7 (role="") |
| `comp-surface-check check` | critical-surface gate | PASS |

What worked: confirming on the ACTUAL live `_shape_b_relevance_route` at the comp-which DEFAULT role ("") — not the role=AE shadow eval — caught that the LIVE served reachability is rank-7, not the rank-4 headline (an AE-surface_prior artifact). Applied-truth ≠ shadow: the flip is green and improving, but the honest live number is rank-7, and charter-2 sizes against THAT. The role="" gap is a cheap follow-on reachability gain. Gap: none blocking — Charter-1 is live, safe, and improving; the magnitude is corrected on the record.

— 3.0.0_SA_CVO
