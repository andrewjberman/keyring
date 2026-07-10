<task_order>
<id>NFRA_COMPLEARN.AMD-P3c</id>
<title>AMENDMENT P3c -- ingestion honesty: the universal writer `comp_log_auto.py` swallows a dropped emission under try/except pass -- add a disclosure (count/marker) so a dropped row is DISCLOSED, not swallowed (R5/R7)</title>
<issued_to>0.8.0_AE_CloudComp (~E context). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn. **EDIT is DAYLIGHT-HELD (`.tools/**->BASE_EXEC`): `comp_log_auto.py` is an enforcer/`.tools` file -- the disclosure edit sequences BEHIND the hold.**</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>staged</status>
<priority>P3c -- closes the "census of survived failures" hole one layer down in the loop's own ingestion. Small, but load-bearing: a silent-noop writer means the whole loop's freshness/health signal can be undercounting invisibly. Sequences behind the daylight hold (it edits an enforcer).</priority>
<project>NFRA_COMPLEARN (amendment: NFRA_COMPLEARN_amend_loop-closure_20260710.md)</project>

<context>
The universal writer `comp_log_auto.py` writes under `try/except pass` (silent-noop) -- a dropped emission is INVISIBLE. A passing assertion never mutated has never been tested; an error log is a census of SURVIVED failures. P3c makes a dropped row DISCLOSED, not swallowed.
</context>

<scope>
1. Add a disclosure (count/marker) to `comp_log_auto.py` so a dropped emission is DISCLOSED, not swallowed (R5/R7).
2. Exercise it: force a write failure and observe the disclosure.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **DISCLOSE, don't swallow:** the try/except pass must not silently drop; a dropped emission surfaces a count/marker (R5/R7 honesty).
  2. **EXERCISED, not asserted (AC-L3c):** prove it by FORCING a write failure and observing the disclosure -- a passing assertion never mutated has never been tested.
  3. **DAYLIGHT HOLD (`.tools/**->BASE_EXEC`):** `comp_log_auto.py` is an enforcer file -- the edit sequences behind the hold (the amendment's ONE daylight-held leg; P3a/P3b are infra/exercise, not enforcer edits).
  4. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target.
</locked_invariants>

<acceptance_criteria>
  - **AC-L3c:** a dropped `comp_log_auto` emission is DISCLOSED (count/marker), not swallowed; EXERCISED by forcing a write failure and observing the disclosure.
</acceptance_criteria>

<references>
  <ref type="amendment">docs/architecture/NFRA_COMPLEARN_amend_loop-closure_20260710.md @ 362272cce (A1 P3c, A2 AC-L3c)</ref>
  <ref type="target">comp_log_auto.py (the try/except pass silent-noop writer; :170 _classify_result)</ref>
  <ref type="daylight-hold">.tools/**->BASE_EXEC (the enforcer-edit hold this sequences behind)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Enforcer edit (comp_log_auto disclosure) -- daylight-held. No served pipeline artifact.</no_reprocess_needed></data_reprocess_scope>
</task_order>
