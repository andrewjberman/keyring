---
name: remote-drive
description: A small ad hoc job from Teams, done end to end by one seat. Two halves -- the device's 0.0.0_AB_MSTR answers LDO-001's REMOTE-JOB bus messages (bid, award, close) with .tools/remote-job.py and spawns a 2.0.0_SA_COO~<N>; that COO runs `/remote-drive J042`: identify the function the requester means, /closer trace it, /atom-decomp the relevant surfaces, do the work, validate it on the real artifact, report to MSTR. Not registered, no PRD, no task orders.
---

# /remote-drive -- one small job from Teams, start to finish

Authority: Andrew-direct 2026-10-02 ~16:4xZ-17:0xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md`. The light form, his
words: *"assess what function the user is talking about and runs closer trace to get the flow of functions involved,
then runs atom-decomp on the relevant surfaces, then just gets to work and validates."*
Protocol (names, messages, payloads, the award rule): `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`.
The cloud side is LDO-001 (`data/transcripts/scripts/teams_chat/tenant.py`): it opens the job on Andrew's `#dev`,
offers it on the agent bus, picks the least-loaded available machine, talks to the requester, and closes the job.

## Half 1 -- the device's MSTR (bus listener armed via `/agentbus`)

Each bus message is one human line plus one line `REMOTE-JOB-JSON {...}`. The cloud is the sender, so the Rule 22b
ACK is the event you send back (the bid, the accept), not a bus ACK.

| Bus line | Do, the same turn |
|---|---|
| `REMOTE-JOB OFFER J042 -- ...` | `python .tools/remote-job.py bid J042`. Nothing else: the bid window is 120 s. A box with no live reviewer (`3.0.0_SA_CVO`, any `~lane`) bids `available: false`, reason `no_reviewer`. |
| `REMOTE-JOB AWARD J042 -- yours ...` | 1. `python .tools/remote-job.py show J042 --json '<the REMOTE-JOB-JSON line>'` (or `--from-file <listener output file>`): prints the brief's path. 2. Pick the next free `~<N>` for `2.0.0_SA_COO` (count live `2.0.0_SA_COO*` first; the laptop cap is three COO sessions); the seat is NEW for this job, a serial not live before the award. 3. `/mstr-spawn 2.0.0_SA_COO~<N> --say "/remote-drive J042 <brief path>"`. 4. `python .tools/remote-job.py accept J042 --coo 2.0.0_SA_COO~<N> --brief-file <brief path>`. `accept` refuses without that file. The requester then hears "I'm on it". |
| The COO's MCP completion report | Hand the live reviewer on this box, by one message, the COO's report path and the job id. The reviewer reads the real artifact, writes its grade record under its own deliverables folder, and runs `python .tools/remote-job.py grade J042 --as <reviewer serial> --verdict PASS\|FAIL --record <record path>`. A FAIL goes back to the COO as its next item; a second FAIL is `fail` with the reason. Only after a PASS: |
| The reviewer's PASS grade | `python .tools/remote-job.py complete J042 --summary "<one line>" [--deployed] --evidence "<commit, deploy proof, the run>"`. A re-open after the requester says it still fails is `--attempt 2`. |
| The COO cannot finish | `python .tools/remote-job.py fail J042 --reason "<one line>"` (clears this machine's lock). |
| `REMOTE-JOB CLOSE J042 -- ...` | Tell the COO by MCP: "close J042: write /log, archetype line, tag `adhoc-remote-job`". When its log commit lands, `/mstr-kill 2.0.0_SA_COO~<N>`, then `python .tools/remote-job.py close J042`. |
| `REMOTE-JOB LOST J042 -- ...` | Nothing. |

MSTR routes; it does not do the job (CLAUDE.md: 0.0.0_AB_MSTR "integrates and never works a project"). One remote
job per machine at a time: `.tools/.remote-job.json` holds the open one, and a busy machine bids `available: false`.

Before a job is counted finished (`remote-job.py complete`), run `python .tools/round-close-check.py --reviewer-only`; `verdict=REFUSED` means it is not finished.

## Half 2 -- the COO: `/remote-drive J042 <brief path>`

1. **Read the brief.** Who asked, what is broken or wanted, which page or function, how they will check it.
2. **Identify the function** the requester means: the page, Lambda, gold script or route. Name it in one line. If the
   brief cannot be tied to one surface, report that to MSTR now (it becomes `fail`) rather than guessing.
3. **`/closer trace <surface>`** for the flow of functions involved, from where the requester sees it to the data.
4. **`/atom-decomp`** the relevant surfaces only, to the depth the fix needs.
5. **Do the work** in your own worktree (`git worktree add ../wk-remote-J042 -b wk-remote-J042 HEAD`); commit through
   `safe-commit.sh` under your own serial.
6. **Validate on the real artifact:** the fix's own test, then ONE real run looked at -- the page served, the Lambda
   invoked, the output read. Never a self-report, never rc=0 alone.
7. **Deploy only through the gates** when the fix needs it: `safe-deploy.sh` / `safe-apply` with a change-management
   ledger opened before the act and closed with proof (CLAUDE.md NEVER-2). A served-output move still needs its
   never-widen sign-off.
8. **Report to your MSTR** by MCP, one message: what changed, the commit, the deploy proof if any, the run you looked
   at, the files the reviewer should read, and the one line the requester can check. Then wait.
9. **On MSTR's close word:** write `/log` with the archetype line and the tag `adhoc-remote-job`, commit it, and stop.

Small by definition: not registered, no PRD, no task orders, no subagents. A job that turns out not to be small is
reported to MSTR as such (it becomes `fail` with the reason), and Andrew decides whether it becomes a project.
