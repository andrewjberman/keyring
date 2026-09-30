# AMGT_HARVST task order -- `HVST-l-1` -- ROUND 22 chain 1 of 2: THE GUARD READS `co_mention_count >= 4` ONLY -- a one-line simplification, outcome-identical

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-l-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~51</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on publication_gold.py or the harvest gold prefixes; this cell writes no gold and deploys nothing.
comp-iam: RUN at L5 -- no new boto3 call; AC2 reads S3 (silver headlines, the newest mention and event parts) with GET/LIST only. NO PUT.
comp-adversary: RUN at L5 -- the adversary is a "simplification" that moves an event. It is equivalent only because `is_roundup == (co_mention_count >= DEFAULT_ROUNDUP_AT)` with DEFAULT_ROUNDUP_AT 5 >= 4. AC1 pins that equivalence in a test; AC2 requires 8 of 8 events identical to the `k-1` rule's.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** The served rebuild is `HVST-l-2`, a separate chain.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~51/scripts/`; outputs named `l1_*`
   -- **never `.scratch/`.** You may IMPORT or copy round 21's script
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~49/scripts/k1_ac2_dry_rebuild.py`, but NEVER run
   it in place: it writes `k1_ac2_result.json` into round 21's committed folder.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~51/AMGT_HARVST.TO-HVST-l-1.guard-reads-co-mention-only.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-l-1.guard-reads-co-mention-only`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~51/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/ROUND_ANALYSIS.round21.md` @`63c272600a`, s.2 ruling 2, as corrected @`3100474cde` s.2a)

- `publication_gold._is_guarded` (~:1098) today reads
  `is_roundup True OR co_mention_count >= EVENT_GUARD_CO_MENTIONS (4)`.
- The producer stores `is_roundup = co_mention_count >= roundup_at` (~:307), with `DEFAULT_ROUNDUP_AT = 5` (~:49). The
  issuer measured it equal on 304 of 304 served mention rows. So the flag limb is SUBSUMED by the co-mention limb.
- **The change:** `_is_guarded` reads `co_mention_count >= EVENT_GUARD_CO_MENTIONS` ONLY. Update its comment to state
  why the flag is not read.
- Nothing else changes.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-l-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with new tests NAMED in the -rA output: _is_guarded is decided by co_mention_count alone (a row with is_roundup True but co_mention_count 3 is NOT guarded; one with is_roundup False and co_mention_count 4 IS); and a pin that DEFAULT_ROUNDUP_AT >= EVENT_GUARD_CO_MENTIONS (the equivalence this simplification rests on); the pass count BEFORE and AFTER printed (base 212 in lib/research/harvest/tests/) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-l-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~51/scripts/l1_ac2_identical_to_k1.py</invocation><expect>OVER TODAY'S INPUTS, event_rows under the NEW guard equals event_rows under the k-1 guard (is_roundup OR co_mention_count >= 4) ROW BY ROW, every field, denominator printed (8 events at the cut); plus, over the served newest mention part, the count of rows where is_roundup != (co_mention_count >= 5), expected 0. PASS only if 8 of 8 are identical and the count is 0</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No change to the `is_roundup` producer, no gold write, no deploy, no change to any event outcome.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Measured by the issuer before the cut** (a dry run with the co-only guard at the base `88dbe4af64`): KEPT 5, CHANGED 3,
   GONE 0, identical to `k-1`. The flag and `co >= 5` agree on 304 of 304 rows.
2. **Independent of `l-2`:** outcome-identical by construction, so the served rebuild does not wait on it.
3. **Base:** suite 212 in `lib/research/harvest/tests/` (228 with the api route file). AC1's named tests FAIL at the base,
   because the flag limb still decides.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>22</round>
<slot>~51</slot>
<fabric>site-z</fabric>
