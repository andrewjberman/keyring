# ADVI_FIRMBKTS task order -- `FB-f-13` -- ACTS 4b AND 4c, PHASE A: THE SERVED-LAYOUT SEAM IN THE TWO LAMBDAS THAT READ THE LEGACY HOME (DORMANT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~22</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- phase A edits repository source only; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. Whether each Lambda's role may read and write the new bucket's prefix is read at the act, not here.
comp-adversary: RUN by the issuer -- `r3_reads.py --files` over the two Lambdas' sources reads UNROUTED 3 (exec-summary-generator: one put, one paginate, one get_object helper) and UNROUTED 4 (opal-partners-data: two get_object, one list_objects_v2, one head_object) at base, so AC1 FAILS by construction; the parity test classes do not exist, so AC2 selects no test at base. Blindness: the census reads syntax: it does not run either Lambda; dormancy rests on the seam's identity in `legacy` mode (the unit tests) and on the census showing every call routed through it.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-f-13` phase A (round 3; the CTO's act-2 half ADDENDUM 1 rows 3 and 4, msg 3677: "exec-summary and opal-partners-data repoint as acts 4b/4c in this window")

Two deployed Lambdas read (and one WRITES) served-class keys of `opal-data-bd`, a legacy home that is frozen once the
producers write the new home:
- `infra/aws/lambda/exec-summary-generator`: reads `platinum/advisors/` (list and `summary.json`, `timeseries.json`, `nna_clients.json`, `positions.json` per
  advisor) and `platinum/leaderboards/`, and WRITES `platinum/advisors/<advisor>/exec_summary.json`, all on the constant
  `S3_BUCKET = "opal-data-bd"` of its `config.py`.
- `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data`: the partners API; its bucket is read per firm from DynamoDB (`s3Bucket`), and it serves
  `gold/artifacts/...` keys through `serve_s3_json`, `serve_s3_json_nocache`, a `head_object` health probe and one
  `list_objects_v2`.

You give each a SEAM, DORMANT: with the mode unset every call names the bucket and key it names today. A later act (not
yours) sets `BD_PLATINUM_MODE=canonical` on a Lambda's configuration; that single value then moves its served reads and the
exec-summary's one write to the new home. You run nothing and deploy nothing.

### 1a. The facts you start from

- The reference seam is `data/black_diamond/scripts/gold/lib/platinum_dest.py` (merged; read it) over the generated view
  `data/black_diamond/scripts/gold/lib/platinum_dest_view.py` (`PLATINUM_CLASSES`: rows `(legacy_prefix, bucket, key_template)`, the template ending in
  `{tail}`). A Lambda cannot import the gold `lib`; it is packaged from its own directory, whose file list is
  `functions.<name>.files` in `infra/aws/lambda/ci/lambda-source-map.json`.
- The mode is the environment variable `BD_PLATINUM_MODE`: unset or `legacy` = today; `canonical` = the new home; any other
  value is a `ValueError`.
- The seam applies ONLY to the pipeline bucket `opal-data-bd`: a call on any other bucket is returned unchanged (the partners
  API serves other firms from their own buckets).
- The issuer's census `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py`, in its `--files` mode, grades named files: a call is ROUTED when its Bucket is
  bound from a call to `platinum_destination`, `platinum_source` or `platinum_list_target` (by those names). Run it first:
  `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py --list --files infra/aws/lambda/exec-summary-generator/lambda_function.py infra/aws/lambda/exec-summary-generator/platinum_reader.py infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`.

### 1b. The steps

0. Work in `/c/dev/wk-firmbkts-22`. Begin every shell call with `cd /c/dev/wk-firmbkts-22 &&`.
1. **The seam module.** Create `served_seam.py` in EACH Lambda directory, byte-identical in both, standard library only,
   Python 3.12, ASCII, with:
   - `destination(bucket, key, mode=None) -> (bucket, key)`; `source(bucket, key, mode=None) -> (bucket, key)` (the same
     resolution: reads follow writes);
   - `list_target(bucket, prefix, mode=None) -> (bucket, prefix, to_legacy)`;
   - the rules of `platinum_dest.py` `destination` and `list_target` exactly, applied only when `bucket == "opal-data-bd"`
     (any other bucket: the identity, `to_legacy` the identity). A prefix that is a PROPER prefix of a served class prefix
     is a `ValueError` in `canonical`.
   It imports the view as `from platinum_dest_view import PLATINUM_CLASSES` (a flat module beside it).
2. **The generated view in each Lambda directory.** `lib/opal_naming.py` emits the gold view with `generate --target`; read
   how that target is wired (`WHOLE_FILE_TARGETS` and its siblings, the same wiring `platinum_dest_view.py` uses) and add
   TWO more whole-file targets: `infra/aws/lambda/exec-summary-generator/platinum_dest_view.py` and `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py`, each the same generated module
   (mark and registry hash as the gold one). Generate both with the builder; never hand-type a table. Then
   `python lib/opal_naming.py targets` must still exit 0, with the two new files classified SHIP on the lambda plane.
3. **Package lists.** In `infra/aws/lambda/ci/lambda-source-map.json` add `served_seam.py` and `platinum_dest_view.py` to the
   `files` list of `exec-summary-generator` and of `opal-partners-data`, so the build ships them.
4. **Route every call.** In `infra/aws/lambda/exec-summary-generator/lambda_function.py`, `infra/aws/lambda/exec-summary-generator/platinum_reader.py` and `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`: each S3 data
   call's bucket and key come from the seam (`b, k = platinum_source(bucket, key)` for a read or head;
   `b, k = platinum_destination(bucket, key)` for the exec-summary's put; `b, p, to_legacy = platinum_list_target(bucket,
   prefix)` for a list or paginate, with `to_legacy` applied to each returned key so the rest of the function sees
   legacy-shaped keys exactly as today). Import them as `from served_seam import destination as platinum_destination,
   source as platinum_source, list_target as platinum_list_target`. Route inside the shared helpers (`_read_json`,
   `serve_s3_json`, `serve_s3_json_nocache`), not at their callers.
5. **Parity tests**, in `data/black_diamond/scripts/gold/tests/test_lambda_seam_parity.py` (unittest, standard library; load each Lambda's
   `served_seam.py` and `platinum_dest_view.py` by path with `importlib.util.spec_from_file_location`), in ONE class named
   exactly `TestLambdaSeamParity`:
   (a) the two `served_seam.py` files and the two generated views are byte-identical to each other, and each view is
   byte-identical to `data/black_diamond/scripts/gold/lib/platinum_dest_view.py`;
   (b) for one key of each of the 11 classes and each mode (`legacy`, `canonical`): the Lambda seam's `destination` and
   `source` for bucket `opal-data-bd` equal `lib/platinum_dest.py` `destination` and `source` (bucket and key);
   (c) `list_target` for a served prefix: `legacy` is the identity; `canonical` names the class bucket and a prefix that is
   not the legacy one, and `to_legacy(dest_prefix + tail)` returns `legacy_prefix + tail`;
   (d) any bucket other than `opal-data-bd` is the identity in both modes; a non-served key on `opal-data-bd` is the
   identity in both modes;
   (e) a recording fake S3 client driven through the exec-summary's `list_active_advisors()` and `_read_json()`, and the
   partners Lambda's `serve_s3_json()`, under `canonical`, records 0 calls whose Bucket is `opal-data-bd` with a key under
   a served prefix. Where a module needs a package not installed in your environment, stub it in `sys.modules` inside the
   test and say so in your report.

## 2. BOUNDS

1. Repository files only: no AWS call, no deploy, no invocation of either Lambda, no `deploy.sh`, no `aws lambda ...`, no
   Terraform apply (CLAUDE.md: Terraform only). Do NOT edit any `.tf` file or any Lambda environment: the mode is set by a
   later act.
2. With the mode unset every call you touch names the same bucket, prefix and key as today and the pages a listing returns
   are the same; if an edit would change a `legacy` result, STOP and file a BLOCKING row.
3. No new delete, copy, write or alert. The exec-summary's one put stays exactly one put, with the same body, content type
   and encryption.
4. Do not edit `data/black_diamond/scripts/gold/lib/platinum_dest.py`, `data/black_diamond/scripts/gold/lib/platinum_dest_view.py`, any registry row, or any check. No bucket name
   typed in a new string literal except the single pipeline bucket constant `opal-data-bd` inside `served_seam.py` (the
   guard); every destination bucket comes from the generated view. Client ids appear in keys: your report names counts and
   paths, never a key. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/lambda/exec-summary-generator/served_seam.py
infra/aws/lambda/exec-summary-generator/platinum_dest_view.py
infra/aws/lambda/exec-summary-generator/lambda_function.py
infra/aws/lambda/exec-summary-generator/platinum_reader.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/served_seam.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py
lib/opal_naming.py
infra/aws/lambda/ci/lambda-source-map.json
data/black_diamond/scripts/gold/tests/test_lambda_seam_parity.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~22/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~22/ADVI_FIRMBKTS.TO-FB-f-13.lambda-seams.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-13"><invocation>cd /c/dev/wk-firmbkts-22 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py --root /c/dev/wk-firmbkts-22 --files infra/aws/lambda/exec-summary-generator/lambda_function.py infra/aws/lambda/exec-summary-generator/platinum_reader.py infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py; echo "exit=$?"</invocation><expect>ROUND 3 READ CENSUS: ALL SITES ROUTED, NOT-SERVED OR EXEMPT</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-13"><invocation>cd /c/dev/wk-firmbkts-22 &amp;&amp; timeout 110 env -u FORCE_COLOR python -m unittest discover -s data/black_diamond/scripts/gold/tests -p "test_lambda_seam_parity.py" -k TestLambdaSeamParity 2&gt;&amp;1 | tail -n 3</invocation><expect>^OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-13"><invocation>cd /c/dev/wk-firmbkts-22 &amp;&amp; timeout 100 python lib/opal_naming.py targets &gt; /dev/null 2&gt;&amp;1; echo "targets-exit=$?"</invocation><expect>targets-exit=0</expect></criterion>
</proof_of_spec>

AC1 is the issuer's census over the two Lambdas' sources (UNROUTED 0), FAIL at base (7). AC2 runs the parity class (the
seam equals the reference seam; the canonical negative arm), FAIL at base (it does not exist: no test selected). AC3 is the
builder's own plane classification with the two new generated views (PASS at base as a control: it FAILS if a view lands as
an unclassified file). Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-13.lambda-seams.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~22`. Commit the
seams, the views, the routed sources, the builder target edit, the source map, the test and your rows, then the instance
second (its artifact rows pin to the commit that holds them). **Do not flip this order's `<status>`**: phases B and C (the
two acts, each with its own pair) are the issuer's to amend. Row ids: `ADVI_FIRMBKTS-D1-W22-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the AC1 output in full, the census counts before and after, the parity
test count, the list of paths you could not drive in test (e), and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** class WORLD by the floor of the acts it prepares; phase A is repository source only and spawns the turn it is
cut. Cut on the CTO's act-2 half ADDENDUM 1 (@6ac66a8950, msg 3677) rows 3 and 4: both Lambdas move in this window beside act 4,
each as its own act with its own pair, change-management entry and DELTA=0 read of its served responses. DESIGN CHOICE for the
CTO's reading (stated, not asked): the cutover of each Lambda is its configuration value `BD_PLATINUM_MODE` (a Terraform
`environment` change), NOT the DynamoDB `s3Bucket` item: the item names a bucket and the key layout differs by home, so
repointing the item alone would miss on every key; a mode on the Lambda keeps the DynamoDB item untouched (0 writers of it
involved) and makes the rollback one environment value. The exec-summary Lambda is a writer of a served key outside the 14
(`platinum/advisors/<id>/exec_summary.json`): its put follows the seam, so after the move the router at act 4 finds it at the
new home. Two follow-ups outside this cell: the partners API's `/health` probe (`head_object` of the summary key) follows the
seam too; and `data/black_diamond/scripts/exec_summary/` carries a second copy of `template_library.py` and `trigger_eval.py`
that this cell does not touch.

<status>pending</status>
<round>3</round>
<workstream>ACT4BC</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-13</to_id>
<slot>~22</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
