# TO IRPT_BCKEND.TO-IB-pr-378 -- irpt-export-render released with persisted_by and the composition-hash binding (pin 49bc13131d), THEN the Performance client statement persist route applied

<to_id>IRPT_BCKEND.TO-IB-pr-378</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~DELL2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:**
- both halves of IB-pr-376 (packet blob f7cd532adf; COO half @66c617a5c7; CTO half @b97fa248b2, which ruled this sequencing);
- IB-pr-373's pair, step 3: the route (CTO msg 1848);
- the IAM leg, applied 2026-10-08T22:47:14Z (laptop, msgs 1843/1851);
- Andrew-direct: dell2 deploys go to `0.7.0_AE_CloudOps~DELL2` (msg 1756).

**Decomp cell:** `IB-pr-378` (decomposition section 83) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hops S07-S08 | **depends_on:** IB-pr-376
(drained), the IAM leg (applied).

---

## WORKER FACE

**Who:** `0.7.0_AE_CloudOps~DELL2`. Work in a clean worktree cut from `box/dell2` at or after the commit carrying this order. Never build
in the dell2 shared tree.

**The halves.** Read all of these at your HEAD first; if any is absent, STOP.
- IB-pr-376 packet: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~184/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-376.md`, blob
  `f7cd532adff37f002fa53c2edc94ad30a9616680`.
- IB-pr-376 COO half: `.../deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_376_PCS_BINDING_COO_HALF.md`.
- IB-pr-376 CTO half: `.../deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_376_CTO_HALF.md`.
- IB-pr-373's route row: `docs/contracts/investor-reporting/v1/routes.json`, `POST /api/scoped/investor-reporting/custody-report`
  (operation `custody-report-persist`, DECLARED, behind the CUSTOM portal authorizer).

**Part A -- the function (the export root, targeted).**
0. **Start reads.**
   - Live CodeSha256 must be `rNjtTwcmhpNdHUV7VcO1cRPcC1wHaANm1oIP+Xvf6Ek=`; otherwise STOP.
   - `release-census.py irpt-export-render --pin 49bc13131d` must print exactly `custody_persist.py` and `custody_write.py`.
   - Porcelain must be empty.
1. **BUILD_ONLY.** The built sha must equal `7T29wPhzbU/FlJpeT3MNSJ5jFWcEmi7bvHiSKECkyns=`.
2. **Offline differential replay, BEFORE the ledger.** One irpt-x10-v1 ANALYSIS and one PERFORMANCE fixture, reserved by the LIVE zip's
   code path, must read back identically through both zips. The negative control (an altered policy_sha256) must be refused by both.
   Commit the replay record. Method: `deliverables/0.9.0_WK_IRPT_BCKEND~182/` (IB-pr-374's replay).
3. **Ledger** (NEVER-2), opened with its sentinel committed. Rollback: S3 version `WiLXOyzMQ8_U42fSAeTIOwyMyw9.A9X3`.
4. **Upload, plan, apply.** Upload; plan the export root to a planfile (only this function's code and object version, `0 to destroy`);
   commit the plan text; `safe-apply`.
5. **Equality reads.** Re-read live: it must equal `7T29wPhz...`. Re-plan: 0. Census: 0. Deploy record. Clean the residue.

**Part B -- the route (the api root, targeted), ONLY after Part A's live read shows `7T29wPhz...`.**
6. Plan `infra/aws/terraform/investor-reporting/api` TARGETED at the one route resource for `POST
   /api/scoped/investor-reporting/custody-report`: `1 to add`, nothing else.
   - Commit the plan text.
   - `safe-apply` from the planfile.
   - Re-plan the same target: 0.
   - Read the route back with `get-routes` filtered to that key.
7. **Close the ledger.**
8. **Branch B.**
   - If Part A's equality fails: roll the function back the same turn, write `rolled_back: true`, file a BLOCKING row, and do NOT apply
     Part B.
   - If Part B fails: remove the route first, then roll the function back only if the CTO half's Branch B requires it (read it).

**Not in this order:** the real persist and the owner/other-firm reads. They follow IRPT_CUSTDY E2a's first real retained custody
submission (CTO msg 1848). The KMS statements are APPLIED, not EXERCISED, until that persist.

**After-reads file:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IB90-1_pcs_release_after_reads.json`, holding:
- `pin`, `census_changed_members`, `start_live_codesha`, `built_sha`, `post_census_changed_members`, `replan_changes`;
- `replay: {identical, negative_control_refused_by_both, record_commit}`;
- `route_applied_after_function_live`, `route_replan`, `ledger_entry`, `ledger_closed`, `rolled_back`, `rollback_source_version`,
  `limits`.

<criterion id="IB90-1-AC1" cell_refs="IB-pr-378"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r90/p90_cells.py" . IB90-1-AC1</invocation><expect>IB90-1-AC1 PASS</expect></criterion>
`IB90-1-AC1` -- pin 49bc13131d, exactly the two members, the start sha equal to the rollback target, built == live (re-read live),
census 0, re-plan 0, replay identical with the negative control refused by both, not rolled back. Base: FAIL (no file).

<criterion id="IB90-1-AC2" cell_refs="IB-pr-378"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r90/p90_cells.py" . IB90-1-AC2</invocation><expect>IB90-1-AC2 PASS</expect></criterion>
`IB90-1-AC2` -- the route is live (re-read live, filtered to its key), applied only after the function was live, route re-plan 0,
ledger closed. Base: FAIL (no file).

<expected_criteria>IB90-1-AC1, IB90-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and nothing else.
- **The only served changes** are irpt-export-render's code (Part A) and the one route (Part B). No IAM (the leg is applied), authorizer,
  table, bucket, other route or other function. Targeted applies only.
- **No real persist and no firm-bucket read from dell2.** No vendor call, no call off Opal infrastructure, no monitor, alarm, SNS or SES.
- **Refusal clause.** A moved start sha, a census other than the two members, a built sha other than the packet's, a failed replay, a
  plan touching anything else, or a failed read-back: STOP, file a row, apply nothing more (Branch B if already applied).
- **Row ids** are `IRPT_BCKEND-D2-S<n>`; `surfaced_at` is the real time. Commit with your own author line via
  `bash .tools/safe-commit.sh -F <msgfile>`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-378.pcs-binding-release-then-route.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/api/
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/lambda/ci/CHANGELOG.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 83 (round 90, workstream ~P), cell `IB-pr-378`.
<owned_cells>IB-pr-378</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB90-1-AC1, IB90-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~DELL2/IRPT_BCKEND.TO-IB-pr-378.pcs-binding-release-then-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2`: commit hashes, built and live CodeSha256, the route read-back, both criteria's last lines,
the ledger entry, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- IB-pr-376 census at 49bc13131d (IB88-1-AC1, issuer re-run): custody_persist.py + custody_write.py, one function; route row DECLARED in routes.json (IB-pr-373), behind the CUSTOM portal authorizer.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes here; the IAM leg applied 22:47:14Z (laptop CloudOps, CloudTrail 717f3ed8, 11/11 simulations).
comp-routes: RUN -- the one route POST /api/scoped/investor-reporting/custody-report is added, targeted, after the function's new sha is live; api 7k3ed8px20 lists 115 routes before (IB77-1-AC1 read).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p90_cells.py dry-run at base (box/dell2 with b97fa248b2) on dell2 2026-10-08 ~23:0xZ: IB90-1-AC1 FAIL, IB90-1-AC2 FAIL (no file); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; dell2 applies by its own applier (Andrew-direct msg 1756).
</preflight>
