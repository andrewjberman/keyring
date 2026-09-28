# SITE-Z AMGT -- REBOOT STATE AND RESTART INSTRUCTIONS (2026-09-28)

**Author:** `1.0.0_SA_CTO~Z`, on Andrew's word (record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_161xZ_CLOSE_OUT_SITEZ_FABRIC_FOR_REBOOT.md`).
**Written:** ~17:0xZ, after every AMGT issuer on site Z had wound down. **Read this first after the reboot.**

## 0. ANDREW'S INTENT (verbatim, 2026-09-28, this terminal)

> "post-reboot, i want to restart all AMGT workstreams, HARVST/CORPUS/RESAPP/etc., so we want a clean startpoint and
> that instruction and state recorded."

> "I am going to work with MSTR~Z to essentially make sure that we are properly integrated here with the work that has
> been getting done on the laptop box, (and vice versa), with the intent being that at the reboot point, we wil have all
> necessary data/structures/development at parity both on local and in remote with the laptop box, and the two fabrics
> can get back started in an organized fashion on their respective workstreams."

**So:** parity with the laptop is `0.0.0_AB_MSTR~Z`'s act with Andrew. This file is the AMGT restart map. Every fact
below is read from the RECORD (git at the time of writing); re-measure before acting on any of it.

## 1. RESTART ORDER

1. **Device first (Andrew's act, admin shell), or every seat restarts without broker messaging** -- see section 5.
2. `0.0.0_AB_MSTR~Z` -- `/watcher`, `/integrate`; confirm CLOUD == origin/CLOUD after the purge/parity work.
3. `1.0.0_SA_CTO~Z` -- `/watcher`, then this file, then re-arm nothing else (zero crons at launch).
4. One COO lane per project, each reading ITS checkpoint (section 2). Suggested seating, as before the wind-down:
   `2.0.0_SA_COO~Y` -> AMGT_HARVST, `2.0.0_SA_COO~X` -> AMGT_CORPUS, `2.0.0_SA_COO~Z` -> AMGT_RESAPP.
5. `3.0.0_SA_CVO~Z` -> L8-L10 for all three AMGT projects. **This ENDS the standing route** that sent AMGT_HARVST's
   L8-L10 to `3.0.0_SA_CVO~O` "while CVO~Z is wound down". If CVO~Z is not re-seated, the route stands.

## 2. PER PROJECT -- where it stands and the FIRST act on restart

### AMGT_HARVST (publications harvest) -- 9 outcomes, none REALIZED; rounds 1-10 CLOSED; round 11 ISSUED, not executed
- **Resume from:** `org/tier1_exec/2.0.0_SA_COO~Y/logs/2026-09-28/session_close_0104-1440Z.md` (@`31900d53e6`) and
  `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round10.md` (corrected in place).
- **Round 11, four orders all `pending`:** `z-0` wire the two timeline routes into `lib/research/api/scoped_amgt.py`;
  `z-1` rebuild `chatter_event` gold under PRD v0.3 (never-widen pair SIGNED both halves: COO @`7f9df49098`, CTO
  `ledger/NEVER_WIDEN_CTO_HALF_chatter_event_rebuild_20260928.md` @`9fddce21db`) -- carries the round's JUDGMENT
  criterion; `z-2` FWD-4 field census (all six facts ARE carried -- mapping in my 20260928T121016Z-reply);
  `z-3` the repo-wide `patch("lib....")` audit (8 sites, 5 files, cross-project paths authorised by this seat).
- **Workers were stopped with 0 unmerged commits.** Worktrees still on disk: `C:/Users/Opal Bloomberg/Desktop/
  wk-hvst-z0-r11`, `wk-hvst-z2-r11` (z-2's two AC scripts, UNCOMMITTED -- the only worker output), `wk-hvst-z3-r11`;
  older: `C:/tmp/wk-hvst-v2`, `C:/tmp/wt-cvoz-harvst`. **FIRST ACT:** the COO re-spawns round 11 against those orders
  (or re-cuts them fresh) -- decide on z-2's uncommitted scripts before removing its worktree.
- **Held outside the round:** portal commit `92a2576254` (the timeline panel, CTO-APPROVED) sits on LOCAL portal DEV,
  unpushed; `0.0.0_AB_MSTR~Z` holds its push until `z-0`'s routes land, then needs Andrew's word (DEV was 22 behind
  origin; merge clean). Vendor cards `w-2`/`w-4`/`w-5` wait on Andrew's per-use word. No serp/social cell until
  identity resolves through existing channels (Andrew, @`a89b7619ca`).

### AMGT_CORPUS (company research corpus) -- 19 outcomes; round 7 OPEN
- **Resume from:** `org/tier1_exec/2.0.0_SA_COO~X/deliverables/CHECKPOINT_AMGT_CORPUS_20260926.md`.
- **Round 7:** acts A (94 model blocks re-derived; CTO-verified by re-run) and B step 1 (95 continuations at `/2`)
  LANDED. **Act B step 2 (the dossier rewrite) was NOT RUN** -- held because the limb-4 gate census (current_method_available
  95, stale_pick 0) timed out twice; the step needs that census to read before it runs. `TO-CRPS-i-5` (the 19-outcome
  evidence pass) is issued and `pending`, never spawned.
- **FIRST ACT:** make the limb-4 census finish (a longer budget or a faster instrument), then step 2, then `i-5`.

### AMGT_RESAPP (security-analysis page) -- 31 outcomes; round 45 OPEN in the record, DONE in the world
- **Resume from:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/CHECKPOINT_20260926_COO_Z.md` and the
  CVO's `org/tier1_exec/3.0.0_SA_CVO/deliverables/SESSION_CHECKPOINT_20260926_Z.md`.
- ⛔ **`TO-AMGT-tt-2` (the redeploy) LANDED on 2026-09-27 ~00:29Z** -- `0.7.0_AE_CloudOps~A` @`bdf48ee216`: "LANDED and the
  entry CLOSED -- 10 legs proven" -- **but its `<status>` still reads `pending`**, because COO~Z wound down before
  draining it. That one flip is what holds round 45's L8/L9 (parked by the CVO on exactly that order).
- **FIRST ACT:** the COO measures the deployed function against tt-2's AC1 (CodeSha256 moved off the base), flips tt-2
  `complete` citing `bdf48ee216`, then the CVO compiles round 45. **Round 46** is already planned: a full
  FWD-1..FWD-31 pass as one cell (COO~Z's checkpoint s.2 item 5).
- **Cross-project:** the HARVST timeline mounts in this project's page header (CTO ruling
  `org/missions/D5/AMGT/AMGT_HARVST/ledger/CTO_RULING_TIMELINE_PLACEMENT_20260928.md` @`277b0795ac`).

### POSN_ASTTAX -- CLOSED. Nothing to restart.

## 3. RULES MADE THIS SESSION THAT THE RESTART INHERITS

- The round's JUDGMENT criterion sits on a cell that can issue without a pending Andrew word (HARVST round-8 analysis).
- A record may be CORRECTED toward what was actually run, never bent toward what the checker expects.
- Group a backlog by MECHANISM before quoting its size (HARVST item 6: 16 rows were 2 defect classes + singletons).
- A pathspec under the `portal` submodule runs as `git -C portal ...`; a render criterion names its data source.
- `prd-signoff.py status` binds halves to the ENDPOINT hash: a CONTRACTS edit reads "current by ENDPOINT hash; this
  half's text CHANGED" (@`ea81ad7be3`). The re-sign of a contract change is a stamp FILE, not the status line.

## 4. SHARED-TOOL FIXES LANDED THIS SESSION (all LOCAL at commit; carried by MSTR~Z's pushes)

`missions-tree-index.py` reads the git index on a sparse cone (@`454fc37e30`); `comp-find` refuses unknown flags and
zero-file pathspecs (@`2d2f697a82`, system doc regen @`f4d0ef436b`); `prd_signoff_lib` status wording (@`ea81ad7be3`).

## 5. DEVICE STATE A REBOOT DOES **NOT** FIX

- ⛔ **Python 3.14 is gutted** (`C:\Program Files\Python314`: `Lib\` holds only pip, `DLLs\` 3 icons, since 2026-09-26
  17:02Z) and sits in the **MACHINE** PATH ahead of Python 3.11. Bare `python` crashes, so `.mcp.json`'s
  `opal-agent-comms` never starts: **no seat on this box has broker messaging** -- mail travels as inbox FILES only.
  **Fix (Andrew, admin PowerShell), approved as REC (a) @`a89b7619ca`:**
  ```powershell
  $p=[Environment]::GetEnvironmentVariable('Path','Machine'); $p | Out-File "$env:USERPROFILE\machine_path_backup_20260927.txt"
  [Environment]::SetEnvironmentVariable('Path', (($p -split ';' | ? { $_ -and $_ -notmatch '\\Python314' }) -join ';'), 'Machine')
  ```
- **Already set by this seat (user scope, reversible):** `PY_PYTHON=3.11`, `PY_PYTHON3=3.11`, so `py.exe` and every
  comp-* `.cmd` shim run 3.11. Remove with `[Environment]::SetEnvironmentVariable('PY_PYTHON',$null,'User')` (and `PY_PYTHON3`).
- **Until the PATH fix:** `safe-commit.sh` fails in any shell whose bare `python` is 3.14; the workaround used all
  session is to prefix Python 3.11 for that one call:
  `PATH="/c/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311:$PATH" bash .tools/safe-commit.sh ...`
- **History purge:** Andrew released it 2026-09-28 ("Release it, purge today"); `0.0.0_AB_MSTR~Z` owns the push freeze,
  the force-push re-sync and the all-clear. Scope was the 28 client screenshot PNGs; the BD password in history was
  NOT in that scope.

## 5a. ⛔ THE S19 PURGE CONSTRAINT -- binds every AMGT restart act (added ~17:5xZ)

Andrew has HELD all site-Z work until every worktree is drained, analysed and merged or superseded
(`0.0.0_AB_MSTR~Z` @`f10abae456`, `mstrZ_S19_POSTPURGE_DRAIN_STATE_AND_PROPOSAL_20260928.md`). origin/CLOUD was
REWRITTEN by the purge. **Merging ANY pre-rewrite branch into the rewritten trunk reconnects the old history and undoes
the purge -- land content by CHERRY-PICK only.** For AMGT that means:
- The HARVST round-11 worktrees (`wk-hvst-z0/z2/z3-r11`) are PRE-REWRITE branches: re-spawn round 11 on fresh
  worktrees cut from the re-synced trunk; carry `z-2`'s two uncommitted AC scripts across by copying the files, never
  by merging the branch.
- The 10 AMGT branches in the drain worksheet are dispositioned in
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_S19_DRAIN_VERDICTS_24_BRANCHES_20260928.md` (CVO~O), with this seat's
  independent concurrence: the six `wk-amgt-13-*` SUPERSEDE; `cvo-z-harvst-l4r`, `closer/amgt-r-20260923` and
  `wk-amgt-14-50` (records only) LAND by cherry-pick; `closer/amgt-experience-z` + `closer/amgt-h-y` HOLD as one
  decision on Andrew's word.

## 6. STATE AT WRITING THAT MAY STILL BE LIVE

- `.git/index.lock` in the shared tree was held from 16:43:09Z to ~17:08Z by `3.0.0_SA_CVO~O`'s slow `git commit`
  (PID 13400); it completed on its own. The stale `amgt-crosswalk-0924-rollback` open-deploy entry (closed in the world
  on 2026-09-24, never committed) is now closed on the trunk @`c292ef25b7`. **No AMGT deploy entry is open.**
