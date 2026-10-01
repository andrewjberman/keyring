# CONTRACT -- AMGT Friday demo: the shared surfaces between RESAPP, DSGN_AMGTV1, HARVST and CORPUS

**Author:** `1.0.0_SA_CTO~Z`. **Placed:** 2026-10-01 ~04:4xZ. **Placement:**
`../CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md` @e18d3a4e6a.
**Source:** `docs/briefs/amgt-security-analysis-friday-demo-brief-20261001.md` @1391c2f70a, Parts II and VII.1.
**Rule:** each surface has ONE writer. A reader that needs something the writer does not serve asks the writer
for a cell. It never works around the gap on its own side. A change to this page is a CTO amendment, not a cell's
choice.

## 0. Writers

| surface | the one writer | readers |
|---|---|---|
| every served field and route under `/api/scoped/amgt` | AMGT_RESAPP (`2.0.0_SA_COO~Z`) | DSGN_AMGTV1 |
| page presentation (`portal/src/pages/SecurityAnalysis/**`) | DSGN_AMGTV1 (`2.0.0_SA_COO~D`) | Andrew |
| the Model tab's row shape (`modelSheet.ts`) and the model blocks it reads | AMGT_CORPUS (`2.0.0_SA_COO~X`) | DSGN_AMGTV1 renders it unchanged |
| harvest bronze/silver/gold under `opal-data-harvest/amgt/harvest/` | AMGT_HARVST (`2.0.0_SA_COO~H`) | AMGT_RESAPP (routes), never the page |

## 1. The monthly chatter route (O1; the bubble chart's dependency)

- **Where:** the already-mounted template `GET /api/scoped/amgt/lead-panel/timeseries/{movement}/{subject}`, with
  `movement=collected` and `subject=chatter`. Riding a mounted template means no gateway or terraform change.
  RESAPP's cell verifies this assumption against the handler's dispatch and the mount test
  (`lib/research/api/tests/test_scoped_amgt_mount.py`). If it is false, the cell says so in a surprise row. It does
  not mount a new route on its own.
- **Response shape (JSON):**
  ```
  {
    "as_of": "YYYY-MM-DD",              // the newest gold day read
    "source": "harvest gold chatter_daily",
    "months": ["2026-01", ..., "2026-10"], // ascending; the current month is partial and says so
    "partial_months": ["2026-10"],
    "rows": [
      { "security_key": "...", "display_name": "...",
        "by_month": { "2026-09": { "collected": 12, "by_publisher": {"sa": 7, "wsj": 3, "bbg": 2, "ft": 0, "barrons": 0} } } }
    ]
  }
  ```
- **`collected`** is the raw count of collected articles that name the security in that calendar month. It has
  **no coverage gate**: partial publisher coverage still counts (R11). A month with nothing is absent from
  `by_month`; it is never written as a zero row.
- One call returns every month. The page's month cursor flips client-side, with no fetch per step.
- **Label:** the page captions sizes as "articles collected", never as "market chatter" (brief VII.4).

## 2. Price bars (O2)

- **Where:** the existing `GET /api/scoped/amgt/lead-panel/rankings/trending/price`.
- **Field added:** `return_30d_pct` (signed percent, e.g. `9.2` means +9.2%) on every row, over the 95-name covered
  universe. The page sorts descending by its absolute value, longest bar first, sign shown by colour.
- **Breakout** fields are served in percent and named `*_pct`. The page displays them as served and never
  multiplies by 100. This resolves the "+0.09%" defect on the RESAPP side only: DSGN removes its own scaling and adds
  none.

## 3. Dates (O4)

- **Server-side fallback:** a per-name or ranking read for date D serves the latest served trading day on or before D
  and returns that day as `as_of`. T-1 is the normal case.
- **The page never constructs a date.** It renders `as_of` as the label. A header cell is empty only when the server
  says `absent` with a reason.
- **The "Breakout (price)" cell** reads the breakout row's value, served by RESAPP under its own field name.

## 4. Absence vocabulary (O3, O4, O5)

- A served field is shown. The words "not served", "unsupported", "ABSENT" and "REFUSED" never reach the page for a
  field the route serves.
- A truly absent value carries `absent_reason` from the server. The page renders DSGN's designed empty state with that
  reason in plain words.

## 5. HARVST to RESAPP

- RESAPP reads gold `chatter_daily` and `article_security_mention` through `lib/research/coverage/pool_reader.py`,
  the same reader the timeline routes use. It runs no hand-rolled S3 sweep.
- Rows HARVST quarantines (the sa wrong-object rows) leave gold before the route counts them. HARVST owns the
  quarantine, and RESAPP counts what gold holds.

## 6. Fixtures

- DSGN builds O1 and O2 against fixtures with exactly the shapes in sections 1 and 2, committed beside its cells.
  When RESAPP lands a route on DEV, DSGN's wiring cell swaps the fixture for the route with no shape change.
- A shape mismatch between fixture and route is a surprise row to `2.0.0_SA_COO~Z` (the writer), never a page-side
  adapter.
