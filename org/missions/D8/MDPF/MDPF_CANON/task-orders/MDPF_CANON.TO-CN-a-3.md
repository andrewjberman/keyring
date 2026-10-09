# MDPF_CANON task order -- `CN-a-3` -- THE BACKFILL OF THE DATED HISTORY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-a-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~3</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed (the live clock stays as read at L5).
comp-iam: DECLARED-NOT-APPLICABLE this cell changes no IAM; it writes only through CN-a-2's write_partition, under CN-a-1's roles.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r1_backfill.py 0 of 7 at base; 7 of 7 against the issuer's reference tree (positive control). Spawned after CN-a-2 completes.
EGRESS CLASS, declared: NONE (the worker writes no AWS; the issuer's CloudOps lane applies after the drain).
</preflight>

## 1. THE CELL -- `CN-a-3` (round 1, THE THREAD for FWD-1; decomposition v1)

Read `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and DEC-2, DEC-14 and DEC-15 first. The L5 fact sheet the issuer cut against is
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/L5_FACTS.md`. This cell is chain 2's second link: it is spawned after `CN-a-2` completes and builds on its writer.

The per-day history of the four artifacts exists only as the legacy dated JSON
`s3://opal-data-assets/portal/gold/mdpf/{scope}/{type}/{YYYY-MM-DD}.json`: 32-58 dates per series, from 2026-07-20..30, with gaps
(L5_FACTS.md section 2). The longer aggregate series (2024-11-01..) inside the single objects is NOT this round's: if you find it
per-scope and dated, file a row naming it for round 2.

1. **A new module `data/mdpf/scripts/gold/mdpf_gold_backfill.py`.** Its interface is fixed (AC1 binds it):
   - `SOURCE_TYPES`: `{"aggregate-aua-timeseries": "aggregate_aua_timeseries", "aum-metrics": "aum_metrics",
     "account-distribution": "account_distribution", "account-units": "account_units"}`.
   - `plan(source_keys, existing)`: a sorted list of `(scope, artifact, date, source_key)`, one for every key of the form
     `portal/gold/mdpf/{scope}/{type}/{YYYY-MM-DD}.json` whose type is in `SOURCE_TYPES`, minus any `(scope, artifact, date)` in
     `existing`. Every other key (category-views, non-model-assets, `_manifests`, `_code`, undated) is ignored.
   - `summarize(plan_rows, source_keys, existing)`: one line per series,
     `BACKFILL {scope}/{artifact}: {n} of {m} source dates ({k} already present)`.
   - `run(plan_rows, read_source, write)`: calls `write(scope, artifact, date, read_source(source_key))` once per row, in order,
     never retrying, and returns the tally of verdicts.
   - The module types no new-home bucket (only the legacy source `opal-data-assets` may appear).
2. **Wire `run_class == "backfill"` into the consolidator's `lambda_handler`:**
   - list the legacy dated tree;
   - list the existing new partitions;
   - `plan`, then print `summarize`;
   - `run` with `read_source` = the legacy object's body turned into records by CN-a-2's `records_for`, and `write` = CN-a-2's
     `write_partition` on `client_for_scope(scope)`.
   - It writes NOTHING else; the daily path is unchanged.
3. **Package it:** add `("mdpf_gold_backfill.py", "data/mdpf/scripts/gold/mdpf_gold_backfill.py")` to `build_package.py`.
4. Unit tests go in `data/mdpf/scripts/gold/tests/test_mdpf_gold_backfill.py` (synthetic keys only).

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`, no IAM call. A read-only `get`/`describe`/`head` is
   allowed. No install, no push. The issuer has CloudOps apply and deploy after the drain. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Every NEW address and name comes from the builders**: `lib/opal_naming.py` `address()`/`key()` in Python, and the
   `../modules/opal_name` Terraform module for names, never a typed bucket, key or role name (PRD CONTRACTS; DEC-15; CLAUDE.md rule 30).
   A builder REFUSAL is a row, never a hand-typed workaround.
4. **Never** (PRD DEC-14):
   - change the conformant compute chain's schedules or platinum's shape;
   - move `platinum/mdpf/global/`;
   - touch `opal-data-mdpf/code/scripts/gold/`;
   - add a second writer of the new gold;
   - add a shadow prefix or a standing comparator.
   The existing JSON emits stay exactly as they are this round; the new parquet is ADDED beside them (the readers and the publisher
   move in later rounds, the publisher last).
5. **CLIENT DATA:** never open or print a client figure or account id; fixtures are synthetic. Never read any
   `org/**/W73_S*_EVIDENCE.json`, `W73_S2_RESOLUTION.json`, an IRPT_DASHBD tie-out file or a COTBKF worker manifest.
6. Keep each file's line endings as you find them (read them first); no non-ASCII; Edit tool for existing files. Python edits pass
   `.tools/commit-gate.sh` (safe-commit runs it).
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_gold_backfill.py
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/tests/test_mdpf_gold_backfill.py
infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~3/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `data/mdpf/scripts/gold/mdpf_gold_parquet.py` (after CN-a-2), and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-a-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/r1_backfill.py"; echo "exit=$?"</invocation><expect>ROUND 1 BACKFILL: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-a-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest data/mdpf/scripts/gold/tests -q --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_beyond_window_absent_for_real --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_source_is_measured_never_interpolated; echo "exit=$?"</invocation><expect>passed, with 0 failed -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-a-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's real run at the round-1 close (never self-graded): the issuer's ad-hoc `run_class=backfill` invocation prints one n-of-m line per series, and the partitions it wrote are exactly the legacy dates not already present; asked 49 Financial's total assets on a day last month, the answer comes from the key's date alone.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~3/MDPF_CANON.TO-CN-a-3.proof_of_spec.json` (AC3 UNVERIFIABLE-BY-INSTRUMENT,
status_reason "graded at the round-1 close run"). **Flip this order's `<status>` to `complete` in the SAME commit as your proof
instance**, only when AC1 and AC2 pass. A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W3-S<k>`, with
`surfaced_at` from `date -u +%FT%TZ` at filing. Report once: the diff (per file, one line each), the output line of every
criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v2.9 @12adb87963 (ADMITTED; the CVO's L6 condition, msg 3000, is arm 1 and arm
5 of `r1_iam.py`). Base box/dell1. LF only. Checks positive-controlled against a reference tree before the cut.

<status>pending</status>
<round>1</round>
<to_id>MDPF_CANON.TO-CN-a-3</to_id>
<slot>~3</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
