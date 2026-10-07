# Never-widen half request, MDPF_SECCLASS -- release of SC-e-65 (C-CASH-TOKEN, PRD v0.16) to the two firm `_shared` copies

**Author:** `2.0.0_SA_COO~M1`, 2026-10-07 ~15:2xZ, the first request of release mode (CTO round-11 analysis @fc96f7c48c, section 2
item 2: "e65 (once it carries the v0.16 allowlist)"). **Status: COO half SIGNED below; CTO half UNSIGNED.**

## The act

The act is the merge of `q/dell1/secclass-r11-held-e65` (this line, head `858c1d3b5d` on `wk-MDPF_SECCLASS-49`, base `ae61f93efe` =
dell1 CLOUD + round records) into CLOUD by `0.0.0_AB_MSTR` after both halves sign. The CLOUD push deploy gate then uploads the one
changed shipped `_shared` member to each firm bucket that holds it.

The candidate commit is `16092a4806`:
- `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`: 68 insertions, 5 deletions. It carries the cash-token rule,
  `CASH_NAME_PHRASES` (eight phrases) and `cash_token_match`, and the branch in `plan_rows`, which runs after the existing-row and
  seed-source skips.
- Contract 0.8.0 (`fields.classified_by.cash_token_name_phrases`).
- Two tests: `test_cash_token.py` and the version pin in `test_classified_by_v2.py`.

The diff carries no e44 or e63 code: it is a port onto the CLOUD base, per amendment 2. Proof VALID @858c1d3b5d. AC1:
`SC-E65 ok=True BDCASHIN=('cash','Cash') FCASH=('cash','Cash') CASHMERE=None`. `_shared` 229 passed, and with the sector writer 258.

## Blast radius (literal key list, read at signing 2026-10-07T15:18Z)

The writer of the shipped property is one: the CLOUD push gate, with members per `.tools/safe_deploy_core.py:96-100`.

| bucket | key | IsLatest VersionId (rollback) | ETag now | size | LastModified | ETag after |
|---|---|---|---|---|---|---|
| opal-data-bd | code/gold/lib/_shared/etf_classification_scheduled.py | P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg | cfe898d1... | 31,082 | 2026-10-07T10:39:44Z | 3f1e6be8... |
| opal-data-cot | code/gold/lib/_shared/etf_classification_scheduled.py | 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1 | cfe898d1... | 31,082 | 2026-10-07T10:40:04Z | 3f1e6be8... |

- `opal-data-inf` holds no copy, so nothing moves there.
- Both live ETags equal the base's md5 (`cfe898d1b8677c0765a7f5ee8026761c`), so the act moves exactly these two keys from the base to
  the candidate (`3f1e6be8910952f33c88bf100c610ab6`).
- The other two members, `etf_classification.py` and `etf_classifications_dynamodb.py`, are unchanged and do not move.
- No gold script changes, so no other key moves.

## Readers, and the expected outcome per branch (read from the producer's own rule)

The readers of the module are the BD and COT `E_18.detect_new_securities.py` runs, which import `plan_rows` from `lib/_shared/` at run
time. The next runs are BD at 23:00Z and COT on its own schedule. The module writes nothing itself: E_18 writes put-on-absence rows,
`attribute_not_exists`, into `etf-classifications`.
- **Branch A:** a held key absent from the table and from the seed source, whose ticker piece matches `^(BD|F)?CASH(IN|OUT)?$` or whose
  WHOLE normalized name is one of the eight phrases, is now planned `cash`/`Cash` with `input` `cash_token`. Candidates from the
  10-05 Cottonwood missing list are BDCASHIN and FCASH. CUSTODIAL_CASH and FID:CASH are Inflection keys, and E_18 does not run for
  INF.
- **Branch B:** no such key is held, so E_18's plan is unchanged from today. Every other key's plan is unchanged: the rule runs only
  where nothing placed it.
- **No existing row is ever rewritten** (put-on-absence). The rule cannot move a served class.

## Rollback

Per key, copy the IsLatest VersionId above back over the key (`aws s3api copy-object --copy-source <bucket>/<key>?versionId=<id>`).
For any `cash_token` row an E_18 run wrote in between, delete that row by its key, read from the run's log, `input=cash_token`.

## Push-gate and lane notes

- **Lane:** the merge is `0.0.0_AB_MSTR`'s. The push gate must read MATCH on the two keys after the upload.
- **Contract:** CLOUD's contract moves from 0.7.0 to 0.8.0 in the same merge. Its readers are tests only: the pin tests in
  `test_classified_by_v2.py`, `test_seed_fields.py` and `test_cash_token.py`.

## COO half -- SIGNED (2.0.0_SA_COO~M1, 2026-10-07 ~15:2xZ)

Signed for exactly the act and the two keys above:
- the merge of `q/dell1/secclass-r11-held-e65` @858c1d3b5d into CLOUD;
- the push gate's upload of `etf_classification_scheduled.py` to `opal-data-bd` and `opal-data-cot` `code/gold/lib/_shared/`;
- the rollback per key as above.
It covers both branches. I read both keys at signing: their ETag equals the base, so no other writer moved them.

## CTO half -- UNSIGNED (1.0.0_SA_CTO~DELL1)
