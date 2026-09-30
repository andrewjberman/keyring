# NFRA_MCPMSP -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Recorded: 2026-09-30T21:35Z. **Reader:** `1.0.0_SA_CTO~O`.

The project's first remediation file. 7 entries, one per graduated row, all OPEN (Z-W4-S1 is published by Z-W4-S2's same act). Five are tooling
defects that recur on the next gateway release or Terraform apply, whichever project runs it. One is a carrier C5 needs
before any cell reads opal-data-inf. None blocks round 2's first item (the portal-v2 zero-read, C5 v0.3).

```json
[
  {
    "id": "NFRA_MCPMSP-Z-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C5 has the per-firm role read its firm's bucket (opal-data-inf for Inflection), but the naming builder routes inflection to opal-data-inflection, which does not exist; the live alias opal-data-inf has lookup false, and the ENFORCE gate refuses the literal. Round 1 reads only the portal-v2 prefix, so C5's firm-bucket half has no conforming carrier.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-S2",
      "infra/logic/registry/scopes.json inflection row (bucket opal-data-inflection; alias opal-data-inf lookup false)",
      "infra/aws/terraform/modules/opal_name/generated_locals.tf:65-79 scope_bucket"
    ],
    "remedy": "Before any cell reads opal-data-inf: a registry route that yields the routed bucket (an LGIC act), or an R20 departure Andrew acknowledges. His 13:0xZ naming exception covers platinum/etfs and BD fees only, not this key. Not a round-2 blocker: round 2's first item is the portal-v2 zero-read (C5 v0.3).",
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
    "id": "NFRA_MCPMSP-Z-W2-S3",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-apply.sh's naming-plan limb plans the WHOLE Terraform directory and ignores -target, so any seat's pending addition refuses every other seat's targeted apply. In a shared directory like infra/aws/terraform/opal-gateway (MCPMSP firm roles, ETFS_RIVALS, Schwab reader) that couples unrelated projects' applies, and each blocked try spends about 4.5 minutes in full-tree refreshes.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W2-S3",
      ".tools/safe-apply.sh last changed 0af3c52597 (2026-09-16), so the limb is unchanged; MS-a-1 applied at 10:03Z (ledger 20260930T0844Z CLOSED). This compile did not measure what cleared the refusal in between."
    ],
    "remedy": "Grade only the targeted resources' names when -target or a saved planfile is given, and keep full-tree grading for an untargeted apply. The gate's owner decides.",
    "owner": "laptop 1.0.0_SA_CTO (LGIC_ENFORCE, gate owner); routed by 1.0.0_SA_CTO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "laptop 1.0.0_SA_CTO (LGIC_ENFORCE, gate owner); routed by 1.0.0_SA_CTO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPMSP-Z-W3-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grant writer's build_package.py stages lambda_function.py from the WORKING TREE, which is CRLF on this Windows checkout while HEAD's blob is LF (.gitattributes eol=lf). The first MS-a-2 package shipped non-HEAD bytes, live for about 4 minutes.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W3-S2",
      "a2.AC2 apply 1: identical=False (381 CRLF pairs staged, 0 in HEAD); re-applied from `git show HEAD:` bytes"
    ],
    "remedy": "Stage from `git show HEAD:<path>` (or normalise to LF) inside build_package.py, so a 'deployed == HEAD' check passes on every checkout.",
    "owner": "2.0.0_SA_COO~O (NFRA_MCPORTAL grant writer)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O (NFRA_MCPORTAL grant writer)",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPMSP-Z-W1-S7",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy-to-ec2.sh builds the dashboard from a nested $WORKSPACE_ROOT/mcportal checkout, but the parent repo's gitlink pins mcportal at fa1ff9693b (README only) while the served bundle is a3bff71ffa (EC2_MANIFEST mcportal_commit). Every gateway release from a fresh worktree therefore needs a hand-made mcportal worktree at the right pin; the MX-r-5/6 and MS-d-1 releases each built one.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S7",
      "git ls-tree 093fc247c6 mcportal = fa1ff9693b; EC2_MANIFEST services.opal-gateway.mcportal_commit a3bff71ffa",
      "the MS-d-1 mcportal worktrees are gone (/c/tmp/ms-1-rel and ms-1-rb absent, 21:3xZ)"
    ],
    "remedy": "Either bump the parent gitlink to the served mcportal commit, or have deploy-to-ec2.sh check out the manifest's mcportal_commit itself. Either way a release tree carries the right pin with no hand step. deploy-to-ec2.sh is already in every gateway release diff.",
    "owner": "1.0.0_SA_CTO~O (gateway release tooling)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O (gateway release tooling)",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPMSP-Z-W1-S8",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gateway test suites append to the TRACKED infra/aws/ec2/opal-gateway/audit.jsonl, so running them in a release tree trips safe-ec2-deploy.sh's 'uncommitted changes' prompt. The same dirt sat in the oa-10 worktree at the crash (2026-09-29).",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W1-S8",
      "MS-d-1 release tree: ' M infra/aws/ec2/opal-gateway/audit.jsonl' (6 lines) after the suites",
      ".runtime/crash-investigation-20260929 worktree scan: oa-10 carried the same tracked edit"
    ],
    "remedy": "Point the suites' audit writer at a temp path, or stop tracking audit.jsonl (the tarball already excludes it).",
    "owner": "1.0.0_SA_CTO~O (gateway)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O (gateway)",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPMSP-Z-W4-S1",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MS-a-3 item 0 shortened provision-account.ps1's -Description literal (86 -> 42 chars, New-LocalUser's 48-char limit) in opal_ai commit 47cfd4b, which is on opal_ai's local DEV only; until it is published, the same over-long literal is what any other checkout of opal_ai provisions with.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S1",
      "measured 21:3xZ: git -C opal_ai branch -a --contains 47cfd4b -> DEV only (local)"
    ],
    "remedy": "Rides Z-W4-S2's publication: publish opal_ai DEV, then bump the parent gitlink.",
    "owner": "0.0.0_AB_MSTR~Z (push)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z (push)",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_MCPMSP-Z-W4-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MS-a-3's nested opal_ai commits 47cfd4b (the -Description length fix, Z-W4-S1) and 61841f5 (the verify-boundary run-as route) are on opal_ai's local DEV only: `git -C opal_ai branch -r --contains 61841f5` names no remote branch. The parent gitlink bump was refused as NOT PUBLISHED, and the real MS-a-3 AC2 boundary run is Andrew's after the drain.",
    "evidence": [
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S1",
      "investigations/INVESTIGATION_v1.Z.md#NFRA_MCPMSP-Z-W4-S2",
      "measured 21:3xZ: git -C opal_ai branch -a --contains 47cfd4b / 61841f5 -> DEV only (local)"
    ],
    "remedy": "Publish opal_ai DEV (the shared-branch push is 0.0.0_AB_MSTR~Z's, on Andrew's word), then bump the parent gitlink, then Andrew runs verify-boundary as Opal_MSP.",
    "owner": "0.0.0_AB_MSTR~Z (push) / Andrew (the AC2 run)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z (push) / Andrew (the AC2 run)",
      "round": "v1"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~O
