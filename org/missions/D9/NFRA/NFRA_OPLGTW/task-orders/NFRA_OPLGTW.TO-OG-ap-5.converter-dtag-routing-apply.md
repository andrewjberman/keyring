# NFRA_OPLGTW task order -- `OG-ap-5` -- APPLY: the Schwab converter's table-tag routing (OG-pn-1 Phase B) and the re-run of the six held 08403355 dates

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-5</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- `opal-assets-silver-schwab` fires on bronze ObjectCreated for three masters and on the 12:15Z sweep; the daily pulls land 09:45/10:15/10:45Z and 21:45/22:15/22:45Z. Apply and re-run outside [09:15,11:35)Z, [12:00,12:50)Z and [21:15,23:35)Z. Not the gateway host; independent of the gateway queue. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; the converter's role and policies are unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~50/NEVER_WIDEN_ASK_OG-pn-1.md: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-pn-1_20261009.md @d41a3068cd, CTO org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_OPLGTW_OG_PN1_DTAG_ROUTING_20261009_Z.md @d66a0fb956 (C1 met by @b3e481b261).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-5` (decomposition addendum R3-T.40)

Deploy the converter change built under OG-pn-1 (`data/assets/scripts/silver/schwab_conversion.py`, packaged byte-equal in
`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, drained @6a27bceca1 and @a4c8b3d53d): a scanned table is graded
by its own D-tag; a D2-only file lands its pinned 0-row section-1 tables; a duplicate routed section raises. Then re-run
ONLY the six held 08403355 dates. READ the ask and both halves; they BIND.

1. **Ledger** `nfra-oplgtw-og-pn-1-converter`, entry AND sentinel committed before the act (CTO C3).
2. **Record the prior** (CTO C2): the live `CodeSha256` and the artifact `VersionId` the function runs now.
3. **Build and apply** through the converter's Terraform path with `bash .tools/safe-apply.sh`, `-target` to that one
   function; the plan reads 1 resource changed, code fields only; any other row is a STOP. Never
   `aws lambda update-function-code`. Read back `CodeSha256` = the built hash, State Active, LastUpdateStatus Successful.
   Write `W/ap5_build.json` = `{"code_sha256", "prior_code_sha256", "prior_artifact_version"}`.
4. **Re-run the six held dates** by ONE direct invoke naming exactly the six bronze keys
   `schwab/08403355/bronze/rps/{20251212,20251215,20251216,20251217,20251218,20251219}/08403355.CRS<date>.RPS.zip` (no
   bronze write). Stop on any converter error. The 12:15Z sweep is the fallback only; record which path ran.
5. **Read back**: each date's completion record QUALIFIED; `fact_rps_s2` and `dim_balance` carry the file's rows,
   `fact_rps` and `dim_position` the pinned 0-row partition. Record every written key's VersionId in
   `W/ap5_rerun.json` (rollback per key, completion records first).
6. Close the ledger and commit, then run AC1 and AC2. A read-back that disagrees: roll the code back to the prior artifact
   version by the same Terraform path, delete the re-run's keys by version, ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- One Lambda's code; the six dates' re-run only. No other date, master, vendor type, bronze, grant or schedule.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-pn-1-converter.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-AE-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)nfra-oplgtw-og-pn-1-converter: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*live CodeSha256 equals the recorded build: yes; differs from the prior: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/bh1.sh AC2; echo "exit=$?"</invocation><expect>(?s)08403355: served dates 758 .*qualified 758; .*open 0; backfilled-but-not-qualified 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the new converter is live and the act is not half-landed.
- `AC2`: all 758 dates of 08403355's history now qualify -- OG-bh-1's last open criterion, read on live S3.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-5.converter-dtag-routing-apply.proof_of_spec.json`, validate it, flip
the ONE `<status>` tag to `complete` only if both PASS, and also update `lambda-source-map.json`'s `opal-assets-silver-schwab`
entry to the deployed build (its own commit). Report once to `2.0.0_SA_COO~O`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream APPLY-PN1, round 33. Halves COO @d41a3068cd, CTO @d66a0fb956; CTO C1 met by @b3e481b261 (drained @a4c8b3d53d).
- After AC2 PASS, OG-bh-1's worker re-runs its AC2 and flips that order (the issuer continues it).
- Pre-cut: ap5.AC1 base FAIL as expected (0 entries; ap5_build.json absent); bh1.sh AC2 base reads qualified 752, open 6.

<status>pending</status>
<round>33</round>
<workstream>APPLY-PN1</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
