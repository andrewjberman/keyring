# MDPF_SECHIST -- Opal's securities database: ingestion and maintenance

```json
{
 "project": "MDPF_SECHIST",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/securities-database-ingestion-maintenance-brief-20261006.md@901edd46a2",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06.
**Brief:** `docs/briefs/securities-database-ingestion-maintenance-brief-20261006.md` @901edd46a2 (`4.0.0_SA_CRO~P`).
**Andrew's words:** the order, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`;
outcomes confirmed and four calls answered, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_181xZ_COO_C_BOTH_SECHIST_REGISTER_HOLD_RIVALS_1Y.md`.
**DISTRIBUTION:** held at ~18:1xZ; LIFTED for round 1 on dell1, Andrew ~19:2xZ "Ok that is fine" (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md`).
Round 1 runs on dell1.
**Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  The morning after an Opal ETF first buys a security, an analyst opens it on the Positioning
         page and sees its class, sector, clean name and every return window a year of history supports,
         with nobody having asked for a pull
         DONE WHEN  EXERCISED -- one real new holding read the next morning, every hop real
         ACCEPT     an analyst picks a security an Opal ETF bought yesterday, opens it on the Positioning
                    page this morning and reads its classification and its returns from one week to one
                    year; nobody ran anything by hand to make that happen
         SOURCE     brief PART I, candidate thread (DIVZ; CSCO and BX the live negative case)

  FWD-2  A client's security shows performance for the whole time the client has held it
         DONE WHEN  EXERCISED -- one client-held security read back to its first appearance in the account
         ACCEPT     an Investor Reporting reader sees a held security's performance from the day it first
                    appeared in the client's account, not from the day Opal started tracking it
         SOURCE     brief O2; Andrew's rule, "from first appearance"

  FWD-3  Anyone can read, for any security, where it came into Opal and how far back its history must go
         DONE WHEN  EXERCISED -- one security with two sources read, and the deeper rule shown governing
         ACCEPT     for any security an operator sees each place it entered (an Opal ETF, a client account by
                    firm, a rival fund) and how much history each requires; the deepest requirement wins
         SOURCE     brief O3

  FWD-4  An operator can see whether each security's history is complete, without asking Bloomberg
         DONE WHEN  EXERCISED -- the stored range, the required range and any gap read for every tracked
                    security
         ACCEPT     for any security an operator reads what history Opal holds, what it should hold, and
                    exactly which days are missing
         SOURCE     brief O4

  FWD-5  Missing days fill themselves, and a gap never shows as a wrong number
         DONE WHEN  EXERCISED -- a real gap filled by the next run, and a window over an unfilled gap read
                    blank
         ACCEPT     when a security misses days in the daily pull, the next run fetches them; until then a
                    return covering those days is shown blank, never calculated across the missing days
         SOURCE     brief O5; PART III, "a blank is acceptable, a wrong number is not"

  FWD-6  Every held instrument is its own security, with its own row and its own history
         DONE WHEN  EXERCISED -- a preferred share, a numeric ticker and an identifier-only holding each
                    read with their own row and series
         ACCEPT     an instrument that is not a plain stock ticker (QXO B is the live case) has its own
                    classification and its own history and never borrows another security's
         SOURCE     brief O6

  FWD-7  The day's Bloomberg spend on history is visible and stays inside one budget
         DONE WHEN  EXERCISED -- one day's spend read against the budget, with a backfill in it
         ACCEPT     an operator reads what history cost today against the shared budget; a security's
                    backfill is paid for once; a backfill never causes a production pull to fail
         SOURCE     brief O7

  FWD-8  A security reads the same on every screen
         DONE WHEN  EXERCISED -- one security read on Positioning, Investor Reporting and Advisor
                    Intelligence, same answer on all three
         ACCEPT     a security's class, sector, clean name and its return for a given period are the same
                    wherever an Opal person looks it up
         SOURCE     brief O8; PART III, the second answer retired

  FWD-9  A money-market fund's performance is shown by one stated rule, never silently blank
         DONE WHEN  EXERCISED -- SALXX read across a week that includes a Monday
         ACCEPT     a reader sees performance for a money-market fund such as SALXX every day under one
                    stated rule, instead of it disappearing whenever the vendor leaves a day empty
         SOURCE     brief O9; Andrew, "I agree with the rec"
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-DEPTH: the depth each ingestion point requires (FWD-3) | Andrew's rulings | Three ingestion points, each with its depth: **Opal ETF holdings (Positioning): one year**; **client account, by firm: from the security's first appearance in that firm's holdings**; **rival funds: one year** ("B, 1 year for rivalfunds"; MDPF_SECCLASS FWD-9 amended to match, v0.12). Advisor Intelligence is not a point of its own: it reads the client firms' holdings. A security's governing depth is the deepest its points require. A new point is a PRD addendum, never a code default. |
| C-SERIES: one stored history per security (FWD-2, FWD-8) | Andrew, "Rec approved" | ONE series per security, starting at its earliest first appearance across every account and point; a holding's period is cut from it, never stored apart. Every screen reads this series. |
| C-MMF: money-market funds (FWD-9) | Andrew, "I agree with the rec" | A money-market fund's daily return is computed from its total-return level, not the vendor's daily-return field (empty on the first trading day of each week, brief O9); a day with neither is blank, never estimated. |
| C-GAP: gaps are blank, never compounded (FWD-5) | this project | A window spanning a missing day reads blank; the next run requests the missing days; the gap record is read before any return is computed. The brief measures that gold compounds present observations without detecting an interior gap today (PART IV.7). |
| C-IDENTITY: one key per instrument (FWD-6) | MDPF_SECCLASS owns the table key; this project carries it end to end | The table's key forms (bare ticker, `CUSIP:`, `BBG:<tkr>:<exch>`) reach the detector, the pull label and the join; no instrument is keyed by the first token of its label (brief PART IV.6). |
| C-TABLE: the row is MDPF_SECCLASS's | MDPF_SECCLASS (`etf-classifications`, its detector, FWD-7/10/12/14) | This project never writes classification; it reads the row and adds only history and coverage records. Any new table field is MDPF_SECCLASS's PRD addendum. |
| C-BUDGET: one Bloomberg budget (FWD-7) | ETFS_RIVALS owns `bbg_budget.py` | History pulls and backfills draw on the same ledger, under the production reserve; a backfill is paid once per security and yields to production. |
| C-PULL: pulls run at site Z | `0.0.3_BG_BBGTerminal`'s daily vehicle | A new pull leg lands in that vehicle as a deploy at site Z; nothing here calls Bloomberg from another box. |
| C-NAMES | law (rule 30) | Every new address and name is `lib/opal_naming.py` output, printed in the order that writes it. |
| C-NO-SHADOW / C-MORATORIUM | law | The frozen backfill prefix and the per-firm price tables are consolidated into the one series, never run beside it; no alert or monitor. |

## 1. The arc

**Start.** History is filled by hand-run pulls; one window for every security; gaps compound silently; non-ticker instruments have no
row or series; two answers for "what is this security". **End.** A security entering through any point is filled to its governing
depth by the next morning, kept complete day over day, read the same everywhere, inside one budget.

## 2. THREAD -- FWD-1, round 1 (when distributed)

The detector sees a new Opal ETF holding; the row exists (MDPF_SECCLASS FWD-10); the pull plan asks Bloomberg for that security's
one-year history in the next daily run; the series lands; the Positioning gold reads it; an analyst reads the security on the page.

## 3. ENRICHMENT BACKLOG (ordered)

1. The gap record and blank-over-gap (FWD-5, FWD-4).
2. Client first-appearance depth by firm (FWD-2, FWD-3); Cottonwood waits on ADVI_COTBKF.
3. Non-ticker instruments (FWD-6).
4. The budget ledger over the history legs (FWD-7).
5. Money-market rule (FWD-9).
6. One answer on every screen, `bd-securities` retired as a second answer with MDPF_SECCLASS FWD-5 (FWD-8).

## 4. WORKSTREAMS AND OWNERS

Round 1 on dell1, a dell1 COO lane seated by the dell1 MSTR. The pull leg is site Z's; the table is MDPF_SECCLASS's.

## 5. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | bound |
|---|---|---|---|---|---|
| S01 | FWD-1 | the per-security pull plan in the site Z daily vehicle | held (brief IV.5: one window for all) | build | one year for an ETF holding |
| S02 | FWD-3 | the depth policy record per ingestion point | held | build | C-DEPTH |
| S03 | FWD-4, FWD-5 | the coverage and gap record per security | held (brief IV.7) | build | blank over a gap |
| S04 | FWD-2 | first appearance per security per firm | held (brief IV.4) | build | cot after ADVI_COTBKF |
| S05 | FWD-6 | the non-ticker key end to end | held (brief IV.2, IV.6) | wire | MDPF_SECCLASS owns the key |
| S06 | FWD-7 | the history legs on `bbg_budget.py` | held (brief IV.8) | wire | production reserve kept |
| S07 | FWD-9 | the money-market rule | held | build | C-MMF |
| S08 | FWD-8 | one series read by every screen | held | wire | no second answer |

## 6. BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| PART I, thread and O1-O9 | the thread; nine outcomes | ENDPOINT; section 2 |
| PART II, boundary | owns lifecycle, depth, series, pull plan; relies on MDPF_SECCLASS, ETFS_*, IRPT, firm producers, site Z | C-TABLE, C-BUDGET, C-PULL |
| PART III, bar | no hand pull; no wrong number; non-ticker first-class; budget; one answer | FWD-1, C-GAP, C-IDENTITY, C-BUDGET, FWD-8 |
| PART IV, substrate 1-10 | table, detectors, first appearance, history, identity, gap, quota, AI reads, naming | S01-S08, C-NAMES |
| PART V, must be true | depth ruling; key; first appearance; per-security windows; budget; money-market; second answer | C-DEPTH, C-IDENTITY, S04, S01, C-BUDGET, C-MMF, FWD-8 |
| PART VII, not claimed | per-security vs per-position, settled; instrument types without total return | C-SERIES; a round-1 read |

-- 1.0.0_SA_CTO

## ADDENDUM v0.2 (1.0.0_SA_CTO~DELL1, 2026-10-07) -- contract note only: Yahoo Finance admitted as a second price source

**Word:** Andrew-direct ~13:2xZ at the `1.0.0_SA_CTO~DELL1` terminal, VERBATIM: "(also you have egress for yfinance yahoo)". Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_13xxZ_EGRESS_YFINANCE_YAHOO_DELL1.md`. The ENDPOINT section is not edited.

- **C-PULL, widened by one source.** Bloomberg stays at site Z in its daily vehicle. Yahoo Finance, read through the `yfinance`
  package already installed on dell1 (1.7.0; no package download), is admitted from dell1 for the Yahoo-sourced share of ADVI_COTBKF's
  price-need file (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` @50a35d3ada:
  3,226 securities, 5,773,776 security-days). Any other use of Yahoo is surfaced to Andrew, not assumed.
- **C-SERIES and C-GAP bind the Yahoo rows** exactly as the Bloomberg rows: one series per security, a missing day is blank, and a
  security with no price is listed (2,914 in the file), never estimated. Every row carries its source.
- **C-BUDGET does not reach Yahoo.** That ledger is Bloomberg's capacity. A Yahoo pull is paced to the vendor's own limits, and a
  refusal from the vendor leaves the day blank and is listed, never retried in a loop.
- Pre-2010 dates raise under the calendar fix. This load is FWD-2 work (enrichment item 2), placed in round 2 by `2.0.0_SA_COO~H1`.

## ADDENDUM v0.3 (1.0.0_SA_CTO~DELL1, 2026-10-09 ~05:5xZ) -- the stored series carries price, dividend/interest and total return

Andrew-direct ~05:4xZ (record @cb023aa95f; see MDPF_DEMQUE ADDENDUM v0.5): every price is the dividend/interest-inclusive total return,
with the components kept for audit. SECHIST is the one series writer (ruling @8a625fa88a), so C-SERIES is amended: one series per
security, and per day the as-traded price, the dividend/interest cash and the total-return value, from Bloomberg or Yahoo. C-GAP binds
all three. C-MMF's total-return level is the same rule, already in force for money-market funds. Ruling:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_BATCH_20261009T0550Z.md` C.
