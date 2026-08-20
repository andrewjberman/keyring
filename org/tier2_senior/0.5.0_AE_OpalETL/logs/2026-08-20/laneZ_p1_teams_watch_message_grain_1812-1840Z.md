# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 1812–1840Z

**archetype:** IMPLEMENT
**Project:** OPAL_ANALYST sec11 addendum — S1 (P1 teams-watch message-grain fix, post-close defect item)

## Summary

Landed the P1 Andrew-facing message-loss fix @7e138ad6ef — `.claude/skills/teams-assist/teams-watch.py`
ONLY, one change one commit, CTO~Z ruling msg 2571 (BG's msg-2567 spec adopted verbatim) implemented
inside the fence: the poll is the CHANGE SIGNAL (touched chat ids only), `read_chat_messages` per
touched chat is the INTAKE (bounded top=25, every message strictly newer than the cursor, oldest-first,
normalized to the poll's flat shape so `is_outgoing` and the emit line are untouched), and the cursor
advances on MESSAGE timestamp — max PROCESSED, parsed-not-lexical, one write per cycle AFTER the emits.
TO6 pin/backoff mechanics byte-untouched (ruling 4). Gateway untouched — `read_chat_messages` was
already on the BG identity allowlist (`identity_scope.py:51`), so no permission act.

**Design points inside the fence, named to the gate (msg 2592):**
- Cursor = max **processed** (emitted OR deliberately-skipped outgoing), not max *emitted* — an
  outgoing-only advance is required or my own reply leaves the chat perma-touched (one extra read per
  cycle forever). The ruling's safety property — never advance past an UNEMITTED INCOMING — holds by
  construction: the write is after the emits.
- A failed chat read HOLDS the global cursor for the whole cycle (loud on stderr): with one cursor
  across chats, a partial advance on a sibling's messages would skip the failing chat's mail
  permanently. Duplicates on retry are the ruled safe direction.
- A read page FULL to the bound (25 fresh) emits a loud stdout backfill note — a possible loss is
  never silent (the denominator rule applied to the read window).
- Parsed timestamp compare everywhere: the seed cursor is second-grain, Graph carries milliseconds,
  and `"...12.095Z" < "...12Z"` lexically — the gateway's own server-side compare is lexical but
  uniform-format; the engine's cursor mixes formats exactly once (first arm), so it parses.
- An unparseable message timestamp EMITS (duplicate-safe) but never becomes the cursor (a corrupt
  cursor would re-emit forever) — the fail-open and fail-closed directions are deliberately different.

## Evidence — exercised, not reasoned (battery: scratchpad `p1_battery.py`, 23 of 23 PASS, rc=0 unpiped)

Real engine driven via its own `_gateway_call` seam (importlib; live credentials file never read or
written); the A2 mutant is the literal HEAD bytes (`git show` with positive control: 323 lines,
`def main` present). Fixture = the measured incident (M1 18:00:12.095Z ST-model question / M2
18:01:07.797Z interval question, cursor seeded second-grain 17:59:00Z).

| Criterion | Result |
|---|---|
| A1 two-in-one-window | BOTH emitted, oldest-first, "(1 of 2)/(2 of 2) since cursor", pre-cursor M0 excluded, cursor = max message ts. PASS |
| A2 mutant discrimination | HEAD engine reproduces the measured loss (M1 vanishes); in-process latest-only intake fails A1 under the FIXED engine (the READ is the fix); restored → passes. PASS |
| A3 crash seam | Raising print at first emit: 0 lines, cursor HELD at seed; next cycle re-emits both. PASS |
| A4 regression | Single-message stdout BYTE-IDENTICAL vs HEAD (+ identical cursor); pin no-match/ambiguous exit-2 + [TEAMS-IDENTITY-FAIL]; expired-only quiet retry pin-held (0 gateway calls); outgoing filter + processed-cursor; failed-read global hold; window-full note. PASS |
| A5 | BG's act on re-arm — handed over in msg 2592/2593 with the re-arm procedure + cursor-continuity note (stored gateway cursor is a Graph ms timestamp the new parser reads directly: no gap, no flood). |

Commit: `7e138ad6ef` (SITEZ, +142/−13, author 0.5.0_AE_OpalETL~Z). Commit-gate PASS. Risk-reflex
[HOLD] cited LD-0214 — read (also read at TO6): it assigns this engine to the AE lane and records the
quiet-retry property; A4 exercised that property green, no conflict. Historical backfill NOT run —
Andrew declined it (sec11 inner ruling, msg 2590); nobody quotes a loss count.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find --name "*teams*"` / `comp-find "teams-watch"` / `comp-find "read_chat_messages"` | Denominators printed (1/43/27 hits); located the engine [HEAD], the TO-1/TO6 records, and the gateway DEF at `infra/aws/ec2/opal-gateway/app/tools.py:600` in one call each | PASS |
| Rail deny on a `sed/grep` over `infra/` gateway source | Deny correct per Rule 21; re-done via native Grep + Read (a function-body read; no comp-tool answers "what does `_run` return") | RAIL HONORED |
| `.tools/commit-gate.sh` | py_compile + ruff clean; retired-alias invariant PASS (7 retired / 95 live, disjoint) | PASS |
| `safe-commit.sh` + risk-reflex | @7e138ad6ef; [HOLD] LD-0214 citation read, supports the change | PASS |
| `git show HEAD:<engine>` + positive control | 323 lines, `def main` = 1 — a real file, not a `fatal:` string; stderr not discarded | PASS |
| No comp-blast/comp-pipescript | Local skill engine with no pipeline edge (the TO6-recorded coverage gap stands: nothing answers "what consumes this SKILL file"); consumer set re-confirmed at source (`identity_scope.py`, SKILL.md) | N/A-JUSTIFIED |

## Surprise channel (reported, not chased)

- Startup `audit-archive-invoker` findings, this box: NON-APPEND-EDIT on `org/tier0/audit/ledger-hook-audit.log`
  (divergence line 1 col 7; baseline 1427709B vs live 111502B) and `org/rcg-sweep-audit.log` (line 3);
  `org/jq-ban-override-audit.log` MISSING (ERROR-FAILCLOSED). Auto-recorded to FINDINGS.md by the tool;
  device-axis class (site-Z tree vs laptop baselines). Not mine; one line here per the surprise-channel rule.

## Blockers

None I hold. A5 = BG's re-arm (queued to their inbox). Next at this seat per msg 2590: S2 — LOCATE the
schema-deferral mechanism (harness MCP config / launcher / seat settings), REPORT before changing;
then S5 (portal_lookup field mode). Ticketing Center channel ids remain event-gated in parallel
(nothing for me until the ids exist). S4/S6 design-gated at CTO~Z — not building.
