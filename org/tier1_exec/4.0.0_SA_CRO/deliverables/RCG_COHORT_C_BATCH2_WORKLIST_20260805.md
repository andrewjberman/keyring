# RCG cohort-C batch-2+ worklist -- 71 MIGRATE files, derived resolutions + lane routing

**Author:** 4.0.0_SA_CRO. **Authority:** R-0024 (ratified spec + policy). **Population:** the 71
remaining cohort-C MIGRATE files at LABELS.jsonl last-row-wins (81 - 10 closed in B-C001 + the 4
D-C002-restored prompts). Re-derive membership before any batch cut; this list is the worklist,
not the roster.

**THE LANE FINDING THAT SHAPES THIS LIST (B-C001 + B-C002, five gate saves):** most of the
remaining mass is NOT CRO-committable -- `docs/architecture` = ANY_CTO, `docs/deployment` =
BASE_EXEC, `infra/*` = CLOUD_OPS_OR_ETL (any-AE), `org/tier0` = MSTR. Cohort-C execution is
therefore mostly PREPARED-INSTRUCTION handoffs: CRO derives + ratifies + closes labels against
the owning lane's commit. CRO-committable directly: `data/*` (DS-shared? verify per commit),
`org/ref/`, `tools/seeking-alpha-ui` (verify), `docs/briefs` (verify -- untested lane).

## Unit table

| Unit | Files | Resolution (derived) | Executes in |
|---|---|---|---|
| P1 prompts-superseded | infra/prompts/{data_scientist,devops_technician}.md | DELETE (stale 02-24 predecessors of newer org/ref canonicals; diff-verified) | AE lane |
| P2 prompts-sole-copy | infra/prompts/{quantitative_assistant,vba_programmer}.md | git mv -> org/ref/prompts/ (canonical persona home; zero live citations) | AE lane |
| L1 lambda-portal strays | infra/aws/lambda/portal/* (4) | R-0019 cohort MIGRATE; canonical lives in v2_portal/bd-pipeline trees -- per-file target derivation done at batch cut; NOT deploy-coupled (source-map verified this session) | AE lane |
| L2 market_query | infra/aws/lambda/market_query/* (3) | same class as L1 | AE lane |
| L3 test_seeking_alpha_unauth | 5 files | same class; test residue of the retired unauth probe | AE lane |
| L4 news_scanner strays | 3 files | news_scanner canonical consolidated elsewhere (07b2ef9367); derive per file | AE lane |
| L5 secrets README | infra/aws/secrets/README.md | derive at cut (likely docs/deployment consolidation) | AE (file) + BASE_EXEC (target) |
| D1 ADVI PRD family | docs/architecture/ADVI_* (6) + advisor_intelligence/ (3) | completed-project PRDs; candidate homes: docs/architecture/archive/ (the Andrew-precedent pattern @a749324e7b) -- needs CTO word on the archive-dir pattern for docs/ | ANY_CTO |
| D2 YALP/INFLEC/misc PRDs | YALP_* (3), INFLEC_* (2), remaining PRDs (6) + inf_data_graph.yaml | same question as D1 | ANY_CTO |
| D3 briefs | docs/briefs/* (8) + docs/reference/find-insure* (1) | dated one-off briefs; same archive-pattern question | ANY_CTO (verify briefs lane) |
| A1 data/analysis | 8 files | one-off diagnostics; targets: owning seat deliverables/ dirs (the 08-04 root-cleanup precedent: machine outputs move beside their citing docs) | CRO-committable (verify) |
| A2 data/schwab analysis | 6 files | same pattern; schwab silver canon lives in data/canonical/schwab (R-0019 KEEP carve-out) -- these are the pre-canon analysis strays | CRO-committable (verify) |
| A3 seeking-alpha strays | data/seeking-alpha/backfill_ui.py + tools/seeking-alpha-ui README pair (3) | tools/seeking-alpha-ui is the live home; derive whether backfill_ui.py joins it or retires | CRO (verify lane) |
| T0 tier0 pair | org/tier0/{MISSIONS.md, MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md} | MISSIONS.md is LIVE + machine-maintained (comp-missions; durable form org/missions/ per LD-0341) -- the MIGRATE label may be STALE vs the 07-28 missions build; recommend RE-ADJUDICATE at the sitting rather than move | MSTR word first |

## Sequencing

1. **AE bundle (P1+P2+L1-L5, 19 files):** single prepared instruction to the AE lane, riding the
   cohort-A channel; CRO supplies per-file targets at cut time; labels close on the AE commit.
2. **A1-A3 (17 files):** CRO-committable batches next session (lane-verify first commit).
3. **D1-D3 (24 files):** blocked on ONE question to CTO~B -- is `docs/architecture/archive/` (or
   equivalent) the ratified pattern for completed-project PRDs? Then a single prepared handoff.
4. **T0 (2 files):** sitting item -- label likely stale against the 07-28 missions rebuild.

## Sitting additions from this derivation

- T0 re-adjudication (MISSIONS.md label vs the LD-0341 machine-maintained reality).
- The B-C002 gate question: how did ~SWEEP's B-0006 commit pass the CLOUD_OPS_OR_ETL gate that
  denied CRO tonight -- sweep-scoped bypass or coverage gap?
