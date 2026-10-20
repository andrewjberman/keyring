# Report to Andrew: the 425-cards report-server fix is live and verified on a fresh report (2026-10-20, 05:0xZ / 1:0x AM ET)

**From:** `1.0.0_SA_CTO~DELL2`. **Answers:** your relayed order (ms bus 5a68c5b3, MSTR msg 11167): live before 9:00 AM ET Tuesday, then
verified with a fresh report filed after the update. The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_013xZ_R34L_LIVE_BEFORE_9AM_ET_VERIFY_FRESH_REPORT.md`.

## Deploy time

**Live since 2026-10-19 21:39Z (5:39 PM ET Monday)**, ahead of the overnight ask.
- Report server version: release r34l, root `0485393f3a-r34l`.
- Every check after the install read OK.
- Receipt: `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34l/A_AFTER_R34L.txt`.

## Verification result: PASS (05:02Z / 1:02 AM ET)

**A fresh request was filed after the update** (REQ-b838e82f), through the Opal report engine.
- It was ready 25 seconds after submit.
- The report page's section list for it reads **3 sections where it used to list about 425 cards**:
  - 1 with a value;
  - 2 marked not available;
  - **0 empty builder-only cards, and 0 "not in this version" cards.**
- Receipt: `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e5d/A_E2E5D.txt` (RUN-DONE PASS). This seat read
  it: the running root is r34l, and the R2 line reads `n_sections=3 value=1 not_available=2 builder_only_without_value=0
  not_in_this_version=0`.

## What it took, and what it found

Four earlier test runs overnight stopped before a report was made. Each stop was measured, and each found a real problem:

1. **A test-file flaw:** a second unknown ticker.
2. **The report server's copy of the request rules was older than the portal.** It refuses the "commentary requested" field.
   - The live PROD form does not send that field (it did only for about 20 minutes on 10-15), so live filings were not hit.
   - The new form waiting on DEV does send it.
   - The fix (the next report-server release, r34m v2) is signed. The new form is held from PROD until that fix is live.
3. **Ticket Center staff filings go to the VENDOR report engine, not Opal's.**
   - Opal's engine is used only for a two-name allow list or a ticket created through another route. The Ticket Center's route never
     qualifies.
   - This contradicts your plan: every Ticket Center request gets the Opal-generated report.
   - The fix is being built now, as a must for this round.
   - The verifying run used an allow-listed test login, so it went through Opal's engine, which is the engine the cards fix lives in.

## Not yet proven

A staff filing, made through the Ticket Center form with nothing set up in advance, getting all four attachments on its ticket. That
needs three releases still to come:
- the routing fix;
- the advisor fix (signed);
- the attachment-and-rules release (signed).

Then one full staff run.

-- 1.0.0_SA_CTO~DELL2
