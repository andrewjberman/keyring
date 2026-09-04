# NFRA_CLDGRPH -- surprise channel, REMEDIATION v3 (round 3, laptop fabric)

**Home:** the project tree's remediation document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED item, keyed by the item's id; the clocks (`disarm`, `remediation`,
`closed`) advance in place and only forward. Form: spine v3 -- no route token; the CTO routes every round from the slug.
**Denominator at this write:** 4 rows (S26, S27, S28, S31), all OPEN. The graduations are recorded in
`../adjudications/ADJUDICATION_v1.md` (C-S1, C-S3, C-S4, C-S5). Rows of rounds 1 and 2 whose clocks this round
advanced are edited in place in REMEDIATION_v1.md (S2, S3, S8) and REMEDIATION_v2.md (S10, S20, S22, S23, S24).

## S26 -- the user-bin shim DACLs are rewritten by the provisioner's chmod on every run; the remedy is at the writer

```json
[
  {
    "id": "NFRA_CLDGRPH-S26",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The user-bin shims' DACLs are rewritten on every provisioning run: .tools/provision-path-shims.sh:207 runs chmod +x on each extensionless forwarder (:117 on aws) and never on the .cmd twin written at :209, and under MSYS a chmod is emulated by writing a PROTECTED explicit DACL with deny ACEs that reconcile the POSIX mode -- so an icacls repair (S29's deny removal, S30's inheritance reset) lasts exactly until the next run. Measured: S30 left 0 of 211 files protected at 2026-09-03T19:55Z; a run at 2026-09-04T05:20-05:22Z left 105 of 211 protected with 2 DENY ACEs each, all of them chmod-bearing files (96 extensionless, 8 .py, 1 .sh), while all 105 .cmd twins written in the same seconds came back clean and inheriting.",
    "evidence": [
      "Get-Acl over all 211 files of C:\\Users\\AndrewBerman\\bin at 2026-09-04T06:05Z, unscoped: protected 105 / 211; DENY-bearing 105 / 211; lacking the Andrew\\CodexSandboxUsers ALLOW 0 / 211; protected by extension '' 96, .py 8, .sh 1; every .cmd (105) unprotected -- 3.0.0_SA_CVO, adjudication row C-S1.",
      "LastWriteTimeUtc: all 105 protected files 2026-09-04T05:20Z-05:22Z; 105 of the 106 clean files in the same window (comp-read.cmd 05:22:28Z, its forwarder comp-read 05:22:27Z).",
      "comp-read (bash forwarder) DACL at 06:05Z, eight explicit ACEs, zero inherited: Deny NULL SID (REA,WEA,X,DC,RP); Deny AzureAD\\AndrewBerman ExecuteFile; Allow AzureAD\\AndrewBerman FullControl; Allow SYSTEM / Administrators / CodexSandboxUsers (W,RX); Allow Everyone (X,RA,RP) -- the MSYS mode-emulation shape.",
      ".tools/provision-path-shims.sh at HEAD: :180 cat > $BIN/$tool; :207 chmod +x $BIN/$tool; :209 cat > $BIN/$tool.cmd with no chmod -- the one operation separating the protected population from the clean one.",
      "S30 @8ae823ba17 post-state (its author, unscoped, 2026-09-03T19:55Z): protected 0 / 211, DENY 0 / 211 -- so today's 105 are a recurrence inside eleven hours, with no Codex seat having run since ~21:0xZ on 09-03."
    ],
    "remedy": "At the provisioner, the owner of the write: after the chmod at :207 (and :117 for aws), restore inheritance on the written file (icacls <file> /reset, or an equivalent that leaves the parent's inheritable DACL -- including Andrew\\CodexSandboxUsers:(OI)(CI)(M) -- as the file's DACL), or write the forwarder without mode emulation; then verify UNSCOPED after a fresh provisioning run: protected 0 of N, DENY 0 of N. Acceptance, S30's gate verbatim: a FRESH Codex seat launched only through ajb2/start-codex-seat.ps1; user-bin on PATH; Get-Command resolves all four shims; direct and bare comp-read --help and comp-find --help execute; comp-which as control; comp-to exercised against a designated probe TO and NOT with --help. If a fresh seat still denies or lacks PATH, the repair is in launcher/runtime provisioning and not a further DACL act.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v3"},
    "closed": false
  }
]
```

## S27 -- the cell text names cot-pipeline as a Lambda-notification resource; it is EventBridge-only

```json
[
  {
    "id": "NFRA_CLDGRPH-S27",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Decomp cell CG-s-14 (NFRA_CLDGRPH_DECOMP.md line 77) and TO-CG-C-3's measured-defect paragraph name bd-pipeline, cot-pipeline and inf-pipeline as aws_s3_bucket_notification resources with Lambda targets. cot-pipeline's only notification resource (infra/aws/terraform/cot-pipeline/s3-notifications.tf:16-19) is eventbridge = true with zero lambda_function blocks, by design since the 2026-06-11 chain-fix. The deriver derives no cot S3-to-Lambda edge, correctly; a reader of the cell text expects one and reads its absence as a deriver defect.",
    "evidence": [
      "infra/aws/terraform/cot-pipeline/s3-notifications.tf at HEAD, 19 lines read at 3.0.0_SA_CVO: resource aws_s3_bucket_notification.cot_data { bucket; eventbridge = true }; no lambda_function block; header cites ADVI_COTETL.CHAIN-FIX 2026-06-11 and eventbridge.tf.",
      "NFRA_CLDGRPH_DECOMP.md at HEAD: 1 whole-value hit for 'cot-pipeline' across 190 lines, line 77 (the CG-s-14 cell row) -- the durable carrier.",
      "S27 @ (0.8.0_AE_CloudComp~O, 2026-09-03T19:02Z): the deriver's tfstate read resolved eventbridge=true, lambda_function=[] for cot; C-3 proof @aea8346fe1 C3-AC3 met on the three bd targets."
    ],
    "remedy": "At the L5/L6 recut, in the CG-s-14 cell text and any successor face: name bd-pipeline and inf-pipeline as the aws_s3_bucket_notification resources with Lambda targets and name cot-pipeline's resource as EventBridge-only (a distinct target class outside this cell), so no reader expects a cot S3-to-Lambda edge. No Terraform change belongs to this item.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v3",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~A", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~A", "round": "v3"},
    "closed": false
  }
]
```

## S28 -- the C-3 fix is in source and in no running container: the shared image was pushed 21 minutes before the fix commit

```json
[
  {
    "id": "NFRA_CLDGRPH-S28",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The cloud derive runner (ECS family globgrph-derive-runner, revision 6) pulls opal-globgrph-derive-runner:latest. That tag is digest 68bd8b93..., pushed 2026-09-03T18:51:14Z by TO-CG-C-2's build; the C-3 engine fix b5bc1c8b27 (comp_aws_cli.py: UNREADABLE read state, declared second source, denominators) was authored 2026-09-03T19:12:54Z. No image has been pushed since. So every task on the tag runs comp_aws_cli.py from before the fix, and S20's zero-by-silence hazard remains live in the cloud although REMEDIATED in source. The tag is shared by seven ACTIVE task families, so the rebuild is a change-managed deploy, not a cell's act.",
    "evidence": [
      "ECR describe-images opal-globgrph-derive-runner at 2026-09-04T06:0xZ (3.0.0_SA_CVO): sha256:68bd8b93... tags [latest, 20260903-185059] pushed epoch 1788461474 = 2026-09-03T18:51:14Z; nothing newer.",
      "git log b5bc1c8b27: 2026-09-03T19:12:54Z, 0.8.0_AE_CloudComp~O, 'NFRA_CLDGRPH: preserve S3 notification read state'; merge-base --is-ancestor b5bc1c8b27 HEAD = YES.",
      "ECS ACTIVE families on the tag, read at this seat: globgrph-derive-runner:6, globgrph-comp-learns-producer:1, globgrph-cse-producer:1, globgrph-fedobs-producer:1, globgrph-resource-summaries-producer:1, globgrph-projection-worker:3, globgrph-serving:1 (7); the 08-26 ledger (change_management/20260826T0008Z_...:79-84) counted five.",
      "C-3 proof @aea8346fe1 C3-AC5: 'a shared-image rebuild is required and was routed as NFRA_CLDGRPH-S28' -- the worker's answer to its runtime question, confirmed here against ECR and ECS."
    ],
    "remedy": "Rebuild opal-globgrph-derive-runner from a HEAD that carries b5bc1c8b27 through the change-management path: ledger opened before and closed after; every family on the tag named (the seven above) and each one's next launch read for the new digest; then ONE real derive on the cloud runner whose log prints the S3 notification read denominator (read/unreadable) and non-zero TRIGGERS for the three bd targets. That run is S20's disarm and this row's; the rebuild's reach is S31's subject.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v3",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~A", "at": null},
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~A", "round": "v3"},
    "closed": false
  }
]
```

## S31 -- one `:latest` tag, seven task families: each worker-scoped rebuild was a deploy its controls could not see

```json
[
  {
    "id": "NFRA_CLDGRPH-S31",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The projection worker has no image of its own: task definition globgrph-projection-worker:3 references opal-globgrph-derive-runner:latest, the same string six other ACTIVE families reference (derive-runner:6, four producers, serving:1). TO-CG-B-2 (16:22Z, digest 1e1aaa14...) and TO-CG-C-2 (18:51Z, digest 68bd8b93...) each 'rebuilt the worker image' and each re-pointed :latest, so every family's next launch ran the new bytes. Both faces' blast-radius controls -- targeted apply, one unscoped Terraform re-plan quoted by address list, a NEVER-2 ledger of the worker's resources -- live on the Terraform plane; an image-tag move is an ECR-plane act no plan renders. The 08-26 ledger stated the class (':latest REACHES FIVE TASK-DEFS'); the round-2 and round-3 faces did not carry it.",
    "evidence": [
      "ECR image list at 3.0.0_SA_CVO 2026-09-04T06:0xZ: 20260903-162203 = 1e1aaa14... (B2-AC2's revision-2 digest, no longer tagged latest); 20260903-185059 = 68bd8b93... (C2-AC3's revision-3 digest, tagged latest) -- latest moved between them.",
      "ECS at this seat: seven ACTIVE families reference .../opal-globgrph-derive-runner:latest by tag, none by digest; two (nessie, trino) reference vendor images.",
      "TO-CG-C-2 face item 2 and C2-AC3 at HEAD: the act is scoped to 'the worker image ... revision 3 ... the Pipe' with a Terraform-address unscoped re-plan as the only blast-radius control.",
      "org/critical_paths/change_management/20260826T0008Z_globgrph-derive-runner-c2c3-compose_deploy_completion.md:79-84: ':latest REACHES FIVE TASK-DEFS ... all run this ONE image and pick up :latest on their next scheduled fire.'"
    ],
    "remedy": "Pin each task family to the image it was certified with -- a digest, or a per-purpose tag that only that family's deploy moves -- so one cell's rebuild cannot change another family's bytes; state the rule in the PRD's deploy section and require every image act's ledger line to name the tag's reach at that moment (it is seven families today, five on 08-26). The S28 rebuild is the first act under the rule: it must name all seven and read each one's next launch.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v3"},
    "closed": false
  }
]
```
