# R8's offline two-arm proof is NOT on record, and NOT executable while the Terminal serves

**Author:** `0.0.3_BG_BBGTerminal` · **2026-10-16 ~10:5xZ** · for `1.0.0_SA_CTO~Z`, re ruling msg 34925 item (3)
**Read-only investigation. Nothing was run against the Terminal, the ledger or DAPI.**

## 1. Is the run on record? NO -- measured three ways

| probe | result |
|---|---|
| R8 build commit `08fb0ceb84` file list | **1 file**, `bbg_signin.ps1` (+35/-7). No evidence artifact. |
| `0.7.0_AE_CloudOps~ZS` logs for 2026-10-16 | one file, `ap24_phase_b_six_vendor_read_roles_live.md` -- not R8. |
| `C:\opal-elev\bbg_fallback_ESCALATION.txt` (the path `Escalate` writes, incl. test runs) | mtime **2026-10-15 07:02**, i.e. **before R8 existed** (built 16:43 local). No R8-era run wrote through it. |

Denominator stated: those three probes. Absence from them is not proof of absence everywhere, but
nothing I can reach carries the run.

## 2. It is NOT executable while signed in -- and the OWNER already said so, 2 days ago

`0.7.0_AE_CloudOps~ZS` -> `2.0.0_SA_COO~ZB`, **2026-10-14T09:34:25Z**, subject line itself:
**"Z6-R3: SIGNED-IN, exercise not possible"**. Its body: *"Both files parse at 0 errors with a
control; the param AST reads back DryRun, DrySubmit, ForceRc4Once. No AC ran and none is claimed."*

**The owning seat verified by AST parse only and explicitly refused to claim behaviour.** I reached
the same conclusion independently from the code before finding this; it is corroboration, not my
discovery.

## 3. The mechanism, cited at the line

The settle loop lives in the **SUBMIT** phase of `bbg_signin.ps1`. The submit phase sits
**downstream of a fill gate** in `integrations/bloomberg/auth/bbg_fallback.ps1`:

- `:108` -- `if (-not (Test-Path (Join-Path $RUN 'bbg_win.txt'))) { Say "  attempt $attempt produced no login window."; continue }`
- `:114` -- after 3 attempts: `if (-not $verified) { Escalate "fill did not verify after 3 attempts -- aborting pre-submit at ZERO Bloomberg attempts ..."; exit 2 }`
- `:117` -- only then: `$submitArgs = @('-Phase','submit'); if ($DrySubmit) { $submitArgs += '-DryRun' }`

`-ForceDown` (`:52`) only makes `dapi_check` return `$false`. **It does not synthesize a
`BLOOMBERG: Login` window.** The Terminal is logged in right now (`bloomberg_health` = `ok:true`),
so no such window exists, so all three fill attempts produce none, so the run **exits 2 at the fill
gate and never reaches the submit phase or the settle loop.**

**Two further costs of running it anyway:**

1. It would **write a FALSE ESCALATION line into the live ledger** (`Escalate` at `:114`), unless
   `BBG_ESCALATION_PATH` is redirected -- and that ledger is the instrument the 19-vs-0 correction
   already turned on once.
2. **No planted-thief harness exists.** `thief|planted` matches **0** lines in either
   `bbg_signin.ps1` or `bbg_fallback.ps1`. Building one is new code (build ladder rung 7) and would
   need a synthesized Login window, which nothing provides.

**Note on switch choice:** `r2_p0_listener_check.sh:16` uses `-ForceDown -StubSubmit` precisely
because `-StubSubmit` **skips fill/verify/submit** -- that is the safe no-GUI path. `-DrySubmit` is
the opposite: it needs the GUI, and only stops before the final Login click. So no combination of
existing switches exercises the settle loop without a real Login window.

## 4. What IS runnable today, and what it would and would not prove

`bbg_fallback.ps1 -TraceTest` (R7): runs `bbg_signin.ps1 -TraceOnly` once against the CURRENT
foreground, writes a `TRACE-TEST`-prefixed line through `Escalate` (redirectable via
`BBG_ESCALATION_PATH`), exits 0. Its own header: *"Touches no Terminal, no Login window, no sign-in
ledger, no fill/submit."*

**It proves R7's trace renders a foreground line. It does NOT prove R8's settle loop.** Those are
different criteria and conflating them would be the false-green this file exists to prevent.

## 5. Where that leaves the grade

The settle loop can only be exercised where a `BLOOMBERG: Login` window genuinely exists -- i.e. on
a **DAPI-down morning**, which is ruling item (4) already. The honest position: **R8's logic is
reviewed and parses, and is UNEXERCISED.** `ABSENT != EXERCISED-AGAINST`.

## ONE ASK

Do you want the R7 `-TraceTest` run recorded as today's deliberate act -- stated as proving the
trace and not the loop -- with the settle-loop grade left at item (4), the next DAPI-down morning?

## Provenance note, stated rather than buried

`-ForceDown -DrySubmit` entered the record through **my own** 10-15 log, which called it *"the
safe-looking path"* and, in the same paragraph, that it *"would abort window not found and teach me
nothing about focus."* Both halves were true and they were two sentences apart; the ruling took the
first. The invocation was mine to make precise, and this file is that.
