# MDPF alignment report -- Andrew's 2026-10-13 voice memo vs what the MDPF projects cover, did and intend

For: Andrew Berman and the laptop CTO. Written 2026-10-13 ~17:0xZ, read-only. Source memo:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/MDPF_REVIEW_TRANSCRIPT.md`.
Name resolution: "Tainin"/"Cainan" = MDPF_CANON. Of the 7 project folders under `org/missions/D8/MDPF/`, CANON is the only one that
sounds like it. "white charts"/"Y-chart" = YCharts.
All times are UTC. Git `%cI` times (ET, -04:00) are converted to UTC.

**Conclusion.** The memo and the projects mostly agree on direction. Three things do not match:
1. **Nothing is working on YCharts as a data source.** It is also out of MDPF_DEMQUE's written scope.
2. **No mechanism links what MDPF_DEMQUE pulls to MDPF_SECCLASS classifying it.** Each PRD names the other only as a boundary.
3. **Of the projects Andrew thinks are "mostly done", only MDPF_HEALGAP is near closing** (5 of 6 outcomes realized). MDPF_STRATID
   needs one grading pass. MDPF_SECHIST is 1 of 9.

---

## 1. What Andrew asked for (ranked)

His explicit top three, in the order he gave them. Items 4-6 are the rest of the memo.

1. **MDPF_CANON keeps moving.** "making sure that Cainan proceeds"; "we need to establish where that's at, what we need to do to
   continue that process forwards".
2. **MDPF_DEMQUE and MDPF_SECCLASS are synchronized.** "a synchronized synergistic flow between the D-E-N-Q-U-E data-Colda polling and
   the SEC class security classification polling". This covers how securities arriving through the 17 qualified DEMQUE items are
   classified daily.
3. **Explore YCharts' backend as a data source.** "walk and translate white charts and their backend into a data-poled source ... free
   up some of that Bloomberg quota"; "do some network traffic recording to see what exactly lives here"; "It may be a separate
   project but we'll directly feed into the D-E-N-Q-U-E project."
4. **The DEMQUE standard card, and backfill moving.** He sees this as gating the rest: "a standard card ... which effectively covers a 1
   through 7, the various needs, depth, breadth"; "we need to make sure that backfill is moving conclusively across the board".
5. **SECCLASS: how securities arrive and get classified.** "seems like the largest one ... We need to establish how these are being
   classified, how they're coming in", using "the ETF classifier table in AWS".
6. **Close checks.** SECHIST: "understand if that's done if we can close that out". HEALGAP: "seems like it's most we've done".
   STRATID: "seems for the most part done".

## 2. Alignment table

Abbreviations in this table:
- **FWD** = an outcome in the project's PRD (product requirements document).
- **R** = graded REALIZED.
- **L8/L10** = the CVO's compile and the CTO's round analysis.

| project | Andrew's intent | chartered outcomes (PRD) | actually delivered / live (evidence) | coverage verdict | recommended move |
|---|---|---|---|---|---|
| **MDPF_CANON** (dell1, round 6) | It proceeds. Know where it is and what continues it. | 8 FWDs (PRD v2.11): FWD-1 freshness readable, FWD-2 per-firm reads, FWD-3 combined figure, FWD-4 publisher reads, FWD-5 all producers write to the MDPF home, FWD-6 per-firm runner, FWD-7 bronze in the common home, FWD-8 legacy copies gone. | **2/8 R** (FWD-1, FWD-7; round-5 analysis @6824a71f63). The FWD-3 Global min-firms fold was **deployed today, 14:05Z**, with no rollback (@eb50646475). Round 7 (frontier account counts) is drafted but not issued (@964a025a44, 14:13Z). FWD-2/4/6/8 wait on ADVI_FIRMBKTS' per-firm router flips. FWD-5 waits on the M10/M12 un-park. | **COVERED** (it is moving: 3 seats committed today) | **KEEP; REPOINT** to: (a) grade FWD-3 on the next 13:30Z fire; (b) issue round 7; (c) Andrew's word on the client-facing /portfolios PROD push; (d) the CTO fixes the stale register (see section 3). |
| **MDPF_DEMQUE** (dell1; execution partly on site Z) | The standard 7-field card for every item. Backfill moving. The 17 items qualified. Fed by YCharts later. | 9 FWDs (PRD v0.3), including FWD-1 (a new client security's history reaches the client page with no hand pull), FWD-3 (a backfill never stops a production pull), FWD-4 (requests priced before they run), FWD-5 (each security identified once), FWD-9 (pull order follows importance). Scope: "meters Bloomberg and Yahoo only". | **1/9 R** (FWD-4; FWD-3 APPLIED, not graded). See below the table. | **PARTLY**: the card is answered for 2 of the items; Bloomberg backfill is held by design | **KEEP; REPOINT** to: finish the card for every remaining item; get Andrew's P1 depth cut; move t34 to a live site Z lane; add a joint contract with SECCLASS. |
| **MDPF_SECCLASS** (dell1, round 24) | Show how arriving securities are classified, via the AWS classifier table. Synchronized with DEMQUE. | 17 FWDs (PRD v0.16): one table (DynamoDB `etf-classifications`) for every holdings surface. FWD-7: new securities in daily holdings get a row on a schedule. FWD-10: stocks newly entering through Opal or rival ETF trading. FWD-11: securities no source can place. | **FWD tally unknown**: no CTO analysis has printed a full board since round 9, and round 19 graded none REALIZED (dell1 box report). See below the table. | **PARTLY**: classification on arrival exists; no link to DEMQUE's intake | **KEEP; REPOINT** to: narrow to the Black Diamond (BD) thread this week (agrees with the dell1 CRO); require a 17-FWD board at the round-24 L10; add the DEMQUE joint contract. |
| **MDPF_SECHIST** (dell1, round 5) | Is it done? Can it close? | 9 FWDs (PRD v0.3): FWD-1 Positioning shows a new holding the next morning; FWD-2 full held-period performance; FWD-3/4 depth and completeness record; FWD-5 gaps fill themselves; FWD-6 one security per instrument; FWD-7 Bloomberg history spend inside one budget; FWD-8 same on every screen; FWD-9 money-market rule. | **1/9 R** (FWD-1, round 2). Last analysis is round 4 (2026-10-09, @167e971ee2). The 10-12 pull landed at 14:39:56Z today (@3423a70a32), so the morning Terminal blocker has cleared. 5 orders open: t12, t17, t18 carried; t21, t22 issued. | **NOT DONE**: its outcomes overlap DEMQUE (FWD-2, FWD-7) and SECCLASS (FWD-6, FWD-8) | **PARK** the seat (agrees with the dell1 CRO). At the next DEMQUE and SECCLASS L10s: **MERGE_INTO:MDPF_DEMQUE** for FWD-2/4/5/7, and SECCLASS for FWD-6/8. Andrew's call (section 6). |
| **MDPF_HEALGAP** (dell1, round 4) | Mostly done. | 6 FWDs (PRD v0.3): the COT Rebalancer bronze heals itself after a lapsed vendor login, with per-feed results, a one-act repair and an honest retry setting. | **5/6 R**: FWD-1, 2, 4 earlier; FWD-3 R today (an induced hole was repaired by the named act); FWD-5 regraded R in ADDENDUM 1 (round-3 analysis @f19cedfddc, 13:59Z). FWD-6 PARTIAL: 20 rows over 164 scheduled pulls, 7 exposed to manual action. Round 4 drained HG-t-16/t-17 today, and its deploy ledger opened at 15:13Z (@af1e5d0fa6). | **COVERED** (Andrew's view is right) | **KEEP to finish, then CLOSE this week** once FWD-6 is graded. |
| **MDPF_STRATID** (dell1, round 2) | Mostly done. | 7 FWDs (PRD v0.6), including FWD-1 PFDE strategy in Global; FWD-2 strategies outside models added; FWD-3 Muni as ALT; FWD-4 a new strategy needs no engineer; FWD-6 nothing double-counted; FWD-7 unidentified strategies visible. | **1/7 graded R** (FWD-1, round-1 ADDENDUM 1). FWD-2/6/7 MEASURED on the 10-12 fire but **ungraded**. The second consecutive clean Global emit was 16/16 (@67ff58b1d3, 13:37Z). All 12 orders complete. FWD-3 waits on call 203a (Muni sleeve membership). | **PARTLY** (built and served; grades owed) | **PARK** the seat now (agrees with the dell1 CRO). **CLOSE after one L8/L10 grading pass** that grades FWD-2/6/7 and dispositions FWD-3/4/5. |
| **YCharts as a data source** (no project) | Record the network traffic, map the endpoints, use it as a quota-free source feeding DEMQUE. | None. DEMQUE PRD BOUNDARY: "Not this scope: ... metering other vendors". DEMQUE brief line 125 lists YCharts as out of scope "except as a named source in O5's routing table". | Substantial prior art exists (section 3). The YCharts session is live: `ycharts_freshness` returned ok:true, HTTP 200, at 16:57Z today. | **NOT COVERED** | **NEW PROJECT** (small, read-only, CRO-briefed). It feeds DEMQUE through a PRD addendum that adds YCharts as a third metered vendor, and only once coverage is proven. |
| MDPF_GLOBAL (registry only, active) | Not named | The Global aggregate. The laptop CTO holds the never-widen pair for any change to its served output (STRATID project.json). | Live work runs through STRATID and CANON on dell1 (`org/projects/MDPF_GLOBAL.json` phase, 2026-10-08). | n/a | KEEP as the ownership record; no seat needed. |
| MDPF_TAXSMA (closed 2026-10-07) | Not named | n/a | Closed on Andrew's word. All 27 orders are terminal: 12 complete, 9 superseded, 6 cancelled. The 6 orphan orders from the pare-down record are already retired. | n/a | CLOSE (done) |

**MDPF_DEMQUE: what has been delivered (evidence).**
- The queue-qualification table lists **17 distinct request ids** (10 Bloomberg, 7 Yahoo), mapped to 5 surfaces: A production daily,
  B client history, E Opal ad-hoc, C product history, D research (`deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md`).
- Andrew's card has the 7 fields he described: who uses it, priority, history depth, field breadth, securities, schedule, budget.
  Only **2 cards are answered**, A2 (ETF pull) and A3/C1 (Rival Funds), plus the surface-level rules
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` @e961fee72f).
- **No new Bloomberg draw starts until the form is complete** (CTO msg 4892).
- Yahoo is moving: the standing extension drew 461,094 cells on 10-12.
- The CARD-A P1 depth cuts were priced at 15:47Z for Andrew's choice (@86abd8733d).
- FWD-1's last hop (the client page) is unconnected (sitez box report, round-8 ADDENDUM 4).

**MDPF_SECCLASS: how arriving securities are classified today (evidence).**
- Live thread: Investor Reporting Holdings and the BD Mix page (STATUS.md @168220e7d3).
- The FWD-7 scheduled classification is complete (TO-SC-k1, round 1).
- The FWD-10 producer was applied 10-08. Its last verification step is held until a scheduled new-security run plans US stocks
  (TO-DEPLOY-e57e61).
- The rolling re-derive was shipped at 06:22Z today; its acceptance read runs on tonight's 23:00Z fire.

## 3. Gaps no project owns or drives

1. **YCharts exploration: nobody owns it.** The prior art is large and closed, so this is a re-use job, not a fresh HAR study.
   - **YALP_MDSRC** closed complete on 2026-05-22 (`org/projects/YALP_MDSRC.json`). It:
     - reverse-engineered YCharts' internal JSON API from 3 recorded browser sessions (HAR files), finding about 40 endpoints, including
       `/charts/fund_data.json` for daily series, `/indices/table_data`, `/securities/securities_info` and `/search/suggest/main`
       (`docs/briefs/mdsrc-ycharts-internal-api-20260520.md`, `docs/briefs/mdsrc-a5-ycharts-har-endpoint-assessment-20260521.md`);
     - confirmed **72 of 76** indices, bond indices, commodities and ETFs replaceable, with 11.7-96.4 years of daily depth
       (`docs/briefs/mdsrc-wsa-ycharts-history-verification-20260521.md`);
     - matched Bloomberg to the cent on 42 of 71 index entries (`docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md`);
     - built a credential pipeline and a market-data pull. Both are still **deployed and dormant**: Lambda functions
       `ycharts-market-data-pull`, `ycharts-session-capture` and `ycharts-session-probe`, last modified 2026-05-22 (live
       `lambda list-functions` read, 16:57Z; whether a schedule fires them was not read).
   - **The gateway's `ycharts_*` tools** reuse the same endpoint contract and one shared session secret
     (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py` @2781aac326).
   - **Not measured anywhere:** YCharts coverage of **DEMQUE's actual items**. The largest open Bloomberg item, the CARD-A P1 slice, is
     370 Fixed Income and 227 Cash Equivalent CUSIP-level names out of 606 (`P1_DEPTH_CUTS_20261013.md`). Whether YCharts serves those
     is `unknown`. The inferred answer is weak coverage for bonds by CUSIP, but nobody has measured it.
   - **On "no quota":** the limit observed so far is **eviction of the one shared session** (403 seat evictions,
     `mdsrc-wsa-ycharts-history-verification-20260521.md`; "shared-account eviction",
     `docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md` line 97). It is not a call quota. A heavy backfill draw could
     evict the session the gateway and IRPT use.
   - **Direction tension:** on dell2, IRPT_YCDGEN's stated intent is "Opal stops calling YCharts" for reports (dell2 box report).
     That concerns the report generator, not market data, but both lean on the same shared session.
2. **DEMQUE <-> SECCLASS synchronization: nobody owns it.**
   - DEMQUE PRD BOUNDARY: "Relies on and does not own: MDPF_SECCLASS and the resolvers (identity)".
   - The SECCLASS PRD names DEMQUE 0 times (grep of `MDPF_SECCLASS_PRD.md`).
   - The queue form has 0 classification mentions.
   - Missing: one rule saying that a security entering through any of the 17 DEMQUE items gets its `etf-classifications` row on
     SECCLASS's scheduled path (FWD-7/10/11), and that DEMQUE's unresolved list (FWD-5) uses the same identity key.
   - Both projects sit under the same dell1 CTO, so one CONTRACTS row in each PRD closes this. A merge is not needed.
3. **The DEMQUE item on site Z has no live process.** TO-DQ-t34's site Z lane has had no process since ~12:2xZ, and its ledger
   `mdpf-demque-zq-t34-close` has been open since 10-11 (sitez box report). The two box reports name different owners: dell1 says the
   site Z CloudOps lane, sitez says the dell1 COO.
4. **The CANON register is stale.**
   - `project.json` `phase` still says "L5 at a COO lane -- none is seated" and `leads.coo` is null, while a COO has run rounds 1-6.
   - `blocking` holds M6 on "LGIC_NAMING-S7", but LGIC_NAMING is register-complete (pare-down record). Whether S7 was ever ruled:
     `unknown`.
   - Owner: the dell1 CTO.

## 4. Fast defined outcomes (close first)

1. **MDPF_HEALGAP closes: FWD-6 graded REALIZED.**
   - Missing: the round-4 deploy ledger closed (opened 15:13Z today), then the CVO's L8 and the dell1 CTO's L10 grading FWD-6 on the 7
     manual-exposed pulls (the HG-t-17 dispositions).
   - Owner: dell1 (the HEALGAP COO, then the dell1 CTO). No Andrew act.
2. **The DEMQUE card is complete for all 17 items, and Andrew picks the CARD-A P1 depth.**
   - Missing: the 7-field card for the remaining items (A1 models pull, A4 constituents, the B, C and D items), plus Andrew's choice of
     depth cut.
   - Bloomberg draws resume after both, inside his "2 weeks of BBG daily quota".
   - Owner: dell1 (the dell1 CTO keeps the form; the DEMQUE COO prices). Andrew answers.
3. **MDPF_CANON FWD-3 graded on the first served fold, and round 7 issued.**
   - Missing: the next 13:30Z fire's read of the deployed fold, the round-6 L10, and issuing round 7 (frontier counts).
   - Owner: dell1 (the CANON COO and the dell1 CTO).
   - Andrew acts afterwards: his word on the /portfolios PROD push.

## 5. Resourcing vs Andrew's ranking

Seats are from today's box reports (dell1 measured 12:55Z-13:04Z, sitez 14:44Z). Commits are the dell1 report's 7-day subject hits;
they include cross-mentions.

| rank | project | seats (box) | commits 7d | fit |
|---|---|---|---|---|
| 1 | MDPF_CANON | COO + CloudOps (dell1) | 180 | Moving. 5th of 6 by commits, but it has a deploy today. |
| 2 | DEMQUE <-> SECCLASS sync | none | 0 | **Unstaffed** |
| 3 | YCharts exploration | none | 0 | **Unstaffed** |
| 4 | MDPF_DEMQUE | COO (dell1); CloudOps lane (site Z, no process) | 315 | Staffed on dell1; site Z leg dead. |
| 5 | MDPF_SECCLASS | COO + CloudOps (dell1) | 697 | **The largest spend by far**: 90 worker slots, 283 surprise rows. |
| 6 | MDPF_HEALGAP | COO (dell1); laptop CloudOps read done | 243 | Right-sized to close. |
| 6 | MDPF_SECHIST | COO (dell1) | 217 | Over-staffed for 5 dated reads. |
| 6 | MDPF_STRATID | COO (dell1) | 174 | Over-staffed: 0 open orders. |

dell1 runs **6 MDPF COO seats under one CTO**; laptop, dell2 and sitez run none. The two items Andrew ranked 2 and 3 have zero seats.

Recommendation:
- Parking SECHIST and STRATID frees 2 dell1 COO seats. Closing HEALGAP frees a third.
- Add the sync as a cell in DEMQUE's and SECCLASS's next rounds. It needs no new seat.
- Start YCharts as an L1 brief by the laptop CRO. The laptop shed 19 projects today (pare-down record), and the AWS side is
  box-neutral. The dell1 CTO is the consumer at L2.

## 6. Questions only Andrew can answer

1. **CARD-A P1 depth: which cut?**
   - Options: A daily, 468,118 cells (175 days of quota); B month-ends before 2026-04-22 then daily, 27,526 (10 days); C flow dates
     plus month-ends, 30,858 (12 days); D C before 2026-04-22 then daily, 35,290 (13 days).
   - **Rec: D.** It fits your 2-week budget and keeps valuations on cash-flow dates for performance.
2. **YCharts: a separate project, or an addendum to DEMQUE?**
   - **Rec: a separate small project.** Step one: measure YCharts coverage of the 17 DEMQUE items (especially the CUSIP-level fixed
     income) by reusing the dormant YALP_MDSRC pull and the gateway client.
   - Step two: a DEMQUE PRD addendum adds YCharts as a metered vendor only where coverage is proven.
   - The shared-session eviction risk needs a pacing rule before any bulk draw.
3. **MDPF_SECHIST: close, park or merge?**
   - **Rec:** park now. At the next L10s, merge its backfill and budget outcomes into DEMQUE and its identity outcomes into SECCLASS;
     then close.
   - Its only distinct remaining item is the money-market rule reads (FWD-9).
4. **MDPF_STRATID call 203a: is the Muni sleeve counted under ALT Strategies at the COT firm and in Global?**
   - **Rec: yes.** This matches your 10-08 wording, "SMA strategies Tax and Muni under ALT Strategies", in the project record. That
     unblocks FWD-3 and lets the project close.
5. **Two client-facing portal PROD pushes wait on your word:** CANON's /portfolios additive band, and SECCLASS's BD Mix
   restated-history sentence.
   - **Rec:** approve CANON's once FWD-3 is graded on the fold. Approve SECCLASS's after tonight's acceptance read passes.

## 7. Method

**Read:**
- the transcript in full;
- 7 tree `project.json` files (6 active, MDPF_TAXSMA closed);
- 28 `org/projects/MDPF_*.json`: 7 active, 11 closed, 10 complete;
- the FWD headlines of 6 PRDs;
- order statuses over every `task-orders/*.md` in the 7 tree folders: 247 files, 13 non-terminal;
- the latest round analyses for CANON (r5), SECHIST (r4), HEALGAP (r3) and STRATID (r1);
- SECCLASS STATUS.md;
- the DEMQUE qualification table, depth-cut file and the CTO's queue form, plus the backfill-law record;
- 6 recent commits per project (`git log --grep`, CLOUD + box/laptop);
- from `C:\Users\AndrewBerman\Desktop\today_report`: the four box reports (dell1 MDPF blocks in full, sitez DEMQUE, laptop HEALGAP,
  dell2 IRPT_YCDGEN), `AGGREGATE_4_of_4_20261013.txt` and the laptop pare-down record;
- YCharts prior art: folder-scoped Grep, 223 files under `docs/` and 25 under `opal-gateway/`, with 5 briefs read in part;
- 2 live reads: `ycharts_freshness`, and a `lambda list-functions` filtered to names containing "ycharts" (4 functions).

**Where this report agrees and disagrees with the box reports:**
- **Agrees** with dell1's recommendations: KEEP CANON, DEMQUE and SECCLASS; PARK SECHIST and STRATID.
- **Adds** CLOSE-after-grading for STRATID and MERGE for SECHIST.
- **HEALGAP:** dell1 and laptop show 3/6 and unknown. This report's **5/6** comes from the round-3 analysis and ADDENDUM 1 written at
  13:59Z, after the reports were read.
- **SECHIST blocker:** dell1 reports the pull blocked on the Terminal sign-in. This is superseded: the pull landed at 14:39:56Z
  (@3423a70a32).
- **CANON:** dell1 shows the fold deploy pending. It was deployed at 14:05Z.
- **DEMQUE open orders:** dell1 shows 1. There are 3 now; t45 and t46 were cut at 15:37Z.
- **DEMQUE appears on two boxes in the aggregate** (lines 13 and 59). **dell1 is true:** placement DELL1, its COO and CTO are on dell1,
  and sitez's own block says "Box of record is dell1". Site Z is an execution host: the drawer task at 14:00Z, the Bloomberg ledger
  upload at 12:30Z, and the t34 lane. The aggregate's 66 projects therefore double-count DEMQUE, and also AMGT_HARVST.

**Not read:**
- broker liveness of each seat (taken from the box reports);
- the SECCLASS per-FWD grades (no board exists since round 9);
- whether the dormant YCharts Lambdas have a schedule;
- `etf-classifications`' current row count (10,834 per the DEMQUE PRD, measured 10-08);
- the remaining SECHIST orders' content;
- holder of call 203a.
