# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-09 03:3xZ -> 05:2xZ (host opal_bloomberg)

**archetype:** COORDINATE

## What moved

- **Andrew-direct ~03:2xZ** (record @5716c7a83d): "there is a lot of indexing work to be done". My NOTHING-LEFT read was
  not his view.
  - Alyssa's two PRD-004 briefs were located on SharePoint `Shared` and read, then mapped to FWDs: input map
    @3ff7a2a654.
  - Live tool reads: map + row Z-S85 @280fd3c814. ycharts_time_series 403; snapshot keyed `None`; model benchmarks
    answer W6.
  - CTO~O asked CRO~Z for the midstream brief (@3455b1783a, 29 entries). PRD v0.7 landed @b06af7c0d2 and was ADMITTED
    @3c7ff0684b (CVO~Z signed).
- **MX-s-19 A6 @d0d5e64d50:** 1.0.0_SA_CTO~Z ruled (32344) that `0.7.0_AE_CloudOps~Z` keeps NFRA_OPLGTW. MX-s-19 goes to
  a fresh site-Z CloudOps lane when it ungates.
- **Round-8 L5:** @d4d7794e7f, then A1 @19248a86b8, then A2 @7a37c5b906.
  - DEFECT (mine): A1 serialized the chain on a wrong premise. I counted the PROSE vintage, not the structured
    `vintage_field` that 37 of 37 rows already carry. A2 withdrew it.
  - The uncommitted decomp briefly held MSTR~Z's box-sync (msg 32371). Committed and reported.
- **Round-8 L6 ISSUED @b0d8580aab:** MX-d-7, MX-c-6, MX-d-8, MX-r-9; 2 of 2 chains.
  - All 11 checks behave as expected at base. 10 FAIL; d7.AC3 PASSES as the regression control.
  - The r9 checks were read live on the SERVED host.
  - An instrument defect was caught by a control: c6_tools.py first saw 7 tools. It now reads `TOOL_CLASSES`: 70
    tools, and a planted fake is caught.
- **project.json NOT updated.** The missions-tree check refuses on an unrelated INDEX-DRIFT (`IRPT_ANLREQ` index `PRD`
  vs tree `EXECUTING`), routed to 0.0.0_AB_MSTR~Z. My uncommitted edit was reverted, so the shared tree is clean.
- **SPAWNED 05:1xZ:** `0.9.0_WK_NFRA_MCPINDEX~28` (MX-d-7) in `wk-mcpindex-r8-28` and `~29` (MX-c-6) in
  `wk-mcpindex-r8-29`.
- **Replies:** cron id and cadence reported to MSTR~Z (32311) and CTO~Z (32389). Law edits 32299 and 32365 acked.

## Open

- **~28 and ~29 running.** On their reports: grade, drain, then continue ~28 with MX-d-8.
- **MX-s-19:** s19.PRE.sh after 03:00Z on 2026-10-13, then a fresh CloudOps lane (A6).
- **FWD-16:** this lane's tick reads NFRA_OPLGTW serve dates.
- **J1:** Alyssa's thread run, booked through 0.0.0_AB_MSTR~Z after MX-r-9's AC2 and AC3.

## Compiler Tools

- `prd-signoff.py status`: STALE, then ADMITTED.
- `comp-surprise --armed`: 14.
- `.tools/wk-provision.sh` x2.
- `to-pipeline-gate`: passed on the issuance.
- `missions-tree-check`: refused once, on the unrelated drift.
- Gateway reads through MCP: ycharts x3, `mdpf_get_model_benchmarks`, SharePoint x4.
- SSM host probes: r9.AC2 and r9.AC3 at base.
