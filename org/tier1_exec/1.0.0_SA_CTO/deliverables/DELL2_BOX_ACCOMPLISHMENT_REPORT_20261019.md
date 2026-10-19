# Dell2 box: accomplishment report (as of Monday 2026-10-19, ~11:40 AM ET)

**Asked by:** ms (Muse, Andrew's operator agent), "on Andrew's word", relayed by the dell2 manager (msg 10748).
**Written by:** the dell2 CTO, `1.0.0_SA_CTO~DELL2`.
**Scope:** the 9 projects placed on dell2, out of 58 projects scanned:
- IRPT_DASHBD, IRPT_BCKEND, IRPT_ANLREQ, IRPT_YCDGEN, DSGN_IRPTV1 and IRPT_CUSTDY (closed);
- TCKT_VNEXT;
- NFRA_TRNSPT and NFRA_OPSWKF.

All 16 dell2 seats were live at 9:0x AM ET today. Times are US Eastern unless marked Z (UTC).

**What happened over the weekend:** the box went offline on Saturday evening and came back this morning. Saturday's work
reached the shared branch at 8:59 AM. Nothing was lost.

---

## 1. Ticket Center: the Analysis Request flow

**Where it stands:** an Opal staff member files an Analysis Request in Ticket Center on the live portal (opalinvest.dev),
naming the firm's advisor and attaching a holdings file. The report is generated and recorded on the ticket.

- **Live since last week:** portal releases v2.1.233 and v2.1.234. They carry:
  - the request form;
  - the fix that stopped the report from being recorded (the revision was sent as a number, not text);
  - the decision tree, the filing notice, the commentary link and the partial-history sentence;
  - the date-only fix;
  - a readable meeting outcome line, at a contrast of 10.1 to 1.
- **Today:** the Analysis Request code on the live portal is identical to the test portal (0 files differ).
- **A defect found in Andrew's live demo this morning:** the report page showed 425 empty cards titled "text". This is
  a report-server bug, not a portal bug: the server handed the page every layout item, including fixed text the PDF
  draws itself.
  - The fix is merged. The page drops fixed-text items and "not in this version" items; the latter become one line
    with their count. Every real value is unchanged.
  - It ships in today's report-server update (target ~1:00 PM ET). Reports filed after that are clean.
- **Commentary on a request:** not live yet. The live portal does not yet ask for a commentary, and the step that turns
  a commentary into a PDF has not passed its end-to-end test.
  - Three test runs found and fixed two gaps in the test itself: the advisor was missing, and an upload had to be
    re-sent while it was still processing.
  - The third run reused a stale upload, so it proved nothing. A fourth run with a fresh upload is approved.
  - "Always ask for a commentary" goes live the same day a commentary PDF opens.
- **The report's price pages** (returns, risk, benchmark, Beta and Alpha): Andrew lifted the "no pricing in v1" hold
  today.
  - 9 price-based items already show values.
  - The remaining 17 are being built now (round 57).
  - A per-holding price table, showing each price's date and source, is being added.

## 2. The live portal release under way now (Andrew's word at ~10:2x AM)

Andrew asked for all dell2 portal work to be on the live portal, and later lifted all holds. A single release is being
built on top of the live version, with typecheck, lint, tests, build and a file-by-file list as its checks. Target:
~11:30 AM ET. It carries:
- the Investor Reporting Performance tab work (43 files): the performance report and its export, the holdings panels,
  and the chart that draws measured stretches with breaks;
- the Trade Request form (6 changes), now shown in the New Ticket list. Its file-upload service is configured on the
  live system; its storage permissions were not read.

Excluded: 5 files that are dell1's work.

After the release, the Ticket Center live check runs (filing and confirming a meeting request) on the released page.

## 3. Investor Reporting: data and pipelines

- **49 Financial:** the first scheduled run with the new transaction table PASSED this morning. It took 8.2 minutes
  against a 12-minute limit, peaked at 5.8 of 6.5 GB, had 0 errors and wrote 26 days of transactions. That change is
  closed.
  - Open: 49 Financial's holdings update has been refused 4 times since Oct 14, because accounts drop out of the
    holdings. The served holdings stay as of Oct 12.
  - A third missing account is being read; an exemption extends to it only if it is missing at the source for the same
    reason. A review of every exemption is set for Oct 26.
- **Inflection:**
  - Its returns feed ran its first scheduled day cleanly: 294 of 294 households, 795 accounts with returns and 68
    without (39 have no start date at the source).
  - The transaction table goes live on Tuesday 10-20, re-pinned today so it keeps a dell1 fix to the same shared
    script. That script's single owner is now settled across boxes: dell2's operator.
  - A history backfill (2,326 days, back to June 2020) is approved. It runs once the raw-file fix proves itself; that
    fix avoids tens to hundreds of GB of duplicate files.
- **Cottonwood:** the reported cash flows were inflated 8 to 13 times, because overlapping 14-day pulls were summed.
  - The reader fix is signed off. It ships after Inflection, followed by a rewrite of every day since July 10.
  - Separately, Cottonwood's client directory has not refreshed since Oct 12. A failed build blocked every later run.
    The fix is approved, and the 6 clients the safety check refused are being traced before anything is forced.
- **Class returns by asset class:** the data contract is done. Publishing waits until the Cottonwood rewrite, so class
  returns are never built on wrong daily returns.

## 4. NFRA projects on dell2

- **NFRA_TRNSPT** (the Opal communications database: Teams transcripts, market updates, investment notes): at
  ROUND_CLOSE. Its last round closed at the drain on Oct 14.
- **NFRA_OPSWKF** (trade submission through Opal, led by the operations lead's Excel workflow): EXECUTING. Its
  Ticket Center front end is the Trade Request form going live today, above.

## 5. Other

- **IRPT_YCDGEN** (Opal-branded YCharts generation): at ROUND_CLOSE. Its price pages are covered in section 1.
- **DSGN_IRPTV1** (the Investor Reporting page remediation): all 84 orders are terminal (75 complete, 9 superseded) as
  of Oct 11.
- **IRPT_CUSTDY:** closed.

## Waiting on Andrew

Nothing on dell2. All 5 open items were closed today on his word. The one item in his hands is sending the
Inflection start-date email, which is approved, with the draft ready for him; it needs his Inflection operations
contact.

## Not dell2's

ms's other request, to stop drafting replies on Andrew's own emails, belongs to COMM_ASSIST, which is placed on the
laptop. It was passed to the laptop CTO with ms's rule verbatim.
