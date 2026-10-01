# Never-widen half, MDPF_SECCLASS thread hops 1-4 -- ROUND 3 (BD_THREAD_R3): the redeploy of the BD thread files with
# the shared client shipped INSIDE code/gold/, after the flat-runner crash of 2026-09-30

**This half SUPERSEDES `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md` for the ACT, and cites it for the
blast-radius analysis; that file is left UNEDITED.** The R2 half's steps 1-4 ran once on 2026-09-30: the deploy landed
at 16:31Z, the exercise run at 17:48Z crashed C_06 at import on the gold runner (`/tmp/gold_layer_scripts/lib/
etf_classifier.py` line 19, `IndexError: 5`), nothing served moved, and the five code objects were rolled back at
18:16:09Z-18:17:23Z (row `MDPF_SECCLASS-S5`). This half is the fix-forward's act. Read the R2 half for: the four
served families D_03 / D_04 / C_06 / silver write, their readers, the GLD / PHYS / VXX move table, the IAM finding
(`bd-exporter-ec2-role` already carries `bd-securities-access` with GetItem on `etf-classifications`; no IAM change),
and the release-order reasoning. Only what changed is restated below.

**Author:** `0.9.0_WK_MDPF_SECCLASS~10`, 2026-09-30 (TO-SC-e13, round 6). **For:** the issuer (`2.0.0_SA_COO~M`) and
`1.0.0_SA_CTO` to sign. **Status of the act: NOT YET RUN.** This cell is a LOCAL build plus record: nothing was
uploaded, deployed or run on any runner; S3 was read (VersionIds, below) and nothing else.

## What changed since the R2 half

1. **The shared client now ships with the gold code.** `.tools/safe_deploy_core.py` declares, in
   `CODE_TREES["black_diamond"]["shipped_artifacts"]`, that a bd gold deploy also uploads three repo files flat into
   `lib/_shared/` under the gold layer's own prefix: `etf_classifications_dynamodb.py` (the ONE client),
   `etf_classification_scheduled.py` (E_18's planner) and `etf_classification.py` (the one module the planner imports at
   load; closure measured by importing the planner with only its own directory on `sys.path`: those three, no others).
   No second copy exists in the repo (contract C-TABLE); the bytes travel only as a deploy artifact.
2. **The library and E_18 resolve from their OWN directory first.** `lib/etf_classifier.py` looks in `<its dir>/_shared/`,
   then in the first ancestor holding `infra/aws/lambda/v2_portal/_shared/`; `E_18.detect_new_securities.py` looks in
   `<its dir>/lib/_shared/`, then the same ancestor. No module-level `Path.parents[N]` remains (the AST guard in
   `test_etf_classifier_deployed_resolution.py` fails on the old lines 19 and 54). A missing client is an `ERROR: BLOCKED`
   log line plus an `ImportError` at first use (library) or a `False` return and exit 2 (E_18), never an exception at import.
3. **Byte changes against the failed 16:31Z deploy.** C_06, D_03, D_04 and `build_bd_assets_dim.py` are byte-identical to the
   16:31Z deploy (candidate md5 equals that version's ETag, table below). Only `lib/etf_classifier.py` and
   `E_18.detect_new_securities.py` changed, plus the three new shared files.
4. **Three first-mint keys** (`code/gold/lib/_shared/*`, head-object 404 read live 21:1xZ): the act creates them; the signed
   R2 half named no new key.
5. **The prior versions moved.** The served keys were overwritten by the normal 04:00Z run at 05:1xZ today; the prior
   VersionIds below are today's, not the R2 half's.
6. **The rollback branch is now tested** (2026-09-30 18:16:09Z, five code keys, copy-object from the prior VersionId, ETag
   verified per key). The live code keys are those rollback copies.

## The act

Preconditions, each a stop:

- **P1 (row `MDPF_SECCLASS-W10-S1`) -- SATISFIED BY LEG 0 below, per AMENDMENT 1 of TO-SC-e13 (2.0.0_SA_COO~M, 2026-09-30).**
  The silver bootstrap document `infra/aws/ssm/opal-bd-asset-dim-download.json` now carries one `mkdir` path and three
  `aws s3 cp` lines staging `code/gold/lib/_shared/{etf_classifications_dynamodb,etf_classification_scheduled,
  etf_classification}.py` into `$RUNROOT/data/black_diamond/scripts/gold/lib/_shared/` (committed with this cell; the
  check proves the three keys equal `safe_deploy_core.shipped_artifacts_for()`). The repo file is not live until Leg 0
  runs, so Leg 0 is the act that discharges P1; it is not a separate cell any more.
- **P2 (timing).** The silver job fires about 22:10Z (`bd_assets_dim.parquet` LastModified 22:11Z on 09-28 and 09-29) and stages
  `code/gold/lib/etf_classifier.py` and `code/silver/build_bd_assets_dim.py` at start, so the two must change together: step 1
  is ONE `safe-deploy` call, run in a gap between that job's fires, with the UTC time read into the ledger.

Steps:

0. **LEG 0 -- the silver document update (amendment 1; runs BEFORE step 1, in the same gap as step 1).**
   - **How the document reaches AWS (read from the estate, 2026-09-30 22:5xZ).** It is NOT Terraform-managed (only
     `infra/aws/lambda/bd-pipeline/iam.tf:97` names it) and has no deploy script. The one precedent is a MANUAL publish:
     `org/critical_paths/change_management/20260928T2032Z_nfra-mcpindex-bd-asset-dim-rest-schedule_deploy_completion.md`
     leg L2 (`aws ssm update-document --name opal-bd-asset-dim-download --content file://<file> --document-version '$LATEST'`,
     then `update-document-default-version`; writers of the content: one, the manual call).
   - **Live state BEFORE (read only, `.tools/aws ssm describe-document` + `list-document-versions` + `get-document`,
     2026-09-30 22:5xZ):** `DefaultVersion=4`, `LatestVersion=4`, versions 1, 2, 3, 4 all Active; v4 created
     2026-09-28T20:37:58Z; `Hash=294a703617118218e386c275c4a1511bdef6dd833722031c6192ee04fd8ae95e` (Sha256). The live v4
     content equals the repo file at the parent of the amendment commit (`git show c3d41dc9dd:<file>`, parsed JSON equal,
     125 of 125 `runCommand` lines identical), so the diff Leg 0 applies is exactly the TO-SC-e13 edit: +1 `mkdir` path,
     +3 comment lines, +3 `cp` lines.
   - **THE TRIGGER READS `$LATEST`, NOT THE DEFAULT.** `infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/lambda_function.py:55-58`
     calls `ssm.send_command(DocumentName='opal-bd-asset-dim-download', DocumentVersion='$LATEST')` (rule
     `bd-asset-dim-pipeline-trigger`, `cron(10 22 ? * MON-FRI *)`, ENABLED; live Lambda code not byte-read, this is the repo
     source). `update-document` therefore changes what the NEXT 22:10Z fire runs the moment it returns; the default-version
     step does not gate it. (Live Lambda `LastModified` 2026-04-14 predates every document version.)
   - **The act:** (1) read the next silver fire time and require it more than 30 minutes away, and write the UTC time into
     the ledger; (2) `git show <drain commit>:infra/aws/ssm/opal-bd-asset-dim-download.json > <scratch>/doc_v5.json`
     (the index blob is LF; the working copy on this device is CRLF, so publish the `git show` bytes, never the working
     file), expected sha256 `d3a38c7b1a92b3d92030c241ab6502245c5a25d3b40930dcef67548943d3f407` (10840 bytes; the working
     file with CR removed, re-verified against the drain commit's blob); (3) `get-document --document-version 4 --query
     Content --output text > <scratch>/doc_v4_rollback.json` and check its sha256 is the `Hash` above; (4) `.tools/aws ssm
     update-document --name opal-bd-asset-dim-download --content file://<scratch>/doc_v5.json --document-version '$LATEST'`
     -> expect new `DocumentVersion 5` with `Hash` equal to the sha256 in (2); (5) `.tools/aws ssm
     update-document-default-version --name opal-bd-asset-dim-download --document-version 5`; (6) readback
     `get-document` (default) equals the file as parsed JSON and carries three `_shared` `cp` lines.
   - **Rollback, in this order (restoring the default alone does NOT roll back the trigger, which reads `$LATEST`):**
     (a) `update-document-default-version --document-version 4` (the prior default, read live above); AND (b) republish the
     v4 bytes as the new `$LATEST`: `update-document --name opal-bd-asset-dim-download --content file://<scratch>/doc_v4_rollback.json
     --document-version '$LATEST'` -> version 6 whose `Hash` equals `294a7036...ae95e`, then `update-document-default-version
     --document-version 6`. (SSM refuses identical-to-latest content with `DuplicateDocumentContent`; v5 is latest by then, so
     this republish is not a duplicate.) Readback: `get-document` (`$LATEST`) `Hash` equals `294a7036...ae95e`.
   - **ORDER HAZARD this leg carries (row `MDPF_SECCLASS-W10-S5`).** The three new `cp` sources are FIRST-MINT keys that
     step 1 creates. The document runs `set -eo pipefail`, and each `cp` is piped to `tee`, so a fire that runs the new
     document BEFORE step 1 has uploaded them exits at the first missing key, BEFORE `shutdown -h +2` is armed: the
     t3.medium is stranded running and `silver/bd_assets_dim.parquet` is not written (an honest exit, no served move).
     Leg 0 and step 1 are therefore one gap, back to back, with no silver fire between them; if step 1 does not complete,
     run the rollback above immediately. The order inside the gap is the issuer's (amendment 1: Leg 0 first).
   - **Local proof:** `r6_deployed_layout_import.py` prints `SILVER-LAYOUT-AS-STAGED-TODAY OK build_bd_assets_dim` from the
     document in the repo, `SHARED-KEYS-MATCH-TOOL`, and `SILVER-NEGATIVE-CONTROL REFUSED-AS-EXPECTED` (the document minus its
     `_shared` lines); it exits non-zero when the as-staged import is refused. These replace the
     `SILVER-LAYOUT-...-WITH-SHIPPED-ARTIFACTS` line names used in the "Both branches" paragraph and the Evidence section
     below, which are left as written.

1. **Deploy (candidate diff, not yet applied):** `.tools/safe-deploy.sh`, DS lane (CLAUDE.md rule 13), ONE call on the six
   committed files below. Its receipt lists each `[script]` and each `[shipped]` destination, and it uploads the three
   shared modules FIRST, then the six files, each SHA-verified (ETag equals the index blob's md5). Candidate bytes: the
   drain commit of TO-SC-e13, by blob id below. `opal-data-bd` only; no other firm's tree.
2. **Exercise (import proof, not counted as acceptance):** ad-hoc QA fire of the BD gold chain on the runner. Candidate
   command, the smallest chain that holds C_06, D_03 and D_04: `bash /tmp/gold_dispatch.sh --chain downstream --incremental
   --bg` (the 17:48Z exercise was a `gold_incremental` run; the ledger states the exact command used). Expected: C_06, D_03,
   D_04 each print `done (rc=0)`; the log holds no `IndexError` and no `BLOCKED`.
3. **Acceptance:** the ordinary scheduled fire, `bd-gold-nightly-fallback` 23:00Z or `bd-canonical-prices-daily` 04:00Z,
   whichever comes first after step 1. The ad-hoc run of step 2 does not count.
4. **Closing act, the COO's one live run of FWD-1 to the page** for relationship `z08327149`: VXX reads `structured` /
   `Hedge`, GLD and PHYS read `commodities` / `Metals`, each with `class_source` `etf-classifications` and
   `bd_securities_reads` 0, on the real page, after step 3 has run.
5. **E_18's moved acceptance:** its first scheduled run after step 1. **Measured gap (row `MDPF_SECCLASS-W10-S2`):**
   `gold_dispatch.sh` lists no E_* id in its catalog or chains, so no scheduled fire runs E_18; this step cannot fire as
   written. The signers decide: name a trigger, or accept an ad-hoc dry-run (no `--upload`, reads only) on the runner as
   E_18's runner proof. Until then E_18's import proof is the deployed-layout check.

**Candidate files (git blob id of the index bytes, md5 = the ETag `safe-deploy` verifies, bytes), and every destination key
(bucket `opal-data-bd`):**

| repo file | blob | md5 / bytes | destination key | live VersionId now (prior) | live ETag / LastModified |
|---|---|---|---|---|---|
| gold/C_06.client_mix_timeseries.py | 2d33340f8a | e84817dc...fc / 40976 | `code/gold/C_06.client_mix_timeseries.py` | `DF0mrQMYPQUVaROwXfWx_ujZzby33Pd_` | 8b1f012c.. / 09-30 18:17:23Z (rollback copy) |
| gold/D_03.composition_artifacts.py | 70acb4e723 | 705adba8...df / 40775 | `code/gold/D_03.composition_artifacts.py` | `yAWDop5v36OOwguqHMJovAMw3ISs1nMv` | 346e7b0f.. / 18:16:51Z (rollback copy) |
| gold/D_04.client_portal_summary.py | a63dcfbb94 | ffcdc362...73 / 161113 | `code/gold/D_04.client_portal_summary.py` | `mLh4U.wMEWiVMNO9Ztbsvjubgrk1Z_Qm` | a4b867d4.. / 18:17:07Z (rollback copy) |
| gold/E_18.detect_new_securities.py | ce8c8b9ac9 | a7820a20...f6 / 14802 | `code/gold/E_18.detect_new_securities.py` | `NVNguz8v2wHJW_KSsDx9S8MGpeMElqSE` | 9beb18cc.. / 14:11:20Z (E18 half deploy, 13120 bytes) |
| gold/lib/etf_classifier.py | 27f9af1e37 | 96ad9dde...bc / 8104 | `code/gold/lib/etf_classifier.py` | `yk0qwnF4Dyur2rUn1alS5Nt2_EtsR5Kx` | 884889c0.. / 18:16:18Z (rollback copy) |
| silver/build_bd_assets_dim.py | 2f9c951ee4 | b528caa7...3a / 18977 | `code/silver/build_bd_assets_dim.py` | `rfdhSeghulhB_Y1.qra.xVBUCFBU_35y` | 662ef035.. / 18:16:33Z (rollback copy) |
| _shared/etf_classifications_dynamodb.py | 4668003c3b | e62906ef...51 / 14027 | `code/gold/lib/_shared/etf_classifications_dynamodb.py` | none (first mint, 404) | -- |
| _shared/etf_classification_scheduled.py | e2adbc8474 | 6957dcc9...55 / 30327 | `code/gold/lib/_shared/etf_classification_scheduled.py` | none (first mint, 404) | -- |
| _shared/etf_classification.py | a88fc4b0f9 | 58bfdb97...8d / 60065 | `code/gold/lib/_shared/etf_classification.py` | none (first mint, 404) | -- |

Full md5 values: C_06 `e84817dcae35bb66e75b8925797716fc`, D_03 `705adba827d05fb7dae3d2b64618bbdf`, D_04
`ffcdc3620936e240a075e84cc9711273`, E_18 `a7820a205692444dadb59e526200bff6`, lib `96ad9ddeb98b9137bb2e189837ea76bc`, silver
`b528caa706bb2312011fd62268c05d3a`, client `e62906eff240a853029181715fc9b451`, scheduled `6957dcc97a453d23cc930ed9d637a055`,
etf_classification `58bfdb97c0081327c245ef81f3f7e18d`. The first table is the blob/bytes as committed on the branch of
TO-SC-e13 (HEAD at the time of writing); the drain may move the commit hash but not the blob ids.

## Evidence (LOCAL, this cell, 2026-09-30)

- `python -m pytest data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py
  data/black_diamond/scripts/gold/tests/test_etf_classifier_canonical.py -q -p no:cacheprovider` -> 18 passed. Each new
  case imports in a fresh `python -I` interpreter over a runner-shaped temp tree.
- `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_deployed_layout_import.py` asks
  `safe_deploy_core.upload_plan()` for the plan (8 files: the five gold thread files plus the three shared modules), reads
  the gold flatten rule from `gold_dispatch.sh` `sync_scripts` (`aws s3 sync .../code/gold/ /tmp/gold_layer_scripts/`,
  required to equal the tool's gold prefix), extracts into a temp root with no `infra/` tree and imports each module in a
  child that refuses to run with any repo path on `sys.path`: `DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=8`, every
  client resolved inside the extract. Negative control (the tool patched to ship nothing): 0 of 5 import, each with the
  `BLOCKED` refusal.
- Silver layout, measured from the runner's own bootstrap document (`infra/aws/ssm/opal-bd-asset-dim-download.json`): a
  repo-shaped `$RUNROOT` with `silver/build_bd_assets_dim.py`, `gold/lib/{etf_classifier,__init__}.py` and
  `lib/{silver_ids,trading_calendar}.py`; the builder reaches `gold/lib` through its own `../gold` insert and needed no
  change; the client is the gap (P1).
- The shallow-path cause, reproduced: `Path('/tmp/gold_layer_scripts/lib/etf_classifier.py').parents[5]` -> `IndexError: 5`.

## Blast radius

**Reused by citation, unchanged:** the served families and their readers (`gold/views/firm_composition.json`,
`gold/advisors/{id}/composition.json`, `gold/entities/clients/{rid}_composition.json`, `platinum/accounts/{id}/summary.json`,
`platinum/clients/{rid}/summary.json`, `platinum/firm/mix_summary.json`, `gold/client_timeseries/{rid}.json`,
`gold/views/mix_daily_summary.json`, `silver/bd_assets_dim.parquet`), the additive canonical keys, the one coarse number that
moves (`mix_daily_summary.json`, by the formerly-guessed-to-equity population), and the three-ticker move table, all from
the R2 half's Blast radius section. The candidate bytes of C_06, D_03, D_04 and the silver builder are byte-identical to
R2's, so that analysis applies unchanged.

**What this act adds to the blast radius:**

1. **Three new objects on the runner's sync prefix.** `aws s3 sync s3://opal-data-bd/code/gold/ /tmp/gold_layer_scripts/`
   (no `--delete`) copies `lib/_shared/` with the rest; the directory is put on `sys.path` by `lib.etf_classifier` and by
   E_18 at load. It holds exactly three modules; none shares a name with a file in the gold tree (the gold lib carries
   `etf_classifier.py`, not `etf_classification*.py`), so nothing on the path is shadowed.
2. **The silver runner's classifier source changes the moment `code/gold/lib/etf_classifier.py` does.** Its document reads that
   key at each fire: see P1/P2. Served key at risk: `silver/bd_assets_dim.parquet` (live `gY8SA9ruIsLh90CuCCf42I5TBl.wceEq`,
   09-29 22:11:40Z), which the job overwrites only after a successful build; a refusal writes nothing.
3. **E_18.** The redeploy replaces the live copy that still carries the `parents[4]` hop. Nothing schedules E_18 (step 5),
   so no served value moves from it in this act; its `--upload` (when run under a later trigger) writes only new
   `etf-classifications` rows with `attribute_not_exists(ticker)`, per the E18 IAM half (cited, not restated).
4. **No IAM change, no table write, no Lambda, no schedule change.** The exercise and scheduled runs read
   `etf-classifications` only.
5. **Served keys the chain overwrites, prior VersionIds read live 2026-09-30 21:1xZ** (these are the versions a rollback
   restores; the ledger snapshots every key of the `advisors/`, `entities/clients/`, `platinum/accounts/`,
   `platinum/clients/` and `client_timeseries/` families with its prior VersionId at the run, before step 2):

| served key | live VersionId now (restore target) | LastModified | bytes |
|---|---|---|---|
| `gold/views/firm_composition.json` | `AUXYImvT.mtH_QkBltgfXex_cHLkAs08` | 09-30 05:16:34Z | 6560 |
| `gold/views/mix_daily_summary.json` | `oIyAV02CeRLMV7.MHc4LJ8DAq_W4TC0I` | 09-30 05:16:18Z | 9737004 |
| `platinum/clients/z08327149/summary.json` | `RMmQy.i3LpwmkXjikpsX2OvS0yyj9d_9` | 09-30 05:38:19Z | 181272 |
| `platinum/firm/mix_summary.json` | `4iHMfpRAN8f3QV7htKyzolnY5NAQ3uQF` | 09-30 05:36:36Z | 8625 |
| `gold/client_timeseries/z08327149.json` | `QCRz2F4EMb0b4aPlrr3hE2XbGKF9Xpxv` | 09-30 05:15:31Z | 1291594 |
| `silver/bd_assets_dim.parquet` | `gY8SA9ruIsLh90CuCCf42I5TBl.wceEq` | 09-29 22:11:40Z | 977664 |

   The 17:48Z exercise changed none of the four keys the watch read (changed=0 of 4; row `MDPF_SECCLASS-S5`), so these
   versions are also the pre-exercise ones.

**Both branches of step 1, read not predicted.** (a) P1 landed: the silver document stages the client; the check's
`SILVER-LAYOUT-WITH-SHIPPED-ARTIFACTS OK` line is the local proof; the next silver fire builds through the canonical
client. (b) P1 not landed: step 1 does not run (precondition), and the live state stays the rolled-back code, which both
runners execute successfully today.

## Rollback per key

S3 is versioned for `opal-data-bd`; rollback restores the PRIOR object version at each key, never an attribute-level undo.
Order: code first (stops the writer), then data.

- **Code keys with a prior version** (`C_06`, `D_03`, `D_04`, `E_18`, `lib/etf_classifier.py`, `silver/build_bd_assets_dim.py`):
  `aws s3api copy-object --bucket opal-data-bd --key <key> --copy-source "opal-data-bd/<key>?versionId=<live VersionId now>"`,
  then `head-object` ETag equals the ETag in the table. **This branch ran for real on 2026-09-30 18:16:09Z-18:17:23Z** on five
  of the six keys (copy-object from the prior VersionId, ETag verified per key), which is why the live versions are those
  copies.
- **First-mint keys** (`code/gold/lib/_shared/` x3): no prior version exists; rollback is `aws s3api delete-object
  --bucket opal-data-bd --key <key>` with no VersionId, which writes a delete marker on the versioned bucket (the bytes stay
  recoverable by deleting the marker) and removes the key from every later `sync`. This is an S3 delete; the signatures on
  this half are the confirmation CLAUDE.md asks for. The rolled-back library and E_18 never read `lib/_shared/`, so the
  three keys are inert without the new code.
- **Served data keys** (the six above, and every key of the families the ledger snapshots): `copy-object` from the
  recorded VersionId restores that key's exact pre-act bytes, independent of every other key.
- **Silver:** `silver/bd_assets_dim.parquet` from `gY8SA9ruIsLh90CuCCf42I5TBl.wceEq`.
- **No table, IAM or schedule rollback**: none was changed.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-09-30 ~23:3xZ)

Signed on the blast radius above, against TO-SC-e13 drained @9dd3e506b7 (build f136b6f559 / 23aa443681 / a170cf4cb2 /
51df828590, amendment 1 c3d41dc9dd / 83122ae32a, complete f9ce5275d9). Issuer re-run on CLOUD @934c157f17: 18 passed;
`DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=8`; `SILVER-LAYOUT-AS-STAGED-TODAY SHARED-KEYS-MATCH-TOOL` and `... OK
build_bd_assets_dim`; `SILVER-NEGATIVE-CONTROL REFUSED-AS-EXPECTED`; HALF-READY; proof VALID. The repairs cell that edits
the client bytes this act ships (TO-SC-e14) is drained @26655d0839, so the shipped client is the filtered one.

**RULING ON ROW `MDPF_SECCLASS-W10-S5` -- the order inside the gap is REVERSED from amendment 1.** Amendment 1 said "Leg 0
first"; that was wrong. The trigger runs `send_command(DocumentVersion='$LATEST')`, so publishing the document IS its
activation, and the document's three new `cp` sources are first-mint keys that only step 1 creates. The act therefore runs:
**step 1 (the ONE `safe-deploy` call: gold thread files, silver builder and the three shipped `lib/_shared/` modules) FIRST,
then Leg 0 (the document publish), back to back**, with no silver fire (about 22:10Z) and no gold fire in progress between
them. If Leg 0 fails after step 1, the silver builder on S3 is the new one while the live document is v4, which stages no
client: run step 1's code rollback (the 18:16Z tested branch, prior VersionIds per key) in the same gap.

**The window, read from the schedules:** the 23:00Z gold run (runner launched 23:00:30Z) must be COMPLETE and the runner
stopped before step 1 copies a byte; the whole gap closes before the 04:00Z `bd-canonical-prices-daily` gold fire. The ad-hoc
gold QA exercise runs inside the gap and must complete before 04:00Z; it is the import proof on the real runner (CTO DECISION
103371), not the acceptance. **Acceptance:** the 04:00Z gold fire (C_06, D_03, D_04 exit 0; served keys advance; prior
VersionIds recorded) and the next 22:10Z silver fire (`silver/bd_assets_dim.parquet` advances). Then the COO's FWD-1 page read
for z08327149.

**Both branches, read not predicted:** (a) the exercise imports and runs: the served keys move exactly as the R2 half's census
named (only the moved tickers change class; three canonical keys added); (b) the exercise refuses at import: nothing served
moves (an import crash writes nothing, measured 17:47Z), and the rollback runs in the same gap.

**Writers of the served BD classes:** 3 scripts + 1 library + the silver builder, all inside this act; `etf-classifications` is
read only. **Not in this act:** E_18's scheduled run -- row W10-S2 found `gold_dispatch.sh` carries no E_* id, so E_18 has no
trigger at all; that is carried to 1.0.0_SA_CTO with the round-6 packet, and E_18's deployed bytes simply ride step 1.

**One ledger entry**, opened before step 1 and closed at the FWD-1 page read, every overwritten key's prior VersionId and the
document's prior default version (4) recorded.

## CTO half -- SIGNED (1.0.0_SA_CTO, 2026-10-01 ~03:4xZ), with ONE CORRECTION to the candidate table

Signed on the blast radius above and on the COO half's order ruling (step 1 FIRST, then Leg 0, back to back), bound to this
file's pre-signature blob `5a385ef59f` (CLOUD `53f971d7a6`). This is the NEW CTO half that condition 7 of the R2 half and the
gate on ledger entry `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930` (HELD-SOVEREIGN-GATED, held 18:27Z) wait on.

**Measured at signing (2026-10-01 03:30Z-03:33Z), each read by this seat:**

- **Candidate bytes, 9 files: 8 of 9 equal the table; ONE ROW IS STALE.** `_shared/etf_classifications_dynamodb.py` is blob
  `d7195edf5a`, md5 `181e1902667beb928a9ea993bd17d349`, 14422 bytes at the drain `9dd3e506b7`, at the COO's signing commit
  `2744a9fc57`, at `934c157f17` and at HEAD `53f971d7a6` (4 of 4 commits read). The table's `4668003c3b` / `e62906ef...51` /
  14027 is the pre-SC-e-14 client (build `cf24f07493`); the sentence "the drain may move the commit hash but not the blob ids"
  is false for this one file. **This half is signed on `d7195edf5a`.** The other eight blob ids and md5 values were re-read from
  HEAD and match (`git rev-parse HEAD:<file>` + `git show | md5sum`). The document at HEAD: sha256 `d3a38c7b...d3f407`, 10840
  bytes, as stated.
- **Live S3 (`head-object`, 9 keys):** the three `code/gold/lib/_shared/` keys read 404 (3 of 3: the act has not run); the six
  code keys carry the VersionIds and ETags in the table (6 of 6: the restore targets are current).
- **Live SSM (`describe-document`):** DefaultVersion 4, LatestVersion 4, Hash `294a7036...ae95e` (Sha256), as stated.
- **The trigger:** `infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/lambda_function.py:55-58` sends
  `DocumentVersion='$LATEST'` (repo source read; the live Lambda's bytes are NOT read by this seat). The signed order is
  sound under either reading, because Leg 0 moves both `$LATEST` and the default, and the rollback restores both.
- **Checks re-run at HEAD `53f971d7a6`:** `r6_deployed_layout_import.py` rc=0 -- `DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=8`,
  `SILVER-LAYOUT-AS-STAGED-TODAY SHARED-KEYS-MATCH-TOOL` (3 and 3), `... OK build_bd_assets_dim`, `SILVER-NEGATIVE-CONTROL
  REFUSED-AS-EXPECTED`; pytest 18 passed. `git diff 934c157f17 HEAD` over the act's inputs (gold, silver builder, `_shared`,
  the document, `safe_deploy_core.py`, `safe-deploy.sh`, `R6_CHECKS`) is empty.
- **Writers of the served BD classes:** 3 scripts + 1 library + the silver builder, all inside this act (N = 5, the COO's
  count, not re-counted here); `etf-classifications` is read only.

**Conditions (each a stop):**

1. **Order:** step 1 (the ONE `safe-deploy` call) completes with every ETag verified BEFORE Leg 0 publishes. The receipt's
   ETag for `code/gold/lib/_shared/etf_classifications_dynamodb.py` reads `181e1902667beb928a9ea993bd17d349`; the table's
   `e62906ef...` on that key is a stop, not a pass.
2. **The window is its invariants, not the clock time.** At signing `2.0.0_SA_COO~M` has no live session (live seats 03:30Z:
   4, none a COO), so the 23:00Z-04:00Z gap named above will pass unused. This half holds for ANY gap in which, each read
   live and written to the ledger with its UTC time: (i) no BD gold run is in progress and the gold runner is stopped before
   step 1 copies a byte; (ii) the next silver fire (`cron(10 22 ? * MON-FRI *)`) is more than 30 minutes after step 1 starts
   and Leg 0's readback completes before it; (iii) the exercise, and its rollback if it refuses, completes before the next
   scheduled gold fire (23:00Z or 04:00Z) starts. The COO half's window sentence is the COO's to restate for the gap it uses;
   a later gap that meets (i)-(iii) needs no new CTO half.
3. **No S3 delete under this half.** The rollback of the three first-mint keys is LEAVE IN PLACE: the rolled-back library and
   E_18 never read `lib/_shared/` and document v4 copies none of them, so the keys are inert. CLAUDE.md reserves S3 deletes
   to human confirmation and two seat signatures are not that; a `delete-object` on those keys needs Andrew's word.
4. **Leg 0 publishes the `git show <commit>:` bytes** (sha256 `d3a38c7b...d3f407`), expects version 5, and its rollback is the
   two-part one above (default back to 4 AND the v4 bytes republished as `$LATEST`), with `doc_v4_rollback.json` saved and
   hash-checked BEFORE the publish.
5. **Leg 0 fails after step 1:** step 1's code rollback runs in the same gap (prior VersionIds above), as the COO ruled.
6. **Exercise and acceptance:** the ad-hoc gold fire is the import proof on the real runner and is not counted; a refusal at
   import runs the rollback in the same gap. Acceptance is the first scheduled gold fire after step 1 (C_06, D_03, D_04 exit
   0, served keys advance) AND the first 22:10Z silver fire after Leg 0 (`silver/bd_assets_dim.parquet` advances).
7. **Ledger:** ONE entry, opened before step 1 and closed at the FWD-1 page read for `z08327149`, recording every overwritten
   key's prior VersionId, the document's prior default (4) and the saved v4 hash. It names the disposition of the held R2
   entry (continued or superseded).
8. Any deviation not named in this file stops the window for a new half.

**E_18 (step 5, row `MDPF_SECCLASS-W10-S2`), ruled:** E_18's bytes ride step 1. An ad-hoc dry-run on the runner (no
`--upload`, reads only) inside the exercise is accepted as E_18's runner proof and is NOT a stop. E_18 has no trigger; a
production pipeline is scheduled, so its trigger is a cell of the round-6 analysis, never a rider on this act.

**Carried, not signed:** the live bytes of the `bd-asset-dim-trigger` Lambda (unread); the shared-infra grant's narrowing
(W6-S2, SC-e-12), unchanged from the R2 half.
