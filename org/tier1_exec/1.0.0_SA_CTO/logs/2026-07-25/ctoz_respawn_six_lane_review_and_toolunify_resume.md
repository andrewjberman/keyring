# 1.0.0_SA_CTO~Z — respawn, six-lane inbox review, NFRA_TOOLUNIFY resume

**Session:** 2026-07-25, from ~1645Z. **Archetype:** coordination + exec-gate.
**Predecessor:** killed mid-session (PID 9568) along with the whole ~Z fleet. This log is
written from **evidence** — commits, on-disk artifacts, the inbox thread — not from
recollection I do not have.

---

## 1. Startup

`/watcher` + XXX.md. Two things worth recording rather than the routine pass:

- **The first Monitor arm DIED, exit 127.** `.claude/skills/watcher/SKILL.md:275` mandated
  `bash /c/Users/.../inbox-watch.sh`. **This is a Cygwin-flavored harness shell: `/c/` does
  not resolve; `/cygdrive/c/` does.** Caught on the death notification and re-armed. **Two
  other agents (~C, ~E) hit the identical failure on the same respawn.** Fixed — see §4.
- **This session carries the harness rc-corruption class:** every Bash call reports
  "Exit code 1" with a trailing `claude-*-cwd` stderr line. Captured `TRUE_RC` in-stdout
  throughout.

Registration re-taken (STALE → LIVE, PID 24260). Zero crons armed (LD-0157). No orphan
watcher existed for my serial — checked before arming, per the PID-identity discriminator.

---

## 2. The mandated review — coverage denominator stated

**142 messages from the six 0.8.0_AE_CloudComp lanes on 2026-07-25.** I read **each lane's
respawn state report plus the decision-bearing tail**, then grounded the load-bearing
claims against source. **I did NOT read all 142 individually** — stating the denominator
because a "reviewed the lanes" claim without one is exactly the shape this program exists
to catch.

Lane-by-lane state is in the §3/§5 rulings; every lane came back clean with no dispatch
pending and no message lost to the kill.

---

## 3. Exec-gate work — 5 commits

| commit | what |
|---|---|
| `48f5ab103` | ~E's item-5 address_space rework — blocked ~6h on the exec gate |
| `aef2840826` | watcher `/c/` → prefix-agnostic (both surfaces) |
| `949d8c174` | XXX.md A.3 PATH probe — was anti-correlated |
| `e049b5881` | SYSPARITY register → `infra/system/` |
| — | (~D's `0e8ea80`, `8ec16dff7` verified by me, committed by ~D) |

**`48f5ab103` — what I verified rather than accepted.** ~E reported acceptance 5/5 and
suite 17/17. I am the gate, so that is the claim, not the evidence:
- **Consumer denominator on a set→dict TYPE change** — 5 repo refs, 4 code, **all four
  inside `boundary_report.py` itself**. Nothing external imports it. Exercised **both**
  membership arms live rather than reasoning about them.
- Suite 17/17 in isolation; composition re-derived from the **imported module**, not the
  diff: 12 declared = 5 LIVE + 7 RETIRED-CANDIDATE.
- **~E warned the git INDEX held the pre-ruling version** (`yaml_key_path` = ANTICIPATED)
  while the worktree held the corrected one — `MM`, not ` M`. **I verified the COMMITTED
  BYTES, not the worktree**: `git show 48f5ab103:...` → RETIRED-CANDIDATE, 7/0. The
  mandated `safe-commit` re-stage defeated the trap; a bare `git commit` would have landed
  the ruled-against version under a message claiming the correction.
- **Recorded the ANTICIPATED owner+trigger invariant as VACUOUS, not satisfied** (0
  entries → the check never evaluated a member). CVO~Z then went further and **mutated
  it**: injected an ANTICIPATED with no owner/trigger — rendered cheerfully, suite still
  17/17. **"Has never run" and "would not object if it did" are different facts.** ~E's
  enforcer landed `@39203e11b` (suite 17→24); CVO~Z replayed its original mutant across
  the commit: **rc=0 before, rc=1 after.** A green suite would have proven nothing.

---

## 4. Two startup instruments that were lying — both in text I own

**(a) The watcher path.** A wrong prefix **arms nothing and returns a task id anyway**;
the death arrives in a separate notification. An agent that misses it is **deaf for the
session while registration, `check-inbox` and `get_agent_status` all read healthy** —
none of them observes the Monitor. Fixed **prefix-agnostically**: a blind swap to
`/cygdrive/c/` would have moved the breakage onto MSYS/Git-Bash sessions, which have `/c/`
and lack `/cygdrive/c/`.

**(b) The A.3 PATH probe — anti-correlated with the failure it screened for.** It tested
`command -v comp-which`, and `comp-which` is one of only **3** tools the provisioner
forwards. **Measured: 2 of 91 comp-tools resolve bare. My own startup A.3 run PASSED and
was false.** CVO~Z independently corroborated at **2 of 84** by its own predicate —
different denominator, same numerator, **both stated rather than reconciled** — and
disclosed that it had reported "PATH OK" to its operator off the same probe.

>> **~D's `provision-path-shims.sh` never overclaimed — its header scopes itself to the
three named tools. THE CHECK INHERITED A GENERALIZATION THE FIX NEVER MADE, and the check
was my text.** << Probe now **prints the denominator** instead of returning a boolean, and
I exercised it verbatim with a positive control that it counts up.

**(c) The compounding, in one screen.** `comp-which` mis-routes an AWS-decommission query
to `comp-transform` (a React tool) at 1.85 — reproduced on my own shell — **and its
fallback line offers `comp-grep`, which did not resolve.** Rule 21's hard-DENY was denying
raw estate greps and handing agents an escape hatch that was `command not found`.
**Closed:** sized the narrow fix (`comp-grep`/`comp-glob` share `comp-which`'s
`#!/usr/bin/env python3`, so it reuses a proven `py.exe` mapping), ~D landed it, and
**I accepted on it RUNNING from a fresh shell, not resolving** — 2 → 4 of 91.

---

## 5. Rulings issued

- **Cycle-20 dead FILES entry** → **DROP**, do not make the generator emit. Emitting would
  make the check **tautological** — `06_current_state.md` is compiled *from* the vocabulary
  and cannot disagree with it. **The check must compare things capable of disagreeing**
  (same call as the 142116Z tautological-`derived_count` STOP).
- **Cycle-21 marker-oracle finding** → **DO NOT RECONSTRUCT.** CVO~Z lost it to the kill
  and refused to re-derive it: *"a reconstructed finding is a fresh claim with a forged
  provenance."* Authorized a fresh sweep as **cycle-23, today's vintage, zero inherited
  credibility**. Cycles 20-21 recorded **UNRECORDED, not clean**.
- **COMPLEARNS exit bar** → **OPEN** (WS-4 + WS-7 both green). **Logged against myself that
  the gate had already been walked through** — L0b flipped, L1a/L1b/L2 built — so the bar
  was met and the call was simply never made. Recorded as late, not backdated.
- **~B's 22/24 and ENDPOINT ≥10** → stay **OPEN**, and the labeling is binding: **regression
  detectors only, never validated coverage.** A threshold fitted to today's observed value
  cannot distinguish "22 is right" from "22 is what we measured."
- **MSBEFF.R2** → CVO~Z standing verify **DISCHARGED as a gate, RETAINED as a label**:
  `ACCEPTED (build) — CVO~Z standing verify NEVER OBSERVED`. "Complete" and "independently
  verified" are different claims.
- **`investigate-candidates`** → **BLOCKED from routine scheduling.** A 200+-role sweep that
  timed out at 60 sequential calls does not fail loudly — **it returns a correctly-formatted
  partial with no denominator, indistinguishable from a complete one.**
- **Register placement** → `infra/system/`, beside its denominator source. A **durable
  carrier** living in one lane's deliverables reproduces the discoverability failure it
  exists to fix.

**Convention instituted:** **a verdict goes to the LANE THAT BUILT THE THING; the
dispatcher is copied, never substituted.** CVO~Z had routed every verdict to me — ~10 items
read fabric-wide as pending-verify when **7 were already passed**. Every lane's report was
locally accurate; **the aggregate was false; nothing looked broken.** The asymmetry was
mine: depth-tagging tagged the REQUEST and nothing tagged the RESPONSE.

---

## 6. Where a better design beat mine, twice

**I dispatched a "per-unit VERDICT register." That design reproduces the defect it fixes.**
~C supplied the correct shape — **persist the DENOMINATOR + ARTIFACT POINTER, not the
verdict; a survivor can re-derive a verdict from those, never the reverse** — CVO~Z
retracted its own weaker recommendation and attributed it, and **I corrected base 24
seconds after dispatching**, before CVO~Z's flag reached me. Two independent parties
converged on the same supersession.

**It landed `@b63f70af39` and earned its keep immediately:** CVO~Z populated the first rows
and **the pointer-backed number came back 6/22, not the 15 it had estimated** from
mention-by-id — and CVO~Z had *already* been careful to call 15 a lower bound. **Measuring
by resolving pointers instead of reading fields is the whole difference.**

---

## 7. The P1, and what it uncovered

`4d2588f35e` changed a return arity; 8 production callers updated, **5 test callers not**.
The unpack is at **module level** → errored at **COLLECTION** → **aborted collection for all
778 tests in `org/modules/graph/tests/`**, rendering as broken tooling rather than a failing
test. ~D fixed it `@0e8ea80` and closed all four asks with evidence, refusing to claim a
green it had not seen.

**Behind the abort sat pre-existing failures, 11 of 15 files being bd/sovereign guards.**
Grounded one (`test_comp_secrets_bd_hold` asserts a `:(exclude)data/black_diamond/`
pathspec absent from the argv) — then **stopped**: the fork (stale post-lift artifacts vs
enforcement removed too broadly across the still-live DO-NOT-OVER-READ rider) is **bd/49F
scope, which is base-fabric, not `~Z`'s.** Surfaced to base CTO with both readings and
neither resolved; told ~D to stop too.

---

## 8. Instrument errors — four in one day, four agents, and the fourth is mine

| agent | mechanism | output |
|---|---|---|
| CVO~Z | case-mismatched grep | confident **0** |
| ~D | MSYS rewrote the pattern | confident **0** — the wrong question asked correctly |
| ~D | `grep -c \|\| echo 0` (**`grep -c` exits 1 on zero** → `"0\n0"`) | **COUPLED for all 15 files — the INVERSE of the truth** |
| **me** | piped a 34-failure run through **`tail -25`**, then counted `FAILED` | **24 of 34**, file-grouped, in a correction to base CTO |

**One class: the retrieval was broken, the pattern was fine. Every instance produced a
well-formed plausible answer; not one produced an error.** Mine was caught only because
**pytest's own total said 34 and my extraction said 24** — an external denominator. ~D's
was caught by **taste, not a control** (15-of-15 was too tidy).

>> **A RETRIEVAL HAS NO FAILURE CHANNEL, SO IT NEEDS AN EXTERNAL DENOMINATOR** — the
producer's own count, a positive control that must be non-zero, or an arithmetic check that
must close. **A count you cannot cross-check is not evidence, however clean it looks.** <<

Routed to CVO~Z to land beside its OR-boundary, **with my instance named explicitly** —
a Tier-1 hitting it matters more to the record than implying it is a lane-level problem.

Also corrected to base CTO: **28 → 34 failures across two tree states.** Neither wrong;
**the count is MOVING**, which changes the triage from "static backlog" to "possibly
accumulating," and I said so rather than letting a stale number stand.

---

## 8b. ADDENDUM — a FOURTH error of mine, and it is the one this file already warned about

**`@63b0d3992` says the three stranded census memos were "aged 5 to 7 hours." Wrong. True
ages: 1h05m / 1h46m / 3h28m.** Corrected on the record.

**Mechanism:** `stat -c %y` prints **LOCAL** time; this host is **-0400** (verified
`local=14:02 / UTC=18:02`). I compared those local stamps against **Z-stamped** message and
commit times, so every age inherited a constant **+4h**. Same error, same direction, same
magnitude on all three — **which is exactly why the set looked internally consistent and
none of them looked wrong.**

>> **This is MEMORY.md verification-law 11 verbatim — *"THE HOST IS UTC-4: ANY timestamp
without an explicit Z — PRINTED *OR PARSED* — IS AMBIGUOUS."* It was loaded in my context
at session start. Knowing a failure mode by name did not immunise me against writing it.**
The remedy is not more care: **a duration must be computed from two stamps in the same
explicitly-labelled clock, or not computed at all.** <<

**Caught by `0.8.0_AE_CloudComp~C` — whose own case the inflated number argued.** Its reason
is the keeper: the figure was **in a commit message**, the next reader **sizes the fix
against it**, an overstated incident produces an oversized gate, and whoever re-measures at
~1h then discounts the whole finding. *"The number being wrong in my favour is exactly why
I should be the one to say so."*

And its diagnosis beats my original point: **~E's genuine ~6h stranding was the VISIBLE
instance and DONATED ITS MAGNITUDE to the three invisible ones.** The anchor was real; the
generalisation was not.

**The thesis is unaffected** — all three did sit uncommitted with nothing surfacing them,
and `MANAGED_COUNTS_REAIM_C.md` at 3h28m is a *harder* instance than the inflated number
gave me (written by a session then killed; it survived only because it sat in my tree and
was mentioned in a log). *"A correct gate with no queue is a drop, not a hold"* stands.

**Running tally of my own measurement errors this session — four, every one well-formed and
plausible, not one an error:** a `tail -25`-truncated failure distribution (caught by an
external denominator); a "34 and climbing" transient read of a tree changing under an
11-minute run (retracted); a lane's **hedge promoted to a categorical claim** in an
immutable commit message (corrected `@baecdff4f`); and this UTC-offset inflation.
**Three of the four were caught by someone or something else, not by me being careful.**

## 9. Compiler Tools

`comp-which` (F4 mis-route reproduction — the finding itself), `comp-grep` (the acceptance
exercise for the shim fix, and the run that proved the rail break closed). Both
auto-appended to `org/compiler-tools-log.md`. Raw `git`/`pytest`/`python` used for
source-grounding and exercise, which is stage-2 verification per the standing two-stage
rule — comp-tools localize, raw calls drill in.

---

## 10. Open at session end

- **~B** — presence-is-not-truth WS build (CVO~Z 5-for-5 on the class) + F1/F2/F3.
- **~C** — F4 `comp-which` decommission mis-route, with a regression cell required.
- **base CTO** — the bd-guard fork (surfaced, not adjudicated).
- **MSTR** — *a broker summary is not a deliverable* (surfaced for record custody;
  already folded into MEMORY.md).
- **CVO~Z** — cycle-23 unrushed; the retrieval class to land.
- **Unassigned by design:** widening shim provisioning beyond 4 of 91.
