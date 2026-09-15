# ANDREW-DIRECT 2026-09-15 ~07:4xZ -- merge the portal and promote once site Z proves ASTTAX on a real ad-hoc pull

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal, mid-turn during /govern cycle 2's follow-up ·
**Recorded:** the same turn it was given.

## VERBATIM AND ENTIRE

> "Take care with merging portal, i think it's probably gonna be good just confirm that they do a real ad hoc pull and
> they data presents properly on Asttax. If sitez can probably nail it on asttax we merge and promote"

(Given in answer to this seat's cycle-2 report: "Not yet. ASTTAX isn't done, and both of your prod-deploy conditions
still fail.")

## WHAT IT SETTLES

1. **The merge and the promote are authorized, on one condition he names:** site Z runs a REAL ad-hoc pull on
   POSN_ASTTAX (a live data run, not a re-read of an already-built date and not a code-only check), and the data then
   PRESENTS PROPERLY on ASTTAX. That is his condition 1 of ~04:4xZ, made concrete: the Holdings Breakdown shows the
   Cottonwood Satellite data with no floating numbers and no missing Characteristics or Performance.
2. **"Take care with merging portal":** the merge runs the full /integrate protocol (per-hunk base ranges, pick versus
   union, one resolution agreed over the bus before either side merges), not a fast merge.
3. **"we merge and promote":** read as covering the acts the merge and promote require: the CLOUD push, the
   CLOUD<->SITEZ merge, the portal reconcile, lifting the portal freeze, and the /prod-deploy. These were held on his
   explicit word at ~02:4xZ ("ill let you know when to push + Call 4 Merge I will let you know as well"); this is that
   word, conditioned.

## WHAT IT DOES NOT SETTLE, AND HOW THIS SEAT READS IT NARROWLY

- **Condition 2 still binds.** His ~04:4xZ word, "Investor Reporting must remain Opal Admin gated, no clients are allowed
  to see that", is not withdrawn by this message. The most restrictive reading holds: the promote also waits for the
  Opal-admin gate (IRPT_FNTEND round 8, FE-s-49) to land on portal DEV and read correctly on the merged tree. At 07:41Z
  FE-s-49 is `pending`, and DEV `src/App.tsx:421` and `:573` still carry the ungated routes.
- **The proof is site Z's to produce.** Site Z owns POSN_ASTTAX; this seat asks, it does not run the pull. Site Z
  names the instrument and the vintage (its stated plan: a served platinum characteristics.json read plus a render of
  the Satellites HoldingsTab).
- **/prod-deploy is DT-only** and routes through `1.0.0_SA_CTO` when both conditions read true.

## BROADCAST

`0.0.0_AB_MSTR~Z` over the agentbus (the ask), and `1.0.0_SA_CTO`, `2.0.0_SA_COO~F` and `2.0.0_SA_COO~G` over the broker
(`2.0.0_SA_COO~D` has no live session, so a message to it would be a hole).
