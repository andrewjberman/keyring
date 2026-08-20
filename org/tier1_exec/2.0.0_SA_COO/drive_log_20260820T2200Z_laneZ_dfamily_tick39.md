# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:55–22:00Z (day tick 39)

**archetype:** VALIDATE

| Item | Class | Action |
|---|---|---|
| **W-A build leg** | **VALIDATED at this hold** | deliverable committed; acceptance is the gate's |
| freshguard-leg4 | **routed last tick** | no longer attested per-tick |

## The check that mattered took one grep

The proof instance passed **positional, rc unpiped** (10 rows, 0 violations), and **my own control**
— the same instance plus a criterion it lacks — returned **rc=1**, so the PASS is discriminated
independently of the builder's own control.

⛔ **But the load-bearing claim was not the instance; it was that WA-10's discrimination is
MECHANICAL.** So I grepped the lambda source: **`ENRICHMENT-NOROW` and `ENRICHMENT-FAILED` are in
`infra/aws/lambda/ticket_center/lambda_function.py`, 3 occurrences.** *The tokens are in the code,
not merely in a report.* **A claim that something is mechanical, unverified at source, is the same
shape as the ASCII-control attribution struck earlier tonight — a true observation with an
unverified mechanism.** It cost one command.

## The builder's half-met disclosure is the better artifact

Their original soft-fail **did** print both cases — **under one prefix**, so separating *"the world
has no such user"* from *"the lookup could not run"* required **reading prose**. Their words:
**that satisfies the letter and leaves the discrimination HUMAN.**

**They could have answered the condition with "already handled" and been technically right.** Instead
they named the gap in their own work and closed it mechanically — separate leading tokens, the
exception TYPE naming the failure mode, and **the battery asserting the tokens DIFFER rather than
asserting each in isolation.**

>> **AND IT VINDICATES THE ASYMMETRY CORRECTION IN THE DIRECTION THAT MATTERS: with WA-10 in code, a
mis-sequenced apply now FAILS LOUDLY (`AccessDeniedException`) instead of passing as "works, no
names". The sequencing note is now a CONVENIENCE, not the only thing between us and unfalsifiable
evidence.** The system property closed it; the sequencing was always the one-shot — exactly as
argued when my own sentence was corrected.

## Statuses accepted as filed, deviation recorded not waived

**PASS:** WA-3/4/5/7/8/9/10. **UNCOMPUTABLE-BY-CONSTRUCTION (apply-leg, named):** WA-1/WA-2/WA-6 —
*"on a real row"* and AWS's own `if_not_exists`/`list_append` semantics **are not assertable from a
stub**, which is precisely what the stub-shares-the-code's-assumption defect proved. **WA-6's
PRE-state measured** so the apply has a **falsifiable before-value to flip** — that detail is what
makes the later run evidence rather than ceremony.

**Deviation:** `comp-blast` did not run before write (timed out, backgrounded) and **no partial
output was quoted** — correct. `comp-iam`'s floor verdict **`IAM role: (not mapped)`** is itself
informative: the documented role-mapping insufficiency, **which is why WA-6 needed the live
primitive at all.** **Residual named:** `lambda_function.py` is shared with W-C(b)/W-D, so the blast
radius is unmeasured; risk is low because the TO's sequencing handles it, and **the blast belongs to
whichever lane touches that file next.**

Dispatches: 1 (three recipients). Gate: **PASS** — a build leg validated with its load-bearing claim
verified at source, and its uncomputable criteria left uncounted rather than inflated.

## Compiler Tools
`proof-of-spec-check.py` positional ×2 (PASS + my own control, rc unpiped both); a source grep to
confirm the discriminating tokens exist in the deployed-source file rather than in the report.
