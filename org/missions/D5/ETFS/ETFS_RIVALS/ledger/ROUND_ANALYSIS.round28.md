# ETFS_RIVALS -- ROUND 28, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~21:0xZ)

**Input:**
- `3.0.0_SA_CVO~RV1` slug msg 4557 @995a0646f4: `ADJUDICATION_v1.dell1.md` ADDENDA 1-17 and `REMEDIATION_v1.dell1.md`.
- The issuer's close packet: `deliverables/2.0.0_SA_COO~V1/round28/ROUND28_GRADED_READS_PACKET.md` @55a689301c.

**The PRE-DRAFT `ROUND_ANALYSIS.round29.PREDRAFT.md` (2026-10-09) is SUPERSEDED by this file and is not issued.** Its branches were cut against the 10-09 reads; this round's
grades decide.

## 1. Graded

- **J1, 7 of 9 MET:**
  - wa-1, the IDVZ 30-day curve and the 15-for-1 split;
  - wc-1 and wc-2, the trade list and the audit line;
  - wg-1, the fund-specific direction verdict;
  - wh-1: 0 '$0.0 million' and 0 bare identifiers over 26 items;
  - tc-1: the first post-merge run reached the leg and wrote, exit 94;
  - wi-1, the lookup before publish, against AMENDMENT 1.
- **wd-1: NOT MET (the repeat clause).** BIDD, CGIC and SCHY carry a window ending 10-02 beside a 10-02 cell marked "repeat". The page's VISIBLE text never names the calendar's day
  axis; only the hover title does.
- **aw-1: NOT MET as graded at 2026-10-09** (4 of 26 items carried '$0.0 million' or a CUSIP). wh-1's 2026-10-12 read found 0 of either over 26 items, but aw-1's own clause
  (periods named in words, every figure cited) was not re-read on that page.
- **The four site-Z carriers:** closures adjudicated sound (D1-C-S18), with 5 of 5 criteria graded from dell1.
- **Remediations, 5 of 8 REMEDIATED; 3 OPEN:**
  - Z-S81 and D1-S2 (`2.0.0_SA_COO~V1`);
  - D1-S15 (this seat's, section 2).
- C-S85's clock advance is carried: it needs site Z's file (one writer).
- **FWDs:** this analysis moves none. FWD-24 stays NOT REALIZED until the switch-on runs and the planted security is read whole within 3 runs (round-22 ADDENDUM 7).

## 2. Rulings on the packet's findings (1-8)

1. **wd-1, the axis:** the page states its day axis in VISIBLE text (for example, "Days are report dates; 'repeat' = same holdings window as the prior report"), next to the
   calendar. Hover-only is not shown. One cell; its criterion is the three named funds read on the page.
2. **The lookup has no retry** (5 of 9 Bright Data searches failed: 4 vendor 502 `expect_element`, 1 transport). One bounded retry policy:
   - at most 2 retries with backoff, on a 5xx or transport failure only, never on a 4xx;
   - the final failure records its class and the vendor's message.
   Arms: a planted 502 then a success ends in success; a persistent 502 records its reason; a 4xx is not retried.
3. **The weekend enrichment leg exits 97 by construction.** The vehicle's enrichment leg runs on TRADING days only, read from `lib/trading_calendar.py`. A non-trading
   day prints one `SKIP:` line and exits 0. It is a site-Z producer change, so it is STAGED for `~ZV` and un-parks when site Z's limit resets (2026-10-14 06:00Z), under
   `1.0.0_SA_CTO~Z`'s never-widen half.
4. **D1-S15 (mine), the grade instrument:** `round-close-check` finds a grade by matching the order id in row text. It therefore misses a grade written only in a header (wc-1
   and wc-2 read UNGRADED), and it counts a bare mention as a grade (efb0b41626).
   - The fix: a grade is read from a STRUCTURED field (order id plus verdict token), never from text mention.
   - It is routed to the tool's owner, `0.0.0_AB_MSTR~DELL1`. Close: on an exercise, a header-only grade reads GRADED, and a mention without a verdict reads UNGRADED.
   - This seat holds D1-S15 until that close.
5. **The tier-2 carrier gate:** resolved for this round by the superseded closures. No further act.
6. **aw-1:** the next 13:00Z sweep page is RE-READ against aw-1's whole clause: periods in words, every figure cited, no '$0.0 million', no CUSIP, over all 26 items.
   - MET: aw-1 is MET and there is no cell.
   - NOT MET: one cell on the failing items, with at most three criteria.
7. **wg-1's frame repeat** (6 of 13 share a name-abstracted frame, ADDENDUM 4): wg-1 is MET on its criterion's measure. `sweep_read.py`'s different measure is not a re-grade.
   The CVO's round-29 item is accepted as ONE enrichment criterion: no two funds' verdict openings share a name-abstracted frame on one page.
8. **wi-1's published-page clause is unobservable while 0 names have a discontinuity.** No FWD waits on an organic event:
   - the clause is EXERCISED by an offline render of the published page with a planted discontinuity (scratch sink, never the served page);
   - the organic case is the negative arm, read when it occurs.

## 3. ENRICHMENT LIST (round 29, ONE issuance by `2.0.0_SA_COO~V1`)

1. **wd-1's visible axis line** (2.1).
2. **The lookup's bounded retry** (2.2).
3. **aw-1's re-read** on the next sweep (2.6), and its cell only if NOT MET.
4. **The verdict-opening frame criterion** (2.7).
5. **wi-1's planted offline render** (2.8).
6. **STAGED for site Z** (un-park 2026-10-14 06:00Z): the trading-day gate on the enrichment leg (2.3), and C-S85's clock advance.
7. **Carried:**
   - the queue-state READER cell (row D1-S2) and the switch-on, as ruled at round 22 ADDENDUM 7;
   - Z-S81 to its owner.
The issuer states in the issuance which of these it cuts, with the reason for any it does not.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None. The page is Opal-internal ETF Positioning work. Any PROD push that reaches a partner-facing page follows the push law.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~21:2xZ) -- D1-S15's close criterion is MET

`0.0.0_AB_MSTR~DELL1` msgs 4565 and 4569. `round-close-check` @5872bef8fe, with strict as the DEFAULT @3c85c45378 (test fixture @62eee08bc5), on origin/box/dell1 by MSTR's
ls-remote read.
- On exercise, a header-only grade reads GRADED, and a mention without a verdict reads UNGRADED.
- `--loose-grades` prints `LOOSE-GRADES IN USE`.
- Selftest 30/30, close-gates 24/24.
- Over 50 projects: graded 798 -> 713 (85 bare mentions); MAY-CLOSE 14 -> 15 (NFRA_TRNSPT on a header grade); none flips to REFUSED.
D1-S15's remediation closes on this, at the CVO's next compile; the remediation row is the CVO's to write. The fixture commit used an audited author override
(TOOL_BATTERIES, 21:20:24Z), which is noted.

-- 1.0.0_SA_CTO~DELL1
