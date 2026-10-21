# NFRA_FIDUPL -- L5 decomposition, ROUND 3 (coverage from the switcher, daily logout and recovery, backfill, the schedule on) -- v1.0, FROZEN AT THE CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-21 ~01:40Z | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path.
**Authority:** CTO msgs 8891, 8909 ("GO on the three open items in this order: switcher read + per-G secret, daily logout, schedule addendum; backfill cells cut now beside them") and the PRD v0.5 @c4f8dc3d51 (v0.4.6: coverage is every G number the switcher lists; the agent recovers the full browser sign-in once per run). Rounds 1 and 2 proved the thread: six files of 20261019 sit in `s3://opal-data-assets/fidelity/alongside/bronze/` (run record `run-20261021T012004Z.json`, ALL_LANDED).
**Input:** the worker reference sections 1 to 12 (section 12 is this round's interfaces); `RESEARCH_20261020_NFRA_FIDUPL_SWITCHER_LIST_READ.md`; `RESEARCH_20261021_NFRA_FIDUPL_FILE_DATE_AND_ACCOUNT_COLUMNS.md`.

## 0. The design in one paragraph

The login's G Number Switcher is the authority on which G numbers exist. Each run reads its list (the `gswitch` form parse already used by the attribution sweep), maps each label to a firm by the CRO's table (an unmatched label lands under `alongside` and is named by ordinal), and checks the list against the per-G secret, which is no longer the source but the cross-check; the secret's value is written once from the live read on the box. Every run ends with the logout the lander's session close already performs; the run now records its statuses. If the scripted sign-in is refused, the run tries the full sign-in once more in the box's own OS-launched Chrome unit (CDP attach), recorded, never looped. The backfill runner walks each G back as far as Fidelity serves, with a run cap and a daily sign-in cap. The schedule is turned on against a named secret version.

## 1. Gaps that are NOT in this round (stated so none is silent)

1. **The on-demand export request** (Export Custom with a date range; Historical Prices and Positions Export) is still unmeasured: the real `ExportClient` adapter of the backfill waits for Andrew's capture. FT-s-4 builds the runner against a fake.
2. **The account-number column of position, balance and transact** (the CRO has only account.txt = 0): `config.json` still holds the account-column map as measured on the box.
3. **Firm scope rows** for firms the table maps but the registry lacks are the CRO's (eight scope rows exist per its report).

## 2. The rectangle (cut by write set)

| cell | what it builds (one adapter) | write set (disjoint; the investigation file is shared and append-only) | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-1** | The switcher read and the per-G secret seed: the live list through the request object, the firm table, the cross-check, the seed payload and the box command `perg_seed.py` (signs in, reads, puts the one secret, logs out) | `infra/aws/ec2/canonical-fidelity/switcher_list.py`, `.../perg_seed.py`, `.../tests/test_switcher_list.py` | C-TENANCY, FWD-9 | WORLD |
| **FT-s-2** | The daily orchestration reads the live list each run, cross-checks it, writes a coverage record and the logout statuses, and tries the recovery once on a password refusal | `.../box/daily.py`, `.../box/run.py`, `.../tests/test_box_daily.py` | C-TENANCY, C-SIGNIN, FWD-3 | WORLD |
| **FT-s-3** | The in-run recovery: a CDP attach to the OS-launched Chrome unit, one full sign-in, logout on close | `.../signin_recover.py`, `.../tests/test_signin_recover.py` | C-SIGNIN | WORLD |
| **FT-s-4** | The backfill runner: per G the earliest date reached and the stop reason, a run cap and a daily sign-in cap | `.../backfill_run.py`, `.../tests/test_backfill_run.py` | C-BACKFILL | WORLD |
| **FT-s-5** | The box role may put the one per-G secret: one per-secret statement in the Terraform root, planned and applied | `infra/aws/terraform/canonical-fidelity-ec2/`; `org/critical_paths/change_management/`; `org/critical_paths/.open_deploys/` | C-TF | WORLD |
| **FT-s-6** | After FT-s-1, FT-s-2 and FT-s-5 are on the box: run the seed once on the issuer's GO, read the secret version (no value), turn the three schedule rules ON against that version, apply under `safe-apply` | the same Terraform root and ledger paths | C-TF, C-WINDOW, FWD-2 | WORLD |

Every order declares WORLD: GATE (xii) floors any `infra/` path there. Criteria are fixture tests plus structure checks; the live proof is the seed run and the first scheduled fire.

## 3. Edges

Data edges: `FT-s-1 -> FT-s-6`, `FT-s-2 -> FT-s-6`, `FT-s-5 -> FT-s-6` (delivery to the box by TO-FU-s-10 sits between). FT-s-1..FT-s-5 are built against the section 12 interfaces and fakes, so they start ready. Maximal paths: `FT-s-1 -> FT-s-6`, `FT-s-2 -> FT-s-6`, `FT-s-5 -> FT-s-6`, `FT-s-3`, `FT-s-4` (five). `fanout: 5 of 5 chains, cap 8`; four worker slots (~4 to ~7) take FT-s-1..FT-s-4, and FT-s-5 and FT-s-6 go to the CloudOps lane `0.7.0_AE_CloudOps~NFRA1` (rule 34).

## 4. Taxonomy record (rule 24)

- **(i) MECE:** the CTO's four items map to cells: switcher read + per-G secret = FT-s-1 (+ FT-s-5 for the put grant); daily logout = FT-s-2 (the close already logs out; the cell records it); schedule addendum = FT-s-6; backfill = FT-s-4; Andrew-direct v0.4.6's recovery = FT-s-3 (+ the hook in FT-s-2). 4 of 4 items covered. Not covered by design: gaps in section 1.
- **(ii) same grain:** one cell is one adapter with one write set. **(iii)** build and apply are separate orders. **(iv)** `complete` means fixtures plus structure pass; FT-s-6 and the live seed are the only cells that touch the world.

## 5. Battery

`comp-iam`: RUN at FT-s-5 (one statement added) and FT-s-6; BLIND to the root's computed names. `comp-schedule`: RUN at FT-s-6 (three rules turned ON). `comp-adversary`: RUN-NOT-APPLICABLE until FT-s-6 (the schedule is the first standing automated sign-in).

## 6. Addendum 2026-10-21 ~01:50Z (issuer, CTO relay of Andrew-direct MSTR 8912: the earliest date is found empirically, nothing waits on Andrew)

Andrew's method: on-demand exports at progressively earlier dates until the channel refuses or returns empty; land what it gives; the completion record names, per file type, the earliest business date landed, the total volume and any hard limit with its evidence. The measured calls already exist (`status.json` with a `dateString`, then `downloadExport.do`, `fetch.fetch_day`), so a past business day is one `fetch_day`. This closes gap 1 of section 1 for the first empirical pass without his capture.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-7** | The real backfill adapter over `fetch.fetch_day` (one business day per window; empty status = retention stop, refusal = entitlement stop) and `backfill_main.py`, the box command that signs in once, walks back through `backfill_run.run`, lands each served day and writes the completion record | `infra/aws/ec2/canonical-fidelity/backfill_adapter.py`, `.../backfill_main.py`, `.../tests/test_backfill_adapter.py` | C-BACKFILL, FWD-6 | WORLD |

Edge: `FT-s-4 -> FT-s-7` (the runner's interface, reference section 12). Executor: worker slot ~8.

## 7. Addendum 2026-10-21 ~02:50Z (issuer, CTO msg 8940: the firm split is Andrew's deliverable 1; GO on a daily-mode proof run on a config copy)

Measured on the box (names and indexes only): the account-number column is account 0, position 5, balance 0, transact 0; prices and security carry none. The proof run exercises, once, the stages that have only run on fakes: the switcher sweep over the 31 G numbers, the account lister's paging, the split under `fidelity/<firm>/`, and the coverage record, on a COPY of the box config so the scheduled fires keep running the raw land.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-8** | On the box: create `config.daily.json` (the config plus `mode`, `firm_labels`, `account_columns`), and on the issuer's GO run `box/run.py` once on it; read the per-firm counts | the same Terraform root and ledger paths (a ledger for the config file and the run) | C-TENANCY, FWD-9 | WORLD |

Edge: `FR-s-2 REPAIR 4 -> FT-s-8` (a delivery of `split.py` sits between). Executor: `0.7.0_AE_CloudOps~NFRA1` (rule 34).

## 8. Addendum 2026-10-21 ~03:45Z (issuer: the live proof run found no working page-2 form among eleven candidates, CloudOps row D1-S13)

The account lister's page 1 returns 2000 rows of 5204 available and none of the eleven candidate paging forms (FR-s-6 REPAIR 1) added a row. The form has to be MEASURED, not guessed again. The cheapest measurement that settles it is a read-only probe in one signed-in session on the current G: per candidate form its status, row count, new-row count and the response's own `pageResponse` and `statuses` codes; and the `accountNumber` search semantics (one request per leading character with `length` 1, reading only `available`), because the human UI may narrow by search and never page.

| cell | what it builds (one module) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-9** | `box/paging_probe.py`: one sign-in, page 1, the eleven forms and a 36-character prefix sweep, counts-only lines, logout in a finally | `box/paging_probe.py`, `tests/test_paging_probe.py` | C-TENANCY, FWD-9 | WORLD (infra path floor) |

Edge: `FT-s-9 -> FT-s-8` (the probe's measurement cuts the next lister repair). Executor: worker slot ~5; the run is 0.7.0_AE_CloudOps~NFRA1 under TO-FT-s-8 (amended); workstream fidelity-r3-paging, a write set disjoint from fidelity-r3-split.

## 9. Addendum 2026-10-21 ~05:00Z (issuer, CTO msg 8990: the G switch scopes the DOWNLOADS, not accountList; probe the export under three G numbers)

The 31-fold G switch left accountList at available=5204 every time (probe v2). The CTO ruled (msg 8990) that accountList is a rep-book view the switch does not scope, and that the six files pulled under a G are that G's book. The cheapest proof is one sign-in that, for the start G and two others, switches, reads the Export Status list for the business day and downloads account.txt only, printing counts and hashes beside the 5009-row landed file. Different per G = the per-G download IS the split.

| cell | what it builds (one module) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-10** | `box/g_export_probe.py`: one sign-in, switch, status list + account.txt download under up to four ordinals, hashes and counts only, restore in a finally | `box/g_export_probe.py`, `tests/test_g_export_probe.py` | C-TENANCY, FWD-9 | WORLD (infra path floor) |

Edge: `FT-s-10 -> FT-s-8` (the probe's result cuts the daily-mode design). Workstream fidelity-r3-gexport, a write set disjoint from fidelity-r3-split and fidelity-r3-paging. Executor of the run: `0.7.0_AE_CloudOps~NFRA1` under TO-FT-s-8 (amended).

## 10. Addendum 2026-10-21 ~06:00Z (issuer, CTO msg 8999: hold the G probes; drive the BACKFILL now at the rep level)

The CTO ruled (msg 8999) that the exports are rep-level and the G switch scopes nothing we export, and asked for backfill probe 1 now: the FT-s-7 walk (`backfill_main.py`), one sign-in, landing by content date under `fidelity/alongside/bronze/`, reporting the first earlier-date result as served, empty or refused with the date.

| cell | what it does (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-11** | On the box, once: `backfill_main.py` over the signed-in domain; read the completion record | the change-management ledger paths | C-BACKFILL, FWD-9 | WORLD |

Edge: none (the box code is already delivered). Executor: `0.7.0_AE_CloudOps~NFRA1` (rule 34). Workstream fidelity-r3-backfill-live, a write set disjoint from the others.

## 11. Addendum 2026-10-21 ~09:57Z (issuer, CTO msgs 9047 and 9048: the 09:45Z fire failed at the EventBridge-to-SSM hop)

The first scheduled fire (rule `fidelity-alongside-fetch-leg-1-daily`, 09:45Z) recorded FailedInvocations 1 and no automation execution: the target ARN as applied is `arn:aws:ssm:us-east-1:313476888478:automation-definition/fidelity-alongside-uploader-document` with no version suffix, and an EventBridge target for an SSM Automation document needs `:$DEFAULT` (or a version). The schedule role's policy already allows `ssm:StartAutomationExecution` on the document with and without a suffix and `iam:PassRole` on the automation role for `ssm.amazonaws.com` (the simulator's implicitDeny on PassRole comes from its missing `iam:PassedToService` context, not from the policy).

| cell | what it does (one fix) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-12** | `schedule.tf`: the three targets' `arn` gains `:$DEFAULT`; safe-apply; read back | `schedule.tf`, the ledger paths | C-SCHEDULE | WORLD |

Executor: `0.7.0_AE_CloudOps~NFRA1` (rule 34). Workstream fidelity-r3-schedulefix.

## 12. Addendum 2026-10-21 ~10:20Z (issuer: the suffix was not the cause; CloudTrail names it)

After the FT-s-12 apply the 10:15Z leg again showed FailedInvocations 1. CloudTrail (`StartAutomationExecution`, 10:15:02Z, assumed role `fidelity-alongside-schedule-role`) answers: AccessDenied, "not authorized to perform ssm:StartAutomationExecution on resource arn:aws:ssm:us-east-1:313476888478:document/fidelity-alongside-uploader-document because no identity-based policy allows" it. SSM authorizes the start on the DOCUMENT ARN (`:document/<name>`); the schedule role's policy allows only the `automation-definition/<name>` forms (which `aws_ssm_document.run.arn` yields). The same single document, one more ARN form.

| cell | what it does (one fix) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-13** | `schedule.tf`: the schedule policy's first statement gains the resource `arn:aws:ssm:<region>:<account>:document/<document name>`; safe-apply; read back by simulation | `schedule.tf`, the ledger paths | C-SCHEDULE | WORLD |

Executor: `0.7.0_AE_CloudOps~NFRA1` (rule 34). Workstream fidelity-r3-schedulepolicy.

## 13. Addendum 2026-10-21 ~10:32Z (issuer: the account-wide GetCommandInvocation grant was not needed)

The manual start of the run document at 10:27:27Z succeeded end to end (startInstance, waitForOnline, runWrapper; ALL_LANDED 6 of 6). CloudTrail for the Automation role shows ListCommandInvocations calls and NO `GetCommandInvocation` call, so the account-wide `ssm:GetCommandInvocation` grant added at 10:26Z (FT-s-13 step 2B, on the CTO's ask to cover every step) is not used and is wider than the role needs. FT-s-14 reverts it.

| cell | what it does | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-14** | `automation.tf`: remove `ssm:GetCommandInvocation` from `ListOwnCommandStar`; safe-apply | `automation.tf`, ledger | C-SCHEDULE | WORLD |

Executor: `0.7.0_AE_CloudOps~NFRA1`. Workstream fidelity-r3-automationrevert.

## 14. Addendum 2026-10-21 ~10:55Z (CTO msg 9065: the 10:45Z leg failed on a THIRD resource form)

CloudTrail for the 10:45Z leg (StartAutomationExecution 10:45:04Z, schedule role): AccessDenied on `arn:aws:ssm:us-east-1:313476888478:automation-execution/*`. SSM authorizes the start against three resource forms (automation-definition, document, automation-execution); the schedule policy names two. Today's three scheduled legs are spent; the schedule is unproven until tomorrow 09:45Z unless the ROLE path is proven by one one-shot run today.

| cell | what it does | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-15** | `schedule.tf`: add `automation-execution/*` to the policy's first statement; safe-apply; simulate all three forms; then ONE temporary one-shot EventBridge rule (same role, same target, same input), read its execution, delete it | `schedule.tf`, the ledger paths, one temporary rule | C-SCHEDULE | WORLD |

Executor: `0.7.0_AE_CloudOps~NFRA1`. Workstream fidelity-r3-schedulethird.

## 15. Addendum 2026-10-21 ~14:40Z (CTO msg 9101: the Historical backfill walk)

Measured 2026-10-21 (record `deliverables/2.0.0_SA_COO~P1/FIDUPL_historical_live_request_and_cap_probe_20261021.md`, and the PBL read below): `POST /ssc/importexport/wc/channel/export/v1/historicalExport.json` answers `S` and the files appear in the Export Status list of the REQUEST day. Custom (the daily's saved profile, `fileTypes` POS and PRC) returns `position<MMDDYY>.txt` and `prices<MMDDYY>.txt` in the standing layouts (62 and 44 comma columns, as-of date in column 0 = the requested date). Standard Format A (`exportFormat "1"`, `fileFormat "FL"`, `fileTypes ["PBL"]`, `indicatorName "AN"`) returns ONE fixed-length file `FI<MMDDYY>.psn` (positions as 156-character records and balances as 56-character records, CRLF; the as-of date is the six characters MMDDYY at offset 17 of every record; 96,822 records for 2026-10-15). A date past the data window is accepted and finishes COMPLETED WITH ERRORS; its download is a 125-byte `<status>` stub reading "The file you requested does not exist". Proven floor on 2026-10-21: positions 2026-06-15, prices 2026-06-18; balances unmeasured.

| cell | what it does | write set | PRC rows | risk |
|---|---|---|---|---|
| **FV-s-1** | `land.py` learns the `.psn` file: content date from MMDDYY at offset 17, address stem `position_balance_fl`, name `position_balance_fl.psn`, the same never-overwrite and run record | `land.py`, `tests/test_land_psn.py` | C-BACKFILL | WORLD (infra path floor) |
| **FV-s-2** | `hist_walk.py`: one sign-in, per trading day newest first one Custom POST (position, prices) and one Standard A POST (PBL), find the new rows in the request-day list, download, EMPTY on the does-not-exist stub, land by content date, three consecutive empties stop a type, state file resumes, one record | `hist_walk.py`, `tests/test_hist_walk.py`, `tests/test_hist_walk_seam.py` | C-BACKFILL | WORLD (infra path floor) |
| **FV-s-3** | CloudOps delivers the shipped set to the box and runs the walk until every type has stopped | ledger paths | C-BACKFILL | WORLD |

Chains: FV-s-1 then FV-s-2 (FV-s-2 calls `land.land_psn`) then FV-s-3: one chain, one worker queue for the first two. Executor of FV-s-3: `0.7.0_AE_CloudOps~NFRA1`. Workstreams: fidelity-r3-histwalk-build (FV-s-1, FV-s-2) and fidelity-r3-histwalk-live (FV-s-3).

## 16. Addendum 2026-10-21 ~16:40Z (CTO msgs 9117 and 9121, Andrew-direct: every Fidelity fact table; bronze JSON for the API surfaces)

Measured 2026-10-21 (records `FIDUPL_depth_experiments_20261021.md` and the 16:21Z session, section 16 of the worker face): transactions come from `historical-transactions` (ISO dates, one account per call allows 366 days; a batch of accounts is limited to 93 days, 200 accounts, and a 2,000-row answer is silently capped, so the build uses one account per call); realized lots from `retrieve-realized-gain-loss/detail` (500 lots per answer, `offset` does NOT page: completeness is read from `totalCount` and the date range is split until it matches); open lots from `open-lots` (limit 2,000, the unrealized surface); the book is the 5,013 accounts of the landed `account.txt` (the account list stops at 2,000 rows), 57 of 60 sampled accounts outside that list answer with line of business `IWS`.

| cell | what it does | write set | PRD rows | risk |
|---|---|---|---|---|
| **FW-s-1** | `api_walk.py`: one sign-in, per account the three API surfaces as raw JSON bronze (`api_transactions`, `api_realized_lots`, `api_open_lots`), floors and counts in one run record, state file resumes | `api_walk.py`, `tests/test_api_walk.py`, `tests/test_api_walk_seam.py` | C-BACKFILL | WORLD (infra path floor) |
| **FW-s-2** | CloudOps delivers it and runs it (chained, alternating with the Historical walk, never overlapping) until every surface has covered every account | ledger paths | C-BACKFILL | WORLD |

Chain: FW-s-1 then FW-s-2. The daily pull of these surfaces (a `--mode daily`, then the schedule) is a later cell after the backfill is proven. Executor of FW-s-2: `0.7.0_AE_CloudOps~NFRA1`. Workstreams: fidelity-r3-apiwalk-build (FW-s-1) and fidelity-r3-apiwalk-live (FW-s-2).

## 17. Addendum 2026-10-21 ~18:05Z (CloudOps runs 2 to 4: three robustness gaps in the two walks)

Observed in the live runs: (1) a failed sign-in prints only the exception class `SigninError`, with no step, so a failure cannot be read (the exception carries `failure_class`); (2) a transient 504 on the Export Status list read ended a Historical walk run as an error; (3) SSM cuts a command's stdout at 24 KB, so the STOP, CLOSE and OK lines of a long run are lost.

| cell | what it does | write set | PRD rows | risk |
|---|---|---|---|---|
| **FX-s-1** | both walks print the sign-in failure class; `hist_walk` retries a 5xx status-list read up to three times; both write their final lines to stderr as well | `hist_walk.py`, `api_walk.py`, `tests/test_walk_robust.py` | C-BACKFILL | WORLD (infra path floor) |

Workstream fidelity-r3-walkrobust. Delivered by CloudOps between runs on the issuer's message.
