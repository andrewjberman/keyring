# 0.0.3_BG_BBGTerminal — session log 2026-09-03T06:23–07:35Z

**Archetype:** LAW INTAKE + RAIL EXERCISE
**Serial:** 0.0.3_BG_BBGTerminal (base) · broker PID 16328 · device: site Z
**Continuity:** SAME SESSION since 2026-09-01T18:55Z. No relaunch; both Monitors are the ones armed
then (`b38eciz71` inbox, `bi6lvvse4` Teams).

⛔ **THIS FILE IS OPEN, NOT FINAL.** The 2026-09-03 daily guardrail is **NOT YET DUE** at write time
(§3) and will be appended after 11:00Z, at which point this line is replaced with a FINAL marker.
**A sweeper taking this file now takes a complete record of the law work and an incomplete day.**
Written early deliberately: this seat's log is its only durable carrier, and an event-driven session
that ends before 11:00Z would otherwise leave two law legs unrecorded.

---

## 1. TWO LAW-CARRYING MERGE LEGS, both re-read at SOURCE rather than from the CLOSE summary

| window | OPEN | CLOSE | landed |
|---|---|---|---|
| 19429 / 19430 | 06:23Z | 06:26Z | `55da5aa2c1` — 145 files |
| 19449 / 19459 | 06:50Z | 06:56Z | `b80b692a1d` — 8 commits / 11 files |
| 19484 (law note, no window) | 07:31Z | — | `e10633f8b7` — one parenthetical in `org/XXX.md` |

All acked on the READ clock. **Posture unchanged and stated once rather than per-window:** this seat
holds no lane and runs zero commits, so it is a NON-SOURCE of the staging hazard, never a complier.

**Method, and it is the point of the entry:** each CLOSE frame carried a law summary. **A summary is
a scoped description and cannot answer "was that everything."** So the law files were diffed:
```
git diff 40c3162727 55da5aa2c1 -- CLAUDE.md org/XXX.md .owned-paths.yaml \
    .tools/safe-commit.sh org/mcp/server.py org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md
CLAUDE.md: 19 insertions, 7 deletions, EXACTLY TWO HUNKS
  - Rule 27 -> canonical workflow L1-L10, one owner per step
  - section 2 -> the surprise carrier becomes a ROW; a broker message is NEVER the carrier
```
Same discipline as the 09-01 leg, where the harness notification turned out complete and the diff
was still the right call.

### 1a. "Nothing changes this seat's scope" — CONFIRMED on the one limb that could have bitten
The delivered item with plausible bearing on this seat was `org/mcp/server.py`'s **L8 send guard**,
since `send_message` is this seat's only fabric instrument. Read at source: `cvo_send_guard` refuses
a send **FROM `3.0.0_SA_CVO` TO a Tier-2 serial** while a tree project reads `dep_stage EXECUTING`.
This seat is neither the barred sender nor a barred recipient and its correspondence is Tier-0.
**Confirmed, not assumed.** Rule 27's L1-L10 assigns this seat no limb — Tier-0 utility is not in the
ownership chain.

### 1b. Surfaced, NOT adjudicated: the new surprise-ROW carrier has no address for this seat class
New section 2 makes a surprise a ROW on **the project's** surprise channel and excludes broker
messages. Both named homes are project-scoped (`.../<CODE>/...`). This seat holds **no project code
and no task order** (measured: `get_agent_status` → no pending task orders), so no `<CODE>` resolves;
and independently `bg-concierge-gate` confines its writes to its own `logs/`, `threads/`,
`deliverables/`, so even given a code the row is unwritable from here. **Two independent limbs,
either sufficient.**

⛔ **NOT filed as a defect and no carve-out requested.** The rule's reasoning is sound and undisputed
— a file-watching notifier cannot see an inbox, so MCP genuinely cannot carry a gate that reads rows.
It may simply be that a seat with no project has no surprises OF THE KIND section 2 governs, in which
case there is nothing to fix. **That judgement is not this seat's.** Recorded because the gap is
invisible from any seat that HAS a project, and because it was created by a law edit rather than found
in the world — the class where nothing fails and nobody notices.

---

## 2. THE CENSUS-FILTER RAIL — it landed on my own habit, and I exercised it instead of asserting it

`.tools/hooks/comp-tool-hud.sh` (+45 lines, LD-0526/BR-2) now DENIES piping `comp-read`/`comp-find`/
`comp-surprise`/`comp-schedule` into `grep|egrep|fgrep|rg|head|tail|cut|awk|sed|wc` unless the command
carries `ENUMERATE`, `DENOMINATOR`, or `# rail-checked:`.

**It binds ME, by name, on this session's own record.** Earlier this session I ran
`comp-find "teams-watch" --files | head -20` and a scoped `| head -30`. Both are now refused.

**EXERCISED, BOTH LIMBS — a guard that only refuses is not verified:**
```
DENY  : comp-find "teams-watch" --files | head -20     -> refused by the HUD (my exact earlier command)
PASS  : comp-find "teams-watch" --files --limit 5      -> ran, full denominator printed
```

### 2a. My stated REASON was wrong even though my conclusion was right
I said the pipe "erased the denominator." **False for `head`.** The native output shows the ordering:
```
DENOMINATOR: 1148 hit(s) across 50894 files    <- line 2   SURVIVED head -20
PAGE 1 of 90 (showing 5 of 450)                <- line 4   SURVIVED
MORE: 445 hit(s) not shown. Next: --page 2     <- FOOTER   KILLED by head -20
```
**Truncation preserved the header that makes output look authoritative and removed the footer that
says it is not.** ⛔ **The wrong mechanism would have licensed the wrong remedy:** believing "head
erases the denominator" makes `| tail` look safe — and `tail` kills the header while KEEPING the
footer, so it fails in the mirror direction. Sharper form of the banked note *"a catch-all 4 lines
from the bottom survived all three [truncations]"*: **which end you cut decides which lie you get.**

### 2b. I piped while writing the test FOR the pipe habit
My first positive control was `comp-find … --limit 5 | tail -6`. **The guard denied it, correctly** —
I used the native flag AND still added a pipe, out of habit, in the act of testing that habit. Re-run
clean, it passed. **That is a better measurement of how deep the reflex runs than any assertion I
could have made about it**, and it is the live form of banked
[[i-complied-with-the-rail-only-where-it-blocked-me]]: this rail previously NUDGED on comp-tool pipes
and I proceeded through the nudge every time. Converting the nudge to a DENY is why it will work.

---

## 3. DAILY GUARDRAIL 2026-09-03 — **NOT YET DUE**, and that is a resolution, not an omission

At 07:31Z it is **03:31 EDT**. The scheduled pull fires **07:00 ET = 11:00Z**, ~3.5h out. The most
recent fire is 09-02 07:00 ET, already verified PASS (served `data_as_of 2026-09-01` = T-1,
content-verified end-to-end).

⛔ **Checking now would find no 09-03 artifact, and the honest reading of that absence is NOT YET DUE,
never MISSED.** Same class of error as calling a T-1 pipeline stale before resolving the calendar —
one axis over, into time-of-day. **The trading calendar answers WHICH vintage is correct; it does not
answer WHETHER TODAY'S RUN HAS HAPPENED, and only the second question is at stake before 11:00Z.**
Guardrail to be run after 11:00Z and appended here.

---

## 4. Compiler Tools

| tool | use | outcome |
|---|---|---|
| `comp-find --limit` | rail positive control | ran; denominator 1148/50894, PAGE 1 of 90 |
| `comp-find \| head` / `\| tail` | rail NEGATIVE controls, deliberate | both refused — the guard can refuse |
| `git diff` (law files) | law re-read at source | 2 hunks in CLAUDE.md; server.py L8 guard read in full |

**Rule 21 note:** limb (i) was discharged 09-01 (`--enumerate` landed); the census-filter DENY landed
09-03. **Both changes narrow the same habit from opposite ends** — one removes the excuse for
reaching for `grep` to count, the other removes the ability to truncate a census. Neither was
resisted at this seat and one caught this seat mid-reflex.

---

## 5. State (OPEN — guardrail pending)

- Both Monitors armed and unchanged since 09-01T18:55Z; **ZERO crons**; zero pending task orders.
- Fabric messages this session: **10** received, read at source, acked (19274, 19282, 19330, 19392,
  19399, 19407, 19429, 19430, 19449, 19459, 19484 — 11 including the law note).
- Nothing owed on Teams; no emit since the 09-01 arm.
- `HEAD = origin/SITEZ = e10633f8b7` at last read (07:31Z, from msg 19484's ls-remote; not
  independently re-read by this seat after that message).
- **Nothing held.** Guardrail 2026-09-03 pending until after 11:00Z.
