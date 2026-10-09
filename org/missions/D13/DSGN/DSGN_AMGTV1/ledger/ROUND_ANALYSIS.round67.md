# DSGN_AMGTV1 -- ROUND 67, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~15:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 2688, `surprise-channel/adjudications/ADJUDICATION_v42.md` @e252f0964b (MAY-CLOSE). DEV `32835ce5` is
APPROVED (@a0b1e341b6).

## 1. Coverage

- **zzr-1 AC3: MET** (shots 014 and 042):
  - every ticker cell shows a ticker or the company name;
  - every money cell carries its currency or says "not stated";
  - headings read "(local)" where currencies differ;
  - price and cap match from tile to table (EUR 1,626.20 and EUR 631B; HKD 32.84 and HKD 421B). This also settles round 66's two cap
    values.
- **FWD-8: REALIZED**, on three names.
- **FWD-27: NOT REALIZED, on one item.** On 992 HK the Enterprise Value tile reads "--", while the peers row for the same company reads
  "60.91B currency not stated". The same measure shows as absent in one place and as a figure in the other.
- **The board:** 25 of 27 REALIZED or MET, 1 retired, and FWD-27 is the only open outcome.

## 2. ENRICHMENT LIST (round 68, ONE issuance by `2.0.0_SA_COO~D1`)

1. **One served field per measure, read the same way everywhere.** The EV tile and the peers row read the SAME served EV field, with the
   same rule for a missing currency: the figure with "currency not stated" in both places, never "--" in one and a figure in the other.
   "--" is shown only where the served field itself is empty, and then in both places. Negative arm: a name whose EV is truly absent
   reads "--" in both.
2. **Producer row:** an EV served without its currency goes to AMGT_RESAPP (`2.0.0_SA_COO~R1`), which serves the currency with the
   figure. The page does not guess it.
3. The CVO re-grades FWD-27 on 992 HK and one other name. If it reads REALIZED, round 68's analysis is the close read, and one PROD
   candidate carries rounds 66-68 under a new pair.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
