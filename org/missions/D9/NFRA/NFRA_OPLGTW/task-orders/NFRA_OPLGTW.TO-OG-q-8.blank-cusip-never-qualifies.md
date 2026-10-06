# NFRA_OPLGTW task order -- `OG-q-8` -- a blank or null cusip never qualifies a dim_asset row (CTO R29)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-q-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (ledger/ROUND_ANALYSIS.round22.md @a28c065593, R29/R30.1).
EGRESS CLASS, declared: NONE (local tests; no live call).
</preflight>

## 1. THE CELL -- `OG-q-8` (decomposition addendum R3-T.16, item 1)

The C3 holdings restriction on `dim_asset` builds its held set in
`infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py` at about `:341`:

    position_cusips = frozenset(row[0] for row in pos_rows)

Nothing filters out a blank. When a held position has a blank or null cusip, the blank enters the held set. The
`PolicyFilter` appended by `sem.qualify_asset_plan` (`app/integrations/schwab/semantics.py`) then admits EVERY
`dim_asset` row whose cusip is blank. A real holder's download returned 23 such rows (row `NFRA_OPLGTW-Z-W28-S1`).
The query path (about `:656-661`) and the download/export path (about `:939-946`) both take this set.

Do this:
1. At that line, drop `None` and every value that is empty after `str.strip()` from `position_cusips`. Change nothing
   else in the qualification logic. A held set that is empty after the drop already refuses
   `asset_read_denied_unqualified` in `qualify_asset_plan`; keep that.
2. Add `tests/test_schwab_q8_blank_cusip.py`, built through the shipped `build_default_service()` construction with no
   seam (copy the harness of `tests/test_schwab_q7_asset_download.py`). Four named tests:
   - `test_ogq8_ac01`: the positions hold a non-blank CUSIP plus one with a blank cusip; `dim_asset` carries rows with
     a blank cusip. The dim_asset QUERY returns 0 blank-cusip rows and the held non-blank CUSIP.
   - `test_ogq8_ac02`: the same fixture through `prepare_download`: 0 blank-cusip rows and the held non-blank CUSIP.
   - `test_ogq8_ac03`: position cusips of `None`, `""` and `"   "` are all dropped; every non-blank held CUSIP is still
     returned.
   - `test_ogq8_ac04`: a grant whose held positions carry ONLY blank cusips refuses `asset_read_denied_unqualified`.
3. Negative control: with the old line restored, `test_ogq8_ac01` and `test_ogq8_ac02` fail. Record that run in
   `W/Q8_NEGATIVE_CONTROL.md`, where `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/`.

## 2. BOUNDS

- No release and no host act: that is `OG-rl-9`, handed after this cell drains.
- No other behaviour of the query or download paths changes. `build_default_service()` and the `asset_policy`
  constructor parameter stay byte-identical.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_schwab_q8_blank_cusip.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-q-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/q8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-q-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/q8.AC2.sh; echo "exit=$?"</invocation><expect>(?s)existing asset test files green 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a blank or null cusip qualifies no row, on the query and download paths alike.
- `AC2`: the existing dim_asset tests stay green.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-q-8.blank-cusip-never-qualifies.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, the negative control, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 23 (addendum R3-T.16, item 1). Chain: `OG-q-8` -> `OG-rl-9`.
- Pre-cut 19:5xZ: `q8.AC1` FAIL (the test file is absent). `q8.AC2` PASS (4 passed + 2 passed): it is the regression
  guard and is expected to stay green.

<status>pending</status>
<round>23</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
