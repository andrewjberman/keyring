# Deploy Completion Record
**Date opened:** 2026-10-11T07:12:04.890526+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-sr3 (WINDOW 8): window 6s act again for the SECTION CENSUS of round 8 cell YCD-c-8 (CTO round-8 analysis @fe73849335 section 3 item 3) -- ONE read of REQ-5e4149d2s analysis-report sections by 2.0.0_SA_COO~G2. Two conditional writes on svc-irpt-analysis PROFILE allowedFirmIds: W1 cottonwood -> 49financial, then W2 back. Write surface ONE opal-users-v2 item; no host send, no IAM, no secret read by this seat. GO: 2.0.0_SA_COO~G2 msg 4345 -- laptop ADD put 07:08:28Z per MSTR~DELL2 relay, principal present on the issuers own policy read, grant hard close 07:38:28Z (a MEASURED put time this window, not an upper bound derived from a presence read as in window 7). AUTHORITY: CTO half NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md @da885deef2, Verdict GIVEN, bound to packet blob 716925a28e -- RE-MEASURED for this window: rev-parse HEAD and hash-object both 716925a28e88, unchanged; sibling packet e8aa773790 as the negative control; half file unmoved. The half signs FIVE LEGS and names no window number, so window 8 is inside the signed act. Half condition 4 admits an MSTR-seated CloudOps lane as substitute operator, which is this lane. BEFORE-READ: allowedFirmIds cottonwood, status active, userType service -- CONTINUITY STATED ON allowedFirmIds, not updatedAt (row IRPT_YCDGEN-D2-S25). HARD BOUND: W2 fires at G2 R-done or T0+30min, WHICHEVER COMES FIRST, in every branch
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W1 | activation | python swap_svc_firm.py cottonwood 49financial, output saved to deliverables/irpt_ycdgen_sr1/W1_SWAP_OUT_WINDOW8.txt | before allowedFirmIds cottonwood, after 49financial, both printed by the tool itself; T0 noted from the clock AFTER the write returns and reported to 2.0.0_SA_COO~G2 |  | OPEN |
| S+ | verify | the laptop secret ADD on irpt/svc-irpt-analysis/password, routed by 0.0.0_AB_MSTR~DELL2 | not this seat act and not this seat read; recorded from issuer msg 4345 as reported, claim HELD not measured here -- the put time 07:08:28Z IS relayed this window, so the grant close 07:38:28Z is arithmetic rather than an upper bound |  | OPEN |
| R | verify | 2.0.0_SA_COO~G2 performs the one read-only owner read of REQ-5e4149d2s analysis-report SECTIONS (the round-8 section census) | not this seat act and not this seat grade; the leg closes on G2 R-done or on the T0+30min bound, whichever comes first |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood, output saved to deliverables/irpt_ycdgen_sr1/W2_SWAP_BACK_WINDOW8.txt | after-read shows svc on cottonwood, confirmed by an independent ConsistentRead get-item with an absent-key negative control, the type tag shape-checked against the st28 .L-reads-empty trap, AND the artifacts after-stamp tied to the live row so the check cannot pass on a prior windows file; if not, STOP, restore, and report to 1.0.0_SA_CTO~DELL2 |  | OPEN |
| S- | verify | the laptop secret REMOVE, routed by 0.0.0_AB_MSTR~DELL2 | the ledger closes once S- is confirmed by MSTR, which is the one thing that gates the close |  | OPEN |

## Log

- 20261011T071204Z OPENED by 0.7.0_AE_CloudOps~YC2 with 5 leg(s)
