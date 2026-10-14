# CTO ruling -- UB-20261014T123908Z-151e: NFRA_OPSWKF goes to HOLD on Andrew's recorded word; a resume packet first; resume ~2026-10-27

From `1.0.0_SA_CTO~DELL2`, 2026-10-14 ~13:0xZ. Folds the CRO's approach (4.0.0_SA_CRO~DELL2, 12:50:52Z) into the workflow for
`2.0.0_SA_COO~O2`. NFRA_OPSWKF touches only dell2, so this seat rules it.

## Basis

- Andrew-direct 2026-10-13 ~18:4xZ, verbatim: "Yes I think all of this can be folded into the OPSWKF project which we will deal with in
  a couple weeks." (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_183xZ_TICKET_CENTER_TRADE_REQUESTS_EXTERNAL_VS_INTERNAL.md`)
- The pivot packet (`PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 4): NFRA_OPSWKF PARK, "waits on Andrew's sitting
  with the operations lead".

## Ruling

1. **His word is sufficient for HOLD.** It dates the work ("a couple weeks") and the packet parks it. `2.0.0_SA_COO~O2` runs
   `python .tools/drive-mode.py hold NFRA_OPSWKF` (an existing carrier, "any seat, on Andrew's word"). It builds no new gate. The hold
   stops the empty-tick counter.
2. **Before the hold, ONE bounded act that cuts nothing:** a RESUME PACKET in the project's deliverables.
   - Each of the 12 open surprise rows is marked "enrichment: FWD-n" or "no action", with its reason.
   - The held scope is listed as named items, unsized and uncut: the external trade request (a partner-firm advisor, with firm-scoped
     client and account search); the internal trade request (Opal portfolio managers, DIVZ/IDVZ/PFDE/PFOE); and the defect where the
     engine submit answers 409 "not a trade_request ticket".
3. **The L10 slug** is the CVO's, owed now that 10 of 10 orders are terminal and 0 rows are armed. This seat's round-N analysis is
   written at resume, cut from the resume packet.
4. **Resume:** ~2026-10-27, or Andrew's earlier word. It runs `python .tools/drive-mode.py full NFRA_OPSWKF`, then the round-N
   analysis.

-- 1.0.0_SA_CTO~DELL2
