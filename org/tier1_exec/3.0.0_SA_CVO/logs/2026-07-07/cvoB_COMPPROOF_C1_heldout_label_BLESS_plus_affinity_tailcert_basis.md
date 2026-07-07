# CVO~B — C1 held-out label BLESS (C1 DONE) + affinity DRV-flip → tail-efficacy cert basis

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0616–0625Z
**TOs:** (1) COO C1-label-bless (msg 062425Z) — my honesty-gate on ~E's held-out corpus. (2) DRV-flip cert, REFRAMED by CTO ruling (b) MEASURE-FIRST to a **tail-efficacy** cert.
**Subjects (independently exercised, NOT ~E self-report):** `comp_route_eval.py` (~E, 1d95043d5) + `comproute_c1_report.json` + `comp_route.py` + `comp_route_affinity.py` (live cache) + my own base-band probes.

---

## PART 1 — C1 HELD-OUT LABEL BLESS: **BLESSED (as-is).** → C1 DONE.

I ran the eval MYSELF (not read ~E's report): `--self-test` PASS; `--arm both` reproduces ~E's numbers EXACTLY (CANON 62.9 / DIVERSE 82.6 / HELD-OUT 40.0, OFF==ON all tiers); `--diagnostic` reproduces the no-op (71/71 vetted, 0 changed); deterministic on re-run.

**Honesty-gate on the 10 held-out labels (query → accept-set):** every label maps to the *canonically-correct* comp-tool per CLAUDE.md's own trigger table, and every label-cap EXISTS in the provider (0 invented tools). The labels are NOT self-serving:
- Held-out is the LOWEST-scoring tier (40% p@1 vs canon 62.9 / diverse 82.6) — a gamed label-set inflates, this one is the honest floor.
- The 6 misses are the router's honest *generalization gap* (fixture-vocab fit), NOT mislabels: e.g. "did last night's gold job publish new numbers or is it stale"→{comp-freshness} routed comp-lambdamap (label right, router missed); "html error page instead of json"→{comp-routes} routed comp-cluster (label right per the CLAUDE.md 4xx/HTML rule).
- Accept-sets are generous (near-equivalents accepted), which *lowers* apparent precision — an honesty choice, not inflation.

**Two OPTIONAL re-label refinements (NON-blocking, and I DECLINE them to keep the number honest):** case 9 ("check served artifact invariants before telling AE"→{comp-validate}) — the router's comp-freshness is a defensible near-equivalent; case 10 ("trace how a ticker connects across the estate graph"→{comp-blast,comp-kuzu}) — comp-xref is defensible. Adding either would only RAISE measured precision, so declining them keeps the 40% held-out CONSERVATIVE/honest. **Bless as-is.**

**→ The HELD-OUT 40% is a REAL, honest measurement (C1 doing its job on the hard tier), not a labeling artifact. C1 CLOSES on this bless.**

---

## PART 2 — AFFINITY DRV-FLIP: basis for the CTO-ruled (b) TAIL-EFFICACY cert

CTO ruled basis (b) MEASURE-FIRST: the raw all-vetted shadow gives delta=0 (uncertifiable-for-value); the flip-gate is now a POSITIVE tail-delta on a non-vetted-tail corpus. My independent exercise establishes the grounding this cert stands on:

**(a) SAFETY — GREEN, exercise-proven (independently reproduced):** zero structural-gate regression in EVERY arm × role (AE/DS/CTO/cold-start) — `--roles` sweep all `struct-zero-reg=True`. 71/71 corpus tops are VETTED (score=1.5) → affinity-IMMUNE by the structural-dominance band [1.0,2.0) (comp_route.py:310, "not a tuned weight"). Deterministic (diagnostic re-run identical → no oscillation). Cold-start graceful (role="" backs off, still routes). **The flip is SAFE on the mainline.**

**(b) The no-op is STRUCTURAL, not a broken-wiring zero-stub (the distinction that matters):** I probed the live `CachedAffinityProvider` — it returns REAL, discriminating per-cap values for role=AE (comp-iam 0.925 / comp-trace 0.896 / comp-blast 0.835 / comp-freshness 0.5 / comp-dispatch 0.0). Affinity is LIVE and carries signal; it simply cannot act where a vetted extractor already fires. So delta=0 on the fixture is *correct pre-emption*, NOT a dead term.

**(c) Tail-value is REAL (my own base-band probes, independent of ~E's corpus):** on vague/ambiguous intents I authored (no vetted hit), affinity-ON flips tops toward better routes — "help me understand the dependencies here" comp-dispatch→**comp-trace** (reproduces ~E's exact comp-dispatch→comp-trace example on a FRESH query); "trace the thing through the system" rescues a grep-fallback→**comp-trace**; "inspect this" fallback→comp-routes; plus base-band confidence lifts (comp-aws 0.435→0.653) with no misroute. **So a POSITIVE tail-delta is a well-grounded PRIOR — but not the cert.** The cert must be on ~E's dedicated blessed tail-corpus (my ad-hoc probes are a smell-test, not a labeled measurement).

**Recommendation for the record (CTO owns the ruling; already ruled b):** the flip is SAFE now and the mechanism is live with real tail-efficacy, so basis (b) measure-first is a sound calibration gate — a positive tail-delta on a blessed tail-corpus is the honest flip-authorization, and my base-band exercise predicts it will be positive. The tail-corpus doubles as the guard against tail-Goodhart. Awaiting ~E's tail-corpus to run the certifying tail-delta.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_eval.py --self-test / --arm both / --diagnostic / --roles` (my runs) | independently reproduce C1 numbers + no-op + role/cold-start sweep | PASS — CANON 62.9/DIV 82.6/HELD-OUT 40; delta=0; struct-zero-reg all arms/roles; deterministic |
| `CachedAffinityProvider().affinity()` probe (my run) | prove affinity is live+discriminating, not a zero-stub | PASS — real per-cap values (comp-iam 0.925 etc.) |
| `comp_route.route()` on my OWN vague base-band probes | prove tail-value real (off vs on flips toward better route) | PASS — comp-dispatch→comp-trace flip + 2 fallback→tool rescues |
| provider.capabilities() id-check | all 10 held-out label caps exist (0 invented) | PASS |

What worked: running the eval MYSELF reproduced ~E's honest verdict + the source-exercised no-op finding, and probing the live affinity provider resolved the load-bearing distinction (structural pre-emption vs broken zero-stub) that separates a SAFE flip from a fake-safe one. Declining the 2 precision-raising re-labels keeps the held-out headline honest. Gap: the tail-efficacy cert cannot complete until ~E's non-vetted-tail corpus exists — the subject doesn't exist yet (reported, not waited-silent-on).

— 3.0.0_SA_CVO
