# MDPF_SECCLASS -- round 22 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-12T11:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T11:15:00Z. L8 packet: 2.0.0_SA_COO~M1 msg 4331, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R22_20261012.md @d9197bde0e
(7,514 B, blob a4fd8a7fe4, verified). Swept by DISPOSITION, not only by time: 7 investigation rows were undispositioned (D1-S31 and
D1-W85-S1..S6; five carry surfaced_at 10:14:38Z, before v19's 10:20Z watermark, but landed after it). 1 ARMED+BLOCKING dismissed disarmed,
6 INERT dismissed; nothing graduates. D1-W83-S5 stays ARMED (REMEDIATION_v12) for the CTO's ruling.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S13",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T11:15:00Z",
    "one_line": "L9 read of the round-22 packet (16 orders, 11 complete, judgment 0; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict). SC-e-95 (risk LOCAL, a read): HOLDS. The record's check reads ok=True on this seat's run; this seat's own S3 reads reproduce its structural facts (the 09-04 harness control has one version, unchanged since 2026-09-22; 10-06..08 changed content after their first build; B_00's catalog line is --force-recent-days 14) and SC-e-91 is live since 09:55:03Z (live C_06 bytes equal the merged fix). Correction: the packet's 'no byte moved' on 2026-10-09 is not literal: the partition changed at 2026-10-12T00:33:48Z (4 rows' units and market_value), with the same row count and the same dollar sum, so the read's byte drift of $0.00 holds in dollars. Not re-derived by this seat: the first-build and rebuilt snapshots (the 130-291 s, 3.3 GB re-derive); those figures are the worker's. RECONCILIATION with round 21's reach split (all at 2026-10-09, mix level $1,846,399.46 = listed $1,326,892.62 + unlisted $519,506.84): the rebuilt Unclassified $883,483.05 equals listed-but-unresolved ($1,326,892.62 - $653,857.12 = $673,035.50) plus the unlisted holdings no classifier places ($210,486.42, 22 blank-ticker structured notes and bonds), $883,521.92, within $38.87; the re-derive's move beyond SC-e-91's maximum, $962,915.51 - $653,857.12 = $309,058.39, equals the unlisted dollars a classifier now places ($519,506.84 - $210,486.42 = $309,020.42), within $37.97. Both gaps sit inside W85-S6's class-versus-total rounding (up to $128.58). So of the $519,506.84 outside the stored lists, about $309,020 moves by a re-derive and $210,486.42 moves by none of the options. WHAT EACH OPTION MOVES, from the read's evidence (the ruling is 1.0.0_SA_CTO~DELL1's; this seat chooses none): (a) ROLLING RE-DERIVE of the last N dates each fire (the read costed N=1, 3, 5: +41-207 s warm per fire, about 8.3-8.8 GB written): at 2026-10-09 Unclassified $1,846,399.46 -> $883,483.05 (-$962,915.51); each date in the window also takes its byte drift (10-06 -$1,348,764.69, 10-07 -$1,491,953.65, 10-08 -$1,933,192.78, class sums) and its reference drift (10-06 Unclassified -$140.16M, equity +$64.25M, structured +$62.59M; 10-07..09 Unclassified about -$0.96M each); it keeps absorbing B_00's re-puts inside the window, but B_00 moves dates up to 14 days back and its oldest content change reached 20 trading days, so a window shorter than that leaves older moves frozen. (b) ONE-OFF REBUILD of 2026-10-06..09: the same restatement once (the same per-date figures as (a)); afterwards B_00's --force-recent-days 14 moves those dates again and they freeze on the rebuilt version; the harness control shows any rebuild restates even an untouched date by reference drift (+$1,106,362.48 class sum at 2026-09-04). (c) ACCEPT: the served snapshots stay as frozen; 2026-10-09 Unclassified moves only by SC-e-91 on its first scheduled fire, $0 to $653,857.12, leaving at least $1,192,475.61 of the served $1,846,332.73; 10-06..08 stay on superseded bytes and the first-build reference, with the dollars above named as the accepted drift. round-close-check --round 22: MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-22 packet (16 orders, 11 complete, judgment 0; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict). SC-e-95 (risk LOCAL, a read): HOLDS. The record's check reads ok=True on this seat's run; this seat's own S3 reads reproduce its structural facts (the 09-04 harness control has one version, unchanged since 2026-09-22; 10-06..08 changed content after their first build; B_00's catalog line is --force-recent-days 14) and SC-e-91 is live since 09:55:03Z (live C_06 bytes equal the merged fix). Correction: the packet's 'no byte moved' on 2026-10-09 is not literal: the partition changed at 2026-10-12T00:33:48Z (4 rows' units and market_value), with the same row count and the same dollar sum, so the read's byte drift of $0.00 holds in dollars. Not re-derived by this seat: the first-build and rebuilt snapshots (the 130-291 s, 3.3 GB re-derive); those figures are the worker's. RECONCILIATION with round 21's reach split (all at 2026-10-09, mix level $1,846,399.46 = listed $1,326,892.62 + unlisted $519,506.84): the rebuilt Unclassified $883,483.05 equals listed-but-unresolved ($1,326,892.62 - $653,857.12 = $673,035.50) plus the unlisted holdings no classifier places ($210,486.42, 22 blank-ticker structured notes and bonds), $883,521.92, within $38.87; the re-derive's move beyond SC-e-91's maximum, $962,915.51 - $653,857.12 = $309,058.39, equals the unlisted dollars a classifier now places ($519,506.84 - $210,486.42 = $309,020.42), within $37.97. Both gaps sit inside W85-S6's class-versus-total rounding (up to $128.58). So of the $519,506.84 outside the stored lists, about $309,020 moves by a re-derive and $210,486.42 moves by none of the options. WHAT EACH OPTION MOVES, from the read's evidence (the ruling is 1.0.0_SA_CTO~DELL1's; this seat chooses none): (a) ROLLING RE-DERIVE of the last N dates each fire (the read costed N=1, 3, 5: +41-207 s warm per fire, about 8.3-8.8 GB written): at 2026-10-09 Unclassified $1,846,399.46 -> $883,483.05 (-$962,915.51); each date in the window also takes its byte drift (10-06 -$1,348,764.69, 10-07 -$1,491,953.65, 10-08 -$1,933,192.78, class sums) and its reference drift (10-06 Unclassified -$140.16M, equity +$64.25M, structured +$62.59M; 10-07..09 Unclassified about -$0.96M each); it keeps absorbing B_00's re-puts inside the window, but B_00 moves dates up to 14 days back and its oldest content change reached 20 trading days, so a window shorter than that leaves older moves frozen. (b) ONE-OFF REBUILD of 2026-10-06..09: the same restatement once (the same per-date figures as (a)); afterwards B_00's --force-recent-days 14 moves those dates again and they freeze on the rebuilt version; the harness control shows any rebuild restates even an untouched date by reference drift (+$1,106,362.48 class sum at 2026-09-04). (c) ACCEPT: the served snapshots stay as frozen; 2026-10-09 Unclassified moves only by SC-e-91 on its first scheduled fire, $0 to $653,857.12, leaving at least $1,192,475.61 of the served $1,846,332.73; 10-06..08 stay on superseded bytes and the first-build reference, with the dollars above named as the accepted drift. round-close-check --round 22: MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R22_CHECKS/r22_residual_read_check.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json at box/dell1: R22-RESIDUAL ok=True dates=4 control_byte_drift=0.0 control_reference_drift=1106362.48 rederive=3 movers_dates=8 control=ok",
        "3.0.0_SA_CVO list-object-versions s3://opal-data-bd/gold/canonical/holdings/: 2026-09-04 1 version (ETag unchanged since 2026-09-22T23:15:37Z); 2026-10-06 9 versions / 5 distinct ETags; 2026-10-07 7 / 5; 2026-10-08 5 / 3; 2026-10-09 3 / 2; latest content 2026-10-12T04:16:42Z",
        "3.0.0_SA_CVO pyarrow read of the 2026-10-09 partition versions: 04:16:35Z 10-11 (the first-build input) and 00:33:48Z 10-12 differ in content (4 rows' units, bd_units and market_value differ positionally) with the same 114,554 rows and the same market_value sum 2,015,391,646.72",
        "3.0.0_SA_CVO head-object code/gold/C_06.client_mix_timeseries.py: ETag 2e35d043163cc18b135d7698cf11dc56 LastModified 2026-10-12T09:55:03Z; its sha256 62e425b5a5ca4d92 equals data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py at HEAD and at e270f70be4 (SC-e-91 live)",
        "data/black_diamond/scripts/gold/gold_dispatch.sh:99 'B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14' (read at box/dell1 HEAD)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json",
        "round 21 Reach split: adjudication row MDPF_SECCLASS-D1-C-S7 and REMEDIATION_v12 row MDPF_SECCLASS-D1-W80-S4",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_SECCLASS --round 22: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-22 packet (16 orders, 11 complete, judgment 0; TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict). SC-e-95 (risk LOCAL, a read): HOLDS. The record's check reads ok=True on this seat's run; this seat's own S3 reads reproduce its structural facts (the 09-04 harness control has one version, unchanged since 2026-09-22; 10-06..08 changed content after their first build; B_00's catalog line is --force-recent-days 14) and SC-e-91 is live since 09:55:03Z (live C_06 bytes equal the merged fix). Correction: the packet's 'no byte moved' on 2026-10-09 is not literal: the partition changed at 2026-10-12T00:33:48Z (4 rows' units and market_value), with the same row count and the same dollar sum, so the read's byte drift of $0.00 holds in dollars. Not re-derived by this seat: the first-build and rebuilt snapshots (the 130-291 s, 3.3 GB re-derive); those figures are the worker's. RECONCILIATION with round 21's reach split (all at 2026-10-09, mix level $1,846,399.46 = listed $1,326,892.62 + unlisted $519,506.84): the rebuilt Unclassified $883,483.05 equals listed-but-unresolved ($1,326,892.62 - $653,857.12 = $673,035.50) plus the unlisted holdings no classifier places ($210,486.42, 22 blank-ticker structured notes and bonds), $883,521.92, within $38.87; the re-derive's move beyond SC-e-91's maximum, $962,915.51 - $653,857.12 = $309,058.39, equals the unlisted dollars a classifier now places ($519,506.84 - $210,486.42 = $309,020.42), within $37.97. Both gaps sit inside W85-S6's class-versus-total rounding (up to $128.58). So of the $519,506.84 outside the stored lists, about $309,020 moves by a re-derive and $210,486.42 moves by none of the options. WHAT EACH OPTION MOVES, from the read's evidence (the ruling is 1.0.0_SA_CTO~DELL1's; this seat chooses none): (a) ROLLING RE-DERIVE of the last N dates each fire (the read costed N=1, 3, 5: +41-207 s warm per fire, about 8.3-8.8 GB written): at 2026-10-09 Unclassified $1,846,399.46 -> $883,483.05 (-$962,915.51); each date in the window also takes its byte drift (10-06 -$1,348,764.69, 10-07 -$1,491,953.65, 10-08 -$1,933,192.78, class sums) and its reference drift (10-06 Unclassified -$140.16M, equity +$64.25M, structured +$62.59M; 10-07..09 Unclassified about -$0.96M each); it keeps absorbing B_00's re-puts inside the window, but B_00 moves dates up to 14 days back and its oldest content change reached 20 trading days, so a window shorter than that leaves older moves frozen. (b) ONE-OFF REBUILD of 2026-10-06..09: the same restatement once (the same per-date figures as (a)); afterwards B_00's --force-recent-days 14 moves those dates again and they freeze on the rebuilt version; the harness control shows any rebuild restates even an untouched date by reference drift (+$1,106,362.48 class sum at 2026-09-04). (c) ACCEPT: the served snapshots stay as frozen; 2026-10-09 Unclassified moves only by SC-e-91 on its first scheduled fire, $0 to $653,857.12, leaving at least $1,192,475.61 of the served $1,846,332.73; 10-06..08 stay on superseded bytes and the first-build reference, with the dollars above named as the accepted drift. round-close-check --round 22: MAY-CLOSE."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S14",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T11:15:00Z",
    "one_line": "D1-W85-S1 (BLOCKING, ARMED) dismissed, disarmed: the issuer's amendment @560873ea45 (merged 1480f5008c) reads three snapshots (served, first build, current) and treats 2026-09-04 as a HARNESS control (one version, byte drift within $1.00, repeatable) whose reference drift is a result. This seat's run of the amended check reads control_byte_drift=0.0 with control=ok, and its own version read shows 09-04 with one version. The conflation the worker stopped on (reference drift read as byte drift) is resolved.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W85-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W85-S1 (BLOCKING, ARMED) dismissed, disarmed: the issuer's amendment @560873ea45 (merged 1480f5008c) reads three snapshots (served, first build, current) and treats 2026-09-04 as a HARNESS control (one version, byte drift within $1.00, repeatable) whose reference drift is a result. This seat's run of the amended check reads control_byte_drift=0.0 with control=ok, and its own version read shows 09-04 with one version. The conflation the worker stopped on (reference drift read as byte drift) is resolved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R22_CHECKS/r22_residual_read_check.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESIDUAL_READ_C06_FREEZE_20261012.json at box/dell1: R22-RESIDUAL ok=True dates=4 control_byte_drift=0.0 control_reference_drift=1106362.48 rederive=3 movers_dates=8 control=ok",
        "3.0.0_SA_CVO list-object-versions s3://opal-data-bd/gold/canonical/holdings/: 2026-09-04 1 version (ETag unchanged since 2026-09-22T23:15:37Z); 2026-10-06 9 versions / 5 distinct ETags; 2026-10-07 7 / 5; 2026-10-08 5 / 3; 2026-10-09 3 / 2; latest content 2026-10-12T04:16:42Z",
        "investigation row MDPF_SECCLASS-D1-W85-S1 (disarm_owner 2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W85-S1 (BLOCKING, ARMED) dismissed, disarmed: the issuer's amendment @560873ea45 (merged 1480f5008c) reads three snapshots (served, first build, current) and treats 2026-09-04 as a HARNESS control (one version, byte drift within $1.00, repeatable) whose reference drift is a result. This seat's run of the amended check reads control_byte_drift=0.0 with control=ok, and its own version read shows 09-04 with one version. The conflation the worker stopped on (reference drift read as byte drift) is resolved."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S15",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T11:15:00Z",
    "one_line": "D1-S31, D1-W85-S2, D1-W85-S3, D1-W85-S4, D1-W85-S5 and D1-W85-S6 (all INERT) dismissed: D1-S31 records D1-W83-S5 BOUNDED (three retained dates, none added; the latest as_of unaffected) per CTO msg 4327, and W83-S5 stays ARMED in REMEDIATION_v12 for the ruling above; W85-S2 (stale line citations), S3 (no StopInstances event, so the fire's runtime is a lower bound), S4 (the 15.5 s C_06 run is the pre-ship early return) and S5 (B_00's nightly --force-recent-days 14 cadence, confirmed by this seat's read of gold_dispatch.sh:99) stand as the read's recorded limits; S6 (class dollars versus the total field differ by up to $128.58 per snapshot) is the rounding that bounds this seat's $38-39 reconciliation gaps.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S31",
      "MDPF_SECCLASS-D1-W85-S2",
      "MDPF_SECCLASS-D1-W85-S3",
      "MDPF_SECCLASS-D1-W85-S4",
      "MDPF_SECCLASS-D1-W85-S5",
      "MDPF_SECCLASS-D1-W85-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S31, D1-W85-S2, D1-W85-S3, D1-W85-S4, D1-W85-S5 and D1-W85-S6 (all INERT) dismissed: D1-S31 records D1-W83-S5 BOUNDED (three retained dates, none added; the latest as_of unaffected) per CTO msg 4327, and W83-S5 stays ARMED in REMEDIATION_v12 for the ruling above; W85-S2 (stale line citations), S3 (no StopInstances event, so the fire's runtime is a lower bound), S4 (the 15.5 s C_06 run is the pre-ship early return) and S5 (B_00's nightly --force-recent-days 14 cadence, confirmed by this seat's read of gold_dispatch.sh:99) stand as the read's recorded limits; S6 (class dollars versus the total field differ by up to $128.58 per snapshot) is the rounding that bounds this seat's $38-39 reconciliation gaps.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh:99 'B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14' (read at box/dell1 HEAD)",
        "investigation rows as listed",
        "adjudication row MDPF_SECCLASS-D1-C-S13 (reconciliation)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S31, D1-W85-S2, D1-W85-S3, D1-W85-S4, D1-W85-S5 and D1-W85-S6 (all INERT) dismissed: D1-S31 records D1-W83-S5 BOUNDED (three retained dates, none added; the latest as_of unaffected) per CTO msg 4327, and W83-S5 stays ARMED in REMEDIATION_v12 for the ruling above; W85-S2 (stale line citations), S3 (no StopInstances event, so the fire's runtime is a lower bound), S4 (the 15.5 s C_06 run is the pre-ship early return) and S5 (B_00's nightly --force-recent-days 14 cadence, confirmed by this seat's read of gold_dispatch.sh:99) stand as the read's recorded limits; S6 (class dollars versus the total field differ by up to $128.58 per snapshot) is the rounding that bounds this seat's $38-39 reconciliation gaps."
  }
]
```
