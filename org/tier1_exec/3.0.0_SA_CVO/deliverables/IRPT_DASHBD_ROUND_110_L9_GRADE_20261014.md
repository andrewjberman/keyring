# IRPT_DASHBD round 110 -- L9 grade of DB110-3-J1 (the Inflection re-render)

**Grader:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~21:2xZ. **Asked by:** msg 7856 (packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND110_B_DRAIN_END_20261014.md`, blob 84a8391b89 @ae515651ad).
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-223.*.md:37`):
- a reader cannot tell from the page which firm's plumbing produced it;
- every unavailable or not-held line reads as plain words, gives its true reason and cannot misinform;
- no figure is printed under a window it does not measure;
- the layout is the 49 Financial layout.

**Read by this seat:** all 20 pages of `C:/dev/_irpt_private_evidence_20261009/fwd21_sample_r110/pages/final/`, as images.

**Recomputed by this seat:** the account since-inception benchmark windows, from the served model series
(`opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`, VersionId 9wcMYjBbgI9j...). I used the project's own reader,
`model_series_windows.windows_from_series(as_of 2026-10-13, first day 2026-06-16)`. Result: Ultra Short 0.1%, Short -2.3%,
Intermediate -0.4%, Long 0.6%, equal to pp.11-14. The Short -2.3% beside a year-to-date 0.1% is consistent: quarter to date for an
as-of of 2026-10-13 opens on October 1, not July 1.

**Re-run on HEAD:** DB110-1, -2, -3, -5 and -6-AC1 PASS. DB110-4-AC1 to AC3 read FAIL on main because they read the portal worktree,
which main's portal checkout is not at. The packet records them PASS in the worker's tree, and this seat does not re-grade them.
These benchmark figures are Opal model benchmarks; no client figure is copied here.

**Result: FAIL on one count, the account labels. Every round-109 count is fixed.**

## Round 109's four counts -- all fixed

1. **Own since-inception window.** Accounts first held on 2026-06-16 carry their own "Since 2026-06-16" benchmark column, recomputed
   above. They no longer carry the household's since-2024 figures. The household's own since-inception benchmarks read "needs more
   history". That is true: the served series opens 2024-04-30, after the household's 2020-05-26.
2. **Gain/loss Ending Value.** Each account's gain/loss review (pp.15-19) prints the same ending value as its overview (pp.10-14) and
   the activity summary (pp.5-6).
3. **Not-spanned words.** Windows an account did not span read "This account did not exist at the start of this period."
4. **One true reason per cell.** The split sentence prints once at household level. The account notes give the not-spanned reason,
   which is also true for those accounts.

The household return now prints for QTD, YTD and the last 12 months. Its claim is stated in the contract.

## NOT MET -- the account labels

- **What prints.** Three account labels read "Account ending 4INT", "Account ending tion (1 of 2)" and "Account ending tion (2 of 2)",
  in the headers, tables and page footers (pp.5-6, 9, 12-14, 17-19).
- **Why that fails.**
  - "Account ending" promises the last characters of an account number. These are fragments of a text field.
  - A client cannot read them as an account, and they show the shape of the platform's identifier on the page. That is the first
    clause: the page reveals its plumbing.
  - Under the second clause, they cannot misinform only if they do not claim to be a number.
- **Remedy.** The issuer's ask to the CTO: fall back to "Account <n> of <N>" (household order) when the custodian number has no run of
  digits, and keep "Account ending NNNN" where it does. Once the CTO rules, this is one render rule. This seat would re-read the label
  pages only.

## Readings (not counts)

- Two accounts end at $0 beside benchmark rows. That is true to the source.
- The p.3 chart legend touches the chart frame. This is cosmetic.
- The narrow holdings columns wrap "Not available yet".

-- 3.0.0_SA_CVO~DELL2
