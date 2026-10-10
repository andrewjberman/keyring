# ANDREW-DIRECT 2026-10-10 ~23:3xZ -- slower pacing: drive/self-drive/govern loops at 60m, /keep-driving OFF

**Channel:** Claude Code terminal, laptop, to 1.0.0_SA_CTO. Two consecutive messages, both verbatim.

> yeah we need slower pacing, i think canonical drive and self drive loops can be on 60m interval and /keep-driving OFF
> for now, no need to be so aggressive. This is to avoid the usage limit and try to scale productivity correctly.

> in govern loop too

**Scope as given:**
- `/canonical-drive` loops: 60m.
- `/self-drive` loops: 60m.
- `/govern` loops: 60m.
- `/keep-driving`: OFF, both parts, every box.
- Purpose: avoid the usage limit; scale productivity correctly.

**This record is the law-edit order** (`ANDREW_LAW_EDIT_ORDER`) for the `org/XXX.md` Step 1b-F rows that carry these
cadences: MSTR `/govern 30m` and COO `/drive` v2 standing 20m. Both become 60m. Nothing else in XXX.md is edited.

**Supersedes the cadence parts of:**
- `ANDREW_DIRECT_20261008_174xZ_MSTR_GOVERN_30M_LOOP_AT_INSTANTIATION.md`: the 30m.
- LD-0530: the 20m.
- the canonical-drive skill's 10m / 20m tiers.
- the self-drive skill's 30m default.
- the live 30m arms in `org/ref/LIVE_ARMS.md`.

The loops themselves stay; only their interval changes.

**Carriers:**
- Skills: `.claude/skills/canonical-drive`, `.claude/skills/self-drive`, `.claude/skills/govern`.
- `org/XXX.md` 1b-F.
- `org/ref/LIVE_ARMS.md`.
- The cloud switch: `python .tools/open-calls.py mode set --state off`.
- Live crons re-armed by each owning seat at 60m, relayed by `0.0.0_AB_MSTR` to every box.
