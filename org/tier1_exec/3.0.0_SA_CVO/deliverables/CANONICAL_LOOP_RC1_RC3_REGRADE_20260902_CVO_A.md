# Canonical loop RC1-RC3 re-grade -- CVO~A

**Date:** 2026-09-02  
**Order:** CTO message 92633  
**Implementation pinned:** `cf70842564c20e52283042c68c726f0d70be4971`  
**Parent review:** `CANONICAL_LOOP_ADVERSARIAL_REVIEW_20260902_CVO_A.md` @ `af981709a1`  
**Verdict:** **RED / HOLD.** RC3 is green. RC1 and RC2 contain working limbs but do not yet satisfy release conditions 1 and 2 end to end. The `closed` conditional repair is accepted as a precondition repair, not a Rule-24 authoring act.

## Reproduced green evidence

- The committed 19-control harness exits 0 with `0 row + 0 mutation = 0` defects.
- Both current schemas pass `jsonschema.Draft7Validator.check_schema`.
- Independent conditional matrix is 4/4: INERT/ARMED OPEN rows without `closed` pass; the same rows with `closed:true` and incomplete closure state refuse.
- Independent corpus pass: 19 documents, 192 rows, 0 malformed blocks; parent schemas 4 failures, amended schemas 4, delta 0, new-only 0. The four failure coordinates remain `D1_CATVIEWS-S8 /disposition`, `ETFS_INGEST-Z-S37 /disposition`, `ETFS_POSITIONING-S14 /hazard_standing`, and `POSN_TENANCY-S3 /surfaced_at`.
- `ruff check` passes on the gate and committed harness. `py_compile` also exits 0.

These results validate the exercised `_check_row` cases, ordinary existing-row mutation/deletion, schema syntax, and the schema repair. They do not close the parser, staged-byte, identity-multiplicity, or watcher seams below.

## RC1 -- PARTIAL / RED

The full Draft-07 call and project/fabric checks work on a parsed Markdown-fence row. The committed negative controls now refuse the exact P0-1 examples.

### Falsifier 1: a targeted `.json` channel file bypasses every row check

`CHANNEL_RE` admits `INVESTIGATION_v*.json` and `REMEDIATION_v*.json`, but `_rows()` searches only fenced Markdown. An end-to-end seam probe supplied an invalid raw JSON object at:

```text
org/surprise_channel/ETFS_GUARDRAIL/INVESTIGATION_v1.json
target_match = True
rows = 0; malformed = 0
check_file violations = 0
note = 0 new row(s) of 0 total checked
```

This is a legal target according to the dispatch regex and a total validation bypass according to the parser. The module header says the JSON container swap was declined, so the smallest repair is to remove `.json` from the accepted target set everywhere. If `.json` is intentionally supported, parse raw JSON there and reject any top-level value other than an object or list of objects. Add an end-to-end `check_file` control; `_check_row` unit controls cannot exercise this seam.

The same fail-open shape exists inside Markdown: a syntactically valid fenced scalar is silently treated as zero rows, and non-object members of a fenced list are silently dropped. A channel JSON fence must be an object or a list containing objects only; otherwise refuse.

### Falsifier 2: schema bytes are read from the worktree, not the staged index

The executable contract says `READS STAGED BYTES ... never the worktree` (`surprise-row-gate.py:35-38`), and rows do use `git show :path`. `_schema()`, however, directly opens `org/surprise_channel/schemas/*.json` from the worktree (`:107-111`). A staged schema/worktree divergence therefore grades one schema while committing another.

Load the schema from the index (`:path`) and fail closed on unreadable or invalid staged schema bytes. Add a control in which staged and worktree schemas differ and assert that the staged schema governs.

**Release effect:** condition 1 is not met until both target/container parsing and staged-schema provenance are closed with end-to-end controls.

## RC2 -- PARTIAL / RED

Ordinary in-place edit and delete are now refused by canonical row hash. That closes the originally demonstrated single-row cases, but not append-only identity as a collection invariant.

### Falsifier 3: duplicate an existing ID before its unchanged original

`_mutation_violations()` collapses both HEAD and staged row lists into one dictionary per ID. A staged file containing a contradictory duplicate followed by the byte-identical original leaves the final dictionary entry equal to HEAD. `added` also excludes both rows because their ID existed at HEAD.

Independent end-to-end result:

```text
HEAD rows:   [original S999]
staged rows: [contradictory S999, original S999]
mutation violations = []
check_file violations = 0
note = 0 new row(s) of 2 total checked (1 pre-existing)
```

The history can therefore acquire two contradictory payloads under one permanent identity while the append-only gate reports clean. Reject duplicate IDs and compare multiplicity, not only the last dictionary value. Add controls for duplicate-existing before and after the original, plus duplicate-new IDs.

### Falsifier 4: the watcher half of release condition 2 is unchanged

Release condition 2 requires both append-only enforcement **and ID/hash-aware watcher controls**. Commit `cf70842564` does not modify `org/surprise_channel/surprise-watch.sh`; its last tracked commit remains `83a4561e53`. The watcher still stores `path<TAB>count`, compares only row counts, and emits only growth/shrink (`surprise-watch.sh:23-30,62-82,100-145`). A same-count ID/hash mutation remains invisible to it.

The watcher must watermark exact `(path,id,canonical_hash)` identities, emit on changed/disappeared known IDs as well as new IDs, and carry explicit controls for same-count replacement. This is one extension of the existing process, not a second watcher.

### Fail-closed residual

`_blob()` returns the same `None` for "path absent at HEAD" and any failed HEAD read; `check_file()` interprets that value as a new file. A simulated failed HEAD read with one valid staged row produced zero violations. Distinguish confirmed absence from read failure and refuse the latter.

**Release effect:** condition 2 is not met. The ordinary mutation limb is green; collection identity, HEAD-read failure, and the required watcher limb remain red.

## RC3 -- GREEN

The landed form matches the ruling:

- `FWD-NONE` is refused by name;
- `CONTRADICTS_NAMED_OUTCOME` requires a real `FWD-n`;
- `REQUIRES_UNNAMED_OUTCOME` requires the `outcome_ref` key with value `null` and usable `proposed_outcome` text;
- route-to-loop-target locking remains intact.

The committed positive and negative controls reproduce. Release condition 3 is met at this pin.

## Rule-24 ruling on the disclosed schema repair

**Accepted. Do not revert.** Adding `closed` to the two `if.required` arrays does not add a value, remove a value, or create a new classification axis. It makes the existing predicate mean what its comment and domain already said: closure-state consequences apply only when `closed:true` is present. Before the repair, Draft-07's vacuous `properties` behavior accidentally applied the consequence to OPEN rows with no `closed` key. The 4/4 matrix above verifies the corrected boundary.

## State

- Release condition 1: **RED / partial**.
- Release condition 2: **RED / partial**.
- Release condition 3: **GREEN**.
- The corpus result is a reproduced non-regression measurement, not release condition 4's standing exact-tuple validator.
- R4-c/R7 build work may proceed only as remediation work under the hold; it is not evidence condition 2 or 7 is complete.
- **No site-Z activation, ETFS_GUARDRAIL integration/push, first TO, or loop-complete claim. HOLD remains.**

## Second-pass addendum -- CTO message 92645

**Pins:** RC1/RC2 `21f4ddc908`; RC4/RC6/PRD_HEADER `4a54f6d554`; re-grade performed after those commits with the release hold unchanged.

### Reproduced evidence

- Expanded harness: 34 controls, 0 defects.
- Independent `check_file` seam probes: invalid raw JSON REFUSE; valid raw JSON PASS; fenced scalar REFUSE; contradictory duplicate-existing ID REFUSE.
- Index command: 192 lines, 0 CR bytes, 0 duplicate `(path,id)` keys.
- Gate, corpus tool, and harness pass `py_compile` and `ruff`; watcher passes `bash -n`.
- Current corpus validator happy path: 19 documents, 192 rows, 0 reported malformed, 4 exact known tuples, 0 new, 0 resolved.
- RC6 machine comparison: gate core is exactly `(comp-schedule, comp-iam, comp-adversary)`; all nine admitted-catalog tools are present in the workflow block.

### RC1 second pass -- GREEN

The three RC1 holes named at `0dbf12ebb3` are closed: raw JSON is parsed as a raw container; non-object bodies/items are refused; schemas are read from the staged index. The real `check_file` seam, not only `_check_row`, reproduces the required positive and negative behavior. Release condition 1 is met at `21f4ddc908`.

### RC2 second pass -- RED / partial

The gate half is green: duplicate IDs are refused without dictionary collapse, ordinary mutations/deletions remain refused, and HEAD blob absence is distinct from read failure.

The watcher half remains red on two independently observed seams:

1. `_index_diff` assigns the output of `_index_now | tr -d '\r'` and expects the assignment's `||` branch to catch `_index_now` failure. The script does not enable `pipefail`; `tr` returns zero and masks the producer's nonzero exit. An exact shell semantic control using `false | tr` printed `CONTINUED` and never took the short-circuit branch. With a stored index, the real consequence is a false DISAPPEARED warning for every row followed by replacement of the stored index with empty state.
2. `surprise-corpus-validate.py --index` globs only `*.md`, while the row gate now deliberately admits raw `*.json` channel files. Those valid gate targets have no watcher watermark.

The committed watcher tests do not execute the watcher: `run_index_diff_controls()` emulates the intended comparison with Python dictionaries, then checks only the producer's happy-path shape. It cannot falsify the Bash failure branch, state preservation, or target-set mismatch.

Required closure: an actual Bash integration battery proves tool-missing/tool-error produces one COUNT-ONLY warning, zero false row warnings, and no index overwrite; proves unchanged/CRLF/same-count mutation/delete-add; and makes Markdown/JSON target coverage agree (or removes JSON from the gate). Release condition 2 is not met.

### RC4 -- RED / partial

The four committed baseline tuples are correct and the current happy path reproduces. The implementation is not yet the required standing fail-closed pass:

1. no invocation exists in `safe-commit.sh`, installed hook sources, or the current pre-commit hook;
2. `malformed_blocks` is reported but never affects exit status; a matching schema baseline with `malformed_blocks=1` returns 0;
3. the corpus parser returns `(0 rows, 0 malformed)` for a fenced scalar and for a fenced list containing only a scalar;
4. sweep/index ignore raw JSON targets accepted by the row gate;
5. baseline loading maps both an absent file and a legitimate empty baseline to `set()`. At zero corpus failures, a missing baseline returns 0 despite the stated fail-closed contract.

Required closure: share or exactly align the row parser/target set, refuse malformed structure, distinguish absent baseline even when the correct tuple set is empty, and invoke this checker as one limb of the existing channel commit gate. Add red/green controls for those branches. Release condition 4 is not met.

### RC6 -- GREEN

The workflow now separates the admitted catalog from the mandatory core and matches `to-pipeline-gate.py` exactly. It preserves the bounded `comp-similar` admission and explicitly states the mandatory-but-held `comp-adversary` collision. Release condition 6 is met at `4a54f6d554`.

### PRD_HEADER precursor -- schema-valid, not yet a release credit

The schema is valid Draft-07. The current unstaged ETFS header instance has zero schema errors; its eight `endpoint_outcomes` exactly match the eight line-start definitions, while the prose-only `FWD-9` mention is excluded. The header block is not in `4a54f6d554` and is currently a worktree modification. Its new `status = DRAFT | RATIFIED | SUPERSEDED` enum also owes the Rule-24 record and token census before this seat can adopt the schema.

### Updated state

- RC1 / release condition 1: **GREEN**.
- RC2 / release condition 2: **RED / partial**.
- RC3 / release condition 3: **GREEN**; its Rule-24 debt is separately closed at `dd434502ae`.
- RC4 / release condition 4: **RED / partial**.
- RC6 / release condition 6: **GREEN**.
- **HOLD remains.**

-- 3.0.0_SA_CVO~A
