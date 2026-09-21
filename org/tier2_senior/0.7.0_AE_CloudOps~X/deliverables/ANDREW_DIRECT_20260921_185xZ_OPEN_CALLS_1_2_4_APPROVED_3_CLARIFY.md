# ANDREW-DIRECT 2026-09-21 ~18:5xZ -- open calls 1, 2, 4 approved; call 3 needs clarification

**Channel:** in session, at the `0.7.0_AE_CloudOps~X` terminal, replying to this seat's `/open-calls` output.
**Recorded by:** 0.7.0_AE_CloudOps~X.

## His words, VERBATIM

> recs approved for call 1 and 2. FOr 3, need more clarification on what your scope/denominator is here. call 4, yes.

## The calls he answered (as this seat put them, ~18:51Z)

**CALL 1 -- Deploy the patched NNA guard to the Inflection runner now: (a) I deploy it, or (b) route it to the data-science seat?**
REC: (a). The runner's `code/gold/lib/nna_coverage_guard.py` is byte-identical (26,438 bytes, LF-normalised) to the
repo version before the patch, so the deploy carries only the message change (158dbeb7bf, merged 6c9cd5140d).
**RULING: (a) approved.**

**CALL 2 -- Who finds out why accounts 351/1206's 09-04 rows left the feed (brief step 1): (a) me, now, or (b) another seat?**
REC: (a). Read-only comparisons of what we already store in S3, no new vendor call.
**RULING: (a) approved.**

**CALL 3 -- Which Inflection ADVI value do you see changing daily?**
This seat's card said "every Inflection file the portal serves was last written 09-05".
**RULING: not answered. He asked for clarification of this seat's scope/denominator.**
(The sentence was inherited from the MSTR brief, whose measured population is the 29 top-level files under
`s3://opal-data-inf/platinum/firm/` plus `platinum/advisors/*/summary.json`. It is not a census of what the portal
reads. This seat owes that clarification, with a measured denominator.)

**CALL 4 -- Fix the morning "EC2 launch failure" texts: yes or no?**
REC: Yes. Send the text only if the retry also fails, and stop retrying once the instance is running.
**RULING: yes.**

## Scope, as given

Calls 1, 2 and 4 are approved as recommended, and nothing wider is implied. Call 3 stays open until he answers
it after the clarification. The 351/1206 excusal ruling itself is not part of call 2, which only establishes the
fact. That ruling has been the CTO's (brief section 5).

Source brief: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/INF_GOLD_CHAIN_NNA_GUARD_STALL_BRIEF_20260921.md`.
