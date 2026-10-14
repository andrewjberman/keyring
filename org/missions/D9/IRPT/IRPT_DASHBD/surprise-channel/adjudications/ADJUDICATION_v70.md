# IRPT_DASHBD: CVO adjudication, round 110 (the Inflection re-render)

<sweep_watermark>2026-10-14T21:20Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T21:20Z, on msg 7856 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND110_B_DRAIN_END_20261014.md`, blob 84a8391b89). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_110_L9_GRADE_20261014.md`): DB110-3-J1 FAIL on one count: three account labels print text fragments ('4INT', 'tion') as 'Account ending'. Round 109's four counts are fixed; the account since-inception benchmarks were recomputed by this seat from the served series and match. 22 rows dismissed below, 2 ARMED among them. Held: D2-W173-S9 (ARMED) and D2-W175-S10 (the labels), D2-S37 (BLOCKING), D2-W178-S2 and -S3 (Cottonwood: performance gold 12 trading days behind with no schedule; holdings end 2026-10-08, cause not established), D2-W178-S1 (ARMED, the CTO's), D2-W177-S4 (the Black Diamond weekend and holiday partitions fit no single basis). No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S7",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T21:20:00Z",
  "one_line": "Round 110. L9: DB110-3-J1 FAIL on the account labels only ('Account ending 4INT', 'tion (1 of 2)', 'tion (2 of 2)'); all four round-109 counts fixed (own since-inception benchmarks recomputed here from the served series VersionId 9wcMYjBb...: 0.1 / -2.3 / -0.4 / 0.6, equal to the render; gain/loss Ending Value matches the overview; not-spanned words; one true reason). DB110-1,2,3,5,6-AC1 PASS on HEAD; DB110-4-AC1..3 read the portal worktree (PASS in the worker's tree, FAIL on main's checkout, as the packet states). Dismissed (22): D2-W175-S1, -S2, -S3, -S5, -S6, -S7, -S8, -S9, -S11 (BLOCKING; each ruled and amended by the issuer in D2-S38, D2-S40..S43, with the amended criteria passing), D2-W175-S4 (ARMED; disarmed by its owner in D2-S40), D2-W173-S2 (ARMED; account first-data dates now come from positions, seen on pp.11-14), D2-W176-S1 (BLOCKING; one golden re-pinned inside the grant, D2-S39), D2-W177-S1 (BLOCKING; no independent close series, answered by the bond-ETF offset read, D2-S39), D2-W177-S2, -S3 (write days and worktree content, read), D2-W178-S4 (calendar fallback on this box), D2-S38, D2-S39, D2-S40, D2-S41, D2-S42, D2-S43 (the issuer's ruling records).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W175-S1", "IRPT_DASHBD-D2-W175-S2", "IRPT_DASHBD-D2-W175-S3", "IRPT_DASHBD-D2-W175-S5",
   "IRPT_DASHBD-D2-W175-S6", "IRPT_DASHBD-D2-W175-S7", "IRPT_DASHBD-D2-W175-S8", "IRPT_DASHBD-D2-W175-S9",
   "IRPT_DASHBD-D2-W175-S11", "IRPT_DASHBD-D2-W175-S4", "IRPT_DASHBD-D2-W173-S2", "IRPT_DASHBD-D2-W176-S1",
   "IRPT_DASHBD-D2-W177-S1", "IRPT_DASHBD-D2-W177-S2", "IRPT_DASHBD-D2-W177-S3", "IRPT_DASHBD-D2-W178-S4",
   "IRPT_DASHBD-D2-S38", "IRPT_DASHBD-D2-S39", "IRPT_DASHBD-D2-S40", "IRPT_DASHBD-D2-S41", "IRPT_DASHBD-D2-S42", "IRPT_DASHBD-D2-S43"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded; every BLOCKING or ARMED row is dispositioned on grounded evidence before the slug.",
  "world_is": "All six round-110 orders complete; merges on origin box/dell2; nothing served or written to AWS. The Inflection household renders with its own windows and true reasons. Labels for custodian numbers with no digit run still print text fragments. The as-of fix waits on Andrew's approval row; Cottonwood stays blocked on its silver and on a producer schedule.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of 20 of 20 pages, fwd21_sample_r110/pages/final/ (private; no client figure copied)",
    "this seat's recompute 2026-10-14T21:1xZ: model_series_windows.windows_from_series on s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json VersionId 9wcMYjBbgI9jMxGANcPBhPIAKBRQMcZt, as_of 2026-10-13, first day 2026-06-16",
    "this seat's re-run on HEAD: DB110-1/2/3/5/6-AC1 PASS; DB110-4-AC1..3 FAIL on main's portal checkout",
    "investigation rows D2-W173-S2, D2-W175-S1..S11, D2-W176-S1, D2-W177-S1..S4, D2-W178-S1..S4, D2-S37..S43",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_110_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "BLOCKING rows ruled and amended by the issuer with the amended criteria passing, two ARMED rows disarmed by their owner or fixed on the page, readings, and the ruling records. The label count, Cottonwood's blockers, the CTO's ARMED row and the BD date fact are held."
 }
]
```
