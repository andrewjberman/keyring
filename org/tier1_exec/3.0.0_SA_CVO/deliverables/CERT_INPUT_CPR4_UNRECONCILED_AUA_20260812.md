# CERT INPUT -- CPR-4 `unreconciled_aua`: CTO's precondition is RIGHT IN REASONING and MIS-AIMED IN TARGET

**Author:** 3.0.0_SA_CVO · **2026-08-12 ~1510Z** · **archetype:** VALIDATE (source + deployed-bytes read,
READ-ONLY). **Inputs:** DS 150400Z (CPR-4 step 4, the gap they refused to gloss) + CTO 150550Z (mutant as a
HARD cert precondition).

## THE HEADLINE: RUNNING THE SPECIFIED MUTANT WOULD PRODUCE A CONFIDENT ANSWER TO THE WRONG QUESTION
CTO requires: *"force incomplete attribution and prove `unreconciled_aua` goes NON-ZERO."*
**That mutant would FAIL, and its failure would be CORRECT BEHAVIOUR, not a defect.** An unattributed
account does not land in `unreconciled_aua` at all -- it lands in the `unclassified` bucket. Anyone running
the mutant as specified would watch the field stay 0.00 and conclude it is hardcoded or broken. **It is
neither.** The control must be re-aimed before it is run, not after it produces a false finding.

## WHAT THE FIELD ACTUALLY IS -- read on the DEPLOYED BYTES, not the repo (that distinction mattered here)
`s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` (229,933 B), the copy that produced the
14:58:55Z serve:
```
holdings_total  = float(acct_value.sum())                                    # deployed :887
identity_gap    = holdings_total - (fee_earning_aua + non_fee_aua + unclassified_aua)   # :888
if abs(identity_gap) > 0.01:  log('ERROR: fee-bucket identity broke ...'); return null_block   # :889-891
unreconciled_aua = round(float(total_aua) - holdings_total, 2)               # :897
```
1. **THE CONSTANT HYPOTHESIS IS REFUTED AT SOURCE.** It is a subtraction of two independently-computed
   quantities. It cannot be a hardcoded `0.0`; the `None`s at `:842-848` are null-block initializers.
   **CTO's stated risk -- "no available control can tell it from a constant" -- is closed by reading it.**
2. **BUT IT IS A *FRAMING* CHECK, NOT AN ATTRIBUTION CHECK, AND THE CODE SAYS SO ITSELF:**
   > *"Retained for schema continuity; ~0.00 **by construction** when the passed total rides the same
   > holdings frame. A nonzero here now means the PASSED total diverged from the holdings frame (a framing
   > question, **never client money to display**)."*
   So the served `0.0` is **~0.00 BY CONSTRUCTION** -- it certifies that the canonical `total_aua` and the
   holdings frame agree. **It carries no information about attribution completeness, and no mutant on the
   attribution axis can make it carry any.** This is my own §5 doctrine entry in the field: two quantities
   riding one frame cannot cross-check each other.
3. **THE PROPERTY THE CERT WANTS *IS* ENFORCED -- by a different and genuinely fail-closed control.**
   `identity_gap` at `:888-891` REFUSES TO EMIT A SPLIT (`return null_block`) if the three buckets do not
   partition the holdings frame. That is the attribution guard, it fails closed, and it is the leg the cert
   should rest on.

## WHAT I RECOMMEND THE CERT REST ON (re-aimed, all runnable on a local fixture, zero live-data risk)
- **A. FRAMING mutant (tests what the field ACTUALLY claims):** pass a `total_aua` that diverges from the
  holdings frame; require `unreconciled_aua` to report the gap. This is the field's real contract.
- **B. ATTRIBUTION mutant, re-aimed at the right control:** feed an account with no billing row; require it
  to land in `unclassified` (NOT in `non_fee`), and require `identity_gap` to hold. **The equivalent
  control already EXISTS and PASSES for the sibling producer:** `INF_D_02`'s three-way partition is
  exercised by `tests/test_book_fee_split.py` -- I RAN IT, 5/5 pass, and its line 82 asserts
  `unreconciled_aua == 32.0` on exactly the unattributed-input shape (25 no-row + 7 NaN-id). ⚠ **That test
  covers `INF_D_02._book_fee_split`, a DIFFERENT producer and a DIFFERENT residual -- I am NOT transferring
  its pass to `INF_D_04`'s field.** It is offered as the pattern to copy, not as coverage.
- **C. DS's three closures stand as they are** -- correct, and correctly characterised by DS as classifier
  properties rather than independent witnesses.

## ⚠ AND A FALSE ALARM I ALMOST FILED -- checked before reporting
`comp-pipescript deployed --pipeline inf-gold` reports **`INF_D_04 STALE`** (local `acf9714a…` vs s3
`eaae8fb4…`). **It is NOT drift.** Byte delta 4,367 against 4,468 lines (one byte per line), and
normalising line endings collapses a whole-file diff to **exactly two lines** -- a comment the REPO
carries and the deployed copy predates:
`# DEPLOY-SERVE-HELD: advisor-of-record daily fold pending arch-gate (live CTO) + NEVER#2 sign-off`
So the divergence is (a) CRLF-vs-LF and (b) a deliberate, self-documenting DEPLOY-HELD marker. **The
deployed code is functionally identical to the repo, and the `unreconciled_aua` computation is byte-for-byte
the same in both** -- which is why my characterisation above holds for the served artifact.
**INSTRUMENT NOTE (mild, not a defect):** `comp-pipescript`'s MATCH/STALE is a raw-hash comparison, so a
line-ending difference alone yields a permanent false STALE on an otherwise-identical file. Worth knowing
before a STALE is read as drift -- I read it that way for about ninety seconds.

## VERDICT
**The cert should NOT close on the mutant as specified, and should NOT be blocked on it either.** The
constant hypothesis is refuted at source on the deployed bytes; the field is correctly zero and
structurally incapable of reporting attribution; the attribution guard is the `identity_gap` refusal. I can
certify on legs A+B once they exist, or certify now with `unreconciled_aua` characterised as
**FRAMING-CHECK, ~0.00 BY CONSTRUCTION -- NOT an attribution signal**, which is the honest description of
what the served value means. CTO's call on which.

-- 3.0.0_SA_CVO
