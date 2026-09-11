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

Rows from `0.9.0_WK_POSN_ASTTAX~3` (cell `AT2-s-5`, TO-S5-1), appended as ONE new fenced block.
Neither row is BLOCKING: every S5 criterion ran and the six writes landed. `W3-S1` is the DURABILITY
of those writes; `W3-S2` is their ATTRIBUTION. Neither is fixed here -- both remedies live outside
this order's `<paths>`.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W3-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~3",
    "surfaced_at": "2026-09-11T15:53:58Z",
    "one_line": "THE SEEDER SILENTLY REVERTS THIS CELL'S WRITE AND AT2-s-2'S RETAG: seed-etf-classifications.py does an UNCONDITIONAL FULL-ITEM put over the whole ticker universe, and the six commodity tickers are ABSENT from ETF_MANAGEMENT_STYLE in all three copies of the canonical module -- so the next seed run rewrites management_style back to 'unknown' on exactly the six rows AT2-s-5 just corrected, and asset_class back to 'hedge' on exactly the six rows AT2-s-2 is about to move.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE WRITE MODE IS A FULL-ITEM PUT, NOT AN UPDATE, read verbatim at infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py@fd9f8ba9a4: line 60 builds 'management_style': ETF_MANAGEMENT_STYLE.get(ticker, 'unknown') and line 58 builds 'asset_class': ETF_CLASSIFICATIONS.get(ticker, 'unknown') into one dict, and the loop writes that dict with batch.put_item(Item=item) under `with table.batch_writer()`. A put replaces the ENTIRE item; there is no ConditionExpression and no per-attribute update anywhere in the script.",
        "THE SIX ARE ABSENT FROM THE STYLE MAP, measured by AST parse rather than by the grep that found the file -- the map is evaluated as a literal, so a commented-out or shadowed entry cannot fool it. infra/aws/lambda/v2_portal/_shared/etf_classification.py@fd9f8ba9a4: ETF_MANAGEMENT_STYLE = 99 keys, value set {'active','passive'}, and DBC/GLD/GSG/IAU/SLV/USO each return None. The same parse over the two sibling copies: partners/lambdas/opal-partners-data/etf_classification.py = 99 keys, same six absent; yang_pipeline/portfolios/yang-generate-etf-returns/etf_classification.py = 97 keys, same six absent. 3 of 3 copies agree, so this is not one stale fork.",
        "DISCRIMINATION -- the map is NOT simply missing every hedge-bucket name, which is what would make this finding vacuous: VIXY is present with 'passive' (:328) and PDBC, itself a commodity fund, is present with 'active' (:337). The map carries hedge and commodity tickers; it carries these six nowhere. And .get(ticker, 'unknown') at :60 is measurably the MINT of the placeholder this entire cell exists to remove.",
        "THE REVERT REACHES A SIBLING CELL, not only this one: ETF_CLASSIFICATIONS in the same module at :237-244 carries GLD/IAU/SLV/DBC/GSG/USO as 'hedge'. AT2-s-2's retag to Commodities would be reverted by the same put in the same run, and neither cell's write surface includes the code map that would prevent it.",
        "SCOPE HONESTY -- WHAT IS NOT MEASURED HERE: whether any schedule, pipeline or deploy step invokes this script. It is a __main__ argparse CLI whose own docstring says 'Run this whenever the classification source is updated', and this worker did NOT census EventBridge, Terraform or task definitions for an invoker -- out of this order's surface and out of this sparse cone. The hazard is therefore a LIVE CAPABILITY WITH AN UNMEASURED TRIGGER, and is stated ARMED on that basis rather than on a measured firing."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX.TO-S5-1 (cell AT2-s-5) asserts that setting management_style to the factually correct value on the six served hedge rows makes those rows safe to hold, and scopes the fix to the DynamoDB registry rows alone; the round-2 chain (AT2-s-6 hardening, AT2-s-5 style, AT2-s-2 retag) treats the registry as the durable place a correction lands.",
    "world_is": "The registry is DOWNSTREAM of a code map that no cell in round 2 writes. The six corrected values are durable only until seed-etf-classifications.py runs, at which point an unconditional full-item put restores management_style='unknown' (the six are absent from ETF_MANAGEMENT_STYLE) and asset_class='hedge' (the six ARE in ETF_CLASSIFICATIONS as hedge), with no error, no diff and no alert. The registry is not the source of truth for this field; the module is, and the module still does not carry these six tickers.",
    "notes": "NOT FIXED HERE, DELIBERATELY. The remedy is a code edit to ETF_MANAGEMENT_STYLE (and, for the sibling cell, ETF_CLASSIFICATIONS) in infra/aws/lambda/v2_portal/_shared/etf_classification.py plus its two copies -- none of which is in this order's <paths>, and the order's BOUNDS forbid widening. Adding the six to the style map would also close the placeholder AT ITS MINT rather than at its landing site. Filed ARMED with the issuer as disarm_owner because the call is a scoping decision (a round-2 amendment or a round-3 cell), not a worker's. That three separately-maintained copies of the canonical module exist at all is a shared-dependency shape a future cell may want to look at; this row does not open it."
  },
  {
    "id": "POSN_ASTTAX-Z-W3-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~3",
    "surfaced_at": "2026-09-11T15:53:58Z",
    "one_line": "THE SIX ROWS NOW CARRY A VALUE WHOSE PROVENANCE FIELDS NAME A DIFFERENT WRITER AND A DIFFERENT DAY: this order's bound restricts the write to management_style ONLY, so updated_by still reads '1.0.0_SA_CTO~X placeholder-name-sweep' and last_updated still reads 2026-08-18T18:05:00Z on rows whose management_style was changed by 0.9.0_WK_POSN_ASTTAX~3 on 2026-09-11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ROW'S OWN PROVENANCE FIELDS, read before the write by get-item on GLD (full item, every attribute): updated_by = '1.0.0_SA_CTO~X placeholder-name-sweep (prior: name=ticker, seed-script)', last_updated = '2026-08-18T18:05:00Z', management_style = 'unknown'. After this order's write the third value reads 'passive' and the first two are unchanged, because the UpdateExpression is 'SET management_style = :new' and names no other attribute.",
        "THE OMISSION IS THE ORDER'S INSTRUCTION, NOT AN OVERSIGHT, quoted from POSN_ASTTAX.TO-S5-1@fd9f8ba9a4 BOUNDS: 'DO NOT TOUCH asset_class. Different field, different cell (AT2-s-2) ... You write management_style ONLY.' Restamping updated_by would have been a second attribute and outside the literal bound, so it was not written and this row was filed instead.",
        "THE TABLE HAS AN ESTABLISHED CONVENTION FOR EXACTLY THIS, which is why the gap is visible rather than theoretical: a prior seat that changed one field DID restamp provenance and encoded the supersession inline -- 'placeholder-name-sweep (prior: name=ticker, seed-script)' is a hand-written 1.0.0_SA_CTO~X updated_by, not the seeder's. The convention exists; this order could not follow it.",
        "CONSEQUENCE, stated narrowly: any later reader -- including 3.0.0_SA_CVO~Z at L9, and any seat auditing whether the retag chain actually ran -- who asks 'who set management_style on GLD, and when' gets 1.0.0_SA_CTO~X / 2026-08-18 from the row itself. The true answer lives only in this project's git history and in this row. No consumer reads updated_by for logic (the classifier reads management_style, asset_class, sub_asset_class, sector and name), which is why this is INERT rather than ARMED."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order restricts this cell's live-world write to the single attribute management_style, on the reasoning that the neighbouring attribute asset_class belongs to cell AT2-s-2 and must not be disturbed by this order.",
    "world_is": "The bound reads on the whole item, not only on asset_class, so it also excludes the item's two PROVENANCE attributes. The six rows are now correct in VALUE and stale in ATTRIBUTION: they assert a writer and a date that did not produce the value they carry. CLAUDE.md's 'A VALUE MUST CARRY ITS CLAIM' wants the opposite, and the table demonstrably supports the convention.",
    "notes": "DELIBERATELY NOT SELF-REMEDIED: restamping updated_by would have been a worker widening its own order, which is a failure class this project already carries rows about. The clean fix is one clause in a future order -- 'write management_style, and restamp updated_by/last_updated to your serial' -- which would serve AT2-s-2 equally. Cross-reference POSN_ASTTAX-Z-W3-S1: a seed run resets updated_by to 'seed-script' on every row anyway, erasing the CTO~X sweep's attribution as well as this cell's. The two rows are separate findings about the same weak provenance surface."
  }
]
```


---

A third row from `0.9.0_WK_POSN_ASTTAX~3`, appended as its own fenced block after the first two (never
edited into them). Surfaced while closing out: the proof-of-spec standard has no artifact shape for this
cell's actual deliverable. NOT BLOCKING -- the instance passes by carrying the live write as evidence on
the script that produced it, which is what the estate's prior art already does.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W3-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~3",
    "surfaced_at": "2026-09-11T16:07:00Z",
    "one_line": "A CELL WHOSE DELIVERABLE IS A LIVE DATASTORE ROW CANNOT NAME THAT DELIVERABLE AS AN ARTIFACT: PROOF_OF_SPEC's artifacts_produced.kind enum carries s3_object but no member for a DynamoDB (or other live non-S3) write, and proof-of-spec-check.py's artifact-resolution limb exempts ONLY s3_object from git resolution -- so a row naming the table resolves as a repo path, fails the 7-40 hex / PENDING-THIS-COMMIT test, and the instance is INVALID until the live deliverable is demoted into another artifact's deploy_evidence prose.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, NOT REASONED: the first run of .tools/proof-of-spec-check.py@fd9f8ba9a4 on this order's instance returned INVALID (rc=1) with, verbatim, \"VIOLATION: artifact-resolution: 'dynamodb://etf-classifications (us-east-1, acct 313476888478) -- attribute `management_style` ...' carries commit_or_etag '...', which is neither PENDING-THIS-COMMIT nor a 7-40 hex commit-ish for a repo artifact\". The other two violations in that run were the same limb on repo paths and are a separate, correctable authoring error; this one is not correctable by better authoring.",
        "THE TWO HALVES OF THE GAP, cited: org/standards/PROOF_OF_SPEC.schema.json@fd9f8ba9a4 artifacts_produced.items.kind enum = ['script','s3_object','terraform','config_data','schedule','iam','test','doc','frontend_component'] -- one live-plane member, and it is S3-specific. .tools/proof-of-spec-check.py@fd9f8ba9a4 artifact_resolution_check() skips a row with `if a.get('kind') == 's3_object': n_s3 += 1; continue` and sends everything else through PENDING-THIS-COMMIT-or-commit-ish resolution against the repo. So the exemption is keyed to ONE storage service by name, not to the property that matters (the artifact is not a git object).",
        "NO PRIOR ART EXISTS TO COPY, which is why this was hit rather than avoided: a census of proof-of-spec instances under org/missions for 'dynamodb://' returns exactly ONE hit, and it is this order's own instance. The instances that DO record live-plane work (NFRA_OPSEC202609.TO-OP3A-S-1, NFRA_IAMROLES202609.TO-IAM-t-2) name only REPO paths with PENDING-THIS-COMMIT and carry the live state in deployed_state + deploy_evidence -- the convention exists and works, but it is a convention discovered by reading peers, not a shape the standard offers.",
        "THE COST IS NOT HYPOTHETICAL AND IT LANDS AGAIN NEXT: cell AT2-s-2 writes asset_class on these same six DynamoDB rows and its deliverable has exactly this shape. Whatever that worker does will either repeat this INVALID cycle or reproduce this workaround by luck.",
        "SCOPE HONESTY: this is a standards observation surfaced by a worker, not a defect in this project's work, and it did NOT block this order -- the instance validates once the live write rides as deploy_evidence on the script that performed it, which is the estate's existing convention. No remedy is proposed here and none is applied."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX.TO-S5-1's CLOSING OUT asserts the worker writes an instance per org/standards/PROOF_OF_SPEC.schema.json naming what it produced, and that .tools/proof-of-spec-check.py must pass before the status flip -- the implicit premise being that the standard can express this cell's deliverable, which the order itself describes as a live-world write ('the DynamoDB table is a live-world write surface, authorised for this cell').",
    "world_is": "The standard can express the SCRIPT but not the WRITE. artifacts_produced is a git-resolved surface with one service-specific escape hatch (s3_object); a DynamoDB item write has no member and no exemption, so the only valid encodings are to omit the live deliverable or to describe it in another artifact's free-text deploy_evidence -- which is what this instance does, and which means the estate's machine-readable artifact ledger structurally cannot see live datastore writes.",
    "notes": "FILED, NOT FIXED, AND DELIBERATELY NOT PROPOSED AS AN ENUM CHANGE: a value-enum proposal arrives with its four-postulate record and a word-boundary token census (CLAUDE.md Rule 24), which is a standards act several lanes outside this worker's <paths> and outside this cell. Recorded so the next live-plane cell -- AT2-s-2 first -- does not pay the same discovery cost, and so whoever owns PROOF_OF_SPEC decides whether the right fix is a new kind member, a wider exemption keyed to non-git artifacts generally, or nothing at all because the deploy_evidence convention is considered sufficient."
  }
]
```


---

A fourth row from `0.9.0_WK_POSN_ASTTAX~3`, appended as its own fenced block. Surfaced BY THE COMMIT
ITSELF: the first commit of this wave that actually files a surprise row was refused by the surprise-row
gate for a reason that has nothing to do with the rows. Remedied in-lane by widening the worktree's
sparse cone -- NOT by the audited override, which would have skipped a real check to land a clean diff.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W3-S4",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~3",
    "surfaced_at": "2026-09-11T16:14:00Z",
    "one_line": "THE WAVE-2 WORKER CONE STILL CANNOT COMMIT A SURPRISE ROW: the corrected cone recipe carries org/projects (which fixed the missions-tree hook, W2-S5/Z-S3) but NOT org/surprise_channel, and .tools/surprise-row-gate.py's standing-corpus pass resolves its schema by FILESYSTEM path -- so the first commit in this cone that files a NEW row died fail-closed on FileNotFoundError for the schema, with the rows themselves never graded.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE REFUSAL, VERBATIM, from the aborted safe-commit run in /c/tmp/wk-posn-s5 on branch wk-posn_asttax-2-5: 'ERROR: BLOCKED -- surprise-channel row gate (steps 7/10). Commit aborted; files unstaged.' / '[surprise-row-gate] BLOCKED -- 1 violation(s) on NEW rows:' / 'standing corpus pass could not run (FileNotFoundError: [Errno 2] No such file or directory: C:/tmp/wk-posn-s5\\\\org\\\\surprise_channel\\\\schemas\\\\investigation_item.schema.json) -- fail-closed'. The same run also printed '[surprise-row-gate] org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md: 3 new row(s) of 12 total checked (9 pre-existing, NOT re-graded)' -- so the gate SAW the rows and still could not grade them.",
        "THE CAUSE IS THE CONE, MEASURED: git sparse-checkout list in this worktree returned exactly 7 entries -- .tools, infra/aws/lambda/v2_portal, org/missions, org/modules, org/projects, org/ref, org/standards. org/surprise_channel is NOT among them, so org/surprise_channel/schemas/investigation_item.schema.json did not exist on disk (ls: No such file or directory) even though it is tracked and readable from the index at HEAD via git show.",
        "THE REMEDY IS EXERCISED, NOT DESCRIBED: `git sparse-checkout add org/surprise_channel` (rc=0) materialised investigation_item.schema.json (9854 bytes) and remediation_row.schema.json (10202 bytes), after which `.tools/surprise-row-gate.py --self-test` returns 'RESULT: 0 arm(s) failed of 103 (+ live census)' rc=0 and the commit proceeds. Widening the cone writes no repo content and stages nothing -- it materialises tracked blobs -- so it is not an edit outside this order's <paths>.",
        "WHAT WAS EXPLICITLY NOT DONE: the gate's own audited escape ('# surprise-row-override: <reason>' in the commit body) was NOT used. The rows were not the problem, so overriding would have landed them with the standing-corpus pass never run -- trading a visible refusal for an invisible gap. Recorded because the override was offered in the refusal text and declined deliberately.",
        "SCOPE HONESTY -- WHAT IS NOT MEASURED: whether `--self-test` alone would have FAILED in the narrow cone. It was run only AFTER the cone was widened, so this row cannot claim the self-test is or is not a sufficient pre-flight for this gate. Z-S3 records a self-test passing in the sibling wk-posn-s7 cone; whether that cone carried org/surprise_channel, or whether the self-test simply does not exercise the standing-corpus path, is UNREAD here. That distinction matters to whoever fixes this and is left open rather than guessed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This worker's face states 'All three commit gates have been verified to RUN in this cone', and the order directs the worker to file any divergence as a row in org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md, validated against org/surprise_channel/schemas/investigation_item.schema.json, and then to land everything in ONE commit through safe-commit.sh.",
    "world_is": "The gates were verified against a commit that files NO NEW ROWS. A commit that DOES file rows takes a different path through .tools/surprise-row-gate.py -- the standing-corpus pass -- which reads the schema from the worktree filesystem rather than from the index, and the cone does not carry it. So the one gate whose whole purpose is to grade surprise rows is the one that cannot run in the worktree where surprise rows are written. The rows in this commit validated cleanly against that same schema when it was read from the index (jsonschema Draft7Validator, 0 errors each), which is how the failure was distinguished from a real row defect.",
    "notes": "THIS DID NOT STOP THIS ORDER -- remedied in-lane and the commit landed with all four rows and the gate running for real. It is filed ARMED and BLOCKING because it is not specific to this worker: every sibling wave-2 worktree cut from the same recipe hits it at the moment it files its first row, which is precisely when a worker is least able to afford a puzzling refusal, and the fail-closed message names a schema path rather than a cone. The cheap fix is one more entry in the cone recipe (org/surprise_channel) -- that is the issuer's call, not a worker's, hence disarm_owner 2.0.0_SA_COO~Z. A more durable fix would be for the standing-corpus pass to read its schema from the index the way this gate's other limb already does (_schema(): 'read from the staged index, never the worktree'); that is 1.0.0_SA_CTO's surface and is named, not proposed."
  }
]
```

```json
[
  {
    "id": "POSN_ASTTAX-Z-W4-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~4",
    "surfaced_at": "2026-09-11T16:02:41Z",
    "one_line": "VXX IS a current holding -- the urgency the DT brief claimed is CONFIRMED -- but it is NOT where the brief puts it. There is no satellites artifact at all; VXX is held in the CORE models LT and ULT and is rendered in the live served positioning_data.json, so the live surface is the four partner firms' positioning page, not Satellites 70/80/90/98.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MODELS PAYLOAD, READ DIRECTLY (S7-AC4, the read the issuer said it had not done): s3://opal-data-portal-v2/benchmarks/model_20260910_v1.pkl, LastModified 2026-09-11T11:04:19+00:00 UTC by s3api, ContentLength 17682489, ETag aa2e619e77d85ffa5a1a8fc9f56112ee. Selected as the newest of 87 objects under benchmarks/model_ (client-side count over an auto-paginated list-objects-v2, sorted by LastModified -- not a page).",
        "VXX HELD, ON THE GENERATOR'S OWN RULE. The holdings frame carries 1547 rows / 56 unique tickers; VXX appears in 36 rows. The decisive read mirrors extract_current_holdings (lambda_function.py:1396-1401, latest date PER MODEL): UST 2026-07-01 no, ST 2026-08-11 no, INT 2026-08-18 no, LT 2026-08-18 YES weight 0.0150, ULT 2026-08-18 YES weight 0.0200. VXX is in the CURRENT slice of 2 of 5 core models.",
        "SECOND INSTRUMENT, DIFFERENT PLANE, so this is corroboration and not repetition: the SERVED artifact s3://opal-data-portal-v2/json/positioning/positioning_data.json (LastModified 2026-09-11T11:06:24+00:00 UTC, gzip, 8123 bytes, produced from the same run as the PKL above) carries VXX in 5 of its 198 holding objects -- $.portfolios.LT.holdings[13], $.portfolios.ULT.holdings[12], $.current_holdings.LT.holdings[13], $.current_holdings.ULT.holdings[12], $.current_holdings.AGG.holdings[20] -- each with asset_class 'Equity' and sub_asset_class 'Volatility'. VXX is not merely in the source frame; it RENDERS today.",
        "THE BRIEF'S LOCATION IS THE PART THAT FAILS. Census of the serving bucket: 0 of 4346 keys in opal-data-portal-v2 match 'satellite' case-insensitively (client-side count over an auto-paginated list-objects-v2 of every key). The positioning generator iterates MODEL_CODES = ['UST','ST','INT','LT','ULT'] (lambda_function.py:197) and the payload's own model axis carries exactly those five. No Satellites 70/80/90/98 artifact was found on this plane.",
        "AND THE REST OF THE RETAG SET IS LATENT, WHICH INVERTS THE BRIEF'S PRIORITY: of the eight tickers AT2-s-2 would move, DBC, GLD, GSG, IAU, SLV, USO and VIXY have ZERO rows anywhere in the models payload -- not merely absent from the current slice. VXX is the ONLY member of the retag set that is held at all, so VXX->Structured is the entire live blast radius and the six-way Commodities split is latent.",
        "POSITIVE AND NEGATIVE CONTROLS ON THE INSTRUMENT, so the zeros are true absences rather than a dead matcher: AGG (a known holding) reads 3 rows; the synthetic ticker ZZZZNOPE reads 0. The ticker match is whole-value, case-insensitive and whitespace-stripped."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The DT brief, carried verbatim into TO-S7-1's cell text and into this worker's face, asserts that VXX is already flowing into Satellites 70/80/90/98, framing the retag's live exposure as sitting on the satellite models.",
    "world_is": "VXX is held and the exposure is LIVE -- so the brief's urgency claim is vindicated -- but its location claim is not. VXX sits in the CURRENT slice of the CORE models LT (1.50%) and ULT (2.00%) and renders in 5 places in the live served positioning_data.json; meanwhile no satellites artifact exists in the serving bucket at all (0 of 4346 keys). The surface a retag would disturb is the partner-facing positioning page, not a satellite model.",
    "notes": "FORM ONLY, NOT SIGNIFICANCE -- the grade is the CVO's at L9. Recorded because targeting follows the brief: a check, a rollback or a render-verification aimed at Satellites 70/80/90/98 would inspect a surface this measurement could not find, while the surface that actually moves goes unwatched. WARN: SCOPE HONESTY ON THE NEGATIVE HALF: 'no satellites artifact' is measured over ONE plane, the opal-data-portal-v2 bucket. A satellites payload living in another bucket, in DynamoDB, or behind a scoped API path (see POSN_TENANCY's 'scoped api path for the satellites') would NOT be visible to this census, and this row does not claim otherwise. What is established without qualification is the POSITIVE half: VXX is held in the core models and served today."
  },
  {
    "id": "POSN_ASTTAX-Z-W4-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~4",
    "surfaced_at": "2026-09-11T16:02:41Z",
    "one_line": "THE FRONTEND CONTRACT HOP IS UNTRACED AND UNTRACEABLE FROM THIS WORKTREE: my order names 'a frontend contract' as a distinct hop class, but portal/ is outside the sparse cone, so 29577 files were UNREADABLE to every census I ran. The served asset_class value post-retag is 'Unknown', and whether the renderer tolerates it has been measured by nobody.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CONE, MEASURED: git sparse-checkout list in /c/tmp/wk-posn-s7 returns exactly .tools, infra/aws/lambda/v2_portal, org/missions, org/modules, org/projects, org/ref, org/standards. 'ls portal' returns EMPTY. portal/ is not present to be read.",
        "THE CENSUS DISCLOSED ITS OWN BLIND SPOT and I am quoting its denominator line rather than paraphrasing it -- S7-AC1, verbatim: 'DENOMINATOR: 500 hit(s) across 3426 file(s) scanned in scope [corpus=all] | 10 EPHEMERAL-FLOOR, NOT searched (--corpus raw reads these) | 29577 UNREADABLE, NOT searched | 26 BINARY, NOT searched'. The 29577 UNREADABLE is the out-of-cone remainder. The 500 hits certify the SWEEP, not the SET.",
        "THE FRONTEND CONSUMER IS NAMED IN-CONE, so this is a known hop rather than a speculative one: org/modules/graph/estate-coverage-resolver.json:2924 records 'portal/src/api/portal-proxy.ts getPositioningData -> /api/general/positioning/positioning_data.json', and org/projects/ETFS_INGEST.json:47 records a ruling about what 'HoldingsTab.tsx renders'. The consumer exists and is identified; it is simply not readable from here.",
        "WHY IT MATTERS RATHER THAN BEING A TIDINESS NOTE: S7-AC3 measured that three separate served-output hops (lambda_function.py:1272-1286, :1416-1430, :1908-1930) rewrite an unmapped class to the literal string 'Unknown' in the fields 'asset_class' and 'assetClass'. So the retag does not merely fail to propagate a new class -- it PUBLISHES a new literal value into a served contract whose consumer has not been inspected. A frontend that buckets, filters or switches on asset_class is an 18th hop, and it is the one hop nobody in this chain has read.",
        "SCOPE OF THE CLAIM: this row asserts NOT-MEASURED, not BROKEN. I make no claim about how the portal behaves on 'Unknown' -- I am recording that the question is open and that my grant and my cone both stop short of it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-S7-1's act names a frontend contract as one of the hop classes the trace must cover ('a value can be carried by a dict key, a comparison chain, a schema field or a frontend contract, and each is a separate hop'), and S7-AC1 asks for a census whose count equals its denominator.",
    "world_is": "The census count did equal its denominator (500 of 500) but only WITHIN the cone; 29577 files including all of portal/ were never searched, and the tool said so on its own denominator line. The frontend-contract hop is therefore enumerated in principle and measured in neither AC1 nor AC3. My write grant and my sparse cone both exclude portal/, so closing it is not an act available to this cell.",
    "notes": "NOT AN OVERRIDE REQUEST AND NOT A SCOPE COMPLAINT -- per CLAUDE.md a path I need that my order's <paths> lacks is a row on the criterion, never a widening, and I did not widen. The AC3 hop set is bounded by AC2 (the generator file) exactly as the criterion defines it, so this does not make AC3 incomplete against its own contract; it bounds how far the WORD 'end to end' in AC6 can be taken, which is why it is filed rather than mentioned. SECOND, SMALLER INSTANCE OF THE SAME CAUSE, recorded here rather than as its own row because the cause is identical, AND CARRYING ITS OWN REMEDY SO IT IS NOT READ AS AN OPEN GAP: org/surprise_channel/schemas/investigation_item.schema.json is also outside the cone and unreadable from the worktree filesystem. It IS reachable in the object store, so these rows were validated against the real schema after extracting it with `MSYS_NO_PATHCONV=1 git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json` (9854 bytes), the same route 0.9.0_WK_POSN_ASTTAX~2 used. THE DISTINCTION THAT MATTERS FOR THE PRIMARY CLAIM ABOVE: a SCHEMA is a single known path and survives object-store extraction; the portal FRONTEND hop is a search over an unknown file set, and no git-show of a path I cannot first enumerate substitutes for a census. The cone blinds a SEARCH in a way it does not blind a FETCH, which is why the frontend half of this row stands unremedied while this half does not."
  },
  {
    "id": "POSN_ASTTAX-Z-W4-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~4",
    "surfaced_at": "2026-09-11T16:02:41Z",
    "one_line": "THE KeyError PREMISE NO LONGER HOLDS, AND ITS RETIREMENT MADE THE FAILURE QUIETER RATHER THAN SAFER: 0 of 17 hops RAISE on a five-class value now that AT2-s-6 has landed, while 14 of 17 SILENTLY DROP it. This defeats TO-S2-1's S2-AC5 as written -- 'confirm the page still renders' is a criterion that cannot discriminate, because the page WILL render, showing 'Unknown'.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE SUPERSEDED PREMISE, QUOTED FROM THE ORDER THAT STILL CARRIES IT: TO-S2-1 BOUNDS reads 'Retagging a HELD ticker to a class the generator does not carry raises KeyError, kills the generator, and blanks the positioning page for all four partner firms.' TO-S7-1's cell text carries the same shape ('the issuer measured the KeyError at the subscript').",
        "MEASURED AT HEAD (S7-AC3, harness bound to the file's real bytes -- each hop's literal source is extracted from lambda_function.py and executed, and the executed text is printed beside its result): HOPS TESTED 17, SURVIVES 3, SILENTLY DROPPED 14, RAISES 0. Accounting closed by subtraction from the AC2 denominator: 79 of 79 enumerate hits fall inside a tested hop, 0 unassigned, hops tested == hops enumerated.",
        "WHY THE RAISE IS GONE, and it is not an accident: AT2-s-6 replaced the direct subscript with a seeded-plus-fallback accumulator (lambda_function.py:258-264) whose own comment states the design -- 'The canonical keys stay seeded, so every fixed-list consumer of these dicts keeps finding them.' That is exactly why the four hardcoded four-class consumers (:894-897, :953-956, :1960-1961) no longer KeyError: they still find their four seeded keys. The hardening removed the CRASH and left the DROP.",
        "THE DISCRIMINATION FAILURE, STATED CONCRETELY. S2-AC5 asks a successor worker to 'confirm the page still renders'. Post-AT2-s-6 the page renders in BOTH the healthy and the broken world, so that criterion returns the same observation either way -- the always-passes shape. The broken world is specifically: three served-output hops rewrite the class to the literal 'Unknown' (:1272-1286, :1416-1430, :1908-1930), the allocation spread and delta omit it entirely (:894-897, :953-956, :1960-1961), and the benchmark allocation silently loses the weight because its if/elif chain has no else (:389-407, probe weight 0.25 accumulating to TOTAL 0.000).",
        "AND IT IS LIVE, NOT HYPOTHETICAL, because of W4-S1: VXX is in the current slice of LT and ULT and renders in 5 places today as 'Equity'. Retagging VXX to 'Structured' turns those 5 served rows into 'Unknown' on the next generator run, with no exception, no log line from the display hops, and a page that still draws.",
        "NEGATIVE CONTROL ON THE HARNESS, so 'SILENTLY DROPPED' is not a dead probe: at every comparison hop the controls 'equity' and 'fixed_income' DO take their branches (printed per hop), and at the display hops 'equity' maps to 'Equity'. The maps and branches work; they simply carry four keys."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-S2-1 asserts the retag's failure mode is a KeyError that kills the generator and blanks the positioning page, and gates its own safety on that tell -- S2-AC5 verifies the retag by confirming the page still renders.",
    "world_is": "After AT2-s-6 the generator does not raise at all on a five-class value: 0 RAISES of 17 hops. It absorbs the value at the seeded accumulator and then drops it at 14 downstream hops, three of which publish the literal 'Unknown' into the served asset_class/assetClass fields. The page renders in both the healthy and the broken world, so the successor's verification step cannot distinguish them.",
    "notes": "FORM ONLY; the grade and any recut are the CVO's at L9 and the COO's at L10. Recorded because the two facts point OPPOSITE ways and could cancel if read singly: 'the KeyError is fixed' reads as reassurance and is true, while 'the tell that the retag went wrong has been removed along with it' is the same fact and is the hazard. Note also that this row does NOT argue AT2-s-6 was wrong -- carrying the value under its own name rather than folding it into a catch-all is what makes the drop COUNTABLE at all, and it is why H4 reads SURVIVES with a WARN line naming the ticker. What is owed is a discriminating acceptance step downstream of it, and that is a cut decision, not mine."
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


---

## Row appended by `2.0.0_SA_COO~Z` at L7 (trigger bound on W3-S1), 2026-09-11

One row from the issuer, bounding a worker's ARMED row without disarming it. `W3-S1` keeps
`hazard_standing: ARMED` -- that field is at-surfacing and immutable, and this row does not
disposition it either. The CVO's L9 `adjudicates` remains the only carrier that can.

```json
[
  {
    "id": "POSN_ASTTAX-Z-S4",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T16:39:53Z",
    "one_line": "BOUNDS POSN_ASTTAX-Z-W3-S1 AND DELIBERATELY DOES NOT DISARM IT. The seeder revert W3-S1 describes is real and un-remedied, but it has NO automatic trigger: an unscoped census over 111 references in 56180 files found zero invokers, and the one gold-producer candidate references the seeder only in comments (CODE=0, COMMENT=2). The hazard is LATENT, not imminent -- and as the named disarm_owner I am declining to disarm it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TRIGGER CENSUS, UNSCOPED, AT THIS SESSION'S VINTAGE. comp-find 'seed-etf-classifications' --all --files: DENOMINATOR 111 hit(s) across 56180 file(s) scanned [corpus=all], bands HEAD=33 SURFACED=26 CONFIG=8 DOC=44. I then INSPECTED what the census found rather than stopping at the count -- the step that matters, because an unscoped read only falsifies a domain if you look at what it surfaced outside it.",
        "THE ONE CANDIDATE THE ROUND-1 DOMAIN COULD NOT HAVE COUNTED, AND IT IS NOT AN INVOKER. The HEAD band surfaced a GOLD PRODUCER SCRIPT, data/etfs/scripts/gold/etf_positioning_publisher.py -- and gold pipelines are scheduled by estate law, so a reference there is the one shape that would overturn 'no automatic trigger'. Measured with comp-read --enumerate 'seed-etf-classifications|seed_etf_classifications': 2 hit(s) across 707 lines, bands DOCSTRING=0 COMMENT=2 DEF=0 CODE=0, both at :188 and :220 citing 'seed-etf-classifications.py:62' as a CONTRAST to how that script writes. Comments, not calls. The gold script does not invoke the seeder.",
        "SO ROUND 1'S VERDICT STANDS, REACHED BY A DIFFERENT INSTRUMENT. S1a-AC6 (instance at HEAD, deliverables/0.9.0_WK_POSN_ASTTAX~1/) reported 'DENOMINATOR: 45 hit(s) across 30964 file(s)' and a verdict of no scheduler, EventBridge rule, CI workflow, deploy script or step function. That was an enumeration of trigger TYPES -- a forward list, the shape Rule 24 warns omits silently. This row re-took it as a SUBTRACTION from all 111 references and reached the same answer, so the two do not merely repeat each other: the second read could have falsified the first and did not.",
        "WHAT THAT DOES AND DOES NOT BUY. It bounds W3-S1 from IMMINENT to LATENT: nothing on a clock reverts the six rows. It does NOT make the revert less real -- seed-etf-classifications.py still does an unconditional full-item put, the six commodity tickers are still absent from ETF_MANAGEMENT_STYLE in all three module copies, and a DELIBERATE manual run still rewrites management_style to 'unknown' on exactly the six rows AT2-s-5 corrected. A manual CLI run is not a trigger a census can see, and this row does not claim otherwise.",
        "NEGATIVE CONTROL ON THE CENSUS INSTRUMENT: the same comp-find pattern returns the two seed scripts themselves and _shared/etf_classification.py in the HEAD band, so the matcher does reach real code files and its silence on invokers is an absence rather than a blind probe. SCOPE LIMIT, STATED: comp-find is REPO-ONLY. An invocation living only in a human runbook, an operator's shell history, or an agent's habit is outside every instrument used here and is exactly how a 'manual-only' script gets run."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX-Z-W3-S1 (ARMED, disarm_owner 2.0.0_SA_COO~Z) asserts that the next seed run silently rewrites management_style back to 'unknown' on the six rows AT2-s-5 corrected and asset_class back to 'hedge' on the six rows AT2-s-2 would move, and records its own trigger as UNMEASURED ('manual CLI, no invoker census run').",
    "world_is": "The revert mechanism is confirmed exactly as W3-S1 states it and is NOT contested here. What was unmeasured is now measured: there is no scheduler, no pipeline and no code path that fires the seeder. It runs only when a person or an agent deliberately runs it. That changes the hazard's CLOCK, not its CONTENT.",
    "notes": "WHY THIS IS NOT A DISARM, stated plainly because I am the seat entitled to file one. A disarm would need the revert to be impossible or remedied; it is neither. The remedy is a code-map edit (add the six tickers to ETF_MANAGEMENT_STYLE across the three module copies) that lies outside every cell of round 2, so no order in this round can close it and I will not manufacture one mid-round -- the spec and decomposition are FROZEN. W3-S1 therefore stays ARMED and travels to L9 with this bound attached. FOR THE L8/L9 READER: the practical consequence is that AT2-s-5's six writes are DURABLE IN PRACTICE until someone runs the seeder, and the same is true of any retag AT2-s-2 would perform -- which is one more reason the AT2-s-7 NO-GO should not be read as the only thing standing between this round and the retag. TWO DEFECTS, ONE OF WHICH IS NOT THE CHAIN: the chain drops five-class values (W4-S3), and the registry does not hold them against a re-seed (W3-S1)."
  }
]
```

---

Two rows from `0.9.0_WK_POSN_ASTTAX~6` (cell `AT2-s-1`, task order `POSN_ASTTAX.TO-S1-1`),
appended as ONE fenced block. Both are about the ORDER'S OWN CRITERIA rather than the code under change,
and neither stopped the order: `S1-AC5`'s invocation does not resolve from the cwd its sibling criteria
require and fails with the same text a genuinely missing predecessor would produce, and `S1-AC1` measures
a property of the INPUT bytes that this order's act deliberately removes.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W6-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~6",
    "surfaced_at": "2026-09-11T17:40:00Z",
    "one_line": "S1-AC5's invocation CANNOT RUN FROM THE CWD ITS SIBLING CRITERIA REQUIRE: it names ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md while S1-AC1/AC2/AC4 name repo-root-relative paths, so run as written from the repo root it returns rc=2 'No such file or directory' -- and that failure is INDISTINGUISHABLE from the negative it exists to detect (the predecessor order missing/not complete), which is a STOP condition for this order.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AS WRITTEN, FROM THE REPO ROOT (/c/tmp/wk-posn-s1, branch wk-posn_asttax-2-1 @f937521939): `timeout 120 grep -n \"<status>\" ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md` -> 'grep: ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md: No such file or directory', RC=2. The comp-tool rail did NOT deny the single-file grep; the failure is purely the relative path.",
        "THE SAME COMMAND, SAME BYTES, FROM org/missions/D4/POSN/POSN_ASTTAX/deliverables/ -> '8:<status>complete</status>' and '68:  `<status>` to `complete`.', RC=0. So the criterion's expectation is satisfiable and the predecessor IS terminal; only the cwd was wrong. Nothing was substituted for the instrument: the command text is identical, byte for byte.",
        "NO CWD SATISFIES ALL FIVE MECHANICAL CRITERIA AS WRITTEN. S1-AC1, S1-AC2 and S1-AC4 name 'infra/aws/lambda/v2_portal/...' and 'git -C .', which resolve at the repo root; S1-AC5's '../task-orders/...' resolves only from a directory that is a SIBLING of task-orders (or from task-orders itself). The two sets do not intersect -- verified by reading the order's own <criterion> invocations at org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S1-1.unknown-is-not-equity.md@f937521939.",
        "CORROBORATION FROM THE ARTIFACT, NOT THE INSTRUMENT: commit 7f247caae0 ('L7(POSN_ASTTAX.TO-S6-1, 0.9.0_WK_POSN_ASTTAX~2): harden the positioning generator ... cell AT2-s-6, chain head') is an ancestor of this worktree's HEAD -- `git log --oneline -- <lambda path>` lists it as the most recent commit on the shared file. That is a SECOND instrument for the same claim (the predecessor is done and its work is already in my bytes), so the AC5 verdict does not rest on the grep alone."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order makes S1-AC5 a STOP: 'the status line pasted verbatim reading `complete`; if not, this order STOPS and files a row rather than editing the same file underneath an unfinished cell.' The worker face repeats it and adds that a rail denial (not a path failure) is the anticipated substitution, to be recorded rather than silently swapped.",
    "world_is": "The anticipated failure mode (rail denial) did not occur. A DIFFERENT one did: the invocation's relative path does not resolve from the cwd every other criterion in the same order requires. Run as written from the repo root it fails rc=2 with 'No such file or directory' -- the exact text a genuinely missing predecessor order would produce. A worker that took that output at face value would STOP this order on a false negative; a worker that re-ran it from the right cwd, as this one did, gets 'complete'.",
    "notes": "THIS DID NOT STOP THIS ORDER. The substitution made was CWD ONLY -- same command, same file, no change of instrument -- and both readings are recorded in the proof-of-spec instance with their cwds. Filed ARMED because the harm is in FUTURE normal operation, not this turn: any seat re-running S1-AC5 verbatim at L9 from the repo root to check this worker's claim gets rc=2 and a false ABSENCE, and an instrument whose failure is indistinguishable from the negative it tests for is the classic silent-stop shape. Disarm is one character of issuer text (an absolute or repo-root-relative path in the criterion), which is the issuer's surface, not a worker's -- hence disarm_owner 2.0.0_SA_COO~Z. The same '../' shape appears in this order's <decomp_ref>/PRD pointers, which are prose and harm nothing; only the mechanical criterion is affected."
  },
  {
    "id": "POSN_ASTTAX-Z-W6-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~6",
    "surfaced_at": "2026-09-11T17:44:00Z",
    "one_line": "S1-AC1 IS A PRE-EDIT MEASUREMENT WHOSE OUTPUT THIS ORDER'S OWN ACT DESTROYS: it asks for 'the three sites and their disagreement' and for a count of DISTINCT defaults, but the act it accompanies collapses the three asset_class call sites to one, so the same invocation re-run at the resulting commit returns ONE line and one default -- not three and two.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRE-EDIT, at f937521939 (the branch point), invocation verbatim from the repo root, RC=0, 4 lines: '91:    return registry_field(ticker, 'management_style', 'passive')  # Default to passive if unknown' / '219:    return registry_field(ticker, 'asset_class', 'fixed_income')  # Default to FI if unknown' / '390:            asset_class = registry_field(ticker, 'asset_class', 'equity')  # Default to equity if unknown' / '550:            asset_class = registry_field(ticker, 'asset_class', 'equity')'. asset_class subset = 3 sites, DISTINCT defaults = 2.",
        "POST-EDIT, same invocation, same cwd, RC=0, 2 lines: '91:    return registry_field(ticker, 'management_style', 'passive')  # Default to passive if unknown' / '258:    return registry_field(ticker, 'asset_class', UNCLASSIFIED_ASSET_CLASS)'. asset_class subset = 1 site, DISTINCT defaults = 1.",
        "THE CAUSE IS THE ACT, NOT A DEFECT: the order directs 'Re-take the three sites' AND 'Make an unrecognised ticker RENDER AS UNRECOGNISED', and the shape chosen routes the two benchmark call sites through classify_etf so the default is defined once. The three sites are therefore a property of the INPUT vintage, not of the deliverable.",
        "NOT A HIDDEN DELETION: git diff --stat HEAD for the file reads '1 file changed, 101 insertions(+), 8 deletions(-)' and the pre-edit line text is recoverable at any time by `git show f937521939:<path>` -- the negative control at deliverables/0.9.0_WK_POSN_ASTTAX~6/negative_control_unknown_is_not_equity.py does exactly that and asserts a positive control on the two old default literals before it will run."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S1-AC1 <expect>: 'every numbered line pasted verbatim, the `asset_class` subset separated from other fields, each with its default named, and the count of DISTINCT defaults across the asset_class sites only', labelled 'THE THREE SITES AND THEIR DISAGREEMENT, RE-TAKEN'. The worker face adds 'AC1 re-measures them and AC1's output is the truth'.",
    "world_is": "The criterion's subject (three disagreeing sites) exists only in the bytes the order starts from. The commit this order produces does not contain three asset_class default sites, so the criterion is not reproducible at the artifact it certifies -- its evidence is vintage-bound in a way the criterion text does not say.",
    "notes": "FILED FOR FORM, NOT SIGNIFICANCE, and it blocked nothing. Mitigated inside the deliverable rather than left to a re-run: the proof-of-spec instance records BOTH readings, each with its own cwd, commit-ish and line numbers, and names which one is the criterion's answer (the pre-edit one). Flagged INERT because the mitigation travels with the instance -- a grader reading the instance has both numbers in front of it and needs no re-run. Raised at all because the general shape is worth the issuer's attention: a BEFORE-measurement criterion and an AFTER-state criterion in the same order both grade 'the file', and only one of them can be true at the commit."
  }
]
```


---

## Row appended by `2.0.0_SA_COO~Z` at L7 (drain-end disarm + declared declines), 2026-09-11

One row from the issuer at the end of the wave-2 drain. It disarms `W3-S4` on exercised evidence and
records, in the plane L9 actually reads, which of this seat's remaining ARMED rows are NOT being
disarmed and why. Nothing here dispositions anything -- that is the CVO's L9 act via `adjudicates`.

```json
[
  {
    "id": "POSN_ASTTAX-Z-S5",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T17:09:15Z",
    "one_line": "DISARM of POSN_ASTTAX-Z-W3-S4 (BLOCKING, the cone missing org/surprise_channel): cause was mine, remedy applied to the two live sibling worktrees mid-flight and built into the fourth, and it is now EXERCISED AT THE COMMIT by four real worker commits and four merged-index drains -- discharging the explicit limit my earlier row Z-S3 placed on itself. Also records, as disarm_owner, my DECLINED disarms on W4-S1, W4-S2, W4-S3 and W6-S1 with a reason for each.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE GAP WAS REAL AND IS MINE: I cut the wave-2 cones carrying seven directories and org/surprise_channel was not among them, so surprise-row-gate.py's standing-corpus pass could not read its own schema from the worktree. 0.9.0_WK_POSN_ASTTAX~3 hit it fail-closed at its first surprise row and remedied its own worktree with `git sparse-checkout add org/surprise_channel` -- deliberately NOT with the audited `# surprise-row-override:` escape, which is the right call and the reason its rows were graded for real.",
        "REMEDY APPLIED TO THE LIVE SIBLINGS BEFORE THEY REACHED IT, at ~16:0xZ: `git sparse-checkout add org/surprise_channel` run against /c/tmp/wk-posn-s7 and /c/tmp/wk-posn-s4 while both workers were mid-execution; each reported 'schemas present: 2 file(s)'. The fourth worktree /c/tmp/wk-posn-s1 was cut AFTER the finding and carried org/surprise_channel from creation (verified at cut: schemas=2). So 4 of 4 wave-2 worktrees ended up with the directory and none of the three later workers hit the refusal.",
        "EXERCISED AT THE COMMIT, WHICH IS THE BAR MY OWN EARLIER ROW SAID WAS STILL OWED. POSN_ASTTAX-Z-S3 disarmed the org/projects cone gap but stated its limit explicitly: 'the exercise ran the gates DIRECTLY, not through a real safe-commit of a worker diff ... EXERCISED-AT-THE-GATE, not EXERCISED-AT-THE-COMMIT.' That caveat is now discharged by four real worker commits that each passed safe-commit with the row gate grading their rows: eec92c9cf2 (~3), 8a911af2d7 (~4), 95e59e1408 (~8), c34eab85dc (~6).",
        "CORROBORATED ON THE MERGED INDEX, a second instrument and a stricter one, since a worker's own commit is graded against its worktree index while the drain is graded against the union: the four drains 6ea4a9d1ef, 7c014732d4, bead9019ce and 7dc668da2d each printed '[surprise-row-gate] ... N new row(s) of M total checked' followed by 'OK: 1 file(s), all new rows carry their step-7/step-10 fields', with no override in play on any of them. Channel now 24 rows, 24 VALID / 0 INVALID against investigation_item.schema.json.",
        "WHAT IS NOT CLOSED, so this disarm is not read wider than it is: the HOOK's underlying property is unchanged -- surprise-row-gate.py still reads its schema from the WORKTREE and still has no --staged mode, exactly as W2-S3 and W2-S4 record for the sibling gates (both 1.0.0_SA_CTO~Z's to disposition). Any future seat cutting a cone without org/surprise_channel reproduces this refusal identically. THE RECIPE, NOT THE HOOK, IS WHAT WAS FIXED. The complete cone measured sufficient across four worktrees this round is: .tools, org/projects, org/missions, org/modules, org/ref, org/standards, org/surprise_channel, plus the infra subtree the cell needs."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "POSN_ASTTAX-Z-W3-S4 asserts that the first safe-commit in a wave-2 cone is refused fail-closed because surprise-row-gate.py's standing-corpus pass reads org/surprise_channel/schemas/ from the WORKTREE and the cone does not carry it, and that every sibling worktree hits this at its first surprise row.",
    "world_is": "Exactly as stated, and it was my cone recipe at fault rather than the gate. The directory was added to both live siblings mid-execution and built into the fourth worktree at cut, so 4 of 4 ended up carrying it and only the surfacing worker ever hit the refusal. Four worker commits and four drains then passed the row gate with no override in play, which is the end-to-end proof Z-S3 said it did not yet have.",
    "notes": "SCOPE: this row disarms W3-S4 ONLY. It dispositions nothing -- the CVO's L9 `adjudicates` is the only carrier that can -- and W3-S4 keeps hazard_standing ARMED, which is at-surfacing and immutable.\n\nRECORDED HERE BECAUSE THE CHANNEL IS WHERE L9 READS, NOT A MESSAGE: as the named disarm_owner I am DECLINING to disarm my four remaining ARMED rows, and the reason differs per row. None is an oversight and none should be read as pending my further action this round.\n  - W4-S1 (VXX held, but the DT brief's stated satellites location fails -- 0 of 4346 bucket keys match 'satellite'). NOT DISARMED: the brief's location claim is wrong and nothing in round 2 owns correcting a DT brief. It is an L10 input.\n  - W4-S2 (BLOCKING -- the frontend-contract hop was never measured; portal/ is outside the worker cone and the census itself printed 29577 UNREADABLE). NOT DISARMED: it is a genuine MEASUREMENT GAP, not a remedied defect. I did not measure it myself because it can only STRENGTHEN the AT2-s-7 NO-GO, never weaken it, so it changes no decision this round -- but an unmeasured hop must not travel as though it were measured.\n  - W4-S3 (BLOCKING -- the KeyError premise is retired; 0 of 17 hops RAISE, which defeats TO-S2-1's S2-AC5). NOT DISARMED, and it must not be: this is the round's most consequential finding. The retag order's acceptance criterion returns the SAME reading in the healthy and the broken world. Fixing it is an L10 re-cut, and the spec is FROZEN mid-round under Rule 27.\n  - W6-S1 (AC5's relative path fails with the exact text a missing predecessor produces -- a STOP criterion whose failure is indistinguishable from its own negative). NOT DISARMED: the worker discriminated in practice with a second instrument (git ancestry of 7f247caae0), but the CRITERION TEXT is still non-discriminating for the next reader. Same class as W4-S3 and the same remedy: an L10 re-cut, not a mid-round edit.\n\nTWO OF MY FOUR DECLINES ARE THE SAME DEFECT CLASS -- a criterion that cannot fail in the broken world (W4-S3, W6-S1). That is a pattern in this round's authorship, mine as issuer, and it belongs in the round-2 analysis rather than in any single row."
  }
]
```

---

## Rows appended by `0.9.0_WK_POSN_ASTTAX~12` at L7 (TO-T3-1, cell `AT3-s-3`), 2026-09-11

Three rows from the hop-test of the two sibling consumers `TO-S7-1` enumerated but never tested.
`W12-S1` reconciles the inherited hit counts. `W12-S2` and `W12-S3` are two DISTINCT two-class
assumptions baked into `yang-generate-allocation-summary`, both ARMED against the retag this cell
gates. Neither was fixed: this cell is READ-ONLY ON BEHAVIOUR by its own bound.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W12-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~12",
    "surfaced_at": "2026-09-11T17:56:00Z",
    "one_line": "The inherited '67 hits / 32 hits' figures for the two sibling consumers are correct NUMBERS at the WRONG GRAIN: re-measured at 651ffd4f16 the two files carry 93 and 49 asset_class HITS, and 67 and 32 are exactly their DISTINCT-LINE counts. Nothing downstream is wrong; the word 'hits' is.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC SIDE: TO-T3-1's cell text (org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.md@651ffd4f16) carries the fenced block 'yang-generate-allocation-summary 67 hits / yang-generate-holdings-attribution 32 hits', inherited from TO-S7-1. The order's own <preflight> declares this: 'the issuer inherits TO-S7-1's hit counts (67 and 32) as ITS figures at ITS vintage and has not re-derived them; AC1 re-takes both denominators independently.' This row is that re-take reporting back.",
        "WORLD SIDE, INSTRUMENT 1 (comp-read, the AC1 invocation, run verbatim): allocation-summary 'ENUMERATE: 93 hit(s) across 378 lines / 8 section(s) scanned | 9 whole | 84 sub'; holdings-attribution 'ENUMERATE: 49 hit(s) across 696 lines / 14 section(s) scanned | 19 whole | 30 sub'. Both rc=0.",
        "WORLD SIDE, INSTRUMENT 2 (deliberately DIFFERENT, so this is corroboration and not repetition -- raw substring-occurrence recount in the AC2 harness, which never calls comp-read): reproduces 93 and 49 as HIT counts ('RECONCILE vs T3-AC1 comp-read: allocation-summary expect 93, got 93 MATCH | holdings-attribution expect 49, got 49 MATCH') AND independently yields 'distinct lines carrying the token=67' for allocation-summary and '=32' for holdings-attribution -- the inherited pair, exactly, with no rounding.",
        "SO THE RESOLUTION IS GRAIN, NOT STALENESS: 67 and 32 are the DISTINCT LINES that carry the token; 93 and 49 are the OCCURRENCES of the token. A line like ':173 qtd_asset_classes = aggregate_by_asset_class(' is 1 line and 2 hits, which is precisely where the two series diverge. No commit moved between TO-S7-1's read and mine that could explain a 26/17 drift, and none is needed.",
        "WHY IT IS STILL WORTH A ROW RATHER THAN A SILENT CORRECTION: the figures travel as 'hits' into the round-3 cell text and would be compared, by the next reader, against a comp-read denominator that counts something else. A denominator certifies the SWEEP, never the SET (Rule 22) -- and here two correct sweeps of the same files disagree by 41 because they count different objects."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-T3-1's cell (inheriting TO-S7-1) asserts the two sibling consumers carry 67 and 32 asset_class HITS respectively.",
    "world_is": "At 651ffd4f16 the files carry 93 and 49 asset_class HITS (comp-read, and an independent substring recount agreeing exactly). 67 and 32 are the DISTINCT-LINE counts of the same two files, reproduced to the unit by the second instrument. The inherited figures are right about the files and wrong about the unit; no measurement below this row depends on the inherited pair.",
    "notes": "Filed by the worker whose AC1 re-take produced the divergence, per the order's bound that a divergence is a row. This CHANGES NOTHING in T3-AC2: the hop set was rebuilt from the files at my own vintage, not from the inherited counts. Stated for L9 so the round-3 record does not carry two incompatible meanings of the same number."
  },
  {
    "id": "POSN_ASTTAX-Z-W12-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~12",
    "surfaced_at": "2026-09-11T17:56:10Z",
    "one_line": "yang-generate-allocation-summary's own comment says Commodities is folded into Equity; its CODE has no Commodities branch at all and passes the value through as its own asset-class row -- which then draws policy_weight 0.0 from a fixed-key benchmark table, so the row renders with a 'bet' equal to its ENTIRE weight. The value survives; its economics do not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC SIDE, TWO PLACES IN THE CONSUMER'S OWN TEXT (infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py@651ffd4f16): :43-44 'Canonical two-asset-class model: Fixed Income and Equity only / (Cash folded into Fixed Income, Hedge/Commodities folded into Equity)'; and the function docstring at :237 'Canonical reclassification: Cash -> Fixed Income, Hedge -> Equity.' The first NAMES Commodities explicitly as a folded class.",
        "CODE SIDE, THE SAME FILE :247-256, read in full: branches exist for ('fixed_income','fixed income') -> 'Fixed Income'; 'equity' -> 'Equity'; 'cash' -> 'Fixed Income'; 'hedge' -> 'Equity'; and then `else: asset_class = raw_asset_class`. There is NO Commodities branch. The else is a PASS-THROUGH, so the comment at :44 is false for the one class it names that the code does not handle.",
        "MEASURED, NOT INFERRED -- a REAL call into the real module under sys.settrace (deliverables/0.9.0_WK_POSN_ASTTAX~12/ac2_hop_harness.py): five-class input ['Commodities','Equity','Fixed Income','Real Estate','Cash'] -> aggregate_by_asset_class(...,'INT') returns ['Fixed Income','Equity','Commodities','Real Estate']. Commodities SURVIVES as its own row and Cash correctly folds. The same call through the OUTER function generate_allocation_summary with a five-class S3 payload returns the identical INT/qtd row set.",
        "THE ARMED PART, from the same measured run: BENCHMARK_ALLOCATIONS at :45-52 is a fixed-key dict carrying only 'Fixed Income' and 'Equity' per model, and :267 reads it as `benchmark_allocations.get(asset_class_name, 0.0)`. Measured output rows: name=Commodities style_weight=10.0 policy_weight=0.0 bet=10.0; name=Real Estate style_weight=10.0 policy_weight=0.0 bet=10.0 -- against Fixed Income -10.0 and Equity -10.0. `bet` is style_weight minus policy_weight, so every class outside the two-key table is rendered as a 100%-overweight position against a zero policy.",
        "DISCRIMINATION: the harness carries a POSITIVE CONTROL -- a deliberately fixed-key reducer over the SAME five-class input returns ['Fixed Income','Equity'] and the harness reports it 'SILENTLY DROPPED'. So the instrument demonstrably CAN report a drop; it reports SURVIVES here because the value survives. And the two-class negative control returns ['Fixed Income','Equity'] with no probe present, so a pass is not an artifact of the probe being unfindable."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell AT3-s-3 asks whether either sibling 'buckets asset_class into its own fixed-key structure' such that a retag 'silently zeroes or mislabels there too'. yang-generate-allocation-summary's own comment at :44 asserts Commodities is folded into Equity.",
    "world_is": "Neither claim holds as written. The code has no Commodities branch and passes the value through (:255-256), so Commodities is NOT folded into Equity -- it survives as its own row, and the comment at :44 is wrong. But the fixed-key structure the cell feared is REAL and sits one hop later: BENCHMARK_ALLOCATIONS (:45-52) carries only Fixed Income and Equity, and :267 defaults every other class to policy_weight 0.0, measured as Commodities bet=10.0 on a 10.0 weight. The retag will not ZERO the class; it will MISLABEL its policy economics.",
    "notes": "ARMED against AT3-s-6, the retag this cell gates. The hazard is not visible today because no five-class value reaches this consumer in production; it fires the moment the retag lands and a Commodities/Real Estate ticker appears in holdings_attribution_data.json. NOT FIXED HERE BY DESIGN -- TO-T3-1's bound is READ-ONLY ON BEHAVIOUR, and a cell that fixes what it measures cannot report on it cleanly. disarm_owner is the issuer because the remedy is a scope decision (extend BENCHMARK_ALLOCATIONS to five keys per model, or accept 0.0 policy for satellite classes) that belongs to whoever cuts AT3-s-6, not to this worker."
  },
  {
    "id": "POSN_ASTTAX-Z-W12-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~12",
    "surfaced_at": "2026-09-11T17:56:20Z",
    "one_line": "Three separate sites in yang-generate-allocation-summary are shaped for EXACTLY two asset classes and silently change behaviour at five -- the symmetric-tilt block stops executing entirely (measured NOT-REACHED under five classes while REACHED under two), the sort key knows only two names, and the placeholder path emits a hardcoded two-row list. No exception, no log, no drop: the logic just stops applying.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SITE 1 -- :306-311 `if len(asset_classes) == 2:` guards the FI/Equity symmetric-tilt enforcement (`asset_classes[eq_idx]['bet'] = round(-fi_bet, 2)`). MEASURED by sys.settrace line coverage over the real module: lines 307, 308, 310, 311 appear in the executed set of the TWO-CLASS control run and are ABSENT from every five-class run. The harness reports them 'NOT-REACHED under five classes (runs ONLY on the 2-class / error path)'. The tilt enforcement is not wrong at five classes -- it is simply gone, with nothing announcing it.",
        "SITE 2 -- :291-292 `asset_class_order = {'Fixed Income': 1, 'Equity': 2}` then `.sort(key=lambda x: asset_class_order.get(x['name'], 99))`. Every class outside the two named collapses to the same sort key 99, so their relative order is dict-insertion order, i.e. whatever order holdings happened to arrive in. Measured five-class output order: ['Fixed Income','Equity','Commodities','Real Estate'] -- correct-looking here only because insertion order happened to agree.",
        "SITE 3 -- :339-341 generate_placeholder_data builds a hardcoded two-element asset_class_rows list ('Fixed Income', 'Equity'). MEASURED by calling it for real: rows = ['Fixed Income', 'Equity']. This is the path taken when the S3 read of holdings_attribution_data.json FAILS (:160-163 catch -> return generate_placeholder_data), so the degraded view can never show a five-class shape even after a successful retag.",
        "SITE 4, same family, measured on a deliberately skewed run (weights summing to 89, hedge present) -- the renormalisation at :296-301 dumps the entire 11-point gap onto the single largest row: Equity style_weight 48.0 -> 59.0, bet -1.0, while Commodities (12.0) and Real Estate (9.0) keep policy_weight 0.0 and bets of +12.0 and +9.0. With two classes that gap had one sensible home; with five it silently concentrates on whichever row is biggest.",
        "COVERAGE THIS RESTS ON, stated as a denominator rather than asserted: 88 of 88 enumerated hop lines across both consumers were reached by an executed run (A 60/60, B 28/28); 80 of 88 under five-class inputs specifically, and the 8 that are not are named individually -- :220-223 (the per-model except branch) and :307-311 (this row's site 1). Nothing is uncovered and unnamed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell frames the risk as a consumer that 'silently zeroes or mislabels' a retagged value, and asks per hop whether Commodities SURVIVES, RAISES or is SILENTLY DROPPED.",
    "world_is": "The three-verdict frame does not have a slot for what this consumer actually does. Commodities SURVIVES every hop in both siblings -- 0 drop sites, 0 raises, measured. What happens instead is that four two-class-shaped code paths stop applying, and the value carries on looking healthy while the arithmetic around it quietly changes meaning. A hop-level SURVIVES verdict is true and, on its own, would be misleading -- which is why this is a row and not a footnote.",
    "notes": "ARMED against AT3-s-6 for the same reason as W12-S2 and with the same owner, but it is a DISTINCT defect with a DISTINCT remedy: W12-S2 is a missing key in a data table, this is control flow gated on a class COUNT. Fixing one does not move the other, so they must not be collapsed into a single remediation. NOT FIXED HERE: TO-T3-1 is read-only on behaviour. Offered to L9 as an input to the retag's acceptance criteria -- a retag criterion that asserts only 'the class appears in the output' would pass in this world while the tilt logic, the ordering and the fallback view were all silently two-class."
  }
]
```


---

## Rows appended by `0.9.0_WK_POSN_ASTTAX~11` at L7 (TO-T2-1, cell AT3-s-2 -- the frontend hop), 2026-09-11

Three rows from the worker that measured the hop `TO-S7-1` disclosed it could not see. None of them
blocked the cell: AC1-AC4 were all completed. S1 records that the criteria's own named invocation cannot
reach a submodule and that one of the order's two fallbacks fails SILENTLY; S2 records which of the two
portal vintages was read; S3 names the one pocket of portal that remains unmeasured.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W11-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~11",
    "surfaced_at": "2026-09-11T21:57:22Z",
    "one_line": "The invocation T2-AC1/T2-AC3 NAME (comp-find) is structurally incapable of answering its own criterion: portal/ is a GITLINK (mode 160000), comp-find is repo-only, and BOTH fallbacks the task order offered are unusable -- `git show HEAD:portal/<path>` is fatal (no subtree exists) and `git sparse-checkout add portal` yields an EMPTY directory, which a census reads as a SILENT ZERO. The route that works is the submodule's own object store at the pin.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal is a gitlink, not a subtree: `git ls-tree HEAD portal` in /c/tmp/wk-posn-t2 @651ffd4f16 prints `160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a\\tportal`. A gitlink stores a COMMIT ID, not the files, so the superproject tree has no portal/<path> entries at all.",
        "THE ORDER'S FIRST FALLBACK FAILS LOUDLY: `git show HEAD:portal/package.json` -> `fatal: path 'portal/package.json' does not exist in 'HEAD'`. The task order's BOUNDS say 'read blobs via `git show HEAD:<path>`'; for this subject that instruction cannot be carried out.",
        "THE ORDER'S SECOND FALLBACK FAILS SILENTLY, WHICH IS THE HAZARD: `git sparse-checkout add portal` governs superproject tree entries only. A submodule's working tree is populated by `git submodule update`, which is a WRITE under portal/ and is forbidden by this order's own freeze. The result is an EMPTY portal/ directory -- and `ls -la portal` in this worktree already shows exactly that (total 4, only ./ and ../). A census over an empty directory returns 0 hits and reads identically to 'no consumers'.",
        "THE VERBATIM CRITERION INVOCATION REPRODUCES ROUND 2'S BLINDNESS EXACTLY: `timeout 300 comp-find 'assetClass|asset_class' --all --files` printed `DENOMINATOR: 797 hit(s) across 3634 file(s) scanned in scope [corpus=all] | 29802 UNREADABLE, NOT searched` and listed ZERO files under portal/. TO-S7-1 recorded 29,577 UNREADABLE for the same reason; the figure moved to 29,802 and the blindness did not change.",
        "THE ROUTE THAT ACTUALLY WORKS, used for this cell and stated so the next worker need not rediscover it: read the submodule's OWN object store. `git -C <workspace>/portal cat-file blob e85f6eb84f:<path>` and `git -C <workspace>/portal ls-tree -r e85f6eb84f` both succeed, because the portal repo at /c/Users/Opal Bloomberg/Desktop/ajb_workspace/portal carries the pinned commit (`git cat-file -t e85f6eb84f` -> `commit`). This is READ-ONLY and touches neither the submodule pointer nor any file under portal/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-T2-1 BOUNDS: 'portal/ is outside your sparse cone. If you need to read it, widen your OWN worktree's cone (`git sparse-checkout add portal`) or read blobs via `git show HEAD:<path>`', and criteria T2-AC1/T2-AC3 name `comp-find ... --all --files` as the invocation that produces 'the PORTAL subset named explicitly'.",
    "world_is": "portal/ is a submodule (gitlink e85f6eb84f), not a directory of the superproject. comp-find is REPO-ONLY by ruling and cannot cross into it; `git show HEAD:portal/<path>` is fatal because no such subtree exists; and `git sparse-checkout add portal` produces an EMPTY directory rather than the portal files. None of the three named routes can enumerate a portal consumer. The measurement was obtained instead from the submodule's own object store at the pinned commit.",
    "notes": "FILED FOR FORM, NOT SIGNIFICANCE. It blocked nothing -- the cell was completed in full via the object-store route -- and the finding it enabled STRENGTHENS the existing NO-GO, exactly as the order anticipated.\n\nWHY ARMED RATHER THAN INERT: the failure mode of the second fallback is a SILENT FALSE ZERO, and this cell exists precisely because a false zero on this hop already travelled once as if it were a measurement. A future worker handed the same BOUNDS text who runs `git sparse-checkout add portal`, sees rc=0, then censuses portal/ and finds nothing would conclude 'no frontend consumers' with no error anywhere in its transcript. That is indistinguishable from a true absence at every rung short of opening the directory. The disarm is a one-line correction to the cone/BOUNDS recipe -- name the object-store route -- which is the issuer's to make, hence disarm_owner 2.0.0_SA_COO~Z.\n\nNOT CLAIMED: that comp-find should cross submodule boundaries. Repo-only is a deliberate ruling and this row does not ask for it to change; it asks that an order which sends a worker into a submodule name a route that reaches one."
  },
  {
    "id": "POSN_ASTTAX-Z-W11-S2",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~11",
    "surfaced_at": "2026-09-11T21:57:22Z",
    "one_line": "TWO VINTAGES OF portal EXIST AND THE READABLE ONE IS NOT THE PINNED ONE: the superproject gitlink pins e85f6eb84f, while the only populated checkout (the main workspace, branch DEV) sits at 30ca034bba -- 14 commits BEHIND the pin. Measured at the pin; verified byte-identical on the subject files, so this cell's reading is unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE PIN: `git ls-tree HEAD portal` @651ffd4f16 -> `160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a`.",
        "THE READABLE COPY: `git -C <workspace>/portal rev-parse HEAD` -> 30ca034bbaa4b9d2864d3acce826e3c2fa59be0a, `--abbrev-ref HEAD` -> DEV, `status --porcelain` -> 0 lines (clean).",
        "DIRECTION ESTABLISHED, NOT ASSUMED: `merge-base --is-ancestor 30ca034bba e85f6eb84f` -> rc=0, so the working tree is an ANCESTOR of the pin, i.e. BEHIND it. `rev-list --count 30ca034bba..e85f6eb84f` -> 14 commits in the pin that the checkout does not have. The first read ran the ancestry the other way round (rc=1) and would have supported the opposite sentence; both directions were run before the claim was written.",
        "WHY IT DID NOT CONTAMINATE THIS CELL: `git -C <workspace>/portal diff --stat 30ca034bba e85f6eb84f -- src/pages/Positioning src/pages/Attribution src/lib/chartColors.ts` returns EMPTY -- every file this cell's verdict rests on is byte-identical at both vintages. The AC1/AC2/AC3 reads were nevertheless taken at the PIN via the object store, which is the correct grain regardless."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-T2-1 treats 'portal' as a single readable object -- 'the PORTAL subset named explicitly' -- and names no commit at which the portal bytes are to be read.",
    "world_is": "There are two portal vintages on this device and they differ by 14 commits. The copy a reader can browse (the populated working tree) is the STALER of the two; the copy the superproject actually pins is reachable only through the submodule's object store. An unqualified 'I read portal' does not say which was read.",
    "notes": "INERT, and deliberately so rather than by omission: the divergence is a normal submodule condition (a DEV checkout left behind a moved pin), not a defect, and it is disclosed here with the exact remedy -- cite the pin and read at it. It is recorded because this round's whole subject is a hop that travelled unmeasured, and 'measured at an unstated vintage' is the next-door failure. GRAIN NOTE for whoever grades AC1-AC4: every portal line cited in the instance is at e85f6eb84f, and the equality check above means the same lines hold at 30ca034bba as well."
  },
  {
    "id": "POSN_ASTTAX-Z-W11-S3",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~11",
    "surfaced_at": "2026-09-11T21:57:22Z",
    "one_line": "ONE POCKET OF portal REMAINS UNMEASURED AND IS NAMED RATHER THAN ROUNDED AWAY: a NESTED submodule, archive/dashboards/main_dashboard (mode 160000), is 1 of the 1201 tree entries at the pin and cannot be read through by the same argument as S1 -- its objects are not in the portal repo.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`git -C <workspace>/portal ls-tree -r e85f6eb84f` yields 1201 entries, of which 1200 are blobs and exactly 1 is `archive/dashboards/main_dashboard  mode=160000 type=commit` -- printed by the census instrument itself as NON-BLOB, so the denominator discloses it rather than hiding it.",
        "THE CENSUS ARITHMETIC IS CLOSED AND CHECKED: 1113 READ + 87 UNREADABLE = 1200 blobs, asserted by the instrument ('READ + UNREADABLE : 1200 (must equal blobs)'). The 87 are vendored .pyc/.so binaries under etl/orchestration/green/fred/lambda/ -- backend dependency payloads, not frontend source -- each named with its reason (BINARY, NUL byte).",
        "RELEVANCE BOUNDED: the pocket sits under archive/, which the banding pass classifies as retired, and no frontend source file under src/ imports from it (the 42 src/ consumers were each read in full). So the residual risk that a five-class consumer hides there is low -- but it is NOT zero and it is NOT measured, which is the only honest statement available."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "T2-AC1 <expect>: 'a stated count of files READ versus files UNREADABLE. If anything is unreadable, say so and say why -- an unreadable file is not an absent consumer.'",
    "world_is": "Beyond the 87 unreadable BLOBS (all vendored binaries, named), there is a category the READ/UNREADABLE split does not cover at all: a nested GITLINK, which is not a file and so appears in neither count. It is 1 of 1201 tree entries and its contents are unreachable from this device's portal object store.",
    "notes": "Filed so that the AC1 denominator cannot be read as total coverage of portal. The claim this cell supports is 'every FRONTEND SOURCE consumer under src/ was read'; the claim it does NOT support is 'every byte of portal was read'. Naming the gap costs one row and prevents exactly the inheritance this cell was created to stop -- an unmeasured pocket travelling inside a measured-sounding total."
  }
]
```


---

## Row appended by `2.0.0_SA_COO~Z` at L7 (the bar/hazard grain gap), 2026-09-11

One row from the issuer, synthesising two worker findings that neither cell could state alone:
`AT3-s-2` and `AT3-s-3` each measured a collapse OUTSIDE the artifact `AT3-s-5`'s bar reads, so a
GO from the bar would be true and insufficient. Filed rather than fixed -- step (2) is L4's and the
spec is frozen mid-round.

```json
[
  {
    "id": "POSN_ASTTAX-Z-S6",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-11T22:14:46Z",
    "one_line": "THE BAR CANNOT SEE EITHER MEASURED COLLAPSE. Step (2) is read at the SERVED ARTIFACT (positioning_data.json), but AT3-s-2 measured the frontend collapsing to two classes DOWNSTREAM of it, and AT3-s-3 measured a sibling chain misweighting on a DIFFERENT artifact. So AT3-s-5 can return GO while a retagged holding renders nowhere and a sibling zeroes its policy weight -- the retag's own gate is narrower than the hazard.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE BAR'S GRAIN, VERBATIM FROM PRD v0.5 s.4 step (2) @49ddcc481d: 'for EVERY ticker in the retag set, the SERVED asset_class value equals its ratified five-class label AND its allocation weight is NON-ZERO and equal to its pre-retag weight, READ FROM THE SERVED ARTIFACT.' The served artifact is positioning_data.json, written by yang-generate-positioning. That is the whole of what TO-T5-1 is instructed to read.",
        "COLLAPSE SITE 1, DOWNSTREAM OF THAT ARTIFACT (AT3-s-2 / W11-S1, worker 0.9.0_WK_POSN_ASTTAX~11): portal/src/pages/Positioning/tabs/HoldingsTab.tsx:1392-1394 iterates a HARDCODED two-value list -- `const assetClassOrder = ['Fixed Income', 'Equity']` then `.filter(ac => groupedHoldings[ac])`. A group keyed Commodities/Structured/Alternatives is NEVER ITERATED: the row renders NOWHERE while its weight stays in the grand total. The worker measured 42 of 42 consumers and returned the verdict COLLAPSES, 12 sites across 8 files.",
        "AND THAT EXACT BUG HAS ALREADY SHIPPED ONCE, which is why this is not hypothetical: the same file documents it at :1364-1372 for the value `Cash`, measured on PROD v2.1.167 -- PFDE 90 -> 89 served-vs-DOM rows, subtotals summing 99.98 under a grand total of 100.01. The remedy folded only Cash and Hedge. A retag reproduces the identical failure with a new value.",
        "COLLAPSE SITE 2, ON A DIFFERENT ARTIFACT ENTIRELY (AT3-s-3 / W12-S2, W12-S3, worker 0.9.0_WK_POSN_ASTTAX~12): yang-generate-allocation-summary survives Commodities through all its hops and then draws policy_weight 0.0 from a fixed two-key BENCHMARK_ALLOCATIONS, rendering `bet` equal to the row's entire weight (measured: style_weight=10.0 policy_weight=0.0 bet=10.0). Four two-class-shaped sites change behaviour silently at five classes. That chain writes holdings_attribution_data.json -- NOT positioning_data.json -- so the bar's artifact does not contain it.",
        "THE ASYMMETRY THE WORKER NAMED, and it is the mechanism: 'Data reaches three lambdas; the code hardening reaches one.' AT3-s-1's write surface is a single code path (yang-generate-positioning/lambda_function.py). The RETAG's data reaches the siblings through a second door -- consumer B imports ETFClassifier directly (:33/:39/:582) and all three checked-in copies of etf_classifications_dynamodb.py are byte-identical (md5 e62906eff240a853029181715fc9b451). Hardening one producer does not protect the other two consumers of the same registry.",
        "SO THE DISCRIMINATOR FAILS IN THE DIRECTION THAT MATTERS: a bar read strictly at positioning_data.json can return GO while (a) the page drops the row entirely and (b) a sibling chain misweights it. The bar is not wrong about what it measures; it is measuring a strictly smaller surface than the hazard occupies. NEGATIVE CONTROL, stated: if both collapse sites were INSIDE positioning_data.json, the bar would catch them -- the gap is the artifact boundary, not the bar's logic."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.5 s.4 step (2), as re-founded @49ddcc481d, states the retag's gate as a CONDITION read FROM THE SERVED ARTIFACT, and the round-3 decomposition makes AT3-s-5 that gate: AT3-s-6 fires on its GO.",
    "world_is": "Two collapse sites were measured this round and NEITHER is inside the served artifact the bar reads. The frontend one is downstream of it (portal HoldingsTab, a hardcoded two-value order list, with the identical bug already shipped for Cash on PROD v2.1.167). The sibling one is on a different artifact entirely (holdings_attribution_data.json). A GO from AT3-s-5 would therefore be TRUE about positioning_data.json and INSUFFICIENT for the retag.",
    "notes": "WHY THIS IS A ROW AND NOT AN EDIT: the spec and the decomposition are FROZEN mid-round (Rule 27), and step (2) is L4's -- `1.0.0_SA_CTO~Z` owns it. I am not widening a bar I do not own, and I am not re-cutting AT3-s-5's criteria after issuance. Pitched to the CTO as a spec/scope call per /drive obligation 7, citing this row.\nWHAT I WILL DO WITH IT REGARDLESS, so nothing waits on the pitch: as the seat that spawns AT3-s-6, I will NOT spawn it on a bare GO from AT3-s-5 while this row is ARMED. The decomposition already requires AT3-s-2 and AT3-s-3 terminal before the retag -- both now are, and both returned findings that say the retag is unsafe downstream of the generator. Their being terminal is a precondition, never a clearance.\nMY RECOMMENDATION, offered and not taken: widen step (2)'s bar at L4 to name the RENDERED surface and the sibling chain, or state explicitly that the retag is deferred until those two surfaces carry five classes. Either is honest; a GO measured only at positioning_data.json is not.\n\u26a0 LIMIT ON MY OWN CLAIM: AT3-s-2 disclosed that what it measured is SOURCE AT A PIN, never EXERCISED -- no build, no render, no diff against the deployed bundle. Its PROD corroboration is for `Cash`, not for `Commodities`. So the frontend collapse is strongly evidenced and NOT observed in a DOM, and this row does not upgrade it."
  }
]
```
