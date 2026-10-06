# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM G: the resident package carries the classification client

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "G",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.8; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.8",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6E.md",
 "cell_ids": ["YCD-n-6"]
}
```

**Why an addendum.** Branch B is installed (ledger `irpt-ycdgen-r6-branch-b-20261006`, V1 closed) and a read-only proof of the producer's real client stack on the host found a blocker no fake-backed test could:
the Opal producer reads classifications through `ETFClassifier` (`layout_overview._default_classifier`), which imports `etf_classifications_dynamodb` and otherwise looks for
`<root>/../v2_portal/_shared`. The resident package carries neither: the file is in `infra/aws/lambda/v2_portal/_shared/`, in no packaged directory. A listed principal's request raises `LayoutRefused` before any output and
ends as an ATTENTION (row IRPT_YCDGEN-S10, ARMED, disarm owner this seat). The research directory is on `sys.path` when `load_opal_producer()` runs, so the first-try import finds the module if the package carries it at
`ycharts/research/etf_classifications_dynamodb.py`; the builder has no way to place one repository file at a different packaged path (m-6 added `--research`, `--opal-map`, `--base-pin`/`--files-from`, `--state-json`).

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-n-6` | release tooling | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py` (new) | m-6's merged tool and tests | none open |

**Writer read.** A scan of 4,247 task-order files (both roots) for a non-terminal order naming the builder, the gate or a `tests/` directory under `IRPT_MVP_P` found 0 hits; m-6 (their last writer) is complete and merged.

**Contract R15 (one repository file at a packaged path).** (1) `--member PACKAGED_PATH=REPO_PATH`, repeatable: the builder packages the tracked file `REPO_PATH` at `--pin` as the member `PACKAGED_PATH`. It refuses (nonzero, a named message) a `PACKAGED_PATH` that
is absolute, contains `..`, or is already a member of the package, and a `REPO_PATH` that does not exist at `--pin`. Under `--base-pin` the member is read from `--pin` and needs no entry in the `--files-from` list; it is recorded, not listed.
(2) The bindings provenance records `members_added`: a list of `{"packaged": ..., "repo_path": ..., "sha256": ...}` (empty list absent when no `--member` is given: a build with no new flag is byte-for-byte the build of today), and the builder's printed report lists them.
(3) `resident_package_gate.py` reads `members_added` from the package's own `reports/resident_bindings.json`; G2 expects each added member equal to `git show <pin>:<repo_path>`, and a member that differs fails G2 with the count printed; the census counts each as added.
(4) A package built with `--member ycharts/research/etf_classifications_dynamodb.py=infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` lets `layout_overview._default_classifier()` return an `ETFClassifier` in a clean interpreter whose only import path
entries are the host's (the package root and the directories `resident_main.py` and `resident_installed.py` put on `sys.path`, with `ycharts/research` appended as `load_opal_producer()` appends it), with no `v2_portal` directory anywhere on it, and with `AWS_DEFAULT_REGION` set so no network call is made.

## Edges and fan-out

M = 1, no dependency. fanout: 1 of 1 chain, cap 8, reason: one additive tooling cell. After it merges the issuer builds branch B2 from the same base pin, the same named list and this one member, gates it, and asks the CTO for a small second half
(one additional public-code member; no permission widens).

## Four-postulate record (Rule 24)

MECE: the packaging gap has one member (a repository file with no packaged path of its choosing); R15 (1) to (4) answer it and nothing else under the builder changes. Same grain: one tool pair. Intent: one outcome (a resident package can carry a named repository file at a named path).
State: a build with no `--member` is unchanged; no package is installed by this cell. pyarrow (row S11) is NOT in this cell: a binary wheel is not a git member and a host dependency is its own act.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (tooling, no deploy, no grant).
