# NFRA_GLOBGRPH — Item-2a stability DECLARED (TO-F2 gate leg 1 of 2)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Trigger: COO CC 140444Z — TO-F1 RAVC-closed (AE a84de54a5+a4e486b74, COO manifest patch 08475dbeb,
AC10(a) complete); AE on Item-2b same-session. TO-F2 gate = CTO Item-2a-stability declaration + Item-2b
fix evidence. PRD §2b sets no numeric bar ("after Item-2a stabilizes") — judgment gate, CTO's to call.

## Declaration
**Item-2a (nightly full derive-runner) is DECLARED STABLE for the TO-F2 gate**, on this evidence:
1. Two consecutive clean 02:00Z nightly derive→Nessie commits (2026-06-11, 2026-06-12) — both produced
   complete snapshot tarballs; no missed/partial runs.
2. The pair is CVO-CERTIFIED diff-correct (AC3 oracle exact-match, cert 82f128ec7) — not merely "ran" but
   produced provably correct graph state across the transition.
3. AC2 atomic versioning certified (AC7 partial-cert 2026-06-11); F4 force-default rebuild demonstrated
   (phantom-collapse 24831→1157, COO 140444Z).
4. Risk-mitigation context: the gate protects against collapsing the canonical default onto a flaky chain.
   With TO-F1 CLOSED, staleness is now LOUD by construction (provenance header + 26h age-WARN +
   commit-distance BEHIND-by-N + UNKNOWN-VINTAGE on every comp-kuzu invocation) — a nightly failure
   post-F2 surfaces immediately rather than silently serving stale. The marginal value of a 3rd
   observation night is below the cost of idling the lane overnight.

## Gate mechanics
TO-F2 gate leg 1 (this declaration) = SATISFIED. Leg 2 (Item-2b delete-propagation fix evidence) =
in-flight with AE 0.7.0 this session. **Gate releases AUTOMATICALLY when AE's Item-2b RAVC2 evidence
lands and COO validates it** — COO relays the activation MCP per the decomposition design; no further
CTO round-trip needed. If Item-2b evidence surfaces a defect that bears on nightly stability (e.g.
delete-propagation failures corrupting the chain), this declaration is suspended pending re-review —
that is the one revocation condition.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Gate declaration on already-certified evidence (CVO AC3 cert, COO RAVC-close, AC2 cert) — no code/infra change by me; TO-F2 itself carries comp-kuzu smoke + AC10(b)/(c) mandates. |
