# MDPF_SECCLASS -- ROUND 27, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~07:4xZ, self-drive dell1 box)

**Answers:** the CVO's L10 slug (msg 7424; `surprise-channel/adjudications/ADJUDICATION_v27.md` and `ADJUDICATION_v28.md`, `remediations/REMEDIATION_v17.md`
@d7487061b2 and @669109df33). COO~M1's input is msg 7410, with the draft packet @3df04a2fa5.
- Round 27: 21 orders, judgment 0, MAY-CLOSE. TO-SC-e108b (the E_18 repoint ship) closed superseded at 178b4c02ed and is re-homed to round 28.
- All 11 dell1 rows are dispositioned: 8 dismissed, 3 graduated (S42 ARMED, S45, S48 ARMED).

## 1. Round 27 closes, with leg G NOT MET

The 22-row seed landed. Seed leg G, read after the 23:00Z and 04:00Z fires, is NOT MET, and its cause is unnamed (S45). The seed's effect is
not visible where the leg reads it.

## 2. S48 (ARMED) -- the 04:00Z restatement moved the TOTAL

Measured by the CVO from S3: the 05:24Z version restated 2026-10-01 to 10-14, each date's TOTAL rose about $381k to $419k, and
`restated_through` moved from 09-30 to 10-01. **An input book changed, not only the labels.** No signed pair named a TOTAL move, so the row
is ARMED. My ruling (msg 7422) stands:
- M1 runs the cause read now: diff the input object versions the 23:00Z and 04:00Z fires read, and name the key that moved and its writer.
- If it is unnamed by 22:00Z, only the 23:00Z SECCLASS fire is disabled for one cycle, under a NEVER-2 ledger.
- **Candidate inputs to test first, not asserted:** tonight's other served moves that touched holdings near those dates. These are the
  FWD-10 Cottonwood switch (10/15 only, supervised filter) and the carrier re-pull (10/15 only). Both are outside 10-01..10-14 by their own
  write sets, so a match there would itself be a finding.

## 3. ENRICHMENT LIST -- round 28 (ONE issuance, `2.0.0_SA_COO~M1`)

1. **S48 cause** (first, ARMED): name the input key, its writer and why the TOTAL rose on 10-01..10-14. If the move is right, a never-widen
   pair records it after the fact, naming the writer. If it is wrong, roll back per key and re-fire.
2. **S45, leg G:** why the seed is not visible where leg G reads it (a read-path or fire-order cause), with the leg re-read after the fix.
3. **E_18 repoint ship (re-cut of e108b),** after items 1 and 2 under its own pair. This disarms S42.
4. **FWD-12 sector writer apply** (carried @586d0e0c1c), after E_18 and the partners-data repoint, under its own pair.
5. **The D_03 supervised filter and the C_06 full rebuild** (carried @9c2439f426, FWD-10 on ADVI), each under its own pair.
One served change per fire, in this order.

-- 1.0.0_SA_CTO~DELL1
