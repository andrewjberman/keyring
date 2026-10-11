# DSGN_IRPTV1 round 12 -- the CVO's answer to the pair's open question

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T07:05:06Z. Row DSGN_IRPTV1-D2-S6.
**Input:** msg 4335 (round 12 drained @709d1be19c); the draft pair `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/FWD1_TRACE_READONLY_PAIR.md` (both halves unsigned; nothing was run).

**The question:** does an API-runner trace with no rendered page meet FWD-1's "real login ... ending in the rendered page"?

**Answer: No.** It is a sound first half and it does not grade FWD-1.

FWD-1's DONE WHEN (PRD) asks four things of the one live trace:

| asked | an API-runner trace with a minted token |
|---|---|
| real login | No. The draft pair's own step says there is no sign-in on that path: the token is minted offline. Row D2-W47-S3 adds that the page signs in by refresh cookie, so a minted token cannot open it at all |
| real backend | Yes, if every hop is a real call |
| real Cottonwood data | Yes, for the named client |
| ending in the rendered page | No. The run ends at JSON. ACCEPT is worded on the screen: a user "can name, from the screen alone" the client, the holdings, the return and the securities |

So the runner can prove each hop answers, read-only, and can stand as the trace's backend arm. FWD-1 is graded only on a run that
signs in as a person does and ends at the page, read as a picture. The pair's "page step" must be ruled in for the run to count;
its default (`PAGE-NOT-RENDERED`) is a run that grades nothing.

## What the pair must hold before either half signs (rows of this round)

- **D2-W47-S2:** the performance GET is a read-through store. A miss computes and persists a report, and for this client's firm the
  fresh path can spend a single-use vendor authorization. A "read-only" pair has to name that branch and what stops it.
- **D2-W47-S1:** the bound "every request a GET but the sign-in" is not true of the page: one POST writes a selection and one POST
  only reads. The pair names both.
- **D2-W47-S3:** a signed-in browser also posts analytics events and prefetches five 49financial files. The blast radius of the
  page step includes them.
