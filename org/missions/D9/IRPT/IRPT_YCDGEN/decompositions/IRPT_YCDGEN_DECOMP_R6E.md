# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM E: the resident package carries the producer, the map, and a named file list

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "E",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.6; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.6",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md",
 "ruling": "msg 105454 (1.0.0_SA_CTO, 2026-10-06 01:14Z): cut the packaging cell now as a round-6 addendum cell, three conditions",
 "cell_ids": ["YCD-m-6"]
}
```

**Why an addendum.** Branch A of the Opal producer's release is installed (ledger `irpt-ycdgen-r6-branch-a-20261006`, CLOSED). Building it measured two gaps that stop branch B:

1. **`ycharts/research` is not a packaged directory** (`build_resident_package.py` `PACKAGE_DIRS`), and `resident_worker.load_opal_producer()` imports `opal_producer` from `<root>/ycharts/research`; the
   Overview element map has no installed home either (`resident_installed._opal_map_loader` needs a pinned `opal_map` binding that no bindings file carries; worker row IRPT_YCDGEN-W1-S13).
2. **The builder ships the whole tree at its pin**, so other seats' unreleased merges ride every resident build (row IRPT_BCKEND-S339, ARMED, disarm owner this seat). Branch A was built from an ephemeral pin
   instead. CTO condition 1 of msg 105454: the package is built from a named file list; its list and count are printed in the packet.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-m-6` | release tooling | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py` (new) | the merged round-6 code, the running package's tar | none open |

**Writer read.** A scan of 4,245 task-order files (both roots) for a non-terminal order whose `<paths>` names either tool file or a `tests/` directory under `IRPT_MVP_P` found 0 hits; this order is their only writer.
Both tools are COO deliverables, used by `2.0.0_SA_COO~P` and this seat for every resident build; the change is additive (new flags, defaults unchanged) so a build with no new flag is byte-for-byte the build of today.

**Contract R13.** (1) `--research`: the builder also packages every tracked non-test file under `infra/aws/lambda/investor-reporting/ycharts/research/` at the pin (`.py`, `.json`, `.sh`, `.md` and `.cjs`;
no `tests/`, `fixtures/`, `__pycache__`) as `ycharts/research/<name>`. (2) `--opal-map REPO_PATH`: that tracked file at the pin is packaged as `ycharts/research/overview_map.json` and the bindings gain
`"opal_map": {"path": "../ycharts/research/overview_map.json", "sha256": <digest>}` (relative to `reports/`, like `census`); without the flag the bindings carry no `opal_map` key. (3) Named file list:
`--base-pin P --files-from LIST` builds the package from P's tree by the same member rule as today, EXCEPT the files named in LIST (one repo path per line; each must exist at `--pin`), which come from `--pin`;
the report prints the list and its count, and the bindings provenance records `base_pin`, the list's sha256 and its count; no unlisted member differs from P. (4) `--state-json FILE` reads the core state document
from a file in place of the S3 read, so tests run offline; the default is unchanged. (5) The gate takes `--base-pin P --files-from LIST` and then compares each listed member to `git show <pin>:<path>` and every
other member to `git show P:<path>`; a member that differs from its expected blob fails G2 with the count printed. (6) A package built with (1) and (2) imports `opal_producer`, `layout_overview`, `runner`, `keeper`
and `held_data` through `resident_worker.load_opal_producer()` in a clean interpreter with the host's import path, and `resident_installed._opal_map_loader` returns the map as a dict.

**Not proved by this cell, and stated so.** The renderer: `layout_overview.render` shells out to `render_pdf.cjs` and a headless browser, and nothing here shows the resident host has them for the producer's use (it has
the YCharts capture library's browser). That is branch B's first real exercise and a condition of branch B's packet.

## Edges and fan-out

M = 1, no dependency. fanout: 1 of 1 chain, cap 8, reason: one tooling cell, additive.

## Four-postulate record (Rule 24)

MECE: the packaging gap has two members (the producer directory with the map; the whole-tree shipping), each answered by one numbered part of R13; nothing else under the builder changes. Same grain: one tool pair.
Intent: one outcome (a resident package can carry exactly a named change set including the producer). State: a build with no new flag is unchanged; no package is installed by this cell.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (thread round, no grant change, no deploy).
