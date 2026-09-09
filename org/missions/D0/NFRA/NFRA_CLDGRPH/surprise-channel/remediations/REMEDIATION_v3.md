# NFRA_CLDGRPH -- surprise channel, REMEDIATION v3 (round 3, laptop fabric)

**Home:** the project tree's remediation document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED item, keyed by the item's id; the clocks (`disarm`, `remediation`,
`closed`) advance in place and only forward. Form: spine v3 -- no route token; the CTO routes every round from the slug.
**Denominator at this write:** 9 rows -- round 5 close (2026-09-09 ~17:3xZ): S31 clocks advanced in place to DISARMED / REMEDIATED / closed on C-S29's live read (7 of 7 globgrph families by digest after TO-CG-E-2, the :latest digest unchanged), PRD v0.5 R13 (no family references a mutable tag) and CLAUDE.md's NEVER-2 clause (an image act names every family the tag reaches); S26 stays open on its Codex-seat acceptance; S34, S35, S53 OPEN at the CTO; round 4 L9 (2026-09-09 ~15:0xZ): S26 clocks advanced in place (DISARMED on this seat's unscoped DACL read after a fresh provisioning run, 211 files / 0 protected / 0 deny; REMEDIATED at the writer @e4167f3c3b; closed false pending the fresh-Codex-seat acceptance, which waits on Andrew's Codex word); S31 untouched (pins 3 of 7 measured, recorded at C-S24); S36 and S57 minted REMEDIATED and closed; S34, S35, S53 minted OPEN (owner 1.0.0_SA_CTO). Round 3 at its write: 4 rows (S26, S27, S28, S31), all OPEN. The graduations are recorded in
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
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-09T15:03Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
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
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~A", "at": "2026-09-04T07:20Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v3"},
    "closed": true
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
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~A", "at": "2026-09-04T17:05Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v3"},
    "closed": true
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
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-09T17:30Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": true
  }
]
```

## S36 -- safe-merge aborted on the conflict every concurrent drain produces; the --continue limb landed; closed

```json
[
  {
    "id": "NFRA_CLDGRPH-S36",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "safe-merge.sh refused and ABORTED on a conflict (:82-85), so a conflicted drain had to be finished with a raw git merge that carried neither the index guard nor the row gate; on an append-only channel every concurrent drain conflicts, so the abort path was the drain path (3 of 3 in round 4).",
    "evidence": [
      "S36 (2.0.0_SA_COO~A, 09-04 15:10Z) with its measured 3 of 3.",
      "@afa47031ed (1.0.0_SA_CTO, 09-04 15:27Z): 'fix(safe-merge.sh): the --continue limb NFRA_CLDGRPH-S36 asked for -- a CONFLICT no longer aborts past the index guard'; comp-read --enumerate 'continue' -> 29 hits at HEAD; CLAUDE.md 14b names the limb."
    ],
    "remedy": "EXECUTED: the --continue limb keeps a conflicted drain inside the guards.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-04T15:27Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": true
  }
]
```

## S57 -- behind.sh silenced the reads its verdict rested on; READ_FAILED is a third outcome; closed

```json
[
  {
    "id": "NFRA_CLDGRPH-S57",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "behind.sh silenced stderr on both S3 reads its verdict rested on, so BEHIND_CAUGHT=false was emitted identically by a not-behind world and by two failed reads.",
    "evidence": [
      "S57 (2.0.0_SA_COO~A, 09-05 10:05Z).",
      "S58 (the owner's ack, 09-05 15:30Z): at HEAD after the pass-3 drain the two reads capture stderr and rc; READ_FAILED x12, read_ok x22, READS_OK x6, UNREAD x7; the third outcome proven to print; D9-AC4 graded on it at C-S12."
    ],
    "remedy": "EXECUTED: the reads fail loud and READ_FAILED is a third outcome distinct from both verdicts.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v4",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~A",
      "at": "2026-09-05T15:30Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~A",
      "round": "v4"
    },
    "closed": true
  }
]
```

## S34 -- the drain destroys a worker's untracked NEVER-2 sentinel; OPEN

```json
[
  {
    "id": "NFRA_CLDGRPH-S34",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "deploy_ledger.py open writes the machine SENTINEL org/critical_paths/.open_deploys/<slug>.json as a side-effect file; a worker commits the change_management rendering and the sentinel stays untracked in its worktree; the drain's git worktree remove deletes the only input the gate reads (2 of 3 sentinels lost in round 4, alive only because the issuer hand-captured them).",
    "evidence": [
      "S34 (2.0.0_SA_COO~A, 09-04 12:55Z) with the measured 4 of 4 -> 6 of 6 sentinel scan after re-homing.",
      "safe-merge.sh at HEAD: comp-read --enumerate 'open_deploys|sentinel' -> 0 hits; no drain-side capture exists. S45 records the mitigation taken this round (every NEVER-2 face names .open_deploys/ in <paths>) -- a face convention, not a mechanism."
    ],
    "remedy": "A mechanism at the drain or the tool: the drain reads a worktree's untracked .open_deploys/*.json before removing it (or safe-merge refuses a drain whose worktree holds one), or deploy_ledger.py open stages the sentinel with the entry it writes; disarm on one worker deploy whose sentinel survives a drain without a hand capture.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": false
  }
]
```

## S35 -- a swept seat cannot tell it was swept; the residue crosses under another author; OPEN

```json
[
  {
    "id": "NFRA_CLDGRPH-S35",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "When git commit --only is refused during another seat's merge, safe-commit has already staged the file and returns rc 128 (the nothing-landed family); the residue sits in the shared index until the next drain commits it under the draining seat's authorship, and nothing announces it (measured: the CTO's ratification record committed by 2.0.0_SA_COO~A in b687429234).",
    "evidence": [
      "S35 (1.0.0_SA_CTO, 09-04 17:28Z).",
      "CLAUDE.md 14b at HEAD prescribes a linked worktree for anything bigger than a one-file edit while other seats are live -- a discipline that avoids the race, not a mechanism that detects the sweep."
    ],
    "remedy": "A mechanism: safe-commit un-stages its own pathspec on a refused commit (or prints the staged residue with the rc so the seat knows), and safe-merge refuses a drain whose index carries a file staged by another seat (its :73-79 guard, extended to the --continue path); disarm on one refused commit leaving nothing staged, measured.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": false
  }
]
```

## S53 -- two of four manifest producers still stamp merge attempts as edge_count; OPEN

```json
[
  {
    "id": "NFRA_CLDGRPH-S53",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Four modules write _build_manifest through _provenance.write_manifest and only two carry stored-count semantics after S8's fix: kuzu_load.py:278 stamps edge_count=loaded and kuzu_stitch_load.py:124 stamps edge_count=written (MERGE executions), and the manifest carries no field saying which.",
    "evidence": [
      "S53 (2.0.0_SA_COO~A, 09-05 08:12Z); S52 (S8's fix scoped to kuzu_nessie_load.py by name).",
      "No commit on kuzu_load.py or kuzu_stitch_load.py since S53 at HEAD (git log on the paths, this seat)."
    ],
    "remedy": "Either the two siblings stamp a post-load COUNT(*), or the manifest carries the producer's semantics in a field a consumer can reject on (CLAUDE.md: a value must carry its claim) -- the stronger fix; disarm on the manifest field landing or both siblings counting stored edges, with one manifest of each producer read.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": false
  }
]
```
