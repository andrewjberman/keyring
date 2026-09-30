# AMGT_CORPUS task order -- `CRPS-ab-2` -- ROUND 26: the unit classifier decides from the key's SERIES median, never one sample

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ab-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (a map commit and re-derive are a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 26. Serves **every served figure's unit**.

## 1. THE CELL -- `CRPS-ab-2`

**Where this came from (round-25 analysis ruling 2).** `integrations/bloomberg/research/build_unit_map.py` classifies a key's unit from
ONE sampled value, the newest fiscal year (`classify_unit`, with `sample_value` feeding it). The result becomes the per-security entry
in `field_map.json`, read per figure by `model_block_pull._resolved_unit`.

On `BP/ LN Equity` that single sample misreads two series:
- **`PE_RATIO`:** FY2016-2025 reads 1031.31, 41.10, 13.46, 31.53, 17.78, 11.91, 15.44, 6.78, 206.72, 1663.44. The sample 1663.44 is a
  real Bloomberg ratio on near-zero EPS. It lies outside the ratio band, so the whole series reads UNRESOLVED.
- **`PROF_MARGIN`:** FY2016-2025 reads 0.0628, 1.4109, 3.1407, 1.4461, -19.1658, 4.7959, -1.0303, 7.2522, 0.2014, 0.029. The sample
  0.029 reads DECIMAL by magnitude, although the series median is about 1.4, so the whole series is refused.

**RULED -- what you build:**
1. A key's unit is decided from its SERIES: the median of |value| over its measured fiscal years (the per-security history the builder
   already loads; `hist_rows`).
   - Use the single sample only when the key has no fiscal-year series.
   - **The bands are not widened.** The same magnitude bands and families decide; only their input changes from one sample to the
     series median.
   - Each change goes in the classifier, with its ground in a code comment.
2. **Tests:** `integrations/bloomberg/research/tests/test_build_unit_map_series_round26.py` (new):
   - BP's two series above decide RATIO and PERCENT;
   - a series whose median is genuinely out of band stays UNRESOLVED;
   - a key with no series falls back to the sample;
   - no network.
   Keep the builder's suites green.
3. Do NOT write the committed `field_map.json`, do NOT touch `model_block_pull.py`, and do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_series_round26.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/SERIES_MEDIAN_ROUND26.md
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ab-2.series-median-units.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ab-2.series-median-units.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written), every S3 object. Scratch `.scratch/ab2/`. Your worktree is a SPARSE
checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO derive.
- Any long-running script runs from a NAMED file with `python -u`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ab-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab2_AC1.sh</invocation><expect>(?m)^ab2 bp_pe_ratio RATIO bp_prof_margin PERCENT keys 100 unresolved_before 31 unresolved_after \d+ bands_unchanged True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ab-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the checker rebuilds a TEMP map from your builder and reads it through the producer's own reader.
  - BP's two series must read RATIO and PERCENT.
  - The count of every served UNRESOLVED figure over the newest block of 100 keys is printed before (31) and after, with one `FIG`
    line per figure. How many close is reported, not demanded.
  - The band constants must hash to the base recorded at the cut.
- AC2: your tests with the builder's suites.
- Write `SERIES_MEDIAN_ROUND26.md` listing the checker's `FIG` lines: each before -> after, from the rule, never predicted.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, the rule change with its ground, and the `FIG` outcomes by class.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-25 analysis ruling 2 and enrichment item 2 @`19207dfb83`. Dry-run at base CLOUD `ae1c849af1`: ab2_AC1 FAIL as
designed (`ab2 bp_pe_ratio UNRESOLVED bp_prof_margin UNRESOLVED keys 100 unresolved_before 31 unresolved_after 31 bands_unchanged
True`). The FIG classes are BBSE3 CAPITAL_EXPEND 10, BP PE_RATIO 10, BP PROF_MARGIN 10, and TSM CURR_ENTP_VAL 1. ab2_AC2 FAIL (no
tests).
<risk>LOCAL</risk>
<status>pending</status>
<round>26</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
