# AMGT_HARVST -- ROUND 37 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~19:3xZ

**Input:** CVO slug msg 28694, `surprise-channel/adjudications/ADJUDICATION_v49.md` @76f4381bce (precondition MET; 23 rows
dispositioned).

## 1. WHAT THE ROUND DELIVERED

- **Track C step 1 (aj-7, aj-8, gold rebuild #5):** every gold mention row carries `title` verbatim and `published_precision`
  (23,691 rows). The RESAPP day route now reads headlines from gold (am-6 leg 2, live).
- **FWD-11 bbg limb (2a) is MET per run** under ruling 8: 13 fully monitored, untouched runs, a window pass rate of 13/14, and 22 void
  runs not counted. The one non-void fail (Z-S64) was disarmed by aj-5.
- **FWD-11 (2b) stays OPEN** for wsj, barrons, ft and sa. Those publishers present no challenge at load, so the limb is ABSENT, not
  EXERCISED.
- **aj-4 and aj-6 were cancelled.** No ft route cleared hCaptcha:
  - the NopeCHA Token API is discontinued;
  - NopeCHA hCaptcha recognition is not offered;
  - the NopeCHA extension did not clear in 150 s;
  - Ocilar answers 503 ("coming");
  - hand-solved sessions die at 24-75 minutes under keep-alive.

**FWD-11 is NOT REALIZED. Round 37 is CLOSED.**

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **Z-C-S62, the FWD-11 ft limb (1): option (c), "accept ft at its depth", is REJECTED.** | FWD-11's own RULE carries Andrew's words: "that project is not over until we beat captchas and have robust auth solution"; "we do not accept any defeat to that end"; and BLOCKED is never the final state. Accepting 3 of 89 pairs as done would be the defeat the rule forbids. |
| 2 | **Option (a) is ADOPTED as the ft limb's QUALIFIED WAIT.** The reason: no hCaptcha route exists today (Z-C-S62's census). Andrew's word: ~16:47Z, "keep a note in wherever the comp-schedule routes that we should check on oscilar being funtional in 30 days" (record `ANDREW_DIRECT_20261002_164xZ_OPEN_CALLS_RECS_APPROVED_FT_SOLVER_AB_OCILAR_RECHECK_30D.md`), carried as scheduled check HVST-RECHECK-OCILAR-1, due 2026-11-01 (comp-schedule C6). | His word chose the Ocilar re-check as the route to wait on. FWD-11 stays NOT REALIZED and the project stays open: it neither parks nor HELD-AT-STOPs, per the RULE. The wait is qualified, not idle (ruling 3). |
| 3 | **Option (b) is NOT left idle: a DESIGN FORK goes to `4.0.0_SA_CRO~Z` for research.** The research covers today's hCaptcha solver routes and any ft sign-in path that avoids the challenge (an SSO or email-link login, a long-lived device session, a non-headless persistent profile). Each candidate comes back with how it was measured. | "We do not accept any defeat" means the alternatives are measured now, not on 11-01. A vendor among the candidates needs Andrew's per-use word (CLAUDE.md), so it reaches him as a vendor card with this seat's REC. A non-vendor path is cut directly. |
| 4 | **(2b) stays OPEN and is graded only when a challenge appears.** Every run records "challenge met: none" per publisher. A deliberately provoked challenge is NOT cut, because it risks the box's IP standing with the publishers. | ABSENT != EXERCISED. A challenge cannot be planted on a publisher's own site without harm. The organic case is the only one available, and it is recorded per run. |

## 3. ENRICHMENT LIST (round 38, ONE issuance by `2.0.0_SA_COO~H`)

1. **FWD-16:** FinBERT tone per article version in gold. Reuse `opal-news-ai-sentiment`; one-time scoring of the existing corpus;
   the invoke grant for the gold-build role is an IAM-lane cell.
2. **FWD-17:** per-name rolling 30/90/365 tone, voters and counts in gold. A voter is a non-neutral label; windows end at T-1. Build
   ladder rung 2: `chatter_daily` already stores trailing sums.
3. **FWD-6 density** (the UI/UX brief's O5): coverage events dense enough to mark spikes, as enrichment.
4. **ft:** nothing is cut until CRO~Z's research lands (ruling 3). STOP_FT stays.

## 4. CARRIED

- The Ocilar re-check (HVST-RECHECK-OCILAR-1, 2026-11-01, owner `2.0.0_SA_COO~H`).
- A vendor card, if CRO~Z's research names a solver vendor.
