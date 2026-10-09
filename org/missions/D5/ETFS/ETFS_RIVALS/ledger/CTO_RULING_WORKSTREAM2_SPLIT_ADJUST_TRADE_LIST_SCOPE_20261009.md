# CTO ruling -- ETFS_RIVALS WORKSTREAM 2, released NOW: split-adjusted history + dramatic-move lookup; the trade list scoped to the toggle

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~05:2xZ, on `2.0.0_SA_COO~V1` msg 1758. **Andrew's words and measurements:**
`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @9d08dd64d4. He asked for
this as work "you can go pursue in the interim", so it runs now and does not wait for round 29.

## Placement

Rule 27: a workstream is a scope, not a round. Round 28 stays frozen on its three acts (the aw-1 deploy, the tc-1 merge, the
switch-on). **Workstream 2** is issued by `2.0.0_SA_COO~V1` (one project, one issuer) as its own issuance, with a write surface
disjoint from those acts. Each item is a build cell with at most three mechanical criteria.

1. **WS2-a, split-adjusted series** (comment 1, items 1-2).
   - Every price series the page draws is adjusted for share-count corporate actions, from STORED corporate-action rows: the dialog
     curve, the holding-implied points, the trade-marker prices and any return read from closes.
   - The factor and its source row are recorded with the series, and the dialog says when a series is adjusted.
   - Proof: TKOMY's 30d curve on a served page reads continuous across 2026-10-07, with the factor 15 read from a row, never typed.
2. **WS2-b, the missing action and the dramatic-move lookup** (comment 1, items 3-4).
   - A stored close past 3x, or below one third, of the prior stored close triggers a web search for that security's corporate action
     on that date (egress is open, law 4d77a9c3ea).
   - A split, reverse split or merger found with its ratio is stored as a corporate-action row carrying its source URL and
     `claim: inferred`, never `measured`.
   - Found nothing: the point is a gap with its reason, never drawn.
   - The gap behind it: the stored actions hold no TKOMY row. If the fix is a Bloomberg field the enrichment leg does not request
     today, that request is a Bloomberg draw and goes through MDPF_DEMQUE's queue as a quoted request.
3. **WS2-c, trade list scoped to the toggle** (comment 2).
   - The dialog's trade list shows only the toggle's window (30, 90 or 365 days), behind a closed disclosure.
   - Its heading names that window, and "Trades in the Last 365 Days" never shows on 30d.

## Guards (a criterion of EVERY workstream-2 order)

1. **No deploy before round 28's reads.** Nothing deploys a rivalfunds Lambda, the gateway or the page, and nothing writes a served
   rivalfunds key, before both round-28 J1 reads are taken: tw-1 at the 11:00Z vehicle run and aw-1 at the 13:00Z sweep. Merged code
   does not reach those runs; only a deploy would.
2. **Disjoint write surface.** No edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py`, which is tc-1's and the round-29
   reader cell's. A cell that finds it must edit that file files a row and stops.
3. **Deploys and served writes go under their own never-widen pair** (this seat's half plus the COO's). The corporate-action rows from
   WS2-b are a served write. The vehicle is a site-Z producer, so any change its run imports also needs `1.0.0_SA_CTO~Z`'s half.

The round-29 pre-draft (`ledger/ROUND_ANALYSIS.round29.PREDRAFT.md`) is unchanged: WS2 is not in it.

## ADDENDUM 1 (~05:5xZ) -- Andrew's comments 4-8 (record @588865eef8; `2.0.0_SA_COO~V1` msg 1851) become WORKSTREAM 3

WS2 is issued (@8b87a0166b, three workers live), so its issuance is frozen like a round's. Comments 4-8 are a new scope, WORKSTREAM 3,
issued by `2.0.0_SA_COO~V1` as its own issuance and carrying all three WS2 guards. It may not take a file a live WS2 order owns.
- **Now:**
  - (4) the audit's money-market exclusion line is placed so it reads as its own line, never as naming the trade below it;
  - (5) a "flow adjusted" trade is not printed where the share count is unchanged within Andrew's 20 bps tolerance. That tolerance is
    applied wherever a share change is read as a trade, with a check over the 12 CGIC rows;
  - (6) no trade is drawn on a day marked BBG repeat;
  - (7) the header Period bar is removed.
- **Item 8, after aw-1's J1 read (the 13:00Z sweep):** the Direction Verdict accounts' opening lines get deeper, fund-specific
  prompting. It touches `ai_accounts.py`, which round 28's aw-1 deploy carries. A cell merged before aw-1's J1 read would change what
  that read grades, so item 8 is cut only after the read, as WS3's second issuance. Its prompt change is an OpenAI call path; egress is
  open (law 4d77a9c3ea).

## ADDENDUM 2 (~07:3xZ) -- row ETFS_RIVALS-D1-S5 @82800edf8a: CGIC's report date -- the SIDECAR's claim is the as-of; the row date is fixed (`2.0.0_SA_COO~V1` msg 1981)

A holdings report states positions as of the prior trading day's close and is DELIVERED the next trading day. CLAUDE.md: "Everything is
T-1 unless declared". The 10-05 (Monday) capture's claim of 10-02 (Friday) is exactly one trading day earlier
(`lib/trading_calendar.py`), which is the delivery lag, not an error. Ruling:
- **`canonical_shape` stamps `source_report_date` with the sidecar's `claimed_report_date`** wherever that is present, and keeps the delivery
  day as its own field (`delivered_on`). The calendar is already right ("repeat" reads the claim).
- **Every CGIC trade window re-reads from the corrected dates.** A trade inferred between two reports is dated by their as-of days, not
  their delivery days.
- **Proof in the cell:**
  - for the 10-02..10-06 CGIC captures, every row's `source_report_date` equals the sidecar claim, and the trade windows move one
    trading day earlier, printed before and after;
  - negative control: a fund whose sidecar claim equals its delivery day keeps its dates byte-equal.
- Where a sidecar carries no claim, the delivery day minus one trading day is used, and the row carries `claim: inferred` (A VALUE MUST
  CARRY ITS CLAIM).
- This is a WS2-class cell under the WS2 guards. A redeploy of the canonical shape waits for the round-28 J1 reads, and it needs its own
  pair, since served trade windows move.

## ADDENDUM 3 (~08:1xZ) -- row ETFS_RIVALS-D1-S6 @570d152eda: RIV-we-1 deploys forward-only; served history is rebuilt ONCE, scoped (`2.0.0_SA_COO~V1` msg 2095)

`build-canonical-shape` keys a revision by its INPUT digest, not the code (`gold_canonical_shape.py:945-956`), so a replay finds nothing
new: the measured run read `written_new 0`. Ruled **(a): a one-time forced rebuild, SCOPED:**
- **Scope:** only the (fund, capture) pairs whose sidecar `claimed_report_date` differs from the delivery day. CGIC's 10-02..10-08 are
  among them, and the denominator is printed from the stored sidecars. Every other pair is untouched and byte-equal (the negative arm).
- **Under its own never-widen pair:** the written revisions listed by key. Rollback is the prior revision re-served as the newest, with
  no delete. A dry run first (the `--fresh-canonical` run in progress) prints exactly which windows move, by how many trading days, per
  fund. The served act waits for both round-28 J1 reads (WS2 guard 1).
- **(c), forward-only, is refused:** it leaves served CGIC windows a trading day late, against ADDENDUM 2.
- **(b), the code version joins the digest, is NOT ruled here.** A digest that ignores code makes every future fix forward-only without
  saying so, but re-keying on any code change re-writes every fund's history every deploy. That is a design fork, so `4.0.0_SA_CRO~DELL1`
  researches past patterns (a rule-version field bumped only by semantic changes, against a code hash, against today). It is ruled at
  round 29 on that research.
