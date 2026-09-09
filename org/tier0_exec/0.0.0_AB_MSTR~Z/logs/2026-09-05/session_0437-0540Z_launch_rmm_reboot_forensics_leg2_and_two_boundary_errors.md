# Launch after an RMM reboot, the leg-2 close, and the same boundary error in both directions -- 0.0.0_AB_MSTR~Z

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DIAGNOSE

**Date:** 2026-09-05 0437-0540Z
**Task Order:** none (launch + standing MSTR duties)
**Status:** COMPLETE for everything in lane. Two items at Andrew, both named below, neither startable here.

## Objective

Launch this seat after the device came back from a reboot, answer Andrew's two direct questions
(what is live on this device, and why the restart), and run the three arm-at-load steps the
XXX.md Step 1b-F MSTR row prescribes. Everything past that arrived unplanned: a BG report, a
cross-fabric reconcile close, and two instrument errors that crossed the device boundary in
opposite directions inside one hour.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-read | `org/XXX.md --for "standing duties / loop arming"` | PASS | Surfaced the 1b-F table; confirmed MSTR = watcher + agentbus + integrate, zero crons |
| comp-which | `"who owns directive D7 client ticket intake..."` | NOFIT | Correctly declined -- said NO CURATED RULE MATCHED and pointed at comp-find rather than ranking a guess as an answer |
| comp-find | `'opal_ticket_intake\|OPAL_D7_ticket_intake' --limit 25` | PASS | 318 hits / 52559 files, denominator printed; located `integrations/ticketing/intake/` |
| comp-read | `.owned-paths.yaml --enumerate 'ticketing'` | PASS | 0 hits -- a TRUE absence: that tree has no lane rule at all |
| comp-read | `org/missions/DIRECTIVES.yaml --enumerate 'D7'` | PASS | The find of the session -- see What worked |
| comp-read | `portal/src/App.tsx --enumerate 'Submit a Request' / 'Submit' / '[Tt]icket'` | PASS | Absence confirmed against a positive control |
| comp-read | `org/ref/SESSION_LOG_STANDARD.md --for "base template headings"` | PASS | This file's shape |

**What worked:** `comp-read --enumerate 'D7'` on DIRECTIVES.yaml returned nine hits and its
QUALIFIERS band put lines 294/297/312 in front of me -- Andrew's 2026-08-25 "D7 is effectively on
hold" and the row's own "quiet weeks are EXPECTED, not stalled". I was one step from routing a
44.5h outage as a live client-facing problem. The qualifier band inverted the urgency of a finding
before it left this seat, which is precisely the right-file-wrong-conclusion failure the tool
exists to catch.

**What failed:** Nothing tool-side. The comp rail refused `comp-read ... | head -60` and the
refusal was CORRECT -- I piped a census into a receiver that erases its denominator. My error,
caught by the mechanism at the moment of the act, which is the intended teaching surface.

**Gap found:** `comp-which` has no curated rule for OWNERSHIP questions ("who owns X"). It
returned three IAM/authz tools at 0.34-0.38 and honestly labelled them FUZZY GUESSES rather than
routing. The honesty is the right behaviour; the gap is that "who owns this surface" is a common
question with a real answer path (`.owned-paths.yaml` + the directive register) and no catalog
entry. Worth a rule; not filed as a surprise row because it is a catalog gap, not a project
defect.

## Work Completed

### 1. Launch, three steps, zero crons

`/watcher`: registration read STALE at PID 20424. Ran the discriminator rather than assuming a
context-clear -- `tasklist` showed 20424 DEAD against a positive control (PID 4524 returned a
row), so it was a genuine orphan and the serial was safe to retake. No `inbox-watch` process
existed for any serial. Armed Monitor `bi12ufuzi`, banner `parent-tied: pid 5233` (armed, not
orphan-capable), watching the canonical NESTED path `org/mcp/inbox/0.0.0_AB_MSTR/~Z` -- not the
flat decoy. Confirmed with `TaskOutput -> running`, the only check that observes a consumer.

`/agentbus`: measured the device rather than assuming it (`device` -> `sitez`, basis workspace
path). No consumer held the lock. Armed Monitor `br32cr0rk`, confirmed running. Both queue depths 0.

`/integrate`: ASSESS-ONLY per the standing rule. Clone complete, SITEZ current 0/0 @ea1835863e.
BASE b000632f27 == the origin/CLOUD head exactly, so CLOUD ahead 0 / SITEZ ahead 17, overlap 0
files, `merge-tree` rc=0.

### 2. Andrew's two questions, answered from measurement

LIVE ON THIS DEVICE: two seats, not the thirteen the broker listed. Tested all 13 PIDs
individually -- eleven DEAD, records persisting only because a reboot gives no seat the chance to
deregister. `0.0.3_BG_BBGTerminal` read STALE and was ALIVE. The broker label was wrong in BOTH
directions, which is why the process table, not the listing, was the instrument.

WHY THE RESTART: Event 1074 names `winagent.exe` (N-able Advanced Monitoring Agent) acting for
NT AUTHORITY\SYSTEM, Planned, 00:30:10 local, comment "Your IT Support provider has initiated a
reboot of this device." The four prior 1074s on this box are all `StartMenuExperienceHost.exe` on
behalf of the human user -- a built-in contrast proving the discriminator discriminates rather
than always saying RMM. Seats died in a tight cluster 00:34:59-00:35:11 (mass termination, not
drift); boot 00:35:52; the only two live sessions both started 00:37:1x. Nothing respawned.

### 3. BG msg 20504 -- received, READ-acked, both findings dispositioned

Bloomberg DAPI DOWN: caused by the same reboot. BG worked four P0 remedies, eliminated three, and
deliberately did NOT fire the sign-in because the scheduled fallback carries a FIRE-ONCE 6h budget
and a manual attempt at 01:00 ET would convert today's 11:00Z fire into an escalation. That is a
mechanism, not caution, and the named exception to the anti-coast rule. Accepted; nothing routed.

D7 ticket intake failing: corroborated the CURRENT failure on a SECOND instrument (Task Scheduler
`LastTaskResult=5`, State Ready, NumberOfMissedRuns 0) -- but recorded explicitly that this
instrument is single-valued and does NOT corroborate the 44.5h DURATION, which remains sourced
only to BG's log census. Then the register reframed it: D7 is ON HOLD by Andrew's own word and
nothing is lost (cursor unmoved). NOT routed, no seat spawned.

Incidental to that check: Andrew's order to pull the submit item DID land (`Submit a Request`
absent from App.tsx, positive control `[Tt]icket` returning 10 hits proves the zero is real). A
`Ticket Center` item survives at `App.tsx:118` in Tools with no `requiresAdmin` beside it.
Surfaced to Andrew as HIS call; NOT adjudicated here, because reading "that whole functionality"
wider or narrower than his words is exactly what a relay may not do.

### 4. Housekeeping BG could not do (it holds no git lane)

Swept the orphaned 2026-09-04 freshness-summons log @bc437390d7, 58 insertions / 0 deletions
(insertions-only is the expected shape for an append-only log, not the amendment-without-edit
tell). The halt-gate REFUSED the first push because this session had no serial file; satisfied it
by writing `org/mcp/sessions/<session-uuid>.serial` rather than overriding. Push verified by
`ls-remote` (the oracle, never the receipt): origin/SITEZ = bc437390d7. Deploy ceiling re-read in
the same breath as the push: 0, and safe-deploy independently confirmed "no deploy-scope script
files detected".

### 5. Cross-fabric: leg 2 closed, and two boundary errors

Sent the laptop the assessment; disclosed the vintage move unprompted when my own push moved the
ref their verdict was measured against. `0.0.0_AB_MSTR` ran leg 2 (origin/CLOUD cb82020ab1) and
verified rather than trusted -- every number reproduced.

ERROR ONE, MINE: I called leg 2 "a pure fast-forward". True against origin/CLOUD, FALSE where it
executes -- their local CLOUD was 54 commits ahead of the pushed head, so it was a real merge. A
fast-forward is not a property of the payload; it is a relation to a ref on a machine I cannot
read, and I asserted it in the same register as numbers that were sound. Conceded, banked.

ERROR TWO, THEIRS, 40 minutes later and in the opposite direction: a two-line `.git/hooks/pre-commit`
cliff fix (untracked, per-device, cannot travel by git). Correct on their box; its unstated
precondition is FALSE here. See Decisions Made.

## Decisions Made

1. **HELD the pre-commit hook edit rather than applying it.** Measured: `38a37be871` is on
   origin/CLOUD and NOT an ancestor of site Z HEAD (positive control ea1835863e -> HEAD YES, so the
   instrument discriminates); neither gate script reads `STAGED` from env (positive control: both
   DO read OPAL_AGENT_SERIAL / CLAUDE_CODE_SESSION_ID / SURPRISE_ROW_OVERRIDE, so the zero is a
   true absence and not a broken matcher); and EXERCISED, both bare calls return rc=0 "OK"
   denominator 0 dispatched path(s). Applying it today drops argv into scripts with no env limb:
   both gates grade zero paths and pass every commit. THE ARGV CLIFF FAILS CLOSED AT rc 126; THE
   REMEDY WOULD FAIL OPEN AT rc 0. Discharging that hazard arms a strictly worse one.
2. **Did NOT ack the final ACK-of-an-ACK.** The oracle exists to prove an agent read CONTENT
   someone is waiting on; nobody was waiting, and acking a receipt regresses without terminating.
   Deliberate deviation from the blanket ack rule, recorded here rather than left as an omission.
3. **Did NOT relaunch the fleet.** Fleet relaunch is the MSTR primitive, but WHICH seats resume is
   a work-composition call belonging to Andrew and the COO. Staged, not fired.
4. **Did NOT run leg 1.** Standing rule is assess-only at load; merge needs Andrew's word.
5. **Did NOT rewrite the shared memory index.** Measured 145 of 517 entries visible (cut at line
   146); 372 dropped silently every session. The prescribed remedy is arithmetically impossible --
   the 517 links ALONE are 53.6KB against a 17.1KB target, so only deleting ~430 pointers to live
   memories would satisfy it. That is a design change to state six seats share, not a tidy-up.

## Files Modified

| Path | What |
|---|---|
| `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-09-04/freshness_summons_step1_1139-1203Z.md` | Swept BG's orphaned log, @bc437390d7 |
| `org/mcp/sessions/<session-uuid>.serial` | Untracked; written to satisfy the halt-gate precondition |
| `~/.claude/.../memory/integrate-step2-is-blind-to-the-integration-window.md` | Outside the repo; extended with the VERB half and the bidirectional boundary rule |

## Blockers

**NOT BLOCKED.** Nothing at this seat waits on another seat. The laptop owes site Z nothing and
said so; leg 2 is closed both directions by its own measurement and mine.

**AT ANDREW (two, neither startable here):**
1. Fleet relaunch composition -- 11 seats down, including `2.0.0_SA_COO~Z` holding an open L4
   question on NFRA_OPSEC202609, seven `0.7.0_AE_CloudOps` lanes, and `3.0.0_SA_CVO~Z` carrying the
   LD-0318 SYSPARITY arm.
2. `/integrate merge` for leg 1 -- site Z is 56 behind origin/CLOUD. Also the precondition for the
   held hook fix.

## Current State

Site Z is reachable and current with its own branch. `origin/SITEZ` = `bc437390d7` = local HEAD
(ls-remote read this session). `origin/CLOUD` = `cb82020ab1`, 56 ahead of SITEZ; SITEZ 1 ahead of
CLOUD (the BG log sweep). Both `is-ancestor` legs read NO, which under the mutual-updatedness
objective is the EXPECTED live-fabric state and not a defect -- neither MSTR is chasing it.

Live on this device: `0.0.0_AB_MSTR~Z` (this seat, Monitors `bi12ufuzi` inbox + `br32cr0rk`
agentbus, both confirmed running) and `0.0.3_BG_BBGTerminal`. Eleven broker rows are ghosts of the
pre-reboot fabric with dead PIDs; they were not deregistered because the broker denies MSTR that
verb. Zero crons at this seat.

The pre-commit hook on THIS box still carries the two unquoted-argv lines at `.git/hooks/pre-commit:124`
and `:138`. That is the CORRECT state until `38a37be871` arrives via leg 1. Sequence to apply
afterwards: verify the ancestor -> confirm the env limb is in the MERGED copies -> change BOTH
lines together, never one -> re-exercise both bare calls and REQUIRE the "input N path(s) from the
STAGED environment variable" line to be OBSERVED, not inferred. If it does not appear, that is a
finding to send, not a mistake on this side.

Bloomberg DAPI is down and expected to self-heal at the 07:00 ET (11:00Z) scheduled fallback; the
FIRE-ONCE ledger was clear at 42h, so today's fire is unblocked. D7 ticket intake is still failing
every 5 minutes and that is acceptable under the hold; nothing is lost.

## Next Steps

1. **[Andrew]** Name the fleet relaunch set -- or "all" -- and this seat runs `/mstr-spawn`.
2. **[Andrew]** Word on `/integrate merge` for leg 1; it unblocks the hook fix as a side effect.
3. **[`0.0.0_AB_MSTR~Z`]** On that word: leg 1, then the hook sequence above, then report the
   EXERCISED result to the laptop either way.
4. **[Andrew]** The memory-index design call -- 28 percent of the shared index is loading.
5. **[Andrew]** Whether `Ticket Center` (`portal/src/App.tsx:118`) falls inside the 2026-08-25
   "that whole functionality" order. Not adjudicated at this seat in either direction.
