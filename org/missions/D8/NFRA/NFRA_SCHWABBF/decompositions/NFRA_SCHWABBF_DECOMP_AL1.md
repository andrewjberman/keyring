# NFRA_SCHWABBF decomposition -- ALONGSIDE WORKSTREAM, round 1 (2026-10-20, issuer 2.0.0_SA_COO~SA): the Alongside Schwab Box, built as text

Workstream `alongside (FWD-8, C-ALONGSIDE)` of NFRA_SCHWABBF, seated by `0.0.0_AB_MSTR` msg 109918 on `1.0.0_SA_CTO` msg 109917; `project.json` `workstreams` names this lane. It shares NO write surface with `2.0.0_SA_COO~SB`'s
cutover workstream (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`, which is FROZEN for its round; this file does not touch it). One issuer per workstream (spine L6).
Authority: PRD v0.5 @159c2a410f, ratified-text half SIGNED by `3.0.0_SA_CVO` at current bytes (`python .tools/prd-signoff.py status NFRA_SCHWABBF` read 2026-10-20 ~15:4xZ: ADMITTED).
The CTO's round-1 analysis ruling 4 held this workstream for that re-sign; the re-sign has landed.

**Andrew-direct words carried into every face (verbatim):** ~13:5xZ 2026-10-20, "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box";
"I will need to RDP into the EC2 box most likely to get that done". ~14:3xZ, "schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts", "abiding by the path structure that already exists in that bucket"
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_143xZ_SCHWABBF_FWD8_CONFIRMED_BUILD_VENDOR_FIRM_PATHS.md`).

## What round 1 of this workstream is

FWD-8's thread is: box exists -> a person signs the SI2 app in -> the login's entitlement list is read -> ONE Cottonwood day is pulled, stored at `address('schwab','cottonwood','bronze',...)` and read -> then the history to Schwab's floor.
Round 1 builds the repo side of every hop that needs no person and no AWS write: the Terraform root, the box scripts, the entitlement read, the puller copy and the sitting runbook. **Nothing is applied, deployed, run against Schwab or written to AWS by a cell.**
The release acts (below) are the NFRA CloudOps lane's and Andrew's, after the cells drain. The thread is NOT exercised in this round; the first exercised read is release act A7.

## Measured at the cut (2026-10-20 ~15:5xZ; the issuer's own reads, none by a worker)

- **The 49F Schwab Box** `i-0f3d57a97f14727af`: `t3.large`, Windows Server 2022 Datacenter (10.0.20348), `us-east-1a`, VPC `vpc-0cc0c6a75e54605e3`, subnet `subnet-039d04cfaee66a5f6`, security group `quartz-si2-spike-sg` (one ingress: TCP 3389 from one /32; egress all), profile `quartz-si2-spike-profile`, key pair `quartz-si2-spike-key`, IMDSv2 `optional`. It is NOT in Terraform (only its IAM is: `canonical-schwab-ec2`). The SI2 app is a ClickOnce install: `C:\Users\Administrator\AppData\Local\Apps\2.0\...\Schwab.SI.Framework.dll`; its shortcut `Schwab Data Delivery.appref-ms` points at `https://si2.schwabinstitutional.com/sdd/Schwab.SI.SI2Desktop.Container.application`.
- **Console session:** `AutoAdminLogon=1`, `DefaultUserName=Administrator`, a `DefaultPassword` present in the Winlogon key; the Administrator session is `console` (active 112+ days); a SYSTEM task `SchwabKeepConsole` runs every 5 minutes: `powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File C:\SchwabData\keep-console.ps1`. The script, 215 bytes, verbatim:
  `$line = (query session 2>$null | Select-String -Pattern 'administrator' | Select-Object -First 1)` then
  `if($line -and ($line -match 'Disc')){ if($line -match '\s(\d+)\s+Disc'){ tscon $matches[1] /dest:console 2>$null } }`.
- **Daily pull hand-off:** `monolith-daily-schedule.tf` (read in full): EventBridge -> SSM `AWS-RunPowerShellScript` as SYSTEM -> the command pulls the puller from S3, registers a one-shot scheduled task `/RU Administrator /IT /RL HIGHEST`, proves it STARTED, waits, propagates `LastTaskResult`. Fire times of the 49F box: 09:45, 10:15, 10:45, 21:45, 22:15, 22:45 Z.
- **The 49F role** (`monolith-iam.tf:36-118`, `iam.tf`): write-only on the monolith (PutObject per master; list conditioned to the source tree; `_ops` and `meta/pulls` per master; NO Get, NO Delete on data), a code-read of one prefix, secret access, the `DenyBdPlane`/`DenyCotPlane`/`DenyInfPlane` statements.
- **Builder outputs** (`lib/opal_naming.py`, run at the cut): `name('schwab','alongside','si2-box','role')` = `schwab-alongside-si2-box-role`; `...'profile'` = `schwab-alongside-si2-box-profile`; `...'sg'` = `schwab-alongside-si2-box-sg`; `...'runner'` = `schwab-alongside-si2-box-runner`; `...'policy'` = `schwab-alongside-si2-box-policy`; `name('schwab','alongside','si2-events','role')` = `schwab-alongside-si2-events-role`; `name('schwab','08719286','si2-pull','daily')` = `schwab-08719286-si2-pull-daily`.
  `address('schwab','cottonwood','bronze','acc','date=2026-10-16')` = `s3://opal-data-assets/schwab/cottonwood/bronze/acc/date=2026-10-16`. The builder REFUSES `instance`, `rule`, `secret`, `kms` kinds and a master number inside a function word (it takes the master as the SCOPE, which `scopes.json` holds as MASTER rows, firm `cottonwood`). `meta` and `_ops` are not builder tiers.
- **Registry:** the four Cottonwood MASTER rows exist (`infra/logic/registry/scopes.json`, CRO `e5c3c708fc`), `vendor: schwab`, `firm: cottonwood`, noted NOT YET ENTITLED. The secret `schwab/alongside/sdd-credentials` exists (graded CONFORMANT, ~13:4xZ). `schwab/alongside/ec2-credentials` does not exist.
- **`~SB`'s cell `BF-w-2`** (the firm-form puller) was MERGED to `box/laptop` at `8360d83c351` (read at the cut: `git grep "function Get-FirmOf" HEAD` finds it in `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`). Cell `AL-p-1` copies that merged puller, so its dependency is met at the cut.

## Issuer rulings inside this decomposition (the issuer rules everything inside its own decomposition; each is a design choice a cell obeys)

1. **A separate Terraform root and a separate box-code folder.** `infra/aws/terraform/alongside-schwab-ec2/` (state key `alongside-schwab-ec2/tfstate`) and `infra/aws/ec2/alongside-schwab-si2/`. Nothing in `canonical-schwab-ec2/` or `canonical-schwab-si2/` is edited by this workstream (disjoint write surface from `~SB`'s `BF-i-2` and `BF-w-2`).
2. **Unlike the 49F box, the instance IS in Terraform** (`prevent_destroy`, `ignore_changes = [ami, user_data]`): the box is new, so there is no import risk; the pet-server rule (never re-image a box holding a human-established session) is carried by the lifecycle block.
3. **No standing RDP ingress.** The security group has zero ingress rules. The sitting uses SSM port forwarding (`AWS-StartPortForwardingSession`, port 3389) so no address is opened; the runbook names the CloudOps fallback (one temporary /32 rule for the sitting, removed after) for the case the operator's machine lacks the SSM plugin.
4. **The master list lives in ONE place:** `local.alongside_masters` in `masters.tf` (master -> label, fire cron). The IAM write statements, the schedule rules and the targets all derive from it with `for` / `for_each`. This is the C-ONBOARD shape on the Alongside side, so adding a master later is one map entry. Four entries: 08719286, 08134043, 08165601, 08480305.
5. **Schedule rules ship `DISABLED`** (`state = var.alongside_schedule_state`, default `"DISABLED"`). A fire before the person's sign-in, or on a master the login does not yet see, would only page. Enabling is release act A9, after the first exercised trace. Fire times (UTC, each at least 30 minutes from every other and from the six 49F fires): `08719286` cron(15 11,23 * * ? *); `08134043` cron(45 11,23 * * ? *); `08165601` cron(15 12,0 * * ? *); `08480305` cron(45 12,0 * * ? *).
6. **`meta/pulls` and `_ops` stay at MASTER scope** (the 49F shape) because Andrew has not answered whether silver, meta and `_ops` move to firm scope (PRD OPEN AT ANDREW, item 1; `BF-i-2` makes the same choice). If he answers firm scope, a later round re-points these statements; the master map makes it one edit.
7. **Bootstrap generates the Windows Administrator password** on the box (random, never printed) and writes it to the new secret `schwab/alongside/ec2-credentials` (metadata-only in Terraform, `prevent_destroy`, never a `secret_version` resource). The 49F box uses `AutoAdminLogon` with the password in the Winlogon key; the Alongside box COPIES that behavior (Andrew: "exact same setup and logic") and the runbook names it as a carried property, not a new one.
8. **The SDD session capturer (`schwab_sdd_session_capture.py`, the `schwab/sdd/session` CMK secret) is NOT copied in round 1.** The daily pull rides the app's vault token (`CredRead SDDSecure`), not the captured blob; the capturer is an enrichment for a later round if the session needs backing up.
9. **The puller is a derived copy of the post-`BF-w-2` file**, differing in exactly its header comment and its `ValidateSet` master list (the four Cottonwood masters). One-time exact-copy check at the cell; NO standing comparator is committed (Andrew's veto).
10. **Code home on the monolith:** `s3://opal-data-assets/code/alongside-schwab-si2/` (the sibling of `code/canonical-schwab-si2/`; `code/` is the reserved system prefix, and the builder has no code tier, so this is the one declared non-builder prefix, written in a comment). Upload of the files there is release act A4.
11. **The thread trace oracle is `BF-t-2`'s `thread_trace.py`** (firm-form, takes the master as an argument); no Alongside trace cell is cut.

## The rectangle (round 1, Alongside workstream)

| cell | what | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `AL-a-1` | Terraform root part 1: backend, master map, IAM role/profile/policy (per-master by file-name prefix), secrets, security group, the Windows instance | C-ALONGSIDE, C-NAMES, C-ONEWRITER | FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |
| `AL-s-1` | Terraform root part 2: the four daily schedule rules (DISABLED), the SSM targets, the events role | C-ALONGSIDE, C-ONBOARD (shape) | FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | AL-a-1 (resource addresses) |
| `AL-e-1` | Box scripts: bootstrap, keep-console, the entitlement read, and the sitting runbook | C-ALONGSIDE | FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing run) | worker | -- |
| `AL-p-1` | The puller copy for the four Cottonwood masters | C-ALONGSIDE, C-BACKFILL, C-DAILY | FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing uploaded) | worker | `BF-w-2` merged on `box/laptop` (workstream `keyform`, `~SB`) -- MET at `8360d83c351` |
| `AL-r-1` | RELEASE, acts A1-A3 as one CloudOps order: change entry, saved plan and `safe-apply` of the Alongside root, code upload to the code home, SSM bootstrap, one reboot, the box-ready reads | C-ALONGSIDE | FWD-8 | NOT-EVALUATED | laptop | WORLD (creates 17 resources, imports 1 secret) | CloudOps seat `0.7.0_AE_CloudOps~NFRA1` (a seat, not a worker) | AL-a-1, AL-s-1, AL-e-1, AL-p-1 merged (met at pin `7ce88d5bdd9`); GO = both never-widen halves signed |
| `AL-r-2` | RELEASE, acts A5-A6: the entitlement read as an Administrator scheduled task, then ONE day of bronze for each master the login sees, and the thread trace | C-ALONGSIDE, C-BACKFILL (one day only) | FWD-8 | NOT-EVALUATED | laptop | WORLD (writes bronze keys under the cottonwood firm prefix) | CloudOps seat `0.7.0_AE_CloudOps~NFRA1` | AL-r-1 complete (met); GO = Andrew's sign-in done and the CTO's condition 6 respected (no rule enabled, one day per master) |

**AL-a-1 AMENDMENT (drain, 2026-10-20 ~17:0xZ; was drafted as cell AL-f-1 and folded into AL-a-1 because PRD v0.8's ratified-text half is REFUSED by the CVO on an unrelated row, C-TIERS, which blocks any NEWLY-ADDED order but not the reopening of an existing one; v0.8 changed no Alongside or naming row).** Evidence. The plan at pin `8bb7fdf9b7c` (`deliverables/2.0.0_SA_COO~SA/PLAN_READONLY_20261020_pin8bb7fdf9b7c_BEFORE_FIX.txt`): `Plan: 1 to import, 9 to add, 1 to change, 0 to destroy` plus four `Module output value precondition failed` errors (scope not in `generated_locals.tf`), and the imported `schwab/alongside/sdd-credentials` would have its live description set to null. With both fixes applied in a scratch copy: `Plan: 1 to import, 17 to add, 0 to change, 0 to destroy` (`..._PLUS_AL-f1_FIX.txt`). The COO lane cannot write `infra/aws` (lane `CLOUD_OPS_OR_ETL` refused the issuer's own commit), so the reopened worker carries the fix: `AL-a-1`'s `<paths>` gain `infra/aws/terraform/modules/opal_name/generated_locals.tf` and a fourth criterion `AL1-a1-AC4` (the name table resolves the four masters).

**Chains (M = 3).** The amendment reopens `AL-a-1` (worker slot ~11, then `AL-s-1` is untouched). A = `AL-a-1` -> `AL-s-1` (slot ~11). B = `AL-e-1` (slot ~12). C = `AL-p-1` (slot ~13). Worker slots 11-13 are this workstream's block (`~SB` holds slots 1-6; a serial is unique per project).

**Write sets (disjoint from each other and from `~SB`'s).**
- `AL-a-1`: `infra/aws/terraform/alongside-schwab-ec2/{main,masters,iam,secrets,box}.tf`, `data/canonical/schwab/tests/test_alongside_box_tf.py`.
- `AL-s-1`: `infra/aws/terraform/alongside-schwab-ec2/schedule.tf`, `data/canonical/schwab/tests/test_alongside_schedule_tf.py`.
- `AL-e-1`: `infra/aws/ec2/alongside-schwab-si2/{bootstrap.ps1,keep-console.ps1,sdd-entitlements.ps1,RUNBOOK_ALONGSIDE_SITTING.md}`, `data/canonical/schwab/tests/test_alongside_box_scripts.py`.
- `AL-p-1`: `infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1`, `data/canonical/schwab/tests/test_alongside_puller.py`.
- The two chain-A cells share one directory but no file; `AL-s-1` READS `AL-a-1`'s addresses `local.alongside_masters`, `aws_instance.alongside_box`, `local.alongside_firm` (fixed by the contract in the `AL-s-1` face).

**Release acts (NOT cells; after the cells drain; the seat holding the access).**
- A0 merge the drain; the COO's one real run of each LOCAL outcome (pytest, the Terraform text read).
- A1 change entry in `org/critical_paths/change_management/` opened; never-widen pair (CTO + COO) naming the blast radius: one NEW role, profile, security group, instance, two secrets (one adopted by import), four DISABLED rules and one events role; nothing existing is modified (`terraform plan` must show adds and one import only).
- A2 `terraform init` + `plan` in the new root (NFRA CloudOps lane, rule 34), plan read by the COO; `safe-apply` (adds + the secret import).
- A3 the code home upload (`bootstrap.ps1`, `keep-console.ps1`, `sdd-entitlements.ps1`, `sdd-daily-pull.ps1`) to `code/alongside-schwab-si2/`; SSM bootstrap run on the new instance; the password secret read back by length only.
- A4 the SITTING (Andrew): the runbook, SSM port forward, ClickOnce install of the SI2 app, sign in with Alongside's Schwab login (a security code may be asked), leave the session logged on.
- A5 the entitlement read (`sdd-entitlements.ps1` as an Administrator scheduled task): which of the four masters the login sees. A master it does not see is named in the report and is Andrew's call to Cottonwood (PRD C-ALONGSIDE); FWD-8 then grades on the masters seen.
- A6 one Cottonwood day pulled (`-OnlyAsOf`), converted, `BF-t-2`'s trace read (FWD-8's thread).
- A7 history to Schwab's floor (C-BACKFILL), outside the fires, under the box's session lock.
- A8 ENABLE the four rules (one `safe-apply` with `alongside_schedule_state = "ENABLED"`), the first scheduled fire read.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: PRD v0.5's candidate list for the parallel workstream, items (a)-(e) (`CELL CANDIDATES`, the last paragraph): (a) the CRO's scope rows -- DONE, `e5c3c708fc`, no cell; (b) the box's Terraform root and puller copy -- `AL-a-1` + `AL-s-1` (root), `AL-p-1` (puller); (c) the person's sign-in -- release act A4, with its runbook in `AL-e-1`; (d) the entitlement read -- script in `AL-e-1`, run at A5; (e) one Cottonwood day end to end, then its backfill -- A6, A7, with the trace oracle already built (`BF-t-2`). By subtraction, remainder: none (C-ONEWRITER's dry-plan check rides `AL-a-1`'s test as a text assertion).
- **Same grain.** One cell per write set. **Intent coherence.** `a`/`s` = what the cloud holds; `e` = what the box runs and what the person does; `p` = what the box pulls. **State coherence.** No cell applies, deploys, uploads, contacts Schwab or writes S3.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE as a tool run. The six 49F fire times are inlined into `AL-s-1` and its test checks the 30-minute separation; the new rules ship DISABLED, so no gate is armed by this round.
- `comp-iam`: DECLARED-NOT-APPLICABLE. The role is NEW (no existing grant to cross-reference); the copy-source statements (`monolith-iam.tf:36-118`, `iam.tf:28-121`) were read at the cut. BLIND: the live IAM plane (0 roles read).
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run. Findings inlined: (1) four masters share one firm folder, so the write grant is enumerated by file-name master prefix, never a folder wildcard; (2) the schedule must not fire before the sign-in (DISABLED default); (3) the ClickOnce install source is a Schwab URL reachable only in an interactive session, so the install is the person's act in the same sitting, not a script; (4) the 204-until-entitled hazard: a pull of an unentitled master returns no content, so the entitlement read (A5) precedes every pull; (5) the SSM hand-off runs as SYSTEM and the vault is Administrator's, so the pull must run as an Administrator scheduled task (the 49F measurement, `monolith-daily-schedule.tf:82-116`).

## Not in round 1

FWD-7's onboarding inversion for the 49F box (`~SB`'s); silver, meta and `_ops` scope (open at Andrew); the session capturer; the held-days record (FWD-3); the 49F box's own edits.
