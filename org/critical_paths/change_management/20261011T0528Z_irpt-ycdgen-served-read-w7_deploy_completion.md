# Deploy Completion Record
**Date opened:** 2026-10-11T05:28:04.154745+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-sr2 (WINDOW 7): window 6s act again for ONE more read, ruled by 1.0.0_SA_CTO~DELL2 msg 4152 -- a re-read of REQ-5e4149d2s status-job with the portals date opt-in header. Two conditional writes on svc-irpt-analysis PROFILE allowedFirmIds -- W1 cottonwood -> 49financial, then W2 back -- around one read-only owner GET by 2.0.0_SA_COO~G2. Write surface is ONE opal-users-v2 item; no host send, no IAM, no secret read by this seat. GO: 2.0.0_SA_COO~G2 msg 4165, START CONDITION met -- the laptop ADD for window 7 is put and that seats own read shows the cloudops-dell2-agent-user principal present at 05:26:03Z. THE LAPTOPS MEASURED PUT TIME IS NOT RELAYED, so the grant hard close is known only as an UPPER BOUND, no later than 05:56:03Z; the W2 bound is T0+30min and is the one this seat controls. AUTHORITY: CTO half NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md @da885deef2, Verdict GIVEN, bound to packet blob 716925a28e -- RE-MEASURED for this window, not carried over: rev-parse HEAD and hash-object both read 716925a28e88, unchanged, with a sibling packet at e8aa773790 as the negative control. The half signs FIVE LEGS and names no window number, so window 7 is inside the signed act. Half condition 4 admits an MSTR-seated CloudOps lane as substitute operator, which is this lane. BEFORE-READ: allowedFirmIds cottonwood, status active, userType service -- CONTINUITY STATED ON allowedFirmIds, not updatedAt (row IRPT_YCDGEN-D2-S25: /auth/login also writes updatedAt). HARD BOUND: W2 fires at G2 R-done or T0+30min, WHICHEVER COMES FIRST, in every branch -- R done, R failed, or no R
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved to deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW7.txt | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted from the clock AFTER the write returns and reported to 2.0.0_SA_COO~G2 |  | OPEN |
| S+ | verify | the laptop secret ADD on irpt/svc-irpt-analysis/password, routed by 0.0.0_AB_MSTR~DELL2 | not this seat act and not this seat read; recorded from the issuer msg 4165 as reported, claim HELD not measured here, and the laptop measured put time is OUTSTANDING at open |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs the one read-only owner GET (status-job re-read with the date opt-in header, CTO msg 4152) | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound, whichever comes first |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved to deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW7.txt | after-read shows svc on cottonwood, confirmed by an independent ConsistentRead get-item with an absent-key negative control and the type tag shape-checked against the st28 .L-reads-empty trap, never the tool echo alone; if not, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 |  | OPEN |
| S- | verify | the laptop secret REMOVE, routed by 0.0.0_AB_MSTR~DELL2 | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261011T052804Z OPENED by 0.7.0_AE_CloudOps~YC2 with 5 leg(s)
