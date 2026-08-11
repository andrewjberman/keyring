# ANDREW-DIRECT — the mdpf aggregate's surviving runtime is the LAMBDA

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0615Z.
**Verbatim:** > "on 2., i think the lambda should be the one"
**Context as put (my window report item 2):** `mdpf_aggregate_aua` runs in TWO runtimes on ONE
key — the EC2 chain's Stage 3 and in-process inside `mdpf-gold-lambda` (clocked daily) — a live
atom-5 violation; I had ruled the structure (end state = ONE runtime) with WHICH evidence-gated.

## THE RULING

**The lambda's in-process run IS the producer of `_aggregate_aua`.** The EC2 chain's aggregate
stage is the duplicate and is DISABLED as part of the cutover (migrate-before-kill sequencing —
disabled after the lambda leg is verified correctly fed, never before).

## WHAT THIS CHANGES, STATED PLAINLY

1. **X-ii's shape is settled:** "re-home the aggregate" = the LAMBDA leg's inputs/outputs re-home
   into the product root (`_staging/`); the chain's Stage 3 aggregate is a DISABLE target, not a
   re-home target. W1a's consumer repoint re-validates against the lambda-producer fact.
2. **The zeros question is now CRITICAL, not exploratory:** the ruled producer currently writes
   `partners=0 / $0.00` staging artifacts (08-09, 08-10 measured). AE's discriminating read narrows
   to: (b) the MEASURED mechanism of the zeros in the lambda's input-resolution path, and (c) the
   forward call for today's 13:30Z fire. If input-starvation, feeding the lambda correctly is the
   FIRST work item of X-ii — the producer must be correct before its duplicate is disabled.
3. **The 13:30Z escalation pre-commitment STANDS:** if today's fire would write zeros, the
   hold-or-let-fire call goes to Andrew with a CTO rec BEFORE the fire.
4. Aligns with the pattern's own logic (the clocked leg survives; event legs accelerate) — the
   lean I stated to AE is now the ruling, by his word, not by the lean.
