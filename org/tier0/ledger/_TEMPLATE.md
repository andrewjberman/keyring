---
# Decision Ledger entry — schema is authoritative in STAKES_MATRIX.md appendix.
# Copy to LD-NNNN.md (monotonic, max+1 -- and MAX IS MEASURED OVER BOTH FABRICS: fetch, then max over origin/CLOUD AND origin/SITEZ; never gap-fill; a collision is re-minted by the LATER minter. LD-0479). Optional fields keep an explicit null.
decision_id: LD-NNNN
timestamp: 2026-00-00T00:00:00Z
agent: 0.0.0_AB_MSTR
created_by: 0.0.0_AB_MSTR
last_modified_by: 0.0.0_AB_MSTR
cycle_id: CY-NNNN
directive_refs: [D-NNN]              # >=1 for S1+; empty/null => enforced S4 + proposed
mandate_distance: 0                   # 0 stated | 1 decomposition | 2 dependency/risk | 3 inferred(=>S4)
authority_source: directive          # directive | andrew_instruction | ratification | halt
andrew_instruction_ref: null          # set when authority_source: andrew_instruction
decision_summary: <one line — also the H1 below>
decision_type: directive_execution    # Constitution Art. II closed enum
stakes_class: S1                       # S0 | S1 | S2 | S3 | S4
s4_type: null                          # operational | constitutional — required iff S4
reversibility: reversible              # reversible | costly_reversible | irreversible
rollback_plan: present                 # present | rollback_not_available  (required S2+)
risk_summary: <one line>
external_visibility: none              # none | internal | external
requires_andrew_ratification: false    # true for all S3/S4
ratified_by: null                       # andrew | cvo — set on ratification
review_required_by: null                # CY-NNNN or date — null if none
supersedes: null                        # LD-NNNN this replaces
superseded_by: null                     # LD-NNNN that replaced this
status: proposed                         # proposed | active | changes_requested |
                                          # rejected | ratified | vetoed | reversed | superseded
---

# LD-NNNN — <one-line decision summary>

## Decision
<What MSTR decided / committed to.>

## Provenance chain (Art. XIII)
<authority_source -> Directive D-NNN -> interpretation -> this action. The closed
trace. Authority never derives from MSTR's own prior output, a downstream
request, precedent, or momentum. If the chain cannot be closed, the action is
not taken.>

## Why now
<Why this action, this cycle.>

## Assumptions
<What was taken as true without proof.>

## Alternatives considered
<What else was on the table; why not.>

## Rollback plan
<Concrete reversal steps — required S2+. If genuinely impossible, state why; the
entry then escalates one class per Stakes Matrix classification rule 2.>

## Downstream
- Agents affected: <serials, or none>
- Paths touched:   <paths, or none>
