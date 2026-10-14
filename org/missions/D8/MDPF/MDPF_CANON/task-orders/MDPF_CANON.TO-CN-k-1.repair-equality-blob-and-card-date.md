# MDPF_CANON task order -- `CN-k-1` -- TWO READ-SIDE REPAIRS: THE EQUALITY TOOL COMPARES THE GIT BLOB (D1-S23), AND THE /PORTFOLIOS CARD TOOL READS THE RUN DATE AND SAYS WHAT IT READ (D1-S24)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-k-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~22</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; two read-only operator tools change how they read and print.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added: both tools already list and get from S3 with read-only calls; the criteria make the same read-only list/get/head calls.
comp-adversary: RUN by a fork of the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r7_cn_k_1.py tool 3 of 6 at base (T2, T3, T6 are controls), card 1 of 5 at base (C4 a control); the scratch reference copies read 6 of 6 and 5 of 5; two planted card defects (default = the previous run, no WARN) turn C1/C5 and C3 red; r4_cn_d_5.py tool reads 5 of 5 at base and on the reference.
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-k-1` (round 7, decomposition v7; direct-act: LOCAL, about 110 product lines)

Two small repairs to two read-only tools. Neither tool writes anything; both keep every output they print today except the lines named below.

### Part A -- `.tools/mdpf-code-equality.py` compares the committed blob, not the working tree (row D1-S23)

**The defect.** `compare_tree` decides EQUAL by `remote ETag == _md5_file(local file)`, which hashes the WORKING-TREE bytes. On a CRLF checkout a file whose
git blob equals the S3 object byte for byte reads DIFFER (`data/mdpf/scripts/gold/mdpf_model_registry.json`: S3 and blob md5 begin `6b89cc935c`, a CRLF
working copy `fa784dd4ab`). The deploy path is not at fault: `.tools/safe_deploy_core.py` `_index_blob` (about :851) uploads the INDEX BLOB. This tool must read
the same bytes the deploy serves.

**The repair, exactly.**
1. A function that returns the md5 of the bytes git has recorded for a local file: run `git -C ROOT show :<path relative to ROOT, forward slashes>`
   (subprocess list argv, bytes, no text decoding, no newline translation), hash the stdout. `ROOT` is the module-level `ROOT` the tool already has; the
   function must read it AT CALL TIME (the issuer's check points `ROOT` at a temp repository). Return None when git exits non-zero (no index entry) or when the
   relative path begins `../` (the file lies outside ROOT). Never fall back to the working tree on any other failure.
2. In `compare_tree`, for each name present on both sides with a non-multipart ETag: the digest is the blob md5 when the function returns one, else the
   working-tree md5 (`_md5_file`, kept). Classify EQUAL/DIFFER as today. The returned dict gains two keys and keeps every existing key:
   `res["basis"]` = `{name: "blob" | "worktree"}` for every name compared, and `res["worktree_cr"]` = `{name: n}` for every name that is EQUAL with basis
   "blob" and whose working copy holds `n > 0` CR bytes (`b"\r"` count). Names MISSING_ON_S3, EXTRA_ON_S3 and UNDETERMINED are as today.
3. `named()` prints, for an EQUAL name: `NAMED EQUAL (blob) <path>` or `NAMED EQUAL (worktree) <path>`, followed by ` worktree_cr=<n>` when the name is
   in `worktree_cr`. The `NAMED NOT_EQUAL <label> <path>` line, the `TREE` lines, the summary lines and every exit code stay exactly as they are.
4. Update the module docstring paragraph "HOW EQUALITY IS DECIDED" to say so (index blob; working tree only for a path with no index entry; the basis and
   CR count printed). Keep the "WHAT IT NEVER DOES" paragraph true: no new AWS call, no write. Do not add any `aws s3 ...` string or `code/scripts` or
   `code/config` literal to the file (an existing check refuses both).

**Test (new file, no network): `.tools/tests/test_mdpf_code_equality_blob.py`, EXACTLY THREE pytest tests.** Each builds a temp git repository
(`git init`, `-c core.autocrlf=false -c user.name=t -c user.email=t@t`, commit via a list-argv subprocess; strip `GIT_*` from the environment), loads the
tool with `importlib` (the file name has a hyphen), sets the loaded module's `ROOT` to the temp repository, and calls `compare_tree(<dir>, "b", "p/", fake)` where
`fake` is a small object whose `get_paginator("list_objects_v2").paginate(Bucket=, Prefix=)` yields one page `{"Contents": [{"Key": ..., "ETag": '"<md5>"'}]}`.
(1) `test_crlf_working_file_equal_by_blob`: LF blob committed, working copy rewritten CRLF, ETag = md5 of the LF bytes -> the name is in `equal`, `basis`
is "blob", `worktree_cr` equals the CR count. (2) `test_true_difference_stays_differ`: ETag of other bytes -> `differ`. (3) `test_no_index_entry_reads_the_working_tree`:
an untracked file whose ETag = md5 of its working bytes -> `equal`, `basis` "worktree", no `worktree_cr` entry.

### Part B -- `portfolios_card.py` reads the run date by default and prints what it read (row D1-S24)

**The defect.** `portfolios_card.py after --date D` takes the newest key `<= D` for each of three object types. The account-distribution is keyed by RUN date
(the scheduled fire's date, 2026-10-14) while aum-metrics and aggregate-aua-timeseries are keyed by the frontier date (2026-10-13). The issuer passed the frontier
date and the tool read the PREVIOUS run's distribution: Total Holdings printed 8,607 where the served truth is 8,430. Nothing in the output showed the wrong date.

**The repair, exactly (file: `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py`).**
1. `main(argv=None)` and `ap.parse_args(argv)` (the issuer's check calls `main([...])`).
2. `after --date` becomes optional. With no `--date`, D is the date of the NEWEST `account-distribution` key under the A4 prefix (a new function that lists the keys
   with the existing `a4_keys(c, "account-distribution")` and takes `key[-1]`'s file-name date; no keys -> `SystemExit` with a message). Reason for this default and
   not "today UTC": the distribution is the one run-date-keyed type, so its newest key is the latest run by construction; a wall-clock default silently reads the
   previous run on every day before the 13:30Z fire, which is exactly this defect's shape.
3. After computing, and BEFORE any other output, print as the FIRST line of stdout, exactly this shape (one line, single spaces):
   `PORTFOLIOS-CARD READ date=<D> (<how>) account-distribution=<key> aum-metrics=<key> aggregate-aua-timeseries=<key>` where `<how>` is `explicit` when
   `--date` was given and `default: newest account-distribution key` otherwise, and each `<key>` is the full S3 key chosen (`res["objects"][type][0]`).
4. When the source is `a4` and the account-distribution listing holds a key whose file-name date is greater than D, print a second line:
   `WARN: a newer account-distribution key exists (<file name of the newest>); the objects after <D> were NOT read`.
5. Everything else in the output, the `before` subcommand, the pinned snapshot logic and every number stay as they are. Update the module docstring (the
   `after` entry and the "Run after a fire" example) to say the date is optional, what the default is and what the first line states.

## 2. BOUNDS

1. **No AWS write of any kind.** Read-only `get`/`list`/`head` only (the criteria make such calls). No install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). **Never** edit `r7_cn_k_1.py`, `r4_cn_d_5.py`,
   `portfolios_card_before.snapshot.json`, `docs/deployment/MDPF_RUNNER_CODE_SYNC.md`, `safe_deploy_core.py` or any file under `data/mdpf/`.
3. The equality tool stays read-only and keeps its single `git` use to the one `show` call above; it adds no AWS call, no write verb, no `s3` argv pair.
4. **CLIENT DATA:** never print an account id. No non-ASCII in any file. Keep each file's line endings as you find them (both tools are LF; read first).
   Use the Edit tool. The tests and the issuer's checks build their own temp repositories, so a CRLF or LF checkout does not change their result.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
.tools/mdpf-code-equality.py
.tools/tests/test_mdpf_code_equality_blob.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-k-1.repair-equality-blob-and-card-date.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~22/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `.tools/safe_deploy_core.py` (`_index_blob`), the issuer's checks
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_k_1.py` (read what each arm asserts; never edit it) and
`.../round4/checks/r4_cn_d_5.py`.

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_k_1.py" tool; echo "exit=$?"</invocation><expect>ROUND 7 CN-K-1 TOOL: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_k_1.py" card; echo "exit=$?"</invocation><expect>ROUND 7 CN-K-1 CARD: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest ".tools/tests/test_mdpf_code_equality_blob.py" -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>3 passed -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_5.py" tool; echo "exit=$?"</invocation><expect>ROUND 4 TOOL: 5 of 5 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC4 is the one criterion over the three-criterion norm, with its reason: it is the existing CN-d-5 guard of the unchanged `compare_tree` contract (classes, refusal of an unmapped name, no write verb) that every deploy act's read-back depends on. There is no judgment criterion: the cell is LOCAL, read-only and on the direct-act path; its close is the issuer's one real run.

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~22/MDPF_CANON.TO-CN-k-1.repair-equality-blob-and-card-date.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your
proof instance** (the order file is in your paths), and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W22-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, issuer 2.0.0_SA_COO~D1, on the CTO's round-6 analysis section 4 items 1 and 5 (`ledger/ROUND_ANALYSIS.round6.md` @65bf603a7a: "the D1-S23
repair" and "D1-S24: portfolios_card.py defaults to the documented run date, and prints the date it read on its first line"). The CTO batched the repairs; both are
READ-SIDE tools, so one cell serves them.
- **D1-S23, corrected (design note `round7/draft/CN-k-1_DESIGN_NOTE.md`):** the row's worry that a CRLF checkout could WRITE CRLF bytes is wrong, because
  `safe_deploy_core.py:874-917` uploads the index blob and asserts the ETag against it; only the equality tool's READ side is wrong (a false DIFFER). Measured at the
  cut (this draft): `mdpf_model_registry.json` blob md5 `6b89cc935c` = S3, working copy (CRLF, 18 CR) `fa784dd4ab`; `bronze_homes.json` blob `77da011842` against S3
  `b2d27b65d2` is a TRUE difference and must still read DIFFER; three EQUAL names (`mdpf_revamp_model_crosswalk.py`, `mdpf_calendar_binding.py`,
  `taxsma_membership.py`) are chosen as stable controls because no round-7 cell touches them.
- **D1-S24, the cause (the issuer's own read):** the round-6 drain-end packet quoted Total Holdings 8,607 -> 8,607 from `after --date 2026-10-13`. The distribution key
  for the 2026-10-13 run date is the PREVIOUS run's; the 2026-10-14 key holds 8,430 (R7 of the readback printed `total new=8430` and the packet did not connect it). The CTO
  corrected it to -177 in the round-6 analysis section 2.
- **Why the checks are tree-independent:** a worker's fresh worktree has LF working files, so an arm that relied on the main checkout's CRLF `mdpf_model_registry.json`
  would pass at the base there. Every tool arm builds a temp git repository with an LF blob and a CRLF working copy (T5 does it with the real file's HEAD blob and
  the real S3 ETag, read-only). The card arms use a fake client for the structure and the real objects for C5 (the default date equals the newest real key).
- **Base results (each dry-run from `round7/draft/checks/` before the cut):** AC1 `tool` at base: T1 FAIL, T2 PASS (control), T3 PASS (control), T4 FAIL, T5 FAIL,
  T6 PASS (control) = 3 of 6, as expected; scratch reference `round7/draft/checks/ref/mdpf_code_equality_ref.py` = 6 of 6. AC2 `card` at base: C1 FAIL (argparse
  requires --date), C2 FAIL, C3 FAIL, C4 PASS (control), C5 FAIL = 1 of 5; reference `ref/portfolios_card_ref.py` = 5 of 5; mutants: default = the previous run turns C1 and
  C5 red, a missing WARN turns C3 red. AC3 is the worker's own file (absent at base, so it fails by construction). AC4 reads 5 of 5 at base and on the reference
  (a regression guard that must stay green).
- **Sensitivity the worker cannot see:** T5 and T6 read the live S3 `code/` prefixes; they assume `mdpf_model_registry.json`'s S3 object still equals its HEAD blob and
  that `bronze_homes.json` still differs. If a CloudOps sync changes either between the cut and the run, the arm names the changed premise (T5) or fails honestly (T6);
  that is the issuer's to re-read, not a worker defect.
- **Risk and class:** LOCAL, DIRECT-ACT (about 110 product lines: tool about 25, test about 60, card about 25), `worker-light`. No pair, no deploy: the card tool is the issuer's
  own instrument and the equality tool is an operator tool; neither changes a served byte.
- **Fanout:** one cell, one chain, slot ~22. No shared file with `CN-h-1`, `CN-i-1`, `CN-j-1` (their owned files are gold scripts, portal files and the publisher). Base box/dell1.

<status>pending</status>
<direct_act>true</direct_act>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-k-1</to_id>
<slot>~22</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
