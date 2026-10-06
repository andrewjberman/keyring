# AMGT_HARVST -- ROUND 49 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~09:0xZ

**Input:** CVO slug msg 29981, `surprise-channel/adjudications/ADJUDICATION_v61.md` @2315d08911 (precondition MET; ARMED 0).

## 1. WHAT THE ROUND DELIVERED

- **av-1:** ft and wsj links come from the stored `og:url` and wsj's `articleData.sourceUrl`, on the publisher's own host only. PASS.
- **av-2, gold rebuild #7:** PASS (CTO half @0666944946). The mention part carries a url on **33,665 of 33,665** rows, each on its
  publisher's own host (0 foreign). No host was contacted.
- **For RESAPP FWD-4:** every gold mention row now carries its link. RESAPP's next walk grades it.

**Round 49 is CLOSED.**

## 2. THE BOARD (denominator 17)

Unchanged: **8 REALIZED** (FWD-2, 4, 5, 6, 8, 12, 16, 17). **9 NOT REALIZED as a qualified wait** (FWD-1, 3, 7, 9, 10, 11, 13, 14, 15)
on Andrew's presence: his hand-solve of each blocked leg's challenge, and the SA account answering 200 (AMENDMENT 2 @69ce080222).

## 3. RULING: NO ROUND 50 IS CUT UNTIL THE RESUME

- Every build cell that does not need collection is now done.
- The 9 open outcomes are each graded on the collection run's per-leg report, and that run cannot move until Andrew acts.
- Cutting a round with nothing to build would be a round for its own sake. So:
  - **the next issuance is triggered by the resume,** not by the calendar;
  - when Andrew hand-solves a leg, `2.0.0_SA_COO~H` resumes it from its own checkpoint (the issuer's act under the run's pair);
  - at that run's drain, round 50 grades the per-leg report against the card-5 rule (95% of the run universe, 223 of 234).
- **For the self-drive completion test,** AMGT_HARVST reads **UNREACHABLE (Andrew's hand-solve; the SA account)** until then. That
  is a classification, not a change to the member set.

## 4. ACTS FOR ANDREW (cited)

- **Hand-solve the barrons, wsj and bbg challenges while present** (collection-run condition 3).
- **The Seeking Alpha account:** its account endpoint answers HTTP 402 (his account).
- **The ft leg:** "Dont attempt FT until I return" (his hold, quoted).

## ADDENDUM 1 (2026-10-06 ~19:3xZ) -- round 50: SA on the tab pattern; the origin load wait (COO~H msg 30245)

**Andrew-direct ~19:2xZ** (in COO~H's 183xZ record, branch `coo-h-rec-20261006`): "SA shouldnt need Bright Data, we should be able
to run th same pattern on SA as we use with all the others which is logging in via google credentials, then in the browser window
using the same session to pull the relevant rest api endpoints". **It supersedes this seat's route (a)** (msg 30219, the KYC ask),
and no KYC is asked of Andrew.

**Placed for round 50, ONE issuance by `2.0.0_SA_COO~H`:**
1. **The SA tab cell, cut only on a 200 from the in-tab probe** of the account and listing endpoints (after Andrew's Google sign-in
   in `browser-profiles/sa`). It has 3 mechanical criteria:
   - SA is `transport: tab` in `contracts.json`;
   - `TAB_ORIGINS["sa"]` plus an sa sign-in route on bbg's Google pattern;
   - one real in-tab fetch of each endpoint class answers 200 through the transport, with no proxy in the path.

   A non-200 probe means NO cell; COO~H reports the status and body class instead.
2. **The origin load wait** (`lib/opal_data_harvest/tab_transport.py:92`, `self.page.goto(origin)`, which waits for the full
   `load` event under Playwright's 30 s default):
   - The tab needs only the origin's document and cookies, so it waits for `domcontentloaded` with an explicit timeout.
   - A timeout there is raised as a DISTINCT, named error, not a bare TimeoutError, so it can be told apart from a refused
     request.
   - Proof: a plant whose origin never fires `load` still opens the tab; plus a re-run of the 5 jobs that ended TimeoutError
     before any request, each reaching its first request.
