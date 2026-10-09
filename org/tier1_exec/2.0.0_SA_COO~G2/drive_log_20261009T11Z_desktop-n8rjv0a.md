# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 11Z-12Z (IRPT_YCDGEN round 7: st29 and the F1 re-run)

- 10:56Z CTO half GIVEN for st29 (msg 3183): install only at 0/0, sha re-read at D2, bound 13:09:10Z. GO relayed.
- 11:54Z irpt-generation 0/0. Applier: U2 P1 D2 V1 closed 11:59Z. Root f0ff4f1653-st29; research row firms = 3; svc -> OPAL.
- 12:00Z F1 REQ-5e4149d2863aea31cc87d660: the resident produced the Opal report (render 12:00:32Z, handled 12:00:39Z, 0 YCharts
  markers). irpt-status refuses to serve it: RetentionRefused 'invalid retention reference' (CloudWatch 12:02:18Z), because the
  Lambda's packaged registry research row is [cottonwood]. Row D2-S20 @69ff59f29d.
- CTO msg 3244: FWD-1 grades on a served read of REQ-5e41 by a 49financial-allowed principal, after 2.0.0_SA_COO~Y2's IRPT_ANLREQ
  release 1 (revision 3) stages the row. No new IRPT_YCDGEN cell.
- 12:12:01Z X1 straight to st27, V2 (allow list Andrew only), W2 (svc on cottonwood). st29 COMPLETE @bcfad5755d. st28's ledger was
  CLOSED SUPERSEDED, and its order was ruled superseded @afec47791f.
- Secret reads reported: 12:00:03Z, 12:02:12Z. Host read reported: SSM f02d8b3e.
