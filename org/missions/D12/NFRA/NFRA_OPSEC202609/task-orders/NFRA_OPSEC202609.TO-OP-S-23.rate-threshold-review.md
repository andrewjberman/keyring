# TO NFRA_OPSEC202609.TO-OP-S-23 -- THE RATE THRESHOLDS MEASURED AGAINST ORDINARY TRAFFIC, NOT GUESSED: a month of WATCH rows turned into a distribution, so a threshold is proposed on evidence -- and the FINAL numbers go to Andrew as `OP-x-5`'s card, never set by this lane (OP-s-23, C-3)

<to_id>NFRA_OPSEC202609.TO-OP-S-23</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

⛔ **BLOCKERS, NAMED, AND ONE OF THEM IS TIME:**
| blocker | state |
|---|---|
| `OP-s-5` | **DONE** -- the logs exist |
| `OP-s-14` | **NOT STARTED** -- nothing is producing WATCH rows yet |
| **a month of WATCH rows** | **cannot exist before `OP-s-14` runs for a month** |

**GO CONDITION: `TO-OP-S-14-21` terminal, PLUS at least one month of WATCH rows accumulated after it.** ⛔ **This face is the one in the project that CANNOT be pulled forward by working harder.** Do not start it early and do not substitute a shorter window: the cell's value is *"a MEASURED distribution over >= 1 month of WATCH rows"*, and a two-week distribution presented as the month is exactly the defect C-3 exists to prevent.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (**C-3**; `OP-x-5` is the card to Andrew) - **Decomp cell:** `OP-s-23` (v0.1.11, s.1a) - **Lane:** AE lane - **Round:** later; staged now so nothing has to be re-derived when the window closes.

---

## THE CELL, AND THE EVIDENCE PROBLEM IT NAMES

The brief measured **3 hours of WAF samples returning ZERO** -- and the cell records the right reading of that: *"consistent with no attack AND with nobody looking."* **A zero from an instrument nobody has characterised is not a measurement of safety.**

**C-3's two binding clauses:**
1. **BLOCK on a single rate trip VIOLATES.** More than one trip is required before a block is warranted.
2. **A threshold presented as FINAL without WATCH rows VIOLATES.**

>> **AND THE THIRD THING, WHICH IS THIS FACE'S WHOLE POSTURE: the FINAL thresholds are `OP-x-5`'s card to Andrew, not this lane's to set.** This task order produces a **distribution and a RECOMMENDATION with its reasoning**. It does not change a threshold. **A face that quietly retunes a live rate rule has taken a decision that was routed to the sovereign.** <<

## DELIVERABLE

1. **THE DISTRIBUTION, over >= 1 month of WATCH rows**: requests per source per window, the shape of ordinary traffic, and where the current thresholds sit against it. **State the window's exact start and end and the row count.**
2. **SEPARATE ORDINARY FROM ANOMALOUS EXPLICITLY.** A distribution that silently includes an attack window recommends a threshold tuned to an attack. **If the window contains an incident, say so and show the distribution both with and without it.**
3. **THE PARTNER FIRMS ARE THE POPULATION THAT MATTERS.** Cross-reference against `OP-s-20`'s ALLOW list: **a threshold that would have tripped on a known partner address during ordinary use is the finding**, and it is more important than the aggregate.
4. **A RECOMMENDATION WITH ITS REASONING AND ITS FALSE-POSITIVE COST**, framed so Andrew can answer in one word. **Name what a wrong threshold costs in each direction** -- too low is a locked-out firm, too high is a rule that never fires.
5. **NO THRESHOLD IS CHANGED BY THIS FACE.** ⛔ The live rate rules are read, never written.
6. **The card routed to `OP-x-5`** for the sovereign call, with the distribution attached as its evidence.
7. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-23.rate-threshold-review.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S23-AC1" cell_refs="OP-s-23"/> `S23-AC1` -- THE WINDOW IS AT LEAST A MONTH AND ITS SIZE IS STATED: window start, window end, and the WATCH-row count. **A window shorter than a month files `UNCOMPUTABLE` with the actual span** -- it does not file a distribution with a caveat.
<criterion id="S23-AC2" cell_refs="OP-s-23"/> `S23-AC2` -- THE DISTRIBUTION IS PRESENTED WITH ORDINARY AND ANOMALOUS SEPARATED: the distribution, plus an explicit statement of whether the window contained an incident and, if so, both versions. **An undifferentiated distribution over a window containing an attack is a FAIL.**
<criterion id="S23-AC3" cell_refs="OP-s-23"/> `S23-AC3` -- THE PARTNER POPULATION IS CHECKED AGAINST THE PROPOSED THRESHOLD: for each firm in `OP-s-20`'s ALLOW list, whether its observed ordinary traffic would have tripped the recommended threshold, with the count that would have tripped printed. **Zero is a fine answer; an unstated answer is not.**
<criterion id="S23-AC4" cell_refs="OP-s-23"/> `S23-AC4` -- NOTHING WAS RETUNED: the live rate rules read before and after this face and shown **identical** -- name, priority, limit and action for each, both times. **A changed threshold is a FAIL even if the new number is better**, because that decision is `OP-x-5`'s card.
<criterion id="S23-AC5" cell_refs="OP-s-23"/> `S23-AC5` -- THE CARD IS ROUTED AND ANSWERABLE IN ONE WORD: the `OP-x-5` card as it was sent, with its recommendation, its reasoning, and the cost named in BOTH directions. **A card that asks Andrew to do the analysis is not a card.**

<expected_criteria>S23-AC1, S23-AC2, S23-AC3, S23-AC4, S23-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-23` (C-3); value: a MEASURED distribution over >= 1 month of WATCH rows.
<owned_cells>OP-s-23</owned_cells>
Read-dependencies, NOT claimed: `OP-s-5` (DONE -- the logs), `OP-s-14` (the WATCH rows; the GO condition), `OP-s-20` (the ALLOW list this cross-references), `OP-x-5` (the sovereign card this feeds; HELD at Andrew and not this lane's to answer).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). This face is read-only on live infrastructure and opens no ledger; it changes nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy; it reads rows and rules.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; its evidence is a live distribution at the assignee's own vintage, and its window is stated rather than assumed.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S23-AC1`, `S23-AC2`, `S23-AC3`, `S23-AC4`, `S23-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-23.rate-threshold-review.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S23-AC1,S23-AC2,S23-AC3,S23-AC4,S23-AC5"` BEFORE the complete flip. **`S23-AC4` is the control that must be able to fail: the before/after rule read is what proves this analysis face did not quietly become a tuning face.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before the analysis">Measure the actual span of available WATCH rows. If it is under a month, STOP and file the span -- the wait is the correct act and it is not a blocker to route around.</phase>
  <phase id="2" when="during">Keep ordinary and anomalous separated from the first pass; separating them afterwards is not the same analysis.</phase>
  <phase id="3" when="after">Re-read the live rate rules and show them unchanged, then route the card.</phase>
</compiler_tools_mandate>
