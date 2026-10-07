# ETFS_RIVALS -- rounds 15 and 16 L8/L9 on the round-16 real run (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~11:00Z. Packets: COO~RV msg 30785 (round 15 @e9e43448dc) and msg 30815 (round 16
@f00567cd5f). Earlier pre-deploy grade: ADJUDICATION_v16.Z.md C-S52. Nothing of rounds 15 or 16 is deployed or served.

- **pc-1 J1: limb 1 MET** (0 of 695 curves join two currencies). **Limb 2 MET for 335 of 432 non-dollar-treated
  securities; NOT MET for 96** (no stored currency: the reader cannot tell, and 43 US-listed ones are told a false thing);
  1 has a stored currency and no price.
- **co-1 J1: MET** on the real-run objects. **pd-2 J1, md-1 J1: NOT MEASURED** (each names the served page).
- Row Z-S55 graduates REMEDIATED. Two items graduate OPEN: C-S54 and C-S55.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S53",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:00:00Z",
    "one_line": "Rounds 15 and 16 L9 on the round-16 real run of day 2026-10-06 (local objects, not served): the currency repair holds on every object (0 of 695 fund-securities carry a holding-implied point without a stored currency of USD; 0 market/implied boundaries jump more than 3x; was 152). Row Z-S55 is REMEDIATED on the real run. co-1 J1 MET; pc-1 J1 limb 1 MET, limb 2 short on 96 securities (C-S54); pd-2 J1 and md-1 J1 NOT MEASURED until the round is served.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S55"
    ],
    "spec_asserts": "RIV-pc-1 J1: on the real day's chart objects no security's curve joins two currencies, and a reader of a non-US security's dialog can tell which currency the prices are in. RIV-co-1 J1: a sample of points equals the market close or the holding-implied price of that day, and each marker equals a trade of the audit page's trade log. RIV-pd-2 J1: graded on the served page. RIV-md-1 J1: graded on the live page in a signed-in browser.",
    "world_is": "Graded object: the 13 chart objects of C:/tmp/rv-r16-realrun/layer/ on site Z (code root CLOUD 0f7e460190), read by this seat's own code against the round-15 objects and against the gold tables downloaded for C-S52.\n- pc-1 J1 limb 1: 695 fund-securities. Stored currency USD: 263, all carrying market and implied points. Stored currency not USD: 336 (335 with market closes only, 1 with no price). No stored currency: 96, no price. Securities with an implied point and a currency other than USD: 0. Market/implied boundaries above 3x or below 1/3: 0. The stored currency equals the gold security_market currency of 10-02 / 10-05 for 599 of 599 keys this seat could look up; the other 96 are the ones with no row.\n- pc-1 J1 limb 2: each of the 335 priced non-dollar securities names its currency in its source sentence (EUR 129, GBp 54, JPY 43, CHF 19, CAD 18, HKD 11, others 61). The 96 without a stored currency name none (C-S54).\n- co-1 J1: the 263 dollar securities' points are identical to the round-15 objects graded in C-S52 (263 of 263); the markers of all 695 are identical to round 15's (695 of 695), so the 123 of 123 marker grade carries. The non-dollar market points were not re-compared on this run.\n- Dollar closes against the same day's implied price (10-05, every fund this seat's holdings download covers): 216 of 217 within 3 percent; the one outside is C-S55.\n- 17 dollar boundaries move more than 5 percent between an implied day and the next market day. 16 are moves between consecutive trading days of 5 to 13 percent; one was checked (PBR +11.5 percent equals the market table's one-day return field) and 15 were not examined; the 17th is C-S55.\n- pd-2 and md-1, read only: one period group of three radios opening on 30d (C-S52); the issuer's round-16 screenshot shows 'Price in TWD' printed over the axis's top figure, and 126 markers riding the top edge of a range that holds 2 prices. Neither criterion is graded here.\n- Cost of the repair, re-measured: all 96 no-currency securities had priced points in the round-15 objects and have none now.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round16/DRAIN_END_PACKET.round16.md @f00567cd5f",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round16/currency_measure_2026-10-06.json @f00567cd5f",
        "adjudications/ADJUDICATION_v16.Z.md ETFS_RIVALS-Z-C-S52 @2804439de0 (the gold objects read)",
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S55"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S54",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:00:00Z",
    "one_line": "After the currency repair, 96 fund-securities with no stored currency carry the sentence 'this listing is not quoted in US dollars'. 43 of the 96 are US-listed keys (INTU, CMG, AJG, BABA US among them), so the page states something false about them; for all 96 the reader cannot tell the currency, and all 96 lost a curve they had in round 15.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-pc-1 J1 limb 2: a reader of a non-US security's dialog can tell which currency the prices are in. Cell text: a key with no stored currency is treated as non-dollar; the script shows 'currency not on file' for a null currency.",
    "world_is": "On the round-16 real-run objects, 96 of 695 fund-securities have currency null. 96 of 96 carry source_words 'No price: no market close on file; this listing is not quoted in US dollars, so the funds' holding reports (in US dollars) are not used.' By key: 43 US-listed, 53 not US-listed. The treatment (no implied price without a stored currency) is the CTO's ruling 30787 term 1; the sentence asserts more than the treatment knows. The script's axis words say 'currency not on file', so the dialog carries two statements that disagree. All 96 had priced points in round 15's objects; for the 43 US-listed keys those points were dollars against dollars.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/rv-r16-realrun/layer/ chart objects on site Z, census by this seat 2026-10-07 ~10:57Z (695 keys; currency null 96; US-listed 43)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round16/DRAIN_END_PACKET.round16.md @f00567cd5f section 'What the ruling costs today'"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S55",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T11:00:00Z",
    "one_line": "INEQ SUNB_US_Equity is stored as USD and its market close does not agree with the fund's own report: close 77.39 on 2026-10-05 against an implied 63.49 the same day (22 percent), and 77.10 on 10-02 after an implied 63.49 on 10-01. It is the one dollar security of 217 compared that is off by more than 3 percent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-22: one price curve per security, market close where Bloomberg has one and the holding-implied price on other days, as one series a reader can read as the price.",
    "world_is": "The curve for SUNB in INEQ steps from about 63.5 (implied) to about 77 (market) and stays there. The cause is not established: the fund may hold a different line of the issuer than the key's Bloomberg security, or report it in another currency. The currency repair cannot see it, because the stored currency is USD. Not measured: whether the same holding differs on the rankings' contribution figures.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/rv-r16-realrun/layer/ charts/INEQ.json points for SUNB_US_Equity 2026-10-01 .. 2026-10-05",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=2026-10-05/holdings-20261006T123244Z-928e3e0810ec.parquet (market_value over quantity, INEQ)",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=2026-10-05/market-20261006T123301Z-b6602b19fad6.parquet (px_close 77.39)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
