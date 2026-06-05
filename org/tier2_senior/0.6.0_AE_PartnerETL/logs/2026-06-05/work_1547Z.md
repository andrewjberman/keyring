# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1547Z (GLDINC build-PRD v0.1 build-LEAD review)

**archetype:** REVIEW

## GLDINC PRD v0.1 buildability review (CTO 8c9acb101, I'm build LEAD)
Reviewed docs/architecture/ADHC_GLDINC_PRD.md for build mechanics. PRD sound + faithful to my audit. Roadmap order ENDORSED (P0 checkpoint first, P1 plumbing-proof). RAVC2'd 5 flags to CTO + CC COO+0.4.0:
- FLAG 1 (key dependency): §4 shadow-write needs a CENTRALIZED OUTPUT-PREFIX override in lib.config key helpers, WRITE-SCOPED only (incremental reads real served oracle inputs, only outputs shadow to gold/_parity/). Verify read/write key separation. Whole parity gate rides on this.
- FLAG 2 (substantive — reconcile-parity gap): incremental only touches today's delta, so it WON'T naturally exercise a historical injection-date/rebaseline/reassignment within a forward N-night window. Need a scoped single-date historical parity re-run to prove the reconcile path — ruling needed: is that within the no-ad-hoc gate or an explicit carve-out? Blocks P2/P4/P5 reconcile proof.
- FLAG 3: state-seeding — P2 (A_03 cum-unit store) + P4 (cum-carry, FIFO state) need persisted state PRE-BUILT before parity night 1 (can't compare cold-incremental vs oracle night 1).
- FLAG 4: dual-run parity-window cost — oracle+incremental both each nightly temporarily INCREASES compute (B_01 doubled ~+20min); confirm portal margin; SEQUENCE shadow AFTER oracle for memory-bound A_03/B_01 (else re-creates the 1.38TB-RSS paging stack the DAG serialized B to avoid).
- FLAG 5: checkpoint resume granularity — per-script .done-skip inside run_chain_parallel (finer than group-level --from, which can't express skip-D_00c-run-D_00 in a parallel sub-phase). Buildable; spec per-script-skip in P0.
- MINOR: cost-model data-starved early (2 points); heuristic+judgment until points accrue.
NET: nothing fatal. Flags 1+2 need design answers before P2+; Flags 1/3/4/5 mine to spec as LEAD; Flag 2 needs CTO+0.4.0 ruling. Offered to draft P0 checkpoint spec + shadow-prefix mechanism once Andrew approves PRD.

## Threads (holding)
- demo-reclone3 ~13/min R8-safe progressing. bd-gold R3 validates tonight. GLDINC PRD pending Andrew approval (no prod touch). inf-gold resolved.
