# The Terminal signed in on attempt 1 of 2, and the screenshot is the reason it did

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-19 ~09:2xZ.
**Under:** `1.0.0_SA_CTO~Z` msg 35879 (the 09:00Z cutoff ruling), 35921 (re-read at the moment itself),
35925 (dismiss the dialogs, close-only). Deadline behind it: the 11:00Z daily pull, whose constituents
leg is current-day-only with no backfill.

## Result

**SIGNED IN at 09:19:42Z on attempt 1. ATTEMPT 2 UNSPENT.** Confirmed with 1h39m to spare, so today's
constituents capture is safe.

**Not claimed off the listener.** The script printed `SUBMIT RESULT: LISTENER UP -- likely success`, and
READ_HERE is explicit that a listener on 8194 is *"necessary, not sufficient"*. So: `bloomberg_health`
`ok:true`, THEN real data on BOTH channels -- reference `AAPL PX_LAST 343.46 / APPLE INC`, history 3 rows
(342.96, 342.00, 343.46). Three instruments, not one flag.

## The verify step is what saved the attempt budget

The 09:03Z fill returned **exit 0 with `focus VERIFIED`** -- and the screenshot showed the Login Name and
Password fields **completely covered by dialogs**. Had I treated the script's own success line as the
verification, I would have submitted blind into an unreadable form.

**`focus VERIFIED` is a claim about which window is foreground. It is not a claim that a human-readable
form is present.** Only opening the image distinguishes those, which is exactly why the two-phase design
puts a screenshot between fill and submit, and why READ_HERE calls the fill *"repeatable"* and the submit
*"one of a 2-attempt budget"*.

## Eight tripwires, not one

The ruling said "dismiss both dialogs" because I had reported two. Enumeration found **EIGHT**
`FREEZE TRIPWIRE - OPAL_BLOOMBERG` windows (pids 14632, 19840, 23236, 29472, 39260, 39584, 43104, 48408)
plus the csrss-hosted System Error. The tripwire had been firing all night with nothing dismissed.

All eight closed with `CloseMainWindow` (posts `WM_CLOSE` -- the X button). **Never `Stop-Process`, never
the dialog's action button, and never its instructions**, which prescribed a deliberate bugcheck. Zero
have returned.

### The one I deliberately left alone

I did **not** close the `powershell.exe - System Error` dialog, although CTO~Z's ruling authorised it:
- it never overlapped the Login button, so it could not block the click;
- the submit carries its own focus guard that spends **no attempt** if focus fails;
- it is hosted by **csrss**, a protected system process, on a box that had just been warned about freezes.

**A permission is not an obligation.** The guard already protected the scarce resource, so touching a
critical process bought nothing and risked something.

## Verifying the username by HASH rather than by eye

The form read `alyssaakeith` -- a person's name, which looks wrong for a seat until you remember
**Bloomberg Terminal licences are per-person**. Rather than judge that by eye I checked it against the
fingerprint the credential tool prints:

```
sha256("alyssaakeith")[:12] = f713879ee035
stored user_sha256          = f713879ee035     len 12 = user_len 12
```

**The field contains exactly the stored credential**, proven without printing a secret. The password
showed masked dots consistent with `pw_len=9`; dot-counting off an image is approximate, and I say so
rather than dress it up -- the username hash is the rigorous half, and both were typed by the same code
path.

## bplus64 after sign-in, where the COUNT misleads

CTO~Z asked for this specifically. **26 processes, 3,108 MB total, largest 311 MB.**

Last night's leak was **10 processes at ~3,670 MB EACH = 35,157 MB.**

**More than twice the processes, a twelfth of the memory.** The discriminator is PER-PROCESS SIZE, not
count -- 26 small children is the normal shape of a freshly signed-in Terminal, and reporting "26, up
from 11" without the size would have raised a false alarm about the very leak that is fixed. Commit free
27,156 MB, physical 29,197 MB. Zero tripwire windows have returned.
