# ADVI_FIRMBKTS -- remediations (compile ordered by the CTO's closure plan)

<sweep_watermark>2026-09-19T21:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~09:1xZ. Trigger: 1.0.0_SA_CTO 103630 and 103656 (RULINGS batches 71 and 74: the compile order). The channel held 2 undispositioned rows of 11; both are graduated here. It also held 5 rows that this seat's 2026-09-14 intake (ADJUDICATION_v1.md, C-S2 and C-S3) graduated to 1.0.0_SA_CTO without writing their remediation rows; the row gate refuses a new row until they exist, so they are written here, each re-read where a read was cheap. Closed on this seat's reads: S2, S7, S10. Open with an owner: S1, S8, S9, W2-S10. The project has no task order yet (its PRD is admitted and waits for L5). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed).

```json
[
  {
    "id": "ADVI_FIRMBKTS-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "portal-auth's Terraform root planned an unrelated in-place change to the production WAF ACL (opal-cloudfront-protection) before any edit. Card 3 applied targeted and closed its ledger; the WAF's planned remove-and-re-add was never applied, so the next full apply of that root meets it on the production front door.",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-C-S3 (3.0.0_SA_CVO, 2026-09-14): graduated to 1.0.0_SA_CTO with no remediation row written; this row is that missed carrier",
      "NOT re-measured at this compile: no plan of portal-auth was run, so whether the diff still stands 17 days on is unread",
      "investigation row ADVI_FIRMBKTS-S1 (0.7.0_AE_CloudOps, 2026-09-13)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1: one read-only plan of portal-auth, read for the WAF resource alone. If the diff stands, it gets its own never-widen packet (a production front-door change) or the config is brought to the live state; until then every apply of that root is targeted, and says so.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The organisation audit trail was imported into shared-infra's remote state while its config existed only at or after commit 9f3fd2cf4a, so a full shared-infra apply from any older checkout planned the trail's destroy, with prevent_destroy living in the config the checkout lacked.",
    "evidence": [
      "git worktree list on this device (this seat, 2026-10-01 09:1xZ): 13 worktrees, 0 whose HEAD lacks 9f3fd2cf4a; control, the main tree's HEAD contains it; origin/CLOUD contains it",
      "adjudication row ADVI_FIRMBKTS-C-S2 (3.0.0_SA_CVO, 2026-09-14): 24 of 33 linked worktrees lacked it then",
      "NOT read: site Z's checkouts. SITEZ is retired as a branch and both devices commit to CLOUD (org/XXX.md), and origin/CLOUD carries the config, so a site-Z checkout older than 2026-09-14 is the only place the hazard could still stand",
      "investigation row ADVI_FIRMBKTS-S2 (2.0.0_SA_COO~E, 2026-09-14)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done on this device and on origin: every checkout carries the config. The row's disarm was the push and the merge, both since made.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-01T09:15Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy_ledger.py re-rendered an entry from its saved state at every close, so notes an operator had appended by hand were overwritten.",
    "evidence": [
      "commit a4b8ac93e0 (1.0.0_SA_CTO, 2026-09-15): 'deploy_ledger re-renders keep the entry's Sign-off section'",
      ".tools/deploy_ledger.py:255 at HEAD (this seat): 'Never hand-edit an entry -- except its ## Sign-off section, which _write_entry carries through every' re-render",
      "investigation row ADVI_FIRMBKTS-S7 (2.0.0_SA_COO~E, 2026-09-14)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done: the tool carries one hand-written section through its re-renders and states the rule for everything else.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "/cloud-ops lists record-terraform-deploy.sh among the commit and deploy tools with no path, and no file of that name exists under .tools/, so a seat following the skill does not find it and the root's CHANGELOG.json goes unwritten.",
    "evidence": [
      "git ls-files (this seat, 2026-10-01): the script is tracked at infra/aws/lambda/ci/record-terraform-deploy.sh; .tools/record-terraform-deploy.sh does not exist",
      ".claude/skills/cloud-ops/SKILL.md:18 names it beside safe-commit.sh and safe-apply.sh, which are under .tools/",
      "infra/aws/lambda/ci/lambda-source-map.json: an entry recorded_by record-terraform-deploy.sh on 2026-09-27, so the script works for a seat that knows where it is",
      "investigation row ADVI_FIRMBKTS-S8 (2.0.0_SA_COO~E, 2026-09-14)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P3: the skill gives the script's path. One line.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The AWS corpus models no CloudTrail trail, so the live plane's drift classes cannot show a trail that was applied outside Terraform, which was the case card 3 existed to fix.",
    "evidence": [
      "comp-find 'opal-organization-trail' --corpus aws (this seat, 2026-10-01 09:1xZ; built 2026-10-01 08:33:07 UTC): 0 hit(s) across 2733 aws node(s), bands none",
      "the tool now says, on a zero, that it is 'a MEASURED zero over 2733 aws node(s) in the graph -- not a claim the term is absent from AWS: only what the graph MODELS can match'",
      "investigation row ADVI_FIRMBKTS-S9 (2.0.0_SA_COO~E, 2026-09-14): the same zero over 2,531 nodes",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the corpus gains the CloudTrail trail as a node class, or the tool's list of unmodelled classes names it. The tool's owner places it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The AWS corpus answered a measured zero for two firm buckets that had been live for sixteen hours when it was built, and a resource missing from the graph carries no drift class, so the zero read as absence. A census cell of this project asking 'does this firm bucket exist' through the corpus would have been told no for exactly the two buckets the project is about.",
    "evidence": [
      "comp-find 'opal-data-(inflection|cottonwood)' --corpus aws (this seat, 2026-10-01 09:0xZ; vintage 'Built from the estate as of 2026-10-01 08:33:07 UTC'): 2 hit(s) across 2733 aws node(s), band S3_BUCKET=2, both drift=DECLARED",
      "positive control, the same call for opal-data-bd: 159 hit(s) across 2733 node(s), S3_BUCKET=1",
      "investigation row ADVI_FIRMBKTS-S10 (1.0.0_SA_CTO, 2026-09-19): 0 hits across 2593 nodes at the 2026-09-19 12:21Z build",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "Done for this project: both buckets are nodes of the corpus and read DECLARED. The structural half is a property of the instrument and is stated in the review for its owner: a zero from the corpus is an absence from the GRAPH, and the graph's own completeness has no denominator.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-01T08:33Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-W2-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A live, undeclared key prefix sits in the 49 Financial data bucket: opal-data-49financial/_campaign/c02-reemit/. It has no Terraform declaration and no registry mark, its name does not grade under the naming grammar, and what it holds is a Python script, not data.",
    "evidence": [
      "s3api list-objects-v2 --bucket opal-data-49financial --prefix _campaign/c02-reemit/ (this seat, 2026-10-01 09:0xZ): first key _campaign/c02-reemit/c02_reemit_mirror_pull.py, LastModified 2026-08-30T02:33:41Z",
      "comp-keys partitions s3://opal-data-49financial/_campaign/ (this seat): 0 date partitions under the prefix",
      "investigation row ADVI_FIRMBKTS-W2-S10 (0.9.0_WK_LGIC_LGCTFM~2, 2026-09-18): the name RAISEs against lib/opal_naming.py grade()",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P2: the project's census cell (F1) lists this prefix with its owner and purpose, and the migration either gives it a registered home or removes it under the owner's word (an S3 delete needs a human confirmation). A script in a firm's data bucket is also a code-in-data-plane question for the CTO.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  }
]
```
