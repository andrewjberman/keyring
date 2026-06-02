# ws-charter cycle 0030 — 2026-06-02 1508Z

**Class:** NOVEL (Andrew-direct scoping + handoff)
**Serial:** 1.0.0_SA_CTO (ws CTO, Tier-1)

## Inbox / direction
- Andrew direct: external partner user `peter@inflectionwealth.com` sees the Global(All) Model Portfolios view instead of the firm-scoped Inflection view. Scope it + hand off a doc for COO to decompose + MSTR to spawn agents. → ANDREW_DIRECTION → NOVEL gate satisfied.

## Investigation (grounded, not hand-waved)
Launched an Explore agent on the portal (DEV) auth/tenant/scope resolution + read the code + verified the backend myself:
- **Root cause (single, portal-side, case b):** `portal/src/pages/ModelPortfolios.tsx:257-259` destructures only `isInternal`/`isDev` (never `claims`), defaults `selectedFirmId='global'`; `:696` selector gated to `internal` only → external users pinned to Global(All). Not Inflection-specific — every external partner hits it.
- **Proven in-repo fix pattern:** `AdvisorIntelligence/index.tsx:42` — `const firmId = internal ? selectedFirmId : (claims?.firmId ?? default)`.
- **Backend verified CLEAN (no backend/DE TO):** `opal-users-v2` authoritative base-table record for peter = `firmId: "inflection"` (the email-index GSI is KEYS_ONLY → returns null = projection artifact; avoided that trap by reading the base table via PK/SK). claims.firmId proven to flow end-to-end because AdvisorIntelligence already scopes external Inflection users correctly off it.
- Inflection partner config + per-firm MDPF endpoints already exist + typed. FE-only, ~1 file.

## Action
- Authored scoping brief: `docs/briefs/mdpf-inflection-scoped-modelportfolios-login-scope-fix-20260602.md` (9de86aae3, pushed). Root cause + evidence + fix shape (§5) + decomposition (§6: TO-1 FE primary→0.4.2_RD~B; TO-2 visual smoke gate) + acceptance (§7 AC1-AC5, visual smoke not data-layer) + blast radius (§8).
- HANDOFF → 2.0.0_SA_COO to decompose (broker 20260602T150853Z); COO routes spawn ask to MSTR.
- Flagging the spawn dependency to Andrew directly (he's live).

## Dependencies / spawn surface
- Implementing FE lane (0.4.2_RD_AdvisorIntelligence~B) OFFLINE. This + AE OPS1 (MDPF scheduling) are the two MDPF work-inputs, BOTH gated on MSTR-spawn — MSTR also OFFLINE. Andrew/MSTR-spawn is the gating dependency. Andrew can spawn directly or bring MSTR up.

## Next-cycle expected state
- COO decomposes brief → TO-1/TO-2; MSTR (or Andrew) spawns RD FE lane.
- I review the FE diff + run visual smoke with Andrew before close.
- MDPF close now gated on: (data) DONE/accepted; (scheduling) AE OPS1; (FE-scope) this fix. All three need agent spawns.
