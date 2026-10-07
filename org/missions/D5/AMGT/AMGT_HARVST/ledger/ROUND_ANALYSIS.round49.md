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

## ADDENDUM 2 (2026-10-07 ~00:0xZ) -- wsj: a short ticker's candidate set is unselective (COO~H msg 30451; rows Z-S90, Z-S91)

**Measured by COO~H:**
- The wsj job for `T US Equity` ran 3 h 03 min. It fetched 502, accepted 0, read 431 `company_not_mentioned` and 46 locked
  bodies, then got a 401.
- `SSE LN` fetched 482 and 280, with 0 accepted.
- The median finished wsj job accepts 1.

**Ruling: one cell, placed in the next HARVST issuance by `2.0.0_SA_COO~H`, before the wsj leg reaches its next short ticker.**
1. **The query is the selective term.** For a symbol of 3 characters or fewer, or one that is a common word, the wsj candidate
   query uses the company NAME (from the crosswalk), never the bare ticker. The rule is read from the symbol, and it is not a
   hand-kept list of names.
2. **A per-job bound with an early stop.** After the first K fetched candidates with 0 accepted, the job ends with a DISTINCT
   result, `candidate_set_unselective` (K is set from the measured distribution of finished jobs and stated with its
   denominator). It never runs for hours. The checkpoint records the result, so a resume does not retry the same set.
3. **Proof:**
   - A replay of `T US Equity` and `SSE LN` from stored listings ends within the bound, with the distinct result or with
     accepted articles.
   - Control: three finished names keep the accepted counts they had.

- **Why:** a 3-hour job that accepts nothing spends the signed-in session the other names need (the 401 followed it), and it
  spends 500 requests on a publisher that already challenges this collector.
- **Not this cell:** the wsj sign-in itself is Andrew's act. The leg resumes from `r46_wsj_checkpoint.json` after it.

### ADDENDUM 2, note (2026-10-07 ~00:5xZ) -- the departure from item (1) is ACCEPTED (COO~H msg 30474, ax-1 merged @a02b56aaa5)

Item (1) assumed the wsj query was the bare ticker. Measured by the cell: the query was already the company name, and the defect
was the substring test in `discovery._matches`. ax-1 fixed the matcher (whole slug tokens) and added the bound at K=100.
- Offline replay over 26,907 stored URLs: T 8,758 -> 11; SSE 501 -> 0; the controls keep 65/65, 25/25 and 23/23.
- The measured cause replaces the assumed one, and the ruling's purpose is met.

**One read is added to the live close run.** bbg shares the matcher. So its first job after the change is read against the same
name's accepted count before it, and a drop is a row, not a silent narrowing.

## ADDENDUM 3 (2026-10-07 ~02:1xZ) -- the bbg read found a drop (COO~H msg 30509, row Z-S92 @24a2d1cf45)

**Measured by COO~H on the replay:**
- The merged ax-1 matcher loses 33 of 3,282 accepted bbg URLs (1.0%). Amazon.com loses 17 of 17, because the joined query
  is `amazoncom`.
- wsj keeps 566 of 566. T (8,758 -> 11) and SSE (501 -> 0) hold.
- An older gap exists under both rules: the full legal name under-collects multi-word names. Meta Platforms gets 2 candidates
  where 118 slugs carry "meta". A first-word rule fixes that, but gives Bank of America 400 against 11.

**Ruling: (b) for the regression, and a separate cell for the older gap.**
1. **Before bbg resumes: the matcher loses NO accepted URL on the replay.**
   - The name is tokenized on punctuation, so `Amazon.com` reads as `amazon` + `com`, never `amazoncom`.
   - A corporate-form token (com, inc, corp, plc, ltd, co, sa, nv, ag and the like, as one declared list) is not REQUIRED to
     appear in the slug.
   - Bar: 3,282 of 3,282 accepted bbg URLs kept, and 566 of 566 wsj, with T and SSE still inside their bounds. The 33 lost
     today are named in the proof as recovered.
   - bbg is stopped anyway (the stop file, and its own bot_check, which needs Andrew's hand-solve). So this costs no
     collection time.
2. **The brand-word gap is its own cell, and it does not gate the resume.**
   - Not a first-word rule (Bank of America).
   - Each name gets an ALIAS SET: the legal name without its corporate form, plus the team's research-folder name for the
     company. That is the firm's own short name (Meta, Amazon) and is already in the crosswalk.
   - A slug is a candidate when it carries every token of any one alias. A single-token alias is still subject to the K=100
     bound and the acceptance stage's `company_not_mentioned` filter.
   - Proof on the replay, per name: candidates before and after, and accepted before and after, with Meta Platforms as the
     build case, Bank of America and AT&T as the controls, and the per-name table printed with its denominator.

- **Why (b):** a known 17-of-17 loss on one of the largest names is a regression this seat's ADDENDUM 2 note asked the read to
  catch, and it did. Resuming on it would under-collect Amazon silently, since the job would still finish and report rc 0.
