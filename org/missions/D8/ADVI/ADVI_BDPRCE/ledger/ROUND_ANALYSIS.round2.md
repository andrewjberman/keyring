# ADVI_BDPRCE -- ROUND 2, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~01:1xZ)

**Input:** `3.0.0_SA_CVO` slug msg 5326, `surprise-channel/adjudications/ADJUDICATION_v2.md` and `REMEDIATION_v2.md` @0447f2df38. MAY-CLOSE.
- 7 of 8 orders merged. BP-b-7 (the FWD-7 packet) is superseded by R1 AMENDMENT 1 (@608d822cc3).
- **Nothing served moved.**
- The thread re-reads live (10.3525 from 2 Buys). The CVO corrected round 1's C-S1: that "trade" was a Transfer In.
- Context: ADVI_BDPRCE and AMGT_RESAPP / ADVI_FIRMBKTS are driven at full capacity (Andrew-direct ~21:1xZ).

## 1. Rulings on the rows sent to this seat

- **W9-S2 (ARMED): the runner logs "OK sentinel emitted" when it emitted none.** A success line with no success hides the Monday and Tuesday failures. **RULED:** the log line
  reports what happened, with a sentinel-absent line when there is none. That is a logging fix in the producer under its own pair; no alert or monitor is built (moratorium).
- **W10-S1, the PRD's "sha256-equal" template claim: CORRECTED** in PRD v1.2. The files are equal only after LF normalisation.
- **W10-S3, the export holds EXACTLY 500,000 rows.** A round-number count is the signature of a vendor cap, and a capped export silently drops lots: the opposite of FWD-9.
  **RULED:** before ANY apply of the Units and Cost Basis switch, a read-only cell proves whether 500,000 is a cap (the export's own paging and limit settings, and a second export
  window). If it is a cap, the export is paged until complete.
- **W12-S1, the banned interpolation is still served:** expected, since R1 is not yet built into the writers. Every interpolated served row appears on the FWD-7 list Andrew reads,
  with what replaces it (a trade price, or "last traded <date>").

## 2. ENRICHMENT LIST (round 3, ONE issuance by `2.0.0_SA_COO~K1`), adopting the issuer's section 6 with the rulings above

1. **R1 AMENDMENT 1 into the module, then the replay re-run:**
   - reinvestment buys are in; par-quoted bonds are per unit; the 153 Transfer-In carry-forwards each carry their observation date;
   - a determinism arm;
   - the late-landed-trades lookback (W6-S3) is widened, or its limit stated on the list.
2. **THE FWD-7 PACKET (BP-b-7 re-cut):** for Andrew, in plain words:
   - each moved price from and to, with why;
   - the dollar effect on the latest snapshot;
   - every interpolated row's fate (W12-S1);
   - the readers each fix reaches.
   The eight 100x rows read UNCHANGED.
3. **THE 500,000-ROW CHECK (W10-S3), then the lot-key fixture proof** (call 239a's key with relationship_id), **then** the WORLD apply of the Units and Cost Basis switch under its
   pair. In that order, each read back.
4. **The honest sentinel line (W9-S2),** under its pair.
5. **Read-only:** the cause of the Monday and Tuesday header-only export; the source of the 1,859 off-canonical lots.
6. **Not this round:** the writers importing R1. They follow Andrew's review of item 2's list, in the issuer's order (the S_00 build, the Lambda, the silver script).

## 3. ACTS ONLY ANDREW CAN DO (cited)

None yet. FWD-7's review of item 2's list is his when the packet lands (PRD DONE WHEN 3).

-- 1.0.0_SA_CTO~DELL1
