# TO NFRA_TRNSPT.TO-TR-rl22 -- the Teams pull survives a LISTING error of one series: record the series, carry on, finish the run

<to_id>NFRA_TRNSPT.TO-TR-rl22</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>pullfixlist</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-rl-22` (`decompositions/NFRA_TRNSPT_DECOMP_R22.md`, AMENDMENT 3) | **outcome_ref:** FWD-3 |
**depends_on:** NFRA_TRNSPT.TO-TR-rf22 (complete)

---

## WORKER FACE

### THE CELL

`TR-rl-22`: TO-TR-rf22 made `_pull_series` in `data/transcripts/scripts/teams/pull.py` survive a refused content READ of one row. The
LISTING call two lines above it has the same hole. Measured at 2026-10-11T03:07Z: `list_meeting_transcripts` for the fourth series,
`research_meeting`, raises `GatewayGraphError` (status 502). That class is not a `Refused`, so the `except Refused` branch does not catch it,
the error leaves `_pull_series`, and `pull.run` ends before the run record is written.

**Build (the repo code and its tests only; nothing is deployed by this order):**
1. In `data/transcripts/scripts/teams/pull.py` `_pull_series`, on the listing call only: add a branch for the row-scoped classes already
   named in `_ROW_READ_REFUSALS`. It does what the `except Refused` branch does (`out["listing"]["refused"] = True`, `out["refused"] += 1`,
   one outcome with `"outcome": REFUSED`, `return out`), with `detail` = `"list <ClassName> status=<n>"` (class name and status only; never
   the body, never the bearer). The `except Refused` branch stays as it is and stays first.
   - `GatewayUnauthorized`, `GatewayNeedsLogin`, `GatewayNotConfigured` and `GatewayToolsAbsent` raised by the listing still raise.
   - Change nothing else in the file.
2. In `data/transcripts/scripts/tests/test_pull_read_refused.py`, add two tests (same injected-transport and in-memory S3 pattern the file
   already uses; no AWS, no HTTP):
   - `test_listing_error_is_recorded_and_the_run_continues`: `pull.run` over the real `series.json` with the LAST series' listing raising
     `GatewayGraphError`; the run returns, that series reads `refused == 1` with an outcome whose detail starts `list GatewayGraphError`,
     every series has an entry, and with `apply=True` the run record is written.
   - `test_run_wide_listing_refusal_still_raises`: a listing that raises `GatewayUnauthorized` still raises out of `pull.run`.

### ACCEPTANCE

<criterion id="TR22-rl22-AC1" cell_refs="TR-rl-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py rl22</invocation><expect>R22-RL22-OK</expect></criterion>
`TR22-rl22-AC1` -- the two named tests exist and the four pull test files pass together.

<expected_criteria>TR22-rl22-AC1</expected_criteria>

Dry-run at the base: `R22-RL22-FAIL missing test_listing_error_is_recorded_and_the_run_continues, test_run_wide_listing_refusal_still_raises`
-- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS or HTTP call, no deploy, no Terraform, no change to `gateway_client.py` or any other module. No transcript text
  anywhere: ids, dates, statuses and counts only. ASCII only.
- If the fix cannot be made on the listing call of `_pull_series` alone, file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused
  across every document under `surprise-channel/`) naming why, and stop.

<paths>
data/transcripts/scripts/teams/pull.py
data/transcripts/scripts/tests/test_pull_read_refused.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R22.md</decomp_doc> (round 22, AMENDMENT 3), cell `TR-rl-22`.
<owned_cells>TR-rl-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR22-rl22-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-rl22.pull-survives-listing-error.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR22-rl22-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the lines changed in `pull.py`, the classes caught on the listing and the ones left to raise, the two test names with pass or
fail, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build; the deploy is cell TR-ra-22 under its pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no new AWS call.
comp-adversary: RUN -- sources: the issuer's 03:07Z status-only listing read of the four series (research_meeting: GatewayGraphError 502, isRefused False), TO-TR-rf22's diff @12c64f3c1f; BLIND to why Graph answers 502 for that meeting. Traps: a blanket catch hiding an expired bearer on the listing (run-wide classes still raise, and a test holds it); a listing outage read as an empty series (it is recorded REFUSED with its class, never as zero rows).
lane: the paths block.
</preflight>

Source: the issuer's own packet defect (R22_TR_RA22_DEPLOY_PACKET_20261011.md section 3 predicted the research listing as REFUSED instead of
reading it); decomposition round 22 AMENDMENT 3, cell TR-rl-22; TO-APPLY-ra22 HALTED until this merges.
