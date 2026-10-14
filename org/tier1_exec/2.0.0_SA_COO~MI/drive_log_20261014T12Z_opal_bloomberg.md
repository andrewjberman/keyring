# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX round 12: MX-r-13 waits on the OPLGTW releases; the project continues to round 13 -- 2026-10-14 09:3xZ-12:1xZ (host opal_bloomberg)

**archetype:** dated WAITs, then a relaunch hand-off (site Z joins the model policy)

## Ticks and events

| time | act |
|---|---|
| 09:3xZ-10:3xZ | Dated WAIT ticks (owner 2.0.0_SA_COO~O). `/next-calls --drive`: 0 calls, 0 FREE |
| 11:3xZ | WAIT on owed ledger `nfra-oplgtw-gateway-release-r30` (0.7.0_AE_CloudOps~Z, in-window; manifest 90967e39ba), then OG-ap-17 |
| 11:5xZ | 1.0.0_SA_CTO~Z msg 34027: NFRA_MCPINDEX does NOT park after round 12. Andrew orders an opal-data-harvest tool set (XB-dc98): company search by ticker/name/CUSIP/ISIN across published/platinum, gold and silver, graded on Lauren's Claude app on the gateway MCP. 4.0.0_SA_CRO~Z assesses, then the CTO's PRD addendum, then this seat cuts round 13. Round 12 stands as cut |
| 12:0xZ | 1.0.0_SA_CTO~Z msg 34033: site Z workers spawn with model haiku, effort high (MP-20261010 @b03d97ac20) |
| 12:1xZ | 0.0.0_AB_MSTR~Z msg 34037: relaunch on Sonnet 5.5 at a safe point. This seat replies READY after this commit |

Tick row: `NFRA_MCPINDEX | L7 | 12 | TOs 1/2 | cells 2/2 | thread none | WAIT: MX-r-13 behind OG-ap-14 (r30) and OG-ap-17`.

## Hand-off for the relaunched seat

- **Re-arm** `/canonical-drive NFRA_MCPINDEX` at 60m (Andrew-direct via msg 33743, LIVE_ARMS row on CLOUD @81ef5aa2db). The session cron
  dies with this session. Do NOT disarm when round 12 closes: the project continues to round 13.
- **MX-r-13** (`task-orders/NFRA_MCPINDEX.TO-MX-r-13.depth-every-tool-release.md`, A1 @45e6f53327) runs when 2.0.0_SA_COO~O
  sends the live deployed_commit at OG-ap-17's close: A2 GO for PHASE A to 0.7.0_AE_CloudOps~MI (cut on the live ref in a NEW
  deploy tree, `infra/logic/registry` in the cone, the two blobs at @8c74d1d902, ANNOUNCE with four equal censuses); measure
  the cut; never-widen ask (COO half signed, CTO half to 1.0.0_SA_CTO~Z); PHASE B GO; on close tell COO~O the deployed_commit
  for OG-hv-2; re-run r13.AC1-AC3 (`deliverables/2.0.0_SA_COO~MI/round12/checks/`); real run of `opal_discover`; flip
  complete; `round-close-check.py --round 12`; L8 packet to 3.0.0_SA_CVO~Z.
- **Round 13** is cut from the CTO's addendum after 4.0.0_SA_CRO~Z's assessment. Workers spawn on haiku, effort high.
- **MX-s-19** (round 7) stays open: s19.AC2 is a dated read 2026-10-19/20 by 0.7.0_AE_CloudOps~MI (ledger
  `nfra-mcpindex-r7-bd-doc-retire`, in-window). That lane is not at a safe point for relaunch.
- Left for MSTR GC: worktree `wk-mcpindex-r12-35` (uncommitted LOCK-RECLAIM line in the override audit log); deploy trees
  `C:/tmp/mx-dep-r11`, `mx-dep-r12`, `mx-dep-r12v2`.

## Compiler Tools

- A relaunch hand-off belongs in a committed log, not only in the session. The cron, the plan and the queued acts all die
  with the context; the log is what the next session reads.
