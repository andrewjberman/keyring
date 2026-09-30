# AMGT_CORPUS task order -- `CRPS-y-2` -- ROUND 23: `derive --no-sa-fallback` -- a derive that never reaches the vendor fallback

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-y-2, CRPS-y-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS or vendor call (the dry-run and stubbed tests only).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 23. Serves **a unit re-derive that can never move a value through a
vendor path**.

## 1. THE CELL -- `CRPS-y-2`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` `stage_derive(s3, security, raw_stamp)` (about
line 1134) fills Bloomberg forecast gaps through the Seeking Alpha fallback. It loads it via `_load_sa_forecast_fallback()`
(about line 366), calls it about line 937, and writes `source: "SA_FALLBACK"` figures and a `forecast_fallback` record
(`gaps_before`, `filled_by_sa`, `classification`). No switch holds it off. The CTO refused a derive whose purpose is a unit
re-label but which could also move VALUES through a vendor call: 8316 and 8766 carry 9 gaps each.

**RULED -- what you build:**
1. `stage_derive(..., sa_fallback=True)` gains the parameter. `cmd_derive` and the CLI gain `--no-sa-fallback`, which passes
   `sa_fallback=False`. Every other caller keeps today's behaviour (default True).
2. With `sa_fallback=False`, `_load_sa_forecast_fallback` is never called and no SA request is made. Each gap stays a gap
   carrying the reason it was not filled. `forecast_fallback` records `classification` `HELD_OFF` (or a name you state),
   `gaps_before` N and `filled_by_sa` 0.
3. `derive --dry-run --no-sa-fallback` prints, per security, the existing `DRY-RUN DERIVE: <sec> -> ...` line ENDING in
   ` sa_fallback held_off`.
4. `integrations/bloomberg/research/tests/test_model_block_no_sa_fallback.py` (new), with stubs and no network:
   - with the flag, the fallback loader is never called, even when gaps exist;
   - the gaps stay labelled, and `filled_by_sa` is 0;
   - without the flag, today's path is unchanged.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_no_sa_fallback.py
integrations/bloomberg/research/tests/test_model_block_sign_per_figure.py
integrations/bloomberg/research/tests/test_model_block_resolved_exception.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-y-2.derive-no-sa-fallback.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/y2/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO real (non-dry-run) derive.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-y-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y2_AC1.sh</invocation><expect>(?m)^DRY-RUN DERIVE: 8766 JP Equity -> .* sa_fallback held_off$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-y-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-y-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y5_AC1.sh</invocation><expect>(?m)^y5 blocks 97 figures \d+ sign_labelled \d+ plain_disagree 0 convention_disagree 0 unresolved_kept \d+ module_in_toplevel yes$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-y-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y5_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the CLI dry-run names the fallback held off, with the flag, for the two names it exists for.
- AC2: your tests (the fallback is never called) with the producer suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-y-2.derive-no-sa-fallback.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the parameter and flag names, and the `forecast_fallback` record a held-off derive writes.

## 7. AMENDMENT 1 (round-23 amendment 1, on 1.0.0_SA_CTO~Z's VERDICT B, msg 27053) -- this order is RE-OPENED for cell `CRPS-y-5`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` `_resolved_sign(mnemonic, security,
observed_value)` returns the field map's sign for (field, security). That is ONE label, sampled from ONE value by
`build_unit_map.classify_sign`, and it is served on EVERY figure (every fiscal year) of that field. Only when the map has no
entry does it fall back to `_sign_label(observed_value)`.

So a loss year reads `POSITIVE`. Over the 97 served blocks, 1,568 figures carry a plain `POSITIVE` / `NEGATIVE` / `ZERO` that
contradicts their own value: PROF_MARGIN, RETURN_ON_ASSET, IS_OPER_INC, IS_EPS, NET_INCOME and more.

`build_unit_map.classify_sign(mnemonic, value, security) -> (label, status, reason)` is the one sign rule:
- a text field gives `N/A (non-numeric field)`;
- `> 0` gives POSITIVE and `< 0` gives NEGATIVE, mapped through `SIGN_CONVENTIONS`: NET_DEBT to "POSITIVE (net-debt position)" /
  "NEGATIVE (net-cash position)", and CAPITAL_EXPEND to "NEGATIVE (Bloomberg cash-outflow convention ...)";
- exactly zero gives UNRESOLVED.

`model_block_pull` already loads that module by path (`_load_build_unit_map()`).

**RULED -- what you build (y-5):**
1. In `_resolved_sign` only:
   - (a) If the map resolves this (field, security) to a sign starting `UNRESOLVED`, return it unchanged. That covers the entry's
     own status or exception (round 19's `_scalar_exception`).
   - (b) Otherwise, classify THIS figure's `observed_value` with `classify_sign(mnemonic, observed_value, security)`. If MEASURED,
     return its label.
   - (c) Otherwise, return `_sign_label(observed_value)`.
   Never return a label whose sign contradicts `observed_value`. Change nothing else in the file.
2. `integrations/bloomberg/research/tests/test_model_block_sign_per_figure.py` (new), with a temp field map and no network:
   - a PLANTED LOSS YEAR: a map sign sampled POSITIVE, and a value < 0, gives NEGATIVE;
   - CAPITAL_EXPEND (the convention path): a negative value gives the cash-outflow label;
   - NET_DEBT: negative gives "NEGATIVE (net-cash position)", and positive "POSITIVE (net-debt position)";
   - a map sign that is UNRESOLVED stays UNRESOLVED;
   - an exact zero gives ZERO.
3. No served write and no derive: the re-derive is the issuer's act under a new pair. Time matters: the CTO bound is 12:00Z.

**Proof for the amendment:** AC3 and AC4 in section 5.
- AC3: your reader on every figure of the 97 newest served blocks, with the committed map: 0 plain labels, and 0 convention
  sign words, contradict their own value (base: 1,568 and 1).
- AC4: your tests with the producer suites.

Write the instance at
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-y-2.amendment1-sign-per-figure.proof_of_spec.json`, run
`python .tools/proof-of-spec-check.py <instance> AC3,AC4 --governing-order <this order>` (rc 0), then append a status tag reading
complete at the END of this file, commit, and report ONCE: each AC line and the lines you changed.

## 8. AMENDMENT 2 (issuer ruling on row `Z-W2-S17`) -- one path granted

`integrations/bloomberg/research/tests/test_model_block_resolved_exception.py::test_dict_valued_field_unchanged`, at line 69, asserts
`_resolved_sign("DICT_F", "EXC JP Equity", 1.0) == "NEGATIVE"`. That serves the map's sampled sign against a positive value, which is
exactly the behaviour VERDICT B supersedes.

**Ruled:** that one assertion expects `"POSITIVE"` (the figure's own sign), with a comment citing CRPS-y-5. The test's other
assertions, which cover the dict-valued UNIT being unchanged, stay as they are. The path is granted above. Change nothing else in that
file.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-22 analysis ruling 3 @`a940eb6813`. Dry-run at base CLOUD `afad83a02f`:
- y2_AC1 FAIL as expected: `model_block_pull.py: error: unrecognized arguments: --no-sa-fallback`.
- y2_AC2 FAIL as expected (no tests ran).
<risk>LOCAL</risk>
<status>pending</status>
<round>23</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>

**AMENDMENT 1 (issuer notes):** round-23 amendment 1 on VERDICT B (msg 27053). Re-opened for cell CRPS-y-5, because the round's issuance gate admits a re-cut only as a MODIFIED order (one issuer per round). Dry-run at base CLOUD 608cd4a257: y5_AC1 FAIL as expected (`plain_disagree 1568 convention_disagree 1 unresolved_kept 602`); y5_AC2 FAIL as expected (no tests ran).
<status>pending</status>

**AMENDMENT 2 (issuer notes):** row Z-W2-S17 ruled; path granted; the order remains pending.
<status>pending</status>

**AMENDMENT 1 executed (0.9.0_WK_AMGT_CORPUS~2):** AC3 and AC4 PASS; instance VALID.
<status>complete</status>
