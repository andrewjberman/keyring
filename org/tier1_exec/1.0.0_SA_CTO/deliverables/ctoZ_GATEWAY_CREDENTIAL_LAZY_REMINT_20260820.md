# THE GATEWAY CREDENTIAL: LAZY RE-MINT — established behaviourally, and the tension it exposes

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~23:20Z
**Measured by:** `0.5.0_AE_OpalETL~Z` (reads), `0.0.3_BG_BBGTerminal` (the call), `2.0.0_SA_COO~Z` (the floor challenge), `3.0.0_SA_CVO~Z` (the protocol gap), me (protocol + independent expiry confirmation)
**Status:** MODEL ESTABLISHED. One link named as UNVERIFIED and deliberately not asserted.

---

## 1. THE MODEL

| Token state at call time | Agent MCP call | Result |
|---|---|---|
| **DEAD** | yes | ⟶ **IMMEDIATE RE-MINT**, ~18s |
| **LIVE** | yes | ⟶ **nothing** |
| any | *proactive client refresh* | ⛔ **FALSIFIED** |

**TTL is 60 minutes.** The re-mint sets `expiry = call time + 60:00` exactly, on all three observed mints.

## 2. THE EVIDENCE

```
BEFORE  23:15:35Z   expiresAt 2026-08-20T23:15:55Z   0.3 min   LIVE
                    (anchored FOUR times: 23:05:06, 23:07:43, 23:08:09, 23:15:35 — two seats)
BOUNDARY            23:15:55Z
AFTER   23:16:31Z   expiresAt 2026-08-21T00:16:13Z   59.7 min  LIVE      +60m18s
```

**The mint time is RECOVERABLE FROM THE VALUE:** `00:16:13 − 60:00 = 23:16:13Z` — **eighteen seconds after
expiry.** Same construction as the 22:16Z mint.

- **2 dead-token positives** (22:16Z, 23:16:13Z)
- **~465 live-token negatives** — the monitor polled every 15s for 2h05m and the token **expired on
  schedule anyway.** *That population existed all evening and nobody had enumerated it; the one call that
  looked like a puzzling lone negative was a sample from it.*
- **1 falsified alternative** — proactive client refresh dies on the **22:06→22:16 ten-minute dead
  window**: a client that refreshed proactively would never have let it sit dead that long.

⚠ **ONE DATUM DROPPED, NOT COUNTED ON EITHER SIDE.** A `22:06:05` figure circulated all evening; a scan of
**29 transcripts** found it **7 times, every occurrence message TEXT**, first appearance in its own author's
prose, **no tool result anywhere.** Its author's memory of it **crossed a compaction** and they dropped it —
against their own position. *The trap worth keeping: they WERE demonstrably reading `expiresAt` in that
window, which is exactly what makes the memory feel grounded. **Being in the habit of measuring does not
make a specific remembered number a measurement.***

**ESTABLISHED WITHOUT ANYONE READING THE CLIENT'S REFRESH LOGIC** — a black-box characterisation with a
discriminating variable, a recoverable derived quantity, and a falsified rival. **Arguably stronger than a
source read alone, because it measures what the thing DOES rather than what it is written to do.**

## 3. ⛔ THE TENSION — stated as a question, one link UNVERIFIED

If dead-token + call ⟶ re-mint, **the 22:06–22:16 dead window needs explaining**, because the monitor was
polling every 15 seconds throughout it — ~40 polls, dead token, **no re-mint.**

**The only reading that fits:** the monitor, like the runner, **checks the pinned token locally and refuses
before calling.** On a dead token it never reaches the gateway — and **a call that is never made cannot
trigger a re-mint.**

> **WHICH WOULD MEAN: OUR OWN DEFENSIVE PRE-CHECKS ARE EXACTLY WHAT PREVENT AUTO-RECOVERY.** Every
> component that refuses-before-calling on a dead token is also declining to make the one call that would
> heal it — **structurally unable to self-heal for the same reason it fails safely.**

**It explains the whole evening:** a human-driven gateway read healed it twice; ~464 automated polls did
not. **Not because agents are special — because the agent path does not pre-check and the automated paths
do.**

⚠ **THE MONITOR'S PRE-CHECK IS NOT MEASURED. `0.5.0_AE_OpalETL~Z` owns that read.** Asserting it is the
move that cost this fabric five retractions tonight, and it is not being made here.

## 4. IF IT HOLDS, IT CHANGES ANDREW'S ITEM 3

His ask: *"a means to reauthenticate itself when the MCP connection dies."*

**If the above is right, the mechanism ALREADY EXISTS** — a call on a dead token re-mints in ~18 seconds —
**and what blocks it is our own fail-safe.** The remedy would not be new machinery; it would be **letting
one component attempt the call it currently declines to make.** That is a materially different and cheaper
answer than the one carded. **NOT re-carded until the link is measured** — better carded once correct than
a fifth time.

## 5. HOW THE MEASUREMENT WAS PROTECTED

A single-caller protocol: **one caller** (`0.0.3_BG_BBGTerminal`, who had a standing duty reason to read
that channel), **one reader** (`0.5.0_AE_OpalETL~Z`, who could read `expiresAt` and had no duty reason to
call), **every other seat off the gateway with compliance stated explicitly rather than privately
intended.** Window `23:15:55Z → 23:19:46Z`; the after-read landed at **23:16:31Z**.

⚠ **MY PROTOCOL HAD A HOLE AND `3.0.0_SA_CVO~Z` FOUND IT: it bound SEATS, and THE RUNNER IS NOT A SEAT.**
The scheduled task straddles the window. It turned out to be silent by construction on a dead token — **the
eager-at-construction file check, correctly relabelled APPLIED-grade, is what kept the experiment clean.**
*An instrument that states its own layer honestly protects a measurement rather than contaminating it.*
