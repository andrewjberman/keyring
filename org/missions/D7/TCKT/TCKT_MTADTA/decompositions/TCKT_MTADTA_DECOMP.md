# TCKT_MTADTA decomposition -- ROUND 1 (2026-10-16, issuer 2.0.0_SA_COO~S1)

Cut on the ratified PRD `org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md` v0.2 @86f3caec3a, ADMITTED (ratified-text half
3.0.0_SA_CVO @e1ad94a7e5, brief half auto: the CRO wrote the brief). Notifier msgs 6559, 6561 from 1.0.0_SA_CTO~DELL1.
Brief: `docs/briefs/tckt-mtadta-ticket-center-metadata-brief-20261016.md@4ec9c9f461`. Endpoint: FWD-1..10 @a7a7df4e6f.

**Round 1 is ONE thread, FWD-1:** Andrew reads one of the eight's real trading day through the front door. Hops, in order:
HOME (bucket, key, registry) -> DOOR (group, role, access Lambda) -> IDENTITY (app, secret, subscriptions) -> COLLECT (filter
and levers before the first write, bronze, cursor, coverage) -> SILVER and the READ (sorted parquet, one day rendered).

**Andrew-direct words carried into the faces (verbatim, records cited in the PRD header):**
- "all other domains/accounts should be dropped at the outset and not stored" (05:4xZ) -- the filter runs before the first write.
- "yes, only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda" (06:2xZ).
- "its a product folder so follows product rules"; "opal-data-trino" (04:0xZ).
- "We will have a separate project to set up the organization, for now just set it up in opal-data-trino as described" (06:0xZ).

## The rectangle (round 1)

| cell | hop / item | surfaces (PRD manifest) | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `MD-h-1` | HOME: registry rows `trino` + `m365-metadata`, targets regenerated, the R20 entry (drop at collection + the KMS key name), and the bucket + KMS key in Terraform (desired) | registry rows; R20 entry; bucket, key | FWD-1, FWD-7, FWD-8 | NOT-EVALUATED | dell1 | WORLD | worker | -- |
| `MD-a-1` | DOOR: the IAM group, the role, the one reader/writer Lambda (`put`, `get_state`, `get_day`, `derive_silver`), and the two single-principal policies on the bucket and the key | the access path | FWD-6, FWD-8 | NOT-EVALUATED | dell1 | WORLD | worker | MD-h-1 (its `access.tf` names the bucket and key resources `main.tf` declares) |
| `MD-i-1` | IDENTITY: the Entra-app registration script (one permission, app-only), the secret container in Terraform, the subscription starter; both scripts DRY-RUN by default | the app and secret; the subscriptions | FWD-1, FWD-9 | NOT-EVALUATED | dell1 | WORLD | worker | -- |
| `MD-c-1` | COLLECT: the population filter and the field levers (before the first write), the cursor, the coverage record, the hourly collector Lambda and its schedule in Terraform (desired); writes only through the door | the collector; bronze/state/coverage planes | FWD-1, FWD-7, FWD-9 | NOT-EVALUATED | dell1 | WORLD | worker | -- (builds to the DOOR CONTRACT below) |
| `MD-s-1` | SILVER and the READ: `silver_builder.py` (bronze events to sorted parquet, Eastern-date partition) and `read_day.py` (one person's day, in order, through the door) | silver plane; person_day read | FWD-1 | NOT-EVALUATED | dell1 | WORLD (the path floor of `infra/aws/lambda/`; nothing runs live) | worker | -- (builds to the BRONZE and SILVER CONTRACTS below) |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED (NOT-EVALUATED is the value before a cell's instance exists).

**Chains (M = 4, one worker each; fan-out 4 of 4, cap 8).**
- A = MD-h-1 -> MD-a-1 (slot ~1: `access.tf` consumes the bucket and key `main.tf` declares).
- B = MD-i-1 (slot ~2).
- C = MD-c-1 (slot ~3).
- D = MD-s-1 (slot ~4).
- NOT edges, by ruling: the collector -> the door (C builds to the DOOR CONTRACT with a fake access client; the seam is proved at the drain);
  the collector -> silver (D builds to the BRONZE CONTRACT); the door -> `silver_builder` (A's handler takes the reader and builder as injected
  modules; D's file is the production module). A contract is an interface fixed here, not file contention.

**Write sets (disjoint; the issuer creates every `__init__.py` and the empty `tests/` directories at the cut).**
- MD-h-1: `infra/logic/registry/scopes.json`, `infra/logic/registry/systems.json`, `infra/logic/registry/root_map.json`,
  `infra/logic/06_CONFORMANCE_LEDGER.md`, the 19 generated targets `python lib/opal_naming.py generate` writes,
  `infra/aws/terraform/trino/main.tf`.
- MD-a-1: `infra/aws/terraform/trino/access.tf`, `infra/aws/lambda/globgrph-trino-access/handler.py`,
  `infra/aws/lambda/globgrph-trino-access/build.sh`, `infra/aws/lambda/globgrph-trino-access/tests/test_handler.py`.
- MD-i-1: `data/m365_metadata/scripts/app/register_app.py`, `data/m365_metadata/scripts/app/start_subscriptions.py`,
  `data/m365_metadata/scripts/app/RUNBOOK.md`, `data/m365_metadata/scripts/tests/test_app.py`, `infra/aws/terraform/trino/identity.tf`.
- MD-c-1: `data/m365_metadata/scripts/collector/` (`filter.py`, `coverage.py`, `collect.py`, `source_client.py`, `access_client.py`),
  `data/m365_metadata/scripts/population.json`, `data/m365_metadata/scripts/tests/test_collector.py`,
  `infra/aws/lambda/m365-metadata-collector/handler.py`, `infra/aws/lambda/m365-metadata-collector/build.sh`,
  `infra/aws/terraform/trino/collector.tf`.
- MD-s-1: `infra/aws/lambda/globgrph-trino-access/silver_builder.py`, `infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py`,
  `data/m365_metadata/scripts/silver/read_day.py`, `data/m365_metadata/scripts/tests/test_read_day.py`.
- Hookups the issuer adds at the merge: a README pointer for `data/m365_metadata/`; the collector's import path in its `build.sh` if a
  report names one.

**Rulings by the issuer (inside its own decomposition).**
1. **Homes.** Terraform root `infra/aws/terraform/trino/` (the root's directory name IS the scope key `trino`, LGIC_ENFORCE DEC-6, the
   `transcripts` root's form). Source at `data/m365_metadata/scripts/` (Python package names take an underscore; the registry key stays
   `m365-metadata`). Lambda sources under `infra/aws/lambda/` beside `transcripts-pull`. Every S3 address is `lib/opal_naming.address()`
   output and every name `name()` output (rule 30).
2. **Round 1 applies nothing.** Every Terraform file is DESIRED: `fmt` clean and `validate` clean on the merged root at the drain. No
   `apply`, no Entra call, no subscription call, no S3 write, no AWS call by any worker. The release acts are listed below.
3. **The KMS key's name.** `name(..., 'key')` is refused (no builder kind). MD-h-1 follows the `transcripts` root's alias form and
   records it as a DECLARED DEPARTURE inside the one R20 entry. It edits no `NAMING_SCHEMA.json` (LGIC's owner decides a kind later).
4. **Entra object ids are NOT built in round 1.** PRD C-POPULATION resolves "against the eight UPNs and their Entra object ids read once at
   collection". Reading object ids needs a Graph permission, and C-APP allows the app ONE permission. MD-c-1 resolves across the four
   UPN fields only; `population.json` carries an `object_ids` map that stays empty. Recorded as a surprise row; an enrichment-list item.
5. **Where derivation runs.** The door "returns query results, never raw bronze objects", so bronze is read only inside the door: the
   `derive_silver` op reads one date's bronze and calls the injected builder. The collector and `read_day.py` hold no read path to bronze.
6. **The coverage record is JSON in round 1.** `gold/collection_coverage/` takes `coverage.json` (object name from the builder call); the
   parquet form arrives with the FWD-9 reads, so the collector Lambda carries no parquet library.
7. **Pre-existing target drift.** At the cut, `python lib/opal_naming.py generate` into a temp directory differs from 8 of the 19
   committed targets before any new row (measured 2026-10-16 ~06:5xZ; the `NFRA_TRNSPT` round 1 met the same). MD-h-1's regenerate therefore
   restamps those 8 for two reasons at once and reports both; the hash-pinned consumers (1 of 142 scanned) are named to their owners at the
   drain, not by the worker.
8. **Workers run the check files** (`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/`), written and dry-run at the base
   by the issuer: every build check printed REFUSED/MISSING at the base; the collector, door and silver checks were also driven GREEN
   against a throwaway reference outside the repo before the cut.

**THE THREE CONTRACTS (fixed here; each face inlines the ones it touches).**

*DOOR CONTRACT -- the Lambda `globgrph-trino-access-lambda`.* `handle(event, context=None, s3=None, log=print, silver_reader=None,
silver_builder=None) -> dict`. Every call writes one log line (op, outcome; never a body). Prefix `m365-metadata/trino/`; bucket from the
`scopes.json` row; every write is `ServerSideEncryption='aws:kms'`.
| op | request | answer |
|---|---|---|
| `put` | `{op, dataset: bronze\|silver\|state\|gold, key, body_b64}` | `{ok: true, key}`; `{ok: false, error}` when the key is outside the prefix or holds `..` |
| `get_state` | `{op, key}` (a `state/` or `gold/collection_coverage/` key only) | `{ok: true, body_b64}` or `{ok: false, error}` |
| `get_day` | `{op, person, date}` (`person` one of the eight, `date` `YYYY-MM-DD`) | `{ok: true, rows: [...]}` the person's silver rows in time order; `{ok: false}` for a non-member |
| `derive_silver` | `{op, date}` (`YYYY-MM-DD`, Eastern) | reads EVERY bronze object under `date=YYYYMMDD`, `silver_builder.build(events) -> bytes`, rewrites that one silver partition (idempotent); `{ok: true, rows: n}` |
| `get` of bronze, anything else | -- | `{ok: false, error}`; bronze is never returned |

*BRONZE CONTRACT -- one object per fire, per Eastern date, per content type.* The collector splits a fire's kept events by the
America/New_York calendar date of `creation_time`. Key `address('m365-metadata','trino','bronze','audit_events', 'date=YYYYMMDD',
object='<ContentType>_<fireISO>.json.gz')`, where `YYYYMMDD` is that Eastern date. Source `CreationTime` carries no zone and is UTC:
the collector appends `Z`. Body: gzip of JSON lines. Each line is a dict of EXACTLY these keys (a
whitelist; every other source key is dropped): `event_id, creation_time (ISO, UTC), workload, operation, record_type, result_status,
actor (a lower-cased member UPN), subject_hash (64 hex or null), participants (list of: a member UPN | "internal-other" | "external"),
site, file_id, file_name, extension, folder, client_ip_class ("office" | "remote" | "unknown")`.

*SILVER CONTRACT -- `silver_builder.build(events: list[dict]) -> bytes` and `partition_date(iso) -> "YYYY-MM-DD"`.* Parquet, one row per
event, sorted by `creation_time`; columns in this order: `event_id, creation_time, date, actor, workload, operation, record_type,
result_status, subject_hash, participants (comma-joined), site, file_id, file_name, extension, folder, client_ip_class`. `date` is the
America/New_York calendar date of `creation_time`. Key `address('m365-metadata','trino','silver','activity_events','date=YYYY-MM-DD',
object='data.parquet')`.

**Release acts after the drain (named, NOT built by any worker; each is the issuer's to route).**
1. `safe-apply` of the `trino` root by a CloudOps seat, with a change-management entry opened at the start and closed at the end
   (NEVER-2), in the order main.tf, access.tf, identity.tf, collector.tf. WORLD; CTO + COO halves.
2. The Entra app registered and the consent granted: **Andrew's act** (Cloud Application Administrator). Carded to him when `MD-i-1` drains.
3. The two secret values put into their containers (the app credential; a random subject-hash key), Opal's office egress addresses entered
   in `population.json` `office_ips` (empty until then, so every address reads `remote`; Andrew or CloudOps holds the list); the three subscriptions started (`start_subscriptions.py --apply`); first content may
   take up to 12 hours.
4. The real thread run: one of the eight, one trading day, through the door, looked at. FWD-1's EXERCISED bar waits on 1-3 and is the first
   item of the round-1 analysis if the round drains before they land. Round 1's drain-time run is the SAME code driven end to end with
   synthetic events and fake clients (no network).

**Not in round 1 (the enrichment backlog, PRD CELL CANDIDATES):** FWD-9 coverage READS and the FWD-8 compromise statement (C-RESIDUAL);
FWD-2 chains (the CVO's note: show one hand-off to a token that reads as a team exit); FWD-3 recurring workflows; FWD-4 timing; FWD-6
analyst questions (`query` op); FWD-5 candidates; FWD-10 content (on his word); Entra object-id resolution (ruling 4).

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the PRD's five round-1 CELL CANDIDATES. By subtraction: candidate 1 (rows and home) splits by
  write set into MD-h-1 (rows, R20, bucket, key) and MD-a-1's policies, which cannot precede the role; candidate 2 (access) = MD-a-1;
  candidate 3 (app, consent, subscription) = MD-i-1 for everything a worker can build, the consent and the live calls being release acts
  2-3; candidate 4 (collector) = MD-c-1; candidate 5 (silver and one readable day) = MD-s-1. Remainder: none; release acts 1-4 are
  named, not cells.
- **Same grain.** One cell per hop adapter; where one candidate has two write sets it is two cells (1 -> h and a).
- **Intent coherence.** `h` homes, `a` the door, `i` identity, `c` collection, `s` the derived read.
- **State coherence.** No cell applies, calls Microsoft, reads or writes S3, grants a principal or creates an alarm. MD-c-1 and MD-s-1
  move no served surface. Terraform written here moves nothing until release act 1.

## Battery (round 1 of a threaded project)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. Thread round; the hourly rule is DESIRED in `collector.tf` and applied at release act 1.
- `comp-iam`: RUN at the drain, not at the cut. The thread touches IAM (a group, a role, two single-principal policies). Denominator:
  `comp-iam gaps` over the merged `trino` root, printed at the drain. BLIND: the new principals do not exist, so no live read or
  `simulate` is possible before release act 1; `gaps` is necessary, not sufficient. The live proof (an admin's direct `GetObject` refused,
  a non-member's invoke refused) is FWD-8's first half and runs after the apply.
- `comp-adversary`: DECLARED-NOT-APPLICABLE. Thread round. Findings read at the cut and inlined where they touch a cell:
  - the CVO's predecessor refusal (C-POPULATION keeps excluded accounts in bronze) is closed by the drop-before-first-write rule;
  - the CVO's v0.2 note on FWD-2 (class tokens must read as a team exit) is a later-round item;
  - a population or field error cannot be repaired from bronze (PRD DECISION 1), so MD-c-1's planted-event check is the guard and
    runs against EIGHT planted cases, not one.
