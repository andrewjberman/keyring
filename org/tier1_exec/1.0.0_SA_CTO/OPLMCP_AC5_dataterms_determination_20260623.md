# OPLMCP AC5 -- Claude-for-Work/Enterprise Data-Terms Determination (CTO, 2026-06-23)

**Owner:** 1.0.0_SA_CTO (PRD AC5 / S6 / OPLMCP.05). **Status:** CERT-GO GRANTED (synthetic); PRODUCTION-record PENDING Andrew attestation.

## What AC5 gates
M365 content (mail / files / calendar) crosses to the Anthropic API when a user's Claude reads it through the gateway. PRD S6/S8: this is permitted ONLY under Claude for Work / Enterprise data terms, and the sign-off must be RECORDED before any NON-ANDREW user is onboarded.

## Determination
1. **CERT (CVO AC2) -- GO.** The AC2 per-user-scope cert runs on SYNTHETIC test mailboxes (distinct synthetic A/B content; no real Opal / client / employee data). The cert therefore does NOT egress real sensitive M365 content -> the AC5 real-content-egress concern is NOT triggered by the cert. CVO is CLEARED to run AC2 + AC3 + AC4 one-pass on the synthetic mailboxes. (The synthetic-content design is the deliberate CTO+CVO sidestep so the cert is not blocked on the production attestation.)
2. **PRODUCTION (real non-Andrew onboarding) -- GATED, PENDING.** Before any REAL non-Andrew user reads REAL mail through the gateway, the full AC5 record must hold: (a) Opal's Claude tier CONFIRMED = Work/Enterprise (terms permit M365 content egress); (b) Andrew's attestation / sign-off RECORDED. PENDING Andrew (tier confirm + co-sign). Finalized in OPLMCP.05.

## Holding the line until production-AC5
URL not broadcast + rollout gated on AC2-pass + this production-AC5 record + the global KILL_SWITCH backstop. So no real non-Andrew content egresses before the record is in hand.

-- 1.0.0_SA_CTO, 2026-06-23
