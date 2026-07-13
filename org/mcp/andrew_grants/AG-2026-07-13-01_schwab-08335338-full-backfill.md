---
grant_id: AG-2026-07-13-01
status: ACTIVE            # ACTIVE | EXPIRED | REVOKED | ONE_SHOT_CONSUMED
granted_by: Andrew
channels: ["in-channel via 2.0.0_SA_COO (033805Z/034102Z)", "Andrew at terminal"]
recorded_by: 0.0.0_AB_MSTR
recorded_at: 2026-07-13T04:12Z
scope_surfaces: ["s3://opal-data-schwab/backfill/08335338/*"]
scope_actions: ["schwab-sdd-rest-pull", "s3-write", "iam-apply-for-backfill"]
scope_firms: ["schwab"]
executing_agents: ["0.7.0_AE_CloudOps"]
expiry: on-completion     # ISO date | on-completion | one-shot
---
# Andrew Grant AG-2026-07-13-01 — Schwab 08335338 Full Backfill (OPAL_ASSETS P1/G3a)

**status:** ACTIVE
**recorded_by:** 0.0.0_AB_MSTR (Andrew-hub / MSTR ledger-write role, phantom-consent gate P-2)
**recorded_at:** 2026-07-13T~04:12Z
**executing_agent:** 0.7.0_AE_CloudOps (commit `43e8dbb3a`; NEVER#6 ledger `69983008e` HELD → AUTHORIZED-EXECUTING)

## Authorized action
Full backfill of **Schwab master account 08335338** via the SDD/REST pull — all file types (RPS/CBUGL/UPT/UPN/RLD/ULN/ULT/ACC/TRN/…), depth **2023-07-12 → present**, monthly-chunked, resumable from manifest. Writes to **`opal-data-schwab/backfill/08335338/` ONLY** (firm-separated; NO bd/cot cross-touch). The 85 tcf files already landed are **KEPT** (Andrew: keep + continue).

## Scope boundary (what this grant does NOT cover — re-grant required)
- **2021 pre-REST depth** — a separate Schwab SDD historical egress; needs a DISTINCT Andrew grant.
- **Served-output cutover (OPAL_ASSETS P2)** — still requires never-widen co-sign (NEVER#2) + NEVER#4 served verification.
- Any 08335338 write outside the `backfill/` prefix.

## Andrew authorization (verbatim, grounded — Rule 22 for authorization)
- **2026-07-13T~03:38Z**, Andrew in-channel to `2.0.0_SA_COO` (relayed 033805Z): *"no that was my real input, i wanted the full backfill."*
- **2026-07-13**, Andrew at terminal to the P0-A lane: *"run it."*
- **Session-opening turn** (0.7.0 headless session), later corroborated by Andrew above as his real input: *"we are definitely going to need to do a full backfill of all schwab files from the 0833 account."*
- **channel:** Andrew direct in-channel (COO relay) + Andrew at terminal; corroborated interactively 033805Z / 034102Z.

## Provenance note (why this grant exists)
This backfill was initially EXECUTED on an UNCORROBORABLE session-opening instruction (85 tcf landed) → HALTED on MSTR/COO sovereign-scope flag → HELD pending corroboration (not purged) → **AUTHORIZED** by Andrew's direct in-channel confirmation above. The hold-pending-corroboration process (never execute-on-faith, never auto-purge) is the doctrine this grant + gate seed. This is the FIRST entry in `org/mcp/andrew_grants/` (phantom-consent gate P-2 bootstrap; canonical schema pending CTO's P-3 wiring — conform on request).

## Expiry
On backfill completion (~21k files ground-true count vs estimate, monthly-chunked). Re-grant required for any 08335338 write beyond this scope.
