# ETFS_RIVALS -- ROUND 2 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~06:0xZ

**Input:**
- CVO~RV slug msg 27553 @98b3262aa2 and review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md`.
- `REMEDIATION_v2.Z.md` (8 items, W2-S4 ARMED) and `REMEDIATION_v1.Z.md` (8 items). That makes 16 OPEN, all owned by this
  seat.
- The census: 66 rows, 0 open, 50 dismissed, 16 graduated.

**Driver:** `/self-drive AMGT_FRIDAY` (ETFS_RIVALS in scope; Andrew-direct @8f56ef5f81). Every call is ruled here.

## 1. WHAT THE ROUND DELIVERED

- 9 of 9 orders terminal.
- Ledger `etfs-rivalfunds-round2` CLOSED.
- W5-S24 disarmed (supersede without delete).
- The package suite reads 189 passed.
- The served page reads `not-updated`, with 6 of 13 funds present.

**Round 2 is CLOSED.**

## 2. RULINGS

| # | row | ruling | why |
|---|---|---|---|
| 1 | **W2-S4** (ARMED; issuer silver 325/325 old-format ids; a re-capture of a landed BASG date keeps the old rows) | **Round 3's first cell.** It is the one-line `_capture_id` change to the live Lambda, under CTO+COO never-widen halves. The positive control is a re-capture of one landed BASG date, whose new rows replace the old in the read. Until it ships, no manual re-fetch of a landed date (COO~RV holds the disarm). | the only live-correctness hazard |
| 2 | **W5-S23** (a signed-out Terminal morning builds no G5 for ANY fund) | **Narrow the gate.** The W3-S13 enrichment gate holds only the funds whose trade window touches a corporate action that needs the pull's enrichment. Every other fund, BASG included, builds its daily G5 without the Terminal. | This KEEPS the endpoint: PRD `:68`, "Andrew does nothing by hand on an ordinary day". The round-2 build had quietly made a daily Terminal sign-in part of the ordinary day. Restoring the endpoint is not an endpoint change, so it needs no word of Andrew's. |
| 3 | **W5-S28** (freshness threshold 0) | A fund's freshness is counted in TRADING days against `lib/trading_calendar.py`. A Bloomberg-fallback fund at T-1 is current, not `not-updated`. | CLAUDE.md: everything is T-1 unless declared; a threshold of 0 false-alarms every ordinary morning |
| 4 | **W1-S8** (the home-producer reader; both home funds read ABSENT) | A round-3 cell. The home funds read from their own producer per C-HOME-PRODUCER, and the page shows "his fund beside its rivals" (FWD-1). | FWD-1 cannot be REALIZED with the home fund absent |
| 5 | **S1** (C-SHAPES vs the ETF positioning vocabulary) | **Reading (a): the ratified vocabulary governs.** For an equity row, `sub_asset_class` IS its GICS sector (`etf_positioning_gold.py` `SUB_ASSET_CLASS_VOCAB = GICS_SECTORS + (...)`). A finer GICS level (industry group, industry, sub-industry) never stands in for a sub-asset class. Both fields are carried, and they agree by construction. The PRD's C-SHAPES line is amended in v0.7 (same commit). | the PRD names that vocabulary as its classification source; the DSGN_AMGTV1 rounds 8-9 defect the line cites was a GRAIN defect (a finer level in the sector slot), and the amended line keeps exactly that guard |
| 6 | **W1-S4 / W1-S5** (issuer positions resolve 0 of 35; resolved-fraction floor 0.0) | A round-3 cell: a crosswalk carrying the CUSIP/ISIN/SEDOL forms, through `lib/research/identity/`. The floor is raised to a measured value with it. W1-S5's not-updated marker is named per fund and per batch in C-GUARDRAILS. | the trade schedule (C-TRADE-SCHEDULE) matches by RESOLVED identity only |
| 7 | **W1-S11, W3-S11, W3-S12, W5-S21** (the revision tie, DVD_CRNCY, child-line identity, quadratic dedup) | Round 4, after the round-3 thread cells. W3-S12 follows the issuer's ruling: a line born of an entitlement is not a trade. Each carries its own control. | none is on the FWD-1 thread; each is a correctness item before backfill |
| 8 | **S2** (gateway deploy lease, route preservation) | Fabric. It is carried to the gateway owner, `1.0.0_SA_CTO~O`'s NFRA_OPLGTW, as an input. It is not an ETFS_RIVALS cell. | lane |
| 9 | **W5-S12** (still listed ARMED; its hazard ended at the ledger close 2026-09-30 15:33:58Z; the gate refuses an in-place disarm block) | Disarmed by this record: ledger `etfs-rivalfunds-round1` closed 15:33:58Z, so the hazard window is over. CVO~RV cites this analysis as the disarm. | an in-place edit is refused by design |
| 10 | **GQGU** absent with no explaining row | COO~RV files a row at the round-3 cut naming why. It is UNMEASURED, not dismissed. | CVO review, "Deferrals" |

## 3. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~RV` cuts for round 3 in ONE issuance

1. **W2-S4** `_capture_id` fix (WORLD, pair; positive control as ruling 1). First.
2. **W5-S23** narrowed gate, plus **W5-S28** trading-day freshness. LOCAL code, with a signed-out-morning fixture: BASG
   builds, and a corporate-action fund holds.
3. **W1-S8** home-producer reader. The page shows both home funds.
4. **W1-S4 / W1-S5** identity crosswalk, a measured floor, and the not-updated marker.
5. **G4 lands GICS** under the amended C-SHAPES (ruling 5).

Each build order carries at most three mechanical criteria.

## 4. FWD-1 GRADE

FWD-1 is NOT REALIZED. Beyond the cells above, it needs two acts:
- the first live 08:03 leg after a Terminal sign-in;
- one signed-in `/rivalfunds` read.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **Sign in to the Bloomberg Terminal on site Z** (his login), for the 08:03 leg on corporate-action days.
2. **One signed-in `/rivalfunds` read** (his login), for FWD-1's acceptance.
