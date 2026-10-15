# Andrew-direct 2026-10-15 ~02:0xZ-02:1xZ (laptop, 1.0.0_SA_CTO terminal) -- /keep-driving ON, hourly loops, each MSTR enforces

## VERBATIM

> "issue /keep-driving ON notification across all boxes, 1hr loops for /self-drive, /canonical-drive, and /govern."

> "yeah need MSTR on each box to enforce this across all active agents who run these loops"

## Applied

- **The switch:** `python .tools/open-calls.py mode set --part all --state on`, by `1.0.0_SA_CTO` at 2026-10-15T02:10:00Z, with
  his words as the reason. The read-back: `scan=on empty_tick=on overrides=[none]` on all four boxes (laptop, sitez, dell1,
  dell2). It was already ON since 2026-10-13T20:34Z; this re-set records his newer word.
- **The loops, every 60 minutes:**
  - each box's CTO runs `/self-drive` over all of that box's open calls;
  - each live COO runs `/canonical-drive` on its project;
  - each MSTR runs `/govern`.
- **Enforcement (his second message):** at every `/govern` cycle, each box's MSTR:
  - lists the box's live CTO, COO and MSTR seats;
  - reads whether each has its loop armed;
  - arms any that is not, per `/unstick` (peek first, key only at a prompt);
  - reports `armed N of M` per box.
- **The laptop at the order:** `1.0.0_SA_CTO` is armed (cron 6ca5a587, hourly). `2.0.0_SA_COO~C` and `2.0.0_SA_COO~CA` are live,
  and MSTR reads their loops.
- **Broadcast:** to `0.0.0_AB_MSTR` for relay, verbatim, to `0.0.0_AB_MSTR~DELL1`, `~DELL2` and `~Z` (msgs at 02:10Z and
  02:1xZ).
