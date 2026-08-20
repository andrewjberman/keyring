# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:25–21:28Z (day tick 32)

**archetype:** COORDINATE

Quiet cycle: fabric clean (deaf=0/28), runner healthy on cadence, inbox empty, no commits but my own
since the prior marker. **One finding, and it is the kind a quiet tick exists to catch.**

| Item | Class | Owner | Attestation | Action |
|---|---|---|---|---|
| **D7 channel-leg A1** | **DEPENDENCY-HELD ON A DARK SEAT** | `0.0.3_BG_BBGTerminal` (dark) → `0.0.0_AB_MSTR~Z` (relaunch lane) | 6 seats live & fresh; BG **not among them** | **surfaced with the changed arm line + the measured path trap** |
| W-A / W-E / W-F | staged, no open design questions on W-E(1)/W-F | `0.5.0_AE_OpalETL~Z`, `1.0.0_SA_CTO~Z` | queue intact | none |
| Live intake runner | **HEALTHY** | `0.5.0_AE_OpalETL~Z` | 21:24:46Z pass, exit 0 | production surface watched |

---
## ⛔ RETRACTED 21:29Z — THIS TICK'S FINDING RESTED ON A FALSE PREMISE, AND IT WAS MINE

**A1 IS NOT BLOCKED AND WAS NEVER BLOCKED.** `0.0.3_BG_BBGTerminal` is **ALIVE** (process truth:
`claude.exe` pid 10260, session since 16:00:03Z) and had **ALREADY RE-ARMED at 21:11Z** — seventeen
minutes *before* I recorded it as dark — with `channels=1 watched (Opal Client Tickets)` **confirmed
in its own banner**. Its absence from the live set is the **POLLER-ABSENCE ARTIFACT**, not a down
seat.

**The corrected state:** A1 is **ARMED AND WAITING FOR A STIMULUS** — the next real post, unprompted,
which *is* the acceptance by design. It is deliberately **not** posting its own "now watching" line,
because a self-post is not a stimulus worth proving anything with.

⛔ **AND THE CLASS IS THE ONE I SPENT THE LAST HOUR DOCUMENTING.** I struck the M4 mechanism from
three of my own records at 21:1xZ, carrying forward *"the reading was FALSE, the seat was ALIVE"* —
and then, one tick later, **convicted that same seat as dark on the same instrument class.** This is
the **third** time tonight this artifact corrupted another seat's evidence about that seat.
**STANDING CORRECTION, adopted here: for `0.0.3_BG_BBGTerminal` specifically, do NOT read liveness
off the live set — read PROCESS TRUTH or its OWN TRAFFIC. Both are cheap.**

⛔ **THE SHARPER LESSON, because I did hedge — and the hedge did not save the record.** My dispatch
said *"surfacing rather than assuming"* and *"not asking for a relaunch on my word."* **But the LOG
asserted the premise flatly: "dependency-held on a dark seat."** *The caution sat in the message
while the claim sat in the durable record* — the same shape as the banked lesson that a declared
bound does not stop the inference. **A hedge on the ACTION is not a hedge on the PREMISE, and only
one of those two artifacts is what the next reader inherits.**

**WHAT SURVIVES AND WAS LOAD-BEARING:** the arm-line warning. The `--channels` flag in the **WINDOWS
path form** was correct and necessary — the seat used the Windows form successfully on the first try,
so the trap was real and the warning is now **discharged**.

*The original finding is preserved below as written, so the correction has something to be a
correction OF.*

## ~~The finding: the last open criterion was waiting on a seat nobody had noticed was down~~ (FALSE — see above)

The channel leg is **landed and accepted** (A2–A7 exercised, 17/17, discriminating mutant). **A1 — a
real channel post waking the agent UNPROMPTED — is the only criterion left**, and it is the one that
closes the answering limb this whole evening has circled.

**It cannot fire while the seat is dark, and it cannot be satisfied retroactively:** first arm
**seeds at NOW**, so the two existing posts (the header and the water-test buzz) structurally cannot
satisfy it. A1 takes the **next** real post after the re-arm.

⛔ **And the re-arm line CHANGED under it.** It now needs `--channels <config>`, **in the WINDOWS
path form** — the `/cygdrive/c/...` form fails `FileNotFoundError` because the config is read by
**native python**, which cannot resolve cygdrive paths (the class already banked in this device's
memory). It refuses **loudly** at arm time rather than missing silently — the good failure mode — but
it still costs the arm and a cycle. **On a correct arm the banner gains `channels=1 watched`; if that
line is absent the flag was not honoured.**

*Method note: `get_agent_status` on that serial returns a payload too large to consume, so liveness
was read from `liveness.json` directly — deriving live/stale from `last_seen` age, since there is no
status field. The instrument that answers the question is not always the one designed for it.*

**Routed, not decided:** the relaunch is `0.0.0_AB_MSTR~Z`'s lane with Andrew. I flagged that a
closed-looking chain is dependency-held on a dark seat, and that **BG being dark is itself an
instance of the M1/M4 class the perpetual-operator frame exists to address.**

Dispatches: 1 (two recipients). Gate: **PASS** — a quiet tick surfaced the one thing that would have
sat silently: the last open acceptance criterion, held by a seat that was not in the live set, with
an arm line that had changed under it.

## Compiler Tools
`fabric-check` / `deploy_ledger` cycle gates; a direct `liveness.json` read (with its own denominator)
after the broker status payload proved unreadable; runner.log as the production surface.
