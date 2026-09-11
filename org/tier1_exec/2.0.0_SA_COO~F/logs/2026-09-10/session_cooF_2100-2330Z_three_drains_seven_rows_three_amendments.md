# IRPT_FNTEND round 1: three orders drained, seven worker rows, three issuer amendments -- 2.0.0_SA_COO~F

**Date:** 2026-09-10
**Task Order:** IRPT_FNTEND L7 drains (FE-s-1, FE-s-2, FE-s-4); L7 in flight (FE-s-3, FE-s-8)
**Status:** IN PROGRESS
**archetype:** COORDINATE
**Workspace CLOUD commits (LOCAL):** `522ec57a5d` `c6b906913c` `9a6886c23a` `f2b8524311` `8da0055a94` `531ff06aab`
**Portal DEV commits (LOCAL):** `6b614a5a` `be041051` `1668ed5b` `b86e6aa2`

---

## Objective

Drain the first three terminal orders through the refuser in both repos, re-verify each with this seat's own instrument run, act as disarm owner on every ARMED row, and keep the queues moving without a second issuance.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | re-run by this seat on each of the three instances | PASS | VALID rc=0 each; surprises 2, 2 and 5 entries all resolving to channel rows |
| bun test / typecheck | re-run by this seat in each worker's portal worktree on two or three criteria per order | PASS | 12/12, 52/52, 19/19; typecheck rc 0 each -- an instrument different from the worker's report |
| safe-merge | workspace branches x3 | PASS | row gate on the merged index each time; the FE-s-4 drain conflicted on the append-only channel (expected) and continued after a union resolution: 10 rows |
| safe-merge | portal branches x3 | PARTIAL | first run refused rc=2 because GATE resolved under the target repo's root; fixed @c6b906913c (resolve beside the script); the FE-s-4 portal merge conflicted on one App.tsx import hunk |
| bun test | full Investor Reporting set on DEV @b86e6aa2 | FAIL (1) | `__tests__/fe-s-2/app-diff.test.ts` reads `.scratch/app.diff`, which exists only in the worker's own worktree -- a criterion artifact failing the DEV set; fixed by FE-s-3's amendment (skip when absent) |
| netstat / taskkill | listeners on 5181, 5182 | WARN | no listeners by the time the drain ran; the workers had ended their servers |

**What worked:** re-running the estate's checker and two criteria per order from the worker's own worktree; the merged-index row gate; the union resolution of the channel conflict by parsing both sides' arrays.
**What failed:** a resolution script raised on an over-broad assertion (a line of `=` elsewhere in `App.tsx`) BEFORE writing, and the following `git add` was on a new line rather than chained, so the portal merge `1668ed5b` committed the file with markers; typecheck's rc read 0 through a pipe. Repaired at `b86e6aa2`; the true rc is read from a redirect, never after a pipe.
**Gap found:** `git worktree remove --force` leaves the node_modules junction and, this time, the two `portal/` directories held open by some process; the junctions were unlinked with `rmdir` and the empty directories are pending removal.

---

## Work Completed

### 1. FE-s-1 drained -- ws `522ec57a5d`, portal `6b614a5a`
6 of 6 PASS. Rows W1-S1 (ARMED, `interface Dirent` in a type shim would merge against `@types/node`) and W1-S2 (INERT). Disarm act granted to FE-s-2 (`F2-AC8`, `F2-AC9`); seat row S1.

### 2. FE-s-2 drained -- ws `f2b8524311`, portal `be041051`
8 of 8 mechanical PASS, 1 judgment recorded. W1-S1 disarmed in code (`DIRENT_NAME=False`, 46/46 fe-s-1 tests). Rows W1-S3 (INERT: the face named the wrong export path for `PageThemeProvider`) and W1-S4 (ARMED: `PageSurfaceControl as="dropdown"` computes white on the silver canvas; the control is do-not-edit). Header actions clip at 390 (recorded under the judgment criterion).

### 3. FE-s-4 drained -- ws `8da0055a94`, portal `1668ed5b` + repair `b86e6aa2`
8 of 8 mechanical PASS, 1 judgment recorded. Rows W2-S1 (INERT: brand sources are gitignored, copied from the primary checkout), W2-S2 (ARMED: `ExportBundle` carries references, not payloads; the package's `RenderBundle` is additive; a contract-conformant backend bundle would be refused), W2-S3 (ARMED: no Lato binary on the estate; fetching is egress), W2-S4 (ARMED: recharts renders an empty wrapper under static markup), W2-S5 (INERT: ui-smoke prints `DID NOT LAND` for any route with a query string while rc=0).

### 4. Issuer amendments at `531ff06aab`, seat rows S2..S5
FE-s-3: Model Portfolios className on the dropdown, header controls re-flowed below the title, the drained diff test skips when its artifact is absent (`F3-AC7`..`F3-AC10`). FE-s-8: `runtime: 'browser'` declared in the manifest (`F8-AC9`). FE-s-9: `export/resolveBundle.ts` turns the reference-only bundle into the `RenderBundle` through the query cache and the typed client; PrintEntry routed through it (`F9-AC9`). W2-S3 is a pending input (a font file only Andrew's word can bring on) carried to L10 as an open call.

### 5. Spawned
FE-s-3 (slot ~1, `/c/tmp/wk-irpt_fntend-1-3-fe-s-3`, port 5181) and FE-s-8 (slot ~2, `/c/tmp/wk-irpt_fntend-2-2-fe-s-8`, port 5182), both from ws `531ff06aab` and portal `b86e6aa2`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Disarm acts travel as issuer amendments to the next non-terminal order in the same slot | mid-round the decomposition is frozen; an amendment to a non-terminal order is the sanctioned shape and the coverage limb counts nothing twice |
| The channel conflict is resolved as the ordered union, existing rows byte-identical | append-only binds both sides; the row gate re-grades only the new rows on `--continue` |
| The App.tsx marker defect is repaired by a follow-up commit, not a rewrite of the merge | DEV is a shared branch; never rebase |
| W2-S3 (Lato) is carried, not disarmed | the disarm is an egress act reserved to Andrew's word |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tools/safe-merge.sh` | GATE resolves beside the script | Yes -- `c6b906913c` |
| `org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-2.*.md` | amendment: shim fix, F2-AC8/9 | Yes -- `9a6886c23a` |
| `.../task-orders/IRPT_FNTEND.TO-FE-s-3.*.md`, `TO-FE-s-8.*.md`, `TO-FE-s-9.*.md` | amendments per rows W1-S4, W2-S4, W2-S2 | Yes -- `531ff06aab` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | 14 rows (9 worker, 5 seat) | Yes -- through `531ff06aab` |
| `portal/src/App.tsx` (portal repo) | marker repair | Yes -- `b86e6aa2` |

---

## Blockers

None at this seat. FE-s-3 and FE-s-8 are executing; FE-s-5, FE-s-6, FE-s-7 seat when FE-s-3 (and FE-s-4, already terminal) land.

---

## Current State

IRPT_FNTEND reads `dep_stage EXECUTING`; 3 of 11 orders terminal; 14 channel rows, of which four are ARMED (W1-S4, W2-S2, W2-S3, W2-S4) with their disarm acts granted to FE-s-3, FE-s-9, FE-s-8 and, for W2-S3, carried to L10. Portal DEV carries the contracts, typed client, fixtures, route, page shell, header and the render package; typecheck rc 0; the one failing DEV test is the criterion artifact FE-s-3 makes skip. All commits LOCAL in both repos; the workspace `portal` gitlink still points at `5907cbca`.

---

## Next Steps

1. **Drain FE-s-3 and FE-s-8** as their reports arrive; then seat FE-s-5 (slot ~1), FE-s-6 (slot ~3), FE-s-7 (slot ~4) in fresh pairs -- wave D, width 3.
2. **Then FE-s-9, FE-s-10, FE-s-11** in slot ~1's queue.
3. **L10** -- ONE message to `1.0.0_SA_CTO`: the CVO watermark against the row count, W2-S3 as an open call (Lato), W2-S2 as a contract question for the counterpart's B15, W2-S4 for its worker cell, W2-S5 for the ui-smoke owner, and the gitlink pointer.
