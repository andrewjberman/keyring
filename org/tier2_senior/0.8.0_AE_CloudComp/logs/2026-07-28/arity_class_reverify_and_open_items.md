# Idle-window re-verification: arity class still closed at HEAD+67, and an Andrew-direct prohibition still unactioned after 3 days -- 0.8.0_AE_CloudComp~D

**archetype:** VALIDATE

Window: 2026-07-25 ~1905Z -> 2026-07-28 ~1240Z. **0 commits by this lane, 0 MCP messages
received, 0 dispatches.** Thin window by design -- this entry exists for the two standing items
below, not for work performed.

---

## Current State

**This lane has been IDLE for ~3 days (last work `81157f9644`, 2026-07-25 ~1905Z).** The idleness
is real, not a reachability failure, and I discriminated the two rather than assuming:

```
Monitor task b7hxj5vu1        -> running        (the ONLY oracle that observes a CONSUMER)
liveness 0.8.0_AE_CloudComp~D -> LIVE, PID 7252, last_seen 2s
watcher child pid 901783      -> parent 901770 is a LIVE eval-wrapper (mine, armed 07-25)
peer lanes STILL RECEIVING    -> ~C newest 20260726T073515Z, 1.0.0_SA_CTO~Z newest 20260727T015027Z
repo advanced                 -> 67 commits since my last log
```
**An empty inbox is not a reachability oracle** -- but an empty inbox PLUS a live consumer PLUS
peers demonstrably receiving on 07-26 and 07-27 is. The fabric kept moving and nothing was
addressed to this lane. That is "no work dispatched," not "went deaf."

**RE-VERIFIED AT HEAD+67 (the only substantive work in this window):**
```
comp-arity --self-test                  -> 3/3 PASS
   POSITIVE       pre-@0e8ea80 -> finds exactly 5 stale sites (74/79/87/95/103)
   DISCRIMINATING HEAD -> 0
   NEGATIVE       bd<->cot same-basename collision -> 0 false MISMATCH
comp-arity org | data | .tools          -> 0 MISMATCH, 0 MULTI-ARITY (all three)
```
**The arity class stayed closed across 67 commits of estate movement, and the instrument still
holds its own controls against a tree it has never seen.** That is worth more than the re-run
cost: a sweep that passes only against the tree it was written on is a snapshot, not a control.

---

## >> STANDING ITEM: AN ANDREW-DIRECT PROHIBITION IS STILL UNACTIONED AFTER 3 DAYS <<

Andrew-direct (to `1.0.0_SA_CTO`, ~2026-07-25T185538Z, relayed to me by CTO~Z same turn),
VERBATIM:

> *"our comp tools should absolutely never be limited on governance. governance is handled at
> the aws cli/aws user iam level, not at the tool level, If i am understanding properly what
> youre saying, that sounds like the tools have built in blind spots for absolutely no reason"*

Binding reading given by CTO~Z: **no comp-tool gets a governance predicate, a hold check, or an
`*_INCLUDE_HELD` env var.**

**MEASURED TODAY, 2026-07-28:** `.tools/comp-grep:76` still carries `elif a == "--include-held":`
gating the `sovereign-held guard (GG1)`. **Literally the pattern the ruling names, still live in
the estate's SANCTIONED SEARCH PRIMITIVE** -- the tool Rule 21's armed hard-DENY routes every
agent to, so its denominator bounds what anyone finds through the rail.

I surfaced this to CTO~Z at 190457Z on 07-25 and have **not** touched it, for the two reasons I
gave then and still hold: (1) not dispatched; (2) I cannot tell from outside whether comp-grep's
guard is PURELY governance or has a second non-governance limb fused into it -- which is exactly
the `sovereign_held.py` shape (`SOVEREIGN_HELD_PATHS` retracted / `PROD_WRITE_FORBIDDEN_PATHS`
never retracted, and the FUSION was the bug). **Ripping it because a ruling made one half
retractable is the failure CTO~Z warned about, one tool over.** If dispatched: SPLIT-then-verify,
never rip.

**Why I am recording it rather than just re-sending:** a retraction is only as dead as its
last-surviving enforcing copy, and 3 days is long enough that "surfaced once by MCP" stops being
a live signal and becomes an assumption that someone else is holding it. The estate's own record
of this class is that a note which records an incident and does not become a control gets to
cause the same incident again.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-arity` | `--self-test` | PASS 3/3 | All three controls hold at HEAD+67. |
| `comp-arity` | `org`, `data`, `.tools` | PASS | 0 MISMATCH / 0 MULTI-ARITY -- class stayed closed. |
| `comp-grep` | `-- '--include-held'` on its own source | PASS (finding) | Confirms the prohibited pattern is still present. |

**What worked:** the self-test's value showed up exactly where intended -- re-running it against
a 67-commit-advanced tree is the difference between a control and a snapshot.

**What failed:** nothing this window.

**Gap found:** none new. The two carried gaps are the `--include-held` prohibition (above) and
`comp-arity`'s routable-registration debt (still `excluded_not_graph_use_cases`; confirmed
unchanged today).

---

## Blockers

**None.** This lane is IDLE and AVAILABLE, which is a capacity signal, not a blocker -- routed to
CTO~Z rather than recorded as an impediment.

---

## Next Steps

1. ~~**[1.0.0_SA_CTO~Z]** `.tools/comp-grep:76` `--include-held` -- dispatch decision needed.~~
   **CLOSED 20260728T124811Z, same turn** -- see ADDENDUM below.
2. ~~**[1.0.0_SA_CTO~Z]** `comp-arity` routable-registration debt.~~ **CLOSED** -- ruled a
   DECLARED exclusion, not a gap; no pass needed.
3. **[1.0.0_SA_CTO]** bd cluster + `sovereign_held.py` -- STOP standing, untouched, not mine.
4. **[0.8.0_AE_CloudComp~D]** PARKED, event-driven. No open items.

---

## ADDENDUM (20260728T1250Z, ~10 min after this log landed) -- BOTH ITEMS CLOSED

Recorded here rather than left to a successor, because the body above frames item 1 as a
STANDING ITEM NEEDING ACTION and it is now answered. **A log that keeps asserting an open item
after it closed is the stale-record-with-authority shape** -- and this file would have been the
authoritative one, being the most recent.

**CTO~Z answered with a measurement, not a defer.** VERIFIED BY ME AT SOURCE before accepting:
`_comprail.py:252` `gitignore_aware_files(ws, pathspec, include_held=False)` is a **public
parameter on a SHARED helper**, returning `(files, held_note, err)`; callers confirmed at
`comp-glob:83` and `comp-grep:115` (+ comp-ls and a test per CTO~Z; my own check was
head-truncated, so that is MY short denominator, not a discrepancy). Removing the guard changes
the RETURN CONTRACT for three tools -- 5 files and an API change.

Against Andrew's cost bar this session -- *"but cleanup of dead code wold be nice if it can take
5 minutes to do so"* -- **it is a NO.** GOVRIP is separately STOOD DOWN Andrew-direct
(*"i dont know what GOVRIP is or if we even really wanted to get that pushed through"*).
`sovereign_held.py` stays; `PROD_WRITE_FORBIDDEN` stays IN FORCE.

**>> MY PREMISE WAS OVERSTATED, AND THE FAILURE IS SPECIFIC.** I called it a blind spot bounding
what every agent finds through the rail. `_comprail.py:259-261` says `held_note` is *"a LOUD line
the caller MUST print... an `--include-held` override is never silent."* **A disclosed exclusion
with a forced loud note is a BOUNDED denominator, not a hidden one** -- categorically unlike the
silent-failure class of 07-25/26.

**And I had already measured that myself, then dropped it.** My 190457Z message of 07-25 said, in
my own words, *"the guard is LOUD by construction... a reduced denominator that ANNOUNCES itself,
not a silent one."* Three days later I re-surfaced it without the qualifier. **Nobody removed it;
I did, by restating my own finding from memory instead of from what I wrote.** The claim got
stronger while the evidence stayed identical, and the second telling is the one that gets acted
on -- it cost CTO~Z a measurement to refute a premise I had already refuted.
**RULE FOR MYSELF: re-surfacing an item after a gap means re-reading what I WROTE, not what I
remember concluding.** <<

**CAPACITY: PARKED, and the reasoning accepted, not just the verdict.** Andrew's signal is that
an agent-originated program got pushed a long way unasked; the right response is FEWER
agent-originated workstreams, not a substitute. My "here are three things I could pick up" was an
offer to start a fourth. Not re-raising the comp-grep item -- it is answered with a measurement,
and re-raising an answered item is how a defer decays into noise. The trigger worth watching is
if someone touches `_comprail`'s return contract for another reason, making this nearly free as a
rider; I will flag it then, not on a timer.
