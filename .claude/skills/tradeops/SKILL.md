---
name: tradeops
description: Spawn ONE seat on the TRADEOPS fabric (docs_abcdeg, broker 7801, tradeops-agent-comms) with Remote Control on, drive it past the development-channels approval prompt that silently freezes autonomous spawns, and PROVE it registered. Use on `/tradeops <serial>`, "spawn a tradeops agent", or when an ajb3 launch produced a tab that never came up. Not for ajb_workspace seats -- those are /mstr-spawn.
---

# /tradeops — spawn a seat on the OTHER fabric, and prove it came up

**`/tradeops <serial>`** — e.g. `/tradeops 4.0.0_SA_CRO`, `/tradeops 1.1.0_SA_CTO`.

One act, three obligations: launch it the way `ajb3` would, add Remote Control, and **do not
report success until the seat has registered on the tradeops broker itself.**

## Why this exists rather than "just run ajb3"

`ajb3` is the tradeops fabric's customary launcher and is correct for a human at a keyboard.
Two things make it insufficient for an agent-driven spawn:

1. **It has no Remote Control switch.** `claude --remote-control [name]` is a real flag; `ajb3`
   does not pass it.
2. ⛔ **Its non-headless path raises a BLOCKING approval prompt, and the freeze is silent.**
   `--dangerously-load-development-channels` — which is how the seat gets
   `server:tradeops-agent-comms`, i.e. the thing that makes it reachable at all — opens with:

   ```
   WARNING: Loading development channels
   Channels: server:tradeops-agent-comms
   > 1. I am using this for local development
     2. Exit
   ```

   `ajb3`'s own source says so, in the `-Headless` switch comment. With nobody typing, the tab
   sits there forever.

> ### ⛔ THE LAUNCH IS NOT THE ORACLE, AND EVERY CHEAP SIGNAL LIES HERE.
> Measured 2026-09-11T21:44Z on the first `4.0.0_SA_CRO` spawn: `wt.exe` returned **exit 0**, the
> tab existed and was correctly titled, `claude.exe` (pid 32620) was **alive** with the exact
> intended command line — and the seat was **frozen at that prompt**, unregistered five minutes
> later. What exposed it was not any of those: it was **CPU flat at 2.7s across an 8-second
> sample** plus **no MCP server child process** plus **absence from the tradeops liveness store**.
> A launched-looking tab and a running process are fully consistent with a dead seat.
> **The only success signal this skill accepts is the serial appearing in the TRADEOPS broker's
> liveness store — a thing only the agent itself can cause.**

## Run it

```
powershell -NoProfile -ExecutionPolicy Bypass -File .tools\tradeops-spawn.ps1 -Serial <serial>
```

| flag | effect |
|---|---|
| *(none)* | launch, wait, auto-unstick once if it stalls, wait again, report |
| `-DryRun` | resolve + validate + print the exact command. Launches nothing. **Describes even when a real run would refuse.** |
| `-NoRemoteControl` | omit `--remote-control` |
| `-TimeoutSec N` | total wait for registration (default 180; the auto-unstick fires at one third) |
| `-Force` | spawn even though that serial already reads live — an accepted identity conflict, printed as such |

**Exit codes: 0 registered · 2 preconditions unmet / launch failed · 3 launched but never
registered · 4 refused, serial already live.**

⛔ **rc=3 IS NOT rc=0 AND MUST NOT BE REPORTED AS ONE.** It means a tab exists and a seat does
not. The script prints a peek PNG path when it has one — **read that image**; it shows what the
tab is actually sitting on, which may be a prompt of a shape this skill has never seen.

## What the engine does, in order

1. **Root.** `OPAL_TRADEOPS_ROOT` if set and real, else the standard clone
   `C:\Users\AndrewBerman\Downloads\docs_abcdeg`. Neither present is a hard stop, never a guess.
   *(That directory **is** the tradeops repo root — `ajb3.ps1` derives it from its own location at
   `entry\windows\`. "In docs_abcdeg" and "on the tradeops repo" name the same place.)*
2. **Drift check against the real `ajb3.ps1`.** This engine MIRRORS ajb3's flag set, and a mirror
   held true only by a comment goes stale silently, so it asserts the four mirrored strings are
   still in ajb3's source and WARNS by name if any vanished. **A warning, never a block** — ajb3
   changing is not a reason to refuse a spawn, but it is a reason to go read it.
3. **Serial validity.** `.tools/launch-directive.py --role <serial>` in the tradeops repo must
   succeed **and must not report the serial as unrecognised**.
   ⛔ **THOSE ARE TWO DIFFERENT CHECKS AND THE FIRST ONE ALONE IS USELESS HERE.** That tool
   returns **exit 0** for a serial it does not recognise, saying so only in its text:
   `UNRECOGNIZED ('<serial>' matched no role pattern)`. The first version of this engine checked
   the exit code and called itself fail-closed; `9.9.9_XX_NotAThing` passed it and would have
   opened a tab for a seat with no role. Caught 2026-09-11 by running the negative case rather
   than by reading the code.
   ⚠ So this check **parses the tool's prose** and inherits every future edit to that string —
   a worse instrument than an exit code, used only because the tool emits nothing better. If the
   marker is ever renamed, the check silently stops catching. `-Force` overrides it deliberately.
4. **Duplicate guard.** If the serial is already in the tradeops liveness store **and its pid is
   alive**, refuse with rc=4. Two live sessions under one serial is an identity conflict and the
   loser is silent. A stale row whose pid is gone is not a blocker and says so.
5. **Launch** in a `wt` tab **titled with the serial**, via a generated runner script so nothing
   has to survive `wt`'s quoting layers. Same cwd, same env
   (`OPAL_BROKER_PORT=7801`, `OPAL_AGENT_SERIAL`, `OPAL_TRADEOPS_ROOT`, `AJB3_NO_WT_RELAUNCH`),
   same first message as `ajb3` — serial, the `/watcher` directive, then the role directive pulled
   live from `launch-directive.py` rather than copied.
6. **Wait for registration.** At one third of the timeout, if still unregistered, **peek** (saving
   a PNG) and then send `1{ENTER}` via `.tools/unstick.ps1`. Then keep waiting.
7. **Report** from the liveness store, not from the launch.

## The auto-unstick, and why it is safe here

`/unstick` is normally **operator-initiated** because it steals desktop focus for a few seconds
and, aimed at a healthy seat, types a stray character into its composer. Two things make it safe
as an automatic step in this one flow, and both must hold:

- **It only ever fires at a seat that has NOT registered.** A healthy seat registers and the
  script exits before the unstick branch is reachable.
- **The prompt shape is known in advance**, because this script is what caused it. `/unstick`'s
  own rule is *peek before keying when the shape is unknown* — here it is known, and the engine
  peeks anyway so a human has the image if `1{ENTER}` turns out to be the wrong answer.

Andrew commissioned this composition directly (2026-09-11): *"make a skill called /tradeops which
does this exact process including the /unstick"*.

⛔ **The tab MUST be titled with the serial or `/unstick` cannot find it** — Windows Terminal pins
titles at tab creation. The engine always titles it; do not launch tradeops seats any other way if
you want this to work.

## Scope

- **ONE seat per invocation.** No fan-out.
- **TRADEOPS ONLY.** ajb_workspace seats are `/mstr-spawn`; the two fabrics have separate brokers
  (7801 vs 7800) and **their seats cannot message each other** — a tradeops seat is unreachable
  from an ajb_workspace inbox and vice versa. Cross-fabric traffic is the two MSTRs over the agent
  bus.
- **This skill writes NOTHING into the tradeops repo** and creates no commit or worktree there. It
  reads `ajb3.ps1`, `launch-directive.py` and `liveness.json`, and launches a process.
- Spawning is infra-class population, which is `0.0.0_AB_MSTR`'s primitive (cross-fabric seats
  explicitly). Another seat wanting a tradeops agent asks MSTR.

## Coverage, stated honestly

Exercised 2026-09-11, each arm run rather than reasoned about:

| arm | result |
|---|---|
| root resolution + drift check | 4 of 4 mirrored strings present |
| real serial (positive control) | rc=0, directive resolved |
| unrecognised serial (negative) | rc=2, refused |
| `-Force` on an unrecognised serial | rc=0, override works |
| already-live serial, real run | rc=4, duplicate guard |
| dry run on an already-live serial | rc=0, describes instead of refusing |

**The negative arm is why this table exists.** Before it was run, the unrecognised-serial case
returned rc=0 and this document claimed the opposite — the check could not fail, and only running
it said so. A positive control alone would have shown green throughout.

The
**launch → stall → peek → `1{ENTER}` → registered** sequence was exercised **by hand** on
`4.0.0_SA_CRO` (registered pid 33724 at 02:03:48Z) — the engine automates exactly that sequence
but has **not itself been run through a live stall yet**. First real invocation is also its first
end-to-end test; treat an rc=3 as informative rather than surprising.

## Engine

`.tools/tradeops-spawn.ps1` — the only mechanism. `.tools/unstick.ps1` is called for the peek and
the keystroke. `ajb3` itself is never invoked (it has no Remote Control switch); its logic is
mirrored, and step 2 is what keeps the mirror honest.
