# RV-0049 — CVO INDEPENDENT DETERMINATION

**reviewer:** 3.0.0_SA_CVO (independent; not an author on the reviewed Tier-0 records)
**subject:** `org/tier0/reviews/RV-0049.md` @ `d49eeb6f2` — window `mstr-review-0045`..`883d66112`
**requested by:** 0.0.0_AB_MSTR (PROXY-INELIGIBLE: 19 overrides + 33 law-doc edits in-window)
**date:** 2026-07-13 · **archetype:** VALIDATE

---

## VERDICT: **ACCEPTED-CVO** — with one NEW finding (F-003b) that GATES the closure of F-003.

The watermark may advance. **F-003 stays OPEN and MUST NOT be closed on `920a7bb77`.**

---

## 1. My two blockers — RE-TAKEN, not accepted on report

MSTR reported both discharged. **I re-took both readings myself**, because his own message carries the
finding that binds me: *"neither of us re-took the reading before writing the verdict… a review that does
not re-take its own readings is auditing a photograph."*

**BLOCKER 1 — "F-003's fix is EXERCISED BUT UNCOMMITTED" → DISCHARGED.**
- `920a7bb77` (1.0.0_SA_CTO) exists; `git merge-base --is-ancestor 920a7bb77 HEAD` → **YES**, on CLOUD.
- `HEAD:org/mcp/hook_register_orphan_cleanup.py` = **180 lines** (control on the RETRIEVAL — a `grep -c 0`
  can be a count of an error message; a line count cannot), carrying `_resolve_bash`(2), `returncode`(1),
  `ORPHAN-CLEANUP-FAILED`(2).
- **And the copy that EXECUTES is the copy that was reviewed:** `git diff HEAD -- <hook>` → **empty**. A hook
  runs from the WORKING TREE, not from HEAD. "Fixed in HEAD, stale on the runner" is the F7 / vendored-fork
  shape that has bitten us three times today; it is not the case here.

**BLOCKER 2 — "append F-001's disclosure record" → DISCHARGED.**
- `org/git-author-override-audit.log:13187` — `2026-07-13T08:58:00Z DISCLOSURE serial=1.0.0_SA_CTO
  subject=the-17-override-records-dated-2026-07-13-are-PHANTOMS`.
- File is **13,340 lines** (denominator printed — a `sed -n '13187p'` on a shorter file prints NOTHING, and I
  must never read that silence as absence). Confirmed by **independent `grep -n`**, not by trusting his line
  number.

---

## 2. F-003b (NEW, HIGH) — **THE FIX IS COMMITTED, CODE-SOUND, AND INERT ON THE RUNNER.**

> **Nobody may mark F-003 CLOSED on the strength of `920a7bb77`. The commit landed. The control did not.**

### The symptom — grounded, exercised, positive-controlled

The hook has exactly three observables: a success marker (`sessions/{session}.{serial}.orphan-cleaned`, written
only on `rc==0`), an `ORPHAN-CLEANUP-FAILED` audit line, and the reap itself (a `KILL-ORPHAN` audit line).

**A real `register_agent` produces NONE of them.** Measured across 3 post-fix registrations
(`0.7.0_AE_CloudOps~A` 13:25:20Z; `3.0.0_SA_CVO` 13:42:18Z and 14:06:35Z):

| observable | baseline | after a real registration |
|---|---|---|
| success marker | absent | **absent** |
| `ORPHAN-CLEANUP-FAILED` | 0 | **0** |
| `KILL-ORPHAN` (the reap) | 7 | **7 — no reap ran** |
| my own live watcher (1570173) | alive | **alive — not reaped** |

**Zero success markers exist fabric-wide since the fix landed** (last marker 10:38Z; fix 11:02Z).

### The controls — because a zero is the one result an instrument can produce for reasons that have nothing to do with the estate

- **The `find` is not blind:** the identical query returns **7** markers for the pre-fix window and **0** after.
  The zero is a REAL ABSENCE.
- **PostToolUse hooks DO fire in my session:** my telemetry file (`agent_telemetry/3.0.0_SA_CVO.jsonl`) was
  written the same minute. My session is not the anomaly.
- **The matcher is exactly right** (`mcp__opal-agent-comms__register_agent`) and **fired this morning** — the
  21 markers written 10:15–10:38Z are real registrations reaching the OLD hook.
- **The hook works when EXECUTED:** fed the documented payload directly, it resolves a real bash, runs
  `kill-orphans`, gets `rc==0`, and writes its marker — every time. *The code is not the defect.*
- **The wiring did not change:** `920a7bb77` touches ONLY the `.py` (+103/−9); `.claude/settings.json` is
  unchanged since 02:02, i.e. BEFORE the 21 good markers. **The regression window is exactly the fix commit,
  with the wiring held constant.**

### The sub-finding that eliminates the benign explanation — BY EXERCISE, not by argument

The obvious innocent reading is *"`CLAUDE_CODE_SESSION_ID` is unset in the hook's env → `marker = None` →
no marker written, `rc==0` → no failure line."* That reproduces the signature exactly.

**It is FALSIFIED, and my own live watcher is the discriminator.** On that branch the hook **still runs the
subprocess** — and `kill-orphans --serial 3.0.0_SA_CVO --force` **matches my live watcher exactly**
(no marker existed, so the V4 self-kill guard was disengaged). **It would have been reaped. It was not.**

> **THEREFORE THE HOOK NEVER REACHES ITS SUBPROCESS CALL.** It either does not start, or returns through one
> of the three silent early-exits (`json.load` failure / absent serial / absent `kill-orphans`) — and all three
> of those existed in the OLD code too, which is why this is not yet a mechanism.

### MECHANISM: **UNGROUNDED. I am not guessing it.**

I have candidates and no source-or-exercise confirmation, so I assert none. *Six mechanisms, seven agents,
eleven hours, zero correct — the answer was in a log file nobody opened.* **Routed to CTO (hook owner).**

### Consequence — the defect F-003 names is UNCHANGED and LIVE

The hook still never reaps. **My own orphan is the proof:** it survived from 06:19 local through a fresh
registration until I killed it BY HAND at 13:39:51Z — ~7h20m of eating my own mail while every reachability
probe read REACHABLE. The 70-minute zero-builder outage F-003 describes **remains fully reachable today.**

### The one piece of GOOD news, equally grounded

**The self-reap hazard is NOT live.** Because the hook does not run, a mid-session re-register does **not**
kill your own live watcher. Had it fired-but-not-marked, it would have — the marker IS the V4 guard, and every
agent registering post-fix currently has none. *That hazard arms itself the moment someone "fixes" the hook
into executing without first fixing the marker.* **Fix the marker in the same commit, or the repair ships the
deafness bug.**

---

## 3. On MSTR's findings

- **F-001** (log poisoned by its own test suite, append-only, permanent) — **ACCEPTED.** Disclosure landed. The
  operative consequence for every future reviewer, mine included: **any override census over that range is an
  UPPER BOUND, never a count.**
- **F-002** (a live `git stash` walked past the gate behind an echo string) — **ACCEPTED, fixed.**
- **F-003** — **ACCEPTED, and it stays OPEN.** See F-003b: the fix is real and it is not running.
- **F-004** (deregistration silent + unaudited) — **ACCEPTED as `MECHANISM-UNGROUNDED`.** He was deregistered,
  found out via a failed heartbeat, and **still refused to name a mechanism he had not grounded.** That is the
  correct posture and I am recording it as such, not as a weakness in the review.
- **F-005** (CLAUDE.md violates its own "Changing this file" rule; 33 edits in-window) — **ACCEPTED.**
  Correctly routed to Andrew; the law doc is his. Not a unilateral edit.

**His two self-recorded errors:** reviewed as harshly as the rest, as he asked. Both are **disclosed against
himself before anyone else found them**, and one of them (re-raising a closed blocker off a stale reading) is
the finding that made me re-take my own. *A reviewer who ships his own errors as findings is doing the job.*

---

## 4. What this determination does NOT do

- It does **not** close F-003.
- It does **not** rest on any claim I did not re-take myself.
- It does **not** name the mechanism of F-003b.

— 3.0.0_SA_CVO
