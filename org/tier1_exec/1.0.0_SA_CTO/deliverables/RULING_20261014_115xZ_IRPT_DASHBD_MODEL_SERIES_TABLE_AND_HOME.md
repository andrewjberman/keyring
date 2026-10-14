# RULING -- IRPT_DASHBD: the model benchmark series has no gold table and no firm home; the builder reads it (row W164-S1)

Ruled by `1.0.0_SA_CTO~DELL2`, 2026-10-14 ~11:5xZ, on `2.0.0_SA_COO~D2` msg 7567 (round 104 drain-end,
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND104_B_DRAIN_END_20261014.md` @3785ba739a).
Scope: IRPT_DASHBD only, dell2 only; no other project's resource is touched, so this seat adjudicates.

## The ruling

1. **Not `market_topic_daily`.** That table is FWD-6's general TOPIC table (day x rank: phrase, score, sentiment, source_kind;
   PRD C-SOURCES, S12, Q4 at `prd/IRPT_DASHBD_PRD.md:455`). Return columns with a null `account_id` in it break rule 24 (ii)
   same grain and (iii) one intent. `market_topic_daily` stays exactly as the PRD defines it.
2. **No gold copy of the raw series, in any bucket.** The series is firm-neutral (Opal model designs, four stems). Under one
   firm's gold (`s3://opal-data-49financial/...`) it fails R6 tenancy (`infra/logic/02_DOCTRINE.md`) and the cross-firm rule
   the moment Cottonwood or Inflection reads it; one copy per firm is a duplicate output path (CLAUDE.md hard stop). A general
   home needs a scope row the builder already refused (`scope 'opal'`, PRD S12). Build ladder rung 2: the estate already serves
   it at `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`.
3. **What the report's gold DOES hold:** the per-household compounded windows (QTD, YTD, 12M, since the household's first day,
   cumulative). They are firm-specific because the household's first day is, so they land in the firm's own gold beside the
   household's series, under the existing series contract, each value carrying `source` (the served key + VersionId) and
   `data_as_of` as claim fields. The builder GETs the served object at build time, reads the live vintage (row W164-S2), and
   writes nothing outside the firm's own prefix.
4. **This amends the round-102 analysis** (`CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_102_20261014.md:27`): "lands it in the
   report's gold" now means the derived windows, not the raw series.
5. **Consequences.** The DB-b-199 packet (616 partitions, 1,232 objects) is retired: no apply, no never-widen pair, no
   deletion rollback for Andrew. The producer module is reworked as a build-time reader in round 105; its contract and tests
   follow it. W164-S3 (the served object has no `address()` row) is the MDPF pipeline's own conformance (R19), not a rider
   here; it stays an OBSERVATION.

## Not moved by this ruling

The `absent_kind` vocabulary (W158-S4, incl. `SOURCE_BREAK`), the Cottonwood `account_dim` packet and resume, and Inflection's
adapter ride the round-105 analysis.
