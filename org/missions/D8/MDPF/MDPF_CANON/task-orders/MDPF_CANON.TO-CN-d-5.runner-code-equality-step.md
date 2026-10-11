# MDPF_CANON task order -- `CN-d-5` -- THE RUNNER'S `code/` EQUALITY STEP (W9-S7, the repo-side half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-d-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~14</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added; the tool is read-only and run by a deploy act. NO scheduled sync job is built (the CTO's ruling, round-3 analysis section 2, W9-S7).
comp-iam: DECLARED-NOT-APPLICABLE -- the tool only lists and reads `s3://opal-data-mdpf/code/`; no grant is added.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r4_cn_d_5.py tool 0 of 5 and live 0 of 2 at base; a reference tool and document read tool 5 of 5 and live 2 of 2 (the arms can pass; a tool that calls put_object reads REUSE-READONLY FAIL).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-d-5` (round 4, decomposition v4)

The MDPF daily runner executes the code it pulls from `s3://opal-data-mdpf/code/` with two `aws s3 sync ... --delete` lines
(`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`, the lines that sync `${CODE_PREFIX}/scripts/` and `${CODE_PREFIX}/config/`;
`CODE_PREFIX="code"`, `MDPF_BUCKET="opal-data-mdpf"`). A repo change reaches the runner only when a deploy act copies the changed file there.
Scripts have such an act (`.tools/safe-deploy.sh`, driven by `CODE_TREES["mdpf"]` in `.tools/safe_deploy_core.py`, `.py` files in the
layers `gold`, `backfill`, `feeders`, `bronze`). Config files under `data/mdpf/config/` have none, and nothing prints whether `code/` equals
the repo. The CTO ruled: the copy is a STEP of the deploy act, and the step prints content equality between `code/` and the repo for both
trees; no scheduled sync job. This cell builds the printing instrument and writes the step down. A CloudOps act (not yours) then runs it.

Create exactly two NEW files. You edit nothing that exists.

### 1.1 `.tools/mdpf-code-equality.py` -- READ-ONLY

Contract (the issuer's check `r4_cn_d_5.py` asserts each line of it):

```
python .tools/mdpf-code-equality.py                         # every tree: one table each, then ONE summary line; exit 0
python .tools/mdpf-code-equality.py --files <repo path> ...  # grade only these: exit 1 if any is not EQUAL; exit 2 REFUSED
```

- **Root.** `ROOT` = `git rev-parse --show-toplevel` (run with the inherited working directory), falling back to the parent of the tool's own
  directory. Put `<ROOT>/.tools` on `sys.path` and `import safe_deploy_core as core`. Type no absolute path.
- **The trees, read and never retyped.**
  - Script trees: for `layer, (home, prefix)` in `core.CODE_TREES["mdpf"]["layers"].items()`, skip a layer named in
    `core.CODE_TREES["mdpf"].get("shared_repo_homes", ())` (those two homes are another tree's); the bucket is `core.CODE_TREES["mdpf"]["bucket"]`.
    That gives four trees: `data/mdpf/scripts/{gold,backfill,feeders,bronze}` -> `code/scripts/<layer>/`.
  - The config tree: repo home `data/mdpf/config` (a module constant, with a comment citing the dispatch sync line), S3 prefix READ from the
    dispatch file at run time: `CODE_PREFIX` from the line `CODE_PREFIX="..."` and the sub-prefix from the `aws s3 sync "s3://${MDPF_BUCKET}/${CODE_PREFIX}/<sub>/"`
    line whose destination ends `/../config/`. Result `code/config/`. If either line is unreadable, print `REFUSED: ...` and exit 2: no default.
    A function `runner_config_prefix(dispatch_path)` does this.
  - The tool contains NO string literal beginning `code/scripts` or `code/config`.
- **`compare_tree(local_dir, bucket, prefix, s3) -> dict`** (module-level; takes the S3 client as an argument so it can be tested with a fake that
  offers only `get_paginator("list_objects_v2").paginate(Bucket=, Prefix=)` returning pages with `Contents` of `{"Key","ETag"}`):
  - local files: every file under `local_dir` recursively, relative POSIX path, skipping a directory named `__pycache__` and any `*.pyc`;
    content hash = md5 of the bytes;
  - remote objects: every key under `prefix` (paginate), name = key minus the prefix, ETag with the quotes stripped;
  - returns `{"local": <count>, "equal": [...], "differ": [...], "missing_on_s3": [...], "extra_on_s3": [...], "undetermined": [...]}`, every list
    sorted: a local file absent remotely is `missing_on_s3`; a remote name with no local file is `extra_on_s3`; a remote ETag containing `-`
    (multipart) is `undetermined` and NEVER `equal`; ETag == md5 is `equal`; otherwise `differ`.
- **Output** (ASCII only), per tree in the order above then config:
  `TREE <home> -> s3://<bucket>/<prefix> | local <n> | EQUAL <e> | DIFFER <d> | MISSING_ON_S3 <m> | EXTRA_ON_S3 <x> | UNDETERMINED <u>`
  then one indented line `  DIFFER <name>` / `  MISSING_ON_S3 <name>` / `  EXTRA_ON_S3 <name>` / `  UNDETERMINED <name>` for each name; then ONE final line
  `MDPF-CODE-EQUALITY: trees <T> | files <N> | equal <E> | not_equal <K>` (with `| named <n> | named_not_equal <k>` appended under `--files`).
  Print every denominator; never a percentage.
- **`--files`**: each name is a repo-relative path. Resolve it to the tree whose `home` is its longest prefix; if any name is under no tree,
  print `REFUSED: not under any runner code tree (nothing read): [...]` and exit 2 BEFORE any S3 call. Otherwise grade as above (exit 1 when a
  named file is not `equal`).
- **Never writes.** No `put_object`, `upload_file`, `copy`, `delete_object(s)`, no `aws s3 cp|sync|rm|mv`. It uses `boto3` read calls only and
  the default credential chain, region `us-east-1`.
- The module docstring states, in plain words: what it compares, that it never repairs, how equality is decided, and the two exit codes.
- It must pass `python -m py_compile` and `ruff check --target-version py39`.

### 1.2 `docs/deployment/MDPF_RUNNER_CODE_SYNC.md` -- the step, written down

A short document (under 60 lines, LF endings) that a deploy actor follows. It MUST contain these exact strings, each as written:
`## ORDER OF ACTS`, `## SEQUENCING`, `mdpf-code-equality.py --files`, `Named files only`, `No scheduled sync job`. Its content:

- **What reaches the runner:** the two sync lines; a repo change reaches the runner only by a deploy act's copy; `--delete` reverts a file
  placed on the runner by hand (the S3 object is the durable one).
- **ORDER OF ACTS** for any deploy that ships a change under `data/mdpf/scripts/` or `data/mdpf/config/`: (1) open the change-management
  entry naming every file by repo path; (2) scripts through `bash .tools/safe-deploy.sh <files>`; a config file by recording the prior
  object's ETag and VersionId then one `aws s3 cp` of that file to `s3://opal-data-mdpf/code/config/<name>`. Named files only: the act never
  copies "every differing file"; (3) read back `python .tools/mdpf-code-equality.py --files <the named repo paths>` and close the ledger legs
  on its output (exit 0 = every named file EQUAL); (4) print the whole-tree view, `python .tools/mdpf-code-equality.py`, and attach it to the entry.
- **What the tool is and is not:** read-only; a DIFFER or MISSING_ON_S3 name is a fact about the tree, and a repo file that is not a runner
  member (a test, a QA tool, a file a bundle ships) is expected to read so. Equality of the whole tree is not a goal; every named file EQUAL is.
- **SEQUENCING:** the tool may run at any time; an act that names a file another open deploy order also names waits for that order's ledger to
  read CLOSED; two acts never copy the same key in one window, and the second reads the first's ledger and the object's VersionId before it
  writes.
- State that **No scheduled sync job** exists or is to be built.

## 2. BOUNDS

1. **No AWS write of any kind**, not from the tool, not from a test, not by hand while building it: read-only `get`/`head`/`list` only. No
   install, no push, no deploy. REFUSE, do not rescue.
2. Only the two files in section 3 are created (plus your deliverables and the surprise channel). Do NOT edit `.tools/safe_deploy_core.py`,
   `.tools/safe-deploy.sh`, `.tools/test_code_trees_invariant.py`, the dispatch script or the issuer's checks: the deploy core is a gated
   tool another seat owns; if you conclude it must change, file a row and stop on that item.
3. **Never** build a scheduler, a monitor, an alarm or a notification, and never a standing comparator beside the deploy (the tool is run by
   a deploy act, on demand).
4. **CLIENT DATA:** the tool prints file names and counts only.
5. No non-ASCII. LF endings. Use the Write tool for the two new files.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
.tools/mdpf-code-equality.py
docs/deployment/MDPF_RUNNER_CODE_SYNC.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~14/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `.tools/safe_deploy_core.py` (`CODE_TREES`), `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`
(the `CODE_PREFIX` assignment and the two sync lines), and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_5.py` (never edit it; read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-d-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_5.py" tool; echo "exit=$?"</invocation><expect>ROUND 4 TOOL: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-d-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_5.py" live; echo "exit=$?"</invocation><expect>ROUND 4 LIVE: 2 of 2 arms -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~14/MDPF_CANON.TO-CN-d-5.runner-code-equality-step.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, and only when both criteria pass.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W14-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the two files (one line each), the output line of every criterion, the commit hash, and any row. Paste the tool's final
`MDPF-CODE-EQUALITY:` line and the five `TREE` lines from one real run (names only; no figure).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = `ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 item 4 (W9-S7). This is the repo-side half; the WORLD half is a
CloudOps ADHOC order the issuer cuts at the drain (below). Written as option (a) on measurement:
- **The deploy path already exists for scripts** (`safe-deploy.sh` over `CODE_TREES["mdpf"]`); what is missing is (i) any path for the
  config files, which `file_to_s3_target` refuses because it admits `.py` only, and (ii) a tree-wide equality print. Editing
  `safe_deploy_core.py` to admit non-script files means changing `file_to_s3_target`, `resolve_tree_layer`, `detect_script_files` and the
  six-layer invariant test of a NEVER-law gate owned by CloudOps: not a cell for a light worker. This cell therefore creates two new
  files and leaves the core alone; a core change, if CloudOps wants one, is its own order.
- **Measured 2026-10-11 ~05:3xZ, read-only (md5 against ETag, tests directories excluded locally):** gold 35 local, 23 equal, 4 differ
  (build_portal_gold_accrual.py, mdpf_model_registry.json, taxsma_assets.py, taxsma_reconcile.py), 8 missing; backfill 11/6/2/3; feeders
  5/3/1/1; bronze 2/2/0/0; config 4/2/0/2 (partner_roster.json, route_bindings_tieout.py). `code/` is not "about 20 commits behind" for the
  scripts the chain runs; most non-equal names are not runner members (tools, QA, a bundle-shipped file, a non-.py data file). The CTO's close
  "code/ reads equal" is therefore restated for the ADHOC: every file the dispatch chain executes or reads is EQUAL, and every other
  non-EQUAL name is listed with its reason. This is the fork the issuer carries to the CTO in the round-4 message.
- **Sequencing against `MDPF_STRATID.TO-APPLY-R2.global-fold-deploy` (PENDING, CloudOps ~DELL1):** that order ships three named files
  (`mdpf_gold_consolidator.py`, `mdpf_category_registry.py`, `build_cottonwood_mdpf_slice.py`) to `code/scripts/gold/` and
  `code/scripts/assets_gold/` through the push gate, then the Lambda (D2), under a signed never-widen pair, its own ledger and its own
  rollback handles. The step this cell writes down copies NAMED FILES ONLY and never "every differing file", so it cannot overwrite R2's keys
  unless the ADHOC names them. The ADHOC names only config files and any script R2 does not name. The tool itself is read-only and may run
  between R2's steps, and R2's step 3 read-back may use `--files` as its proof. Cutting the ADHOC to run before R2 closes is allowed only on
  disjoint names; a shared name waits for R2's ledger to read CLOSED.
- **The ADHOC (issuer, at the drain; WORLD, CloudOps ~DELL1):** (1) run the tool whole, attach the print; (2) classify every non-EQUAL name
  as deploy-now / deliberate (bundle, QA, test, non-code) / row; (3) deploy ONLY the config files the runner reads
  (`route_bindings.yaml` is EQUAL; `partner_roster.json` is superseded by the accrual bundle per `safe_deploy_core.py` and stays absent;
  `route_bindings_tieout.py` is a QA tool) and any script the chain executes that is MISSING; (4) read back with `--files`. The ledger names
  every key and the prior ETag/VersionId.
- **Risk and class:** LOCAL (no `infra/` path, no deploy verb in an invocation). `worker-light`: two new files of about 120 and 40 lines.
- **Fanout:** independent of every other round-4 cell (disjoint write set; no edge); slot ~14, a chain of one.
- Base box/dell1. LF only.

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-11 ~06:2xZ, row MDPF_CANON-D1-W13-S1):** the proof instance is named beside the order's own file stem, `MDPF_CANON.TO-CN-d-5.runner-code-equality-step.proof_of_spec.json`, because the pipeline gate searches for `<order file stem>.proof_of_spec.json`; section 5's path is corrected, no criterion or path of the grant changes. Gate limb: only GATE (viii) grades a modification, and `<placeholders>` is NONE.

<status>pending</status>
<round>4</round>
<to_id>MDPF_CANON.TO-CN-d-5</to_id>
<slot>~14</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
