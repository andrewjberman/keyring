# NFRA_OPLGTW task order -- `OG-pm-1` -- re-measure p95 over the first full trading day on 4b6b823fae and grade it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~27</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read after a dated window closes; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- CloudWatch GetMetricStatistics read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-16 analysis s.4 item 5, row Z-W16-S5).
EGRESS CLASS, declared: NONE beyond read-only Opal AWS (CloudWatch, EC2_MANIFEST history).
</preflight>

## 1. THE CELL -- `OG-pm-1` (decomposition addendum R3-T.10, item 5; row Z-W16-S5)

Row Z-W16-S5 (REMEDIATION_v3, OPEN): p95 after `4231bd2ddc` read 0.955 s over 5 off-hours hours (546 requests).
- That is +72.5% against OG-p-1's 0.5535 s reference, above the 20% cap.
- The remedy: re-measure over at least one full trading day, against the same reference and cap, and grade it.

**HANDED after 2026-10-06T00:00Z** (the window must have closed). Then:
1. Reuse `deliverables/0.9.0_WK_NFRA_OPLGTW~16/probes/assemble_capacity_r4.py`'s metric read: ALB `TargetResponseTime`
   p95 for the opal-gateway target, `GetMetricStatistics`, ONE period of 86400 s over
   `2026-10-05T00:00:00Z`..`2026-10-06T00:00:00Z`.
   - Also read `RequestCount` and the 5xx sum for the same window.
   - Also read the 24 hourly p95s, for the record only.
2. **Served release over the whole window:** `EC2_MANIFEST.json` git history shows `4b6b823fae` deployed at
   `2026-10-04T23:12:32Z` and no later deploy before the window end. A host md5 read at the run time is the second
   witness. If another release landed inside the window, record `served_whole_window: false`; the record still stands
   but cannot PASS, so file a row.
3. Write `P95_R17.json`:
   - `window_start`, `window_end`;
   - `served_release`, `served_whole_window`;
   - `request_count`, `5xx_sum`, `p95_seconds`, `hourly_p95`;
   - `reference_seconds: 0.5535`, `cap_fraction: 0.20`;
   - `verdict`: `WITHIN_CAP` when `p95 <= 0.6642`, else `REGRESSION`;
   - `row_id` when the verdict is REGRESSION.
4. **REGRESSION:** file a row for the CTO (`spec_asserts` = the 20% cap; `world_is` = the measured p95, request count,
   and the hours that drive it) and name it in `row_id`. Do not investigate the cause beyond the hourly profile.

## 2. BOUNDS

- Read-only. No host change, no alarm, no monitor, no dashboard (standing moratorium).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W27-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/pm1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)window 2026-10-05T00:00:00Z\.\.2026-10-06T00:00:00Z; served 4b6b823fae whole window True;.*verdict (WITHIN_CAP|REGRESSION); consistent True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/NFRA_OPLGTW.TO-OG-pm-1.p95-full-trading-day.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 5). Alone.
- An essential wait, qualified: the measured object is a full trading day that has not yet occurred at the cut
  (Sunday 2026-10-04 ET). Its reason is the row's own remedy, and its word is the CTO's analysis item 5 ("the first full
  trading day on 4b6b823fae (Monday 2026-10-05)"). The issuer hands the order after 2026-10-06T00:00Z.
- AC1 passes on either verdict: the cell grades and does not tune.
- Pre-cut: `pm1.AC1` FAIL (the record is absent).

<status>pending</status>
<round>17</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
