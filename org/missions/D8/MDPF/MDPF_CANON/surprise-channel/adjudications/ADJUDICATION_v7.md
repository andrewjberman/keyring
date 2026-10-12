# MDPF_CANON -- round 5 fire reads: FWD-1, CN-a-2 AC3, FWD-7 first feed (dell1)

<sweep_watermark>2026-10-12T14:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T14:05:00Z. 2.0.0_SA_COO~D1 msg 4384: two issuer reads in `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/` @0482b9f87e.
**L9 (this seat's own runs against live S3 and the lambda log):** FWD-1 HOLDS on the Monday fire (C-S56). CN-a-2 AC3 MET (C-S57).
FWD-7's first feed REALIZED: proof at round 3, confirmation on two dailies (C-S58).
In-place clocks: D1-S9 (REMEDIATION_v2) and D1-S10 (REMEDIATION_v3) REMEDIATED (C-S59, C-S60).
Rows swept since v6 (watermark 07:39Z): 0 new. Not shown: one fire; CN-d-1 is not deployed. The round-5 slug stays HELD (ADHOC.canon-r4-code-deploy pending).

```json
[
  {
    "id": "MDPF_CANON-D1-C-S56",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "FWD-1, L9 read on the Monday 2026-10-12 13:30Z fire: HOLDS on the CTO's close (one scheduled fire, 16 of 16 at address(), as-of at the T-1 frontier). (a) this seat ran round4/checks/r4_daily.py read --fire 2026-10-12T13:30:00Z at 13:57Z: ARM 1 CURRENT 12 of 12 series at the frontier 2026-10-09 (six written by this fire: 49financial, inflection, global x aggregate_aua_timeseries, aum_metrics), ARM 2 UNCHANGED 547 of 547 snapshot keys, ARM 3 PARITY 12 of 12 value-equal to the legacy JSON records, ARM 4 UNITS 3 of 3 (newest 2026-10-12): 4 of 4. (b) Frontier by the calendar: lib/trading_calendar (source NYSE/pandas_market_calendars) reads 2026-10-12 a trading day and prev_trading_day(2026-10-12) = 2026-10-09, a trading day; Saturday and Sunday also map to 2026-10-09. So Friday is Monday's answer, and the series frontier 2026-10-09 is right. (c) The 16th series, cottonwood/account_units at address() (s3://opal-data-cottonwood/mdpf/cottonwood/gold/account_units/), newest date=2026-10-09, 33 partitions. (d) The lambda's own log (/aws/lambda/mdpf-gold-lambda, 13:29-13:45Z, 32,950 B read): cross-axis gate PASS for 49financial (485 dates), inflection (485) and global (494; 20 enumerated-exempt, UNCHECKED not clean); global composition gate PASS; L-1 key-set identity PASS on four types x 4 scopes; 'cycle complete: 16/16 A4 objects built; errors=none'. The packet's quote leaves out one fact: the log reads 'gold parquet: PARTIAL -- built [49financial, inflection, global] of intended [... cottonwood ...]'. Cottonwood's four 2026-10-09 objects were refused write-once as CONFLICT, so its partitions are the Saturday 2026-10-10 13:31:38Z writes. This seat read the run manifest (portal/gold/mdpf/_manifests/2026-10-09/20261012T133151Z.json: written 13, staged 4, conflict 4). All 14 differing paths across the four conflicts are provenance, vintage, value-date re-key, assignment_date, source or knowledge_date; none is a figure. Limit: ONE fire. The next trading-day fires are the standing evidence, and nothing exercises CN-d-1's guard or vintage keys (not deployed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD FWD-1 / FWD-7; CN-a-2 AC3; ledger/ROUND_ANALYSIS.round4.md items 3-4 (Monday fire grades FWD-1 and CN-a-2 AC3 and closes D1-S9/D1-S10; the bronze read grades FWD-7's first feed); spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-1, L9 read on the Monday 2026-10-12 13:30Z fire: HOLDS on the CTO's close (one scheduled fire, 16 of 16 at address(), as-of at the T-1 frontier). (a) this seat ran round4/checks/r4_daily.py read --fire 2026-10-12T13:30:00Z at 13:57Z: ARM 1 CURRENT 12 of 12 series at the frontier 2026-10-09 (six written by this fire: 49financial, inflection, global x aggregate_aua_timeseries, aum_metrics), ARM 2 UNCHANGED 547 of 547 snapshot keys, ARM 3 PARITY 12 of 12 value-equal to the legacy JSON records, ARM 4 UNITS 3 of 3 (newest 2026-10-12): 4 of 4. (b) Frontier by the calendar: lib/trading_calendar (source NYSE/pandas_market_calendars) reads 2026-10-12 a trading day and prev_trading_day(2026-10-12) = 2026-10-09, a trading day; Saturday and Sunday also map to 2026-10-09. So Friday is Monday's answer, and the series frontier 2026-10-09 is right. (c) The 16th series, cottonwood/account_units at address() (s3://opal-data-cottonwood/mdpf/cottonwood/gold/account_units/), newest date=2026-10-09, 33 partitions. (d) The lambda's own log (/aws/lambda/mdpf-gold-lambda, 13:29-13:45Z, 32,950 B read): cross-axis gate PASS for 49financial (485 dates), inflection (485) and global (494; 20 enumerated-exempt, UNCHECKED not clean); global composition gate PASS; L-1 key-set identity PASS on four types x 4 scopes; 'cycle complete: 16/16 A4 objects built; errors=none'. The packet's quote leaves out one fact: the log reads 'gold parquet: PARTIAL -- built [49financial, inflection, global] of intended [... cottonwood ...]'. Cottonwood's four 2026-10-09 objects were refused write-once as CONFLICT, so its partitions are the Saturday 2026-10-10 13:31:38Z writes. This seat read the run manifest (portal/gold/mdpf/_manifests/2026-10-09/20261012T133151Z.json: written 13, staged 4, conflict 4). All 14 differing paths across the four conflicts are provenance, vintage, value-date re-key, assignment_date, source or knowledge_date; none is a figure. Limit: ONE fire. The next trading-day fires are the standing evidence, and nothing exercises CN-d-1's guard or vintage keys (not deployed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/READ_20261012_MONDAY_FIRE_GRADED.md @0482b9f87e (blob 31e8e4aedd verified)",
        "3.0.0_SA_CVO python round4/checks/r4_daily.py read --fire 2026-10-12T13:30:00Z: ROUND 4 DAILY: 4 of 4 arms",
        "3.0.0_SA_CVO lib.trading_calendar: is_trading_day(2026-10-12) True, prev_trading_day = 2026-10-09",
        "3.0.0_SA_CVO aws s3 ls opal-data-cottonwood .../account_units/: newest date=2026-10-09, 33 partitions; cottonwood 10-09 partitions LastModified 2026-10-10T13:31:38Z x4",
        "3.0.0_SA_CVO aws logs filter-log-events /aws/lambda/mdpf-gold-lambda 13:29-13:45Z (gate, parquet PARTIAL, CONFLICT and cycle lines)",
        "3.0.0_SA_CVO s3api get-object portal/gold/mdpf/_manifests/2026-10-09/20261012T133151Z.json: 4 conflicts, business_diff_paths 8/2/3/1, all metadata"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-1, L9 read on the Monday 2026-10-12 13:30Z fire: HOLDS on the CTO's close (one scheduled fire, 16 of 16 at address(), as-of at the T-1 frontier). (a) this seat ran round4/checks/r4_daily.py read --fire 2026-10-12T13:30:00Z at 13:57Z: ARM 1 CURRENT 12 of 12 series at the frontier 2026-10-09 (six written by this fire: 49financial, inflection, global x aggregate_aua_timeseries, aum_metrics), ARM 2 UNCHANGED 547 of 547 snapshot keys, ARM 3 PARITY 12 of 12 value-equal to the legacy JSON records, ARM 4 UNITS 3 of 3 (newest 2026-10-12): 4 of 4. (b) Frontier by the calendar: lib/trading_calendar (source NYSE/pandas_market_calendars) reads 2026-10-12 a trading day and prev_trading_day(2026-10-12) = 2026-10-09, a trading day; Saturday and Sunday also map to 2026-10-09. So Friday is Monday's answer, and the series frontier 2026-10-09 is right. (c) The 16th series, cottonwood/account_units at address() (s3://opal-data-cottonwood/mdpf/cottonwood/gold/account_units/), newest date=2026-10-09, 33 partitions. (d) The lambda's own log (/aws/lambda/mdpf-gold-lambda, 13:29-13:45Z, 32,950 B read): cross-axis gate PASS for 49financial (485 dates), inflection (485) and global (494; 20 enumerated-exempt, UNCHECKED not clean); global composition gate PASS; L-1 key-set identity PASS on four types x 4 scopes; 'cycle complete: 16/16 A4 objects built; errors=none'. The packet's quote leaves out one fact: the log reads 'gold parquet: PARTIAL -- built [49financial, inflection, global] of intended [... cottonwood ...]'. Cottonwood's four 2026-10-09 objects were refused write-once as CONFLICT, so its partitions are the Saturday 2026-10-10 13:31:38Z writes. This seat read the run manifest (portal/gold/mdpf/_manifests/2026-10-09/20261012T133151Z.json: written 13, staged 4, conflict 4). All 14 differing paths across the four conflicts are provenance, vintage, value-date re-key, assignment_date, source or knowledge_date; none is a figure. Limit: ONE fire. The next trading-day fires are the standing evidence, and nothing exercises CN-d-1's guard or vintage keys (not deployed)."
  },
  {
    "id": "MDPF_CANON-D1-C-S57",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "MDPF_CANON.TO-CN-a-2 AC3 MET on the Monday fire, superseding the NOT MET this seat carried from rounds 1-2 (ADJUDICATION_v2 header; row C-S19). Graded on the scheduled fire, as the round-2 and round-4 analyses direct, not on an ad-hoc QA run. The fire wrote data.parquet at address() for every scope it built: the six frontier partitions plus account_units, and the other series were already at the frontier. Existing keys stay unchanged: 547 of 547 snapshot ETags kept, and the four cottonwood objects were refused write-once rather than overwritten, their differing paths metadata only (row C-S56). The legacy JSON matches: PARITY 12 of 12 frontier partitions value-equal to the writer's records of their legacy JSON. Limit: one fire.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD FWD-1 / FWD-7; CN-a-2 AC3; ledger/ROUND_ANALYSIS.round4.md items 3-4 (Monday fire grades FWD-1 and CN-a-2 AC3 and closes D1-S9/D1-S10; the bronze read grades FWD-7's first feed); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-a-2 AC3 MET on the Monday fire, superseding the NOT MET this seat carried from rounds 1-2 (ADJUDICATION_v2 header; row C-S19). Graded on the scheduled fire, as the round-2 and round-4 analyses direct, not on an ad-hoc QA run. The fire wrote data.parquet at address() for every scope it built: the six frontier partitions plus account_units, and the other series were already at the frontier. Existing keys stay unchanged: 547 of 547 snapshot ETags kept, and the four cottonwood objects were refused write-once rather than overwritten, their differing paths metadata only (row C-S56). The legacy JSON matches: PARITY 12 of 12 frontier partitions value-equal to the writer's records of their legacy JSON. Limit: one fire.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row MDPF_CANON-D1-C-S56",
        "ADJUDICATION_v2 (CN-a-2 AC3 carried NOT MET, D1-S9)",
        "3.0.0_SA_CVO r4_daily.py read: ARM 2 and ARM 3 PASS"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-a-2 AC3 MET on the Monday fire, superseding the NOT MET this seat carried from rounds 1-2 (ADJUDICATION_v2 header; row C-S19). Graded on the scheduled fire, as the round-2 and round-4 analyses direct, not on an ad-hoc QA run. The fire wrote data.parquet at address() for every scope it built: the six frontier partitions plus account_units, and the other series were already at the frontier. Existing keys stay unchanged: 547 of 547 snapshot ETags kept, and the four cottonwood objects were refused write-once rather than overwritten, their differing paths metadata only (row C-S56). The legacy JSON matches: PARITY 12 of 12 frontier partitions value-equal to the writer's records of their legacy JSON. Limit: one fire."
  },
  {
    "id": "MDPF_CANON-D1-C-S58",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "FWD-7's first feed, L9 read: REALIZED. Its PROOF, the on-demand receiving step run deliberately and read where it landed, was graded MET at round 3 (C-S21: 10 of 10 at address() date=2026-10-11, SSM Success). Its CONFIRMATION, the routine daily delivery landing there too, now reads twice on this seat's runs of round4/checks/r4_daily_bronze.py. For 2026-10-11 (--since 06:00Z): PULL 9 model files + 1 sentinel at the builder's date=2026-10-11 (sentinel 12:52:46Z, after the hand pull); STEP run mdpf_daily_20261011_125228 complete with STAGE0-BRONZE ok; FEEDER 3 of 3 feeds written after; OLDHOME 0 of 1030 old-prefix objects written; 4 of 4. For 2026-10-12: the same, 4 of 4 (run mdpf_daily_20261012_125232, sentinel 12:52:52Z). Limits: the feeds' values were not re-diffed against a live feed for these two days (the DELTA=0 read is round 3's, on 2026-10-09). And the 10-11 run's FEEDER arm is now satisfied by the newer 10-12 feeds too, so the 10-11 PULL and STEP arms are the day-specific evidence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD FWD-1 / FWD-7; CN-a-2 AC3; ledger/ROUND_ANALYSIS.round4.md items 3-4 (Monday fire grades FWD-1 and CN-a-2 AC3 and closes D1-S9/D1-S10; the bronze read grades FWD-7's first feed); spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-7's first feed, L9 read: REALIZED. Its PROOF, the on-demand receiving step run deliberately and read where it landed, was graded MET at round 3 (C-S21: 10 of 10 at address() date=2026-10-11, SSM Success). Its CONFIRMATION, the routine daily delivery landing there too, now reads twice on this seat's runs of round4/checks/r4_daily_bronze.py. For 2026-10-11 (--since 06:00Z): PULL 9 model files + 1 sentinel at the builder's date=2026-10-11 (sentinel 12:52:46Z, after the hand pull); STEP run mdpf_daily_20261011_125228 complete with STAGE0-BRONZE ok; FEEDER 3 of 3 feeds written after; OLDHOME 0 of 1030 old-prefix objects written; 4 of 4. For 2026-10-12: the same, 4 of 4 (run mdpf_daily_20261012_125232, sentinel 12:52:52Z). Limits: the feeds' values were not re-diffed against a live feed for these two days (the DELTA=0 read is round 3's, on 2026-10-09). And the 10-11 run's FEEDER arm is now satisfied by the newer 10-12 feeds too, so the 10-11 PULL and STEP arms are the day-specific evidence.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/READS_20261011_SUNDAY_FIRE_AND_BRONZE_HOME.md @0482b9f87e (blob cf116d32fb verified)",
        "3.0.0_SA_CVO python round4/checks/r4_daily_bronze.py --run-date 2026-10-11 --since 2026-10-11T06:00:00Z: 4 of 4",
        "3.0.0_SA_CVO python round4/checks/r4_daily_bronze.py --run-date 2026-10-12 --since 2026-10-12T06:00:00Z: 4 of 4",
        "row MDPF_CANON-D1-C-S21 (round 3, the on-demand proof)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-7's first feed, L9 read: REALIZED. Its PROOF, the on-demand receiving step run deliberately and read where it landed, was graded MET at round 3 (C-S21: 10 of 10 at address() date=2026-10-11, SSM Success). Its CONFIRMATION, the routine daily delivery landing there too, now reads twice on this seat's runs of round4/checks/r4_daily_bronze.py. For 2026-10-11 (--since 06:00Z): PULL 9 model files + 1 sentinel at the builder's date=2026-10-11 (sentinel 12:52:46Z, after the hand pull); STEP run mdpf_daily_20261011_125228 complete with STAGE0-BRONZE ok; FEEDER 3 of 3 feeds written after; OLDHOME 0 of 1030 old-prefix objects written; 4 of 4. For 2026-10-12: the same, 4 of 4 (run mdpf_daily_20261012_125232, sentinel 12:52:52Z). Limits: the feeds' values were not re-diffed against a live feed for these two days (the DELTA=0 read is round 3's, on 2026-10-09). And the 10-11 run's FEEDER arm is now satisfied by the newer 10-12 feeds too, so the 10-11 PULL and STEP arms are the day-specific evidence."
  },
  {
    "id": "MDPF_CANON-D1-C-S59",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "D1-S9 (REMEDIATION_v2) closes REMEDIATED; only remediation.state and closed move. Its close condition holds on this seat's read: one scheduled fire (Monday 13:30Z) has 16 of 16 at address(). The 12 of the tool's arms plus cottonwood/account_units and the frontier read are in C-S56; cottonwood's four are Saturday's write-once partitions with metadata-only conflicts. r4_daily.py, the round-4 successor of r2_daily.py, reads 4 of 4, and CN-a-2 AC3 grades MET (C-S57). The weekend failures the row named (global refused, 49financial A7 skip, inflection CONFLICT) are the D1-S10 weekend shape: Monday's log shows all three scopes' gates PASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S9"
    ],
    "spec_asserts": "MDPF_CANON PRD FWD-1 / FWD-7; CN-a-2 AC3; ledger/ROUND_ANALYSIS.round4.md items 3-4 (Monday fire grades FWD-1 and CN-a-2 AC3 and closes D1-S9/D1-S10; the bronze read grades FWD-7's first feed); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S9 (REMEDIATION_v2) closes REMEDIATED; only remediation.state and closed move. Its close condition holds on this seat's read: one scheduled fire (Monday 13:30Z) has 16 of 16 at address(). The 12 of the tool's arms plus cottonwood/account_units and the frontier read are in C-S56; cottonwood's four are Saturday's write-once partitions with metadata-only conflicts. r4_daily.py, the round-4 successor of r2_daily.py, reads 4 of 4, and CN-a-2 AC3 grades MET (C-S57). The weekend failures the row named (global refused, 49financial A7 skip, inflection CONFLICT) are the D1-S10 weekend shape: Monday's log shows all three scopes' gates PASS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediation row MDPF_CANON-D1-S9 (REMEDIATION_v2)",
        "rows MDPF_CANON-D1-C-S56 and C-S57"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S9 (REMEDIATION_v2) closes REMEDIATED; only remediation.state and closed move. Its close condition holds on this seat's read: one scheduled fire (Monday 13:30Z) has 16 of 16 at address(). The 12 of the tool's arms plus cottonwood/account_units and the frontier read are in C-S56; cottonwood's four are Saturday's write-once partitions with metadata-only conflicts. r4_daily.py, the round-4 successor of r2_daily.py, reads 4 of 4, and CN-a-2 AC3 grades MET (C-S57). The weekend failures the row named (global refused, 49financial A7 skip, inflection CONFLICT) are the D1-S10 weekend shape: Monday's log shows all three scopes' gates PASS."
  },
  {
    "id": "MDPF_CANON-D1-C-S60",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "D1-S10 (REMEDIATION_v3) closes REMEDIATED; only remediation.state and closed move. Its close condition holds: the rule is written (ROUND_ANALYSIS.round3.md section 2: the weekend refusal stays, no calendar-aware skip, Monday is the first fire at Friday's frontier) and the first fire it names is read. Monday 2026-10-12 built global at 2026-10-09 (the global cross-axis gate PASS over 494 dates; C-S56), while the Sunday read in the issuer's file shows the predicted weekend refusal of global alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S10"
    ],
    "spec_asserts": "MDPF_CANON PRD FWD-1 / FWD-7; CN-a-2 AC3; ledger/ROUND_ANALYSIS.round4.md items 3-4 (Monday fire grades FWD-1 and CN-a-2 AC3 and closes D1-S9/D1-S10; the bronze read grades FWD-7's first feed); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S10 (REMEDIATION_v3) closes REMEDIATED; only remediation.state and closed move. Its close condition holds: the rule is written (ROUND_ANALYSIS.round3.md section 2: the weekend refusal stays, no calendar-aware skip, Monday is the first fire at Friday's frontier) and the first fire it names is read. Monday 2026-10-12 built global at 2026-10-09 (the global cross-axis gate PASS over 494 dates; C-S56), while the Sunday read in the issuer's file shows the predicted weekend refusal of global alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediation row MDPF_CANON-D1-S10 (REMEDIATION_v3)",
        "ledger/ROUND_ANALYSIS.round3.md section 2",
        "row MDPF_CANON-D1-C-S56"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S10 (REMEDIATION_v3) closes REMEDIATED; only remediation.state and closed move. Its close condition holds: the rule is written (ROUND_ANALYSIS.round3.md section 2: the weekend refusal stays, no calendar-aware skip, Monday is the first fire at Friday's frontier) and the first fire it names is read. Monday 2026-10-12 built global at 2026-10-09 (the global cross-axis gate PASS over 494 dates; C-S56), while the Sunday read in the issuer's file shows the predicted weekend refusal of global alone."
  }
]
```
