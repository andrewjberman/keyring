# Relaunch 01:06-03:20Z: four acceptance reads passed, and two documented controls turned out to be false

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (the four acceptance reads), DIAGNOSE (the J1 false pass, the
LD-0630 reach), SCRIBE (three rows, one memory supersession)

Window: this session's whole life, 01:06Z (server pid 10324 start) to 03:20Z. Prior log:
`../2026-10-08/startup_2100-2155Z_an_ack_the_cursor_could_not_show_me.md`.

## Current State

Relaunched under `--strict-mcp-config` by `0.0.0_AB_MSTR~Z` (msg 32201, hunk @26f9e5289f, ruling
@6abc00a2d5 AMENDMENT 1). All four acceptance reads PASS. Both watchers armed, 1 row each, no
stacking. Delivery ledger 8/8 READ, 0 unacked. Three commits, all under this seat's author line:
`550eac8853`, `c086fcc096` (both ON ORIGIN box/sitez), `eaf6d69c9a` (LOCAL; ls-remote re-measured
at 03:2xZ). Nothing unblocked outstanding. Two items held at Andrew, neither released by today's
egress law edit: the gateway allowlist widening (`opal_discover` etc. still
`identity_scope_denied`) and the drafted Teams reply (draft-and-ask, which is not an egress gate).

The 2026-10-09 11:00Z vehicle-log transcription is NOT this seat's: `0.0.0_AB_MSTR~Z` msg 32284 cut
the carrier to `0.7.0_AE_CloudOps~Z` under dell1 order `TO-RELAY-tw1-vehicle-log-20261009`.

## 1. The four acceptance reads (msg 32201), measured not recalled

| read | instrument | result |
|---|---|---|
| exactly 3 MCP servers | this session's own `org/mcp/sessions/ce25a793-...mcp.json`, 3 keys | PASS: bloomberg, opal-agent-comms, opal-gateway-bbg; all three answered live |
| registered LIVE | `register_agent` | PASS, pid 10324 |
| `bloomberg_health` | the tool | PASS `ok:true`, `//blp/refdata` |
| token subject oid 517aa5ee | read-only decode of `~/.claude/.credentials.json` sub claims | PASS: `6810043e-.../517aa5ee-...`, LIVE, 1 of 3 opalinvest.dev records |

A scope denial is not a failure (32201's own words) and `opal_discover` duly denied.

## 2. FALSE CONTROL #1 -- the relaunch runbook's own falsifier (row OPAL_ANALYST-Z-S1 @550eac8853)

`refs/RELAUNCH.md` s.2 step 3 states the negative control "Andrew's oid `2e21f8e5-...` matches 0".
It reads **2 of 3** on the identity filter alone: serverName `opal-gateway` and `opalgateway`, both
EXPIRED, one of them by only 1009 s -- so it was LIVE within the hour before the read. The claim
was almost certainly true when measured; what changed is a re-mint, not the pin.

The pin is sound by TWO independent filters and I verified it live: `teams-watch.py:236-239` tests
`PIN_SERVER.lower() in serverName.lower()`, and `opal-gateway-bbg` is not a substring of either
name, so both are excluded before the identity limb and again by the expiry filter at :242.

Hazard INERT, deliberately: `_read_pinned_token` has no fallback branch (:227-229), so an
unsatisfiable pin dies loudly instead of widening. The cost of leaving it is a future
relaunch-runner mis-reading its own falsifier. The durable form is a STRUCTURAL control over the
filter the engine applies, not a count over a mutable credential store. `refs/` is
`0.0.0_AB_MSTR~Z`'s to write; this seat surfaced and did not.

## 3. FALSE CONTROL #2 -- a J1 criterion a vendor-down morning would have passed (rows ETFS_RIVALS-Z-S79, -S80 @c086fcc096, @eaf6d69c9a)

The ask (dell1 `1.0.0_SA_CTO~DELL1` msg 1422, relayed 32267) wanted the 2026-10-09 11:00Z vehicle
log. That fire was 8.5 h out. But RIV-tw-1's J1 at task order :88 reads "the **2026-10-08 and
later** vehicle logs show the enrichment leg's lines and exit code unchanged with the switch
unset" -- so today's fire was already an evidence day and was in hand.

Transcribed verbatim from `~/opal_bbg_logs/bbg_tplus1_20261008_070001.log` (11932 B, 137 lines,
written by Scheduled Task `OPAL_BBGTML_daily_pull`, lastRun 07:00:01 local = 11:00Z,
LastTaskResult 50):

```
  86: RIVALFUNDS BLOOMBERG LEG EXIT CODE: 93 -- nothing written. Other legs UNAFFECTED.
  87: RIVALFUNDS ENRICHMENT STEP (RIV-e-1)
 137: RIVALFUNDS ENRICHMENT EXIT CODE: 97 -- nothing written.
```
HISTORY OWED: **0 occurrences, denominator the whole file.**

**That zero cannot grade J1.** 21 vendor-session-failure lines start at L65 -- before the legs --
`Failed to connect to 127.0.0.1:8194`, `session pool state=Failed`, `Platform failed 3 consecutive
times`, `Failed to start session`; and the leg's own result JSON carries `"unreachable": true`,
`"responses": 0`, `BloombergError: could not start blpapi session ... (is the Terminal running +
logged in?)`. The fire died before any `daily` code ran. ABSENT is not EXERCISED-AGAINST. Graded at
face value, J1 reads PASS on a run that never exercised the criterion -- a false pass on the one
criterion of the cell no instrument can settle.

S79 filed OBSERVATION / ARMED. S80 is a correction to S79 filed by its own author within the hour:
S79 named `disarm_owner 2.0.0_SA_COO~RV`, which msg 32284 says is gone; dell1's `2.0.0_SA_COO~V1`
holds it. An ARMED row whose disarm owner is unreachable cannot discharge, and the channel is
append-only, so the carrier is a NEW row with `adjudicates: [ETFS_RIVALS-Z-S79]`. General lesson
recorded there: an ARMED row's `disarm_owner` is a LIVENESS claim with a shelf life, and nothing in
the schema makes it rejectable when the named seat dies.

Also written: `deliverables/0.0.3_BG_BBGTerminal/transcribe_vehicle_log.py`, which makes the 10-09
act one command for whoever is alive, copies lines rather than retyping them, flags a non-reached
leg, and refuses to substitute an ad-hoc run for a scheduled fire.

**Why no ad-hoc QA run** (CLAUDE.md names this as a defect unless the evidence is stated): the
criterion is about the SCHEDULED job's own fire from the working tree with the switch unset (task
order :67). An ad-hoc run is a different run and would not evidence it; worse, the OFF-path
behaviour is keyed on existing state, so firing now would disturb the discriminator the scheduled
run exists to produce.

## 4. LD-0630's reach is per-seat restart, which its acceptance claim did not say

Registration dropped three times this session, each with pid 10324 alive. 32201 said the relaunch
"picks up the LD-0630 liveness fix" -- true of MY server and insufficient.

LD-0630's own text: the row is deleted by ANY OTHER seat's `_clean_stale`. Fix commit `739f951642`
is 2026-10-08T20:01:52-04:00. `Win32_Process` start times: 11 live `python org/mcp/server.py`
processes started 16:57-18:18 local, 2-3 h BEFORE the fix, so they run pre-fix bytes and still
prune on the plain 600 s rule; `broker.py` (pid 13032) started 16:57 local too. Mine (21:06) and
one at 22:01 are the only post-fix servers. An in-place file edit never reaches a running process.

`0.0.0_AB_MSTR~Z` msg 32288 accepted the read and ruled AGAINST cycling 11 working seats (two
rounds have live windows at 11:00Z and 13:00Z): drops are accepted until those sessions turn over,
and this seat re-registers on sight. Harm is bounded to a "no live session" read and QUEUED sends;
file-carried mail still lands.

## 5. Two process notes on myself

- **msg 32267 replayed as "URGENT, act NOW" because I never acked it.** I read it off the
  filesystem via the `[INBOX]` event and worked the entire ask without touching the READ clock; it
  sat SENT for 39 minutes looking undelivered to its sender. The replay was the mechanism working.
  This is a recurrence of a banked lesson, not a new one.
- **A zero I nearly reported as a finding was my own window bug.** `git log --author=... --since=`
  returned EMPTY for commits I had just made: `--since` takes LOCAL time and I passed a UTC
  instant still in the future locally. A positive control on the three hashes settled it in one
  call. Related: `--date=format:'%H:%MZ'` prints LOCAL time under a literal `Z`, so the commit
  times in a naive table would have been wrong by four hours.

## 6. Egress law edit 4d77a9c3ea -- what it did and did not release

Acked 32293 and verified against CLAUDE.md's bytes, not the relay's paraphrase: "Egress is open on
every channel, except Bloomberg" and "Bloomberg pulls go only through their queue; other vendor
APIs need no per-use word."

Consequence taken: the banked memory
`an-existing-narrow-producer-still-needs-andrews-per-use-vendor-word` instructed writing "needs
Andrew's per-use word" for ANY vendor. That is now the RESTRICTIVE error that entry's own second
half warns about -- the half that announces itself with nothing while every gate reads green. A
supersession block was appended naming what is repealed and what stands: Bloomberg's queue
carve-out, the unchanged human-confirmation list, and the MECHANISM rule (vendor pulls live in a
scripted producer with a trigger), which this edit does not touch and which is now the only
remaining discipline on a vendor pull.

What it did NOT release: the drafted Teams reply. Two non-egress gates remain -- this seat's
launch-prompt draft-and-ask on anything outward-facing, and `send_chat_message`'s own contract
requiring explicit confirmation of chat and text. Testing that gate would mean sending the message,
which is performing the act, not probing it. The allowlist item is likewise untouched; the edit
explicitly defers per-user entitlement scoping until a second MCP user.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-read --for` | `teams-watch.py` token selection; RIV-tw-1 J1 bar; CLAUDE.md autonomy | PASS; the UNREAD LEDGER made the J1 skip explicit, and J1 was in the unread set -- read it directly at :88 rather than trusting the summary |
| `comp-find` (content) | `HISTORY OWED` emitter; `LD-0630`; `517aa5ee` | PASS: wrong object caught early -- the emitter is `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py:917/937`, NOT `etf_daily_pull.py` where I first looked |
| `comp-find --name` | `*vehicle*`, `OPAL_ANALYST*` | PARTIAL: `*vehicle*` returned 88 deploy-vehicle hits, a pure wrong-object read; the HEAD band on `OPAL_ANALYST*` correctly showed a legacy flat project |
| `surprise-row-gate.py` | 3 new rows across 2 channels | PASS all three; denominators 1/1, 235, 236 |
| `safe-commit.sh` | 3 commits | PASS; `msg-verify MATCH` on each; verdicts read by token, never a positional slice |
| `to-check.py --all --assignee` | what this seat holds | 0 active TOs, scanned 4936, 0 parse errors |
| `audit-archive-invoker.py` | startup A.2 | 15 findings, denominator printed; an OWNED class (the archive is MSTR's), so surfaced in-report and NOT re-filed |

**What worked:** `comp-find`'s band labels caught two wrong-object reads before either reached a
conclusion -- the deploy-vehicle hits and the `etf_daily_pull.py` dead end. Writing the
transcription with a script rather than by hand is what kept "verbatim" true.

**What failed:** my own id-extraction for the next free row index -- `sort -t'S' -k3` collapsed to a
single row because `ETFS_RIVALS` itself contains an `S`. The count (77) and the max (78) disagreed
with the printed list, which is what exposed it; a regex-anchored Python read settled it.

**Gap found:** nothing in the investigation schema makes a dead `disarm_owner` rejectable, so an
ARMED row can be left undischargeable by a seat's death with no refuser. Recorded in S80; not this
seat's to fix.

## Blockers

None BLOCKED on evidence. Two items reserved at Andrew (not blockers on this seat's work): the
gateway allowlist widening, and the drafted Teams reply. Both verified as still reserved against
today's bytes rather than assumed -- the law edit changed the egress class and released neither.

## Next Steps

- [`0.7.0_AE_CloudOps~Z`] holds the 2026-10-09 11:00Z transcription under dell1 order
  `TO-RELAY-tw1-vehicle-log-20261009`; `transcribe_vehicle_log.py` and the 10-08 day are committed
  for it.
- [`2.0.0_SA_COO~V1`] owns the S79 disarm: one sentence that J1 is read on the first fire that
  REACHED the leg, not the earliest date in its range.
- [`0.0.0_AB_MSTR~Z`] owns the `refs/RELAUNCH.md` negative-control fix (S1) and carries both rows
  to dell1.
- This seat: event-driven on the Teams and inbox watchers; re-register on sight; the daily upload
  guardrail records check is discharged for 2026-10-08 (the 07:00 fire failed rc=50 and was
  recovered and CTO-graded earlier today).
