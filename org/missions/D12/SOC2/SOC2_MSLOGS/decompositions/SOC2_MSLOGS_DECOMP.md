# SOC2_MSLOGS decomposition -- ROUND 1 (2026-10-16, issuer 2.0.0_SA_COO~S1)

Cut on `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` v0.2 @5df576eada (ADMITTED: `python .tools/prd-signoff.py status SOC2_MSLOGS`),
and on the CTO's round-1 scope (msg 6869): the thread is the switch to raw (every account, the sign-in feed, the new `audit_records` table, the 7
days re-fetched, `audit_events` frozen), the `timeline` read, silver over `audit_records`, and Andrew's FWD-1 read of one real account's window
through the door. Nothing else of the PRD is in round 1 (FWD-2..9 are later rounds; scope is capped at FWD-9).

The system already runs: the Entra application, the secrets, the hourly collector, the door with two aliases, the bucket and key, the MFA Denies
(built under the closed project TCKT_MTADTA, passed to this project unchanged: Andrew-direct 2026-10-16 ~16:2xZ, "i dont care abt tckt metadata
anymore that project is closed"; record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`).
Round 1 changes that system in place; it builds no second one (Andrew-direct: no shadow pipeline).

**Andrew-direct words carried into every face that touches them (verbatim):**
- "the premise is if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was, its really about disaster recovery/remediation."
- "everything should be in the trino audit bucket ... the premise is not for workflows, its for identifying common patterns and establishing if a suspicious one appears. Silver is just formatted bronze in parquet for query, gold is effectively pattern baselines."
- "We should scrub all ticket center frameworks from this schema."
- "It should have a globgrph iam group that can read/write/do ops in there, and if we want to know things about it, we drive/query that lambda."

## The rectangle (round 1)

| cell | hop / item | surfaces | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `SM-c-1` | COLLECT, the switch to raw: every account, no filter, four feeds, bronze byte-for-byte into `audit_records`, a raw-era cursor, already-stored is not a gap, a bounded `recollect` window, derive over two days with a budget; the four-feed subscription script; the collector package scrubbed of the Ticket Center | collector package, collector handler and build, subscription script and its test | FWD-1, FWD-9 | NOT-EVALUATED | dell1 | LOCAL | worker | -- (builds to the COLLECTOR CONTRACT v3 and the DOOR CONTRACT v3 below) |
| `SM-a-1` | DOOR: write-once raw bronze keys, `audit_events` frozen, `timeline`, `recollect`, `get_day` removed, derive over two days, the door may invoke the collector | door handler and its tests, `access.tf` | FWD-1, FWD-6, FWD-8 | NOT-EVALUATED | dell1 | WORLD (path floor: terraform) | worker | -- (builds to the SILVER CONTRACT v3) |
| `SM-s-1` | SILVER: `build(records, only_date)` over raw records with typed common columns and the full record in `raw_json`; the `timeline` reader script; the eight-account read scripts deleted | silver builder and its test, the silver scripts | FWD-1 | NOT-EVALUATED | dell1 | LOCAL | worker | -- |
| `SM-g-1` | HOME: the registry row `m365-metadata` owned by D12, the R20 ledger entry X18 retired, targets regenerated | `infra/logic/registry/systems.json`, `infra/logic/06_CONFORMANCE_LEDGER.md`, the generated targets | FWD-1 (the address `audit_records` must resolve) | NOT-EVALUATED | dell1 | LOCAL | worker-light | -- |
| `SM-x-1` | SCRUB: the Ticket Center name out of the Terraform headers, the app registration script, the README and the RUNBOOK; behaviour unchanged | `main.tf`, `identity.tf`, `collector.tf` (comments and two strings), `register_app.py`, README, RUNBOOK | (cosmetic; Andrew's "scrub all ticket center frameworks") | NOT-EVALUATED | dell1 | LOCAL | worker-light | -- |
| `SM-r-1` | RELEASE: build the two zips, one `safe-apply` updating the collector and the door in place under a ledger entry, start the sign-in subscription, verify the switch live, Andrew's FWD-1 read | the live account and tenant | FWD-1, FWD-8 | NOT-EVALUATED | dell1 | WORLD | seat (`0.7.0_AE_CloudOps~SOC21`) | SM-c-1, SM-a-1, SM-s-1, SM-g-1, SM-x-1 (all merged); Andrew's FWD-1 read |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains (M = 5; fan-out 5 of 5, cap 8).**
- A = SM-c-1 -> SM-r-1 (slot ~1).
- B = SM-a-1 -> SM-r-1 (slot ~2).
- C = SM-s-1 -> SM-r-1 (slot ~3).
- D = SM-g-1 (slot ~4). No edge to the release by file; the release applies the merged tree, so the merge precedes it.
- E = SM-x-1 (slot ~5). Same.
- The joins into SM-r-1 are edges by observed completion (the release applies the merged tree), not file contention. The five worker write sets are disjoint.

**Write sets (disjoint).**
- SM-c-1: `data/m365_metadata/scripts/collector/{raw_records,collect,coverage_record,source_client,access_client}.py` (raw_records.py is new), `collector/filter.py`
  (deleted), `data/m365_metadata/scripts/population.json` (deleted), `data/m365_metadata/scripts/app/start_subscriptions.py`,
  `data/m365_metadata/scripts/tests/{test_collector.py,test_app.py}`, `infra/aws/lambda/m365-metadata-collector/{handler.py,build.sh}`.
- SM-a-1: `infra/aws/lambda/globgrph-trino-access/{handler.py,tests/test_handler.py}`, `infra/aws/terraform/trino/access.tf`.
- SM-s-1: `infra/aws/lambda/globgrph-trino-access/{silver_builder.py,tests/test_silver_builder.py}`,
  `data/m365_metadata/scripts/silver/read_timeline.py` (new), `silver/{read_day,first_content}.py` (deleted),
  `data/m365_metadata/scripts/tests/{test_read_timeline.py (new),test_read_day.py (deleted),test_first_content.py (deleted)}`.
- SM-g-1: `infra/logic/registry/systems.json`, `infra/logic/06_CONFORMANCE_LEDGER.md`, the sixteen non-portal generated targets (listed on the order).
- SM-x-1: `infra/aws/terraform/trino/{main,identity,collector}.tf`, `data/m365_metadata/scripts/app/register_app.py`, `data/m365_metadata/README.md`,
  `data/m365_metadata/scripts/app/RUNBOOK.md`.
- SM-r-1: the live account and tenant, `org/critical_paths/` for the ledger, and `infra/aws/terraform/trino/layer.auto.tfvars` if absent (the public layer ARN).
- Hookups at the merge: none expected.

**Rulings by the issuer.**
1. **The existing system is changed in place.** Same Lambdas, same bucket, same key, same group, same Deny policies. The Terraform change is small:
   the door role may invoke the collector, and the door gets `COLLECTOR_FUNCTION`. The two function zips change. No resource is added to the account.
2. **Bronze `audit_records` = one object per blob.** Key `m365-metadata/trino/bronze/audit_records/date=<Eastern yyyymmdd of the blob's contentCreated>/<contentId>.json.gz`;
   the body is `gzip(raw bytes exactly as the Management API served them, mtime=0)`, so gunzip returns the served bytes. The contentId (measured 2026-10-16 on the live
   feed) has the shape `<23 digits>$<23 digits>$audit_<kind>$Audit_<Kind>$<tail>`; the naming builder accepts it as an object name (measured). The collector parses the
   body only to count records.
3. **Write-once.** The door refuses a `put` to an existing `audit_records` key with `{"ok": false, "already_stored": true}`; the collector counts that as stored
   (already), never a gap, never a failure. A re-fetch therefore cannot change a stored byte.
4. **Era switch.** A cursor without `"era": "raw"` (the whole existing one) is a cold start: the collector re-lists and re-fetches the 7 days (the old table is
   reduced, so the raw copy cannot come from it). Coverage records carry `era`. `audit_events` is read-only from the switch (no door `put` to it);
   its objects and its silver stay as history.
5. **Derive.** After puts, the collector calls `derive_silver(d)` for every Eastern day `d` that received a bronze object and for `d-1` (a blob's records may
   straddle midnight into the next Eastern day). The door builds silver for `d` from `audit_records` partitions `d` and `d+1`, keeping records whose own Eastern
   CreationTime date is `d`. A fire out of derive time carries `derive_pending` in the cursor and finishes next fire. The reduced-era silver for those dates is
   overwritten (the row set is a superset: all accounts).
6. **`recollect`.** A member asks the door for a window inside 7 days; the door asynchronously invokes the collector with `{"recollect": {"start","end"}}`; the
   collector re-fetches that window raw into `audit_records` (already-stored counts as success), writes coverage records marked `recollect`, and does NOT touch the
   cursor. The member never supplies bytes. Not in round 1: `rederive`, `exposure`, `session_span`, `persistence`, `baseline`, `outside_baseline`, gold baselines.
7. **Round 1's read is `timeline`**, over silver, for any account in the tenant (C-POPULATION is every account), a window of up to 31 days, at most 5000 rows with a
   `truncated` flag, rows in time order. `get_day` and the eight-account list are removed everywhere.
8. **The sign-in feed.** `Audit.AzureActiveDirectory` is subscribed with the existing application credential at release (SM-r-1). If the vendor refuses for a missing
   permission, the refusal is reported verbatim and the consent is Andrew's act (carded then), never an inference now.
9. **The release is one apply** of the `trino` root: only in-place updates (two functions' code, the door role policy, the door environment, and the Project tag and key
   description strings that SM-x-1 re-words). The CloudOps seat reads the plan and refuses any create, destroy or replace.
10. **Wait.** After the sign-in subscription starts, its first content can take up to 12 hours (vendor). That wait is essential and qualified on FWD-1's sign-in half; the
    other three feeds already carry content, so Andrew's FWD-1 read does not wait on it.

**THE CONTRACTS this round touches (fixed here).**

*COLLECTOR CONTRACT v3.* Package `data/m365_metadata/scripts/collector/` (flat in the zip). `raw_records.CONTENT_TYPES == ["Audit.Exchange","Audit.SharePoint","Audit.General","Audit.AzureActiveDirectory"]`;
`raw_records.parse_blob(raw_bytes) -> list`. `source.list_content(ct, start, end) -> [{"id","created"}]`; `source.fetch_raw(ct, blob_id) -> bytes` (the served bytes).
`collect.run_once(source, access, config, now, cursor=None, clock=None, budget_seconds=None, max_workers=1, window=None) -> dict` with keys `fetched`, `already_stored`,
`failed`, `bronze_objects`, `cursor`, `complete`; `window=(start_iso, end_iso)` selects recollect mode. `collect.bronze_key(day, blob_id)`; `collect.CURSOR_KEY`. Cursor
`{"era":"raw","last_end","seen":{ct:{id:created}},"derive_pending":[iso dates]}`. `access.put(dataset, key, body) -> dict` (never raises on a refusal reply),
`access.get_state(key)`, `access.derive_silver(date) -> {"ok","rows"}`. `handler.parse_recollect(event, now) -> (start, end)` raises `ValueError` outside the rules
(strings, end after start, start not older than 7 days, span at most 7 days). The coverage record per day and content type: `listed`, `fetched`, `already_stored`, `events`, `gap`,
`status`, `era`; the document carries `recollect: true|false`. The collector reads no population file, no subject key and no office address list.

*DOOR CONTRACT v3.* `handle(event, context=None, s3=None, log=print, silver_reader=None, silver_builder=None, lambda_client=None, now=None) -> dict`; `key_ok(dataset, key)`.
Aliases and gating as v2. Ops: collector alias `put`, `derive_silver`, `get_state` (cursor key alone); member alias `timeline`, `recollect`, `get_state`, `list_state`,
`derive_silver`. `timeline {account,start,end}` -> `{"ok":true,"rows":[{"time","feed","operation","result_status","client_ip","item_name","user_id","record_id"}],"truncated":bool}`,
the reader behind it `silver_reader.timeline_rows(s3, bucket, silver_prefix, account, start, end) -> [row dicts]`. Bronze key grammar (full match, prefix
`m365-metadata/trino/`): `bronze/audit_records/date=\d{8}/<id chars>.json.gz` where the id is `[0-9]{10,30}\$[0-9]{10,30}\$audit_[a-z]+\$Audit_[A-Za-z]+\$[A-Za-z0-9]+`; no other bronze
key is admitted for a put. Silver, state and coverage grammars as v2. Environment `BUCKET`, `COLLECTOR_FUNCTION`.

*SILVER CONTRACT v3.* `silver_builder.COLUMNS` = record_id, creation_time, date, feed, record_type, operation, result_status, user_id, user_type, client_ip, object_id, site_url,
item_name, mailbox_owner, organization_id, raw_json; `build(records, only_date=None) -> parquet bytes`; `partition_date(iso)`. `records` are the raw Management API record dicts.
`read_timeline.py`: `fetch(invoker, account, start, end)`, `render(reply)`, real invoker with `Qualifier="member"`.

**The cards at Andrew (his acts; the issuer cards each when its step is reached).**
1. His FWD-1 live read: he names one account and a window and reads the timeline through his MFA session (the RUNBOOK step).
2. Any Entra consent the sign-in feed needs, only if the vendor refuses without one.

**Not in round 1:** FWD-2 baselines, FWD-3 and FWD-4 drills, FWD-5, FWD-6 analyst reads beyond `timeline`, FWD-7, retention, employee notice (a fact, not a gate), any extra op of C-READS.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the CTO's round-1 thread (msg 6869: switch to raw; the sign-in feed; `audit_records`; the 7-day re-fetch; `audit_events` frozen;
  the `timeline` read; silver over raw; Andrew's read) plus the PRD v0.2 housekeeping (C-HOMES; Andrew's scrub). By subtraction: the switch = SM-c-1 (collector side) and
  SM-a-1 (door side); the sign-in feed = SM-c-1 (script) and SM-r-1 (start); `audit_records` = SM-c-1, SM-a-1; 7-day re-fetch = SM-c-1 (cold start) then SM-r-1 (observed);
  `audit_events` frozen = SM-a-1; `timeline` = SM-a-1 (op) and SM-s-1 (silver and the reader); C-HOMES = SM-g-1; the scrub = SM-x-1 plus each cell scrubbing the files it owns;
  Andrew's read = SM-r-1. Remainder: none. Files in the old system not named by any cell and still carrying behaviour: `source_client.py` (SM-c-1), `silver/first_content.py`
  (SM-s-1, deleted).
- **Same grain.** Workers build in the repository; the seat releases to the account.
- **Intent coherence.** `c` collect, `a` door, `s` silver, `g` registry, `x` scrub, `r` release.
- **State coherence.** The five workers apply nothing and call nothing live. Only SM-r-1 touches the account and the tenant.

## Battery (round 1)

- `comp-schedule`: RUN at SM-r-1 (the hourly rule read back; fires since the switch clean: `s1_check_r1.py switch`). BLIND: a fire proves no new content landed.
- `comp-iam`: RUN at the release (`s1_check_r1.py applied` reads the door role policy and both alias Denies live). BLIND to a principal this project did not name.
- `comp-adversary`: DECLARED-NOT-APPLICABLE for the workers; findings inlined where they touch a cell: the CVO's two negative arms for the access cell (a second write to an
  existing bronze key is refused; a recollect of a stored window reads already-stored, not a gap) are criteria of SM-a-1 (`ops`, `bronze`) and SM-c-1 (`recollect`).
