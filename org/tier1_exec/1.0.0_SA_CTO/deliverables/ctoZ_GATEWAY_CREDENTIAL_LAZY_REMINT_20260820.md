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

> ⛔ **AMENDED 23:21Z — THE LINK IS MEASURED, AND IT WAS ALREADY IN MY INBOX WHEN I WROTE THAT IT WAS NOT.**
>
> ```
> teams-watch.py:477-479
>     while True:
>         tok = read_token()
>         if tok:            <- THE ENTIRE POLL BODY IS INSIDE THIS BRANCH
> ```
>
> On a dead token `tok` is falsy and **the monitor does nothing — it never reaches the gateway.**
> **Measured twice, independently:** by `0.5.0_AE_OpalETL~Z` at **23:16:16Z**, and re-read at source by
> `0.0.3_BG_BBGTerminal` at ~23:19Z.
>
> ⛔ **RETRACTED 23:23Z — THE PRE-CHECKS ARE MEASURED; MY CAUSAL CLAIM ABOUT THEM IS WRONG.**
>
> ~~"Our own defensive pre-checks are what prevent auto-recovery."~~ **`3.0.0_SA_CVO~Z` refuted it and my
> own data agrees with them:** the monitor and runner **read a stored token from a file and use it
> directly — NEITHER CAN MINT.** Only the Claude Code client mints, and teams-watch's docstring says so
> deliberately: *"Claude Code owns the refresh (rotating tokens), so this never refreshes itself."*
> **A de-pre-checked poller calling with a dead token gets a 401 and stays dead** — it burns a request and
> heals nothing.
>
> ⛔ **THE CONFOUND IS TOTAL, AND IT IS WHY I WAS ABLE TO BELIEVE THIS:**
> **every automated component both PRE-CHECKS and IS A RAW POLLER; every healing call both SKIPPED A
> PRE-CHECK and WENT THROUGH A MINTING CLIENT.** All five observations carry both variables together, and
> **the data cannot distinguish them.** I picked one, `3.0.0_SA_CVO~Z` picked the other, and only their
> prior is independently supported — **a STATED DESIGN INTENT beats an INFERRED MECHANISM when both fit
> the same observations.**
>
> **Why I picked the wrong variable: I had spent the preceding hour on refuse-before-calling** — the exit
> 2s, the silent-by-construction property, the protocol gap. **The pre-check was the variable in hand and
> I never generated the alternative. AVAILABILITY, NOT EVIDENCE.**
>
> **WHAT SURVIVES:** the pre-checks are real and measured — runner refuses before fetching, monitor gates
> its whole body on `if tok:`. **That is an observation. The claim that this is WHAT PREVENTS RECOVERY is
> withdrawn.**

⚠ **AND THE WAY I MISSED IT IS A NEW SHAPE WORTH MORE THAN THE FINDING.** The measurement did not arrive
late — **it arrived at 23:16:16Z, inside a retraction of a test-contamination alarm, in the same minute as
the test result itself.** I read it as being about **test hygiene** and filed it there. When the question
changed sixty seconds later — *"does the monitor pre-check?"* — **I did not re-read the datum I already
had, because in my head it was answered filed under a different heading.**

> **NOT A MISSING MEASUREMENT. A MEASUREMENT PRESENT AND FILED UNDER THE WRONG PURPOSE.** Every
> not-measured verdict tonight was reached by looking; **this one was reached by remembering what a datum
> had been about.** *A datum's purpose is assigned by the question live when it lands, and it does not
> re-file itself when the question moves.*

## 4. IF IT HOLDS, IT CHANGES ANDREW'S ITEM 3

His ask: *"a means to reauthenticate itself when the MCP connection dies."*

> ⛔ **THIS SECTION IS RETRACTED IN FULL. `0.0.0_AB_MSTR~Z` HELD IT AT THE FERRY BOUNDARY AND NEVER
> CARRIED IT.**
>
> ~~"The mechanism already exists and what blocks it is our own fail-safe — the remedy is letting one
> component attempt the call it currently declines."~~ **WRONG, per §3's retraction: a raw poller cannot
> mint, so removing the guard produces A CALL, NOT A RECOVERY.**

**THE REMEDY SPACE IS `3.0.0_SA_CVO~Z`'s, and Andrew already has it:** **route through a minting client**,
or **carry your own credential.** No correction to him is required — the version he holds is the
better-supported one.

⚠ **AND THE FAILURE MODE OF MY VERSION IS THE ONE WORTH RECORDING** (`0.0.0_AB_MSTR~Z`): it would have put
a *remove-one-guard* ask in front of the sovereign whose effect is **a failed request rather than a
recovery** — and **it would have looked cheap and safe, which is worse than looking wrong.** *A
wrong-and-expensive ask gets scrutinised. A wrong-and-cheap one gets approved.*

**THE HONEST OPEN EDGE:** nobody has read the client's mint logic, and `3.0.0_SA_CVO~Z` explicitly does not
assert there is no third path. That surface belongs to whoever owns it.

## 5. HOW THE MEASUREMENT WAS PROTECTED

A single-caller protocol: **one caller** (`0.0.3_BG_BBGTerminal`, who had a standing duty reason to read
that channel), **one reader** (`0.5.0_AE_OpalETL~Z`, who could read `expiresAt` and had no duty reason to
call), **every other seat off the gateway with compliance stated explicitly rather than privately
intended.** Window `23:15:55Z → 23:19:46Z`; the after-read landed at **23:16:31Z**.

⚠ **MY PROTOCOL HAD A HOLE AND `3.0.0_SA_CVO~Z` FOUND IT: it bound SEATS, and THE RUNNER IS NOT A SEAT.**
The scheduled task straddles the window. It turned out to be silent by construction on a dead token — **the
eager-at-construction file check, correctly relabelled APPLIED-grade, is what kept the experiment clean.**
*An instrument that states its own layer honestly protects a measurement rather than contaminating it.*
