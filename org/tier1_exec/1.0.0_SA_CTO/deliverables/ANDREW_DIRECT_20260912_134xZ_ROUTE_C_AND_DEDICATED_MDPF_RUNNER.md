# ANDREW-DIRECT 2026-09-12 ~13:4xZ -- route (c), and a DEDICATED runner rather than a firm-specific one

**Received at:** the 1.0.0_SA_CTO terminal, in-session. **Recorded by:** `1.0.0_SA_CTO`.
⚠ **RECORDED LATE AND THAT IS THIS SEAT'S DEFECT.** `org/XXX.md` requires record + broadcast in the
SAME TURN. He ruled at ~13:4xZ, immediately redirected the conversation to a design brainstorm, and
this seat followed the redirect without first landing the record. **The ruling stood unrecorded for
roughly ninety minutes while work proceeded on its consequences.** Landing it now.

## VERBATIM AND ENTIRE -- two messages, in order

The first, answering a one-card `/open-calls` frame whose call was *"The three-firm directory build
cannot run without breaking firm isolation. (a) grant a narrow exception to the fence, or (c) split it
into three per-firm runs whose outputs are assembled separately?"*:

> "C"

The second, minutes later, unprompted:

> "There should be a dedicated mdpf runner for this also not reusing a firm specific runner"

## WHAT (c) RULED

**The cross-firm exception is REFUSED.** The directory build is split into per-firm runs rather than
granted an exception to `DenyForeignFirmPrincipals`. The recommendation he approved argued that the
fence is a structural guarantee about client data while the build is one feature's convenience, and
that trading the first for the second sets the precedent that the fence yields to schedule pressure.

⛔ **SO ROUTE (a) IS CLOSED AND STAYS CLOSED** unless he re-opens it by name. `0.7.0_AE_CloudOps~C`
was told this; nothing on `MDPF_GLOBAL.TO-IAM1` proceeds on an exception.

## WHAT THE SECOND MESSAGE ADDED

A **dedicated** runner for this work -- **not** `bd-exporter-ec2-role`'s host (firm-specific, built for
another purpose) and **not** a continued borrowing of the shared `mdpf-daily-runner` that carries
MDPF's own production chain. ⚠ **THIS SEAT READS IT AS BOTH**, since both were live candidates when he
wrote it and the sentence excludes a firm-specific runner explicitly while asking for a dedicated one.
**The narrow reading is recorded; if he meant only the firm-specific exclusion, that is his to say.**

## WHAT HAS HAPPENED SINCE, AND WHY THE IMPLEMENTATION IS NOT YET CUT

He then redirected to design: *"Let's actually brainstorm this by the process itself, what data
actually needs to be provided and where is it currently existing."* That produced measurements which
**changed what (c) costs**:

- `run_firm()` in `directory_runner.py` is ALREADY fully per-firm, and `main()` already accepts
  `--firms`. **The three-firm exposure is one `for` loop, not a data dependency** -- so (c) is an
  invocation and hosting change, not a rewrite.
- There is **no assembly step**: each firm's run lands its own file in its own destination
  independently. The "assembler that never holds two firms' identity data", which this seat described
  earlier as necessary, **does not need to exist.**
- The durable shape he then asked for is an accrual layer, specified for his review at
  `SPEC_IRPT_GOLD_ACCRUAL_MDPF_20260912.md` @`ac3915c7eb` -- **review only, authorizes nothing.**

## STATE AT THE MOMENT OF RECORDING

`IRPT_BCKEND` round 2 is FROZEN at 10 of 12 and nothing here re-opens it. `MDPF_GLOBAL.TO-IAM1` stays
OPEN at pending with AC4 FAIL, correctly. ⭐ **AND (c) MAY DISSOLVE THAT ORDER'S REMAINING NEED
ENTIRELY** -- under a per-firm split the mdpf host no longer reads 49financial at all, so the eleven
grants it stopped on may simply not be required. **NOT ASSERTED, NOT MEASURED, and not acted on.**

## OPEN AT ANDREW AS OF THIS RECORD

He has taken the platinum destination and read-path question to `4.0.0_SA_CRO`, VERBATIM:
*"I'm going to handle this with 4.0.0 we need to solve the formatting end to end once and for all, i
will get back to you shortly."* **This seat holds and starts nothing on that thread.**
