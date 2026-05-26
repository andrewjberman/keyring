# Portal main tree must always return to DEV after any PROD operation

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-26
**Route to:** 1.0.0_SA_CTO (rule ratification) + 2.0.0_SA_COO (DT-pod operational doctrine) + Andrew (sovereign — this is a recurring footgun he flagged)
**Brief class:** PROCESS-RULE proposal (charter-class; warrants CLAUDE.md rule + structural enforcement)
**Trigger:** Andrew direct 2026-05-26 ~16:35Z — "DT will do it, I want you to write a brief on the subject because we need to make it a rule that you always switch localhost back to DEV because this is an obnoxious footgun that keeps happening"

---

## 1. Problem statement

The portal submodule has two branches: `DEV` (development; what local `bun run dev` should serve) and `PROD` (deployed-to-server state). Promotions cherry-pick DEV commits onto PROD. The promotion mechanism uses `git checkout PROD` in the main portal worktree — and then **does not switch back to DEV when done**. The main tree stays stranded on PROD.

Consequence: anyone running `bun run dev` from `portal/` is unknowingly serving PROD source. New DEV features (e.g. today's ADVI_DEMOV1.008 demo-tenant connection) are invisible at localhost. The footgun is silent — `bun run dev` doesn't warn that the branch is PROD; the UI renders fine; only the missing feature reveals the strand.

Andrew's empirical: "I'm on localhost, is PROD on localhost again?" — yes, repeatedly.

## 2. Incident inventory

| Date | Strand event | How discovered |
|---|---|---|
| 2026-05-22 | Two promotions same day (pod 3 + SSCN) both left main tree on PROD | Caught + banked into memory `feedback_portal_prod_promotion_strands_main_tree` |
| 2026-05-26 ~16:30Z | Main tree found on PROD when DE 0.4 went to author TO-008 portal demo-tenant connection | DE 0.4 worked around via `.runtmp/portal-dev-verify` ephemeral worktree; main tree NOT restored; Andrew hit localhost expecting demo, didn't see it; flagged as footgun |

Recurrence rate: at least 3 separate strand events in ~5 days. Likely more unrecorded (silent until the next feature-add-to-DEV makes it visible).

## 3. Root cause

The existing memory `feedback_portal_prod_promotion_strands_main_tree` already captures the diagnosis: the cherry-pick-onto-PROD mechanism does `git checkout PROD` in the shared main tree with no `git checkout DEV` after. The fix recommended in that memory is to promote in an **ephemeral `git worktree add`** so the main tree never moves off DEV.

Today's incident shows the memory's recommendation isn't being structurally enforced — DT pods still do (or recently did) `git checkout PROD` in the main tree. The DE 0.4 fix-by-worktree (`.runtmp/portal-dev-verify`) is a downstream symptom: when the main tree is on PROD, DE work has to detour into a worktree. That's not a fix; it's an accommodation that compounds the cleanup debt.

## 4. Proposed rule

**Portal main worktree (`portal/`) always sits on `DEV`. Any operation that changes its branch state MUST restore DEV in the same operation.**

Three corollaries:

1. **Promotions use an ephemeral worktree, not the main tree.** Per the existing memory: `git worktree add /tmp/portal-prod-promote PROD && cd /tmp/portal-prod-promote && git cherry-pick <sha> && git push origin PROD && cd - && git worktree remove /tmp/portal-prod-promote`. The main tree never leaves DEV.

2. **If a promotion has already stranded the main tree on PROD, the agent that discovers it restores DEV.** Cheap: `cd portal && git checkout DEV` (after cleaning any stranded ephemeral worktree). The agent that touches portal next is responsible; this is everyone-cleans-up-the-kitchen discipline.

3. **`bun run dev` from `portal/` is the canonical local dev path.** Agents do NOT run `bun run dev` from a `.runtmp/portal-*` worktree to work around a stranded main tree — that hides the strand and lets it persist. Fix the strand first; then run dev from the main tree.

## 5. Structural enforcement candidates

The rule is cultural until structurally enforced. Options ranked by reliability:

**(A) Git hook on portal submodule — post-checkout warning.** When main tree's HEAD becomes `PROD`, print an `ERROR: portal main tree on PROD; switch to DEV via 'git checkout DEV'` warning. Doesn't prevent the strand; surfaces it loudly. Low effort; medium effectiveness.

**(B) Wrapper script for all PROD promotions** — `.tools/portal-promote.sh <commit-sha>` that performs the ephemeral-worktree promotion + cleanup atomically. Make this the only sanctioned promotion path; ban bare `git checkout PROD` in the main tree (a separate `git()` shadow function could refuse the operation, similar to the `headmove-guard` per `ADHC_OWNPTH.010`). High effort; high effectiveness.

**(C) Pre-`bun run dev` check** — small wrapper script (or `predev` npm script) that verifies portal main tree is on DEV; aborts with a clear message if not. Low effort; high local-symptom prevention.

**(D) CI/scheduled job that catches stranded main tree** — Andrew or COO sees a recurring "main tree is on PROD" alert. Low effort; lagging signal.

Recommended combination: **(A) + (B) + (C)** — three nets at three different moments (post-checkout warning, promotion-script enforcement, local-dev launch check). (B) prevents the strand at the source; (A) + (C) catch any that slip through.

## 6. Routing recommendation

- **CLAUDE.md rule addition** — promote this rule to a numbered Critical EC2 Deployment Rules-class entry (rule 19 or co-located with rule 9/10 EC2 deployment context). One-paragraph rule + reference to the existing memory. **ws CTO authority.**
- **Structural enforcement implementation** — author a small project: `.tools/portal-promote.sh` (option B) + `.tools/portal-predev-check.sh` (option C) + portal-submodule post-checkout hook (option A). **DT-pod owns the script(s); CTO authors PRD; COO decomposes.**
- **Memory update** — extend `feedback_portal_prod_promotion_strands_main_tree` with the 2026-05-26 incident + reference to this brief + reference to (eventual) CLAUDE.md rule + structural-enforcement tools. **DE/whoever-discovers next strand can update.**

## 7. Asks of ws CTO

1. Ratify the rule + sequence the CLAUDE.md addition (one-paragraph entry)
2. Author a PRD for the structural-enforcement scope (small; options A + B + C; ~2-4h DT wall) — or rule out structural enforcement and accept the cultural-rule + memory as sufficient
3. Confirm routing to COO for DT-pod decomposition once PRD scope locked

## 8. Asks of ws COO

1. After CTO PRD: decompose into TOs for DT-pod (whichever DT is live)
2. Add a `/spot-check` cycle check: scan `git -C portal symbolic-ref HEAD` periodically; flag if `refs/heads/PROD` for >N minutes outside an in-flight promotion window
3. Stand-down the `.runtmp/portal-dev-verify` worktree once main tree is restored to DEV (cleanup debt from today's incident)

## 9. Open questions

- **Q1 (CTO/Andrew):** Is the cultural rule alone sufficient, or is structural enforcement (options A+B+C) warranted given the 3-in-5-days recurrence rate? My lean: structural — the recurrence rate is the empirical "cultural is insufficient" signal. ~2-4h DT effort vs ongoing silent-footgun cost.
- **Q2 (CTO):** Should `.tools/portal-promote.sh` replace the existing DT promotion path entirely (i.e., remove the bare-`git checkout PROD` capability for DT pods via shell shadow), or coexist as opt-in? Lean: replace + shadow-ban — partial adoption keeps the footgun alive.
- **Q3 (Andrew):** Any portal-submodule operations other than promotions that move main tree off DEV? (E.g., hot-fix scripts that branch from PROD?) If yes, the rule needs a carve-out enumerating them; if no, the rule is absolute.

## 10. References

- Memory: `feedback_portal_prod_promotion_strands_main_tree` (canonical; created post-2026-05-22 incident)
- Today's incident anchor: ADVI_DEMOV1.008 TO-008 ship (portal/DEV commit `03a85441`); main tree found on PROD (`0be05530` top); DE 0.4 detoured through `.runtmp/portal-dev-verify` worktree
- Sister structural-enforcement pattern: `ADHC_OWNPTH.010` `git()` shell-shadow for destructive HEAD moves (precedent for option B's git-shadow-ban approach)
- Existing portal commit-discipline rule: CLAUDE.md "Portal" + "Git" sections; rule additions land alongside
