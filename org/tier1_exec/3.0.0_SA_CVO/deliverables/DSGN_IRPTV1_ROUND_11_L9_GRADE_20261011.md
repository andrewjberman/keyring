# DSGN_IRPTV1 round 11 -- L9 grades (four judgments)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11 ~06:5xZ.
**Inputs:** msg 4273 (IV-e-82, IV-e-84, IV-e-86 drained @fb60e94fd8, @1bbdf8ba8e, @3863a42ce4) and msg 4276 (round 11 fully drained
@8f6e2524d5). Records under `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/`.
This seat ran no portal test. Code reads are at portal origin DEV `6f70e36b` and candidate `1cd1cf25`.

| judgment | verdict |
|---|---|
| IV-e-82: the 43 proposed rulings | **29 REGRESSION: ACCEPTED. 14 KNOWN-LEGACY: NOT ACCEPTED as labelled** |
| IV-e-84: the press test through React's private hook dispatcher | **ACCEPTED, with one condition** |
| IV83-AC2: the corrected row reads unambiguously and follows DESIGN.md | **MET** on the candidate's render |
| IV85-AC2: the decision NEEDS_SERVED_ROUTE follows from the cited code | **MET** |

## 1. IV-e-82 -- the three-run sample and its rulings

- **The sample holds.** `SUITE_SAMPLE.json`: three runs at portal `7bb81fa8`, 1,087 pass / 27 skip / 43 fail each, and the three
  failing sets are the same 43 ids (this seat compared the three lists in the record). The 43 rulings cover exactly that set. That is
  the sample rows W23-S1, W29-S10 and W34-S1 were waiting for.
- **29 REGRESSION: accepted.** 18 are contract-against-portal drift (the contract is ahead of the portal half), 6 spawn `bun` at a
  path under another user's profile, 5 are named in no row.
- **14 KNOWN-LEGACY: not accepted as labelled.** Each basis shows the failure was named in an earlier row. None of the 14 cites a
  ruling that retires the assertion. Row S7's remedy allows two outcomes only: a regression to fix, or a legacy assertion retired by
  the CTO's ruling. "Named before" is neither. These 14 are KNOWN and UNRULED. Nine of them are matched to row S59 by suite family,
  not by test id.
- **Three of the 43 deserve an early look**, whatever their label:
  - `fe-s-1/source-bounds`: two portal source files carry a forbidden vendor token. That is a live bound failing, not a stale test.
  - `fe-s-40/window` F40-AC5: the portal calendar disagrees with `lib/trading_calendar.py` (fallback years 2010 against 2024).
  - `fe-s-47` F47-AC6: recorded red in row S56 and fixed in S57 on 2026-10-03; it is red again.

## 2. IV-e-84 -- the press test

- **It has teeth.** Both mutants the earlier row named fail it (the worker's runs): a handler that fills nothing, and one that
  fills another ticker. The handlers pressed are the component's own closures.
- **Why the mechanism is tolerable here:** the portal installs no DOM and no test renderer (`package.json` holds `react` and
  `react-dom` only), so no supported way to press a button exists. If React changes the internal it reads, the test throws; it
  cannot pass silently.
- **What it does not do:** effects do not run, and only the component's own element tree is walked, so a button inside a child
  component would not be found.
- **Condition:** it stays the only test of its kind until the CTO decides how the portal presses things (install a DOM test
  library, or bless this dispatcher as one shared helper). `react` is pinned by caret (`^19.2.4`); the internal is not a public API.
  It is the single test in the portal that reads React internals (this seat's search of origin DEV).

## 3. IV83-AC2 -- the corrected Holding cell (candidate `1cd1cf25`, not on DEV)

- **Reads unambiguously.** Read from both screenshots: "APPL, analysed as AAPL" and "FBIFX, analysed as SGOV", with "MSFT" alone on
  the uncorrected row. The wording equals the disclosure list printed above the table. "uploaded as" appears nowhere.
- **DESIGN.md, the three named points:** navy ink on white; the one added class is the existing navy palette token at the small text
  size, so no new colour; numerals are tabular through the page-wide rule (`index.css` body, `font-variant-numeric: tabular-nums`).
- **The product change is one cell:** 14 lines in `ProspectComposer.tsx` against DEV `6f70e36b`, reading the served
  `disclosures.corrections[].to_value`. Nothing is derived on the page.
- **Limits.** This is a local build with three stubbed requests, not a served page. Two things the render shows that this cell did
  not introduce: the two dollar columns are left-aligned, where DESIGN.md C2 says figures right-align; and the disclosure line calls
  a spelling correction "a proxy you named".

## 4. IV85-AC2 -- Export on Analysis

- **The decision follows.** `index.tsx:311` hard-codes the Analysis export gate closed; `AnalysisTab.tsx` publishes no export
  target; `retained_ref` exists on the Performance wire only (`contracts/wire/PerformanceReport.ts:64`). An Analysis export needs a
  retained report's id, revision and hash, and no Analysis response serves one. Wiring a prop would invent a payload.
- The criterion's second clause (an exported file holds what the tab shows) does not apply: nothing was wired, and no product file
  changed. The CTO has ruled on it (msg 4234).

## Still owed by this seat

The grade row and the round 11 adjudication. The project's `INVESTIGATION_v1.md` carried another seat's uncommitted edit when this
file was written; they land once that edit is committed.
