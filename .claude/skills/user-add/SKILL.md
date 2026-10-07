---
name: user-add
description: Add one user to the Opal portal for a partner firm (Cottonwood, 49 Financial, Inflection): the three rows in the login tables, a temporary password, a read-back, and an Outlook DRAFT for Andrew with the username and password. Use when Andrew asks to add, onboard or give portal access to a person at a firm.
---

# /user-add -- add one portal user for a partner firm

**Authority (Andrew-direct 2026-10-07 ~16:1xZ, `1.0.0_SA_CTO` terminal, VERBATIM):** *"We should have a skill for this that will do
the whole process per firm (currently Cottonwood, 49 Financial, and Inflection), with references to the relevant tables,
structures, and Opal Login Flow and relevant prior user management art."* First run: Kenneth Cusick at Cottonwood, same day.

## Invocation

`/user-add <firm> <email> "<Full Name>" [admin]` -- firm is `cottonwood`, `49financial` or `inflection`. Anything missing is asked
of Andrew once, never guessed (a 49 Financial or Inflection ADVISOR also needs the advisor fields below).

## Hard rules

- **Only on Andrew's word naming the person.** A login is an entitlement; record his words verbatim first.
- **No email is sent by an agent.** The result goes to Andrew as an Outlook DRAFT (`create_draft`), never `send_email`.
- **The password is generated, shown once, and written to no committed file, log or broker message.** It appears in the draft
  and in the reply to Andrew, nowhere else.
- **One writer: `users/scripts/create_user_v2.py`.** Never hand-write a row with `put-item`. `users/scripts/create_user.py` is
  deprecated.
- A firm not in the script's `FIRMS` table is refused by the script. Adding a firm is a separate change, not this skill.

## The tables and their structures (us-east-1)

| Table | Row | Fields the script writes |
|---|---|---|
| `opal-users-v2` | `PK=USER#<email>`, `SK=PROFILE` | `email, firmId, name, role (user or admin), tier, status=active, mustChangePassword=true, passwordHash (bcrypt), mfaEnabled=false, mfaChannel=none, createdAt, updatedAt, passwordChangedAt, createdBy` |
| `opal-users-v2` | `PK=FIRM#<firmId>`, `SK=MEMBER#<email>` | `userId=<email>, role, joinedAt` |
| `opal-partner-cottonwood` | `email` (key) | `firmRole, createdAt, updatedAt, createdBy` |
| `opal-partner-49financial`, `opal-partner-inflection` | `email` (key) | the same, plus `advisorRole, advisorName, advisorKey` for an advisor |

Indexes on `opal-users-v2`: `email-index` (email; projects keys only, so follow with `get-item`) and `firmId-index` (firmId, PK).
The firm's own row is `PK=FIRM#<firmId>`, `SK=META` (domain, bucket, tier).

**The table names are singular: `opal-partner-<firm>`.** A request that says `opal-partners-<firm>` means these.

| Firm | `firmId` | Email domain the script enforces | Partner table | Advisor fields |
|---|---|---|---|---|
| Cottonwood | `cottonwood` | `cottonwoodmail.com` | `opal-partner-cottonwood` | no |
| 49 Financial | `49financial` | `49financial.com` | `opal-partner-49financial` | yes |
| Inflection | `inflection` | `inflectionwealth.com` | `opal-partner-inflection` | yes |

Read the live values from `FIRMS` in the script before relying on this table; the script is the authority.

## The login flow, in the order a new user meets it

1. The **username is the email address** (the token's `sub`).
2. First sign-in with the temporary password; `mustChangePassword=true` forces a new password, and the temporary one stops working.
3. MFA is the user's own opt-in afterwards (the auth handler overwrites `mfaEnabled` and `mfaChannel`); the script writes it off.
4. The token carries `sub, name, tier, role, firmId`; the firm's partner-table row decides what the firm's pages show.

References: `infra/aws/auth/ARCHITECTURE.md` (FILE), `infra/aws/auth/validator.py` (FILE).

## Procedure

1. **Record** Andrew's words in a committed file under the running seat's `deliverables/`.
2. **Read first, write nothing:**
   - the person is absent: `aws dynamodb query --table-name opal-users-v2 --index-name email-index` on the email returns `Count 0`
     (if not, STOP and tell Andrew; never `--force` without his word);
   - one existing user of the same firm, as the shape to match (redact `passwordHash` in any output);
   - the partner table's row count, as the before number.
3. **Create:** from the repo root,
   `python .claude/skills/user-add/add_user.py <firm> <email> "<Full Name>"` (add `--role admin` or the three `--advisor-*`
   flags when Andrew named them). It calls the canonical script with `--no-ses` and prints `USERNAME=` and `TEMP_PASSWORD=`.
4. **Read back, with a control:** `get-item` the PROFILE, the MEMBER row and the partner row; check the printed password against
   the stored hash with `bcrypt.checkpw` (expect True) and a wrong string (expect False); the partner table's count is before + 1.
5. **Draft:** `create_draft` to the new user, cc whoever asked Andrew for the access, replying on that thread's subject, in
   Andrew's voice: the username, the temporary password, that a new password is chosen at first sign-in. Put the portal address
   in only if it is read from a source that states it; otherwise leave a bracketed line for Andrew to fill.
6. **Report to Andrew:** username, temporary password, the three rows written, where the draft is, and anything not done.

## Known gaps (state them in the report until fixed)

- The script stamps `createdBy` as `0.7.0_AE_CloudOps@opal.agent` whoever runs it. The record of who ran it is the Andrew-direct
  file of step 1.
- The script writes `name` and not `firstName` / `lastName`, which older rows carry (`users/scripts/backfill_user_names.py`
  exists for that). Check whether the portal greets by first name before calling a new row complete.
- Without `--no-ses` the script asks AWS to email the new user a verification link. The mail service is in production mode
  and existing users sign in with that verification never completed, so the skill always passes `--no-ses`.

## Prior art

- `users/scripts/create_user_v2.py` -- the canonical writer and its header contract.
- `users/scripts/partners/README.md`, `partner_contracts.py`, `provision_cottonwood.py`, `provision_49financial.py`,
  `provision_inflection.py` -- per-firm provisioning and the partner-table contracts.
- `docs/reference/user-provisioning-firm-scope-profiles-20260528.md` -- the live reads the firm profiles were built from.
- `infra/aws/auth/migration/` -- how the user table reached its current shape.
