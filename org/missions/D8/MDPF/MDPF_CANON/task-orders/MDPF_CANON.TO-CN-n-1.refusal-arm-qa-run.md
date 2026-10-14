# MDPF_CANON task order -- `CN-n-1` -- THE REFUSAL ARM DRIVEN: A QA RUN WHERE THE GLOBAL FOLD'S POOL IS HELD BY ONE FIRM (row D1-W16-S1; FWD-3's third arm)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-n-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~21</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell runs an existing build once, locally.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added to any deployed role; the run makes read-only calls (get, head, list) under your own credentials, and the instrument raises on any other call.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- `r7_cn_n_1.py grade` 0 of 6 and `served` 0 of 4 at base (no run record); `guard` 5 of 5 (a control over merged code); `selftest` OK (a synthetic good record passes and five planted defects turn it red).
EGRESS CLASS, declared: NONE (the run writes no AWS; the instrument blocks and records every non-read call).
</preflight>

## 1. THE CELL -- `CN-n-1` (round 7, decomposition v7)

**What this is.** Round 6 merged a guard in `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (`guard_global_min_firms_fold`, called in `build_all` right after
`guard_global_served_identity`): when the Global fold's pool has a value on the LAST date and fewer than two firms hold it, Global is refused WHOLE
(`SystemExit` with the prefix `GLOBAL MIN-FIRMS FOLD REFUSED:`), the refusal is recorded under `manifest["errors"]["global"]`, and the three firm scopes
build as before. No one-firm day has happened in production, so that arm has never run end to end. Your job is to DRIVE it once, in QA, and file the record.
You build NOTHING: the instrument `r7_cn_n_1.py` (issuer's, read-only for you) does the run and the grading.

**AMENDMENT 1 (the issuer's, 2026-10-14 ~15:0xZ; you are the RE-SEATED worker on this slot).** A first seat drove the run once and it ended RAISED, not with a Global refusal. Its record is already on your
branch's base under `deliverables/0.9.0_WK_MDPF_CANON~21/run/` and its rows are `MDPF_CANON-D1-W21-S1` to `-S3` in the investigation file (inherited state; do not edit them). The cause was the
INSTRUMENT's plant, not the guard: it edited the firm artifacts in place, so the inflection category-views build saw peers that no longer summed to the total, and it blanked `model_value` without `account_count`,
so the cross-axis presence gate failed Global first. The issuer has fixed the instrument (the plant now edits deep COPIES handed to the Global builder only and blanks the count with the value; a RAISED run
records `writes: []`). This is a NEW outcome on a corrected instrument, so the "run once" rule restarts: run `selftest`, `plan`, the clock check, then `drive` ONCE more into the SAME `run/` directory
(it overwrites the first seat's files, which are in git history), then section 4. If this run also does not behave, Step 3 applies unchanged.

**AMENDMENT 2 (the issuer's, ~15:1xZ; you are the THIRD seat on this slot).** The second seat's run (rows `MDPF_CANON-D1-W21-S4`, `-S5`, inherited, do not edit) was refused by the cross-axis presence gate again, and the log shows why: the Global builder
re-sets every frontier `account_count` from its own count source AFTER the plant (the log's `ROW11 frontier-stamp` line), so blanking the count could not hold. The instrument now plants a ZERO `model_value` (`fill=0.0`) instead of a blank, which
keeps count and value both present and leaves the line not held. This is the issuer's INFERENCE from that log line, not yet a measured result; your run measures it. Run `selftest`, `plan`, the clock check (outside 13:00Z-14:10Z), then `drive` ONCE into the same `run/`
directory, then section 4. Whatever the run does, Step 3 applies unchanged, and this is the last drive of this order: if it is refused for any other reason, keep the record, file the row and stop.

**AMENDMENT 3 (the issuer's, ~15:3xZ; you are the FOURTH seat on this slot, and the plant has MOVED).** The third seat's run (row `MDPF_CANON-D1-W21-S6`, inherited, do not edit) was refused by `GLOBAL COMPOSITION GATE FAILED ... 1 band/total violation`:
the composition gate runs inside the Global build, before `guard_global_min_firms_fold` is called, so ANY plant placed inside the build trips an earlier gate. The instrument now plants AT THE GUARD'S OWN CALL SITE: it wraps
`guard_global_min_firms_fold`, runs the REAL guard on a deep copy whose firm scopes carry the one-firm pool, and when the guard refuses Global it hands the run on with the ORIGINAL scopes and Global dropped (the guard's own swallowed-refusal
shape). Every earlier gate therefore sees the unplanted build. Expected: `errors=['global']` with the `GLOBAL MIN-FIRMS FOLD REFUSED:` prefix, `writes=0`, `blocked-calls=0`. The `drive` command line is unchanged. Run `selftest`, `plan`, the clock
check (outside 13:00Z-14:10Z), then `drive` ONCE into the same `run/` directory, then section 4. This is the FINAL drive of this order: a refusal for any other reason is kept as a record and a row, and the cell then stands on its guard arm (AC3).

**The instrument** (`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py`; read its header and the functions `plant_single_firm_pool` and `cmd_drive`; never edit it):
- `drive --run-dir DIR` calls the consolidator's `build_all(trigger, dry_run=True, out_dir=<temp>)` ONCE. `dry_run=True` writes nothing to S3 (the handler documents QA-local mode as "ZERO S3
  writes anywhere"). The instrument also installs a guard on every botocore call: any operation not named Get, Head, List, Describe, Lookup or Simulate RAISES and is recorded. It wraps
  `spine.build_global_artifact` so that, on the run's own in-memory firm builds, every model line held by fewer than two firms on the last date is held by exactly ONE firm.
- It snapshots the served prefixes (`portal/gold/mdpf/`, `gold/mdpf_revamp/` in bucket `opal-data-assets`, every object version) before and after, records the manifest errors, the log text and the call kinds, and
  deletes its local A4 bodies after listing their names.

### Step 1 -- precondition reads (stop and file a row if any is false; do not run)

1. `git rev-parse --show-toplevel` resolves and you are in your assigned worktree; `python -c "import boto3, pyarrow"` succeeds.
2. `python "<instrument>" selftest` prints `ROUND 7 CN-N-1 SELFTEST: OK`.
3. `python "<instrument>" plan` prints a plant record with `"planted": true` and a served snapshot count. It makes read-only calls only.
4. The clock: read `date -u +%H:%MZ`. The scheduled gold fire is 13:30Z daily and its objects land by ~13:35Z. Do NOT start `drive` between 13:00Z and 14:10Z (a fire writing during your
   run would change the served snapshot and read as a write by you). If you are inside that window, wait until after 14:10Z; a worker cannot be messaged, so do not ask.

### Step 2 -- the run (ONCE; it reads many objects and can take several minutes)

```
python "<instrument>" drive --run-dir "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run"
```

Run it in the foreground with the longest timeout your shell allows (up to 10 minutes) or in the background with a redirected log and a poll; do not run it twice for one outcome. When it ends it
prints one `QA run done` line. Expected: `status=non-green` (an errors entry for global), `errors=['global']`, `writes=0`, `blocked-calls=0`. Then run the three criteria in section 4.

### Step 3 -- if the run does not behave (file a row, keep working; never edit the instrument or any product file)

- `build_all` raises before the guard (an environment gap such as missing credentials, a missing module, an S3 read failure): copy the error line into a row, keep the `run/` files the instrument wrote, and stop on AC1/AC2.
- The refusal text differs (Global refused for a DIFFERENT reason, such as the served-identity guard, or not refused at all): that is a finding about the guard or the plant. Keep the record, file a row naming
  the exact `manifest_errors.global` text, and stop on AC1. Do not change the plant.
- `blocked-calls` greater than 0: the build tried to write under `dry_run`. Keep `s3_ops.json`, file a row naming the blocked call kind, and stop on AC2.

## 2. BOUNDS

1. **No AWS write of any kind**, by you or by the run (the instrument blocks it). No apply, deploy, invoke, `s3 cp`/`put`/`rm`, `safe-deploy`, no lambda call. Read-only `get`/`list`/`head`/`describe` only.
2. **No product file changes.** Your only writes are the five record files the instrument creates in your `run/` directory, your proof instance, the order's status flip and surprise rows. Never edit
   `r7_cn_n_1.py`, the consolidator, the spine or any test. Never add a QA prefix, key, table, bucket or scratch object anywhere (a `lib/opal_naming.py` address kind for one does not exist, and a
   shadow output path is vetoed).
3. **Never commit the A4 bodies**: the instrument keeps them in a temp directory and deletes them; commit only the five named record files.
4. **CLIENT DATA:** never print an account id or paste a level into a row or report; report counts, names of keys and the instrument's printed lines. No non-ASCII. Use the Edit tool.
5. QA, never production evidence: say so in your report. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-n-1.refusal-arm-qa-run.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (`apply_global_min_firms_fold`, `guard_global_min_firms_fold`, `build_all`, `lambda_handler`),
`data/mdpf/scripts/gold/build_mdpf_spine.py` and the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/`.

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py" grade --run-dir "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run"; echo "exit=$?"</invocation><expect>ROUND 7 CN-N-1 GRADE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py" served --run-dir "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/run"; echo "exit=$?"</invocation><expect>ROUND 7 CN-N-1 SERVED: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_n_1.py" guard; echo "exit=$?"</invocation><expect>ROUND 7 CN-N-1 GUARD: 5 of 5 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC3 is the difference control for AC1: the same guard, over the served unfolded objects of 2026-10-09, folds when unplanted and refuses when planted, so AC1's refusal is the plant's doing and not the
data's. There is no judgment criterion: the record is QA, and the organic one-firm day stays the negative arm.

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~21/MDPF_CANON.TO-CN-n-1.refusal-arm-qa-run.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes. Commit with `.tools/safe-commit.sh` naming exactly: the order, the instance, and the five record files
(`run/qa_run.json`, `run/qa_run.log`, `run/served_before.json`, `run/served_after.json`, `run/s3_ops.json`).

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W21-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the `QA run done` line, the output line of every criterion, the arms that printed, the commit hash, and any row. State that the record is QA and not production evidence.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, issuer 2.0.0_SA_COO~D1, on the CTO's round-6 analysis (`ledger/ROUND_ANALYSIS.round6.md` @65bf603a7a, section 3 item 3 and section 4 item 4): "the refusal arm,
DRIVEN: one QA run of the gold consolidator over a COPY of the inputs with a single-firm pool planted, writing to a QA prefix only. Arms: Global is refused WHOLE; the prior Global object's
VersionId is unchanged (the served prefix is listed before and after: 0 writes); the run logs the refusal. QA, never production evidence (CLAUDE.md)."
- **Findings that shaped the cell (read at HEAD, not asserted):** (1) `lambda_handler` documents QA-local mode as ZERO S3 writes with "no scratch S3 prefix -- the shadow-prefix veto", so the "QA prefix" is met
  as no prefix; (2) `lib/opal_naming.py` carries no QA, scratch or ephemeral address kind (a case-insensitive search returned nothing), so a QA prefix could not be built under Rule 30 anyway; (3) the refusal at
  `apply_global_min_firms_fold` step 6a fires BEFORE the differential identity, so the plant (blanking other firms' fold lines on the last date) reaches it without breaking the headline arrays; (4)
  `build_all` under `dry_run` still performs S3 READS (feeds, the tax prelude if configured, the cottonwood family, A7), so the run is not offline and its duration is UNMEASURED: the issuer did not run `drive` (a
  directive of the drafting fork) and ran `selftest`, `guard`, `grade` and `served` (at base) and `plan` only.
- **Unsettled:** whether `build_all` runs to completion on DELL1 inside the worker's shell limits (credentials for the cottonwood and firm feeds, the tax prelude disabled because its capability env is unset
  locally, `pyarrow`). If it does not, the record is a finding row and the arm is driven offline by AC3 only; the cell then re-cuts as a CloudOps `qa_local` invoke (the deployed handler's documented mode,
  `ADHOC.canon-r6-fold-deploy` leg D4), which would need an invoke event with a planting hook the deployed code does not have, so the offline guard run would remain the evidence. The issuer may prefer to run
  `drive` itself (the instrument is its own) and skip the worker; the CTO's text says "cell", so it is cut as one.
- **Direct-act:** the cell is LOCAL with zero product lines, so it takes the DIRECT-ACT path (`<direct_act>true</direct_act>`): a worker executes it, it drains, it runs no L2, L4-R or L8-L10; its close is the issuer's
  re-read of `grade`, `served` and `guard` on the committed record.
- **Not in this cell:** the organic one-firm day (read when it occurs); any change to the guard, the fold or the lambda; the CloudOps deploy of anything.
- **Pair:** none. The blast radius is empty: the instrument blocks every non-read call, and the served prefixes are listed before and after, plus a live head of the prior Global ts by key and VersionId.
- **Risk and class:** LOCAL. `worker` (not light): one run that may need diagnosis before a finding row.
- **Fanout:** one cell, one chain, slot ~21. Base box/dell1.

<status>pending</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-n-1</to_id>
<slot>~21</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
