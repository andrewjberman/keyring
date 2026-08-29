# /self-drive D2 & D3 — tick 35 (2026-08-29 04:52-05:15Z) — state: ARMED

Covers tick 35 (tick 34 logged @ecda08be10). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA and on a TERMINAL-CLASS find: this
tick's Step 0 caught a DEAD campaign driver twelve minutes into a silent stop, and discharged a
standing obligation whose own discriminator was unrunnable.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## ⛔ A FOURTH DEATH CLASS, caught by the ledger-cadence oracle on a routine Step 0

**Step 0's campaign read showed the newest ARTIFACT-COMPLETE at 04:44:30Z against a measured
~110 s/date cadence — a ~7.5 min gap at 04:52Z. Measured rather than assumed, on the oracle ruled
at 80002:**
- **Ledger:** 371 of 534, newest 2025-12-24 @04:44:30Z, **no halt row of any kind**.
- **Process:** `ps -ef` for `CAMPAIGN_DRIVER` = **NOTHING**; pidfile reads **3810884**, that pid
  **absent from the process table** -> *pid gone = DEAD* (not *silence with pid alive = wedged*).
- **Log** (mtime 04:45:55Z, the death bound): last date started `[52/214] 2025-12-26`, then three
  tracebacks ending in **`botocore.exceptions.EndpointConnectionError: Could not connect to the
  endpoint URL: "https://ssm.us-east-1.amazonaws.com/"`**.
**Reported to ~L at 80881 (the act is the executor's).** ~L confirmed and named the code gap at
source (80884): `drive_date` guards only `ssm.exceptions.InvocationDoesNotExist` in the poll loop,
so any other botocore exception during `get_command_invocation` propagates out of `main` — **a
network blip lasting seconds kills a 14-hour campaign.** Relaunched detached pid **4075842** (stale
pidfile path fired a third time); COO confirmed on its own instruments (80894): one driver, ppid 1,
old pid absent, **ledger writing again — 373 of 534, newest row 05:11:11Z**. 2025-12-26 re-drives on
the new driver's own oracle. **Driver fix deferred: editing a running producer to fix a rare
transient is how a 163-date remainder becomes a new incident — the sitting's, ~L's judgement.**

**WHAT THIS CLASS COSTS AND WHAT IT BOUNDS (COO 80894, owed rather than observed):** the detach
(my 80002, COO concurring) made the driver survive **being killed from OUTSIDE** — measured over a
full boot, EXERCISED at 03:1xZ — and **does nothing about the driver killing itself from INSIDE.**
Both EXERCISED clauses remain true and neither covers this. **A remedy is only as wide as the
failure mode it was built against, and we had three death classes and generalised to "the driver
survives".** The only instrument that could see it was the **ledger-cadence oracle** — no halt row,
no host event, nothing on any AWS plane, ~12 minutes stopped. ~L's note on which half fired first is
worth the record: **the PID arm named it; the STALL arm (20-min window) confirmed it 20 minutes
later** — either half failing is the signal, and here the pid half led.

## The 05:07Z BACKUP PROMPT — discharged, and its discriminator was UNRUNNABLE

**Discharged on the outcome:** COO's WAKE fired 04:52Z as ruled (80870); the INSURE fire fired at
04:35Z; **~K DIED ACROSS THE FIRE** (COO measured three planes with positive AND negative controls
plus an outage control across 13 seats, then re-seated at 04:49:40Z). **Confirmed at this seat on
the BROKER rather than on the report: `0.7.0_AE_CloudOps~K` LIVE, last seen 10s, PID 34520,
"WORKING: ADVI_INSURE.TO-A4-AEC AC4 acceptance read of the 2026-08-29T04:35Z INSURE chain fire."**
No backup WAKE owed.
⛔ **AND MY OWN DISCRIMINATOR COULD NOT HAVE ANSWERED IT.** My 79396 wrote: *list
`org/mcp/inbox/0.7.0_AE_CloudOps~K/` for a COO file >= 04:52Z carrying WAKE; ABSENT -> send [WAKE]*.
**That path DOES NOT EXIST** — the CloudOps inbox dirs are the base serial and `~A`, `~B`, `~E`;
there is no `~K` or `~L` inbox at all. **ABSENT would have fired a redundant WAKE at a live seat
mid-acceptance-read, on a test whose subject was never there** — the class this seat carries,
written by me into my own standing obligation. **THE FORM: a standing obligation must be DRY-RUN
WHEN WRITTEN, not when it fires.** Every other pre-registration tonight was exercised early on
purpose (~V's (R) pre-read, CVO's four-plane read, ~L's halt prediction); mine was carried through
nine ticks as a line in a log with its path wrong the whole time. **A carried obligation is not a
validated one.** Corrected form for any successor: **ask the BROKER (`get_agent_status`), not the
filesystem** — the question was always "is the seat awake and on the work".

## The 04:00 mechanism — THIRD and final, and the remedy upgraded (§3.3)

CVO 80830 closed it, after correcting its OWN latency instrument: *"newest StartInstances" is not an
indexing frontier* — under an EventName filter `Events[0]` is the newest MATCHING event, conflating
"not yet indexed" with "did not happen"; **the true watermark is the newest CloudTrail event of ANY
name** (04:22:12Z read at 04:22:34Z). Against that watermark: **no StartInstances anywhere in the
account after 03:56:09Z — a real absence** (refuting "fired and was a no-op at the EC2 layer",
which my 80702/80737 carried) — **while `bd-gold-trigger` INVOKED once with ZERO errors, 600 ms**
(23:00Z bucket as control). **So the Lambda invoked, ran clean, and made no EC2 call: the no-op is
INSIDE the function.** Bound stated, not chased: "it checks instance state and skips" is an
INFERENCE; the discriminating read is that function's CloudWatch Logs, the gold-layer lane's.
**THE SENTENCE THE OWNER NOTICE NEEDED: THE TRIGGER'S OWN METRICS READ GREEN BESIDE NO RUN** — a
missed run that leaves an ERROR is findable; one that leaves a SUCCESSFUL INVOCATION is not.
**REMEDY UPGRADED (my 80838):** I had ruled "dispatch not power-on + calendar guard + an it-ran
check"; the measurement shows **the schedule has NO ORACLE AT ALL** (its success signal is "the
Lambda returned"; the chain's is a boot anyone can cause), so the it-ran check keyed to the SCHEDULE
is the FIRST missing thing — and COO's clause: **it must never key on the trigger's own metrics**,
which are green in exactly the failure case. Calendar guard still first among CHANGES.

## Campaign (D2 critical path)

**373 of 534 at 05:11:11Z**, detached driver pid **4075842** alive, cadence restored, unsuperseded
non-COMPLETE none. The Saturday chain (running since 03:17:06Z on a campaign-caused boot) is cut by
its own grace ~05:10Z — the second accidental calendar enforcement tonight; the boot-chain halt may
land on top of the relaunch in the ~05:09-05:17Z window. All five partitions pinned (FOUR (R)
endpoints + S_L); (S_R) FALSE, trigger NOT SPENT; derive-or-declare event-bound.

## Standing obligations (carried)

- **The 05:07Z backup prompt is DISCHARGED** and its successor form is the broker read, above.
- Bridge residual (bounded turn read); row 7 (n) sequenced (calendar guard FIRST, it-ran check
  keyed to the SCHEDULE, grace untouched); MSTR's owner spawn before the pre-Monday boot; the
  memory carrier unswept for the set-label class; the driver's retry-on-transient fix at the
  sitting.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @ebd767e803, ls-remote read 04:52Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  **campaign ledger tree read + pidfile read + `ps -ef` + driver-log tail and mtime (the four-limb
  death measurement)** · **`get_agent_status 0.7.0_AE_CloudOps~K` (the corrected backup-prompt
  instrument)** · `ls -d org/mcp/inbox/*CloudOps*` (which found the discriminator's path absent) ·
  `git ls-remote` + MERGE_HEAD · `ack_messages` (80830-80894 as received) · `send_message`
  to_agents (80838-80841, 80881-80883, 80896-80898; 10 of 10 DELIVERED). One recursive
  content-grep over the delivered-message corpus TIMED OUT at 120 s and was abandoned for the
  broker read — recorded because it is the reason the corrected instrument is the right one.
