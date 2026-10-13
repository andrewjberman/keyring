# BOX STATUS REPORT -- laptop -- 2026-10-13

Written by `4.0.0_SA_CRO` on the form `org/tier1_exec/1.0.0_SA_CTO/deliverables/BOX_STATUS_REPORT_FORM_20261013.md` (@ed890da86d),
on Andrew's word of ~12:3xZ (record `ANDREW_DIRECT_20261013_123xZ_BOX_STATUS_REPORTS_FOR_THE_LAPTOP_AUDIT_AND_REALLOCATION.md`).
Every number was read at as_of; `unknown` marks a read not made, with the reason in the prose.

How the population was read:
- (a) register: `org/projects/*.json` plus `org/missions/D*/*/*/project.json` (398 + 50 files) where `fabric` or `placement` is
  laptop and `status` is not `closed`. That gives 12 projects. The form's rule keeps `complete` and `merged` rows in, so they are
  blocks here.
- (b) live seats: 8 `claude.exe` processes on this box, matched 8 of 8 to the broker's live list. Projects they name, from roster
  summaries and their 7-day commits: NFRA_CTLPLN (`2.0.0_SA_COO~C`, `3.0.0_SA_CVO~L`, `0.7.0_AE_CloudOps~U7`); IRPT_ANLREQ
  (`0.7.0_AE_CloudOps~ANL`); ADVI_FIRMBKTS and MDPF_HEALGAP (`0.7.0_AE_CloudOps~FBL`). `0.0.0_AB_MSTR`, `1.0.0_SA_CTO` and this seat
  run fabric-wide work, not a project. That gives 4.
- (c) open orders: 6,178 order files read; 859 are not terminal. A project counts when it is laptop-placed or the order's
  `<issued_to>` is a live laptop seat. That gives 13.
- The union of (a), (b) and (c) is 24 projects.

```yaml
box: laptop
author: 4.0.0_SA_CRO
as_of_utc: 2026-10-13T13:00:00Z
branch_pin: 74478aca31
population:
  register_placed: 12
  live_seat_named: 4
  open_order_named: 13
  union: 24
seats_live: 8                 # claude.exe processes, 8 of 8 matched to the broker live list
seats_by_role: {MSTR: 1, CTO: 1, COO: 1, CVO: 1, CRO: 1, CloudOps: 3, workers_24h: 3}   # workers: distinct 0.9.0_WK_NFRA_CTLPLN~n authors, 24 h
account_state: ok             # this session and 7 others running; no limit notice on this box (dell2's limit is dell2's)
open_deploy_ledgers: 27       # union over 2 of 2 live worktrees: 16 in the main tree at HEAD + 11 only in the stale worktree wk-NFRA_CTLPLN-76 (last commit 2026-10-12 15:37Z); 2 of 27 name laptop
scheduled_jobs_owned: 6       # 6 enabled Opal Windows tasks of 7 Opal tasks (ETF NetAssets Daily Probe disabled); session crons: unknown (CronList is per-session)
open_calls_this_box: 0        # open-calls.py list: 7 rows, 0 open
crossbox_open_to_this_box: 4  # crossbox-call.py list --open: 4 rows addressed to laptop, all ACKED, none closed (f559 to COO~C; 552a, e261 to CloudOps~ANL; 1 more)
```

## Projects being worked

```yaml
project: NFRA_CTLPLN
macro: D0/NFRA
placement: laptop
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "the portal data proxy fence (opal-portal-data-proxy): which partner logins may read internal routes"
intent: "One control plane for four boxes: the laptop plans, site Z integrates and deploys, dell1 and dell2 execute, one round at a time."
desired_outcome_when_done: "Every box runs work from git orders with one writer per file, no deploy from a publish, and partner data fenced to the right firm."
status:
  round: 11
  dep_stage: EXECUTING
  fwd_realized: "unknown/28"   # FWD-1 and FWD-28 REALIZED at round 11 (ledger/ROUND_ANALYSIS.round11.md); the full grade table was not read
  last_l10_utc: 2026-10-12
  open_orders: 1
  last_commit_utc: 2026-10-13
seats_on_this_box: [2.0.0_SA_COO~C, 3.0.0_SA_CVO~L, 0.7.0_AE_CloudOps~U7]
dependencies: ["dell1 lane for round-6 CT-x-1", "Andrew's public keys for FWD-27 (SSH over the tailnet)"]
blockers:
  - what: "FWD-28 firm tokens vs the naming gate (row W62-S6)"
    owner: "1.0.0_SA_CTO"
    clears_when: "the CTO rules W62-S6"
  - what: "FWD-27 SSH enable waits on Andrew's public keys and elevated lines"
    owner: "Andrew"
    clears_when: "keys supplied"
next: ["CT-aa-5/CT-aa-6: remove the Dev-type clause from the proxy fence (live since 2026-10-12 15:02Z)", "seat-boundary cell (S9117/S9118)", "crossbox-limb cell (S32)"]
andrew_acts: ["authorize the proxy log purge and refresh-token invalidation (laptop outcome page 2026-10-12)", "supply public keys for FWD-27 (ledger/ROUND_ANALYSIS.round11.md)"]
footprint:
  commits_7d: 1135
  seats: 6
  aws_resources_owned: unknown
  scheduled_jobs: 2
  open_deploy_ledgers: 0
  standing_holds: ["Dev-type clause live on the proxy fence until CT-aa-6"]
if_parked_this_week: "The Dev-type widening stays live on the partner data proxy, and the logged refresh tokens stay unpurged; 3 laptop seats plus workers stand down."
cro_rec: KEEP
cro_rec_why: "The proxy fence protects partner data, and its live widening and token log need this week's round; cut the round to those two chains."
```
Delivered: partner logins get 403 on 39 of the proxy's 41 internal routes, and the proxy stopped logging callers' tokens
(2026-10-12; 0 of 38 log events since 11:02 ET carry one). FWD-1, one order run laptop -> dell1 -> CLOUD -> laptop, was REALIZED
at round 11 (`b46f662cc2`). Scheduled jobs: `Opal box-sync` and `Opal open-calls scan` are counted here; that attribution is
inferred. 1,135 commits in 7 days is the heaviest load on the box.

```yaml
project: IRPT_ANLREQ
macro: D9/IRPT
placement: dell2
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: "yes"
client_surface: "Investor Reporting analysis requests (a client's request to a finished report)"
intent: "A client analysis request runs end to end, from intake to a generated report and its commentary."
desired_outcome_when_done: "A partner files an analysis request and receives the report without staff hand-work."
status:
  round: 20
  dep_stage: EXECUTING
  fwd_realized: "unknown"   # dell2's ledger, not read from this box
  last_l10_utc: unknown
  open_orders: 3
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~ANL]
dependencies: ["dell2 COO and CTO lanes (project owner)"]
blockers: []
next: ["the next laptop read order from dell2 when one is issued"]
andrew_acts: []
footprint:
  commits_7d: 1015
  seats: 1
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "dell2 loses its laptop reader; 2 acked cross-box orders (552a, e261) stay open."
cro_rec: KEEP
cro_rec_why: "KEEP the project on dell2; the laptop seat exists only because dell2 lacks kms:Decrypt on the IRPT key, and stands down once that is granted (ANDREW_DIRECT_20261013_131xZ)."
```
The laptop's share is one CloudOps seat that runs stored-input recounts for dell2 (TO-READS-Y10 complete, 05:35Z). The project's
own status belongs to dell2's report.

```yaml
project: ADVI_FIRMBKTS
macro: D8/ADVI
placement: dell1
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "each firm's own S3 bucket behind the advisor and investor-reporting pages"
intent: "Each firm's data moves into that firm's own bucket, and every reader is repointed to it."
desired_outcome_when_done: "No firm's data sits in a shared or another firm's bucket, and every page reads the canonical path."
status:
  round: 7
  dep_stage: EXECUTING
  fwd_realized: "unknown"   # dell1's ledger
  last_l10_utc: unknown
  open_orders: 7
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~FBL]
dependencies: ["dell1 COO (project owner)", "laptop edge functions (FB-f-19, applied 2026-10-12)"]
blockers: []
next: ["round 7: a second fresh reader and the exec-summary trigger fix (dell1)"]
andrew_acts: []
footprint:
  commits_7d: 654
  seats: 1
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 1
  standing_holds: []
if_parked_this_week: "A half-migrated firm-bucket cutover: 49financial readers are moved, other firms are not; open ledgers on dell1 stay open."
cro_rec: KEEP
cro_rec_why: "KEEP the project on dell1 (a half-finished migration is the worst state to stop in); the laptop seat exists only because dell1 cannot simulate IAM or deploy the protected edge functions, and stands down once granted (ANDREW_DIRECT_20261013_131xZ)."
```
The laptop applied the edge-function leg (FB-f-19, 2026-10-12) and the Inflection fence admit (FB-f-21, 2026-10-13 01:18Z). The
1 open ledger counted is `advi-firmbkts-fb-f-19-act4-edge-leg-laptop-20261012`, and it exists only in the stale worktree.

```yaml
project: MDPF_HEALGAP
macro: D8/MDPF
placement: dell1
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "Model Portfolios data (gap healing behind the page)"
intent: "Gaps in the model-portfolio series heal themselves on the next scheduled run instead of by hand."
desired_outcome_when_done: "A missed day in the Model Portfolios data is filled automatically and shown honestly."
status:
  round: 3
  dep_stage: EXECUTING
  fwd_realized: "unknown"   # dell1's ledger
  last_l10_utc: unknown
  open_orders: 0
  last_commit_utc: 2026-10-13
seats_on_this_box: [0.7.0_AE_CloudOps~FBL]
dependencies: ["dell1 COO (project owner)"]
blockers: []
next: ["dell1's round-3 acts (ht10, ht15)"]
andrew_acts: []
footprint:
  commits_7d: 265
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 2
  standing_holds: []
if_parked_this_week: "Nothing on the laptop; dell1's two open healgap ledgers are dell1's."
cro_rec: KEEP
cro_rec_why: "dell1-led; the laptop only lent one read (HG-t-10, done clean 12:30Z), so it costs the laptop nothing."
```
`seats: 0` because the laptop seat (FBL) is already counted under ADVI_FIRMBKTS. The 2 ledgers are dell1's
(`healgap-r3-act-ht10...`, `healgap-r3-act-ht15...`).

## Projects placed here and active, with no live seat

```yaml
project: ADVI_PERFRP
macro: D2/ADVI
placement: laptop
status_register: active
repos: [ajb_workspace, portal, aws-infra]
client_facing: "yes"
client_surface: "49 Financial Books tab and the advisor public-profile Book view (performance attribution)"
intent: "49 Financial gets per-client performance attribution and reporting comparable to the Black Diamond dashboard."
desired_outcome_when_done: "A 49 Financial advisor opens the Books tab and sees each client's performance attribution."
status:
  round: 1
  dep_stage: EXECUTING
  fwd_realized: "unknown"   # PRD v0.3 s.11 table not graded since 2026-08-28
  last_l10_utc: none
  open_orders: 3
  last_commit_utc: 2026-10-09
seats_on_this_box: []
dependencies: ["the 49F account spine (ADVI_49F, closed 2026-10-07)"]
blockers:
  - what: "3 open orders are addressed to role classes, not seats (DE-class, AE-class, a DS lane seated 2026-08)"
    owner: "2.0.0_SA_COO"
    clears_when: "the orders are seated or withdrawn"
next: ["Andrew confirms whether the 49F vision still stands"]
andrew_acts: []
footprint:
  commits_7d: 1
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots; safe to park. No seat, no job and no ledger."
cro_rec: PARK
cro_rec_why: "Its spine project ADVI_49F was closed on 2026-10-07 as an old vision; this one should wait for the same question to be asked of it."
```
The last real progress was 2026-08-28 (TO-R1-AE PASS, `debe9bc7b4`). Andrew's 2026-10-07 close record names INSURE and 49F as
"very old ... i do not know if their vision is still relevant"; PERFRP is built on that 49F spine.

```yaml
project: ADVI_ROSTERCOLS
macro: D2/ADVI
placement: laptop
status_register: active
repos: [ajb_workspace]
client_facing: "yes"
client_surface: "49 Financial Net Worth roster: 6 columns showing 'Unavailable - no source'"
intent: "Source the six empty columns on the 49 Financial Net Worth roster."
desired_outcome_when_done: "The roster shows a value or a stated reason in all six columns."
status:
  round: none
  dep_stage: REGISTERED
  fwd_realized: "0/unknown"   # no PRD exists
  last_l10_utc: none
  open_orders: 0
  last_commit_utc: 2026-09-10
seats_on_this_box: []
dependencies: []
blockers: []
next: ["a brief, if kept"]
andrew_acts: []
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: 0
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots; safe to park."
cro_rec: PARK
cro_rec_why: "Registered, never briefed, no work since 2026-09-10; it belongs to the same 49F question as ADVI_PERFRP."
```

```yaml
project: LGIC_LGCTFM
macro: D14/LGIC
placement: laptop
status_register: active
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "One instrument (the legacy transform) that every migration uses to map a legacy pipeline onto the canonical structure."
desired_outcome_when_done: "Every migration project runs the same transform and produces the same artifacts."
status:
  round: unknown
  dep_stage: EXECUTING
  fwd_realized: "unknown"   # tree ledger not read
  last_l10_utc: unknown
  open_orders: 0
  last_commit_utc: 2026-10-07
seats_on_this_box: []
dependencies: []
blockers: []
next: ["none scheduled"]
andrew_acts: []
footprint:
  commits_7d: 2
  seats: 0
  aws_resources_owned: 0
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: ["held-at-stop ruling restored 2026-09-20 (project.json)"]
if_parked_this_week: "Nothing rots; the tool keeps working. Runs dated 2026-10-11 exist under workflows/legacy_transform/ (used by dell1)."
cro_rec: PARK
cro_rec_why: "The instrument already works and is in use; no development is needed this week."
```

```yaml
project: NFRA_SPMOVE
macro: D9/NFRA
placement: laptop
status_register: active
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none (an Opal SharePoint AWS folder)"
intent: "Move the Schwab master workbooks into a SharePoint folder whose paths follow the AWS naming structure."
desired_outcome_when_done: "Staff find each month's Schwab workbook in SharePoint at its canonical path."
status:
  round: none
  dep_stage: PRD
  fwd_realized: "0/7"   # 7 contracts in PRD v0.1, none built
  last_l10_utc: none
  open_orders: 0
  last_commit_utc: 2026-10-01
seats_on_this_box: []
dependencies: ["LGIC_NAMING (complete)"]
blockers: []
next: ["PRD sign-off, if kept"]
andrew_acts: []
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: 0
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots; safe to park."
cro_rec: PARK
cro_rec_why: "A small internal convenience at PRD stage with no work in 12 days; nothing waits on it."
```

```yaml
project: OPAL_ADVIPOINTERS
macro: D2/OPAL
placement: laptop
status_register: active
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "Advisor Intelligence and Model Portfolios data paths"
intent: "One traceable path from vendor bytes to the portal for all three firms, with legacy routes retired last."
desired_outcome_when_done: "Every ADVI and MDPF page reads one canonical path per firm."
status:
  round: none
  dep_stage: none
  fwd_realized: "unknown"   # PRD v1.0 of 2026-08-12, stale-dates disclosure 2026-08-29
  last_l10_utc: none
  open_orders: 10
  last_commit_utc: 2026-09-17
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 10 open orders"]
andrew_acts: []
footprint:
  commits_7d: 0
  seats: 0
  aws_resources_owned: unknown
  scheduled_jobs: 0
  open_deploy_ledgers: 0
  standing_holds: []
if_parked_this_week: "Nothing rots; the same goal is being driven by ADVI_FIRMBKTS and MDPF_CANON on dell1."
cro_rec: CLOSE
cro_rec_why: "Superseded: ADVI_FIRMBKTS and MDPF_CANON now carry its canonical-path goal; its 10 open orders sit on lanes with no session."
```

## Registered as complete or merged (rows (a) keeps)

```yaml
project: ADVI_49FSRC
macro: D2/ADVI
placement: laptop
status_register: complete
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Settle the 49 Financial data sourcing choices."
desired_outcome_when_done: "Settled; register reads complete."
status: {round: none, dep_stage: CLOSED, fwd_realized: "unknown", last_l10_utc: none, open_orders: 0, last_commit_utc: 2026-09-14}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip status complete -> closed"]
andrew_acts: []
footprint: {commits_7d: 0, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; already done."
cro_rec: CLOSE
cro_rec_why: "Completed 2026-08-30 on Andrew's 'Rec approved'; only the register flip remains."
```

```yaml
project: ADVI_BDPLAT_RESTORE
macro: D2/ADVI
placement: laptop
status_register: complete
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Restore the Black Diamond platinum scripts."
desired_outcome_when_done: "Restored; register reads complete."
status: {round: none, dep_stage: CLOSED, fwd_realized: "unknown", last_l10_utc: none, open_orders: 0, last_commit_utc: 2026-09-14}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip status complete -> closed"]
andrew_acts: []
footprint: {commits_7d: 0, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; already done."
cro_rec: CLOSE
cro_rec_why: "Its one order closed 2026-08-19; only the register flip remains."
```

```yaml
project: LGIC_NAMING
macro: D14/LGIC
placement: laptop
status_register: complete
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "One naming schema for every S3 address and resource name (lib/opal_naming.py)."
desired_outcome_when_done: "Done: the builders exist and the commit-time gate refuses typed names."
status: {round: 5, dep_stage: CLOSED, fwd_realized: "unknown", last_l10_utc: 2026-09-16, open_orders: 0, last_commit_utc: 2026-10-09}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip status complete -> closed"]
andrew_acts: []
footprint: {commits_7d: 4, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; the naming library stays in use."
cro_rec: CLOSE
cro_rec_why: "Closed at L10 on 2026-09-16; the 4 commits in 7 days are other projects citing it."
```

```yaml
project: ADVI_BDPARITY
macro: D2/ADVI
placement: laptop
status_register: merged
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Check our 49F outputs against Black Diamond's own calculated outputs."
desired_outcome_when_done: "Merged into another project; nothing of its own remains."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 5, last_commit_utc: 2026-10-06}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 5 open orders", "flip status merged -> closed"]
andrew_acts: []
footprint: {commits_7d: 1, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; 5 orphan orders stay open and keep showing in order counts."
cro_rec: CLOSE
cro_rec_why: "Already merged; its 5 non-terminal orders are dangling records."
```

```yaml
project: ADVI_COTKEY
macro: D2/ADVI
placement: laptop
status_register: merged
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Fix the Cottonwood advisor key (Portfolio Group, not rep code)."
desired_outcome_when_done: "Merged into another project."
status: {round: none, dep_stage: DECOMP, fwd_realized: "unknown", last_l10_utc: none, open_orders: 0, last_commit_utc: 2026-10-06}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip status merged -> closed"]
andrew_acts: []
footprint: {commits_7d: 1, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Merged; register hygiene only."
```

```yaml
project: ADVI_STITCH
macro: D2/ADVI
placement: laptop
status_register: merged
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Stitch 49F history against the Black Diamond legacy history."
desired_outcome_when_done: "Merged into another project."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 0, last_commit_utc: 2026-10-06}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["flip status merged -> closed"]
andrew_acts: []
footprint: {commits_7d: 1, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Merged; register hygiene only."
```

```yaml
project: ADHC_OWNPTH
macro: ADHC
placement: NONE
status_register: complete
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "A pre-commit hook that blocks a commit touching paths outside the author's permitted set."
desired_outcome_when_done: "Done: the owned-paths hook is installed on every box."
status: {round: none, dep_stage: none, fwd_realized: "7/7", last_l10_utc: none, open_orders: 1, last_commit_utc: 2026-10-13}
seats_on_this_box: [1.0.0_SA_CTO]
dependencies: []
blockers: []
next: ["close or withdraw the 1 open order addressed to 1.0.0_SA_CTO"]
andrew_acts: []
footprint: {commits_7d: 6, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; the hook keeps running."
cro_rec: CLOSE
cro_rec_why: "Complete since 2026-05-22 (7 of 7 orders); one stray open order brings it into this list."
```
`placement: NONE`: the register row has no fabric field. It entered the population through (c), an open order issued to the
laptop CTO.

## Closed projects that still carry open orders or a running job

```yaml
project: NFRA_OUTSET
macro: D11/NFRA
placement: laptop
status_register: closed
repos: [ajb_workspace, aws-infra]
client_facing: "no"
client_surface: "none"
intent: "Outset tooling: comp-heat and the semantic estate pipeline."
desired_outcome_when_done: "Closed."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 22, last_commit_utc: 2026-10-01}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["retire the Windows task OpalOutsetDriftLaptop", "withdraw the 22 open orders"]
andrew_acts: []
footprint: {commits_7d: 0, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 1, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Already closed, but a scheduled task keeps firing: OpalOutsetDriftLaptop ran at 08:45 ET today (rc=0) and publishes drift to S3 for a closed project."
cro_rec: CLOSE
cro_rec_why: "Closed in the register, but a live job and 22 open orders remain; finish the close by retiring both."
```

```yaml
project: NFRA_CLDGRPH
macro: D0/NFRA
placement: laptop
status_register: closed
repos: [ajb_workspace, aws-infra]
client_facing: "no"
client_surface: "none"
intent: "The cloud graph compile (kuzudb projection of the AWS estate)."
desired_outcome_when_done: "Closed."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 14, last_commit_utc: 2026-10-09}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 14 open orders"]
andrew_acts: []
footprint: {commits_7d: 5, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; 14 orphan orders stay open."
cro_rec: CLOSE
cro_rec_why: "Closed; its orders are dangling records."
```

```yaml
project: MDPF_TAXSMA
macro: D8/MDPF
placement: dell1
status_register: closed
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "49 Financial and Global category totals on Model Portfolios"
intent: "Tax SMA trading status through reconciliation to category totals."
desired_outcome_when_done: "Closed on Andrew's word 2026-10-07 ('done at this point')."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 6, last_commit_utc: 2026-10-13}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 6 open orders"]
andrew_acts: []
footprint: {commits_7d: 10, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; 6 orphan orders stay open."
cro_rec: CLOSE
cro_rec_why: "Closed on Andrew's word; its orders are dangling records."
```
The register row says `fabric: laptop` but the tree row says placement DELL1. The 10 commits in 7 days are other projects
citing the code.

```yaml
project: ADVI_49F
macro: D2/ADVI
placement: laptop
status_register: closed
repos: [ajb_workspace, aws-infra]
client_facing: indirect
client_surface: "49 Financial performance figures (TWR engine)"
intent: "Fix the 49 Financial canonical runner chain's TWR-engine defects."
desired_outcome_when_done: "Closed on Andrew's word 2026-10-07."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 3, last_commit_utc: 2026-10-09}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 3 open orders"]
andrew_acts: []
footprint: {commits_7d: 4, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots; 3 orphan orders stay open."
cro_rec: CLOSE
cro_rec_why: "Closed on Andrew's word (old vision); its orders are dangling records."
```

```yaml
project: ADVI_INSURE
macro: D2/ADVI
placement: laptop
status_register: closed
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "The insurance advisor product."
desired_outcome_when_done: "Closed on Andrew's word 2026-10-07."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 3, last_commit_utc: 2026-10-08}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 3 open orders"]
andrew_acts: []
footprint: {commits_7d: 3, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Closed on Andrew's word; its orders are dangling records."
```

```yaml
project: ETFS_GUARDRAIL
macro: D8/ETFS
placement: laptop
status_register: closed
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Stop the monthly ETF ownership report from publishing over data the estate does not have."
desired_outcome_when_done: "Closed at L10 2026-09-05 (8 of 8 outcomes served)."
status: {round: none, dep_stage: ROUND_CLOSE, fwd_realized: "8/8", last_l10_utc: 2026-09-05, open_orders: 4, last_commit_utc: 2026-10-01}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 4 open orders"]
andrew_acts: []
footprint: {commits_7d: 0, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Closed with 8 of 8 served; only orphan orders remain."
```

```yaml
project: NFRA_COMPEFFICACY
macro: D11/NFRA
placement: laptop
status_register: closed
repos: [ajb_workspace]
client_facing: "no"
client_surface: "none"
intent: "Every comp-tool Andrew named ends cleared, retired or merged."
desired_outcome_when_done: "Closed."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 2, last_commit_utc: 2026-10-08}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 2 open orders"]
andrew_acts: []
footprint: {commits_7d: 1, seats: 0, aws_resources_owned: 0, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Closed; only orphan orders remain."
```

```yaml
project: IRPT_CUSTDY
macro: D9/IRPT
placement: dell2
status_register: closed
repos: [ajb_workspace]
client_facing: indirect
client_surface: "Investor Reporting custody data"
intent: "Investor Reporting custody intake."
desired_outcome_when_done: "Closed."
status: {round: none, dep_stage: EXECUTING, fwd_realized: "unknown", last_l10_utc: none, open_orders: 1, last_commit_utc: 2026-10-11}
seats_on_this_box: []
dependencies: []
blockers: []
next: ["withdraw the 1 open order"]
andrew_acts: []
footprint: {commits_7d: 187, seats: 0, aws_resources_owned: unknown, scheduled_jobs: 0, open_deploy_ledgers: 0, standing_holds: []}
if_parked_this_week: "Nothing rots."
cro_rec: CLOSE
cro_rec_why: "Closed; one orphan order remains (worker ~18)."
```
The register row says `fabric: laptop` but the tree row says placement DELL2. The 187 commits in 7 days are dell2 subjects
citing the code.

## Box-level closing

- **Would hurt most if stopped this week:**
  1. NFRA_CTLPLN's round-12 chains: a live Dev-type widening on the partner data proxy, and 49 token-shaped plus 38 refresh-token
     lines unpurged in its log.
  2. ADVI_FIRMBKTS's laptop legs: the firm-bucket cutover is half done.
  3. IRPT_ANLREQ's laptop reader: client-facing work, at the cost of one idle seat.
- **Could stop today with no loss:** the 15 CLOSE rows below OPAL_ADVIPOINTERS (pure register and order hygiene). Within them, retire `OpalOutsetDriftLaptop`,
  a daily job for a closed project, and the one-shot Windows task `OpalReinstate-1.0.0_SA_CTO-20260916`, which still names
  model `claude-opus-5`. PARK ADVI_PERFRP, ADVI_ROSTERCOLS, LGIC_LGCTFM and NFRA_SPMOVE: none holds a seat, a job or a ledger.
- **Seats freed by the PARK/CLOSE calls:** 0. Every live laptop seat sits on a KEEP project; the gain is attention and 71 dangling
  orders withdrawn (61 across the 15 hygiene rows, plus 10 for OPAL_ADVIPOINTERS).
- **Could not classify fully:**
  - `fwd_realized` for the cross-box projects. Read: each owning box's ledger.
  - LGIC_LGCTFM's round. Read: its tree ledger.
  - `aws_resources_owned` everywhere. Read: `comp-estate --resource <code>`, not run within the time box.
- **Main tradeoff:** NFRA_CTLPLN carries 1,135 commits in 7 days, so the week's real choice is how much of its 28-outcome scope to
  keep beyond the fence work.

## Compiler Tools

`python .tools/open-calls.py list`; `python .tools/crossbox-call.py list --open`; `get_live_agents` plus a `claude.exe` process
census; `git ls-tree` of `org/critical_paths/.open_deploys/` over `git worktree list --porcelain` (2 of 2 worktrees);
`Get-ScheduledTask` and `schtasks`; `git log --since='7 days ago' -F --grep=<CODE>` for commits_7d (whole branch, all boxes'
integrated history); `org/projects/*.json` and `org/missions/D*/*/*/project.json`; a parse of all 6,178 order files for
`<status>`/`<issued_to>`; `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round11.md`. Not used: `round-close-check.py`
(time box).
