# MDPF_HEALGAP -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_HEALGAP-W<n>-S<k>`; seat rows `MDPF_HEALGAP-S<k>`.

```json
[
  {
    "id": "MDPF_HEALGAP-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "FWD-3 asks for the eleven missing model_detail days 2026-08-31..09-10 to be repaired by one act, but the runner sends Black Diamond no as-of date: a --date repair would land TODAY's model composition under those eleven dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py @c21432885a: ingest() (lines 400-458) uses `date` only to build landing keys; the vendor calls are POST /api/models/strategies/search and POST /api/accounts/search with body {skip,take,sort,searchString} (line 231) and GET /api/models/{id} (line 313), none carrying a date",
        "the brief's own control (PART VI.3): the 2026-09-01T02:50Z one-shot re-run for 2026-08-31 landed models and accounts, i.e. current-state pages written under a past date"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-3: the eleven missing days of 2026-08-31 to 2026-09-10 repaired by one act; afterwards exactly those are present. ACT 2: the word is asked for only when the hop-0 read predicts that the repair will fill the days.",
    "world_is": "The Rebalancer endpoints the runner uses return current state only (no as-of parameter is sent, and none is known to exist). A repair can fill the eleven keys, but with 2026-10-xx compositions, not the compositions in force on those days. Whether any endpoint serves historical composition is unread. The disclosure ACT 2 owes Andrew changes from 'may return empty' to 'would fill the days with the wrong-dated composition unless a historical source exists'. Not a round-1 act (FWD-3 is enrichment 2); no vendor call made."
  },
  {
    "id": "MDPF_HEALGAP-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "Hop 0's cause read is answered in the repo, not unread: the count-reconcile self-gate raised between accounts and model_detail on 2026-08-31..09-10, fixed by c53e48f7fb and deployed 2026-09-11T03:26Z; the runner's log group keeps only 14 days, so the original failure lines are gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda_function.py _reconcile_counts docstring (lines 337-363) at HEAD; git log c53e48f7fb 2026-09-10 22:17 -0400 'a count mismatch is DISCLOSED, not fatal -- one closed account froze the Cottonwood model chain for 11 days'",
        "aws lambda get-function cot-rebalancer-runner 2026-10-07: LastModified 2026-09-11T03:26:00Z",
        "aws s3api list-objects-v2 opal-data-assets blackdiamond/cottonwood/meta/2026-09-0 -> no complete-stamp; meta/2026-10-01..07-complete.json present, each ~06:01Z",
        "aws logs describe-log-groups /aws/lambda/cot-rebalancer-runner: retentionInDays 14; filter-log-events 2026-09-05T05:50Z+1h returns nothing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD section 2 hop 0 and brief PART VII.1: why rebalancer_model_detail stopped 2026-09-01..09-10 while its siblings landed is UNREAD and must be read before building.",
    "world_is": "It is a second cause class (a vendor-maintained counter treated as a fail-closed gate), already closed in code and deployed. Its primary evidence (the runner's log) has aged out at 14 days, which also bounds FWD-2: 'read from the run's own result' cannot mean the CloudWatch log for anything older than two weeks."
  },
  {
    "id": "MDPF_HEALGAP-W2-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~2",
    "surfaced_at": "2026-10-07T08:54:00Z",
    "one_line": "HG-t-2 cannot commit: the naming gate (ENFORCE) refuses the literal cot-bronze-complete in the new .tf file as a NEW hand-kept carrier of 'cot', and the only admitting routes (an r20_exception or tf_local entry in org/standards/NAMING_LEGACY_READS.json) are outside this order's write grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... -- infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf (worktree wk-healgap-1-2, base 474ec88e5a): rc=1, 'NAMING REFUSE cot_rebalancer_reattempt.tf:23 cot-bronze-complete -> lookup(cottonwood)' and ':34 arn:aws:events:{x}:{x}:rule/cot-bronze-complete -> lookup(cottonwood)'; commit aborted, files unstaged",
        "infra/logic/registry/resources.json:2309 registers cot-bronze-complete as an EVENT_RULE under system blackdiamond (legacy-shaped name), so modules/opal_name name() cannot produce it and the gate's opal_name-module-arguments context does not apply",
        "hg_t2_tf_check.py requires the literal rule = \"cot-bronze-complete\" and a source_arn matching rule/cot-bronze-complete, so the literal cannot be moved out of the file without failing AC1",
        "AC1 TF-OK and AC2 SEAM-OK both pass on the uncommitted file; the proof-of-spec instance validated rc=0 before the commit attempt"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's grant (the .tf file, the investigation file, the deliverables folder, the order file) is enough to land HG-t-2, and the file copies the runner file's style.",
    "world_is": "A NEW .tf literal carrying the token cot is refused at commit unless NAMING_LEGACY_READS.json carries an r20_exception entry (needs a conformance-ledger register row) or a tf_local entry for it; both are outside the write grant and not the worker's to add. The file, proof instance and deliverables sit uncommitted in worktree C:/tmp/wk-healgap-2; the order stays pending. No gate was bypassed, no check weakened. Issuer decision needed: obtain the waiver entry, or reshape the order."
  }
]
```
