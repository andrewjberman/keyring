# AMGT_CORPUS -- ROUND 35 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-04 ~21:0xZ

**Input:** CVO slug msg 29221, `surprise-channel/adjudications/ADJUDICATION_v41.md` @04ff86b965. The packet is
`deliverables/2.0.0_SA_COO~X/ROUND35_DRAIN_END_PACKET.md` @f699518c86.
**Precondition:** MET for this round's rows (Z-S85, Z-W1-S29 and Z-W1-S30 are DISARMED on evidence the CVO read). The 36 legacy ARMED
rows (rounds 2-34) were dispositioned in prose at their own rounds, and the instrument cannot read prose. The CVO owns their
machine reconciliation as REMEDIATION_v1. That is bookkeeping on settled rows, not an open hazard, so it does not hold this
analysis.

## 1. WHAT THE ROUND DELIVERED

- **ak-1:** unit families for the 52 (drained @7c43d48775). **ak-2:** the re-pin script names its interpreter (@61c58e31bc).
  **ak-3:** the dry run reads rc 0 (@a5a561d96b).
- **ak-4 (SERVED, ledger `amgt-corpus-r35-ak4` CLOSED @66a15668e1).** It covered the map rebuild (66 -> 118 fields, 0 base units
  moved), 96 re-derives with no vendor call, and the re-pin to `74e00624b0` (Python311).
- **The served result:** 0 pointer-unit figures over the 52's 32,826 figures (all 32,826 carried the pointer unit in round 34).
  BA's Model tab shows the act's block.

**Round 35 is CLOSED.**

## 2. GRADES

- **FWD-22: REALIZED.** The 2026-10-04 13:00Z scheduled fire re-pulled 96 of 96 with rc 0 (run log :327, :329). A later dry run
  reads `already_current 96`. The CVO read the log and the task itself.
- **FWD-20: open.** The 52 now carry measured units, and the CVO's BA sample shows 51 of 52 against filed figures with 0 wrong
  families. The 49 V3 rows still do not render on the Model tab (`modelSheet.ts`). That is now the only thing between FWD-20 and
  its DONE WHEN.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **FWD-20's V3 rows on the page** (round-34 item 2, packet candidate 3) | **Round-36 cell:** `modelSheet.ts` renders the 49 V3 rows with their measured units, or with their reason where none is measured. This is a portal product-file candidate: this seat reviews it, and the DEV push takes Andrew's word (CLAUDE.md Portal). | Round-34 ruling 2 gated the rows on measured units. That gate is met: 0 pointer units are served. |
| 2 | **The units judgment the CVO left open** (packet candidate 1; v41 section 2: "not read: a non-USD name, and the per-family sample across names") | **Round-36 READ cell, graded at L9 as judgment.** It checks one non-USD name's currency labels (BP/_LN or TSM) and one field per family across three names, against Bloomberg's field definitions. No vendor call: it reads the stored blocks. | ak-1 decided the families on landed values. A per-family read across names is what turns "measured" into "right". |
| 3 | **The 802 UNRESOLVED entries for the 52**, of which 656 read "no value returned" (packet candidate 2) | **No cell.** Each serves with its reason. | The DONE WHEN is "every served figure carries a measured unit or a reason". A value Bloomberg did not return has nothing to measure, and the reason is its claim. Resolving them would take new requests, which is a vendor question with no outcome behind it. |
| 4 | **Z-W1-S32:** `EQY_FUND_YEAR` lands no value, so its YEAR family is untested | **Closed under ruling 3.** It serves "no value returned". The YEAR family's first real test is the first landed value; no ad-hoc pull. | Moving the request to prove one field would be a vendor leg that no outcome needs. |
| 5 | **Z-W1-S31:** four dividend-yield fields were put in `ZERO_VALUE_UNIT_FROM_BASIS`, an exemption the order did not name | **KEPT, and ratified here.** | A 0% yield on a non-payer is a measured value in PERCENT, not an absence. ZERO-DOMINATED would have served a real zero as unresolved. The CVO records the row against this ruling. |
| 6 | **The first fire on the new pin** (2026-10-05 13:00Z; v41's caveat) | **A round-36 regression read, not a re-grade.** Expect 96 pulled, rc 0 and 0 pointer units. It is a Monday, so the content is Friday's close (trading calendar). | FWD-22 is REALIZED on the 10-04 fire. The 10-05 fire proves the re-pin did not break it. |

## 4. ENRICHMENT LIST (round 36, ONE issuance by `2.0.0_SA_COO~X`)

1. **FWD-20:** `modelSheet.ts` renders the 49 V3 rows with measured units or reasons (portal candidate; CTO review; DEV push on
   Andrew's word).
2. **The units judgment:** one non-USD name plus a per-family sample across three names, from the stored blocks; graded at L9.
3. **The 2026-10-05 13:00Z fire on pin `74e00624b0`:** 96 pulled, rc 0, 0 pointer units.
4. **No vendor call beyond the scheduled daily pull.**

## 5. ACTS FOR ANDREW (cited)

- The DEV push of the round-36 Model-tab candidate, when it is approved (CLAUDE.md Portal: `0.0.0_AB_MSTR` pushes a product-file
  candidate on his word).
