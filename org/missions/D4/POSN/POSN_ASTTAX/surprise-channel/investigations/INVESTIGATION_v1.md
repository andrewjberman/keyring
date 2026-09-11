# POSN_ASTTAX -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `0.9.0_WK_POSN_ASTTAX~1` at L7, task order `POSN_ASTTAX.TO-S1A-1`, 2026-09-11. **Home:**
the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only during the round.**

**Why this file is opened here.** The first row was found while writing the `S1a-AC5` comparison script
(loading `ETF_CLASSIFICATIONS` from `_shared/etf_classification.py` to scan it against the DynamoDB
table). It is a mismatch between what that module's own documentation asserts about its data and what
the data itself holds -- the step-7 trigger -- surfaced incidentally to AC5 and not itself one of the
order's twelve named criteria, so it is filed here rather than folded into an acceptance row.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W1-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~1",
    "surfaced_at": "2026-09-11T06:21:38Z",
    "one_line": "_shared/etf_classification.py documents its asset-class vocabulary as THREE values ('fixed_income', 'equity', 'other') but ETF_CLASSIFICATIONS never assigns 'other' to any of its 136 tickers -- 7 tickers (GLD, IAU, SLV, DBC, GSG, USO, VIXY) carry the undocumented value 'hedge' instead, which silently breaks the module's own is_hedge() helper.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/_shared/etf_classification.py:38-40 @e356d7c1d0: comment reads \"Categories: 'fixed_income', 'equity', 'other'\" immediately above ETF_CLASSIFICATIONS; the same three-value claim is repeated in get_asset_class()'s docstring at :925 ('Returns: Asset class: ...or 'other'').",
        "Measured live at the same commit: `Counter(ETF_CLASSIFICATIONS.values())` = {'fixed_income': 66, 'equity': 63, 'hedge': 7}, total 136 tickers -- zero occurrences of 'other', and a fourth, undocumented value 'hedge' used for GLD/IAU/SLV/DBC/GSG/USO/VIXY (etf_classification.py:237-244).",
        "HEDGE_TICKERS (etf_classification.py:288-291) is built as `{ticker for ticker, ac in ETF_CLASSIFICATIONS.items() if ac == 'other'}` -- since no ticker carries 'other', HEDGE_TICKERS is the empty set at runtime (measured: `ec.HEDGE_TICKERS == set()`), so `is_hedge('GLD')` returns False even though `get_asset_class('GLD')` returns 'hedge'.",
        "comp-find 'is_hedge' --all (vintage this session): 6 hits, all DEF/export/doc (three module copies' own definitions, _shared/__init__.py's re-export, README.md's one-line doc) -- no live pipeline call site found, so the break is currently DORMANT rather than actively mis-serving, which is why this is filed OBSERVATION/ARMED rather than BLOCKING."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "_shared/etf_classification.py's own header comment (line 40) and get_asset_class()'s docstring (line 925) both assert the asset-class vocabulary is exactly three values: 'fixed_income', 'equity', 'other'.",
    "world_is": "The live data never uses 'other' (0 of 136 tickers) and instead uses an undocumented fourth value 'hedge' for 7 tickers, which is also the value the DynamoDB-serving vocabulary (etf_classifications_dynamodb.py:91) and the live Positioning branch set (lambda_function.py:355-368, re-taken at S1a-AC7) both use -- so the dict's DATA already agrees with the wider FOUR-value live vocabulary; only its own COMMENT is stale, and that staleness is what breaks HEDGE_TICKERS/is_hedge().",
    "notes": "Not this order's to fix (READ-ONLY, no edit to either classifier module per BOUNDS). Relevant to a later cell reading this module for the class-edge work C-MEMBERSHIP-AT-L5 reserves: the DOCUMENTED category list should not be trusted over the DATA. Filed OBSERVATION because it did not block S1a-AC1..AC12; ARMED because a future caller of is_hedge() (dormant today, per the comp-find evidence above) would get silently wrong answers, and because a reader trusting the stale comment over the data could mis-scope the class-edge work."
  }
]
```

---

## Rows appended by `0.9.0_WK_POSN_ASTTAX~2` at L7, task order `POSN_ASTTAX.TO-S6-1` (cell `AT2-s-6`), 2026-09-11

Three rows, one fenced array, appended (never edited in place). `S1` and `S2` concern the generator
this order hardened -- `S1` its premise's line citations, `S2` the citations this order's own fix
invalidates for the six sibling cells held behind it. `S3` concerns the commit mechanism the order
mandates.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W2-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~2",
    "surfaced_at": "2026-09-11T12:37:56Z",
    "one_line": "TO-S6-1 cites the default guard at ':72,:81' of the positioning generator, but at this vintage there is exactly ONE 'value if value else default' guard and it sits at :66 inside registry_field(); old :81 is a CALLER of that guard and old :72 is a blank line, so S6-AC2's window (lines 68-84) does not contain the guard the criterion names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S6-AC2 invocation output, run verbatim at 2d8b5f7314 before any edit: sed -n '68,84p' infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py printed ETF_BETA_OVERRIDES (:74-77) and def classify_management_style (:79-81) -- no 'value if value else default' line anywhere in the 17-line window.",
        "Native Grep over the same file @2d8b5f7314 for 'if value else' returned exactly ONE hit, line 66: 'return value if value else default' (denominator: 1 hit, 1 file, whole file scanned), inside def registry_field (:53).",
        "Old :81 @2d8b5f7314 is \"return registry_field(ticker, 'management_style', 'passive')\" -- a CALL SITE that passes a default INTO the guard, not the guard itself; old :72 is an empty line (measured by indexing the pre-edit bytes).",
        "The guard's SHAPE was confirmed exactly as the order describes it (one 'value if value else default' expression, structurally unable to fire on the truthy string 'unknown'), so the order's premise held on substance and the fix proceeded un-improvised; only the two line numbers were wrong."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX.TO-S6-1's measured-by-the-issuer block asserts ':72,:81  \"value if value else default\"  -- CANNOT fire on the TRUTHY placeholder \"unknown\"', i.e. TWO guard sites at lines 72 and 81, and S6-AC2's invocation reads lines 68-84 to show them.",
    "world_is": "ONE guard site at :66 (inside registry_field), reached by BOTH classifiers (classify_etf :209 and classify_management_style :81) -- so a single edit at :66 fixes both paths, which is what this order did. Lines 72 and 81 are respectively a blank line and one of the two callers.",
    "notes": "Filed rather than folded into S6-AC2 because the criterion's INVOCATION is the thing that does not produce its NAMED RESULT: a grader re-running sed -n '68,84p' will not see a guard, at this vintage or any other. S6-AC2 is recorded with that window's verbatim output PLUS the :66 read that actually answers the question. INERT: the premise held on substance, the fix is landed and proved by S6-AC5, and no downstream consumer is left holding a wrong belief by this row alone -- the inheritable-citation hazard is carried separately by POSN_ASTTAX-Z-W2-S2."
  },
  {
    "id": "POSN_ASTTAX-Z-W2-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~2",
    "surfaced_at": "2026-09-11T12:37:56Z",
    "one_line": "This order's own fix inserts 30 net lines into the positioning generator, so EVERY line citation below :66 in the round-2 decomposition and in the six sibling task orders held behind this chain head is now stale by +10 or +30 -- including AT2-s-1's three cited lines (:209, :360, :520), which move to :219, :390 and :550.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "difflib.SequenceMatcher over the pre-edit bytes (git show HEAD:<path> @2d8b5f7314, 94164 bytes, 2268 lines) against the post-edit worktree bytes (96268 bytes, 2298 lines): delta +30 lines, from two opcodes -- insert at old :66 (new :66-75, +10) and replace of old :237-243 (new :247-273, +20).",
        "Citation map, old -> new, content-matched line by line: :66->:76, :81->:91, :207->:217, :209->:219, :221->:231, :228->:238, :360->:390, :520->:550, :1917->:1947, :1926->:1956. Old :239 and :243 (the two direct subscripts) no longer exist as such -- they are the lines this order replaced.",
        "TO-S6-1's BOUNDS name the shifted lines explicitly and attribute them to a LATER cell: \":209 defaults to fixed_income while :360 and :520 default to equity. That disagreement is AT2-s-1's cell, not yours.\" All three of those numbers are stale the moment this order commits.",
        "Positive control that the shift is real and not an artifact of the diff instrument: sed -n '218,246p' (S6-AC1's own invocation) no longer prints the two allocation dicts at those offsets -- post-edit the same region reads at 227-272, re-read verbatim and recorded in the S6-AC1 acceptance row."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round-2 orders and decomposition cite lines of infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py as fixed coordinates (TO-S6-1: :207-209, :221-226, :228-231, :239, :243, :1917, :1926, :360, :520), and the issuance holds six sibling cells behind this chain head so they are worked AFTER these bytes change.",
    "world_is": "Those coordinates are valid only at 2d8b5f7314. After this order's commit every citation below :66 is off by +10 (and below old :237 by +30). A sibling worker who navigates by the cited line number rather than by the named symbol will land on the wrong line -- and for AT2-s-1, which is a line-level edit to the very defaults this order's guard now makes reachable, that lands inside the comment block this order inserted.",
    "notes": "ARMED and pointed AT THE ISSUER because the exposure is created BY the sequencing the issuance chose (chain head edits the file, six held cells cite it) and the remedy is a one-line-each re-pin of the sibling orders before they are dispatched, or an instruction to navigate by symbol name rather than by offset. disarm_owner 2.0.0_SA_COO~Z as the author of the held orders; the citation map above is the whole input the disarm needs. Not a defect in this order's fix, and nothing here asks for the fix to be reshaped."
  },
  {
    "id": "POSN_ASTTAX-Z-W2-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~2",
    "surfaced_at": "2026-09-11T12:37:56Z",
    "one_line": "The Rule-14 commit gate (.tools/commit-gate.sh, universal, fail-closed, no --force bypass) CANNOT RUN in a cone-mode sparse worktree: commit_gate_runner.py imports five modules from org/modules/graph + compproof and reads comp-constants.config.yaml from the workspace root, and org/modules/graph is outside the cone this round's worktrees use -- so a .py commit from such a worktree is refused by a gate CRASH, not by a finding about the code.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured in this worktree (/c/tmp/wk-posn-s6, branch wk-posn_asttax-2-6 @2d8b5f7314): timeout 120 bash .tools/commit-gate.sh <the one edited .py> printed \"ModuleNotFoundError: No module named 'comp_constants_cli'\" raised from .tools/commit_gate_runner.py:96, and exited rc=1.",
        ".tools/commit_gate_runner.py:79-81 sets GRAPH_DIR = WORKSPACE/org/modules/graph and COMPPROOF_DIR = GRAPH_DIR/compproof, inserts both on sys.path, then imports comp_constants_cli, manifest_check_cli, shell_cli, log_open_lint and ses_sender_lint_cli (:96-100). ls -d org/modules in this worktree: 'No such file or directory'. git sparse-checkout list returns .tools, infra/aws/lambda/v2_portal, org/missions/D4/POSN/POSN_ASTTAX, org/ref, org/standards -- org/modules is absent by construction, not by accident.",
        ".tools/commit-gate.sh has NO fallback limb: its last line is exec python $SCRIPT_DIR_WIN/commit_gate_runner.py $@, so the import crash IS the gate's exit code. .tools/safe-commit.sh:640-661 runs that gate on every in-scope file, unstages them and exits 1 on any non-zero rc, and its own comment states \"--force does NOT bypass a gate FAILURE\" -- so the refusal has no sanctioned escape.",
        "Discrimination -- the crash is NOT a finding about the file under test: with the five modules made importable, the SAME gate on the SAME bytes printed 'All checks passed!' / 'OK: no unguarded strict-utf8 log reads.' / 'OK: pre-commit gate clean for 1 of 1 file(s)' at rc=0. The file was clean throughout (py_compile OK; ruff --target-version py39 'All checks passed!'; ds-precommit-check.py rc=0 -- each run standalone).",
        "A second, distinct failure mode sits behind the first: once the imports resolve the gate exits rc=2 with 'ERROR: config not found: ...comp-constants.config.yaml', because comp_constants_cli resolves that config against its own module ancestry, so a relocated module set also needs the repo-root config mirrored beside it. commit-gate.sh's own header documents rc=2 as 'a GATE DEFECT ... so it can never be read as a clean commit'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 14: 'Every .py edit passes .tools/commit-gate.sh (py_compile + ds-precommit + ruff py39). Universal.' TO-S6-1 mandates the commit go through .tools/safe-commit.sh, which re-asserts that gate fail-closed, while the worker face mandates a cone-mode sparse worktree that excludes org/modules/graph (deliberately -- a full 33k-file checkout is OOM-killed on this device at 94% memory load).",
    "world_is": "The two mandates are incompatible as written: the gate is unrunnable in the worktree the order requires, and it fails CLOSED, so the mandated commit mechanism refuses every .py commit with an ImportError instead of a verdict about the code.",
    "notes": "DID NOT BLOCK THIS ORDER. Remedied without widening the cone and without touching any repo path: git archive HEAD org/modules/graph | tar -x -C .scratch/gatemods reads the tree out of the OBJECT STORE into this worker's scratch (183 entries; no sparse-checkout change, no repo file materialized, so the 33k-file re-checkout that OOM-killed the previous attempt is not risked), the repo-root comp-constants.config.yaml is copied beside it, and PYTHONPATH points at the two directories for the safe-commit call only. After that the gate runs its real checks and passes. WOULD block any sparse-cone worker that does not reproduce this, and the sparse cone is now this device's standard answer to the OOM, so the next .py-editing worker meets it too. disarm_owner 1.0.0_SA_CTO~Z as the owner of .tools/ (a runner that degrades loudly, or names the missing path, rather than dying at import); 2.0.0_SA_COO~Z can also disarm operationally by adding org/modules/graph to the cone it provisions, at a memory cost it owns the measurement of. Neither remedy is attempted here: .tools/ and the cone are both outside this order's four-path write surface."
  }
]
```

---

## Row appended by `0.9.0_WK_POSN_ASTTAX~2` at L7, task order `POSN_ASTTAX.TO-S6-1` (cell `AT2-s-6`), 2026-09-11 -- second pass

Surfaced while validating the three rows above: the row gate itself refuses in this worktree. Filed
as its own row rather than folded into `S3` -- same class, different mechanism.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W2-S4",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~2",
    "surfaced_at": "2026-09-11T12:42:02Z",
    "one_line": "A SECOND gate is unrunnable in a cone-mode sparse worktree for a DIFFERENT reason: .tools/surprise-row-gate.py's standing-corpus pass loads org/surprise_channel/schemas/investigation_item.schema.json from the FILESYSTEM and fail-closes with FileNotFoundError when that path is outside the cone -- while the gate's own per-commit grader reads the very same schema from the STAGED INDEX, where it is present and readable.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured in this worktree (/c/tmp/wk-posn-s6 @2d8b5f7314): timeout 120 python .tools/surprise-row-gate.py <this file> printed '[surprise-row-gate] BLOCKED -- 1 violation(s) on NEW rows: standing corpus pass could not run (FileNotFoundError: [Errno 2] No such file or directory: 'C:/tmp/wk-posn-s6\\\\org\\\\surprise_channel\\\\schemas\\\\investigation_item.schema.json') -- fail-closed' and exited rc=1.",
        "The two readers disagree BY CONSTRUCTION, and only one of them is sparse-safe: surprise-row-gate.py:976-981 resolves the schema with _blob(root, \"\", rel) -- i.e. git show :org/surprise_channel/schemas/investigation_item.schema.json, the STAGED INDEX, whose docstring at :973-975 states 'The index is what the commit contains. Unreadable = REFUSE' -- while the standing-corpus limb reached at :1825-1827 raises a FILESYSTEM FileNotFoundError. A sparse cone removes the working-tree FILE while leaving the INDEX ENTRY intact, so it breaks exactly one of the two.",
        "Discrimination -- the refusal is not a finding about the rows: the same schema, extracted from the object store at 2d8b5f7314 (git show HEAD:<schema path>, 9854 bytes) and run over every row in this file with jsonschema 4.26.0 Draft7Validator, returned 4 of 4 VALID (denominator = all rows in the file: 1 pre-existing + the 3 appended by this order). The gate never evaluated a row before refusing.",
        "Same invocation also measured WHY the gate reported '0 new row(s) of 1 total checked' against a file that holds 4 rows on disk: it grades STAGED bytes, never the worktree (stated at surprise-row-gate.py:40), and these rows were unstaged at that moment -- so that count is correct behaviour and is NOT part of this row's claim."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The surprise channel is the sanctioned off-task carrier for every seat (CLAUDE.md section 2: append a row and keep working), its gate .tools/surprise-row-gate.py validates every NEW row, and an uncommitted/ungraded row is estate-wide fail-closed -- so the row path must be available to an L7 worker in the worktree the issuance gave it.",
    "world_is": "In a cone-mode sparse worktree the gate refuses before grading anything, because one of its two schema readers goes to the filesystem for a path the cone excludes. The refusal names a missing FILE, not a defective ROW, and its own message points the reader at an override or at the gate's owner.",
    "notes": "DID NOT BLOCK THIS ORDER, and no repo path outside this order's four-path write surface was created to work around it: the rows were validated against the schema extracted from HEAD into this worker's scratch (evidence 3), and the commit carries the gate's own documented audited escape, the '# surprise-row-override: ...' line in the commit message body, whose reason states that the schema was unreadable from disk and names the independent validation. SAME CLASS as POSN_ASTTAX-Z-W2-S3 (a .tools gate that resolves a path outside the cone cannot run), DIFFERENT MECHANISM (an import crash there, a filesystem schema read here), so it is filed separately rather than folded in. COVERAGE, STATED HONESTLY: 2 gates of an UNENUMERATED denominator -- both were met incidentally while executing this order and NO census of .tools was run (out of this order's scope), so the population of sparse-cone-unsafe gates is UNKNOWN, not 2. disarm_owner 1.0.0_SA_CTO~Z as the owner of .tools/; the one-line shape of a fix is visible in the gate itself -- route the standing-corpus limb through the same _blob staged-index read the per-commit grader already uses."
  }
]
```

---

## BLOCKING row appended by `0.9.0_WK_POSN_ASTTAX~2` at L7, task order `POSN_ASTTAX.TO-S6-1` (cell `AT2-s-6`), 2026-09-11

The commit for this order was REFUSED and the work is complete but uncommitted. Third gate of the
same class as `S3`/`S4`, and the first with no override path. Two named remedies, both out of this
worker's write surface.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W2-S5",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~2",
    "surfaced_at": "2026-09-11T13:07:47Z",
    "one_line": "THE COMMIT FOR THIS ORDER CANNOT LAND. A THIRD gate fails in the cone-mode sparse worktree, and this one is fail-closed with 'never bypass' and no override path: the missions-tree-check pre-commit hook runs a validator that globs org/projects/*.json from the FILESYSTEM, the cone excludes org/projects, so it read 0 of the 368 register rows that exist in the index and refused the commit with INDEX-MISSING for a register row that IS present in git.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The refusal, verbatim from the safe-commit run in this worktree (/c/tmp/wk-posn-s6, branch wk-posn_asttax-2-6 @2d8b5f7314): 'BLOCKED: missions-tree-check -- the project tree's validator REFUSES this commit' / 'missions-tree-index check: tree=1 project(s) under 1 directive folder(s), 1 valid | flat index rows=0 (generated=0, hand-written=0, parse-errors=0)' / '[INDEX-MISSING] org/missions/D4/POSN/POSN_ASTTAX: no org/projects/POSN_ASTTAX.json (remedy: derive --write)' / 'RESULT: 1 violation(s)'. safe-commit then printed 'ERROR: safe-commit did NOT commit (rc=1)'.",
        "THE REGISTER ROW IT CALLS MISSING IS PRESENT IN GIT: git ls-tree HEAD org/projects/POSN_ASTTAX.json returns '100644 blob 0cae36d55bf7d0422d2288009f205fa406b9e4a4', and git ls-files --stage returns the same blob at stage 0 -- so the file is in BOTH the HEAD tree and the index. Only the WORKING TREE lacks it, because the cone excludes org/projects (ls -d org/projects: 'No such file or directory'; the cone is .tools, infra/aws/lambda/v2_portal, org/missions/D4/POSN/POSN_ASTTAX, org/ref, org/standards).",
        "THE DENOMINATOR COLLAPSED, and that is the discriminator: git ls-files 'org/projects/*.json' counts 368 register rows in the index; the validator reported 'flat index rows=0'. It graded 0 of 368. A validator whose corpus read returns EMPTY cannot distinguish 'this project is unregistered' from 'I cannot see the register', and it took the first branch.",
        "The mechanism is a filesystem glob: .tools/missions-tree-index.py:138 builds its index map '{code: (row, is_generated, path)} over org/projects/*.json' and gates rows on Path.is_file() (:63, :180), raising INDEX-MISSING at :282. The hook .tools/git-hooks/missions-tree-check.sh runs 'python $TOOL check' with no --staged mode, and its own header states the bound: 'check reads the WORKTREE, not the staged index ... the generator has no --staged mode. Named here so it is a known hole, not a discovered one.' That named hole is exactly what a sparse cone opens.",
        "NO SANCTIONED ESCAPE EXISTS for this one, unlike the surprise-row gate: the hook is fail-closed by design ('a gate that vanishes silently reads exactly like its approval') and its refusal text says 'remedy: fix the state the violation names (R5 = the register's members list, 0.0.0_AB_MSTR's lane); never bypass.' safe-commit's --force covers only contamination checks. The hook does honour a PRECOMP_REPO_ROOT env override, but pointing it at a DIFFERENT (full) checkout would grade another worktree's state and return a green that describes a tree this commit is not in -- that is evidence laundering, so it was NOT done.",
        "Repository-confirmed non-landing, asked of git rather than of the tool's stdout: git log -1 --format='%h~%an~%s' still returns 2d8b5f7314 (0.0.0_AB_MSTR~Z's integrate commit), git log --author='0.9.0_WK_POSN_ASTTAX~2 <' returns EMPTY, and git rev-parse HEAD is unchanged at 2d8b5f7314. Negative control: the same git log against a bogus hash errors rather than returning a row."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX.TO-S6-1 mandates that this order end in ONE commit through .tools/safe-commit.sh carrying the generator fix, the proof instance, this worker's deliverables and the <status> flip together, made from the cone-mode sparse worktree the worker face provisions and forbids widening.",
    "world_is": "That commit is refused by a pre-commit hook for a state that is not wrong in the repository, only invisible in this worktree. Every acceptance criterion is met (proof-of-spec-check.py returned VALID rc=0 on all 7 expected ids with all five paths staged, 6 mechanical rows PASS with their expect patterns matched, S6-AC7 carried as judgment with no self-verdict), the Rule-14 commit gate passed 3 of 3 files, and the work sits COMPLETE BUT UNCOMMITTED in /c/tmp/wk-posn-s6 on branch wk-posn_asttax-2-6. The <status> flip to complete is made in the worktree and is therefore NOT in the record: at HEAD the order still reads staged, which is the honest state.",
    "notes": "THIS IS THE CHAIN HEAD, so six sibling round-2 cells stay held until it is disarmed. Two remedies, both outside this worker's four-path write surface, so neither was attempted: (A) OPERATIONAL, 2.0.0_SA_COO~Z, unblocks this round now -- add org/projects to this worktree's cone (368 small json files, nothing like the 33k-file full checkout that OOM-killed the previous attempt at this round) and re-run the same safe-commit, or drain the uncommitted work from a full checkout; the branch holds NO commits, so the work exists only as worktree state and a discarded worktree loses it. (B) DURABLE, 1.0.0_SA_CTO~Z, owner of .tools -- give missions-tree-index.py a staged or git-backed corpus read (its sibling gate surprise-row-gate.py already reads its corpus via git show :<path>), or make an EMPTY register read refuse as could-not-evaluate rather than as INDEX-MISSING, since 0 of 368 is not an absence. THIRD INSTANCE of the class in POSN_ASTTAX-Z-W2-S3 and -S4 (a .tools gate resolving a path outside the cone), and the first one that is BLOCKING rather than remediable in-worker. COVERAGE, STATED HONESTLY: 3 gates met incidentally while executing one order; NO census of .tools was run, so the population is UNKNOWN, not 3 -- and the three found so far share one dependency (a fully materialized worktree) that no per-gate check would have surfaced."
  }
]
```

```json
[
  {
    "id": "POSN_ASTTAX-Z-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T13:27:47Z",
    "one_line": "The '# surprise-row-override:' escape in a commit message is ALL-OR-NOTHING: it suppresses EVERY violation surprise-row-gate.py raises on that commit, not only the class its stated reason names. Measured on commit 7f247caae0, where an override authored for a schema FileNotFoundError silently absorbed FIVE unrelated identity violations as well -- 6 suppressed, 1 explained.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Commit 7f247caae0 (branch wk-posn_asttax-2-6, author 0.9.0_WK_POSN_ASTTAX~2, invoked by 2.0.0_SA_COO~Z). Its message carries ONE '# surprise-row-override:' line whose stated reason is solely the standing-corpus pass failing to LOAD its schema: \"FileNotFoundError ... org/surprise_channel/schemas/investigation_item.schema.json, a path the cone excludes\".",
        "safe-commit.sh stdout at that commit, verbatim: \"[surprise-row-gate] OVERRIDDEN (reason given): ... -- 6 violation(s) on NEW rows follow as WARN.\" The gate then printed SIX WARN lines: ONE is the schema-load failure the reason names; the other FIVE are a DIFFERENT class -- \"NEW row POSN_ASTTAX-Z-W2-S<n> carries W2 but the committer 2.0.0_SA_COO~Z is not a worker\" -- for S1 through S5. So the override's BLAST RADIUS was 6 and its stated reason covered 1.",
        "DISCRIMINATOR, and it is what makes this a control defect rather than a nuisance: had the five identity violations been the ONLY failures, the same override line would have suppressed them with a reason that does not mention them at all, and the commit would have read as 'OVERRIDDEN (reason given)' exactly as it did here. The gate itself flags the gap in its own words: \"PROVENANCE NOT VERIFIED BY THIS GATE\".",
        "COVERAGE -- the five identity violations are NOT themselves a defect and are NOT what this row is about. They fire because the gate reads the committer from the session serial (2.0.0_SA_COO~Z) rather than from --author (0.9.0_WK_POSN_ASTTAX~2), which is an artifact of the ISSUER invoking a worker's commit after the worker subagent could not be resumed. The designed path is sound: at the DRAIN (safe-merge.sh c2245247a6) the same gate printed \"MERGE COMMIT -- foreign-row sweep exempt for 5 row(s) a PARENT carried, attributed to 1 seat(s) (0.9.0_WK_POSN_ASTTAX) and graded at their own authorship\" and returned \"OK: 1 file(s), all new rows carry their step-7/step-10 fields\" with NO override in play.",
        "NEGATIVE CONTROL on the rows themselves, so this row is not read as doubting them: all five were independently validated by the worker against the schema extracted from HEAD (git show, 9854 bytes, jsonschema 4.26.0 Draft7Validator) at 5 of 5 VALID, and the merged-index grade above passed them at their own authorship. The rows are sound; the OVERRIDE'S SCOPE is the finding."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The override is documented per-reason: surprise-row-gate.py's own refusal text instructs \"put '# surprise-row-override: <reason>' in the commit message body\", and CLAUDE.md's treatment of audited escapes (Rule 14a on GIT_COMMIT_AUTHOR_OVERRIDE being 'audited, SINGULAR') establishes that an audited escape is expected to be scoped to what its reason names.",
    "world_is": "The override is a single boolean exported to the hook (SURPRISE_ROW_OVERRIDE), so it is scoped to the COMMIT, not to the violation class. One reason disarms the whole gate for that commit. A seat writing an honest reason for one failure cannot avoid also suppressing any other failure the gate would have raised, and nothing in the output separates 'the failure I explained' from 'the failures I did not know about' except reading all the WARN lines and comparing them to the reason by hand.",
    "notes": "Filed by the seat whose own act exposed it: 2.0.0_SA_COO~Z invoked this commit because the worker subagent could not be resumed, which is what produced the five extra violations for the override to absorb. OBSERVATION rather than BLOCKING -- nothing is mis-served, the rows landed correctly attributed, and the drain graded them clean on the merged index. ARMED because the next seat to use this escape inherits the same unbounded radius, and because the gate's WARN-vs-BLOCK presentation makes a suppressed violation look reviewed. Remedy is the gate owner's to choose and is NOT prescribed here; the shape suggested by the gate's own sibling behaviour would be to scope the override to a named violation class or row id, so an unrelated failure still refuses. Related and NOT the same finding: POSN_ASTTAX-Z-W2-S3 and -S4 (also 1.0.0_SA_CTO~Z) record that two gates cannot RUN in a cone-mode sparse worktree because they read from the filesystem rather than the staged index; this row is about the ESCAPE from a gate, not about a gate crashing. POSN_ASTTAX-Z-W2-S5 (BLOCKING, 2.0.0_SA_COO~Z) is REMEDIED by this seat at its own grain -- the cone now carries org/projects, org/missions and org/modules and missions-tree-index.py returns rc=0 -- but its disarm is a separate citing row, not this one."
  }
]
```


---

## Rows appended by `2.0.0_SA_COO~Z` at L7 (disarm rows, round 2), 2026-09-11

Two DISARM rows filed by the `disarm_owner` of the two ARMED rows this seat owed. Each is a NEW
citing row, never an in-place flip: `hazard_standing` is at-surfacing and immutable, so `W2-S2`
and `W2-S5` keep ARMED and these rows carry the disarm. Neither row dispositions its target --
that is the CVO's L9 act via `adjudicates`.

```json
[
  {
    "id": "POSN_ASTTAX-Z-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T15:33:02Z",
    "one_line": "DISARM of POSN_ASTTAX-Z-W2-S2 (the +30-line citation shift), on a WIDENED denominator: the shift is real but reaches NO graded contract. Re-measured across ALL SIX staged sibling orders -- 0 of 28 criterion invocations navigate by line offset; every one navigates by symbol, content, regex or diff. No L6-amend is owed; only ungraded PROSE in two orders is stale.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DENOMINATOR PRINTED, and it is WIDER than the one the predecessor session recorded. That session measured '0 of 10 criterion invocations across TO-S1-1 and TO-S7-1' -- 2 of the 6 orders the hazard spans. Re-measured this session over ALL SIX staged orders (TO-S1-1, TO-S2-1, TO-S3-1, TO-S4-1, TO-S5-1, TO-S7-1) at HEAD 7b0c8b9e3f: 28 <invocation> blocks total, of which 0 match any line-offset navigation form (sed -n <lineno>, awk NR==<lineno>, tail -n +<lineno>, head -N <file>). Per-order invocations/offset-hits: S1-1 5/0, S2-1 5/0, S3-1 4/0, S4-1 4/0, S5-1 5/0, S7-1 5/0.",
        "UNSCOPED RE-READ, because an invocation-scoped scan cannot see a citation living in another graded tag. Every ':NNN' or 'line NNN' token anywhere in the six orders: 5 hits total. THREE are TO-S1-1 prose (:209, :360, :520) -- ungraded narrative, stale, and already named by W2-S2 itself. ONE is TO-S7-1 prose (:239). ONE lands inside a GRADED tag: TO-S7-1 <preflight> ':239'.",
        "THE ONE GRADED-REGION HIT IS NOT AN INSTRUMENT, read verbatim: TO-S7-1's <preflight> comp-adversary line reads 'the issuer measured ONE hop (the :239 subscript) and has NOT traced the chain'. That is narrative provenance about a measurement the ISSUER made at authorship vintage 2d8b5f7314 -- it directs no navigation and grades nothing; no worker executes it. So the graded-contract count stays 0.",
        "NEGATIVE CONTROL on the matcher, so '0 of 28' is not read as a dead regex: the same offset patterns run against the COMPLETED TO-S6-1 -- whose S6-AC1/S6-AC2 invocations do use sed -n '218,246p' and sed -n '68,84p' -- return NON-ZERO hits. The matcher fires when the shape is present, so its zero on the six staged orders is a true absence rather than a blind instrument.",
        "The shift itself is NOT disputed and is not re-measured here: W2-S2's own citation map (old -> new, content-matched) stands as recorded, and commit 7f247caae0 is an ancestor of origin/SITEZ (git merge-base --is-ancestor, with a passing negative control that the predicate can return false)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX-Z-W2-S2 asserts that every line citation below :66 in the round-2 decomposition and in the six held sibling orders is stale by +10/+30 once AT2-s-6 commits, and points the hazard at the issuer for a re-pin of the siblings before they are dispatched.",
    "world_is": "The coordinates are stale exactly as stated, but staleness only harms where a GRADED contract navigates by offset, and none does: 0 of 28 criterion invocations across all six staged orders, and the single line citation sitting inside a graded tag is narrative provenance rather than a navigation step. The exposure is confined to ungraded prose in two orders. Disarmed on that basis -- NOT on the shift being absent.",
    "notes": "THE DISARM BASIS DIFFERS FROM THE PREDECESSOR'S IN ITS DOMAIN, which is the reason it was re-measured rather than inherited: a 2-order read standing in for a 6-order hazard is a scoped check certifying a wider claim (CLAUDE.md Rule 22 shared-scope blindness, Rule 24 wrong-domain subtraction). The wider read AGREED, and additionally surfaced the <preflight> ':239' hit that an invocation-scoped read structurally could not see. THE REMEDY IS STILL CARRIED, not dropped: each wave-2 worker face carries W2-S2's citation map with an explicit instruction to navigate by symbol rather than by offset. This row disarms the hazard; it does NOT disposition W2-S2, which is the CVO's L9 act via `adjudicates`."
  },
  {
    "id": "POSN_ASTTAX-Z-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T15:33:02Z",
    "one_line": "DISARM of POSN_ASTTAX-Z-W2-S5 (BLOCKING -- the cone-blinded missions-tree-check refusal that stopped the AT2-s-6 commit): the cause was MINE, a worker cone cut narrower than the banked recipe, dropping org/projects. The corrected cone is built and EXERCISED this session -- the gate that refused now returns rc=0 with its denominator restored from 0 to 360.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REMEDY EXERCISED, not described. Worktree /c/tmp/wk-posn-s7 cut from HEAD 7b0c8b9e3f as a cone-mode sparse checkout carrying .tools, org/projects, org/missions, org/modules, org/ref, org/standards, infra/aws/lambda/v2_portal. Measured inside it: org/projects 381 files PRESENT (the narrow cone had it absent -- 'ls -d org/projects: No such file or directory'), .tools 404 tracked, org/missions 1723 tracked, org/modules 428 tracked.",
        "THE REFUSING GATE NOW PASSES, verbatim: 'missions-tree-index check: tree=11 project(s) under 7 directive folder(s), 11 valid | flat index rows=360 (generated=11, hand-written=349, parse-errors=0)' then 'RESULT: 0 violation(s)', rc=0. W2-S5's recorded refusal read 'flat index rows=0' with '[INDEX-MISSING] org/missions/D4/POSN/POSN_ASTTAX'.",
        "THE DISCRIMINATOR IS THE ONE W2-S5 NAMED ITSELF: that row's third evidence line identified the collapsed denominator as the tell -- 'It graded 0 of 368. A validator whose corpus read returns EMPTY cannot distinguish this project is unregistered from I cannot see the register.' The denominator is now non-empty (360 rows read), so the validator is seeing the register rather than passing for want of data. A pass that still printed rows=0 would NOT have disarmed this.",
        "THE OTHER TWO CONE-BLINDED GATES ALSO RUN in the same cone (their rows W2-S3 and W2-S4 stay 1.0.0_SA_CTO~Z's to disposition): surprise-row-gate.py --self-test returns 'RESULT: 0 arm(s) failed of 103 (+ live census)', rc=0, where the narrow cone raised FileNotFoundError on its schema; commit_gate_runner.py returns rc=0 with imports resolving, where the narrow cone raised ModuleNotFoundError.",
        "SCOPE HONESTY -- what this does NOT prove: the exercise ran the three gates DIRECTLY, not through a real safe-commit of a real worker diff. The end-to-end proof is the first wave-2 worker commit landing through safe-commit.sh inside this cone; until one does, this is EXERCISED-AT-THE-GATE, not EXERCISED-AT-THE-COMMIT. Stated rather than implied."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX-Z-W2-S5 asserts the AT2-s-6 commit cannot land because the fail-closed missions-tree-check hook globs org/projects/*.json from the FILESYSTEM, the sparse cone excludes org/projects, and no sanctioned override path exists for that hook.",
    "world_is": "The mechanism is real and UNCHANGED -- the hook still reads the worktree, still has no --staged mode, and the hole its own header names stands as a standing property of any sparse cone. What was defective was my cone, not the hook. A cone carrying org/projects satisfies it: rc=0, 0 violations, 360 register rows read.",
    "notes": "CAUSE OWNED AT THIS SEAT: I cut the cone narrower than the recipe banked after the earlier OOM incident and dropped org/projects. The corrected recipe is exercised above and is carried into every wave-2 worktree. THE UNDERLYING HOLE IS NOT CLOSED BY THIS ROW AND MUST NOT BE READ AS CLOSED -- any future seat cutting a cone without org/projects reproduces this refusal exactly. That standing exposure is the CTO-owned class already carried by W2-S3 and W2-S4; this row disarms only the instance that blocked AT2-s-6. Dispositioning W2-S5 remains the CVO's L9 act."
  }
]
```

---

## Rows appended by `0.9.0_WK_POSN_ASTTAX~8` at L7, task order `POSN_ASTTAX.TO-S4-1` (cell `AT2-s-4`), 2026-09-11

Three rows, ONE fenced array, appended at the end (no existing row edited, renumbered or re-graded).
`S1` is a read this worktree's cone could not serve. `S2` and `S3` both concern the three blank rows this
order filled -- `S2` why they were blank and why that recurs, `S3` the SHAPE of the blank not matching the
producer's rule. Neither was acted on: the seeder is not in this order's write surface.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W8-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~8",
    "surfaced_at": "2026-09-11T16:02:11Z",
    "one_line": "TO-S4-1 and CLAUDE.md both require a new surprise row to be validated against org/surprise_channel/schemas/investigation_item.schema.json, but that path is not materialized in this worker's cone-mode sparse worktree, so the schema had to be read out of the object store with git show instead of off the filesystem.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/tmp/wk-posn-s4 prints exactly 7 cone entries -- .tools, infra/aws/lambda/v2_portal, org/missions, org/modules, org/projects, org/ref, org/standards -- and org/surprise_channel is not among them.",
        "ls org/surprise_channel/schemas/ in this worktree: 'No such file or directory' (rc=2). ls org/ confirms the directory itself is absent from the cone while org/missions, org/projects, org/ref and org/standards are present.",
        "git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json at HEAD fd9f8ba9a4 returns the full draft-07 document, rc=0 -- the blob is in the repository, only the working-tree materialization is missing, so the remedy is an instrument swap and not a missing artifact.",
        "NOT A GATE FAILURE, measured rather than assumed: timeout 120 python .tools/surprise-row-gate.py --self-test in this same cone returns 'RESULT: 0 arm(s) failed of 103 (+ live census)', rc=0 -- the row gate is NOT blinded by the missing path; only the worker's own filesystem read of the schema is."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's BOUNDS and the worker face instruct: validate the appended row against org/surprise_channel/schemas/investigation_item.schema.json before committing, naming it as a readable path.",
    "world_is": "org/surprise_channel is outside this worktree's sparse cone, so that path does not exist on the filesystem; the schema was read at HEAD from the object store (git show HEAD:<path>) and the row validated against that copy. The row gate itself self-tests clean in the same cone, so nothing is blocked.",
    "notes": "Same family as W2-S3/W2-S4/W2-S5 (cone-blinded reads in the wave-2 worktrees) but a DIFFERENT path and a different consumer: those rows concern gates, this one concerns the worker's own validation read. Filed as form, not significance. A cone that also carries org/surprise_channel would close it; whether that is worth doing is not this worker's call."
  },
  {
    "id": "POSN_ASTTAX-Z-W8-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~8",
    "surfaced_at": "2026-09-11T16:02:11Z",
    "one_line": "All three blank sub_asset_class rows already carry the CORRECT value in the registry's own upstream served artifact, yet the DynamoDB rows stood blank for 17 days -- because seed-etf-constituents.py only ever writes a row on CREATE and preserves every existing row, so a row born blank never heals when upstream later fills it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-portal-v2/platinum/etfs/positioning_data.json read this session (VersionId HQYvt1tnqm7Z5XApTZThUwAL273jJtF5, 148526 bytes, document as_of 2026-09-11T13:01:23Z): ICT sub_asset_class 'Industrials' (book IDVZ), MER sub_asset_class 'Utilities' (book IDVZ), 2602335D sub_asset_class 'Financials' (book PFDE).",
        "Same artifact, whole-population read: 189 holding rows scanned, 0 distinct tickers with a blank or absent sub_asset_class upstream -- the gap exists ONLY in the DynamoDB registry, not in its source.",
        "DynamoDB get-item on all three tickers before the fill: last_updated 2026-08-25T17:48:57Z and updated_by 'seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)' on each, with no sub_asset_class attribute at all -- 17 days blank while the upstream carried a value.",
        "MECHANISM, cited at its vintage: infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py at b3d830094c, :183 initialises creates/updates/skips; :200-206 routes an EXISTING ticker to skips unless --force-names is passed; :212-214 prints the skipped row as KEEP and flags only the NAME as differing; :222-223 writes creates + updates only. sub_asset_class is never compared against upstream on the preserve path, so no re-run at default flags can refresh it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-S4-1 frames the three blanks as the registry's own coverage gap to be filled by hand, and the round-1 analysis it quotes treats 282-of-285 as a property of the registry.",
    "world_is": "The blanks are a STALENESS artifact of the seeder's preserve-existing path, not a gap in the underlying data: the correct values for all three sit in the served artifact the seeder itself reads, and 0 of 189 upstream holding rows are blank. The hand fill closes these three; the mechanism that let them stand stays exactly as it is.",
    "notes": "ARMED because it harms through FUTURE NORMAL operation, not through anything left half-done here: any constituent first seeded while its upstream sub_asset_class is absent is written blank and is never refreshed, so the same gap regenerates silently on the next new holding. NOT ACTED ON by this order -- the seeder is not in this worker's paths grant and the generator surface is AT2-s-6's. Also recorded because it bounds the durability of this order's fill: a default re-seed preserves the filled values, and a --force-names re-seed would today re-derive the SAME three values from upstream, so the fill is not at risk from either path at this vintage."
  },
  {
    "id": "POSN_ASTTAX-Z-W8-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~8",
    "surfaced_at": "2026-09-11T16:02:11Z",
    "one_line": "The producer's own rule says a missing upstream sub_asset_class lands in DynamoDB as an EMPTY STRING, but all three blank rows carried the attribute ABSENT entirely -- 3 MISSING and 0 EMPTY -- so the two blank shapes S4-AC1 asks to be distinguished are not the shape the seeder's bytes predict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py:194 at b3d830094c writes sub_asset_class as c['sub_asset_class'] or '' -- an empty string, not a dropped key -- and :223 filters the item with 'if v is not None', which an empty string survives.",
        "Measured, S4-AC1 scan of etf-classifications this session: denominator 285 items (Count 285, ScannedCount 285, no LastEvaluatedKey); MISSING attribute 3 (2602335D, ICT, MER); EMPTY STRING or whitespace-only 0; NULL-type or non-string 0; populated 282.",
        "The detector was not blind to the empty-string shape: the mutant arm of this order's control fed it a synthetic MUT_EMPTY row carrying sub_asset_class as an empty string and it reported that row as EMPTY, separately from MUT_MISSING, in the same run that read 0 empty strings live.",
        "VINTAGE CHECK: the seeder has exactly ONE commit (b3d830094c, 2026-08-25T13:41:12-04:00 = 17:41:12Z) and the three rows' last_updated is 2026-08-25T17:48:57Z, 7m45s later -- so the HEAD bytes cited above are the bytes that wrote these rows, and this is not a stale-source comparison."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S4-AC1 requires MISSING-attribute rows and EMPTY-STRING rows to be listed separately because they are different shapes in DynamoDB, and the seeder at HEAD asserts by construction that an unpopulated value is written as an empty string.",
    "world_is": "Every blank row is the MISSING shape and none is the empty-string shape, which the producer's cited line cannot produce. The CAUSE IS NOT DETERMINED BY THIS ROW and is deliberately not guessed at -- the divergence is recorded, not explained.",
    "notes": "Matters to a consumer, which is why it is filed rather than dropped: a blank test written as a key-presence check and one written as a falsy-value check disagree on exactly one of these shapes, and the estate currently holds rows of one shape while its producer's rule specifies the other. Not acted on: this order's write surface is the three values."
  }
]
```

---

### One further row appended by `0.9.0_WK_POSN_ASTTAX~8`, same task order, after the deliverable scripts met the commit gate

`S4` was surfaced by this order's own commit-gate run and is about the gate, not about the registry.
Filed as a separate block rather than folded into the block above, because that block was already
written and an appended row is never inserted into an existing one.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W8-S4",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~8",
    "surfaced_at": "2026-09-11T16:23:40Z",
    "one_line": ".tools/ds-precommit-check.py reports every name bound inside a MODULE-LEVEL while body as an undefined name and exits rc=1, refusing valid Python that runs rc=0; the identical body inside a function and the identical body in a module-level for loop both pass, so the blind spot is specifically the module-level while body.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "POSITIVE ARM, 5-line repro: a module-level 'while True:' whose body binds 'page' and then reads it. python runs it rc=0 and prints the value; python .tools/ds-precommit-check.py on the same file exits rc=1 with the single line \"repro_while.py:4: undefined name 'page'\" -- the name is bound one line above the use.",
        "NEGATIVE CONTROL 1 (same body, function scope): the identical loop inside def f(x) -- python rc=0, ds-precommit-check rc=0, empty output. The finding is about SCOPE, not about the code.",
        "NEGATIVE CONTROL 2 (same body, module-level for loop): 'for i in [1]:' binding 'page' in its body -- python rc=0, ds-precommit-check rc=0, empty output. So the checker handles module-level loop bindings in general; only the while form is blind.",
        "MET LIVE, not constructed: the S4-AC3 fill script as it actually RAN (rc=0, three accepted DynamoDB update-item calls, evidence in this order's proof-of-spec instance) was refused by bash .tools/commit-gate.sh with 7 undefined-name errors at :36-:43 -- every one of them inside its module-level while body -- and BLOCKED at rc=1. Wrapping that loop in measure_value_set() with no behavioural change turned the same invocation into 'OK: pre-commit gate clean for 4 of 4 file(s)', rc=0.",
        "Exit codes were re-measured WITHOUT a pipe after a first reading took tail's status instead of the checker's; the rc values above are the checker's own."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Rule 14: every .py edit passes .tools/commit-gate.sh (py_compile + ds-precommit + ruff py39), and the ds-precommit limb refuses a file for using an undefined name.",
    "world_is": "The undefined-name limb has a scope blind spot: names bound inside a module-level while body are reported undefined even though the interpreter resolves them and the script runs. The refusal is fail-CLOSED (valid code blocked, never invalid code admitted), and the two negative controls above bound the defect to exactly that one form.",
    "notes": "ARMED because it harms through FUTURE NORMAL operation: every author who writes a module-level while loop meets the same refusal, and the refusal text names a defect that is not in the code, so the natural responses are a pointless refactor (what this worker did, and disclosed in the shipped script's docstring) or a --force. NOT ACTED ON: .tools/ds-precommit-check.py is outside this order's <paths> write surface, and fixing a gate is not this cell. The workaround cost here was one refactor of a deliverable script plus one re-run to keep the shipped bytes and the recorded output the same artifact."
  }
]
```

---

### One further row appended by `0.9.0_WK_POSN_ASTTAX~8`, same task order, while writing the proof-of-spec instance

`S5` is about the proof-of-spec contract, not the registry: it was surfaced by this order's own instance
failing to declare its live-table deliverable, and it is filed BEFORE the instance cites it, because a
`surprises` entry whose row is not yet committed is refused by the checker's SURPRISES limb.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W8-S5",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~8",
    "surfaced_at": "2026-09-11T16:41:05Z",
    "one_line": "PROOF_OF_SPEC.schema.json's artifacts_produced.kind enum has no member for a LIVE DATABASE artifact, and proof-of-spec-check.py treats every kind except s3_object as a repo path that must carry a commit-ish -- so an order whose entire deliverable is three DynamoDB attribute values can be declared only by mis-labelling it s3_object or by not declaring it at all.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/PROOF_OF_SPEC.schema.json at fd9f8ba9a4, artifacts_produced.items.properties.kind enum, read in full and subtracted rather than recalled: script, s3_object, terraform, config_data, schedule, iam, test, doc, frontend_component -- 9 members, of which 8 name repo artifacts and 1 names an S3 object. No member names a database row, item or attribute.",
        ".tools/proof-of-spec-check.py:203 (docstring of the artifact-resolution limb): 'For every artifacts_produced row that names a REPO artifact (kind != s3_object)' -- the kind field is the ONLY switch between the repo plane and the live plane, and :336 is the skip ('if a.get(\"kind\") == \"s3_object\": ... continue').",
        "MEASURED on this order's own instance, both branches run rather than argued: with kind=config_data and a dynamodb:// path the checker emitted 'artifact-resolution: ... carries commit_or_etag \"LIVE TABLE...\", which is neither PENDING-THIS-COMMIT nor a 7-40 hex commit-ish for a repo artifact' and returned INVALID rc=1. With kind=s3_object the same row is skipped ('1 s3_object (not a git ref; skipped)') and the instance can reach rc=0.",
        "The third branch was also priced and rejected: dropping the row entirely leaves the order's ONLY real deliverable -- three live attribute values -- undeclared in artifacts_produced, which is the A_03 zero-battery shape the coverage limb exists to catch."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 24 requires a schema to be MECE over its declared domain, and the proof-of-spec contract requires every artifact produced to be declared with a kind that describes it; the schema's own `firm` field records the estate's ruling on exactly this failure mode -- 'an inexhaustive enum on a ratified schema forces either a false firm or a permanent violation'.",
    "world_is": "The kind enum is inexhaustive over the artifacts this estate actually produces: a DynamoDB item attribute has no member. This worker took the documented lesser evil -- s3_object, declared as a substitution inside the row's own deploy_evidence, so a reader cannot mistake it for a claim about S3 -- rather than leaving the deliverable undeclared.",
    "notes": "ARMED because it harms through FUTURE NORMAL operation: every future order whose deliverable is a live table write meets the same fork, and the cheap branch is the silent one -- a row labelled s3_object with no disclosure reads as an S3 object to every later consumer, including any census that groups artifacts by kind. NOT ACTED ON: org/standards/PROOF_OF_SPEC.schema.json and .tools/proof-of-spec-check.py are both outside this order's <paths> write surface, and a value-enum proposal is a Rule 24 act needing its own four-postulate record and token census, which is not this cell. The remedy shape, stated but not proposed: a member for the live data plane, or a kind-independent 'plane' switch, so the repo/live decision stops riding on one value of a type field."
  }
]
```
