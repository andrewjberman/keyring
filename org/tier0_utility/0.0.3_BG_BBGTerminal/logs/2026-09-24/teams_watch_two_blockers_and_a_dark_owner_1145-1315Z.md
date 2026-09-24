# `0.0.3_BG_BBGTerminal` -- 2026-09-24 11:45Z-13:15Z -- THE TEAMS WATCH: TWO BLOCKERS, AND THE OWNER IS DARK

Successor record for this seat's PRIMARY STANDING DUTY. Supersedes nothing in
`leadpanel_price_producer_0932-1045Z.md` (that log is the mandate; this one is Teams).
⛔ **The thread-memory file `threads/2026-08-07-andrew-capability-roster/2026-09-24.md` names
`0.5.0_AE_OpalETL~Z` as the engine owner. THAT ROUTE IS DEAD -- see section 4.**

## 1. THE WATCH IS BLIND FOR **TWO INDEPENDENT** REASONS, AND ONLY ONE IS THE CREDENTIAL

| | state | evidence |
|---|---|---|
| **(1) token expired most of the time** | **CONFIRMED** | below |
| **(2) reads fail even when it is NOT expired** | **MEASURED, cause UNKNOWN** | below |

⛔ **FIXING (1) ALONE YIELDS A WATCH THAT AUTHENTICATES AND DELIVERS NOTHING.** Do not let a credential
remedy close this.

## 2. BLOCKER (1) -- CONFIRMED, and the mechanism is a COUPLING

A gateway MCP call mints a **15-minute** token **only when the current one is EXPIRED**; nothing else
writes `~/.claude/.credentials.json`.

- **Negative arm** (no autonomous refresh): mtime unmoved across **two separate expiry episodes -- 29 min
  and 9 min** -- with no gateway call. The 29-minute one was measured at 12:37:02Z, *before this test was
  conceived*, so it was not selected for.
- **Positive arm** (mint on demand): 12:37:02Z expired -> ONE call -> 12:38:14Z fresh, mint 12:37:21Z.
  Repeated at 13:06:38Z. **TTL 15 min exact, four observations.**

⭐ **SO THE WATCHER'S SIGHT IS COUPLED TO THIS SEAT'S OWN MCP ACTIVITY** -- it sees for 15 minutes after a
gateway call, i.e. while the seat is already awake, and goes blind once it idles. **A monitor that works
only while you are already watching is not a monitor.**

WARN: **CONFIRMED IS NOT "NEVER".** A refresher on a cadence longer than 29 minutes would look identical.

## 3. BLOCKER (2) -- THE ONE I ALMOST MISSED, AND THE WAY I ALMOST MISSED IT

At 13:06:38Z the token was minted and live to 13:21:38Z. The newly-armed watch printed
`token selected: identity=...6810043e.../517aa5ee...` -- and then, over ~70 s:

```
35 output lines = 1 arm banner + 1 token-selected + 33 "read failed ... cursor HELD, retry next cycle"
ZERO successful reads, ZERO emits, all FOUR chats, EVERY cycle, token LIVE throughout
```

⛔ **SO READS FAIL INDEPENDENTLY OF TOKEN FRESHNESS.** The 12:37Z warm window showed the SAME all-four
failures. **THE WATCH HAS NOT SUCCESSFULLY READ ANYTHING TODAY, WARM OR COLD.**

⛔ **HOW I ALMOST MISSED IT, because it is the reusable part:** I found a real mechanism (expiry) and let
it explain EVERY symptom instead of checking WHICH symptoms it covered. Expiry explains the cold windows
and never explained the warm ones -- **and the contradicting `read failed` lines were in output I had
already read and quoted.** Sixth correction on that thread; they all share this shape.

**HYPOTHESIS, NOT A FINDING** (recorded so a successor starts somewhere, not so it is believed):
`teams-watch.py` reads an `mcpOAuth` record whose `serverUrl` is `mcp.opalinvest.dev` and may present that
**MCP-gateway** token directly to `graph.microsoft.com` -- wrong audience, would fail 100% regardless of
freshness, and is consistent with the `read_chat_messages` Graph 500s AND with the MCP poller working
(it authenticates server-side on its own credential).
WARN: **It is NOT consistent with the watch having worked historically** -- thread memory records real
deliveries on 08-20 and 09-11 -- so either something changed or the hypothesis is wrong. **Untested.**

## 4. THE ENGINE OWNER NAMED IN `TEAMS_DUTY.md` IS DARK -- DO NOT ROUTE THERE AND STOP

`0.5.0_AE_OpalETL~Z`, measured by `0.0.0_AB_MSTR~Z` at 13:1xZ on three instruments: broker **NOT
REGISTERED**; newest commit under that author **2026-09-10** (base-serial control fires, so the query
discriminates); its inbox's newest file **2026-09-11**, and it holds **0 of 2** copies of the findings.

⛔ **THIRTEEN DAYS DARK. NAMING IT AS OWNER IS A PARKING, NOT A DELIVERY** -- CLAUDE.md's *"Queued if not
live is a WISH"*, and this seat did it repeatedly today in messages to other seats. The findings are held
by `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` (2 of 2). **Routing -- task order to a live AE lane, card to
Andrew, or moot -- is `1.0.0_SA_CTO~Z`'s call under R-66's pre-commitment.** Not this seat's.

## 5. THE ACTUAL HARM IS NEITHER BLOCKER

**Andrew's `2026-09-23T19:40:01.767Z` message is unread at ~17.5 h.** It is a `oneOnOne` the poller DID
return (so the channel-coverage limit does not reach it), its `body.content` is `""` with
`isDeleted:false`/`eventDetail:null`, and `read_chat_messages` on that chat returns **Graph 500** twice.

⛔ **THE BLOCKER IS A MISSING CAPABILITY, NOT A STATE: no tool on this gateway fetches `hostedContents`.**
Neither a warm token, nor a keep-alive, nor a channel read reaches it. **Five messages from this seat
today were about the credential; none moved this message.** Two routes out: a `hostedContents` GET added
to the gateway, or Andrew re-sending as text -- the latter is a **draft-and-ask**, never an auto-send.

**ACK-FIRST IS OWED AND UNDISCHARGED.** `0.0.0_AB_MSTR~Z` surfaced the finding to Andrew as an operator
act; that is a different duty and does not discharge this one.

## 6. REACHABILITY POSTURE FOR A SUCCESSOR

**NOT event-driven on Teams.** Re-arm the watch (it self-heals the instant reads work), but **do not treat
an armed watch as coverage** -- verify the `token selected` line AND a successful read before believing
it. Reachability today is a **manual `poll_addressed_teams_messages` per turn**; last run 13:06Z over the
full window since `2026-09-23T20:08:35Z` returns **count 0**, so nothing has arrived while blind.

⭐ **The engine HOLDS ITS CURSOR per-chat on every failed read** (`cursor HELD, retry next cycle`), so all
of this **delays** mail and does not **lose** it. That is the design working and is worth saying beside
the defect.
