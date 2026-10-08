# Graph coherence build -- what is live, how to use it, what comes next

**Lead:** `4.0.0_SA_CRO`, on Andrew-direct ~16:5xZ ("lead the development of this function ... lets get through it")
and ~17:0xZ ("Call 1, sure"). Records in this folder. **Written:** 2026-10-08 ~17:3xZ.
**Folds in:** the activity-overlap research of 2026-10-07 (`FABRIC_PROXIMITY_MAP_RESEARCH_20261007.md`): one record, "a
box did a thing to a surface", with four verbs.

## 1. What is live (laptop, measured)

| Piece | Where | Proof |
|---|---|---|
| The tool | `.tools/fabric-activity.py` (@4ce1e3659e, then @b6d8b3f995, @2ea9a7bb97, @95aee88562) | commit gate clean |
| The store | `s3://opal-313476888478-globgrph/fabric/activity/v1/dt=<day>/box=<box>/<time>_<sha>.json`: one record per commit, outside `warehouse/`, so the served graph's build is untouched | 5,047 objects at 17:2xZ |
| The hook | `.tools/git-hooks/fabric-activity-post-commit.sh`, wired into the laptop's `.git/hooks/post-commit` at 17:09Z by `install-fabric-activity.sh` | `emit.log`: OK lines for this seat's commits and other seats' (e.g. 6ded8fd5d9); the hook runs in the background |
| History | 2,934 commits since 2026-10-07 04:00Z backfilled; the box is INFERRED from serials and carried as `box_claim` on every record. A measured record wins over an inferred one. | `backfill` output |

## 2. How to use it (any box with S3 read on the graph bucket; `--graph` also needs the graph token)

```
python .tools/fabric-activity.py who <path-or-surface> [--hours 24] [--graph]
python .tools/fabric-activity.py overlap [--hours 24] [--all]
python .tools/fabric-activity.py boxes [--hours 24]
```

- **who** answers "who else is working on this?" with all four verbs:
  - EDITS: commits by box, each marked MERGED or on-box against `origin/CLOUD`.
  - DECLARES: open task orders whose `<paths>` cover it, with the box taken from the project's placement.
  - HOLDS: open deploy entries that name it.
  - With `--graph`: what the estate graph says it is, with the graph's vintage.
- **overlap** is the overlap map on request: surfaces with two or more boxes on them, Terraform first, then code, the
  registry and tools. Record folders and append-only files are left out unless `--all`.
- **boxes** gives the figures per box: commits, seats, surfaces, and how many of those another box is also on.

A surface is the coarsest unit that still names one thing: a Terraform module (`tf:shared-infra`), a Lambda source
folder, a gold script (`pipeline:<firm>:<tier>:<script>`), a lib module, a tool, a skill, a portal folder, or a
project's record tree.

## 3. What it showed on its first runs (box inferred for history)

- Last 24 h: 5 surfaces had two or more boxes on them, out of 116 code, infra, registry and tool surfaces touched:
  `tf:harvest` (laptop, site Z), `tf:opal-assets` (dell1, laptop), `lambda-src:ci` (dell1, dell2, laptop),
  `lib:opal_data_harvest` (laptop, site Z), `tool:cleanup-disk.ps1` (laptop, site Z).
- `tf:opal-assets` is the dangerous shape the research named. dell1 and the laptop both committed to it today, and an
  OPEN deploy entry (`healgap-r2-act1-runner-code-20261008`) holds it.
- Per box, last 24 h: laptop 659 commits / 41 seats; site Z 218 / 40; dell2 218 / 39; dell1 210 / 18.

## 4. What comes next (enrichment, in order)

1. **The other three boxes run the installer.** Asked of `0.0.0_AB_MSTR` (push, then relay to each box's MSTR). From
   then on every box's records are measured, not inferred.
2. **The Dells get `--graph`** when `2.0.0_SA_COO~C` lands the Dell graph read (its cell 2, ~18:3xZ).
3. **An overlap page**, if Andrew wants a page rather than the command.
4. **Fold the records into the served graph.** This waits on the engine decision, which a new CRO holds
   (`GRAPH_ENGINE_HANDOFF_20261008.md`). Until then the join to the estate happens at query time.
5. **Fix `placement-check.py:90`** (row `NFRA_CTLPLN-S32`), so the control plane's own overlap viewer stops placing every
   Dell project on the laptop.

## 5. Limits, stated

- A commit made on another box that is not yet pushed is visible here only once that box runs the hook.
- DECLARES and HOLDS are read from this box's tree, so another box's unpushed order or deploy entry is not seen.
- Box inference for history uses serial patterns: a lane ending in 1 or 2 is a Dell, ~Z is site Z, a worker goes by
  its project's placement, and other agents are the laptop. Commits under a human name stay "unplaced".
- No monitor, alert or refusal exists. It answers when asked.
- The first backfill pass (before the inference fix) left about 2,100 superseded objects in the store. Reads ignore
  them, and they fall out of the default window after two days. Nothing was deleted.
