# /self-drive "AMGT fabric ops" -- tick 1 -- `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md` @64a6172e7b.
**Cron:** `13,43 * * * *`, session job faa57fd1. **state: ARMED**
**Scope:** 4 projects: AMGT_CORPUS, AMGT_RESAPP, AMGT_HARVST, DSGN_AMGTV1. All are `active`, `EXECUTING`, placed site-z.
Device: sitez. Open TOs in scope: 13 pending (CORPUS p-1..5; DSGN w-1..6; HARVST g-1, g-2) plus RESAPP ww-1.
**Sequence:** all 4 are UNPLACED, so their own directive rules govern them. No flags. (The header's `projects: 1` counts
the queried projects that are placed, so it is not drift.)
**Inbox:** 0 unread. Mail since the edict was READ-acked: 26637 (COO~X), 26638 (COO~D), 26639 (COO~H), 26640 (COO~Z).

## Post-crash steps 1 and 2 (edict @626d53db16)

| seat | report | verified here |
|---|---|---|
| 2.0.0_SA_COO~X | @f65777840e: 14-1/2/3 resume in place; p-4 is cut when ww-1's entry closes; 14-5 restore on Andrew's go | same measurement as the inventory |
| 2.0.0_SA_COO~D | @ded6446182: w-1 salvaged @e051ec096d | e051ec096d holds the 4 files (+71/-19); the tree is left with only `.scratch/` |
| 2.0.0_SA_COO~H | @bdde2227e0: g-1 salvaged to `refs/archive/wt-20260929/wk-AMGT_HARVST-45-wip` @a4374c7043 | ref resolves; the commit carries universe_securities.py, publication_gold.py, the tests, and the proof_of_spec |
| 2.0.0_SA_COO~Z | @8d79cf769c: ww-1 NEVER-2 entry ABANDONED NOT-STARTED; AE~A respawned at restart | `.open_deploys` holds 0 ww1 entries |
| 3.0.0_SA_CVO~Z | OUTSTANDING (`wt-cvoz-harvst`, canonical-flow grade) | -- |

## Calls ruled by the driver

| call | ruling | why |
|---|---|---|
| `wk-hvst-z2-r11`: 3 patch-unique commits carrying client screenshots from before the purge (COO~H) | The branch is KEPT. The checkout joins the removal list. The purge decision on the 3 commits goes to 0.0.0_AB_MSTR~Z, the purge owner. PARKED: owner MSTR~Z; it un-parks when MSTR~Z is live (msg 26648 is QUEUED). | Keeping the branch loses nothing. What happens to client data is the purge owner's call. |
| `coo-y-leadpanel-20260924` | PARKED: owner 2.0.0_SA_COO~Y (a laptop seat); it un-parks when COO~Y is live on site Z | The 3 modified harvest `.tf` files have no other owner |

Zero governance or reserved-class calls this tick, so nothing was pitched to CVO~Z.

## Acts

- Arming record and LIVE_ARMS row @64a6172e7b. The 2026-09-28 AMGT row is struck.
- Step-3 restart sent (msgs 26643-26648): COO~X/~Z/~H/~D arm their paired `/canonical-drive`.

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Acts only Andrew can do (cited)

1. **Go on worktree removal and repair** [CLAUDE.md Agent Autonomy: recursive deletion and destructive git].
   - Remove 12 checkouts: `wk-crps10-1`, `-12-1`, `-13-1`; `wk-dsgn-amgtv1-9` to `-12`; `wk-hvst-r16-42`, `r17-43`,
     `r17-44`; `ae-a-vv4`; `wk-hvst-z2-r11`.
   - Repair `wk-crps14-5` in place. Every branch is kept.
2. Read the Seeking Alpha subscription state (HTTP 402, `AMGT_HARVST-Z-W37-S4`) [entitlement].
3. Lift *"lets hold on pushes and merges for now"* for portal `92a2576254` [a hold set by name].
   - Fetch read this tick: the commit is on local DEV and not on origin/DEV (`--is-ancestor` rc=1 after the fetch).

## Compiler Tools

- `directives-check.py --json`: 15 live directives; D5 has 3 members, and DSGN_AMGTV1 resolves under D13.
- `sequence-check.py --project` x4 plus positive controls NFRA_MCPINDEX and MDPF_CANON, both PLACED.
- `active-commitments.py` (2 lines, none in scope).
- `postcrash_worktree_inventory.py`: 57 of 57 worktrees.
- `git cherry` / `rev-list` per branch; `ls-tree` over `.open_deploys` in every worktree.
- `lambda get-function-configuration opal-amgt-scoped-api`.
- One rail refusal: a raw grep, re-done with `git log`.
