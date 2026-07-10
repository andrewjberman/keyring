# Deploy Completion Record
**Date opened:** 2026-07-10T20:21:46.474931+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260710T203631Z
**Deploy:** NFRA_COMPLEARN AMD-P3d serving-layer vintage disclosure: derive :latest rebuild (producer) + RunTask -> v2 served comp_learns_status.json with source_vintage (reader agent-local, already live). Zero-widen, CTO~A-gated.
**Authored by:** 0.8.0_AE_CloudComp~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer+reader code on CLOUD (Dockerfile unchanged; reader agent-local) | c1919a60a + 26c25c343 pushed to origin/CLOUD | c1919a60a (producer+reader+deliverable) + 26c25c343 (derives_from labeling) pushed to origin/CLOUD; Dockerfile unchanged (COPYs comp_learns_produce.py already; reader comp_learns_status.py is agent-local via .tools/comp-learns-status, not imaged -> already live, v1-compat) | CLOSED 20260710T202206Z |
| L2 | activation | derive :latest rebuild (globgrph-derive-build) carries updated comp_learns_produce.py (~B single-owner, after B2) | CodeBuild SUCCEEDED + new :latest ECR digest | NOT FIRED / rolled-back (no-op). CTO~A HELD the served write 203512Z: a derive :latest rebuild from CLOUD HEAD would rush-deploy HELD leg-4/freshguard code (_provenance stamp_marker merge+CAS + derive_runner fix, gated on deployed-runtime IfMatch + an UNRUN probe per the leg-4 ledger). ~B caught it pre-fire via the COPY-set-delta gate. Zero rebuild fired, zero image change. P3d live-deploy DEFERRED to ride the leg-4 JOINT rebuild when leg-4 clears. | CLOSED 20260710T203631Z |
| L3 | verify | no-TF 0-diff (existing task-def globgrph-comp-learns-producer:1 + nightly rule pull :latest) | no .tf changed + task-def references :latest | 0-diff: git status shows NO .tf changed by this deploy; existing comp_learns_producer.tf task-def globgrph-comp-learns-producer:1 + rule opal-globgrph-comp-learns-producer-nightly reference :latest (P3, 20260701) -> updated producer rides the existing task-def, no TF apply needed | CLOSED 20260710T202206Z |
| L4 | verify | RunTask globgrph-comp-learns-producer:1 writes v2 served JSON | task exit 0 + SERVED served/comp_learns_status.json schema=v2 source_vintage.overall.status=BEHIND binding=code_heat (verify SERVED not source, F5) | NOT RUN -- deferred with L2. No RunTask, no served-artifact write; served JSON stays v1 (reader agent-local + v1-compatible -> zero regression, CTO-confirmed). The LIVE-served BEHIND disclosure + served-write RAVC2 wait for the leg-4 joint rebuild; a NEW deploy ledger opens at that joint deploy. Nothing landed here. | CLOSED 20260710T203631Z |

## Log

- 20260710T202146Z OPENED by 0.8.0_AE_CloudComp~E with 4 leg(s)
- 20260710T202206Z LEG L1 closed: c1919a60a (producer+reader+deliverable) + 26c25c343 (derives_from labeling) pushed to origin/CLOUD; Dockerfile unchanged
- 20260710T202206Z LEG L3 closed: 0-diff: git status shows NO .tf changed by this deploy; existing comp_learns_producer.tf task-def globgrph-comp-learns-p
- 20260710T203631Z LEG L2 closed: NOT FIRED / rolled-back (no-op). CTO~A HELD the served write 203512Z: a derive :latest rebuild from CLOUD HEAD would rus
- 20260710T203631Z LEG L4 closed: NOT RUN -- deferred with L2. No RunTask, no served-artifact write; served JSON stays v1 (reader agent-local + v1-compati
- 20260710T203631Z CLOSED -- all 4 legs proven
