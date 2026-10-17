# IRPT_ANLREQ round 55, workstream ~G (ENGINE) -- decomposition: the resident's entry module puts lib on sys.path (for r34k)

Issuer `2.0.0_SA_COO~G2`, 2026-10-17.

**Input:** IB2 rolled r34j back at 02:08Z: V1 green, V2S FAIL, SPY `CHECK_FAILED EXCEPTION` with 0 rows on the checker's first ask, ZQXWVK `NOT_KEPT NO_ROWS`, the V2 script's own second ask (`default_history`, which never imports the calendar) clean. The cause is deterministic and the issuer's: AR-g-157's checker does `import trading_calendar` inside `_check_one`, and `lib` is not on the service's `sys.path`: `ycharts/generate/resident_main.py:20-23` adds `intake, ops, reports, _keys, _authz, _gate, ycharts/session, ycharts/extract` and no `lib`, so every symbol reads CHECK_FAILED. Reproduced with no Yahoo: `python -I` over the shipped r34j tree, a fake history, SPY gives CHECK_FAILED EXCEPTION; `import trading_calendar` there gives ModuleNotFoundError; and the V2 offline test run on the merged checker fails the same case. The issuer ran that test BEFORE AR-g-157 merged (the old checker was in the repository) and not after: the lesson is in the drive log. CTO msgs 10166 and 10172: r34k puts `lib` on the path ONCE where the others are added (`resident_main.py`), adds a package-layout smoke under `python -I` over the BUILT tree importing every member the static walk marks LIVE, runs the V2 offline test on the merged tree at the pin and records the order, and has V2 print the exception class on a first failure; no retry-once; the 10 fresh-process Yahoo test for the record (done: 10 of 10 clean, 22 rows, last 2026-10-16 763.25, 1.0 to 1.6 s).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **One worker cell, the line.** `AR-g-159`: `lib` joins the tuple in `resident_main.py` (`for _relative in (...)`), and `test_resident_main.py` gains the two tests that would have caught r34j: the tuple holds `lib`, and a package-layout run under `python -I` (the checker, the calendar and `resident_main.py` copied into a temporary tree; `sys.path` set from the tuple exactly as `resident_main` sets it) reads SPY KEPT on a Saturday; the same run with `lib` taken out reads CHECK_FAILED.
- **The rest is the issuer's release tooling, not a worker cell:** the whole-package import smoke (`smoke_imports_r34.py`: `python -I`, `sys.path` set from the tuple in the built tree's own `resident_main.py`, every module the static reachability walk marks LIVE imported; a `ModuleNotFoundError` for a name the package itself holds is a FAILURE, a name it does not hold (a third-party library absent on the build box) is a NOTE), its place in the build driver, the verifier and the packet; the V2 script setting its `sys.path` from the same tuple and printing the checker's exception class; the V2 offline run on the merged tree with the order recorded.
- **Why the walk alone cannot catch it:** `r32_reachability.py` treats `lib` as a directory on the resident's path (its `DIRS`), which the service does not do; the smoke uses the service's real list.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-159` | `resident_main.py` adds `lib` to its path tuple; two tests in `test_resident_main.py` | `ycharts/generate/resident_main.py`, `ycharts/generate/tests/test_resident_main.py` | WORLD (the floor of an infra path; code and tests only, nothing deployed) |

## Edges and chains

- ONE chain; the r34k release (`AR-g-160`, the issuer's) follows it.

## Four-postulate record

(i) Domain: the resident's import path. (ii) One grain: a directory on `sys.path`. (iii) One intent: a package member that imports from `lib` imports in the service. (iv) What this cut does NOT move: the order of the other entries, the factory import, the loop, every other member.

fanout: 1 of 1 chains, cap 8, reason: one worker cell.
