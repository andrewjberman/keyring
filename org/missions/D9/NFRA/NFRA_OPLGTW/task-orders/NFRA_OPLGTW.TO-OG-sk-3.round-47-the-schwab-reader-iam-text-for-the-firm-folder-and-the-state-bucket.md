# NFRA_OPLGTW task order -- `OG-sk-3` -- the Schwab reader IAM TEXT for the 0840 move: silver by file name in the firm folder, the completion marker by file name in the new firm state bucket; TEXT ONLY, nothing applied (round 47; the CTO's conditions of 2026-10-20 17:49Z and 20:18Z)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sk-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sk-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~179</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform TEXT and a read-only record; nothing is applied, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the comp-iam tool is not run here: this order EDITS the text of the two Schwab reader role policies in `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf`; it applies nothing (apply is `~NFRA1`'s, under `safe-apply`, in the release window, under its own signed never-widen pair). The only new reach: `s3:GetObject`/`GetObjectVersion` on four silver files-by-name in the existing bucket and on ONE state object name in the NEW bucket `opal-data-49financial`, with prefix-conditioned `s3:ListBucket`; no write, no bucket-wide read.
comp-adversary: DECLARED-NOT-APPLICABLE -- the shape is the CTO's, verbatim (ferry 17:49Z): "GetObject only, on `arn:aws:s3:::opal-data-49financial/schwab/49financial/state/*/date=*/08403355.*`, with the master in the file name; ListBucket conditioned on the prefix `schwab/49financial/state/`; no bucket-wide read and no write; each master added later is one more resource line in its own ask". This order narrows it further to the ONE state object the catalog reads today (`complete`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sk-3` (decomposition addendum R3-T.124, amendment A16, round 47, workstream ENRICH-R47-N)

WHY. After the cutover the gateway's Schwab catalog reads master `08403355`'s silver from `s3://opal-data-assets/schwab/49financial/silver/<table>/date=D/08403355.parquet` and its completion marker from `s3://opal-data-49financial/schwab/49financial/state/complete/date=D/08403355.complete.json` (RELAYED layout; `OG-sk-2` is the code). The data role (`gateway-schwab-read-role`) and the catalog role (`gateway-schwab-catalog-read-role`) are fenced by `NotResource` denies over the locals of `schwab_reader_iam.tf`, so they must name the new objects or the dual read is refused at the door. Fence by FILE NAME: IAM cannot fence a folder shared by masters, so each master is its own object-name pattern, never `silver/<t>/*`.

DO, in `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` ONLY (the OLD grants stay byte-for-byte: the old form is the fallback):
1. In the `locals { ... }` block add, with EXACTLY these names (the checks evaluate them with `terraform console`):
   - `schwab_state_bucket = "opal-data-49financial"` and `schwab_state_bucket_arn = "arn:aws:s3:::${local.schwab_state_bucket}"`;
   - `schwab_firm_silver_prefixes` = the four prefixes `schwab/49financial/silver/<t>/` for `t` in `dim_position`, `dim_balance`, `dim_asset`, `dim_transaction`;
   - `schwab_firm_silver_object_arns` = `[for p in local.schwab_firm_silver_prefixes : "${local.schwab_bucket_arn}/${p}date=*/08403355.parquet"]` (the master in the FILE NAME);
   - `schwab_firm_silver_prefix_forms` = `[for p in local.schwab_firm_silver_prefixes : "${p}*"]`;
   - `schwab_state_complete_object_arns` = `["${local.schwab_state_bucket_arn}/schwab/49financial/state/complete/date=*/08403355.complete.json"]`;
   - `schwab_state_complete_prefix_form` = `["schwab/49financial/state/complete/*"]`;
   and change the three existing locals so that `schwab_data_object_arns` is `concat(<the existing for-expression>, local.schwab_firm_silver_object_arns)`, `schwab_data_prefix_forms` is `concat(<existing>, local.schwab_firm_silver_prefix_forms)`, and `schwab_catalog_object_arns` is `concat(<existing>, local.schwab_state_complete_object_arns)`. `schwab_catalog_prefix_form` stays EXACTLY as it is (it conditions listing of the OLD bucket).
2. In the CATALOG role's policy block (`aws_iam_role_policy.schwab_catalog_read_policy`) change the `NotResource` of the statement `DenyListingOtherBuckets` to the list `[local.schwab_bucket_arn, local.schwab_state_bucket_arn]` and ADD two statements for the state bucket, the Deny directly after `DenyListingOutsideCompletionPrefixes` and the Allow directly after `AllowCompletionPrefixListing`:
```
      {
        Sid       = "DenyStateListingOutsideCompletionPrefix"
        Effect    = "Deny"
        Action    = "s3:ListBucket"
        Resource  = local.schwab_state_bucket_arn
        Condition = { StringNotLike = { "s3:prefix" = local.schwab_state_complete_prefix_form } }
      },
      {
        Sid       = "AllowStateCompletionPrefixListing"
        Effect    = "Allow"
        Action    = "s3:ListBucket"
        Resource  = local.schwab_state_bucket_arn
        Condition = { StringLike = { "s3:prefix" = local.schwab_state_complete_prefix_form } }
      },
```
   The DATA role's policy block is NOT edited (its statements are built from the locals, so the four firm silver ARNs and listing forms flow into it). Add a comment block above the new locals naming the cutover and the file-name fence. Run `terraform fmt` on the file so `terraform fmt -check` accepts it. Do NOT run `terraform init`, `plan` or `apply` in `infra/aws/terraform/opal-gateway/`.
3. The bucket-side fact (read-only): find the Terraform that creates the bucket `opal-data-49financial` and any bucket policy on it (use Grep over `infra/aws/terraform/shared-infra/` first: `s3-49financial.tf` and `s3-lgic-firm-buckets.tf` name it) and write `W/SK3_BUCKET_POLICY.json` = `{"body": {"bucket": "opal-data-49financial", "owner_file": "<repo-relative .tf>", "policy_file": "<repo-relative .tf holding a bucket policy, or null when none is declared>", "policy_denies_unlisted_principals": <bool or null when there is no policy>, "names_gateway_catalog_role": <bool or null>, "identity_policy_alone_suffices": <bool>, "needs_change": <bool>, "reason": "<one or two sentences>"}}`. `needs_change` is true exactly when a bucket policy denies principals it does not list AND does not name the gateway catalog role (the role ARN is built from `gateway-schwab-catalog-read-role`). If true, ALSO file a BLOCKING row: do NOT edit that bucket policy (it is outside this order).

## 2. BOUNDS

- Write only `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf`, `W/` and, if a row is needed, the channel. No other Terraform file, no code, no contract, no test, no `apply`, no `plan`, no AWS call, no `terraform init` in the gateway root. Scratch for `terraform console` goes in your own scratch folder, never inside the repository tree you commit.
- No account number, tid, oid, e-mail, ARN of a real principal or account id in any file you write (the bucket and role NAMES above are fine).
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~179/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W179-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sk-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)terraform console evaluated all ten locals.*: ok.*firm silver object ARNs: four, the master in the FILE NAME.*: ok.*state completion: one object ARN naming 08403355\.complete\.json, one listing form: ok.*data role: the OLD 12 object ARNs unchanged and in order, then the 4 firm ARNs.*: ok.*catalog role: the OLD 3 completion ARNs then the 1 state ARN.*: ok.*no bucket-wide or folder-wide grant.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sk-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)terraform fmt -check accepts the file: ok.*catalog policy: 8 statements.*: ok.*data policy: still 6 statements and no mention of the state bucket: ok.*no write, delete, wildcard-action or sts action.*: ok.*diff against the pin: \d+ added, \d+ removed.*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-sk-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sk3.AC3.sh; echo "exit=$?"</invocation><expect>(?s)bucket named opal-data-49financial; owner_file \S+ is a \.tf that holds the bucket name \(read here\): ok.*policy_file \S+ is null or a \.tf that holds the bucket name \(read here\): ok.*needs_change \S+ is consistent with.*: ok.*reason stated: ok.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the locals evaluated by `terraform console` (the issuer's script). `AC2`: the statements and the size of the diff. `AC3`: the bucket-side fact, read against the files it cites.

## 5. WHEN YOU ARE DONE

Commit, then write the proof instance at `W/NFRA_OPLGTW.TO-OG-sk-3.round-47-the-schwab-reader-iam-text-for-the-firm-folder-and-the-state-bucket.proof_of_spec.json` and validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-sk-3.round-47-the-schwab-reader-iam-text-for-the-firm-folder-and-the-state-bucket.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-N, amendment A16 of R3-T.124. Third cell of release R3c (`OG-sk-2` code and contract, `OG-sk-3` this IAM text, `OG-sk-4` `family_depth`). `~NFRA1` applies the Terraform under `safe-apply` in the release window: the apply is the widening the never-widen pair names (the gateway's FIRST grant on `opal-data-49financial`).
- `<risk>WORLD</risk>` is the `infra/` floor (a grant). Pre-cut: `AC1`, `AC2`, `AC3` base FAIL as expected. Arm: a scratch reference edit (32 added, 4 removed) read `AC1` PASS (8 of 8 lines, evaluated by `terraform console` in a scratch module) and `AC2` PASS, then was restored byte-for-byte (clean status). `AC3` needs the worker's record, so it was not armed.
- LISTING note for the asks: S3 `ListBucket` conditioned on a prefix reveals KEY NAMES under that prefix (not contents). Today `schwab/49financial/` holds only `08403355`'s objects; when another master lands there its key names become listable to this role (its contents stay unreadable: the object grants are by file name). The CTO's 17:49Z condition accepts the prefix-conditioned listing; the ask states this sentence.

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-N</workstream>
<slot>~179</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
