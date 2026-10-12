# MDPF_SECCLASS -- round 23 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-12T14:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T14:30:00Z. L8 packet: 2.0.0_SA_COO~M1 msg 4343, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R23_20261012.md @f000eb436f
(7,421 B, blob e3611b63f4, verified). Swept by disposition: 7 undispositioned rows (D1-W86-S1..S6, D1-W87-S1), all dismissed; this seat files
one new ARMED finding (C-S17: the SC-e-97 pair names no firm-total move) and graduates it. D1-W83-S5 stays ARMED (REMEDIATION_v12).

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S16",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:30:00Z",
    "one_line": "L9 read of the round-23 packet (18 orders, 13 complete; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict): SC-e-96 and SC-e-98 (reads) and SC-e-97 (risk SERVED, built and merged @772b5c9f02, NOT live: the served C_06 is SC-e-91's 09:55:03Z object) HOLD on this seat's re-run of every criterion. THE $75.9M-$153.0M A DAY: reproduced to the cent from the served firm snapshots. It is the D_04 remainder (total minus the six canonical classes) on 2026-09-30..10-06, held in the legacy 'unclassified' key of snapshots C_06 built before the current classifier; a rebuild leaves $0 to $53,010.45 there. So it is a RECLASSIFICATION across classes, not an Unclassified-only figure: those dollars move into canonical classes (the record does not split which). It is not two orders above round 22: round 22 measured 10-06's reference drift at -$140.16M Unclassified (equity +$64.25M, structured +$62.59M); the ~$0.3M of round 22 was the unlisted share at 10-09. On 10-03..10-05 a further ~$6.5M sits in neither a canonical class nor the 'unclassified' key (row W86-S5, reproduced: 10-03 remainder minus key 6,480,424.81). SERVED KEYS the window reaches (from the half request, confirmed against the code it cites): gold/views/mix_daily_summary.json (firm and advisor days), 3,274 relationship JSONs and views with legacy copies (13,096 keys), D_03's firm_mix_views(_daily).json and advisor mix/mix_daily/mix_timeseries.json, and D_04's platinum/firm/mix_summary.json mix (10-09), mix_periods (the Q3 and September 2026 bars ending 2026-09-30; Q4, October and 2026 ending 10-09) and composition.mix. FIRM TOTAL: not measured by the issuer; this seat's proxy says it likely moves (row C-S17). Issuer amendments (TO-SC-e96 @85664b5801; TO-SC-e97 @7ebc58f42f, @d4a47f548a): no gate limb graded them; both sound on this seat's runs. round-close-check --round 23: MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-23 packet (18 orders, 13 complete; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict): SC-e-96 and SC-e-98 (reads) and SC-e-97 (risk SERVED, built and merged @772b5c9f02, NOT live: the served C_06 is SC-e-91's 09:55:03Z object) HOLD on this seat's re-run of every criterion. THE $75.9M-$153.0M A DAY: reproduced to the cent from the served firm snapshots. It is the D_04 remainder (total minus the six canonical classes) on 2026-09-30..10-06, held in the legacy 'unclassified' key of snapshots C_06 built before the current classifier; a rebuild leaves $0 to $53,010.45 there. So it is a RECLASSIFICATION across classes, not an Unclassified-only figure: those dollars move into canonical classes (the record does not split which). It is not two orders above round 22: round 22 measured 10-06's reference drift at -$140.16M Unclassified (equity +$64.25M, structured +$62.59M); the ~$0.3M of round 22 was the unlisted share at 10-09. On 10-03..10-05 a further ~$6.5M sits in neither a canonical class nor the 'unclassified' key (row W86-S5, reproduced: 10-03 remainder minus key 6,480,424.81). SERVED KEYS the window reaches (from the half request, confirmed against the code it cites): gold/views/mix_daily_summary.json (firm and advisor days), 3,274 relationship JSONs and views with legacy copies (13,096 keys), D_03's firm_mix_views(_daily).json and advisor mix/mix_daily/mix_timeseries.json, and D_04's platinum/firm/mix_summary.json mix (10-09), mix_periods (the Q3 and September 2026 bars ending 2026-09-30; Q4, October and 2026 ending 10-09) and composition.mix. FIRM TOTAL: not measured by the issuer; this seat's proxy says it likely moves (row C-S17). Issuer amendments (TO-SC-e96 @85664b5801; TO-SC-e97 @7ebc58f42f, @d4a47f548a): no gate limb graded them; both sound on this seat's runs. round-close-check --round 23: MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py window-read|rederive|wiring|half|unlisted at box/dell1: WINDOW-READ ok=True dates=15; ROLLING-REDERIVE ok=True (rule, window, restated, outside_untouched, idempotent, orphan_removed); ROLLING-WIRING ok=True (no_typed_window=True); HALF-REQUEST ok=True 7 of 7; UNLISTED ok=True securities=32 total=883483.05 unplaced=210486.42; pytest data/black_diamond/scripts/gold/tests 179 passed",
        "3.0.0_SA_CVO read s3://opal-data-bd/gold/views/mix_daily_summary.json (LastModified 2026-10-11T05:23:28Z) firm[date] 2026-09-24..10-09: 09-24..09-29 carry no commodities/structured/cash keys and a remainder of -$80.37..$73.19; 09-30..10-06 carry all six classes plus legacy 'unclassified' and 'other' keys, remainder (total minus the six classes) 76,259,877.65 / 75,964,048.04 / 150,433,862.60 / 152,418,257.84 / 152,995,165.84 / 148,224,563.78 / 140,161,790.57, held in the 'unclassified' key (76,259,973.86 .. 140,161,795.27; 'other' 0.00); 10-07..10-09 remainder 998,762.85 / 972,621.40 / 1,846,332.73",
        "3.0.0_SA_CVO pyarrow sum of market_value over the CURRENT gold/canonical/holdings/<date>.parquet vs the served firm[date].total: equal to the cent on 2026-10-09 only (2,015,391,646.72); above served by 32,079,997.98 (09-25), 224,041,973.12 (09-26), 223,812,108.95 (09-27), 270,086,670.20 (09-28), 179,758,545.96 (09-29), 172,345,196.98 (09-30), 173,097,836.54 (10-01), 28,215,020.75 (10-02), 5,203.59 (10-03), 48,507.12 (10-04), 21,236,498.17 (10-05), 21,798,230.14 (10-06), 21,542,619.84 (10-07), 21,045,481.88 (10-08)",
        "3.0.0_SA_CVO head-object code/gold/C_06.client_mix_timeseries.py: ETag 2e35d043... LastModified 2026-10-12T09:55:03Z (SC-e-91's ship; SC-e-97 not live)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md (Blast radius, Both branches, the per-date table)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/WINDOW_READ_C06_ROLLING_20261012.json",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_SECCLASS --round 23: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-23 packet (18 orders, 13 complete; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict): SC-e-96 and SC-e-98 (reads) and SC-e-97 (risk SERVED, built and merged @772b5c9f02, NOT live: the served C_06 is SC-e-91's 09:55:03Z object) HOLD on this seat's re-run of every criterion. THE $75.9M-$153.0M A DAY: reproduced to the cent from the served firm snapshots. It is the D_04 remainder (total minus the six canonical classes) on 2026-09-30..10-06, held in the legacy 'unclassified' key of snapshots C_06 built before the current classifier; a rebuild leaves $0 to $53,010.45 there. So it is a RECLASSIFICATION across classes, not an Unclassified-only figure: those dollars move into canonical classes (the record does not split which). It is not two orders above round 22: round 22 measured 10-06's reference drift at -$140.16M Unclassified (equity +$64.25M, structured +$62.59M); the ~$0.3M of round 22 was the unlisted share at 10-09. On 10-03..10-05 a further ~$6.5M sits in neither a canonical class nor the 'unclassified' key (row W86-S5, reproduced: 10-03 remainder minus key 6,480,424.81). SERVED KEYS the window reaches (from the half request, confirmed against the code it cites): gold/views/mix_daily_summary.json (firm and advisor days), 3,274 relationship JSONs and views with legacy copies (13,096 keys), D_03's firm_mix_views(_daily).json and advisor mix/mix_daily/mix_timeseries.json, and D_04's platinum/firm/mix_summary.json mix (10-09), mix_periods (the Q3 and September 2026 bars ending 2026-09-30; Q4, October and 2026 ending 10-09) and composition.mix. FIRM TOTAL: not measured by the issuer; this seat's proxy says it likely moves (row C-S17). Issuer amendments (TO-SC-e96 @85664b5801; TO-SC-e97 @7ebc58f42f, @d4a47f548a): no gate limb graded them; both sound on this seat's runs. round-close-check --round 23: MAY-CLOSE."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S17",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:30:00Z",
    "one_line": "The SC-e-97 pair's blast radius names no firm-total or AUA move, yet the window restatement can change them: the half request says the total_aua and cube totals for the window days are 'not in the record and are not measured', and its own orphan columns show relationships in the current partition but not stored (18..205 a day; 172..205 on 09-26..09-28) and stored relationships absent from the partition (up to 15 a day, which branch 3 removes). This seat's proxy, the current partition's market_value sum, equals the served firm total to the cent only on 2026-10-09 and sits $5,203.59 to $270,086,670.20 ABOVE it on the other 14 window dates. The proxy is not the rebuild (it disagrees with round 22's re-derived byte drift of -$1.35M..-$1.93M on 10-06..08), so the size of the firm-total move is NOT established; that it is not zero is likely. The advisor map also drops advisors with no window day (W86-S4, carried by D1-W80-S3), which is a served change the pair does not name either.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~M1",
    "spec_asserts": "CLAUDE.md section 5 (NEVER move served output without never-widen sign-off): the sign-off names the act's blast radius and covers BOTH branches; a served restatement of daily firm totals and AUA is in that radius.",
    "world_is": "The SC-e-97 pair's blast radius names no firm-total or AUA move, yet the window restatement can change them: the half request says the total_aua and cube totals for the window days are 'not in the record and are not measured', and its own orphan columns show relationships in the current partition but not stored (18..205 a day; 172..205 on 09-26..09-28) and stored relationships absent from the partition (up to 15 a day, which branch 3 removes). This seat's proxy, the current partition's market_value sum, equals the served firm total to the cent only on 2026-10-09 and sits $5,203.59 to $270,086,670.20 ABOVE it on the other 14 window dates. The proxy is not the rebuild (it disagrees with round 22's re-derived byte drift of -$1.35M..-$1.93M on 10-06..08), so the size of the firm-total move is NOT established; that it is not zero is likely. The advisor map also drops advisors with no window day (W86-S4, carried by D1-W80-S3), which is a served change the pair does not name either.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO pyarrow sum of market_value over the CURRENT gold/canonical/holdings/<date>.parquet vs the served firm[date].total: equal to the cent on 2026-10-09 only (2,015,391,646.72); above served by 32,079,997.98 (09-25), 224,041,973.12 (09-26), 223,812,108.95 (09-27), 270,086,670.20 (09-28), 179,758,545.96 (09-29), 172,345,196.98 (09-30), 173,097,836.54 (10-01), 28,215,020.75 (10-02), 5,203.59 (10-03), 48,507.12 (10-04), 21,236,498.17 (10-05), 21,798,230.14 (10-06), 21,542,619.84 (10-07), 21,045,481.88 (10-08)",
        "3.0.0_SA_CVO read s3://opal-data-bd/gold/views/mix_daily_summary.json (LastModified 2026-10-11T05:23:28Z) firm[date] 2026-09-24..10-09: 09-24..09-29 carry no commodities/structured/cash keys and a remainder of -$80.37..$73.19; 09-30..10-06 carry all six classes plus legacy 'unclassified' and 'other' keys, remainder (total minus the six classes) 76,259,877.65 / 75,964,048.04 / 150,433,862.60 / 152,418,257.84 / 152,995,165.84 / 148,224,563.78 / 140,161,790.57, held in the 'unclassified' key (76,259,973.86 .. 140,161,795.27; 'other' 0.00); 10-07..10-09 remainder 998,762.85 / 972,621.40 / 1,846,332.73",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md :28 ('not in the record and are not measured') and the orphan columns of its per-date table",
        "investigation row MDPF_SECCLASS-D1-W86-S4; REMEDIATION_v12 row MDPF_SECCLASS-D1-W80-S3"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v13.md."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S18",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:30:00Z",
    "one_line": "D1-W86-S1 and D1-W86-S6 (BLOCKING) dismissed, dispositioned by the issuer's amendments and confirmed on this seat's reads: S1 (no 'unclassified' key on 09-25..09-29) is answered by reading D_04's own rule (this seat's served read: those days lack the key, remainder -$42.04..$73.19); S6 (the naming gate refusing an S3 key literal) is answered by reading only the sibling gold_dispatch.sh (ROLLING-WIRING no_typed_window=True). D1-W87-S1 dismissed: the 10-09 partition's newer version has the same rows and dollar sum (this seat's round-22 read). D1-W86-S2 (cost instrument), D1-W86-S3 (the -$962,915.51 against its inputs, inside the $128.58 rounding), D1-W86-S5 (key vs remainder ~$6.5M on 10-03..05, reproduced; the restatement replaces those days whole) stand as the read records them. D1-W86-S4 (advisor map carries this fire's advisors only) is carried by REMEDIATION_v12 D1-W80-S3 and named in C-S17's remedy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W86-S1",
      "MDPF_SECCLASS-D1-W86-S6",
      "MDPF_SECCLASS-D1-W87-S1",
      "MDPF_SECCLASS-D1-W86-S2",
      "MDPF_SECCLASS-D1-W86-S3",
      "MDPF_SECCLASS-D1-W86-S5",
      "MDPF_SECCLASS-D1-W86-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W86-S1 and D1-W86-S6 (BLOCKING) dismissed, dispositioned by the issuer's amendments and confirmed on this seat's reads: S1 (no 'unclassified' key on 09-25..09-29) is answered by reading D_04's own rule (this seat's served read: those days lack the key, remainder -$42.04..$73.19); S6 (the naming gate refusing an S3 key literal) is answered by reading only the sibling gold_dispatch.sh (ROLLING-WIRING no_typed_window=True). D1-W87-S1 dismissed: the 10-09 partition's newer version has the same rows and dollar sum (this seat's round-22 read). D1-W86-S2 (cost instrument), D1-W86-S3 (the -$962,915.51 against its inputs, inside the $128.58 rounding), D1-W86-S5 (key vs remainder ~$6.5M on 10-03..05, reproduced; the restatement replaces those days whole) stand as the read records them. D1-W86-S4 (advisor map carries this fire's advisors only) is carried by REMEDIATION_v12 D1-W80-S3 and named in C-S17's remedy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read s3://opal-data-bd/gold/views/mix_daily_summary.json (LastModified 2026-10-11T05:23:28Z) firm[date] 2026-09-24..10-09: 09-24..09-29 carry no commodities/structured/cash keys and a remainder of -$80.37..$73.19; 09-30..10-06 carry all six classes plus legacy 'unclassified' and 'other' keys, remainder (total minus the six classes) 76,259,877.65 / 75,964,048.04 / 150,433,862.60 / 152,418,257.84 / 152,995,165.84 / 148,224,563.78 / 140,161,790.57, held in the 'unclassified' key (76,259,973.86 .. 140,161,795.27; 'other' 0.00); 10-07..10-09 remainder 998,762.85 / 972,621.40 / 1,846,332.73",
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R23_CHECKS/r23_checks.py window-read|rederive|wiring|half|unlisted at box/dell1: WINDOW-READ ok=True dates=15; ROLLING-REDERIVE ok=True (rule, window, restated, outside_untouched, idempotent, orphan_removed); ROLLING-WIRING ok=True (no_typed_window=True); HALF-REQUEST ok=True 7 of 7; UNLISTED ok=True securities=32 total=883483.05 unplaced=210486.42; pytest data/black_diamond/scripts/gold/tests 179 passed",
        "investigation rows as listed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W86-S1 and D1-W86-S6 (BLOCKING) dismissed, dispositioned by the issuer's amendments and confirmed on this seat's reads: S1 (no 'unclassified' key on 09-25..09-29) is answered by reading D_04's own rule (this seat's served read: those days lack the key, remainder -$42.04..$73.19); S6 (the naming gate refusing an S3 key literal) is answered by reading only the sibling gold_dispatch.sh (ROLLING-WIRING no_typed_window=True). D1-W87-S1 dismissed: the 10-09 partition's newer version has the same rows and dollar sum (this seat's round-22 read). D1-W86-S2 (cost instrument), D1-W86-S3 (the -$962,915.51 against its inputs, inside the $128.58 rounding), D1-W86-S5 (key vs remainder ~$6.5M on 10-03..05, reproduced; the restatement replaces those days whole) stand as the read records them. D1-W86-S4 (advisor map carries this fire's advisors only) is carried by REMEDIATION_v12 D1-W80-S3 and named in C-S17's remedy."
  }
]
```
