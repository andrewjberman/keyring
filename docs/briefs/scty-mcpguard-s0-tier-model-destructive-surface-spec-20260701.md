# SCTY_MCPGUARD S0 — Tier-Model + Destructive-Surface Spec (for CTO arch-gate)

**Build-lane:** 0.5.0_AE_OpalETL (build-pen) | **Gateway owner-of-record:** 0.7.0_AE_CloudOps | **Call-path:** 0.8.0_AE_CloudComp
**Arch-gate:** 1.0.0_SA_CTO (tier-model FIRST, then S0 registry) | **Live-cert:** 3.0.0_SA_CVO (verifier-not-fixer)
**Chain:** brief c9ab8e986 → CTO fold fd9113e82 → COO GO (SCTY_ONBOARDING_GUARDRAILS_decomposition.md) → this spec
**Status:** DRAFT for CTO arch-gate. NO code lands until (a) CTO gates the tier-model + (b) 0.7.0/0.8.0 confirm the integration point. Grounded against `infra/aws/ec2/m365-mcp-gateway/app/{identity,tools}.py` (Read, 2026-07-01), NOT assumed.

---

## PART A — USER-TYPE TIER MODEL (item 0, CTO arch-gates FIRST)

### A.1 Tiers

| Tier | Identity | Capability posture | MCPGUARD cap/confirm profile |
|---|---|---|---|
| **MASTER-ADMIN / systems** | `andrew@opalinvest.com` (+ an explicit systems/service allowlist, config-pinned) | full delegated envelope (all currently-scoped ops) | exempt from blast-radius CAPS (G1); **NOT exempt from the tier-independent safety invariant — confirm-on-irreversible (G3) still applies** (CTO corollary, fd9113e82) |
| **STANDARD-EMPLOYEE** | any other verified `@opalinvest.com` identity | least-privilege; write only where the role needs it | conservative default caps (G1); confirm-on-destructive (G3); reversibility-first (G4); the OneDrive-stopper posture |
| **READ-ONLY / service-derive** | ingestion/service consumers (e.g. NFRA_MSGRAPH derive, MS_INGEST_BEARER) | **read-only gateway capability at the PERMISSION layer (B2)** — Files.Read.All / Sites.Read.All, never Files.ReadWrite.All → destructive is IMPOSSIBLE, not guard-caught | N/A (no write surface reaches the guard) |

Default for an unrecognized-but-verified identity = **STANDARD-EMPLOYEE** (least-privilege), never master-admin.

### A.2 Identity → tier resolution (THE arch-critical rule — grounded on identity.py)

`tier_resolve(request) -> Tier` consumes the email from `identity.get_user_email(request)` (identity.py:128), which dispatches by `_cfg.IDENTITY_PROVIDER` across 5 providers (identity.py:119-125):

| Provider | Verification | Tier-trustworthy? |
|---|---|---|
| `alb_oidc` | ES256 sig verified vs regional ELB key (identity.py:62) | **YES** |
| `cloudflare` | RS256 sig verified **IFF** `CF_ACCESS_TEAM_DOMAIN`+`CF_ACCESS_AUD` set (identity.py:30, 45) | YES only when JWT-verify is configured; else header-trust → NO |
| `verified_access` | **`verify_signature=False`** — TODO (identity.py:94) | **NO** (this is PREMCP P1b — coupling) |
| `tailscale` | header-trust (`Tailscale-User-Login`) | NO (relies on network isolation only) |
| `header` | raw `X-User-Email`, DEV ONLY (identity.py:113) | **NO — spoofable** |

**THE RULE (fail-closed, the whole model rests on this):** an elevated tier (master-admin OR any write-capable tier) resolves **ONLY** when the active `IDENTITY_PROVIDER` is in the **signature-verified set** = `{alb_oidc, cloudflare-with-JWT-verify-configured, verified_access-AFTER-P1b-lands}`. Under any non-verified provider (`header`, `tailscale`, unconfigured `cloudflare`, pre-P1b `verified_access`), `tier_resolve` **forces every caller to READ-ONLY / most-restricted** (or the gateway refuses to serve write tools) — because a spoofable email claim = a spoofable master-admin. **A master-admin tier keyed off a forgeable `X-User-Email` is the single highest-severity failure of this design; the fail-closed rule prevents it structurally.**

- **Coupling surfaced to CTO:** this binds GAP-1 (tier) to **PREMCP P1b** (VA-signature-verify TODO). If prod runs `verified_access`, master-admin cannot be trusted until P1b lands. **BLOCKER on the live prod `IDENTITY_PROVIDER` value** — asked 0.7.0 (owner) in the sync; the spec's fail-closed rule holds regardless, but the *usable* tier ceiling depends on the live provider.
- master-admin + systems allowlist is **config-pinned** (Secrets/config, not code) so adding a systems identity is an auditable config change, not a deploy.

### A.3 Consumption (one table, two layers)
`tier_resolve` output parametrizes BOTH: (1) MCPGUARD cap/confirm profile in `_run()` (Part B chokepoint); (2) PREMCP per-consumer capability scope (B2 read-only-token selection). One resolver, both layers key off it — no duplicate identity logic.

---

## PART B — S0 DESTRUCTIVE-SURFACE ENUMERATION (item 0b — the `destructive_ops` registry)

### B.1 Grounded tool inventory (tools.py, all 25 @mcp.tool() — Read 2026-07-01)

**Chokepoint (confirmed):** every tool calls `_run(tool, args, fn)` (tools.py:47) → resolves user+token → `fn(token)` → `audit.log_call`. This is the 100%-coverage interception point for G2/G1/G3/G6. *(Pending 0.8.0 confirm: any Graph path that BYPASSES `_run()` — the REST /teams/poll reuse of `poll_addressed_impl`, the ms_ingest `/ms/*` path. A bypass = a guard hole.)*

**READ-ONLY (SAFE — 20 tools, bypass the guard, zero latency on the read path):**
whoami, list_recent_email, search_email, read_email, list_calendar, list_onedrive, search_files, read_file, find_sharepoint_site, list_site_files, read_site_file, read_site_workbook, read_workbook, search_site_files, get_item, get_site_item, list_site_drives, read_document, list_chats, read_chat_messages, list_teams, list_channels, read_channel_messages, poll_addressed_teams_messages.

**MUTATING (5 tools — the ENTIRE current destructive surface):**

| Tool | Graph call | Class | Reversible? | Blast dimension |
|---|---|---|---|---|
| `create_draft` | POST /me/messages (tools.py:123) | write-draft | YES (draft, not sent; deletable) | 1 draft — low |
| `send_email` | POST /me/sendMail (tools.py:140) | **irreversible-send** | **NO** (can't unsend) | # recipients, external domains |
| `reply_email` | POST /me/messages/{id}/reply (tools.py:147) | **irreversible-send** | **NO** | # recipients |
| `send_chat_message` | POST /chats/{id}/messages (tools.py:397) | **irreversible-send** | NO (Teams msg posted) | 1 chat |
| `send_channel_message` | POST /teams/{id}/channels/{id}/messages (tools.py:436) | **irreversible-send** | NO | whole-channel visibility |

### B.2 KEY RECONCILIATION FINDING (PRD §2 vs deployed reality)
The MCPGUARD PRD §2 destructive-surface inventory anticipates **file-delete / overwrite / move / mail-delete / calendar-delete / mailbox-rule** ops. **NONE of these are exposed as tools today** — the current mutating surface is exclusively **send-class** (4 irreversible sends + 1 draft). Consequences:
1. **"Delete the whole OneDrive" (the G1 headline) is NOT reachable via any current tool.** The immediate real risk is **irreversible SENDS** (mass/external email, channel posts) — so **G3 confirm-on-irreversible is the highest-value FIRST guard today**, ahead of G1 blast-cap (which has no delete surface to cap yet).
2. **The latent delete capability lives in the TOKEN, not a tool:** tools.py:282 states the delegated scope includes **Files.ReadWrite.All**. So a *future* delete/overwrite tool — or any path that issues a raw Graph mutation — would inherit write/delete. This is exactly why **B2 (read-only-scope token for read consumers)** + **fail-closed classification** matter: the guard must be correct for the surface that will exist, not just today's. *(Pending 0.7.0 confirm of the exact live token scope.)*

### B.3 The `destructive_ops` registry (build artifact) + fail-closed default
Each tool tagged `{class, mutating: bool, reversible: bool, native_undo, blast_dimensions[], irreversible: bool}`. The 20 reads → `SAFE`. The 5 mutating → tagged per B.1. **FAIL-CLOSED DEFAULT (CTO arch-gate (b)): any tool NOT present in the registry is treated as DESTRUCTIVE-until-classified** — so a newly-added write tool (the future delete tool) cannot slip past the guard unclassified. G2 reads this registry at `_run()` entry; SAFE → pass-through; mutating/unknown → route to G1/G3/G4/G6 by tag.

---

## PART C — sequencing + gates (what lands after this spec is gated)

1. **CTO arch-gates Part A (tier-model) FIRST** — esp. the A.2 fail-closed rule + the P1b coupling. → then Part B registry.
2. **0.7.0 confirms** integration point (`_run()`), live `IDENTITY_PROVIDER`, live token scope. **0.8.0 confirms** no `_run()`-bypass path.
3. Then build order (each CTO-gate at implementable + CVO live-cert): tier_resolve → G2 classify (registry) → **G3 confirm-on-irreversible** (highest-value given the send-only surface) → G1 blast-cap (guards the future delete surface + mass-recipient sends) → G4 reversibility-first → G6 audit/alert. Then PREMCP A1 (revocation) + B2 (read-only-scope).
4. CVO live-cert bar: an actual over-threshold/irreversible call is REJECTED/confirmed on the running gateway; a read-only-scoped token actually CANNOT write — proven live, not asserted.

**Open items → RAVC:** 0.7.0/0.8.0 sync answers (fired 171204Z/171214Z); CTO arch-gate on Part A. This spec touches NO live path — it is design only.

*Grounded 2026-07-01 against identity.py + tools.py (Read). Author: 0.5.0_AE_OpalETL (build-pen). Gateway owner-of-record: 0.7.0_AE_CloudOps.*
