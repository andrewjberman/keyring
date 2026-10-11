# ADVI_FIRMBKTS task order -- `FB-g-26` -- THE TWO STALE-ADVISOR CLEANUPS READ THE `Errors` OF `delete_objects` AND EXIT NON-ZERO NAMING THE KEYS (THE CTO'S ACT-0 ADDENDUM 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-26</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~47</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository files only; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- two producer scripts and one test file; no AWS act and no grant. The delete grant they will need is a separate cell under the act-0 pair's addendum.
comp-adversary: RUN by the issuer -- at base `r4_failloud.py` reads 1 of 4 (F4, one delete_objects call and no delete_object call per script, PASSES as the control; F1 to F3 FAIL as expected: no Errors read, no exit, no test file). Blindness: the check reads the scripts' syntax tree and runs the unit test with a stubbed client; it cannot see S3's real answer to a denied batch (the boto3 contract is that per-key failures return in Errors with HTTP 200).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-26` (round 4, workstream `FAILLOUD`; the CTO's act-0 CTO half ADDENDUM 1 item 2, msg 3931)

Two producer scripts delete a departed advisor's files at the destination bucket with `s3.delete_objects(...)` and never
read the response. `delete_objects` answers HTTP 200 with a per-key `Errors` list when a key is refused (AccessDenied
included), so a refused cleanup removes nothing and says nothing. After act 2 the destination is the canonical home. Make both
sites fail loud. Nothing else about either script changes.

### 1a. Behavior (the whole spec)

1. **One function per script.** In each of `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` and `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`, move the single `s3.delete_objects(Bucket=..., Delete=...)`
   call into a module-level function `_delete_batch_fail_loud(s3, bucket, objs)` (one definition per file, called from
   exactly the place the call was). It performs the same `delete_objects` call, then reads `resp.get('Errors') or []`.
2. **When `Errors` is non-empty:** print one line `ERROR: delete_objects refused <n> of <m> keys in <bucket>:` followed by
   each failing key with its `Code` (all of them, one per line), then exit non-zero (`sys.exit(2)`). Do NOT catch the exit
   anywhere. When `Errors` is absent or empty: return normally, printing nothing new.
3. **Nothing else changes.** The batching (1000 keys), the `by_bucket` grouping, the `platinum_destination(k)` mapping, the
   dry-run branch and every other line of both scripts stay exactly as they are.
4. **The unit test.** Add `data/black_diamond/scripts/gold/tests/test_delete_errors_fail_loud.py` (unittest, standard library only, in the style of
   `test_platinum_dest.py` in the same folder). It loads each script's function without running its main (follow how
   `test_platinum_dest.py` obtains the script module; if importing a script runs heavy work, load only the function by
   `ast`/`exec` of its source), and asserts, for EACH of the two scripts: (a) a stub client whose `delete_objects` returns
   `{'Errors': [{'Key': 'k1', 'Code': 'AccessDenied', 'Message': 'x'}]}` makes the function exit non-zero (SystemExit with a
   non-zero code) and its output names `k1` and `AccessDenied`; (b) a stub returning `{'Deleted': [{'Key': 'k1'}]}`
   returns normally and exits nothing. That is at least four test methods.

## 2. BOUNDS

1. Files that change: `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`, `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` and the new `data/black_diamond/scripts/gold/tests/test_delete_errors_fail_loud.py`. No other file; no AWS call; no deploy.
2. The scripts are deployed by a separate act. Do not edit any manifest, source map or workflow.
3. ASCII only; keep each file's existing line endings (read them first; do not convert). If the commit is refused by a
   gate, do not override or force: file a BLOCKING row with the gate's lines.
4. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/D_02.advisor_client_detail.py
data/black_diamond/scripts/gold/tests/test_delete_errors_fail_loud.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~47/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~47/ADVI_FIRMBKTS.TO-FB-g-26.delete-errors-fail-loud.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-26"><invocation>cd /c/dev/wk-firmbkts-47 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_failloud.py --arms static --root /c/dev/wk-firmbkts-47; echo "exit=$?"</invocation><expect>ROUND 4 FAIL-LOUD: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-26"><invocation>cd /c/dev/wk-firmbkts-47 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-47 --allow data/black_diamond/scripts/gold/D_04.client_portal_summary.py --allow data/black_diamond/scripts/gold/D_02.advisor_client_detail.py --allow data/black_diamond/scripts/gold/tests/test_delete_errors_fail_loud.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~47/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require data/black_diamond/scripts/gold/D_04.client_portal_summary.py --require data/black_diamond/scripts/gold/D_02.advisor_client_detail.py --require data/black_diamond/scripts/gold/tests/test_delete_errors_fail_loud.py; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads each script's syntax tree (the one call's response read for `Errors` and a non-zero exit naming the keys), runs
the unit test (four methods or more) and counts the delete calls (one per script). AC2 is the write-surface bound. Each
invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-26.delete-errors-fail-loud.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~47`.
Commit the three files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W47-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2
outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's act-0 CTO half ADDENDUM 1 (msg 3931, item 2: "both sites read delete_objects Errors and
exit non-zero naming the keys; close is a stubbed per-key AccessDenied raising and a clean delete passing"). Its two blobs
join act 2's set by the issuer's addendum to the act 2 pair. Row `ADVI_FIRMBKTS-D1-S29`. Workstream `FAILLOUD`. Class WORLD
by the path floor (producer scripts), not deployed by this cell.

<status>pending</status>
<round>4</round>
<workstream>FAILLOUD</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-26</to_id>
<slot>~47</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
