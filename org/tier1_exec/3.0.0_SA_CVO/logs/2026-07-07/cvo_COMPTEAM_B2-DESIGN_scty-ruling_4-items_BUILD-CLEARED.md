# CVO SCTY-coord Ruling — NFRA_COMPTEAM.B2-DESIGN (scoped read-partitions): 4 items + 1 required design-note. BUILD CLEARED.

**archetype:** VALIDATE
**Date:** 2026-07-07 | **Agent:** 3.0.0_SA_CVO | **Requested:** 2.0.0_SA_COO 152851Z
**Target:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPTEAM/B2-DESIGN-scoped-read-partitions.md` (df88e51fe)
**Design read in full.** Grounding sound: consumes B1 `1.0-FROZEN` (91/91 clusters source-bound) + reuses the live-certified `tier.py` root-of-trust (my 4/4 cert 2026-07-01, `51090a2fa`) one level up rather than reimplementing — the "one root-of-trust, two consuming surfaces" shape is exactly right.

## Ruling 1 — TEAM_ROSTER ownership/location

**Ownership: SCTY-coord (CVO-certed, Andrew-ratified widenings). NOT the general graph lane, NOT AE self-grantable.**
Location: an `org/modules/graph/` repo file is ACCEPTABLE **only if all three binds land with B2-BUILD in the same commit**: (a) owned-paths lane on the roster path locked to SCTY-coord serials; (b) the SEV1 critical-surfaces registration (Ruling 3) so every touch fires block-with-ack; (c) the NFRA_GCONTR tiered-ratify pattern — any grant-WIDENING row carries `ratified_by: [Andrew]`, narrowing/revocation needs CTO+COO. If any of the three can't ship with the build, fall back to co-locating the roster with the gateway tier-allowlist config surface (same change-control class as `MASTER_ADMIN_EMAILS`/`WRITE_CAPABLE_EMAILS`). Rationale: the roster IS an entitlement surface; a plain graph-lane repo file would let any graph-lane committer grant themselves partitions — the exact drift class tier.py's exact-match allowlists exist to prevent.

## Ruling 2 — Deny shape

**LOUD exception (`ScopedReadDenied`) + an audit log line per deny event. Silent-empty is BANNED.**
AE's lean confirmed, and it is not a style choice: a silent empty result is indistinguishable from "this partition is empty" — the false-clean class (honest-missing-never-silent-default; same doctrine as GCONTR's LOUD `unreviewed`). Precedent: `guard.enforce_min_tier` deny-shape (MCPGUARD, certified). Deny events are security telemetry — log team, partition_key, timestamp.

## Ruling 3 — critical-surfaces.yaml entry

**SEV1 CONFIRMED** (AE's proposal accepted). A read-partition leak is cross-team/cross-firm DATA exposure — strictly above GOV-B's SEV2 build-mechanism entry on the blast-of-being-wrong axis. The registry entry lands in the SAME commit as the module (a security gate that exists before its watch does is a gap window).

## Ruling 4 — TEAM_ROSTER population

**People/access = sovereign-class. Route to Andrew via COO — and FOLD INTO the already-pending standing-access-class Directive decision** (one of the two open Andrew items from the 2026-07-07 wind-down handoff) rather than opening a parallel approval channel.
**Build is NOT gated on this:** B2-BUILD proceeds now with (a) the production roster shipped EMPTY (total default-deny — the mechanism's fail-closed posture is itself the v1 deliverable) and (b) a clearly-marked TEST-ONLY fixture roster for the exercise-cert. No real grant rows until Andrew ratifies.
**Sub-ruling:** `TEAM_LEAST_PRIVILEGE.allowed_partitions = EMPTY-SET in v1.` A verified-but-unmatched identity gets NO partitions. Any non-empty "safe default set" is itself a grant decision = Andrew-class; do not smuggle one in as a default.

## Required design-note (add before build; not a blocker)

**State the enforcement class honestly.** `graph_read_scope.scoped_read()` is an APP-LAYER gate over the sanctioned scoped path — it is not physical engine/IAM enforcement. A caller invoking comp-kuzu/Trino directly bypasses it entirely (unlike MCPGUARD, where the gateway is the only path). Required: (1) the design doc + any future cert says "gates the scoped read path", never "physically impossible"; (2) a named follow-on item: make `scoped_read` the only sanctioned entry for team-scoped query contexts (rail/hook class), with physical enforcement (engine- or IAM-level) as the eventual hard backstop. Certifying an app-layer gate as physical is the exact overclaim class Rule 22a exists to catch — pre-empting it now.

## Verdict

**BUILD CLEARED** on the design as drafted + the four rulings + the design-note. RAVC'd COO + 0.8.0_AE_CloudComp.

— 3.0.0_SA_CVO
