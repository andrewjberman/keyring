# st32: the library moved, and a hold I did not talk myself out of

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, COORDINATE

**Serial:** `0.7.0_AE_CloudOps~YC2` (lane, dell2)
**Window:** 2026-10-11 15:58Z -> 17:30Z. Prior log `5c0214665a`
(`st31_installed_and_a_reason_that_is_nowhere.md`).
**Orders:** `IRPT_YCDGEN.TO-APPLY-st32` (`<risk>WORLD</risk>`, cell `YCD-d-13`) and
`IRPT_YCDGEN.TO-APPLY-j4` (`<risk>SERVED</risk>`, same cell) -- both `complete`.
`IRPT_YCDGEN.TO-APPLY-x1dry` (`<risk>SERVED</risk>`, cell `YCD-c-14`) -- **`pending`, HELD, not run.**
**Commits:** `523077a89e` (st32 close), `1c6851461b` (j4 close), both ON ORIGIN at last read.

---

## Current State

Written for a reader with zero prior context.

**The resident host `i-0167fd745ad906a66` runs `/opt/irpt-resident/0485393f3a-st32`**, installed
16:09:55 UTC over the st31 this lane installed at 13:43Z. Active, `NRestarts=0`, MainPID `876525`,
0 tracebacks. Four roots now sit on the host (st32 running, st31, st30, st27).

**One host file moved, which no release before it did.**
`/opt/investor-reporting-ycharts/ycharts_session.js` went from st31's `857d90b8...` to the package's
`a1c2880169c5f799...`, with the old copy kept beside it as `ycharts_session.js.before-0485393f3a-st32`
and verified at st31's digest. st30 and st31 rewrote that file with byte-identical content; st32
changed it.

**All three of st32's changes are APPLIED, UNEXERCISED** -- the capture library and its persisted
receipt fire only at a capture, `cause_claim: measured` only at a fifth failed delivery, and none
runs at a restart.

**j4's baseline, delivered to a waiting run order:** `SIGNIN_LINES=0`, `CHILDREN=0`,
`TRACEBACKS_SINCE_START=0`, `POLLS_60S=3`, library still st32's, window = the unit's own
`ActiveEnterTimestamp` of 16:09:55 UTC. TCKT_VNEXT's fifth run starts only on that zero.

**x1dry is held, verified, and ready.** It is the dry exercise of st32's rollback library step -- the
one step in the whole chain with no run behind it. Its own order forbids running it while the fifth
run is between submission and close.

**Nothing else is owed.** Twelve orders terminal, one held.

---

## st32: the control that inverted

On st30 and st31 the correct result was an **unchanged** host library, because the package's copy was
byte-equal and the installer's library step rewrote the same bytes. On st32 the correct result is the
opposite: an unchanged library would have been the finding. Measured both sides -- the installer's own
`before:` line reads `library=857d90b81960d69a`, V1 reads `host library a1c2880169c5f799... =
bindings = want`. Independent corroboration that does not go through the digest I read: the factory
came up OK, and it refuses `PINNED_FILE_DIFFERS:library` unless the host file is the one the bindings
pin. The wrapper did not move.

**Three GO citations, not two**, because the CTO half carries a condition whose satisfaction is its
own file. All verified at the bytes. I did not rely on the packet's trailing `CTO HALF (owed)` line --
third release running that the trailer is stale; it fails safe, so it stays a control and not a row.

**The packet declares TWO P1 STOPs and the order requires THREE.** The third is the CTO's condition 1
folded into P1. I read `pre_read.sh` for all three before sending it, because discovering a missing
STOP afterwards would have burned the one pre-read.

**STOP-READ-3 guards a real gap, and I read the gap rather than assuming the STOP was ceremonial.**
The installer keeps the old library with a bare `cp -p` at line 79 under `set -uo pipefail` with no
`-e`. An already-present file at that path would be silently overwritten, destroying the true st31
copy -- the only rollback source for a step that has never run -- and nothing later in the script
re-checks it. P1 proved the path absent; V1 proved the copy landed at st31's digest. That is why the
condition exists, and it is the pattern worth keeping: a STOP whose purpose is invisible until you
read the line it protects.

---

## The control of mine that did not discriminate

For the NO SIGN-IN zero -- the claim the whole release hangs on, with the vendor session failing and
the order forbidding any sign-in -- my first instinct was to sweep the session tokens over V1's own
saved file. It returned 4, then 1, and for a moment that looked like a finding.

It was not. Those four lines were V1's own **label text**: `V1 capture pins`, `V1 host_capture
sha256`, and the NO SIGN-IN line whose label literally contains the words "a capture, an eviction or
a session refresh". A file-level grep cannot distinguish a journal line from a label naming the same
words, so it was simply the wrong instrument -- over-matching in the direction that manufactures
alarm rather than hides it, which is the safer direction but still useless.

The sound reading is the script's own journalctl-scoped count (0), compared against P1's pre-install
baseline of the same measure (also 0), with a positive control showing the token set matches real
journal content (5 against the j1 run-4 record). I recorded the failed control in the proof instance
by name rather than quietly replacing it, because a reader deserves to know which instrument the
zero actually rests on.

---

## j4: an urgent read with a trap in the window

The order's named trap is the one that matters: a count taken over a window that **starts after the
unit's own start** would make a capture in the gap invisible -- and this baseline is what authorises a
first sign-in, so a false zero is the costly direction. The window is therefore the unit's own
`ActiveEnterTimestamp`, printed so a reader can re-derive it, and it equals what st32's V1 printed.
`RESTARTS=0` closes the remaining question: there is no earlier start this window would miss.

A second hazard sits behind it. systemd prints the stamp as `Sun 2026-10-11 16:09:55 UTC`, which
`journalctl --since` does not take verbatim, so it must be normalised -- and a silently failed
normalisation hands journalctl an empty `--since`. So the `SIGNIN_LINES` line lives in the **else**
branch of that conversion check: on failure the script prints `SIGNIN_WINDOW_UNRESOLVED` and no
count at all, which drives AC2's presence test to 0 and **refuses** rather than reporting a number
over the wrong span. Building the criterion so that a broken instrument fails it is better than
building one that a broken instrument can satisfy.

Sent within a minute of the read, as the urgency required.

---

## x1dry: the hold, and why I did not reason my way past it

The order says it must not run while TCKT_VNEXT's fifth run is between submission and close. My j4
baseline is precisely what authorises that run, delivered four minutes before the order arrived.

I took the order's own step-1 gate read: the generation queue read **0 visible / 0 in flight / 0
delayed**. The tempting inference was that 0/0/0 means nothing is in flight, so the run must be
closed, so I may proceed. That inference is wrong in a specific way: **an unsubmitted run and a
closed run read identically.** Given that the baseline had just gone out, unsubmitted was the likelier
of the two, and no read my bounds allow can tell them apart. So I declined to infer it, parked the
order with its owner and the un-parking condition, and asked for one line.

**Then the world settled it.** At ~17:28Z the same queue read **0 visible / 1 in flight / 0
delayed** -- a message being worked right now. The fifth run is live on the host. Had I read 0/0/0 as
"closed" half an hour earlier, I would have been running a host script during another seat's live run,
which is exactly what the order forbids. That is a corroboration of the hold rather than a new ask, so
it is recorded here instead of sent to the issuer's inbox (rule 31: FYIs and corroborations go to the
record).

Done while held, with no host contact: the order blob verified (`8979fe1329` @`049834ad31`), and the
script checked against its own preflight claim -- `H` has exactly **one** assignment and it is
`mktemp -d`, every write targets `$H/...`, `$REAL` appears only as a `cp` source, `systemctl` is
`is-active`/`show` only. So the temp-dir discipline holds: `H` cannot point at the real directory, and
`rm -rf $H` cannot reach it.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` / `close-leg` x4 / `close --slug irpt-resident-st32-20261011` | PASS | 4 legs; opened BEFORE the first put, closed 20261011T161306Z |
| `proof-of-spec-check.py` | st32 and j4 instances | PASS (rc=0) both, FIRST pass each | st32 3/3 + 14/14 controls; j4 3/3 + 6/6; 0 DID-NOT-DISCRIMINATE either |
| `comp-schedule` / `comp-iam` | not run | DECLARED-NOT-APPLICABLE on all three orders | re-checked against each act as executed; every grant exercised was proved by a LIVE call |
| `comp-adversary` | the orders' named traps, graded as controls | PASS | st32's three-STOP reconciliation; j4's window trap; x1dry's `H`-from-mktemp claim verified without running it |
| `to-pipeline-gate` / `surprise-row-gate` | at commit | PASS | both complete-flips graded; no new rows this window |

**What worked.** Reading the issuer's script for the thing the order depends on *before* sending it --
on st32 that was all three STOP emissions, on x1dry it was the single `H` assignment. Both are cheap
and both would have been expensive to discover afterwards.

**What failed.** Two things, both mine. The NO SIGN-IN file-level grep above. And the x1dry park
message was refused by the broker at 163 words against the 150 cap -- correctly; I cut it to the one
ask rather than reaching for `send_override`, which exists for a human operator's request and not for
my own verbosity.

**Gap found.** None new. The `output_evidence` catch-22 recurred on st32's AC1 and j4's AC2/AC3 and
was handled as before (the count on its own line inside a transcript block, which satisfies both the
`^N$` match under `re.M` and the thin-evidence floor). Row `D2-S41` already carries the class.

---

## MCP traffic

6 in the window. Received and acked: msg 5278 (st32 order), 5382 (j4, URGENT), 5392 (x1dry, with its
hold). Sent: st32 V1-closed to the issuer (1146 B) and the after-the-fact host-send report to
`0.0.0_AB_MSTR~DELL2` (1058 B, required by st32 and not by j4 or x1dry); j4's baseline with all seven
lines (1097 B); the x1dry park-and-ask (970 B, after the 163-word refusal). All byte-verified. Three
`[WATCHER-EXPIRED]` notices, each re-armed the same turn; one watcher-row census confirmed exactly
one live stream rather than stacked ones.

One provenance note worth keeping: **j4's and x1dry's order FILES were both in this lane's folder
before their dispatch messages arrived**, having ridden the issuer's own commits through box-sync. I
did not act on either until its dispatch landed and was acked, because for a Tier-2 seat the dispatch
is the authorisation and not the presence of a file.

---

## Blockers

**ONE, and it is a condition owned elsewhere, not a seat that is late.**
`IRPT_YCDGEN.TO-APPLY-x1dry` is HELD by its own order while TCKT_VNEXT's fifth run is between
submission and close. Measured evidence the hold is live: the generation queue read 0 visible / **1 in
flight** at ~17:28Z. **Un-parked by:** one line from `2.0.0_SA_COO~G2` that the run has closed, asked
for at 16:58Z. I run it the same turn.

Owned elsewhere and named so nothing is stranded: `D2-S56`, `D2-S53`, `D2-S51` with
`2.0.0_SA_COO~G2`; `D2-S52` with `1.0.0_SA_CTO` by R-19; `D2-S45` still ARMED and untouched by any of
this window's three orders.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~YC2]` On the issuer's close line: run x1dry -- queue gate, `host_read.py
   dry_exercise_rollback_library.sh`, expect `X1 DRY RESULT: PASS`, `X2 NEGATIVE CONTROL: PASS`, `X3
   temp dir removed: yes`, the real library unchanged at st32's digest and the restart count
   unchanged. Any FAIL line, a changed library hash or a changed restart count: STOP and report as is.
2. `[2.0.0_SA_COO~G2]` That one line. It is the only thing between this seat and the last open order.
3. `[1.0.0_SA_CTO~DELL2 / 2.0.0_SA_COO~V2]` st32's CTO condition 2, which is not this seat's: the
   first receipt after the fifth run is read for what it must NOT hold -- a posted value, a cookie, a
   tokenised URL -- before any part of it is quoted in a record or a message.
4. `[2.0.0_SA_COO~G2]` After the fifth run: st32's D1 and D2 and st31's D1 all have their first real
   exercise available, and `D2-S51`'s question about which READY S5 instruments becomes answerable
   from a run that actually reaches READY.
