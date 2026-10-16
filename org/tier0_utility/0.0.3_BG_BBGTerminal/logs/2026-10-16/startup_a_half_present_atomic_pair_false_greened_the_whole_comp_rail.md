# Startup 2026-10-16T01:5x-02:3xZ -- a half-present atomic pair false-greened all 102 comp-tools, and a thread daily was missing

**archetype:** MIXED

Session start on site Z. `/watcher` then `org/XXX.md` + `prompt.md` On-Launch. Two defects found,
both repaired in-session; one measurement routed and ruled on; one record reconstructed.

## 1. Launch state -- all gates read, not assumed

| step | result |
|---|---|
| registration | was **NOT REGISTERED**; registered PID 33468 |
| inbox watcher | census 0 rows -> armed (task `brwgi23uo`, pid 4672); expired at 1770 s, re-armed same turn (task `b2kqznulv`, pid **26472**), census 1 row, nothing reaped |
| delivery ledger | **25/25 READ, 0 unacked**, inbox empty |
| identity gate (2a) | **PASS** -- `whoami` on `opal-gateway-bbg` = `opalbloomberg@opalinvest.com`, not Andrew |
| `bloomberg_health` | `ok: true`, `127.0.0.1:8194`, `//blp/refdata` |
| Teams Monitor | armed; **ARM RECEIPT read before serving anything**: `identity=517aa5ee-...` (the oid pin, not BARE), `channels=1`, `cursor=2026-10-15T20:10:39.653Z` |
| task orders | **0 active**, denominator 7113 scanned |
| crons | **zero armed**, per the XXX.md Step-F table for this serial |

**The cursor is not backward.** `cursor=20:10:39.653Z` is exactly my own last outgoing message of
10-15 (msg `1792095039653`), so the arm sits at the newest served point -- no SUSPECT-REPLAY
condition, nothing to re-serve. Checked rather than assumed, per `refs/TEAMS_DUTY.md`.

## 2. DEFECT ONE -- `python3` had only half its atomic pair, and 102 tools returned rc=0 saying nothing

`org/XXX.md` step 1b-A.3 prints two lines. The first read **`PATH: 102 of 102 comp-tools resolve
bare`**. The second read **`EXERCISE: *** RESOLVED BUT DEAD ***`**. The first was true and
meaningless; the second was the whole finding.

**Mechanism, measured:** `~/bin` held **`python3.cmd` but not the extensionless `python3`** -- and
that `.cmd`'s own header says *"ATOMIC PAIR: both files or neither."* PATHEXT makes Windows shells
prefer the `.cmd`, so **PowerShell resolved `python3` fine**; bash ignores `.cmd`, fell through
`~/bin` to `AppData/Local/Microsoft/WindowsApps/python3` -- the **App Execution Alias stub** -- which
prints its Store advert **on STDOUT** and **exits 0**.

Every `.tools/comp-*` carries `#!/usr/bin/env python3`. So **all 102 returned rc=0 with the advert as
their answer.** `comp-which` printed the advert. So did `comp-find`.

**Repaired** by writing the missing half (`file:///C:/Users/Opal%20Bloomberg/bin/python3`; prefers the
Python311 user install, measured 3.11.9, falling back to Python314). Re-exercised: A.3 now reads
**`EXERCISE: a forwarder RAN`**, and `comp-find` returns real output -- including a real pathspec
ERROR, which is itself the proof the engine was reached rather than the stub.

**Why this is worse than a loud break, and the general form.** The sibling defect already banked on
this box (bare `python` on a gutted Python314) died **loud**: rc=1, no output, outside the script's
own exit contract. This one **succeeds**: rc=0, plausible-length stdout, empty stderr. A rail built
to stop blind grep was answering nothing, and no instrument said so. **An atomic pair is a
two-member denominator -- count both members, never one**, and `command -v` proves a FILE is
reachable, never that it ANSWERS.

**Surfaced, not fixed beyond the repair:** `python3` is **not** in `provision-path-shims.sh`'s named
non-comp set (exactly `aws` + `check-inbox`), so that script cannot regenerate it and A.3's own
"run provision-path-shims.sh" hint **cannot fix this class**. `org/XXX.md` is LOCKED and the script
is `0.8.0_AE_CloudComp~D`'s. Routed to `0.0.0_AB_MSTR~Z` as this box's integrator, one ask, DELIVERED
02:24:41Z.

## 3. DEFECT TWO -- 10-15 was served and never recorded in thread memory

`prompt.md` makes thread memory the carrier of what is OWED; the serve loop's step 4 writes it.
**The 10-15 session did steps 1-3 and not 4.** Newest daily in every thread dir was **10-14**, so
recall on 10-16 would have read 10-14 as current and been blind to two live Andrew-directs and a CTO
ruling. The session log and a deliverables record held it; the carrier recall reads did not.

**Reconstructed** from the day's own logs, not from memory, as
`threads/2026-08-07-andrew-capability-roster/2026-10-15.md` (5811 B, 0 non-ASCII), labelled
written-late in its own header, plus a `THREAD.md` Day-index entry. The pre-existing
"index gap, stated not filled" note was widened to name 10-10..10-14 rather than left reading as
though the gap were smaller than it is.

**I got my own census wrong first and caught it.** My first pass matched `.md` only, and the ruled
daily format is `.jsonl` from the 2026-08-21 boundary -- so my denominator was scoped to where I
expected the answer, not to where it could be. Re-ran across both extensions: same verdict, but the
first read was unsound and would have been unsound in the other direction just as easily.

**And the re-run surfaced a declarative drift worth naming:** **30 of 30** dailies under `threads/`
are `.md`; **zero** are `.jsonl`, including files created nearly two months after the boundary that
`refs/THREAD_MEMORY.md` says is binding (CVO~Z verdict @07988f39fb). I wrote `.md` to match 30/30
practice and my own recall path rather than fork the format on a lone file. **`refs/` is unwritable
from this seat by design**, so the doc-vs-practice gap is surfaced, not resolved.

## 4. R8's two halves do not land together -- measured, routed, ruled

My one dated obligation is to read the **10-16 11:00Z** fire. Its precondition is whether the CTO's
R8 ruling (@079108405c, msg 34565) is in the tree the scheduled task runs. **`OPAL_BBGTML_daily_pull`
runs `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` from the shared working tree, not a
worktree pin** (read off the task's own Actions), NextRun 10-16 07:00 local.

| R8 change | state on `box/sitez` @`0faeb93352` |
|---|---|
| submit: settle-until-stable-foreground | **LANDED** -- bounded settle loop present, plus R7's 5 `Get-FgTrace` |
| verify: re-derived glyph fixture | **NOT LANDED** -- `bbg_verify.ps1` untouched since **08-20** @`0387041915` |

The commit message on the submit half read "(branch only)", which would have been the wrong thing to
conclude from: the file **is** in this working tree. Checked the file, not the message.

**The sharp part, passed as data not direction:** the 08-20 battery's border-artifact mutant measures
**exactly 10** -- the same value signature A read. So widening `$uLo` to `len-2` to absorb the
post-10-06 rendering would **re-admit that mutant**; re-deriving the fixture would not. Signature A
currently PASSES, so nothing blocked tomorrow either way -- the hazard is latent, which is exactly
why it needed saying while nobody was under pressure to touch it. One ask to `1.0.0_SA_CTO~Z`,
DELIVERED 02:22:59Z.

### RULED 02:25:50Z -- msg 34652, acked

`1.0.0_SA_CTO~Z`, addendum @`46f4d60360` (LOCAL on `box/sitez`), record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPAL_BBGTML_R8_STABLE_FOREGROUND_FIX_20261015_Z.md`:

- The fixture **does NOT land before 11:00Z -- deliberately.** Signature A passes, so an untouched
  `bbg_verify.ps1` **lets the fire grade the settle loop alone.** The deferral is a single-variable
  test, not an oversight, which is the one reading I had not considered.
- **Widening `$uLo` to `len-2` is REFUSED, on the mutant measurement.**
- Fixture parked as the next R-cell, cut by COO~ZB **after** the fire is graded.
- `bbg_verify.ps1` to be left as it is until then.

**So the gap was real, the reason for it was better than my framing, and the latent hazard is now
closed by a refusal rather than left to a future hand.**

## 5. My own broker staleness, recurring

`get_live_agents` read this seat **[STALE] (1845 s)** while it was working -- the same defect my
`2026-10-14` daily records against myself, from the same cause: re-arming watchers and censusing
processes without calling `heartbeat`. A watcher census proves the WATCH is alive; only a heartbeat
proves the SEAT is, and peers route on the broker. Corrected 02:2xZ.

**And the broker corrected a second assumption:** `liveness.json` carried **3 rows**;
`get_live_agents` returned **10 LIVE**. Had I read the file as the roster I would have called a busy
fabric quiet.

## 6. Daily guardrail -- the two artifacts I own are GREEN, and the endpoint's own top-level field says STALE

`portal_get_pipeline_freshness` at 02:3xZ returns top-level **`as_of: 2026-09-30`, `stale: true`**.
**That is not a statement about this pipeline and must not be quoted as one.**

| source | cadence | data_as_of | behind T-1 | stale |
|---|---|---|---|---|
| **`data_pkl`** | weekly | **2026-10-14** | **1** | **false** |
| **`model_pkl`** | weekly | **2026-10-14** | **1** | **false** |
| `attribution_excel` | monthly | 2026-09-30 | 11 | true, **`frozen: true`** |
| `peer_excel` | monthly | 2026-09-30 | 11 | true, **`frozen: true`** |
| `cma_excel` | annually | 2026-12-31 | 0 | false |

The two PKLs are mine and both landed 10-15T14:30:42Z under execution `5c731d51`. At 02:3xZ
(= 10-15 22:3x ET, after the close) T-1 is 10-15, so **10-14 data sitting one trading day behind T-1
is exactly the expected pre-fire state** -- the 10-16 07:00 ET fire is what brings 10-15. Trading
calendar resolved before reading any of this, per CLAUDE.md NEVER#1.

**The trap, named because it is one line away from a false alarm:** the top-level `stale: true` is a
**minimum across five sources of mixed cadence**, and it is driven entirely by two sources that
declare `frozen: true` at the last month-end. A monthly artifact 11 trading days after 09-30 is
on-cadence, not late. **Nothing I own is stale, and the field that says otherwise is answering a
different question** -- the aggregate has no `freshness_basis`, so its verdict and the daily
pipeline's health are not the same claim.

## 7. The Teams watch expired at 1770 s, and proving the gap empty took TWO polls, not one

`timeout 1770` fired as designed (exit **124**, not a crash); orphan census **0** python rows, so
nothing survived the reap. Re-armed, pid 15620, receipt read: `identity=517aa5ee-...`, `channels=1`.

**The arm receipt carried the ambiguity:** `cursor=2026-10-15T20:10:39.653Z` -- **identical to the
previous arm**, so the 30-minute watch advanced it zero. The output file explains why it might not
have been quiet by choice: the pinned token **expired at cycle 1** (pin HELD, re-selected
successfully -- the engine's designed recovery, working), then a transient
`WinError 10054 connection forcibly closed`. **A quiet watch and a deaf watch produce the same
unchanged cursor**, and the cursor cannot separate them.

**Resolved by independent poll rather than by assuming either reading** -- and it needed **two**
calls, which is the part worth keeping:

| surface | instrument | result |
|---|---|---|
| DM + group chats | `poll_addressed_teams_messages since=20:10:39Z` | **0** |
| Opal Client Tickets channel | `read_channel_messages` (ids from `channels.json`) | **`@odata.count: 2`**, both 2026-08-20 own-account sends -- nothing since |

**The trap: `poll_addressed_teams_messages` does NOT cover channels.** Its own contract says
*"v1 covers DM + group chats; channel @-mentions are a fast-follow"* -- while the watch I armed
covers **1 channel**. So its `count: 0` is a complete answer for two of the three watched surfaces
and **silent about the client-facing one**. Reading that 0 alone as "nothing arrived" would have been
right today and wrong by exactly one surface, and the surface it omits is the one that matters most.
**The gap is empty on BOTH halves, measured separately.** No backlog sweep owed.

### Window 2 (02:2x-02:5xZ) and the pattern that only two windows could show

Expired 124 as designed, orphan census **0**, re-armed pid 14492. **Cursor advanced to
`2026-10-16T02:49:43.214Z`** -- exactly the last message served -- so the watch processed both
`[TEAMS]` events correctly and the output carried **exactly 2**, nothing missed mid-window. Tail
re-measured anyway on both surfaces (**0** DM/group since 02:49:43Z; channel still `@odata.count: 2`,
both 08-20): no gap.

**The pattern, which one window could not have shown:** `pinned token expired -- quiet retry, pin
HELD (cycle 1)` appears in **BOTH** windows, and **`cycle 1` is the FIRST poll after arming**. So the
token on disk is **already expired at every arm**; the engine re-selects and recovers, which is why
the watch works at all. Two consequences worth having in writing:

1. **Every arm opens with a failed poll**, and the recovery line is **stderr-only** -- so from inside
   the session a healthy arm and a degraded one are indistinguishable, which is the same
   stdout-receipt-vs-banner hazard the skill already names, one layer down.
2. **Window 2 ended on an expiry with NO re-select line after it** before `timeout` fired, so the
   last recorded state was degraded. That is exactly why the tail was re-measured rather than
   inferred from the advanced cursor -- **a cursor advances on messages, so it says nothing about the
   health of the silence after the last one.**

**Not re-filed: this is the Graph TTL item already standing in the OWED list as another seat's.** The
`cycle 1` / 2-of-2 measurement sharpens it and belongs in the record, not in an inbox (CLAUDE.md rule
31: FYIs and corroborations go to the record). Subsequent 30-minute re-arms are routine and get no
further entry unless the shape changes.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `comp-which "how do I grep the repo"` (XXX.md A.3) | **the Store advert, rc=0** -> after repair, the real router | **This is defect one.** Its value was entirely in the EXERCISE line; the `102 of 102` resolution count beside it was true while every tool was dead. |
| `comp-find 'glyph' integrations/bloomberg` | 9 hits / 101 files, all in `bbg_verify.ps1` | Located the verifier in one call after a `glyph` grep of `bbg_signin.ps1` returned **0** -- that 0 was correct and would have read as "R8's verify half is absent from the codebase" rather than "it lives in a sibling file". |
| `comp-find 'teams-watch.py'` | 1392 hits / 208044 scanned, banded | Found the arm line's home. The denominator is why I paged rather than treating page 1 as the answer. |
| `comp-find --name '*.md'` | **ERROR: pathspec selects 0 files** | The rail refused to return a zero it could not justify -- the documented "unrecognised flag becomes a pathspec" trap, caught by the tool instead of by me. |
| `to-check.py --all --assignee` | **0 active, 7113 scanned** | A bare 0 would have been unreadable; the denominator makes it an answer. `--all` is load-bearing. |
| `audit-archive-invoker.py` | rc=1, 16 findings, archive **deferred** (lane not GOVERNANCE_AUDIT-permitted) | All 16 are owned classes (the `git-author-override-audit.log` non-append is the known 1b909ec898 reorder). Re-filed none. |
| `Get-ScheduledTask` + Actions for `OPAL_*` | 14 tasks; daily_pull targets the shared tree, NextRun 10-16 07:00 | Settled "does the fix reach tomorrow's fire" by reading the task's own target instead of assuming the repo path. |
| `get_live_agents` vs `liveness.json` | **10 LIVE** vs **3 rows** | Two liveness surfaces, one authoritative. Also caught my own STALE. |

## Owed

- **Mine, dated:** read the **10-16 11:00Z** fire result and report. Unattended success would be the
  first since 10-04; failure yields R7's trace naming the foreground thief. **The fire now grades the
  settle loop alone**, per the 02:25:50Z ruling -- a cleaner test than it would have been.
- **CLOSED 02:34:09Z, msg 34661 (acked):** `0.0.0_AB_MSTR~Z` added the `python3` pair as
  `provision-path-shims.sh`'s **third** named non-comp entry at `a9147c39fb` (+34/-2), interpreter
  `py.exe -3` with **no user path baked** -- a better form than my restored shim, which bakes
  Python311. He did not re-run the full script, so my `~/bin/python3` stays live until the next
  re-provision rewrites it. **Verified his equivalence claim rather than accepting it:** `py -3` on
  this box resolves to **3.11.9 / Python311**, the same interpreter mine picks. That check was worth
  running -- `py -3` selects the highest REGISTERED Python 3, and if it had resolved to Python314
  (measured gutted on 09-28) the re-provision would have silently repointed the shim at a
  known-broken interpreter. It does not. This same session's three files are committed at
  `1d9aaa3abb` (287 insertions); both commits **LOCAL** on `box/sitez`, origin read at `569e4bb77e`
  via `ls-remote`, carried by the next box pass.
- **Carried on his word, unchanged:** 3 Teams items plus Alyssa's detail; the 22:26Z screenshot
  unviewed by choice; Graph TTL; Z6 R5 under COO~ZB; two serving-path fixes with CTO~Z. COMM_ASSIST
  r14 E1 test email remains NOT-ATTEMPTED-BY-POLICY.
- **Not mine, surfaced:** the `.jsonl`/`.md` daily-format drift (30/30 `.md`) -- needs a `refs/` writer.
- **Not mine, closed tonight:** the `$uLo` widening hazard, refused by ruling.
