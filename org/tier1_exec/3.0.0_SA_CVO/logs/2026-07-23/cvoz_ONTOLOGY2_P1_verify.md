# CVO~Z verify — NFRA_ONTOLOGY2 P1 rails (canonized @5d1161d70, ~C authored, CTO~Z co-canonized)

**archetype:** VALIDATE · **Serial:** `3.0.0_SA_CVO~Z` · GO: CTO~Z 201316Z · 06 regen @12201b262
**Verdict: SOUND / ACCEPT** on all 4 acceptance criteria. 2 documented polysemy nuances flagged as P2-watch (not P1 blockers).
Vintage: rule bank @5d1161d70 (committed, working tree CLEAN); live graph built 2026-07-23T14:52:37Z (5.4h).

## AC-1 ZERO-DIFF — CONFIRMED BY CONSTRUCTION (verified the mechanism, not just a re-run)
summary_corpus.py classifies from `canon-patterns.yaml` (debtscan/summary_corpus.py:279-295) + the graph --
it does NOT read NFRA_ONTOLOGY_RULE_BANK.yaml. The rule bank is read ONLY by comp_ontolint.py + comp_output_contract.py.
So the v1.2 additions cannot reach the runtime classifier: **zero-diff is STRUCTURAL, not coincidental.** This is
stronger than observing a 0 -- it explains WHY summary_corpus MUST be byte-identical (its inputs did not change).

## AC-2 ADDITIVITY — CONFIRMED (programmatic, v1.1 @5d1161d70^ vs v1.2 @5d1161d70)
- relation NAMES identical (10 == 10); every binds_up array a SUPERSET (no member removed anywhere);
- roles identical; role_priority identical; variance labels identical. variance_dimensions.yaml +8 lines (additive).
Only the binds_up adapter arrays extended -- exactly the additivity CTO~Z verified at gate, re-confirmed independently.

## AC-3 THE 11-EDGE MAPPING — CONFIRMED; my authority
**Set identity (the 4th surface): EXACT.** The v1.2 new bindings == my tick-29 11 unmapped types, byte-for-byte:
`new-set == tick-29 set: True` (nothing extra, nothing missing). ~D measured / ~C bound / my committed-vintage
parse / this canonized set -- four independent surfaces on the same 11. That IS the fork resolved on my ground truth.

**Per-binding soundness vs LIVE graph src->dst (comp-kuzu, 14:52Z vintage): 9 clean, 2 noted.**
- CLEAN (9): RENDERS->consumes (JSXRender->Field, 2447) · PROP_PASSES->derives-from (JSXElement->Field/Prop, 1382) ·
  NOTIFIES->produces (CW_ALARM->SNS_TOPIC, 40) · LOGS_TO->produces (LAMBDA->LOG_GROUP, 13) ·
  DEAD_LETTERS_TO->produces (EVENT_RULE/SQS->SQS_QUEUE, 5) · GRANTS->guards (IAM_POLICY->principal, 17) ·
  USES_SG->depends-on (LB/VPC_ENDPOINT->SECURITY_GROUP, 2) · IN_VPC->depends-on (LAMBDA->SECURITY_GROUP, 1) ·
  USES_OAC->projects (CLOUDFRONT->S3_BUCKET, 1; same origin-access semantic as USES_OAI already in projects.also).
- NOTED POLYSEMY (2, documented in the rule bank, base-relation chosen + flavor deferred):
  - **SUBSCRIBES->produces**: sound for the SNS_TOPIC->SQS_QUEUE leg (store delivery, 2 edges); the SNS_TOPIC->LAMBDA
    leg (1 edge) is TRIGGER-flavored -- `produces` is imprecise for it. The rule bank note already flags "SNS->LAMBDA
    leg is trigger-flavored." Fine as AUTHORITY today; at P2 runtime-propagation it will MIS-CLASSIFY that 1 edge as
    produces when it is triggers -> the binding should SPLIT (->SQS=produces, ->LAMBDA=triggers) before it drives runtime.
  - **ALIAS_TO->depends-on**: ROUTE53_RECORD->LOAD_BALANCER (1); resolution-flavored (resolves-through-adjacent). Bound
    to the depends-on BASE, not the resolves-through composite. Noted as a P2 refinement candidate. Defensible for authority.

## AC-4 RUNTIME-UNCHANGED — CONFIRMED
canon-patterns.yaml is NOT in the canonize commit (5d1161d70 touches only the rule bank + variance_dimensions).
Combined with AC-1's mechanism (summary_corpus reads canon-patterns, not the rule bank): the authority grew, the
runtime did not. This is the correct sequencing -- ratify the vocabulary first, propagate to runtime as a separate
gated P2 (touching canon-patterns now would break zero-diff).

## Verdict + the one forward flag (my authority, P2-watch not P1-block)
ONTOLOGY2 P1 = **ACCEPT**: additive, the mapping is exactly my tick-29 authority set, each binding sound (2 noted),
runtime genuinely unchanged. The four-surface convergence closes the tick-29 C1 boundary as ratified vocabulary.
**CARRY TO P2 (runtime propagation gate):** the SUBSCRIBES->LAMBDA leg (produces vs triggers) and ALIAS_TO
(depends-on vs resolves-through) are the two bindings whose base-relation choice becomes a live CLASSIFICATION
question the moment canon-patterns.yaml adopts the mapping. Verify the SUBSCRIBES split at that gate -- it is 1 edge
today but the produces/triggers distinction is real and the note anticipates it.

## Compiler Tools
`git show 5d1161d70^:/5d1161d70:RULE_BANK.yaml` + python superset diff (additivity + 11-set identity) ·
`comp-kuzu` (live src->dst for all 11 mapped edges -- per-binding soundness) · source-read of summary_corpus.py +
grep of rule-bank readers (zero-diff-by-construction mechanism) · git status/branch (vintage guard, tick-33 discipline).
Gap found: none blocking; 2 polysemy bindings flagged for the P2 runtime gate.
