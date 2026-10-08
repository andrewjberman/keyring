# Per-box branches -- build placement and owners (1.0.0_SA_CTO, 2026-10-08 ~18:1xZ)

**Design:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/PER_BOX_BRANCH_DESIGN_20261008.md` @7242a56f84, Andrew's answers verbatim
in its section 9 (~18:0xZ): laptop MSTR integrates `CLOUD` (site Z MSTR standby); the graph reads every `origin/box/*` plus
`CLOUD`; site Z switches first, then the Dells, the laptop last; cadence on fixed minutes, made size-invariant by section 10.
Andrew: "let the conclusions to these points be known quickly because we're already under strain."
**Mode:** fast build, no registered project (Andrew ~16:0xZ); the CROs drive, `0.0.0_AB_MSTR` lands fabric infrastructure.

| # | Build item | Owner | Lands | Gate before site Z switches? |
|---|---|---|---|---|
| B1 | The `CLOUD`-literal pass over the 48 files (section 6.1): `.tools/hooks/never-rules-gate.sh` adds `box/*` to the shared-branch list (no rebase, no force-push); scripts read "the branch checked out"; `/integrate` and `/git-pull` gain the BOX PASS (take the trunk, then push `box/<box>`) and the INTEGRATOR PASS (one octopus merge of every box branch ahead, one grade, one tree-drop check, one push; a conflicting box is merged alone or held; a running pass skips its next slot) | 4.0.0_SA_CRO~A (sole owner of `safe-commit.sh` / `safe-merge.sh`, msg 107030) | 0.0.0_AB_MSTR | YES |
| B2 | **Deploys stay on the authoring box.** `.tools/git-hooks/pre-push-safe-deploy.sh` deploys only on a push of `refs/heads/CLOUD` today, so under per-box branches every deploy would fire from the laptop integrator. That contradicts Andrew ~16:4xZ ("We should no longer need to be running deploys for the whole fabric on this box"). Rule: a deploy fires on the authoring box's own push of `box/<box>`, over that box's diff against `origin/CLOUD`; the integrator's push of `CLOUD` deploys nothing. NFRA_CTLPLN's contract C-TRUNK-DEPLOY (surface S01) is the same file: 2.0.0_SA_COO~C is told, holds no live cell on it, and does not edit it | 4.0.0_SA_CRO~A | 0.0.0_AB_MSTR | YES |
| B3 | Time one real integration pass; if the grade is the long pole, grade only the paths the merge changed | 4.0.0_SA_CRO~A | 0.0.0_AB_MSTR | NO (before the Dells switch) |
| B4 | The graph reads every `origin/box/*` plus `CLOUD` (the activity tool and the `stitch-refresh` freshness read) | 4.0.0_SA_CRO | 4.0.0_SA_CRO's own commits | NO |
| B5 | Worktree "merged" test reads `origin/CLOUD` OR the box branch (`.tools/cleanup-disk.ps1`, and the worktree-removal rule) | 4.0.0_SA_CRO~B | 0.0.0_AB_MSTR | NO |
| B6 | `/govern` minute offsets (laptop `0,30`, site Z `6,36`, dell1 `12,42`, dell2 `18,48`) in the skill text and `org/ref/LIVE_ARMS.md` | 1.0.0_SA_CTO | done in this commit | -- |
| B7 | Cut-over: site Z creates `box/sitez` at its `CLOUD` tip, pushes, switches its shared tree; the laptop runs the first integrator pass (a no-op proof); then dell1, dell2; the laptop last | 0.0.0_AB_MSTR~Z, then ~DELL1, ~DELL2, 0.0.0_AB_MSTR, each on its own box; 0.0.0_AB_MSTR coordinates | -- | after B1 + B2 are on origin |
| B8 | Delete the 159 old `origin/q/*` branches | -- | -- | Andrew's word (a delete); after the model runs clean |

**Order change, Andrew ~19:5xZ** (verbatim in `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20261008_195xZ_LAPTOP_TO_BOX_BRANCH_PROGRAMMATIC_PULLS.md`):
"we need to get this box pushed to its box branch". B7's "the laptop last" is reversed: the laptop switches to `box/laptop` now.
Until 4.0.0_SA_CRO~A's programmatic pass lands, the laptop's commits reach `CLOUD` only through the integrator pass that
0.0.0_AB_MSTR runs.

Rollback (design section 6.4): each box switches back to `CLOUD` after one last box-branch merge; nothing is deleted until the
model has run clean.
