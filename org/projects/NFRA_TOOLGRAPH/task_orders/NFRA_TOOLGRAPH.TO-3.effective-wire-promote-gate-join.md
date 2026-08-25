<task_order>
<id>NFRA_TOOLGRAPH.TO-3</id>
<title>P3 -- the quality-sensor wire (feed the exercised assurance verdict into comp_tool_health.classify_full's stubbed `effective` bool) + the PROMOTE / comp-tool-health-gate extension (UNASSURED may not be promoted) + the quality-adjusted worklist JOIN</title>
<issued_to>0.8.0_AE_CloudComp (build: tooling + gate). **STAGED -- NOT DISPATCHED.** Gated on Andrew's builder spawn + TO-2 (the Assurance plane) + PASSCRAFT-P2. **EDIT side is DAYLIGHT-HELD (`.tools/**->BASE_EXEC`): the EFFECTIVE-axis wire + the PROMOTE-gate edit touch `.tools/` / org/modules/graph and sequence BEHIND the hold.** Coordinate the PROMOTE-gate extension with NFRA_PROMOTE's owner (do NOT re-home the gate).</issued_to>
<issued_by>2.0.0_SA_COO~A (PRD decomposition 2026-07-10; returned to 1.0.0_SA_CTO~A for the arch-gate)</issued_by>
<issued_date>2026-07-10</issued_date>
<status>complete -- SPRING-CLEAN 2026-08-25: closed WITH its project NFRA_TOOLGRAPH, which was closed the same day for having no directive attachment. Closed as a record act, not a work verdict; the work is recoverable by re-minting the project. Prior status: staged</status>
<priority>P3 -- the highest-leverage / smallest change: the code already flips KEEP<->FIX on the `effective` bool; the moment the wire lands, comp-freshness flips KEEP->FIX on the axis built for it. Sequences behind TO-2 + behind the daylight hold for the enforcer edits.</priority>
<project>NFRA_TOOLGRAPH</project>

<context>
comp_tool_health's value signal is `mean_outcome_value` computed from the RESULT column (comp_tool_health.py:163,196), and RESULT = `_classify_result()` = exit-0 -> PASS (comp_log_auto.py:170). So the number meant to say "this tool is correct" inherits the success-token-bound-to-the-wrong-step fallacy: a tool that exits 0 while LYING scores value-healthy -> KEEP (comp-aws `score --class zzqq-nope` logged PASS; comp-freshness GREEN on the frozen as_of it exists to catch). The one axis that would catch "does it reach the right answer" -- EFFECTIVE -- is stubbed `None` today (classify_full(...effective=None), comp_tool_health.py:26-28,136). TO-3 feeds the exercised assurance verdict into that reserved bool.
</context>

<scope>
1. **The quality-sensor wire (smallest change, highest leverage):** feed the EXERCISED assurance verdict (from TO-2's plane) into `comp_tool_health.classify_full`'s already-stubbed `effective` bool (:136) -- **do NOT re-architect health.** The code already flips KEEP<->FIX on it.
2. **The promotion gate:** extend PROMOTE + `comp-tool-health-gate` so an UNASSURED tool/recognizer may not be promoted or cited as `ASSURED` (COMPASSURANCE R-4: HARD-block for SEV1/IAM/sovereign surfaces, nudge-and-proceed elsewhere). Coordinate with NFRA_PROMOTE's owner -- do NOT re-home the gate.
3. **The quality-adjusted JOIN:** Behavior(demand) x Assurance(quality) x Change(heat) ranks the worklist on quality-adjusted value -- "the highest-demand tool whose R1/R4/R7 is RED on a HOT surface," not the most-typed missing tool.
</scope>

<locked_invariants note="CTO~A arch-gate checks these">
  1. **SMALLEST CHANGE -- do NOT re-architect comp_tool_health:** feed the `effective` bool the code already reserves; do not fork or rebuild the health scorer.
  2. **DAYLIGHT HOLD (`.tools/**->BASE_EXEC`):** the EFFECTIVE-axis wire + the PROMOTE-gate edit are enforcer edits -- they sequence BEHIND the hold. The MEASUREMENT (reading the plane) is exercise-only and precedes the edit.
  3. **GOODHART GATE (CTO-owned, shared with COMPLEARN sec.5 + the COMPLEARN amendment):** the quality-adjusted worklist KEEPs only on a VALUE improvement (rail-escapes prevented / chains shortened / drift caught), NEVER a usage one. ONE gate, both consumers (this + COMPLEARN leg-4).
  4. **PROMOTE-gate NOT re-homed:** coordinate the extension with NFRA_PROMOTE's owner.
  5. **BOUNDARY (sovereign):** no bd / 49F / Schwab read or target.
</locked_invariants>

<acceptance_criteria>
  - **AC2 (the wire, EXERCISED):** the seeded anti-correlated tool (comp-freshness, or its FALSE-target twin) flips `KEEP->FIX` the instant its ToolAudit verdict feeds the EFFECTIVE axis; with `effective=None` it reads KEEP. THE FLIP IS THE ACCEPTANCE.
  - **AC3 (the gate, EXERCISED):** an UNASSURED SEV1/IAM tool cannot be cited `ASSURED` or promoted; the block fires, naming the red rail.
  - **AC4:** the worklist ranks a RED-on-HOT tool above a merely-missing tool (quality-adjusted, not demand-only).
</acceptance_criteria>

<references>
  <ref type="prd">docs/architecture/NFRA_TOOLGRAPH_PRD.md @ 362272cce (sec.3 the wire/gate/JOIN, sec.4 P3, sec.5 AC2/AC3/AC4)</ref>
  <ref type="landing-point">comp_tool_health.py:136 (classify_full effective bool) / :163,196 (mean_outcome_value from RESULT) / comp_log_auto.py:170 (_classify_result = exit-0->PASS)</ref>
  <ref type="gate-coord">NFRA_PROMOTE (the promotion gate owner -- coordinate, do not re-home)</ref>
  <ref type="shared-gate">NFRA_COMPLEARN amendment leg-4 (the CTO-owned Goodhart gate is shared -- one gate, both consumers)</ref>
  <ref type="daylight-hold">.tools/**->BASE_EXEC (the enforcer-edit hold the wire + gate-edit sequence behind)</ref>
</references>

<data_reprocess_scope><no_reprocess_needed>Enforcer edits (comp_tool_health wire + PROMOTE-gate) -- daylight-held. No served pipeline artifact; the EFFECTIVE-axis flip is the exercised acceptance.</no_reprocess_needed></data_reprocess_scope>
</task_order>
