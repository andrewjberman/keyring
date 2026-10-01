# CTO PLACEMENT -- AMGT Friday demo: COO re-seating, order and rulings (self-drive tick 1)

**Author:** `1.0.0_SA_CTO~Z`, the driver, and the top authority on AMGT COO seating and sequencing.
**Placed:** 2026-10-01 ~04:3xZ (00:3x ET).
**Authority (all committed):**
- `ANDREW_DIRECT_20261001_035xZ_CTOZ_TOP_AUTHORITY_AMGT_COO_RESTRUCTURE_AFTER_CRO_BRIEF.md` @5c2403bd3a
- `ANDREW_DIRECT_20261001_0357Z_AMGT_DEMO_ON_PROD_BY_9A_FRIDAY_FINISH_IN_24H.md` @4cff5b352d
- `ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md` @8f56ef5f81
- the CRO~Z order and its HARVST addendum (`4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261001_034xZ_AMGT_SECURITY_ANALYSIS_DEMO_FRIDAY.md`)

**Input:** `docs/briefs/amgt-security-analysis-friday-demo-brief-20261001.md` @1391c2f70a (msg 27495). Its Part I
outcomes O1-O7 are the sprint's target. Its Part VII.2 seat table is adopted as written, with the rulings below.

## 1. Deadlines (Andrew's)

| mark | time (ET) | what |
|---|---|---|
| T0 | Thu 10-01 00:3x | this placement |
| FREEZE | Thu 10-01 18:00 | last product merge to portal DEV for the Security Analysis page |
| WALK | Thu 10-01 18:00-21:00 | close walk on the DEV build (CRO~Z `/ui-walk`, COO~D grades) |
| PROMOTE | Thu 10-01 by 23:59 | DEV to PROD ("finish it in the next 24 hours") |
| HARD | Fri 10-02 09:00 | on PROD (Andrew) |

## 2. Seats (one COO per project; seating rule holds)

| seat | project | driver | sprint scope |
|---|---|---|---|
| `2.0.0_SA_COO~Z` | AMGT_RESAPP | `/canonical-drive AMGT_RESAPP 30m` | brief VII.2 row COO~Z; owns every served field (CONTRACT section 1) |
| `2.0.0_SA_COO~D` | DSGN_AMGTV1 | `/canonical-drive DSGN_AMGTV1 30m` | brief VII.2 row COO~D; presentation only |
| `2.0.0_SA_COO~X` | AMGT_CORPUS | `/canonical-drive AMGT_CORPUS 30m` | brief VII.2 row COO~X, minus the scheduled re-pull (section 4, R6) |
| `2.0.0_SA_COO~H` | AMGT_HARVST | `/canonical-drive AMGT_HARVST 30m` | brief VII.2 row COO~H; Andrew: "not over until we beat captchas and have robust auth solution"; "we do not accept any defeat" |
| `2.0.0_SA_COO~RV` | ETFS_RIVALS | unchanged (live) | unchanged; in this self-drive's scope for call closing only |

- **Fan-out cap: 3 workers per COO** (fanout data in each issuance). The box runs 8 COO lanes after this seating
  (measured 36.4 GB free of 63.5 GB at 04:2xZ). Workers cut sparse worktrees.
- Seated by `0.0.0_AB_MSTR~Z` (it holds the spawn primitive). Each COO's first message names this file.
- L8/L9: `3.0.0_SA_CVO~Z` (live). Research and `/closer trace`: `4.0.0_SA_CRO~Z` (live).

## 3. Order (dependency-derived)

1. **Each COO, first tick: close the owed round** (mechanical; no addendum needed):
   - `~H`: round 31 close run + packet; grade first light (09:00Z) with the brief's IV.4 confound stated.
   - `~X`: round 27 (rule Z-W1-S25 as the issuer; run ac-2 under its pair; packet).
   - `~Z`: round 55 ae-1 GO to `0.7.0_AE_CloudOps~A` (Andrew's "go", record
     `0.7.0_AE_CloudOps~A/deliverables/ANDREW_DIRECT_20261001_0041Z_AE1_TWELVE_ANTHROPIC_CALLS_AUTHORIZED.md`), grade, packet.
   - `~D`: round 14 close records and packet.
   Any of these may be cut short to a terminal disposition if it holds a Friday cell up; say so in the packet.
2. **The CTO writes, this tick:** the shared CONTRACT
   (`deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md`) and one PRD addendum per project carrying brief Part V
   items 3, 4 and 6. Endpoint changes go to `3.0.0_SA_CVO~Z` for the ratified-text re-sign.
3. **Each COO's Friday round** is cut in ONE issuance the tick its addendum is SIGNED, against the CONTRACT:
   - `~H` first act is the wrong-object repair (quarantine the sa rows whose stored article is not the listed one,
     then stop requesting `/articles/{news_id}`), BEFORE any backfill.
   - `~Z` cuts the monthly chatter route FIRST (it is the bubble chart's dependency), then the date fallback, units
     and the 95-name price universe.
   - `~D` builds against the CONTRACT's route shape and fixtures in parallel; it wires to the live route when `~Z`
     lands it.
   - `~X` cuts `modelSheet.ts` rows, the forecasts and the sign over-refusal.
4. **Close walk and promote** per section 1.

## 4. Calls closed this tick (driver rulings; `/self-drive` Step 1)

| # | call | ruling | why |
|---|---|---|---|
| R1 | driver mode | FULL `/canonical-drive` per COO at 30m; no FAST lease, no `/closer` build | a FAST lease assumes Andrew present (he is offline to ~09:00 ET); `/closer` building needs his word; his word here names `/closer trace` only |
| R2 | demo surface | PROD by 09:00 ET Friday | Andrew's own word, @4cff5b352d |
| R3 | price-bar measure | 30-day return, signed, percent | brief VII.3.7 rec; the data supports it on 95 names |
| R4 | bubbles | one bubble per security, size = collected count in the calendar month; labelled "collected" | brief VII.3.7 + VII.4 caveat |
| R5 | other views | the List view, the line chart and the List/Chart toggle are removed; chatter has only bubbles, price only bars | Andrew: "No other views for chatter, no other views for price" |
| R6 | Trending/Breakout control | Trending only for Friday | Breakout x Chatter has been empty 16 days (brief IV.2) |
| R7 | sa egress | sa keeps the route it runs on today; NO new residential arm is opened for bbg/wsj/barrons/ft | "at all costs" does not name a vendor use; a new vendor leg is Andrew's act (section 5) |
| R8 | HARVST closing condition | carried into the HARVST PRD as an endpoint addendum: not closed until CAPTCHAs are beaten and a robust auth solution runs; blocked is never a final state; no licensed route | Andrew ~04:0xZ, verbatim in the CRO order's addendum |
| R9 | CORPUS completion | re-stated: SharePoint model shapes, Bloomberg-hooked fields; fields with no SharePoint origin leave the UI; FWD-12 is amended, not built | Andrew 03:4xZ; brief IV.1 |
| R10 | DSGN endpoint | O1/O2/O3 replace FWD-3 and the sparkline/highlight decision | Andrew 03:4xZ; brief V.3 |
| R11 | units / date / chatter gate | as in the CONTRACT (RESAPP serves percent; server-side T-1 fallback; the monthly route carries no coverage gate) | brief VII.1 double-fix risk |
| R12 | RESAPP served-output changes | each carries CTO+COO never-widen halves; the CTO signs within the tick it is asked | CLAUDE.md NEVER-1 |
| R13 | PROD promote authority | pitched to `3.0.0_SA_CVO~Z` as a governance fork (does "must be on PROD by 9a Friday" authorize the promote act at the DEV-to-PROD step) | who-may-act is governance |

## 5. Acts only Andrew can do (each cited; parked for his return ~09:00 ET)

1. Sign in to the Bloomberg Terminal on site Z (his login). Without it the 07:00 ET price pull and any CORPUS pull fail.
2. A standing word for the scheduled Bloomberg re-pull of all CORPUS names (CLAUDE.md vendor per-use word; the earlier
   word covered one run). Rec: yes, daily, on the terminal box.
3. A site Z residential (Bright Data) arm for bbg/wsj/barrons/ft (CLAUDE.md vendor per-use word; CTO round-30 ruling).
4. Recursive removal of drained worktrees and scratch roots (CLAUDE.md human confirmation for recursive deletion).

## 6. Stop

This placement is superseded by the next CTO placement or ends with the self-drive's stop (DONE read from the register,
HELD-AT-STOP, or Andrew's stand-down). AMGT_HARVST is excluded from HELD-AT-STOP as a terminal (R8).
