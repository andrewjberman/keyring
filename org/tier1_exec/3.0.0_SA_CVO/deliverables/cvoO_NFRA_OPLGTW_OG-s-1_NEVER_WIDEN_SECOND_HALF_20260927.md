# OG-s-1 -- never-widen sign-off, SECOND (non-acting) half: SIGNED

Signer: `3.0.0_SA_CVO~O`, OPLGTW's CVO leg and a non-acting seat. Recorded 2026-09-27; clock read ~21:3xZ.
Ask: `2.0.0_SA_COO~O` file `20260927T212047Z_2.0.0_SA_COO_O_OG-s-1_never-widen_second_half_asked.md`.
Word: Andrew-direct @785fc4d71f, "/sprint for Andrew only". Order `NFRA_OPLGTW.TO-OG-s-1.sprint-owner-only` @95e499c916;
PHASE A announce drained @ce32a3ddef.

**The act this half covers, and nothing wider:** release `6a98a0553a`, which is the live `fe94911257` plus
`deploy-to-ec2.sh` only. It narrows `/sprint*` from every signed-in tenant account to the owner.

## Re-read by this seat

| claim | this seat's read | holds |
|---|---|---|
| the live base is fe94911257 | S3 `latest` ETag d67a7435 = the fe94911257 artifact | yes |
| one file changes | `git diff --stat fe94911257 6a98a0553a -- infra/aws/ec2/opal-gateway`: deploy-to-ec2.sh only, +2/-1 | yes |
| one `.env` key changes | parsed the printf literal at both commits: 27 -> 28 entries, 9 -> 9 `%s` placeholders; key added `SPRINT_VIEW_ALLOWED_EMAILS`, none removed, no other value changed (ENABLED_INTEGRATIONS included) | yes |
| the roster is the owner | its single entry (an `@opalinvest.com` address) equals `OTP_MAILBOX`, `MASTER_ADMIN_EMAILS` and `DASHBOARD_OWNER_EMAILS` in the same literal. The value was compared, not printed. | yes |

## Readers of the key (the count this seat owes since OA-g-2)

`git grep` at fe94911257 over `app/` finds 2 readers: `config.py:103-104`, which parses it lower-cased and stripped
into a frozenset, and `sprint_view._allowed` (`:173-175`). `_allowed` is called by `sprint_page` (`:182`) and
`sprint_archive` (`:222`), the two data handlers of `/sprint*`. `sprint_redirect` serves no data. `/login`, `/mcp` and
every other route never read the key. So the narrowing is exactly `/sprint*`, which is Andrew's verbatim scope.

## Both branches (from `_allowed`: an empty roster admits all, otherwise membership)

- **The owner:** admitted. Every identity provider lower-cases and strips the email (`identity.py:26, :66, :122, :130,
  :138` at fe94911257), and the roster is lower-cased, so the claim's case cannot lock him out.
- **Every other signed-in tenant account:** 403 "Not on the Daily Sprint roster" on `/sprint`, `/sprint/` and the day
  and archive pages, audited as DENIED. This is the deliberate narrowing on Andrew's word.

## The `.env` rewrite (the MX-r-3 condition, restated)

The deploy rewrites the whole host `.env` from the literal. The announce's GO step 1 (`:111-115`) reads, before the
act, the tool list (46), `ENABLED_INTEGRATIONS` (the literal) and the `SPRINT_VIEW_ALLOWED_EMAILS` count (0). A mismatch
there is a STOP.

## Rollback, per key

`opal-gateway-fe94911257.tar.gz` (79 of 79 files identical to live, per the announce), redeployed through the same
wrapper. Its literal carries no roster, so `/sprint` returns to tenant-wide. No data is written.

## Verdict

**SIGNED** for the act above as bounded here. No condition is added beyond the order's own GO steps.

-- 3.0.0_SA_CVO~O
