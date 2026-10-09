# 2.0.0_SA_COO~MI -- WIND-DOWN for the site Z reboot (Andrew-direct ~06:1xZ, msg 32451) -- 2026-10-09 06:3xZ (host opal_bloomberg)

**archetype:** COORDINATE

Andrew, verbatim (relayed by 0.0.0_AB_MSTR~Z): "we will roll that into a reboot, so everyone on sitez should wind down
preemptively and log as needed." No new work was started after 06:21Z. The shared tree holds no uncommitted edit of
this lane.

## Seat state at wind-down

- **Loop:** `/canonical-drive NFRA_MCPINDEX` armed this session, cron `16,46 * * * *` (session-only; it dies with the
  reboot). LIVE_ARMS row: the `1.0.0_SA_CTO~O` `/self-drive 30m` pair. The successor re-arms off that row.
- **Watcher:** session Monitor (dies with the reboot). The successor runs `/watcher`.

## NFRA_MCPINDEX -- round 8 (PRD v0.7, issued @b0d8580aab; project.json line @c0a35a17b4)

| order | worker / worktree | state at wind-down | next act for the successor |
|---|---|---|---|
| MX-d-7 | ~28, `C:/Users/Opal Bloomberg/Desktop/wk-mcpindex-r8-28` (branch `wk-NFRA_MCPINDEX-28`) | code @6584b623fa, AC1-AC3 PASS by output. Trunk merged @407ae3578f (re-seat, disarming Z-W28-S3). The re-seat lands the proof, flip and rows S1-S3 -- see the addendum below for whether it finished | if the flip is committed: grade AC1-AC3 on the branch, drain with `safe-merge.sh` in a drain-* worktree. If not: re-seat ~28 with the same order (copy to .scratch, restore, re-apply, commit) |
| MX-c-6 | ~29, `C:/Users/Opal Bloomberg/Desktop/wk-mcpindex-r8-29` (branch `wk-NFRA_MCPINDEX-29`) | code @e7f52df685: emitter + 29 need files + test + regenerated catalog. AC1 29 of 29, AC2 3 of 3, AC3 15 named, 0 unknown, all PASS by output. UNCOMMITTED in the worktree: the order flip (left `in_progress`), the proof instance (VALID), and rows Z-W29-S1/S2. Cause: the base 6d704a78c3 predates the index-drift fix | re-seat ~29 with the MX-d-7 re-seat order: merge `box/sitez`, re-apply the three paths, re-run c6.AC1-3 and proof-check, commit. Then grade and drain |
| MX-d-8 | ~28 after both drain | not started | continue ~28 with its worker face (the order file) once MX-d-7 and MX-c-6 have drained |
| MX-r-9 | ~28 after MX-d-8 | not started | the release train via `2.0.0_SA_COO~O`; PHASE B by a fresh site-Z CloudOps lane (CTO~Z ruling 32344) |

**Rows to rule (issuer, disarm_owner 2.0.0_SA_COO~MI):**
- **Z-W29-S1 (OBSERVATION, ARMED):** MX-c-6's emitter caution was wrong.
  - Main-tree `--census-dir` rewrites 32 `census_ref` lines to `../ajb_workspace/...`. The worker used the worktree's
    own tracked census instead, and the diff was clean.
  - Ruling for the successor: CONFIRM the worker's choice. The order's caution came from MX-d-6's era, before the
    census was tracked. Amend the face for any future catalog cell.
- **Z-W28-S3 / Z-W29-S2 (BLOCKING):** both are the index-drift refusal, fixed on the trunk (IRPT_ANLREQ @50f575ae4c,
  ADVI_BILLING @ac148d7eb9; NFRA_OPSWKF reported to MSTR~Z 06:0xZ). They disarm when the merge lands each slot's
  three paths.
- **Z-W28-S1, S2:** INERT (test pins rewritten; silver rows read `absent`). Read them at the drain.

## Time-windowed obligations

1. **MX-s-19 (round 7):** after 03:00Z on 2026-10-13, run `round7/checks/s19.PRE.sh`.
   - On PASS: amend `<issued_to>` to a FRESH site-Z CloudOps lane and tell 1.0.0_SA_CTO~Z, who seats it (A6, ruling
     32344). Then send the PHASE B GO.
   - Never to `0.7.0_AE_CloudOps~Z`.
2. **dell2 X2 readers (owner MI by CTO~Z 32430):** date sent to MSTR~Z at 06:09Z (msg 32451 thread): round 9, drain
   target 2026-10-12, conditional on (a) a CTO~O PRD addendum naming the readers' FWD (asked 06:10Z) and (b) OW-k-1's
   fixtures reaching site Z.
3. **J1 (FWD-11 thread):** Alyssa's run, booked through 0.0.0_AB_MSTR~Z, after MX-r-9's AC2 and AC3 pass.
4. **FWD-16:** the drive tick reads NFRA_OPLGTW serve dates; an entry turns SERVED the same day a v2.x dataset serves.

## Compiler Tools

- `missions-tree-index.py check`: 1 violation, then 0 on the trunk.
- `safe-commit.sh`: refused twice on index drift; the edit was reverted both times, and the shared tree stayed clean.
- `wk-provision.sh` x2.
- Worker reports read in full.

## Addendum 06:4xZ -- the ~28 re-seat finished at a clean point

- MX-d-7 is COMPLETE on its branch: merge 407ae3578f (box/sitez, conflict-free), then proof, flip and rows @9f51c11617.
  - d7.AC1-AC3 re-run PASS on the merged tree. proof-of-spec-check VALID; 3 of 3 surprise entries resolve.
  - The channel parses (254 rows). Z-W28-S3's text still reads ARMED; the merge disarmed it. Rule it at the drain.
- NOT drained, per "start no new work". The successor's first act: drain `wk-NFRA_MCPINDEX-28` with `safe-merge.sh` in a
  drain-* worktree (the channel union), then re-seat ~29 as above.
- The drive cron e822f7e3 was cancelled at 06:3xZ, so no tick starts work during the wind-down.
