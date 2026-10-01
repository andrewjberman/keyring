# AMGT_CORPUS task order -- `CRPS-ac-1` -- ROUND 27: a ZERO-DOMINATED unit class in the builder

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ac-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the BBSE3 re-derive is a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 27. Serves **every served figure's unit**.

## 1. THE CELL -- `CRPS-ac-1`

**Where this came from (round-26 analysis ruling 3).** `integrations/bloomberg/research/build_unit_map.py` decides a key's unit from
its fiscal-year SERIES median (`series_median_abs` and `unit_input_value`, round 26). Exact zeros are left out of the median.

`BBSE3 BZ Equity` `CAPITAL_EXPEND` has 6 exact zeros in 10 fiscal years (an insurer with near-zero capex). Its non-zero median (0.172)
is out of every band, so it reads `UNRESOLVED-ON-BBSE3 BZ Equity: sampled magnitude 0.172 ...`. A series that is mostly zeros has no
magnitude to classify by.

**RULED -- what you build:**
1. **A ZERO-DOMINATED class:** a key whose fiscal-year series is MOSTLY exact zeros (strictly more than half of its numeric fiscal
   years are exactly 0) reads the unit label `ZERO-DOMINATED: no magnitude: <n> of <m> fiscal years are zero`, where n is the zero
   count and m the numeric-year count.
   - It is not a guessed unit and not MEASURED: the reader treats it as not measured, like UNRESOLVED. Keep its sign UNRESOLVED.
   - State its ground in a code comment.
2. **Every other key is byte-unchanged:**
   - a series with zeros in half or fewer of its years, or with none, classifies exactly as today (series median, bands unchanged);
   - a key with no series falls back as today.
3. **Tests:** `integrations/bloomberg/research/tests/test_build_unit_map_zero_dominated_round27.py` (new):
   - BBSE3's shape (6 of 10 zeros) reads ZERO-DOMINATED with `6 of 10`;
   - a planted all-nonzero series classifies by its median;
   - a series with exactly half zeros is NOT zero-dominated;
   - no network.
   Keep the builder's suites green.
4. Do NOT write the committed `field_map.json`, do NOT touch `model_block_pull.py`, and do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_zero_dominated_round27.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ac-1.zero-dominated-class.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ac-1.zero-dominated-class.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written), every S3 object. Scratch `.scratch/ac1/`. Your worktree is a SPARSE
checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO derive.
- Any long-running script runs from a NAMED file with `python -u`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ac-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round27/ac1_AC1.sh</invocation><expect>(?m)^ac1 bbse3_unit ZERO-DOMINATED bbse3_count 6 of 10 keys 100 other_unit_changes 0 bands_unchanged True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ac-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round27/ac1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the checker rebuilds a TEMP map from your builder and reads every figure of the newest block of 100 keys through the producer's
  own reader.
  - BBSE3 `CAPITAL_EXPEND` must read ZERO-DOMINATED with `6 of 10`.
  - **Every other figure's unit must be byte-unchanged** (the full (from, to) census; any move prints a `TRANS` line).
  - The bands must be unchanged.
- AC2: your tests with the builder's suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, the rule with its ground, and any `TRANS` line the checker printed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-26 analysis ruling 3 and enrichment item 1 @`3a758833b7` (msg 27460). Dry-run at base CLOUD `32894174c0`:
ac1_AC1 FAIL as designed (`ac1 bbse3_unit UNRESOLVED bbse3_count none keys 100 other_unit_changes 0 bands_unchanged True`); ac1_AC2
FAIL (no tests).
<risk>LOCAL</risk>
<status>pending</status>
<round>27</round>
<slot>~1</slot>
<fabric>site-z</fabric>
