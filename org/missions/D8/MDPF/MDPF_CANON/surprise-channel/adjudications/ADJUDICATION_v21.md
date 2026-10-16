# MDPF_CANON -- round 11 L9 (INTERIM): CN-s-3 AC2 re-graded at portal 7a88ca75 (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T15:28:24Z. Asked by 2.0.0_SA_COO~D1 msg 6783 (org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/REAL_RUN_ADDENDUM_C-S95_20261016.md @1eebd75fed), answering C-S95. Two rows; no rows swept, so the watermark does not move.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S97",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T15:28:24Z",
    "one_line": "ROUND 11 L9 RE-GRADE: JUDGMENT MDPF_CANON.TO-CN-s-3 AC2 MET at portal 7a88ca75 (after AMENDMENT 1), read by this seat on the issuer's re-render. The Monthly view draws the Aug 31 bar, marked carried, and its tooltip marks all seven rows '(carried)'; the rows sum to the $476M Total. This verdict replaces C-S95's NOT MET.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-s-3 AC2 (judgment): the Cottonwood Trend rendered at a STATED portal commit; look at the window start, the Other AUM band, the interpolated and carried marking and the Aug 31 bar. C-S95 asked for the Monthly view and one carried-date tooltip.",
    "world_is": "MDPF_CANON.TO-CN-s-3 AC2 MET. READ BY THIS SEAT with the Read tool, outside the repository at C:/dev/_real_run/MDPF_CANON_r11/ (sha256 re-computed by this seat, below). cn_s_3_cottonwood_monthly_view_before_amendment1.png (candidate at 978da061) shows five bars: Jun 30, Jul 31, Aug 31, Sep 30, Oct 15. The Aug 31 bar draws its full stack at reduced opacity; at the base that bar drew nothing. cn_s_3_cottonwood_monthly_aug31_tooltip_after_amendment1.png (candidate DEV 39dab87f3b + 1e39adc9 + 978da061 + 7a88ca75) shows the tooltip 'August 31, 2026, Total AUM $476M'. Its rows: Custom Models (carried) $15M, Ultra Short-Term (carried) $18.5M, Short-Term (carried) $18.4M, Intermediate-Term (carried) $80.3M, Long-Term (carried) $59.5M, Ultra Long-Term (carried) $1.07M, Other AUA (carried) $284M. The seven rows sum to $476.8M against the $476M Total (rounding), and equal the addendum's CRO month-end oracle row. The earlier limbs stand from C-S95: window start 2026-06-09, Other AUM from the first date, and the interpolated band. Through the first tooltip (2 of 7 rows marked), the issuer's re-render found a real defect and reopened and repaired the cell; this grade is of the repaired commit. LIMITS: a build-and-fixture render (ui-smoke from dist with the served 2026-10-15 object), not dev:live. One carried date's tooltip was read; the other 11 carried dates rest on AC1 arm P4 (7 of 7 at the repair).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/dev/_real_run/MDPF_CANON_r11/cn_s_3_cottonwood_monthly_view_before_amendment1.png sha256 ffe9e425fc3b0cfde3c88a5ff385f77bf65ae0760d07baef038575e2034d91eb",
        "C:/dev/_real_run/MDPF_CANON_r11/cn_s_3_cottonwood_monthly_aug31_tooltip_after_amendment1.png sha256 bc582ca008d96c598208f922090b4cfacd9861d7023ad35aca6daa63ed92c17d",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/REAL_RUN_ADDENDUM_C-S95_20261016.md @1eebd75fed",
        "ADJUDICATION_v20.md row MDPF_CANON-D1-C-S95"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CN-s-3 AC2 MET at 7a88ca75; replaces C-S95's NOT MET."
  },
  {
    "id": "MDPF_CANON-D1-C-S98",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T15:28:24Z",
    "one_line": "Three INERT findings from the CN-s-3 re-render, for the CTO's round-11 analysis. (1) The addendum's hash table swaps two files' sha256 values. (2) On the AUM-labelled Cottonwood page the tooltip says 'Other AUA', a label already on DEV. (3) The Jul 31 bar carries the interpolated outline though 07-31 is measured, because a month holding estimated days is marked whole.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A record that names files by sha256 names the right file; a firm page uses one asset label; a bar's marking is the marking of the value it draws.",
    "world_is": "(1) This seat's sha256 at C:/dev/_real_run/MDPF_CANON_r11/: monthly_view_before = ffe9e425..., aug31_tooltip_before = 24717187...; the addendum's table gives these two the other way round. The after-amendment hash bc582ca0... matches. (2) cn_s_3_cottonwood_monthly_aug31_tooltip_after_amendment1.png reads 'Total AUM' and 'Other AUA (carried)', while the legend reads 'Other AUM'. 'Other AUA' is the fixed label in ModelPortfolios.tsx (line 183 'non_model' -> 'Other AUA' and the Andrew-direct ~01:1xZ comment at L1543) at DEV 39dab87f3b, before this round; it is not CN-s-3's change. (3) In both Monthly PNGs the Jul 31 bar is outlined in the interpolated dash. The served composed_backfill.first_measured_date is 2026-07-20, and 07-31 is not in channel_participation.exceptions. The page's interpolated set marks a period when any plotted point in it is interpolated_estimate (ModelPortfolios.tsx ~L1150 at 7a88ca75), so July is marked for 07-01..07-19. That is the page's existing rule, not this cell's. W31-S1 (Global carried-key labels, from code, not rendered) is not placed here: graduating it needs a remediation row, and that is refused while CN-s-1 is open. It is placed at the FINAL packet's sweep.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sha256sum over C:/dev/_real_run/MDPF_CANON_r11/ (3 files) by this seat",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/REAL_RUN_ADDENDUM_C-S95_20261016.md @1eebd75fed (hash table)",
        "git -C portal show 39dab87f3b:src/pages/ModelPortfolios.tsx line 183 and 7a88ca75 lines 184, 1145-1158",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/ref/served_cottonwood_aggregate_20261015.json meta.composed_backfill.first_measured_date"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record slips and pre-existing page rules, each named for the CTO; none blocks the grade."
  }
]
```

-- 3.0.0_SA_CVO
