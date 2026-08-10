# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-10 1638–1655Z
**Archetype:** build/fix (P0)
**Project:** OPAL_ANALYST — TO-1 durable identity pin in teams-watch.py
**Commit:** `0f1bbcf0e` (SITEZ, own lane, NOT pushed per LD-0367)

## Summary
OPAL_ANALYST.TO1 executed to completion on COO~Z GO (inbox 20260810T163702Z). The shared
`/teams-assist` monitor engine `.claude/skills/teams-assist/teams-watch.py` now takes an
additive `--server <substring>` / `--identity <sub/UPN substring>` pin that filters
`mcpOAuth` records BEFORE the freshest-expiring sort; no-match / expired-only / ambiguous
all die loudly (`[TEAMS-IDENTITY-FAIL]` on stdout + exit 2), never a fallback. Bare
invocation keeps the legacy selection path unchanged (operator compatibility). The
`/bbg-teams-assist` SKILL.md canonical arm line now passes the pin
(`--server opal-gateway-bbg --identity opalbloomberg`); wrapper references removed
(scratch-wrapper pattern dead by design per the TO).

## Ground-truth notes
- Live `~/.claude/.credentials.json` on this box: 4 opalinvest.dev records; VALID =
  `opal-gateway` (andrew@opalinvest.com) + `opal-gateway-bbg` (opalbloomberg@opalinvest.com);
  EXPIRED = `m365`, `opal` (both andrew@). Exactly the dual-valid race the TO names.
- Bare selection TODAY picks opalbloomberg@ (its token currently expires later) — the race
  winner flips with refresh order, which is why the discriminating positive control below
  pins to the identity bare would NOT need to pick (`--identity andrew` → andrew@ selected).
- Pre-existing environment quirk (NOT introduced, NOT fixed — out of scope): under native
  Windows python with no TMPDIR, the cursor default `/tmp/teams-watch.cursor` is unwritable
  (FileNotFoundError). All exercised runs below set TMPDIR. Flagged for TO-2 runbook
  consideration (the concierge box arm procedure should carry a valid TMPDIR).

## Compiler Tools (every TO `<run>`, observed output vs `<expect>`)

| Phase | Run | Observed | Verdict |
|---|---|---|---|
| 1 | `.tools/comp-find "teams-watch"` | DENOMINATOR: 121 hits / 24506 files scanned (3 UNREADABLE). Engine at `.claude/skills/teams-assist/teams-watch.py` [HEAD]; gateway `/teams/poll` at `infra/aws/ec2/m365-mcp-gateway/app/server.py:579` [SURFACED]; consumers = /teams-assist (SKILL.md:128 — monitor model retired for that skill, engine left in place, bare compat still binding) + /bbg-teams-assist (arm via prompt.md On-Launch step 3 / TEAMS_DUTY.md). No new consumer. | PASS (consumer set unchanged vs PRD §5.2) |
| 2 | `python .claude/skills/teams-assist/teams-watch.py --once` (bare) | rc=0; `token selected: identity=opalbloomberg@opalinvest.com` (freshest-expiring across all records — legacy path code-untouched; selection recorded) | PASS (bare behavior preserved; selection recorded) |
| 2 | `... --once --identity opalbloomberg` | rc=0; `token selected: identity=opalbloomberg@opalinvest.com`, both identities' tokens valid on box | PASS |
| 2 | commit-gate via safe-commit | py_compile + ruff PASS; commit `0f1bbcf0e` landed (risk-reflex warnings surfaced + citations read; non-blocking) | PASS |
| 3 | NEGATIVE control: `... --once --identity no-such-identity-xyz` (separate invocation, post-commit) | `[TEAMS-IDENTITY-FAIL] no-token-for-identity: no mcpOAuth record matches the pin (--server=None --identity=no-such-identity-xyz)`; rc=2; NO fallback selection, no poll occurred | PASS |
| 3 | POSITIVE control: `... --once --server opal-gateway-bbg --identity opalbloomberg` ×3 consecutive (post-commit) | 3/3: `token selected: identity=opalbloomberg@opalinvest.com`, rc=0 | PASS |
| extra | expired-only: `--server m365` | `expired-token-for-identity: 1 matching record(s), all expired`; rc=2 | PASS (PRD §4.1 error case) |
| extra | ambiguous: `--server opal-gateway` (substring matches both valid records) | `ambiguous-token-match: 2 valid records match the pin (opal-gateway, opal-gateway-bbg)`; rc=2 — never sort-and-hope | PASS (PRD §4.1 error case) |
| extra | discriminating positive: `--identity andrew` | rc=0; `token selected: identity=andrew@opalinvest.com` — the pin drives selection, not the expiry sort | PASS |

## Acceptance criteria
1. Pinned selection == pinned identity 3/3 with both identities valid — MET (above).
2. No-match / expired-only / ambiguous exit non-zero with named reasons — MET (rc=2, all three exercised).
3. Bare invocation selection path byte-untouched; behavior recorded — MET.
4. `/bbg-teams-assist` SKILL.md arm line passes the pin — MET (`0f1bbcf0e`).
5. This Compiler Tools section — MET.
6. safe-commit under own author line, no push — MET (`0f1bbcf0e`, SITEZ lane, unpushed).

## Blockers
None.

## Next steps
- [2.0.0_SA_COO~Z] TO-1 completion reported (commit + exercised outputs); TO-2 GO is COO's call.
- [0.5.0_AE_OpalETL~Z] TO-2 (relaunch runbook) STAGED — not begun, per GO. TMPDIR quirk noted above for the runbook.
