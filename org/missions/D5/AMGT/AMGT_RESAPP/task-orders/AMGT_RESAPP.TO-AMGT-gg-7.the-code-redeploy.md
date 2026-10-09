# AMGT_RESAPP task order -- `AMGT-gg-7` -- THE ROUND-82 REDEPLOY OF `opal-amgt-scoped-api`: THE UNVGY REASON, FEED MENTIONS, THE TIMELINE PRICE SERIES AND THE PRINT LINE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm or cadence; one redeploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM line moves (the price-history read is already granted); the plan STOPs on any IAM change.
comp-adversary: RUN at the cut -- live aAkcp2l1 (ee-6) serves none of gg-4, gg-5, gg-6.
EGRESS CLASS, declared: NONE for the build (wheels local).
</preflight>

## 1. THE ACT -- `AMGT-gg-7` (round 82, decomposition s.90)

The same act as round 81's AMGT-ee-6 (`task-orders/AMGT_RESAPP.TO-AMGT-ee-6.the-code-redeploy-and-the-snapshot.md` -- read its face
whole: the rollback download, the detached build, the wheels, condition 5, the untargeted plan, one resource), ONE code leg and no
snapshot leg, at the build commit the GO names. The pair lists the CONTENT-DIFF.

**Begin only when** the GO names the build commit and both halves are committed. A failing criterion is the ROLLBACK trigger.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no route added, no schedule change, no S3 delete, no vendor or SEC
   call, no push of shared branches, no portal promote.
2. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
3. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
4. 49 Financial data never goes into another firm's tree.

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
  <criterion id="AC1" cell_refs="AMGT-gg-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round82_prep/checks/r82_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-82 deployed check passes; R82 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_deployed.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_deployed.py"; echo "exit=$?"</invocation><expect>R81 DEPLOYED: YES and R80 DEPLOYED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-gg-7.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the prior and new CodeSha256, and the kept paths;
- the CONTENT-DIFF and the pip log's index-request count;
- every criterion's output lines.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Serves AMGT-gg-4, gg-5, gg-6 on the live function. STAGED: waits for those to drain (and gg-5's wiring line), the pair, and the build commit. AC1 base: NO CELLS LISTED exit 2 until the GO fills the list.

<status>staged</status>
<round>82</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-09T07:4xZ by the issuer, on 1.0.0_SA_CTO~DELL1 msg 1999 (CTO half @fab454cb98). GO terms: build pin 7b84cfc5a9 exactly, from a DETACHED worktree; wheels C:/tmp/r80-wheels re-hashed against the round-78 record; pair COO @520c6e0f92 + CTO @fab454cb98 (ee-6 conditions 1-5 carried: the content-diff list or STOP; load_registry + address() from the built files before apply, /thesis 200 after; rollback package hash-checked aAkcp2l1 kept; ledger opened before apply, closed after, record-terraform-deploy.sh run; PLUS condition 6: print whether any request path CALLS publication_gold's alias matcher (_match_counts / mention_rows / build_mention) -- issuer's pre-read at the pin: the serve path reaches only _day_of, _latest_gold_snapshot_rows_cached, _baseline, _event_id, BACKFILL_FLOOR, so it ships INERT, which the build confirms or STOPs; condition 7: lookup('4698') read from the BUILT scopes.json, and one existing address() byte-equal before and after). r82_deployed_cells.txt holds 3 lines (@520c6e0f92), all NO on live aAkcp2l1, so AC1 expects R82 DEPLOYED: YES 3 of 3. dell1 IAM parity bounds 2-4 ride. Egress is open except Bloomberg (law edit 4d77a9c3ea); no Bloomberg call in this act.</status>
