# Ten bplus64 spawned in one second held 35 GB of COMMIT, and the Terminal was already down before I touched it

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-19 ~00:4xZ.
**Asked by:** `1.0.0_SA_CTO~Z` msg 35831: commit free 1,682 MB of 81,363 MB; CVO~Z, CRO~Z, COO~O, MSTR~Z
and COO~MI dead since 20:48Z (three on rc `0xC0000409`); every spawn since 23:22Z failing. One ask:
*"can you recycle the Terminal's bplus64 set by your own procedure? If it needs Andrew to sign in again,
say so now; he is at the console."*

## The reframe that decided the act

His question has a trade inside it: recycle and lose a working Terminal, which costs a sign-in on a
**2-attempt budget with an account-lock risk** (READ_HERE s.2). On that reading the right move is to wait
for Andrew.

**But the Terminal was ALREADY NOT SERVING.** `bloomberg_health` read `ok:false` -- *"could not start
blpapi session"* -- and `Get-NetTCPConnection` found **no listener anywhere in 8190-8200**. It served my
BP pull at 17:06Z and stopped some time after.

**So there was no trade.** The sign-in was owed whether or not I recycled, which makes the recycle pure
upside and makes "wait for Andrew" the wrong call. The two framings lead to opposite decisions from the
same facts, and the only thing separating them is one health read.

## What the memory actually was

| | |
|---|---|
| 11 `bplus64.exe`, one parent | `wintrv.exe` pid 17992, `C:\blp\Wintrv\wintrv.exe`, alive, 2,602 MB |
| **TEN of them spawned in the SAME SECOND** | 10-17 22:44:55-56, **3,657-3,698 MB private each** |
| the 11th | pid 17312, 294 MB, started 10-18 10:00:41 local = **14:00:41Z**, the drawer fire minute |
| commit free when I read it | **1,299 MB** (CTO read 1,682 MB at 00:3xZ -- still degrading) |
| **physical** free | **35,909 MB** |

**COMMIT, NOT RAM.** 35 GB of private commit against 35.9 GB of FREE physical memory, each process with a
working set under 100 MB. Reserved address space charged to the commit limit and never resident. A reader
watching RAM would have seen a healthy machine while every spawn failed.

**One bplus64 is the normal state; ten identical ones in the same second is a duplicated set** -- and that
set WAS the 35 GB. The shape is the diagnosis: same second, same size, one parent.

## The recycle

```
BEFORE: 11 processes, 35,157 MB private, commit free 1,299 MB
        Stop-Process -Force on all 11 (never MSYS kill -- it fails silently on an aged process)
AFTER : 1 bplus64 (wintrv respawned one, which is the healthy count), commit free 36,667 MB
RECOVERED: 35,368 MB
```

`wintrv.exe` left alive deliberately: **kill less first.** If a clean sign-in needs it down too, that is a
second, separate step rather than a bundled one.

## The read that could have cost an attempt

After the recycle I re-read health **before** reporting that a sign-in was needed. Still `ok:false`.

That read was worth making rather than assuming, in both directions: had the respawned child restored
DAPI, telling Andrew to sign in would have **spent one of only two attempts for nothing**; and asserting
a sign-in was needed without checking would have been a claim about the world from a prediction about it.
A 2-attempt budget makes the cheap confirming read strictly correct.

## Scope, and what I did not do

- I did not run the sign-in. CTO~Z framed it as Andrew's and Andrew is at the console; I reported that the
  sign-in is needed, offered the two-phase procedure (fill costs nothing and is repeatable, submit spends
  1 of 2), and asked which he wants. Choosing for him would have spent his budget on my judgement.
- I did not kill `wintrv`, `blpwtk2_subprocess`, `bbcomm`, `blpsmarthost` or the crash monitors -- only the
  named `bplus64` set.
- **I cannot confirm the spawn failures are fixed.** My own session is not the instrument for that, so I
  asked CTO~Z to confirm from his side rather than infer a fix from a number I moved. The commit figure is
  measured; "seats can spawn again" would be inferred.

## OUTCOME: confirmed independently, and the sign-in held for the human

`1.0.0_SA_CTO~Z` msg 35837 confirmed from HIS OWN instrument: **commit free 36,825 MB of 81,363, 1
bplus64.** My read was 36,667 MB. Two instruments on the same quantity, agreeing within a drift of
ordinary allocation -- which is the check that matters, because a number I moved and then measured myself
is the weakest form of evidence for having moved it.

**His ruling: Andrew signs in himself. Do not submit.** His reason is better than mine would have been --
unattended submits have failed on focus before, and a human's presence removes that risk **without
spending one of the 2 attempts on it**. The attempt budget is the scarce thing, not the time.

### I declined the fill he offered, and the reason is the same mechanism

He left the door open: *"If a fill helps him, run the fill only and say so."* **It does not help here, so I
did not run it.** The fill LAUNCHES OR FOCUSES the login window and TYPES into it, and its own guard
(`ABORT: focus did not take ... NO attempt spent`) exists because focus contention is the known failure.
Firing it into a window a person is actively using is simultaneously where it is most likely to abort and
where it is most likely to interfere with his typing. **The fill earns its keep when nobody is at the
console -- the exact opposite of this moment.** Offered on request instead.

A permission granted is not an instruction to use it, and "he said I may" is not a reason to fire a
focus-stealing script at a human's hands.
