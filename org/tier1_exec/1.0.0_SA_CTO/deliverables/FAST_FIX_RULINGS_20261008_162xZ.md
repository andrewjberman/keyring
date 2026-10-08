# FAST FIX rulings -- GitOps, process GC, graph coherence (1.0.0_SA_CTO, 2026-10-08 ~16:2xZ)

**Order:** Andrew-direct ~16:0xZ, addendum in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
@fdef7ad167: "we need to get fast solutions out across the boxes while we get organized".
**Lists ruled:** GitOps `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/GITOPS_FAST_FIXES_20261008.md` @5504357066;
GC `docs/briefs/process-gc-fast-fixes-20261008.md` @8b88d72639; graph
`org/tier1_exec/4.0.0_SA_CRO/deliverables/GRAPH_COHERENCE_FAST_FIXES_20261008.md` @6418d9ab13.
Every item below is ACCEPTED as written unless the row says otherwise. Each applier states its expected outcome before
it acts and reports the measured result after.

## Order of landing (one integrator, 0.0.0_AB_MSTR, laptop)

| # | Item | Applies | Boxes | Condition |
|---|---|---|---|---|
| 1 | GitOps F3: `core.untrackedCache true` | each box's MSTR, own clone | all four | run `git update-index --test-untracked-cache` first; skip a box that fails |
| 2 | GitOps F4: `.gitattributes` `merge=union` on the two surprise-channel patterns only | 0.0.0_AB_MSTR | all, by trunk | as written; no other file pattern |
| 3 | GC FF3: one Traps line in `.claude/skills/watcher/SKILL.md` (`timeout 1790 bash -c` for a hand-armed Monitor) | 0.0.0_AB_MSTR | all, by trunk | as written |
| 4 | Graph F2: correct the Cypher example at `.tools/comp-which:1198` | 0.0.0_AB_MSTR | all, by trunk | as written |
| 5 | GC FF1 + FF2: `kill-maint.ps1` tree-kill + the four new classes | DRAFT and exercise: 4.0.0_SA_CRO~B (it holds the reproduction); LAND: 0.0.0_AB_MSTR | all, by trunk | lands only with the laptop arms A/B/C re-run against the patched script and a dry-run census printed; a live seat's watcher is the negative control (never a target) |
| 6 | GitOps F1: `/integrate` Step 1 drains in a linked worktree, then fast-forwards the shared tree | 0.0.0_AB_MSTR edits the skill; each box's integrator uses it from its next drain | all four | the tree-drop check runs in the worktree before the fast-forward; the GC reaper never targets a `drain-*` worktree |
| 7 | GitOps F2: `safe-commit.sh` lock reclaim by liveness, logged, spawn-free; give-up 300 s | 0.0.0_AB_MSTR | all, by trunk | HIGH BLAST RADIUS: lands only after `bash -n` and the two-waiter exercise (holder alive past 60 s = no reclaim; holder killed = reclaim + a `LOCK-RECLAIM` log row) |
| 8 | GC FF4: one dry-then-go `/kill scripts` sweep per box | each box's MSTR | all four | only after item 5 is on that box; the operator reads every target before `go` |

## Graph items

- **F1 (Dells read the graph): NO NEW RULING NEEDED.** `opal/mcp/graph-read-token` is one of the 28 PLATFORM-KEY secrets
  in the census (`vendor_secrets_census.json`: 28 of 114 classed PLATFORM-KEY, this token among them), and Andrew already
  said "WIDEN THE TWO GRANTS, YES" to "the 28 platform keys" at ~13:2xZ (record
  `ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md` row 3).
  My msg 106669 exclusion is superseded by that word. It ships with the grant widen, which is UNAPPLIED: its apply seats
  (2.0.0_SA_COO~C, 0.7.0_AE_CloudOps~E) are not live after the reboot. Proof stays as the list says: one `comp-kuzu`
  query on dell1 and on dell2.
- **F3 (one full rebuild + why 2026-10-07 did not publish):** WITHDRAWN ~16:4xZ. Its premise is false (4.0.0_SA_CRO msg
  107000): the nightly full rebuild published every night 10-04 through 10-08, read from the projection manifests; the
  "last full 10-04" read came from a marker field that each incremental update overwrites. Its task order
  NFRA_CTLPLN.TO-GRAPH-1 (@5431396b08) goes to `cancelled` by its issuer, 2.0.0_SA_COO~C.
- **F4 (say the vintage):** ACCEPTED; binds by reading. Every seat that acts on a graph answer quotes its `VINTAGE:` line.
- **F5 (no Deny on the Dells' graph-bucket write):** ACCEPTED on Andrew's call 3 ("They should be able to"); row
  `NFRA_CTLPLN-S31` is dispositioned by that word, no Deny is added. The sanctioned write shape is the project's (draft
  FWD-6).

## Not ruled here

GC's "held for Andrew" items (unattended runs) and GitOps' branch-model change stay with Andrew.
