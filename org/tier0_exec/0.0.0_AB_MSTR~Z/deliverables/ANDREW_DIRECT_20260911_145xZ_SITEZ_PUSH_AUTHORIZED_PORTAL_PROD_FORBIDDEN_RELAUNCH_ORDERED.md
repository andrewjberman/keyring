# ANDREW-DIRECT 2026-09-11 ~14:5xZ -- SITEZ push authorized, portal PROD forbidden, relaunch ORDERED

**archetype:** COORDINATE

**Channel:** Andrew-direct at the `0.0.0_AB_MSTR` (laptop) terminal, relayed verbatim to this seat
over the agent bus as MessageId `db01766b-c4ff-4f49-b996-7f41a5d46250`, 2026-09-11T14:52:48Z.

**Received by:** `0.0.0_AB_MSTR~Z`.

## THE ORDER, VERBATIM AND ENTIRE

> "They should not be pushing any portal work to prod, they can commit/push to DEV only when it
> relates to PORTAL. However if they want to push to SITEZ for ajb_workspace, that's fine. In either
> case they need to see who was last online pre-reboot and bring them back and get that device up to
> speed."

## WHAT IT AUTHORIZES, AND WHAT IT DOES NOT

| surface | standing |
|---|---|
| SITEZ / `ajb_workspace` push | **AUTHORIZED** -- "if they want to push to SITEZ for ajb_workspace, that's fine" |
| portal **PROD** | **FORBIDDEN, FLAT** -- "should not be pushing any portal work to prod". No qualifier, no condition |
| portal **DEV** | **PERMITTED ONLY FOR PORTAL WORK** -- "only when it relates to PORTAL". The constraint is on the **CONTENT**, not the branch: a DEV push carrying non-portal work is outside his word |
| relaunch of the pre-reboot seats | **ORDERED** -- "see who was last online pre-reboot and bring them back and get that device up to speed" |

**THIS SUPERSEDES THE HOLD.** Twenty minutes earlier `0.0.0_AB_MSTR` correctly told this seat to hold
`@9dfe8e1115`, because Andrew's prior word ("push cloud sure but wait on DEV") named CLOUD and DEV and
not SITEZ. **He has now named SITEZ.** The hold was right when given and is discharged by a later
ruling, not by anyone's reinterpretation of the earlier one.

> **The asking is what produced the ruling.** This seat declined to read "push cloud" as reaching
> SITEZ and said so rather than widening. Recorded because the cheap move -- assuming the authority --
> would have produced the same push with no ruling behind it, and nothing would have looked different.

## WHAT THIS RULING DOES *NOT* REACH -- stated because the adjacency is the hazard

⛔ **THE CLOUD->SITEZ MERGE LEG IS STILL GATED AND HE HAS NOT GIVEN IT.** "Push SITEZ is fine" is not
"merge CLOUD into SITEZ". They are different acts with different blast radii: the push publishes this
device's own commits; the merge imports 119 CLOUD commits into this branch and is the precondition for
the audit-archive repair. This seat's `/integrate` run was **assess-only** and nothing in tonight's
word changes that. Flagged by `0.0.0_AB_MSTR` in the same message and agreed here.

⛔ **"UP TO SPEED" IS NOT INTERPRETED, BY EITHER MSTR.** He said bring them back and get the device up
to speed. What each returning seat then does is **that seat's own startup law, its own record and its
own lane** -- not a re-tasking from an MSTR. Relaying, not adjudicating.

## THE FIVE TO RELAUNCH, FROM THIS SEAT'S OWN PRE-REBOOT ROSTER

| serial | runtime | pre-reboot log |
|---|---|---|
| `1.0.0_SA_CTO~Z` | codex | @1d36e8df4c |
| `2.0.0_SA_COO~Z` | claude | @23783dd2b6 |
| `2.0.0_SA_COO~ZZZ` | claude | @b8386bea24 |
| `3.0.0_SA_CVO~Z` | codex | **NEVER LOGGED** |
| `4.0.0_SA_CRO~Z` | codex | @c187072692 |

**`3.0.0_SA_CVO~Z` is the one seat with no log of its own to resume from.** Its owed acts (the v0.4
ratified-text sign; round-4 L8/L9/L10) are carried in the `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~ZZZ`
logs, so nothing waits on it -- but it must be **told** that at launch rather than left to discover it
by finding an empty logs dir.

## THE ORPHANED-LAUNCHER TRAP -- DOES NOT APPLY HERE, AND WHY

`0.0.0_AB_MSTR` hit this on the laptop this morning and flagged it so this seat would not hunt for it:
`start-codex-seat.ps1` runs codex INLINE and `-NoExit` leaves the launcher shell holding the seat's
`OPAL_SPAWN_MARKER_v1` serial, so a dead codex seat can leave a LIVE launcher window with zero
children, and `/mstr-spawn` step 1b then refuses the relaunch as a duplicate until the shell is
reaped.

**A REBOOT CLEARS ALL OF IT.** This box booted 2026-09-11T14:10:36Z and this seat measured **zero
`codex.exe`** -- so there are no stale markers and no orphan shells. Spawn clean.

⚠ **STILL RUN PROCESS TRUTH FIRST ON EACH SERIAL** -- not for orphans, but because **Andrew launches
seats by hand and the spawn tool's own checks are blind to an Andrew-launched session.** He is at this
device.

## ACTS TAKEN BY THIS SEAT UNDER THIS RULING

Recorded as they are executed; see the session's commits.

1. This record, committed on this seat's serial.
2. SITEZ push of the held `@9dfe8e1115` plus this record -- **authorized tonight, not inferred.**
3. Relaunch of the five, process truth first on each serial.

**NOT done:** the CLOUD->SITEZ merge (gated), any portal push of any kind (PROD forbidden; DEV is
permitted only for portal content and this seat is carrying none), any re-tasking of a returning seat.

---

## AMENDMENT 1 -- 2026-09-11 ~15:0xZ: THE PORTAL DEV LINE ABOVE IS SUPERSEDED. NOTHING PORTAL MOVES.

⛔ **STRIKE the `portal DEV -- PERMITTED ONLY FOR PORTAL WORK` row in the table above, and the clause
in the NOT-done paragraph that repeats it.** They record the rule as it was relayed at 14:52Z and it
was overtaken five minutes later. They are left in place rather than edited away so the supersession
is legible, but **they are NOT the operative rule.**

**Andrew-direct at the `0.0.0_AB_MSTR` terminal, 2026-09-11 ~15:0xZ, VERBATIM AND ENTIRE:**

> "nobody does any portal promotes until i say so is the takeaway here."

Relayed as bus `cef9fc66-a72f-44fb-8981-82d563752adb`; acked by this seat as `4b855ca8`.

He gave this as **THE TAKEAWAY** -- the rule to carry forward -- immediately after `0.0.0_AB_MSTR`
asked him whether "can commit/push to DEV only when it relates to PORTAL" lifted a portal DEV hold.

**THE OPERATIVE RULE IS THE SIMPLE ONE, NOT THE NUANCED ONE:** nothing portal moves, **DEV included**,
until he names it. Neither MSTR is adjudicating whether "promote" technically excludes a DEV push --
it might, but he was answering a DEV question and framed the answer as the takeaway rather than as a
further qualifier. **The faithful read is the conservative one:** the cost of being conservative is a
delay; the cost of being wrong is an unauthorised move on a client-facing surface. If a portal DEV
push genuinely blocks someone, **ASK HIM** rather than reason from the relay or from this paragraph.

**Applied symmetrically at the other end, which is why this is a rule and not a fabric-local hold:**
the laptop's own portal DEV push (10 commits, IRPT_FNTEND, typecheck-green at `32a744dc`) STAYS HELD,
and `2.0.0_SA_COO~F`'s workspace gitlink bump stays held behind it.

**NO ACT OF THIS SEAT IS AFFECTED.** This seat is carrying zero portal content. The `portal/`
submodule is dirty in this worktree -- it was dirty at session start, inherited, not touched here --
and it was not staged, not committed and not pushed. The two commits this session are both `org/`
records.

**UNCHANGED AND STILL LIVE:** the SITEZ push authorization (exercised -- see Amendment 2), the
relaunch order (executed -- see Amendment 2), and the CLOUD->SITEZ merge leg remaining **GATED**.

> **WHY THIS AMENDMENT EXISTS AT ALL, and it is the transferable part:** the superseded line was
> already **COMMITTED AND PUSHED** when the correction arrived. A superseded rule sitting in a PUSHED
> record is worse than one in a local draft -- **the next reader has no signal it was overtaken**, and
> the record's authority is exactly what makes the stale line dangerous. Same class as a stale
> citation. The remedy is an amendment that strikes it by name, never a rewrite of the pushed commit.

## AMENDMENT 2 -- 2026-09-11 ~15:0xZ: the push and the relaunch, as executed

**SITEZ PUSH -- DONE.** `83c719e2af..c00e5ee902`. Verified from the REMOTE (`ls-remote`), not from the
push output: `origin/SITEZ` = local HEAD = `c00e5ee902`, 0 ahead. Payload 2 commits, both this seat's;
no other lane's work rode it. **Deploy ceiling re-read in the SAME BREATH as the push** (a ceiling
older than the push is a floor, not a ceiling): **0** files under `data/*/scripts/**`, and
`safe-deploy`'s own run agreed -- "no deploy-scope script files detected, nothing to do". **That push
deployed nothing**, on two instruments rather than one.

**RELAUNCH -- ALL FIVE LAUNCHED.**

| serial | launcher | marker pid |
|---|---|---|
| `1.0.0_SA_CTO~Z` | `spawn-agent.ps1` (claude) | 39200 |
| `2.0.0_SA_COO~Z` | `spawn-agent.ps1` (claude) | 40144 |
| `2.0.0_SA_COO~ZZZ` | `spawn-agent.ps1` (claude) | 40728 |
| `4.0.0_SA_CRO~Z` | `spawn-agent.ps1` (claude) | 42776 |
| `3.0.0_SA_CVO~Z` | **`ajb2` (codex)** | 42728 |

⭐ **THE RUNTIME SPLIT WAS MEASURED HERE, NOT TAKEN FROM THE RELAY.** `0.0.0_AB_MSTR` listed CTO~Z,
CVO~Z and CRO~Z as codex seats. **On THIS device only `3.0.0_SA_CVO~Z` has a `.runtime/codex-seats/`
directory** -- it is the sole entry -- and it is also the only one of the five showing the codex
send-path signature in `agent-spawn-audit.log` (repeated `IDENTITY_SEND_UNVERIFIED ... never called
register_agent` across rotating pids). `2.0.0_SA_COO~Z` has an explicit `SPAWN` line from
`spawn-agent.ps1`, which is the claude path. The relay's "both dead codex seats" referred to the
**LAPTOP's** box; generalising it to site Z would have put two seats on the wrong runtime.
**A peer's roster is evidence about the peer's device.**

⚠ `spawn-agent.ps1` has **no codex path** -- it always runs `ajb -Headless`. The CVO~Z window was
therefore launched by mirroring that script's detached-window pattern with `ajb2`, **carrying the same
`# OPAL_SPAWN_MARKER_v1: <serial>` literal** so `/mstr-kill` and the concurrency cap still track it.
A codex seat launched without that marker is invisible to both.

**`--say` hints were deliberately minimal and factual** -- each seat was pointed at its OWN pre-reboot
log commit and nothing more. **No work-state assertion was written into any hint**, and no returning
seat was re-tasked: "up to speed" is not interpreted by either MSTR, and what each seat does next is
its own startup law, record and lane.

⚠ **`3.0.0_SA_CVO~Z` HAS NO LOG OF ITS OWN TO RESUME FROM** -- it never answered the pre-reboot /log
census. Its owed acts (the v0.4 ratified-text sign; round-4 L8/L9/L10) are carried in the
`1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~ZZZ` logs, so nothing waits on it, but it must be **told** that
rather than left to discover an empty logs dir. ⛔ **"SO NOTHING WAITS ON IT" IS STRUCK -- SEE
AMENDMENT 3. IT IS FALSE AT THE ARTIFACT.**

### A PROBE THAT MEASURED ITSELF -- caught before it was reported, and the sign is the point

The first process-truth pass matched **all five serials to a single pid** -- which was **this seat's
own PowerShell probe**, whose command line contained the five serials because the query had put them
there. Re-run excluding self AND parent: exactly one non-self `claude.exe` (`0.0.3_BG_BBGTerminal`),
**zero `codex.exe`**, and a negative control confirming no live process named any of the five.

`/mstr-spawn` step 1b already documents this class as the "scanner-self false-positive (empirical
2026-05-26)" with the `$_.ProcessId -ne $selfPid` remedy. ⭐ **But the documented instance matched ONE
serial and produced a false REFUSE -- which fails safe and announces itself the moment you act. This
one matched FIVE and would have produced a false HEALTHY: "the fabric is up, nothing to relaunch."
That never announces itself.** The skill's note covers only the fail-safe direction, and **a
multi-term query is what flips the sign**: the more terms in the query, the more convincing the
self-match looks. Worth folding into the skill by whoever owns it (`1.0.0_SA_CTO`); recorded here
because the asymmetry, not the trap, is the new part.

---

## AMENDMENT 3 -- 2026-09-11 ~15:2xZ: ALL FIVE ARE LIVE; and "SO NOTHING WAITS ON IT" IS STRUCK

### The struck sentence, and why it was wrong

Amendment 2's roster section said `3.0.0_SA_CVO~Z`'s owed acts are carried in the `1.0.0_SA_CTO~Z` and
`2.0.0_SA_COO~ZZZ` logs **"so nothing waits on it."** ⛔ **The first half is true. THE SECOND HALF IS
FALSE AT THE ARTIFACT and is struck.**

**The falsifier, measured by two seats independently within the same quarter-hour:**
`python .tools/prd-signoff.py status AMGT_RESAPP` reads **WITHHELD** -- the ratified-text half is
STALE on `3.0.0_SA_CVO~Z` (signed at v0.3; bytes since moved to `f576e011be53`) -- and **two live
seats were parked behind it**: `2.0.0_SA_COO~ZZZ`'s own broker summary read "surface round v5 (PARKED,
gated on CVO v0.4 sign)", and `1.0.0_SA_CTO~Z` could not grade round 4 at L10 without the slug.

**What was carried is the CVO's CONTEXT, not the fabric's ability to proceed without it.** Those are
different claims and the sentence conflated them. Caught by `1.0.0_SA_CTO~Z` (msg 21403) and
independently by `2.0.0_SA_COO~ZZZ` (msg 21404).

⭐ **THE PART WORTH KEEPING: `2.0.0_SA_COO~ZZZ` named the NARROW reading under which the sentence is
true** -- nothing waits on the absent LOG -- **said that was how it read it, declined to adjudicate
which reading was intended, and routed the ambiguity anyway.** A sentence that is true under the
author's reading and false under a natural one is not a harmless imprecision when it sits in a record
that sets a relaunch priority: it could have de-prioritised the one spawn that unblocked two seats.
**Both seats routed rather than absorbed, and neither re-litigated it.**

### All five are LIVE

| serial | evidence |
|---|---|
| `1.0.0_SA_CTO~Z` | broker LIVE, Monitor `bknashx5c` |
| `2.0.0_SA_COO~Z` | broker LIVE, Monitor `bcushi3e1` |
| `2.0.0_SA_COO~ZZZ` | broker LIVE, Monitor `bjompscuw` |
| `4.0.0_SA_CRO~Z` | broker LIVE, Monitor `bbkr8d2lo` |
| `3.0.0_SA_CVO~Z` | broker LIVE PID 38960, "codex seat bound thread=01a0910a bridge=43128 detector=2812" |

**The CVO was corroborated on a second grain rather than the broker alone:** every file in
`.runtime/codex-seats/3.0.0_SA_CVO~Z/` was rewritten at 15:16Z, having been frozen at pre-reboot
timestamps 04:02-10:09, and `turn-bridge.stdout.log` kept growing after.

### ⛔ THE CODEX RELAUNCH FAILED THREE TIMES AND LOOKED HEALTHY EVERY TIME

**This is the transferable finding of the relaunch.** `3.0.0_SA_CVO~Z` was never missed and never
de-prioritised -- it was attempted first and failed silently three times, each attempt leaving a
launcher window with **the correct command line, the correct `OPAL_SPAWN_MARKER_v1`, and zero
children.** Nothing in the window, the marker scan or the concurrency count looked wrong.

**ROOT CAUSE, from CAPTURED STDERR rather than inference:**

```
. : The term 'C:\Users\Opal' is not recognized as the name of a cmdlet...
+ . C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.tools\ajb2.ps1; ajb2 ...
```

This workspace path contains a **SPACE** ("Opal Bloomberg"). `CommandLineToArgvW` **CONSUMES** the
double quotes around a dot-sourced path, so the launcher received `. C:\Users\Opal` and split on the
space. **FIX: dot-source the 8.3 SHORT path** (`C:\Users\OPALBL~1\Desktop\AJB_WO~1\TOOLS~1\ajb2.ps1`),
which contains no spaces and therefore needs no quotes.

⛔ **`spawn-agent.ps1` ALREADY DOCUMENTS THIS EXACT HAZARD IN ITS OWN COMMENTS -- for its `wt`
transport only** ("CommandLineToArgvW ... CONSUMES `\"` characters -- a dot-sourced `. \"$ajb\"`
arrives BARE and splits on whitespace, **fatal on any clone path containing a space (and silent on one
that doesn't)**"). **And `spawn-agent.ps1` has NO CODEX BRANCH AT ALL** -- it always runs
`ajb -Headless`. **So on a space-containing checkout, a codex seat cannot be relaunched by the standard
primitive, and the failure is silent.** Routed to `1.0.0_SA_CTO` as the tooling owner; **not edited
here** -- no tool change and no gate without Andrew's word.

⚠ **TWO HYPOTHESES WERE TESTED AND DISPROVEN FIRST, recorded so nobody retries them:**
1. *"codex does not resolve under `-NoProfile`"* -- **FALSE.** `codex.exe` resolves identically with
   and without the profile (`C:\Users\Opal Bloomberg\.bun\bin\codex.exe`, machine PATH). This one was
   plausible because the predecessor's log credited "profile dot-source" for a working launch.
2. *"the `wt` vs `Start-Process` transport"* -- **FALSE.** Both failed, including `wt` with the short
   path, which is the form `spawn-agent.ps1` itself uses.

>> **Neither was resolved by reasoning about it; both were killed by ONE run with stdout/stderr
   redirected to a file. Three attempts were spent on hypotheses and one on a capture. The capture
   should have been first** -- a silent failure with a healthy-looking artifact is exactly the case
   where the cheap move is to make the process talk, not to theorise about why it is quiet. <<

### D7 -- DIAGNOSED ON THE LAPTOP SIDE; the parked carrier is updated, not closed

`1.0.0_SA_CTO` (laptop, msg 95986, relayed as bus `45a2fa1f`) answered the exact UNKNOWN the park file
named as the first thing an owner should check: **`opal-tickets` status-index query for `open` returns
Count 0** -- so **nothing is queued behind the 403 and no client is waiting.** See the carrier file for
the mechanism and the remedy; it remains PARKED because the remedy is Andrew's.

