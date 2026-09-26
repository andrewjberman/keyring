# SIGN-OFF (1.0.0_SA_CTO half) -- the bounded admin + internal + Dev UI-walk principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`
blob `1301fcffcda6401269e72f85017ed3a56f7e8e2c` @`d6c195b6dd` (2.0.0_SA_COO~P msg 101153).
**Authority:** Andrew-direct, "Agent on an admin+dev login" (addendum @`e2eae53ae3`).
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~13:2xZ.

## Signed, as the packet reads

**What is created:**
- ONE K1: role admin, firmId opal-capital, userType Dev.
- ONE K1-CRED, read by name.
- K2 lives no more than 60 minutes. The row is deleted and verified, and the refresh token dies with it.

**The radius is stated and accepted:** a superadmin session for its life. That includes every admin and Dev bypass and
the `/auth/admin/*` user write surface. The bound is the interval plus the walker's script, **page reads only**.

**The audit:**
- The committed, scrubbed HAR holds 0 non-GET/HEAD requests outside `/auth/login` and `/auth/refresh`, and 0 requests
  to `/auth/admin/`.
- A before/after user census.
- Branch (d) makes any admin or write request a BLOCKING row, with the same-turn read.

## Added

1. **Disk first.** C: has at least 5 GB free before the login. The last walk lost its HAR to ENOSPC. Write the HAR
   scrubbed in-stream, never to a raw file that needs a later scrub.
2. **What the walk grades.** It is DSGN_IRPTV1 round 5's drain act (analysis @`61cd39d895` section 1): FWD-1's trace,
   round 4's AC4s and round 3's five NOT_EVALUATED. The walk script names each, with the screen that grades it.

## Second half

**4.0.0_SA_CRO**, as for fe8e8d89. P creates nothing until both halves are at HEAD.
