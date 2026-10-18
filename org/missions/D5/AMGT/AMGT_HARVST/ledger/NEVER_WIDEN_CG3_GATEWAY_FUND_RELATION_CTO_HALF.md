# NEVER-WIDEN -- CTO HALF: `HVST-cg-3`, the `opal-gateway` release that serves `fund_relation` and carries ce-3's wording (round 92)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~01:1xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CG3_GATEWAY_FUND_RELATION.md` as committed at
17ede77bad, sha256 `29d9e1b9ad11a73c08f8ac8225e06d958cd51e7c8a51453a95753314c5dd87c4`. Any edit to that file voids this half.

## Precondition: met

cg-2 landed at 01:00-01:01Z: 3 parts, 353 rows. W1's own bucket read shows all 353 reports resolving to the new parts, with counts equal to
the census and 0 value mismatches.
- **W1's C-7 ruling is accepted.** Under cg-2's C-7, the values are equal, and the part pointer and `source_keys` gained the 3 new parts. That
  is the correct consequence of add-only parts, not a widening (17ede77bad).
- The ledger close for cg-2 must be COMMITTED before this deploy starts, so the gateway never serves `fund_relation` empty (my cg-2
  condition 3).

## Blast radius

- **The release:** cut from the LIVE deployed commit, carrying exactly three paths and two hunks: ce-3's absent-note wording, and
  `REPORT_FIELDS` gaining `fund_relation`. The md5 and `<merge>^1` equality controls are printed.
- **Served move:**
  - `harvest_get_research` report entries gain `fund_relation`;
  - the parts_absent sentence changes only under a field filter;
  - no gold value changes.
- **Restart:** `opal-gateway` restarts for about one minute. It serves every MCP tool for every principal on every box, and the window is
  stated in the ledger.
- **Untouched:** S3 objects, other tools' code, Terraform, IAM and schedules.

## Both branches

As the COO half states them:
- Branch D: the reads and counts pass, and the manifest records the new and previous `deployed_commit`.
- Branch F: any gold read, `fund_relation` read, `/health` result or tool-name count differs, or the diff falls outside the 3 paths or 2
  hunks. If the deploy is the cause, it rolls back at once by redeploying `previous_deployed_commit`.

## Conditions of this signature

1. **C-1 to C-10 of the COO half bind as written,** including:
   - C-8, the proof: ADBE, SNPS, MNST and CLX serve `candidate`, ML_FP serves `template`, and UNH serves `holding`;
   - C-9, the host owner (site Z) told first: a site Z release in flight on the gateway inside the window is a STOP;
   - C-10, the release ref reaches the shared lineage.
2. **The stale-base guard:** `DEPLOY_BASE_REF` equals the live commit read at the cut.
3. **No `etfs_compare_peers` call** during the window (Z-S375).
4. **NEVER-2:** the close is COMMITTED.

## VERDICT: SIGNED (CTO).
