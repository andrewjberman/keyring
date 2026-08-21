# /drive tick 45 — 2.0.0_SA_COO~Z lane Z — 22:57Z→23:01Z

**Cycle result: went looking for a false green on the standing production exposure and found a
genuine control instead. The intake is a live credential canary firing every 5 minutes.**

## ⚠ The movement window this tick is 42 seconds — `since_tick` carries no signal

The tick fired 42s after the previous marker update, so counts of 1–2 are an artifact of the window,
not of the seats. **`0.0.3_BG_BBGTerminal` reading `since_tick=0` is NOT a PARKED signal** — their
last work-call is 8.6m old (well inside the 30m threshold) and they closed their seat deliberately
(*"Quiet until real traffic"*). **No nudge ladder opened, and opening one on this window would have
been a false conviction manufactured by my own cadence.**

Denominator: 23,180 telemetry rows. All seven seats within 9 minutes.

## The finding I almost filed — and why it was false

Every green pass reads `INTAKE PASS OK -- fetched=0 buzzed=0 …`. Census over the runner log:
**37 passes, 2 with `fetched>0`, 1 with `buzzed>0`.** So 34 of 37 greens sent nothing.

**The alarming version was drafted:** *"exit 0 on a zero-traffic pass never invokes the send leg, so
it cannot distinguish a live token from an unexercised one — an instrument that could not have said
otherwise, sitting on the standing production exposure."*

**IT IS FALSE.** `runner.py:187` — `send = gateway_send_factory(cfg)` is called **unconditionally**
in `main()`, **before** `run_once`. And `tok = tw.read_token()` sits at `:107` **in the factory
body**, not inside the returned `send` closure.

>> ✅ **THE CREDENTIAL IS READ AT CONSTRUCTION, EVERY PASS, REGARDLESS OF TRAFFIC.**

⛔ **CORRECTED 23:04Z — I GRADED THIS ONE LAYER TOO STRONG. IT IS `APPLIED`, NOT `EXERCISED`.**
*(`0.5.0_AE_OpalETL~Z` @3632, checked at source in their own code rather than agreeing with me.)*
`read_token()` → `_read_pinned_token()` (`teams-watch.py:158-197`) **is a PURE FILE READ** — scanned
for `urlopen` / `requests.` / `http.client` / `socket` / `_gateway_call`: **none**. It opens the
credentials JSON, filters by pin, decodes the JWT **locally**, and the entire liveness test is:

```python
live = [r for r in recs if r.get("expiresAt", 0) / 1000 > time.time()]
```

>> **THAT IS THE TOKEN'S OWN CLAIM ABOUT ITSELF, AGAINST THIS BOX'S CLOCK. Nothing asks the gateway
anything.** `exit 0` proves the record **exists**, **matches the pin uniquely**, and **is not locally
expired**. **It does not prove the gateway would accept it.** Passing-while-dead: a revoked token, a
rotated gateway secret, a server-side session invalidation, clock skew.

⛔ **AND MY OWN DENOMINATOR MADE IT CONCRETE — I HAD THE NUMBER IN HAND AND DREW THE WRONG GRADE
FROM IT:** of the 37 passes I counted, the **one** with `buzzed>0` is the **only** pass that ever put
the credential on the wire. **1 exercised, 36 file reads.**

✅ **THE EAGER-vs-LAZY FINDING STANDS** and the design credit is deserved — AE~Z declined to soften
that half. What was wrong was **one word**, and it is the word that decides whether a future reader
believes **the wire is covered.** It is not.

*So the 22:54:46Z pass verifies the token was present, pinned, and unexpired-by-its-own-clock as of
four minutes prior — on a pass that sent nothing.*

**CORROBORATED INDEPENDENTLY BY THE LOG'S SHAPE**, which is the part worth keeping: the three exit-2
refusals print `REFUSED (exit 2): pinned gateway token expired` with **no `INTAKE PASS OK` line and
no `fetched=` count at all** — the refusal precedes every summary. *Source says eager; log shape says
eager. Two independent lines, and I would not have trusted the source read alone.*

## Why the design choice is load-bearing and under-credited

**EAGER-AT-CONSTRUCTION vs LAZY-AT-FIRST-SEND is the difference between a canary and a landmine.**
Lazy would let a dead credential sit undetected through every quiet hour and surface on the **first
real client ticket** — exactly the A1 moment the fabric is waiting on, and the worst possible time to
discover it. Eager catches it within 5 minutes at zero traffic.

*The fabric spent tonight naming instruments that pass because nothing exercised them. This one
exercises itself on purpose.*

## The exposure that remains, stated precisely

**DETECTION IS SOLVED FOR THE EXPIRY CLASS ONLY. REPAIR IS NOT SOLVED AT ALL.**

⛔ **A REVOKED-BUT-UNEXPIRED CREDENTIAL IS DETECTED BY NOTHING HERE**, and it presents differently
from the story everyone has been telling: **a GREEN pass, then a send failure on the first real
client ticket — `exit 3`, NOT `exit 2`.** Different code, different story, and it lands at the A1
moment. *(In fairness: expiry IS the dominant failure mode on a ~1h TTL, and an applied-grade check
aimed at the actual failure mode is a good control.)* The token expires roughly hourly and its refresh needs a live
agent MCP call — the runner cannot refresh what it can only observe. The standing exposure is not
*"we might not notice"*; it is **"we notice within 5 minutes and can do nothing unless a seat is
awake."** The detect/deliver seam again — and this time **detection is the half that works.**

**TIMING — arithmetic, not measurement:** hand-restored ~22:15Z against a ~1h TTL puts the third
refusal window near **23:15Z**. Named so nobody reads a 23:2xZ `exit 2` as a new defect; it is the
known exposure on schedule.

✅ **CONFIRMED BY MEASUREMENT 23:05:06Z** (`0.5.0_AE_OpalETL~Z` @3660, read from the pinned record;
denominator 4 mcpOAuth records, exactly 1 matching the pin; no token material read):
**`expiresAt = 2026-08-20T23:15:55Z`.** The arithmetic was right.

> ⛔⛔ **EVERYTHING IN THIS SUBSECTION IS SUPERSEDED — SEE THE 23:11Z ADDENDUM AT THE END OF THIS
> FILE. IT WAS MY SECOND POSITION AND IT WAS WRONG.** Kept in place because the retraction is part of
> the record, **marked here rather than only at the bottom** so a reader who stops mid-file cannot
> take it as current. *(That failure mode — a superseded claim left standing at the point of the
> claim, with the correction filed elsewhere — is the one I spent this evening flagging in other
> seats' records. Marking it in place is the same fix as putting W-B's prohibition at the top.)*

~~⛔ **AND IT FALSIFIED THE REFRESH MECHANISM THREE SEATS BELIEVED.** `0.0.3_BG_BBGTerminal` made a
gateway duty read at 23:02Z expecting it to extend the credential to ~00:02Z. **The expiry did not
move** — it is still the value the 22:16Z hand-restore set. **A PLAIN GATEWAY CALL DOES NOT REFRESH
THE CREDENTIAL.**~~ ← **FALSE AS STATED.** The 23:02Z measurement is correct; the *generalisation*
is not. A call against a **LIVE** token does nothing; a call against an **EXPIRED** one **re-mints**.

~~>> **THIS MAKES THE STRUCTURAL FINDING WORSE, NOT BETTER.** I told MSTR~Z the path was *"kept alive
three times by agents doing something else"* — which implies a staffed fabric is self-sustaining, and
that implication is unsupported.~~ ← **RETRACTED. THE ORIGINAL CARD LINE WAS RIGHT.** That *is* the
mechanism; I withdrew it prematurely and restored it at 23:11Z.

~~>> **THE PATH IS NOT KEPT ALIVE BY BEING STAFFED. IT IS KEPT ALIVE BY SOMEONE DELIBERATELY
RE-AUTHENTICATING IT.**~~ ← **FALSE.** The 22:16Z act was an **ordinary read**, not a deliberate
re-auth — `1.0.0_SA_CTO~Z` mislabelled it and I carried the mislabel. A staffed fabric **does** heal
it incidentally.

**OPERATIONAL:** intake fires ~:09:45 and ~:14:45 (both inside the window, both pass) and **~:19:45Z
— the refusal**, absent a re-auth. *Not an emergency and not manufactured as one:* a refusal is
recoverable, the next pass retries, the exit contract handles it as designed. **The only real cost is
a client ticket arriving inside the dark window — which is A1, which is exactly what is pending.**

## A census defect of my own, caught in passing

First count was `grep -c 'refused\|token expired'` → **37**, briefly read as *"every pass had a
refusal event."* **It matched the healthy lines** — every OK summary contains the substring
`refused=0`. Corrected with the uppercase token: **`REFUSED` = 3, `refused=0` = 35.**

>> **A SUBSTRING THAT APPEARS INSIDE ITS OWN NEGATION IS AN UNUSABLE SEARCH TERM** — and the number
it produced was *exactly the total*, which is the shape most likely to be mistaken for a real
finding.

## Coverage — checked and found SOUND

- All 7 seats within 9 minutes of a work-call; none stale, none blocked
- `OPAL_D7_ticket_intake`: `LastResult=0` at 22:54:46Z, `NextRunTime` 22:59:45Z, `PT5M` — healthy
- Gateway credential: **present, pinned, and unexpired-by-its-own-clock at 22:54:46Z — `APPLIED`
  grade, NOT exercised.** *(This line read "verified live … by exercise" and survived my first
  correction pass, which fixed two occurrences and missed this one — the **file-level vs
  per-occurrence** verifier defect I already hit earlier tonight, repeated by me, in the act of
  correcting an overstatement. Caught by a per-occurrence sweep: 6 hits, this the only stale one.)*
- No new commits in the window (42s — expected, not a finding)

## Carry-forward

- Item A (five `_meta` marks) build → both gateway changes ride one boot test
- W-A apply at the laptop; W-B awaiting Andrew; W-D limb (2); W-E criteria (2)(3)
- W-C capacity-blocked behind the 6-seat ceiling
- A1 on the next real client ticket
- Credential repair remains agent-dependent — the one part detection cannot cover


---

## Addendum 23:11Z — RESOLVED, and my correction was itself wrong. Third position, best grounded.

`0.5.0_AE_OpalETL~Z` @3685 found the column nobody was tracking: **TOKEN STATE AT CALL TIME.**

| time | act | token state at call | expiry after |
|---|---|---|---|
| ~21:06 | channel read | **at/past expiry** | **REFRESHED** → 22:06:05Z |
| 22:09 | **RUNNER pass** | EXPIRED | unchanged, `exit 2` |
| 22:14 | **RUNNER pass** | EXPIRED | unchanged, `exit 2` |
| 22:16 | gateway read | EXPIRED | **REFRESHED** → 23:15:55Z |
| 23:02 | channel read | **LIVE, ~14 min left** | **UNCHANGED** |

>> **EVERY REFRESH HAPPENED ON AN ALREADY-DEAD TOKEN. THE ONE CALL AGAINST A LIVE TOKEN DID
NOTHING.** The observations were never in conflict — they were being compared without the column that
separates them.

**CORROBORATED INDEPENDENTLY BY ARITHMETIC:** both refreshes landed on **call-time + exactly 60:00**
(`21:06:05 + 60:00 = 22:06:05`; `22:15:55 + 60:00 = 23:15:55`), to the second. Two independent
re-mints hitting the minute-and-second is a second line of evidence that those were re-mints and
23:02Z was not.

**SO THE MECHANISM IS LAZY REFRESH AT THE BOUNDARY:** an ordinary agent gateway call **re-mints an
EXPIRED token** and **does nothing to a LIVE one.**

### The original card line was right and I withdrew it prematurely

*"Kept alive by agents doing something else"* **is supported** — that is precisely the mechanism.
`1.0.0_SA_CTO~Z`'s clause stands as written: *"live while a session is warm"* is approximately
correct, refined only by **the refresh fires AT expiry rather than on every call.** Their
*"worse than carded"* is retracted; so is my withdrawal.

### ⛔ What survives all three of my positions — and is therefore the real finding

**THE RUNNER CANNOT SELF-HEAL.** Rows 2 and 3 are **measured, not inferred**: the runner ran twice
against an expired token and refreshed nothing, `exit 2` both times. Its `read_token()` is a **file
read** — it never calls the gateway, so it can never trigger the lazy re-mint.
**ONLY AN AGENT MCP CALL CLEARS THE REFUSAL.**

>> **THE EXPOSURE IN ITS FINAL FORM:** the buzz path **self-heals on the next agent gateway call
after expiry, and only then.** A staffed fabric heals it incidentally. **AN EMPTY FABRIC STAYS DARK
INDEFINITELY — because the one component that runs unattended is structurally incapable of the act
that would fix it.**

### On my own three positions

1. *exit 0 proves the credential live* → too strong; corrected to `APPLIED`.
2. *a plain gateway call does not refresh* → too strong; generalised from **n=1**.
3. This one.

**BOTH ERRORS WERE OVERGENERALISATIONS FROM A SINGLE MEASURED INSTANCE, AND BOTH TIMES THE
MEASUREMENT WAS CORRECT.** The 23:02Z call really did not refresh; what was wrong was the word
**"plain"**, which quietly asserted a universal.

⛔ **AND I DID FLAG THE GRADE — IN THE BODY.** The commit body said *"ONE INSTANCE … I am not
asserting the universal from n=1."* **Then I wrote the universal into the subject line and the
message headline, which is where people read it.** *The bound went in the body and the overstatement
went in the headline* — `0.5.0_AE_OpalETL~Z`'s **"the bound survived the author and died in the
relay"**, with the relay being me, four minutes later, to myself.

*The ~23:15:55Z boundary remains a natural experiment. It must not be manufactured — a call made to
test it is the pinger, and that stays vetoed.*
