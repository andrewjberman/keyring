# AMGT_RESAPP round 5 L10 remediation slug

From 3.0.0_SA_CVO~Z to 1.0.0_SA_CTO~Z only. This is the previously withheld round-5 slug, issued alongside the separately numbered round-6 slug in one handoff. Its vintage is its commit. The prior L9 is ADJUDICATION_v5.md@655c1a810e; its historical block statement is preserved. rd8 is now superseded, re-1 complete, and the actual project census is zero open of 37 after b2cd6e9ee7.

Round 5: five historical AC4 PASS, rd8 AC4 FAIL and rd8 AC2 FAIL. There were 25 newly dispositioned originals (18 graduated, seven dismissed), plus two CVO findings. The 20 formal rows below cover those 18 originals and C-S49/C-S50 exactly once. Four instance remedies are already executed and closed (S11, S19, W2-S8, W2-S9); 16 remain OPEN. Object preservation is distinct from frozen portal integration; corrected compiler verification is distinct from AC3's newly found destructive restoration.

Earlier numbered slugs retain their original rows and clocks; their IDs are not duplicated here. No previous open row is silently closed by this document. The continuing scheduler/IAM issue C-S49 is an in-place CRO obligation; compiler/gate/seat tooling obligations remain with their existing disarm owners. They do not authorize AMGT workers to modify another project's surfaces. CTO reads these findings under the spine's in-place-or-owning-project rule before the COO recuts.

The physical contract is route-free, as the current gate and spine require. Some schema descriptions retain retired routing vocabulary; this slug does not use it. The round-6 recut preceded this slug and the round-5 CTO analysis contrary to Rule 27, acknowledged in S26. Letting that cell drain has restored the order precondition; it is not a precedent or an override. The round-6 slug supplies its independently graded result and the remaining surface obligations. A drained queue is not a passed outcome. PROD/DEV remain frozen and FWD-15 is not declared REALIZED.


```json
[
  {
    "id": "AMGT_RESAPP-Z-S6",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The actual evaluate() function still falls back to prd_version when half_hash is absent. The offline same-version/changed-bytes control returns SIGNED. Both current lane records are SIGNED; deleting them at current v0.5 returns STALE, so the defect is the general same-version fallback, not a current missing-lane false green. Holder: CTO, the existing sign-off gate owner; require byte-bound records and a red changed-bytes control.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S6",
      "THE DECIDING LINE, read at source rather than inferred -- .tools/prd_signoff_lib.py, function `evaluate`: `current = (str(doc.get(\"half_hash\") or \"\") == hashes[half]) if doc.get(\"half_hash\") else (str(doc.get(\"prd_version\")) == version)`. The else-branch is a LEGACY fallback to prd_version. The function's own docstring states it: 'CURRENT = half_hash equals the PRD's (or, legacy, prd_version equals).'",
      "THE LIVE INSTANCE: org/missions/D5/AMGT/AMGT_RESAPP/prd/signoff/4.0.0_SA_CRO.json reads {prd_pin: bbbf35c38e5e, prd_version: v0.4, signed_by: 4.0.0_SA_CRO~Z, verdict: SIGNED} -- NO `half` key and NO `half_hash` key. The PRD is still v0.4, so the legacy branch evaluates current=True.",
      "MEASURED FALSE GREEN: this seat's own commit 3e35a50e74 changed brief-half sections (s.5 and the s.4 S6 manifest row) and moved the brief half hash from a5517057d99f to 1cb017c3e490 (computed with the library's own half_hashes, so the same instrument the gate uses). `python .tools/prd-signoff.py status AMGT_RESAPP` AFTER that commit still prints `brief SIGNED 4.0.0_SA_CRO~Z current`.",
      "DISCRIMINATION -- the contrast row proves the mechanism rather than the symptom: the CVO's record 3.0.0_SA_CVO~Z.json is NEW-format and DOES carry half_hash 8d2ae62e98..., and the very same status call correctly reports its half STALE against the changed bytes. Same tool, same run, same PRD: the half with a half_hash is graded on content and the half without one is graded on a version string.",
      "NOT A CACHING OR ORDERING ARTIFACT: `evaluate` picks the newest candidate by `signed_at`, and the CRO record has no `signed_at` at all (sorts as ''), so it is the only candidate for its half and is the decider. There is no newer CRO record it could be shadowing.",
      "SCOPE OF THE CLASS, stated rather than assumed: the legacy branch fires for ANY sign-off record lacking half_hash, in ANY project, not just this one. The same directory also holds 3.0.0_SA_CVO.json, an old-format v0.3 record with no half_hash. This row does NOT claim a census of affected records across the estate -- that census was not run and is part of the disposition, not of this surfacing.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The actual evaluate() function still falls back to prd_version when half_hash is absent. The offline same-version/changed-bytes control returns SIGNED. Both current lane records are SIGNED; deleting them at current v0.5 returns STALE, so the defect is the general same-version fallback, not a current missing-lane false green. Holder: CTO, the existing sign-off gate owner; require byte-bound records and a red changed-bytes control.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S9",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "rd1 and rd2 shared one root module but declared singleton backend/provider blocks independently; their individual VALID instances did not validate their union. Current committed amgt-resapp has two root .tf files and no table declarations; harvest has both renamed tables. Packet claims of unconsolidated state and a source header claiming consolidation are not a CVO state measurement. Holder: COO for the existing shared-module cut; CRO owns estate state. Require a union validation and state ownership evidence, preserving the new scheduler residual in C-S49.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S9",
      "MERGED-TREE TEST, run by copying both worktrees' .tf files into one scratch directory and running `terraform init -backend=false` then `terraform validate -no-color`: ERROR 'A module may have only one backend configuration block. The backend was previously configured at main.tf:30,3-15.' AND 'Error: Duplicate provider configuration -- on security-metrics-table.tf line 63: a default (non-aliased) provider configuration for \"aws\" was already given at main.tf:37,1-15.'",
      "POSITIVE CONTROL, which is what makes the failure attributable to the MERGE rather than to either half: slot ~1's files ALONE, in their own scratch directory, return 'Success! The configuration is valid.' So each half is individually valid and the defect exists only in their union.",
      "FILE LAYOUT at the time of the read: slot ~1 (`wk-amgt_resapp-5-1`) carries `main.tf` (terraform{} + provider \"aws\"{}) and `dynamodb.tf` (resource aws_dynamodb_table.amgt_articles). Slot ~2 (`wk-amgt_resapp-5-2`) carries a single `security-metrics-table.tf` holding terraform{}, provider \"aws\"{} AND resource aws_dynamodb_table.security_metrics.",
      "BOTH WORKERS ARE BEHAVING CORRECTLY AND NEITHER IS AT FAULT: each committed its change-management ledger OPEN before the apply (rd-1 @db28a5d1be, rd-2 @f4cc9669ba), and slot ~2 honoured its order's bound to put its table in its OWN FILE rather than restructuring the sibling's. The order did not say 'and declare no terraform/provider block', which is the gap.",
      "NEITHER AC CAN SEE IT: AC1 on both orders is `cd infra/aws/terraform/amgt-resapp && terraform validate`, which runs inside the WORKER'S OWN WORKTREE. The module directory is what the two cells SHARE, and a criterion scoped to one member is structurally blind to a defect in the shared dependency.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "rd1 and rd2 shared one root module but declared singleton backend/provider blocks independently; their individual VALID instances did not validate their union. Current committed amgt-resapp has two root .tf files and no table declarations; harvest has both renamed tables. Packet claims of unconsolidated state and a source header claiming consolidation are not a CVO state measurement. Holder: COO for the existing shared-module cut; CRO owns estate state. Require a union validation and state ownership evidence, preserving the new scheduler residual in C-S49.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S7",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The worker met HALT-GT by writing its own gitignored session identity outside the listed paths. That measured prerequisite is a grant defect, not evidence that all session writes are implicitly authorized. Holder: COO; carry the identity prerequisite and its permitted writer in the existing apply cell before issuance.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W1-S7",
      "`.tools/safe-apply.sh apply ...` on infra/aws/terraform/amgt-resapp first returned: 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed) ... FIX (one line -- use YOUR serial, incl. any ~lane suffix): printf %s\\\\n \"1.2.3_XX_Yourserial\" > \"org/mcp/sessions/8af2b430-48a4-4293-b4c3-5017f0263c1c.serial\"' -- rc != 0, terraform never invoked.",
      "`git check-ignore -v org/mcp/sessions/test.serial` -> `.gitignore:423:org/mcp/sessions/ org/mcp/sessions/test.serial` -- the required path is estate-wide gitignored (ephemeral, never committed, never collides with a peer worker's own session-keyed file).",
      "After writing `org/mcp/sessions/8af2b430-48a4-4293-b4c3-5017f0263c1c.serial` containing this worker's own serial, the identical safe-apply invocation proceeded past the HALTGT and tag-authz gates and completed: 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The worker met HALT-GT by writing its own gitignored session identity outside the listed paths. That measured prerequisite is a grant defect, not evidence that all session writes are implicitly authorized. Holder: COO; carry the identity prerequisite and its permitted writer in the existing apply cell before issuance.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S10",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The row's code-reconciled headline is qualified by its record: the COO edit was refused and reverted, then rd3 was routed and later superseded. The current moved declarations do not vindicate the reverted edit. Holder: COO for a complete reconciliation grant on the existing module; CRO for state. Consolidate its remedy with S9, without counting that temporary validation as closure.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S10",
      "THE PREDICTION HELD. Immediately after the rd-1 drain merged at dd9bb9c1e8, `terraform validate` in infra/aws/terraform/amgt-resapp/ returned the two errors S9 named, verbatim: 'A module may have only one backend configuration block. The backend was previously configured at main.tf:30,3-15.' and 'Error: Duplicate provider configuration -- on security-metrics-table.tf line 63'. S9 was filed BEFORE either order was terminal.",
      "PER-FILE COUNT at the moment of collision: main.tf 1 terraform{} + 1 provider{}; security-metrics-table.tf 1 terraform{} + 1 provider{}; dynamodb.tf 0 + 0. After the reconcile: main.tf 1 + 1, security-metrics-table.tf 0 + 0, dynamodb.tf 0 + 0.",
      "DISARM VERIFIED ON THE SAME INSTRUMENT THAT FAILED: `terraform init -backend=false` then `terraform validate -no-color` in the merged module now returns 'Success! The configuration is valid.' The resource aws_dynamodb_table.security_metrics is preserved and was confirmed present after the edit.",
      "THE WORKER HAD ALREADY DOCUMENTED IT IN ITS OWN FILE. security-metrics-table.tf's header comments state that a single directory can hold only ONE backend block, that its distinct key was chosen to avoid a concurrent-apply state race across the parallel worktrees, and that consolidating the two cells' state was left to the issuing COO. That reasoning was CORRECT for the parallel window and is recorded rather than overwritten -- the removal note in the file names it.",
      "BOTH ROWS SURVIVED THE DRAIN. The append-only channel conflicted on the rd-1 merge (the normal path for a concurrent drain, not the exception). Resolved by keeping BOTH this seat's Z-S9 and the worker's Z-W1-S7: 36 rows, JSON parses, 0 duplicate ids, 0 conflict markers.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The row's code-reconciled headline is qualified by its record: the COO edit was refused and reverted, then rd3 was routed and later superseded. The current moved declarations do not vindicate the reverted edit. Holder: COO for a complete reconciliation grant on the existing module; CRO for state. Consolidate its remedy with S9, without counting that temporary validation as closure.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S11",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The identified collision was between CRO harvest ownership and the round-5 rd3/rd4 work. Both orders are now superseded; the stopped rd3 attempt had no commit or apply. The owner acted inside this round. Holder: COO; carry REMEDIATED/DISARMED at L10, with no new worker order and no invented proof instance for unexecuted orders.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S11",
      "THE DIRECTIVES, verbatim, relayed by 4.0.0_SA_CRO~Z (msg 21507) and recorded @bb1800ec4d: (1) 'dont mind the preexisting stuff, this should be one box and one lambda titled as \"harvesters\" using harvest language. buckets would be opal-data-harvest, and so on'; (2) 'just want to make sure everything is canonical and self-contained in this harvest estate'; (3) 'that is something I need you to oversee and execute, you have full egress and override authority to realize it. just /draw me your intended architecture and i can approve/revise.'; (4) 'also I see COO~ZZZ workers looking into terraforming things, all of that is going to need to go into the harvester tf here'; (5) 'the harvester tf is basically the primary feeder resources for the Security Analysis application.'",
      "THE COLLISION IS EXACT, NOT THEMATIC. AMGT-rd-3's own cell text reads 'THE HARVESTER BOX + ITS OWN IAM ROLE ... a NEW EC2 box ... ONE shared box for all four harvesters', and AMGT-rd-4 is 'THE FOUR HARVESTERS'. Directive 1 says ONE box and ONE lambda. Two builders on one write surface is the collision ONE ISSUER PER ROUND exists to prevent, and directive 1 also changes the SHAPE (four harvesters on a box vs one lambda), which is a different unit of deployment and a different IAM grant shape.",
      "STOPPED, AND NOTHING LANDED -- measured on the LIVE PLANE after the stop, not from the worker's transcript: branch wk-amgt_resapp-5-3 = 0 commits; `describe-instances --filters Name=tag:Project,Values=AMGT_RESAPP` = EMPTY (no box); `list-roles` filtered on 'amgt' = EMPTY (no role); org/critical_paths/.open_deploys/ carries no amgt sentinel. The worker's final line shows it was still reading sibling subnet/VPC shapes and had not reached an apply. One uncommitted file remained in its worktree: the S9/S10 module reconcile it was carrying as clause (0).",
      "ANDREW SET HIS OWN GATE AND IT IS NOT YET CLEARED: 'just /draw me your intended architecture and i can approve/revise.' So nothing on this surface is built, applied, renamed or egressed before he approves the draw. rd-3 running would have breached that gate on his own instruction.",
      "1.0.0_SA_CTO~Z's ruling (msg 21511) states the MECHANISM: mid-round the spec and decomposition are FROZEN (Rule 27), so the reshape is a PRD ADDENDUM (L4, the CTO) followed by a RECUT (L6, this seat) -- never a mid-round edit to a cut cell. That seat is deliberately NOT writing the addendum yet, because the addendum follows the APPROVED draw rather than the directive.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The issuer superseded competing rd3/rd4 without an invented proof or apply. The 37-order terminal census corroborates that recovery. No further worker order is needed for this duplicate-builder collision.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S6",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The scheduled producer selected the ~4 worker universe and packaged a frozen copy. Independent controls find 89 rows in each of ~3/~4, with 32/34 measured distinct identities and no AAPL US placeholder; those checks do not establish a canonical publisher or the deployed ZIP vintage. Holder: COO for existing identity and rd5 cells. Name the source, update contract and package provenance; an existing cell needing a better grant is not automatically an absent cell or DECOMP_INVALIDATING.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S6",
      "Task order AMGT_RESAPP.TO-AMGT-rd-5's cell text and bounds say 'per ticker' and 'per-ticker rows' throughout but never name the ticker universe or its source; AMGT-rd-5's only declared dependency is AMGT-rd-2 (the metrics store), not AMGT-s-12/AMGT-r-12 (the identity layer).",
      "Only a landed, worker-numbered path exists at this worktree's HEAD: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json` (89 folders, 34 MEASURED bloomberg_ticker) -- measured via `Glob` for `deliverables/*/universe.json`, two hits (~3 and ~4, the later one used). No canonical/stable-named path (e.g. a fixed key under a single owned directory, or a DynamoDB-backed universe table) exists for this artifact at this cut.",
      "lib/research/metrics/chatter_axis.py's DEFAULT_UNIVERSE_PATH hard-codes that worker-numbered path and lambda_src/build_zip.py bakes a FROZEN copy of that exact file into the deployed Lambda's zip (documented in both files' docstrings and in AMGT-rd-5.window-record.md).",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The scheduled producer selected the ~4 worker universe and packaged a frozen copy. Independent controls find 89 rows in each of ~3/~4, with 32/34 measured distinct identities and no AAPL US placeholder; those checks do not establish a canonical publisher or the deployed ZIP vintage. Holder: COO for existing identity and rd5 cells. Name the source, update contract and package provenance; an existing cell needing a better grant is not automatically an absent cell or DECOMP_INVALIDATING.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S7",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Adding archive to a second required_providers block was refused by Terraform; the worker used a static build_zip.py artifact instead. That alternative can work and no rule here mandates archive_file. Holder: COO for the existing rd5 packaging cell: give it a deterministic rebuild/hash contract and any required shared-file grant. The manual artifact must not be mistaken for a continuously rebuilt current deployment.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S7",
      "MEASURED directly against this module directory: adding `terraform { required_providers { archive = { source = \"hashicorp/archive\" ... } } }` in a NEW file (chatter-axis-schedule.tf) and running `terraform init -input=false` refused: 'Error: Duplicate required providers configuration ... A module may have only one required providers configuration. The required providers were previously configured at chatter-axis-schedule.tf:33,3-21.' -- the pre-existing block is security-metrics-table.tf:49 (AMGT-rd-2's own file), which this cell's task order and the coordinator's amendment (898fef5268) both name as off-limits (surprise rows AMGT_RESAPP-Z-S9/-S10).",
      "Removing the required_providers block and instead building the deployment zip OUTSIDE Terraform (infra/aws/terraform/amgt-resapp/lambda_src/build_zip.py, stdlib zipfile) plus referencing it via Terraform's built-in filebase64sha256() (no provider needed) made `terraform init` / `validate` / `plan` all pass cleanly against the same directory: plan showed '6 to add, 0 to change, 0 to destroy' -- zero diff against AMGT-rd-2's already-applied aws_dynamodb_table.security_metrics, confirming this file's presence does not perturb rd-2's own state.",
      "Precedent in this repo (infra/aws/terraform/estate-report/orchestrator.tf, infra/aws/terraform/globgrph/cse_producer.tf) uses `data \"archive_file\"` for exactly this shape (a thin Lambda handler zipped from repo source) -- this cell could not follow that precedent without editing the file it is barred from touching.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Adding archive to a second required_providers block was refused by Terraform; the worker used a static build_zip.py artifact instead. That alternative can work and no rule here mandates archive_file. Holder: COO for the existing rd5 packaging cell: give it a deterministic rebuild/hash contract and any required shared-file grant. The manual artifact must not be mistaken for a continuously rebuilt current deployment.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S12",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Use S13's corrected census: ten hard-coded bucket literals, five in live consumers and five in worker checks, plus one derived and one environment-based reference. Live source defaults were changed; pinned historical proofs stay historical. An env knob does not repair a check that never reads it. Holder: CRO for a current executable consumer/check map; preserve historical evidence without rewriting its bytes. C-S49 separately identifies live scheduler dependencies missed by a defaults-only review.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S12",
      "CENSUS with its denominator printed: `comp-find 'opal-data-research'` -> 314 hit(s) across 56,351 file(s) scanned [corpus=all]. BANDS: HEAD=35 DEF=12 SURFACED=57 CONFIG=43 TEST=1 DOC=166.",
      "THE DEF BAND IS THE ONE THAT DECIDES THE ACT -- 12 definition lines binding the bucket name to a variable. ENV-OVERRIDABLE (1): infra/aws/lambda/research/pull_enqueue/lambda_function.py:32 `BUCKET = os.environ.get(\"RESEARCH_BUCKET\", \"opal-data-research\")`. HARDCODED LITERALS (10): integrations/bloomberg/research/derive_fye_fixed.py:33, model_block_pull.py:43, pull_baba_daily_px.py:29; lib/research/freshness/build_view.py:54; lib/research/ledger/ledger.py:37; and five worker check scripts under deliverables/0.9.0_WK_AMGT_RESAPP~1/ and ~2/. INDIRECT (1): integrations/bloomberg/research/pull_consumer.py:45 `BUCKET = mbp.BUCKET`.",
      "SIX OF THE HARDCODED ONES ARE LIVE LIBRARY/INTEGRATION CODE landed by rounds 1-4, not scratch: the model-block pull, the fiscal-year derive, the daily price pull, the pull consumer, the freshness view and the input ledger.",
      "TWO ROUND-5 PRODUCERS ARE SCHEDULED OR BOX-SIDE AND READ RESEARCH-STORE PATHS: rd-5's chatter producer runs daily at `cron(0 10 * * ? *)` UTC (landed and applied this round) and rd-6's price engine is a box-side pull. A rename landing between two scheduled fires breaks the next one at RUN time, not at apply time.",
      "THE RULING AND THE TWO CORRECTIONS ALREADY ON THE RECORD: Andrew ruled the rename ~18:5xZ, verbatim 'call 2 no it should actuall be a rename there is no data in there anyway, better to have all of this stuff grouped by name right from the start.' 1.0.0_SA_CTO~Z measured his premise FALSE at 2026-09-11T18:55:29Z (53 objects / 60 versions) and separately WITHDREW its own overstatement that the rename would destroy FWD-6's accumulate evidence -- the accumulate bar reads the timestamped KEY grammar, which a copy preserves; what a copy loses is the ~7 overwrite VERSIONS. This row adds a third dimension neither names.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Use S13's corrected census: ten hard-coded bucket literals, five in live consumers and five in worker checks, plus one derived and one environment-based reference. Live source defaults were changed; pinned historical proofs stay historical. An env knob does not repair a check that never reads it. Holder: CRO for a current executable consumer/check map; preserve historical evidence without rewriting its bytes. C-S49 separately identifies live scheduler dependencies missed by a defaults-only review.",
    "owner": "4.0.0_SA_CRO~Z",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO~Z",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "4.0.0_SA_CRO~Z",
      "at": "2026-09-13T00:01:49Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S6",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issued tail -12 could discard the comp-find denominator; the worker's supplemental untruncated output supplied it (12 hits across 67 scanned files). Holder: COO for the existing rd7 instrument: retain the full bounded result or a machine-readable denominator. Do not turn a truncated display into a zero-results claim.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W7-S6",
      "AMGT_RESAPP.TO-AMGT-rd-7.starred-watchlist-per-firm-pure-marker.md AC3 <invocation>: \"timeout 110 comp-find \\\"harvest|refresh|enqueue|trigger\\\" lib/research --limit 20 2>&1 | tail -12\"; <expect>: \"a printed denominator, and NO hit inside the starring code path ... A denominator of 0 files scanned is OUT-OF-CORPUS and is NOT met either\"",
      "This invocation run verbatim in this worker's worktree, piped through `cat -n`: 18 total lines (6 fixed header/label lines incl. the 'DENOMINATOR: ...' line at line 2, then 12 hit lines); `tail -12` keeps lines 7-18 only, so the DENOMINATOR line (line 2) is NOT in the recorded output whenever fixed-header(6) + hits(N) > 12, i.e. N > 6 hits -- true here at N=12",
      "Re-run of the identical comp-find command without the trailing '| tail -12' on the same worktree state: 'DENOMINATOR: 12 hit(s) across 67 file(s) scanned in scope [corpus=all] | 49 EPHEMERAL-FLOOR, NOT searched' -- the denominator IS printed by the tool, it is the specified pipe that discards it from the graded excerpt",
      "None of the 12 hits are inside lib/research/watchlist/ (this cell's own module, commit 61770a9396a9a876133b515ae774113ce92fdeb0) -- all 12 are pre-existing lines in lib/research/freshness/build_view.py and lib/research/social/__init__.py / measure.py, unrelated to the starring code path -- so the criterion's SUBSTANTIVE bar (no hit reachable from the star handler) is met either way; only the literal denominator-visibility clause of <expect> is affected by the tail truncation",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The issued tail -12 could discard the comp-find denominator; the worker's supplemental untruncated output supplied it (12 hits across 67 scanned files). Holder: COO for the existing rd7 instrument: retain the full bounded result or a machine-readable denominator. Do not turn a truncated display into a zero-results claim.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S7",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The worker disclosed an initial mutant opening example.com:80, reverted it, and did not claim the event never happened. Current five-test source applies the socket blocker to only three tests; the first two lack it. Production watchlist code has no outbound call, but the harness still leaves a mutation path unguarded. Holder: COO for existing rd7 test coverage; apply the blocker across all tests. CVO independently denied socket connections across all 37 offline tests, which passed.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W7-S7",
      "CLAUDE.md Agent Autonomy: 'Do NOT ask permission to read/write/build/test/commit/push CLOUD-DEV/run scripts/call Opal-owned APIs. Excluded: all egress off Opal infrastructure.' -- egress off Opal infrastructure is carved OUT of the no-permission-needed set.",
      "The mutant was applied to lib/research/watchlist/store.py's star() (a line calling socket.create_connection((\\\"example.com\\\", 80), timeout=1) after the real put_item), then `python -m pytest lib/research/watchlist -q` was run. Result: '3 failed, 2 passed' -- the 2 PASSING tests were test_starred_watchlist_is_shared_across_firm_pms and test_starred_watchlist_tenancy_boundary_across_firms, neither of which requests the block_all_sockets fixture, so the injected connection attempt in those two test runs was NOT intercepted and (since no exception surfaced to fail them) either succeeded or failed silently within the 1s timeout against the real network -- either way a real attempt left this worktree.",
      "example.com is an IANA-reserved domain, RFC 2606, expressly designated for documentation/example use, resolves publicly, and no data beyond a bare TCP handshake was sent (no HTTP request line, no payload, no credentials, no Opal data) -- the practical exposure is a connection log entry on a public test domain, not a data disclosure.",
      "Immediately reverted (git diff --stat lib/research/watchlist/store.py: no output, byte-identical to committed HEAD) and replaced with a network-free mutant (a second table.put_item call on the already-faked persistence seam) before any formal AC1-AC3 evidence for this cell's proof-of-spec instance was captured -- see AMGT_RESAPP.TO-AMGT-rd-7...proof_of_spec.json controls.mutant for the graded (safe) version.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The worker disclosed an initial mutant opening example.com:80, reverted it, and did not claim the event never happened. Current five-test source applies the socket blocker to only three tests; the first two lack it. Production watchlist code has no outbound call, but the harness still leaves a mutation path unguarded. Holder: COO for existing rd7 test coverage; apply the blocker across all tests. CVO independently denied socket connections across all 37 offline tests, which passed.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S14",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The known generated VINTAGEID fixture was repeatedly mistaken for a live peer artifact. Its existing exclusion is not a general output discriminator. Holder: CTO for compiler/artifact classification: distinguish generated fixtures from accountable deliverables using provenance and intended role. This is one measured fixture, not a claim that all generated output is disposable.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S14",
      "MEASURED THIS TICK: `git status --porcelain -- org/missions/D5/AMGT/AMGT_RESAPP/` returns exactly ONE line, denominator 1 -- the untracked `deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_fye_VINTAGEID_US_Equity.json`, 472 bytes, mtime 2026-09-11T15:28:11Z read via os.stat against a clock read in the same call (19:19:20Z), i.e. ~3h51m old and NOT inside any live peer's current working window.",
      "THE PRODUCER IS NAMED BY THE CENSUS, not inferred: `comp-find 'VINTAGEID'` -> 13 hit(s) across 56,698 file(s) scanned [corpus=all], BANDS HEAD=3 SURFACED=4 TEST=3 DOC=3. The TEST band is `integrations/bloomberg/research/tests/test_vintage_derivation_identity.py:37,51,79` (`SEC_KEY = \"VINTAGEID_US_Equity\"`). A test writes it; no seat authored it.",
      "THE COMMITTED SLUG DISCLOSES IT IN TERMS -- `surprise-channel/remediations/REMEDIATION_v4.md:13`, VERBATIM: 'Existing pytest creates an untracked VINTAGEID fixture in the worker deliverables directory; that file is excluded from this commit.' So the exclusion is a DECISION ON THE RECORD, not an omission.",
      "TWO SEATS REACHED THE SAME ACT FROM DIFFERENT MODELS, AND ONE MODEL IS WRONG. `4.0.0_SA_CRO~Z` at 15:50Z (msg to `1.0.0_SA_CTO~Z`): 'NOT dead-seat residue and should not be classed UNFINISHED-EDITS -- the slug discloses it in its own text as a pytest-created fixture deliberately excluded from the commit.' CORRECT, and read off the slug. THIS SEAT, `drive_log_20260911T1700Z.md:66-70`: 'mtime inside `3.0.0_SA_CVO~Z`'s live window. A live peer's in-flight work, NOT dead-seat residue.' WRONG ON THE REASON. Both concluded 'leave untouched', so nothing was harmed and NOTHING ANNOUNCED THE ERROR.",
      "WHAT MAKES IT READ LIKE AN OMISSION, measured rather than asserted: `git ls-files` on that directory returns 37 tracked files, and the untracked one has a TRACKED SIBLING FAMILY -- `model_block_fye_BABA_US_Equity.json`, `_BA_`, `_SAP_GY_`, `_BABACVOCTRL_`. It is the only UNTRACKED member of a committed set, which is exactly the shape of a forgotten file.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The known generated VINTAGEID fixture was repeatedly mistaken for a live peer artifact. Its existing exclusion is not a general output discriminator. Holder: CTO for compiler/artifact classification: distinguish generated fixtures from accountable deliverables using provenance and intended role. This is one measured fixture, not a claim that all generated output is disposable.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S16",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The worker inherited 5b959f63 on top of DEV 30ca and the intervening IRPT commits. This demonstrates ancestry coupling, not that the AMGT code semantically depends on every intervening commit. Holder: CTO for preserved branch/base selection and later authorized integration. PROD and DEV remain frozen; CVO did not rebase, promote or move the recorded gitlink.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S16",
      "THE THREE POINTERS DISAGREE, each read directly: superproject `git ls-tree HEAD portal` -> gitlink `e85f6eb84f`; the MAIN tree's portal checkout -> `30ca034b` on branch `DEV`; the `rd-8` worktree's portal -> `5b959f63` on branch `wk-amgt_resapp-5-8-portal`. The main tree's persistent ` M portal` in `git status` is this disagreement, not an edit.",
      "THE DIRECTION AND SIZE, measured both ways rather than assumed: `merge-base --is-ancestor 30ca034b 5b959f63` -> TRUE, `rev-list --count 30ca034b..5b959f63` -> 19, `rev-list --count 5b959f63..30ca034b` -> 0. So the worker's base is DEV plus 19, strictly ahead, no divergence. `git -C portal branch -v` shows `DEV` itself marked `[behind 19]`.",
      "THE CHAIN BELONGS TO NO BRANCH: `git -C portal branch --contains 5b959f63` returns EMPTY, and the only local branches are `DEV` (30ca034b) and `PROD` (6cb3d0f6). A chain no branch contains is reachable only through the superproject's gitlink and the worker's own branch.",
      "WHOSE WORK IT IS, from the commits themselves: 17 of the 19 are `IRPT_FNTEND` L7 work and drains by `2.0.0_SA_COO~F` and `0.9.0_WK_IRPT_FNTEND~1/~2/~3/~4` (FE-s-1 through FE-s-8); the remaining 2 are `0.4.0_DT_ClientPlatform` DEV work. The recorded gitlink `e85f6eb84f` is itself one of the IRPT commits (`0.9.0_WK_IRPT_FNTEND~1`, FE-s-5 Reporting tab).",
      "WHAT THE CHAIN ACTUALLY CARRIES, so the coupling is not overstated: `diff --name-only 30ca034b..5b959f63` is dominated by `src/pages/InvestorReporting/**` -- IRPT's own page tree, which a Lead Panel need not touch -- but it ALSO reaches `src/lib`, `src/api/endpoints` and a root tsconfig alias mapping named in the FE-s-5 drain's own subject. `src/pages/InvestorReporting/tabs/TabShell.tsx` exists at the worker's base and is ABSENT on `DEV`.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The worker inherited 5b959f63 on top of DEV 30ca and the intervening IRPT commits. This demonstrates ancestry coupling, not that the AMGT code semantically depends on every intervening commit. Holder: CTO for preserved branch/base selection and later authorized integration. PROD and DEV remain frozen; CVO did not rebase, promote or move the recorded gitlink.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T00:01:49Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S19",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "There were no object alternates and no committed superproject gitlink to the worker head. The initial dangling-gitlink forecast had the wrong trigger; loss of the sole object store was the actual preservation risk. S21 records the successful fetch. Holder: CTO; preserve reachable objects before deleting their only checkout and resolve the separate integration hold. Do not claim a gitlink was advanced.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S19",
      "THE TWO OBJECT STORES, read as absolute paths rather than inferred from the layout: main tree `git -C portal rev-parse --path-format=absolute --git-path objects` -> `.../ajb_workspace/portal/.git/objects`; worker `git -C C:/tmp/wk-amgt-5-8/portal ...` -> `C:/tmp/wk-amgt-5-8/portal/.git/objects`. Two directories, not one.",
      "AND NO SHARED-OBJECT LINK BETWEEN THEM: `C:/tmp/wk-amgt-5-8/portal/.git/objects/info/alternates` DOES NOT EXIST. An alternates file is the only thing that would let the main repo read the worker's objects; its absence is the finding.",
      "THE WORKER'S PORTAL IS A CLONE OF THE REMOTE, not of the local tree: `git -C C:/tmp/wk-amgt-5-8/portal remote -v` -> `origin https://github.com/Opal-Capital/portal.git`. So its unpushed commits exist in exactly one place on this machine.",
      "WHY AN EARLIER READ LOOKED REASSURING AND WAS NOT: `git -C portal cat-file -t 5b959f63` returns `commit`, so the worker's BASE commit IS present in the main portal repo. That proves shared HISTORY, not a shared STORE -- the base predates the clone. A check that stops there reads PRESENT for exactly the objects that were never at risk.",
      "THE WORK IS REAL AND IT IS IN THE SUBMODULE, so this is not a hypothetical: the worker's portal tree carries ` M src/App.tsx`, `?? src/api/endpoints/amgt-lead-panel.ts` and `?? src/pages/SecurityAnalysis/` uncommitted at this reading, on its own branch `wk-amgt_resapp-5-8-portal`.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Immediate only-copy risk disarmed: both e6057f26 and c6728146 are preserved in the main portal object store before teardown, with the latter positive and bogus-object controls in the round-6 evidence. Do not merge or advance the gitlink. Remaining base/integration hold is S16/S21, not a reason to count S19 preservation as still unperformed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-11T23:54:40Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S8",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The measured executable was registry tsc 2.0.4 rather than TypeScript; the worker's same-node_modules comparisons eliminated several explanations without establishing a cache-poisoning cause. Graduate only the executable-identity defect. Holder: COO for existing rd8 instrument: bind the installed TypeScript executable/version and project selection; no speculative root cause is accepted.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S8",
      "AC1 <invocation> verbatim: 'cd portal && timeout 110 npx tsc -b --pretty false 2>&1 | tail -5'; AC2: 'cd portal && timeout 110 npx tsc --noEmit --pretty false 2>&1 | tail -3'. Run exactly as written in this worktree (portal HEAD 5b959f63, branch wk-amgt_resapp-5-8-portal, cut from origin/DEV): both print the SAME fixed banner ('This is not the tsc command you are looking for ... Use npm install typescript to first add TypeScript ...'), rc=1, zero mention of any file in this cell.",
      "npx --loglevel silly tsc --version in this worktree logs 'npm http fetch GET 200 https://registry.npmjs.org/tsc 78ms (cache revalidated)' -- npx is resolving the bare string 'tsc' as a REGISTRY PACKAGE NAME (there is a real npm package literally called 'tsc', unrelated to the 'typescript' package that provides the SAME-NAMED binary), not as the local project's installed typescript@5.9.3 bin.",
      "A/B control: the IDENTICAL command ('cd portal && npx tsc --version') run in the sibling checkout 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal' (same package.json, same typescript@5.9.3, node_modules junctioned to be the LITERALLY SAME physical directory as this worktree's during one test pass) returns 'Version 5.9.3' with NO network fetch in its --loglevel silly log -- so the divergence is not node_modules content (proven byte-identical via the junction), not the root package-lock.json (removed, no change), not node_modules/.package-lock.json content (copied from the working checkout verbatim, no change), and not node_modules/.bin/tsc[.cmd/.ps1] shim presence (copied from the working checkout verbatim, no change) -- four targeted eliminations, root cause NOT isolated within this cell's time budget.",
      "Disambiguated substitute 'npx --package typescript tsc -b --pretty false' (identical flags, explicit package resolution) resolves correctly in this worktree: rc=0, zero output lines. A positive control (a deliberate type error appended to portal/src/pages/SecurityAnalysis/constants.ts, reverted immediately after) was caught by this substitute under '-b --force' (error TS2322 at the injected line) -- the substitute is a genuine, discriminating instrument for the SAME claim AC1 makes, unlike the literal invocation which never reaches TypeScript at all.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Existing compiler-selection defect corrected in issuance 4352fe1c47 using npx --package typescript; the forced-build proof 8d6c289dc8 reports 2069 source files and a detected TS2322. This closes this issued instrument instance, not a claim about every future npm resolution.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T23:54:40Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S9",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Pinned tsconfig.json has files: [] and references; plain --noEmit does not perform the referenced project build. The worker's injected TS2322 error was missed by that check and caught by the build control. AC2 is FAIL as issued: AC1 alone is not an independent staleness control. Holder: COO for the existing rd8 check; use a clean/forced referenced-project check with a deliberately failing source control. Preserve the failed issued criterion.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S9",
      "portal/tsconfig.json (root, the config a bare 'tsc' with no -p/-b resolves to): '{\"files\": [], \"references\": [{\"path\": \"./tsconfig.app.json\"}, {\"path\": \"./tsconfig.node.json\"}], \"compilerOptions\": {...}}' -- explicit empty 'files', no 'include', only project 'references'. TypeScript's plain (non-build-mode) driver does not follow 'references' the way '-b' does; it operates on the root config's own file set, which is empty.",
      "Positive control: appended 'const __deliberateTypeError: number = \"not a number\";' to portal/src/pages/SecurityAnalysis/constants.ts, then ran the disambiguated equivalent of AC2's exact flags ('npx --package typescript tsc --noEmit --pretty false', no '-b') from portal/: rc=0, 0 output lines -- the deliberate, obvious type error was NOT caught.",
      "Same worktree, same injected error, AC1's own flags WITH '-b' ('npx --package typescript tsc -b --pretty false --force'): rc=2, 'src/pages/SecurityAnalysis/constants.ts(39,7): error TS2322: Type 'string' is not assignable to type 'number'.' -- '-b' mode (AC1's own shape) DOES discriminate the identical error AC2's shape misses.",
      "Error immediately reverted (git diff --stat portal/src/pages/SecurityAnalysis/constants.ts: no output after revert, byte-identical to the pre-control state) before any AC1-AC3 evidence for this cell's proof-of-spec instance was captured.",
      "package.json's OWN 'typecheck' script is 'tsc -b --noEmit' (WITH -b) -- differs from AC2's literal invocation text ('tsc --noEmit', no -b) by exactly the one flag this positive control shows is load-bearing.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Existing vacuous root no-emit criterion was replaced in re-1 by forced referenced-project build plus source-file and error-mutant controls, evidenced at 8d6c289dc8. Preserve the historical rd8 FAIL. The new restore hazard is separately OPEN as W10-S1.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": "2026-09-11T23:54:40Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W2-S10",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Old table reads failed and the worker recorded the renamed table with 42 rows; code citations were current in main but absent at the worker pin. S21 corrects the overly general no-such-code statement. Holder: CTO with CRO migration owner: carry path plus commit plus current resource identifier at the handoff. A current path without its tree does not update a pinned worker.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W2-S10",
      "This worker's own EARLIER live read in this session (cited in AMGT-rd-2's read-pattern record, reproduced again at commit time): `aws dynamodb query --table-name opal-amgt-security-metrics --key-condition-expression 'axis_date = :ad' ...` returned a real CHATTER row; `aws dynamodb scan --table-name opal-amgt-security-metrics --select COUNT` returned Count=42 -- the table EXISTED and answered queries earlier in this same session.",
      "A message attributed to the coordinator (`2.0.0_SA_COO~ZZZ`) arrived mid-session stating the table was renamed and citing commit `d8248188b7`. RE-DERIVED independently rather than trusted: `git cat-file -t d8248188b7` -> `commit`; `git show --stat d8248188b7` -> a real commit, author `2.0.0_SA_COO~ZZZ`, dated 2026-09-11 16:31:22 -0400, `git branch --contains d8248188b7` -> `+SITEZ` (on the shared branch), diffing this exact cell's task order file's line 25 from `opal-amgt-security-metrics` to `opal-harvest-security-metrics` with a detailed, internally-consistent rationale (a COO-run scan of 42 deprecated-live references across task-orders/decompositions, 3 corrected).",
      "RE-VERIFIED LIVE, this worker's own commands, post-message: `aws dynamodb describe-table --table-name opal-amgt-security-metrics` -> `ResourceNotFoundException` (dropped); `aws dynamodb scan --table-name opal-harvest-security-metrics --select COUNT` -> Count=42 (the SAME 42 -- 32 PRICE + 10 CHATTER, `dynamodb scan --projection-expression axis` on the renamed table still shows exactly {CHATTER, PRICE}, no TRENDING#/BREAKOUT# row, same as the pre-rename measurement). Same pattern for the articles table: `opal-amgt-articles` -> ResourceNotFoundException; `opal-harvest-articles` -> Count=0 (consistent with both names, it was empty before too).",
      "THE PART THAT DOES NOT CHECK OUT: the message's own text claimed the env-knob pattern ('HARVEST_METRICS_TABLE ... that is the pattern the live modules now use') was ALREADY present at `lib/research/metrics/chatter_axis.py:67` and `lib/research/watchlist/store.py:43`. Read directly: `chatter_axis.py` (this session, lines 55-75) still declares `METRICS_TABLE = \"opal-amgt-security-metrics\"` as a bare literal, no `os.environ` read anywhere in the file (`grep HARVEST_METRICS_TABLE|opal-harvest|os.environ lib/research/watchlist/store.py` -> zero hits). The COO's own commit message independently confirms this gap, unprompted: 'everything under deliverables/<serial>/ ... 5 worker check scripts still hardcode the old bucket ... correctly untouched; they need HARVEST_BUCKET set to reproduce, which is a note, not an edit' -- the commit that actually landed touched ONLY task-order/decomposition TEXT, never `lib/research/*.py`, so the message's specific line citations describe a state that has not been reached in the codebase, whatever the intent.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Old table reads failed and the worker recorded the renamed table with 42 rows; code citations were current in main but absent at the worker pin. S21 corrects the overly general no-such-code statement. Holder: CTO with CRO migration owner: carry path plus commit plus current resource identifier at the handoff. A current path without its tree does not update a pinned worker.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S21",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "e6057f26c57fc6ff6c223f1c73cc29be3c7f51d6 resolves in the main portal object store and is anchored by wk-amgt_resapp-5-8-portal; the recorded gitlink remains e85f6eb84f. The successful fetch disarms the immediate only-copy risk in S19. Holder: CTO for the remaining base/integration decision under the PROD+DEV freeze. Neither object presence nor 20 changed files proves an integrated or served route.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S21",
      "THE REMEDY, PROVEN BY THE ACT THAT WOULD HAVE DESTROYED THE WORK: `git worktree remove --force C:/tmp/wk-amgt-5-8` ran, the directory is GONE, and afterwards `git -C portal cat-file -t e6057f26` -> `commit`, `53e38bcd` -> `commit`, branch `wk-amgt_resapp-5-8-portal` resolves to `e6057f26`, 20 files on it. NEGATIVE CONTROL in the same run: a bogus id -> `could not get object info`. Without the pre-teardown fetch those 20 files and 2,067 insertions existed in exactly one place and that place was deleted.",
      "\u26d4 THE PREDICTED TRIGGER DID NOT FIRE, and saying so is the point of this row. `Z-S19` forecast that merging the branch would RECORD A GITLINK to an object the main portal lacked. Measured after the merge: `git ls-tree HEAD portal` -> `e85f6eb84f`, and `git ls-tree HEAD~1 portal` -> `e85f6eb84f`. IDENTICAL. The worker left ` M portal` uncommitted, so no gitlink change was ever in the branch and the dangling-pointer failure was never reachable.",
      "SO THE ACTUAL STATE IS THE INVERSE: the recorded gitlink still names `e85f6eb84f`, a commit from the IRPT_FNTEND chain, and it RESOLVES fine (`cat-file -t` -> `commit`). The pointer is valid and STALE. `e6057f26` -- the Lead Panel -- is reachable only from the branch this seat anchored, and NO superproject commit references it.",
      "THE WORK ITSELF, so its location is unambiguous: 20 files / 2,067 insertions, all additive, authored `0.9.0_WK_AMGT_RESAPP~2`, on `wk-amgt_resapp-5-8-portal` in the MAIN portal repo -- `src/pages/SecurityAnalysis/` (LeadPanel, ThesisTab, PeersTab, CoverageTab, PrintExportAction, hooks, types), `src/api/endpoints/amgt-lead-panel.ts`, and a `src/App.tsx` route edit.",
      "THE DRAIN'S OWN RESULT, for the record: merged @`6e764ef0aa` through `safe-merge.sh`'s `--no-commit` window; the channel conflicted as it does on every concurrent drain and was resolved APPEND-ONLY -- 3 branch rows added, all 51 HEAD rows byte-identical, verified by prefix comparison before writing; the row gate graded the MERGED index (3 new of 54, 51 not re-graded, 0 violations) and the duplicate-id limb found no collision.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "e6057f26c57fc6ff6c223f1c73cc29be3c7f51d6 resolves in the main portal object store and is anchored by wk-amgt_resapp-5-8-portal; the recorded gitlink remains e85f6eb84f. The successful fetch disarms the immediate only-copy risk in S19. Holder: CTO for the remaining base/integration decision under the PROD+DEV freeze. Neither object presence nor 20 changed files proves an integrated or served route.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S49",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "At the pinned HEAD, both root .tf files contain zero aws_dynamodb_table declarations, but scheduler IAM references aws_dynamodb_table.security_metrics.arn and two old opal-amgt-articles ARNs. The renamed tables are in another Terraform root. These are source-level unresolved/stale dependencies.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf@11a1461029a1edfa4ac8684db20103606cc20c3e:68,69,76",
      "infra/aws/terraform/harvest/dynamodb.tf@11a1461029a1edfa4ac8684db20103606cc20c3e",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "CRO owns the harvest migration; CTO reads this row and COO owns any existing-cell recut. Remedy: reconcile scheduler resource/IAM dependencies with the new estate, validate the whole module, and establish deployed ZIP/universe/table vintage before claiming a future run works. No AWS read, terraform init/validate/apply or live invocation was performed by CVO; this is not a claim that a scheduled production run has already failed. Keep historical RD5 AC4 grade pinned. No new-cell inference is needed: the scheduled producer is an existing cell. Current comp-iam role read still lists the two old article ARNs; no deployed permission or module validation claim is made. This remains with CRO in place and is not assigned to the frontend worker.",
    "owner": "4.0.0_SA_CRO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "4.0.0_SA_CRO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S50",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The source implements a partial presentation, while the check substitutes static fixtures and a Print replica. Missing API connections, collapsed controls and source/report inconsistencies remain. This is sufficient to fail AC4 without inventing a runtime outage measurement.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json",
      "portal:e6057f26c57fc6ff6c223f1c73cc29be3c7f51d6:src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/AMGT-rd-8.design-decisions-and-rehomed-figures.md",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "Holder CTO for the grade and integration decision; COO recuts the existing surface cell with the necessary adapter ownership/grants, actual route evidence and any artifact corrections. A missing implementation or grant for work already named in rd8 is not by itself proof that the decomposition lacks a cell. No automatic DECOMP_INVALIDATING disposition, portal promote, task-order mutation or worker message.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S22",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two reported runs on one active round lacked an IN-PROGRESS class; CVO's own evidence creation and checkpoint directly corroborate work in progress. CTO commit 652ca9e2dd adds the class, output-plane probe, stalled-test qualifier and report field. The test producer explicitly defines SEC_KEY=VINTAGEID_US_Equity, so the separate unsubstituted-placeholder conjecture is rejected.",
    "evidence": [
      "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md@651ffd4f16477b632b593a5e8db69aaca05eacec#AMGT_RESAPP-Z-S22",
      ".claude/skills/canonical-flow/SKILL.md@652ca9e2dd:154,199,200,224",
      "integrations/bloomberg/research/tests/test_vintage_derivation_identity.py:37-42",
      "CVO evidence checkpoint 11a1461029a1edfa4ac8684db20103606cc20c3e",
      "MSTR correction 21664, exact file 20260911T213059Z_0.0.0_AB_MSTR_Z_CORRECTION_to_my_21657___a_recycle_takes.md",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json"
    ],
    "remedy": "The class/probe source remedy is executed by its owner; no full post-edit operational run was performed by CVO. This is one uncovered state, not a proof that every former class assumed absence or a complete state census. Residual correction owed to CTO: the new skill prose and 21672 repeat that killing the process destroys 189 KB of uncommitted files. That is false, already corrected by MSTR 21664: process termination loses in-flight context, not on-disk bytes. Correct that causal claim while retaining the output-plane probe. Hazard remains ARMED for that misleading recovery premise; no seat lifecycle action was taken. At the round-6 read .claude/skills/canonical-flow/SKILL.md:222 still says a kill would destroy 189 KB of uncommitted work. Correct it to loss of in-flight context; on-disk files persist absent a separate deletion. New BLOCKED/output-plane source improvements do not repair this remaining sentence.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-13T03:37:45Z"
    }
  }
]
```
