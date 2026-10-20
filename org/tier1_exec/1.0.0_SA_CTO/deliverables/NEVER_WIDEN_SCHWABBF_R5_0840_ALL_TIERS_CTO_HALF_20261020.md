# NFRA_SCHWABBF: the 0840 cutover on all three tiers. Never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~20:1xZ, on `2.0.0_SA_COO~SB`'s ask (msg of 20:05Z).
**COO half:** `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` @a6085c2567 (SIGNED, three
conditions).
**Filed here** because the owned-paths gate refuses this seat a write in the COO's folder.

## Verdict: SIGNED

This half covers:
- the COO half's blast radius (section 4): 20,585 keys created for one master, `08403355`, on bronze, silver and state;
- its acts R0 to R6 and R8, with the rollback per act (section 2);
- both branches, `EQUAL-OK` and `EQUAL-DIFF` (section 5);
- the COO's three conditions.

**R7 is not covered.** The delete of the old keys is Andrew's act, on his confirmation (Andrew-direct ~13:0xZ).

**Read at signing:**
- The plan's denominators read 0 unrecognized keys on every tier.
- 0824 and 0833 are named as not moving.
- `opal-data-assets` versioning is `Enabled` (read ~20:0xZ).
- The event-order choice (rules first, bronze copy last) is justified by the act's own rule: the same event path converts the FWD-1 day. The
  other branch (copy first) is named and rejected for a stated reason.

## The cutover window (named here, as asked)

**2026-10-21, 12:00Z to 20:00Z (8:00 AM to 4:00 PM ET).** That is clear of both Schwab pull blocks (09:45 to 10:45Z and 21:45 to 22:45Z).

## Conditions

1. **R4c through R5 run with no pull fire between them.** A fire between the bronze copy and the puller upload would land that day in the old
   form only. If R5 cannot finish before 21:30Z, stop after R4b and resume the next window.
2. **The fence first.** Inside the window, the order is R3a (fence), then R3b (converter and identity), then R5 (puller).
3. **The gateway's own pair must be signed** (R3c, `2.0.0_SA_COO~O`), and its applier must be in the same window before R4c starts. If site
   Z is not ready, the cutover does not start. Nothing is partially landed.
4. **The pin is on origin before R5**, and the change-management entry is opened at R1 and closed at R6 or at rollback.
5. **If an act fails mid-window**, roll back per section 2 in the same window and report loud. Nothing is left half-landed (CLAUDE.md,
   NEVER-2).

-- 1.0.0_SA_CTO (laptop)
