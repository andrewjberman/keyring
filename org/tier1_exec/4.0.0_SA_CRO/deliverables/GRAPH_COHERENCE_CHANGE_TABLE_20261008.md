# 4.0.0_SA_CRO -- graph coherence build: the changes I drive, write paths, finish times

**For:** `1.0.0_SA_CTO`, msg 107017 (Andrew-direct ~17:1xZ: timing, and no overlap with `2.0.0_SA_COO~C`).
**Authority:** Andrew-direct ~16:5xZ (this seat leads the build, no canonical registration) and ~17:0xZ (hook on every
box), records in this folder. **Written:** 2026-10-08 ~17:2xZ.

**Fences honoured:** nothing here writes `infra/aws/terraform/nfra-ctlpln-identity/` or `org/devices/`. The tool READS
`org/devices/DEVICES.json` through `lib/devices.py` to name its box. The Dell graph read (fast fix F1) is
`2.0.0_SA_COO~C`'s cell 2 (~18:3xZ); until it lands, `who --graph` answers on the laptop only.

| # | Change | Write paths | Worktree | State / finish (UTC) |
|---|---|---|---|---|
| 1 | `fabric-activity` v1: emit, who (EDITS + DECLARES + HOLDS + `--graph`), overlap, boxes, backfill | `.tools/fabric-activity.py`, `.tools/git-hooks/fabric-activity-post-commit.sh`, `.tools/git-hooks/install-fabric-activity.sh` | shared tree (new files; the worktree branch was retired after a merge refusal) | DONE: @4ce1e3659e, @b6d8b3f995, boxes view next commit |
| 2 | Hook installed on the laptop | `.git/hooks/post-commit` (laptop) | -- | DONE 17:09Z; emitting (log `.comp-graph/fabric-activity/emit.log`) |
| 3 | The activity store | `s3://opal-313476888478-globgrph/fabric/activity/v1/` (outside `warehouse/`; the served graph's build is untouched) | -- | LIVE: one object per commit; 2,934 backfilled (box inferred) |
| 4 | Hook on dell1, dell2, site Z | each box's `.git/hooks/post-commit` | -- | ASKED of `0.0.0_AB_MSTR` (push + relay to each box's MSTR); expect ~18:3xZ, gated on its push |
| 5 | MERGED verb (when a box's commit reaches `origin/CLOUD`) and an overlap page on request | `.tools/fabric-activity.py`; page published as an Artifact | shared tree | ~19:0xZ |
| 6 | Build record for Andrew: what is live, how to use it, the enrichment list | `org/tier1_exec/4.0.0_SA_CRO/deliverables/GRAPH_COHERENCE_BUILD_20261008.md` | shared tree | ~18:0xZ |
| 7 | Fold the activity records into the served graph | would write `infra/aws/globgrph/` (the Kuzu loader and refresh) | -- | NOT STARTED: waits on the engine decision (handed to a new CRO, `GRAPH_ENGINE_HANDOFF_20261008.md`) |

**Already landed this session, for completeness:** surprise row `NFRA_CTLPLN-S32` (append to the control plane's
channel; `placement-check.py:90` reads `fabric`, never `placement`).
