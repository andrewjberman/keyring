# NFRA_OPLGTW task order -- `OG-sk-1` -- READ-ONLY CENSUS: every gateway code path, contract key, catalog entry and IAM statement that builds or grants a Schwab key or prefix from the master (round 47; the Schwab 0840 move to `schwab/49financial/`, Andrew-direct ~17:0xZ; the CTO's ruling of 2026-10-20 20:18Z: the gateway edit ships as a DUAL READ in its own small release before the cutover window 2026-10-21 12:00-20:00Z)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sk-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sk-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~177</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- reads Terraform files as text; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the census supports the CTO's ruling (ferry 2026-10-20 20:18Z, "ship the gateway edit as a DUAL READ ... in a 2026-10-21 07:00-11:30Z slot") and the owner assignment of his ferry of 17:13Z.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sk-1` (decomposition addendum R3-T.124, amendment A14, round 47, workstream ENRICH-R47-L)

WHY. Andrew-direct (via the laptop MSTR and the laptop CTO, RELAYED to this seat, not measured by it): Schwab master `08403355` moves from `schwab/08403355/{bronze,silver,meta,_ops}/` to the firm folder in one cutover. Silver goes to `s3://opal-data-assets/schwab/49financial/silver/<table>/date=YYYY-MM-DD/08403355.parquet` (replacing `data.parquet`; 18 tables); meta and `_ops` become a STATE tier in a different bucket, `s3://opal-data-49financial/schwab/49financial/state/{complete,conversions,pulls,backfill_status,daily_pull}/date=D/08403355.<name>`; rolling objects (`08403355.last_run.json`, `08403355.backfill-status.json`) take the UTC date of the write and readers take the NEWEST partition at or before today. `08242234` and `08335338` DO NOT move: they stay at `schwab/<master>/...`. The gateway must read the new form FIRST and the old form second (dual read), fenced BY FILE NAME (`<master>.parquet`, `<master>.<name>`), never by the folder alone. To cut that edit with an exact file list, this seat needs the census first.

DO (read-only; you write ONLY `W/SK_CENSUS.json`, and `W/` scratch files you name in your report):
1. Walk `infra/aws/ec2/opal-gateway/` (app/, deploy/, runbooks/, tests/, and any other folder holding `.py`, `.json`, `.yaml`, `.yml`, `.md`, `.sh` or `.tf`) and `infra/aws/terraform/opal-gateway/*.tf`, and the second contract copy `org/standards/NFRA_OPLGTW_CONTRACT.json`. Start from these and do not stop at them: `app/integrations/schwab/{catalog,query,export,integration,aws_roles}.py`, `app/client_adapter_schwab.py`, `app/data_entitlement.py` (`_master_accounts` reads the newest `dim_position` snapshot), `app/family_depth.py`, `app/download_routes.py`, `app/schwab_audit.py`, `app/refs/DATA_CATALOG.yaml` (144 lines name `08403355`), `deploy/NFRA_OPLGTW_CONTRACT.json` (the `data_prefixes` and `completion_prefixes` of `08403355`), `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` and `family_depth_read_iam.tf`. Use the Grep and Glob tools; `# rail-checked:` is not available to you, so do not use recursive grep in Bash.
2. For EVERY file holding the regex `schwab/|08403355|completion_prefixes|data_prefixes`, write at least one entry: `{"file": <repo-relative path>, "line": <int, the line that builds or names the key/prefix/grant>, "kind": "silver_key" | "state_key" | "bronze_key" | "prefix_const" | "iam" | "contract" | "catalog" | "test" | "doc" | "other", "master_dependent": <bool: the text changes with the master>, "edit": "DUAL_READ" (reads the old and new form) | "NEW_PATH_ONLY" (names only the new form, e.g. the IAM grant on the new bucket, the contract entry for the new prefix) | "NONE", "reason": "<one sentence>"}`. A file may carry several entries; cite the lines that matter (the key builders, the listing calls, the contract keys, each IAM statement naming Schwab).
3. `reader_iam` = `{"tf_file": "infra/aws/terraform/opal-gateway/schwab_reader_iam.tf", "statements_naming_schwab": <int, the count of lines in that file matching the word schwab, case-insensitive>, "role_ref": "<the Terraform address of the gateway reader role, NOT an ARN or an account id>", "bucket_grants": ["<bucket names the role reads today, from the file>"], "needs_new_bucket": <bool: `opal-data-49financial` is absent today>}`.
4. `fence_points` = at least TWO places where a listing by prefix is turned into a per-master set (the place a folder shared by masters would leak one master's files to another's grant): `{"file", "line", "what": "<one sentence>"}`.
5. `scanned` = `{"gateway_files": <int, the number of files you walked under infra/aws/ec2/opal-gateway/>, "tf_files": <int>, "contract_copies": 2}`. Counts only; no account number, tid, oid, e-mail, ARN or account id anywhere in the file.
6. Write the file as `{"body": {"scanned": ..., "entries": [...], "reader_iam": {...}, "fence_points": [...], "dual_read_notes": ["<up to 8 sentences: for each distinct read path (account list, files list, describe, query, family_depth backfill status, completion check, catalog), how a dual read (new first, then old) would be shaped there, and any path where it CANNOT be a simple fallback>"]}}`.

## 2. BOUNDS

- READ-ONLY: write only `W/` and, if a row is needed, the channel. No product file, no test, no Terraform file, no contract edit, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~177/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W177-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sk-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)independent sweep: \d+ files swept under the gateway folder, \d+ hold a Schwab prefix token; census names \d+ files in \d+ entries.*hit files missing from the census: 0 \(want 0\).*contract_copies 2 \(want 2\); every entry carries kind, line, master_dependent, edit and a reason: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sk-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entry citations: (\d+) of \1 cited lines exist and hold a Schwab token \(want all\): ok.*reader IAM \.tf \S+ exists True; statements_naming_schwab (\d+) equals the count of schwab lines read here \2: ok.*fence points: [2-9]\d* listed \(want 2 or more\), each citation true and described: ok.*contract entry in the deploy copy True and in the standards copy True; an iam entry True: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the census covers every file an independent sweep finds. `AC2`: the cited lines are true (read by the check, not taken from the census) and the census names what the dual-read cell needs: the reader IAM file, two or more fence points, the two contract copies.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sk-1.round-47-census-of-every-gateway-path-that-builds-a-schwab-key-from-the-master.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-sk-1.round-47-census-of-every-gateway-path-that-builds-a-schwab-key-from-the-master.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-L, amendment A14 of R3-T.124. The census is the first of two cells: the second (the DUAL READ build, `OG-sk-2`) is cut from this census's file list the moment it is graded, because `<paths>` is a permission list and must name every file the build writes. The release is its own small gateway release under its own signed pair, in the CTO's slot 2026-10-21 07:00Z-11:30Z after batch16 closes, live before the cutover window 12:00Z; the IAM grant on `opal-data-49financial` (scoped as the CTO's 17:49Z ferry: GetObject on `state/*/date=*/08403355.*` only, prefix-conditioned ListBucket, no write) is the named widening.
- The layout facts above are RELAYED (the laptop CTO, COO~SB msgs 109948, 109949, 109971, 110001; PRD v1.0 C-TIERS); this seat measured none of them. The worker is told to cite what the gateway code says, not what the relay says.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (no census). Arm: a scratch census built from the same sweep (56 entries) read `AC1` PASS and `AC2` PASS (with a deliberately wrong cited line `AC2` read NOT OK, the negative control), then was deleted.

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-L</workstream>
<slot>~177</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
