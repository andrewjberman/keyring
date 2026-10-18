# MDPF_SECCLASS -- round 28 L8 (dell1)

<sweep_watermark>2026-10-18T01:53:27Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T01:53:27Z, on 2.0.0_SA_COO~M1 msg 7827 (org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R28_20261018.md @363dbc9e5d). Swept: 11 dell1 rows never named (9 dismissed, 2 graduated). REMEDIATION_v17 S48 and S45 are advanced in place in the same commit. The watermark moves to now.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S33",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T01:53:27Z",
    "one_line": "ROUND 28 L8: MAY-CLOSE (22 orders, judgment 0). S48's cause is named, and this seat's own served measure of 2026-10-02 (+407,720 on the total, ADJUDICATION_v27) equals the issuer's checker on the changed inputs (+407,720.32), so S48 closes, disarmed. S45 closes on the corrected leg G re-read. The newest served version (00:24Z, after the 23:00Z fire) moved only 8 dates, by -306 to -2,449, and added no date. S42 stays ARMED. 9 rows dismissed; W100-S3 and S52 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S49",
      "MDPF_SECCLASS-D1-S50",
      "MDPF_SECCLASS-D1-S51",
      "MDPF_SECCLASS-D1-W99-S1",
      "MDPF_SECCLASS-D1-W99-S2",
      "MDPF_SECCLASS-D1-W100-S1",
      "MDPF_SECCLASS-D1-W100-S2",
      "MDPF_SECCLASS-D1-W100-S4",
      "MDPF_SECCLASS-D1-W100-S5"
    ],
    "spec_asserts": "REMEDIATION_v17 S48: close when the cause is read and recorded, and this seat re-reads one restated date against its stated cause. S45: SEED22-LEGG ok=True or a ruling names the cause. Spine L8/L10.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~01:5xZ. S48: the packet names the cause. B_00 (gold_dispatch.sh:99, --force-recent-days 14 on every fire) re-derived 14 dates from three changed inputs (the A_03 positions cube, the canonical prices, the A_00 accounts dimension), upstream of which the 49F bronze run at 00:02-00:08Z landed realized lots that restore two open accounts. The after-the-fact never-widen pair is signed by the CTO (msg 7442). This seat's own diff at ADJUDICATION_v27 C-S30 read 2026-10-02's served total rising +407,720 between 87CvfcFp and l2Wqoi6i. The issuer's checker recomputes sum(market_value) on the changed canonical inputs for that date as +407,720.32. One restated date agrees with its stated cause to the dollar, so S48's clocks are advanced in place (DISARMED, REMEDIATED, closed). The packet's carried note stands: the per-date ranges of the two measures (canonical +382,473 to +450,743; served about +381k to +419k) are not reconciled across all 14 dates. S45: the leg G expectation was computed on the wrong table (gold/holdings_lots); the corrected re-read, seed_legg_reread_lcfyx.py, prints ok=True dates=15 bad=0 tol=5 (row S50). That is the 'ruling names the cause' branch, met, so S45 is advanced in place. NEWEST SERVED VERSION: mix_daily_summary.json 0IrqqSvy (2026-10-18T00:24:42Z) against l2Wqoi6i (2026-10-17T05:24:08Z) has restated_through 2026-10-01 unchanged, 2,299 dates in both, 0 added (the last date is still 2026-10-15), and 8 dates changed (2026-10-08 to 10-15) with totals -306, -612, -918 ... -2,449. That is a steady -306 a day, small and inside the 14-day window, so the 23:00Z fire did not widen the restatement. Why no 2026-10-16 row landed is not read. S42 stays ARMED: the 23:00Z fire's E_18 stdout line is not read (the issuer holds '0 candidates' from the single run only). DISMISSED: S49, S50 and S51 (the cause reads and the disarm record). W99-S1 and W99-S2 (premise magnitude and the Cottonwood lead, both answered). W100-S1, W100-S2, W100-S4 and W100-S5 (the leg G instrument findings that produced S50).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v27.md row MDPF_SECCLASS-D1-C-S30 (this seat's served diff, 2026-10-02 +407,720)",
        "aws s3api list-object-versions and get-object --version-id 0IrqqSvy... of mix_daily_summary.json; diff against l2Wqoi6i (this seat)",
        "python .tools/round-close-check.py --project MDPF_SECCLASS --round 28 -> MAY-CLOSE",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R28_20261018.md @363dbc9e5d"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Cause reads, the disarm record and instrument findings, each answered within the round."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S34",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T01:53:27Z",
    "one_line": "Graduated to REMEDIATION_v18 (2). W100-S3: a NAME:: row classes LORD ABBETT CONVERTIBLE I as cash against the ruled fixed_income for LCFYX. S52: E_18 skips the nine held-out names because an April ticker_resolution table marks them resolved, so they stay invisible to it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W100-S3",
      "MDPF_SECCLASS-D1-S52"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "Both are named in the packet's 'What the round established'. The table is gold/dimensions/ticker_resolution.parquet: one version 2026-04-07T21:54:55Z, writer classification/resolve_tickers.py.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_SECCLASS-D1-W100-S3, MDPF_SECCLASS-D1-S52",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R28_20261018.md @363dbc9e5d"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v18."
  }
]
```

-- 3.0.0_SA_CVO
