# NFRA_OPLGTW task order -- `OG-ti-1` -- the whole schwab test set passes in ONE pytest process

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ti-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~25</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- test fixtures only; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local tests; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-16 analysis s.4 item 4, row Z-W15-S37).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ti-1` (decomposition addendum R3-T.10, item 4; row Z-W15-S37)

`python -m pytest tests -k schwab` run as ONE process in `infra/aws/ec2/opal-gateway` errors at setup on 9 to 11 tests,
all `RuntimeError` from the StreamableHTTP session manager. Each erroring file passes in its own process. Known
erroring ids at the cut include `test_ogq6_ac01`-`04`, `test_ogz4_ac01`-`02`, `test_ogq4_ac01`-`03`, and the two
`test_schwab_rl5_asset_query.py` tests.

The cause class: a module-level or session-scoped app or session manager is started more than once in one process.
Give each acceptance-fixture module its OWN session manager or app instance, or a fixture that builds and tears down
per module, so that ordering cannot matter.
- Change test fixtures and test helpers only (`tests/`, including `tests/acceptance/` and any `conftest.py` there).
- If a fix needs a product file, STOP that line and file a BLOCKING row naming it.

Prove it:
1. Run the whole set in one process; it reads 0 errors.
2. Run it again with `-p no:randomly` and in reverse file order (`--reverse` if available, else list the files
   reversed); it reads the same.
3. Record all three runs in `TI1_RUNS.md`.

## 2. BOUNDS

- No product code (`app/`) and no deploy. Tests are not in any release by this cell.
- Never delete, skip or xfail a test to make the count. The collected total must not drop.
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
  <criterion id="AC1" cell_refs="OG-ti-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/ti1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)one process: collected \d+; passed \d+; errors 0; failures \d+; failures beyond baseline 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/NFRA_OPLGTW.TO-OG-ti-1.schwab-tests-one-process.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 4). Alone.
- `OG-q-7` adds a test file in parallel. The check runs on the drained CLOUD, so whichever drains second re-runs AC1
  on the union; the issuer re-grades at the drain.
- Pre-cut: see the issuance commit for the `ti1.AC1` one-process reading at b91a1a44cf.

<status>pending</status>
<round>17</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
