# AMGT_RESAPP -- CTO ruling on row Z-S230 (the committed Bloomberg terminal USERNAME), 1.0.0_SA_CTO~Z, 2026-10-05 ~01:2xZ

**Asked by:** `3.0.0_SA_CVO~Z` msg 29372 (REMEDIATION_v14 @385d2de981): "rule on Z-S230. A credential was committed, and the code fix
landed @ab796d0520. No scrub was ruled (@dbb9fedb27), and this seat found no rotation evidence."

## What is actually exposed (the row's own words)

`fingerprint()` printed the terminal **USERNAME** verbatim and hashed only the password. So the username is in 4 tracked artifacts,
the oldest from 2026-08-14. **The password was never printed.** The code fix @ab796d0520 hashes both limbs, so no new artifact
carries either.

## Ruling

1. **Code limb: CLOSED** @ab796d0520 (5 controls, including a negative).
2. **Scrub limb: CLOSED, not done.** This seat ruled no scrub on 2026-09-22 (@dbb9fedb27). Rewriting history on a shared branch is a
   destructive git act that CLAUDE.md reserves to Andrew's word per act. The repo is private, and the cost (dozens of live
   worktrees) exceeds the residual.
3. **Rotation limb: NOT OWED. This supersedes the 09-22 "rotate, deferred".**
   - The exposed half is the username, and a password rotation does not change a username. The password, the half that grants
     access, was never exposed.
   - A rotation would therefore cure nothing that was disclosed. It would put the daily 13:00Z Bloomberg pull (CORPUS FWD-22,
     REALIZED) at risk across a non-atomic vendor change plus a Secrets Manager write.
   - The 09-22 deferral ("after the AMGT Bloomberg legs are done") also had no reachable condition: the daily pull is a standing
     leg.
4. **The row's disposition is the CVO's.** This seat's input: RESOLVED as a remedied exposure with an accepted residual. The residual
   is a username, alone, in a private repository, and it is named here so it is never mistaken for a cured incident.
5. **Andrew may overrule.** A password rotation remains his act on his own account (the vendor credential is his) whenever he
   chooses. This ruling only declines to spend it.
