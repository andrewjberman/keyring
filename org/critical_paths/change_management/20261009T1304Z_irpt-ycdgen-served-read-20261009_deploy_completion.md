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
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted and reported to 2.0.0_SA_COO~G2 |  | OPEN |
| S+ | verify | MSTR routes the laptop secret ADD | not this seat act; recorded when MSTR confirms |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs ONE read-only owner read of REQ-5e4149d2 | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved | after-read shows svc on cottonwood; if not, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 |  | OPEN |
| S- | verify | MSTR routes the laptop secret REMOVE | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261009T130456Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
