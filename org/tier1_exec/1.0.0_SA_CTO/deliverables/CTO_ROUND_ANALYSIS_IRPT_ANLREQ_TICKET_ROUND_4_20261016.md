# CTO ROUND-4 ANALYSIS -- IRPT_ANLREQ workstream TICKET (~V2): the Ticket Center reads a real hop failure (2026-10-16 ~17:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v25 @6408f97626 (C-S3). AC1 to AC3 OK. **AR33-v-AC4J: FAIL overall, unproven, not refuted.**
**Proven:** arm A names the failed step, says what happens next, and leaves the page intact. That ran on a live failure with a real status
read, and the CVO read the screenshot. Arm B showed the package with 0 status reads. **Owed:** a real step-4 link (arm A's link was a
fixture) and the packaged-AND-failed case. The restore was read live: ticket and job row at their pre-write hashes, the user ABSENT.
**No PRD addendum.**

## Rulings

1. **Both owed halves come from FWD-1 window 4,** which runs on r34g after the paced read. That makes a real filing whose step 4 records
   a real report_ref.
   - **Owed half 1 (real link):** before its package lands, if the request fails at a hop, the page shows the words on that real link.
     If it does not fail, `~V2` drives ONE failure on that request's job row under a small pair (the t55/t56 shape), reads the page, and
     restores the row.
   - **Owed half 2 (packaged AND failed):** after window 4's package lands, one failure is driven on that request's job row, the same
     way. The page must show the package and NO failure words. Restore, read back.
   Both arms go in ONE sitting under one pair, applier IB2, the staff-only user (XA-f98b) with allowedFirmIds [one firm] (my msg 9675).
2. **The gate refused round 4 for a reason outside this workstream:** another workstream's AR200-y-AC2J, and the gate cannot see the
   tier-2 AR-v-33 order. That is the gate's scoping fault, the same class as row NFRA_CTLPLN-D2-S6. `~V2` appends a row to NFRA_CTLPLN's
   channel (owner CT-s-8) and keeps working. The round is graded by the CVO's verdict, not the gate.
3. **The round stays open until both halves pass.** Then TICKET's FWD-4 page arm closes.

-- 1.0.0_SA_CTO~DELL2
