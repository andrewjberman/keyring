# SIGN-OFF (1.0.0_SA_CTO half) -- the bounded Opal-class walk principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_WALK_PRINCIPAL_20260926.md`
blob `fe8e8d8979727c07cf6bbf469640314cc9045d7b` @`87c1396686` (2.0.0_SA_COO~P msg 101081).
**Authority:** Andrew-direct ~02:1xZ, "have an agent do those walks and record HAR" (@`37025a10e9`).
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~02:4xZ.

## Signed, as the packet reads

**What is created:**
- ONE `opal-users-v2` PROFILE item (K1): role `user`, firmId `opal-capital`, no userType, no MFA, no member row.
- ONE SSM SecureString (K1-CRED), read by name only.

**Who acts:**
- 2.0.0_SA_COO~P creates it, then deletes it and verifies the deletion.
- 2.0.0_SA_COO~D walks, inside 60 minutes.
- The last access token dies within 15 minutes of the delete.

**The walker's script, the only acts allowed:**
- the page reads;
- the 49F retry;
- Purfeerst's Performance, the armed one-use Orion call, which the gate refuses a second time;
- ONE upload of `aapl-vnq-12.03.csv`.

No export, no second vendor call, no grant or admin act.

**The HAR** is committed with credentials scrubbed (password, Authorization headers, cookies, token values). The
branches (a)/(b)/(c) and the sequence 1-8 stand as written, all before 2026-09-26T12:00Z.

## Blast radius accepted, stated

For the interval, the principal holds an internal Opal user's read reach across every firm. The bound is the interval
plus the walker's script, not the grant, and the committed HAR proves the script. That is the reach Andrew's own login
holds, and it is the only class that reaches all three acts he delegated.

## Added

- **K1-CRED key:** the SecureString uses aws/ssm or a scoped key. Its name and interval go in the ledger; its value
  never does.
- **Delete failure:** if any delete is refused, branch (c) runs the same turn: `status=disabled`, then escalate to
  the CTO and Andrew.

## Second half

**4.0.0_SA_CRO**, which is not in the act. The CRO signs on the same blob. P creates nothing until both halves are at
HEAD.
