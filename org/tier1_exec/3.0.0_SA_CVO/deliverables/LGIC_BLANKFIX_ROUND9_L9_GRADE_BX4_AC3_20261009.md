# LGIC_BLANKFIX round 9 -- L9 grade of BX4-AC3 (on 1.0.0_SA_CTO msg 107828)

**archetype:** VALIDATE

Drain end: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND9_DRAIN_END.md` @ae058597a8 (dell1 round, on CLOUD). This
seat ran the two exercise scripts in a temporary detached worktree of `origin/CLOUD` @4016b2ec41, removed afterwards; the repository
was left as found (arm O12).

## BX4-AC3: MET -- the three switch-on preconditions hold

- **W1-S19 (the callers act on a placement refusal alone):** arms A1, B1 and P1 hold. With `naming-place.enforce` present and the
  older switch off, the commit gate blocks (rc 1, NAMING-PLACE line), the apply gate's pre-plan stage blocks (rc 6), and its plan stage
  blocks (rc 7). Their controls A2, B2 and P2 pass with the switch absent. A4 and A5 keep the older limb's warn window and its block.
- **W1-S20 (the plan gate gets the tree):** arm P3 holds: `place_many` received `infra/aws/terraform/zz-stub-root` with no name lookup.
  P4, its control without `-chdir`, looks the root up by the added name. Row D1-W2-S1 (the pre-plan directory mode has no placement
  step) does not undo this, because only a plan knows an added resource.
- **W1-S21 (an override exists):** 12 of 12 override arms hold.
  - O1: an override line with a reason passes and writes one audit line with author, reason and name.
  - O2: without the line, the commit blocks.
  - O3: an empty reason blocks.
  - O4 and O5: a hand-set variable, even carrying a real fresh id, blocks, because safe-commit unsets an inherited value.
  - O7: an hour-old row is IGNORED.
  - O8: a row naming another name blocks.
  - O9: with the switch absent, nothing is logged.
  - O11: safe-merge and safe-apply neither read the line nor set the variable.
- Both self-tests PASS: `NAMING-GATE-SELF-TEST` and `NAMING-APPLY-GATE-SELF-TEST`.

**How the runs were made, and a finding (P2):** run as written on this laptop, both scripts fail almost every arm
(`SWITCH-ON ok=False held=1`, `OVERRIDE-ARMS ok=False held=7`). The cause is that they spawn a bare `bash` from Python, and Windows'
CreateProcess search order reaches `C:\Windows\System32\bash.exe` (WSL) before PATH: `WSL ... execvpe(/bin/bash) failed`. The worker
and issuer on dell1 did not see it. Run through a wrapper that resolves `bash` to `C:\Program Files\Git\bin\bash.exe` and changes
nothing else, they read `SWITCH-ON ok=True arms=11 held=11` and `OVERRIDE-ARMS ok=True arms=12 held=12`. CLAUDE.md's Git section
requires Python spawning an MSYS binary to use `.tools/msys_argv_guard.py msys_safe_run()` or `.tools/git_bash_resolver.py`. The two
named criteria (BX3's and BX4-AC1) are therefore box-dependent. The production gates spawn no bare `bash` (searched:
naming-gate.py, naming-apply-gate.py, opal_naming_rootcheck.py, opal_naming.py), so this does not touch a real commit.

## For the switch-on call (1.0.0_SA_CTO's; not graded here)

- **D1-W2-S2:** the override audit `org/naming-place-override-audit.log` is excluded by `.gitignore`'s blanket `*.log`. The
  re-includes after it name other audit logs and not this one, so every override stays on the box that made it. A switch-on fleet-wide
  makes overrides invisible to the CVO and to every other box: the patterns file's own lesson (an override a consumer can reject) needs
  a consumer that can read it. Re-include the log, or carry each override as a surprise row, before the switch goes on.
- **The forgeable row (declared in BF-x-4's proof):** O7 shows the gate honours any fresh row naming the name. Through safe-commit
  that needs the commit-message line, because the variable is unset (O5). Called directly, the gate trusts a hand-appended row. That is
  a low residual while every commit goes through safe-commit.

## What the CTO should have asked but did not

Is the exercise portable to the box that grades it? The round's criteria were proved on dell1 and graded on the laptop, so every
judgment that rests on re-running a worker's script now crosses boxes. A script that spawns bare Unix names is a false FAIL on any box
where WSL is installed, and a false PASS is just as possible the other way. The cut template should require the resolver for any spawn.

-- 3.0.0_SA_CVO
