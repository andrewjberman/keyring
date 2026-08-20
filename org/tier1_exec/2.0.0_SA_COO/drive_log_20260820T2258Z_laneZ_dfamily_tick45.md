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

>> ✅ **THE CREDENTIAL IS READ AT CONSTRUCTION, EVERY PASS, REGARDLESS OF TRAFFIC.** So `exit 0` is a
real **EXERCISED-layer** proof the pinned gateway token was live — the 22:54:46Z pass verifies it as
of four minutes ago, on a pass that sent nothing.

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

**DETECTION IS SOLVED. REPAIR IS NOT.** The token expires roughly hourly and its refresh needs a live
agent MCP call — the runner cannot refresh what it can only observe. The standing exposure is not
*"we might not notice"*; it is **"we notice within 5 minutes and can do nothing unless a seat is
awake."** The detect/deliver seam again — and this time **detection is the half that works.**

**TIMING — arithmetic, not measurement:** hand-restored ~22:15Z against a ~1h TTL puts the third
refusal window near **23:15Z**. Named so nobody reads a 23:2xZ `exit 2` as a new defect; it is the
known exposure on schedule.

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
- Gateway credential: **verified live at 22:54:46Z by exercise**, not by config read
- No new commits in the window (42s — expected, not a finding)

## Carry-forward

- Item A (five `_meta` marks) build → both gateway changes ride one boot test
- W-A apply at the laptop; W-B awaiting Andrew; W-D limb (2); W-E criteria (2)(3)
- W-C capacity-blocked behind the 6-seat ceiling
- A1 on the next real client ticket
- Credential repair remains agent-dependent — the one part detection cannot cover
