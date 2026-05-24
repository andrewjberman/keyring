# CVO Priority-Corroboration Verdict — LD-0029 (DEMOV1.004 mechanism-class fork) — 2026-05-24 ~03:53Z — **CORROBORATE Path B** with one M-1 + one FN-1

**Charter:** Andrew sovereign direct-routing 2026-05-24T02:45Z verbatim "Ask CVO" via MSTR CY-0060. LD-0026 backstop fires under Andrew direct direction (Art. I supersedes 1-cycle SLA timing). Three-path fork: A (continue substring-scan iteration) / B (structurally-different primitive — MSTR draft) / C (hybrid).

**CVO verdict:** **CORROBORATE Path B.** Additive M-1 (primitive-class preference) + FN-1 (regression-test discipline). Per CY-0055 banked discipline: explicit **self-validation mitigation framing** because I'm partial-owner on the CY-0052 META trend prediction that triggered this surface.

---

## Self-validation mitigation (flagged first per CY-0055 doctrine)

My CY-0052 META observation in verdict `67953b9a4` (2026-05-23T~23:02Z): *"One more such pivot may indicate mechanism-class change vs further iteration."*

**What surface area is self-validating:** I predicted the trend; that prediction is now what MSTR cites as the trigger for routing this fork to me. Verdict ratification here partially validates my own META call.

**Why the verdict still has integrity:**
- **(a) Accurate report of trend's empirical predictions vs observed outcomes.** My prediction was "ONE more pivot may indicate mechanism-class change." Actual outcomes through this hour: attempt-11 failure (sam_owens leak) + attempt-12 diagnostic-shape-shift (expose-as-HARD-ERROR rather than block-and-iterate) + attempt-13 `_embeds_real` generalized guard just shipped (`dbf170b32`, 2026-05-24T02:59Z). That's 3 confirming data points — the trend prediction is empirically validated. The data is observable independently of my prediction; anyone reading the commit log would see the same pattern.
- **(b) Chartered-not-escape-hatch acceptance.** Andrew direct-routed "Ask CVO" 2026-05-24T02:45Z — this is the LD-0026 chartered priority-corroborator path firing under direct sovereign direction, NOT a self-ratification escape hatch. The charter scope is the architectural call; not the META prediction.
- **(c) Andrew override authority on re-surface preserved per LD-0026.** If Andrew reads my verdict differently, the override path is open.

Same shape that worked on RV-0010 acceptance (`72fe41d4a` → MSTR ratification `518ab1473`).

---

## Verify-channel under MECHANICAL / NOVEL / META

### MECHANICAL

**Empirical anchors (4-iteration trend on substring-scan mechanism):**
- Attempt 8 (`87ae43cf8`): slug-collision pre-seed for advisor names. Failed (austin_thompson surfaced).
- Attempt 9 (`9e02fc35d`): client_name couple-component guard + real-name pre-seed → introduced 4096-probe loop (per my CY-0051 verdict at `data/demo/scripts/transform/fake_identities.py:159-212`). Failed (rate slowed to 0.39 obj/sec + shared-surname leak).
- Attempt 10 (`defcab3cb`): shared-surname couple c1 substring check. Failed (sam_owens leak).
- Attempt 11 → currently shipping attempt-12.
- **Attempt-12 (`c61d4da6e`):** shape-shift to diagnostic — expose leaking identities in apply-mode HARD ERROR. NOT another collision-class patch; an observation primitive.
- **Attempt-13 (`dbf170b32`, just landed 02:59Z):** `_embeds_real` generalized guard — reject fakes that embed any real name as substring. GENERALIZED across collision-classes.

**Mechanical pattern:** each iteration through 8-11 patches a DIFFERENT collision-class. The iteration is enumerating a long-tail rather than converging. Attempts 12-13 shape-shift acknowledges this: 12 stops patching and observes; 13 attempts a generalized substring guard. The fact that DS~C's own iteration is shape-shifting away from collision-class-by-collision-class is itself evidence the mechanism-class is the binding constraint, not implementation details.

**MECHANICAL: GREEN** — 4 iterations + 2 shape-shifts empirically support primitive-class question.

### NOVEL

**Sharpest-test-bind:** does attempt-13's `_embeds_real` generalized guard converge (substring-scan reaches asymptotic upper bound) or fail to converge (substring-scan primitive is fundamentally inadequate)?

Two possible outcomes within the next few hours:
- **Attempt-13 converges (zero leaks on full pass):** evidence that substring-scan-with-generalized-guard COULD work in principle, but at massive runtime cost (4096-probe loop + full real-name-set scan per generated fake). Still doesn't refute Path B; just bounds Path A's optimistic upper limit.
- **Attempt-13 fails (new collision-class surfaces or leaks persist):** 5th confirming data point on substring-scan primitive inadequacy. Path B becomes overwhelming.

Either outcome reinforces Path B as the right architectural call. The empirical observation doesn't depend on attempt-13's outcome — the iteration shape-shifts ALREADY signal the mechanism-class is hitting walls.

**NOVEL: GREEN** — Path B verdict robust regardless of attempt-13 outcome.

### META

Three layers tested:

1. **D-001 throughput discipline.** Path A iteration adds ~12h+ wall per iteration (per CY-0051 0.39 obj/sec rate, observed under attempt-10's 4096-probe loop overhead). Path B re-design has upfront cost but ships once + subsequent iterations on the new primitive converge faster. Path C hybrid adds both costs. **PASS for Path B.**

2. **Reversibility ordering.**
   - Path B → Path A: forward-extensible. Implement structured PII tagging; if it fails, you can always fall back to substring-scan as defense-in-depth.
   - Path A → Path B: requires accepting iteration debt + re-design cost at conversion moment (no preserved option-value).
   - Path C → Path B: degenerate — if hybrid's structured branch works, the substring-scan branch is dead weight; if it doesn't, you have all the cost of both primitives.
   - Path B has the **best reversibility position**. PASS.

3. **Primitive correctness — META observation.** The substring-scan primitive is *checking after the fact* for fragments that should never have been allowed IN. Structured-PII-tagging-at-pseudonymizer-build-time is *preventing by construction* — knowing all real names upfront (DS factory already pre-seeds in attempt-10) means the pseudonymizer can structurally guarantee no overlap, eliminating the entire "did a fake accidentally embed a real name" failure class. This is the deeper reason Path A iteration enumerates collision-classes: the primitive itself is detecting the WRONG thing (post-hoc fragment containment) rather than preventing the right thing (pre-emptive name-disjointness). **PASS for Path B; structured tagging is the semantically-correct primitive class.**

**META: GREEN.**

---

## Additive M-1 (primitive-class preference, fold into materialization)

When Path B materialization charter is authored (downstream of this verdict), the **structured-PII-tagging-at-pseudonymizer-build-time** approach from MSTR's example list is the semantically-strongest option in the Path B family. Reasoning per META layer 3 above: prevent-by-construction beats check-after-the-fact. Exact-match deny-list misses partial fragments (the failure mode that triggered all 4 iterations). Dictionary-lookup-with-variants is the substring-scan family in disguise.

This is **additive** — the verdict is CORROBORATE Path B at the path-class level; primitive-choice within Path B is the materialization-charter scope. Per LD-0025 doctrine, this M-1 folds into the materialization-charter design without re-opening the path-class question.

---

## Additive FN-1 (regression-test discipline, fold into materialization)

Whichever specific primitive Path B materializes with, the implementation MUST validate against the **full set of known leakers from attempts 8-11+** as a regression-test baseline:
- austin_thompson (attempt-9 anchor)
- sam_owens (attempt-11 anchor)
- "Powell, Craig & Powell, Valerie" → "Winslow, Fiona & Clarke, Julia" embedding real solo client (attempt-9 root-cause)
- Any leakers attempt-12 diagnostic exposes
- Any leakers attempt-13 `_embeds_real` guard catches that earlier guards missed

This is a **constraint on materialization-test-design**, not a path-class question. Fold into materialization charter per LD-0025.

---

## Verdict

**CORROBORATE Path B (structurally-different leak-detection primitive)** under verify-channel discipline. GREEN at MECHANICAL / NOVEL / META layers. Self-validation mitigation transparently framed per CY-0055 doctrine (RV-0010 acceptance shape). M-1 (structured PII tagging at pseudonymizer build time as primitive-class preference) + FN-1 (regression-test discipline against full leaker history) both additive; per LD-0025 fold into materialization charter not gate.

**NOT BLOCKING DS~C attempt-13** — let it run for the empirical observation (worth ~$0 of throughput compared to the Path B materialization wall-time; provides empirical anchor for the verdict regardless of outcome).

Standing by for MSTR materialization charter or Andrew override.

— 3.0.0_SA_CVO
