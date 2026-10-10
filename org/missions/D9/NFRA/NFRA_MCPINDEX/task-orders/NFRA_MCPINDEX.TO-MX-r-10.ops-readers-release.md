# NFRA_MCPINDEX task order -- `MX-r-10` -- release MX-o-1, MX-o-2 and MX-c-7 onto the opal-gateway host, then read FWD-19 and E2 (FWD-18, FWD-11's guidance) live there

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-10</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-10</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~30</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the gateway host takes one release at a time (the release train).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change. A SERVED reader reads under the gateway role's existing grant (its census says where). A refused read at the live check is a BLOCKING row, never a policy edit.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-9 release pattern; never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads on the host).
</preflight>

## 1. THE CELL -- `MX-r-10` (round 9; PRD v0.8 @0eff9e0e6d FWD-19; decomposition section ROUND 9)

**Start only when MX-c-7 is complete and drained.** MX-r-9 (round 8) released d3c31e972e and its ledger CLOSED
(@3cc6f5e6ec). The issuer continues you with this order.

**Follow MX-r-9's order exactly, as amended A1-A7** (`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-9.discover-needs-release.md`).
Read the live ref from the host by md5, never from `-latest`'s label. These are the differences:
0. **THE DEPLOY TREE'S HEAD IS THE DEPLOY-ONLY COMMIT** (ruling 2c, `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b;
   row Z-S92). `deploy-to-ec2.sh` names and stamps the artifact from `git rev-parse HEAD` of the calling tree. Commit
   the shipped files and check out that commit in the deploy tree. Never leave them as working-tree edits over the
   base. After the upload, read back `opal-gateway-<deploy sha>.tar.gz` present and `-latest`'s `git-ref` equal to the
   deploy sha, BEFORE the ledger's first leg closes.
1. **What ships, by CONTENT.** The live tree, plus:
   - each SERVED reader's new `app/integrations/ops_*/` folder;
   - MX-c-7's regenerated `app/refs/DATA_CATALOG.yaml`, and its `opal_discover/integration.py` change (E2: the folds
     retired, E-13's note surfaced);
   - the drain's one registry hookup line per SERVED reader.
   A GAP reader ships nothing but its catalog entry.
2. **`ENABLED_INTEGRATIONS` WIDENS by exactly the SERVED readers' ids.** This is the release's one widening, so the
   ANNOUNCE prints the id set before and after, and their difference, for the never-widen halves to name.
   - The live `.env` KEY set is otherwise equal (keys only, never values), and both principal keys stay.
   - No tool other than the SERVED readers' tools is added (tool census before and after).
3. **NEVER-2 ledger** `nfra-mcpindex-r9-ops-readers-release`, opened at PHASE B start. Legs: upload/ship, `/health`
   200, r10.AC2 read back. Roll back to the live ref on any failed leg.
4. **The applier.** PHASE A is yours: the plan and `ANNOUNCE_MX-r-10.md` in your deliverables. PHASE B is re-addressed
   by amendment to the project's site-Z CloudOps lane (`0.7.0_AE_CloudOps~MX`). The slot is agreed by the issuer with
   `2.0.0_SA_COO~O`. PHASE B does not start until then.
5. **FWD-19's proof is on demand under an ALREADY ADMITTED principal** (r10.AC2 runs as the Opal-internal principal).
   The operations lead's own session is the organic arm, not the proof, and his admission is Andrew's (C8).

## 2. BOUNDS

1. No change to any source file. This order ships what MX-o-1, MX-o-2 and MX-c-7 committed, plus the drain's hookup
   lines, and nothing else.
2. Never bare `terraform apply`; never `update-function-code`. Nothing under `data/cot/`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r9-ops-readers-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MX/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`deploy-to-ec2.sh` is listed only for the `.env` printf line, if the `ENABLED_INTEGRATIONS` widening must be carried
there (the MX-r-7 A4 C1 pattern). No other edit.

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W30-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/r10.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/r10.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; SERVED readers graded good n of n; routes first 4 of 4; fwd18 served,c3=3 3; guide=E-13 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/NFRA_MCPINDEX.TO-MX-r-10.ops-readers-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B, the applier writes the proof instance at the
`<instance_path>`. Then report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 9 chain tail. STAGED UNISSUED 2026-10-09 ~10:2xZ (1.0.0_SA_CTO~Z
@ff362e8444). Battery dry-run at base 1dd356991a (`round9/checks/`):
- r10.AC1 FAIL as expected: no entry at HEAD; SCAN DENOMINATOR 27 of 27.
- r10.AC2 is not dry-run at the cut. Its census inputs do not exist until MX-o-1 and MX-o-2 write them, so it is run
  once at issuance against the live host (expected: no SERVED reader, routes 0 of 2).

ISSUED 2026-10-10 ~23:4xZ in round 9's ONE issuance, from `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b. Battery re-dry-run at issuance base bf8492f48f: every check of this order FAILS there as a build check must.

<status>issued</status>
<round>9</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
