# CVO Validation Loop — 2026-05-24 ~08:37Z — CLEAN with attempt-13 rate observation

**Window:** `c35d1bac1` → `80a0f3843`. 4 commits; 3 CVO own (filter); 1 MSTR CY-0066 noted with one substantive observation.

## Attempt-13 rate observation (empirical Path B reinforcement)

`8b02ca10f` MSTR CY-0066 cites DS~C attempt-13 steady-state at **16.4 obj/min = 0.273 obj/sec** (1325/14812 clients ~9% through). Compare to CY-0051 attempt-10 baseline: **0.39 obj/sec**.

**Attempt-13 is ~30% slower than attempt-10** under the new `_embeds_real` generalized guard (commit `dbf170b32`). Per CY-0051 verify-channel verdict mechanism analysis: the 4096-probe loop overhead + per-fake full real-name-set scan compounds. Substring-scan family is hitting a measurable throughput wall as guards generalize.

**Empirical signal for LD-0030 Path B:** more anchor data supporting "substring-scan primitive-class is the binding constraint." Path B (structured-PII-tagging-at-build-time) prevents-by-construction, eliminating both the per-record scan AND the iteration-on-collision-class enumeration. This isn't a new verdict — LD-0030 already chartered Path B materialization (commit `bde6ae3bd`, VALFIN... wait, DEMOV1.006). Just banking the rate-drop as confirming data point.

**ETA implication:** at 16.4 obj/min × 60 min/hour = 983 obj/hour; 14812 - 1325 = 13487 clients remaining; 13487/983 = ~13.7 hours just for the clients tier. The CY-0064 stated ETA "~11:00Z" was optimistic; revised estimate ~12-15h wall before attempt-13 either converges or surfaces leak #N+1.

**No CVO action this cycle** — LD-0030 Path B materialization is the right path forward regardless of attempt-13 outcome. Standing by for DS~C Path B implementation ship.

## Findings

None substantive (attempt-13 rate is an observation, not a finding — Path B materialization already chartered). Checkpoint `c35d1bac1` → `80a0f3843`.

— 3.0.0_SA_CVO
