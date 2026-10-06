# ESTATE SITTING PACKET -- 32 PENDING DAYS IN ONE SITTING (2026-09-04 .. 2026-10-05)

**Authority:** Andrew-direct at the 3.0.0_SA_CVO terminal 2026-10-06 ~02:0xZ, his answer to this seat's question "How do you
want to sit them?": VERBATIM **"Build packet (Recommended)"** -- the option read "I write one packet: each of the 70
entity-fields gets a recommendation by the last sitting's rules ... You then say 'approve all recs' or rule by row, and I land
all 32 days." The loop's operator is 3.0.0_SA_CVO (semantic-evolution RULING 3).
**Prepared by:** 3.0.0_SA_CVO, 2026-10-06 03:07Z. **Ruling:** pending. Nothing lands before his word.

## How the 32 days reduce to 70 rows

| Quantity | Count |
|---|---|
| PENDING days (2026-09-04 .. 2026-10-05; 0 MISSING, 0 FAILED, 0 AI-absent) | 32 |
| Proposals across those days | 223 (157 MEASURED, 62 INFERRED, 4 UNMEASURED) |
| Distinct (entity, field) pairs | 70 |
| already ruled ADOPTED or RATIFIED in an earlier sitting (Block R) | 24 |
| INFERRED- or UNMEASURED-only on every occurrence (Block C) | 15 |
| carrying a MEASURED occurrence, never ruled or rejected before only as inferred-only | 31 |
| of which recommended ADOPT or AMEND (Block A) | 3 |
| of which recommended REJECT, each with its reason (Block B) | 28 |

**The rules, the same as the 2026-09-04 sitting** (`ESTATE_SITTING_PACKET_20260904.md`): a re-proposal of ratified text is
superseded by the ratified text; inferred-only text has no measured claim to land; an adopted text is respelled so no
vocabulary value is minted, and time-bound clauses and sentences about the producer's own instrument are dropped. Two grounds
recur in Block B and are new only in volume: file-pair co-change counts, and one day's uncommitted laptop working tree.

**Landing home, read at HEAD:** `org/modules/graph/estate-coverage-manifest.yaml`. The 08-20 field-home act has landed:
`classification` adoptions sit on the family row (TS-5 carries one), and `description` keys exist (14). A description adoption
lands as a `description:` key on the family row with a comment citing the day record. All three Block A families have rows.

**Each day then lands as its own record** (`org/estate-reports/YYYY-MM-DD.md`, the S3 adjudicated copy, the manifest flip LAST),
citing this packet and the ruling.

---

## BLOCK A -- RECOMMEND ADOPT OR AMEND (3 rows; the text below is the text that lands)

### A1. MA-01-market-overview-tiered / description (2 days, 09-07..09-14) -- AMEND
Portal-critical modeled market data product. s3://opal-market-data-v2 is not one of its sources: that bucket was deleted on 2026-07-30 after a dependency sweep found no reference to it in the deployed code of the estate's portal-critical modeled readers.

*Basis:* Measured now: head-bucket opal-market-data-v2 returns 404. AMEND because the proposal also names the generator `market-overview-tiered-generator`, and no Lambda of that name exists at this read (ResourceNotFoundException); that clause and the partner-data architecture paragraph are dropped.

### A2. PPI-04-opal-partners-data / description (1 day, 10-03..10-03) -- ADOPT
Partner-data component. Its deployed environment sets USERS_TABLE=opal-users-v2, the estate's official user database by the 2026-07-30 ruling; opal-users is the deprecated predecessor. trade-auth-handler carries the same setting, so a change to the opal-users-v2 contract touches both.

*Basis:* Measured now: lambda get-function-configuration opal-partners-data reads USERS_TABLE=opal-users-v2. The ruling asked that this be logged wherever possible.

### A3. TS-6-trade-auth-handler / description (1 day, 10-03..10-03) -- ADOPT
Trade-submission authentication handler. It resolves user identity against opal-users-v2: its deployed environment sets USERS_TABLE=opal-users-v2, the official user database by the 2026-07-30 ruling. The older opal-users table is the deprecated predecessor and is not this handler's user table.

*Basis:* Measured now: lambda get-function-configuration trade-auth-handler reads USERS_TABLE=opal-users-v2. The predecessor's item count is dropped (true for one day).

---

## BLOCK B -- RECOMMEND REJECT, MEASURED BUT NOT LANDABLE (28 rows)

| # | Entity / field | Days | Ruled before | Reason |
|---|---|---|---|---|
| B1 | `find-insure-casefind-pipeline` / description | 2 days, 09-04..09-09 | REJECTED | duplicates the adopted classification (A4, 2026-08-13) and adds a dormancy figure that is time-bound |
| B2 | `cot-pipeline` / enrichment | 2 days, 09-04..09-30 | REJECTED | rests on one day's uncommitted working-tree state on the laptop: true on the capture day, false once committed or discarded |
| B3 | `PPI-12-opal-session-analytics` / enrichment | 2 days, 09-06..09-07 | REJECTED | duplicates the adopted classification (A1) plus a 14-day co-change reading; rejected on the same ground before |
| B4 | `FRED-01-yield-curve-daily-ingest` / enrichment | 3 days, 09-06..09-28 | REJECTED | carries the same gate and teardown facts as the ratified description (2026-08-20); a second carrier of ratified text |
| B5 | `FRED-04-yang-macro-canonical` / description | 4 days, 09-06..09-27 | REJECTED | rests on a 90-day cold-subtree reading, true for the scan window only; ownership of data/yang_pkl among three entities is still unresolved |
| B6 | `bd-gold-layer-pipeline` / description | 9 days, 09-07..10-03 | REJECTED | restates the partner-data architecture ruling and adds a 14-day co-change reading; nothing specific to this entity is measured |
| B7 | `FRED-01-yield-curve-daily-ingest` / classification | 2 days, 09-09..09-14 | REJECTED | classifies the stop as 'unconfirmed' from what the stratum cannot see; a statement about the instrument, not the entity |
| B8 | `MA-08-yang-generate-volatility` / classification | 3 days, 09-09..09-15 | REJECTED | the same 90-day cold-subtree reading as FRED-04; leaves two readings open by its own words |
| B9 | `inf-bronze-api-pull` / description | 2 days, 09-10..09-15 | REJECTED | restates the partner-data architecture ruling; the retarget it describes is unverified by its own words |
| B10 | `PPI-03-opalinvest-auth-handler` / description | 2 days, 09-16..09-29 | REJECTED | says itself that it reflects the pre-window layout and must be re-verified before use |
| B11 | `FRED-05-yang-macro-timeseries` / description | 1 day, 09-27..09-27 | REJECTED | the same 90-day cold-subtree reading as FRED-04 |
| B12 | `PPI-05-opal-portal-data-proxy` / description | 6 days, 09-07..10-05 | -- | identifies the entity as the client module portal/src/api/portal-proxy.ts, where the 2026-07-30 sweep names portal-data-proxy a deployed modeled reader; an identity conflict, and the rest rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B13 | `PPI-04-opal-partners-data` / enrichment | 5 days, 09-07..10-05 | -- | its user-table sentence is carried by the adopted description (A2); the rest rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B14 | `TS-6-trade-auth-handler` / enrichment | 2 days, 09-07..09-11 | -- | the same fact as the adopted description (A3) |
| B15 | `ops-infrastructure-monitors` / description | 2 days, 09-11..09-11 | -- | says the infrastructure_monitor function tracks org/critical_paths/.open_deploys and .open_findings; its source references neither path at HEAD; and the rest rests on one day's uncommitted working-tree state on the laptop: true on the capture day, false once committed or discarded |
| B16 | `MA-04-fear-greed-fetcher` / description | 1 day, 09-11..09-11 | -- | rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B17 | `MA-03-market-regime-classifier` / description | 1 day, 09-11..09-11 | -- | rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B18 | `MA-04-fear-greed-fetcher` / enrichment | 4 days, 09-12..10-05 | -- | rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B19 | `MA-03-market-regime-classifier` / enrichment | 4 days, 09-12..10-05 | -- | rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B20 | `MA-05-volatility-fetcher` / enrichment | 1 day, 09-12..09-12 | -- | rests on file-pair git co-change counts: true for one window, and the stratum's own grain rule bars reading file pairs as coupling between resources (the 2026-09-03 B2 precedent) |
| B21 | `inf-ec2-launch-resilience` / enrichment | 1 day, 09-14..09-14 | -- | is a placeholder about unattributed paths, by its own words; it describes the instrument, not the entity |
| B22 | `inf-ec2-launch-resilience` / description | 1 day, 09-30..09-30 | -- | is a registry naming question (the entity's name does not match the canon producer label), not prose; routed to 1.0.0_SA_CTO as a registry reconciliation, not landed as a description (inf-ec2-launch-resilience against producer inf-ec2-launch-monitor) |
| B23 | `bd-gold-layer-legacy` / classification_reason | 1 day, 09-27..09-27 | -- | is a registry naming question (the entity's name does not match the canon producer label), not prose; routed to 1.0.0_SA_CTO as a registry reconciliation, not landed as a description (bd-gold-layer-legacy and bd-gold-layer-pipeline against producer bd-gold-layer-runner) |
| B24 | `bd-gold-layer-legacy` / description | 2 days, 09-29..10-03 | -- | is a registry naming question (the entity's name does not match the canon producer label), not prose; routed to 1.0.0_SA_CTO as a registry reconciliation, not landed as a description (the same three names) |
| B25 | `MA-09-ycharts-market-data-pull` / description | 2 days, 09-30..10-01 | -- | is a registry naming question (the entity's name does not match the canon producer label), not prose; routed to 1.0.0_SA_CTO as a registry reconciliation, not landed as a description (ycharts-market-data-pull against producer irpt-ycharts-generate) |
| B26 | `bd-asset-dim` / enrichment | 1 day, 09-28..09-28 | -- | rests on one day's uncommitted working-tree state on the laptop: true on the capture day, false once committed or discarded |
| B27 | `bd-allocations` / enrichment | 1 day, 09-28..09-28 | -- | rests on one day's uncommitted working-tree state on the laptop: true on the capture day, false once committed or discarded |
| B28 | `bd-bronze-transactions` / enrichment | 1 day, 09-28..09-28 | -- | rests on one day's uncommitted working-tree state on the laptop: true on the capture day, false once committed or discarded |

**Registry questions (B22-B25), for 1.0.0_SA_CTO, not prose:** three registry names do not match the canon producer
label the resolver attributes paths to: inf-ec2-launch-resilience (producer inf-ec2-launch-monitor); bd-gold-layer-legacy and
bd-gold-layer-pipeline (producer bd-gold-layer-runner); MA-09 ycharts-market-data-pull (producer irpt-ycharts-generate).

---

## BLOCK C -- RECOMMEND REJECT, INFERRED OR UNMEASURED ONLY (15 rows)

| # | Entity / field | Days | Ruled before |
|---|---|---|---|
| C1 | `FRED-04-yang-macro-canonical` / classification | 1 day, 09-04..09-04 | REJECTED |
| C2 | `PPI-13-schwab-anonymizer` / description | 5 days, 09-07..09-28 | REJECTED |
| C3 | `causality-market-update` / classification | 1 day, 09-09..09-09 | REJECTED |
| C4 | `finbert-sentiment-scoring` / classification | 1 day, 09-09..09-09 | REJECTED |
| C5 | `globgrph-incremental-updater` / description | 2 days, 09-09..10-01 | -- |
| C6 | `bd-gold-foundation` / description | 1 day, 09-10..09-10 | REJECTED |
| C7 | `globgrph-derive-runner-fargate` / description | 3 days, 09-11..09-30 | -- |
| C8 | `layer3-gpt-curation` / description | 1 day, 09-12..09-12 | -- |
| C9 | `globgrph-nessie-fargate-service` / enrichment | 1 day, 09-12..09-12 | -- |
| C10 | `find-insure-casefind-pipeline` / enrichment | 1 day, 09-13..09-13 | REJECTED |
| C11 | `MA-06-market-update-authoring-toolchain` / enrichment | 1 day, 09-14..09-14 | REJECTED |
| C12 | `globgrph-nessie-fargate-service` / classification | 1 day, 09-14..09-14 | -- |
| C13 | `bd-gold-foundation` / enrichment | 1 day, 09-28..09-28 | -- |
| C14 | `bd-historical-prices` / enrichment | 1 day, 09-28..09-28 | -- |
| C15 | `bd-gold-detail-checker` / enrichment | 1 day, 09-28..09-28 | -- |

---

## BLOCK R -- ALREADY RULED; EVERY OCCURRENCE IS SUPERSEDED BY THE RATIFIED TEXT (24 rows)

| # | Entity / field | Days | Ruled before (verdict, first record) |
|---|---|---|---|
| R1 | `PPI-12-opal-session-analytics` / classification_reason | 2 days, 09-04..10-04 | ADOPTED (2026-08-17) |
| R2 | `TS-5-parquet-batch-export` / description | 6 days, 09-04..09-30 | ADOPTED (2026-08-12) |
| R3 | `FRED-01-yield-curve-daily-ingest` / description | 15 days, 09-04..10-05 | ADOPTED, ALREADY-RATIFIED- (2026-08-11) |
| R4 | `MA-06-market-update-authoring-toolchain` / description | 3 days, 09-04..09-15 | ADOPTED (2026-08-12) |
| R5 | `inf-gold-dispatch-ec2` / enrichment | 1 day, 09-04..09-04 | ADOPTED, ALREADY-RATIFIED- (2026-08-11) |
| R6 | `FRED-07-deck-generation` / classification | 6 days, 09-04..09-27 | ALREADY-RATIFIED- (2026-08-11) |
| R7 | `FRED-06-exec-summary-generator` / classification | 5 days, 09-04..09-27 | ADOPTED-WITH-AMENDMENT, ALREADY-RATIFIED- (2026-08-13) |
| R8 | `PPI-12-opal-session-analytics` / description | 4 days, 09-05..09-30 | ADOPTED (2026-08-12) |
| R9 | `MA-01-market-overview-tiered` / enrichment | 2 days, 09-05..09-08 | ADOPTED (2026-08-16) |
| R10 | `PPI-05-opal-portal-data-proxy` / enrichment | 10 days, 09-05..10-04 | ADOPTED (2026-08-16) |
| R11 | `PPI-12-opal-session-analytics` / classification | 22 days, 09-06..10-05 | ADOPTED (2026-08-12) |
| R12 | `TS-5-parquet-batch-export` / classification | 21 days, 09-06..10-05 | ADOPTED-WITH-AMENDMENT, ALREADY-RATIFIED- (2026-08-11) |
| R13 | `causality-market-update` / description | 1 day, 09-06..09-06 | ADOPTED (2026-08-11) |
| R14 | `cot-pipeline` / description | 7 days, 09-06..10-05 | ADOPTED-WITH-AMENDMENT (2026-08-13) |
| R15 | `TS-5-parquet-batch-export` / classification_reason | 5 days, 09-06..10-04 | ADOPTED (2026-08-17) |
| R16 | `FRED-06-exec-summary-generator` / description | 1 day, 09-07..09-07 | ADOPTED (2026-08-17) |
| R17 | `inf-gold-dispatch-ec2` / description | 1 day, 09-08..09-08 | ADOPTED-WITH-AMENDMENT (2026-08-18) |
| R18 | `globgrph-nessie-fargate-service` / description | 2 days, 09-09..09-13 | ADOPTED-WITH-AMENDMENT (2026-08-18) |
| R19 | `MA-06-market-update-authoring-toolchain` / classification | 4 days, 09-13..10-01 | ADOPTED-WITH-AMENDMENT (2026-08-31) |
| R20 | `PPI-13-schwab-anonymizer` / classification | 1 day, 09-15..09-15 | ADOPTED-WITH-AMENDMENT (2026-08-14) |
| R21 | `bd-bronze-transactions` / description | 1 day, 09-15..09-15 | ADOPTED (2026-08-12) |
| R22 | `MA-08-yang-generate-volatility` / description | 1 day, 09-27..09-27 | ADOPTED, ALREADY-RATIFIED- (2026-08-11) |
| R23 | `FRED-07-deck-generation` / description | 7 days, 09-27..10-05 | ADOPTED (2026-08-28) |
| R24 | `bd-gold-layer-pipeline` / enrichment | 1 day, 09-28..09-28 | ADOPTED (2026-08-13) |

---

## What a ruling of "approve all recs" does

- Lands the three Block A texts as keys on their manifest rows, one commit.
- Writes 32 day records, each listing its own proposals with the verdict from this packet; uploads each to
  `s3://opal-estate-report/adjudicated/YYYY/MM/DD/`; flips each manifest to ADJUDICATED (days with an adoption) or
  NO-SEMANTIC-CHANGES (days without), last.
- Sends the registry questions (B22-B25) to 1.0.0_SA_CTO in one line.


## Ruling, part 1 (Andrew-direct 2026-10-06 03:12Z at this terminal)

Asked "How do you rule?" with the options approve all recs / rule by row / no changes, he chose VERBATIM **"Rule by row"**:
he names the rows he wants changed, and every other row lands as recommended. His row rulings follow here when given.
Nothing has landed yet.

## Ruling, part 2 (Andrew-direct 2026-10-06 ~03:2xZ at this terminal)

After a plain-language summary (3 of 223 suggestions worth landing; the rest repeats, one-day facts, co-change
signals or text already ruled) and the question "Shall I land the 3 and close the 32 days?", he answered VERBATIM
**"yeah agreed"**. He named no row under "Rule by row", so every row lands as recommended. Whether the daily
suggestion step is kept, made weekly or dropped was put to him as his own later decision; nothing here decides it.

-- 3.0.0_SA_CVO
