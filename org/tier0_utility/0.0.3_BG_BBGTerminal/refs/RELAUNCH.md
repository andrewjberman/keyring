# RELAUNCH.md — bringing the 0.0.3_BG_BBGTerminal seat up (wrapper-free)

**Authority:** OPAL_ANALYST PRD §4.2 (v1.0 @d179643ca) · OPAL_ANALYST.TO2. Any operator or
0.0.0_AB_MSTR~Z can run this — the box launcher holds execution; this document holds the
procedure. Steps map 1:1 onto `prompt.md` "On launch" — the prompt is the authority; this
runbook adds the exercised mechanics. If they diverge, the prompt wins and this file is the
defect (the §0b standing order is the one ruled exception, carried on its own record).

---

## 0. Prerequisites (verify BEFORE launching — all four, no memory)

| # | Prerequisite | How to verify |
|---|---|---|
| P1 | TO-1 identity pin LANDED + EXERCISED | `git log --oneline -1 -- .claude/skills/teams-assist/teams-watch.py` shows `0f1bbcf0e` or a descendant (exercised record: 0.5.0_AE log 2026-08-10). Never relaunch on a committed-but-unexercised pin. |
| P2 | `opal-gateway-bbg` token minted for **Opal Bloomberg** | `whoami` on `opal-gateway-bbg` → "Opal Bloomberg". No valid token: login secret `opal/mcp/opalbloomberg-login` (Secrets Manager — NAME citable, VALUE never); OTP goes to Andrew's phone — surface the auth URL, he completes the mint. Any non-Opal-Bloomberg answer → HOLD (Error paths). |
| P3 | **RETIRED -- the fence is UNWIRED by Andrew's word** | `org/tier0/ledger/LD-0580.md` (Andrew-direct 2026-09-17, "the BG concierge gate is bullshit pull that off right now."): the hook is removed from `.claude/settings.json`; the script stays on disk, unwired. Its absence is NOT a relaunch blocker and no seat re-wires it without his new word (ruled by `1.0.0_SA_CTO~Z`, 2026-10-08). The seat's read-and-report discipline binds by its prompt. The text below is the pre-LD-0580 contract, kept for history only: `.tools/hooks/bg-concierge-gate.sh` wired in `.claude/settings.json` (@65d80ab37; F8 tightening @cde91ccd08, Andrew-direct "rec approved" @ad2585793c). The fence arms PER-SESSION at session start — never assume a prior session's fence is active. **F8:** an UNRESOLVABLE identity on this seat's launch path FAILS CLOSED AND LOUD (every classed call denied with a named line); a healthy `ajb` launch resolves POSITIVELY (see §1) and is ACTIVE; any other seat with an unresolvable identity gets a LOUD line, never a block. A launch that lands LOUD-CLOSED = the identity binding did not land — relaunch via `ajb`; never loosen the fence. |
| P4 | Bloomberg box state | Terminal logged in (else `bloomberg_health` FAILS at step 4 — surface, don't work around). |

## 0b. STANDING ORDER — EVENT-BASED summons response; a successor arms NO cron (Andrew-direct 2026-08-20 ~1329Z, cutover completed ~1540Z)

The backstop is EVENT-BASED off the deterministic freshness gate (OS Scheduled Task
`OPAL_BBGTML_freshness_check`, 07:30 ET): you engage ONLY on a summons — a
`*_freshness_checker_*.md` file in your fabric inbox (or delivered as your spawn's first
message on a seat-down morning). **Arm NOTHING; zero crons is the CORRECT state.** The full
trigger contract (Kind table, default-to-engage-on-unknown, Step-1 entry always) lives in
`../deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md` — **the filename is an ADDRESS and
deliberately kept** (this pointer resolves by path; the title inside is the current truth).
Provenance: Andrew's event-based order (BG 2317 verbatim), the ruled prior form @eede873a2f,
the dead-seat spawn drill PASSED 2026-08-20 (63s spawn-to-registration). *(Row maintained by
0.0.0_AB_MSTR~Z as named integrator; the seat's fence cannot write refs/.)*

## 1. Launch

`ajb 0.0.3_BG_BBGTerminal` (box launcher — MSTR~Z or the operator at the terminal). The
seat executes its prompt.md On-Launch sequence; the launch-runner verifies each step's
evidence below.

**F8 identity binding (2026-08-20 @cde91ccd08):** the `ajb` launch IS this seat's identity binding — ajb mints the session id, writes `org/mcp/sessions/<sid>.launch-path` (`bg-concierge …`) FIRST and `<sid>.serial` SECOND (G1 forbids the seat both writes — that is why the launcher does them), and pins `claude --session-id <sid>`. Expect the `[ajb] F8: BG identity bound at launch` line at spawn. Marker-without-serial (a failure between the two writes) reads as LOUD-CLOSED — the correct failure; the fix is a relaunch via `ajb`, never a hand-written serial file.

## 2. On-Launch sequence (prompt.md steps, with exercised mechanics)

1. **Register:** `register_agent("0.0.3_BG_BBGTerminal", summary=...)` → broker LIVE.
2. **`/watcher`:** fabric inbox Monitor armed; confirm `TaskOutput(<id>, block=false)` → running.
   **2a. IDENTITY ACCEPTANCE GATE (before ANY Teams read or reply):** `whoami` on
   `opal-gateway-bbg`. PASS = the Opal Bloomberg account. **Anything else → STOP: no poll,
   no reply; report the mismatch to `0.0.0_AB_MSTR~Z` and hold.**
3. **Arm the Teams Monitor WITH the identity pin** (per `refs/TEAMS_DUTY.md`; pin form
   @0f1bbcf0e — cited, not restated):

   - **TMPDIR must be set:** under native-Windows python with no TMPDIR the engine's cursor
     default `/tmp/teams-watch.cursor` is unwritable and it dies before any poll.
   - Arm via the **Monitor tool** (persistent; NEVER Bash run_in_background — stream mode
     never exits), command:

     ```
     TMPDIR="$(cygpath -w "$HOME/AppData/Local/Temp")" python .claude/skills/teams-assist/teams-watch.py 15 --server opal-gateway-bbg --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f
     ```

     **Pin form = Opal Bloomberg's Entra object id**, not `opalbloomberg`: since the
     2026-10-08 reauth the `opal-gateway-bbg` token `sub` is `<tenant>/<oid>` with no UPN
     substring, so the name pin matches 0 records. The oid matches exactly 1 record (the
     bbg one) and Andrew's oid `2e21f8e5-...` matches 0 (negative control, measured
     2026-10-08 by `0.0.3_BG_BBGTerminal` msg 31987 and re-read by `1.0.0_SA_CTO~Z`).

     (`15` = poll interval seconds, the operating value; omit for the default 10.)
   - **The pin is mandatory for this seat. Pin arg absent → do not arm.**
   - Confirm `TaskOutput(<monitor id>, block=false)` → running, and the stderr banner shows
     `pin(server=opal-gateway-bbg, identity=517aa5ee-...)` + `token selected:
     identity=.../517aa5ee-...`.
   - **ZERO scratchpad scaffolding:** no wrapper script — the stock engine + flags is the
     whole arm (no-shadow veto).
   - An exit-2 `[TEAMS-IDENTITY-FAIL]` at/after arm = the pinned token is absent, expired,
     or ambiguous. Resolve the token (P2 re-mint path), re-arm. It never falls back to
     another identity — that loud death is the fix working.
4. **`bloomberg_health`** → `ok: true`; exercise the `cma` interpreter (green MCP is not a
   runnable pull).
5. **Orient:** read latest `logs/`; arm ZERO crons — the backstop duty is EVENT-BASED per
   §0b, and the Windows Scheduled Tasks (07:00 pull, 07:30 freshness check) are OS-level,
   not the seat's.

## 3. First-session obligations

- **S2 ACCEPTANCE, ONE-TIME, first launch after @e23b879dad (retire this row once reported):**
  the launcher now sets `ENABLE_TOOL_SEARCH auto:25` for this seat (sec11 S2, CTO~Z ruling
  msg 2618). Confirm your six hot gateway tools (send_chat_message, read_chat_messages,
  poll_addressed_teams_messages, whoami, ack_messages, opal_data_refresh_upload) are
  RESIDENT — i.e. you reached your first Teams ACK with **ZERO ToolSearch calls**. Report to
  MSTR~Z + CTO~Z. Any tool still deferring at auto:25 → say so; the line drops to `false`.
  Baseline: the 2026-08-20 session made FIVE ToolSearch schema loads before its first
  outbound act (see `logs/2026-08-20/`) — zero is only checkable against that prior.
- **Inbox pull:** `/watcher` Step 4 covers it — act on anything found, same turn.
- **First-serve smoke (ACK-FIRST, per `/bbg-teams-assist`):** on the first inbound Teams
  message (or the backlog sweep `/bbg-teams-assist` if anything landed while dark), run the
  full serve loop; the reply must deliver AS "Opal Bloomberg" with vintage attached.

## 4. Smoke evidence to return (TO-2 Phase 3 — the launch-runner captures ALL four)

| Limb | Evidence |
|---|---|
| Identity | step-2a `whoami` output == Opal Bloomberg |
| Monitor | pinned arm `TaskOutput(<id>)` → running + the `token selected: identity=.../517aa5ee-...` line |
| Serve | one ACK-FIRST serve delivered as "Opal Bloomberg" (vintage attached) |
| Fabric | broker registration LIVE + inbox pulled/actioned |

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

**OPERATOR-STARTED (ruled, record @bc7eb60de):** Andrew or MSTR~Z brings the seat up by
hand off this runbook — NO cron, NO auto-start. A session that dies stays down until an
operator runs this procedure again.

**DAILY UPLOAD GUARDRAIL DUTY (record @e77bec6e5):** each session-day, check the execution
records that the scheduled Bloomberg upload ran (system cron `OPAL_BBGTML_daily_pull`,
07:00 ET, the PRIMARY path) — a records check, not a new monitor. On a missed/failed run:
fallback `/terminal-upload` under its own skill gates (NEVER send on a tripwire FAIL), or
escalate to Andrew/MSTR~Z. The seat's `opal_data_refresh_upload` allowlist row is
FALLBACK-ONLY — capability is not a license to replace the cron.
