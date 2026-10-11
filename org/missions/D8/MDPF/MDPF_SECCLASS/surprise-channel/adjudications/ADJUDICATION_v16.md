# MDPF_SECCLASS -- round 20 L8/L9 adjudication

<sweep_watermark>2026-10-11T04:22Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T04:22:00Z.

L8 packet: 2.0.0_SA_COO~M1 msg 3469, org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R20_20261011.md @c5f0b3956c.
Three cells (SC-e-87 SERVED; SC-e-88 and SC-e-89 LOCAL), orders=3, judgment=0, MAY-CLOSE. Every criterion of the three orders was
re-run on this seat's own session at box/dell1 HEAD 1977885433, and SC-e-87's 23-security reach was re-run against the LIVE
etf-classifications table with this seat's own script. SC-e-87's leg G (the served read after a scheduled BD fire) is NOT graded here:
the ship is pair-gated at 0.7.0_AE_CloudOps~SC1 and no BD fire has run on the shipped bytes.

Rows dispositioned: 4 new investigation rows (D1-W77-S1, D1-W78-S1, D1-W78-S2, D1-S28) plus this seat's L9 record (D1-C-S2).
Graduated (INERT): D1-S28, D1-W77-S1, D1-W78-S1, with D1-S26 and D1-S27 carried with their round-20 progress. Dismissed below:
D1-W78-S2 (by D1-C-S3) and D1-C-S2. THE SLUG IS HELD: surprise-row-gate refuses every new remediation row while
TO-SC-e87b (the ship, 0.7.0_AE_CloudOps~SC1) is `pending` (LD-0521, Andrew-direct 2026-09-03: the slug waits until every task order
is complete). REMEDIATION_v11 is written and held, byte-ready, at
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R20_SLUG_HELD_REMEDIATION_v11.md`. It moves into `remediations/`, with the one slug
message, when TO-SC-e87b is terminal. Both D1-S26 and D1-S27 stay OPEN.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:22:00Z",
    "one_line": "Round 20 L9: no judgment owed. On this seat's own runs, SC-e-87 fixes D1-S26 in code (all three BD served sites reach the NAME:: fallback for a non-blank ticker-no-row position; 23 of 23 securities, $966,285.46, move on the live table; 0 stay), SC-e-88's issuer amendment of AC1 is sound and states its gate limb, and SC-e-89's three limbs pass. Leg G is not graded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; an issuer amendment states which gate limb graded it.",
    "world_is": "SC-e-87: D_04 :170-176, C_06 :235-238 and D_03 :141-144 each add an `else`/`elif not canonical_class` branch calling classify_with_identity(ticker, name[, cusip]) for a non-blank ticker classify() misses; a ticker WITH a row never reaches it. A fourth caller of classifier.classify, E_25.aua_decomposition_audit.py:192, does not take the fallback, but E_25 is a phase-0 diagnostic that writes gold/manifests/ only, not a served key (the half request counts N=1 writer of platinum/firm/mix_summary.json, D_04 :554). The 23 securities sum to $966,285.46 against round 19's served BD Unclassified of $972,621.40 (data_as_of 2026-10-08), so about $6,335.94 should remain Unclassified after the ship on that basis; leg G should be read against that, not against zero. SC-e-88: AMENDMENT 1 (@287ef0d2ee) is the issuer's amendment of its own criterion, and both the commit and the order state 'Gate limb: none graded this modification'. It is not weaker than the cell's purpose (name the cause of D1-S27): the one reproducing date, 2026-10-08, recomputes to the cent (recomputed_total = served total = 2,014,814,865.45; gap -128.57) and its top residuals, sorted by size, all sit at exactly 1e-6 of their relationship's value, which is 6-decimal share rounding. The two non-reproducing dates are reported as drift (D1-W78-S1), not hidden. The checker's 'reproduces' test reads the worker's own recomputed_total; the original criterion relied on the same field, so the amendment does not weaken it on that axis.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/sc_r20_served_reach.py D_04 | C_06 | D_03 (04:0xZ, HEAD 1977885433) -> 'SERVED-REACH site=<S> ok=True target=('equity', 'equity', 'Name Row', 'etf-classifications') controls=3/3' for all three",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py <the e87 half request> -> 'HALF-READY'",
        "data/black_diamond/scripts/gold: python -m pytest -q tests -> 120 passed (COT gold suite not re-run here: SC-e-87 changes BD files only)",
        "this seat's own live run (scratchpad cvo_r20_live_reach.py: D_04._classify_with_canonical against ETFClassifier() on the live table, read-only) -> 'CVO-LIVE-REACH denominator=23 moved=23 usd=966,285.46 by_class={equity: 20, fixed_income: 3} control_ok=True'; negative control ZZZQX9 / no NAME:: row -> unclassified",
        "comp-find 'classify_with_identity' over data/black_diamond/scripts: 27 hits in 172 files, 3 served sites + lib DEF + tests; comp-find 'classifier\\.classify\\(' : 5 files, the fourth live caller E_25.aua_decomposition_audit.py",
        "python .../R20_CHECKS/c06_gap_record_check.py gap -> 'C06-GAP ok=True dates=1 drift=2 max_abs_err=0.0039 cause_len=1035 basis=rounding'; scope -> 'C06-SCOPE ok=True bad=0'",
        "independent read of s3://opal-data-bd/gold/views/mix_daily_summary.json firm rows: 2026-10-08 total 2,014,814,865.45, gap -128.57 (record recomputed_total 2,014,814,865.45); 2026-10-06 gap -4.71 vs recomputed 167.10; 2026-10-07 gap 128.06 vs recomputed -120.97; eight classes in the firm row",
        "git show 287ef0d2ee: 'Gate limb: none graded it (a modification; no <placeholders> at HEAD; not a newly-added order)'",
        "python .../R20_CHECKS/seatgates_limbs_check.py call|own|slug -> 'LIMB-CALL ok=True unrelated=0 related=1', 'LIMB-OWN ok=True resolved=0.7.0_AE_CloudOps~SC1 own_hits=0 other_hits=1', 'LIMB-SLUG ok=True hits=1'",
        "python .tools/round-close-check.py --project MDPF_SECCLASS --round 20 -> orders=3 judgment=0 graded=0 ungraded=0 self_graded=0 verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:22:00Z",
    "one_line": "D1-W78-S2 (OBSERVATION/INERT) dismissed: True of the residual-sum test alone, but the issuer's AMENDMENT 1 added the discriminating test the row asks for: each listed residual must sit inside |residual| <= total_mv * 4.5e-6. On 2026-10-08 the top five residuals are sorted by size and each is exactly 1e-6 of its relationship's value, so every relationship is inside the bound. Mass outside the eight classes at any relationship would put its residual at that out-of-class share, orders of magnitude above the bound. The served firm row carries exactly the eight classes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-W78-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "True of the residual-sum test alone, but the issuer's AMENDMENT 1 added the discriminating test the row asks for: each listed residual must sit inside |residual| <= total_mv * 4.5e-6. On 2026-10-08 the top five residuals are sorted by size and each is exactly 1e-6 of its relationship's value, so every relationship is inside the bound. Mass outside the eight classes at any relationship would put its residual at that out-of-class share, orders of magnitude above the bound. The served firm row carries exactly the eight classes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e88 AMENDMENT 1 (@287ef0d2ee): 'each listed residual at most total_mv * 4.5e-6, which out-of-class mass would break by orders of magnitude'",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json 2026-10-08 top_residuals (total_mv, residual): (97942124, -97.94), (9535321, 9.54), (9246154, -9.25), (7601183, -7.60), (7245631, 7.25), each |residual|/total_mv = 1.0e-06",
        "s3://opal-data-bd/gold/views/mix_daily_summary.json firm 2026-10-08 keys: alternatives, cash, commodities, equity, fixed_income, other, structured, unclassified, total",
        "investigation row MDPF_SECCLASS-D1-W78-S2 (worker ~78)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "True of the residual-sum test alone, but the issuer's AMENDMENT 1 added the discriminating test the row asks for: each listed residual must sit inside |residual| <= total_mv * 4.5e-6. On 2026-10-08 the top five residuals are sorted by size and each is exactly 1e-6 of its relationship's value, so every relationship is inside the bound. Mass outside the eight classes at any relationship would put its residual at that out-of-class share, orders of magnitude above the bound. The served firm row carries exactly the eight classes."
  }
]
```
