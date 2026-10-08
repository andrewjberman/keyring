# ANDREW_DIRECT 2026-10-08 ~16:4xZ -- the reaper may run unattended once session shells are reliably assigned

**Channel:** laptop terminal, to 4.0.0_SA_CRO~B, in answer to the GC audit's open call "may the reaper run `go`
unattended" (`docs/briefs/process-gc-long-term-script-audit-20261008.md` section 3).
**Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

> "I dont mind if the killer runs unattended as long as there is a clear mechanism of assigning PIDs to Claude Code and
> Codex session shells. Those should never be killed by these kind of operations, everything else i dont care about
> as much."

Same session, minutes later (~16:4xZ), verbatim:

> "I need you to lead the development of this function as we dont have time to really hand it off to a whole
> canonical-flow project registration, this should be fairly fast to get through, lets get through it, ask me any
> questions you need in /open-calls format as you go and we'll figure out how to integrate it across the fabric as we
> go."

## Placement

- **Condition for unattended runs:** the reaper (`.tools/kill-maint.ps1`) can name, for every live Claude Code session
  and every live Codex session, the PIDs that make up its session shell. It never targets any of them.
- **Everything else** (orphans, replaced copies, leaked natives) is lower stakes on Andrew's word.
- **Lane:** 4.0.0_SA_CRO~B LEADS the build directly (no canonical-flow registration, on the second quote), asking
  Andrew in open-calls form as it goes. 0.0.0_AB_MSTR lands the commits on the shared branch. The rollout across boxes
  is worked out with Andrew as it goes.
