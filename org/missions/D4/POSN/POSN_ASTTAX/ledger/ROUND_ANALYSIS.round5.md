# POSN_ASTTAX -- ROUND 5 ANALYSIS (L10)

**From** `1.0.0_SA_CTO~Z`, L2/L4 owner, answering `3.0.0_SA_CVO~Z`'s round-5 slug
`surprise-channel/remediations/REMEDIATION_v5.Z.md` @`1edf35dbc3` (L9: `surprise-channel/adjudications/ADJUDICATION_v7.Z.md`).
**2026-09-15 ~03:0xZ.** Portal gitlink `e85f6eb84f`, unmoved; round-5 portal work on `refs/drains/posn-5-portal` `dd1d33c6db`,
behind the freeze. No promote, no DEV/PROD push.

> **VERDICT: PRD ADDENDUM v0.9 LANDS WITH THIS ANALYSIS, AND THE RECUT IS A THREE-CELL ROUND 6 -- B6, F4, F5 -- CUT TONIGHT.**
> Round 5 built and deployed what its nine cells named, and CVO~Z found every instance valid. Andrew then read the page and
> ruled three things round 5 never specified: a class no book in the view holds is not shown (~00:4xZ, ~02:1xZ), each satellite
> holding shows its own characteristics and performance (~02:1xZ), and it is fixed tonight (~02:3xZ, *"we're not waiting for the
> next day"*). v0.9 appends `FWD-7` and four constraints. `2.0.0_SA_COO~Z` cuts ONE round-6 issuance once both L4-R halves of v0.9
> read SIGNED at current bytes.

---

## 1. COVERAGE -- the subtraction, measured this tick

```
DENOMINATOR   28 task orders under POSN_ASTTAX (24 complete, 2 superseded, 2 cancelled; 0 open)
DECLARED       7 (FWD-1..FWD-7, v0.9)
COVERED        6
UNCOVERED = declared MINUS covered = { FWD-7 }     <- appended at v0.9; round 6's B6 and F4 name it

  FWD-1 19 orders   FWD-2 7   FWD-3 3   FWD-4 3   FWD-5 5   FWD-6 6   FWD-7 0
```
Instrument: every `task-orders/*.md` read whole, `<status>` parsed, outcome ids matched as whole words `FWD-<digits>`;
FWD-1..FWD-6 are the positive controls of the same match. **NOTED, NOT A GAP:** `TO-V4-1` (B4, the characteristics lambda)
names no outcome id, so the census credits its work to no order. It changes no count above, because FWD-6 is named by six others.

WARN: **NAMING IS NOT SERVING (the v0.6 qualifier still binds).** Six outcomes named is not six served; s.5 grades them.

## 2. WHAT ROUND 5 ESTABLISHED

| cell | order | landed | carried into |
|---|---|---|---|
| B1 | `TO-V1-1` | both positioning generators deployed; five-class keys and labelled-zero benchmark rows served | done |
| B2 | `TO-V2-1` | `holdings.json` served beside `registry.json`, one Black Diamond total per ticker, nine satellites | R2 relabel tonight (s.6) |
| B3 | `TO-V3-1` | the seeder guard | `C-S138` docstring, next tooling edit |
| B4 | `TO-V4-1` | `cot-satellites-characteristics-producer` deployed, per-satellite aggregates | **B6** (`C-HOLDING-MEASURES`, `C-B4-SCHEDULE`) |
| F1 | `TO-V5-1` | the colour registry, Structured pink family, Commodities yellow | `C-S139` (one yellow for Metals and Commodities), carried |
| F2 | `TO-V6-1` | the Positioning page renders the five classes | **F5** |
| F3 | `TO-V7-1` | the Satellites mode reads the served artifacts, no arithmetic in the adapter | **F4**, **F5** |
| R1 | `TO-V8-1` | the retag, thirteen tickers, both stores, both levels | the served Satellites labels (s.6) |
| B5 | `TO-V9-1` | the edge router admits the two new leaves | `C-S135` (MFA-capable probe at the integration cut), carried |

CVO~Z: nine of nine proof instances structurally VALID; 232 of 232 investigation originals dispositioned (`@1edf35dbc3`).

## 3. ROUTING THE SLUG'S THREE REMEDIATIONS, AND WHAT RIDES WITH THEM

| id | remedy asked | disposition |
|---|---|---|
| `C-S142` | one presence set per render for legend, rows, count and bars; order and colours kept | **v0.9 `C-PRESENT-CLASSES` -> F5** |
| `C-S143` | the Satellites footer binds to the served holdings' date and source | **v0.9 `C-SUMMARY-COPY` -> F5** |
| `C-S144` | per-ticker measures from B4, attached by the adapter without arithmetic, MC / Active / Credit sourced or omitted explicitly | **v0.9 `FWD-7` + `C-HOLDING-MEASURES` -> B6 + F4.** Sourced, not omitted: Yang's `current_holdings` rows carry all seven panel fields for 23 of the 25 satellite tickers; the Bloomberg fallback maps `aum <- FUND_TOTAL_ASSETS` (equal to Yang's `aum` on 5 of 5 shared tickers) and publishes `active` / `credit` NULL; CASH has no source |

**Riding the same cells (seat rows, already carried):** `Z-S117` label rounding and `Z-S115` blend copy -> F5; `Z-S120` /
`Z-S130` B4's schedule before its input -> B6 (`C-B4-SCHEDULE`).

**Graduated by L9, not round-6 cells:** `C-S135` (an MFA-capable authenticated probe, at the integration cut), `C-S136`
(`record-terraform-deploy.sh` banner vs its bun fallback -- deployment tooling owner), `C-S138` (seeder docstring -- next edit
of that file), `C-S139` (a second yellow for Metals is a palette expansion; the laptop's name-keyed colour rule, msg 22957,
is where it is decided).

The disarm of `C-S142`, `C-S143` and `C-S144` is a NEW citing row by this seat once both v0.9 halves read SIGNED -- a disarm
that cites an unsigned spec cites text that may still move.

## 4. L4 GUIDANCE THAT MUST REACH THE ROUND-6 CELL TEXT

1. **B6's discriminator is B4's own purity.** `build()` is pure; the bar runs it at HEAD's code and at the cell's code over the
   SAME three inputs and requires the two artifacts, minus the new `tickers` block, to parse identical. The `tickers` block
   carries every ticker any satellite holds, once, with its `source`.
2. **B6 deploys through Terraform, then is DRIVEN** with an explicit `bbg_as_of` (the handler already accepts it,
   `lambda_function.py:82-83`). The never-widen halves print `characteristics.json`'s writer census, cover both branches, and
   name the rescheduled rule's next fire as the organic leg. No wait (Rule 27).
3. **The schedule is `cron(30 12 * * ? *)` UTC** -- after the 07:00 America/New_York pull in both DST states -- never
   success-of-upstream.
4. **F4 depends on B6 DEPLOYED, and its bar reads served bytes.** The edge caches `/api/scoped/satellites/*` under
   `opal-scoped-advisor-by-firm` (DefaultTTL 60 s); fixtures, where a criterion needs them, are built from the served bytes
   and name their VersionId (`C-S135`: the committed credential fixtures are MFA-gated).
5. **F5's presence set spans every column the current view draws** -- portfolio columns, and benchmark columns in the
   Benchmark / Relative / Custom views -- and is taken per mode, never across modes. Colours stay keyed by class name. The
   zero-row design comment at `PositioningSummary.tsx:575-577` is removed with the behaviour.
6. **F4 and F5 are disjoint files and run in parallel.** Portal commits land on a round-6 drain ref cut from
   `refs/drains/posn-5-portal` `dd1d33c6db`, recorded in `ledger/PORTAL_REFS.md` at its first commit; the gitlink does not move.
7. **F5's Satellites bar reads the RELABELLED `holdings.json`** (s.6): four classes present (Fixed Income, Equity, Structured,
   Commodities). Models lists three (Fixed Income, Equity, Structured).

## 5. STATE -- 0 of 7 REALIZED

- **FWD-3, FWD-4, FWD-6 cannot be REALIZED on the served portal while the freeze stands.** F1-F3 are built and verified on the
  drain ref and served to no user; the promote is Andrew's separate word. That wait is his, expressly, not a coast.
- **FWD-1, FWD-2, FWD-5** -- R1 landed in both stores and the Yang-served payloads carry it; the served Satellites
  `holdings.json` still labels GLD `hedge` and VXX `equity` until the relabel (s.6), so the Satellites arm reads unrealized.
- **FWD-6** additionally owes F5 (`C-PRESENT-CLASSES`, `C-SUMMARY-COPY`).
- **FWD-7** is new and uncovered until B6 and F4 are cut.

## 6. ALSO THIS SESSION, OUTSIDE THE ROUND

- **R2, tonight's Satellites relabel -- a CTO act, not a cell.** The deployed registry producer (zip == CodeSha256; four modules
  byte-identical to HEAD) run with `--as-of 2026-09-14`, because its Lambda passes no date and the 2026-09-15 roster lands
  ~06:00:43Z. No-write capture already measured: `registry.json` identical; `holdings.json` 30 label cells (GLD x7, VXX x8), 0
  other differences. CTO half R2 @`d1685fb4ea`; **the COO half is owed before any write.** The 07:00Z fire stays the organic leg.
- **Card-4 ledger `posn-bbg-etf-pull-gld-vxx`:** L2 is the 2026-09-15 07:00 ET scheduled pull, unchanged.
- **Relayed, not taken:** msg 22963 (laptop, D1_CATVIEWS L1 presence shows a zero bucket as $0). Site Z works POSN_ASTTAX only by
  Andrew's word; the opposite presence semantics of that page and this one are his to reconcile.

---

**PRD ACTION: ADDENDUM v0.9 LANDED WITH THIS ANALYSIS.** `3.0.0_SA_CVO~Z` re-signs the ratified-text half (FWD-7 appended);
`4.0.0_SA_CRO~Z` re-signs the brief half (four constraints). **The recut is `2.0.0_SA_COO~Z`'s: ONE issuance of B6, F4 and F5,
after both halves read SIGNED.** This analysis cuts nothing.

Push state: LOCAL (this seat never pushes; `0.0.0_AB_MSTR~Z` carries).
