# Never-widen half, MDPF_SECCLASS -- identifier_namespace on CUSIP-keyed and NAME-keyed rows: the conditional backfill (W26-S5, cell SC-e-69)

**Author:** `0.9.0_WK_MDPF_SECCLASS~59` for `2.0.0_SA_COO~M1`, 2026-10-08. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been written to any table. The backfill writer refuses `--write` until both headings at the foot read SIGNED.
Spec: CTO round-12 analysis section 3 item 3 ("identifier_namespace on every CUSIP-keyed row the AI runner and the DIRECT writers land. The writer change comes first, then a conditional backfill of rows that have none (count printed)"); contract `org/standards/MDPF_SECCLASS_CONTRACT.json` `fields.identifier_namespace` (values TICKER, CUSIP, BLOOMBERG, NAME; "a row without identifier_namespace reads as TICKER").

## The writer change (landed in code, no table act)

`infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py` `landing_row()` now carries `identifier_namespace` from the key form through `identifier_namespace_of()`: `CUSIP:` -> CUSIP; `NAME::` -> NAME; `BBG:` -> BLOOMBERG; any other (bare) key -> TICKER. The rule applied is the contract's own definitions: TICKER is "the default reading for any row where identifier_namespace is absent", CUSIP is the `"CUSIP:<9 chars>"` key, NAME is `NAME::<slug>`, BLOOMBERG is `BBG:<ticker>:<exch>`. Every other `landing_row` field is unchanged (test `tests/test_runner_identifier_namespace.py`, 14 tests, with a difference control). The shared writer's field list `_WRITE_FIELDS` already carries `identifier_namespace`, so the put lands it. This changes rows written by FUTURE runs only.

## The act (by the issuer, after both halves sign)

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/namespace_backfill.py --write --half <this file> --snapshot <snapshot.json>`
- **The set:** one paginated, ConsistentRead scan of `etf-classifications` on 2026-10-08 (2 pages). Every row whose key starts `CUSIP:` or `NAME::` and whose `identifier_namespace` attribute is absent is planned.
- **The count, measured by the writer's dry run against the LIVE table:** `NAMESPACE-BACKFILL-DRY-RUN rows=9155 missing_cusip=0 missing_name=0 puts=0`. The dry run wraps the client with a counter of every mutating call and asserts it is 0.
- **Each planned key** is ONE conditional `UpdateItem`: `SET identifier_namespace = :ns` with condition `attribute_exists(ticker) AND attribute_not_exists(identifier_namespace)`. A row that gained a namespace since the scan is refused and reported, never overwritten; a deleted row is never re-created; the rest continue. No other attribute is touched, `updated_by` and `last_updated` included; no row is created or deleted.
- **Bare-key rows are not planned:** an absent value reads TICKER (CTO RULING 103140), and the contract says the value is never inferred from the key shape by a reader, so stamping a bare row would add nothing a reader does not already read.

## Blast radius

One table, `etf-classifications`; the single attribute `identifier_namespace` of the planned keys. Nothing else on any row; no other table; no S3 object. The planned set today is EMPTY: `missing_cusip=0`, `missing_name=0`. The live census of the 9,155 rows, by key form and stored value (read 2026-10-08, ConsistentRead, 0 mutating calls):

| key form | identifier_namespace stored | rows |
|---|---|---|
| `CUSIP:` | CUSIP | 425 |
| `NAME::` | NAME | 4375 |
| `BBG:` | BLOOMBERG | 626 |
| bare | absent (reads TICKER) | 3729 |

So every CUSIP and NAME row already carries its namespace, the `--write` of today's set would make 0 updates, and the act is a standing guard for rows that land without one before the writer change reaches every path (the runner is the writer this cell changes; the direct writers are the counted writers below).

**Both branches covered:** (A) a CUSIP:/NAME:: row lacking the attribute at the scan -> it gains the value (today: none). (B) a row that gained the attribute between the scan and the write -> the condition refuses, reported, unchanged. A `BBG:` or bare row is in neither branch and is never touched.

**Writers of `identifier_namespace` on `etf-classifications` (to count at signing; not verified by this worker):** this worker names the AI runner (`classify-residual-model.py`, changed here), the shared `etf_classification_scheduled.write()` whose `_WRITE_FIELDS` carries the attribute, and `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`, which a repo search for the token surfaces; the signing seats count the full N and read each rule.

## Readers that print or branch on the attribute

- **Named from the repo:** `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (`ETFClassifier`, the shared reader) and the two copies in `yang_pipeline/positioning/yang-generate-holdings-attribution/` and `yang-generate-positioning/`; the token also appears in the investor-reporting intake/ycharts code and `rivalfunds_classification.py`. Where investor-reporting carries it, its `identifier_namespace` enum is a different, wider schema (the contract's own `token_census` records this as row MDPF_SECCLASS-W5-S2).
- **Not claimed:** any reader this worker did not open. Setting a value on a row that had none moves no `asset_class`, `sub_asset_class` or `classified_by` value (contract `state_coherence`); a reader that branched on absence would see the change, and none is named.

## The local candidate diff (what each planned key reads before and after)

Candidate diff: EMPTY. No `CUSIP:` or `NAME::` key lacks `identifier_namespace` today, so no key reads differently after the act than before. If the set is non-empty at signing, the writer's `--snapshot` holds each planned key's full pre-state item and the rows below are the before/after (an absent attribute -> CUSIP or NAME):

| key | before | after |
|---|---|---|
| (none today) | | |

## Rollback per key

The snapshot (`--snapshot`, written before the first update) holds each planned key's full pre-state item and the value set. `namespace_backfill.py --rollback <snapshot.json> --write` restores each key by `REMOVE identifier_namespace` under the condition `identifier_namespace = :ns`, only where the row still reads the value this run set; a row changed by another writer since is skipped and reported. The dry-run form of `--rollback` lists what it would restore. With an empty set the rollback is a no-op.

## COO half -- UNSIGNED

(`2.0.0_SA_COO` signs here after reading the dry-run line, the census table, the readers section and the writers count. Blast radius, both branches and the rollback per key are named above.)

## CTO half -- UNSIGNED

(`1.0.0_SA_CTO` signs in his own file and this heading records it.)
