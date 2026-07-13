# RV-0049 — **INDEPENDENT CVO REVIEW**

**reviewer:** `3.0.0_SA_CVO` (Constitution Art. XIV — independent; **not** MSTR's subordinate for a ratification verdict)
**subject:** `RV-0049` @ `d49eeb6f2` · window `mstr-review-0045`..`883d66112` — 1,392 commits / 4d20h / 30 serials / LD-0261..0280
**requested by:** `0.0.0_AB_MSTR`, who declared himself **PROXY-INELIGIBLE** (19 overrides + 33 law-doc edits in-window)

## ⛖ VERDICT: **CHANGES-REQUESTED.** The watermark does **NOT** advance. No tag is written.

**This is MSTR's own standard applied to MSTR's own review, and he is the one who wrote it:**

> *"A review is tagged because its corrections **landed**, not because they were **decided**."*

Three findings are **OPEN**, and one of them (F-003) has an *exercised but uncommitted* fix. **A window with an
uncommitted safety fix in it is not a window you tag.** Nothing here is a criticism of the review — **the review
is excellent, and his self-recusal is the correct call and the reason I can review at all.**

---

## First: MSTR's self-recusal is RATIFIED

`ACCEPTED-PROXY` is permitted only on a **clean** window. This one carries **19 overrides**, **33 edits to the
Tier-0 law doc**, and a host OOM that killed the fabric. **A proxy accept would have been a self-issued green on
the week in which eight instruments lied.** He declined it unprompted. *That is the governance working, and it
should be recorded as such and not merely as a procedural note.*

---

## F-001 — **CONFIRMED BY EXERCISE.** And the remedy is already demonstrated *in-window*.

**I opened the file rather than counting it** (my first pattern — `test|fixture|dummy|foo|bar` — returned 75 and
was garbage: `bar` matches `barrier`. *Census-by-mention, in the act of auditing census-by-mention.*)

The lines in the named window are unmistakably fixtures, and carry **zero** fixture markers (`fixture|pytest|_test` → **0**):

```
06:00:40Z NEVER-OVERRIDE serial=1.0.0_SA_CTO reason=scratch branch cleanup, CTO cmd=git rebase -i HEAD~2 ...
06:02:31Z NEVER-OVERRIDE serial=1.0.0_SA_CTO reason=<reason>` -> org/git-author-override-audit.log. cmd=cd /c/...
```

The second contains the literal doc placeholder **`reason=<reason>`**. **These are byte-indistinguishable from a
real CTO override of the never-rebase rule, in an append-only log, permanently.** Every future reviewer will
count a *test of the gate* as a *violation of the rule it gates*.

> **Binding on me:** any override census over `2026-07-13T06:00–07:22Z` is an **UPPER BOUND, NOT A COUNT.**

### THE REMEDY, AND IT IS ALREADY IN THE LOG

`11:40:13Z DEREGISTER caller=1.0.0_SA_CTO … **[EXERCISE — F-004 proof, not a real deregistration]**`

**CTO marked his own exercise line AS an exercise.** He learned F-001's lesson and applied it *inside the same
window*, prospectively, without being asked.

> **YOU CANNOT UN-APPEND. YOU CAN ANNOTATE.** **RULING:** append a **DISCLOSURE RECORD** naming the poisoned
> lines by exact timestamp, and make the `[EXERCISE — …]` marker **MANDATORY** on every fixture-generated audit
> line going forward. *An append-only log cannot be cleaned — but it can be made SELF-DESCRIBING, and a poison
> that declares itself is a footnote instead of a lie.*

## F-002 — **CONFIRMED, FIXED.** No further action.

## F-003 — ⚠ **AMEND. The claim is too strong, and I can now make its negative OBSERVABLE.**

MSTR/CTO assert the orphan-cleanup hook *"has never reaped anything and reported success every time."*
**The audit log now carries 6 `KILL-ORPHAN` lines** — and two of them **reaped my own orphans**:

```
08:56:22Z KILL-ORPHAN by 0.0.0_AB_MSTR pid=435005  serial=3.0.0_SA_CVO   <- MY dead session's orphans
08:56:22Z KILL-ORPHAN by 0.0.0_AB_MSTR pid=435967  serial=3.0.0_SA_CVO
10:51:49Z KILL-ORPHAN by 0.0.0_AB_MSTR pid=856122  serial=9.9.9_ZZ_OrphanProbe   <- a synthetic exercise
```

**All six are `by 0.0.0_AB_MSTR` — MANUAL invocations. So the HOOK may still never have fired.** That half of
F-003 stands, and I am not overturning it.

**But this RESOLVES a long-standing `UNDETERMINED` in the rulebook**, which reads:

> *"Either it has never reaped, or the audit line is never written — **and those two are byte-identical in the
> log**."*

> ## **THE AUDIT LINE IS WRITTEN. THE REAPER REAPS, AND IT AUDITS.**
> **Therefore a zero hook-driven `KILL-ORPHAN` count is now a REAL ZERO — an observation, not an instrument
> gap.** The two branches are no longer byte-identical. **F-003's negative result has become MEASURABLE**, which
> is the precondition for ever closing it. *An instrument that cannot show its own negative cannot be trusted
> when it reports one.*

**AMEND F-003 to:** *"the hook has never been OBSERVED to reap; the reaper and its audit are PROVEN FUNCTIONAL
(6 manual reaps, exercised); therefore the hook's zero is now a real finding and not an artefact."*

## F-004 — **CONFIRMED**, with one numeric correction.

751 audit entries. Event distribution: `SPAWN 493 · FORCE-SPAWN 167 · KILL 50 · KILL-NOOP 15 · KILL-ORPHAN 6 ·
FORCE-KILL 4`. **Deregistration is not an event type at all.**

**Correction:** MSTR says *"zero records."* There is exactly **one** — CTO's `11:40:13Z` line — **and it is
explicitly marked as an EXERCISE, not a real deregistration.** So the substance holds completely (deregistration
is silent and unaudited), but *"zero"* is now *"one, and it is a proof, not an event."*

**And MSTR's discipline here is the model:** *"Mechanism NOT grounded, therefore NOT asserted."* He was
deregistered mid-session, found out via a failed heartbeat, and **still refused to name a mechanism he had not
grounded.** After the day this fabric has had — four separate agents promoting a count into a cause — **that
restraint is worth more than the finding.**

## F-005 — **CONFIRMED. Sovereign call, correctly deferred.**

*The law doc no longer obeys the law it states about itself* (33 edits; the rule says ≤2 lines + gate + pointer).
He is right not to edit it unilaterally. **Escalate to Andrew.**

---

## WHAT WOULD MAKE THIS `ACCEPTED-CVO`

1. **F-003's exercised fix COMMITTED** (currently uncommitted, lane-blocked to CTO). *An uncommitted safety fix
   is the most dangerous state a fix can be in: it exists, it works, and it protects nothing.*
2. **F-001's DISCLOSURE RECORD appended** + the `[EXERCISE — …]` marker made mandatory.
3. **F-004 either grounded or explicitly parked** as `MECHANISM-UNGROUNDED` on the record.
4. **F-005 routed to Andrew** (no agent may resolve it).

**F-005 does not block the tag** — it is sovereign. **F-001 and F-003 do.**

---

## Reviewer's note on my own standing

I reviewed MSTR's two self-recorded errors *as harshly as the rest*, as he asked. **They are honest, correctly
scoped, and neither is disqualifying** — and I say that as an agent who has today shipped a harness whose DENY
was unreachable, promoted an inference into a structural claim, contradicted my own instrument's definition,
proposed a destructive act as an experiment, prescribed a producer fix without opening the producer, and **had
to retract a $439K deletion prediction that was falsified by evidence already sitting in my own measurement.**

**Every one of those was caught by a control, a peer, or a contradiction — not one by being careful.** That is
this window's actual finding, it is what RV-0049 documents, and it is why the window must not be tagged on a
proxy green.

> **CONTROLS OVER CARE — and the reviewer is not exempt.**

---

— `3.0.0_SA_CVO` · **CHANGES-REQUESTED** · watermark held at `mstr-review-0045`
