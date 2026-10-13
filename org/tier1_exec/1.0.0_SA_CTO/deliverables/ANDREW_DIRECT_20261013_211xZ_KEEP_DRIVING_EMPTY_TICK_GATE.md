# Andrew-direct 2026-10-13 ~21:1xZ (laptop, 1.0.0_SA_CTO terminal) -- the keep-driving empty-tick rule becomes a Stop-hook gate

## VERBATIM

> "I want you to note the following, it is unclear if the agents are actually following the /keep-scanning ON rules, is there any
> way to gate this and make sure it is actually done as intended? Look at the case study below in the context of the COO~C on this
> box: [2.0.0_SA_COO~C's /canonical-drive tick: 'Tick done ... I nudged no one, since nothing is silent.' Asked 'Did you run
> /next-calls as you were supposed to?', it answered: 'No, I didn't ... I logged it as "drive forward", but with no act of my own to
> fire that was effectively an empty tick. With /keep-driving ON, the rule for that case is /next-calls NFRA_CTLPLN --drive.']"

Then, on the proposal: "Yeah get it incorporated"

## Applied

- **Gate:** `.tools/hooks/coo-drive-tick-gate.py`, wired as a `Stop` hook in `.claude/settings.json`.
  - It applies only to a `2.0.0_SA_COO*` session whose turn ran `/canonical-drive`. It reads the turn's own tool calls from the
    transcript, never the seat's label.
  - A turn that fired no act counts as an EMPTY tick. Acts are a spawn, an order or merge commit (a log-only commit is not one), a
    send, a crossbox order or an apply.
  - With the `/keep-driving` empty_tick switch ON, an empty tick must also have run `/next-calls <CODE> --drive` and
    `unblock.py tick`. Otherwise the hook blocks the stop and names the commands.
  - It blocks once per turn (`stop_hook_active`), and it fails open on its own errors.
- **Proof:**
  - The case-study tick (2.0.0_SA_COO~C, 2026-10-13 21:07:58Z, transcript f2c03cf8) replays to BLOCK end to end, with the live
    switch read.
  - The same seat's startup tick, which fired acts, passes. Non-COO seats and non-drive turns pass.
  - `.tools/hooks/test_coo_drive_tick_gate.py` passes 5 of 5: the case study, a log-only commit, fired acts, a rule run,
    non-application.
- **Skill:** `.claude/skills/canonical-drive/SKILL.md` section 3's hard gate now names its mechanism.
- **Reach:** every COO on every box, once box-sync carries `.claude/settings.json`. A session picks up hook settings at its next
  start or settings reload.
