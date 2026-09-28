# NFRA_OPALAI -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Recorded: 2026-09-28T14:26:00Z. **Reader:** `1.0.0_SA_CTO~O`.

The project's first remediation file. 7 rows, all graduated by C-S6: 3 REMEDIATED on evidence re-read here, and 4
OPEN (Z-S4 and Z-S17 are fabric gates routed to the CTO; Z-S20 and Z-W8-S1 are the issuer's).

```json
[
  {
    "id": "NFRA_OPALAI-Z-W2-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "app/audit.py's _ARGS_ALLOWLIST did not declare opal_asker_query, so the fail-closed default omitted the asker oid, key and verdict from the audit row.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-W2-S2",
      "commit 050035f941 (app/audit.py:94)",
      "git show 6a98a0553a:infra/aws/ec2/opal-gateway/app/audit.py (the served pin carries the row)"
    ],
    "remedy": "Executed: the allowlist row exists at HEAD and in the served gateway pin.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPALAI-Z-S11",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "install-owned-paths.sh --submodule resolved REPO_ROOT from the ambient cwd, so it could install into the wrong tree.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S11",
      "commit aa2f79ef0d (.tools/git-hooks/install-owned-paths.sh:34 resolves from _SELF_DIR first)"
    ],
    "remedy": "Executed: REPO_ROOT resolves from the script's own location.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPALAI-Z-S14",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-ec2-deploy.sh wrote jq.exe's CRLF temp output into EC2_MANIFEST.json, and the naming gate at Step 3 refused every graded line.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S14",
      "commit 765093b0e3 (infra/aws/ec2/safe-ec2-deploy.sh:212, tr -d CR)"
    ],
    "remedy": "Executed: the temp output is CR-stripped, as SOURCE_PATH already was at :99.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPALAI-Z-S17",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The owned-paths wrapper and owned-paths-check.sh resolve the superproject from the FIRST 'git worktree list' entry. For a submodule that is its gitdir (.git/modules/<name>), which has no superproject, so a nested linked worktree outside any parent worktree commits with the lane check SKIPPED.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S17",
      ".tools/git-hooks/owned-paths-check.sh:59",
      ".tools/git-hooks/install-owned-paths.sh:95"
    ],
    "remedy": "OPEN: resolve the superproject from the worktree's own path, or refuse (fail CLOSED) when no superproject resolves, and prove it on a nested linked worktree outside a parent. A fabric gate, so routed to its owner.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S20",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "opal_ai CI cannot pass: its workflow installs no pytest, and the moved portal_lookup.py carries 15 ruff errors. With no branch protection the red is silent.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S20",
      "gh run list (opal_ai): the only run is 36203070607, failure"
    ],
    "remedy": "OPEN: install pytest in the workflow, clear the 15 ruff errors, and show one green run. FWD-13 is unmet until then.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-W8-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "tests/test_data_entitlement_guard.py cannot be collected on this device (moto absent), so 'keeps passing' was UNREAD for OA-f-1 and remains unread after OA-f-2 deployed.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-W8-S1",
      "python -c 'import moto' -> ModuleNotFoundError (this seat, 14:0xZ)"
    ],
    "remedy": "OPEN: one run of the suite on a device with moto, with its count recorded.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPALAI-Z-S4",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The lane resolver returns UNDEFINED for a path with no lane row before it consults the worker grant, so a granted path can only be committed through the audited author override.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S4",
      "commit history of NFRA_OPALAI OA-w-2 (lane rows added for opal_ai/**, which closes this project's instance only)"
    ],
    "remedy": "OPEN, not re-measured by this seat: consult the worker grant before returning UNDEFINED. NFRA_MCPORTAL MP-w-1 met the same ordering. A fabric gate, so routed to its owner.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v1"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
