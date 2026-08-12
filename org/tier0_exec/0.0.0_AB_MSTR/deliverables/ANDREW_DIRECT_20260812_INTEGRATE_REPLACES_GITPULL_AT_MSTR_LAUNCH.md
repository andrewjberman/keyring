# ANDREW-DIRECT 2026-08-12 — `/integrate` REPLACES `/git-pull once` AT MSTR LAUNCH

**Channel:** laptop terminal, direct to `0.0.0_AB_MSTR`
**Date:** 2026-08-12 (during the first completed `/integrate` run, merge `4c7f053632`)
**Recorded by:** `0.0.0_AB_MSTR` · **Broadcast:** site Z MSTR (bus), COO/CTO/CVO on next liveness

---

## THE RULING — VERBATIM, NOT PARAPHRASED

> *"Also something I want to bring in to the mstr launch script is not just blindly running git
> pull, its better to run /integrate as a joint fabric parity assessment and this parity can either
> be just an assessment (default), or it can be /integrate merge, which is assess and proceed the
> merge."*

## WHAT IT ESTABLISHES

1. **The MSTR load step is `/integrate`, not `/git-pull once`.** The act at load is a **joint
   fabric parity assessment**, not a same-branch pull.
2. **Two modes, and the DEFAULT IS ASSESSMENT.** Bare `/integrate` measures and reports —
   **merges nothing, pushes nothing, resolves nothing.** `/integrate merge` is assess-and-proceed.
3. ⚠ **THIS INVERTED THE PRIOR DEFAULT.** Bare `/integrate` previously ran Steps 0–7 *including
   the merge and the push*. Any agent working from a cached memory of the old default will expect a
   reconcile that did not happen — **so the assessment states its own terminal state explicitly in
   its closing line; it is never inferred.**

## THE GAP I CLOSED RATHER THAN INHERITED (flagged to Andrew, adopted from site Z)

**`/git-pull` and `/integrate` answer DIFFERENT questions.** The pull fast-forwarded the local
branch to its own remote — **same-branch currency**. `/integrate` reconciles CLOUD vs SITEZ —
**cross-branch parity**. A straight swap would have silently dropped same-branch currency, which is
the exact defect `/git-pull once` was added to close (sessions opening N commits behind, every
startup evidence read wrong-by-omission).

**RESOLUTION — site Z's shape, which is better than my first one and was adopted over it:**
do **not** place the pull *beside* `/integrate` as a second step. Make it **Step 1b, a PRECONDITION
of the assessment**, because —

> **A PARITY ASSESSMENT COMPUTED FROM A STALE LOCAL REF IS WRONG THE SAME WAY A SHALLOW CLONE IS
> WRONG.** Both produce confident, well-formed divergence numbers off an incomplete graph. Step 1
> already closes that for *history depth*; Step 1b closes it for *branch currency*.

So the pull is **not replaced — it is ABSORBED as the thing that makes the assessment
trustworthy.** That framing is load-bearing: an integrator who skips it does not miss a nicety,
they **get wrong numbers** — the only kind of enforcement that actually holds.

### SEVERITY IS ASYMMETRIC BY DEVICE (carried forward from Andrew-direct 2026-07-30)

| device | Step 1b behavior |
|---|---|
| **NON-PRIMARY (site Z / any `~Z`)** | **FAIL LOUD.** The pull IS the sync guarantee; a failed or skipped one is a **REAL FINDING**. That machine is downstream of a tree that commits and pushes continuously. |
| **PRIMARY (laptop)** | **WARN.** Incidental hygiene — "we are effectively source"; a deferral past live uncommitted seat-work is consistent with intent. |

⚠ **A laptop pull-deferral is NOT precedent for a site-Z one.**

## THE MEASURED INSTANCE THAT MOTIVATES IT (site Z, 2026-08-12 ~1320Z)

`/git-pull once` ran per the launcher and printed `596254785b..91e1854258  CLOUD -> origin/CLOUD`
**on screen**. The seat then ff'd its own branch, saw 0 behind, and moved on — **never looking at
CLOUD.** The other fabric had advanced ~34 hours and the startup was **structurally incapable** of
noticing: the act performed was same-branch currency and the question that mattered was
cross-branch parity. **The information was on the screen and the procedure had no slot for it.**
That session then spent four hours discovering the divergence by hand.

This is precisely Andrew's *"not just blindly running git pull"* — **and it is not hypothetical.**

## CARRIERS UPDATED (all three, same commit)

| carrier | change |
|---|---|
| `.claude/skills/integrate/SKILL.md` | Step 1b added (precondition + severity split + the 1320Z instance); invocation table inverted to assess-as-default + `merge`; frontmatter description names the launch role and both modes |
| `.tools/ajb.ps1` | MSTR directive item 3 rewritten; design-rule comment block records the supersession. **Parse-checked (0 errors) AND exercised** — MSTR row renders, CTO/COO rows unaffected |
| `org/XXX.md` Step 1b-F | MSTR row: load step is `/integrate` assess-only; the older `/git-pull once` clause marked SUPERSEDED with its never-arm-the-loop half still binding |

## SCOPE — WHAT THIS DOES *NOT* DO

- **It does not authorize a merge at launch.** Assess-only is the load form, deliberately.
- **It does not retire `/git-pull`.** The skill still exists for its own uses; what changed is the
  MSTR *launch step*.
- **It creates no gate.** Nothing is held on an approval; the assessment reports and the MSTR acts.

## RELATED — the method finding from the same run

Site Z's self-catch, adopted into `/integrate` Step 3 and recorded as **theirs, against their own
analysis**: *a conflict hunk shows the whole contested region from both sides, including lines
neither side touched — so it answers "what region is contested," never "which rows did each side
change."* The instrument that answers the real question is
`git diff --unified=0 $BASE origin/<side> -- <file>`, comparing BASE-side ranges. Designed-domain
mismatch (Rules 22/22a class): reading the hunk more carefully cannot fix it, and it fails by
producing **a plausible escalation to a law owner who is not needed** — an unbounded delay on a
quiet fabric.
