# NEVER-WIDEN CO-SIGN -- CTO HALF -- AMGT_RESAPP round 11, cell `AMGT-rj-10`: THE DEPLOY AND THE LIVE READ

**Signer:** `1.0.0_SA_CTO~W` (the project's CTO limb on Andrew's word of 2026-09-14 ~23:2xZ, @`ce7371d0b3`).
**Date:** 2026-09-15 ~07:4xZ. **Verdict:** SIGNED, for the blast radius below and only it, with the two branches
named in s.4 covered on both sides.
**Counterpart half:** `ledger/NEVER_WIDEN_ROUND11_ONE_STORE_COO_HALF.md` (`2.0.0_SA_COO~W`, @`065fa6070d`, 30 lines,
in the tree at this signing). **This half is the CTO's own read of the act's blast radius**, re-derived from the
producers' rules and the live plane at this seat, not a restatement of the COO's. Where the two halves disagree on a
NUMBER the disagreement is named (s.3); on the ACT they agree.

## 1. RULING: NEVER-1 BINDS THIS ACT

CLAUDE.md NEVER-1: *"NEVER move served output without never-widen sign-off (CTO+COO)."* The act changes the code of
the two functions that produce and serve every `/api/scoped/amgt/*` payload (the adapter `opal-amgt-scoped-api`, the
producer `amgt-resapp-chatter-axis`), edits their two role policies, and writes a ranking generation. The served
content of the coverage, thesis, peers, overlay-points, rankings, timeseries, management and posture reads moves.
That is moving served output. Both halves present as files in the main tree = rj-10 AC1 met.

## 2. THE ACT, READ FROM THE PRODUCER'S OWN RULE (the harvest root's terraform against `harvest/tfstate`)

**Vintages.** The harvest root at HEAD `a9cea42d5d` (7 `.tf` files; 26 top-level resource declarations + 2 module
calls, censused by this seat: `api-gateway.tf` 6, `chatter-axis-schedule.tf` 6, `dynamodb.tf` 2, `s3.tf` 4,
`scoped-amgt-api.tf` 7, `sqs.tf` 1, `main.tf` 0). `harvest/tfstate` read from the backend object at ~07:3xZ:
**serial 34, terraform 1.15.8, 32 entries = 30 managed + 2 data, 42 managed instances** (the one `for_each` route
resource carries 11). Composition of the 32: the 16 pre-existing (enqueue 6, tables 2, bucket + 3 config, SQS,
`module.harvest_enqueue` 3), the 6 the round-10 producer consolidation `ri-2` moved in (two roles, two policies, the
function, the schedule), the 10 the round-10 mount `ri-4` added (integration, 11-instance route, role, policy,
attachment, permission, `terraform_data`, `module.scoped_amgt_api` 3). `s3.tf` at HEAD reads `bucket =
"opal-data-harvest"` and `aws_s3_bucket.harvest` is in state -- round 10's precondition is now a committed fact.

**The four addresses the plan MAY change, and nothing else:**

| address | what changes | how the change is caused |
|---|---|---|
| `module.scoped_amgt_api.aws_lambda_function.this` (`opal-amgt-scoped-api`, live `Active`, CodeSha256 `sSanbq4vc+SDwxKfHplJr32E7hiPTYSJKm37hVMkPHA=`, 75917 B, LastModified 2026-09-15T03:48:34Z, python3.11) | code (`source_code_hash`) | the artifact `research/opal-amgt-scoped-api.zip` re-uploaded by the round-10 closure builder extended with `lib/research/coverage/pool_reader.py`, the two schema files under `lib/opal_data_harvest/`, a vendored `jsonschema`, and chain A's adapter edits; `data.aws_s3_object.artifact` re-reads its metadata at plan |
| `aws_lambda_function.chatter_axis_producer` (`amgt-resapp-chatter-axis`, live `Active`, CodeSha256 `fj8wqp9jaZWfMaBrrAyUImGnt2c5Xeb7losUr+i65mM=`, 24370 B, LastModified 2026-09-15T02:33:20Z, python3.12) | code (`source_code_hash` via `filebase64sha256()` of the local build) | `lambda_src/build_zip.py` extended with the pool reader, the crosswalk, the generation writer, the schema files, `jsonschema` |
| `aws_iam_role_policy.scoped_amgt_api_grants` | policy document | at HEAD three statements: `ReadRankedAxesAndPoints` (Query/GetItem/BatchGetItem on the metrics table + `/index/*`), `ReadTheArticleStoreForTheCoverageTab` (Query on `opal-harvest-articles` + `/index/*`), `WriteOnlyTheFirmsOwnStarMarkers` (PutItem/DeleteItem on the metrics table). After: the article-store statement REMOVED; `s3:GetObject` on `arn:aws:s3:::opal-data-harvest/<prefix>*` for the nine prefixes and `s3:ListBucket` on the bucket arn under an `s3:prefix` condition ADDED; the other two statements byte-unchanged |
| `aws_iam_role_policy.chatter_axis_lambda` | policy document | at HEAD three statements: `ReadArticlesTickerDateIndex` (Query on `opal-harvest-articles` + `ticker_date_index`), `WriteSecurityMetrics` (PutItem/BatchWriteItem on the metrics table), `OwnLogStreamOnly`. After: the articles statement REMOVED; the S3 read statements ADDED; the other two byte-unchanged |

**Expected plan: `0 to add, 4 to change, 0 to destroy`**, the four addresses above enumerated APART from the two
`data.aws_s3_object.artifact` reads (slug lesson W17-S5). The other 28 entries (38 instances) are outside this
signature: any add, any replace, any destroy, or a change on a fifth managed address (the log groups, the schedule,
the scheduler role, the routes, the tables, the bucket, the queue, the enqueue set) is NOT the act this half covers
and `rj-10` STOPS at AC4.

**One write outside terraform:** the artifact key `research/opal-amgt-scoped-api.zip` in the versioned artifacts
bucket. Round 10 created it (404 before, 75917 B after); this act OVERWRITES it, so the bucket's versioning is the
rollback: **the worker prints the key's current `VersionId` (head-object) BEFORE the upload** and the rollback is a
copy of that version back to the key plus a re-apply, not a delete marker.

**One write outside terraform, on data:** the producer's QA invoke (AC7) writes one COMPLETE generation per chatter
axis for today -- rows at `<AXIS>#<date>#<generation_id>` and a pointer item at `<AXIS>#<date>` / `_CURRENT` --
additive; prior rows never deleted.

## 3. THE PROPERTIES THIS ACT MOVES, AND THEIR WRITERS COUNTED (the rule the COO half printed as ONE)

**Property A: the rows of `opal-harvest-security-metrics`.** ⛔ **THREE writers at HEAD, not one**, censused by
this seat over the repo (`comp-find`, DEF band: 6 files define against the table name; three of them WRITE):

| writer | rule | partitions it writes | live rows at ~07:3xZ (full scan, 62 items, 4 partitions, no pagination token) |
|---|---|---|---|
| W1 `lib/research/metrics/chatter_axis.py` `default_write_rows` -- the Lambda `amgt-resapp-chatter-axis` (QA invoke; the 10:00Z schedule) | `batch_writer(overwrite_by_pkeys=['axis_date','ticker'])`, upsert per row, never clears (the measured defect, brief @`5ae6dd04b5`) | `TRENDING_CHATTER#<d>`, `BREAKOUT_CHATTER#<d>` | `TRENDING_CHATTER#2026-09-12` 10, `TRENDING_CHATTER#2026-09-15` 10; and the pre-registry `CHATTER#2026-09-11` 10 |
| W2 `integrations/bloomberg/research/price_axis_pull.py` -- box-side, Bloomberg DAPI, an operator run | one item per ranked ticker at `f"{axis}#{as_of_key}"` for each of `axes_for_subject("PRICE")`; NO pointer, NO generation id | `TRENDING_PRICE#<d>`, `BREAKOUT_PRICE#<d>` | **none under the registry's names**; only the pre-registry `PRICE#2026-09-10` 32 rows |
| W3 `lib/research/watchlist/store.py` -- the adapter's star/unstar routes | `put_item` / `delete_item` on the marker row at `_partition_key(firm_id)` | the firm's marker partition | 0 today |

Only W1 is migrated by this round (rj-5 writes the generation writer; rj-10 deploys it). W2 is UNCHANGED by the act
and keeps writing bare crossed partitions with no pointer whenever an operator runs it. W3 is unchanged and its grant
(`WriteOnlyTheFirmsOwnStarMarkers`) stays byte-identical. The COO half's "ONE writer" is true of the CHATTER
partitions and false of the table; the difference matters at property B.

**Property B: the served ranking payloads (`/lead-panel/rankings/*`, the overlay's points, `/timeseries/*`).** One
producer (the adapter) reads them, and after rj-9 it "follows G-1's pointer ... never a bare date partition"
(decomposition s.19c). For the CHATTER axes that is the act. For the PRICE axes the pointer does not exist
(W2 writes none), so the reader's rule has two branches and this half covers BOTH:

- **Measured today:** the adapter resolves every (movement, subject) to the CROSSED partition
  `<MOVEMENT>_<SUBJECT>#<date>` (`scoped_amgt.py`, `resolve_axis` off the producers' registry; the legacy `PRICE#`
  partition is no longer read since `rf-1`). The live table holds NO `TRENDING_PRICE#` or `BREAKOUT_PRICE#` partition.
  **So every served PRICE ranking already reads `row_count 0` at HEAD, for any date, and the act cannot lower it.**
- **Branch B1 (the reader falls back to the bare crossed partition when no pointer exists -- the CRO's follow-up
  residual 1):** served PRICE output is unchanged by the act now and stays served the next time W2 runs. INSIDE this
  signature.
- **Branch B2 (the reader returns an explicit ABSENT state, e.g. `state: no_generation`, for a pointerless
  partition):** served PRICE output is unchanged NOW (0 -> ABSENT-explicit), and the next W2 run lands rows the page
  will not show until W2 is migrated. INSIDE this signature for THIS act, on the condition that the state is
  EXPLICIT on the payload (never a silent empty list); the W2 migration is a later cell and is named here so nobody
  reads the empty Price axis as the world's.
- **NOT covered:** a reader that raises, 500s, or serves a MIXED generation on any axis.

**Property C: the served coverage payload.** Removing both roles' `opal-harvest-articles` grants means coverage can
only come from the pool after the act. Both branches: a name with pool objects (the bounded commissioning uploads:
publications/v1 and publication-links/v1 exist on the live bucket, 53 objects at the ~04:5xZ draw) serves items; a
name without them serves `store_item_count 0` with the `states` block. An `AccessDenied` from the retired table
cannot occur because nothing reads it after the act; an `AccessDenied` on the POOL (a prefix missing from the new
grant) surfaces as `states.denied` per C-ONE-STORE and is a STOP for rj-10's AC8, not a quiet empty.

**Property D: the two role policies.** Writers: the harvest root only (the roles are declared in
`scoped-amgt-api.tf` and `chatter-axis-schedule.tf`; no other root attaches to either role -- both are
`aws_iam_role_policy` inline documents, so a second writer would have to be a second inline declaration on the same
role name, and the census above finds none). The act NARROWS DynamoDB (two Query statements removed) and WIDENS S3
READ (nine prefixes on Opal's own bucket, `GetObject` + conditioned `ListBucket`); it adds NO `s3:PutObject`,
`s3:DeleteObject`, `dynamodb:Scan`, wildcard resource, or grant on `opal-data-etfs`. REC, not a STOP: the producer
role reads four of the nine prefixes (`publication-links/v1/`, `publications/v1/`, `crosswalk/v1/`,
`universe/v1/`); a four-prefix grant on `chatter_axis_lambda` is the least-privilege shape and is inside this
signature; the nine-prefix grant the COO half names is also inside it.

## 4. BLAST RADIUS, PER KEY, AND THE ROLLBACK FOR EACH -- BOTH BRANCHES COVERED

| key | may be touched? | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | YES (updated in place) | copy the prior artifact version (VersionId printed before upload; CodeSha256 `sSanbq4vc+...`, 75917 B) back to the key and re-apply |
| `amgt-resapp-chatter-axis` code | YES (updated in place) | rebuild at HEAD `a9cea42d5d`'s inputs (prior CodeSha256 `fj8wqp9j...`, 24370 B) and re-apply |
| `aws_iam_role_policy.scoped_amgt_api_grants`, `aws_iam_role_policy.chatter_axis_lambda` | YES (documents) | `git revert` the two `.tf` edits and apply (`0 to add, 2 to change, 0 to destroy`) |
| the metrics table's NEW rows (generation rows + pointer items) | YES, additive | leave in place (the old adapter never queries `<AXIS>#<date>#<gen>`); ⛔ the pointer item at `<AXIS>#<date>` / `_CURRENT` sits INSIDE a legacy bare-date partition -- **it must carry NO `rank_sort` attribute**, or the rolled-back adapter's `axis-rank-index` Query on that partition returns it as an eleventh row. The worker prints the pointer item's attribute names at AC7; if `rank_sort` is present, the rollback ALSO deletes the pointer items |
| the metrics table's EXISTING rows (62 today, 4 partitions) and W2's future bare partitions | NO | none needed; a delete of any existing row is outside this signature |
| the `_CURRENT` semantics on a re-invoke (the changed-winner control) | YES: the pointer moves to the new generation; the old generation's rows stay | re-point to the prior `generation_id` (an item write), never a row delete |
| `opal-harvest-articles` (the table) | NOT touched by the apply; its grants removed | re-apply the reverted policies |
| `s3://opal-data-harvest` objects | NOT written by the act (read grants only) | none |
| `opal-data-etfs` | NOT touched, no grant | none |
| the 11 routes on `7k3ed8px20`, the authorizer, the schedule, the queue, the bucket, the enqueue set | NOT touched (28 entries / 38 instances unchanged in the plan) | none; a change on any of them is a STOP |
| the portal (DEV/PROD/gitlink `e85f6eb84f`) | NOT touched; chain A's page lands on `refs/drains/rj-portal` only | freeze stands: COMMIT YES / PROMOTE NO |
| the 10:00Z schedule | NOT changed; its next fire runs the NEW producer code | the code rollback above covers it; the fire is inside the act's world either way |

**If the apply fails midway:** terraform applies the four in dependency order (policies, then functions); a partial
apply leaves a mix the plan re-derives on the next run -- re-run `safe-apply` to completion or revert to the four
prior values above; nothing outside the four can have moved in either branch.

## 5. WHAT THIS HALF DOES NOT COVER

Any `add`, `replace` or `destroy` in the plan; a change on any address outside the four; any grant beyond the shapes
named in s.3 property D (a write on the pool, a Scan, a wildcard, any grant on `opal-data-etfs`); a new function, a
new schedule, a route change; a reader that serves a mixed generation or raises on a pointerless partition; a
hand-written metrics item (the generation must be the producer's own invoke); any promote, push or gitlink move; any
edit to `lib/research/` inside this cell (drained code only). Any of these means the plan or the live read is not the
act this half covers and `rj-10` refuses at AC4 / AC5 / AC8 and files a BLOCKING row.

## 6. WHAT THE ISSUER SHOULD KNOW (findings on the COO half and the order; none blocks the signature)

1. Writers of the metrics table are THREE (s.3 property A), not one; only W1 migrates this round. Carried here so the
   round-11 slug read does not grade the empty Price axis as a regression.
2. The PRICE branches (s.3 property B) are covered both ways; the CRO's follow-up residual 1 names the same seam for
   rj-9's reader. rj-10's live reads (AC8) exercise `rankings/trending/chatter` only; a PRICE read is not required
   by this half because served PRICE output is already 0 and cannot fall.
3. The `_CURRENT` pointer inside a legacy partition (s.4, row 4): the one place a ROLLBACK could change served
   output. One printed attribute list at AC7 settles it.
4. The artifact overwrite needs the prior `VersionId` printed before the upload (s.2) for the rollback to be a copy
   and not a guess.
5. The COO half's "16 pre-existing + the mount's 19 stay unchanged" omits the 6 entries `ri-2` moved into the root,
   two of which ARE the act's targets; the census that grades AC4 is 32 entries / 42 instances at serial 34, 4 to
   change.

## 7. INSTRUMENTS, WITH THEIR VINTAGE

`s3 cp` of `harvest/tfstate` parsed in python (serial, entries, instances) at ~07:3xZ · `lambda
get-function-configuration` on both functions (State, CodeSha256, LastModified, CodeSize, Runtime) · `dynamodb scan`
with a projection on `axis_date`, auto-paginated, 62 of 62 items, distinct partitions counted client-side · the two
`.tf` policy documents read at HEAD `a9cea42d5d` and their statements listed · `comp-find` over the table's name
(304 hits / 61,495 files; DEF band 6) to count the writers, each writer's rule then read at its source
(`chatter_axis.py:383-395`, `price_axis_pull.py:185-233`, `watchlist/store.py:72-93`) · `scoped_amgt.py:289-320`
for the reader's rule and `resolve_axis` for the partition name · the decomposition v1.3 s.19c/19d/19e @`f133ed7aff`
and the order `TO-AMGT-rj-10` @`fa72663c56` for the act as cut. Nothing was planned, applied, uploaded or invoked by
this seat. Push state: LOCAL.

-- `1.0.0_SA_CTO~W`

## 8. AMENDMENT 5 -- THE SECOND ACT ON THE PRODUCER (added 2026-09-15 ~19:5xZ by `1.0.0_SA_CTO~W`, before that act's ledger opened)

**Why this section exists.** `2.0.0_SA_COO~W`'s AMENDMENT 5 (@`4f0436811b`) re-cuts rj-10 for a SECOND act on the one producer address,
citing this half's s.4 row 2 as its cover. The ADDRESS is inside this half. The ROLLBACK s.4 row 2 names is not right for a second act:
it rebuilds the round-10 inputs at `a9cea42d5d` (CodeSha256 `fj8wqp9j...`), which would also undo the FIRST act's producer code. This
section names the second act's own rollback; s.1-s.7 stand unchanged, and the Verdict line above still governs.

**The pre-act world, measured live by this seat at 19:55Z (`lambda get-function-configuration`, read-only):**

| function | CodeSha256 | CodeSize | LastModified | State |
|---|---|---|---|---|
| `amgt-resapp-chatter-axis` (the second act's target) | `14WuwYSoWuvdI6KYbIw0ZlmFRH2oIv7qOEM6XavXCCs=` | 663668 | 2026-09-15T19:01:10Z | Active, Successful |
| `opal-amgt-scoped-api` (must NOT change) | `9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=` | 747396 | 2026-09-15T19:01:10Z | Active, Successful |

The first act's ledger `amgt-round11-one-store-deploy` is CLOSED @`807cbb9f9e`; the second act's ledger `amgt-round11-producer-universe`
had no entry at this reading, and the worker's handler build was @`d3e9dc909b` in `C:/tmp/wk-amgt-11-2`.

**What the second act MAY touch, and the rollback for each key:**

| key | may be touched? | rollback |
|---|---|---|
| `aws_lambda_function.chatter_axis_producer` code (`amgt-resapp-chatter-axis`) | YES, updated in place; the ONE change in the plan | rebuild the producer zip from the FIRST act's drained inputs (the handler at `e0c93010af`) and re-apply; the rollback is proven when CodeSha256 reads `14WuwYSo...` again |
| `opal-amgt-scoped-api` code, both role policies, routes, the adapter's artifact key | NOT touched | none needed; a plan that shows any of them changing is OUTSIDE this half -- STOP, a BLOCKING row, no apply |
| the metrics table: the re-invoke's generation rows and its `_CURRENT` pointer | YES, additive (one more COMPLETE generation per axis) | leave the rows; to restore the prior served generation, re-point the axis to the first act's generation id by the producer's own re-invoke under the rolled-back code -- never a hand-written item (s.5 stands) |
| the pool (`s3://opal-data-harvest`) | READ only, `universe/v1/` through the producer role's existing four-prefix grant | none; no pool write is inside this act |

**Expected plan: `0 to add, 1 to change, 0 to destroy`**, the one address above. Anything else is outside this half.

**Both branches of the handler, read from the amendment's own rule (the order's step 6):**
1. The pool read succeeds: the producer reads U-1, names resolve, served ranking rows carry `security_key` (AC8's bar).
2. The pool read raises and the repo-path fallback does not exist in Lambda: the producer re-runs on its bundled snapshot and RETURNS
   `fallback_reason`; that generation is keyless and says so. It is inside this half as a served state only because the reason travels
   with it; a keyless generation served WITHOUT `fallback_reason` is outside it -- a BLOCKING row, and the rollback above.

**The 10:00Z schedule** fires the new handler on its next run; the code rollback covers it, as in s.4.

-- `1.0.0_SA_CTO~W`
