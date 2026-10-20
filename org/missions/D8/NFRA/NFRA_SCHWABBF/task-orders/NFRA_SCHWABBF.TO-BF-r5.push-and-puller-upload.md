# TO NFRA_SCHWABBF.TO-BF-r5 -- push the pin to origin, deploy the Black Diamond key function under a second ledger entry, and upload the puller

<to_id>NFRA_SCHWABBF.TO-BF-r5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) | **outcome_ref:** FWD-1, FWD-4, FWD-6 |
**GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending`; do not act before that flip.

---

## WORKER FACE

### GO

(not yet written. It will read: inside 2026-10-21 12:00-20:00Z and finishing by 21:30Z; `TO-BF-r4` complete with its three verifies clean and the DLQ at 0; no pull fire has fallen since R4c began.)

### THE CELL

`BF-r-5`, release act(s) R5 of the 0840 cutover on all three tiers (bronze, silver, state) of master `08403355` (Tax SMA 0840-3355). Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation (act R7, NOT yours, never in this order). The pair that authorizes your acts: the COO half (the release plan, "COO half -- SIGNED") and the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c (msg 110003, covers R0-R6 and R8). Fence rows: COO half `org/missions/D8/NFRA/NFRA_SCHWABBF/ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb. Read first: the release plan `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (sections 1-6), the decomposition `org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, the CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` (its four conditions bind you), and the `/cloud-ops` skill (safe-apply, the ledger, the identity rules). The AWS CLI is `.tools/aws`.

### DO, IN ORDER

1. Preconditions, printed: the verify lines of `BF-r-4` are exit 0; `date -u` is before 21:30Z and no fire (09:45, 10:15, 10:45, 21:45) fell since the R4c copy started (read the box's `C:/schwab-sdd/daily/08403355/daily-pull.log` tail over SSM, read only, and the S3 listing for old-form keys of today's date). If a fire already wrote an old-form key for 08403355, STOP and report.
2. Open the SECOND ledger entry: `python .tools/deploy_ledger.py open --slug nfra-schwabbf-0840-key-function-and-puller-20261021 --title "NFRA_SCHWABBF 0840 key function and puller" --author 0.7.0_AE_CloudOps~NFRA1 --window-hours 4` with legs `L7|code-deploy|data/black_diamond/scripts/bronze/_monolith_bronze.py to its code home (the pre-push gate deploys it)|head-object ETag equals the repo file's md5` and `L8|s3-upload|infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 to s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1|head-object ETag equals the repo file's md5`. The entry NAMES `data/black_diamond/scripts/bronze/_monolith_bronze.py` (the deploy gate holds that file until an OPEN entry names it). Commit the entry and its sentinel together, paths-only.
3. PUSH: the pin the GO line names must be on origin. Run the push of `box/laptop` the way the box does (`.tools/box-sync.sh`, or `git push origin box/laptop`); print the pre-push gate's output (it deploys `_monolith_bronze.py`); verify with `git ls-remote origin box/laptop` that the remote head contains the pin (`git merge-base --is-ancestor <pin> <remote head>`; print both). Verify the deploy: `head-object` (and `list-object-versions`, newest version) of the code object the gate printed, its ETag against `md5sum` of the repo file `data/black_diamond/scripts/bronze/_monolith_bronze.py`. Close leg L7 with the proof.
4. UPLOAD THE PULLER (after the verify, never before): print `md5sum` and size of `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`; print the CURRENT object's ETag and VersionId (the rollback); `aws s3 cp infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1 --sse AES256`; `head-object` again: the ETag equals the md5. Read how the box picks the script up in the precedent entry `org/critical_paths/change_management/20261009T0205Z_nfra-oplgtw-og-tm-1-taxsma-master_deploy_completion.md` (leg L4 and the lines after it) and do exactly that, nothing more. Close leg L8 with the proof.
5. Close both ledger entries only when every leg of each carries proof (`deploy_ledger.py close`). Leave the first entry open if any of L1-L6 lacks proof, and say so. Save outputs under `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r5/`, commit paths-only, report.
ROLLBACK: the puller: copy the prior object version back to the same key (the bucket is versioned) and say so; the key function: redeploy the prior object version of the code object; the pin on origin stays (history is not rewritten).

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="BF6-r5-AC1" cell_refs="BF-r-5"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r5.push-and-puller-upload.proof_of_spec.json BF6-r5-AC1</invocation><expect>VALID</expect></criterion>
`BF6-r5-AC1` -- the pin is on origin, the key function and the puller are deployed with matching hashes, the second entry is closed with proof, and no old-form key for 08403355 was written in the interval.

<expected_criteria>BF6-r5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file.
- **Never:** `terraform apply` outside `safe-apply`; any apply, copy or write outside the legs this order names; deleting an S3 object or version; touching `08242234`, `08335338` or any other master's keys or grants; reading or printing a Schwab token or any secret value; a second concurrent Schwab session; enabling or editing an EventBridge rule; stopping an instance.
- **Window.** The CTO's window is 2026-10-21 12:00-20:00Z. Outside it you do nothing in this order except what its GO line allows. Any failure rolls back that order's legs in the same window (rollback per step below) and is reported at once.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R3-S<k>`; read the investigation file for the highest `R3-S<k>` and use the next; the gate may renumber it), commit the row AT ONCE with `safe-commit.sh` paths-only and tell the issuer its hash, and do not improvise. Append the row at the BYTE level (the file mixes CRLF and LF: do not use an editor that rewrites line endings).

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-r-5`.
<owned_cells>BF-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: BF6-r5-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-BF-r5.push-and-puller-upload.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-r5-AC1` BEFORE the flip. The instance records, as artifact rows, every printed output the steps ask for.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SB`):** the pre-push gate output, the remote head and the ancestor check, both ETag/md5 pairs with the prior version ids, the two entries' status, any row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the pull fires are 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO condition: no pull fire between R4c and R5; BLIND: the live EventBridge rules (read at step 1 of `BF-r-1`).
comp-iam: RUN -- no grant is added; the box role already holds the puller's firm writes (BF-r-3); the push and the S3 uploads run under the CloudOps identity; BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; findings inlined in the steps -- (1) the deploy gate deploys the named file at the first push after the second entry opens, so the entry opens only after the copies verified; (2) an old-form key written by a pull fire in the gap would be a second form (FWD-4): step 1 checks for it; (3) the puller upload follows the verified copy because a legacy-only file makes the puller's guard exit 6.
lane: the <paths> block IS the grant; CloudOps seats act on infrastructure under a task order (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE, C-DAILY; the release plan; the CTO half @e7d8af9d1c; decomposition round 6 cell BF-r-5.
