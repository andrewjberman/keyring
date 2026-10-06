# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM H: the characteristics reader runs single-threaded

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "H",
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
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6G.md",
 "cell_ids": ["YCD-o-6"]
}
```

**Why an addendum.** The CTO ruled (msg 105485, point 3) that pyarrow joins branch B2 so the 81 characteristics-fed held groups do not print a false `INPUT_MISSING`. Staging the pinned pyarrow (18.1.0, from AWS's own
`AWSSDKPandas-Python312:16` layer; tar sha256 `dad8a09e0887...`) and proving it on the host in `/tmp` found that it imports and reads the real `bbg/2026-10-02/characteristics.parquet` (114 rows, 14 columns), **but a read from a
`BytesIO` with the default thread pool aborts the interpreter at exit on this host (exit 134, "terminate called without an active exception")**; the same read with `use_threads=False` exits 0, and a read from a path exits 0
(cases A to I, `act/host_pyarrow_exit_probe.sh`). The producer's reader is the BytesIO form (`layout_overview._read_characteristics`, line 842). A resident service stops on every install and rollback, and an abort at exit leaves a
failed unit and a core dump. The fix is one argument; it is a code change in a file whose last writer (h-6) is complete.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-o-6` | 4 Classify, 6 Compute (held data) | `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`, `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py` | pyarrow | none open |

**Writer read.** A scan of 4,248 task-order files (both roots) for a non-terminal order naming either file found 0 hits.

**Contract R16.** `layout_overview._read_characteristics` reads the characteristics parquet with `use_threads=False`: `pq.read_table(io.BytesIO(body), columns=[...], use_threads=False)`. Every row it returns, for the same bytes, is unchanged. No other line of the module changes.

## Edges and fan-out

M = 1, no dependency. fanout: 1 of 1 chain, cap 8, reason: one-argument fix. Branch B2 is built after n-6 and o-6 have merged: the base pin `3d705e700f`, the named list (the 11 files of branch B, with `layout_overview.py` at its new content and
`resident_worker.py` at the ephemeral pin), one `--member` for the classifier client, and the pinned pyarrow tar staged by the wrapper.

## Four-postulate record (Rule 24)

MECE: the pyarrow adoption has three parts, each with one owner: the classifier client (n-6), the reader argument (this cell), the host dependency and its environment line (the issuer's wrapper). Same grain: one call site. Intent: one outcome
(a clean exit after a characteristics read). State: row values do not change; the default-threaded path is not left behind.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (a one-argument code change, no deploy, no grant).
