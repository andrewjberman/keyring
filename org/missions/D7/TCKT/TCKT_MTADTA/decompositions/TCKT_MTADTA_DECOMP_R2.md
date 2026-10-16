# TCKT_MTADTA decomposition -- ROUND 2 (2026-10-16, issuer 2.0.0_SA_COO~S1)

Cut on the CTO's round-1 analysis `org/missions/D7/TCKT/TCKT_MTADTA/ledger/ROUND_ANALYSIS.round1.md` @6b5ef41fc9 (msg 6588), on PRD v0.4
@2614b497ed (ADMITTED; v0.3 @5f1437308a settled rows D1-S2, D1-S4, D1-S5, and msg 6589's "yes" widened the collector alias to three
operations). The CVO's slug: `surprise-channel/remediations/REMEDIATION_v1.md` @0182d243c8 (6 rows). Round 1 (`TCKT_MTADTA_DECOMP.md`) is
frozen and closed.

**Round 2 is the thread going live.** Its product is FWD-1 read by Andrew on real data. The round has two halves: a REPAIR half that three
workers build in parallel and the issuer merges (the door, the collector, the first-content read), and a RELEASE half that a CloudOps seat
runs on dell1 under a change-management entry once the repairs are merged (the apply, then the identity and the scheduled fires), with
Andrew's consent in the middle. Round 1 applied nothing; this round applies the `trino` root once.

**Andrew-direct words carried into every face that touches them (verbatim; records cited in the PRD header):**
- "yes, only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda" (06:2xZ).
- "all other domains/accounts should be dropped at the outset and not stored" (05:4xZ).
- "its a product folder so follows product rules"; "opal-data-trino" (04:0xZ).

## The rectangle (round 2)

| cell | hop / item | surfaces | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|---|
| `MD-x-1` | REPAIR, the door: invoked-alias gating (collector alias: put, derive_silver, cursor read; member alias: reads, never a put), a key allowlist (no person or file name in a key), `list_state`, aliases and one principal each in Terraform, `s3:ListBucket` out of the Deny | access.tf, door handler | FWD-1, FWD-6, FWD-8 | NOT-EVALUATED | dell1 | WORLD | worker | -- |
| `MD-x-2` | REPAIR, the collector: coverage per fire, counts by each blob's own day (content time from the listing), the cursor trimmed by age, the id-only actor counter, `derive_silver` after bronze, the alias client, builder-equal keys, `collector.tf` on direct references and the alias | collector package, collector.tf | FWD-1, FWD-7, FWD-9 | NOT-EVALUATED | dell1 | WORLD | worker | -- |
| `MD-x-3` | the first-content read: one script that prints counts only (volume per person, event types, the id-only actor count) for a day, through the door | read client | FWD-1 | NOT-EVALUATED | dell1 | LOCAL | worker | -- |
| `MD-r-1` | RELEASE, the apply: build the two zips, one `safe-apply` of the `trino` root under a change-management entry, then FWD-8's first half exercised live (an admin `GetObject`, a non-member invoke, the collector role's grants) and a plan that exits 0 after the policy lands | the live account | FWD-8, FWD-1 | NOT-EVALUATED | dell1 | WORLD | seat (`0.7.0_AE_CloudOps~TM1`) | MD-x-1, MD-x-2 (merged); Andrew's word on who joins the group |
| `MD-r-2` | RELEASE, the identity and the fires: Andrew's consent, the two secret values, the office egress addresses where the estate holds them, the three subscriptions, two scheduled fires; Andrew's live read of FWD-1 | the live tenant | FWD-1, FWD-7, FWD-9 | NOT-EVALUATED | dell1 | WORLD | seat (`0.7.0_AE_CloudOps~TM1`) | MD-r-1; Andrew's consent |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

**Chains (M = 3; fan-out 3 of 3, cap 8).**
- A = MD-x-1 -> MD-r-1 -> MD-r-2 (slot ~1 serves MD-x-1; the CloudOps seat serves MD-r-1 and MD-r-2 after the merge).
- B = MD-x-2 (slot ~2). It JOINS chain A at MD-r-1: the release waits for both merges, so MD-x-1 and MD-x-2 are on different chains and run in parallel.
- C = MD-x-3 (slot ~3). No edge: it builds to the door contract below.
- The join MD-x-2 -> MD-r-1 is an edge by observed completion, not file contention. The three worker write sets are disjoint.

**Write sets (disjoint).**
- MD-x-1: `infra/aws/lambda/globgrph-trino-access/handler.py`, `infra/aws/lambda/globgrph-trino-access/tests/test_handler.py`,
  `infra/aws/terraform/trino/access.tf`.
- MD-x-2: `data/m365_metadata/scripts/collector/{filter,coverage_record,collect,source_client,access_client}.py`,
  `data/m365_metadata/scripts/tests/test_collector.py`, `infra/aws/lambda/m365-metadata-collector/handler.py`,
  `infra/aws/terraform/trino/collector.tf`.
- MD-x-3: `data/m365_metadata/scripts/silver/first_content.py`, `data/m365_metadata/scripts/tests/test_first_content.py`.
- MD-r-1 and MD-r-2: the live account and `org/critical_paths/` for the ledger; repo writes only `infra/aws/terraform/trino/layer.auto.tfvars`
  (the public AWS-managed layer ARN, no secret) and the order's own records.
- Hookups at the merge: none expected.

**Rulings by the issuer.**
1. **Round 1's `access.tf`, `handler.py`, `collector.tf` are reopened** to the cells above because the CTO's v0.3/v0.4 rulings changed their
   contract. The `collector.tf` patch of round 1 (direct references) is folded into MD-x-2 and the patch file is superseded.
2. **The alias design.** One function, `publish = true`, two aliases: `collector` and `member`. The door reads `context.invoked_function_arn`.
   The group policy grants invoke on the `member` alias ARN alone; the collector role's policy grants invoke on the `collector` alias ARN alone;
   a Lambda resource permission admits the collector role on its alias. (A resource policy cannot name an IAM group, so the group's reach is its
   identity policy; PRD C-ACCESS v0.4 says the same.) An unqualified invoke, an unknown alias or no context is refused on every op.
3. **The key allowlist is the D1-S4 enforcement.** The door admits a key only if it matches the builder's grammar for its dataset (a date
   partition and a fixed object name), so no person, address or file name can ever sit in a key. The coverage object is
   `coverage_<fireISO compact>.json`; the cursor is the one `cursor.json`.
4. **Door operations.** `collector` alias: `put` (bronze, state, gold only), `derive_silver` (answers `{ok, rows}` and nothing else),
   `get_state` on the cursor key alone. `member` alias: `get_day`, `get_state` (state and coverage keys), `list_state` (state and coverage
   prefixes only), `derive_silver`. Every other op, on every alias, is refused.
5. **Release sequence, one apply.** Zips built, layer ARN in `layer.auto.tfvars`, `terraform init`, one `safe-apply`. The CloudOps seat's
   identity is the box's `cloudops-dell1-agent-user` (measured), a NON-member of the group by design, which is what makes the refusal checks
   meaningful. Group membership is Andrew's word (card below), not the seat's act.
6. **No worker, and no seat but Andrew, ever reads stored content.** The first-content read prints counts only and runs under a group member
   (Andrew); nothing it prints is copied into the repository.
7. **The 12-hour wait is essential and qualified.** After the subscriptions start, the first content may take up to 12 hours (the vendor's
   word, PRD cell candidate 3). MD-r-2's mechanical criteria need only two scheduled fires (hourly, empty or not); Andrew's FWD-1 read waits
   on content for one of the eight and is recorded as a wait with its owner.

**THE CONTRACTS this round touches (fixed here).**
*DOOR CONTRACT v2.* `handle(event, context=None, s3=None, log=print, silver_reader=None, silver_builder=None) -> dict`; `key_ok(dataset, key)`;
`PREFIX`. Alias comes from `context.invoked_function_arn` (`...:function:<name>:<alias>`). Ops and aliases as ruling 4. `list_state` request
`{op, prefix}` answers `{ok, keys: [...]}`. Every call writes one log line (op, outcome; never a body, key or person). Key grammar (full-match,
bucket prefix `m365-metadata/trino/`): bronze `bronze/audit_events/date=YYYYMMDD/Audit.(Exchange|SharePoint|General)_YYYYMMDDTHHMMSSZ.json.gz`;
silver `silver/activity_events/date=YYYY-MM-DD/data.parquet`; state `state/subscription_cursor/current/cursor.json`; coverage
`gold/collection_coverage/date=YYYY-MM-DD/coverage_YYYYMMDDTHHMMSSZ.json`.
*COLLECTOR CONTRACT v2.* `source.list_content(content_type, start, end) -> [{"id", "created"}]` (the Management API's `contentId` and
`contentCreated`); `source.fetch(content_type, id) -> [events]`; cursor `{"last_end", "seen": {content_type: {id: created}}}` trimmed to
7 days by `created`; `coverage_record.fire_key(day, fire_iso) -> key`; `collect.bronze_key(day, content_type, fire_tag) -> key`;
`access.put`, `access.get_state(cursor key)`, `access.derive_silver(date) -> {ok, rows}`; `access_client.lambda_invoker(client, function_name,
qualifier)`; `filter.process_batch` returns `counters["dropped_id_only"]` (events whose only actor field is a GUID).

**The cards at Andrew (his acts; the issuer cards each when its step is reached).**
1. Who is in `globgrph-trino-access-group` (REC: his IAM user alone; he runs the day read and the first-content read).
2. The Entra consent: he runs `register_app.py --apply` under his delegated token (the RUNBOOK), or grants the consent at the printed URL.
3. His FWD-1 live read: he names one of the eight and a trading day and reads it.

**Not in round 2:** FWD-9 coverage reads beyond the repaired object, the FWD-8 statement, FWD-2, FWD-3, FWD-4, FWD-6 analyst questions,
FWD-5, FWD-10 (CTO's order of later rounds).

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the CTO's four round-2 items (release; FWD-8 refusals; the repair cell; first-content reads) plus the
  CVO's six remediation rows. By subtraction: item 1(a) = MD-r-1; item 1(b)-(d) = MD-r-2; item 2 = MD-r-1 (the refusals run at the apply) with the
  door's side in MD-x-1; item 3 splits by write set into MD-x-1 (door), MD-x-2 (collector); item 4 = MD-x-3 (the script) run by Andrew at the end of
  MD-r-2. Remediation rows: D1-S5 -> MD-x-1; D1-S2 -> MD-x-2 (the id-only counter); D1-S4 -> MD-x-1; D1-W3-S2 -> MD-x-1, MD-x-2 (builder-equal keys);
  D1-W3-S3 -> MD-x-2; D1-W3-S5 -> MD-x-2. Remainder: none.
- **Same grain.** Workers build; seats release. Where one item has two write sets it is two cells.
- **Intent coherence.** `x` repairs, `r` releases.
- **State coherence.** The three workers apply nothing and call nothing live. Only MD-r-1 and MD-r-2 touch the account and the tenant.

## Battery (round 2)

- `comp-schedule`: RUN at MD-r-2: the hourly rule read back and two consecutive fires (`r2_check_r2.py fires`). BLIND: a fire that lands content
  is not required by the criterion; content takes up to 12 hours.
- `comp-iam`: RUN at the apply: `comp-iam simulate` is replaced by `iam simulate-principal-policy` inside `r2_check_r1.py refusals` (the collector role:
  invoke its alias allowed, the member alias, any S3 and any KMS action not allowed). BLIND: the round-1 `comp-iam` census did not list the new roles;
  the checks read the live policies instead.
- `comp-adversary`: DECLARED-NOT-APPLICABLE for the workers. Findings inlined where they touch a cell: the CVO's remediation rows (the faces cite
  them); the issuer's own D1-S4 and D1-S5 rulings.
