# TCKT_VNEXT F10 -- L9 grade, TO-APPLY-F10 AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~03:5xZ, on the L8 packet `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.F10.md`
@0c50a6b802 (msg 2325). Row: TCKT_VNEXT-D2-S11.

| criterion | verdict | evidence |
|---|---|---|
| TO-APPLY-F10 AC2: steps 5-6 (deployed bytes and env) and leg M's positive arm and negative arms | MET | live reads by this seat: CodeSha256 RFRuryx.., LastModified 01:01:08Z, Successful, COMMENTARY_ALLOWED_FIRMS byte-exact, package route live with CUSTOM auth over all 117 routes; no f10 entry open in `.open_deploys`; ledger CLOSED 4/4. `F10-M_arms_result.json`: step 4 201 created_by svc-commentary; step 6 400 naming 'demo' (the clamp, not the attachment check); 5a no firm data; 5b 403 'Missing firm identity'; 7 403 LIST refused; step 3 claims on stored bytes, 90.00 days |

**Weighed, none changes the grade:**
- (a) Step 4's attachment is synthetic. AC2 asks for the arm, not a real report; real ids flowing through are H6's live run or TV-r-1.
- (b) The test ticket stays open; Andrew left it open (record 35fabf20c8). It is not an AC2 clause.
- (c) The dell1 reach of the read grant is row D2-S9, the CTO's.

**Note:** the arms file quotes the created ticket's answer, which includes internal staff email addresses. Internal, not client data;
no action asked.
