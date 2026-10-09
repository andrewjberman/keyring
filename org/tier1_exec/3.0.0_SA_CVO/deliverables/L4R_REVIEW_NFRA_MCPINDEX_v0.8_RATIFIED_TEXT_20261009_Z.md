# L4-R review, NFRA_MCPINDEX PRD v0.8, ratified-text half -- SIGN (3.0.0_SA_CVO~Z for 3.0.0_SA_CVO, 2026-10-09 ~07:4xZ)

**Asked by** `1.0.0_SA_CTO~O` msgs 32483 and 32484 (both acked). **Bytes reviewed:**
`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @0eff9e0e6d; `git diff 3c7ff0684b 0eff9e0e6d`, whole
(+53 -2: the version bump, FWD-19 in ENDPOINT, the v0.8 addendum). Half hash at delivery: `cdd1cd1d5a03`.

## Sources read at their pins

- **Andrew's word**, `ANDREW_DIRECT_20261009_05xxZ_TICKET_CENTER_TRADE_INTAKE_AND_FIT_READ.md` @709da7cded: line 9
  carries "MCPINDEX on the sitez box as far as how claude gets the data in question", as cited. The record's s.2 lists
  six items: Billing, Trade rec, Post model update rec, and three FA alerts.
- **Option A**, `ANDREW_DIRECT_20261009_05xxZ_OPS_LEAD_LOCALHOST_DASHBOARD.md` @1740ba55ec, :15-16: "one server his
  Claude pulls from (NFRA_MCPINDEX, site Z)". Matches the addendum.
- **Fixtures** @cc539738c6: `trade_rec.json` row keys are account, custodian, trade_date, symbol, side, quantity,
  opal_status, custodian_status, matched; `billing.json` row keys are account, household, billing_period, aum,
  fee_rate_bps, fee_amount, status. Both are equal to FWD-19's ACCEPT lists, field for field.

## Verdict: SIGN

FWD-19 carries the word at its width for placement: all six items are placed in this project, two as served readers
and four as catalogued GAP entries. The bar is EXERCISED, with a second-instrument count and the C4 envelope. "A
fixture is never served as data" closes the shape-as-data hole, and "a reader with no served source is a GAP entry"
keeps FWD-19 from closing on a fixture. Items 2-5 agree with C1, C4, C7 and C8 as signed at v0.7. Item 4's moratorium
line restates the standing law and adds no gate.

## Carried (not grounds)

1. **Post model update rec is catalogued `unowned` with no stated reason.** It is a data read, the same kind as trade
   rec. The moratorium does not reach it. The round that cuts FWD-19 should either give it a reader cell or record why
   not.
2. **The three FA items have a read half that is not an alert.** Examples: the list of high-cash accounts, asset
   transfers and restricted accounts. The moratorium bars the push, not the read. When Andrew answers the alert
   question (asked in session, per the record), the read half should get an owner and should not stay `unowned`.
3. **The brief half is owed.** The input is an Andrew-direct record, not a CRO brief. `prd-signoff.py status` reads the
   brief half SIGNED (auto), but the addendum itself says the brief half is owed by `4.0.0_SA_CRO~Z` or a live COO not
   holding the round. That discrepancy is the CTO's to settle; this half does not depend on it.

-- 3.0.0_SA_CVO~Z
