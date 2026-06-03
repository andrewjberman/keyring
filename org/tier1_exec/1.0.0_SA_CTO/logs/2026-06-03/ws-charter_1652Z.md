# ws-charter — 2026-06-03 1652Z — comp-validate NO_CONFIG flip GO'd (ratified condition MET)

**CLASS:** FIX (execution of ratified LD-0148 doctrine; flip authorization).
**Trigger:** DS step-(ii) inventory (`20260603T165106Z`).

## Decisive finding (DS inventory)

**Gate-path (flip-safety) set = EMPTY.** No automated path (safe-deploy.sh / ds-commit-gate.sh / git-hooks / infra/aws/lambda/ci / gold dispatch+runner / EC2 deploy) consumes comp-validate's exit code — grep-confirmed. `prd-evidence-check.sh` references it but is WARN-ONLY (always exit 0) + zero callers. comp-validate's verdict is consumed by AGENT JUDGMENT (DS reads it before signaling AE), not a CI gate.

Exhaustive bucket-count (awareness, not pre-work): ~152 NO_CONFIG — gold ~106/129, silver ~28/29, bronze 18/18. Config stanzas: 18 (BD 12 + INF 6). Waivers: 0.

## RULING — GO the flip, ordered, 2 guardrails

- **Ratified flip-condition (LD-0148: "hold until live-gate NO_CONFIG inventory clean") is MET** — the live-gate set is empty (nothing to clean), zero automated-breakage. MSTR's hold is satisfied by definition.
- **The loud NO_CONFIG message (already shipped 5009155c0/1bb8b7766) is the load-bearing safety fix** — consumer is agent-judgment reading the verdict, so the loud "UNVALIDATED, NOT a pass" already kills the Andrew-named false-green at exit-0. The exit-code flip is correctness-completeness (no NEW safety gain since no exit-code consumer), but we complete it.
- **ORDER (same change):** (a) seed 2-3 exemplar waivers (legit non-validatable gold: debug/diagnostic) — precedent for the escape; (b) COO broadcasts a fabric 1-liner (NO_CONFIG->exit-2, config/waiver/--lenient); (c) flip default; (d) I re-scribe protocol/CLAUDE.md "phased->flipped" on DS confirm.
- **Do NOT pre-clean the ~152** — opportunistic config/waiver at point-of-use is the intended fail-closed (surfaces 82% gold / 97% silver / 100% bronze have no validate coverage = true useful signal). No exact per-id dispositions needed (fuzzy count sufficient).

## Routed

DS (GO + order, 165241Z); COO (announce-line ask + drive-awareness that post-flip exit-2s are expected-not-incidents, 165254Z); MSTR (ratified-condition-MET note, no re-ratify — operational execution of ratified doctrine, 165301Z).

## Follow-on

- DS: exemplar waivers -> ping me for announce line -> flip -> confirm.
- CTO: re-scribe COMP_VALIDATE_PROTOCOL §10/§10.1 + CLAUDE.md "phased/held" -> "default flipped, live {date}" on DS flip-commit confirm.
- Unrelated in-flight: bd full-publish running (bd AC4 served-parity + W2b verify + v2.1.113 render-smoke pending its completion).
- Andrew stack: keep-warm GO · cost-basis a/b · v2.1.114 GO.
