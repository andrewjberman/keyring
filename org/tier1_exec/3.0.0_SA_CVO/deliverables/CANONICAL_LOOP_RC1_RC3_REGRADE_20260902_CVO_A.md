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

-- 3.0.0_SA_CVO~A
