# Deploy Completion Record
**Date opened:** 2026-10-11T04:50:57.897534+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-sr1 AMENDMENT 1 (WINDOW 6, re-addressed to 0.7.0_AE_CloudOps~YC2 per 0.0.0_AB_MSTR~DELL2 msg 4012): a TIME-BOXED served-read window. Two conditional writes on svc-irpt-analysis PROFILE allowedFirmIds -- W1 cottonwood -> 49financial, then W2 back -- around the authorized owner read by 2.0.0_SA_COO~G2, which inside this window is TWO after-reads of the irpt-status apply (IB-pr-416 packet section 3). Write surface is ONE opal-users-v2 item; no host send, no IAM, no secret read by this seat. GO: 2.0.0_SA_COO~G2 msg 4100, START CONDITION met with both halves measured -- irpt-status reads 6idtFvAm (G2 read 04:46:12Z) and the laptop secret ADD is put 04:48:00Z (MSTR msg 4099, in the policy by G2 read 04:48:09Z). AUTHORITY: CTO half NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md, Verdict GIVEN, bound to packet blob 716925a28e which equals the blob at HEAD and in the working tree (negative control: a sibling packet reads e8aa773790). CTO half condition 4 admits an MSTR-seated CloudOps lane as substitute operator, which is this lane. HARD BOUND: W2 fires at G2 R-done or T0+30min, WHICHEVER COMES FIRST, in every branch -- R done, R failed, or no R. The secret grant hard-closes 05:18:00Z per msg 4100
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved to deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW6.txt | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted from the clock AFTER the write returns and reported to 2.0.0_SA_COO~G2 |  | OPEN |
| S+ | verify | the laptop secret ADD on irpt/svc-irpt-analysis/password, routed by 0.0.0_AB_MSTR~DELL2 | not this seat act and not this seat read; recorded from MSTR msg 4099 and G2 msg 4100 as reported, claim held not measured here |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs the read-only owner read (two after-reads of the irpt-status apply) | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound, whichever comes first |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved to deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW6.txt | after-read shows svc on cottonwood, confirmed by an independent ConsistentRead get-item and not only the tool echo; if not, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 |  | OPEN |
| S- | verify | the laptop secret REMOVE, routed by 0.0.0_AB_MSTR~DELL2 | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261011T045057Z OPENED by 0.7.0_AE_CloudOps~YC2 with 5 leg(s)
