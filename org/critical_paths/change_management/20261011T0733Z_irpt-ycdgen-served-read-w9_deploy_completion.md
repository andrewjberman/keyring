# Deploy Completion Record
**Date opened:** 2026-10-11T07:33:21.896753+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-sr4 (WINDOW 9): window 6s act again for the read ordered by 1.0.0_SA_CTO~DELL2 msg 4362 (held-store intersect). Two conditional writes on svc-irpt-analysis PROFILE allowedFirmIds: W1 cottonwood -> 49financial, then W2 back, around one read-only owner read by 2.0.0_SA_COO~G2. Write surface ONE opal-users-v2 item; no host send, no IAM, no secret read by this seat. GO: 2.0.0_SA_COO~G2 msg 4390, START CONDITION met -- that seats read of the secret resource policy shows the window-9 principal PRESENT. NO LAPTOP PUT TIME WAS RELAYED THIS WINDOW, so the grant hard close is NOT computable here: a presence read says when someone looked, never when the grant was put, and the 30-minute grant clock runs from the put. This is the window-7 shape returning after window 8 had it right (w8 carried a measured put of 07:08:28Z). CONSEQUENCE RECORDED AT OPEN: the only deadline this seat can compute is its OWN W2 bound T0+30min, and the grant may close BEFORE it. The put time is asked of the issuer in the W1 report; until it arrives the reader deadline is UNKNOWN and the issuer is told not to pace off the W2 bound. AUTHORITY: CTO half NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md @da885deef2, Verdict GIVEN, bound to packet blob 716925a28e -- RE-MEASURED for this window, fourth independent re-measurement: rev-parse HEAD and hash-object both 716925a28e88, unchanged; sibling packet e8aa773790 as control; half unmoved. The half signs FIVE LEGS and names no window number. Half condition 4 admits an MSTR-seated CloudOps lane as substitute operator, which is this lane. BEFORE-READ: allowedFirmIds cottonwood, status active, userType service -- CONTINUITY ON allowedFirmIds, not updatedAt (row IRPT_YCDGEN-D2-S25). LABEL DEFECT ACKNOWLEDGED BY THE ISSUER (msg 4381), not this seats to fix: the order still names cell YCD-a-7 in decomp_ref and cell_refs, copied from sr1, where the round-8 cells are YCD-c-8 and YCD-e-8; the acts and bounds are right. HARD BOUND: W2 fires at G2 R-done or T0+30min, WHICHEVER COMES FIRST
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved to deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW9.txt | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted from the clock AFTER the write returns and reported to 2.0.0_SA_COO~G2 |  | OPEN |
| S+ | verify | the laptop secret ADD on irpt/svc-irpt-analysis/password, routed by 0.0.0_AB_MSTR~DELL2 | not this seat act and not this seat read; at OPEN the only evidence is the issuers PRESENCE read, with NO put time relayed, so the grant close is UNCOMPUTABLE here and is asked for in the W1 report |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs the one read-only owner read ordered by CTO msg 4362 (held-store intersect) | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound, whichever comes first |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved to deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW9.txt | after-read shows svc on cottonwood, confirmed by an independent ConsistentRead get-item with an absent-key negative control, the type tag shape-checked against the st28 .L-reads-empty trap, AND the artifacts after-stamp tied to the live row so the check cannot pass on any of the now-THREE prior windows files; W2 fires only inside a machine-checked guard that the R-done names TO-APPLY-sr4; if the after-read is wrong, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 |  | OPEN |
| S- | verify | the laptop secret REMOVE, routed by 0.0.0_AB_MSTR~DELL2 | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261011T073321Z OPENED by 0.7.0_AE_CloudOps~YC2 with 5 leg(s)
