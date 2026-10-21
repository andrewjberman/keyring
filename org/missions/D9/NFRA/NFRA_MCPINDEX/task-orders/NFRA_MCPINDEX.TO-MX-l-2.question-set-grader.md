# NFRA_MCPINDEX task order -- `MX-l-2` -- a grader for the fixed FWD-26 question set: did the run pick the right folder and table from the index, without listing the bucket first

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round28-GATEWAY.md</decomp_doc>
<owned_cells>MX-l-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-l-2.question-set-grader</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~98</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one new script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant. The script reads two local JSON files and writes one.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base: the script is absent) and the planted mutants inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-l-2` (round 28, workstream GATEWAY; PRD v0.20 FWD-26, signed and admitted; CTO round-27 analysis `ledger/ROUND_ANALYSIS.round27.md` item 2)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). FWD-26 says: for a plain-words question about Schwab, Orion or Cottonwood Black Diamond, Claude picks the right folder and table from the index WITHOUT listing the bucket first. The issuer wrote a fixed set of 12 plain-words questions, each with its expected folder and table. You build the NEW script `workflows/gateway_battery/fwd26_grade.py` that grades a run's picks against that set, and its test file `workflows/gateway_battery/tests/test_fwd26_grade.py`. The script never calls the gateway and reads no AWS data; it reads two local JSON files and writes one.

**The question set** is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/evidence/FWD26_QUESTION_SET.json` (`fwd26_questions/1`). Read it first. Its top level holds `schema`, `catalog_md5_read` (32 hex characters), `needs_candidate_e_served` (a list of question ids, today `["O3"]`), `grade_rule`, `count`, `items`. Each item holds `id` (S1..S4, O1..O4, B1..B4), `vendor`, `firm`, `question`, `expected_table`, `expected_locations` (a list of `{bucket, prefix, catalog_entity, size}`; S1..S4 list one folder per Schwab master, so any master passes), `accept_also` (a list of `{bucket, prefix, catalog_entity, reason}`; only O1 has one, the folder the catalog says has identical content), `size_classes_proposed` and other fields you carry no meaning from. The grade rule in its own words: a run passes a question when the FIRST folder and table Claude names, chosen from the index and without listing the bucket first, equals one of the expected locations (or an accept_also entry); a folder ending in `_s2` is a different source and fails; naming the right folder after a bucket listing fails.

### The contract (verbatim from the decomposition; it is the whole specification)

**L2 QUESTION-SET GRADER.** `python workflows/gateway_battery/fwd26_grade.py grade --questions FILE --picks FILE --out FILE [--served-md5 MD5]`. `--questions` is the `fwd26_questions/1` file; `--picks` is `fwd26_picks/1`: `{"schema","run":{"principal":str,"read_at":str},"picks":[{"id","bucket","prefix","table","listed_bucket_first":bool}]}` (one pick per question id; the run records for each question the FIRST folder and table named from the index). Verdicts per question, in this precedence: `missing_pick` (no pick for the id) FAIL; `listed_first` (listed_bucket_first true) FAIL even when the folder is right; `s2_folder` (the prefix's last segment ends `_s2`) FAIL unless the question's expected location itself ends `_s2`; `wrong_folder` (the (bucket, prefix) is in neither `expected_locations` nor `accept_also`) FAIL; `wrong_table` (the pick's table differs from the table of the matched location, taken from the location's last prefix segment) FAIL; else PASS. When `--served-md5` is given and does not equal the questions file's `catalog_md5_read`, a question listed in `needs_candidate_e_served` that FAILs `wrong_folder` or `missing_pick` is graded `not_served` (a FAIL that names the cause) instead. The output `fwd26_grade/1` holds per-question `{id, verdict, class, matched}`, `counts` (`questions`, `pass`, `fail`, `not_served`, per class) and the questions' `size_classes_proposed` carried through. Stdout `FWD26 questions=Q pass=P fail=F not_served=N`; exit 0 iff `fail` and `not_served` are 0, 1 otherwise, 2 on an unreadable or malformed input (a pick for an unknown id, a duplicate id, a non-bool `listed_bucket_first`). A second subcommand `ideal --questions FILE --out FILE [--mutate none|listed|s2|wrong-folder|wrong-table|missing]` writes a picks file in which every pick equals the first expected location (the control); each `--mutate` mode then applies exactly one defect to exactly the first question so the grader's refusals can be planted. Same input, same bytes.

### The settled silences (the issuer's rulings; follow them where the contract above is silent)

1. **Output shape.** Each item of the output is `{"id","verdict","class","matched","size_classes_proposed"}` and no other key. `verdict` is `PASS`, `FAIL` or `NOT_SERVED`. `class` is the FAILURE class: null for a PASS; one of `missing_pick`, `listed_first`, `s2_folder`, `wrong_folder`, `wrong_table` for a FAIL; `not_served` for a NOT_SERVED. `matched` is `{"bucket","prefix"}` of the matched expected or accept_also location (the normalized prefix, see 3) for a PASS and for a `wrong_table`, else null. `size_classes_proposed` is copied from the question (null when the question has none). The top level is `{"schema":"fwd26_grade/1","run":<the picks file's run object, or {} when absent>,"items":[...],"counts":{...}}`. `counts` has exactly the keys `questions`, `pass`, `fail`, `not_served` and `by_class`; `by_class` has exactly the six keys `missing_pick`, `listed_first`, `s2_folder`, `wrong_folder`, `wrong_table`, `not_served`, each the number of items with that class. `fail` counts the FAIL items only; `not_served` counts the NOT_SERVED items only; `pass + fail + not_served = questions`. Items are in the questions file's order. The file is JSON with `indent=1`, sorted keys, UTF-8, LF, one trailing newline.
2. **Validation, every failure is exit 2 with `REFUSED: ...` on stderr and NO output file** (an argparse error is not enough; the text must start `REFUSED:`): the questions file is not a readable JSON object, its `schema` is not exactly `fwd26_questions/1`, `items` is not a non-empty list, an item lacks a non-empty string `id` or `expected_table`, two items share an id, an item has no non-empty `expected_locations` list or a location lacks a non-empty string `bucket` or `prefix`; the picks file is not a readable JSON object, its `schema` is not exactly `fwd26_picks/1`, `picks` is not a list, a pick lacks a non-empty string `id`, `bucket`, `prefix` or `table`, a pick's `listed_bucket_first` is missing or not a bool, a pick names an id that is not a question id, two picks share an id; `--served-md5` is not 32 hexadecimal characters. A question with NO pick is not a refusal: it is `missing_pick`. Extra keys in a pick are ignored. No subcommand is exit 2.
3. **Comparison.** `bucket` is compared exactly. A `prefix` (a pick's and a location's) is compared after adding one trailing `/` when it has none; nothing else is normalized. A pick's `table` is trimmed of surrounding spaces and compared exactly with the LAST non-empty segment of the matched location's prefix (so an accept_also folder needs its own table name, not the question's `expected_table`). The `s2_folder` test looks at the last non-empty segment of the pick's prefix: it ends `_s2`. The exception ("unless the question's expected location itself ends `_s2`") applies when the last segment of any of the question's `expected_locations` ends `_s2`.
4. **`--served-md5`** is compared case-insensitively with the questions file's `catalog_md5_read`. When it is absent, or equal, nothing is graded `not_served`. The `not_served` grading applies only to ids in `needs_candidate_e_served`, and only to a question that would otherwise be a FAIL of class `wrong_folder` or `missing_pick`; a correct pick for such a question is a PASS whatever is served; every other question is graded as usual.
5. **`ideal`.** The control picks file is `{"schema":"fwd26_picks/1","run":{"principal":"ideal-control","read_at":"1970-01-01T00:00:00Z"},"picks":[...]}` (the fixed `run` makes the bytes repeat), one pick per question in the questions file's order, each the question's FIRST expected location (`bucket`, `prefix` as written in the file), `table` the last non-empty segment of that prefix, `listed_bucket_first` false; JSON as in 1. The mutations touch only the first pick: `listed` sets its `listed_bucket_first` true; `s2` appends `_s2` to the last segment of its prefix (keeping the trailing slash) and `_s2` to its table; `wrong-folder` replaces its bucket, prefix and table with the first expected location (and that prefix's last segment) of the NEXT question in file order (the last question wraps to the first); `wrong-table` appends `_x` to its table; `missing` leaves that pick out. `none` is the control. Stdout of `ideal` is `IDEAL picks=<n written> mutate=<mode>`, exit 0.
6. **Nothing else.** The script imports only the standard library, no AWS, HTTP or process library. A grade of a clean ideal file is exit 0 with `FWD26 questions=12 pass=12 fail=0 not_served=0`.

### Inputs you read (you do NOT edit them)

- The question set above, `workflows/gateway_battery/tool_battery.py` (for the house style of verdict names, exit codes and the `REFUSED:` stderr line) and `workflows/gateway_battery/size_census.py` (for the command-line conventions of a new script), and `workflows/gateway_battery/tests/test_tool_battery.py` (the model for a test file: the script is run by path as a subprocess on small inputs written inside the test with `tmp_path`).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. FIRST run `git sparse-checkout add workflows/gateway_battery workflows/atom_decomposition infra/aws/ec2/opal-gateway/app infra/aws/lambda/ci/function-map` (the only sparse change you may make; the issuer pre-adds them, and the command is harmless when they are there). Without them the cone can lack the question set's neighbours or the folder the naming gate reads, and the commit gate then prints NAMING ERROR.
1. Read the question set and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l2_check.py` (the executable form of this section; read what each arm grades). Write the script, then the test file: at least 8 tests of your own, on a small question set you write inside each test (not the real one): all pass; any master folder passes; an accept_also folder needs its own table; listed_first fails a right folder; s2_folder; wrong_folder and missing_pick; not_served only for the listed question and a different md5; malformed picks exit 2 and write nothing; the ideal control and its five mutants; same input, same bytes.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's question set, checks or decomposition, `tool_battery.py`, `size_census.py`, any other script or test under `workflows/`, `members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, or the round-23 to round-27 evidence. No AWS call, no network call, no grant, no deploy, no push. The criteria write their outputs under a temporary directory.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39, and it BLOCKS a strict-utf-8 `open()` of a path whose name or variable contains `log` or `catalog`: write `errors="replace"` on every `open()` you add for reading. The naming gate must exit 0 on your code commit; if it prints NAMING ERROR, add the sparse folders of step 0 and run it again before you commit.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script; tests under `tests/` and data files are exempt. (The script reads every id, bucket, prefix and table from the question set.)
4. The contract in section 1 and the settled silences are the whole specification. Where they are silent, do the smallest thing and say which in your report; do not widen the output (no new key in an item, no new option beyond `--served-md5` and `--mutate`).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l2.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `l2_check.py` in the same folder). Do not edit any of them. (The environment variable `L2_PKG_DIR` in the check is the issuer's; leave it unset.)
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/fwd26_grade.py
workflows/gateway_battery/tests/test_fwd26_grade.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~98/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-l-2.question-set-grader.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W98-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-l-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l2.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (the real question set, 12 questions, 20 expected locations); the ideal control writes one pick per question and grades FWD26 questions=12 pass=12 fail=0 not_served=0 with rc 0, every item PASS with the matched location; the five single-defect mutants (listed, s2, wrong-folder, wrong-table, missing) each fail exactly the first question with class listed_first, s2_folder, wrong_folder, wrong_table and missing_pick and the other eleven pass -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-l-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l2.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the nine refusals each exit 2 with REFUSED on stderr and no file; every master folder of a Schwab question passes; an accept_also folder passes with its own table and is wrong_table with the other; a prefix without its trailing slash passes; a wrong folder after a bucket listing is listed_first; the not_served arms (plain FAIL without a md5 and with an equal md5, NOT_SERVED with a different md5, a correct pick still PASS, an unlisted question still FAIL); two runs give the same bytes; no AWS or network library -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-l-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l2.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 8 passed) for `test_fwd26_grade.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~98/NFRA_MCPINDEX.TO-MX-l-2.question-set-grader.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The proof's `to_id` is the FULL order id `NFRA_MCPINDEX.TO-MX-l-2.question-set-grader` (the short id is read as a defect at the round close). The checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, and record the output so that `RESULT: PASS` is followed by `exit=0`.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. Message files are written with the Write tool, ASCII, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 28, workstream GATEWAY, worker ~98. Source: PRD v0.20 FWD-26 (signed and admitted, CVO review @a81f56eb3e, whose one note asked for the fixed question set), the CTO's round-27 analysis (msg 36317, `ledger/ROUND_ANALYSIS.round27.md` @f5f824c16e) item 2 and the ruling on the size thresholds (msg 36313). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round28-GATEWAY.md` (contract R28.3 L2, frozen at the cut). The graded RUN of the question set (a session of Claude picking from the served index with no bucket listing) is the issuer's drain act (R28.4 step 2), not this cell: the cell builds the grader. Settled silences 1 to 6 are the issuer's reading of the one-paragraph contract; the contract's per-item `class` means the failure class and its counts "per class" are `by_class`, the verdict set gains `NOT_SERVED`, a missing `listed_bucket_first` is a refusal, and a prefix without its trailing slash is normalized (one slash). Lessons carried from rounds 24 to 27: the sparse cone may lack folders (step 0, with the naming-gate folder); the commit gate blocks a strict utf-8 `open()` on a path whose name contains `log` or `catalog`; every mutant in the checks is planted from the real question set; the refusal arms require the script's own `REFUSED:` text; the proof's `to_id` is the full order id.
Base dry-runs 2026-10-21 (script and test file absent): `l2.AC1` base: FAIL as expected (1 of 12 arms ok: the control that the question set is the accepted 12); `l2.AC2` base: FAIL as expected (0 of 1: the ideal control cannot be written, so the refusal and acceptance arms do not run at the base); `l2.AC3` base: FAIL as expected (test file absent). The issuer's scratch reference (a standard-library script and a 13-test file outside the repository, pointed at with `L2_PKG_DIR`) passes all three (12 of 12, 25 of 25, 13 tests). Four single-defect copies of the reference each fail the check: one that ignores `listed_bucket_first` fails `l2.AC1` (the listed mutant) and `l2.AC2` (the precedence arm); one that never grades `not_served` fails `l2.AC2` (two arms); one that tests the wrong folder before the `_s2` folder fails `l2.AC1` (the s2 mutant); one that does not normalize the trailing slash fails `l2.AC2`.

<status>issued</status>
<round>28</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
