# PROJECT CENSUS -- every project touched in the last two weeks, which box it is on, and what state it is in

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-06 ~18:5xZ (2:5x PM Eastern). Read-only.
- **Order:** Andrew-direct ~18:3xZ, verbatim with his full voice transcript in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`.
  This is his "Document 1". Document 2, the plan, is `docs/briefs/four-box-acceleration-plan-20261006.md`.
- **Window:** 2026-09-22 to 2026-10-06 (two weeks).
- **Sources, each read today:**
  1. every `project.json` in `org/missions/` (39 rows) with its PRD header and task-order statuses;
  2. `.tools/registry-check.py -all` (71 rows, including the older flat registry);
  3. `.tools/placement-check.py`, the control plane's own placement read (NFRA_CTLPLN FWD-7);
  4. the git history of the shared trunk `CLOUD`, local and remote (`origin/CLOUD` = `66b1b42a71`, which carries site Z's
     work up to its last push);
  5. the laptop broker's live-agent list at ~18:4xZ.
- **The one blind spot, stated first:** site Z's last commit on the shared trunk is 2026-10-05 23:58 local. Its work since
  then (it rebooted ~13:5xZ today and is working again; relays show walks at 17:5xZ and 18:4xZ) is on site Z's disk
  only and is not counted here. Site Z's live agents cannot be listed from the laptop; they are inferred from commits.

---

## 1. Summary

| | laptop | site Z | total |
|---|---|---|---|
| Live projects placed by the control plane's read | 17 | 14 | 31 |
| Projects with commits in the two-week window (mission tree) | 21 | 11 | 32 |
| Projects in active execution right now (task orders open or a round running) | 7 | 7 | 14 |
| Execution (COO) lanes with commits in the last 24 hours | 4 (C, M, P, Y) + D until held | 6 (Z, X, RV, H, O, D) | 10 to 11 |
| Cross-box write overlaps the placement read finds | -- | -- | 26 (mostly the shared deploy ledgers) |

**Reading:** the laptop is carrying four or five execution lanes plus every planning seat. Its standing limit is three COO
sessions. Site Z carries six execution lanes plus its own planning seats. Neither box has room for the three quarterly
goals; the Dells are the room.

---

## 2. Active agents

### Laptop (broker list, ~18:4xZ)

| Seat | What it is doing now |
|---|---|
| `0.0.0_AB_MSTR` | fabric manager; merged and pushed the trunk at 16:2xZ (`66b1b42a71`) |
| `1.0.0_SA_CTO` | planning: PRDs for MDPF_SECCLASS, IRPT_YCDGEN, IRPT_BCKEND, NFRA_CTLPLN, ADVI_COTBKF |
| `3.0.0_SA_CVO` | grading: CTLPLN round 1 graded PASS; PRD sign-offs |
| `4.0.0_SA_CRO` | this seat: briefs |
| `4.0.0_SA_CRO~H`, `~P`, `~X` | research lanes: household-count research done; the DIVZ/IDVZ (TrueShares) fix; one starting |
| `2.0.0_SA_COO~C` | ADVI_COTBKF round 1 (Cottonwood backfill), 3 workers running; finished CTLPLN round 1 at 13:25Z |
| `2.0.0_SA_COO~M` | MDPF_SECCLASS round 7, one worker running |
| `2.0.0_SA_COO~P` | IRPT_BCKEND / IRPT_DASHBD / ADVI_PERFRP (Investor Reporting back end, dashboard, 49F performance) |
| `2.0.0_SA_COO~Y` | IRPT_YCDGEN round 6 (the in-house YCharts report) |
| `2.0.0_SA_COO~D` (laptop) | DSGN_REBRND / DSGN_IRPTV1 portal design; **held by Andrew at ~14:35Z** (LIVE_ARMS hold row), not live now |

### Site Z (from commits on the trunk; the last one 2026-10-05 23:58)

| Seat | Last commit | Project |
|---|---|---|
| `2.0.0_SA_COO~Z` | 10-05 23:31 | AMGT_RESAPP (Security Analysis research pack) |
| `2.0.0_SA_COO~X` | 10-05 23:48 | AMGT_CORPUS (research corpus) |
| `2.0.0_SA_COO~RV` | 10-05 23:38 | ETFS_RIVALS (rival funds) |
| `2.0.0_SA_COO~H` | 10-05 23:30 | AMGT_HARVST (publication harvest) |
| `2.0.0_SA_COO~O` | 10-05 23:20 | NFRA_OPLGTW (Opal Gateway) and the MCP family |
| `2.0.0_SA_COO~D` (site Z) | 10-05 23:49 | DSGN_AMGTV1 (Security Analysis page) |
| `2.0.0_SA_COO~AI`, `~MI`, `~MS`, `~MP` | 10-01 to 10-03 | NFRA_OPALAI, NFRA_MCPINDEX, NFRA_MCPMSP, NFRA_MCPORTAL (quiet or parked) |
| `1.0.0_SA_CTO~Z`, `~O`; `3.0.0_SA_CVO~Z`, `~O`, `~RV`; `4.0.0_SA_CRO~Z`, `~RV`; `0.0.0_AB_MSTR~Z`; `0.7.0_AE_CloudOps~A`, `~RV` | 10-05 | site Z's planning, verification, research, integration and cloud-ops lanes |

**Finding:** the lane letter `D` is in use on BOTH boxes at once (`2.0.0_SA_COO~D` runs DSGN_REBRND on the laptop and
DSGN_AMGTV1 on site Z). Two live seats share one serial. The control plane's per-box serials (C-SERIALS) are the fix;
until then the two cannot be told apart in the record.

---

## 3. Every project, by box and state

States, in the canonical loop's terms: **EXECUTING** (L5-L7, a round open or running), **PRD READY** (L4 signed, no round
open), **AT L2/L3** (endpoint or registration), **QUIET** (no commits in 7 days, not closed), **CLOSED**.

### 3.1 Laptop

| Project | What it is | State | Lane | Two-week activity |
|---|---|---|---|---|
| NFRA_CTLPLN | the four-device control plane | **round 1 COMPLETE** (4 of 13 outcomes PASS); round 2 waits on dell1 standing | COO~C (round 1 done) | 11 commits today |
| ADVI_COTBKF | Cottonwood 10-year backfill from Commonwealth | **EXECUTING** round 1 (3 task orders pending) | COO~C | registered and issued today |
| MDPF_SECCLASS | one classification table (bd-securities consolidation, sector, AI classifier) | **EXECUTING** round 7; PRD v0.12 | COO~M | 166 commits |
| MDPF_SECHIST | the securities database: ingestion and history for every security (Andrew's "pipeline aggregation" inflow work) | **PRD READY** v0.1 co-signed; distribution HELD by Andrew (~18:1xZ) | none | 2 commits (new today) |
| IRPT_YCDGEN | the in-house YCharts report (the ticketing system's first workflow) | **EXECUTING** round 6; PRD v0.8 | COO~Y | 152 commits |
| IRPT_BCKEND | Investor Reporting back end: ingestion, scoping, execution | **EXECUTING**; PRD v0.28, 173 orders complete | COO~P | 1,122 commits |
| IRPT_DASHBD | client reporting dashboard (total-return reporting gold) | **EXECUTING** round 26, 1 order issued | COO~P (workstreams ~P, ~D) | 179 commits |
| ADVI_PERFRP | 49F performance attribution and reporting per client | **EXECUTING** (registry: worked 10-05) | COO~P | flat registry row |
| DSGN_IRPTV1 | Investor Reporting page remediation | **HELD by Andrew** ~14:35Z (no main-branch merge without his word) | COO~D | 473 commits |
| DSGN_REBRND | portal visual elevation (design system) | **HELD by Andrew** ~14:35Z | COO~D | 160 commits |
| NFRA_TRNSPT | communications database: transcripts, market updates, investor commentary input | **QUIET** since 10-02; round 2 orders all complete, no close | COO~T (not live) | 64 commits |
| MDPF_TAXSMA | Tax SMA membership and daily assets | **EXECUTING** but slow: 4 pending, 2 staged | COO~T / COO~D | 43 commits |
| LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM | the naming canon and its builders | **QUIET** (5+ days) | COO~G (not live) | 1-2 commits |
| ADVI_FIRMBKTS, MDPF_CANON, NFRA_SPMOVE | bucket migration; MDPF canon migration; SharePoint movements | **PRD READY / QUIET** (no orders) | none | 1-3 commits |
| IRPT_FNTEND, NFRA_CLDGRPH, NFRA_OUTSET, NFRA_COMPEFFICACY, ETFS_GUARDRAIL | -- | **CLOSED** in the window | -- | closing commits |

### 3.2 Site Z

| Project | What it is | State | Lane | Two-week activity |
|---|---|---|---|---|
| AMGT_RESAPP | Security Analysis: the automated research pack | **EXECUTING**; PRD v0.40; 82 orders pending, 19 staged | COO~Z | 1,147 commits |
| AMGT_CORPUS | the research corpus | **EXECUTING**; 55 orders pending | COO~X | 709 commits |
| AMGT_HARVST | publication harvest | **EXECUTING** round 48 | COO~H | 988 commits |
| DSGN_AMGTV1 | Security Analysis page redesign | **EXECUTING** round 43 | COO~D (site Z) | 485 commits |
| ETFS_RIVALS | rival active-ETF holdings (rivalfunds) | **EXECUTING**; 13 orders pending; one deploy held | COO~RV | 618 commits |
| NFRA_OPLGTW | Opal Gateway (Schwab questions and downloads in Claude) | **EXECUTING**; 1 order pending | COO~O | 469 commits |
| NFRA_OPALAI | opal_ai V1, the Opal Analyst in Teams | **AWAITING ANDREW** (close run approved, waiting on his launch) | COO~AI | 265 commits |
| NFRA_MCPINDEX | the Opal MCP tool index | **QUIET** since 10-02; 5 orders issued | COO~MI | 397 commits |
| NFRA_MCPMSP | the Opal MSP Analyst for partner firms | **HELD** in-lane (ships after opal_ai) | COO~MS | 118 commits |
| NFRA_MCPORTAL | mcp.opalinvest.dev operator console | **PARKED** (CTO~O ruling) | COO~MP | 107 commits |
| NFRA_SPRINTWIN | the daily sprint report | **EXECUTING** (scheduled publish live) | CRO~Z / CTO~Z | 18 commits |
| ADVI_49F | 49F canonical runner chain (TWR engine defect) | **EXECUTING** (worked 10-04 by CTO~O) | site Z | flat registry row |
| NFRA_REPORT, NFRA_IAMROLES202609, NFRA_OPSEC202609 | infrastructure reporting, IAM least privilege, platform hardening | **QUIET** (no commits in two weeks on the mission rows) | none live | 0 |
| POSN_ASTTAX, POSN_AGGFIX | Positioning taxonomy and aggregate | **CLOSED** | -- | -- |

### 3.3 Older flat-registry projects still marked active but cold (more than 72 working hours)

44 rows. The ones that bear on the quarterly goals: ADVI_BDPARITY (Black Diamond parity harness), ADVI_STITCH (49F Black
Diamond history stitching), ADVI_COTKEY (Cottonwood keying), ADVI_INSURE (49F insurance assets), OPAL_TICKET_VNEXT
(ticketing), TRSB_LEDGER (trade submission audit trail, inactive), D3_MODELOVERLAY, OPAL_TAXSMA family, GLOBALALARM.
None has a box field (FWD-7 covers the 37 mission-tree rows only).

---

## 4. Andrew's list, checked against the record

| What he named (transcript) | Box he said | Project(s) found | Agrees? |
|---|---|---|---|
| the control plane | laptop | NFRA_CTLPLN | yes |
| Cottonwood upload mechanics (Commonwealth backfill) | laptop | ADVI_COTBKF | yes |
| YCharts workflow on-premises | laptop | IRPT_YCDGEN | yes |
| performance reporting across 49F, Inflection, Cottonwood | laptop | IRPT_BCKEND, IRPT_DASHBD, ADVI_PERFRP (laptop); ADVI_49F (worked from site Z) | mostly; one piece on site Z |
| the Black Diamond adapter to consolidate Commonwealth history with daily Black Diamond data for Cottonwood | laptop | **no project yet**; ADVI_COTBKF's FWD-8 (line up old and current accounts) is the nearest | **gap** |
| the securities pipeline aggregation (inflows: positioning, models, investor reporting, Advisor Intelligence) | laptop | MDPF_SECHIST (new today), MDPF_SECCLASS | yes |
| transcripts / investor commentary | laptop | NFRA_TRNSPT | yes; quiet since 10-02 |
| rival funds | site Z | ETFS_RIVALS | yes |
| opal_ai, gateway, agent, analyst | site Z | NFRA_OPALAI, NFRA_OPLGTW, NFRA_MCPMSP, NFRA_MCPINDEX, NFRA_MCPORTAL | yes |
| infrastructure (NFRA) on site Z | site Z | NFRA_REPORT, NFRA_IAMROLES202609, NFRA_OPSEC202609, NFRA_SPRINTWIN | yes; three are quiet |
| AMGT corpus, research app, harvest | site Z | AMGT_CORPUS, AMGT_RESAPP, AMGT_HARVST | yes |
| DSGN_AMGTV1 | site Z | DSGN_AMGTV1 | yes |

**Not on his list but live:** DSGN_REBRND and DSGN_IRPTV1 (laptop, held by him today); MDPF_TAXSMA (laptop); the naming
canon projects (laptop, quiet); NFRA_SPRINTWIN (site Z).

---

## 5. The control plane's own state (detail in Document 2)

- **Round 1 (no Dell needed): COMPLETE, graded PASS** by `3.0.0_SA_CVO` @`a69d29a7b0`:
  - FWD-5: pushing any branch other than the trunk no longer deploys anything (live on the laptop; on site Z once it
    pulls `66b1b42a71` or later);
  - FWD-2: one device register, `org/devices/DEVICES.json`, with laptop and site Z; scripts read it, never a path;
  - FWD-8: per-box append files, and a commit check that refuses the wrong box's file;
  - FWD-7: a box field on all 37 mission rows and the placement read used in this census.
- **Round 2 (the thread, laptop -> dell1 -> site Z -> laptop): NOT STARTED.** It waits on dell1 standing.
- **The bidding operation (FWD-13): NOT BUILT.** `.tools/remote-job.py` now reads its device list from the register, but
  still bids CPU and memory only and its awards still run through LDO-001.
- **Not built:** the publish-and-integrate queue (FWD-4), the standing push rule (FWD-6; text approved, lands with the
  queue), leases (FWD-9), per-box identities (FWD-10), restart safety (FWD-11), the one decision list (FWD-12).
- **The CTLPLN seat (`2.0.0_SA_COO~C`) fronts both NFRA_CTLPLN and ADVI_COTBKF** on Andrew's word at ~18:1xZ (CTO record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_181xZ_COO_C_BOTH_SECHIST_REGISTER_HOLD_RIVALS_1Y.md`); it is running the backfill now and holds CTLPLN round 2, which waits on dell1.
  (CORRECTED ~19:1xZ: this line first said the seat had moved on.)

---

## 6. Limits

- Site Z's work after 2026-10-05 23:58 is not visible here (section header).
- "Executing" is read from task-order statuses and commit recency, not from each COO's own drive log.
- Commit counts include worker and merge commits; they measure activity, not progress.
- The 44 cold flat-registry rows were listed, not opened.
