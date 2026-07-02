# NFRA_AGENTBUS.S1 — 5-control cross-principal security-model DESIGN SPEC (authored in the ETL-standby gap)

**archetype:** IMPLEMENT
**secondary_archetypes:** SCRIBE

**Workspace CLOUD commit:** `4aa59029f` (docs/briefs/nfra_agentbus_s1_security_model_spec_DRAFT_20260702.md + TO flip)
**Trigger:** COO~B GO (20260702T170633Z, LD-0239) — S1 authorized, ETL-priority-sequenced. Authored in the inf ETL-standby gap (base COO + COO~B both blessed light S1 prep in the gap; drop-on-republish-ping preserved).

## Current State

Delivered the S1 security-model DESIGN SPEC — the load-bearing design gating S2-S4. Design-only (no live wiring / no two-fleet activation; fenced for a separate Directive). Arch-gate routed to CTO (his 5-control arch-gate = S1 acceptance + S2-S4 unlock). TO flipped staged->pending.

### The spec (all 5 controls fail-closed, bound to REAL interfaces, one broker-adapter choke point)
- **C1** IAM/KMS per-employee partition (queue-pair per collab, per-collab KMS, default-deny queue-policy) — S2 builds; live G2 test.
- **C2** action-vs-data authz, LAYERED: SCTY_PREMCP entitlement (WHO may act) + SCTY_MCPGUARD user-type tier (HOW MUCH/HOW SAFELY); unset classification -> fail-closed-as-action; DATA-share = read-only-by-construction.
- **C3** signed attribution off the COMPTEAM sig-verified root-of-trust; absent/forged -> REJECT.
- **C4** egress strip reusing the COMPTEAM strip-list, applied BEFORE SendMessage; hit -> redact/block.
- **C5** propose-only default; mutation only via the C2 path.
- Composition WHO(1+3)/WHAT-LEAVES(4)/WHAT-RECEIVER-MAY-DO(2+5) + fail-closed OUTBOUND/INBOUND ordering; intra-fleet opal-agent-comms path UNCHANGED (grounded: server.py send_message/check_inbox + inbox/, port 7800).
- Interface-bindings table + a SEQUENCING FLAG (S3 adapter BUILD depends on the C2/C3/C4 IMPLEMENTATIONS landing — MCPGUARD/PREMCP/COMPTEAM) + 4 open CTO arch-gate Qs (SS11).

### Lane note
docs/architecture/ is ANY_CTO (owned-paths block hit on first commit) — so the spec is homed as a DE-authored DRAFT in docs/briefs/; CTO promotes to docs/architecture/ on arch-gate acceptance (the same author-vs-land pattern as P2-3 comp-cluster).

## Decisions Made
- Authored in the ETL-standby gap only because the inf re-publish is a LONG-window event (full 63-step chain re-run; base COO ETA ~17:35Z) — a genuine productive-idle window, both COOs blessed it, and I stayed drop-ready (Monitor + periodic inf-state re-check).
- Designed against the SPECIFIED interfaces; invented none. Flagged the impl-availability sequencing dependency rather than assume it.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| `comp-which` (locate SCTY/COMPTEAM interfaces) | routed | posterior-router near-miss; read the 4 dep PRDs directly |
| `comp-grep` (interface extraction on the 3 dep PRDs) | grounded | MCPGUARD tier-model, PREMCP RS256 token, COMPTEAM sig-root + strip-list |
| `comp-grep` (broker choke-point, server.py) | grounded | intra-fleet path (send_message/check_inbox + inbox/, 7800) UNCHANGED — extend-not-replace |
| non-ASCII gate (spec artifact) | clean after fix | converted em-dashes + the `in`-set symbol to ASCII |
| `safe-commit.sh` | PASS (after relocate) | surface-check OK -> 4aa59029f |

Phase-2 note: comp-iam/comp-routes LIVE review is design-stage-N/A (the SQS/adapter/IAM don't exist yet — S2/S3 builds); the single-choke-point composition is asserted in the spec (SS7); live IAM/route verification is S2/S4's job.

## Next Steps
- **[1.0.0_SA_CTO]** arch-gate the 5-control model (= S1 acceptance + S2-S4 unlock); rule the 4 open Qs (strip redact-vs-block, receiver-adjudication shape, signature primitive, collaboration-lifecycle owner).
- **[2.0.0_SA_COO (SCTY lane)]** coordinate the C2 PREMCP-token shape + MCPGUARD tier-gate API when SCTY firms up; S3 sequences after those land.
- **[0.4.0_DE, me]** PREEMPTIVE: the inf re-publish (~17:35Z) drops S1 — close the serving loop on base COO's sentinel ping. Then: re-design any CTO-redlined control; align S3 call-sites to the real SCTY interfaces when they land.
