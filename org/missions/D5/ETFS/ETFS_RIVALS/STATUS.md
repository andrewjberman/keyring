# ETFS_RIVALS (rivalfunds) -- status (FULL; round 6 DEPLOYED 2026-10-02 ~19:5xZ; L9 at the CVO)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL on Andrew's word ("yes you can move to /canonical-drive for the remainder";
record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261002_141xZ_CANONICAL_DRIVE_MAX_PARALLEL_RELAYED.md`).
Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team:
- reviewer `3.0.0_SA_CVO~RV`: grades 1-14 PASS; round-6 L8 read 20:03Z;
- open calls `4.0.0_SA_CRO~RV`: CALLs 1-13 ruled; the layout pass and GICS fixes 1-3 are on Andrew's word.

As of 2026-10-02T20:1xZ.

## Pins

| What | Value |
|---|---|
| Deployed artifact pin | CLOUD **eb6e9f04ff** in the five rivalfunds Lambdas (round 6 + the census repair fc022275b5 + CRO~RV's layout 31d2375993); the daily Lambda carries the AI gate |
| Deploy record | NEVER-2 `etfs-rivalfunds-round6` CLOSED 7/7 (2e1558edc9); pair COO 03036ef58b / CTO 15f3366309; post-act `deliverables/2.0.0_SA_COO~RV/round6/postact_round6_deploy.json` |
| Served page 2026-10-02 | batch rv-publish-1002r6: 13/13 funds, 213 trades, AI 12/12 (22 PASS / 2 FAIL), 1,833,385 B (cap 2,097,152) |
| AI accounts | 2026-09-30 run 20261002T195217Z-ai (the scheduled stage, the first): PASS 24/24, a1-chain/5; 2026-10-01 and 2026-10-02 the seat runs |
| AI secret | `rivalfunds/openai-api-key` (a labelled COPY of `openai-api-key`; a dedicated OpenAI project key is Andrew's act) |
| Round 6 | 14/14 orders complete (issuance 1e8515aa01); worktrees `/c/tmp/wk-riv6-1..6` (removal is human-confirmed) |

## Next proof

1. **L9:** 3.0.0_SA_CVO~RV grades J1 of ap-1, r-6, ui-2, ui-3, ui-4 and ui-5 on the served pages. Then the L10 slug goes to
   the CTO, and the CTO answers with the round-6 analysis.
2. **2026-10-05 07:00 / 08:03 ET:** the vehicle's first `get(id(), name())` capture and DVD_CRNCY request (proved live on
   9 funds). Read the morning markers and silver; names reach the page.
3. **2026-10-05 09:00 ET:** the first unattended scheduled AI account; read its run status in the manifest.

## Open findings (rows or calls, owner named)

- IDVZ (I-4): the TrueShares page layout changed on 10-01, so the net-assets Lambda scraper fails and no IDVZ holdings land.
  The source-policy switch to bloomberg_primary is Andrew's or CRO~RV's call.
- BIDD, CGIC and SCHY (I-4): Bloomberg returns T-2 reports at 07:10 ET; still 09-30 at 12:47 ET 10-02.
- Census: 33 GICS rows read "missing" though the rankings classify them (ETFT 9, PCLG 11, TSEL 9, WCMG 4): round 7.
- Name pick: a same-date tie in identity_maps (57 + 17 cells differ between the Lambda and a local run): round 7.
- G5: the three x-1 exits price at the next G5 build.
- Page size: 1.83 MB; holding dialogs drop above 1.95 MB.

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. Workers never call a vendor, write S3 or deploy.
