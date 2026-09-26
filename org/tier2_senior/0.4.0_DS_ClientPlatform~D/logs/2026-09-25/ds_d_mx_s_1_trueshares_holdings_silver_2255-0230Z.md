# 0.4.0_DS_ClientPlatform~D -- MX-s-1: TrueShares holdings reach silver

**archetype:** MIXED

Session 2026-09-25 ~22:55Z -- 2026-09-26 ~02:30Z. Lane seated on Andrew's word (option 4, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260925_220xZ_CTO_O_NEXT_STEPS_ALL_FOUR.md`).
Orders from `2.0.0_SA_COO~O` at msg 25952: MX-s-1 then MX-s-2.

## Current State

**MX-s-1 is done on everything this lane can reach; AC1 PASS, AC2 refused as unreachable.**
MX-s-2 (the Black Diamond cusip bridge) is NOT started -- it is next.

Startup: `/watcher` armed (the lane was NOT REGISTERED and had zero watcher rows), `org/XXX.md` A.1-E
complete, `LIVE_ARMS.md` read -- no arm row for this lane, so zero crons, event-driven.

- Cause found and measured: two stacked defects, either alone sufficient. The deployed Lambda bundle
  predates the holdings converter by six weeks and carries **0** occurrences of
  `_convert_trueshares_holdings`; and `expected_partitions_etf` hardcoded `netassets_page` for every
  trueshares key, which is simultaneously why the sweep never dispatched a holdings key and why the
  guard read `missing 0`.
- Fixed and committed: `6c6232a5d7` (the feed follows `kc.feed`), `23efc28a2f` (the float64
  parse-or-raise pinned to the declared type, not to pandas' inferred dtype).
- Backfilled: 66 of 66 partitions, 2,367 rows, 0 defects on artifact re-read, idempotent on re-run.
- Rows `Z-S3..Z-S6` filed at `b2df0b5aef`.
- Deliverable + runner at `44f5910f8f`.

## What I got wrong, and the instruments that caught it

1. **I read a gate's verdict from a positional slice.** `safe-deploy ... | tail` printed `exit=0` --
   which was `tail`'s exit, not the gate's. The gate had in fact hard-BLOCKED. Re-measured by capturing
   `rc` into a variable. This is the banked lesson `never-read-a-gates-verdict-from-a-positional-slice`
   and I walked straight into it anyway; writing it down is not applying it.
2. **I nearly reported a three-blocker cause that was really two.** The missing `.csv` notification rule
   looked like a third independent blocker until I checked for a scheduled sweep -- which exists, is
   ENABLED, and lists bronze directly, so it bypasses the event rule entirely. Asking "which symptoms
   does this NOT cover" turned a wrong count into a correct one plus a latency finding.
3. **Three separate sparse-checkout artifacts read as real failures**: the halt-gate said my serial
   resolved to no known agent, `missions-tree-check` reported 27 INDEX-ORPHANs, and the watcher census
   read 0 rows for a live watcher. All three were my own cone, not the world. The discriminator each
   time was running the same instrument in the main tree.

## Blockers

**One, and it is not mine to clear.** AC2 cannot pass from the DS lane: `backfill-status.json` has
exactly one writer, the sweep, which runs the deployed bundle. Owner DT/AE, rows `Z-S4` / `Z-S5`.
Everything else on MX-s-1 is complete. Not a stall -- named, owned, and timed (a rebuild before
2026-09-26T23:30Z also prevents the guard flip).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'bd_assets\.parquet' --all --limit 60` | 68 hits / 75,160 files. Established **N=1 writer** of the builder's input before touching NEVER-1's writer-count rule. Worked. |
| `comp-find` | `comp-find 'dtype == object' --all --limit 25` | 26 hits / 75,199 files; 8 are the defective guard, 6 of them vendored. Sized the framework exposure for row Z-S3. Worked. |
| `comp-find` | `comp-find 'expected_partitions_etf' --all --limit 20` | 5 hits, bands DEF=2 SURFACED=2 TEST=1 -- showed the repo/lambda pair and the single existing test. Worked. |
| `comp-find` | `comp-find 'backfill_status' --band HEAD --limit 12` | `--band DEF` returned 0 while 156 hits existed; `--band HEAD` found the file. A band is a filter, not a denominator -- a DEF zero is not absence. |
| `comp-pipescript io` | `comp-pipescript io etf_conversion.py --pipeline all` | **`Unknown script in tree [all]: ETF_CONVERSION`.** NOT-APPLICABLE, measured. The `opal-data-assets` ETF tree is in no indexed pipeline, so the DS role minimum has no coverage here. `--pipeline data/assets` is not even an accepted choice. |
| `comp-pipescript deployed` / `postdeps` | same script | Same gap, same reason -- the script resolves in no tree. |
| `safe-deploy.sh` | `.tools/safe-deploy.sh data/assets/scripts/silver/etf_conversion.py` | `SKIP-NOT-MEMBER`, 404, **`NOTHING WAS DEPLOYED`**. It maps this dir to `opal-data-mdpf/code/scripts/silver/`, which is not how the converter runs. The tool's own output warns not to read its OK line as a deploy -- correct and worth copying elsewhere. |
| `safe-commit.sh` | 4 commits | All gates clean. `surprise-row-gate` graded 4 new rows OK. `missions-tree-check` correctly refused twice on my sparse cone before passing. |
| `proof-of-spec-check.py` | the MX-s-1 instance | Refused the first draft on 14 precise violations (schema shapes, missing required blocks, `artifact-coverage` on 4 artifacts). Every one was real. |

**Gap worth naming:** the `data/assets` ETF silver pipeline is invisible to `comp-pipescript` in all
three verbs. A DS seat working this tree has no dependency-graph instrument at all -- part of how a
registered feed sat unconverted for a month with every tool green.

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~D`]** MX-s-2, the Black Diamond cusip bridge. Already measured at
   startup and it changes that order's premise: `build_bd_assets_dim.py`'s only input,
   `silver/bd_assets.parquet`, is **itself frozen at 2026-04-14** with the same 10,937 asset_ids, so
   scheduling the builder as R-2 (2) rules would rebuild identical bytes and fix **0 of the 791**
   missing asset_ids. The daily `silver/assets/` partitions also stop at 2026-06-18 while
   `silver/transactions/` is current to today. Carry this into MX-s-2 rather than re-deriving it.
2. **[DT/AE, via `2.0.0_SA_COO~O`]** rebuild `opal-assets-silver-etf` -- the one act that closes AC2 and
   disarms `Z-S5`. Before 2026-09-26T23:30Z avoids the served guard flip entirely.
3. **[`2.0.0_SA_COO~O`]** route `Z-S3` (the shared `mirror_conversion` guard) and `Z-S6` (pathfinder
   `missing 2`).
