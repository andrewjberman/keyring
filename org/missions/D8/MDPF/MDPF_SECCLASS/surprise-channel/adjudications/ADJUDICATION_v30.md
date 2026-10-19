# MDPF_SECCLASS -- round 29 L8 (dell1)

<sweep_watermark>2026-10-19T14:52:17Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-19T14:52:17Z, on 2.0.0_SA_COO~M1 msg 8310 (org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R29_20261019.md @26ee88136c (sha256 0792686bc0186fc1...)). Swept: 7 dell1 rows never named, 4 dismissed and 3 graduated (1 ARMED). REMEDIATION_v17 D1-S42 is disarmed in place (remediation OPEN), and REMEDIATION_v19 carries its disarm row C-S37. The watermark moves to now.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S35",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-19T14:52:17Z",
    "one_line": "ROUND 29 L8: MAY-CLOSE (26 orders, judgment 0). This seat read E_18's own output in two scheduled chain logs. The 2026-10-17 23:00Z fire shows 0 candidates, 9 already resolved, 0/0 written or refused. The 2026-10-19 04:03Z fire, after the TO-SC-e116b ship, prints 'Held out by the resolution table ...: 14' with all 14 tickers named. The held-out names are no longer a silent miss, so D1-S42 is DISARMED (disarm row C-S37); its remediation stays OPEN, because the 14 remain unclassified (S55). 4 rows dismissed; W104-S2, S53 and S55 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W104-S1",
      "MDPF_SECCLASS-D1-W102-S1",
      "MDPF_SECCLASS-D1-W102-S2",
      "MDPF_SECCLASS-D1-S54"
    ],
    "spec_asserts": "REMEDIATION_v17 D1-S42 (ARMED): E_18 was blind to old-list-only tickers; close when E_18's own output reads 0 old-list-only tickers after the ship. The CTO's round-28 analysis (msg 7829): the E_18 first-fire read, and the held-out display on scheduled fires.",
    "world_is": "READ BY THIS SEAT 2026-10-19 ~14:5xZ. Packet hash verified. s3://opal-data-bd/gold/logs/chain_full_20261017_230043.log (E_18 at 2026-10-18T00:05:03Z, lines 3594-3607): holdings gold/holdings_lots/2026-10-09.parquet, resolution table 4424 names, tickerless 1,316, already resolved 9, candidates 0, written/refused 0/0, truly unresolved 72. s3://opal-data-bd/gold/logs/chain_full_20261019_040119.log (E_18 at 2026-10-19T05:07:28Z, lines 4819-4847): holdings gold/holdings_lots/2026-10-16.parquet, tickerless 1,511, already resolved 14, 'Held out by the resolution table (real ticker absent from the canonical table): 14', listing BALCX, CIMAX, DODBX, FPE, FSNQX, HBLFX, JBAWX, KAMIX, PCEF, TRRJX, TRRNX, VTTVX, WTM, XPMIX, then candidates 0, written/refused 0/0, truly unresolved 108. S42's hazard was silence (held-out tickers never shown). Every scheduled fire since the ship now prints them by name, so the hazard is disarmed at the 05:07:28Z fire this seat read. The close condition (0 old-list-only tickers in E_18's output) is not what the output prints, and the 14 are still held out of classification. So the remediation stays OPEN, with the table-gating question carried by S55. The issuer reports etf-classifications at 11,375 items (paginated count) at 14:34Z, unchanged; not re-read here. DISMISSED: W104-S1 (the partners-data source path). W102-S1 and W102-S2 (the dispatcher order and the weekly lots writer, both premise corrections). S54 (the 2026-10-16 row is absent from the 00:24Z served version because A_03's window ends at the newest silver transactions date, and the 2026-10-16 trades land after the 23:00Z fire; schedule order, not a code fault, and it appears from the next 04:00Z fire).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-bd/gold/logs/chain_full_20261017_230043.log (E_18 at 2026-10-18T00:05:03Z, lines 3594-3607) (read by this seat)",
        "s3://opal-data-bd/gold/logs/chain_full_20261019_040119.log (E_18 at 2026-10-19T05:07:28Z, lines 4819-4847) (read by this seat)",
        "python .tools/round-close-check.py --project MDPF_SECCLASS --round 29 -> MAY-CLOSE (issuer)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R29_20261019.md @26ee88136c (sha256 0792686bc0186fc1...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Premise corrections, a source-path fact and a schedule-order absence."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S36",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-19T14:52:17Z",
    "one_line": "Graduated to REMEDIATION_v19 (3): W104-S2 (ARMED: the partners-data classifier returns the table's asset_class verbatim, a wider set than the pre-read said; inlined in the round-30 repoint cell, which waits on Andrew for its client-facing apply), S53 (the served TOTAL rises about $32k less than canonical holdings on Monday to Thursday dates and equally on Friday to Sunday, cause not read), and S55 (14 real tickers held out by the April name-to-ticker table and never candidates).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W104-S2",
      "MDPF_SECCLASS-D1-S53",
      "MDPF_SECCLASS-D1-S55"
    ],
    "spec_asserts": "Spine L10: every ARMED row is dispositioned before the slug; an item that bears on a later act graduates with an owner and a close condition.",
    "world_is": "See C-S35 and the packet section 'Owed at the round-30 cut'. S53's residue is between -31,616.79 and -32,192.93 on 10-01, 10-05 to 10-08 and 10-12 to 10-14, and 0.00 on 10-02 to 10-04 and 10-09 to 10-11.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_SECCLASS-D1-W104-S2, MDPF_SECCLASS-D1-S53, MDPF_SECCLASS-D1-S55",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R29_20261019.md @26ee88136c (sha256 0792686bc0186fc1...)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows W104-S2, S53 and S55 in REMEDIATION_v19; disarm row C-S37 for D1-S42."
  }
]
```

-- 3.0.0_SA_CVO
