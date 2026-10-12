# MDPF_SECCLASS -- round 23 ADDENDUM 1: the C-S17 disarm read (dell1)

<sweep_watermark>2026-10-12T14:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T14:05:00Z. Addendum: 2.0.0_SA_COO~M1 msg 4365, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R23_ADDENDUM_1_20261012.md @ef7f425cc8
(blob 2a3e7a8198, sha1 8b06afe3f171, verified); CTO half ADDENDUM 2 (msg 4368) @1f036a93b7. Swept by disposition: 5 rows (D1-S32,
D1-W86-S7..S10), all dismissed. C-S17's disarm clock moves in REMEDIATION_v13; nothing else in an earlier file is edited.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S19",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "D1-C-S17 DISARMED on this seat's own reproduction (disarm.state ARMED -> DISARMED in REMEDIATION_v13; the remediation stays OPEN until the first post-ship read). (1) The amended radius reproduces on ALL 15 window dates: the rebuilt firm total equals the served client_performance AUA, and AUA minus the served firm total equals the stated move, within $0.0044. (2) Why this seat's earlier proxy differed: it summed every row of the current canonical partition, while the build's total, like the AUA, counts only gated accounts; it equals the move on 7 dates (09-25..09-27, 10-02..10-04, 10-09) and sits $22.8M-$23.4M above on 8 (09-28..10-01, 10-05..10-08). C-S17's 'up to $270,086,670.20' was the proxy, not the move; the move is +$246,650,838.07 at most (09-28). (3) Both branches: CTO ADDENDUM 2 condition (6) is a per-date STOP-and-rollback (any date whose served total after the act is not equal to the AUA within rounding), which binds the 14 dates where the total moves and the one where it holds (10-09); the advisor branch (502 of 840 advisor-days moving, about $55M of attribution) is STOP-gated by the COO half's condition 10 (each advisor-day within $250 of the committed table, the same 56 keys), and condition (6) itself prints the advisor table without a threshold. (4) The radius is in the pair, not only the packet: the half request's sections Totals and AUA, Added and dropped, Advisors the map drops and Period bars @ef7f425cc8, the COO half addendum 1 (conditions 9-12) and the CTO half ADDENDUM 2 @1f036a93b7 (re-signed, conditions 6-7).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S32"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-C-S17 DISARMED on this seat's own reproduction (disarm.state ARMED -> DISARMED in REMEDIATION_v13; the remediation stays OPEN until the first post-ship read). (1) The amended radius reproduces on ALL 15 window dates: the rebuilt firm total equals the served client_performance AUA, and AUA minus the served firm total equals the stated move, within $0.0044. (2) Why this seat's earlier proxy differed: it summed every row of the current canonical partition, while the build's total, like the AUA, counts only gated accounts; it equals the move on 7 dates (09-25..09-27, 10-02..10-04, 10-09) and sits $22.8M-$23.4M above on 8 (09-28..10-01, 10-05..10-08). C-S17's 'up to $270,086,670.20' was the proxy, not the move; the move is +$246,650,838.07 at most (09-28). (3) Both branches: CTO ADDENDUM 2 condition (6) is a per-date STOP-and-rollback (any date whose served total after the act is not equal to the AUA within rounding), which binds the 14 dates where the total moves and the one where it holds (10-09); the advisor branch (502 of 840 advisor-days moving, about $55M of attribution) is STOP-gated by the COO half's condition 10 (each advisor-day within $250 of the committed table, the same 56 keys), and condition (6) itself prints the advisor table without a threshold. (4) The radius is in the pair, not only the packet: the half request's sections Totals and AUA, Added and dropped, Advisors the map drops and Period bars @ef7f425cc8, the COO half addendum 1 (conditions 9-12) and the CTO half ADDENDUM 2 @1f036a93b7 (re-signed, conditions 6-7).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read s3://opal-data-bd/gold/timeseries/client_performance.parquet VersionId 0Dx5uzxSXleuqe6zrNpwhdLAb4VZnmfK (total_aua summed by date) and gold/views/mix_daily_summary.json VersionId VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD (firm[date].total) against the half request's Totals and AUA table @ef7f425cc8: on all 15 window dates served total, AUA and rebuilt total agree with this seat's reads within $0.0044 (max abs residual), and AUA minus served equals the stated move: +32,079,997.99 / +224,041,973.12 / +223,812,108.95 / +246,650,838.07 / +156,381,570.16 / +149,473,963.54 / +150,330,435.07 / +28,215,020.75 / +5,203.60 / +48,507.12 / -1,825,338.25 / -1,348,850.60 / -1,491,834.79 / -1,933,181.74 / 0.00 (09-25..10-09)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md section 'Totals and AUA' (the 15-row table)",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md ADDENDUM 2 (conditions 6 and 7) @1f036a93b7",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_COO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md :130-131 (condition 10, advisor-days within $250)",
        "investigation row MDPF_SECCLASS-D1-S32 (the issuer's disarm evidence)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-C-S17 DISARMED on this seat's own reproduction (disarm.state ARMED -> DISARMED in REMEDIATION_v13; the remediation stays OPEN until the first post-ship read). (1) The amended radius reproduces on ALL 15 window dates: the rebuilt firm total equals the served client_performance AUA, and AUA minus the served firm total equals the stated move, within $0.0044. (2) Why this seat's earlier proxy differed: it summed every row of the current canonical partition, while the build's total, like the AUA, counts only gated accounts; it equals the move on 7 dates (09-25..09-27, 10-02..10-04, 10-09) and sits $22.8M-$23.4M above on 8 (09-28..10-01, 10-05..10-08). C-S17's 'up to $270,086,670.20' was the proxy, not the move; the move is +$246,650,838.07 at most (09-28). (3) Both branches: CTO ADDENDUM 2 condition (6) is a per-date STOP-and-rollback (any date whose served total after the act is not equal to the AUA within rounding), which binds the 14 dates where the total moves and the one where it holds (10-09); the advisor branch (502 of 840 advisor-days moving, about $55M of attribution) is STOP-gated by the COO half's condition 10 (each advisor-day within $250 of the committed table, the same 56 keys), and condition (6) itself prints the advisor table without a threshold. (4) The radius is in the pair, not only the packet: the half request's sections Totals and AUA, Added and dropped, Advisors the map drops and Period bars @ef7f425cc8, the COO half addendum 1 (conditions 9-12) and the CTO half ADDENDUM 2 @1f036a93b7 (re-signed, conditions 6-7)."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S20",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T14:05:00Z",
    "one_line": "D1-W86-S7, D1-W86-S8, D1-W86-S9 and D1-W86-S10 (INERT) dismissed: S7 (the CVO proxy does not reproduce) is right and is explained in C-S19 (ungated partition sum vs gated build total); S8 (advisor attribution follows the current rel_architect lookup, about $55M moving between advisors) is named in the radius and STOP-gated by COO condition 10, and the CTO's condition (7) tells Andrew of the largest move; S9 (the after figures exclude SC-e-91's retained pass, not measured) is a recorded limit the post-act read covers; S10 ($69.72 between the D_04 rule and the stored key on 10-09) sits inside the $128.58 class-vs-total rounding (W85-S6).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W86-S7",
      "MDPF_SECCLASS-D1-W86-S8",
      "MDPF_SECCLASS-D1-W86-S9",
      "MDPF_SECCLASS-D1-W86-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W86-S7, D1-W86-S8, D1-W86-S9 and D1-W86-S10 (INERT) dismissed: S7 (the CVO proxy does not reproduce) is right and is explained in C-S19 (ungated partition sum vs gated build total); S8 (advisor attribution follows the current rel_architect lookup, about $55M moving between advisors) is named in the radius and STOP-gated by COO condition 10, and the CTO's condition (7) tells Andrew of the largest move; S9 (the after figures exclude SC-e-91's retained pass, not measured) is a recorded limit the post-act read covers; S10 ($69.72 between the D_04 rule and the stored key on 10-09) sits inside the $128.58 class-vs-total rounding (W85-S6).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read s3://opal-data-bd/gold/timeseries/client_performance.parquet VersionId 0Dx5uzxSXleuqe6zrNpwhdLAb4VZnmfK (total_aua summed by date) and gold/views/mix_daily_summary.json VersionId VrrTn2RrESHBImlLOMHQbNP6Fvzi9NZD (firm[date].total) against the half request's Totals and AUA table @ef7f425cc8: on all 15 window dates served total, AUA and rebuilt total agree with this seat's reads within $0.0044 (max abs residual), and AUA minus served equals the stated move: +32,079,997.99 / +224,041,973.12 / +223,812,108.95 / +246,650,838.07 / +156,381,570.16 / +149,473,963.54 / +150,330,435.07 / +28,215,020.75 / +5,203.60 / +48,507.12 / -1,825,338.25 / -1,348,850.60 / -1,491,834.79 / -1,933,181.74 / 0.00 (09-25..10-09)",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md ADDENDUM 2",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_COO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md :130-131",
        "investigation rows as listed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W86-S7, D1-W86-S8, D1-W86-S9 and D1-W86-S10 (INERT) dismissed: S7 (the CVO proxy does not reproduce) is right and is explained in C-S19 (ungated partition sum vs gated build total); S8 (advisor attribution follows the current rel_architect lookup, about $55M moving between advisors) is named in the radius and STOP-gated by COO condition 10, and the CTO's condition (7) tells Andrew of the largest move; S9 (the after figures exclude SC-e-91's retained pass, not measured) is a recorded limit the post-act read covers; S10 ($69.72 between the D_04 rule and the stored key on 10-09) sits inside the $128.58 class-vs-total rounding (W85-S6)."
  }
]
```
