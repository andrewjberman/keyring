# /canonical-drive IRPT_YCDGEN -- 2.0.0_SA_COO~G2 on dell2, 2026-10-09 00:2x-02:2xZ

## st26 (st24 + brand + svc for ONE seat F1)
- 00:53Z U2 closed by 0.7.0_AE_CloudOps~DELL2 @571f607cfb; shell window opened 01:00:23Z (laptop TO-APPLY-20 B2); 01:08Z D2+V1 CLOSED @ffd85b8e7c: load_brand from the RUNNING root, no env; producer_for svc=OPAL.
- Secret reader live 01:20:15Z. 01:25Z F1: upload refused NOT_AUTHORIZED. Cause read in CloudWatch by ~Y2 (msg 2059): E5 (IRPT_BCKEND release 3, live 21:26Z) -- a filer listing the tenant must name the firm advisor. Not release 5 (my first reading, msg 2052, corrected).
- Own errors, corrected on the record: (1) msg 2065 claimed an advisor_email retry routes to YCHARTS (read from the UPLOAD owner); the x-6 census showed the ANALYSIS owner is forced to the submitter (submission_service.py:115), so it routes OPAL or is refused at submit -- corrected in msg 2107. (2) The 21:11Z re-poll's second secret read was reported late (msg at 21:37Z).
- CTO 2067: X1 now. Applier X1+V2 01:30:49Z (SSM 856b6197): st24, Andrew only; ledger irpt-ycdgen-f1-st26-20261008 CLOSED 7/7 @70403dcfaa (F1 NOT RUN). Secret reader removed 01:34:00Z; shell window closed 01:43:20Z.

## Cells
- YCD-x-6 (producer by acting principal, CTO 2067) issued @0dc9addc92; worker ~8 census: 0 of 21 accepted-request fields carry an actor; the analysis owner is the submitter. Closed on its census (CTO 2111) @b6850ec51e, drained @494bb3ee9d; row D2-W8-S1.
- Advisor census (CTO 2118; direct read stands, CTO 2148) @c7ba00eea0: 49financial 11/11 and inflection 6/7 advisorKey rows; cottonwood 0/5; 0 admin anywhere. Row D2-S4 @1440a9d3d1. svc cannot file for cottonwood under E5; the seat arm moves to 49financial (swap after st27).

## st27 (st24 + brand, Andrew-only, stays live)
- CTO 2118. Candidate @e606008994 (override IRPT_COMPLETION_Y); gate PASS, G5 vs st24 added 2 changed 2 identical 265. Order TO-APPLY-st27 + packet @45970defc8; CTO half GIVEN @6066a7d5cb; order pending @caa54a41f5. U2 closed @b5f34fd947 (02:23Z); "open now" sent 02:24Z. Wrapper doc fixes @2c7a8de477.

## Riders for ~Y2's irpt-ycharts-generate
- msg 2011: f60e6f1d2a inert on the live path except the OPAL_REPORT_PDF drop (inferred unused). msg 2159 reply: c6c3c0b674 + e923e0f463 + f60e6f1d2a inert; the live zip's default policy row sha e0046398 equals the 5b pin's (measured).

## Rules received
- /keep-driving ON for every box and COO (Andrew ~01:5xZ, MSTR 2140): an empty tick runs /next-calls --drive.
- Law edits: box/* is a shared branch (538f0f51a7); rule 30 naming gate refuses hand-typed names (c55a7b39cd).

## tick 98 -- ~02:24Z
lease FULL. st27 U2 closed, window asked. NO-OP: P1/D2/V1 wait on the laptop's window-open time.

## Compiler Tools
- None beyond the package, merge, row and issuance gates; AWS reads were read-only (DynamoDB counts, Lambda config/zip, SQS depth).
