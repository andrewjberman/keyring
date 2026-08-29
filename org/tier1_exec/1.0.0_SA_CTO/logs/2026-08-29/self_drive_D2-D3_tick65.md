# /self-drive D2 & D3 — tick 65 (2026-08-29 19:55Z) — state: ARMED

Covers **ticks 61-65** (tick 60 logged @f9f069f73f, tick 54 marked twice more @1886397303 and
@bf52476270 — all **ON ORIGIN**). Cron bde882a4 (:07/:37). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO`.
Written on a delta that **moved the register UP for the first time in this loop**, and on two
corrections of my own instruments.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (1 complete). ⛔ **Open TOs 24 -> 25**
(D2 18 -> **19**) — **a TO was CUT, not closed.** ✅ **Both instruments agree at 25** (register
`open_tos` and a fresh `to-check` extraction). Claims scan **342 of 342 JSONs**: D2 7 / D3 1,
**0 claimed-not-member**. Ledger **15 rows / 0 unconsumed** (CRLF 15 of 15). No MERGE_HEAD.

## ✅ THE DELTA — a surprise item became formal work in 80 minutes

`ADVI_49F.c02-GROSSLEG` *"stored-gross-of-fee-leg-determination"*, cut to `0.4.0_DS_ClientPlatform~N`,
face written 19:48Z. The chain, end to end:
```
  18:27Z  0.4.0_DS_ClientPlatform~C files it ARMED, keeps building, says the owner is not itself
  18:32Z  this seat DISARMS: owner = DS lane (Rule 13), blast radius BUILD-ONLY (serve arm-(a) gated)
  18:57Z  3.0.0_SA_CVO returns the evidence scope -- and REFUSES my framing (below)
  19:22Z  2.0.0_SA_COO seats ~N, finder explicitly excluded
  19:48Z  the TO exists
```
**The defect: `twr_daily` `r_gross` is LOWER than `r_net` by the fee rate on 11,705 of 11,705 fee
days — gross-of-fee should be higher.** Not client-facing (serve is gated, publisher unbuilt).

## ⛔ TWO INSTRUMENTS OF MINE CORRECTED, BOTH BY PEERS READING WHAT I PUBLISHED

**1. The reachability cross.** Tick 54's *"21 of 28 TOs have no live assignee"* — I re-ran it at
tick 61 **because a seat had been added**, which was the whole point of not carrying it forward.
⛔ **It re-read the ROSTER live and reused a TO list HARDCODED at tick 54, ninety minutes earlier.**
`2.0.0_SA_COO` caught it: the BDPARITY faces DO name `~C` (re-addressed @`31b1499c96` before
seating). Fresh: **8 of 24, not 7 of 28 — wrong in both terms.** ⛔ **And my own Step 0 printed
`24` in the same tick the cross printed `28`. Two numbers on one page disagreed and I published the
wrong one.** Marked in place three times; the third mark corrects the second.
✅ **What survives is COO's instance, not mine: `~V` does allocated work and appears on NO TO face
at all — which no face-based instrument can ever see.**

**2. The accept-arm framing.** I called the live exposure *"a wrong ACCEPT arm certifies silently."*
`3.0.0_SA_CVO` censused the arms tree (18 files, denominator printed): both arms touching `r_gross`
key on **EQUALITY**, never magnitude. ⛔ **A wrong-signed gross makes an equality arm read UNEQUAL
— it FAILS LOUDLY. Opposite class.**
```
  arm keyed on a VALUE     -> inherits a corrupt input and can PASS.  Silent.
  arm keyed on a RELATION  -> a corrupt input BREAKS the relation.    Loud.
```
⛔ **And the frame was the risk, not the answer: a seat that had ACCEPTED it would have hunted for
silently-certifying arms, found none, and reported CLEAN against a question that was never the right
one — a verified negative, which is worse than a wrong answer.** ✅ **That seat declined to inherit
it. Resisting the frame was the work.**

## The `server.py` retry — authorised, written, HELD

`0.0.0_AB_MSTR` routed the codex sidecar root cause to this lane; `2.0.0_SA_COO` 83582 answered
**"WANTED, take it"** and said explicitly it was a want-signal, **not a gate**.
⛔ **Sized by measurement, and the sizing limb was COO's:** a transient holder clears in 5x50ms, a
**continuous** one exhausts it — **and a retry that exhausts reads as DONE while still killing
sidecars occasionally.** `0.0.0_AB_MSTR` could not measure *what* holds the file (no Sysinternals;
installing it for a diagnostic fails the build ladder) but measured the **RATE**: 3 sidecars, **ZERO
new deaths, ~2,850 consecutive beats** at the oldest. ✅ **A continuous holder is incompatible with
that rate**, so the holder is transient and the budget covers it — **COO closed its own limb on that
and refused to launder the still-unmeasured cell.**
**Written:** 5 attempts / 50 ms, **re-raises on exhaustion on purpose** (a swallow converts a loud
death into silent liveness drift). `py_compile` rc=0; `import time as _time` confirmed module-scope
at `:41`; CRLF unchanged; **and it mirrors the function's own idiom — `:149-154` already retries the
lock the same way.**
⛔ **HELD, UNCOMMITTED: WINDOW 53 open 19:35Z, no CLOSE at 19:51Z, origin unmoved.** A hold ends at
the CLOSE, not at origin moving — and origin has not moved either.
⛔ **UNTESTED against a real collision, and it cannot be: forcing a `WinError 5` means taking an
exclusive lock on `liveness.json`, which would CAUSE the defect in a live heartbeat.** Reasoned from
the mechanism, sized from a peer's rate, **not exercised** — said here so a reader does not inherit
confidence the patch has not earned.

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** ⛔ **The denominator moved AWAY from done this tick and
that is correct:** a cut TO is work becoming visible, not work regressing.

## RESERVED at Andrew

**ONE, mine: `ADVI_49FSRC`** — his word on Mike at 49 Financial, or a supersede-close.
**NOT-MINE (`2.0.0_SA_COO`'s, noted not counted):** the BDPARITY P1-PROBE card, blocked on two of
his words. ✅ **I measured that card rather than asking whether it was accurate — it carries my
egress ruling correctly and improves on it** (*"the machine will not stop it; only he will"*, and
endpoints quoted back BEFORE the first call, which closes a gap I had left).

state: ARMED · push state: **server.py and this log both LOCAL and HELD**; origin/CLOUD
`1896be6985` (ls-remote 19:51Z); all 11 prior session commits ON ORIGIN with a positive control.

## Compiler Tools

- `directives-check --json` and a **FRESH `to-check` extraction every tick, cross-checked against
  each other** (the fix for the tick-61 defect: 25 vs 25 this tick) · claims scan 342 JSONs ·
  `server.py` read at source + patched + `py_compile` + module-scope import verified · **live
  read-only `File.Open(...,FileShare.None)` probe on `liveness.json`** — an instrument nobody had,
  **deliberately NOT run in a loop: it takes the exclusive lock and would CAUSE the failure it
  measures** · TO-face vs roster cross **re-derived from source, not from a constant** · verdict
  ledger byte-read · two-limb CLOSE oracle · `ack_messages` — ids from each opened file's own
  `Msg-ID` line, `to_serial` verified in `broker.db` (`?mode=ro`) first · `send_message`
  (83426-83428, 83429-83431, 83441-83443, 83444-83446, 83447-83449, 83472-83474, 83506-83507,
  83538-83540, 83552-83554, 83568-83570; **all DELIVERED, 0 QUEUED**).
