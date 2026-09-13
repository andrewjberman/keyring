# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 56 (covers ticks 54-56)

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T07:40:40Z**
Tick 53's log is `@41591aab04`, committed `2026-09-13T03:04:00-04:00` (author time, not the
filename). **Ticks 54 and 56 were QUIET. Tick 55 was not, and this log exists to discharge it.**

> **WRITTEN BECAUSE A FOLD WAS PROMISED AND IS NOW DUE.** Tick 55's act was folded with the words
> *"the next written log names Z-S51"*. Three ticks have passed. The 6-tick floor is not reached, so
> nothing forced this -- but **deferring a folded act a second time is how "fold" becomes "never"**,
> and this seat named that drift itself two ticks ago.

---

## 1. `Z-S51` `@ad577a7cd2` -- UN-PARKING AN ITEM THIS SEAT PARKED FOR A BAD REASON

At 22321 this seat filed the `to-pipeline-gate` full-stem defect as tooling, **on the stated ground
that "the workaround is sound."** `2.0.0_SA_COO~Z` (22323) measured that ground and it does not hold.

**All three mechanisms verified at source by this seat rather than relayed:**
```
proof-of-spec-check.py:281-283  "the artifact must be TOUCHED by the instance's own commit ...
                                 Present at <c> but not touched by it -> the CCX violation"
                                 -> IT GRADES ON COMMIT HISTORY, NOT CONTENT
to-pipeline-gate.py:1602-1603   stem = basename(rel).rsplit(".md")[0]  -> derived from the FILENAME;
                                 the order's own <proof_of_spec> block is never consulted
to-pipeline-gate.py:1629-1633   refuses on rc != 0 -- it RUNS the validator, not a presence test
```
⛔ **So once an instance's PENDING artifacts are committed they are clean and therefore UNSTAGEABLE:
no future commit can touch them, and a byte-identical copy at the derived path can never be
CO-COMMITTED.** `0.9.0_WK_POSN_ASTTAX~16` proved identity on four instruments (md5, sha256, `wc -c`
37964 both sides, `cmp` rc=0) and **the copy still graded INVALID with 2 CCX while the source graded
VALID.**

⚠ **WHERE THIS SEAT WENT WRONG, named precisely rather than softened.** `~17` could write both paths
only because ITS artifacts had not yet landed; `~16`'s had. **A remedy that holds before a commit and
not after is not a workaround** -- and this seat generalised from the one visible instance without
asking which side of that line it sat on.

⭐ **AND IT INVERTS THE PARKING ARGUMENT ON ITS OWN TERMS.** The park cited Andrew's 02:22Z ruling
that tooling must not disrupt the work of the fabric. **This defect BLOCKS the work of the fabric**,
so fixing it is the work rather than a disruption from it.

**DISPOSITION: PARKED -> OWNED BLOCKING ITEM of this seat**, with a trigger rather than an intention.
**Fix adopted** (`2.0.0_SA_COO~Z`'s REC, because it removes the CLASS not the instance): make the
gate's derivation read the order's own `<proof_of_spec>` block instead of the filename stem.
**Trigger, both conditions required:** (i) POSN round 4 out of mid-flight -- a change to which
instance path is REQUIRED can refuse a worker's flip mid-run, and workers are flipping now; (ii) an
estate-wide A/B against HEAD's gate, refusals counted both ways with a positive control, before
anything lands. **Not promised tonight**, and 22323 explicitly did not propose it as tonight's work.

⭐ **THE MOST REUSABLE THING IN THE EXCHANGE IS NEITHER SEAT'S ANALYSIS.**
`0.9.0_WK_POSN_ASTTAX~16` was **instructed by its own issuer** to place the copy, **measured why the
instruction was wrong, and filed a row instead of complying.** Had it obeyed, the order would have
acquired a permanently-INVALID instance and the refusal text would have mutated into something
reading like a worse and different problem. **A worker refusing a wrong instruction with a
measurement is a control no gate provides.**

## 2. WHAT WAS QUIET, AND ONE FILTER FAULT FOUND IN THE QUIET

Ticks 54 and 56: no CTO limb owed on either project -- every slug has its analysis, both PRDs
ADMITTED with both halves signed current. POSN round 4 draining under its own power (13 -> 14
complete across the window). AMGT unchanged at 47 of 47 with L8/L9 awaiting the CVO keystroke.

⚠ **A COUNT THIS SEAT PUBLISHED TWICE WAS A FILTER ARTIFACT.** `ls -1 <inbox> | grep -v '^read$'`
reported **1 undrained item** on two ticks; `ls -1F` plus a `grep -v '/$'` reports **0**. `ls -1`
emits the directory as `read` on this device only sometimes, so the anchored filter missed it.
**Small, but it read as an unhandled message sitting in this seat's inbox**, which is exactly the
kind of number that gets acted on. Corrected by asking for FILES rather than ENTRIES.

## 3. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 2 RESERVED · NO PITCH   (all-reserved tell does not fire)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  EXECUTING  REACHABLE  0 OPEN of 47 -- L8/L9 awaiting the CVO keystroke, with Andrew
  POSN_ASTTAX  EXECUTING  REACHABLE  5 OPEN of 19 -- round 4 draining
  UNREACHABLE: 0   HELD-AT-STOP: not reached
```
`3.0.0_SA_CVO~Z` re-measured: `bridge-state.json` still **ABSENT**, seat alive as `python`, unbound.
**No nudge and no second escalation** -- mail cannot reach an unbound seat, MSTR said so, and the
keystroke is with Andrew.
**Push state:** `origin/SITEZ ad577a7cd2`, local **0 ahead** -- everything this seat has written is
published. `HEAD:portal e85f6eb84f`, unmoved. No TO cut, no dispatch, no apply, no retag, no deploy,
no promote.

## Compiler Tools

`proof-of-spec-check.py` and `to-pipeline-gate.py` read at their cited lines before accepting a
measurement that reversed this seat's own disposition · `ls -1F` with a trailing-slash filter to
separate directories from files, after an anchored `grep -v '^read$'` produced a false count twice ·
`git log -1 --format=%aI` for the log cursor and `git log --author --since` to enumerate this seat's
acts in the window · the fence-line channel reader admitting both block shapes · `git status
--porcelain` before the append · `date -u` at the write · post-commit `git show HEAD:` with a `Z-S99`
negative control · `safe-commit.sh -F` with a non-shell-written message file · short send subjects.
