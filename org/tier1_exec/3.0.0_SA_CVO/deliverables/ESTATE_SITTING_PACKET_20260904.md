# ESTATE SITTING PACKET — 26 PENDING DAYS IN ONE SITTING (2026-08-08 .. 2026-09-03)

**Authority:** Andrew-direct at the 3.0.0_SA_CVO terminal 2026-09-04 ~05:0xZ, VERBATIM **"a for both"**
(record @92af61a111): card 2's option (a) — *adjudicate the 26 PENDING estate-report days in one
sitting now, oldest first.* The loop's operator is 3.0.0_SA_CVO (semantic-evolution RULING 3).
**Prepared by:** 3.0.0_SA_CVO, 2026-09-04 ~05:5xZ. **Ruling:** pending — Andrew rules per row below
(adopt / amend / reject) or by block; nothing lands before the word.

## How the 26 days reduce to 64 rows

| Quantity | Count |
|---|---|
| PENDING days (manifest status PENDING, oldest 08-08, newest 09-03; 08-07 is AI-ABSENT by producer note, 08-06 proposes nothing) | 26 |
| Proposals across those days (the producer re-proposes the same (entity, field) every day it re-flags it) | 237 |
| Distinct (entity, field) pairs | 64 |
| Pairs already RATIFIED on 2026-08-20 (record org/estate-reports/2026-08-20.md) — every later or earlier occurrence is mechanically *already ratified / superseded by the ratified text* | 7 |
| NEW pairs needing a ruling | **57** |
| of which carrying at least one MEASURED occurrence | 37 |
| of which INFERRED- or UNMEASURED-only on every occurrence | 20 |

A ruling on a pair rules every day that carries it. Each day then lands as its own record
(`org/estate-reports/YYYY-MM-DD.md` + S3 adjudicated copy + manifest flip LAST), citing this packet
and the ruling.

**Landing homes, per the 08-20 finding (unchanged unless the CTO's field-home act has landed; verified at
landing):** a `description` adoption lands on the entity's row in
`org/modules/graph/estate-coverage-manifest.yaml` (regen-durable, manifest wins). A `classification`,
`classification_reason` or `enrichment` adoption has no canonical field and lands in the day record
only — exactly as #2, #3, #5, #6 did on 08-20.

**Rule-24 discipline applied to every ADOPT:** the producer's coined enum-shaped tokens
(`DEPRECATED-LEGACY`, `DELETE-GATED`, `CONDEMNED - DISSOLUTION ORDERED`, `DRIFT-SUSPECT / ...`) are
respelled into descriptive prose so no vocabulary value is minted; time-bound clauses ("13 days stale
at window open", "~18 days stale", "as of scan time") are dropped because they are true for one day
and false for every day after; sentences about the producer's own instrument ("the stratum counted 0
co-change pairs") are dropped because they describe the report, not the entity. The SUBSTANCE of each
adopted proposal is otherwise unchanged. Where a respell changes more than shape it is marked AMEND.

---

## BLOCK A — RECOMMEND ADOPT (25 rows; text below is the text that lands)

### A1. PPI-12-opal-session-analytics / classification (20 days, 08-11..09-03) — ADOPT, record-only
Decommission ordered. The 2026-07-30 ruling orders complete decommission of the opal-sessions system
(the opal-sessions DynamoDB table, the opal-session-analytics lambda, the four /analytics/* API routes
and the portal ingest calls); permanent deletion is staged as Q-23. PPI-12 is not a live analytics
component; it remains in the estate only as a deletion-pending artifact until Q-23 executes.

### A2. PPI-12-opal-session-analytics / description (5 days) — ADOPT, manifest row
Opal session analytics system: the opal-sessions DynamoDB table, the opal-session-analytics lambda,
four /analytics/* API routes and the portal-side ingest calls that carried session telemetry. Ordered
decommissioned completely by sovereign ruling 2026-07-30, with the destructive teardown staged under
Q-23; every part named is in scope for removal. Prose describing it as a live, connected system is
superseded.

### A3. PPI-12-opal-session-analytics / classification_reason (1 day) — ADOPT, record-only
Decommission-directed but not verified removed: the 2026-07-30 ruling names the table, lambda, four
routes and portal ingest calls as one connected system to decommission completely; the table delete
was denied at the permission layer and the destructive action was restaged as Q-23 with GO pending.

### A4. find-insure-casefind-pipeline / classification (8 days) — ADOPT, record-only
Parked project, dormant. One of the find-insure-* lambda quartet operating against s3://opal-data-imo
(business-development prospecting of insurance-sales firms as prospective asset-management clients).
Ruled KEEP as a parked project at the 2026-07-30 sovereign review: retained in place, not deleted, not
running as an active production pipeline. Any classification calling it an active production
workload is superseded.

### A5. cot-pipeline / description (7 days) — ADOPT (AMEND: migration status clause dropped), manifest row
Cottonwood partner-data pipeline whose historical landing zone is s3://opal-data-cot. That bucket is
not the terminal design: the 2026-07-30 PARTNER-DATA TARGET ARCHITECTURE ruling makes
opal-data-assets the canonical and singular source of truth for all partner data, with the bd, inf
and cot buckets migrating into its /bronze -> /silver -> /gold medallion. Until the migration lands,
opal-data-cot is a Cottonwood partner-data bucket in migrate-into-assets state.

### A6. PPI-13-schwab-anonymizer / classification (7 days) — ADOPT (respell of `DEPRECATED-LEGACY`), record-only
Deprecated legacy path, off the main partner-data chain, retirement gated. PPI-13 is the legacy
Schwab anonymization path feeding s3://opal-data-schwab, a bucket ruled should-not-exist-anymore; the
live Schwab path lands under assets/schwab/ inside opal-data-assets. Retirement is gated, not
executed: the open gate is an autoschwab-EC2 connection check plus a live-writer census.
Classification as the live or main-chain Schwab route is drift and must not be reasserted.

### A7. PPI-13-schwab-anonymizer / classification_reason (1 day) — ADOPT, record-only
Two sovereign anchors: the 2026-07-30T17:5xZ Andrew-direct deprecating 49F Converter ops (the schwab
chain this anonymizer serves), and the 2026-07-30T19:4xZ s3://opal-data-schwab note (bucket
should-not-exist-anymore; assets/schwab/ supersedes it under the partner-data target architecture;
gate = autoschwab-EC2 connection check plus live-writer census).

### A8. TS-5-parquet-batch-export / description (6 days) — ADOPT, manifest row
Parquet batch-export leg historically recorded under the trade-submission product. Characterized at
the 2026-07-30 sovereign session as the deprecated-looking parquet batch-export leg and placed under
REVIEW; it is not an active component of the kept, live trade-submission product (opal-trade-submissions
plus trade-security-identifiers), which must not be swept by name association. The trade-users proto
of the same product was ruled TEARDOWN on 2026-07-30 because of its coupling to this leg (Q-7).

### A9. TS-5-parquet-batch-export / classification_reason (3 days) — ADOPT, record-only
Carried as a deprecated-looking export path under open sovereign review, not an active export leg:
the 2026-07-30 ruling on s3://opal-data-trade-submissions kept the bucket (it backs the portal Trade
Submission page) and expressly ordered REVIEW of the parquet batch-export leg; the trade-users
teardown ruling is coupled to the same Q-7 leg. tests/trade_pipeline is cold (>= 90 days).

### A10. MA-06-market-update-authoring-toolchain / description (5 days) — ADOPT, manifest row
Toolchain for authoring market-update content. Its persistence layer is unresolved: s3://opal-market-update
has been associated with this entity by naming inference only, and that bucket is delete-gated ("very
likely delete") pending a consumer trace of the live fred daily flow; the true owner of that bucket and
flow may be MA-07-causality-market-update-generator, causality-market-update, or an entity outside the
catalogued set. This description asserts no storage binding until the consumer trace lands.

### A11. MA-06-market-update-authoring-toolchain / classification (1 day) — ADOPT (respell of `DELETE-GATED`), record-only
Delete-gated, sunset-pending; not steady-state production. The toolchain's anchor bucket
s3://opal-market-update carries the 2026-07-30 "very likely delete" ruling, and a combined news-av plus
market-update teardown package was staged for release 0.7.0 the same day. Teardown is preconditioned
on stopping the fred-data-ingestion daily write first (the gate: a consumer trace of the live fred
flow). The surface remains present but is not to be described as steady-state production.

### A12. bd-bronze-transactions / description (3 days) — ADOPT, manifest row
Bronze-tier (raw) transaction records from the Black Diamond custodial source within the partner-data
estate. The "bd" tag is the Black Diamond custodial source fossilized into legacy bucket naming ("just
poor naming" per the sovereign note); it is not a tier name and not a generic black-diamond store.
Under the 2026-07-30 target architecture opal-data-assets is the canonical singular source of truth
for partner data, organized bronze (raw) -> silver (parquet, structured/cleaned) -> gold
(logic/derived/analytical); the legacy s3://opal-data-bd bucket is migrating into it.

### A13. mdpf-global-view / description (2 days) — ADOPT, manifest row
A view in the opal-data-mdpf estate, whose pipeline includes the mdpf-daily-trigger lambda. The
sovereign condemned the mdpf bucket on 2026-07-30 ("this whole bucket is garbage") and explicitly
denied that these resources have anything to do with the real ETF actual-holdings flow, so any recorded
linkage of this view to ETF holdings reporting is superseded and denied. The mdpf estate is ordered
dissolved into opal-data-assets (medallion) and opal-data-portal-v2 (platinum serving), with an
investigation mandated.

### A14. mdpf-global-view / classification (1 day) — ADOPT (respell of `CONDEMNED - DISSOLUTION ORDERED`), record-only
Condemned; dissolution ordered 2026-07-30 (questionable existence). The entire opal-data-mdpf surface
was condemned outright and ordered dissolved into opal-data-assets and opal-data-portal-v2 with an
explicit investigation. Any CANON or KEEP label still carried for mdpf-global-view is drift from that
ruling, not warrant.

### A15. etfs-reports-pipeline / classification_reason (2 days) — ADOPT, record-only
Classification held pending the ordered investigation. Any assertion that etfs-reports-pipeline is the
settled ETF actual-holdings daily writer is suspended: the sovereign condemned s3://opal-data-mdpf and
stated the real ETF actual-holdings daily writer "has nothing to do with any of these resources", and
s3://opal-data-etfs is migrate-gated as mission-critical ETF rebate ops pending robustness and
assets-overlap clash review. Until the mdpf dissolution investigation and the etfs gate reviews
conclude, no settled-writer role is recorded.

### A16. bd-gold-layer-pipeline / enrichment (2 days) — ADOPT, record-only
This pipeline's documented home in the legacy opal-data-bd estate sits under a declared target
architecture that points elsewhere: under the 2026-07-30 PARTNER-DATA TARGET ARCHITECTURE ruling its
gold output belongs in the opal-data-assets /gold tier ("logic/derived/analytical"), not in
opal-data-bd, which is migrating into assets.

### A17. causality-market-update / description (1 day) — ADOPT, manifest row
Causality record for the opal-market-update flow. Prose describing the flow as live, generating
market-update output with downstream consumption, is superseded: under the 2026-07-30 ruling
s3://opal-market-update is delete-gated and judged very likely delete, the gate being a consumer trace
of the live fred daily flow; a teardown package was staged the same day.

### A18. MA-01-market-overview-tiered / enrichment (1 day) — ADOPT, record-only
MA-01 (generator: market-overview-tiered-generator) was one of the two portal-critical modeled readers,
with portal-data-proxy, on which the deletion of s3://opal-market-data-v2 was gated. That gate is
closed by deletion: opal-market-data-v2 was deleted on 2026-07-30 (474 objects archived local-only;
head_bucket 404), and the deletion record shows zero references to the bucket in the deployed code of
both readers. opal-market-data-v2 is retired from this entity's lineage.

### A19. PPI-05-opal-portal-data-proxy / enrichment (1 day) — ADOPT, record-only
opal-portal-data-proxy (PPI-05) is one of the two portal-critical modeled readers, with
market-overview-tiered-generator, on which the deletion of s3://opal-market-data-v2 was gated. The
bucket was deleted 2026-07-30 (head_bucket 404) after the deployment zips of both readers were
checked for code references. The modeled read edge from this proxy to opal-market-data-v2 is dead;
any lineage still asserting it has drifted.

### A20. bd-portal-publisher / enrichment (1 day) — ADOPT, record-only
Recorded as a direct publish path from the opal-data-bd estate (the 49 FINANCIAL partner-data bucket
whose name fossilizes the Black Diamond custodial source) into the portal serving layer. That wiring
sits against the 2026-07-30 partner-data target architecture: opal-data-assets is the singular source
of truth, bd is migrating into it, and opal-data-portal-v2 is scoped to /platinum serving artifacts
with partner inputs exclusively from the assets medallion. A direct bd-gold-to-portal route conflicts
with that end state and is to be reconciled at migration.

### A21. inf-gold-dispatch-ec2 / description (1 day) — ADOPT (AMEND: staleness clauses dropped; the 08-20 ratified enrichment already carries the last-confirmed date), manifest row
EC2 host for the Inflection (inf) partner gold-layer dispatch. Its entrypoint, orion-gold-dispatch.sh,
pulls the shared runner bundle from s3://opal-runner-shared (script lines 95-96) on each inf gold
dispatch run.

### A22. globgrph-nessie-fargate-service / description (1 day) — ADOPT (AMEND: co-change hedges dropped), manifest row
Fargate service in the globgrph estate carrying the service name nessie. The 2026-07-30 rulings group
the DynamoDB tables nessie _objs and _refs into the globgrph resource set (all globgrph resources are
to be summarily terraformed) and record a shared-reader organization on
s3://opal-313476888478-globgrph (question Q-6). Both relationship claims rest on those rulings and
await confirmation in the terraform act.

### A23. FRED-07-deck-generation / description (1 day) — ADOPT, manifest row
Deck-generation pipeline organized as five subtrees: lambda_api, mcp_server, scripts, specs and tests.
The whole deck_generation source tree is cold on the commit record (every subtree last touched >= 90
days ago), consistent with the dormant classification ratified 2026-08-20. This is a source-freshness
statement, not a decommission: the runtime citation leg is unmeasured, so a deployed Lambda built from
this tree may still execute, and no sovereign ruling covers deck_generation.
*(CVO check 2026-09-04: the working tree agrees — newest file under deck_generation/ is dated
2026-06-26, last commit 2026-06-23.)*

### A24. FRED-06-exec-summary-generator / description (5 days) — ADOPT, manifest row
Executive-summary generation component of the FRED-06 surface. Its maintenance state is unverified:
the only measured signal is its test subtree tests/exec_summary, cold for >= 90 days; the citation leg
is unmeasured and no production runtime paths were captured, so neither live production use nor active
development is confirmed. Consistent with the dormant-suspect/unverified classification ratified
2026-08-20.

### A25. FRED-06-exec-summary-generator / classification_reason (1 day) — ADOPT, record-only
Classified cold on the test leg only: tests/exec_summary has no touches for >= 90 days and zero paths
under the entity changed in-window; no sovereign ruling supplies a keep or delete warrant. A
single-leg signal: source, build and invocation legs were not measured, so the classification stays
dormant-suspect/unverified pending a runtime/citation-leg check (the 08-20 respell).

---

## BLOCK B — RECOMMEND REJECT, measured but not landable (12 rows)

| # | Entity / field | Days | Why reject |
|---|---|---|---|
| B1 | PPI-12-opal-session-analytics / enrichment | 3 | Duplicate carrier of A1-A3 plus a 14-day co-change measurement that is true for one window only. |
| B2 | TS-5-parquet-batch-export / enrichment | 3 | Uses commit co-change (0 pairs in 14d) to refute a DESIGN coupling stated in a ruling; wrong instrument for the claim, and time-bound. |
| B3 | cot-pipeline / enrichment | 2 | A staleness note about the 07-30 "mid-migration" stamp; A5 carries the substance without the clock. |
| B4 | FRED-01-yield-curve-daily-ingest / enrichment | 2 | Attribution by name-closeness to "fred-data-ingestion"; the proposal cannot confirm the ordered stop; INFERRED/UNMEASURED-tagged. FRED-01's ratified 08-20 description stands. |
| B5 | MA-06-market-update-authoring-toolchain / enrichment | 1 | Duplicate of A10/A11 with time-bound clauses ("sixteen stale days"). |
| B6 | ceo-daily-wsjft-digest / enrichment | 1 | Duplicate carrier of the description ratified 08-20 (same identity, same unreconciled code, same open review). |
| B7 | FRED-04-yang-macro-canonical / description | 7 | The yang_pkl six (B7-B12): one git measurement of ONE subtree (data/yang_pkl, cold on the commit record since 2026-02-06) attributed to THREE entities, each proposal disclaiming its own attribution ("the true owner may instead be FRED-05, MA-08, or another entity"). A classification that attaches "to the closest shown match without asserting ownership" is not a classification (Rule 22 GRAIN: the object read is not the object claimed). The cold fact is already carried once, on MA-08's description ratified 08-20. And the repo subtree is not the yang pipeline's live input path: the day's Bloomberg PKLs reach the yang pipeline through the portal /data-refresh channel, which git cannot see, so git coldness there says nothing about the pipeline's currency. |
| B8 | FRED-04-yang-macro-canonical / classification | 4 | as B7 |
| B9 | FRED-05-yang-macro-timeseries / classification | 2 | as B7 |
| B10 | FRED-05-yang-macro-timeseries / description | 1 | as B7 |
| B11 | MA-08-yang-generate-volatility / classification | 3 | as B7 (and coins `DRIFT-SUSPECT / DORMANT-WRITER-CANDIDATE`) |
| B12 | MA-08-yang-generate-volatility / classification_reason | 1 | as B7 |

## BLOCK C — RECOMMEND REJECT, INFERRED- or UNMEASURED-only on every occurrence (20 rows)

A value must carry its claim; the producer tagged every occurrence of these pairs INFERRED,
UNMEASURED or (one) untagged, so none may be treated as measured. Rejecting lands nothing and forbids
nothing: a later MEASURED occurrence is a new proposal.

C1 mdpf / enrichment (untagged) · C2 PPI-13-schwab-anonymizer / description · C3 bd-gold-layer-pipeline /
description (3 days) · C4 bd-canonical-prices / description · C5 finbert-sentiment-scoring / classification ·
C6 MA-01-market-overview-tiered / description · C7 yang-cma / classification · C8 bd-gold-layer-pipeline /
classification (2 days) · C9 bd-gold-layer-pipeline / classification_reason · C10 inf-bronze-api-pull /
description (2 days) · C11 etfs-reports-pipeline / description · C12 find-insure-casefind-pipeline /
enrichment · C13 smartx-rest-daily-ingest / classification · C14 smartx-rest-daily-ingest / description ·
C15 bd-allocations / description · C16 FRED-01-yield-curve-daily-ingest / classification ·
C17 find-insure-casefind-pipeline / description · C18 PPI-03-opalinvest-auth-handler / description ·
C19 bd-gold-foundation / description · C20 causality-market-update / classification

## BLOCK D — already ratified 2026-08-20; every other occurrence is mechanical (7 pairs, no ruling needed)

FRED-01-yield-curve-daily-ingest / description (19 days) · FRED-07-deck-generation / classification
(21 days) · TS-5-parquet-batch-export / classification (30 days) · FRED-06-exec-summary-generator /
classification (13 days) · MA-08-yang-generate-volatility / description (5 days) · ceo-daily-wsjft-digest /
description (4 days) · inf-gold-dispatch-ec2 / enrichment (4 days). Each day's record marks these
*already ratified 08-20 (record @<commit>)*; the producer re-proposes them daily because three of the
four field kinds have no canonical home to read the ratified text back from (the 08-20 structural
finding, routed to the CTO).

---

## What lands on the word, per day, oldest first (08-08 .. 09-03, 26 days)

1. `org/estate-reports/YYYY-MM-DD.md` — decision record: the day's proposals in a verdict table
   (ADOPTED / ADOPTED-WITH-AMENDMENT / REJECTED / ALREADY-RATIFIED-0820), citing this packet and the
   ruling verbatim; description adoptions also edit the manifest row (prose only) in the same commit.
2. `aws s3 cp` the record to `s3://opal-estate-report/adjudicated/YYYY/MM/DD/estate-report-YYYY-MM-DD.md`.
3. Manifest flip LAST: `{"status":"ADJUDICATED"|"NO-SEMANTIC-CHANGES","by":"3.0.0_SA_CVO","at":...,"repo_commit":...}`.
   A day whose every proposal is REJECTED or ALREADY-RATIFIED flips NO-SEMANTIC-CHANGES.

**Answer forms that suffice:** "approve all recs" · "approve all recs except A5 -> reject" · "B7-B12 adopt"
· any row-by-row list. An AMEND with your own text: give the text and it lands verbatim.
