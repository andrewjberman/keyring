# Making the unattended sign-in VERIFY deterministic — options, evidence, and what I did not determine

**Author:** `0.0.3_BG_BBGTerminal`, 2026-08-20 ~1310Z.
**Raised by:** Andrew, at this terminal, reading the 08-20 backstop postmortem.
**Assigned by Andrew to:** `0.0.0_AB_MSTR~Z`, **personally.**

> **ANDREW-DIRECT, VERBATIM (2026-08-20, chat, this terminal):**
> *"How is this fuzzy? Is there any way to improve this part? it seems like it should be fairly
> deterministic like verything else"*
>
> then, on the write-up:
>
> *"write it up and issue to MSTR~Z and tell them to handle it personally"*

**Citations pinned to vintage:** `bbg_verify.ps1` @`480daa841f` (its last commit), tree @`cde87899b6`.

**Proportion, stated up front: THIS IS AN IMPROVEMENT, NOT AN INCIDENT.** Nothing failed on 08-20 —
the verify passed, the sign-in succeeded, the pull published clean and served-verified. Andrew asked
the right question about a soft spot. It is not a fire.

---

## 1. What the verify does today

`bbg_verify.ps1` is the pre-submit gate: it decides whether an unattended fill is good enough to
click Login **once**. Called at `bbg_fallback.ps1:89`, retried up to 3x at `:76-92`; a persistent
failure aborts **at ZERO Bloomberg attempts** (`:93`). That design is correct and the abort path is
the right one — none of what follows argues otherwise.

It does **not read the login fields.** It reads a **screenshot** of them, cropping two rectangles:

| limb | method | deterministic? | source |
|---|---|---|---|
| password length | counts dark pixel-column runs -> `9 (expect 9)` | **YES, exact** | `Count-Dots` `:44-56` |
| username | Windows OCR on a 3x upscale, then Levenshtein similarity | **NO** | `Ocr-Region` `:73-93`, `:99` |

Gate = `okDots AND okUser` (`:103-105`), with `UserMinSim = 0.62` (`:16`).

08-20 live result: `password dots: 9 (expect 9)` and
`username OCR: 'filyssaak?ith' vs expected len 12; similarity 77% (min 62%)` -> **PASS**.

## 2. Why it is fuzzy — the fuzziness is DOWNSTREAM of the screenshot, not a design preference

Once the input is a photograph, OCR is the only way to recover text, and OCR on a stylized font is
inherently approximate. **The question worth asking is not "why is the OCR fuzzy" but "why is it
reading a picture at all."**

**Because the deterministic route appears closed. Measured 2026-08-20 ~1308Z, not assumed:**
Bloomberg's UI is Chromium (`blpwtk2`). Its windows expose **one opaque pane** to UI Automation —
`IB - IB Manager` returns exactly **1** descendant, a nameless `Chrome_WidgetWin_0`. No edit
controls, no values. `WM_GETTEXT` has nothing to address either.

**POSITIVE CONTROL (the probe works, so the `1` means something):** non-Bloomberg top-level windows
on the same desktop returned **38** (Explorer tray), **32** (Teams), **16** each (six agent
terminals), 31, and 2. **MAX non-Bloomberg = 38 vs Bloomberg = 1.**

> ⚠ **THE CONTROL CARRIES THE MOST USEFUL FINDING IN THIS DOCUMENT: Teams is ALSO Chromium and it
> DOES expose a tree (32 descendants).** So this is **not a Chromium limitation** — Chromium builds
> its accessibility tree **on demand**, and Bloomberg's host has not enabled it. **A deterministic
> read may therefore be ATTAINABLE rather than impossible.** That single fact is what makes Option 1
> worth trying instead of dismissing.

## 3. THE BIGGER PROBLEM IS NOT THE OCR — IT IS THE HARDCODED RECTANGLES

The field regions are fixed pixel offsets measured once, on one dialog, at one position (`:39-40`):

```
$UserRect = ($WinLeft+60, $WinTop+206, 240, 26)
$PassRect = ($WinLeft+58, $WinTop+285, 120, 22)
```

**The file's own header records what that already cost (`:28-31`):** the previous constants sampled
the blank band above the logo, so **every correct unattended fill was judged EMPTY and aborted
pre-submit on 08-16, 08-17 and 08-18.** Three days in which the automation could not recover at all
— and the live path had never been exercised against a real filled shot; only the `-Fixture` path had.

**The two failure shapes are not equivalent:**

- **OCR degrades GRACEFULLY.** A slightly-wrong read still scores high and passes; a genuinely wrong
  field scores low and aborts safely.
- **A WRONG RECTANGLE FAILS TOTALLY.** It reads empty, aborts every single time, and the recovery
  capability is simply gone until a human notices. It is silent in the *safe* direction, which is
  exactly why it survived three days.

It is exposed to any dialog-layout change, DPI/scaling change, resolution change, or Bloomberg
update. **This is the part that is not deterministic in the way that matters.**

## 4. Ranked options

**Option 1 — READ THE VALUES, NOT THE PICTURE.** Obtain/enable the Chromium accessibility tree for
the login dialog and query the username field's value directly. **Kills the OCR AND the rectangles in
one move**, and removes the DPI/layout exposure entirely.
*Feasibility: UNPROVEN for the login dialog — see §5. The cheap settling test is named there.*
*To check: Chromium activates a11y on a client signal (historically `WM_GETOBJECT`, or
`--force-renderer-accessibility`); whether `blpwtk2` honors either is the open question.*

**Option 2 — IF 1 FAILS: MAKE THE USERNAME LIMB EXACT, THE SAME WAY THE PASSWORD LIMB ALREADY IS.**
The password check does not OCR anything — `Count-Dots` (`:44`) counts glyph runs. **Apply the
identical technique to the username box: expect 12 runs.** Deterministic, reuses code already in the
file, needs no OCR engine, and it catches the real hazard: **a 9-character password landing in the
username field is 9 runs, not 12.** OCR then becomes a LOGGED OBSERVATION rather than a gate.
*Highest confidence-per-effort. I would start here if Option 1 stalls.*

**Option 3 — MAKE THE RECTANGLES SELF-LOCATING (independent of 1 and 2).** Find the input boxes by
their own visual signature (the orange field) rather than fixed offsets. **This is the thing that
actually broke for three days**, and it is worth doing even if Option 1 succeeds — unless Option 1
removes the screenshot path entirely, in which case it is moot.

**Option 4 — RAISE THE 0.62 FLOOR.** Weakest; listed for completeness. It keeps a fuzzy instrument in
a gate position and merely tunes it. **Not recommended as the answer.**

## 5. What I did NOT determine — read this before acting on §2

- **I tested the MAIN Bloomberg windows, NOT the login dialog.** It was not open, and **I deliberately
  did not open one**: that would spend a fire-once ledger attempt and is the P0 gate's business, not
  mine. **The login dialog may be a different window class with different behavior.** §2 is strong
  evidence, **not proof for the specific dialog.**
- **THE CHEAP TEST, and it costs nothing extra:** at the **next genuine recovery**, while the
  `BLOOMBERG: Login` dialog is legitimately open, enumerate its UIA tree (a read-only walk, ~2s) and
  record the descendant count plus whether any element exposes a Value. **That settles Option 1
  either way.** I can run it inside my Step-2 recovery and report — it adds no attempt and no risk.
- I did not test whether `--force-renderer-accessibility` or a `WM_GETOBJECT` probe activates the
  tree. Both are cheap, but both touch a live trading terminal, so they are the owner's call.
- **I have changed nothing under `integrations/bloomberg/auth/`.** This seat is read-only and does no
  git. **Nothing here is implemented.**

## 6. Why the fuzzy limb was not load-bearing on 08-20 (proportion, stated honestly)

The known failure mode is **the password landing in the unmasked username field** — my own error,
2026-08-11, which burned one Bloomberg attempt. **That case shows 0 dots, not 9**, so the EXACT limb
catches it. The OCR limb passing at 77% on mangled text endangered nothing that day.

**The reason to fix it anyway:** the exact limb covers the hazard we have *already seen*. The fuzzy
limb is what stands between an automated fill and a **Bloomberg lockout** for hazards we have not
seen yet — and a 62% floor on unreadable text is close to "usually passes."

**A gate guarding a lockout should not be the softest link in a chain whose every other link is exact.**
