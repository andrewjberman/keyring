# MDPF_SECCLASS -- round 19 L8/L9 adjudication

<sweep_watermark>2026-10-11T02:59Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:59:00Z. L8 packet: 2.0.0_SA_COO~M1 msg 3400, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R19_20261011.md @a8e96112f4. Reads only: orders=0, judgment=0, MAY-CLOSE. Ledger reads re-run on this seat's own session: e84 G PASS, remap-b G PASS, e79 G NOT MET (D1-S26 confirmed at HEAD). e60 arm 2 is closed by the CTO (ADDENDUM 1 @4cac828d3c). 3 rows since the round-18 watermark (D1-S25, D1-S26, D1-S27), all graduated INERT to `remediations/REMEDIATION_v10.md`.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:59:00Z",
    "one_line": "Round 19 L9: no judgment owed; reads only. On this seat's own runs, e84 G PASS (COT: 1,061 positions, $17,324,520.48, moved out of unclassified, all six-class; served mismatch 0 of 31; firm unclassified $65,222,136.02 against the $84,275,714.93 baseline) and remap-b G PASS (4 of 4 Cottonwood clients sum to 1 within 1e-5, 0 multi_asset served, firm_composition gap COT $0.01 / BD $0.00). e79 G NOT MET: the three BD classify sites reach classify_with_identity only for a blank ticker, so the 23 ticker-no-row securities still serve unclassified (BD firm Unclassified $972,621.40 at data_as_of 2026-10-08).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Two of the four ledger reads hold on an independent re-run against served bytes; the third (e79) holds as NOT MET for the reason D1-S26 gives; the fourth (e60 arm 2) rests on the CTO's ruling, which this seat did not re-run. e84's served comparison matches 31 names, not the full 1,061 placed: the served check covers only the names visible on each client's latest concentration date. BD's firm_composition reads data_as_of 2026-10-02 while its total equals the 2026-10-08 firm snapshot; that is by design (D_03 scales the weekly holdings basis to the canonical AUA, D_03.composition_artifacts.py:330-334), so it is not a row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R17_CHECKS/e84_cot_post_fire_read.py 2026-10-09T12:08:32Z (02:5xZ) -> 'E84-G ok=True verdict=PASS partition=2026-10-09.parquet placed=1061 placed_mv=17324520.48 census={cash 880, equity 87, fixed_income 44, commodities 4, alternatives 46} outside_six=[] served_matched=31 served_mismatch=0 firm_unclassified_now=65222136.02 baseline_unclassified_mv=84275714.93'",
        "independent read: s3://opal-data-cot/platinum/firm/mix_summary.json LastModified 2026-10-10T11:57:02Z (after the 2026-10-09T12:08:32Z ship), VersionId jnBMigYkYAqAnzO9spOTj7b3nzIEOawF, data_as_of 2026-10-09, unclassified 65,222,136.02",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R19_CHECKS/remap_b_g_read.py (02:5xZ) -> 'REMAP-B-G ok=True cot_clients=4 cot_sum_ok=4 multi_asset_present=0 comp_gap_cot=0.01 comp_gap_bd=0.00'; client sums 1.000000 x3 and 0.999999 (z09305703), versions modified 2026-10-10 11:53Z",
        "box/dell1 HEAD 1974b85f4e: D_04.client_portal_summary.py:160-167, C_06.client_mix_timeseries.py:228-233 and D_03.composition_artifacts.py:135-140 each call classify_with_identity('', ...) only under 'not ticker.strip()'; comp-find 'classify_with_identity\\(' over data/black_diamond/scripts/gold: 21 hits in 117 files, 3 production callers, 1 definition, 16 tests",
        "s3://opal-data-bd/platinum/firm/mix_summary.json LastModified 2026-10-11T00:45:32Z, VersionId 5Ws3Q6veR.qd3bueY48qALseVpW10kRl, data_as_of 2026-10-08, Unclassified 972,621.40",
        "e60 arm 2: 1.0.0_SA_CTO~DELL1 ruling @4cac828d3c (ADDENDUM 1, arm 2 CLOSED as non-e60 drift); pointer only, not re-run here",
        "round-close-check.py --project MDPF_SECCLASS --round 19 -> orders=0 judgment=0 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  }
]
```
