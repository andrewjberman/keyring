# NFRA_OPLGTW task order -- `OG-ti-2` -- finish the one-process isolation: no per-module reset seam, the S40 subset green

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ti-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~25</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- test fixtures only; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local tests; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-17 analysis s.4 item 4; rows Z-W15-S37, S40).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ti-2` (decomposition addendum R3-T.11, item 4)

OG-ti-1 (round 17) made the whole schwab set pass in one process. It did so with a SEAM: `tests/conftest.py` clears the
StreamableHTTP session manager's `_has_started` flag around every module, and `test_schwab_rl5_asset_query.py` patches
the class-level cached service. Rows Z-W25-S2 and Z-W15-S40 show the isolation is incomplete:
- other `og_v2` tests still read the first-built cached service;
- the S40 subset fails in one process: yearinreview, q7 download, rl5 asset query, schwab_query, grain_r9 and
  `test_ogz2_ac08` (4 failed and 2 errors at round 17).

Finish it so that ordering CANNOT matter, without the reset seam:
- Each test module or fixture builds its own app and session manager, or the harness builds a fresh one per use.
- Each test reads a fresh service rather than a process-cached one.
- Fixes go in test fixtures and test helpers ONLY. If a fix needs a product file, file a BLOCKING row naming it and
  stop that line.

Prove it three ways: the whole set in default order, in `-p no:randomly` order, and with the file list reversed. Also
run the S40 subset in one process. Record every run in `TI2_RUNS.md`.

## 2. BOUNDS

- No product code (`app/`) and no deploy. Never delete, skip or xfail a test. The collected total must not drop.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W25-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ti-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r18/checks/ti2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)conftest reset seam refs 0; whole set: collected \d+, errors 0, failures beyond baseline 0 \[\]; S40 subset: passed \d+, failed 0, errors 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/NFRA_OPLGTW.TO-OG-ti-2.schwab-isolation-finish.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 18 (R3-T.11, item 4). It touches `tests/` in parallel with OG-ln-1's port (OG-ln-1 adds
  `test_schwab_host_inputs.py`). The issuer re-runs `ti2.AC1` on the drained union.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>18</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
