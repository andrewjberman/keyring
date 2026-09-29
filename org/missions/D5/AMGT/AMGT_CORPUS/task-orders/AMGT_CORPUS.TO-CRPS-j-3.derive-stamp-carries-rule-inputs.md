# AMGT_CORPUS task order -- `CRPS-j-3` -- ROUND 8: the model-block derive reads the newest LANDED raw stamp that carries the current case rule's inputs, and says per key which stamp does or that none does

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-j-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; no derive is run.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads of landed raw only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 8. Serves the served-Base-case guard of **FWD-12** through rows
`Z-S47` / `Z-W2-S10`. **Read `integrations/bloomberg/READ_HERE.md` before anything else in `integrations/bloomberg/`** -- and
note this cell never talks to the Bloomberg terminal or any vendor: it reads raw that has ALREADY LANDED in S3.

## 1. THE CELL -- `CRPS-j-3`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` has stages `pull` (vendor), `derive` (landed
raw -> `model_block.json`) and `cases-report` (read-only: rebuild the cases in memory from the newest landed raw and print
one line per key). Both `derive` and `cases-report` choose the raw via `_latest_stamp(s3, sec_key)`: the newest stamp that
carries BOTH a `refdata` and a `histdata` bronze object (`_stamps_with_raw_pair`). Since today (@`b56fef3032`) the Base case
is computed by ONE rule, `lib/research/api/case_rule.py` (`compute_cases`; `model_block_pull._compute_cases` delegates to
it): adjusted P/E = median of (PX_LAST / f) / IS_COMP_EPS_ADJUSTED over closed fiscal years joined on fiscal year;
Base = consensus EPS x that P/E x f. Measured by the issuer over all 97 block keys (read-only `cases-report`): 69 SERVED,
and six ABSENT with *"no adjusted P/E history on the landed block (no closed fiscal year carries both a PX_LAST and a
pos..."*: **6861_JP_Equity, BZLFY_US_Equity, CAT_US_Equity, CSL_AU_Equity, PBR_US_Equity, TSM_US_Equity**. For two of
them (6861_JP, CSL_AU) the earlier diagnosis (row `Z-S47`) found an OLDER landed histdata stamp carrying history the newest
stamp lacks. Whether an older landed stamp carries what the CURRENT rule needs is not yet measured for any of the six.

**RULED -- what you build:**
- A read-only stage `stamp-census --securities <tickers...>` (add it to `main`'s `stage` choices). For each key, over the
  stamps `_stamps_with_raw_pair` returns (newest first), it reads each stamp's landed raw with the module's own readers and
  reports whether the stamp carries the rule's inputs -- i.e. `case_rule.compute_cases` over that stamp's figures does NOT
  refuse for missing history/EPS (a currency refusal is not an input refusal; report it as carrying). Per key, one line
  `stamp <key> newest <stamp> newest_carries <yes|no> carrying <stamp|none>`; final line EXACTLY:
  `stamp_census keys <N> newest_carries <a> older_carries <b> none_carries <c> sum <a+b+c>`. Writes nothing.
- The stamp SELECTION used by `derive` and `cases-report`: the newest qualifying stamp that carries the rule's inputs; if no
  landed stamp carries them, the newest qualifying stamp exactly as today (so the refusal and its reason are unchanged). A
  key whose newest stamp already carries the inputs selects the same stamp as today -- nothing moves for it.
- Do NOT edit `lib/research/api/case_rule.py` (AMGT_RESAPP's rule) or any rule constant; this cell changes which landed raw
  is read, never how a case is computed.
- `integrations/bloomberg/research/tests/test_stamp_inputs_selection.py` (new), offline fixtures: newest carries -> newest
  selected; newest lacks, an older carries -> the older; none carries -> the newest (and the refusal reason unchanged); the
  census partition sums to the keys read.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_stamp_inputs_selection.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-j-3.derive-stamp-carries-rule-inputs.md
</paths>

READ-ONLY: every other file, `lib/research/api/case_rule.py` included; every landed S3 object. Scratch `.scratch/j3/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NEVER run `pull` (vendor) or `derive` (it writes served blocks); `cases-report`
  and `stamp-census` only. No Bloomberg terminal, MCP or gateway call.
- The existing tests under `integrations/bloomberg/research/tests/` keep passing unmodified (`test_latest_stamp_raw_pair.py`
  pins today's pair rule: your selection sits ON TOP of it); if one pins behaviour this rule must change, REFUSE with its name.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-j-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j3_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-j-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j3_AC2.sh</invocation><expect>stamp_census keys 6 newest_carries \d+ older_carries \d+ none_carries \d+ sum 6\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-j-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j3_AC3.sh</invocation><expect>j3 keys_read 97 of 97 unserved_vs_base 0 of \d+ ratio_moved_vs_base 0\b</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on the six keys' real landed raw (the partition, whatever its values); AC3 the
  bound over all 97 keys against the issuer's base log taken at the cut: no key served at the base is unserved, and no served
  ratio moves (a key moving ABSENT -> SERVED is the intended effect and is only listed).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-j-3.derive-stamp-carries-rule-inputs.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's per-key lines and summary; AC3's `newly_served` line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-7 analysis s.5 item 3 @`03327ebbf9`, RE-GROUNDED at L5 (decomposition v8.0 s.1a; row `Z-S51`): the
rule moved under `Z-S47` at @`b56fef3032`. No re-derive or re-mint follows this round (decomposition s.8): a derive under the
new rule would move 48 served ratios and 22 dispositions. Checks dry-run at the base @`e3fd90cb63`: AC1 FAIL (no test file),
AC2 FAIL (argparse refuses `stamp-census`), AC3 PASS (`j3 keys_read 97 of 97 unserved_vs_base 0 of 69 ratio_moved_vs_base 0`,
105 s).

<risk>LOCAL</risk>
<status>pending</status>
<round>8</round>
<slot>~3</slot>
<fabric>site-z</fabric>
