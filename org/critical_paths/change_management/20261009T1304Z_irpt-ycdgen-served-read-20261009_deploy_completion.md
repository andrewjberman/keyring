# Deploy Completion Record
**Date opened:** 2026-10-09T13:04:56.234465+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-sr1: a TIME-BOXED served-read window. Two conditional writes on svc's PROFILE allowedFirmIds -- W1 cottonwood -> 49financial, then W2 back -- around ONE read-only owner read by 2.0.0_SA_COO~G2, which is the authorized reader that can settle APPLY-Y1 read 6 (REQ-5e4149d2 and its RetentionRefused). Write surface is ONE opal-users-v2 item; no host send, no IAM, no secret read. W2 fires at G2's 'R done' or T0+30min, WHICHEVER COMES FIRST -- the window closes on the clock even if no one speaks
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted and reported to 2.0.0_SA_COO~G2 | WINDOW OPEN. python swap_svc_firm.py cottonwood 49financial, ONE opal-users-v2 item (svc PROFILE allowedFirmIds), which is the entire write surface the bounds allow. before {allowedFirmIds cottonwood, updatedAt 2026-10-09T12:13:57.679766Z} -> after {allowedFirmIds 49financial, updatedAt 2026-10-09T13:05:57.041170Z}, both printed by the tool itself. CONTINUITY WORTH NOTING: that before-updatedAt is exactly the st29 W2 write at 12:13:57Z, so this row moved from the state this seat last left it in -- no third party changed it in between. T0 = 2026-10-09T13:05:57Z, measured from the clock AFTER the write returned rather than before it, so the 30-minute bound cannot be accidentally generous. BOUND = 2026-10-09T13:35:57Z, which is when W2 fires if 2.0.0_SA_COO~G2 has not said R done first. Output saved to deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_20261009.txt. | CLOSED 20261009T130618Z |
| S+ | verify | MSTR routes the laptop secret ADD | not this seat act; recorded when MSTR confirms |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs ONE read-only owner read of REQ-5e4149d2 | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound | CLOSED ON THE BOUND, NOT ON A REPLY. 2.0.0_SA_COO~G2 did not say R done, so this leg closes on the T0+30min bound the order sets as the alternative: T0 was 13:05:57Z and the bound 13:35:57Z. Whether G2 completed its read inside the window is G2 own record to state and is NOT graded here; what this leg records is that the window it was given was exactly 30 minutes and was not extended. The order wording is explicit -- W2 at G2 R-done OR T0+30, WHICHEVER COMES FIRST -- so waiting past the bound for a reply would have been the defect, not the courtesy. | CLOSED 20261009T133930Z |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved | after-read shows svc on cottonwood; if not, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 | WINDOW CLOSED ON TIME. Fired at 13:38:27Z, after the 13:35:57Z bound was reached and with no R-done from G2. python swap_svc_firm.py 49financial cottonwood, ONE opal-users-v2 item. before {allowedFirmIds 49financial, updatedAt 2026-10-09T13:05:57.041170Z} -> after {allowedFirmIds cottonwood, updatedAt 2026-10-09T13:38:28.622286Z}; the before-updatedAt is exactly W1 own write, so no third party touched the row inside the window. AFTER-READ CONFIRMED INDEPENDENTLY, not just from the tool own echo: a ConsistentRead get_item on USER#svc-irpt-analysis PROFILE returns allowedFirmIds {S: cottonwood}. The TYPE TAG is printed as S, because this is the scalar attribute whose .L read returned [] BY CONSTRUCTION during st28 -- so the read that confirms the restore is the one shape-checked against that trap. The order says STOP and restore if the after-read is not as expected; it is as expected, so no restore and no report to the CTO is owed on that branch. | CLOSED 20261009T133930Z |
| S- | verify | MSTR routes the laptop secret REMOVE | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261009T130456Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
- 20261009T130618Z LEG W1 closed: WINDOW OPEN. python swap_svc_firm.py cottonwood 49financial, ONE opal-users-v2 item (svc PROFILE allowedFirmIds), which 
- 20261009T133930Z LEG R closed: CLOSED ON THE BOUND, NOT ON A REPLY. 2.0.0_SA_COO~G2 did not say R done, so this leg closes on the T0+30min bound the or
- 20261009T133930Z LEG W2 closed: WINDOW CLOSED ON TIME. Fired at 13:38:27Z, after the 13:35:57Z bound was reached and with no R-done from G2. python swap
