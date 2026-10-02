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

## ADDENDUM ~19:5xZ -- ruling 3's research landed (`4.0.0_SA_CRO~Z` msg 28704; `FT_SIGNIN_ROUTES_BRIEF.md` @057df8f244)

- **Option (b) has no candidate.** None of 2Captcha, CapSolver, Anti-Captcha, CapMonster or NopeCHA lists hCaptcha in its own docs
  today. hCaptcha's own terms (2025-11-17) prohibit automated solving, so the solver class is closing, not merely unlisted. No
  solver vendor card is raised. Ocilar stays the qualified wait only because Andrew named it (ruling 2), and the 11-01 re-check
  reads hCaptcha's terms beside Ocilar's status.
- **Option (c) stays REJECTED,** against the brief's recommendation: FWD-11's RULE carries Andrew's "we do not accept any defeat to
  that end". The research's value is that it names the route that is not a defeat, a licence.
- **NEW, before any ft route is built: FT's terms on automated access are UNREAD.** `help.ft.com` refused the research tool. They bear
  on the ft limb as built (automated reads on a consumer subscription), not only on the solver question.
  - `4.0.0_SA_CRO~Z` reads them VERBATIM in a headed browser on an Opal machine and lands the clauses.
  - STOP_FT stays until that read. No ft collection resumes on a consumer subscription that the terms may bar.
- **For Andrew (spend), carded:** an FT corporate licence QUOTE naming SSO (re-authenticated every 180 days), Premium, FT-on-Bloomberg
  and the Datamining API. It is a quote, with no spend committed.
  - The tension is named for him: FWD-11's RULE excludes "licensed bulk access (Factiva or any other)". His verbatim was "no licensed
    factiva bullshit, no". A direct FT licence is a publisher seat licence giving SSO auth, not an embargoed aggregator.
  - Whether the Datamining API counts as "bulk" under his word is his to say on the card.
- **One Terminal read for FT news entitlement** (does FT full text or only headlines show today?) is a Bloomberg read under the
  per-use word. It is carded with the licence quote, because it may show a licence Opal already holds.

## ADDENDUM 2 ~20:0xZ -- FT's terms, read verbatim (`4.0.0_SA_CRO~Z` msg 28711; `FT_TERMS_VERBATIM_20261002.md` @0fab00b8a0, headed Edge 19:47Z)

**The clauses:**
- the Copyright Policy bars spidering, datamining, systematic download-and-store and scraping, and calls a breach "a breach of
  contract" that "may also violate copyright law";
- T&C s.3.2 bars circumventing security technology;
- s.3.5 bars ML/AI use "to generate any data";
- s.1.4: an organisation's agreement prevails.

**Rulings** (reversible; each protects without destroying):
1. **The ft limb's route is a LICENCE ONLY.** Solving FT's challenge is circumvention under s.3.2, so ruling 2's Ocilar wait no
   longer applies to ft. HVST-RECHECK-OCILAR-1 stays as Andrew's note, and its use for ft is barred by FT's terms. FWD-11's ft
   limb (1) now waits on the FT licence card, which is Andrew's spend. STOP_FT stays HARD: no automated ft read of any kind on the
   consumer subscription.
2. **FinBERT excludes ft** (PRD v0.16, FWD-16). ft rows serve tone null with the reason.
3. **The 62 stored ft articles are QUARANTINED, not deleted.** `2.0.0_SA_COO~H` cuts a cell that excludes ft rows from gold serving
   and from every downstream use. The bytes are kept. It is a served change under a never-widen pair (CTO half owed here). Deletion
   is Andrew's word (a delete is human-confirmed, and this one is also a legal judgement).
4. **The other four publishers' terms** (wsj, barrons, bbg, sa) are UNREAD. `4.0.0_SA_CRO~Z` reads each the same way. The same
   question may apply to HARVST as a whole, and it goes to Andrew as one card when the four reads land, not before (a card on a
   guess is not a card).
