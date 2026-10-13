# BOX STATUS REPORT -- dell2 -- 2026-10-13

Written by `4.0.0_SA_CRO~DELL2` under Andrew-direct 2026-10-13 ~12:3xZ
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_123xZ_BOX_STATUS_REPORTS_FOR_THE_LAPTOP_AUDIT_AND_REALLOCATION.md`),
form `org/tier1_exec/1.0.0_SA_CTO/deliverables/BOX_STATUS_REPORT_FORM_20261013.md`. Relay: laptop CTO msg 108741 via
`0.0.0_AB_MSTR~DELL2` msg 6919.

Population method. (a) Of 399 `org/projects/*.json`, 10 carry `fabric: dell2` with a status other than closed. No register file
carries a `placement` key: 0 of 399. (b) 15 claude.exe seats were counted by process at 13:00Z. Their broker `Working on`
lines name 8 projects: IRPT_BCKEND, NFRA_TRNSPT, TCKT_VNEXT, IRPT_ANLREQ, IRPT_DASHBD, DSGN_IRPTV1 (named as parked),
IRPT_YCDGEN and ADVI_COTBKF. (c) I scanned 6,010 order faces that carry `<issued_to>`. The non-terminal faces issued to a
dell2 seat or a dell2 project name 4 projects: ADVI_COTBKF, IRPT_ANLREQ, IRPT_BCKEND and TCKT_VNEXT. The union is 10, and
(b) and (c) add no project that (a) lacks.

`commits_7d` in every block uses one basis: non-merge commits on box/dell2 in the 7 days to 13:20Z that touch
`org/missions/<D>/<MACRO>/<CODE>/`. Work integrated from other boxes through CLOUD is included. The denominator is 15,798
non-merge commits on box/dell2 in the same window.

```yaml
box: dell2
author: 4.0.0_SA_CRO~DELL2
as_of_utc: 2026-10-13T13:20:35Z
branch_pin: 8aebb0849959ef89f532df3e678dfc709541acfc   # local box/dell2 HEAD at as_of; origin box/dell2 read eef24e799b (ls-remote, same second)
population:
  register_placed: 10        # 10 of 399 project JSONs: fabric=dell2, status not closed (0 of 399 carry a `placement` key)
  live_seat_named: 8         # by the broker summaries of the 15 seats counted by process
  open_order_named: 4        # non-terminal order faces issued to a dell2 seat / dell2 project, of 6010 faces with <issued_to>
  union: 10
seats_live: 15               # claude.exe launcher processes (bun\bin\claude.exe) at 13:00Z; each has one child process; broker shows the same 15 LIVE
seats_by_role: {MSTR: 1, CTO: 1, COO: 7, CVO: 1, CRO: 1, CloudOps: 4, workers_24h: 59}   # COO: ~P2 ~T2 ~V2 ~Y2 ~D2 ~G2 ~C2; CloudOps: ~IB2 ~YC2 ~AQ2 ~TV2; workers = distinct 0.9.0_WK_<dell2 project>~n author lines on box/dell2 in 24h
account_state: ok            # INFERRED, not measured: 15 seats heartbeating within 15 s at 13:00Z. dell2 runs on the fresh account (fc10 addendum 1); the first account's limit and the Oct 17 reset are recorded there; this seat did not read usage
open_deploy_ledgers: 4       # dell2-device ledgers on box/dell2 HEAD (17 ledger files on HEAD in all, 102 distinct names across 53 worktree HEADs): irpt-dashbd-thresholds-swap, irpt-status-rule-all-eight, tckt-vnext-r16-cw2, irpt-holdings-key-restore (deleted in the working tree, uncommitted: closing). A fifth, nfra-trnspt-a18 (device=laptop), names NFRA_TRNSPT
scheduled_jobs_owned: 12     # 3 MEASURED Windows tasks (Opal box-sync, Opal open-calls scan, OPAL_autolaunch_agents) + 9 session loops RECORDED in org/ref/LIVE_ARMS.md (MSTR /govern 60m, CTO /self-drive 60m, 7 COO /canonical-drive 60m), not measured per seat (CronList is per session). Cloud schedules are counted per project below
open_calls_this_box: 6       # open-calls.py list: 27 rows, 6 OPEN (3cb1, fbb1, 01c5, e260, 5cb1, 2e30)
crossbox_open_to_this_box: 10   # crossbox-call.py list --open, addressed to dell2: 1 OPEN (XB-...024430Z-8522 to ~C2) + 9 ACKED not closed
```

## Projects

```yaml
project: IRPT_BCKEND
macro: D9/IRPT
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "portal Investor Reporting tabs (directory search, holdings, performance, narrative, export): this project serves the routes and export files a partner-firm login receives"
intent: "An advisor finds an authorized client and opens its relationship and accounts from Opal's own directory, scoped to their firm, without waiting on a vendor report."
desired_outcome_when_done: "Every Investor Reporting route serves firm-scoped, Opal-computed holdings, performance, narrative and exports, refreshed on a schedule, and an unauthorized replay reveals nothing."
status:
  round: 178                      # workstream P round counter (CTO round-178 analysis @327e1e685a)
  dep_stage: EXECUTING
  fwd_realized: "0/13"            # PRD v0.53, 13 endpoint outcomes; last per-FWD table (CTO rounds 47-60) graded 12 of 12 NOT REALIZED; FWD-5 this project's share REALIZED 2026-10-07, whole outcome waits on IRPT_FNTEND
  last_l10_utc: 2026-10-13        # REMEDIATION_v54 @936ddf2b3c, 08:35Z
  open_orders: 2                  # of 403 order files: TO-IB-pr-512 pending, TO-IB-pr-497 parked (366 complete, 32 superseded, 3 cancelled)
  last_commit_utc: 2026-10-13     # 11:18:49Z @83c71d60db
seats_on_this_box: [2.0.0_SA_COO~P2, 0.7.0_AE_CloudOps~IB2]
dependencies: ["IRPT_FNTEND (owns the grade on FWD-1/3/4/5/8/11)", "runner host (EC2) next scheduled Online for the IB-pr-512 apply", "ADVI_FIRMBKTS (a STOP at the apply's step-0 policy read routes there)", "YCharts stored session (vendor)"]
blockers:
  - what: "round-close-check REFUSED: 2 of 66 judgment criteria ungraded (TO-IB-rti-3 R93-AC3, TO-IB-rtj-2 L4-SIGNOFF)"
    owner: "3.0.0_SA_CVO"
    clears_when: "a CVO adjudication row grades both"
next: ["TO-IB-pr-512: apply the signed minimal holdings packages pair (IB-pr-510) at the runner host's next scheduled Online, then first read (~IB2)", "TO-IB-pr-497: one read-only temp-file count on the builder host (parked)", "provenance read of the 4 unattributed live members (CTO r178 item 2)"]
andrew_acts: []
footprint:
  commits_7d: 1107                # basis in the file preamble
  seats: 2
  aws_resources_owned: unknown    # investor-reporting Terraform declares 17 Lambdas across 15 roots shared with IRPT_DASHBD/IRPT_ANLREQ/TCKT_VNEXT; no per-project owner field to split on
  scheduled_jobs: 7               # Terraform-declared, not live-read: 6 ENABLED (directory-refresh, retry, keepwarm 5-min, holdings-snapshot, holdings-performance, INF performance; MON-FRI) + intake_poll DISABLED
  open_deploy_ledgers: 0          # 0 of 17 on box/dell2 HEAD; its 2026-10-12 holdings ledgers closed @aa73530282
  standing_holds: ["signed never-widen pair IB-pr-510 bounds the IB-pr-512 apply", "DEPLOY-SERVE-HELD sentinel on holdings_performance.py (release state not re-read)"]
if_parked_this_week: "Six enabled cloud schedules keep firing on the bytes now served; the signed IB-pr-512 pair goes stale unapplied; IRPT_YCDGEN PART 2, IRPT_ANLREQ and TCKT_VNEXT, which wait on this project's acceptance half, stall; ~P2 and ~IB2 stand down."
cro_rec: KEEP
cro_rec_why: "It is the live backend behind client-facing Investor Reporting, three other dell2 projects wait on its acceptance half, and its open work is one signed apply plus one parked read."
```

Delivered: on Monday 2026-10-12 the 14:15Z scheduled holdings fire was read back from the served records, and both of its
deploy ledgers were closed (@aa73530282). Andrew's placement word is "I am ok with your move of the IRPT pair back to Dell2"
(2026-10-07 ~07:0xZ), and SEQUENCE v6 has the project at stage 4 with no waits. Two risks. After 178 rounds no FWD is
REALIZED in full, and no per-FWD regrade has been run since the rounds 47-60 table. The live irpt-ycharts-generate package
(Terraform in this project) also lacks the ticket gate that HEAD has (row W312-S3), and only IRPT_YCDGEN's lead can
release it.

```yaml
project: IRPT_DASHBD
macro: D9/IRPT
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "portal Investor Reporting dashboard (Performance chart and reporting views) through the reporting read route that partner-firm advisor logins open; later the quarter-end client reports (FWD-12..14). PROD mount not read: yes under unsure = yes"
intent: "An advisor opens one partner-firm account on the live portal and sees its daily total return (conservative GIPS method, gross of fees and labelled so) for any window in about two seconds, served from a precomputed per-account series."
desired_outcome_when_done: "Every client firm's accounts are served from one Opal-shape reporting gold with a defensible return figure, and quarter-end client reports come from Opal instead of Black Diamond (FWD-11..20)."
status:
  round: 87                       # drain-end @97188ae069 13:04Z, COO reads MAY-CLOSE; first-fire ledger leg still open
  dep_stage: EXECUTING
  fwd_realized: "0/20"            # INFERRED: PRD v0.11 has 20 FWDs; no REALIZED grade found in 423 files; last explicit tally 0 of 10 at rounds 15-17
  last_l10_utc: 2026-10-12T17:36:30Z   # ADJUDICATION_v51 @3959c6611f; CTO round-87 analysis @51269814cc
  open_orders: 0                  # 0 of 161 (158 complete, 3 superseded)
  last_commit_utc: 2026-10-13T13:04:00Z
seats_on_this_box: [2.0.0_SA_COO~D2, 0.7.0_AE_CloudOps~IB2]
dependencies: ["IRPT_BCKEND (holdings price return), dell2", "MDPF_SECCLASS (etf classifications), dell1", "ADVI_FIRMBKTS (household union-find)", "Black Diamond as tie-out comparator; Schwab silver"]
blockers:
  - what: "Deploy ledger irpt-dashbd-thresholds-swap-20261013 leg L7: the first scheduled fire after the 12:39:43Z release is unread"
    owner: "2.0.0_SA_COO~D2"
    clears_when: "the 2026-10-14 11:41Z fire reads clean (l5b_read.py) and the ledger closes, or the release rolls back to the prior S3 version the same session"
  - what: "FWD-8 not gradable: outside-tolerance segments lack a named reason (197 DEFECT at round 48, not re-measured)"
    owner: "2.0.0_SA_COO~D2"
    clears_when: "every segment outside 0.35pp carries a named reason"
next: ["L7 first-fire read 2026-10-14 11:41Z and close the ledger", "round-87 L10 slug, then the CTO round-88 analysis", "re-grade the flow-timing class against Black Diamond's default convention (BD_FLOW_TIMING_HELP_READ_20261013.md)"]
andrew_acts: []
footprint:
  commits_7d: 509
  seats: 2                        # COO~D2 also holds DSGN_IRPTV1; IB2 also serves IRPT_BCKEND
  aws_resources_owned: 22         # Terraform-declared across reporting-gold/-publish/-read: 3 Lambdas, 3 schedules, 5 roles, 7 inline policies, 1 integration, 2 routes, 1 permission; only the gold Lambda live-read
  scheduled_jobs: 3               # EventBridge Scheduler: gold 07:41 ET, publish 08:15 ET, summaries 08:45 ET, weekdays; gold fire evidenced live today, the two publishers not read
  open_deploy_ledgers: 1          # irpt-dashbd-thresholds-swap-20261013 (L1-L6 closed, L7 open)
  standing_holds: ["never-widen pair for the thresholds swap (COO @7c9ad9d0f0, CTO @c5e183273f)", "Black Diamond flow-timing class unworked until the firm's setting is established"]
if_parked_this_week: "Three weekday schedules keep firing on a release hours old while ledger irpt-dashbd-thresholds-swap-20261013 stays OPEN with L7 unread: a bad first fire would go unseen and un-rolled-back."
cro_rec: KEEP
cro_rec_why: "A production Lambda took a release today and its ledger closes only on tomorrow's fire read, and its gold feeds the January 1 Black Diamond replacement (SEQUENCE stage 2); keep it to the ledger close and the round-88 analysis."
```

Delivered: today's scheduled gold fire wrote 13 objects to the reporting gold prefix at or after 11:30Z (ledger L6). The
live Lambda has been CodeSha J6M/92Mh since 12:39:43Z. A dry run used 348 s of 765 s and 1,221 MB of 2,557 MB. FWD-1's
real run (2026-10-02) measured 5,288 ms from tab to chart, and the target is about 2 s. The register JSON is stale. It
still says "D9 is LAPTOP" with coo_lane `~P`, and SEQUENCE flags the project LANE-DARK on that lane, while `~D2` drives it.
round-close-check prints REFUSED (10 early orders have no proof file), and that contradicts the COO's MAY-CLOSE.

```yaml
project: IRPT_ANLREQ
macro: D9/IRPT
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "Ticket Center Analysis Request form and ticket page (DEV live; the PROD ticket page is client-facing per the CTO round-20 analysis) and the package files opened from the ticket"
intent: "One Analysis Request goes from the Ticket Center form to a finished package (report, branded Opal PDF with commentary, original Excel) on the same open ticket, with no person in between."
desired_outcome_when_done: "An advisor's request filed on the form finishes by itself with typo check, swap and no YCharts, an Opal person finds the whole package on the open ticket, and another firm is refused every file."
status:
  round: 20                       # workstream Y round 20 (CTO round-20 analysis @5e7f40b27a)
  dep_stage: EXECUTING
  fwd_realized: "0/7"             # PRD v0.4 FWD-1..7; no record grades any REALIZED; round-1 analysis: FWD-1 NOT REALIZED
  last_l10_utc: 2026-10-13T07:10:56Z   # CVO round-19 slug @c219042317; CTO answered 07:12Z
  open_orders: 3                  # of 100: TO-AR-y-212 (~61), TO-AR-y-213 (~64), TO-APPLY-R20 (~AQ2)
  last_commit_utc: 2026-10-13T12:58:24Z
seats_on_this_box: [2.0.0_SA_COO~Y2, 0.7.0_AE_CloudOps~AQ2, 0.7.0_AE_CloudOps~YC2]
dependencies: ["IRPT_BCKEND (~P2): resident library release carrying the W328-S1 repair", "IRPT_YCDGEN: irpt-ycharts-generate, under hold D2-W53-S9", "NFRA_TRNSPT (~T2): TR-dp-24 commentary post", "dell1 open call e7f2: Andrew's held portal PROD promote"]
blockers:
  - what: "FWD-1 live run waits on a person filing one test Analysis request in a partner firm (open call dell2-20261012T222152Z-2e30)"
    owner: "Andrew"
    clears_when: "an Opal staff member files the synthetic request naming TCK-20261012-c546fead and uploads the two synthetic files (Andrew 12:23Z card 1: later)"
  - what: "Ledger irpt-status-rule-all-eight-20261013 opened 12:25Z with 0 of 9 legs closed while ~AQ2's line reads IDLE"
    owner: "0.7.0_AE_CloudOps~AQ2"
    clears_when: "TO-APPLY-R20 runs its 9 legs and closes the ledger, or closes it NOT-RUN"
  - what: "round-close-check REFUSED: 22 of 39 judgment criteria have no CVO verdict row"
    owner: "3.0.0_SA_CVO"
    clears_when: "each ungraded criterion carries a verdict row"
next: ["TO-APPLY-R20: status rule into all eight packagers and irpt-status (signed pair @67cadd141d)", "drain TO-AR-y-212/213 (proofs on worker branches @44280fb471, @0c16982e06)", "r19.1 backstop repair, then the two-leg release"]
andrew_acts: ["staff test filing plus two synthetic uploads (open call 2e30; card 1, 'later')", "portal PROD promote carrying the ticket wording (dell1 e7f2; card 9: localhost 5174 smoke, then promote)"]
footprint:
  commits_7d: 595
  seats: 3
  aws_resources_owned: unknown    # surfaces shared with IRPT_BCKEND/IRPT_YCDGEN/NFRA_TRNSPT; no separable list
  scheduled_jobs: unknown         # no schedule cited in PRD or orders; an intake poller's owner was not read
  open_deploy_ledgers: 2          # irpt-status-rule-all-eight-20261013 (open); irpt-holdings-key-restore-20261013 (on HEAD, deleted in the working tree uncommitted)
  standing_holds: ["D2-W53-S9: no rebuild of the generate function until its four unpinned members are pinned or released", "D2-S109: no release carrying ycharts_session.js before the IRPT_BCKEND host library release"]
if_parked_this_week: "The status-rule ledger (0/9 legs, window to ~16:25Z) goes RED unless finished or closed NOT-RUN; two worker branches with undrained proofs go stale; release 19 stays live and correct; open call 2e30 loses its consumer."
cro_rec: KEEP
cro_rec_why: "It is the one Analysis Request project Andrew named (10-08 word compressing the workstreams); drive it this week only to the FWD-1 live run and stop opening reader-hardening rounds."
```

Delivered: release 19 (the reader that turns back two-account and total-row templates) went live on the resident host at
06:09Z and on irpt-ycharts-generate at 06:27Z on 2026-10-13, and the CVO read the digest. Twenty rounds have produced no
REALIZED FWD. Rounds 10-20 mostly hardened the holdings reader, and the end-to-end request has never run live. The
project runs under `ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md`, which also
compresses TCKT_VNEXT into it. The register still carries both projects. Seat note: `~Y2`'s broker line names
TO-AR-y-162, which reads `complete`, so the line is stale.

```yaml
project: TCKT_VNEXT
macro: D7/TCKT
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "Ticket Center board and ticket page on the portal (partner-firm requesters; C-FENCE firm check on get and list)"
intent: "The Ticket Center takes typed requests, the Analysis Request first: a holdings file attached through the upload door and the finished report opened from the same ticket."
desired_outcome_when_done: "An Opal person files an Analysis Request with a holdings file and opens the finished report from the ticket, and a sign-in at another firm is refused both."
status:
  round: 16
  dep_stage: EXECUTING
  fwd_realized: "0/9"             # PRD v0.4 FWD-1..9; DECOMP_R16: FWD-1 NOT REALIZED and not run; FWD-2 met for the ticket, not read for the file
  last_l10_utc: 2026-10-12T22:28:02Z   # round-14 slug; CTO round-15 analysis @0d75f50385
  open_orders: 1                  # of 57: TO-RUN-R16-cw2 (~TV2)
  last_commit_utc: 2026-10-13T13:08:06Z
seats_on_this_box: [2.0.0_SA_COO~V2, 0.7.0_AE_CloudOps~TV2]
dependencies: ["IRPT_ANLREQ (staff test filing 2e30, package path)", "IRPT_BCKEND / IRPT_YCDGEN (upload door, POST analysis)", "NFRA_TRNSPT (commentary trigger for FWD-6)"]
blockers:
  - what: "FWD-1 not run since round 6; the YCharts path stopped since round 4 and rounds 7-16 cut no thread work"
    owner: "1.0.0_SA_CTO~DELL2"
    clears_when: "the thread runs through IRPT_ANLREQ's no-YCharts path"
  - what: "Round-16 crawl: sitting 1 hit a STOP that wrote nothing; sitting 2 amended in at 13:02Z (@06bd872615)"
    owner: "0.7.0_AE_CloudOps~TV2"
    clears_when: "legs L2-L6 close, including the synthetic identity row read ABSENT"
next: ["TO-RUN-R16-cw2 sitting 2: close test tickets TCK-20261009-a1052909 and TCK-20261012-13cd3a1d, then delete the synthetic identity", "close open calls fbb1 and 5cb1 on that receipt", "CVO grade of the round-16 slug"]
andrew_acts: ["organic first real Analysis request by a staff member (open call 3cb1; card 8, 'later today')"]
footprint:
  commits_7d: 272
  seats: 2
  aws_resources_owned: unknown    # writes opal-ticket-api and ticket rows, but the Ticket Center is shared and ownership was not read
  scheduled_jobs: unknown         # none cited in PRD or orders
  open_deploy_ledgers: 1          # tckt-vnext-r16-cw2-two-ticket-crawl-20261013 OPEN, 1 of 6 legs, window 4 h from 12:44Z
  standing_holds: ["YCharts vendor path stopped since round 4"]
if_parked_this_week: "Parking mid-sitting would leave a synthetic users-table identity live and the crawl ledger RED after ~16:44Z, so finish or roll back R16-cw2 first; after that nothing rots (C-FENCE refusals are live, test tickets just stay open)."
cro_rec: MERGE_INTO:IRPT_ANLREQ
cro_rec_why: "Andrew's 10-08 word already compresses it into the one Analysis Request project, its FWD-1/2 restate IRPT_ANLREQ's FWD-1/5, and both write the same Ticket Center files; close the crawl ledger, fold C-FENCE in, free ~V2 and ~TV2."
```

Delivered: the C-FENCE refusals are live in opal-ticket-api. Round 7 proved the no-users-row 403s and round 9 the
status-active 403s. Today at 12:45Z ledger leg L1 read the live CodeSha256 equal to the source map. round-close-check reads
MAY-CLOSE (11/11 judgments graded, 55/55 proofs OK). Risk: the crawl mints a synthetic identity in a partner firm's
tenant, and the ledger stays open until that row reads ABSENT. Two drivers write one surface, because TCKT_VNEXT and
IRPT_ANLREQ both write `portal/src/pages/TicketCenter/` and `ticket_center/lambda_function.py`.

```yaml
project: IRPT_YCDGEN
macro: D9/IRPT
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: indirect
client_surface: "Investor Reporting > Analysis tab report (Opal-made); built and dormant on the trunk, no output reaches any login today"
intent: "Andrew submits one real portfolio for an Overview and opens an Opal-branded report in the same sitting, every figure computed by Opal and nothing asked of YCharts."
desired_outcome_when_done: "Everyone using the Analysis tab gets the Opal-made report for all three report types and Opal stops calling YCharts for it."
status:
  round: 17                       # CTO round-17 analysis @c741ef41fa, nothing cut
  dep_stage: ROUND_CLOSE
  fwd_realized: "0/22"            # PRD v0.13, 22 outcomes; FWD-1 NOT MET rounds 10-17
  last_l10_utc: 2026-10-11        # REMEDIATION_v13 @1549efce5d, 21:18Z
  open_orders: 0                  # 0 of 53
  last_commit_utc: 2026-10-13     # 02:38:31Z @f1c4389a54 (an IRPT_ANLREQ drain naming it); last tree commit 2026-10-11T23:31Z
seats_on_this_box: [2.0.0_SA_COO~G2]
dependencies: ["IRPT_BCKEND acceptance half of PRD v0.13", "NFRA_OPSWKF FWD-9", "NFRA_TRNSPT closed-list check", "TCKT_VNEXT request-id match", "IRPT_ANLREQ form half"]
blockers:
  - what: "Binding PART 2 is sequenced behind four other projects' served changes (CTO r17 section 3)"
    owner: "1.0.0_SA_CTO~DELL2"
    clears_when: "the four changes are applied and PART 2 names each by its applied digest"
  - what: "Sign-off tool reads a PRD half SIGNED before the signature exists (row IRPT_BCKEND-D2-S83)"
    owner: "0.0.0_AB_MSTR~DELL2"
    clears_when: "the row is placed with the tool's owner and the tool fixed"
next: ["release the ticket gate onto the live irpt-ycharts-generate package (row W312-S3), the reason G2 was seated today", "cut PART 2 once the four dependencies land", "grade round-close (0 of 6 judgment criteria graded)"]
andrew_acts: ["sit for the FWD-1 run: submit a real portfolio and open the Opal report (CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_17_20261011.md s4)", "put svc-irpt-analysis on the producer's allow list (IRPT_YCDGEN_PRD.md:248)"]
footprint:
  commits_7d: 220
  seats: 1
  aws_resources_owned: unknown    # runner host release st32 and irpt-generation-dlq named in records; no per-project Terraform root counted
  scheduled_jobs: unknown         # PRD C-VENDOR names a scheduled refresh; applied state not read
  open_deploy_ledgers: 0
  standing_holds: ["C-SWITCH allow list starts with Andrew's sign-in only and changes only on his word"]
if_parked_this_week: "No client output stops, but the live irpt-ycharts-generate stays without the ticket gate (W312-S3), the gap Andrew seated G2 to close today; st32 keeps serving as installed; G2 stands down."
cro_rec: KEEP
cro_rec_why: "Keep it narrowly: Andrew seated G2 today ('Seat it now') to release one known live gap only this lead can release; after that release nothing can be cut until IRPT_BCKEND's acceptance half lands, so park it then."
```

Delivered: the st32 resident release has been on the runner host since 2026-10-11, and its rollback step passed with a
negative control (@bb557d26ed). The ticket-gated worker is merged but dormant (@dddafd6832). No Opal-made report has
reached Andrew. The fifth run on 2026-10-11 failed NO_AUTHENTICATED_PROBE (@77f135f74f). Andrew's word is card 2 of
`ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`. The PRD author line says "laptop", while the register and
SEQUENCE say dell2.

```yaml
project: DSGN_IRPTV1
macro: D13/DSGN
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "portal Investor Reporting page: header plus the Performance, Holdings and Analysis tabs, which partner-firm advisor logins open"
intent: "An Opal user opens Investor Reporting, picks one named partner-firm brokerage account, and reads its identity card, YTD return with spread, Models/SMAs/Client split and security list on the portal panel system."
desired_outcome_when_done: "The advisor-facing Investor Reporting page reads in client language on Opal's light portal look, with every system fact one click away and no producer vocabulary on its face (FWD-1..23)."
status:
  round: 33                       # CTO round-33 analysis @39d21c5657: "Nothing is cut in this project"
  dep_stage: EXECUTING
  fwd_realized: "0/23"            # INFERRED: worker ~45 state table 2026-10-11 (not a grade): APPLIED 9, EXERCISED 14, REALIZED 0
  last_l10_utc: 2026-10-13T00:26:13Z   # REMEDIATION_v12 / ADJUDICATION_v21 @011a05ef2c
  open_orders: 0                  # 0 of 126
  last_commit_utc: 2026-10-13T03:12:13Z
seats_on_this_box: [2.0.0_SA_COO~D2]
dependencies: ["IRPT_BCKEND ~P2: account_id member on each partner ACCOUNT node, riding the builder host bundle", "portal PROD promote (dell1 e7f2), on Andrew"]
blockers:
  - what: "The page cannot switch to the account id until the producer serves account_id (rows D2-W69-S1, D2-W72-S2)"
    owner: "2.0.0_SA_COO~P2"
    clears_when: "the IRPT_BCKEND producer cell is live with account_id served"
  - what: "Every DEV candidate's PROD rides the held promote e7f2 (row D2-W61-S2)"
    owner: "Andrew"
    clears_when: "Andrew smokes DEV @f6446051 on localhost:5174 and the promote runs"
next: ["close D2-W60-S1, D2-S21, D2-W70-S4 (candidate 64980b4d is on DEV)", "switch the page to account_id once served", "PROD via the e7f2 promote"]
andrew_acts: ["smoke portal DEV @f6446051 on localhost:5174 and promote if it passes (card 9; PORTAL_PROD_PROMOTE_SMOKE_LIST_DEV_f6446051_20261013.md)"]
footprint:
  commits_7d: 135
  seats: 1                        # shared: COO~D2 reads it parked
  aws_resources_owned: 0          # owns only the render of portal/src/pages/InvestorReporting/**
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: ["PROD rides Andrew's held promote e7f2", "YCharts not named as a vendor-report source: 'not now' (call 0eab CLOSED)"]
if_parked_this_week: "Nothing rots; safe to park: 0 open orders, 0 schedules, 0 ledgers; the producer fails closed so the page shows nothing wrong; DEV candidates wait on the e7f2 promote either way."
cro_rec: PARK
cro_rec_why: "The round-33 analysis cut nothing and every remaining item waits on IRPT_BCKEND's account_id cell or Andrew's PROD promote; a formal park costs nothing and keeps COO~D2 on IRPT_DASHBD, un-parking when account_id is served."
```

Delivered: portal candidate 64980b4d (a plain-sentence reason on the unsupported vendor-report card) is on origin/DEV as
of today. Portal PROD is still @37aa1247 (2026-10-09). DEV is 163 commits ahead of PROD, and 143 of the changed files
are under InvestorReporting. All of it reaches clients only through Andrew's smoke and promote. The park comes from a CTO
sequencing ruling (round 33), not from Andrew's word. The project has no SEQUENCE row, and its placement record says "held
by Andrew; goes where the IRPT projects go". round-close-check prints REFUSED (29 of 60 judgments ungraded).

```yaml
project: ADVI_COTBKF
macro: D8/ADVI
placement: dell2
status_register: active
repos: [ajb_workspace]
client_facing: no
client_surface: "none: served silver tables in Opal's own store with 0 readers; PRD v0.7 releases no reader before the re-serve that carries the closed correction list"
intent: "An analyst picks one partner-firm account and reads its whole transaction history, daily after-fee returns back to 2013, documents and crosswalk from Opal's own store, traceable to the custodian's delivery."
desired_outcome_when_done: "The partner firm's 10-year custodian delivery is held in Opal as received, typed, priced on a stated basis and readable per account, with its sensitive fields held only where Andrew decided."
status:
  round: 80
  dep_stage: EXECUTING
  fwd_realized: "5/9"             # endpoint read 4/9 (FWD-1,5,6,8) round 26 @a9aca322b9, plus FWD-3 REALIZED with 2 named exceptions (CTO ADDENDUM 11, round 34); no full re-read since
  last_l10_utc: 2026-10-12        # CVO slug REMEDIATION_v48 @29d14cb8dd 02:46Z; CTO round-80 analysis @7bfd7c4664
  open_orders: 3                  # of 173: TO-CB-cb-1, cb-2, cb-3 issued
  last_commit_utc: 2026-10-13T12:40:56Z
seats_on_this_box: [2.0.0_SA_COO~C2]   # plus worker subagents ~155, ~156 inside its session
dependencies: ["MDPF_DEMQUE on dell1: as-traded closes for 15 funds; 7 landed, 8 rejected LOW_TRADE_AGREEMENT", "MDPF_SECHIST securities-history store on dell1"]
blockers:
  - what: "Row D2-S131 BLOCKING: every held fund day is UNPRICED under C-BASIS until dell1's closes land; 8 of 15 rejected"
    owner: "dell1 MDPF_DEMQUE issuer (serial not read)"
    clears_when: "dell1 lands the 8 rejected funds' closes, or the CTO rules on 7 of 15 after the CB-cb-2 read-back"
  - what: "Row D2-W152-S1: three equities priced at 1/2, 1/7, 1/10 of the store row, cause unknown"
    owner: "1.0.0_SA_CTO~DELL2"
    clears_when: "CB-cb-1 drains and the round-81 analysis rules"
next: ["drain CB-cb-1 and CB-cb-2 (records committed on worker branches, not merged)", "CB-cb-3: re-cut the correction list (worker ~157 not yet spawned)", "round-80 slug, then the CTO round-81 analysis"]
andrew_acts: []
footprint:
  commits_7d: 622
  seats: 1
  aws_resources_owned: unknown    # writes custodian bronze/silver prefixes, the restricted prefix and its breakglass role, and has had Lambda deploys; live count not read
  scheduled_jobs: 0               # PRD surface manifest S01-S10 holds no schedule
  open_deploy_ledgers: 0
  standing_holds: ["D2-S131: no pre-2026-06-08 holdings rebuild, no consumer on the minted table, nothing re-priced", "PRD v0.7: no reader before the corrected re-serve", "988 bond account-days HELD_SOURCE_UNDER_REVIEW", "C-RESTRICTED: CRM zip not landed (FWD-2/4/7)"]
if_parked_this_week: "Nothing rots and no reader is served; drain the two worker branches and drop ~157 before standing C2 down; dell1's request stays filed; the served return history keeps its known defects with 0 readers."
cro_rec: PARK
cro_rec_why: "80 rounds and 622 tree commits in 7 days produce price-basis findings on a table no reader may use, blocked on dell1's fund closes; drain round 80, then park until all 15 closes are in."
```

Delivered: FWD-1 is one account's transaction history, 3,537 rows (2016-01-25 to 2026-06-22), read from served silver. A
row traces back to the delivery zip with its sha256 matching (ENDPOINT_READ_20261009.md). FWD-5 is a served index of
11,119 documents (round 6, 2026-10-07). Andrew's word conflicts with this PARK rec. He seated C2 today at about 12:23Z with
"We have the room to do this, yes" (card 6), while the CTO's rec on that call was "wait unless the weekly budget has room:
no live defect and no dependent project". Risk: the round-72 analysis calls the served return history defective, with at
least 9 fund series valued low and 1,700 securities with no close. It is safe only because there are 0 readers.

```yaml
project: ADVI_BILLING
macro: D8/ADVI
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: yes
client_surface: "Advisor Intelligence page fee panel (one billed quarter's fee against the custodian debit), portal DEV only @6d383958; PROD rides Andrew's promote"
intent: "Work out one household's fee for one past quarter from Opal's own data, show it to an advisor in Opal, and match it to what the custodian actually debited, outside Black Diamond."
desired_outcome_when_done: "Opal computes, explains and traces every advisory fee to its agreement and produces the quarterly custodian fee file without Black Diamond, and Andrew has made the buy-or-build call on a priced comparison."
status:
  round: 3
  dep_stage: EXECUTING
  fwd_realized: "1/6"             # FWD-3 REALIZED (CVO round-3 grade, CTO ADDENDUM 4 @44f3540b16); FWD-1 exercised on DEV
  last_l10_utc: 2026-10-09        # CVO slug @28215996eb 10:16Z
  open_orders: 0                  # 12 of 12 complete
  last_commit_utc: 2026-10-11T03:22:21Z   # last tree commit (header-only); last substantive 2026-10-09T10:19:55Z
seats_on_this_box: []
dependencies: ["Andrew's portal PROD promote (dell1 e7f2)", "NFRA_OPLGTW on sitez: gateway copy_site_file_to_s3 (released 2026-10-11)", "d08 cutover for the served ownership map (row D2-W4-S2)"]
blockers:
  - what: "FWD-1 realizes only when the fee panel reaches PROD"
    owner: "Andrew"
    clears_when: "the localhost:5174 smoke passes and portal DEV promotes to PROD (card 9)"
  - what: "No COO seated: 2.0.0_SA_COO~B2 idle since 2026-10-09T10:19Z; LIVE_ARMS lists it not seated (sequence WAITING on Andrew's firm answers)"
    owner: "Andrew"
    clears_when: "Andrew's word seats a COO lane, or the firms' billing answers arrive (SEQUENCE.yaml:127)"
next: ["land the Q3 2026 statement through copy_site_file_to_s3 (closes site Z NFRA_OPLGTW round-33 AC3, XB-ad8b)", "FWD-1 grades on the PROD promote", "CTO~DELL2 writes the round-4 enrichment list"]
andrew_acts: ["smoke portal DEV on localhost:5174 and promote (card 9)", "bring each firm's billing system, fee terms and sign-off (SEQUENCE.yaml:127; Q-2 brief PART V)"]
footprint:
  commits_7d: 42
  seats: 0
  aws_resources_owned: 6          # Terraform-declared in advi/billing-read: 5 resource blocks + 1 Lambda module; live not re-read
  scheduled_jobs: 0
  open_deploy_ledgers: 0          # its 3 ledgers closed
  standing_holds: ["C-NO-VENDOR-YET: no billing vendor contacted", "C-NO-UPLOAD: the custodian fee file uploaded only on Andrew's word", "D2-W4-S2: ownership map waits for the d08 cutover"]
if_parked_this_week: "No job fires and no ledger is open; the billing-read Lambda sits idle and the panel ships to PROD with any promote anyway; site Z's NFRA_OPLGTW round 33 cannot close until the first E2 put (XB-ad8b)."
cro_rec: PARK
cro_rec_why: "Unseated since 2026-10-09 and waiting on Andrew's firm answers; its next outcome realizes on a promote he already holds, so keep it parked, but have one existing seat make the single Q3 statement put that site Z's close waits on."
```

Delivered: on 2026-10-09 the fee panel landed on portal DEV, rendered on real served data, and the CVO graded FWD-3
REALIZED. advi-49f-billing-read-lambda refused another firm's admin token with a 401, so the cross-firm arm was
exercised. The project ran rounds 1-3 in one day. It has stalled, not finished. A stale record: REMEDIATION_v3 row
D2-W7-S1 still reads OPEN, but site Z built and released the tool (OG-rl-16). Andrew's word it runs under:
`ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md`.

```yaml
project: NFRA_TRNSPT
macro: D9/NFRA
placement: dell2
status_register: active
repos: [ajb_workspace]
client_facing: yes                # unsure = yes: the drafter posts to a ticket in a partner-firm tenant; whether a partner login can open the draft was not measured; the database itself is staff-only
client_surface: "commentary DRAFT on the requester's Ticket Center ticket (FWD-10 route; 0 posts to date); the meeting/mail database is staff-only"
intent: "Every Opal Teams meeting type plus admitted market-update mail and decks land wiped and readable in one database with no person running a step, and a drafter turns a ready analysis report's abstract fields into a commentary draft on its ticket."
desired_outcome_when_done: "Andrew reads a meeting in the database the afternoon it happens, finds any past meeting Microsoft still holds, and each ready analysis report gets a staff-reviewable commentary draft without anyone fetching or typing."
status:
  round: 24
  dep_stage: EXECUTING
  fwd_realized: "2/11"            # FWD-4 (round-20), FWD-7 (round-12 ADDENDUM 2); FWD-1 EXERCISED, waits on Andrew's ACCEPT
  last_l10_utc: 2026-10-12T17:19Z # round-23 slug REMEDIATION_v11 @85dc14651c
  open_orders: 0                  # 75 of 75 complete
  last_commit_utc: 2026-10-13T12:27:48Z
seats_on_this_box: [2.0.0_SA_COO~T2]
dependencies: ["NFRA_OPLGTW (site Z gateway: Teams/mail listing, share-link resolver)", "IRPT_ANLREQ (one staff-filed analysis request)", "TCKT_VNEXT (test ticket)", "Microsoft Graph transcripts (~120-day hold)", "Kimi model call (C-KIMI standing word)"]
blockers:
  - what: "TR-dp-24 (FWD-10's first live draft post) parked until one staff-filed test Analysis request names the partner-firm test ticket"
    owner: "Andrew"
    clears_when: "the filing is made (open call 2e30; card 1, 'later')"
  - what: "research_meeting (FWD-2, type 4 of 4): folder located, listing waits on a site Z share-link resolver"
    owner: "1.0.0_SA_CTO~Z"
    clears_when: "the resolver ships; open call 01c5 then closes (card 3: agents find it via the gateway)"
  - what: "FWD-8 ADMITTED read: the second reader is trusted to the terminal IAM user, whose key is on no fabric box"
    owner: "Andrew"
    clears_when: "the three read-only commands run on the terminal machine, or the key is rotated (open call e260; card 4: he does not know the key)"
next: ["TR-fr-24: read run.json at the first fire after the next ocio_ic and asset_management_ic meetings (FWD-2)", "round-25 completeness rows: four refused Monday meetings, 2026-06-01 UNDECIDABLE (FWD-3/4)", "TR-dp-24 first post once the filing lands"]
andrew_acts: ["read MM-20261012-0858 in the database (FWD-1 ACCEPT; CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_24_20261012.md s5)", "name one past meeting and find it (FWD-3)", "staff test filing (open call 2e30)", "locate or rotate the terminal IAM user's key (open call e260)"]
footprint:
  commits_7d: 224
  seats: 1
  aws_resources_owned: 39         # served-graph nodes with owner_pipeline=transcripts, of 2926 scanned (vintage 2026-10-13 13:00:53Z); 11-12 may be the Teams chat-assist service
  scheduled_jobs: 2               # EventBridge: teams transcripts pull hourly 13-22 UTC MON-FRI, outlook pull daily 23:30; live rule state not read
  open_deploy_ledgers: 1          # nfra-trnspt-a18-second-reader-laptop-20261009, HELD, device=laptop
  standing_holds: ["a18 ledger held on the FWD-8 ADMITTED read", "D2-S31: no plan of the transcripts root from a tree not hashing to the live digest", "drafts never sent; abstract fields only (C-KIMI)"]
if_parked_this_week: "The two EventBridge pulls keep firing on current code and keep landing meetings and mail (park the seat, not the pulls); the drafter stays idle; the a18 ledger stays held at the laptop; COO~T2 stands down; an unlanded research meeting ages toward the ~120-day hold, weeks away."
cro_rec: PARK
cro_rec_why: "The thread runs on its own schedule and every remaining outcome waits on an Andrew act or site Z's resolver, so a live COO spends dell2's account on waits; re-seat when the staff filing or the resolver lands."
```

Delivered: the 14:00Z scheduled hourly fire on 2026-10-12 landed Monday meeting MM-20261012-0858 from bronze to silver
with no person in the loop, at a peak of 239 MB of 1024 MB. The first unaided landing was 2026-10-09 16:00Z (1 meeting, 436
rows, 98 held out). FWD-3 rules four Monday meetings LOST to `refused`, with 2026-06-01 UNDECIDABLE. One read flips it:
site Z's gateway request log for 2026-09-29. `STATUS.md` in the tree is stale (2026-10-02). Disabling the pulls would
lose meetings to the hold.

```yaml
project: NFRA_OPSWKF
macro: D9/NFRA
placement: dell2
status_register: active
repos: [ajb_workspace, portal]
client_facing: indirect
client_surface: "Ticket Center trade-request form (portal DEV only; 1ce56459 not an ancestor of origin/PROD); trade dashboard and submit route fenced to Opal staff; trades land in client accounts at custodians"
intent: "One trade request goes from an advisor through a Ticket Center ticket to the operations lead and on to the custodian with nothing typed twice, on one trail, and nothing reaches a custodian he did not send."
desired_outcome_when_done: "The operations lead runs trade submission from Opal with the trail from request to custodian confirmation, and the trade services answer Opal staff only through one door."
status:
  round: 1                        # thread round 1; workstream S ran rounds 1-2 plus the FWD-10 cell
  dep_stage: EXECUTING
  fwd_realized: "3/10"            # FWD-8, 9, 10 REALIZED (CVO ADJUDICATION_v1-v3); FWD-7 exercised on fixtures only
  last_l10_utc: 2026-10-11T21:55Z
  open_orders: 0                  # 10 tree orders complete; 7 seat-folder orders terminal
  last_commit_utc: 2026-10-12T02:21:02Z
seats_on_this_box: []
dependencies: ["Andrew's sitting with the operations lead (SEQUENCE.yaml:129-134)", "NFRA_MCPINDEX readers for FWD-7's live adapter (site Z)", "NFRA_OPLGTW (gateway SharePoint upload)", "TCKT_VNEXT / Ticket Center"]
blockers:
  - what: "SEQUENCE wait: FWD-1 to FWD-6 cannot be specified before Andrew sits with the operations lead"
    owner: "Andrew"
    clears_when: "the sitting happens and its notes reach 1.0.0_SA_CTO~DELL2"
next: ["OW-r-1: real run of FWD-1 on DEV, after the sitting", "CTO~DELL2 dispositions the 2026-10-12 finding that firmId opal-capital alone passes both trade fences", "FWD-7 live adapter once NFRA_MCPINDEX readers land"]
andrew_acts: ["sit with the operations lead (SEQUENCE.yaml:133; Q-3 brief PART V)", "name the SharePoint folder for the ops-kit delivery (R1_RUN/OW_KR1_KIT_REAL_RUN_20261009.md)"]
footprint:
  commits_7d: 90
  seats: 0
  aws_resources_owned: 0          # 0 served-graph nodes with owner_pipeline nfra_opswkf (of 2926); it changed pre-existing trade-pipeline resources but owns none
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: ["SEQUENCE wait on the sitting (CVO verdict 2026-10-11: binds all but workstream S)", "row D2-S7 INERT with the CTO"]
if_parked_this_week: "Nothing rots; safe to park. No schedule, ledger or seat; the staff-only fences stay deployed; the trade form sits on DEV only."
cro_rec: PARK
cro_rec_why: "The runnable security workstream is done (3/10 REALIZED, fences deployed) and every remaining outcome is gated on Andrew's sitting with the operations lead."
```

Delivered: FWD-10 was REALIZED on 2026-10-12 at about 00:05Z. One reversible setting closed the trade-submission API's
public endpoint, and the probe discriminated 401 -> 404 (CVO `NFRA_OPSWKF_FWD10_L9_GRADE_20261012.md`). The project has
been idle since 2026-10-12 02:21Z. Risk carried: the 2026-10-12 code read found that both trade fences admit on
`firmId == opal-capital` alone, whatever the email domain. It went to the CTO, and no disposition row exists yet.

## Box-level close

- **Would hurt most if stopped this week.** (1) IRPT_DASHBD: a production Lambda released at 12:39Z today, three weekday
  schedules, and an open ledger whose L7 read is tomorrow at 11:41Z. (2) IRPT_BCKEND: the live backend behind
  client-facing Investor Reporting, with 6 enabled schedules, a signed apply waiting on the host's Online, and 3
  projects waiting on its acceptance half. (3) IRPT_ANLREQ: the one Analysis Request journey Andrew named, plus an open
  0/9-leg ledger that goes RED at ~16:25Z if abandoned.
- **Could stop today with no loss.** NFRA_OPSWKF and ADVI_BILLING are already unseated, with 0 schedules and 0 ledgers.
  DSGN_IRPTV1 has 0 orders and 0 ledgers and waits on IRPT_BCKEND and the promote.
- **Seats freed by these recs: 4 COO and 1 CloudOps, 15 -> 10.** The four COO seats are `~T2` (NFRA_TRNSPT), `~V2`
  (TCKT_VNEXT merge), `~C2` (ADVI_COTBKF, after the round-80 drain) and `~G2` (IRPT_YCDGEN, after the W312-S3 release).
  The CloudOps seat is `~TV2`, after the R16 crawl ledger closes. The DSGN_IRPTV1 park frees none, because `~D2` stays on
  IRPT_DASHBD.
- **Two Andrew acts unlock most of the box.** The portal PROD promote (dell1 e7f2, card 9: smoke on localhost:5174) gates
  FWDs in ADVI_BILLING, DSGN_IRPTV1 and IRPT_ANLREQ. The one staff test filing (open call 2e30, card 1) gates IRPT_ANLREQ
  FWD-1, NFRA_TRNSPT TR-dp-24 and TCKT_VNEXT.
- **Audit signal.** 7 of 10 projects have 0 REALIZED FWDs: IRPT_BCKEND after 178 rounds, IRPT_DASHBD after 87,
  DSGN_IRPTV1 after 33, IRPT_ANLREQ after 20. Only ADVI_COTBKF (5/9), NFRA_OPSWKF (3/10), NFRA_TRNSPT (2/11) and
  ADVI_BILLING (1/6) have outcomes graded REALIZED. Each of the four highest-round projects also prints REFUSED on
  round-close-check while its COO reads MAY-CLOSE. Except TCKT_VNEXT, which reads MAY-CLOSE.
- **Classified with low confidence.** NFRA_TRNSPT client_facing could be indirect rather than yes. One read settles it: a
  C-FENCE get by a partner-firm login on a ticket carrying a draft post. For IRPT_DASHBD, whether the dashboard is
  mounted on PROD is unread. Several fwd_realized values are INFERRED from the absence of a REALIZED grade, because these
  PRDs carry no per-FWD status column.

## Compiler Tools

`/watcher` (Monitor + census); `get_live_agents` and the claude.exe census by process; a python scan of `org/projects/*.json`
(399) and of 6,010 `<issued_to>` order faces; `python .tools/open-calls.py list`; `python .tools/crossbox-call.py list
--open`; `git worktree list` with `git ls-tree` over 53 worktree HEADs for `.open_deploys` (102 distinct names);
`Get-ScheduledTask`; `python .tools/sequence-check.py --project <CODE>` (x10); `git log --no-merges` path-scoped for
commits_7d; per-project research by five read-only helpers, which used the PRDs, `round-close-check.py`, CTO analyses and
the served graph. Gap: `to-check.py --assignee` did not see tree orders under the default 14-day scope, so I used my own
face scan.
</content>
</invoke>
