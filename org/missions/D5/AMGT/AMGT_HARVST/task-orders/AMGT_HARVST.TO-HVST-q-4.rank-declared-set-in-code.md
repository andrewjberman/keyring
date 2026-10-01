# AMGT_HARVST task order -- `HVST-q-4` -- ROUND 27 chain 4: `C-HV-RANK-DECLARED-SET` IN CODE -- eligibility before no-signal, the declared publisher set, declared-set-only scoring, the floor HOLD, the population printed through `generation_writer.py` (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~73</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- amgt-resapp-chatter-axis is a scheduled producer reading CHATTER_AXIS_SOURCE=legacy; this cell changes the gold branch's code only and deploys nothing, so no scheduled fire runs it.
comp-iam: RUN at L5 -- no AWS write; in-memory runs over fixtures and read-only gold reads. NO PUT, NO env change, NO deploy.
comp-adversary: RUN at L5 -- the adversary is an unsearched name scored as quiet, or a found-only article lifting a name's score. AC1 plants both and requires the unsearched name EXCLUDED (NOT_SEARCHED) and the found-only article unscored.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO ENV CHANGE (`CHATTER_AXIS_SOURCE` stays `legacy`), NO DEPLOY, NO S3 WRITE.** The flip is `HVST-q-7`.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~73/scripts/`; outputs named `q4_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~73/AMGT_HARVST.TO-HVST-q-4.rank-declared-set-in-code.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-q-4.rank-declared-set-in-code`.

<paths>
lib/research/metrics/chatter_axis.py
lib/research/metrics/generation_writer.py
lib/research/metrics/tests/test_q4_rank_declared_set.py
lib/research/metrics/tests/test_chatter_incomplete.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~73/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CONTRACT (`prd/AMGT_HARVST_PRD.md` v0.4 `C-HV-RANK-DECLARED-SET`, verbatim in substance)

- Each generation declares its publisher set. A publisher that refused for the whole universe in the window is not in the
  set.
- A name is ELIGIBLE only if every publisher in the declared set covered every day of the window. Any other name is EXCLUDED
  with its reason (`PARTIAL_COVERAGE`, `NOT_SEARCHED`) and is never scored.
- Eligibility is decided BEFORE the no-signal test. An unsearched name is never read as a quiet one.
- The score counts only articles from publishers in the declared set. A found-only article is never scored.
- Every generation prints its population, `{declared_publishers, universe, eligible, ranked, excluded: {reason: count}}`,
  and the excluded names, through `generation_writer.py`. The footer reads "Ranked N of U names; M not ranked (coverage
  incomplete)".
- FLOOR: 10 eligible names. Below it the generation HOLDs with an `empty_reason`, and the prior generation stays served.

**Today's gold branch** (`chatter_axis.py` ~:612-637) HOLDs the whole generation if ANY name is unresolved across all
publishers. This cell replaces that all-names rule with the contract above, on the gold branch only. The legacy branch is
unchanged.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-4"><invocation>python -m pytest lib/research/metrics/tests/test_q4_rank_declared_set.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~73/scripts/q4_ac2_gold_branch_in_memory.py</invocation><expect>POPULATION:</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-q-4"><invocation>python -m pytest lib/research/metrics/tests/ -rA --tb=line</invocation><expect>0 failed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1** (fixture plants, each asserted):
  - (a) a name with no coverage in the window is EXCLUDED `NOT_SEARCHED`, not ranked and not quiet;
  - (b) a name with one declared publisher missing a day is EXCLUDED `PARTIAL_COVERAGE`;
  - (c) a found-only article does not change any score;
  - (d) 9 eligible names HOLD with an `empty_reason`, and 10 rank;
  - (e) the population dict and footer are written through `generation_writer.py`.

  A mutant restoring the all-names HOLD fails, and so does a mutant scoring found-only articles.
- **AC2:** the producer's gold branch is run IN MEMORY (no write) over the served gold at the served as-of, with declared set
  (bbg, wsj). It prints the `POPULATION:` line (the dict), the state (COMPLETE or HOLD with `empty_reason`), and the ranked
  rows if any.
- **AC3:** the base is commit `ff4405d3d5`, pinned at cut. It prints the base and after pass counts, and `0 failed`.

## 3. MERGE ORDER

This cell merges only after `HVST-q-1` drains (ruling 6). The issuer holds the merge.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` s.4 item 4.
- The CTO's FWD-7 ruling is @`ddcc71fd2d`, and the CRO research is @`784068f4c0`.
- `HVST-q-7`'s flip rides this code.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>27</round>
<slot>~73</slot>
<fabric>site-z</fabric>
