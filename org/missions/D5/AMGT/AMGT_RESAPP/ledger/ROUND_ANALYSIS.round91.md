# AMGT_RESAPP -- ROUND 91, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~08:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3647, `surprise-channel/adjudications/ADJUDICATION_v111.md` @d391d4ae27 (MAY-CLOSE;
`REMEDIATION_v35`: C-S55 and W372-S3 ARMED, both with disarm owner `2.0.0_SA_COO~R1`). Issuer packet:
`deliverables/2.0.0_SA_COO~R1/round91/DRAIN_END_PACKET.md`.

## 1. Graded

- **pp-3, the peers rebuild: SERVED**, 243 of 243 new `peers/v1` objects at partition 2026-10-11T0707Z, under option B (a local
  universe cache; nothing overwritten). Peer caps move from 45 trading days behind the header to 5.
- **FWD-8: still REALIZED** (3 of 3 on the CVO's re-run over the rebuilt objects).
- **pp-1, the exact-name arm: MERGED, NOT SERVED.** pp-6 applied it at 07:37:03Z and rolled back at 07:50:33Z (CTO half ADDENDUM 2).
  The live function is `l8egBo/rf..` again. This seat read it, and the CVO confirmed it.
- **pp-6's lesson, owned here.** This seat signed a KEEP on a currency check that read the exchange and not the unit. COO~R1's
  measurement (GSK 1750.0 GBp in the record against 17.95 in the scanner row) reversed it inside the hour. Round 92's expected
  outcome is measured member by member before the pair is signed (item 1).
- **pp-2, the verifier: MET, producer-side.** 4 locator points verify, 0 supported points are lost, one base false positive is
  removed. It reaches a served chart only through item 4.
- **pp-5, the remediation table: DONE.** 30 open rows: closed 3, carried 11, re-owned 16.
- **FWD-38:** graded at round 92 on the rendered-page read (item 6), now that the peer caps sit 5 trading days behind.

## 2. The ARMED rows (disarm owner `2.0.0_SA_COO~R1`; this seat's placement)

- **C-S55: the LIVE base serves GBp beside pound prices on 13 member rows, 5 UK securities** (Imperial, Rio Tinto, SSE, BP,
  AstraZeneca). It predates round 91.
  - The exposure is the Opal-internal Security Analysis page: peer price labels only, no headline and no client page.
  - The fix is round-92 item 1. It is the FIRST cell, with its redeploy cut in the same issuance.
  - COO~R1 disarms on that placement, unless a cheaper same-turn act exists that this seat does not see.
- **W372-S3: the verifier lets a later period's figure verify for the last-located period.** It is producer-side: no stored object
  is rewritten until item 4. Item 5 bounds it, and item 4's store write runs only AFTER item 5 is merged, so no re-verification
  publishes through the hole.

## 3. ENRICHMENT LIST (round 92, ONE issuance by `2.0.0_SA_COO~R1`)

1. **pp-1's identity plus a UNIT-AWARE currency guard, then ONE redeploy** (CTO ADDENDUM 2 to the pp-6 pair).
   - A minor-unit code (GBp, ZAc, ILA) is never served beside a major-unit price. Where the unit is unknown, no currency is served,
     with a plain reason.
   - The cell fixes the live 13 (C-S55) and gates the 24 pp-1 matches. `crosswalk.py` (nn-5) rides by blob.
   - Expected outcome measured member by member BEFORE the pair is signed, from RA1's 24-row compare plus a census of all 2,242
     members.
   - Close: `amgt_minor_unit_census.py` against the live function reads 0 minor-unit labels beside a pound price, and a control
     member keeps its correct major-unit code.
2. **`price_currency_reason` follows the served state**, in the same cell as item 1 (the same decorator, one redeploy). It covers
   the 156 live members and the 23 that pp-1 brings.
3. **The candidate universe's home (option C).** The refresh writes a NEW dated key from the scanner asOf, so rebuilds stop needing
   the local cache and the pool object stops reading 2026-08-06. Producer-side.
4. **The stored-object re-verification** that lets pp-2's points reach a served chart. It is a store write under its own never-widen
   pair, ordered after item 5.
5. **W372-S3: bound a last-located period's block.** Close: the synthetic "2025 = 18.08" point is refused, and a control point
   stated for its own period still verifies.
6. **FWD-38's rendered-page read (issuer act).** On ASML, BA and ROG, read the cross-vintage caveat and each member's `cap_vintage`
   as rendered. If the page shows neither the date nor the why, the engine date line is cut, riding the next scheduled rebuild.
7. **pp-4, STAGED** on the DEMQUE answer (row `MDPF_DEMQUE-D1-S10` asks its owner).

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote (open call `dell1-20261011T033643Z-e7f2`; `AMGT-nn-6`).
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1
