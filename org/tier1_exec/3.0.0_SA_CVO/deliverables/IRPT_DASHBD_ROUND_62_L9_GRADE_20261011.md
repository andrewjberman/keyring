# IRPT_DASHBD round 62 -- L9 grade of the rule-24 record's no-claims rule (DB-b-118)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:21:36Z. Row IRPT_DASHBD-D2-S8.
**Input:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/THRESHOLD_CLAIM_RULE24.json` (msg 4142 (rounds 59-62 drained @bbc9e11292, @2f0664fab0, @6d0b3ce3a8, @4d4e3ee317)).

**The rule graded:** a thresholds input that carries no `threshold_claims` is not refused and is never read as measured. The
writer stamps each non-null value `held`, each null value `absent`, and sets `threshold_claims_source` to `defaulted_no_claims`.

**Verdict: SOUND.**

| question | finding |
|---|---|
| Does it obey the law (no claim field means the value may not be treated as measured)? | Yes. The default can never yield `measured` or `inferred`. A consumer that requires `measured` rejects every defaulted value |
| Is `held` true of a value handed over with no statement? | Yes on the declared domain, which is how the WRITER knows the value: it neither measured nor derived it. It may understate a value that was in fact measured upstream. That errs on the safe side |
| Can a consumer tell a stated `held` from a defaulted one? | Yes. `threshold_claims_source` is its own column, so the two axes stay apart (one axis, one intent). A fifth member such as "unstated" would have widened the law's four-member set |
| Is a null ever dressed as a value? | No. A null is `absent`; a null under any other claim is refused, and a value under `absent` is refused |

This seat re-ran the order's three checks (PASS) and the new test file (32 passed).

## What follows from it

- **The live 49F thresholds file carries no claims.** The next dim row written from it reads `held` on every non-null threshold,
  where two of them (tolerance, large flow share) are in fact measured. That is truthful and understated. Adding stated claims to that
  file is a follow-on; it is not a defect of the rule.
- **A Cottonwood row 3 with no thresholds** reads five `absent` and types its value columns double (the amendment's test).
- The contract is at 0.4.0 with 28 columns. Its `method_versions` list still names rows 1 and 2 only (row D2-W93-S3).

## Rounds 59 to 61, read with this compile

- Round 60's record reads row 3 TRUE for Cottonwood on every stated field and left one item open: whether a bond's close carries
  accrued interest. ADVI_COTBKF round 57 answered it (dirty; no measured row holds a bond), graded by this seat today.
- DB61-1-AC1 reads FAIL at HEAD, as the issuer said it would: its census compares to HEAD's bytes and DB-b-118 moved the producer
  after the R45 pin. The signed packet binds the pinned commits. This seat did not re-read the R45 packet's delta.
