# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~1343-1503Z
**Archetype:** TO execution (BE deploy + behavior verify) + portal PROD promote
**Projects:** OPAL_PORTALREFRESH (TO_PORTALREFRESH_BE_01) + P0 formal close + promote v2.1.137

## P0 formal close (delta since 1320Z log)
- Yang uploaded corrected 07-16 data DIRECTLY at 13:42Z (exec 53a06944, bypassing the pre-upload
  gate -- recorded; the DRFR/MDPF_VARFLAG motivating case). validate_data_pkl.py vs 0712 prior =
  PASS all checks (665-row parity, modal span, NAV 112.7854). Served verified data_as_of
  2026-07-16, ST YTD 1.86/vol 3.30. P0 accepted-closed by CTO 144751Z.

## TO_PORTALREFRESH_BE_01 -- deployed data-refresh-v2.3.0, ledger CLOSED (e0079e916)
- F1 seam join per CTO arch ruling (reader-side): rollback resolves SFN pipeline_execution_id from
  DDB executionArn -> describe_execution -> input; reads UUID-keyed outputs-manifest first,
  exec-keyed legacy fallback read, re-processing degraded path; manifestKey logged + returned.
- F2 server-side 409 guard (REJECTED_ALREADY_RUNNING / REJECTED_STATE_UNVERIFIABLE fail-closed).
- F3 non-ASCII cleanup; F4 nested authorizer.lambda.email extraction + Rule-23 docstring swap.
- Chain: 05980fae1 (audited GIT_COMMIT_AUTHOR_OVERRIDE -- AE-lane enumeration gap, grant decision
  routed to COO) -> build-and-upload -> plan (1 change) -> safe-apply -> 0-diff -> record ->
  tag data-refresh-v2.3.0 -> push --follow-tags.
- EXERCISED at the deployed runtime: version-restore fired (manifestKey=archive/53a06944-...,
  99 files, byte-identical target chosen deliberately); concurrent rollback -> 409 w/ contract
  payload; fallback re-process exercised via synthetic row on current-vintage inputs (pipeline
  SUCCEEDED, served re-verified identical, row deleted); F4 proven in runtime log + DDB
  (be01-verify@opalinvest.dev). F4 FORMAL acceptance deferred to first REAL portal action row.
- Contract v1.1 (409 statuses + manifestKey) messaged to DE BEFORE landing; DE ACK 135735Z.

## Portal promote v2.1.137 (after Andrew's hold released via DE-final 144455Z + CTO ruling 144751Z)
- Batch: FE_01 rollback UI 9374414d4 + Emergency Rollback tab (Option A Andrew-approved)
  064658cd2 + passengers 84436ed1/3df9231e. I pushed DEV (DE role-blocked from push).
- PROD f11c15a1 == DEV 064658cd2 (parity empty), tag portal-v2.1.137 peel-verified, CI
  29590054532 SUCCESS, pointer f9695257b, main tree DEV throughout, freeze declared/released at
  COO both windows. Stale 07-15 promote worktree registration removed (physical dir persists,
  Windows long-path class, inert).

## Open / carried
- F4 first real-email history row: report when observed (Andrew's next portal action).
- Annotation question to Andrew: today's dev@test.com rows -- attributedTo annotation, never overwrite.
- COO decision pending: CLOUD_OPS_OR_ETL lane grant for sovereign-delegate DT (SoD-routed).
- MDPF_VARFLAG shadow-build (CTO-registered @6b86d2712); FM-1 arithmetic at Andrew.

## Compiler tools
comp-grep (TF/module/source-map discovery, pipeline_execution_id trace), comp-glob (tf census),
comp-routes origins (CF distribution). comp-iam not needed: no new (action,resource) pairs --
role already held sfn describe/list (exercised paths confirm).
