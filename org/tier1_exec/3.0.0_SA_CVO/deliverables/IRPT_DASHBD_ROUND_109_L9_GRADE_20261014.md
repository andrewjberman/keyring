# IRPT_DASHBD round 109 -- L9 grade of DB109-2-J1 (the first Inflection render)

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~18:4xZ. **Asked by:** msg 7801 (packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND109_B_DRAIN_END_20261014.md`, blob 9de51f92ce @62cad87c50).
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-215.*.md:39`):
- a reader cannot tell from the page which firm's plumbing produced it (only the firm title differs);
- every line that says a figure is unavailable or not held reads as plain words and cannot misinform;
- no account return or lot figure is implied that the source does not hold;
- the layout is the 49 Financial layout.

**Read by this seat:** all 20 pages of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r109/pages/run5/`, as images.
DB109-1-AC1, DB109-2-AC1 and DB109-3-AC1 re-run on HEAD: 3 of 3 PASS. No client figure is copied here. The benchmark percentages
quoted below are Opal model benchmarks, not client figures.

**Result: FAIL on clauses 2 and 3. Clauses 1 and 4 are met.**

## Met

- **Plumbing.** No custodian, platform or system name appears. Only the title reads "Inflection Wealth Management". The one firm-level
  sentence, "Account-level returns are not available for this firm yet.", states availability, not plumbing.
- **Layout.** Every section, table and column of the 49 Financial report is in place, in order.
- **Lots.** Lot figures are absent everywhere, and the lot sentence says so.

## NOT MET

1. **A wrong figure under a window it does not measure (pp.11-14).**
   - Accounts ending 0002 to 0005 have a column "Since 2026-06-15".
   - Its four Opal Model Benchmark rows print 8.3%, 11.7%, 27.6% and 39.0%.
   - These are exactly the household's "Since 2024-07-30" benchmark figures on p.4. A four-month benchmark return cannot equal the
     two-year one.
   - Under clause 3, this is a figure the source does not hold for that window. The likely seat of it is the account first-data date,
     which the contract derives from a return table this firm does not have (row W173-S2).
2. **A printed figure called unavailable (pp.15-19).**
   - Each account's "Gain or Loss Review, Last 12 Months" prints "Ending Value: Not available yet".
   - The same accounts' ending values print on pp.5-6 and pp.10-14: two read $0, three read non-zero values.
   - No note names the absent Ending Value. The only note there is about lots.
   - The issuer's whole-document rule reads 0 conflicts, so this pair is outside it.
3. **A false reason (pp.11-14).**
   - The benchmark rows for Year To Date and Last 12 Months read "Not available yet".
   - The note says they "need more history than is available yet".
   - P.4 prints the same benchmarks for those windows.
   - The true reason is that the account did not exist at the window's start. That is the not-spanned case, which has its own words
     since contract 0.4.3.
4. **Two reasons for the same cells (p.5).**
   - The household note says "Opal does not split net additions into contributions, withdrawals and income yet. The same applies to
     each account."
   - The four account notes below it say each account's Contributions, Withdrawals and Income "need more history than is available
     yet".

## Condition before any client render (the issuer's reading (a), not a count here)

The account labels read "Account ending 0001" to "0005". These are ordinals from the issuer's relabel ruling (D2-S36), so no real
number prints in this private sample. But "ending 0001" states an account number. A client render must print the real last four, or a
label that does not claim to be one ("Account 1"). Row W173-S9 stays ARMED until the real last-four rule is settled; the CTO carries
that as a data fact.

## Readings (not counts)

- **The $0 accounts.** Two accounts print $0 ending value beside four benchmark rows. That is true to the source, but a client may ask
  why a closed or empty account is shown. This is the issuer's reading (b).
- **A singular sentence over a table.** P.9 says "Lot-level detail is not available for this account yet." above a five-account
  table. Use "these accounts".
- **Page splits.** The holdings table splits across two sheets (pp.7-8), and the lot sentence sits at the top of a page apart from its
  heading. Both are cosmetic.

## Remedy

1. The account since-inception window takes the account's own first-data date for the benchmark comparison, or prints the not-spanned
   words. It never takes the household's figures.
2. The gain/loss Ending Value is filled from the same member the account overview prints, or that pair joins the whole-document rule
   with a note naming it.
3. Benchmark cells for a window the account did not span use the not-spanned words, not "needs more history".
4. One reason per cell: the account split-column notes defer to the household line.

-- 3.0.0_SA_CVO~DELL2
