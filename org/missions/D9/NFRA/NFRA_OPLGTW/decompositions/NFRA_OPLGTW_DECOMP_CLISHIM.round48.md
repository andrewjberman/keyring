# NFRA_OPLGTW -- decomposition of the CLI-SHIM workstream, round 1 (tagged round 48 for the close check; 2.0.0_SA_COO~O, 2026-10-21 ~15:3xZ)

**Scope.** PRD v3.19 FWD-23 (the MCP as an AWS-CLI shim: list, describe and query over granted folders, bounded, paged), FWD-24 (the entitlement is a bucket or a folder, per person, and nothing else), and the per-firm client grant shape (the CTO's msg 36202, row Z-S432). Ruled by the CTO (msg 36299): its own workstream, its own decomposition and its own L10, with write surfaces disjoint from round 47 (gateway CODE against round 47's grant-store RECORDS and one cut release branch). Round 47 closes at batch17 plus its open orders; this workstream closes on its own slug. The `<round>` tag of its orders is 48 so that `round-close-check.py --round 47` does not count them; its own check is `--round 48 --workstream CLISHIM-<letter>`.

**Frozen inputs read for this decomposition.** PRD v3.19 @788a27f4ee (ADMITTED); the CRO's brief `docs/briefs/mcp-cli-shim-bounded-query-brief-20261021.md`; the CTO's rulings: FWD-24 shape (msg 36300: a bucket or bucket/prefix string in `channels_allow`, `channels_deny` subtracts, deny wins), the CVO's cure at v3.19 (the shim's prefix check and the reader IAM exclude every bronze or raw prefix, proof adds a refused bronze read under a whole-bucket grant), the five sensitive column classes dropped by name (tax identifiers, mailing addresses, email addresses, phone numbers, date of birth), the typed tools stay until FWD-23 is proven.

**Findings that shape the cells (measured in the source at HEAD).**
- `app/data_entitlement.py:254` `_CHANNEL = ^[a-z][a-z0-9_]{0,63}$` is applied to `channels_allow` and `channels_deny` by `parse_person_access`; a bucket name (hyphen) or a bucket/prefix (slash) makes the whole record Malformed and the gateway fails closed for every tool of that person (row Z-S447, ARMED). OG-cs-1 fixes the reader FIRST.
- The deployed grant writer refuses an ADD to `tools_allow` or `channels_allow` without `widening_confirm: true`, and `app/admin_people_access.py` drops it (COO~MP's measure): OG-cs-5.
- The bounded engine exists (`app/integrations/schwab/engine.py`: spawned DuckDB child, 256 MiB, 30 s, closed-grammar plan, 12 objects / 64 MiB compressed, 2 jobs, HMAC cursor); it takes LOCAL source paths, so a folder read downloads the objects under the cap and runs the plan in the child.

## Cells

| cell | what | writes (under `infra/aws/ec2/opal-gateway/` unless named) | class | wave | after |
|---|---|---|---|---|---|
| `OG-cs-1` | the folder-grant decision (a pure function) and the parser that accepts a folder string in `channels_*` | `app/data_entitlement.py`, `app/folder_grant.py` (new), `tests/test_cs1_folder_grant.py` (new) | worker | 1 | none |
| `OG-cs-5` | the access POST carries an optional boolean `widening_confirm` into the writer event | `app/admin_people_access.py`, `tests/test_cs5_widening_confirm.py` (new) | worker-light | 1 | none |
| `OG-cs-2` | the shim tools as functions with explicit dependencies: `list_folder`, `describe_object`, `query_object`: admission by OG-cs-1, S3 list and footer ranged reads, the plan and cursor, the five-class column drop, all through OG-cs-3's interface | `app/folder_tools.py` (new), `tests/test_cs2_folder_tools.py` (new) | worker | 2 | OG-cs-1 and OG-cs-3 drained |
| `OG-cs-3` | the folder engine helpers (pure): the five sensitive classes dropped by name, the request mapped to the engine's closed-grammar plan, the source-size caps, a footer-only parquet describe | `app/folder_engine.py` (new), `tests/test_cs3_folder_engine.py` (new) | worker | 2 | none (cut with wave 2, built at once) |
| `OG-cs-7` | the per-firm client grant shape: `decide()` admits a `client_*` call only inside a granted (vendor, firm) pair | `app/data_entitlement.py` (after OG-cs-1 drains), `tests/test_cs7_*.py` (new) | worker | 2 | OG-cs-1 |
| `OG-cs-8` | the contract revision: the per-account, per-column and masked-reference clauses are stated superseded for folder grants; both copies stay byte-equal | `deploy/NFRA_OPLGTW_CONTRACT.json`, `org/standards/NFRA_OPLGTW_CONTRACT.json`, `tests/test_cs8_contract_supersession.py` (new) | worker-light | 2 | none (built at once) |
| `OG-cs-6` | reader IAM over the three buckets' folders excluding every bronze or raw prefix (a widening, with halves) | `infra/aws/terraform/opal-gateway/` | applier | 3 | OG-cs-2 |
| `OG-cs-9` | the release that carries the drained cells (batch18) and the registry hookups (`app/tools.py`, the catalog rows, tool counts), the issuer's hookup commit | release, ledger | applier | 3 | OG-cs-1..8, OG-cs-6 |

Hookups (a registration line in `app/tools.py`, the integration registry, the catalog entries, the tool-count pins) belong to NO cell: the issuer adds them at the merge in one commit.

## Waves and the clock

Wave 1 (OG-cs-1, OG-cs-5) is cut at once: disjoint files, no dependency. Wave 2 is cut when OG-cs-1 drains (its function is the admission the others import); wave 3 is the applier's. The CTO's target: the first release at or before 2026-10-23 06:00Z.

## Proof posture

Every code cell carries at most three mechanical criteria (the behaviour by an issuer-written probe, the footprint bound, the cell's tests and neighbours); every check is a file dry-run at the base. The cell proofs are LOCAL; the release proofs are SERVED (a driven call per group, the negative arms: a principal without the folder refused by folder name with 0 reads; a bronze read refused under a whole-bucket grant; a column of a sensitive class absent from a describe).

## Interfaces fixed between the cells (so OG-cs-2 and OG-cs-3 are written independently)

`app/folder_grant.py` (OG-cs-1): `SERVED_BUCKETS`, `is_folder_entry(entry)`, `folder_decision(is_master_admin, is_opal, rec, bucket, key) -> (allowed, reason)`.
`app/folder_engine.py` (OG-cs-3): `SENSITIVE_CLASSES`, `sensitive_class(name)`, `drop_sensitive(names) -> (kept, dropped)`, `plan_from_request(request, allowed_columns) -> QueryPlan`, `check_sources(sizes) -> None | {code, reason, suggestion}`, `describe_parquet(read_range, size) -> {columns, num_rows, row_groups}`.
`app/folder_tools.py` (OG-cs-2) imports both and the engine's `ExecutionEngine`; its three functions take every dependency (principal, person_access record, S3 client, engine) as an argument, so the registry hookup that supplies them is the issuer's.

## Disclosed deferrals (named, not hidden)

The Cottonwood Black Diamond MM/DD/YYYY date parse inside a query (FWD-23 DONE WHEN (f)) needs a date-format hint in the engine's closed grammar, an edit of `app/integrations/schwab/engine.py`; it is a later cell (`OG-cs-4`) and may slip behind the first release. The 21M-row Commonwealth file, SmartX, Eclipse and Commonwealth are deferred by the PRD. The per-firm client grant shape (OG-cs-7) and the reader IAM text (OG-cs-6) are cut after OG-cs-1 drains because their faces depend on the folder-grant function and on a measured reading of `client_core` and `schwab_reader_iam.tf`.
