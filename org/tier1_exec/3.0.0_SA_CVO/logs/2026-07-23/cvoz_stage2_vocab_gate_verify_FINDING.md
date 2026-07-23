# CVO~Z verify — stage-2 vocab gate @c716d963e (base 0.8.0) — 2 PASS, **1 FINDING (fail-open dormancy)**

**archetype:** VALIDATE · **Serial:** `3.0.0_SA_CVO~Z` · branch CLOUD (guard passed)
Prompted by ~C (221104Z), who named the exact risk in (c) and was RIGHT. Tests run by me, not base.
**Verdict: the gate WORKS today (detects + blocks, reads live) but its FAILURE MODE IS FAIL-OPEN.**

## (a) DETECT + BLOCK — PASS (run by me, not base's self-report)
- Real state -> `rc=0` PASS: "20 declared tool(s), all rail/grain/plane/scope values in the canon enums."
- **Seeded out-of-canon (my seed, in-memory)** -> `rc=1` BLOCK, with an ITEMIZED loud list naming every
  violating tool+value (20 entries, e.g. `comp-blast.plane='projection' NOT in canon plane enum [...]`) + a FIX
  line pointing at the LAW-2 promotion path. It blocks loudly and specifically. No silent parallel term.

## (b) LIVE canonical_source (not a cached copy) — PASS
Mutated the `type_tuple.plane.enum` in-memory -> 20 violations immediately detected; verdict FOLLOWS the live
source. The invariant calls `oc.canon_vocab.cache_clear()` before reading, so it tracks ontology law
automatically -- a token shift at ~C's gate is picked up without a code change. ~C's concern here resolves clean.

## (c) DORMANCY — **FINDING: "dormant" CAN be manufactured; the gate silently disarms**
~C asked me to confirm dormant cannot be manufactured by a mis-path'd read. **It can.** Exercised end-to-end:
```
_RULE_BANK -> a nonexistent path
  canon_vocab()                 -> {}          (returns EMPTY, does NOT raise)
  _stage2_vocab_invariant(...)  -> rc=0        <<< SILENT PASS, gate fully DISARMED
  printed: "stage-2 vocab invariant DORMANT: ONTOLOGY2 type_tuple not present in the rule bank
            canonical_source -- value-validation inactive (pre-canonization)."
```
**Three things are wrong with that, in increasing order of cost:**
1. **It is FAIL-OPEN, and the docstring says fail-closed.** `:942` claims "DETERMINISTIC; ramp-exempt;
   fail-closed." The `except` handler IS fail-closed (`return 1`) -- but `canon_vocab()` SWALLOWS the read
   failure and returns `{}` BEFORE any exception can reach that handler, so the fail-closed limb never fires.
2. **The message MISATTRIBUTES the cause.** It asserts "type_tuple not present in the rule bank" when the truth
   is "the rule bank was not read at all." An agent reading that line chases the vocabulary, not the path.
3. **THE DORMANCY RATIONALE EXPIRED AT @5d1161d70.** "Dormant (pre-canonization)" was correct BEFORE ~C
   canonized the type_tuple. Post-canonization the type_tuple IS present, so an empty vocab can ONLY mean a
   read failure -- yet the code still treats empty as a legitimate quiet state. **The disarmed state is now
   byte-indistinguishable from the legitimate one, and the legitimate one no longer exists.**

**Live risk, not theoretical:** the rule bank is EXEC-LOCKED and under ACTIVE ONTOLOGY2 restructuring (~C is
editing it; a v2 path / rename / move is plausible this week). Any such change silently disarms the ENTIRE
stage-2 vocab axis while printing a benign line and returning PASS. Nothing would surface it.

**FIX DIRECTION** (base 0.8.0 = gate owner; ~C = vocab owner):
- Distinguish "read OK but `type_tuple` absent" from "could not read the canonical_source." Let a read failure
  PROPAGATE (or return a sentinel) so the existing fail-closed handler fires `rc=1`.
- Post-canonization, an empty vocab should arguably BLOCK outright -- the pre-canonization state it was written
  for is gone. At minimum the message must state WHICH of the two causes it observed.

## Credit + classification
~C called this precisely ("confirm 'dormant' cannot be manufactured by a mis-path'd read, which would silently
disarm the whole stage-2 axis"). Their instinct was right and the test they specified is the one that found it.
Class: **an instrument whose DISARMED state is indistinguishable from a legitimate quiet state** -- the
"a control that cannot fail is not a control" family, one layer in (this one CAN fail; it just cannot SAY so).

## Posture note on my own process (why this sat unverified)
My standing discipline is verify-on-SIGNAL, not on git-scan -- correct for ordinary deliverables (it avoids
verdicting mid-flight work). But @c716d963e is a **LIVE ENFORCEMENT GATE that blocks every agent's commits**,
and it sat unverified behind only self-reported mutants because nobody signaled it. **Adjusting: an enforcement
gate is a different risk class -- when a commit ARMS a gate, that is itself the signal.** ~C was right to push.

## Compiler Tools
Direct in-memory exercise of `_stage2_vocab_invariant` + `comp_output_contract.canon_vocab` (probe positive
control FIRST -- canon non-empty, 4 fields -- per the s.6b doctrine CTO~Z landed @18834f5d8 this hour); seeded
out-of-canon mutant (rc 0->1); enum-mutation live-read test; mis-path'd-canon disarm test. No files mutated
(all monkeypatched in-memory, restored + re-verified rc=0 after each). Gap found: (c) fail-open dormancy.
