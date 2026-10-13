# ADVI_FIRMBKTS -- round 4 remediations (dell1)

<sweep_watermark>2026-10-13T06:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T06:10:00Z. Graduated at ADJUDICATION_v5: 33 rows. FWD-1 PARTIAL (D1-C-S29); FWD-4 PARTIAL at stage
APPLIED for the validator's canonical ownership read (D1-C-S37).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W35-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The client-data check of the commit gate did not run on this device: the hashed account-id list is absent at its default path, so safe-commit printed WARN and commit 711d72b756 landed unchecked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W35-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W43-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit printed WARN that the client-data check could not run (hashed account-id list absent on this device); commit c64a667818 was not checked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W43-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W45-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit printed WARN that the client-data check could not run (hashed account-id list absent on this device); commit 8114bac9cf was not checked for client account ids (a repeat of ADVI_FIRMBKTS-D1-W43-S2).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W45-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W49-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-commit's commit-gate checked 0 of 1 file (the registry JSON is outside its graded suffixes) and the client-data check printed WARN with the hashed account-id list absent; commit 3a6d8aa89d was not checked for client account ids (a repeat of ADVI_FIRMBKTS-D1-W43-S2 and W45-S2).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W49-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W53-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The safe-commit client-data check could not run for the flip commit: the hashed account-id list is absent on this box, so the commit was not checked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W53-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W54-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The safe-commit client-data check could not run for the re-pin commit e274a0e60c: the hashed account-id list is absent on this box, so the commit was not checked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W54-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W57-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The client-data-check on the FB-g-34 commit ran WARN, not PASS: the hashed account-id list is absent on this device, so the commit was not checked for client account ids.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W57-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W54-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pre-commit risk reflex put HOLD on infra/aws/lambda/ci/lambda-source-map.json and cited a memory file that is not readable on this box; the commit proceeded.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W54-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-13T06:10:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W42-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf, citing deploy-completion notes about other roots' main.tf files (a basename match); the commit landed rc=0 on 273de502f0.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W42-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W43-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf citing deploy-completion notes about other roots' main.tf files (a basename match); the commit landed rc=0 on c64a667818.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W43-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W45-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf by basename match, citing another root's deploy note; commit 8114bac9cf landed rc=0 (a repeat of ADVI_FIRMBKTS-D1-W43-S1 and W42-S1).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W45-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W57-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The safe-commit risk-reflex advisory on FB-g-34 cited a device memory note that is absent from this device's memory directory, so the cited note could not be read before the commit.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W57-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S26",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-apply's cross-box seat gate read open_deploy=hit verdict=STOP for another seat's OPEN deploy that names the bd-pipeline root, and in WARN mode the apply proceeded; the actor sees that line only once the apply is running, unless it runs --dry-seat-gates first.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S26",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S30",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The cross-box seat gate reports an OPEN deploy (iamroles-r7-narrow-portal-s3, 0.7.0_AE_CloudOps~IR) that reads CLOSED in this tree's change-management entry and whose sentinel is in none of the 50 worktrees read, and it names the shared-infra root by path token alone; with a cross-box call naming the same root, the gate read STOP in WARN mode for a one-resource apply that touches neither.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S30",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The device or gate owner restores the check (the hashed account-id list on dell1; the risk reflex reading notes by full path and only when readable; the seat gate reading the change-management record before an open entry). Close when: the named check runs clean on dell1",
    "owner": "0.0.0_AB_MSTR",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W52-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-g-32 census: the Budgets reads are denied to the worker identity, so the find-insure-budget-alerts Budgets actions are unread and that topic lists its code publisher only.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W52-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Read with the SEV1 page path (D1-S15/S16/S20): each unread publisher or literal is accounted. Close when: the SEV1 census names each with its disposition",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W52-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-g-32 census: a live Lambda (ec2-runtime-monitor) publishes to ec2-long-running-alerts, which has an SMS subscription, but its source is not in this tree, so the census lists no code publisher for that topic.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W52-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Read with the SEV1 page path (D1-S15/S16/S20): each unread publisher or literal is accounted. Close when: the SEV1 census names each with its disposition",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W52-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-g-32 census: data/inf/scripts/gold/lib/aor_attribution_audit.py:204 publishes to the topic named by INF_AOR_DRIFT_SNS_ARN, which no tree wiring sets; its docstring names opal-partner-etl-ops-alerts, so the census does not count it.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W52-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Read with the SEV1 page path (D1-S15/S16/S20): each unread publisher or literal is accounted. Close when: the SEV1 census names each with its disposition",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W52-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Repository Terraform carries E.164 phone-number literals in a comment and in a variable default, outside this order's paths; the census cites them by path only and writes none.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W52-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Read with the SEV1 page path (D1-S15/S16/S20): each unread publisher or literal is accounted. Close when: the SEV1 census names each with its disposition",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W60-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The naming gate documents a test exemption for the path segment /tests/, but the test directories this order names are test/, so every edit under them is graded.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W60-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The owner rules or fixes (the naming gate's test-directory exemption; the fence instrument's encoding; the BD pricing findings routed to the producing pipeline's project). Close when: the fix or ruling names the row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-13T06:10:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S28",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The standing scoped-exemption instrument infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py reads ok=False at HEAD: its scratch root before_strip fails init on one(list), and it raises a cp1252 UnicodeEncodeError unless PYTHONIOENCODING=utf-8 is set.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S28",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The owner rules or fixes (the naming gate's test-directory exemption; the fence instrument's encoding; the BD pricing findings routed to the producing pipeline's project). Close when: the fix or ruling names the row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S32",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bd_price_update.py:344 takes the median of calc_price over silver/transactions/<date>.parquet rows that repeat once per portfolio group (no transaction_id dedupe on the per-date loader :263-271), so the T-1 price is weighted by how many groups hold the asset -- a rule nobody chose. Routed from dell2 (IRPT_DASHBD-D2-W122-S1).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S32",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The owner rules or fixes (the naming gate's test-directory exemption; the fence instrument's encoding; the BD pricing findings routed to the producing pipeline's project). Close when: the fix or ruling names the row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S33",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "B_01.holdings_lots.py picks each asset's served price by sort_values('date', ascending=False).drop_duplicates('asset_name', keep='first') over the concat of silver/prices/<date>.parquet and canonical_prices.parquet; the default sort is not stable, so on a same-date tie which object's price wins is undefined by the code -- the 'not established' of dell2 D2-W125-S1/-S2 is not establishable by reading.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S33",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The owner rules or fixes (the naming gate's test-directory exemption; the fence instrument's encoding; the BD pricing findings routed to the producing pipeline's project). Close when: the fix or ruling names the row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S34",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three SERVED readers key on the silver/transactions FILE day, not trade_date: B_03.account_gains.py:327, bd_price_update.py:265 and its Lambda twin :143. The late-August rewrites moved 5,580 ids one file each toward their own trade date (0 then, 4,505 and 1,030 now), so a re-run of those readers can serve different 08-20..08-23 figures than first served.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S34",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "The owner rules or fixes (the naming gate's test-directory exemption; the fence instrument's encoding; the BD pricing findings routed to the producing pipeline's project). Close when: the fix or ruling names the row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S40",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The exec-summary generator is triggered by a gold chain-complete EVENT, not a 04:30Z cron, and that event has not been emitted by any gold chain in the run log since at least 2026-04-25 (every chain logs put-events failed); the generator has not run since 2026-05-04, before and independent of the cutover.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S40",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S35",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r3_f7_delta.py apply reads every overwrite key's prior version serially (49,110 head_object calls, about 42 minutes at 17 per second) BEFORE its first copy, prints nothing until it ends, opens the rollback record in append mode, and its --budget-seconds bounds only the copy phase; an outer timeout kills the record phase silently and each re-run appends duplicate rows.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S35",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S39",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-FB-f-11 instrument gaps: the first-hour origin 403/404 read has no per-behavior source; the performance adapter's census event refuses at input validation so it writes no evidence key; the sample's ownership_read field cannot be filled from logs.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S39",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W52-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FB-g-32 AC1 arm S2 checks that each cited code file exists, not that the cited line exists; a publisher cited at a nonexistent line passes S2 and a nonexistent file fails it.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W52-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W40-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The router's v15 header comment still says the canonical list is EMPTY today. The bounds keep every line other than the local definition and its comment, so the header now contradicts the imported list.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W40-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W44-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Removing the adapter's hand statements left its explanatory comments in s3-49financial.tf above code that no longer exists, so they now describe Denies and locals the file does not hold.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W44-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W53-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The flip tool's --apply step rewrote the generated mark line of the nested portal/ submodule working copy (firmDisplayNames.generated.ts), uncommitted, though the order said to touch nothing under portal/.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W53-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S35"
    ],
    "remedy": "Round 5: the issuer cuts or rules each (the exec-summary trigger diagnosis per ADDENDUM 12; the delta tool; instrument gaps; stale comments; the portal mark line committed or restored). Close when: the round-5 cut or a ruling names the row",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S33",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NEW: auth-validator-edge's own spec fails 1 of 6 at HEAD -- 'ownership_key: dormant shipped list (i) the list is the generated one: frozen, and none of the generated FIRM_CONFIG buckets is in it' expects false and reads true, because the flip put opal-data-49financial in the list. FB-g-37 updated the router and guard expectations but not the validator's; the deployed validator v23 is not affected, but a build gate that runs this spec refuses the next validator build.",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-D1-C-S33"
    ],
    "remedy": "The validator spec's dormancy expectation is updated to the flipped list (as FB-g-37 did for the router and guard). Close when: auth-validator-edge's bun test reads 0 fail at HEAD",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S34",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NEW, a recurrence of D1-C-S21: TO-FB-f-9 reached complete in round 4 with AC2 and AC3 still typed '--since <MOVE_TS>'; the invocation does not run as written (bash syntax error). With MOVE_TS supplied this seat reads both PASS (D1-C-S27).",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-D1-C-S34"
    ],
    "remedy": "Same remedy as D1-C-S21; this row carries the round-4 recurrence. Close when: D1-C-S21 closes",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S37",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NEW: FWD-4's comparison does not cover the validator's post-move ownership decisions (accounts and relationship paths, 27 v23 request lines, none on those paths); FWD-4 is PARTIAL at stage APPLIED for that read (D1-C-S26).",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-D1-C-S37"
    ],
    "remedy": "A deliberate post-move comparison of the validator's ownership decisions on the accounts and relationship paths (a signed non-admin session, before/after). Close when: that comparison is recorded",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  }
]
```
