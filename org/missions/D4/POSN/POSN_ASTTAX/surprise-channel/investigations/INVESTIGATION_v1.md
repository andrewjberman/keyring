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
