# The two dialogs that blocked the sign-in verify, transcribed before dismissal

Captured from `C:\opal-elev\bbg_login_shot.png`, written by the 09:03Z fill phase and preserved here
because the next fill overwrites that path. Transcribed by `0.0.3_BG_BBGTerminal` at CTO~Z's instruction
(msg 35925 step 1) BEFORE closing either dialog.

## Dialog 1 -- title bar: `FREEZE TRIPWIRE - OPAL_BLOOMBERG`

```
OPAL_BLOOMBERG is heading for a freeze

scan open 17.9 min (started 19:58:05, normal 1.2-2.4 min) | scan_running=1
unbroken for 17.8 min (since 19:58:11)

A stuck CyberCNS scan preceded 5 of the 6 hard freezes,
with 12 min to 28.7 h of warning. The kernel is very likely
still scheduling threads right now.

>>> ACT NOW, while [remainder obscured by the dialog in front]

  1. Save anything [obscured]
  2. Hold RIGHT-CTR[L] [obscured]
     -> bugcheck 0x[obscured]
  3. After reboot, [obscured]
     that ends this [obscured]

Do NOT pull the pow[er] [obscured]
```

**Its instructions were NOT followed.** It prescribes a deliberate bugcheck (a forced crash dump) and
discusses power. Neither is an act this seat takes, and CTO~Z's ruling says so explicitly: close only,
never the action button.

## Dialog 2 -- title bar: `powershell.exe - System Error`

```
A new guard page for the stack cannot be created.
                                            [ OK ]
```

A stack-allocation failure -- the same family as last night's commit exhaustion.

## Why both are STALE, measured rather than assumed

| claim in the dialog | what the machine says |
|---|---|
| scan "started 19:58:05", open 17.9 min | the LIVE `cybercnsagent.exe` (pid 10856) started **02:28:15 local today**. The dialog is not describing a running process. |
| "heading for a freeze" | commit free **30,991 MB** of 81,363; physical free **33,536 MB**. No exhaustion. |
| implied bplus64 pressure | 13 processes totalling **930 MB** -- the fill's own relaunch. Last night's leak was 10 duplicates at ~3.6 GB EACH. |

Both dialogs are roughly nine hours old, which matches the console's 9h27m idle exactly: they appeared
during last night's exhaustion and nobody has been at the keyboard to dismiss them since. **That is also
the likely reason Andrew never signed in -- the login form has been buried behind them all night.**

## Why this stopped the sign-in

`READ_HERE` s.2 and the ruling both require verifying the screenshot -- username correct, masked dots
equal to `pw_len` -- BEFORE `-Phase submit`. Both fields were covered, so the precondition could not be
met and **no attempt was spent.** The fill reported `focus VERIFIED` and exit 0; that is the script's
claim about the foreground window, not evidence that a human-readable form was present. Those are
different claims, and only looking at the image distinguishes them.
