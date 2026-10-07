# ANDREW-DIRECT 2026-10-07 ~15:5xZ (1.0.0_SA_CTO terminal) -- add a new Cottonwood client user, Kenneth Cusick

## His words, VERBATIM AND ENTIRE

> "By the way, we need to make an addition of a new Cottonwood client, "Kenneth Cusick" at kenny.cusick@cottonwoodmail.com. He should be added to the opal-users-v2 table as well as to the opal-partners-cottonwood table. Please ping me back with his username and a temporary password, i recommend it being a draft in outlook (see the email from christa.bass@cottonwoodmail.com)."

## Scope, as written

- WHO: Kenneth Cusick, kenny.cusick@cottonwoodmail.com, firm Cottonwood.
- WHAT: one row in `opal-users-v2` and one in `opal-partners-cottonwood`.
- BACK TO HIM: the username and a temporary password; he recommends an Outlook DRAFT (not a sent mail), and points at an email
  from christa.bass@cottonwoodmail.com as the reference.
- NOT said: his role or permissions beyond "client"; that anything is sent to Kenneth or to Christa by an agent.

## A second word, ~16:1xZ, same terminal, VERBATIM

> "We should have a skill for this that will do the whole process per firm (currently Cottonwood, 49 Financial, and Inflection), with references to the relevant tables, structures, and Opal Login Flow and relevant prior user management art."

## What was done (2026-10-07 16:15Z to 16:2xZ)

- The table he called `opal-partners-cottonwood` is `opal-partner-cottonwood` (singular) in the account; that is the one written.
- Before: `email-index` query for the address returned Count 0; the partner table held 4 rows.
- Written by the canonical script `users/scripts/create_user_v2.py` with `--no-ses` (no email sent to anyone), role `user`:
  `opal-users-v2` `USER#kenny.cusick@cottonwoodmail.com / PROFILE` (firmId cottonwood, tier advisor, status active,
  mustChangePassword true), `FIRM#cottonwood / MEMBER#kenny.cusick@cottonwoodmail.com`, and the `opal-partner-cottonwood` row
  (firmRole user). Read back by get-item, all three present; the partner table holds 5 rows.
- The temporary password was generated, checked against the stored hash (True; a wrong string False), and is NOT in this file.
  It is in the Outlook draft and in the reply to Andrew.
- Outlook DRAFT created, not sent: subject "RE: Opal Platform Access", to kenny.cusick@cottonwoodmail.com, cc
  christa.bass@cottonwoodmail.com. The portal address is left as a bracketed line for Andrew.
- Role read as `user`, the role of the three real Cottonwood people already there. The row's `createdBy` reads
  `0.7.0_AE_CloudOps@opal.agent` because the script hardcodes it; this seat ran it.
- The skill: `.claude/skills/user-add/SKILL.md` and `add_user.py`.
