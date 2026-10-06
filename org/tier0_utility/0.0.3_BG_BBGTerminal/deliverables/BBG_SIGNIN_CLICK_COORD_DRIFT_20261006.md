# Click-coordinate drift in bbg_signin.ps1 -- measurement and proposed remedy

**Status:** PROPOSAL. **NOT APPLIED.** `integrations/bloomberg/` is no-modify; the fix is
Andrew's word (`0.0.0_AB_MSTR~Z` msg 30038). Filed as surprise row **OPAL_BBGTML-Z-S2**
@952f3c8a00 (LOCAL). This file exists because the measurement below is PERISHABLE -- it is
specific to this dialog's live geometry and would have to be re-derived from scratch later.

**Measured:** 2026-10-06 ~12:0x-12:2xZ, on the live `BLOOMBERG: Login` dialog during an
authorized Step-2 recovery. Seat `0.0.3_BG_BBGTerminal`.

---

## 1. The defect

`bbg_signin.ps1` holds three ABSOLUTE SCREEN constants and clicks them with `SetCursorPos`:

```
$COORD_USER   = @(659, 348)
$COORD_PASS   = @(659, 426)
$COORD_LOGIN  = @(590, 482)
```

The live dialog sits at `L=275 T=64 R=1237 B=833` (962x769). Measured against the captured
bitmap, every one of the three lands on **RGB(0,0,0)** -- bare dialog background:

| control | true window rect | true screen centre | constant | offset |
|---|---|---|---|---|
| username field | x 61-301, y 202-230 | (455, 279) | (659,348) | **+204, +69** |
| password field | x 63-303, y 283-307 | (455, 360) | (659,426) | **+204, +66** |
| Login button | x 60-162, y 339-361 | **(386, 414)** | (590,482) | **+204, +68** |

Probe control: the password-field interior sampled `RGB(255,160,40)`, so the probe does detect
controls where they are. The offset is consistent across all three, i.e. a whole-dialog
translation, not three independent errors.

## 2. Why it is worse than a failed click

The unattended path does not degrade visibly. `bbg_fallback.ps1` -> `bbg_signin.ps1 -Phase
submit`:

1. records a fire-once ledger attempt **before** clicking (deliberate, correct),
2. clicks dead background,
3. waits 18 s, finds no listener,
4. reports `SUBMIT RESULT: still no listener` and escalates "sign-in submitted (1 attempt
   used) but DAPI still down".

**Bloomberg never received a login attempt.** The escalation text names a cause that did not
happen, and the fire-once budget burns down against a counter Bloomberg is not incrementing.
Entries on 2026-09-23 and 2026-09-27 read exactly this way.

## 3. The remedy is already in the tree

`bbg_verify.ps1` ALREADY solves this problem, in the same session, and the two files never
compare notes:

- it locates the username box dynamically (`$UserBox`, bands-scanned search),
- derives the password rect from it by a measured relation (`x-3, y+83`),
- falls back to constants on a MISS and prints *"a layout/DPI change may be live"*.

On 2026-10-06 it reported `locator: username field FOUND x=81 y=222 w=240 h=28` and
`delta vs constants dx=0 dy=0`. **Its own constants are correct.** The drift is confined to
`bbg_signin.ps1`'s screen-space constants -- which is precisely why it stayed invisible: the
one instrument positioned to notice a layout change was reporting zero drift in a DIFFERENT
coordinate space.

### Coordinate spaces (the thing to get right)

`Shot` captures from `(Left-20, Top-20)`, so:

```
shot coords  = window-relative + 20
screen       = window origin + (shot - 20)
```

Verified: locator `UserBox` shot (81,222) -> window (61,202) -> screen centre
`(275+61+120, 64+202+14)` = **(456,280)**, against (455,279) measured independently. Password
derived likewise lands (456,359) against (455,360) measured.

### Proposed change (shape only)

Replace the three frozen constants with values derived at call time from `GetWindowRect` plus
the located box, reusing `bbg_verify.ps1`'s locator rather than adding a second one:

```
userC  = (L + UserBox.x + UserBox.w/2 , T + UserBox.y + UserBox.h/2)
passC  = (L + UserBox.x + UserBox.w/2 , T + UserBox.y + 93)
loginC = (L + UserBox.x + 50          , T + UserBox.y + 148)
```

The two offsets `+93` and `+148` are measured from this dialog (username box top y=202 ->
password centre y=295, Login button centre y=350) and are stated in the same box-top-relative
style the file already uses for `PassRect`. **They are the one part of this proposal that is a
single-dialog measurement and should be re-confirmed by whoever applies it.**

### Falsifiable test it must pass

1. **Negative control, first:** assert each computed point is NOT `RGB(0,0,0)` before clicking.
   That single assertion would have caught this defect on the day it appeared, and it needs no
   knowledge of what the right answer is.
2. Positive control: computed username centre lands inside the located box.
3. After submit: 8194 listener count goes 0 -> 1 and the `BLOOMBERG: Login` window disappears.
   Both were observed on 2026-10-06 at 12:22Z from one click at (386,414).

## 4. Two adjacent findings (separate rows, not fixed by the above)

- **Z-S3, verify band.** `uLo=len-1, uHi=len` -> 11..12 for a 12-char username, derived from a
  fixture where ONE glyph pair touches. The live 12-char `<username>` contains TWO
  doubled-letter pairs -> renders 10 -> fails
  **every** time (3/3 on 2026-10-06), while the same gate's OCR scored the fill **100%**. The
  comment calls a 10 "fail-safe-rare"; for this credential it is total. Fix: derive the band
  from the credential's own doubled-letter count, or demote `okUser` to advisory beside the OCR.
- **Z-S4, Caps Lock.** Bloomberg's own *"Caps Lock is on"* warning was present in the 07:04
  fallback screenshot; machine state read `CapsLock: True`. The typer is `SendKeys::SendWait`,
  which is Caps-Lock-sensitive for alphabetic characters, so the password may have been typed
  case-inverted. The dot-count check cannot see it (case does not change the count) and the
  field is masked, so it is unverifiable by screenshot. Fix: clear Caps Lock in the fill path
  and log its state. Whether it contributed to the submitted-but-still-down days is **NOT
  established**.

## 5. Non-application

This file proposes; it applies nothing. It is not authorization to edit
`integrations/bloomberg/`, and it is not a second sign-in authorization -- the Step-2 scope
fence in `STANDING_ORDER_0715_DAILY_BACKSTOP.md` section 5 is unchanged.
