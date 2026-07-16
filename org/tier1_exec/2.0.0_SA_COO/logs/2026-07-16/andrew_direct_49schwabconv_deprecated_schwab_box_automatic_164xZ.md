# ANDREW-DIRECT (recorded verbatim): the manual Schwab download/convert process is DEPRECATED — the schwab box does it automatically

**archetype:** SCRIBE
**Channel:** COO terminal (2.0.0_SA_COO session, direct)
**Time:** 2026-07-16 ~16:4xZ (clock read from `date -u`, not derived)
**Recorded by:** 2.0.0_SA_COO, same turn per `org/XXX.md` ("Andrew-direct instructions — RECORD + BROADCAST, same turn")

## VERBATIM

> "that is deprecated now though because we dont need to do manual/local downloads anymore, the whole process is automatic in the schwab box"

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

## What it was said about

COO had just grounded a coupling in the `opal-data-schwab` decommission (Andrew-direct ~16:2xZ via
`0.5.0_AE_OpalETL`, verbatim @ `de4978e3a`): the AE-owned recurring skill
`.claude/skills/49-schwab-conv/SKILL.md` writes to the exact bucket being decommissioned —

- `SKILL.md:28` — Raw S3 dest `s3://opal-data-schwab/01_raw/` (all ext) + `*.RPS` mirror to `s3://opal-data-schwab/bronze/rps/`
- `SKILL.md:13` — its whole AE-ownership rationale is the `opal-data-schwab` resource-based DENY on DS
- Trigger: **Andrew's own voice** — *"we downloaded the new Schwab data" / "convert the Schwab files"*

COO was about to route it to `0.5.0` + CTO as **"the census must re-point this skill."**

## THE CORRECTION — and it inverts the remedy, not the fact

The coupling is **real** (grounded at source, 1 of 1 skill files referencing the bucket). The **remedy COO was
about to route was wrong.** The skill does not need re-pointing. **Its premise is dead:** there are no manual
local downloads anymore, so the trigger event (*"we downloaded the new Schwab data"*) will not occur, and the
box does the whole process.

**A deprecated process does not get REDIRECTED. It gets RETIRED.**

This is **the SALVAGE blade Andrew issued the same hour** (~15:4xZ, via `0.7.0_AE_CloudOps~B`, committed
`e3aaec0b0`), applied to COO's own finding:

> "not necessarily 'fixing' the calibrations if the calibrations are just wrong. The idea is to identify what is
> actually important, what are actually good ideas in this report, and then we grab those and refine as needed,
> and throw out all the trash."

The blade: **"if this check fires, is there something a human would DO?"** For `/49-schwab-conv` the answer is
now **no — the box already did it.** So: DISCARD, not REFINE. And the sibling correction from that same ruling
applies exactly: *suppressing a bad check KEEPS the bad check; deletion is cleaner.* **Re-pointing a dead skill
at a new bucket is the same error as recalibrating a check nobody would act on — it preserves the thing while
making it look tended.**

## Class

This is the **deprecation/retraction-propagation class**, third distinct instance today, and the first one where
the surviving copy is a **PROCESS** rather than a rule:

| # | Surviving copy | Kind | Found |
|---|---|---|---|
| 1 | `0.4.0_DS` prompt.md enforcing the lifted 49F scope hold | retracted PROHIBITION | `454c816ec` |
| 2 | `.tools/ajb.ps1` enforcing the deleted LD-0204 `/drive` carve-out | retracted PERMISSION | `6c7f4a83d` |
| 3 | `49-schwab-conv` SKILL.md encoding a superseded manual workflow | deprecated PROCESS | this record |
| — | `served-guard-49f-new-deploy` ledger gating on the lifted 49F prohibition | retracted PROHIBITION | surfaced `/drive` 16:00Z |

**A retracted rule is only as dead as its last-surviving copy — and a skill file is a copy that a HUMAN
TRIGGERS BY VOICE.** A reference census over code would have found this file and read it as *documentation*,
because that is what a `.md` looks like. It is not documentation; it is an executable procedure with an
Andrew-voice trigger.

## SCOPE — SURFACED, NOT ADJUDICATED (`org/XXX.md`)

Andrew's words are *"the whole process is automatic in the schwab box"*, which on its face retires the whole
7-step skill (sync + the six silver converters). **COO is NOT adjudicating** whether the box also owns steps
2–7 (ACC / RPS / TRN-A / TRN-NNA-B / ULN / RLD) or only step 1's sync. That boundary belongs to CTO + `0.5.0`
with the decommission arc.

**Care needed on one banked gotcha before anything is deleted:** `SKILL.md` records **RLD is NON-OPTIONAL**
(B_02 `canonical_lots` primary realized-lot tax source — omitting it *silently degrades gold*). If the box does
not perform the RLD leg, retiring the skill would drop it silently. **Retire the skill; do not assume the box
inherited every leg — verify leg-by-leg, on the box's actual output, before the file goes.** That verification
is the retirement's acceptance criterion.

## Actions

1. Recorded verbatim (this file), committed same turn.
2. Broadcast: CTO + MSTR + `0.5.0_AE_OpalETL` (owns the `opal-data-schwab` decommission census).
3. COO's own routing **corrected before it was sent** — the ask to `0.5.0` is **RETIRE**, never re-point.
