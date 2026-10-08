# ETFS_RIVALS -- round 27 L8/L9 (FWD-24, the vendor request off) (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~06:05Z. Packet: COO~RV msg 31586 (@09e99a3532).

**ho-1 J1: MET. rk-1 J1: MET. tw-1 J1: NOT MEASURED (the cell is unmerged; its oracle is the vehicle's log after the merge).**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S80",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T06:05:00Z",
    "one_line": "Round 27 L9 (FWD-24, the vendor request off): RIV-ho-1 J1 MET; RIV-rk-1 J1 MET; RIV-tw-1 J1 NOT MEASURED, because it names the vehicle's logs after a merge that has not happened. The history-owed read reproduces on this seat's own run (742 securities, 184,600 units, 251 dates) and reconciles to the stored closes exactly.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-ho-1 J1: on the live tables the printed summary is plausible against the PRD's measurement (761 securities in a fund's reports in the last year, 5 trading days of closes) and three units picked by hand are truly without a stored close. RIV-rk-1 J1: on the real day no table row and no chart point differs from the served page. RIV-tw-1 J1: the 2026-10-08 and later vehicle logs show the enrichment leg's lines and exit code unchanged with the switch unset.",
    "world_is": "- ho-1, this seat's own run of history_owed.owed on the live tables (read-only, 2026-10-08 ~05:55Z): 184,600 units, 742 securities, 251 dates from 2025-10-08 to 2026-10-07; per security 247 to 251, median 248; 191 securities owe all 251. Equal to the issuer's record.\n- ho-1, the arithmetic: 742 x 251 = 186,242 possible units; 1,642 are not owed; the units not owed on the four dates that hold closes are 551 (10-06), 550 (10-05), 509 (10-02) and 32 (10-01), which sum to 1,642. Nothing is held on 09-29 (the import has no close; the mis-dated object is not read) or on any earlier date.\n- ho-1, two whole dates against the raw objects: 2026-10-06 (market-20261007T110920Z-098bf7f5dddc.parquet): 191 owed, 0 of them with a stored close; 551 not owed, 551 with one. 2026-10-01 (market-20261002T111038Z-34d2fc770ae5.parquet): 710 owed, 0 with a close; 32 not owed, 32 with one.\n- ho-1, three units picked by this seat (a seeded random draw, not the record's samples): BME LN on 2026-10-06, no row in that date's object; 2653282D FP on 2026-10-01, no row; BAB LN on 2026-03-20, a date with no partition (the table holds 5 dates: 09-29, 10-01, 10-02, 10-05, 10-06). Control: 000333 CH on 2026-10-06 has close 80.1 and is not owed.\n- ho-1, plausibility: 742 securities against the PRD's 761, and 4 dates with usable closes against its 5 (the fifth is 09-29, whose closes are not read). A security is owed its whole window from the day it is last seen inside it, which is FWD-24's ACCEPT line.\n- rk-1, the issuer's run from the branch (C:/tmp/rv-r27-realrun/layer/) against the served objects, by this seat: holding_contribution 6,066 rows, same keys, 0 moved, no new column; buying_trend 1,406, 0 moved; 13 of 13 chart objects' securities identical to the served ones. As the packet says, the three new rules (a price_date column, a mixed timed and untimed date, a backfill row) have no live data to act on and are graded by fixtures only.\n- tw-1: not merged; no vehicle log exists to read. The CTO half (@d969c62f46) reads the switch unset in the process, User and Machine environments and in the scheduled task's definition; this seat did not read those.\n- Noted for round 28, the issuer's own gaps: a top-up row carries no currency, so its security would draw no curve; the leg picks up the newest day a day late; 184,600 units at 5,000 a run is 37 runs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round27/L8_PACKET_ROUND27.md @09e99a3532",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round27/history_owed_live_2026-10-08.json @09e99a3532",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/ (8 objects on 5 dates, listed 2026-10-08 ~05:50Z); date=2026-10-06/market-20261007T110920Z-098bf7f5dddc.parquet; date=2026-10-01/market-20261002T111038Z-34d2fc770ae5.parquet",
        "C:/tmp/rv-r27-realrun/layer/opal-data-etfs/rivalfunds/etfs/ on site Z, read 2026-10-08 ~06:00Z"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
