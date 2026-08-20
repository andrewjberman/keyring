# RELAUNCH.md — bringing the 0.0.3_BG_BBGTerminal seat up (wrapper-free)

**Authority:** OPAL_ANALYST PRD §4.2 (v1.0 @d179643ca) · OPAL_ANALYST.TO2 · authored by
0.5.0_AE_OpalETL~Z 2026-08-10. Any operator or 0.0.0_AB_MSTR~Z can run this — the box
launcher holds execution; this document holds the procedure.

Steps map 1:1 onto `prompt.md` "On launch" (1, 2, 2a, 3, 4, 5) — the prompt is the
authority; this runbook adds the exercised mechanics (pin flags, TMPDIR, evidence
capture). If they ever diverge, the prompt wins and this file is the defect.

---

## 0. Prerequisites (verify BEFORE launching — all four, no memory)

| # | Prerequisite | How to verify |
|---|---|---|
| P1 | TO-1 identity pin LANDED + EXERCISED | `git log --oneline -1 -- .claude/skills/teams-assist/teams-watch.py` shows `0f1bbcf0e` (or a descendant). Exercised record: 0.5.0_AE log 2026-08-10 (negative control rc=2, positive 3/3). Do NOT relaunch on a committed-but-unexercised pin. |
| P2 | `opal-gateway-bbg` token minted for **Opal Bloomberg** | `whoami` on `opal-gateway-bbg` → "Opal Bloomberg". If no valid token: the login secret is `opal/mcp/opalbloomberg-login` (Secrets Manager — NAME citable, VALUE never); OTP goes to Andrew's phone; surface the auth URL and Andrew completes the mint. If whoami answers Andrew or any non-Opal-Bloomberg identity → HOLD (see Error paths). |
| P3 | Mechanical fence present | `.tools/hooks/bg-concierge-gate.sh` wired at `.claude/settings.json:145` (@65d80ab37). **The fence loads PER-SESSION at session start (PRD App C): a stale/prior session's fence is NEVER assumed active — a fresh launch is what arms it.** |
| P4 | Bloomberg box state | Terminal logged in (else `bloomberg_health` will FAIL at step 4 — surface, don't work around). |

## 0b. STANDING ORDER — re-arm the 07:15 daily backstop cron EVERY session (Andrew-direct 2026-08-20)

**A relaunching successor ARMS `CronCreate("15 7 * * *", <the backstop check>)` at startup
while this ruling stands** — full firing procedure, both Andrew verbatims, the authorization
scope fence, and the re-arm warning live in
`../deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` (BG-authored 2026-08-20; ruling
record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260820_MSTRZ_LET_THE_FALLBACK_TRY_SELF_HEAL_UNTOUCHED.md`
@eede873a2f). **This row is the EXPLICIT exception to the "Tier-0 UA arms ZERO crons"
default** — without it, that law points a successor away from a live sovereign instruction
(the silent-drop shape the COO `/drive` and CVO~Z SYSPARITY rows record). The cron is
session-only; this pointer is what makes the order survive a relaunch. *(Row placed by
0.0.0_AB_MSTR~Z as named integrator — the seat's G1 fence correctly cannot write refs/.)*

## 1. Launch

`ajb 0.0.3_BG_BBGTerminal` (box launcher — MSTR~Z or the operator at the terminal).

The seat then executes its own prompt.md On-Launch sequence. The launch-runner verifies
each step's evidence below.

## 2. On-Launch sequence (prompt.md steps, with exercised mechanics)

1. **Register:** `register_agent("0.0.3_BG_BBGTerminal", summary=...)` → broker LIVE.
2. **`/watcher`:** fabric inbox Monitor armed; confirm `TaskOutput(<id>, block=false)` → running.
   **2a. IDENTITY ACCEPTANCE GATE (before ANY Teams read or reply):** `whoami` on
   `opal-gateway-bbg`. PASS = the Opal Bloomberg account. **Anything else → STOP: no poll,
   no reply; report the mismatch to `0.0.0_AB_MSTR~Z` and hold.** (First launch 08-07: this
   gate correctly caught an andrew@ mint once. It is a data assertion at the seat's own
   boundary, not a fabric approval gate.)
3. **Arm the Teams Monitor WITH the identity pin** (per `refs/TEAMS_DUTY.md`; TO-1's landed
   form @0f1bbcf0e — cited, not restated):

   - **TMPDIR first (TO-1 finding 2026-08-10):** under native Windows python with no TMPDIR,
     the engine's cursor default `/tmp/teams-watch.cursor` is unwritable and the engine dies
     `FileNotFoundError` before any poll. The arm command MUST carry a valid TMPDIR.
   - Arm via the **Monitor tool** (persistent; NEVER Bash run_in_background — stream mode
     never exits), command:

     ```
     TMPDIR="$(cygpath -w "$HOME/AppData/Local/Temp")" python .claude/skills/teams-assist/teams-watch.py 15 --server opal-gateway-bbg --identity opalbloomberg
     ```

     (`15` = poll interval seconds, the 08-07 operating value; omit for the default 10.)
   - **The pin is mandatory for this seat. Pin arg absent → do not arm.** Bare arming is the
     identity-blind P0 defect TO-1 closed.
   - Confirm `TaskOutput(<monitor id>, block=false)` → running, and the stderr banner shows
     `pin(server=opal-gateway-bbg, identity=opalbloomberg)` + `token selected:
     identity=opalbloomberg@opalinvest.com`.
   - **ZERO scratchpad scaffolding:** no wrapper script, no `teams-watch-bbg.py` — that
     pattern is dead by design (no-shadow veto). The stock engine + flags is the whole arm.
   - An exit-2 `[TEAMS-IDENTITY-FAIL]` at/after arm = the pinned token is absent, expired,
     or ambiguous. Resolve the token (P2 re-mint path), then re-arm. It will never fall back
     to another identity — that loud death is the fix working.
4. **`bloomberg_health`** → `ok: true`; confirm the `cma` interpreter connects (green MCP is
   not a runnable pull — exercise the interpreter).
5. **Orient:** read latest `logs/`; arm ZERO crons (the two Windows Scheduled Tasks are
   OS-level, not the seat's).

## 3. First-session obligations

- **Action the pending fabric inbox message:**
  `org/mcp/inbox/0.0.3_BG_BBGTerminal/20260807T182104Z_0.0.0_AB_MSTR_Z_Concierge_completion_set_landed_--_mecha.md`
  (MSTR~Z completion-set notification, unread since 08-07) — read + act/ack per its content.
- **First-serve smoke (ACK-FIRST, per `/bbg-teams-assist`):** on the first inbound Teams
  message (or the backlog sweep `/bbg-teams-assist` if anything landed while dark), run the
  full serve loop; the reply must deliver AS "Opal Bloomberg" with vintage attached.

## 4. Smoke evidence to return (TO-2 Phase 3 — the launch-runner captures ALL four)

| Limb | Evidence |
|---|---|
| Identity | step-2a `whoami` output == Opal Bloomberg |
| Monitor | pinned arm `TaskOutput(<id>)` → running + the `token selected: identity=opalbloomberg@...` line |
| Serve | one ACK-FIRST serve delivered as "Opal Bloomberg" (vintage attached) |
| Fabric | broker registration LIVE + the 08-07 inbox message actioned |

Any limb failing → **HOLD the relaunch (never leave it half-landed); surface to COO~Z +
CTO~Z with the failing limb.** Return the evidence to 0.5.0_AE_OpalETL~Z (TO-2 verifier),
cc 2.0.0_SA_COO~Z.

## Error paths (exhaustive for this procedure)

| Symptom | Meaning | Action |
|---|---|---|
| whoami → Andrew (or any non-Opal-Bloomberg) | wrong/absent identity mint | HOLD. No poll, no reply. Report to MSTR~Z; re-mint per P2. |
| Pin arg absent from the arm line | identity-blind arm about to happen | Do NOT arm. Fix the arm line (step 2.3). |
| `[TEAMS-IDENTITY-FAIL] no-token-for-identity` rc=2 | no mcpOAuth record matches the pin | Re-mint (P2), re-arm. Never widen the pin to make it match. |
| `[TEAMS-IDENTITY-FAIL] expired-token-for-identity` rc=2 | pinned token lapsed | Refresh/re-mint, re-arm. |
| `[TEAMS-IDENTITY-FAIL] ambiguous-token-match` rc=2 | >1 valid record matches the pin | Tighten the pin (both `--server` and `--identity`); never sort-and-hope. |
| `FileNotFoundError .../teams-watch.cursor` | TMPDIR unset/invalid on native Windows python | Set TMPDIR in the arm command (step 2.3). |
| `bloomberg_health` not ok | Terminal down/logged out | Surface (Andrew brings the Terminal back); do not touch it. |
| Fence BLOCKED on a tool call | the system working | Do not retry or route around; real need → Andrew via MSTR~Z. |

## Steady state

**RULED (Andrew-direct 2026-08-10 ~1653Z, record @bc7eb60de): OPERATOR-STARTED.** Andrew or
MSTR~Z brings the seat up by hand off this runbook — NO cron, NO auto-start. A session that
dies stays down until an operator runs this procedure again.

**DAILY UPLOAD GUARDRAIL DUTY (Andrew-direct Q5, record @e77bec6e5):** each session-day the
seat CHECKS EXECUTION RECORDS that the scheduled Bloomberg upload ran — the system cron
`OPAL_BBGTML_daily_pull` (07:00 ET) is the PRIMARY path, and the check is of records, not a
new monitor (alarm moratorium untouched). On a missed/failed run: fallback `/terminal-upload`
under its own skill gates (NEVER send on a tripwire FAIL), or escalate to Andrew/MSTR~Z. The
seat's gateway allowlist carries `opal_data_refresh_upload` as a FALLBACK-ONLY row
(# andrew-asked, same record) — fallback capability is not a license to replace the cron.
