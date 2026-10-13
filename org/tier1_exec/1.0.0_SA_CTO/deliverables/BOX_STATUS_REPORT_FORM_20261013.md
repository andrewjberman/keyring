# BOX STATUS REPORT -- the form (designed by 1.0.0_SA_CTO on Andrew's word of 2026-10-13 ~12:3xZ)

One file per box, written by that box's `4.0.0_SA_CRO` lane, at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_<box>_20261013.md` with `<box>` one of `laptop`, `sitez`, `dell1`,
`dell2`. Due 2026-10-13 16:00Z. Validate before committing: `python .tools/box-status-report-check.py <file>` must print `OK`.
Commit on the box's own branch under the CRO's author line; MSTR integrates it to CLOUD; the laptop reads it from there.

WHY (Andrew, verbatim): "we want to run an audit on the laptop box and establish how we will reallocate, because I think there are
a lot of projects that are less of a priority and it makes more sense for us to really pare down and establish what is necessary
for the drive this week." Write for that reader: every project on the box, what it is for, where it stands, what it costs to keep
running, what breaks if it is parked, and the CRO's own call.

## Rules of the form

1. EVERY project the box holds is a block: measured, not remembered. The population is the UNION of (a) `org/projects/*.json` with
   `placement` or `fabric` naming this box and `status` not `closed`; (b) every project a LIVE seat on this box names (the roster's
   `Working on` and the order files' `<issued_to>`); (c) every project with an order file on this box whose `<status>` is not terminal.
   Print the three counts and the union count in the header. A project found by (b) or (c) but absent from (a) is still a block,
   flagged `placement: NONE`.
2. One YAML block per project in exactly the schema below (the validator refuses a missing key; `unknown` is a legal value for a
   count you could not measure, never a guess). The prose under each block is for the human reader; the YAML is what the audit
   aggregates across the four boxes.
3. Names, counts, dates, hashes and paths only. No client name, no account id, no key, no token, no balance (the repo rule).
4. `client_facing` is `yes` when a partner-firm or client login can open the page or receive the output (the push law's class;
   unsure = yes); `indirect` when it feeds a client-facing surface without being one (a data pipeline behind a page); `no` otherwise.
   Name the surface.
5. `cro_rec` is the CRO's own call, one of `KEEP` (drive this week), `PARK` (stop cleanly, nothing rots), `CLOSE` (done or not
   worth finishing), `MERGE_INTO:<CODE>` (fold into another project). Give the one-sentence why. Andrew decides; the form does not.
6. `if_parked_this_week` must name what actually happens: scheduled jobs that keep firing on stale code, open deploy ledgers,
   holds someone set, a client expecting output, a seat that must be stood down -- or "nothing rots; safe to park".
7. Denominators beside every number. A read you could not make says `unknown` with the reason, never a blank.

## Header (once per file)

```yaml
box: <laptop|sitez|dell1|dell2>
author: <full CRO serial>
as_of_utc: <YYYY-MM-DDTHH:MM:SSZ>
branch_pin: <box/<box> commit hash at as_of>
population:
  register_placed: <n>        # (a) projects JSONs placed on this box, status not closed
  live_seat_named: <n>        # (b) projects live seats on this box name
  open_order_named: <n>       # (c) projects with a non-terminal order file on this box
  union: <n>                  # blocks in this file
seats_live: <n>               # claude.exe-backed seats on this box at as_of (count by process, not by heartbeat)
seats_by_role: {MSTR: n, CTO: n, COO: n, CVO: n, CRO: n, CloudOps: n, workers_24h: n}
account_state: <ok | at_limit_until_<UTC> | unknown>
open_deploy_ledgers: <n>      # org/critical_paths/.open_deploys/ on this box's live worktrees
scheduled_jobs_owned: <n>     # Windows scheduled tasks / session crons this box's seats own
open_calls_this_box: <n>
crossbox_open_to_this_box: <n>
```

## Per-project block (repeat for every project in the union)

```yaml
project: <CODE>
macro: <D<n>/<MACRO>>
placement: <box of record | NONE>
status_register: <active|inactive|complete|merged|NONE>
repos: [<ajb_workspace|portal|opal_ai|mcportal|aws-infra>, ...]   # only those this project's cells write
client_facing: <yes|indirect|no>
client_surface: "<page, report, file or 'none'>"
intent: "<one sentence: the outcome the project exists to produce (FWD-1's journey, in plain words)>"
desired_outcome_when_done: "<one sentence: what is true for Opal or a client when the register reads complete>"
status:
  round: <n | none>
  dep_stage: <value | none>
  fwd_realized: "<n>/<N>"       # from the PRD's outcome table and the last L10 analysis
  last_l10_utc: <date | none>
  open_orders: <n>
  last_commit_utc: <date of the newest commit naming the project on this box's branch>
seats_on_this_box: [<serial>, ...]
dependencies: ["<project, box, data or vendor this waits on>", ...]      # [] if none
blockers:                                                            # [] if none
  - what: "<one line>"
    owner: "<serial | Andrew>"
    clears_when: "<the act that clears it>"
next: ["<the next cell or act>", "<the one after>"]                   # at most 3
andrew_acts: ["<act> (<citation>)", ...]                             # [] if none; acts only, never decisions
footprint:
  commits_7d: <n | unknown>
  seats: <n>
  aws_resources_owned: <n | unknown>
  scheduled_jobs: <n>
  open_deploy_ledgers: <n>
  standing_holds: ["<hold>", ...]
if_parked_this_week: "<what happens, concretely>"
cro_rec: <KEEP | PARK | CLOSE | MERGE_INTO:<CODE>>
cro_rec_why: "<one sentence>"
```

Then, under the block, at most eight lines of prose for the reader: what the project has actually delivered so far (one
measured artifact or served output, with its date), and anything the YAML cannot carry (a dispute between boxes, a word of
Andrew's the project runs under, a risk).

## Box-level closing section (prose, at most fifteen lines)

- The three things on this box that would hurt most if stopped this week, and why.
- The three things that could stop today with no loss.
- Seats that would be freed by the CRO's PARK/CLOSE recommendations (count by role).
- Any project on this box the CRO could not classify, and what read would classify it.

## Compiler Tools (name the ones you used)

`python .tools/open-calls.py list` (this box); `python .tools/crossbox-call.py list --open`; `python .tools/round-close-check.py
--project <CODE>`; `git log --since='7 days ago' --format=%h -- <paths>` for commits_7d; `get_live_agents` / the roster by process;
`ls -a org/critical_paths/.open_deploys/`; the project JSON and PRD outcome table for `fwd_realized`.
