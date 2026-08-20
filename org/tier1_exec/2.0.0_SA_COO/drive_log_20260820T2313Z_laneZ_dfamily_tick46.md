# /drive tick 46 — 2.0.0_SA_COO~Z lane Z — 23:09Z→23:17Z

**Cycle result: caught my OWN carry-forward naming the wrong constraint for several ticks — and the
drive imperative was pushing me at the act that would have spent a working seat on a lane that
cannot start for two more links.**

## Movement

| seat | since_tick | age | verdict |
|---|---|---|---|
| `0.0.0_AB_MSTR~Z` | 7 | 0.8m | ADVANCING |
| `0.0.3_BG_BBGTerminal` | 8 | 0.2m | ADVANCING (re-opened for the boundary test) |
| `0.4.0_DT_ClientPlatform~Z` | **0** | 7.2m | **CLOSED-BY-DECLARATION, not PARKED** — 0 TOs, nothing held, nothing armed, by their own close |
| `0.5.0_AE_OpalETL~Z` | 10 | 0.1m | ADVANCING |
| `1.0.0_SA_CTO~Z` | 8 | 0.1m | ADVANCING |
| `2.0.0_SA_COO~Z` | 9 | 0.7m | self |
| `3.0.0_SA_CVO~Z` | 10 | 0.3m | ADVANCING |

Denominator: 23,367 telemetry rows. **No nudge ladder opened** — DT~Z's zero is a declared close over
a 4.5-minute window, not a stall.

## The finding: my own carry-forward named the wrong constraint

For several ticks I have carried **"W-C capacity-blocked behind the 6-seat ceiling."** That names the
wrong gate, and the error is not cosmetic — **it implies freeing a seat would unblock the lane.**

**MEASURED 23:15Z, from the TOs themselves:**

| link | state |
|---|---|
| W-C half (b) | staged **behind W-A** (shared Lambda file, CTO~Z-sequenced) |
| W-A | **`<status>pending</status>`** — GO rides a commit's MCP, **queued behind dep-3 registration** |
| dep-3 | CTO~Z @942d4d885c: *"the current dep-2/dep-3 chain is UNCHANGED and remains the critical path"* |

>> **W-C IS TWO LINKS BACK: `dep-3 → W-A → W-C(b)`. Capacity is a THIRD constraint that does not bind
until the first two release.**

**The TO's own text already said it** — *"this half is staged behind W-A regardless"* — sitting
directly beside the capacity paragraph. **The capacity paragraph is the one that got carried forward,
because it is the one that sounds actionable.**

## ⛔ And the drive imperative pushed me at the wrong act

*"Resolve gates, don't attest them"* + a drained seat (`0.4.0_DT_ClientPlatform~Z` closed with 0 TOs)
+ MSTR~Z's *"naming the seat to release is COO~Z's allocation call"* reads as: **make the allocation
call now.** I was one step from it.

>> **THAT WOULD HAVE RELEASED A WORKING SEAT FOR A LANE THAT CANNOT START FOR TWO MORE LINKS.**
**A gate that is real but NOT THE BINDING ONE still refuses to open, and the effort spent opening it
is spent.** The skill's anti-coast pressure is correct and it is *directional* — it says *act*, not
*act on this*. Choosing which gate is still the COO's job.

**The allocation call is unchanged and remains mine.** MSTR~Z's swap path stands; the naming is still
the first act **when W-C goes hot.** What is corrected is **when "hot" arrives: not when a seat
frees, but when W-A lands.**

## Second correction in the same paragraph — LAPSED, not never-spawned

The TO says `0.4.0_DE_ClientPlatform~Z` *"HAS NEVER REGISTERED THIS SESSION"* — true of
`liveness.json`, and it **reads as "this serial has never existed."**

**MEASURED:** its telemetry file carries **289 rows**, last work-call **2026-08-20T16:18:43Z — ~6.9
hours ago.** **It is a LAPSED seat, not a never-spawned serial.** That matters to whoever seats it: a
lapsed seat may carry in-flight state, partial work, or a handoff a fresh spawn would not inherit.

⚠ **AND IT EXPOSES AN INSTRUMENT TRAP: THE TELEMETRY FILE'S EXISTENCE IS NOT A LIVENESS SIGNAL.**
DE~Z has a file; it is 6.9h stale. **An age filter is the only thing separating them** — a census
keyed on file-presence alone reads this seat as live. *(My own scan filtered by age and correctly
showed 7 seats, not 8. The trap was one careless query away.)*

## The credential boundary — clean pass, test still running

- 23:14:46Z pass: `exit 0` with ~70s of token remaining — correct
- 23:15:55Z: expiry
- 23:16:0xZ: `0.0.3_BG_BBGTerminal` called on an **expired** record → **SUCCESS, 200, full payload**,
  one call, no retry, no 401

✅ **RESOLVED 23:17Z — LAZY RE-MINT CONFIRMED ON BOTH ARMS.**

**DEAD-TOKEN ARM** (`0.5.0_AE_OpalETL~Z` @3763, after-read at 23:16:31Z, inside the window):

| | time | `expiresAt` | state |
|---|---|---|---|
| BEFORE | 23:15:35Z | `2026-08-20T23:15:55Z` | LIVE, 0.3 min — **anchored 4×** (23:05:06, 23:07:43, 23:08:09, 23:15:35) |
| BOUNDARY | 23:15:55Z | — | — |
| AFTER | 23:16:31Z | `2026-08-21T00:16:13Z` | LIVE, 59.7 min |

>> **The credential refreshed — expiry moved forward 60m18s.** And **the mint time is recoverable
from the value:** `00:16:13 − 60:00` puts the re-mint at **23:16:13Z — eighteen seconds after
expiry**, the same construction as both earlier refreshes (call-time + exactly 60:00).

**LIVE-TOKEN ARM — and this is the finding, from an instrument nobody thought to count**
(`1.0.0_SA_CTO~Z` @3756): the monitor has polled every 15 seconds for 2h05m — **roughly 464 gateway
calls on a LIVE token — and the token expired on schedule anyway.**

>> ⛔ **THE LIVE-TOKEN HALF NO LONGER RESTS ON ONE NEGATIVE; IT RESTS ON ~464.** And it reframes the
observation that started all of this: **BG's 23:02Z call was never a puzzling anomaly — it was ONE OF
HUNDREDS.** *A lone confusing negative turned out to be typical the moment somebody enumerated the
population it came from.* That is the denominator lesson in its purest form, and the population was
running all evening in plain sight.

**Channel still at 2 posts — no client ticket, so A1 is unsatisfied and the test is CLEAN rather than
superseded.**

## Coverage — checked and found SOUND

- 7 seats present, all within 8 minutes; the 8th telemetry file is a 6.9h-lapsed serial, correctly
  excluded by the age filter
- Intake: `exit 0` through the boundary, `PT5M`, no unexpected refusal
- No new blocked state; no deploy-ledger change since tick 44's read

## Carry-forward — with the constraint stated correctly this time

- **W-C: SEQUENCE-blocked at `dep-3 → W-A`, NOT capacity-blocked.** Capacity binds only after W-A
  lands. My allocation call waits on that, not on a free seat.
- W-A: `pending`, behind dep-3 registration
- Item A (five `_meta` marks) build → both gateway changes ride one boot test
- W-B awaiting Andrew; W-D limb (2); W-E criteria (2)(3)
- A1 on the next real client ticket
- Credential: the runner cannot self-heal — only an agent call clears a refusal
