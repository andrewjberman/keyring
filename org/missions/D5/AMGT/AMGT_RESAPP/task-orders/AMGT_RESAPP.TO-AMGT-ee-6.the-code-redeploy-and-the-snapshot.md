# AMGT_RESAPP task order -- `AMGT-ee-6` -- THE ROUND-81 REDEPLOY OF `opal-amgt-scoped-api`: THE NAME-RESOLVING ROUTE, THE LONG-FORM DATES, AND THE /freshness SNAPSHOT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ee-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm or cadence; one redeploy and one invoke of the existing snapshot event.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM line moves; the plan STOPs on any IAM change.
comp-adversary: RUN at the cut -- live OUOsYXa (dd-4, 03:37:34Z) 404s a typed ticker or name and serves ISO days in the /freshness words. The build will also carry dd-1's merged section_coverage.py (each 20-F name's passage_coverage lists Item 4.B as wanted).
EGRESS CLASS, declared: NONE for the build (wheels local); terraform init already done on this box (dd-4).
</preflight>

## 1. THE ACT -- `AMGT-ee-6` (round 81, decomposition s.89)

Under ONE NEVER-2 entry and ONE never-widen pair, as round 80's dd-4 did (its order is the model:
`org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-dd-4.the-code-redeploy-from-dell1.md`), with TWO legs:

1. **Code leg.** The live package downloaded from `get-function` `Code.Location` and hash-checked as the rollback; the build from a
   DETACHED worktree at EXACTLY the commit the GO names, `--build-only`, wheels from `C:/tmp/r80-wheels` re-hashed against
   `round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt`; the CONTENT-DIFF lists exactly the files the pair names (a file not on it is a
   STOP); CTO condition 5 again (load_registry() and one address() from the built files before the apply; one /thesis GET 200 after);
   ONE `safe-apply`, the plan read whole and refused on any change outside the function's code; the new CodeSha256 differs from the
   live one and equals the built file's.
2. **Snapshot leg.** After the code leg, invoke the snapshot's scheduled event once
   (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so /freshness is re-written by the new code; read its stamp.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/` first.
`r81_deployed_cells.txt` (beside the round-81 checks) lists the deployed checks; the GO states how many lines it holds.
A failing criterion is the ROLLBACK trigger: the kept live package through the module, one `safe-apply`, same session.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no route added, no schedule change, no S3 delete, no vendor or SEC
   call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ee-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-81 deployed check passes; R81 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ee-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_deployed.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_deployed.py"; echo "exit=$?"</invocation><expect>R80 DEPLOYED: YES and R79 DEPLOYED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ee-6.the-code-redeploy-and-the-snapshot.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the prior and new CodeSha256, and the kept paths;
- the CONTENT-DIFF and the pip log's index-request count;
- every criterion's output lines;
- the snapshot stamp after the event and what the event printed.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Serves AMGT-ee-1 and AMGT-ee-2 on the live function, and carries dd-1's merged section_coverage.py served change. STAGED: waits for ee-1 and ee-2 to drain, the pair (COO + 1.0.0_SA_CTO~DELL1), and the build commit. AC1 base: NO CELLS LISTED exit 2 until the GO fills the list.

<status>staged</status>
<round>81</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>pending -- AMENDMENT 1 + GO 2026-10-09T05:0xZ by the issuer: RE-ADDRESSED to 0.7.0_AE_CloudOps~RA1, a fresh lane seated for AMGT_RESAPP only (MSTR~DELL1 msg 1745), on to-decomp-ref-lint's seating finding (0.7.0_AE_CloudOps~DELL1 holds ETFS_RIVALS; rule 27). GO terms: build pin 881540dcfd exactly; wheels C:/tmp/r80-wheels re-hashed against the round-78 record; pair COO @f4288f543a + CTO @1e8dff07a6 (five conditions: the content-diff list or STOP; load_registry + address() from the built files before apply, /thesis 200 after; rollback package hash-checked OUOsYXa and the snapshot's pre-event VersionId recorded; code leg verified before the snapshot event; ledger opened before apply, closed after the snapshot leg, record-terraform-deploy.sh run). r81_deployed_cells.txt holds 2 lines (@1ff7bcb7f9), both NO on the live base; run AC1 after the snapshot leg. terraform init of harvest/ was done on this box by dd-4. Graded by no gate limb (a modification).</status>
