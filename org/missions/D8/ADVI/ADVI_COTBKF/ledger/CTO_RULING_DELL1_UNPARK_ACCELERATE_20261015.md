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

## Amendment 1 (~18:1xZ) -- the unmatched holders (P2) count as inactive for Yahoo (answers `2.0.0_SA_COO~Q1` msg 6113, DQ-t-64 @0a1fa594f8)

Census: 4,634 CUSIPs held by anyone; V2 holds 2,929; outside V2 1,705 = P1 32, P2 1,448 (holder match open), P3 225.

- **"Active" means set V2.** A name held only outside V2, P2 included, may take a Yahoo price under the not-for-active label. That label is
  its own column, not `porting_verdict`. No Yahoo price feeds an account in V2.
- **If a P2 holder later matches into V2,** its names join the Bloomberg need that `2.0.0_SA_COO~C1` sizes. Bloomberg then replaces the Yahoo
  price for that account.
- **The CUSIP-to-symbol resolver goes on a non-Bloomberg source:** 1,691 of the 1,705 have no symbol. It is Q1's next cell.

-- 1.0.0_SA_CTO~DELL1

## Amendment 2 (~18:4xZ) -- Cottonwood's 27 active Bloomberg slices go AHEAD of the ETFS_RIVALS backfill (answers `2.0.0_SA_COO~Q1` msg 6121)

- **Queue order on the Bloomberg queue:** B1, failed-14, the porting test, then COO~C1's 27 active slices (154,024 cells, tier 2, finish about
  2026-11-24), then the seven ETFS_RIVALS requests (tier 3, about 213,000 units). This amends this seat's msg 5778, which placed RIVALS behind
  B1 and failed-14 only.
- **Why:** Andrew's 10-15 word accelerates Cottonwood's active-account need ("We need to pick up the pace on this"; "Active accounts should get
  BBG pricing exclusively"). ETFS_RIVALS parks after round 30 on his 10-13 word. His 10-14 word devotes dell1 to ADVI/MDPF work.
- **Cost, stated to Andrew:** the RIVALS backfill starts about 27 days later, around 2026-11-24. Call 99be (trading-day draws) would shorten
  both if he grants it.
- Placement is Q1's act; no quota or budget changes.

-- 1.0.0_SA_CTO~DELL1

## Amendment 3 (~18:5xZ) -- account matching (answers crossbox ORDER `XB-20261015T182453Z-e03b`, `4.0.0_SA_CRO~DELL2` research `RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.md`)

Andrew, verbatim (dell2 record `ANDREW_DIRECT_20261015_175xZ_BETTER_MATCHING_CRM_KEY_AND_COLUMN_RUN.md` @628b6102dc): "No we need to do better
at matching. ... im wondering if there could be an intermediary key fashioned from something in there." Follow-up: "The name is also a very
obvious match mechanism if nobody tried that already to push stuff over the line."

FWD-9 stands: a link is never guessed. `2.0.0_SA_COO~C1` cuts, in its next round:
1. **R3, custodian-number equality** (BD `fact_holdings."Account Number"`): deterministic, control 2 of 2. It yields 87 forward links, none
   active. It is cheap and certain, so it is cut.
2. **R4, name to a unique BD household, then a narrowed holdings fingerprint inside that household, within the date window.** A link is
   DETERMINISTIC only when the fingerprint passes; otherwise it is a CANDIDATE. Name plus registration class alone is never deterministic (15
   wrong picks in the control). Client-line propagation (89 households) feeds the same inside-household step and is graded the same way.
3. **Exact account name 1:1 with a corroborating date window and registration class** is how Andrew's "push stuff over the line" is answered:
   a REVIEW LIST of candidate links for a person to confirm, never an automatic link. The list carries no PII values: it shows link ids and
   corroboration flags only.
4. **The CRM zip** (C-RESTRICTED, Andrew's own rule) and **a mapping-file request to Cottonwood** are Andrew's. They are carried as open call
   `dell1-20261015T184344Z-d3cc` on this box. No cell reads the zip.

The yield is reported against the 387 unmatched active accounts, of which 168 are post-migration new clients with no predecessor, so the
reachable denominator is 219.

-- 1.0.0_SA_CTO~DELL1

## Amendment 4 (~19:0xZ) -- the Bloomberg history rate, and the finish dates it gives (answers `2.0.0_SA_COO~C1` msg 6139)

- **5,858 cells is the rate per DRAWING DAY.** It is `history.ceiling` in `data/mdpf/scripts/demque/bbg_allowance.json`: the largest single-day
  history sum on the served demand ledger (dt=2026-10-08), claim `measured`. It is a floor of the true capacity, not a vendor cap.
- **The CRO's 23,432 is 4 x 5,858**, the four non-trading days in a 14-day window (the DQ-t-27 schedule). It was labelled "a day" in error.
  Neither number is wrong; they are different windows.
- **Finish dates, computed with `lib/trading_calendar.is_trading_day` from 2026-10-17 at 5,858 per drawing day:**

| set | cells | drawing days | non-trading days only (today's rule) | every day (call 99be (a), upper bound) |
|---|---|---|---|---|
| B1 + failed-14 + porting test | 45,317 | 8 | 2026-11-08 | 2026-10-24 |
| plus C1's 27 active slices | 199,341 | 35 | **2027-01-30** | **2026-11-20** |

  C1's 11-24 / 12-04 assumed drawing every day, so they hold only if Andrew grants 99be. The "every day" column is an upper bound on speed:
  on a trading day the history channel gets what production leaves.
- **1,006 of the 2,739 new CUSIPs cannot be priced** by the builder (no Commonwealth window). They stay outside the slices until a window
  exists; C1 reports them as a named gap, not a draw.

-- 1.0.0_SA_CTO~DELL1
