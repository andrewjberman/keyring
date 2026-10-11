# MDPF_CANON task order -- `CN-a-2` -- THE ONE PARQUET WRITER (THE EMITTER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-a-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~2</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed (the live clock stays as read at L5).
comp-iam: DECLARED-NOT-APPLICABLE this cell changes no IAM; it reads os.environ GOLD_WRITER_ROLE_ARN_<FIRM>, granted by CN-a-1.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r1_emit.py 0 of 7 at base (the module is absent); 7 of 7 against the issuer's reference tree (positive control); pytest data/mdpf/scripts/gold/tests with the three known-red test_global_fold_flag2 cases deselected: 94 passed at base
EGRESS CLASS, declared: NONE (the worker writes no AWS; the issuer's CloudOps lane applies after the drain).
</preflight>

## 1. THE CELL -- `CN-a-2` (round 1, THE THREAD for FWD-1; decomposition v1)

Read `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and DEC-2, DEC-14 and DEC-15 first. The L5 fact sheet the issuer cut against is
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/L5_FACTS.md`. This cell starts chain 2; `CN-a-3` (the backfill) builds on its writer after it completes.

Gold today: `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (the `mdpf-gold-lambda`) writes dated JSON to the legacy tree for
scopes 49financial, inflection, cottonwood and global (emit loop about :2765-2799; `a4_key()` :2170). There is NO parquet for the four
artifacts anywhere. Copy the parquet and assumed-session pattern of `taxsma_assets.py` / `taxsma_session()` (:1168-1186).

1. **A new module `data/mdpf/scripts/gold/mdpf_gold_parquet.py`, the ONE writer of the new gold.** Its interface is fixed (AC1 binds
   it):
   - `ARTIFACTS = ("account_distribution", "account_units", "aggregate_aua_timeseries", "aum_metrics")`.
   - `partition_uri(scope, artifact, date)` returns `address("mdpf", scope, "gold", artifact, f"date={date}", object="data.parquet")`.
   - `client_for_scope(scope, boto3_module=None)`:
     - For a firm scope, it assumes `os.environ["GOLD_WRITER_ROLE_ARN_" + scope.upper()]` through `sts` and returns an S3 client on
       those credentials.
     - It RAISES when that variable is unset; never fall back to the Lambda's own credentials.
     - For `global`, it returns the Lambda's own S3 client.
   - `write_partition(s3, scope, artifact, date, records)`:
     - Serialize `records` (a list of flat dicts) to parquet with pyarrow and read the existing object first.
     - If the object is absent, put it and return `"written"`.
     - If the bytes are equal, return `"unchanged"` without a put. If they differ, return `"conflict"` without a put.
     - It never overwrites (history is never rewritten).
   - `run_status(intended_scopes, built_scopes)` returns `"PASS"` only when every intended scope was built, else `"PARTIAL"` (PRD M16).
   - The module types no `s3://` and no `opal-data-` string.
2. **Wire it into the consolidator's daily run, ADDED beside the existing JSON emits (which stay byte-for-byte as they are):**
   - For each scope the run builds and each artifact it has, call `write_partition` for the run's data-as-of date.
   - The records are the artifact's figures as flat rows. Define one small `records_for(artifact, payload)` in the new module and
     document its row shape in a docstring.
   - `account_units` is standalone only for cottonwood. For the other scopes, write it from the figures the run already computes
     (the folded `total.account_units`), or record its absence in the manifest. Do not invent a figure.
   - Count the parquet emits into the run manifest with `run_status(intended, built)`: a run that set out to build four scopes and
     built two reads `PARTIAL`.
3. **Package it:** add `("mdpf_gold_parquet.py", "data/mdpf/scripts/gold/mdpf_gold_parquet.py")` to `build_package.py`'s list.
4. Unit tests for the module go in `data/mdpf/scripts/gold/tests/test_mdpf_gold_parquet.py` (synthetic records only).

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
data/mdpf/scripts/gold/mdpf_gold_parquet.py
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/tests/test_mdpf_gold_parquet.py
infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~2/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `data/mdpf/scripts/gold/taxsma_assets.py`, `lib/opal_naming.py`, and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-a-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/r1_emit.py"; echo "exit=$?"</invocation><expect>ROUND 1 PARQUET WRITER: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-a-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest data/mdpf/scripts/gold/tests -q --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_beyond_window_absent_for_real --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_source_is_measured_never_interpolated; echo "exit=$?"</invocation><expect>passed, with 0 failed -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-a-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's real run at the round-1 close (never self-graded): after CloudOps deploys the package, one ad-hoc QA run of the gold Lambda writes `data.parquet` at `address()` for each built scope and artifact; a second run reads `unchanged`; the legacy JSON is byte-identical to a run without the change.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~2/MDPF_CANON.TO-CN-a-2.proof_of_spec.json` (AC3 UNVERIFIABLE-BY-INSTRUMENT,
status_reason "graded at the round-1 close run"). **Flip this order's `<status>` to `complete` in the SAME commit as your proof
instance**, only when AC1 and AC2 pass. A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W2-S<k>`, with
`surfaced_at` from `date -u +%FT%TZ` at filing. Report once: the diff (per file, one line each), the output line of every
criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (FWD-1) over PRD v2.9 @12adb87963 (ADMITTED; the CVO's L6 condition, msg 3000, is arm 1 and arm
5 of `r1_iam.py`). Base box/dell1. LF only. Checks positive-controlled against a reference tree before the cut.

<status>complete</status>
<round>1</round>
<to_id>MDPF_CANON.TO-CN-a-2</to_id>
<slot>~2</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
