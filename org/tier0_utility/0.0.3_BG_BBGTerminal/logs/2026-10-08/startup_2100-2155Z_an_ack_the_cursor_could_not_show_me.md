# Startup 21:00-21:55Z: the owed item the monitor could never have emitted

**archetype:** MIXED

**Window:** 2026-10-08 21:00Z - 21:55Z | **Seat:** 0.0.3_BG_BBGTerminal
**Trigger:** launch prompt -- `/watcher`, then `org/XXX.md`.

## Current State

Startup complete on every named step. Both watchers armed, 1 row each, no stacking.
DAPI UP (entitled session, `dapi_check` exit 0). Daily pipeline closed green earlier today
(`data_as_of 2026-10-07`, correct T-1). **ONE OWED ITEM FOUND AND NOT YET DISCHARGED:** a
substantive Teams reply to Andrew, drafted, held at draft-and-ask on his word.

## 1. THE FINDING: an ack whose own cursor made it invisible

A prior session acked Andrew's three forwards at **20:19:15.796Z** and ended without the
substantive reply and without any 2026-10-08 thread daily.

>> **The Teams cursor had advanced to EXACTLY that ack's timestamp.** So the monitor had
nothing to re-emit, `check-inbox` was empty, delivery state read 40/40 READ, and
`get_agent_status` showed no pending task orders. **Every delivery-shaped instrument said
clear.** The item was owed by a promise, and no transport instrument tracks promises.

It surfaced from RECALL alone: TEAMS_DUTY requires comparing the armed `cursor=` against the
newest thread daily. Cursor 10-08T20:19Z vs newest daily 10-07. The documented hazard is a
cursor BEHIND the record (replay). This was the inverse -- a cursor AHEAD of the record --
and the right question was not "what will replay" but **"why did a day the cursor crossed
leave no record behind?"**

**The rule earned its keep in the direction it was not written for.** TEAMS_DUTY's check is
framed entirely around the backward case; the forward case is the one that bit, and the same
comparison catches both. Worth stating where the ref can be amended by its owner.

## 2. The three forwards, and the one point that changes the ask

Author is **Alyssa Keith** (`ad037ea5-...`), forwarded by Andrew with no cover note: a write-up
that the gateway's Schwab channel cannot do the Tax SMA quarterly job, plus two screenshots,
the second written explicitly "as a list you could hand to Andrew for the gateway".

**Her own first screenshot says: "Your access profile is per user, so other people at Opal may
see more."** That makes every red X in her needs table a fact about HER PROFILE, not the estate.

>> For master 0840-3355 that is two different asks at very different cost: an ENTITLEMENT GRANT
if the Tax SMA master is already in the Schwab feed, or a PIPELINE BUILD if it was never
ingested. Her evidence -- "I searched both masters for Chiles's exact 9/30 value and got no
match" -- tests only the two masters her profile exposes and **cannot distinguish them.** The
denominator is her access profile; the sentence beside it reads as an estate fact. Same class
as the banked lesson "a TRUE number carried into a population it never measured".

Cost basis, realized gain/loss and 13-month retention read as real absences either way: they
are missing COLUMNS and a 30-day retention limit, not a missing master.

## 3. Capability exercised, not recalled (2026-10-08 ~21:25Z)

| call | result |
|---|---|
| `opal_discover` | `identity_scope_denied` |
| `opal_describe` | `identity_scope_denied` |
| `blackdiamond_list_fees` (49financial) | `identity_scope_denied` |
| `schwab_*` | no such tool on this surface |

3 of 3 denied, identical code, "widening is an Andrew ruling". **Stopped at three:** a fourth
denial would not have changed the act (CLAUDE.md section 2).
So this seat can neither confirm nor contradict her table, and says so rather than inferring.

## 4. THE IDENTITY PIN HELD ACROSS A TOKEN LAPSE -- measured, not assumed

Read from the expired monitor's own output, which is the only place the banner lands:

```
armed interval=15s cursor=2026-10-08T20:19:15.796Z pin(server=opal-gateway-bbg, identity=517aa5ee-...)
pinned token expired -- quiet retry, pin HELD (cycle 1)
re-selected after lapse: identity=6810043e-.../517aa5ee-...
```

The re-selection took **Opal Bloomberg's** oid, not Andrew's `2e21f8e5-...`. That is CRO~Z's
fourth defect (the unpinned watcher grabbing the freshest token regardless of identity)
exercised against the live failure mode -- a token lapse -- and surviving it. The banner's
`cursor=` also matched the value read independently from the cursor file beforehand, so the
two instruments agreed.

The two "pinned token expired" lines are blocker (1), the 15-minute issuer TTL with
mint-on-expired-only. Known, gateway-owned, not this seat's.

## 5. Two process notes

**5a. P1 verified by CONTENT, not ancestry.** RELAUNCH P1 says check the engine commit is
`0f1bbcf0e` or a descendant. `merge-base --is-ancestor` passed, but CLAUDE.md 22a says a pin
is resolved by CONTENT. Enumerated the engine on disk instead: `PIN_SERVER`/`PIN_IDENTITY`
parsed at :176-177, `_pin_fail("no-token-for-identity")` at :241, no fallback path. The flag
about to be relied on is actually present in the bytes that will run.

**5b. The exit bound was missing and the hook caught it.** The Teams watch was armed bare.
`teams-watch.py` never exits, so the harness's 30-minute kill would have reaped the wrapper
and orphaned the python child every cycle. Stopped it, confirmed 0 leaked rows, re-armed under
`timeout 1770 bash -c`. Exit 124 at expiry is that bound firing, not a fault. RELAUNCH's
"ZERO scratchpad scaffolding" bars a wrapper SCRIPT; it does not bar an exit bound.

## 6. Registration dropped mid-session

`heartbeat` returned "not registered" ~25 min after a successful `register_agent`.
Re-registered, same PID 13824. `org/mcp/liveness.json.corrupt` is present in the tree
(untracked). Surfaced, not chased -- not this seat's lane.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `comp-read --for` | TEAMS_DUTY arm-banner contract; READ_HERE cma question | both answered; UNREAD LEDGER made the skip explicit |
| `comp-read --enumerate` | content-verify the identity pin in the engine on disk | 17 hits, 8 whole; `PIN_IDENTITY` + `no-token-for-identity` confirmed in CODE band |
| `comp-find --files` | locate `teams-watch.py`, `RELAUNCH.md` | engine found; RELAUNCH HEAD band was all inbox copies, resolved by direct `ls` |
| `comp-find --band` | `cma` interpreter path | CONFIG band = MEASURED ZERO; SURFACED band held it (`C:\Anaconda\envs\cma\python.exe`) |
| `dapi_check.py` under cma | startup step 4 | DAPI UP, exit 0, blpapi 3.26.4.2 + tia |
| `get_delivery_state` | launch ledger | 40/40 READ; 2 in-session arrivals acked by id |

**What failed / gaps:**
1. **A CONFIG-band zero is not an absence.** `comp-find --band CONFIG "cma"` returned a
   measured zero over 98 files while 60 SURFACED hits held the answer. The band filter was
   the wrong domain for the question, and the zero was printed with a real denominator --
   exactly the shape that reads as "not there".
2. **Two Bash calls aborted whole** on the comp-rail (a `find`, and a `comp-read` piped to
   `head`). A rail denial kills every later segment, so a gated read belongs in its own call.
3. **A heredoc carrying this log's own text failed to parse** (backslashes + fenced block).
   Written with the Write tool instead -- the same non-shell-writer rule CLAUDE.md 14a sets
   for commit messages applies to any content-bearing file.
4. `cma` is not on PATH under any name; it resolves only as an absolute path. The startup
   instruction names it as if it were a command.
5. Bloomberg draw this session: `dapi_check`'s own SPX Index/PX_LAST probe, 1 security x
   1 field, recorded rather than argued away -- same handling as the predecessor's
   post-sign-in confirmation call.

## Owed

- **Teams reply to Andrew: DRAFTED, NOT SENT.** Draft-and-ask per this thread's 10-07 record;
  3 sentences per his standing <=2-3 rule (first cut ran ~190 words and was cut).
- **Open call put to Andrew in session:** re-wire the concierge fence or leave it unwired
  (LD-0580; CTO ruled 2026-10-08 that re-wiring needs his new word). `prompt.md` still
  describes the fence as live, which is now a stale carrier.
- Alyssa's four questions are Andrew's, not this seat's. Still carried from 10-07: the
  "more details" he promised her on 09-30.

## 7. ADDENDUM 22:3x-22:4xZ -- "APPLIED" covered the addition, not the isolation

`0.0.0_AB_MSTR~Z` msg 32078 reported the opal-gateway-bbg one-session move APPLIED, citing:
"user-level ~/.claude.json lists only bloomberg, brightdata and opalgateway, with no
opal-gateway-bbg".

>> **That one sentence carries two facts and only one was read.** It proves the bbg server
arrives via `--mcp-config` (the claim made). It equally proves `opalgateway` IS still in the
user-level config and therefore still loads here (the claim not made). `--mcp-config` is
ADDITIVE, so `.tools/bg-gateway.mcp.json` declaring ONLY opal-gateway-bbg does not exclude
anything.

**Measured inside the session:** both `mcp__opal-gateway-bbg__*` and `mcp__opalgateway__*` are
on this seat's tool surface. The sibling was NOT called to establish this -- presence is
observable without invocation, and calling it is the thing prompt.md forbids.

`0.0.0_AB_MSTR~Z` msg 32085 confirms and narrows: the prepared plan took bbg off every OTHER
session (applied); keeping opalgateway OFF the BG seat "was never in that plan", and
`--strict-mcp-config` is the named mechanism.

**Consequence:** the proxy-identity server that would let this seat read Andrew's private DMs
and reply to colleagues AS Andrew is reachable, and the fence that used to deny every non-bbg
`opal-gateway` call is unwired (LD-0580). Discipline is the only barrier. Andrew's call; put to
him in session and by MSTR at the site-Z terminal.

**The general shape, worth carrying:** a measurement taken to confirm X also settles Y, and Y
goes unread because nobody was asking it. The tell is a sentence whose evidence enumerates a
set -- here, three server names -- where the ABSENCE of one was the point and the PRESENCE of
another was equally stated.
