# AMGT_CORPUS task order -- `CRPS-ad-2` -- ROUND 28: a zero sample no longer refuses a whole series

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ad-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the served re-derive is a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: RUN by the issuer at the cut on CLOUD bd29533457 -- ad2_AC1 `ad2 keys 100 refuse 364 refuse_zero_sample 354 ba_dps_shown 0 of 10 value_moves 0 unit_moves 0 other_sign_moves 0 errors 0` (FAIL as designed); ad2_AC2 `no tests ran` (the new test file is absent); the other suites in AC2 read 38 passed at base. Blind spot: the check face's own bucket function is the only reader graded.
EGRESS CLASS, declared: NONE beyond S3 reads of opal-data-harvest.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 28. Serves FWD-20 ("a zero-valued figure whose sign is otherwise measured is
SHOWN, not refused (control: BA's DPS)").

## 1. THE CELL -- `CRPS-ad-2`

**What is wrong, measured.** `integrations/bloomberg/research/build_unit_map.py` `classify_sign` (`:490-509`) samples ONE value per
(security, field) for the map. When that sample is exactly 0 it writes the per-security sign
`UNRESOLVED-ON-<security>: sampled value is exactly zero -- sign is ambiguous, not claimed`. Then
`integrations/bloomberg/research/model_block_pull.py` `_resolved_sign` (`:734-758`) keeps a map sign that starts with UNRESOLVED on
EVERY figure of that series (its rule (a)), before it would sign the figure by its own value (rules (b) and (c)). The check face
(`lib/research/checkface/run_checks.py` `unit_status_for`) refuses any figure whose sign contains UNRESOLVED.

So Boeing's DPS -- 4.69, 5.97, 7.19, 8.22, then six years of 0.0 -- is refused in every year. Over the newest block of 100 keys: 364
refused fiscal figures, 354 of them for this reason (IS_DIV_PER_SHR and EQY_DPS on 18 names: 30 all-zero series, 6 with one sign).
The other 10 are BBSE3's capital expenditure, whose UNIT is not measured (ZERO-DOMINATED, round 27); they stay refused.

**RULED -- what you build:**
1. When the map's sign for a (security, field) is UNRESOLVED **only because the sampled value was exactly zero** (and the unit is
   measured), each figure is signed by its OWN value -- the same per-figure rule the producer already applies (`classify_sign` on the
   figure's value, else `_sign_label`): a positive figure reads its positive label, a negative one its negative label, and an exact 0
   reads `ZERO`. Choose where it lives (`_resolved_sign`, or the map's sign for that reason) and state the ground in a code comment.
2. **Everything else is byte-unchanged:** every value; every unit; every sign whose map reason is anything else (a unit-unresolved
   sign stays UNRESOLVED -- that is BBSE3's case; an absent value stays UNRESOLVED).
3. **Tests:** `integrations/bloomberg/research/tests/test_zero_sample_sign_round28.py` (new), no network:
   - a series shaped like BA's DPS (four positive years, six zeros; map sign UNRESOLVED on the zero-sample reason) signs 4.69 as
     positive and 0.0 as ZERO;
   - a unit-unresolved sign (the map reason `unit unresolved (...)`) stays UNRESOLVED on a non-zero figure;
   - an all-zero series reads ZERO on every figure.
   Keep the sign, unit-map and check-face suites in AC2 green.
4. Do NOT write the committed `field_map.json`, do NOT derive, and write no S3 object. The served blocks move only at the issuer's
   later paired act.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_zero_sample_sign_round28.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ad-2.zero-value-sign-over-refusal.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ad-2.zero-value-sign-over-refusal.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written), every S3 object. Scratch `.scratch/ad2/`. Your worktree is a SPARSE
checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. Every `.py` edit passes `.tools/commit-gate.sh` (commit via `.tools/safe-commit.sh`).
- NO vendor call, NO S3 write, NO derive.
- Any long-running script runs from a NAMED file with `python -u`. AC1 takes about 4 minutes.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ad-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/ad2_AC1.sh</invocation><expect>(?m)^ad2 keys 100 refuse 10 refuse_zero_sample 0 ba_dps_shown 10 of 10 value_moves 0 unit_moves 0 other_sign_moves 0 errors 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ad-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/ad2_AC2.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
</proof_of_spec>

- AC1: the checker rebuilds a TEMP map from your builder, runs your producer's `stage_derive` for every one of 100 keys with a
  write-capturing client (nothing is written), and grades the captured blocks with the check face's own bucket function: refused
  fiscal figures 364 -> 10, none on the zero-sample reason, BA's 10 DPS figures all shown, and no value, unit or other-sign move
  against the served blocks. It prints every (from, to) sign transition.
- AC2: your tests with the sign, unit-map and check-face suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, where the rule lives and its ground, and every `TRANS` line the checker printed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-27 analysis s.3 item 2 @`99b83b495a` (CTO+COO never-widen halves at the served act, `CRPS-ad-4`). Base CLOUD
`bd29533457`: ad2_AC1 FAIL as designed; ad2_AC2 `no tests ran`. Zero-sample census: 36 series on 18 names (30 all-zero / 294 figures;
6 one-sign / 60). A zero is a measured zero under VERDICT B (the figure signs itself), so all 354 become showable.
<risk>LOCAL</risk>
<status>pending</status>
<round>28</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
