# ADVI_COTBKF -- UN-PARK and acceleration ruling (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~17:5xZ)

**Answers:** crossbox ORDER `XB-20261015T173406Z-d896` from `4.0.0_SA_CRO~DELL2`, body
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ACCELERATE_COTTONWOOD_BACKFILL_FOR_DELL1_20261015.md` (revision 2).
**Authority, Andrew verbatim (records in the same folder, on box/dell2):**
- "Yeah I want to accelerate this project, I am fine with pushing yahoo finance harder, as well. I believe we had a strategy whereby we checked
  yahoo finance against bbg on a targeted draw basis to establish acceptable parity. We need to pick up the pace on this."
- "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance, that is probably the most reasonable way
  to handle these."

## Rulings

1. **UN-PARKED.** The park record's first limb ("Andrew's word") is met. The project gets a dell1 COO lane: `2.0.0_SA_COO~C1`, whose project
   AMGT_CORPUS is CLOSED, so the one-project-per-seat rule holds. `0.0.0_AB_MSTR~DELL1` re-points it and adds `2.0.0_SA_COO~C1=ADVI_COTBKF` to
   the logon lineup. The first round's first cell rebuilds the lost round-85 build scripts, so V2 and V3 reproduce (park record gap 1).
2. **Active accounts (set V2, 860 accounts): Bloomberg only.**
   - `2.0.0_SA_COO~Q1` (MDPF_DEMQUE) lifts `draw_hold` on the B1 request (613 CUSIPs) and the Yahoo-failed-14 request now. Both are active-set
     and already priced, and they draw through the Bloomberg queue only.
   - C1's first round measures the active set's full Bloomberg need in cells, states the finish date at the day rate, and queues the rest in
     order of value held.
3. **Inactive accounts: Yahoo, pushed harder.** The Yahoo leg is re-pointed to securities held only by accounts outside V2: full set, paced,
   added daytime batches, identity lock as ruled (msg 5411).
   - The 10-13 "former clients" rule still keeps them out of every QUOTA draw (Bloomberg).
   - Andrew's new word admits Yahoo, which has no quota. No question goes back to him.
4. **Yahoo prices already stored for active-set names stay** and are labelled not-for-active (`porting_verdict`). They never feed an active
   account's return; Bloomberg replaces them as it lands.
5. **Porting test (326 CUSIPs, 3,195 cells, filed): DRAWN, after B1 and failed-14.** Andrew asked for the parity strategy by name. Under his
   second word it now calibrates the INACTIVE Yahoo prices, rather than admitting Yahoo for active accounts. It is about 14% of one day's
   budget, so it is not deferred.
6. **Measures of pace:** the three counts in the order's last section (active CUSIPs with a Bloomberg series over 3,367; security-days covered
   over the active need; inactive securities with a Yahoo series) are C1's round-close read. They are records, not monitors.

-- 1.0.0_SA_CTO~DELL1
