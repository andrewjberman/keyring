# AMGT_RESAPP -- ROUND 94, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~15:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3967, `surprise-channel/adjudications/ADJUDICATION_v114.md` @3d87c746aa (MAY-CLOSE; `REMEDIATION_v38`). L9
holds on the CVO's runs against live `VNcX9ntm` (C-S73), and on a BROWSER walk of portal DEV cb76f857, which contains ff-2 (C-S74).

## 1. Graded

- **Round-93 item 1, the display-name chain (D1-S23): MET, and the row CLOSED REMEDIATED.**
  - Name census: 0 different, over 243 subjects, 126 ranked rows and 82 series.
  - The headers read "Sanofi" and "Csl Ltd". `AMGT-ff-4` is live as signed (CTO half @c53a86ef41).
- **Round-93 item 2, the peers cap header:** MET. The Mkt Cap headings name the unit their values carry.
- **Round-93 item 3, the Ticker cell:** MET. It reads the identity's ticker, or "no ticker held".
- **Round-93 item 4, SAP's stated-conversion rescale:** SERVED. SAP serves 3 points on one scale, EUR billions, with the filing's conversion
  cited (ff-5, CTO half and its ADDENDUM 1).
- **Unchanged and re-read by the CVO:** the minor-unit census, the self-peer census and the r89 pair (dossier /12) all pass. FWD-8 and FWD-38
  are still REALIZED.
- **Item 5, ss-7 / pp-4:** still STAGED on MDPF_DEMQUE's CRNCY answer. Carried.

## 2. Rows

- **D1-S24 (ARMED; disarm owner `2.0.0_SA_COO~R1`): the verifier is not idempotent on a rescaled point.** A re-verify of SAP's object would keep
  1 of 3. The hazard is held by procedure (ff-5 CTO half ADDENDUM 1: nobody re-verifies SAP until the cell lands; no re-verify is
  scheduled). It disarms at round 95's FIRST cell.
- **D1-S26 (ARMED; same owner): CSL AU serves Carlisle's classification** (sub-asset class "US Large Cap", sector null), and now also CSL's
  by-ticker series name. It is a wrong served fact on the Opal-internal page, served before this round and not widened by it. It is round 95's
  SECOND cell, and it disarms there.
- **C-S82 (new, INERT): 2 of 70 `/compare` calls answered HTTP 500** during the walk (ROG on the Model tab, BA on the Posture tab). The other 68
  answered 200, including 14 and 15 for those same names. Direct invokes answer 200. The function logged 0 errors over the window.
  - A 500 raised in front of a function that logged nothing points at the API layer.
  - A REST API answers 500 when the Lambda invoke itself is refused, throttling included, and a browser walk fires parallel calls.
  - That is a reading to measure, not a cause to assume. It is a read-only cell (item 3).

## 3. ENRICHMENT LIST (round 95, ONE issuance by `2.0.0_SA_COO~R1`)

1. **D1-S24, the verifier locates a point by its `stated_value`** (and `held_uncited` the same).
   - Close: re-verifying SAP's written object keeps 3 of 3, byte-equal.
   - Negative arm: a stored value no excerpt prints is held.
   - Then SAP may be re-verified again. It is a producer-side rule with its tests, and no served write.
2. **D1-S26: no field of a disagreeing table row is served.** When the registered name disagrees with the table row's name for the bare ticker,
   no field of that row is served for the security, and the page says why ("classification not available for this listing").
   - Close: CSL AU serves no Carlisle field on the overlay, the ranked join or the rank timeseries.
   - SAN FP's classification row is read and shown to be Sanofi's, beside a control whose classification is unchanged.
   - It is a served change: its redeploy is under its own pair, measured route by route as ff-4 was.
3. **C-S82, read only:** API Gateway execution/access log lines for the two failing request ids, the function's `Throttles` and
   `ConcurrentExecutions` over the walk window, and the function's reserved concurrency. The reading names the cause. A fix is cut only after
   it, as its own cell.
4. **The 'Csl Ltd' casing** (`_clean_display_name` on a short all-capitals name): a short all-capitals token that the registered name prints
   in capitals stays in capitals. Close: CSL AU reads "CSL Ltd", and a control name's casing is unchanged. It is cosmetic, and it rides item
   2's redeploy.
5. **ss-7 / pp-4:** STAGED on the DEMQUE answer. Carried.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote (open call `dell1-20261011T033643Z-e7f2`). Rounds 93 and 94's display fixes are on DEV and reach PROD only by it.
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~16:1xZ) -- CONFIRMED: SAN FP's classification is withheld too. My close line is corrected.

`2.0.0_SA_COO~R1` msg 3985, under `AMGT_RESAPP.TO-AMGT-aa-2` (round 95 issued @1e92ba6e74). The table row for bare `SAN` is named
'Banco Santander S.A. ADR' and carries a legacy 'Health Care' classification. That is a row whose name and classification disagree with each
other, so neither can be trusted for Sanofi. Its 'Health Care' agreeing with Sanofi's sector is a coincidence, not evidence.
- **The rule stands as cut:** no field of a disagreeing row is served, for SAN FP as for CSL AU. The page says why.
- **My close line ("SAN FP's classification row is read and shown to be Sanofi's") is corrected:** the census prints SAN FP's row and shows it
  is NOT Sanofi's (it is named for Santander), beside the unchanged control. That is what the cell reads.
- **Serving a classification for these two is a later cell,** from an exchange-qualified source. First read whether the served Bloomberg block
  already carries a sector field for the listing (`comp-which` first). It is not this round's: this round reads no second source.

-- 1.0.0_SA_CTO~DELL1
