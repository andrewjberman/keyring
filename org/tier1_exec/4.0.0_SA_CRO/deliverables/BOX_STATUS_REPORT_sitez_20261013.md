# BOX STATUS REPORT -- sitez -- 2026-10-13

**Author:** `4.0.0_SA_CRO~Z`. **Ask:** Andrew-direct 2026-10-13 ~12:3xZ, relayed by `0.0.0_AB_MSTR~Z` msg 33623
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_123xZ_BOX_STATUS_REPORTS_FOR_THE_LAPTOP_AUDIT_AND_REALLOCATION.md`).
**Form:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/BOX_STATUS_REPORT_FORM_20261013.md`. Every number below was read at
`as_of_utc` on this box; `unknown` carries its reason.

**How the population was measured (rule 1).** (a) `org/projects/*.json` and the mission-tree `project.json` files whose
`placement`/`fabric` names site Z: 12 codes, 6 not closed (COMM_ASSIST, NFRA_MCPINDEX, NFRA_MCPMSP, NFRA_MCPORTAL, NFRA_OPALAI,
NFRA_OPLGTW). (b) The roster's `Working on` for the 10 seats live at 13:0xZ names 5 codes (NFRA_MCPINDEX, NFRA_MCPORTAL,
NFRA_OPLGTW, NFRA_IAMROLES202609, COMM_ASSIST). (c) Non-terminal orders whose `To:` or `By:` is a site-Z lane, or whose worker
belongs to a site-Z-placed project: 24 orders over 11 codes. Site-Z lanes were taken as the 35 serials in the spawn closure of
`0.0.0_AB_MSTR~Z` since 2026-10-06 (`org/mcp/agent-spawn-audit.log`, 173 SPAWN rows); `org/devices/DEVICES.json` lists only
lane letter `Z` for this box (claim `measured`, but it misses ~O, ~MP, ~MI, ~MQ, ~AI and the rest -- a stale register row).
Union = 14 blocks; 2 of them (AMGT_HARVST, MDPF_DEMQUE) are placed on dell1 and enter because site-Z lanes execute their orders.

```yaml
box: sitez
author: 4.0.0_SA_CRO~Z
as_of_utc: 2026-10-13T14:44:20Z
branch_pin: 590f119de8
population:
  register_placed: 6          # 12 codes name site Z in either register; 6 are not closed
  live_seat_named: 5          # roster read 13:0xZ, 10 live seats (0.7.0_AE_CloudOps~ZW respawned 13:09Z, not in that read)
  open_order_named: 11        # 24 non-terminal orders over 11 codes (to-check --all: 152 active orders, 61 projects, 6178 faces)
  union: 14
seats_live: 11                # claude.exe processes at 14:32Z, each naming one serial
seats_by_role: {MSTR: 1, CTO: 1, COO: 2, CVO: 1, CRO: 1, CloudOps: 4, workers_24h: 3, BG_utility: 1}
# COO = ~O (OPLGTW) and ~MP (MCPORTAL); CloudOps = ~Z, ~MI, ~MQ, ~ZW; BG_utility = 0.0.3_BG_BBGTerminal (process alive, broker
# heartbeat ~23 h stale). workers_24h = distinct 0.9.0_WK_ authors of site-Z-placed projects on HEAD in 24 h (NFRA_MCPORTAL
# ~13, ~14, ~15); the 87 worker authors on HEAD in 24 h are mostly other boxes' work arriving through CLOUD.
# Ended today with no process and no KILL line (MSTR~Z): 0.7.0_AE_CloudOps~ZQ, 0.7.0_AE_CloudOps~MP, 2.0.0_SA_COO~AI,
# 2.0.0_SA_COO~MI (and ~ZW, since respawned).
account_state: ok             # weekly-limit stop 2026-10-12 14:15Z-20:27Z (MSTR~Z); 11 seats running at as_of
open_deploy_ledgers: 16       # shared tree box/sitez checkout, tracked + untracked; union over all 20 live worktrees = 93
                              # distinct, 77 of them only on stale linked worktrees (left behind after their act closed)
scheduled_jobs_owned: 17      # 16 Opal Windows scheduled tasks (13 enabled, 3 disabled) + 1 session cron in LIVE_ARMS
                              # (0.0.0_AB_MSTR~Z /govern, hourly). Other seats' session crons were not read (CronList is per session).
open_calls_this_box: 8        # open-calls.py list: 38 rows, 8 OPEN
crossbox_open_to_this_box: 26 # crossbox-call.py list --open: 24 ACKED + 2 OPEN addressed to sitez, of 52 shown / 170 files;
                              # 25 of the 26 are dell1 or dell2 orders to site-Z CloudOps lanes (~ZQ, ~ZW, ~ZV, ~ZC, ~ZG)
```

**Scheduled tasks this box runs (16 Opal-owned, LastTaskResult at the last fire, local ET):** `Opal box-sync` (every 10 min,
0); `Opal open-calls scan` (every 10 min, running); `OPAL_autolaunch_agents` (at logon, 0); `OPAL_BBGTML_daily_pull` (07:00,
**50 today**); `OPAL_BBGTML_freshness_check` (07:30, **2 today**); `OPAL_BLOOMBERG-FreezeTripwire` (every minute, 0);
`OPAL_DEMQUE_bbg_ledger_upload` (08:30, 0); `mdpf-demque-drawer-daily` (10:00, 0); `amgt-induction-daily` (09:00, **4 today**);
`Opal Data Harvest - Continuous Cycle` (running since 04:09); `OPAL_D7_ticket_intake` (every 5 min, **2**); `OPAL_vendor_watch`
(hourly, 0); `OPAL_restore_etf_daily_pull_20261009` (one-shot, 0, no next run); three disabled (`Opal Data Harvest - Local
Publications`, `OpalResearch-ExecManagement`, `OpalResearch-FilingsAnalyzer`).

## Projects

### NFRA_OPLGTW

```yaml
project: NFRA_OPLGTW
macro: D9/NFRA
placement: sitez
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: "yes"
client_surface: "the Opal MCP gateway's Schwab and Black Diamond tools and filtered CSV downloads, used from a work Claude account; the BD fee tool returns client-firm fee data (unsure = yes)"
intent: "A verified Opal employee asks Schwab questions in Claude through the existing gateway and downloads filtered CSVs, with masters kept separate and per-user entitlements enforced."
desired_outcome_when_done: "A named Opal user signs in from a work Claude account and gets accurate, entitlement-scoped Schwab answers and CSVs, with no developer setup."
status:
  round: 35
  dep_stage: EXECUTING
  fwd_realized: "0/18"        # PRD ENDPOINT FWD-1..FWD-19 less FWD-9 = 18; FWD-1..8 last graded HELD (rounds 18-23); rounds 24-34 ruled rows, not FWD grades
  last_l10_utc: 2026-10-11
  open_orders: 2              # to-check --all: OG-ap-11 (0.7.0_AE_CloudOps~Z), OG-ga-1 (worker ~28)
  last_commit_utc: 2026-10-13
seats_on_this_box: [2.0.0_SA_COO~O, 0.7.0_AE_CloudOps~Z, 1.0.0_SA_CTO~Z, 3.0.0_SA_CVO~Z]
dependencies: ["dell2: rows OG-tl-1 and OG-rl-16 graded from dell2 row D2-S30 (round-34 analysis)", "NFRA_MCPORTAL FWD-20 gateway breakdown: Andrew's close condition for this project"]
blockers:
  - what: "OG-bd-1 (deny unprofiled callers of blackdiamond_list_fees) re-cut waits on the admission of 2 unprofiled callers"
    owner: "1.0.0_SA_CTO~Z / 2.0.0_SA_COO~O (Andrew answered yes 2026-10-13 ~14:0xZ, record @90867982ed; site Z call -1b36 still reads OPEN)"
    clears_when: "the 2 callers are admitted by profile and grant, then round 35 E4 ships the deny"
  - what: "project close is held by Andrew until he has seen the full gateway breakdown (vendors, tools and indexes, entitlements)"
    owner: "Andrew (via NFRA_MCPORTAL FWD-20)"
    clears_when: "NFRA_MCPORTAL serves FWD-20 and Andrew reads it"
next: ["round 35 E1: per-family DLQ drain (each 16:00Z silver sweep keeps only its own family's messages)", "round 35 E2/E3: .pptx OG-mu-1 release with key-form statement; Teams bearer holders read then narrow", "round 35 E4: OG-bd-1 deny re-cut on the admission (Andrew yes @90867982ed)"]
andrew_acts: []
footprint:
  commits_7d: 614             # git log --since='7 days ago' --grep=NFRA_OPLGTW HEAD
  seats: 4
  aws_resources_owned: unknown   # not counted this pass: gateway EC2 release, grant-writer lambda, per-family silver sweeps; needs a comp-find --corpus aws read by pipeline
  scheduled_jobs: unknown        # the per-family 16:00Z silver sweeps and the 12:15Z sweep are AWS schedules; not counted per family this pass
  open_deploy_ledgers: 0         # no oplgtw/og-* name in the shared tree's .open_deploys (16 read)
  standing_holds: ["project close held on the MCPORTAL gateway breakdown (Andrew-direct 2026-10-12 ~20:5xZ)", "OG-bd-1 held on the caller admission (now answered yes)"]
if_parked_this_week: "Scheduled gateway sweeps keep firing on the current release; Z-S91 (one family's sweep drains the whole shared DLQ and reports others' failures as its own) stays live; the BD fee deny does not ship, so 2 unprofiled callers keep reading client-firm fee data; COO~O and CloudOps~Z stand down."
cro_rec: KEEP
cro_rec_why: "It is the live client-data surface on site Z with an open entitlement gap (the BD fee deny) that Andrew has just cleared to ship, and its round 35 is already cut."
```

Delivered: round 34 (L10 2026-10-11, @026a983b34) shipped the trunk deploy fix (deploy-to-ec2.sh carries 5 allowlist references, up
from 0) and the CT-i-11 /hx/teams release, read live: COMM_ASSIST channel_poll 29 of 29 failed=0, up from 59 of 59 failing.
Andrew-direct 2026-10-12 ~20:5xZ: "I wouldnt close this project (OPLGTW) until I have seen a full breakdown of the
vendors/channels available via the gateway". Risk: 614 commits in 7 days is the heaviest churn on the box; 0 of 18 FWDs
graded REALIZED after 35 rounds, because the rounds since 24 rule surprise rows rather than grade outcomes.

### NFRA_MCPINDEX

```yaml
project: NFRA_MCPINDEX
macro: D9/NFRA
placement: sitez
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "the gateway's discover family and tool catalog (DATA_CATALOG.yaml), served on the same MCP gateway NFRA_OPLGTW's users reach"
intent: "Every Opal data property is answerable in Claude from one well-indexed catalog: a discover family, purpose-built tools per property, a typed fallback query and on-demand history."
desired_outcome_when_done: "An Opal user asks Claude about any covered property and the gateway routes it to the right purpose-built tool from one catalog, with retired workflows named."
status:
  round: 9
  dep_stage: ROUND_CLOSE
  fwd_realized: "2/19"        # FWD-12 (round 8) and FWD-18 (round 9) REALIZED; latest grade per FWD across 7 analyses
  last_l10_utc: 2026-10-11
  open_orders: 1              # MX-s-19 bd-doc-merge-retire, 0.7.0_AE_CloudOps~MI, PENDING (PHASE B applied; AC2 on 2026-10-19/20)
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~MI, 1.0.0_SA_CTO~Z, 3.0.0_SA_CVO~Z]
dependencies: ["dell2: ADVI_BILLING (billing producer) and NFRA_OPSWKF (trade-rec fund-grain producer) for FWD-19", "2.0.0_SA_COO~C (not on site Z): row Z-S97, 5 of 24 round-close suite failures"]
blockers:
  - what: "FWD-19 the ops lead's readers: no reader cell until a dell2 producer serves"
    owner: "dell2 producers (ADVI_BILLING, NFRA_OPSWKF)"
    clears_when: "either producer serves; the issuer then cuts that one reader"
  - what: "FWD-11 the thread with Alyssa is HELD at Andrew"
    owner: "Andrew"
    clears_when: "Andrew books the session with Alyssa (J1)"
next: ["MX-s-19 AC2 read on 2026-10-19/20, then round 7 L8", "a FWD-19 reader cell when a dell2 producer serves"]
andrew_acts: ["book the FWD-11 thread session with Alyssa (ROUND_ANALYSIS.round9.md @bc8e36fdd5, J1)"]
footprint:
  commits_7d: 178
  seats: 3
  aws_resources_owned: unknown   # catalog and discover release ride the gateway; not counted this pass
  scheduled_jobs: 0
  open_deploy_ledgers: 1         # nfra-mcpindex-r7-bd-doc-retire.json (shared tree), OPEN on its L5 read only
  standing_holds: ["PARKED at ROUND_CLOSE since 2026-10-11 ~15:2xZ, no round 10; un-park on a FWD-19 producer, Andrew booking Alyssa, or MX-s-19's runs"]
if_parked_this_week: "Already parked at ROUND_CLOSE; one deploy ledger stays open until MX-s-19's 2026-10-19/20 read, which CloudOps~MI can run on its date; nothing else rots."
cro_rec: PARK
cro_rec_why: "Every remaining outcome waits on dell2 producers or Andrew's booking, so it needs no seat this week beyond closing its one ledger."
```

Delivered: MX-r-10 shipped the catalog and discover release (live c3af8687e4); FWD-18 REALIZED in round 9, read from the
served catalog (3 of 14 entries name the retired workflow). Andrew-direct 2026-09-17 commissioned it ("expand the tool index in
the Opal MCP Server endpoint"); 2026-10-12 item 6 asked why the producers need dell2 rather than building here, and the
CTO's answer stands until he rules. Risk: Z-S97, the round-close suite reads 19 of 24; until 24 of 24, a verdict is read with
the five known failures beside it.

### COMM_ASSIST

```yaml
project: COMM_ASSIST
macro: D9/COMM
placement: sitez
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: "yes"
client_surface: "drafts in Andrew's name for mail from the five firms (client branch of FWD-4); nothing is sent without his 1"
intent: "Every Teams or Outlook message addressed to Andrew reaches his phone with a draft in his voice, and his text reply routes it."
desired_outcome_when_done: "Andrew answers his Teams and mail from texts, drafts read as his, and every message received is counted against what was texted."
status:
  round: 15
  dep_stage: EXECUTING
  fwd_realized: "0/4"         # FWD-1 APPLIED, FWD-2 BUILT, FWD-3 APPLIED, FWD-4 APPLIED (latest analysis round 14)
  last_l10_utc: 2026-10-11
  open_orders: 0              # to-check --all; round 15 read cell CA-g-1 issued @b97f6de809, no open order face counted
  last_commit_utc: 2026-10-12
seats_on_this_box: [1.0.0_SA_CTO~Z, 3.0.0_SA_CVO~Z]
dependencies: ["NFRA_OPLGTW CT-i-11 gateway release (landed; channel_poll 29 of 29 failed=0)"]
blockers:
  - what: "FWD-3 needs one real channel @mention to reach his phone (round 15 D2)"
    owner: "Andrew"
    clears_when: "anyone @mentions him once in one of the 8 watched channels (call sitez-20261012T210024Z-288f)"
  - what: "FWD-4 internal branch E1 is not exercised: no seat holds a non-Andrew Opal sending identity"
    owner: "Andrew"
    clears_when: "an Opal colleague emails him the CA-e-1 test text, or he names a mailbox a seat may send from (call sitez-20261011T030519Z-058e)"
next: ["CA-g-1 / D2 read: one hour of channel_poll failed=0 plus one real @mention reaching his phone", "E1 mail-day check (check_e1_mail_day.py) once the test mail arrives", "Z-S9 import-test shadowing rides the first cell cut"]
andrew_acts: ["have anyone @mention him once in a watched Teams channel (sitez-20261012T210024Z-288f)", "have one Opal colleague email him the CA-e-1 test text, or name a sending mailbox (sitez-20261011T030519Z-058e)"]
footprint:
  commits_7d: 138
  seats: 2                    # COO 2.0.0_SA_COO~ZZ is the issuer and has no live process at this read
  aws_resources_owned: unknown   # LDO-001 module: teams-global-chat-assist ingress and handler lambdas (infra/aws/terraform/transcripts); not counted
  scheduled_jobs: unknown        # channel_poll runs on a schedule in AWS; count not read
  open_deploy_ledgers: 0
  standing_holds: ["FWD-4 client branch stands as a qualified essential wait (Andrew 'Yes.' 2026-10-11 ~03:2xZ, @5e10dd2dc5)"]
if_parked_this_week: "The deployed ingress and handler keep running and texting Andrew; Z-S13 (the gateway's channel_messages route answers 502 about once every two hours) stays unworked; nothing is sent in his name, so no client harm."
cro_rec: KEEP
cro_rec_why: "Its remaining closes are two Andrew acts of a minute each plus one read, and it is the channel Andrew named for ad hoc work (2026-10-13 record @90867982ed), so it costs almost nothing to finish this week."
```

Delivered: round 14 (L10 2026-10-11) D1 APPLIED c583d4f9e5, live function carrying round 13 (five parties pinned,
channel_poll names its failure); since the gateway /hx/teams release, channel_poll reads 29 of 29 failed=0 with 8 channels
(row Z-S12, @7f492465d7). Andrew-direct 2026-10-13 ~14:0xZ: the "bid" is for ad hoc fixes arriving through this channel,
approved at his discretion there. Moved laptop -> site Z 2026-10-09 (record ANDREW_DIRECT_20261009_061xZ_COMM_ASSIST_MOVES_TO_SITEZ.md).

### NFRA_IAMROLES202609

```yaml
project: NFRA_IAMROLES202609
macro: D12/NFRA
placement: sitez
status_register: complete
repos: [ajb_workspace, aws-infra]
client_facing: "no"
client_surface: "none"
intent: "Know and shrink the estate's IAM posture: every role in code or owned, unused permissions measured, a narrowing's breakage known in advance."
desired_outcome_when_done: "Every IAM role is declared, exempt or owned, and a permission can be narrowed with its breakage known beforehand, re-runnable without hand work."
status:
  round: 9
  dep_stage: CLOSED
  fwd_realized: "8/8"
  last_l10_utc: 2026-10-13
  open_orders: 0
  last_commit_utc: 2026-10-13
seats_on_this_box: []
dependencies: []
blockers: []
next: []
andrew_acts: []
footprint:
  commits_7d: 251
  seats: 0                    # COO 2.0.0_SA_COO~ZI has no live process; CTO~Z and CVO~Z hold no further act
  aws_resources_owned: 0      # roles adopted into Terraform belong to their owning roots (16 of 16 rows owned at close)
  scheduled_jobs: 0
  open_deploy_ledgers: 0      # iamroles-r9-narrow-schwab.json only on one linked worktree, not the shared tree
  standing_holds: []
if_parked_this_week: "nothing rots; safe to park (already closed: NEVER-2 entry closed, no rollback used)."
cro_rec: CLOSE
cro_rec_why: "8 of 8 outcomes are REALIZED and the CTO ruled it closed at round 9's L10, as Andrew asked ('I think this one can be wound down/closed')."
```

Delivered: round 9 L10 2026-10-13 @d00d438bc4 rules CLOSED: 8 of 8 FWDs REALIZED; at close 16 of 16 role rows are owned
(8 declared, 5 exempt, 2 deferred with a reopen condition, 1 retired, 0 unowned). project.json reads status closed /
dep_stage CLOSED (the register enum here maps to `complete`). Andrew-direct 2026-10-12 ~20:5xZ: "Dell boxes should not be
curtailed ... I think this one can be wound down/closed"; Addendum 1 (dell agents' invoke narrowing) was withdrawn.
One linked worktree still carries an open ledger name (iamroles-r9-narrow-schwab.json); verify it closed before GC.

### NFRA_MCPORTAL

```yaml
project: NFRA_MCPORTAL
macro: D6/NFRA
placement: sitez
status_register: active
repos: [ajb_workspace, mcportal, aws-infra]
client_facing: "no"
client_surface: "mcp.opalinvest.dev (Control Plane, Open Calls, MCP Server pages) -- Andrew only, /sprint any Opal staff login; no partner-firm or client login"
intent: "One operator console at mcp.opalinvest.dev where Andrew sees and steers the fabric: per-person MCP grants, the call log, the kill switch, every box's projects, git state and open calls."
desired_outcome_when_done: "Andrew runs grants, open calls and the gateway's vendor/tool/entitlement picture from one page instead of asking seats."
status:
  round: "GW r1 (main line r5; C17 r2 cut pending E1)"
  dep_stage: EXECUTING
  fwd_realized: "0/20"          # last full board: ROUND_ANALYSIS.round4.md (0 REALIZED / 3 NOT_REALIZED / 16 DEFERRED of 19; PRD v0.7 adds FWD-20)
  last_l10_utc: 2026-10-12       # ROUND_ANALYSIS.c17-round1.md ~14:2xZ @53231d51ee (grades no FWD); last board 2026-10-09 ~01:3xZ @460bc0af2f
  open_orders: 7                 # to-check --all: 6 ACTIVE, 1 PENDING (MP-c-2, q-1, v-2, x-5, z-4, z-5 + 1)
  last_commit_utc: 2026-10-13T12:04Z
seats_on_this_box: [2.0.0_SA_COO~MP, 0.7.0_AE_CloudOps~MQ, 1.0.0_SA_CTO~Z, 3.0.0_SA_CVO~Z]
dependencies: ["NFRA_OPLGTW gateway release queue (MCPORTAL ships through the opal-gateway host)", "NFRA_MCPINDEX ledgers on the same gateway queue"]
blockers:
  - what: "MP-z-4 dynamodb:Scan grant re-cut to a fresh lane after 0.7.0_AE_CloudOps~MP hung"
    owner: "0.7.0_AE_CloudOps~MQ"
    clears_when: "z-4 applied under its never-widen pair; then MP-z-5 release on G-REL3"
next: ["MP-z-4 Scan grant on gateway-access-state-table (0.7.0_AE_CloudOps~MQ)", "MP-z-5 release of the Gateway breakdown page (G-REL3)", "MP-z-6 close run: Andrew reads the breakdown (G-SEE3)"]
andrew_acts:
  - "Open https://mcp.opalinvest.dev/control-plane once and name one box's projects (open call sitez-20261009T173038Z-21c5, G-SEE, FWD-14)"
  - "Sign in once as the second (non-owner) account in MP-v-2's headed window (sitez-20261009T173040Z-f0d2, G-2ND, FWD-2)"
  - "Open /control-plane and /open-calls once and close one real call (sitez-20261011T000025Z-8ed7, G-SEE2)"
footprint:
  commits_7d: 171                # git log --since='7 days ago' --grep=NFRA_MCPORTAL HEAD
  seats: 4
  aws_resources_owned: unknown   # no per-project ownership tag in the served graph; its pages ride NFRA_OPLGTW's gateway host
  scheduled_jobs: 0              # 0 of 215 scheduled tasks on this box name it
  open_deploy_ledgers: 0         # nfra-mcportal-cp2-release CLOSED 2026-10-10 23:12Z; copies remain only in 7 stale linked worktrees
  standing_holds: ["MP-c-2 on G-CLOSE (Alyssa's sitting, Andrew's hold)", "C17 E1 cut may proceed: CONSENT on five conditions given 2026-10-13 @b5ce7b2966 (4.0.0_SA_CRO~Z)"]
if_parked_this_week: "MP-z-4 stays unapplied (nothing half-landed), the gateway breakdown Andrew named as MCPORTAL's first outcome is not delivered, and NFRA_OPLGTW cannot close because its close waits on that breakdown (ruling 2026-10-12 item 2); live pages keep serving; seats freed: 2.0.0_SA_COO~MP, 0.7.0_AE_CloudOps~MQ."
cro_rec: KEEP
cro_rec_why: "It carries the one outcome Andrew named first on 2026-10-12 (the gateway breakdown that gates OPLGTW's close), half the GW round is already drained, and it is Opal-internal so it costs no client risk."
```

Delivered: the Control Plane page LIVE since 2026-10-09 ~16:12Z (MP-x-4 drained @a933da0d8a); CP2 (Overlap, Git state, Open Calls)
LIVE since 2026-10-10 23:04Z on gateway 2a5966dfbd (MP-r-2 complete @937a9e38a4). GW round 1: MP-z-1 @fda2ca67a3, MP-z-2
@bcddb3e6b0 (mcportal 6fbd25e), MP-z-3 @7218b1e3ae drained (COO~MP summary 2026-10-13). Runs under Andrew-direct 2026-10-12
~20:5xZ (ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md items 2/4): the gateway breakdown is the first
distinct outcome, cut ahead of every other open order. Risk: four of seven open orders wait only on Andrew acts of 1-3 minutes
each (three open calls above, one Alyssa sitting); FWD board has read 0 REALIZED since round 1. Gitstate cold read 7.6 s against a
10 s safety bar (c17-round1), margin narrowing as the write rate grows.

### NFRA_MCPMSP

```yaml
project: NFRA_MCPMSP
macro: D6/NFRA
placement: sitez
status_register: inactive        # register value is "hold" (no status enum); Andrew-direct 2026-10-12 ~20:5xZ item 7
repos: [ajb_workspace, aws-infra]
client_facing: "yes"
client_surface: "a Teams agent answering partner-firm users (Inflection and Cottonwood first) from each firm's own data -- NOT live; no partner sender has been served"
intent: "One Opal-hosted Teams analyst that partner-firm staff can ask questions of, answering only from that firm's data through a central gateway that assumes the firm's AWS role per request."
desired_outcome_when_done: "A partner-firm user on an allowlisted domain asks the agent in Teams and gets an answer from their own firm's data, and no other firm's."
status:
  round: 3
  dep_stage: ROUND_CLOSE
  fwd_realized: "0/11"          # ROUND_ANALYSIS.round1.md tally 0 REALIZED / 2 HELD / 9 NOT_REALIZED (denominator 11); rounds 2-3 analyses grade no FWD REALIZED
  last_l10_utc: 2026-10-09       # ROUND_ANALYSIS.round3.md ~09:2xZ @2016db240c, enrichment list EMPTY
  open_orders: 0
  last_commit_utc: 2026-10-09T09:34Z
seats_on_this_box: []            # 2.0.0_SA_COO~MS (issuer) holds no process on this box at as_of
dependencies: ["G-MSPID: the MSP calling identity, supplied and signed in by Andrew", "NFRA_MCPORTAL register_tenant (sole writer of the tenant_firm record, PRD v0.4 C4)"]
blockers:
  - what: "HOLD on Andrew's word -- 'a project to address downstream of where we are at now'"
    owner: "Andrew"
    clears_when: "Andrew's word to un-hold; then G-MSPID answered, and 2.0.0_SA_COO~MS re-cuts MS-sv-1/rn-1/rx-1, then FWD-6/7"
next: ["nothing this week (held)"]
andrew_acts: []
footprint:
  commits_7d: 19                 # git log --since='7 days ago' --grep=NFRA_MCPMSP HEAD
  seats: 0
  aws_resources_owned: unknown   # MS-d-2 release LIVE (2c0f84966d) and MS-dn-1 Deny APPLIED stand; no per-project tag census made
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: ["HOLD, Andrew-direct 2026-10-12 ~20:5xZ item 7", "G-MSPID ('Not yet' 2026-09-30; 'doesnt matter right now' 2026-10-01)"]
if_parked_this_week: "nothing rots; safe to park -- already held, no open orders, no ledger, no scheduled job; the applied Deny and the MS-d-2 release stay as they are."
cro_rec: PARK
cro_rec_why: "Andrew already held it as downstream work and every remaining outcome needs his G-MSPID identity, so it should stay parked with no seat attached."
```

Delivered: round 2 put MS-d-2 LIVE (2c0f84966d) and the MS-dn-1 Deny APPLIED (project.json PRIOR 2026-10-01); round 3 merged
MS-s-2 @4ddac69190 and MS-rr-1 @f3684818f7 (closed 2026-10-09). Runs under Andrew's channel rulings of 2026-09-30 (pilot
federated chat, production multi-tenant bot) and the sender allowlist (four Opal and partner domains). It is the only
client-facing project in this file and it is not live. Status note: the register value "hold" is not in the form's
status_register set; carried here as `inactive`, the closest value, with the source word in the comment.

### NFRA_OPALAI

```yaml
project: NFRA_OPALAI
macro: D6/NFRA
placement: sitez
status_register: active
repos: [ajb_workspace, opal_ai]
client_facing: "no"
client_surface: "the Opal Analyst in Teams for Opal staff (asker profiles: Andrew, Alyssa); no partner-firm or client login"
intent: "The Opal Analyst as a product: one Teams-facing agent over one indexed Opal MCP, built in the opal_ai repo and run from a released copy under a non-admin account with no workspace access."
desired_outcome_when_done: "An Opal colleague asks the Analyst a routine question in Teams and gets the same answer they would get in their own Claude, inside their entitlements."
status:
  round: 2
  dep_stage: EXECUTING
  fwd_realized: "0/13"          # ROUND_ANALYSIS.round1.md: 0 REALIZED / 4 HELD / 9 NOT_REALIZED; round 2 has not reached L10
  last_l10_utc: 2026-09-28       # @a8baa4b23d
  open_orders: 3                 # OA-e-8, OA-t-1, OA-t-3 (all PENDING, gated behind the item-0 close run)
  last_commit_utc: 2026-10-12T21:37Z
seats_on_this_box: [1.0.0_SA_CTO~Z]   # issuer 2.0.0_SA_COO~AI holds no process since ~12:2xZ 2026-10-13 (MSTR~Z, no KILL line)
dependencies: ["NFRA_OPLGTW gateway (opal_asker_query served on r29)", "NFRA_MCPINDEX (the indexed MCP the Analyst reads)", "NFRA_MCPORTAL Entitlements tab (FWD-8 is graded against it)"]
blockers:
  - what: "close-run arm (a): Alyssa's own asker question has not arrived (Monday ask sent 2026-10-12 14:04Z, poll closed without firing)"
    owner: "Andrew"
    clears_when: "Andrew's sitting with Alyssa on 2026-10-13 (ruling 2026-10-12 item 3) produces her question to the Opal Bloomberg account"
next: ["item-0 close run grades arm (a)", "OA-t-1 / OA-t-3 parent halves and the ajb.ps1 BG retirement (PRD C11)", "OA-e-8 speed-stage measure"]
andrew_acts:
  - "Sit with Alyssa on the Analyst (Andrew-direct 2026-10-12 ~20:5xZ item 3: 'I will handle this with Alyssa tomorrow')"
  - "Send one Teams message from his account to the Opal Bloomberg account (open call sitez-20261009T170635Z-a519; he answered 'later')"
footprint:
  commits_7d: 80                 # git log --since='7 days ago' --grep=NFRA_OPALAI HEAD
  seats: 1
  aws_resources_owned: unknown   # its served path is NFRA_OPLGTW's gateway; no per-project tag census made
  scheduled_jobs: 0              # 0 of 215 scheduled tasks on this box name the Analyst
  open_deploy_ledgers: 0
  standing_holds: ["Andrew's 2026-10-06 hold on call 1 (arm (a) sits behind it)", "no seat messages Alyssa (laptop CTO ruling @441f2f547d)"]
if_parked_this_week: "nothing rots on the seat side: the three pending orders stay gated on the close run, opal_ai PROD stays at its last release, no ledger or job is open; the cost is that the result of Andrew's Alyssa sitting has no live issuer to grade it until re-seated."
cro_rec: PARK
cro_rec_why: "Its only remaining input is Andrew's own sitting with Alyssa, so a live COO seat would only wait; park it and re-seat 2.0.0_SA_COO~AI the day that sitting yields her question."
```

Delivered: opal_ai PROD 9c0a80b8d0 (G-PUSH done 2026-10-01); close-run arm (b) PASS on gateway r29 on 2026-10-09 (a fresh
un-profiled sender got the how-to-get-access answer, no data read; @349edef03b, disarm row Z-S71 @aa266008dd). Runs under
Andrew-direct 2026-09-24 (one repo opal_ai, CI in it, develop in the workspace and run without workspace access) and the
2026-10-12 item 3. Risk: the Analyst's live process could not be read (Opal_Agent processes need an elevated read), so whether
it is serving right now is unknown. The round-1 board is 15 days old; round 2 has 3 of its orders still pending.

### OPAL_BBGTML

```yaml
project: OPAL_BBGTML
macro: NONE/OPAL                 # no directive (closed 2026-08-25 spring clean: not attached to DIRECTIVES.yaml)
placement: NONE
status_register: NONE            # register reads "closed"; the code still carries live work (below)
repos: [ajb_workspace, aws-infra]
client_facing: "indirect"
client_surface: "served model-portfolio benchmark figures (model_portfolio_benchmarks.json from the yang-pipeline) shown on portal Model Portfolios pages"
intent: "The daily Bloomberg terminal pull for the model-portfolio exposure dashboard (pull -> validate -> /data-refresh upload) and the guards that stop a stale benchmark series being served."
desired_outcome_when_done: "Every trading day the terminal pull lands, the freshness check passes, and no stale benchmark number reaches a served page."
status:
  round: none                    # fix-route orders outside the canonical pipeline (TO-GUARD-1..4, CTO fix route @58e472b0b6)
  dep_stage: none
  fwd_realized: "n/a"            # closed project, no PRD outcome table
  last_l10_utc: none
  open_orders: 1                 # TO-GUARD-4, PENDING, to 0.7.0_AE_CloudOps~RV
  last_commit_utc: 2026-10-11T03:43Z
seats_on_this_box: [0.0.3_BG_BBGTerminal]   # process alive (pid 20640), broker heartbeat stale ~23 h at 13:1xZ
dependencies: ["Bloomberg DAPI on this terminal machine (today's 07:00 ET pull FAILED with DAPI down, MSTR~Z)", "MDPF_DEMQUE (dell1) meters the pull's budget and runs OPAL_DEMQUE_bbg_ledger_upload here"]
blockers:
  - what: "TO-GUARD-4 built and proved on branch rv-bbgtml-guard4 (AC1 PASS, five arms, 3b65362444) but not merged: Andrew's no-modify order on integrations/bloomberg/ was lifted for GUARD-3's two edits only"
    owner: "Andrew"
    clears_when: "Andrew's merge word on open call sitez-20261013T021538Z-2da6"
  - what: "OPAL_BBGTML_daily_pull LastTaskResult 50 at 2026-10-13 07:00 ET; OPAL_BBGTML_freshness_check LastTaskResult 2 at 07:30 ET"
    owner: "0.0.3_BG_BBGTerminal"
    clears_when: "DAPI back up and a re-run or the 2026-10-14 07:00 ET run lands with freshness PASS"
next: ["read today's failed 07:00 ET pull and re-run once DAPI is up (0.0.3_BG_BBGTerminal)", "merge TO-GUARD-4 on Andrew's word", "give the code a live register home"]
andrew_acts:
  - "Merge word on TO-GUARD-4 (open call sitez-20261013T021538Z-2da6)"
footprint:
  commits_7d: 40                 # git log --since='7 days ago' --grep=OPAL_BBGTML HEAD (includes MDPF_DEMQUE/MDPF_SECHIST commits that name it)
  seats: 1
  aws_resources_owned: unknown   # the stale-benchmark guard lives in yang-pipeline (TO-GUARD-1 live 2026-10-06); no per-project tag census made
  scheduled_jobs: 3              # OPAL_BBGTML_daily_pull (07:00 ET), OPAL_BBGTML_freshness_check (07:30 ET), OPAL_BLOOMBERG-FreezeTripwire (every minute)
  open_deploy_ledgers: 0         # bbgtml-guard3-checker-tripwire-merge-20261007 CLOSED 2026-10-07; copy remains only in 1 stale linked worktree
  standing_holds: ["Andrew's no-modify order on integrations/bloomberg/ (lifted for GUARD-3 only)"]
if_parked_this_week: "the three scheduled tasks keep firing on their own (07:00 and 07:30 ET daily, the tripwire every minute); with no seat tending them a failed pull like today's goes unread and the served benchmark figures go stale on a client-facing page; the GUARD-4 branch ages."
cro_rec: KEEP
cro_rec_why: "It is the live daily Bloomberg feed behind served benchmark figures and it failed this morning, so it must stay tended; its register row should be re-opened or re-homed so the work stops running under a closed code."
```

Delivered: TO-GUARD-1 stale-benchmark guard LIVE 2026-10-06 (AC1-AC3 PASS, @49103d5f96; 171 wrong served numbers stopped);
TO-GUARD-3 checker and tripwire merged 2026-10-07 09:54Z with the first live read PASS on both arms (@7f22fe3cf6). WHICH CODE
CARRIES THE WORK: OPAL_BBGTML itself, though its register row reads closed (spring clean 2026-08-25, "we can reinvent a project").
The guard orders run as seat acts on a closed project on 1.0.0_SA_CTO~Z's fix route (TO-GUARD-4 face, pipeline-override line);
the pull is operated by 0.0.3_BG_BBGTerminal through /bbg-daily and /terminal-upload; MDPF_DEMQUE (dell1) only meters its budget
and MDPF_SECHIST reads its output. Risk: a closed code with 3 live scheduled jobs and no live issuer (2.0.0_SA_COO~Z has no process).

### AMGT_HARVST

```yaml
project: AMGT_HARVST
macro: D5/AMGT
placement: DELL1
status_register: active
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none client-facing; feeds the AMGT research Chatter axis (Opal-internal research surface, read from the PRD name)"
intent: "Retrieve every publication mention of a covered company with its provenance, kept as received and graded by strength over time."
desired_outcome_when_done: "The research app's Chatter axis and the company event spine are fed continuously by a harvest whose every row traces to its source."
status:
  round: 83
  dep_stage: EXECUTING
  fwd_realized: "8/17"
  last_l10_utc: 2026-10-13
  open_orders: 6
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~ZW, 2.0.0_SA_COO~H]
dependencies: ["site Z runner host (scheduled task 'Opal Data Harvest - Continuous Cycle')", "Andrew's WSJ/Barron's sign-in (HVST-bx-4)", "dell1 CTO/CVO/COO~W1 for analysis and issuance"]
blockers:
  - what: "9 of 17 FWD outcomes are NOT REALIZED as a qualified wait on Andrew's presence (FWD-1, 3, 7, 9, 10, 11, 13, 14, 15; board unchanged since round 47)"
    owner: "Andrew"
    clears_when: "Andrew is present for the collection run's sign-in acts (HVST-bx-4)"
  - what: "Z-S115 ARMED: one click in the runner's console window stalls the producer silently"
    owner: "2.0.0_SA_COO~W1"
    clears_when: "round 84 cuts bz-3a/3b (windowless runner) and it deploys at a cycle boundary on site Z"
next: ["round 84 bz-3a/3b: launch the site Z runner windowless (Z-S115 prevention)", "W135-S2 close read at the first ended cycle under pin 1c69fa35a3", "close or re-issue bo-1/bp-1 (issued 2026-10-08 to workers ~122/~123, status still issued)"]
andrew_acts: ["WSJ/Barron's sign-in, HVST-bx-4 (ledger/ROUND_ANALYSIS.round83.md s.4)"]
footprint:
  commits_7d: 567
  seats: 2
  aws_resources_owned: unknown
  scheduled_jobs: 1
  open_deploy_ledgers: 1
  standing_holds: ["harvst-bs3-zw-runner-20261009 HELD-SOVEREIGN-GATED (site Z runner pin)", "ft held on Andrew's word (round 46)"]
if_parked_this_week: "The site Z scheduled task 'Opal Data Harvest - Continuous Cycle' (running since 08:09Z today) keeps collecting on pin 1c69fa35a3 with the Z-S115 console-stall hazard unprevented, so a stall goes unnoticed unless ~ZW keeps its hourly log read; ledger harvst-bs3-zw-runner stays open; bo-1/bp-1 and bz-5/6/7 stay issued."
cro_rec: PARK
cro_rec_why: "The board has sat at 8/17 since round 47 with the other 9 waiting on Andrew, and the recent rounds are runner upkeep; leave the collector running on its pin, cut only the Z-S115 windowless fix, and stop issuing rounds until Andrew can give the sign-in."
```

Delivered: FWD-17 re-confirmed REALIZED at round 46 (699 = 233 x 3); round 83 analysis 2026-10-13 ~06:5xZ by 1.0.0_SA_CTO~DELL1 grades the site Z runner re-pin (bz-1) PINNED-AND-RUNNING. Box of record is dell1; site Z carries the runner host, the ~ZW applier lane (bz-5/6/7) and the open runner ledger. ~ZW had no process from ~12:2xZ today and was respawned 13:09Z by 0.0.0_AB_MSTR~Z; bo-1/bp-1 (to workers ~122/~123 by 2.0.0_SA_COO~H, 2026-10-08) look abandoned since the issuing COO is now ~W1 -- not verified, the issuer's read. client_facing is "no" on the basis that the research surface is staff-only; dell1's CRO should confirm.

### MDPF_DEMQUE

```yaml
project: MDPF_DEMQUE
macro: D8/MDPF
placement: DELL1
status_register: active
repos: [ajb_workspace]
client_facing: "indirect"
client_surface: "daily prices that value holdings on the Model Portfolios client pages (FWD-1's last hop, not yet connected per round 8 ADDENDUM 4)"
intent: "Price, rank and draw every history backfill inside the Bloomberg and Yahoo budgets without crowding out a production pull."
desired_outcome_when_done: "Backfills land through one queue on budget, and a live client's holdings are valued on the client pages from the drawn prices."
status:
  round: 8
  dep_stage: EXECUTING
  fwd_realized: "1/9"
  last_l10_utc: 2026-10-12
  open_orders: 2
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~ZQ]
dependencies: ["Bloomberg DAPI on site Z (the 07:00 ET run FAILED today with DAPI down)", "dell1 COO 2.0.0_SA_COO~Q1 for round 9 issuance"]
blockers:
  - what: "TO-DQ-t34 (site Z drawer closes completed requests, risk WORLD) pending; its lane ~ZQ has had no process since ~12:2xZ today"
    owner: "2.0.0_SA_COO~Q1"
    clears_when: "~ZQ is respawned or t34 is re-cut to a live site Z lane, and ledger mdpf-demque-zq-t34-close closes"
next: ["round 9 (R1 a/b): standing daily extension to T-1 under its never-widen pair", "round 9 R1 (c): the 76-trading-day backfill through the queue", "FWD-3 ACCEPT read on a production morning run"]
andrew_acts: []
footprint:
  commits_7d: 332
  seats: 1
  aws_resources_owned: unknown
  scheduled_jobs: 2
  open_deploy_ledgers: 1
  standing_holds: []
if_parked_this_week: "Two site Z scheduled tasks keep firing on their current code: mdpf-demque-drawer-daily (14:00Z daily, last rc=0) and OPAL_DEMQUE_bbg_ledger_upload (12:30Z daily, last rc=0); ledger mdpf-demque-zq-t34-close (OPEN since 2026-10-11 18:53Z) stays open with no live lane; BBG_ACTUALS.jsonl carries an uncommitted local edit in the shared tree."
cro_rec: KEEP
cro_rec_why: "It is the budget guard on the Bloomberg pulls that feed client-page prices, and site Z holds two of its scheduled jobs and an open ledger that should not be left without a live lane."
```

Delivered: FWD-4 REALIZED at round 6 (a pre-flight request quoted then drawn ON_TIME); the t24 backfill drew 5,858 of 5,858 cells on 2026-10-10 (FWD-3 APPLIED, not REALIZED). Round 8 ADDENDUM 4 traced that no client page reads the file yet, so FWD-1's last hop is unconnected. Box of record is dell1; site Z carries the drawer host, the BBG ledger upload and lane ~ZQ. The PRD's outcome count (9) is read from FWD ids in MDPF_DEMQUE_PRD.md; only FWD-3 and FWD-4 were graded in rounds 4-8.

### D12_PHONE_OTP_ALL_AWS

```yaml
project: D12_PHONE_OTP_ALL_AWS
macro: D12/PLATFORM_OPS
placement: NONE
status_register: active
repos: [ajb_workspace, portal, aws-infra]
client_facing: "yes"
client_surface: "client portal sign-in: SMS as a second channel for the login code, plus the post-login phone enrolment card on /market"
intent: "Deliver the client portal's login code by SMS through AWS End User Messaging, alongside the email channel."
desired_outcome_when_done: "A client can enrol a verified phone and receive the login code by SMS."
status:
  round: none
  dep_stage: EXECUTING
  fwd_realized: "unknown"
  last_l10_utc: none
  open_orders: 1
  last_commit_utc: 2026-09-10
seats_on_this_box: []
dependencies: ["AWS toll-free number provisioning and carrier verification (SP-1)", "Andrew's verification fields and sign-off on the carrier-verification text"]
blockers:
  - what: "SP-1 provisioning and carrier verification HELD; nothing provisioned"
    owner: "Andrew"
    clears_when: "Andrew supplies the verification fields and signs the carrier-verification text, held at 1.0.0_SA_CTO~Z"
next: ["SP-1 provisioning on Andrew's fields", "SF-2 phone capture UI completion", "SF-1 enable after a delivered test SMS"]
andrew_acts: ["supply the toll-free verification fields and sign the carrier-verification text (org/projects/D12_PHONE_OTP_ALL_AWS.json blocking)"]
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 1
  standing_holds: ["d12-sms-origination-identity-activation HELD-SOVEREIGN-GATED since 2026-09-02"]
if_parked_this_week: "Nothing rots: the SB backend is deployed inert (SB-1..9, 2026-09-01) and the email channel is unaffected; the open ledger stays HELD-SOVEREIGN-GATED as it has for 41 days; order SF-SITEZ stays open with no live assignee."
cro_rec: PARK
cro_rec_why: "Zero commits in 7 days, the only gate is Andrew's SP-1 fields, and the backend sits inert and safe, so it costs nothing to park and should restart only when he supplies the fields."
```

Delivered: SB backend deployed inert and certified E1-E8 PASS on 2026-09-01; SF-3 done @portal 17c9a829. It enters this report only through order SF-SITEZ (to 0.4.0_DE_ClientPlatform~Z by 2.0.0_SA_COO~Z, issued 2026-09-01, last commit 2026-09-01), which is live-but-gated, not rot: its status line says it stays open until SF-2 lands and SF-1's gate is met. Neither its assignee nor its issuer has a process on site Z today. No PRD outcome table was found, so fwd_realized is unknown. Register placement is absent (no placement key).

### D1_CATVIEWS

```yaml
project: D1_CATVIEWS
macro: D1/MDPF
placement: NONE
status_register: active
repos: [ajb_workspace]
client_facing: "yes"
client_surface: "Model Portfolios category views (Models, SMA, Alternatives, Insurance, Client) on the client portal"
intent: "Serve the ruled five-category taxonomy and view tree end to end, with every per-firm producer resolving membership through one registry."
desired_outcome_when_done: "Every firm's model portfolios appear under the ruled categories, resolved from the one registry."
status:
  round: none
  dep_stage: EXECUTING
  fwd_realized: "unknown"
  last_l10_utc: none
  open_orders: 1
  last_commit_utc: 2026-09-27
seats_on_this_box: []
dependencies: ["mdpf gold Lambda path-to-live (D1-i-1, D1-i-2)"]
blockers:
  - what: "order TO-N1-DS stuck at 7 of 8 PASS with AC7 UNCOMPUTABLE since 2026-08-29; no seat has touched it since"
    owner: "2.0.0_SA_COO~Z"
    clears_when: "the issuer (or the D1 COO) flips the order terminal or re-cuts AC7 to a computable read"
next: ["issuer reads AC7 and flips TO-N1-DS complete or superseded", "confirm with the D1/MDPF owner whether D1_CATVIEWS itself is still live work"]
andrew_acts: []
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots on site Z: the order is built, on origin and 7 of 8 scored; it simply keeps showing as ACTIVE on the board."
cro_rec: CLOSE
cro_rec_why: "Its only site Z thread is a 46-day-old order whose build landed and scored 7 of 8 on 2026-08-29, so the order should be flipped terminal by its issuer; whether the D1 project itself continues is the D1 owner's call, not site Z's."
```

Delivered: TO-N1-DS proof of spec scores 8 rows, 7 PASS + 1 UNCOMPUTABLE, 0 FAIL (org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D1_CATVIEWS.TO-N1-DS_PROOF_OF_SPEC.json, last commit 2026-08-29). The order (issued 2026-08-28 by 2.0.0_SA_COO~Z to 0.4.0_DS_ClientPlatform~Z) is ROT on site Z: last commit 2026-08-29, neither seat live. The flip to terminal is the issuer's (2.0.0_SA_COO~Z) or, with no live issuer, the D1/MDPF COO's. CLOSE here means close the site Z order; the project's own status is not measured here.

### ETFS_POSITIONING

```yaml
project: ETFS_POSITIONING
macro: D4/ETFS
placement: NONE
status_register: complete
repos: [ajb_workspace, aws-infra]
client_facing: "yes"
client_surface: "ETF Positioning page (DIVZ/IDVZ/PFDE/PFOE with a Models-to-ETFs toggle)"
intent: "Render the four ETFs in the existing Positioning page shape with a Models/ETFs toggle."
desired_outcome_when_done: "The ETF Positioning page is promoted to PROD on Andrew's word once ETFS_INGEST discharges its two conditions."
status:
  round: none
  dep_stage: CLOSED
  fwd_realized: "unknown"
  last_l10_utc: none
  open_orders: 2
  last_commit_utc: 2026-10-07
seats_on_this_box: []
dependencies: ["ETFS_INGEST done (the two promote conditions)", "Andrew's PROD promote word"]
blockers: []
next: ["flip TO-13-DS and TO-14-AE terminal (the identifier repair applied 2026-08-29)"]
andrew_acts: []
footprint:
  commits_7d: 3
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots: the project is complete and the repair was applied 2026-08-29; the two orders keep showing ACTIVE on the board."
cro_rec: CLOSE
cro_rec_why: "The register already reads complete and both open orders describe a repair applied and scored on 2026-08-29, so they are stale faces that only inflate the open count."
```

Delivered: TO-14-AE APPLIED 2026-08-29T14:17Z by 0.7.0_AE_CloudOps~N, AC1-AC3 PASS (AC3 scored on the scheduled 22:00Z fire, silver/holdings/2026-08-29.parquet); AC4 rides a named later run. TO-13-DS (to 0.4.0_DS_ClientPlatform~Y) and TO-14-AE (to 0.7.0_AE_CloudOps~N), both issued 2026-08-29 by 2.0.0_SA_COO~Z, last touched 2026-08-29: ROT. The flip to terminal is the issuer's (2.0.0_SA_COO~Z) or the D4/ETFS COO's. The 3 commits in 7 days name the project but were not opened.

### NFRA_C3MATERIALIZE

```yaml
project: NFRA_C3MATERIALIZE
macro: D11/NFRA
placement: NONE
status_register: closed
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Materialize identity from four per-plane views up to an L4 identity layer (the C3 layer)."
desired_outcome_when_done: "A materialized identity layer with a certified bridge determination."
status:
  round: none
  dep_stage: EXECUTING
  fwd_realized: "unknown"
  last_l10_utc: none
  open_orders: 1
  last_commit_utc: 2026-10-03
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip TO-L3S7A-CCY terminal (cancelled or superseded, citing the 2026-09-23 close)"]
andrew_acts: []
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots: the project closed 2026-09-23; one pending order face remains."
cro_rec: CLOSE
cro_rec_why: "The register closed it on 2026-09-23 and the one pending order (last commit 2026-08-30) is an orphan face that should be flipped terminal with a pointer."
```

Delivered: the register reads closed 2026-09-23 while dep_stage still reads EXECUTING (a register inconsistency, not measured further). TO-L3S7A-CCY (issued by 2.0.0_SA_COO~X, carries no issued_to tag, status pending, last commit 2026-08-30) is ROT. 2.0.0_SA_COO~X is in the site Z spawn closure; the flip to terminal is the issuer's (~X) or the NFRA owner's, citing the close. The order has no `<issued_to>` tag; to-check reads its assignee 0.8.0_AE_CloudComp~X from another field.

## Box-level closing (site Z)

**Tally:** 14 blocks -- KEEP 5 (NFRA_OPLGTW, NFRA_MCPORTAL, COMM_ASSIST, OPAL_BBGTML, MDPF_DEMQUE), PARK 5 (NFRA_MCPINDEX,
NFRA_MCPMSP, NFRA_OPALAI, AMGT_HARVST, D12_PHONE_OTP_ALL_AWS), CLOSE 4 (NFRA_IAMROLES202609, D1_CATVIEWS, ETFS_POSITIONING,
NFRA_C3MATERIALIZE). Six of the seven active site-Z projects run under Andrew's 2026-10-12 rulings (record @cdb5ff66b1).
- **Hurts most if stopped:** (1) OPAL_BBGTML: the daily Bloomberg pull behind served benchmark figures; it failed today (pull
  rc 50, freshness rc 2), and the work runs under a code the register reads closed. (2) NFRA_OPLGTW: the live gateway on client
  data, with the fee-data deny for 2 unprofiled callers ready to ship on Andrew's yes. (3) MDPF_DEMQUE: dell1's project, but site Z
  runs its two scheduled tasks and holds its open ledger `mdpf-demque-zq-t34-close` on lane ~ZQ, which has no process.
- **Could stop today with no loss:** the 4 CLOSE items (IAMROLES 8/8 and closed; D1_CATVIEWS, ETFS_POSITIONING and C3MATERIALIZE
  are 5 order faces 23-46 days old whose work is done or closed -- their issuers flip them terminal), plus NFRA_MCPMSP, already held.
- **Seats freed by the recs:** COO 0 live (2.0.0_SA_COO~AI and ~MI, the issuers of the two parked NFRA projects, already have no
  process); CloudOps up to 2 (0.7.0_AE_CloudOps~MI after MX-s-19's 10-19/20 read; ~ZW only if dell1 agrees to park AMGT_HARVST).
- **Lent capacity:** 25 of the 26 open cross-box items addressed here are dell1/dell2 orders to site-Z CloudOps lanes. Site Z is
  partly an execution host for dell1 (HARVST, DEMQUE); the reallocation should decide that explicitly.
- **Not classified (no block):** 4 Opal scheduled tasks on this box belong to no project in the union -- `amgt-induction-daily`
  (lib.research.corpus, likely AMGT_CORPUS; rc 4 today), `OPAL_D7_ticket_intake` (integrations/ticketing; rc 2, every 5 min),
  `OPAL_vendor_watch` (workflows/vendor_watch), `OPAL_restore_etf_daily_pull_20261009` (one-shot git restore, done, no next run).
  The read that classifies them: each script's project register row, by its owner.
- **Register defects found:** `DEVICES.json` lists lane letter `Z` only for this box; open call `sitez-20261011T224736Z-1b36`
  still reads OPEN after Andrew's yes (@90867982ed).

## Compiler Tools

`python .tools/to-check.py --all` (152 active orders, 61 projects, 6178 faces scanned); `python .tools/open-calls.py list`
(38 rows, 8 OPEN); `python .tools/crossbox-call.py list --open` (170 files, 52 shown); `get_live_agents` plus a `claude.exe`
process census (11 seats); `git worktree list --porcelain` + `git -C <wt> ls-tree` + `ls -a` over all 20 worktrees for
`.open_deploys/`; `Get-ScheduledTask` (27 non-Microsoft tasks, 16 Opal-owned); `org/mcp/agent-spawn-audit.log` SPAWN closure
for the site-Z lane set; `git log --since='7 days ago' --grep=<CODE> HEAD` per project; each project's `project.json`, PRD
outcome table and latest `ledger/ROUND_ANALYSIS*.md`. Not used: the served AWS graph (`aws_resources_owned` reads `unknown` on
every block for that reason). Per-project research was split across three forks of this seat; every block was read back here.
