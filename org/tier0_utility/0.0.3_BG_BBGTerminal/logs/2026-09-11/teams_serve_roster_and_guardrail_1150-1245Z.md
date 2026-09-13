# 0.0.3_BG_BBGTerminal — session log 2026-09-11T11:50–12:45Z

**archetype:** TEAMS SERVE + DAILY GUARDRAIL

**Serial:** `0.0.3_BG_BBGTerminal`, session `fd87eb7b-…`, PID 6104 — **same continuous session** as the
2026-09-10 startup (three logs that date). Woken by the Teams Monitor after an overnight idle.

⛔ **THE ANDREW-FACING SUBSTANCE IS NOT REPEATED HERE.** F1 (the lapse), F2 (the roster wrong when
sent) and F3 (the corrected roster repeating the defect) live in
`threads/2026-08-07-andrew-capability-roster/2026-09-11.md`, with the standing instruction at that
thread's `THREAD.md` row 5 and the rule itself at `refs/TEAMS_DUTY.md` "Reply norms" bullet 2.
**This file carries only what is SESSION-scoped and would otherwise go unrecorded** — one carrier
per fact, which is the same discipline the day's findings were about.

---

## 1. DAILY GUARDRAIL 2026-09-11 — GREEN, and the sign-in held

| limb | measurement |
|---|---|
| 07:00 ET pull | `bbg_tplus1_20260911_070002.log` — `PRECONDITION: PASS -- DAPI UP` · `PULL EXIT CODE: 0` · `PUBLISH vintage 20260910` · `RESULT: PUBLISHED 2026-09-10 -- verified by content, not by self-report` · ETF leg 0 · constituents leg 0 |
| 07:30 ET checker | `2026-09-11T11:30:03Z PASS: data_as_of=2026-09-10 expected_frontier=2026-09-11 trading_days_behind=1` — healthy T-1. **No SCHEDULE-GAP** (yesterday's was the 09-07→09-09 outage) |
| terminal, live | `bloomberg_health -> ok:true` at 12:39Z — measured, not assumed, because this seat told `2.0.0_SA_COO~ZZZ` to treat "the terminal is up" as perishable and the same binds here |

⭐ **LAST NIGHT'S 19:47Z SUPERVISED SIGN-IN HELD THROUGH THE 07:00 FIRE.** The precondition passed
with **no fallback sign-in**, so **no attempt was spent** — the attempt ledger is unchanged at 13.
One supervised attempt covered both the AMGT_RESAPP unblock and this morning's scheduled run. The
mid-session sign-out hazard recorded in `logs/2026-09-10/terminal_signin_for_amgt_resapp_1942-1950Z.md`
§3 did **not** recur in this window; that is one clean overnight, not a closed hazard.

---

## 2. SESSION MECHANICS — a broker blip, measured rather than assumed

`register_agent` at 12:37Z returned **`Broker: unavailable`** where every prior call that session
returned `connected (port 7800)`. **Probed rather than carried forward:** `get_agent_status` at
12:39Z returned LIVE, last seen 20 s, and drained four queued messages — so the broker was back and
the blip was transient. **Channel push stayed enabled throughout**, and filesystem delivery is a
separate carrier from the broker anyway, so the inbox Monitor was never the thing at risk.

⚠ **The four "URGENT ... act NOW" messages in that drain were all ALREADY OPENED, ACTED ON AND
ACKED** (21047, 21352, 21354, 21362). **Re-emission is not new work**, and the drain's own
`ack_messages(...)` prompt would have had me re-ack four ids whose READ rows already existed.
Read the ledger, not the prompt: `get_delivery_state` showed READ=5 / SENT=1 over denominator 6,
the single SENT row being the message that arrived during the check (21372, acked at 12:45Z).

⚠ **The liveness reaper pruned this seat repeatedly across long quiet turns** — every
re-registration returned the **same PID 6104**, so none was an identity conflict. Same benign shape
the 09-06 and 09-10 logs each recorded.

---

## 3. COMPILER TOOLS

| Tool | Invocation | Result |
|---|---|---|
| `git show <hash>:<path>` + **positive control** | `MSYS_NO_PATHCONV=1`, control string `"What happened"` = 1, three edit-only strings = 0 | **falsified the integrator's inference** that my later edits rode its first sweep; on this box a mangled `git show` returns clean-empty and would have faked the same three zeros — the control is what made the absence real |
| `git log --follow` | vs `--diff-filter=A` at the current path | recovered birth **2026-08-10 / `0.5.0_AE_OpalETL~Z`** where `--diff-filter=A` returned the **08-14 rename** wearing a birth's shape. Banked by the integrator as `a-rename-reads-as-an-add-under-diff-filter-a` |
| `Read` on the gate | `.tools/hooks/bg-concierge-gate.sh:152` | `threads/` is permitted with **no `THREAD.md` carve-out** — falsified **my own** claimed fence; the attempted write then confirmed it by exercise |
| `find_sharepoint_site` | live call, 12:37Z | closed the unexercised bucket in my own corrected roster (F3) |
| `read_chat_messages` before the ACK | the emit's body preview was EMPTY | reading the message is not researching it; a receipt for an unknown object is how an ack goes wrong |

**Rule 22 note:** the three claims that could cost another seat or the principal — the pushed-blob
state, the allowlist's history, my own write fence — were each taken to a **second, differently
shaped instrument**, and **two of the three came back against me.**

---

## 4. STATE AT CLOSE

Registered LIVE PID 6104; inbox Monitor `bh55lbr03` and Teams Monitor `by8vel475` both running;
zero crons. Terminal UP. Portal serving `data_as_of 2026-09-10` = healthy T-1, both OS tasks green,
next fires 09-12. Sign-in budget: 13 ledger entries, one attempt of two unspent.

**OPEN, and neither is mine to close:**
1. **Andrew's 06:44Z attachment ask — UNSERVED.** No text accompanied the file; the file is
   unreadable from this identity. **Waiting on his content or his question.** Not closed.
2. **A5 live positive — STILL UNSATISFIED.** He sent ONE message today; the two-in-a-row frame was
   not exercised and the interim re-send rule STANDS. **Not manufactured.**
3. **D7 client-ticket intake** — 171.2 h at the 09-10 reading, unchanged escalation, corroborated
   by `0.0.0_AB_MSTR~Z` from the Task Scheduler plane.
4. **`teams-watch.py` agent-triggered lapse recovery** — `0.5.0_AE_OpalETL~Z`; **recurred overnight
   and cost five hours on a real Andrew message** (thread record F1), routed as information with
   no act.
5. **Mid-session terminal sign-out has no automatic recovery** — route is Andrew; one clean
   overnight is not a closed hazard.
6. **`OPAL_BBGTML_freshness_check` `StartWhenAvailable=False`** — with this seat's transient-alarm
   qualifier attached; `0.0.0_AB_MSTR~Z` holds the call.

⚠ **UNCOMMITTED: this file only.** Every other record of this seat's is on origin — the integrator
swept four times today (`@2d8b5f7314`, `@3f8aff81bd`, `@4513ed216d`, `@b359fa84dd`), each time after
**this seat flagged the dirt before the integrator found it**, which is why nothing else is
LOCAL-only. **Push state of every hash cited: UNREAD BY THIS SEAT** — all quoted from
`0.0.0_AB_MSTR~Z`'s `ls-remote` reads; a hash relayed is not a hash verified.
