---
name: feedback_hud_branch_a_query_less_no_generated_questions
description: Andrew-direct 2026-08-07 -- the comp-read HUD renders the QUERY-LESS form (Branch A); no auto-generated questions. A panel that asserts nothing cannot be wrong; a guessed question fails invisibly.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3ac52682-b124-4e3e-8f7c-dd090241b4e9
  modified: 2026-08-07T00:27:29.563Z
---

**Andrew-direct 2026-08-07 ~0025Z, `3.0.0_SA_CVO~B` terminal, VERBATIM:**

> *"I think Branch A is safer for this"*

**THE FORK HE WAS RULING ON.** When the comp-read HUD fires on a file an agent is looking at,
either:
- **BRANCH A — render the QUERY-LESS form.** No question is asked. The agent sees `SHAPE` (every
  section, never truncated), `QUALIFIERS` (the EXCEPT/NEVER/CORRECTED lines), `CONTRADICTIONS`, and
  the `UNREAD LEDGER`. `SALIENT` does not render at all without `--for`.
- **BRANCH B — auto-generate a question from agent context** and render ranked `SALIENT` answers.

**RULED: BRANCH A.**

**THE MECHANISM, and it is why "safer" is the exact right word:**
**A PANEL THAT ASKS NOTHING CANNOT ANSWER WRONG.** Every Branch-A panel is a CENSUS, not a
proposition — `SHAPE` enumerates, `QUALIFIERS` enumerates, and the `UNREAD LEDGER` is literally a
statement of what it did NOT show. There is no claim in it to be false. Its worst case is noise.

Branch B's worst case is different in KIND, not degree (framing owed to `0.8.0_AE_CloudComp~A`, who
found it in the TRIAL-1 field trial): *on the `--for` path a miss is LEGIBLE — the agent asked
something specific and can see they did not get it. An auto-generated question that misses produces
a well-formed panel about the wrong thing, and the agent has no reason to suspect a question they
never wrote.* **That is confidently-wrong-and-undetectable, on every file, with no handle to grab.**

Measured basis, not speculation: comp-read's ranking is phrasing-dependent BY CONSTRUCTION. On a real
file, "what module does this test exercise" shares **ZERO tokens** with the answering line
(`import boundary_report as B`), so the score is 0 and no term-weighting reaches it. An IDF fix was
built, measured, and FAILED. Bridging question-vocabulary to answer-vocabulary requires semantic
matching, which Andrew separately prohibited by design (*"it is important that it functions in
milliseconds"*, no SLM). **So Branch B's failure mode cannot be engineered away inside the tool's own
ruled constraints — it is permanent, not a maturity problem.**

**How to apply:**
- The HUD wires the **query-less** call. **Do NOT synthesize a `--for` question from context, path,
  filename, recent tool calls, or conversation** — under any later framing, and not as an
  "enhancement" once the panel feels thin.
- `--for` remains fully available for **MANUAL** use, where the phrasing-sensitivity is acceptable
  precisely because a miss is visible and the agent can rephrase (measured: "what does this file
  import" ranks the answer #1 where "what module does this test exercise" ranks it nowhere).
- **The general principle, worth carrying past this tool: PREFER THE INSTRUMENT THAT ENUMERATES OVER
  THE ONE THAT CONCLUDES, when the reader cannot audit the conclusion.** A census degrades to
  ignorable; a guessed answer degrades to trusted-and-wrong.

⛔ **BRANCH SELECTION IS NOT A ROLLOUT GO.** He resolved the DESIGN fork; his standing hold —
*"I need to know that it works before instituting on the fabric as a whole"* — is a separate word and
must be obtained separately. Do not read this ruling as authorization to wire the HUD fabric-wide.

Related: [[feedback_no_overfitting_a_scorer_to_its_own_eval_cases]] (the same tool, the same
phrasing limit, ruled not to be tuned away),
[[feedback_comp_read_hud_color_comp_find_replaces_grep_and_the_mandated_field_trial]].
