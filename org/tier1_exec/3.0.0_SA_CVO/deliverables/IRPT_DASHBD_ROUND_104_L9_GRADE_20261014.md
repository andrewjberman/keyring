# IRPT_DASHBD round 104 -- L9 grade of DB104-1-J1

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~12:0xZ. **Asked by:** msg 7566, corrected by msg 7570. Packet:
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND104_B_DRAIN_END_20261014.md`, blob 02d3d6ccbe
(@8a1b544b3e).
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-197.*.md:39`), a re-grade of round 103's J1 with two clauses:
- every client-facing line that says a figure is unavailable or not held reads as plain words a client understands, and cannot misinform;
- the holdings table stays in the baseline's orientation.

**Read by this seat:** all 14 pages of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r104/pages/r104_final/`, as images.
I re-ran DB104-1-AC1 to DB104-5-AC1 on HEAD: 5 of 5 PASS. No client figure is copied here; only page numbers, row labels and counts.

**Result: FAIL on the first clause; the orientation clause is met.** Round 103's two defects are fixed. The new defects are in what
the notes tell the client, not in how plain the words are.

## Fixed since round 103 (met)

- **Unheld classes print the dash.** On p.6, Alternatives, Commodities and Unclassified print the baseline's dash (3 of 3).
- **The chart title is honest.** P.3 reads "Opal model benchmark returns, last 12 months" and draws the four benchmark lines.
- **Kind notes name their figures.** No bare "This figure ..." line is left.
- **Orientation is unchanged from round 103.** On p.6, classes are rows and the baseline's columns are in order. The sub-class level is
  said in words.

## Clause 1 -- NOT MET, on three counts

1. **A note says a figure "needs more history" while the same report prints that figure.**
   - P.5, Activity Summary, Last 12 Months: the Household row and all three account rows read "Not available yet" for Beginning Value and
     Net Gain. The note above says these "need more history than is available yet".
   - P.3 prints the household's last-12-month Beginning Value. P.4 prints its last-12-month Net Gain. Pages 8 to 10 print each account's
     last-12-month Beginning Value and Net Gain, and the three accounts sum to the household's figures on p.4.
   - P.6 says the household's Net Gain "needs more history" for all four windows. P.4 prints the household's Net Gain for those same
     four windows.

   A client is told the figure does not exist yet, and it is on another page. That misinforms. Either the absent cell takes the value
   the same report already prints, or it says why this table cannot show it.
2. **A section note contradicts the table under it.** P.8 opens Account Overview with "Return (Cumulative), Since 2024-07-08;
   Return (Cumulative), Last 12 Months: is not available yet." Directly below, account 9269 prints a last-12-month return. Only one of
   the three accounts (p.10) lacks that figure. Either the note sits with the account it describes, or it names that account.
3. **Template slot names print as client lines, and the report points the client to a page that is not there.**
   - P.1 labels a row "Accounts, each with its registration name and last four digits".
   - P.4 labels rows "Since-inception column heading" and "Footnote for a window not held for the entire period".
   - P.6 labels a row "Class hierarchy".
   - The asterisks on "Net Gain*" and "Return (Cumulative)*" point to no footnote.
   - Every page says "This report is incomplete without the accompanying disclosure page". P.14, the disclosure page, reads "Not
     available yet".

   A client does not know what a "window not held for the entire period" footnote is. A client cannot follow a pointer to a disclosure
   that is absent.

The notes are also hard to read: long runs joined by semicolons and closed by ": is not available yet." (p.2, p.5, p.6). This alone
would not fail the clause.

## Remedy (one render cell)

- An absent cell never claims "needs more history" for a figure the same report prints. Fill it from the same served member, or give
  the true reason ("not split into contributions and withdrawals yet").
- A section note names the account it describes, or sits beside it.
- Slot names become client words, or the line is dropped while its member is absent: a row heading, a footnote that does not exist,
  "Class hierarchy". An asterisk prints only with its footnote.
- While the disclosure page is absent, the footer does not point to it, or the report is not issued. That is the CTO's call: the
  disclosure page is likely a release gate, not wording.

-- 3.0.0_SA_CVO~DELL2
