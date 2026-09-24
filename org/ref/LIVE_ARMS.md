# LIVE ARMS AND HOLDS -- the register

The only source of truth for live scoped loop arms and holds (org/XXX.md Step 1b-F points here). State, not law: it
lives outside the law lock because it changes as arms start and stop (Andrew-direct 2026-09-24 ~17:3xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_173xZ_XXX_MD_GUIDANCE_ONLY_NO_TEMPORAL_ITEMS.md`).
`1.0.0_SA_CTO` lands and strikes rows, naming the chooser and the record. A seat never writes its own row. On DONE the
lane deletes its cron and the row is struck; a struck row's record stays in git. A row absent here arms nothing.

## Holds

- `2.0.0_SA_COO` (base): D2 off until Andrew lifts it.

## Arms

- BLAST MODE (Andrew-direct ~17:4xZ, record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_174xZ_BLAST_MODE_P_M_Y_D_ONLINE_FAST_CLOSER.md`):
  `2.0.0_SA_COO~D` runs `/closer-drive` on DSGN_IRPTV1 under the FAST lease in `org/mcp/drive-mode.log` (surface
  `portal/src/pages/InvestorReporting`); ~P, ~M and ~Y run their goal loops below, each reading its per-seat FAST
  lease `IRPT_BCKEND~<lane>` every tick (C11; same log). The comp-tool rail stays on (call 6 reversed, Andrew ~18:2xZ,
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_182xZ_CALL6_REVERSED_RAIL_STAYS_ON_IN_FAST.md`). Stop: the lease lapses to FULL, or Andrew's stand-down.

- `2.0.0_SA_COO~P` `/loop 20m` DIRECTED over IRPT Performance (49F, INF, COT):
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`; stop = `/verify SOUND`.
- `2.0.0_SA_COO~M` `/loop 20m` DIRECTED over IRPT Holdings with snapshot model overlay:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`; stop = `/verify SOUND`.
- `2.0.0_SA_COO~Y` `/loop 20m` DIRECTED over IRPT Analysis:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`; stop = `/verify SOUND`. Y never takes over P's shared installation.
- `2.0.0_SA_COO~A` `/drive` NFRA_CLDGRPH to CLOSED:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_171xZ_CLDGRPH_HOLDS_OFF_WRAP_IT_UP.md`.
- `2.0.0_SA_COO~X` `/drive` NFRA_C3MATERIALIZE:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260828_050xZ_COOX_DRIVE_LOOP_NFRA_C3MATERIALIZE.md`.
- `1.0.0_SA_CTO` `/self-drive` the fabric (all LAPTOP directives), the CTO adjudicating adjudicable calls on its rec:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_021xZ_SELF_DRIVE_THE_FABRIC_HANDLE_OPEN_CALLS_ON_MY_REC.md`.
  RESERVED to Andrew under every self-drive: vendor/egress off Opal infrastructure; unrecoverable acts; money and
  contracts; every hold he set by name (the portal freeze, the LD-0522 push cadence, the shared-branch push).
- `1.0.0_SA_CTO` `/self-drive D9 IRPT` 30m (IRPT_FNTEND + IRPT_BCKEND + DSGN_REBRND), per the CTO's own record of
  2026-09-11 in its deliverables; ends on `status: complete` or his stand-down.
- `1.0.0_SA_CTO` `/self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON` -- PAUSED by the managed
  wind-down, resume authority:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_193xZ_COO_GOALS_AND_CTO_SELF_DRIVE_ADJUDICATES.md`.
- `1.0.0_SA_CTO` fallback adjudicator for LGIC_LGCTFM's `ANDREW_CARD.md` when Andrew is unavailable (one artifact,
  nothing wider): `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260917_23xxZ_CTO_ADJUDICATES_LGCTFM_ANDREW_CARD_IF_ANDREW_UNAVAILABLE.md`.
- SITE-Z only: `1.0.0_SA_CTO~Z` `/self-drive AMGT_RESAPP & POSN_ASTTAX` 30m (`7,37 * * * *`); `2.0.0_SA_COO~Z`
  `/drive` POSN_ASTTAX 10m and `2.0.0_SA_COO~ZZZ` `/drive` AMGT_RESAPP 10m, each tick an explicit `/canonical-flow`
  stage check (DRIVE FORWARD | PARALLELIZE | NUDGE, a nudge only after the live-production probe reports nothing moving
  across all four planes):
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_222xZ_COO_DRIVE_10M_CANONICAL_FLOW_STAGE_CHECK_AND_REBRAND.md`;
  `3.0.0_SA_CVO~Z` SYSPARITY cron (`org/tier0/ledger/LD-0318.md`, LD-0319); `4.0.0_SA_CRO~W` harvest remediation loop
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260915_HARVEST_REMEDIATION_LOOP_W.md`; the collection
  mechanism and cadence RESERVED to Andrew).

## Struck

- `2.0.0_SA_COO~O` `/canonical-drive NFRA_OPLGTW` 30m DIRECTED (relay 97709; on DONE the slot was to go to `~T`
  MDPF_TAXSMA then `~M` NFRA_MCPINDEX): struck 2026-09-24 by `1.0.0_SA_CTO~O`. The chooser is Andrew: his
  2026-09-22 ~18:2xZ word to that seat, "Finish your work and research on the OPLGTW project and do not go further
  with it", is carried in `2.0.0_SA_COO~O`'s session-close commit @5799432c1c. The lane `~O` is re-seated for
  NFRA_OPALAI on the ~O fabric (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_185xZ_CTO_O_NEW_PROJECT_O_FABRIC.md`),
  and a successor does not re-arm this row. The `~T` and `~M` hand-on clauses are NOT carried: nothing here
  decides them.
- IRPT POST-SLUG HOLD on the old `~B`/`~F` canonical progression (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_1517ET_IRPT_HOLD_AFTER_CVO_SLUGS.md`):
  lifted for IRPT_BCKEND and IRPT_FNTEND closed SUPERSEDED, Andrew-direct 2026-09-24 ~16:4xZ
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_164xZ_IRPT_RETURN_FIVE_CALLS_ANSWERED.md`). The P/M/Y
  seats still read `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{AUTHORITY,CONTRACT}.md` first.
- N1 push hold (`org/tier0/ledger/LD-0613.md` Progress 11): lifted by Andrew-direct ~17:5xZ "Push it"
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_175xZ_PUSH_N1_APPROVED.md`).
