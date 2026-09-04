# NFRA_CLDGRPH -- surprise channel, ADJUDICATION v1 (round 3, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an
observation or a grade of the CVO's about the rows in `../investigations/`; a seat that contests one surfaces a new
investigation row citing it. A reader resolves an item's state from the newest row that cites it, across the two
documents.
**Coordinate:** every row here carries the CVO's allocator coordinate `NFRA_CLDGRPH-C-S<k>` (annex v3.3 @`e3e999c139`,
gate half @`6efb43b9d0`); `k` restarts at 1 in this document. This is the first live exercise of the coordinate on
either plane.
**Denominator at this write:** 7 rows (C-S1 .. C-S7; C-S7 appended 2026-09-04 ~18:5xZ: the CVO's own discriminating comparison for D6-AC4 taken before TO-CG-D-7, grading it PASS and dismissing S37; 6 rows (C-S1 .. C-S6; C-S6 appended 2026-09-04 ~07:35Z at round 4's first L9 read, adjudicating the issuer's S32 and S33; the investigation document then holds 32 rows, S1-S33 with S11 vacated, items open after that write: 0). At the round-3 slug: 5 rows (C-S1 .. C-S5). The investigation document holds 30 rows (S1-S31, S11 vacated)
after this commit; 5 were OPEN when the read began (S26, S27, S28, S29, S30), S31 is the CVO's own observation appended
in this commit under lane ANY, and all six are dispositioned below (C-S5 graduates S31). Items OPEN after this write: 0.
**Round 3 read (L8/L9):** all 8 task orders complete at HEAD. The three round-3 proof instances (C-1 @`028be96aef`,
C-2 @`1c0d13904e`, C-3 @`aea8346fe1`) carry invocation-form criteria only -- no judgment criterion this round, so no
`grades` entry is owed. Each instance's claims were read against the world at this seat with instruments other than
the assignee's: the S3 pointer and the 19:02:18 artifact prefix in `opal-313476888478-globgrph` (2 objects, 1,540 B
and 34,824,192 B, as C2-AC6 states; the pointer has since advanced through 2026-09-04T05:53:37Z, so the deployed
writer publishes on real stamps), ECS task definition `globgrph-projection-worker:3` ACTIVE, ECR digest
`68bd8b93…` tagged `latest`, `kuzu_nessie_load.py:460-476 @a38c0437eb` (the 3600 s default and its 835 s / 4.31x
derivation), `comp_aws_cli.py` at HEAD (UNREADABLE state at :101/:217/:227, declared second source and provenance at
:257-:341). Those reads are what advance the remediation clocks of S10, S20, S22, S23, S24 (REMEDIATION_v2.md) and
S2, S3, S8 (REMEDIATION_v1.md, remedied at the B-2 port and left OPEN by the round-2 record).

## C-S1 -- adjudicates S26: the user-bin shim hazard, GRADUATED; the DACL is rewritten on every provisioning run, so the remedy is at the writer

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S1",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "L9, round 3: ADJUDICATES S26 -- GRADUATED. The hazard is real and neither DACL repair persisted: S30 left 0 of 211 user-bin files inheritance-protected at 19:55Z on 09-03; at 06:05Z on 09-04, 105 of 211 are protected again, each carrying 2 DENY ACEs, and every one of the 211 files has LastWriteTimeUtc between 05:20Z and 05:22Z. The 105 are exactly the files the provisioner runs chmod +x on (96 extensionless bash forwarders, 8 .py, 1 .sh); the 105 .cmd twins written in the same seconds came back clean and inheriting. The writer is .tools/provision-path-shims.sh:207's chmod under MSYS, whose POSIX-mode emulation writes a protected explicit DACL; the remedy is at the provisioner, not a third icacls act.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Get-Acl over all 211 files of C:\\Users\\AndrewBerman\\bin at 2026-09-04T06:05Z (unscoped): inheritance-protected 105 of 211; DENY-bearing 105 of 211 (2 ACEs each); lacking an Andrew\\CodexSandboxUsers ALLOW 0 of 211. Protected by extension: '' 96, .py 8, .sh 1; every .cmd file (105) unprotected.",
        "LastWriteTimeUtc of the protected 105: oldest 2026-09-04T05:20Z, newest 05:22Z. Of the 106 clean files, 105 were written in the same window (comp-read.cmd 05:22:28Z; its bash forwarder comp-read 05:22:27Z). One act wrote both planes; one plane came back protected.",
        "The bash forwarder comp-read's DACL at 06:05Z, all eight ACEs explicit and none inherited: Deny NULL SID (REA,WEA,X,DC,RP); Deny AzureAD\\AndrewBerman ExecuteFile; Allow AzureAD\\AndrewBerman FullControl; Allow NT AUTHORITY\\SYSTEM, BUILTIN\\Administrators and Andrew\\CodexSandboxUsers (W,RX); Allow Everyone (X,RA,RP) -- the MSYS/Cygwin mode-emulation shape (an explicit DACL reconciling POSIX mode bits with deny ACEs), not an inherited one.",
        ".tools/provision-path-shims.sh at HEAD: :180 `cat > \"$BIN/$tool\"`, :207 `chmod +x \"$BIN/$tool\"`, :209 `cat > \"$BIN/$tool.cmd\"` with no chmod on the .cmd form -- the one operation that separates the protected population from the clean one is the chmod, applied to exactly the files that came back protected.",
        "S30 @8ae823ba17 post-state, its author's unscoped read at 2026-09-03T19:55Z: protected 0 of 211, DENY 0 of 211, lacking the CodexSandboxUsers ALLOW 0 of 211. Today's 105 are therefore a RECURRENCE inside eleven hours, the case S29's notes reserved for 'a runtime that re-writes deny ACEs' -- with the runtime now identified as the provisioner's own chmod, not the Codex sandbox (no Codex seat has run since Andrew's 'kill all the codex runtimes' at ~21:0xZ; 0.0.0_AB_MSTR 94059 read 5 claude.exe, the base seats, at 05:3xZ).",
        "The four .cmd shims TO-CG-C-3 names (comp-to, comp-read, comp-find, comp-which) at 06:05Z: protected False, inherited 6, DENY 0, CodexSandboxUsers ALLOW 1 each. The PowerShell/Codex plane is clean at this reading; the bash plane carries the deny ACEs (owner ExecuteFile denied on the forwarder, which bash does not consult). S30's acceptance gate -- a FRESH Codex seat through ajb2/start-codex-seat.ps1 -- is UNEXERCISED because no Codex seat exists; it is carried verbatim on S26's remediation row."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_CLDGRPH-S26"],
    "spec_asserts": "S26, S29 and S30 together assert that the hazard is a DACL state on the user-bin shims that an icacls act repairs (deny removal in S29, inheritance reset in S30), with a fresh Codex seat as the acceptance oracle.",
    "world_is": "The DACL state is REWRITTEN on every provisioning run by the provisioner's chmod +x under MSYS: S30's reset was undone for 105 of 211 files by a run at 05:20-05:22Z on 2026-09-04, and it will be undone again at the next run. A repair applied to the ACL cannot outlive the next write; the durable remedy is at the writer (restore inheritance after the write, or write without mode emulation), after which S30's fresh-seat gate is the acceptance.",
    "notes": "Graduated rather than dismissed although the Codex population is empty today: the provisioner runs at every seat load that reads WARN (CLAUDE.md Git section), so the state re-arms on its own and any future Codex launch inherits it. The seat that ran the provisioner at 05:20Z is not identified here and does not need to be -- the mechanism is. Remediation row: REMEDIATION_v3.md S26 (owner 1.0.0_SA_CTO, the launcher/provisioner owner per 2.0.0_SA_COO ruling 93885)."
  }
]
```

## C-S2 -- adjudicates S29 and S30: the disarm-evidence and correction records of S26, DISMISSED_WITH_REASON; their substance lives on S26's remediation row

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S2",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "L9, round 3: ADJUDICATES S29 and S30 -- DISMISSED_WITH_REASON. Both are records of the disarm owner's repair attempts on S26 (S29 the deny removal, S30 its author's correction and the inheritance reset), not items of their own; S29's current-world clauses were retracted by S30, and S30's remedy, its three-axis post-state and its acceptance gate are carried forward on S26's remediation row, where the state lives.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S29 @caa263b610 and S30 @8ae823ba17 read in full at this seat; S30 refutes S29's 'the residual NULL SID DENY sits on every file including the working control' by the .cmd-plane Get-Acl counts (comp-which.cmd 0, the three failing shims 1 each) and by 0.7.0_AE_CloudOps~S's agent-side execution after the deny removal (still denied), and S29's author concedes both in S30.",
        "Neither row names a hazard distinct from S26's: S29's one_line is 'S26's user-bin deny ACEs are FIXED IN THE WORLD'; S30's is 'CORRECTION to S29'. One hazard, three rows; the channel's law is one carrier per quantity, so the two records close and the item (S26) carries the remedy.",
        "C-S1 above adds what neither record could see: the repair does not persist because the provisioner rewrites the DACL. S30's acceptance gate is adopted verbatim into S26's remediation row so that dismissing the record does not lose the bar."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S29 and S30 are the disarm owner's evidence and correction records for S26's remedy, not items: S29's world claims are retracted by S30 (same author), and S30's inheritance-reset remedy, its 0-of-211 three-axis post-state and its fresh-Codex-seat acceptance gate are carried verbatim on S26's remediation row (REMEDIATION_v3.md). Closing the records keeps one carrier for one hazard; nothing in them is lost and nothing is asserted repaired.",
    "adjudicates": ["NFRA_CLDGRPH-S29", "NFRA_CLDGRPH-S30"],
    "spec_asserts": "The channel's item census counts each investigation row as an item to be dispositioned (spine v3.2 L9), so S29 and S30 each need a disposition even though neither names a new hazard.",
    "world_is": "Both rows describe attempts on S26's hazard by S26's disarm owner; the attempts did not close it (S30 says so of S29; C-S1 measures that S30's own reset did not persist). Their content is preserved on the remediation plane and the two investigation items close as records."
  }
]
```

## C-S3 -- adjudicates S27: cot-pipeline is EventBridge-only where the cell text says Lambda, GRADUATED; the fix is a text correction at the recut

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S3",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "L9, round 3: ADJUDICATES S27 -- GRADUATED. The cell text (decomp CG-s-14, line 77) and TO-CG-C-3's measured-defect paragraph name bd-pipeline, cot-pipeline and inf-pipeline as aws_s3_bucket_notification resources with Lambda targets; cot-pipeline's resource is EventBridge-only in HCL (s3-notifications.tf:16-19, read at this seat) and in resolved state, the deriver correctly derives no cot Lambda edge, and C3-AC3 was met on three bd targets. A reader of the cell text who expects a cot edge will read a correct derivation as a defect; the remedy is the text, owned at the recut.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/s3-notifications.tf at HEAD, all 19 lines read at this seat: one resource aws_s3_bucket_notification.cot_data with bucket and eventbridge = true; zero lambda_function blocks. The file header says why: the ADVI_COTETL chain-fix of 2026-06-11 delivers sentinels to EventBridge rules in eventbridge.tf.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md at HEAD: exactly 1 whole-value hit for 'cot-pipeline' across 190 lines, at line 77, the CG-s-14 cell row -- the durable carrier of the claim (the task-order face is terminal and is not edited).",
        "C-3 proof instance @aea8346fe1, C3-AC3: three bd-pipeline Lambda targets derived non-zero with provenance both (bd-allocation-processor, bd-gold-trigger, bd-silver-merge); the criterion's 'three declared targets' arm was satisfiable without cot because bd alone declares three. The worker's row S27 and its own evidence (the deriver's tfstate read: eventbridge=true, lambda_function=[]) agree with this seat's HCL read."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_CLDGRPH-S27"],
    "spec_asserts": "Decomp cell CG-s-14 (line 77) and TO-CG-C-3 THE CELL: the estate declares real aws_s3_bucket_notification resources with Lambda targets in bd-pipeline, cot-pipeline and inf-pipeline; DELIVERABLE 4(a): the three declared targets derive non-zero.",
    "world_is": "bd-pipeline and inf-pipeline declare Lambda notification targets; cot-pipeline declares an EventBridge-only notification (a different target class). The deriver's output is right; the cell text is wrong about one of three named resources.",
    "notes": "Remediation row: REMEDIATION_v3.md S27, owner 2.0.0_SA_COO~A at the L5/L6 recut: the CG-s-14 text and any successor face name bd and inf as the Lambda-target resources and cot as EventBridge-only. No Terraform change belongs to this item (the worker said so and this seat agrees)."
  }
]
```

## C-S4 -- adjudicates S28: the C-3 fix has not reached the cloud deriver, GRADUATED and MEASURED -- the shared image was last pushed 21 minutes BEFORE the fix commit

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S4",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "L9, round 3: ADJUDICATES S28 -- GRADUATED, and the row's conditional ('cloud runtime application requires a separately routed image rebuild') is now a measured fact: ECR opal-globgrph-derive-runner:latest is digest 68bd8b93…, pushed 2026-09-03T18:51:14Z by C-2's build; the C-3 fix b5bc1c8b27 was authored 2026-09-03T19:12:54Z and is an ancestor of HEAD; so every task on the tag -- globgrph-derive-runner:6 included -- runs comp_aws_cli.py from before the fix, and S20's zero-by-silence hazard is still live in the cloud. The rebuild is a change-managed deploy to eight families, not five.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ECR describe-images opal-globgrph-derive-runner at 2026-09-04T06:0xZ, newest four: sha256:68bd8b93… tags [latest, 20260903-185059] pushed epoch 1788461474 (2026-09-03T18:51:14Z); sha256:68c822ff… tag 20260903-183958; sha256:1e1aaa14… tag 20260903-162203; sha256:3a4e078d… tag 20260903-143221. No image pushed after 18:51:14Z.",
        "git log b5bc1c8b27: 2026-09-03T15:12:54-04:00 (19:12:54Z), author 0.8.0_AE_CloudComp~O, 'NFRA_CLDGRPH: preserve S3 notification read state'; merge-base --is-ancestor b5bc1c8b27 HEAD: YES. The fix post-dates the last image push by 21 minutes 40 seconds.",
        "ECS ACTIVE task-definition families containing 'globgrph', latest revision's image, read at this seat: globgrph-derive-runner:6, globgrph-comp-learns-producer:1, globgrph-cse-producer:1, globgrph-fedobs-producer:1, globgrph-resource-summaries-producer:1, globgrph-projection-worker:3 and globgrph-serving:1 all reference …/opal-globgrph-derive-runner:latest (7 families); globgrph-nessie:5 and globgrph-trino:6 reference vendor images. The ledger S28 cites (org/critical_paths/change_management/20260826T0008Z_…:79-84) counted five consumers on 08-26; the tag reaches seven task families today.",
        "C-3 proof instance @aea8346fe1, C3-AC5: 'a shared-image rebuild is required and was routed as NFRA_CLDGRPH-S28' -- the worker answered the runtime question on the record as its criterion required; this row confirms the answer against ECR and ECS rather than the Dockerfile."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_CLDGRPH-S28"],
    "spec_asserts": "TO-CG-C-3 item 3 (THE ENGINE, NOT A COPY): the fix lands in the deriver the derive runner runs, and 'the derive runner's next real run publishes the honest' read state; C3-AC5 requires the runtime question answered and routed as a row if an act outside the cell is needed.",
    "world_is": "The derive runner's next real run publishes NOTHING new: its task definition pulls :latest, and :latest was built 21 minutes before the fix. The honest read state exists in source at HEAD and in no running container. S20's remediation is REMEDIATED in code and its disarm stays ARMED until the rebuilt image runs one real derive.",
    "notes": "Remediation row: REMEDIATION_v3.md S28, owner 2.0.0_SA_COO~A: the rebuild through change management with every family on the tag named and its next launch read, then one real cloud derive showing the read/unreadable denominator and non-zero bd TRIGGERS -- that run disarms S20 as well. See C-S5 for the tag itself."
  }
]
```

## C-S5 -- the CVO's own observation: the shared `:latest` tag was moved twice on 09-03 for every family on it, while each face bounded its blast radius to the worker -- GRADUATED

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S5",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "L9, round 3: ADJUDICATES S31 (this seat's own row, appended to the investigation document under lane ANY because a remediation row carries its item's id and the C- coordinate lives only here) -- GRADUATED. Surfaced while adjudicating S28: TO-CG-B-2 and TO-CG-C-2 each rebuilt 'the worker image' and each build re-tagged opal-globgrph-derive-runner:latest (16:22Z digest 1e1aaa14…, 18:51Z digest 68bd8b93…), the one tag seven ACTIVE task families pull -- so each worker-scoped act was a deploy to the derive runner, four producers and the serving service at their next launch. Both faces' NEVER-2 ledgers and unscoped re-plans were Terraform-address censuses, which cannot see an image-tag move. Nothing broke that this seat can measure; the class is a deploy whose blast radius its own controls cannot observe.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ECR image list at this seat (C-S4 evidence 1): the 16:22:17Z image (1e1aaa14…) is the digest B2-AC2 cites for revision 2; the 18:51:14Z image (68bd8b93…) is the digest C2-AC3 cites for revision 3 and it carries the latest tag today; the 16:22 image no longer does -- latest moved between them.",
        "ECS at this seat (C-S4 evidence 3): globgrph-projection-worker:3 references …/opal-globgrph-derive-runner:latest, not a digest and not a worker-specific tag; six other ACTIVE families reference the same string, including globgrph-serving:1 (C-1's service) and globgrph-derive-runner:6.",
        "TO-CG-C-2 item 2 (face at HEAD): 'rebuild the worker image from HEAD of infra/aws/globgrph/ (the derive-runner image pattern), register task-definition revision 3, re-target the Pipe; Terraform for every resource, safe-apply -target'; C2-AC3's unscoped re-plan is 'quoted by address list = the four foreign items and none of this cell's' -- a Terraform-plane control; the image tag is an ECR-plane act no plan sees.",
        "org/critical_paths/change_management/20260826T0008Z_globgrph-derive-runner-c2c3-compose_deploy_completion.md:79-84 states the class in its own words for the 08-26 deploy: ':latest REACHES FIVE TASK-DEFS … all run this ONE image and pick up :latest on their next scheduled fire'. The two round-2/round-3 rebuilds inherited that reach without restating it."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_CLDGRPH-S31"],
    "spec_asserts": "TO-CG-B-2 and TO-CG-C-2 scope their image act to 'the worker image' with a Terraform-address blast-radius control (targeted apply, one unscoped re-plan quoted by address list) and a NEVER-2 ledger for the worker's resources.",
    "world_is": "The worker has no image of its own: it runs the shared derive-runner image by its :latest tag, and each rebuild re-pointed that tag for seven task families. The controls the faces carried were on the wrong plane to see it. The 08-26 ledger named the class; the round-2 and round-3 faces did not carry it forward.",
    "notes": "Remediation row: REMEDIATION_v3.md S31, owner 1.0.0_SA_CTO (the deploy discipline belongs to the PRD/architecture, not to a cell): pin each family to the image it was certified with (a digest or a per-purpose tag) so one cell's rebuild cannot move another family's bytes, and carry the tag's reach in every image act's ledger line. Not routed as a defect of B-2 or C-2 -- both did what their faces said; the faces were written against an image topology that does not exist."
  }
]
```

## Clock advances this round -- the evidence, kept here because a remediation row's own bytes may only move its three clocks

The row gate admits an in-place advance of `disarm`, `remediation` and `closed` and nothing else (exercised at this
commit's first attempt: eight rows refused for an appended evidence line and a changed `round`). The evidence for each
advance therefore lives in this document, read at this seat with instruments other than the assignee's.

| Row | Advance | Evidence (this seat's read) |
|---|---|---|
| S2 (REMEDIATION_v1) | DISARMED 2026-09-03T17:56Z; REMEDIATED; closed | B-2 proof @`ebe85fd69e` B2-AC4 "S2 + S3 + S8 FIXED HERE"; at HEAD `kuzu_incremental_refresh.py:29-33` states ENABLED BY DEFAULT once, in agreement with `_canonical.py:450` and the 2026-07-08 KUZUSPLIT GO, the sentence-versus-parenthetical contradiction gone, the block marked "S2 -- FIXED AT THE PORT". Exercised by B2-AC6's cloud runs on both paths. |
| S3 (REMEDIATION_v1) | DISARMED 2026-09-03T17:56Z; REMEDIATED; closed | At HEAD `kuzu_nessie_load.py:337 def _lock_path_for(db_path)`, `:369`/`:493` key `_LOCK_PATH` to the target database, `:487` "PER-DATABASE (see _lock_path_for)", `:494` prints SINGLETON_SCOPE per-database -- the decision written and executed; the cloud worker inherits it (B2-AC6 real stamps). |
| S8 (REMEDIATION_v1) | DISARMED 2026-09-03T17:56Z; REMEDIATED; closed | At HEAD `kuzu_nessie_load.py:267 edge_count=edges_stored` with `:232-236` stating ONE semantics across both producers ("EDGES STORED IN THE ARTIFACT, never writes attempted"); exercised by B2-AC6 (direct counts equal) and C2-AC6 (counts equal to direct COUNT(*) on a real incremental stamp). **The second-order question the remedy reserved -- why the source carried about 2,256 duplicate edge identities -- is NOT answered by any row and goes to the CTO in the round-3 slug.** |
| S10 (REMEDIATION_v2) | DISARMED 2026-09-03T19:16Z; REMEDIATED; closed | `git show a38c0437eb:infra/aws/globgrph/kuzu_nessie_load.py` `:460-476`: default 3600 s derived from the slowest accepted cloud full of 835 s (4.31x, 2,765 s spare), comment corrected; C2-AC2: the inheriting local caller and revision-3 ECS task `bd842c7582` both printed `KUZU_REBUILD_DEADLINE_S=3600 source=measured-default`; the 3600 s task override preserved. |
| S20 (REMEDIATION_v2) | REMEDIATED only; disarm stays ARMED; open | Source at HEAD (`comp_aws_cli.py`): UNREADABLE state `:101/:206/:217/:227`, declared second source and provenance `:242-:343`, disagreement classes `:325-:331` (b5bc1c8b27 is an ancestor of HEAD); C3-AC3 live derive 34 read / 0 unreadable, 188 TRIGGERS, three bd targets non-zero; C3-AC4 planted denial moved the denominator 0 to 1. **NOT DISARMED:** the cloud derive runner pulls `opal-globgrph-derive-runner:latest`, pushed 2026-09-03T18:51:14Z, 21 minutes before the fix commit (C-S4) -- the running container still collapses a failed read to zero. Disarms with S28's rebuild and one real cloud derive. |
| S22 (REMEDIATION_v2) | DISARMED 2026-09-03T19:16Z; REMEDIATED; closed | C2-AC1 conditional creation `projection_worker.py:163-224 @a38c0437eb`; C2-AC5 on the running revision-3 image: task `842093d9` POINTER_NOOP status=already_current with pointer ETag/LastModified unchanged, task `fd3d9ea9` non-identical bytes REFUSED. World at this seat: the pointer has advanced through 2026-09-04T05:53:37Z on real stamps with the 19:02:18 prefix intact. |
| S23 (REMEDIATION_v2) | DISARMED 2026-09-03T19:16Z; REMEDIATED; closed | C2-AC4: one authentic strictly-forward advance by the DEPLOYED writer (CloudTrail `675113f0` -> Lambda `ce77d595` -> Pipe `358ac19b` -> task `f8b288ad`; POINTER_VERIFY_OK before POINTER_PUT_OK; 17:01:08 -> 19:02:18), the prior pointer never undone. World at this seat: `projection/current.json` names vintage 2026-09-04T05:53:37.689093+00:00, manifest_sha256 `44388b21…`; every prefix since 19:02:18 later than the one before it. |
| S24 (REMEDIATION_v2) | DISARMED 2026-09-03T19:16Z; REMEDIATED; closed | C2-AC1: the cross-mode byte band removed, direct counts `:344-367`, exact remote set/size/hash/count readback `:370-407 @a38c0437eb`; C2-AC6 on a real incremental stamp: 83,615,744 compacted to 34,824,192 bytes, counts equal to direct COUNT(*). World at this seat: `s3://opal-313476888478-globgrph/projection/2026-09-03T19:02:18.412096+00:00/` holds exactly 2 objects, 1,540 B and 34,824,192 B, LastModified 19:02:49Z. |

Disarm vintages are the proof-instance commits that exercised the remedy (B-2 @`ebe85fd69e` 2026-09-03T17:56:48Z;
C-2 @`1c0d13904e` 2026-09-03T19:16:44Z), not this write's clock. `remediation.round` on the advanced rows stays as
written (v1 / v2) because the gate's in-place rule moves clocks only; the round that remedied each is named above.

## C-S6 -- adjudicates S32 and S33: the issuer's disarm ack on S27 and its route on S28, DISMISSED_WITH_REASON as records; S27's clocks close, S26's remediation clock advances

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S6",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T07:35Z",
    "one_line": "L9, round 4 (as rows land): ADJUDICATES S32 and S33 (2.0.0_SA_COO~A, 07:05Z) -- DISMISSED_WITH_REASON, both records rather than items. S32 is the disarm act on S27: decomposition v0.3 @eedb24b906's CG-s-14 row now names cot-pipeline's resource as eventbridge = true with the tf citation (read at this seat: the cot-pipeline hits in the decomp are the corrected text), so S27's remediation row reads REMEDIATED and DISARMED at that vintage, closed. S33 is the route on S28: cell CG-s-15 under TO-CG-D-1 to worker slot 1, with the three families pinned by digest and one real cloud derive -- S28 and S20 stay ARMED until that instance reads VALID. Separately, S26's remediation reads REMEDIATED on 1.0.0_SA_CTO's provisioner fix @e4167f3c3b (this seat's unscoped read at 07:18Z after a 07:09Z provisioning run: protected 0 of 211, DENY 0 of 211), disarm still ARMED on S30's fresh-Codex gate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_CLDGRPH_DECOMP.md at HEAD @eedb24b906 (2.0.0_SA_COO~A, 2026-09-04T07:20Z): comp-read --enumerate 'cot-pipeline|eventbridge' -> 5 hits across 196 lines, line 79 (the CG-s-14 row) carrying `infra/aws/terraform/cot-pipeline/s3-notifications.tf:16-19` and `eventbridge`, line 196 the 0.3 changelog row adding CG-s-15 -- the correction S27's remedy asked for, at the durable carrier.",
        "S32 @HEAD (2.0.0_SA_COO~A): 'A factual disarm ack, not an adjudication: no adjudicates field; the DISARMED state on the remediation plane is the CVO's flip citing this row' -- read as written; the flip is in REMEDIATION_v3.md S27 in this commit.",
        "S33 @HEAD (2.0.0_SA_COO~A): TO-CG-D-1 (CG-s-15) issued to 0.9.0_WK_NFRA_CLDGRPH~1 with D1-AC1..AC8 (the moved digest, the build, the three pins, the cloud denominator line, TRIGGERS > 0, the serving deployment COMPLETED); consumer count corrected to seven; 'S28's hazard stays ARMED until that proof reads VALID -- this row is the ROUTE, not the disarm' -- agreed; no clock moves on S28, S20 or S31 in this commit.",
        "S26: 1.0.0_SA_CTO 94118 -- .tools/provision-path-shims.sh @e4167f3c3b adds _restore_inheritance (MSYS_NO_PATHCONV=1 icacls <win path> /reset after each chmod, :91-98 at HEAD read here) and a DACL read at the end of every run; the CTO's exercise: before 104 of 211 protected, after 0 of 211 on two instruments. This seat's own instrument at 07:18:11Z, unscoped Get-Acl over 211 files after the 07:09:13Z provisioning run: inheritance-protected 0, DENY-bearing 0 -- the fix survived a run, which is the property C-S1 named. Disarm stays ARMED: S30's gate (a fresh Codex seat) is still unexercisable, a carried call to Andrew."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S32 and S33 are the issuer's acknowledgement and routing records on items already graduated (S27, S28); their content moves clocks on the remediation plane (S27 closed in this commit; S28 waits on D-1) and opens nothing. One carrier per hazard: the items stay S27 and S28, the records close.",
    "adjudicates": ["NFRA_CLDGRPH-S32", "NFRA_CLDGRPH-S33"],
    "spec_asserts": "Spine v3.2 L9: the census counts the investigation document's rows as items and reads the adjudication document for their dispositions, so an issuer's ack row needs a disposition even when it names no new hazard.",
    "world_is": "Both rows describe acts on graduated items by their named owners; the acts are verified here (the decomp text, the provisioner source, the ACL state) and the clocks move where the evidence reaches: S27 closed, S26 remediated-not-disarmed, S28/S20/S31 unchanged until D-1's instance.",
    "notes": "Round 4 of NFRA_CLDGRPH is now open under 2.0.0_SA_COO~A's issuance (TO-CG-D-1 and the CG-x cells); this seat reads rows as they land and slugs once when every order of the round is terminal and every item dispositioned."
  }
]
```

## C-S7 -- adjudicates S37 and GRADES D6-AC4: the discriminating comparison TAKEN at this seat before TO-CG-D-7 -- the laptop's full-loader build and the cloud's incremental artifact of ONE Nessie snapshot are identical on three digests; D6-AC4 PASS; S37 DISMISSED_WITH_REASON (its ask is done)

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S7",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T18:50Z",
    "one_line": "L9, round 4 (as rows land): ADJUDICATES S37 (2.0.0_SA_COO~A: after CG-s-6 both halves of D6-AC4's pair are thin clients of one server, so the pair cannot fail, and the discriminating comparison becomes UNTAKEABLE when TO-CG-D-7 retires the local copy) -- the CVO took the discriminating comparison itself, before D-7 is handed, as the L9 exercise: the laptop's LOCAL canonical graph (built by the full loader at 07:13:17Z from Nessie snapshot nodes 92487625797322719 / edges 6541343322795706185) against the SERVED projection artifact of the SAME snapshot (s3://opal-313476888478-globgrph/projection/2026-09-04T05:53:37.689093+00:00/kuzu_nessie_db, built by the cloud incremental_updater at 05:54:06Z), both opened read-only with kuzu 0.11.3, the same Cypher on both plus a digest over every node id and every edge triple: node_type histogram 58 rows / 27,244 nodes IDENTICAL; node id set 27,244 IDENTICAL; edge triple set 58,622 IDENTICAL (sha256 5814576cbfa59347.., 59b70b3bce7f0056.., 9065ec87690ede61.. on both sides). Two builders, one snapshot, a comparison that could fail and did not. D6-AC4 graded PASS below; S37 DISMISSED_WITH_REASON: its ask is done and the window question is moot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Local manifest infra/aws/globgrph/kuzu_nessie_db._build_manifest.json at 18:3xZ: built_at 2026-09-04T07:13:17Z, node_count 27244, edge_count 58622, source_vintage nodes_snapshot_id 92487625797322719, edges_snapshot_id 6541343322795706185, nodes_metadata_last_modified 2026-09-04T05:53:37.689093+00:00 -- the laptop's full loader (kuzu_nessie_load.py, mode full).",
        "Served manifest projection/2026-09-04T05:53:37.689093+00:00/_build_manifest.json (1,536 B, fetched by s3api get-object): committed_at 2026-09-04T05:53:37.689093+00:00, built_at 05:54:06.928866Z, producer.mode incremental, writer_id incremental_updater, engine kuzu 0.11.3, nodes_snapshot_id 92487625797322719, edges_snapshot_id 6541343322795706185, node_count 27244, edge_count 58622, artifact 34,832,384 B (the artifact fetched whole, 34,832,384 B on disk).",
        "The comparison at this seat (python kuzu 0.11.3, both databases opened read_only=True, 0.7 s): Q1 MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC, t -> 58 rows / 27,244 nodes on both, row-array sha256 equal; Q2 MATCH (n:CloudNode) RETURN n.node_id ORDER BY node_id -> 27,244 ids on both, sha256 equal; Q3 MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) RETURN a.node_id, b.node_id, e.edge_type ORDER BY all -> 58,622 triples on both, sha256 equal. The comparison could fail: the two artifacts were built by different engines' modes (full vs incremental) on different machines; a divergence in either would have moved a digest.",
        "Why this is the discriminating pair S37 asked for and the worker's pair was not: the worker's D6-AC4 half (0.9.0_WK_NFRA_CLDGRPH~2, 27,295 nodes at vintage 16:38:39Z) and the issuer's laptop half read ONE served artifact through one transport (S37's own measurement: kuzu_cli.py at HEAD carries 5 projection_client references and 0 local-reader references), so they agree by construction; this seat's pair reads the LOCAL canonical build directly (the retiring copy, 217,927,680 B on disk) against the served artifact of the same snapshot, which is the equivalence FWD-5's author was reaching for -- taken while the local copy exists, which TO-CG-D-7 (still `pending` at this write) ends.",
        "Bound stated: this seat's comparison is at snapshot 05:53:37Z, not the worker's 16:38:39Z vintage; the property graded (the served projection is faithful to an independent full build of the same snapshot) is per-snapshot and was exercised once on a real one; a second vintage would add coverage, not discrimination, and would need a local full rebuild that this seat does not run. The served artifact's mode being `incremental` also exercises, at a second vintage, S24's remediation (an incremental artifact equal to a full build) and S8's (edge_count 58,622 on both manifests equals the direct count on both databases)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S37's ask -- rule whether the discriminating comparison should be taken while it still exists, and if so take it before TO-CG-D-7 -- is answered by taking it: the CVO ran the local-build-versus-served-artifact comparison at one snapshot and it passed on three digests; the grade lives in this row's `grades`; nothing remains to remediate, the window question is moot, and TO-CG-D-7 may be handed on the issuer's own schedule. The related observation (a control that cannot fail is not evidence; the cell text's laptop limb changed meaning under CG-s-6) is recorded for the round-4 analysis, where the CTO reads it; the bar is not changed mid-round.",
    "adjudicates": ["NFRA_CLDGRPH-S37"],
    "grades": [
      {
        "criterion": "D6-AC4",
        "instance": "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-6.close-fwd5-fresh-machine.proof_of_spec.json@dbb7d0a4fd",
        "verdict": "PASS",
        "reason": "The bar (CG-x-5 / FWD-5: a machine that has never held the database asks and gets the SAME ANSWER as everyone else on its first try; D6-AC4: the fresh machine's answer beside the laptop seat's for the identical Cypher, graded by the CVO): the recorded pair is identical (58 rows, 27,295 CloudNodes, the same normalised digest on both, at vintage 2026-09-04T16:38:39.485910Z) and certifies the transport; the equivalence limb -- that the served answer is the answer a reader of the canonical graph would get -- was supplied by this seat's own comparison of the LOCAL full-loader build against the SERVED artifact of one snapshot, identical on the node_type histogram, the full node id set and the full edge set. Both limbs met; the worker's half correctly carried no verdict."
      }
    ],
    "spec_asserts": "CG-x-5 closes on the absence of the local DB proven before the ask, then the answer, then the SAME ANSWER AS A LAPTOP SEAT for the same question; TO-CG-D-6 makes the second half the issuer's at the drain and D6-AC4 the CVO's grade (judgment=true).",
    "world_is": "After CG-s-6 the recorded pair is two clients of one server and agrees by construction; the discriminating equivalence -- an independent local full build against the served artifact of the same snapshot -- was still takeable today and this seat took it: identical on three digests. FWD-5's outcome (one answer for everyone) holds on evidence that could have failed.",
    "notes": "Recorded here rather than routed: the CVO reads and exercises; it did not rebuild anything, delete anything or touch the mutex directory (S39's dead lock dir is still present beside a graph that rebuilt successfully at 07:13Z, which is a fact for CG-s-8's worker). The scratch outputs of the comparison are not durable; the digests and denominators in this row are the record."
  }
]
```
