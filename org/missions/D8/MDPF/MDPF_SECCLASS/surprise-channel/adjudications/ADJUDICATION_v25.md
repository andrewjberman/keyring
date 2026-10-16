# MDPF_SECCLASS -- round 25, L8 compile (dell1)

<sweep_watermark>2026-10-16T03:22:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T03:22:12Z. L8 packet: 2.0.0_SA_COO~M1 msg 6452, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R25_20261016.md @eca46d7714. The round has no judgment criterion.
Rows swept by id-set difference against every adjudication and remediation file: 7 dell1 rows of 108 never named, all dispositioned here
(C-S26 dismisses 6, C-S27 graduates 1). After this file 0 dell1 rows are unnamed, so the watermark moves to now.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S26",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T03:22:12Z",
    "one_line": "ROUND 25 L8: SC-e-102 leg G re-run by this seat and reproduced. Content is equal outside the 10-10..10-13 re-derive window, the served families are in sorted bytes, and D_04's total recompute diff is 0. Six rows dismissed, including W92-S2 (ARMED), disarmed on that read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S16",
      "MDPF_SECCLASS-D1-W91-S1",
      "MDPF_SECCLASS-D1-W92-S1",
      "MDPF_SECCLASS-D1-W92-S2",
      "MDPF_SECCLASS-D1-W92-S3",
      "MDPF_SECCLASS-D1-S40"
    ],
    "spec_asserts": "Spine L8/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; the round has no judgment criterion (round-close-check judgment=0).",
    "world_is": "THIS SEAT RAN org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_legg_read.py read at 2026-10-16T03:1xZ. Firm dates differing: 4 of 2,297, exactly 2026-10-10..10-13, in mix_daily_summary and firm_mix_views_daily. Advisor mix_daily: 56 moved, 7 not canon-equal, all on 10-10..10-13, and sorted bytes now on 56 of 56. Sorted bytes are also now on mix_daily_summary and firm_mix_views_daily (+ alias). restated_through 2026-09-29 pre and post. LEGG-D04: pre total 2024173838.39 and post 2024164661.27, each equal to its same-order recompute (diff 0.000000), with the post key order sorted. Three advisor files (abby_horton, erick_webb, sydney_cobb) carry no new version and are absent from the served summary, as the packet states. W92-S2 (ARMED): the D_03 re-serialised families moved once with content equal outside the window, so the hazard the row named did not occur: disarmed, as D1-S40 states. W92-S3: the last-digit float concern did not occur (D_04 diff 0.000000). W91-S1: the read states its basis for a bar's class dollars, so the choice is recorded. W92-S1: a test-helper name (_load for _load_c06), behaviour equal. D1-S16: dismissed in its own row on the issuer's ruling (msg 1176 @7f8dc1ed54); named here so a CVO row covers it. D1-S40: the issuer's citing row. NOT IN THE CELL'S CLAIM, recorded: the read also prints firm_mix_summary sorted_bytes_now=0 (not sorted); the packet does not claim that family, and its writer is not C_06's _write_mix_summary.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_legg_read.py read (3.0.0_SA_CVO, 2026-10-16T03:1xZ): LEGG-DATES firm n=4 of 2297; advisor not canon-equal=7; LEGG-D04 diff=0.000000 pre and post",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R25_20261016.md @eca46d7714",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is disarmed on this seat's own leg G read, recorded as a stated choice, or ruled by the issuer; none leaves a live hazard."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S27",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T03:22:12Z",
    "one_line": "Graduated to REMEDIATION_v15: W92-S4. E_25 load_mix_summary_latest reads a firm_daily key that no gold writer produces, so its ac2 result is an error for every object C_06 writes. E_25 is registered in no infra chain, so the row is INERT.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W92-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py:130 defines load_mix_summary_latest, which reads summary.get('firm_daily', {}); :382 stores it as results['ac2_aua_by_asset_class']. C_06 writes the key 'firm' (row W92-S4). A search of infra/ for E_25 returns 0 files, and data/black_diamond names it only in the script itself and in a comment in lib/etf_classifier.py, so it runs by hand if at all. An audit that reports an error on every run is a broken instrument, not a served defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py:130, :382",
        "Grep 'E_25' over infra/: no files; over data/black_diamond: 2 files (the script, lib/etf_classifier.py)",
        "investigation row MDPF_SECCLASS-D1-W92-S4"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row in REMEDIATION_v15."
  }
]
```

-- 3.0.0_SA_CVO
