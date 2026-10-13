# NFRA_DEVPLN -- portal settlement list (cell DP-s-1)

- Measured refs (read-only, no fetch): origin/DEV `f6ef1d25`, origin/PROD `15c97549`, written 2026-10-13T18:55:11Z (UTC).
- Tool: `.tools/portal-settlement-list.py` on the portal repo `portal/`. Every git call is a read.
- Headline: DEV is ahead of PROD by 201 commits; PROD is ahead of DEV by 33 commits; 229 files differ DEV-not-PROD; 9 remote branches hold work not on DEV.
- The class column is the unsure rule (an input). Andrew rules each group once: approve forward, hold on a branch, or drop.

## 1. DEV-not-PROD groups (git diff --name-only origin/PROD...origin/DEV)

| group | class | files changed | commits touching (origin/PROD..origin/DEV) | top three committers (commits) |
|---|---|---|---|---|
| InvestorReporting | client-facing | 143 | 105 | 2.0.0_SA_COO~D2 (20); 0.9.0_WK_DSGN_IRPTV1~49 (11); 0.9.0_WK_DSGN_IRPTV1~53 (10) |
| SecurityAnalysis | opal-internal | 51 | 40 | 0.9.0_WK_AMGT_CORPUS~2 (10); 0.9.0_WK_DSGN_AMGTV1~142 (3); 0.9.0_WK_DSGN_AMGTV1~135 (2) |
| TicketCenter | client-facing | 19 | 27 | 0.9.0_WK_IRPT_ANLREQ~51 (13); 0.9.0_WK_IRPT_ANLREQ~11 (3); 0.9.0_WK_TCKT_VNEXT~11 (3) |
| AdvisorIntelligence | client-facing | 4 | 7 | 0.9.0_WK_ADVI_BILLING~2 (2); 2.0.0_SA_COO~B2 (2); 0.9.0_WK_MDPF_SECCLASS~84 (1) |
| api | client-facing | 3 | 8 | 0.9.0_WK_ADVI_BILLING~2 (2); 0.9.0_WK_IRPT_ANLREQ~51 (2); 0.9.0_WK_DSGN_IRPTV1~49 (1) |
| firmAccess | client-facing | 1 | 1 | 0.9.0_WK_NFRA_CTLPLN~70 (1) |
| other | client-facing | 8 | 7 | 0.9.0_WK_DSGN_IRPTV1~49 (2); 0.9.0_WK_AMGT_RESAPP~349 (1); 0.9.0_WK_DSGN_IRPTV1~59 (1) |

## 2. PROD-only commits (git rev-list origin/DEV..origin/PROD): 33

| # | sha | author | date | subject | same patch on DEV (git cherry) |
|---|---|---|---|---|---|
| 1 | 15c97549 | 0.9.0_WK_NFRA_CTLPLN~70 | 2026-10-12T06:45:41-04:00 | gen(NFRA_CTLPLN CT-w-8, 0.9.0_WK_NFRA_CTLPLN~70): FIRM_ALLOWED_PATHS is the generated block of firm_pages.json with the hand-kept comments carried as notes (CTO ruling msg 108504) | yes (DEV carries the same patch) |
| 2 | 37aa1247 | 0.9.0_WK_DSGN_AMGTV1~142 | 2026-10-09T12:30:39-04:00 | AV-zzs-1 item 5: Peers subject cell withheld by item 4 carries the tile's own reason as title; one exported copy of the words | yes (DEV carries the same patch) |
| 3 | e88ced18 | 0.9.0_WK_DSGN_AMGTV1~142 | 2026-10-09T12:20:34-04:00 | AV-zzs-1 item 4: subject row passes header unit and basis; withholds as the tile does | yes (DEV carries the same patch) |
| 4 | 44d2d022 | 0.9.0_WK_DSGN_AMGTV1~142 | 2026-10-09T12:00:45-04:00 | AV-zzs-1: subject row Price/Mkt Cap/EV print the header tile figure or -- | yes (DEV carries the same patch) |
| 5 | a97e5dff | 0.9.0_WK_DSGN_AMGTV1~141 | 2026-10-09T11:24:49-04:00 | memberTicker: served exchange ticker unless empty, numeric or SEDOL-shaped (AV-zzr-1 amendment 2) | yes (DEV carries the same patch) |
| 6 | 11db6620 | 0.9.0_WK_DSGN_AMGTV1~141 | 2026-10-09T10:55:20-04:00 | AV-zzr-1: peer table reads clean -- readable tickers, honest money headings, own-currency cells, one price/cap format across tile and table; harness DataTooltip stubs | yes (DEV carries the same patch) |
| 7 | 18364342 | 0.9.0_WK_DSGN_AMGTV1~140 | 2026-10-09T08:35:10-04:00 | AV-zzq-1: strip a repeated leading heading label from the served description | yes (DEV carries the same patch) |
| 8 | c6c1eb2a | 0.9.0_WK_DSGN_AMGTV1~138 | 2026-10-09T08:08:03-04:00 | AV-zzp-1: thesis window prints served company description; drafted lines headed From the filing | yes (DEV carries the same patch) |
| 9 | f8ec0937 | 0.9.0_WK_DSGN_AMGTV1~135 | 2026-10-09T07:33:07-04:00 | AV-zzo-1 amendment 1: whole sentence is one inline press button, figure spans are underlined spans; drafting harness unwrap re-anchored | yes (DEV carries the same patch) |
| 10 | 74b9e941 | 0.9.0_WK_DSGN_AMGTV1~136 | 2026-10-09T07:26:57-04:00 | TimelinePanel: draw every event label in one band (AV-zzo-2 item 4) | yes (DEV carries the same patch) |
| 11 | 5bc7ff8a | 0.9.0_WK_DSGN_AMGTV1~135 | 2026-10-09T07:08:08-04:00 | AV-zzo-1: thesis window says nothing false about the description; a figure opens its passage | yes (DEV carries the same patch) |
| 12 | 5505a662 | 0.9.0_WK_DSGN_AMGTV1~137 | 2026-10-09T07:04:58-04:00 | AV-zzo-3: a name matching several companies shows the served candidates | yes (DEV carries the same patch) |
| 13 | 092aa39b | 0.9.0_WK_DSGN_AMGTV1~136 | 2026-10-09T07:04:42-04:00 | AV-zzo-2: event labels laid out on 3 rows with no overlap; 11px | yes (DEV carries the same patch) |
| 14 | 2e41c008 | 0.9.0_WK_DSGN_AMGTV1~134 | 2026-10-09T06:30:09-04:00 | AV-zzn-1: price line joined, axis and legend say what it is, news types to current contract | yes (DEV carries the same patch) |
| 15 | 90db1e84 | 0.9.0_WK_DSGN_AMGTV1~131 | 2026-10-09T05:43:44-04:00 | AV-zzm-1: Peers fold says why an UNSTATED Average is blank; harness arms; caption arm renamed | yes (DEV carries the same patch) |
| 16 | b7ea9a21 | 0.9.0_WK_DSGN_AMGTV1~133 | 2026-10-09T05:40:11-04:00 | AV-zzm-3: news list ranked by served mentions, top band and feed together | yes (DEV carries the same patch) |
| 17 | 1baceb6b | 0.9.0_WK_DSGN_AMGTV1~132 | 2026-10-09T05:41:33-04:00 | AV-zzm-2: the timeline spine draws the served price line (right-hand axis, gap on a missing day), or says once there is none | yes (DEV carries the same patch) |
| 18 | fa5ba2af | 0.9.0_WK_DSGN_AMGTV1~130 | 2026-10-09T04:05:13-04:00 | DSGN_AMGTV1 round 60, AV-zzl-1: the round-59 repairs batched, battery re-anchored | yes (DEV carries the same patch) |
| 19 | 6e278b7b | 2.0.0_SA_COO~D1 | 2026-10-09T03:04:23-04:00 | merge-hookups(DSGN_AMGTV1 round 59, 2.0.0_SA_COO~D1): NewsTab passes the served top_band items to the one news surface; the print title reads the display name and ticker | yes (DEV carries the same patch) |
| 20 | a6366f9c | 0.9.0_WK_DSGN_AMGTV1~129 | 2026-10-09T02:53:18-04:00 | feat(SecurityAnalysis): Model opens on a summary, tiles stay quiet, print names the company (DSGN_AMGTV1 AV-zzk-6, SAW-17/19/22) | yes (DEV carries the same patch) |
| 21 | 34f7eb0a | 0.9.0_WK_DSGN_AMGTV1~126 | 2026-10-09T02:53:30-04:00 | AV-zzk-3: tabs in the first screen, identity once, plumbing out of the face (SAW-11, SAW-12, SAW-14, SAW-20, SAW-21) | yes (DEV carries the same patch) |
| 22 | b0fb5f57 | 0.9.0_WK_DSGN_AMGTV1~127 | 2026-10-09T02:51:08-04:00 | AV-zzk-4: Thesis and Posture say each absence once; segment notes fold (SAW-10, SAW-11, SAW-18, SAW-21) | yes (DEV carries the same patch) |
| 23 | bc1cea11 | 0.9.0_WK_DSGN_AMGTV1~124 | 2026-10-09T02:51:46-04:00 | feat(SecurityAnalysis): spine says what moved the name, not how the collector ran (DSGN_AMGTV1.TO-AV-zzk-1, SAW-01/02/03/04/08) | yes (DEV carries the same patch) |
| 24 | a2f2b132 | 0.9.0_WK_DSGN_AMGTV1~128 | 2026-10-09T02:49:27-04:00 | AV-zzk-5: Exec and Peers say each absence once | yes (DEV carries the same patch) |
| 25 | 1a7cc602 | 0.9.0_WK_DSGN_AMGTV1~125 | 2026-10-09T02:48:08-04:00 | AV-zzk-2: one news surface, each headline once (HeaderBrief), TopBand draws no news card | yes (DEV carries the same patch) |
| 26 | 886b4e82 | 0.9.0_WK_DSGN_AMGTV1~123 | 2026-10-09T01:32:26-04:00 | AV-zzj-1: filing panel does not say a breakdown is absent beside a drawn segment table | yes (DEV carries the same patch) |
| 27 | bf780f94 | 0.0.0_AB_MSTR~DELL1 | 2026-10-09T01:35:34-04:00 | merge DEV->PROD: DSGN_AMGTV1 r53-r57 + AMGT_CORPUS r40 + IRPT_BCKEND/IRPT_YCDGEN/TCKT_VNEXT @ DEV 2d42e9b733fc0f589aadc0e6d367c2f320abe5e9. Base f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae. Rollback: f73f9ab0eb4f7c9f28171fa8e8e7d3ea5d21ffae. Pair: CTO half b44ccdfe2c + COO half 260524dfec. Changed pages, all internal (requireInternal): SecurityAnalysis, Freshness, InvestorReporting, TicketCenter. Authored 0.0.0_AB_MSTR~DELL1. | n/a (merge commit; git cherry omits merges) |
| 28 | f73f9ab0 | 0.0.0_AB_MSTR | 2026-10-08T14:44:29-04:00 | merge DEV->PROD: v2.1.204 -- Security Analysis DSGN_AMGTV1 rounds 46-52 (one statement of inputs, the coverage sentence, officers as served, the research team's pack) + MDPF_SECCLASS + IRPT_YCDGEN/CUSTDY/BCKEND + TCKT_VNEXT; pinned to DEV dbeb6764; Andrew 'recs approved' 2026-10-08; pair COO @454754ec7d CTO @b30f3952c6 | n/a (merge commit; git cherry omits merges) |
| 29 | b06863fe | 2.0.0_SA_COO~D | 2026-10-07T01:56:45-04:00 | merge DEV->PROD: v2.1.203 -- Security Analysis DSGN_AMGTV1 round 45 (the company in one line under the name card; the day's news band; where each input came from and when it last ran; the re-run button removed; one filing passage per press, table passages with their column labels, readable axis ticks; one heading per business segment) + AMGT_RESAPP /freshness round 77 (served stale flag and keyed date, owner line) + /freshness limited to Dev users @ DEV 8ddfe409948cc79bb45e5ac27a8136264ce8c9d4. Base ab3191d084be9fb8d570cf71ec6e39b2a11ade24. Rollback: ab3191d084be9fb8d570cf71ec6e39b2a11ade24. Authored 2.0.0_SA_COO~D on Andrew-direct 2026-10-07 ~05:5xZ promote it (/prod-deploy). | n/a (merge commit; git cherry omits merges) |
| 30 | ab3191d0 | 2.0.0_SA_COO~D | 2026-10-06T21:24:11-04:00 | merge DEV->PROD: v2.1.202 -- benchmark heat map ETF-mode Since Inception annualized like the model row (1814185b) + Attribution funnelled Equity holdings sort and colour (61a8dd5a) + auth same-origin by default (64d2503e) + AMGT_CORPUS round 39 Security Analysis header currency and Model sheet label wrap (f8d92450) @ DEV 34803ef6d8d3760506c484da1453e77d92a68122. Base f8c947591a3fe7ddfdb37057b760338356efa18f. Rollback: f8c947591a3fe7ddfdb37057b760338356efa18f. Authored 2.0.0_SA_COO~D on Andrew-direct 2026-10-07 ~01:0xZ go route it, relayed MSTR~Z msg 30488 (/prod-deploy). | n/a (merge commit; git cherry omits merges) |
| 31 | f8c94759 | 2.0.0_SA_COO~D | 2026-10-06T16:54:23-04:00 | merge DEV->PROD: v2.1.201 -- Security Analysis DSGN_AMGTV1 rounds 43+44 (no bare number as a peer ticker, plain company names, a driver-chart point opens its served filing passage, business segments on the Thesis tab) + AMGT_RESAPP /freshness page + DSGN_REBRND colour changes reverted (project closed) @ DEV 6b4e89a8744e811ab2b97e1c29d196220d2bdd9d. Base ce6f0721be8df364a818e7d76c83607850d2b5fd. Rollback: ce6f0721be8df364a818e7d76c83607850d2b5fd. Authored 2.0.0_SA_COO~D on Andrew-direct 2026-10-06 ~18:1xZ recs approved (/prod-deploy). | n/a (merge commit; git cherry omits merges) |
| 32 | ce6f0721 | 2.0.0_SA_COO~D | 2026-10-05T16:12:51-04:00 | merge DEV->PROD: v2.1.200 -- Security Analysis redesign DSGN_AMGTV1 rounds 34-42 (open to every Opal employee via requireInternal; header key figures with served reasons and full-value tooltips; news timeline markers, footers and end line; designed panel states) + AMGT_CORPUS Model sheet rows @ DEV 1135984d7f6a05cddfc198249ca8b84cd3f138f1. Base c69b474716f21d492daafd6a8024d1a5f742d628. Rollback: c69b474716f21d492daafd6a8024d1a5f742d628. Authored 2.0.0_SA_COO~D on Andrew-direct 2026-10-05 ~20:0xZ (/prod-deploy). | n/a (merge commit; git cherry omits merges) |
| 33 | c69b4747 | Andrew Berman | 2026-10-04T16:19:36-04:00 | merge DEV->PROD: v2.1.199 -- DSGN_REBRND W3-S5 state fixes, StatusPanel (CTO batch 238), DSGN_IRPTV1 fixes @ DEV c7bc52c8a422de45d674bd8dd6bff1bed745dd78. Base dbd29c63200dd5f8c44de9cbc56447a25b402a8e. Rollback: dbd29c63200dd5f8c44de9cbc56447a25b402a8e. Authored 0.0.0_AB_MSTR on Andrew-direct 2026-10-04 ~20:0xZ. | n/a (merge commit; git cherry omits merges) |

## 3. Remote branches with work not on DEV (ahead of origin/DEV; excludes DEV, PROD, HEAD): 9

| branch | ahead | cherry + (patch not on DEV) | cherry - (already on DEV) | merge commits (cherry omits) | tip sha | tip date | owner (tip author) |
|---|---|---|---|---|---|---|---|
| wk-dsgn-irptv1-r25-61-prodcut | 34 | 2 | 25 | 7 | fc876722 | 2026-10-11T14:16:13-04:00 | 0.9.0_WK_DSGN_IRPTV1~61 |
| cand-dell1-secclass-e53-r9 | 4 | 0 | 4 | 0 | 4cc41317 | 2026-10-07T08:01:38-04:00 | 0.9.0_WK_MDPF_SECCLASS~37 |
| irpt-dev-candidate-3-20260924 | 3 | 2 | 1 | 0 | 7897f891 | 2026-09-24T03:04:43-04:00 | 2.0.0_SA_COO~P |
| cand-dell1-secclass-e59-r10 | 2 | 0 | 2 | 0 | c0ec00e6 | 2026-10-07T10:14:11-04:00 | 2.0.0_SA_COO~M1 |
| q/dell2/wk-IRPT_BCKEND-167-portal/r1 | 2 | 0 | 2 | 0 | 63b9382a | 2026-10-07T19:19:45-04:00 | 0.9.0_WK_IRPT_BCKEND~167 |
| sitez/merge-trial-20260915 | 2 | 0 | 0 | 2 | 1a1e13ef | 2026-09-15T05:24:31-04:00 | 0.0.0_AB_MSTR~Z |
| irpt-dev-candidate-7-20260924 | 1 | 0 | 1 | 0 | 814d7473 | 2026-09-24T08:58:01-04:00 | 2.0.0_SA_COO~P |
| irpt-opal-scope-p-portal-20260923 | 1 | 1 | 0 | 0 | e0531491 | 2026-09-23T11:12:24-04:00 | 2.0.0_SA_COO~P |
| wk-IRPT_ANLREQ-51-portal-r4 | 1 | 1 | 0 | 0 | 890f1d0f | 2026-10-11T07:05:45-04:00 | 0.9.0_WK_IRPT_ANLREQ~51 |

## 4. Machine lines

```text
group InvestorReporting class=client-facing files=143 commits=105
group SecurityAnalysis class=opal-internal files=51 commits=40
group TicketCenter class=client-facing files=19 commits=27
group AdvisorIntelligence class=client-facing files=4 commits=7
group api class=client-facing files=3 commits=8
group firmAccess class=client-facing files=1 commits=1
group other class=client-facing files=8 commits=7
```

SETTLEMENT-LIST dev_ahead=201 prod_ahead=33 groups=6 files_total=229 files_other=8 branches=9
