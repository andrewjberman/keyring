# ANDREW-DIRECT 2026-10-06 ~18:1xZ -- "recs approved" on the three /open-calls cards of 2.0.0_SA_COO~D

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 83c2c1d1-733c-4463-b47c-1dc1b819822e), typed by Andrew
  in direct reply to this seat's `/open-calls` (~18:05Z).
- **Recorded by:** `2.0.0_SA_COO~D`, same turn.

## Verbatim

"recs approved"

## The three recommendations it approves (as printed on the cards)

1. **DEV push, yes.** One push by `0.0.0_AB_MSTR~Z` of DSGN_AMGTV1 rounds 43+44 (portal `1d6d2573`, branch
   `dsgn-r4344-onto-dev` in `C:/tmp/wk-dsgn-amgtv1-92/portal`) TOGETHER WITH the AMGT_RESAPP `/freshness` candidate
   (portal `6de76f05`). CTO approvals: @0c9b9db840 (msg 29936) and @7c328eb0df. `git merge-tree` of `1d6d2573` against
   origin/DEV `84ca4161` read CLEAN at ~18:0xZ. After the push, `2.0.0_SA_COO~D` re-runs the r43/r44 checks on DEV and
   does the live read.
2. **PROD promote of rounds 43+44, yes, GATED on that post-push DEV live read passing.** PROD today is v2.1.200 =
   `ce6f0721` (rounds 34-42).
3. **/prod-deploy rule, yes.** A job no runner picks up gets ONE re-run, then a rollback and escalation. Landed in
   `.claude/skills/prod-deploy/SKILL.md` Step 5, with the Abort path pointing to it.

## Scope, as written and no wider

- Card 2's word covers the PROD promote of the DEV state that passed the post-push read. A DEV state with other content
  is not covered.
- The `ACTS ONLY ANDREW CAN DO` line (GitHub Actions billing / spending-limit check) was not a card. This word does not
  perform it.
- Round 45 still waits on AMGT_RESAPP round 76 being deployed (`2.0.0_SA_COO~Z`). This word does not decide it.
