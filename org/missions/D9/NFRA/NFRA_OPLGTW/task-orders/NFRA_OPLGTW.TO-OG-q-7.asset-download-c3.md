# NFRA_OPLGTW task order -- `OG-q-7` -- the C3 holdings restriction on the dim_asset download paths

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-q-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the restriction reads the same position snapshot the query path reads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-16 analysis s.4 item 1).
EGRESS CLASS, declared: NONE (local tests under moto; no live call).
</preflight>

## 1. THE CELL -- `OG-q-7` (decomposition addendum R3-T.10, item 1)

Served gateway `4b6b823fae` answers a `dim_asset` QUERY under the C3 holdings restriction but REFUSES the same
`dim_asset` DOWNLOAD (`UNAVAILABLE asset_policy_selection_unavailable`). That is FWD-4's gap.

In `infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py` (CLOUD at the cut):
- The query path applies the restriction at about `:621-654`. It calls `sem.qualify_asset_plan`, using a qualified
  position snapshot for the same master and date, filtered to the grant's accounts, and it does so before any engine
  job. The function is in `app/integrations/schwab/semantics.py:330-360`. It denies `asset_read_denied_unqualified` on
  an empty holding set or when there are no position sources. Otherwise it appends `PolicyFilter(cusip in held)`.
- `prepare_download` (about `:816`) and `export_query` (about `:893`) instead refuse with the placeholder
  `if q.dataset == "dim_asset" and self._asset_policy is None: raise ServiceError(UNAVAILABLE, "asset_policy_selection_unavailable")`.

Do this:
1. Apply the SAME mechanism on both download paths, reusing the query path's code (extract a helper if the three call
   sites would otherwise copy it), and retire the two guards.
2. Leave `build_default_service()` and the `asset_policy` constructor parameter byte-identical, so the acceptance seam
   still works.
3. Add `tests/test_schwab_q7_asset_download.py`, built through the shipped `build_default_service()` construction with no
   seam (copy the harness of `tests/test_schwab_rl5_asset_query.py`). It holds four named tests:
   - `test_ogq7_ac01`: a `dim_asset` `prepare_download` returns only CUSIPs held by the grant's accounts.
   - `test_ogq7_ac02`: a planted UNHELD CUSIP is absent from that download.
   - `test_ogq7_ac03`: a grant whose accounts hold nothing refuses `asset_read_denied_unqualified`.
   - `test_ogq7_ac04`: the `dim_asset` QUERY returns the same held set as the download (the query is unchanged).
4. Restate `tests/test_schwab_rl5_asset_query.py`'s download-refused test. Its premise (downloads refuse) is retired
   by this cell. It now asserts the held-only download; keep its name and say so in a comment.
5. Negative control: with the old guard restored, `test_ogq7_ac01` fails. Record that run.

## 2. BOUNDS

- No release and no host act: that is `OG-rl-6`, handed after this cell drains.
- The query path's behaviour does not change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_schwab_q7_asset_download.py
infra/aws/ec2/opal-gateway/tests/test_schwab_rl5_asset_query.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-q-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/q7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-q-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/q7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)guards '_asset_policy is None' 0 \(want 0\); qualify_asset_plan call sites \d+ \(want >= 3\); failures beyond baseline 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-q-7.asset-download-c3.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, the negative control, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 1). The CTO's list calls this cell "OG-q-6". That id was taken on 2026-09-18 by
  the completed C3-rules wiring order (`TO-OG-q-6.c3-rules-wiring.md`), so this cell is `OG-q-7`.
- Chain: `OG-q-7` -> `OG-rl-6`.
- Pre-cut: `q7.AC1` FAIL (the test file is absent); `q7.AC2` FAIL (2 guards, 1 call site).

<status>pending</status>
<round>17</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
