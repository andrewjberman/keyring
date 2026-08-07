---
name: feedback-comp-find-replaces-grep-rollout-hold-lifted
description: "Andrew-direct 2026-08-07 -- the rollout hold on comp-find replacing grep is LIFTED. Rule 21 repoint is GO at CTO. comp-read's HUD is NOT covered by this lift."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3ac52682-b124-4e3e-8f7c-dd090241b4e9
  modified: 2026-08-07T04:35:33.623Z
---

**Andrew-direct 2026-08-07 ~0055Z, `3.0.0_SA_CVO~B` terminal, VERBATIM:**

> *"(A) lift it. ALso CTO~D is working on stuff with CVO~C and CRO Base."*

**"(A) lift it" ANSWERS the `/open-calls` BLOCKING item: "Lift the hold on comp-find replacing grep
— yes or no?" ANSWER: YES.**

**WHAT IS NOW AUTHORIZED:** the Rule 21 law-surface repoint — `comp-grep` / `comp-glob` →
`comp-find` — at `1.0.0_SA_CTO`. This discharges the standing hold he set 2026-08-06 (*"I need to
know that it works before instituting on the fabric as a whole, cant just route it if its broken or
otherwise suboptimal"*), on the evidence he required: TRIAL-1, run by a non-author
(`0.8.0_AE_CloudComp~A`, @541f73019), returned comp-find **PASS** — *"I would keep using it with the
mandate lifted, unreservedly."*

⛔ **SCOPE — THIS LIFT IS comp-find ONLY. IT DOES NOT COVER comp-read's HUD.** Two tools, two
decisions, and only one is lifted. The HUD remains unwired and its trigger is measured-and-failing
(89% firing rate on the option-3 spec). **Do not read a comp-find lift as HUD authorization** — they
arrived in the same conversation and are the easiest pair in this program to conflate.

**THE EXECUTION MECHANISM, non-negotiable and it has a live precedent for failing:**
**BOTH LAYERS MOVE IN ONE WINDOW — the Rule 21 LAW TEXT *and* the hook's FALLBACK RUNNER.** On
2026-07-29 the rail denied a raw grep, routed the agent to `comp-grep`/`comp-glob`, and those did
not resolve: **the gate FAILED OPEN AT ITS OWN DESIGNATED FALLBACK, immediately after reporting
healthy.** An agent hitting a denial that names a tool the law text does not mention has no route
out. Rule 21's deny is ARMED, so the swap is announce-then-enforce, never silent.

**SECOND HALF — A CORRECTION TO A CLAIM I MADE, and the lesson is mine:** I reported `1.0.0_SA_CTO~D`
as IDLE capacity in `/open-calls`. **It is not.** Andrew: it *"is working on stuff with CVO~C and CRO
Base."* I read its BROKER SUMMARY ("Standing by for Andrew's priority task") and treated it as
current. **The stimulus-scan rule is explicit that GIT WINS OVER THE BROKER SUMMARY** — an agent
heads-down looks stale on the broker and is ACTIVE in git — and I applied that rule correctly to
other agents in the same sweep and not to this one. **A stale self-report read as live state is the
producer-self-report class (Rule 22a), applied to an agent instead of a pipeline.** Reporting free
capacity that is not free invites a dispatch onto a working seat.

**How to apply:**
- Before reporting an agent IDLE, cross-check its recent commits, not just its broker line. **The
  broker summary is aspirational; the commit log is behaviour.**
- Note also that `3.0.0_SA_CVO~C` appears in his sentence and was **not** in my `get_live_agents`
  read — so the live roster I reported was incomplete as well as stale. **Never present a fabric
  roster as complete on one broker call.**

Related: [[feedback_hud_branch_a_query_less_no_generated_questions]] (the tool this lift does NOT
cover), [[feedback_comp_read_hud_color_comp_find_replaces_grep_and_the_mandated_field_trial]] (the
hold this discharges).
