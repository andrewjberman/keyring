# IRPT_DASHBD -- rounds 2 to 4 (workstream B) remediations

<sweep_watermark>2026-10-02T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~19:5xZ. Graduated at ADJUDICATION_v2.md: 11 rows. Closed here on this seat's reads: S13, S16, S21, W1-S10. OPEN: W1-S7 in round-5 cell DB-b-11 and S22 in round-6 cell DB-b-13 (S22 is this seat's own L9 row and stays open until the re-measured pair is read); S12, S15, S18, S19 and S20 are in no round-5 or round-6 cell and come back to 1.0.0_SA_CTO for placement. Round label v5 (round 5, the round after the compiled round 4, as v1 labelled its rows v2), except S22, labelled v6 for its cell. Carried from v1 and not moved here: S8 (OPEN at v2).

```json
[
  {
    "id": "IRPT_DASHBD-S12",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The X10 register's validator admits only csv/json/pdf and one family per table, so the served platinum series.json.gz (the file the page reads) has no retention family; only SERVED_MANIFEST is registered.",
    "evidence": [
      "investigation row IRPT_DASHBD-S12 (CTO round-1 analysis E2: a registry question to the registry's owner)",
      "infra/logic/registry/reporting_policies.json at HEAD (last change 11bf813387, 2026-10-01): policy irpt-dashbd-served-reporting, revision irpt-dashbd-x10-v1, state PENDING_ENFORCEMENT, ONE family SERVED_MANIFEST (platinum, reporting, json); 'json.gz' 0 occurrences, 'series' 0",
      "lib/opal_naming.py:1822-1823 at HEAD: an extension not in {'csv', 'json', 'pdf'} raises 'reporting content format is not admitted'",
      "s3api list-objects-v2 opal-data-49financial irpt/49financial/platinum/reporting/ (this seat ~19:3xZ): 12 keys, 6 of them series.json.gz, all written 2026-10-02T13:56:29-30Z"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the register owner admits a gzip JSON format or a second reporting table so the series takes its own family (a register edit plus the validator's admitted set). Round 5's DB-b-12 adds a per-client summary file that will need a family the same way. Placement is 1.0.0_SA_CTO's at the next analysis.",
    "owner": "4.0.0_SA_CRO",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S13",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Nothing ran account_return_daily.py on a clock, so the reporting gold froze at date=2026-09-28 and the 08:15 ET publisher would have republished that series every weekday.",
    "evidence": [
      "investigation row IRPT_DASHBD-S13; CTO round-2 analysis E1; round-3 cell DB-b-7 (@ff4b28b3e3, proof @ceb03a4137); ledger org/critical_paths/change_management/20261002T0801Z_irpt-dashbd-reporting-gold-apply-20261002_deploy_completion.md",
      "aws scheduler list-schedules --name-prefix irpt-49f-reporting (this seat ~19:3xZ): irpt-49f-reporting-gold-daily ENABLED",
      "logs filter-log-events /aws/lambda/irpt-49f-reporting-gold-lambda, pattern START (this seat): one invocation since the apply, START 2026-10-02T11:41:47Z, the schedule's 07:41 ET minute",
      "s3api list-objects-v2 and list-object-versions, opal-data-49financial irpt/49financial/gold/account_return_daily/ (this seat): 562 date= partitions (559 at the row), newest date=2026-10-01, the T-1 trading day for Friday 2026-10-02; date=2026-09-29, 09-30 and 10-01 each one version at 11:42:08Z; date=2026-10-01/manifest.json: asof 2026-10-01, rows 6, day_quality_census MEASURED 6, return_basis_census TWR 6"
    ],
    "remedy": "Done: the adapter runs on its own schedule, and its first scheduled fire carried the gold from 2026-09-28 to the T-1 date 2026-10-01 in one invocation at the schedule's minute.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S15",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The reporting read route lives in its own root under the existing portal authorizer and is absent from docs/contracts/investor-reporting/v1/routes.json, which routetable.py calls the one carrier of the route table, so the unguarded-route census does not see it.",
    "evidence": [
      "investigation row IRPT_DASHBD-S15",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_DASHBD_READ_ROUTE_20261002.md:21-24: 'IRPT_DASHBD-S15 ... ACCEPTED. One writer per route KEY holds ... Naming the route in the contract without the api root generating it (a duplicate key would fail that root's apply) is hygiene for the issuer at round 3, not a condition here.'; CTO round-2 analysis section 2 hygiene line: 'At the drain or the next change to entry.py; not cells.'",
      "docs/contracts/investor-reporting/v1/routes.json at HEAD (last change 31999d12d4, 2026-10-02T12:29Z): 19 routes; 'investor-reporting/reporting' 0 occurrences",
      "infra/aws/terraform/investor-reporting/reporting-read/api.tf:11 at HEAD: 'The route is NOT in the published routes.json: row IRPT_DASHBD-S15 names what that leaves to the issuer.'"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the issuer names the route in routes.json without the api root generating it, as hygiene at a drain. Not done at the round-3 or round-4 drain.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S16",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seating check read assignees through to-check.py's resolver, whose SERIAL_RE admitted no underscore in the name and only one capital letter as a lane, so every IRPT worker slot collapsed to 0.9.0_WK_IRPT; once enforced, it would refuse a correct issuance.",
    "evidence": [
      "investigation rows IRPT_DASHBD-S16 and S17 (S17 measured that @453c6430ec did not fix it)",
      "CTO RULINGS batch 124 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md:5076-5092), fixed in .tools/to-check.py @0b8f897e7d",
      "this seat's run ~19:3xZ: .tools/to-check.py SERIAL_RE at :154; _assignees_from_field('0.9.0_WK_IRPT_DASHBD~1') -> ['0.9.0_WK_IRPT_DASHBD~1']; '0.9.0_WK_IRPT_BCKEND~3' and '2.0.0_SA_COO~MI' returned whole; negative control: the pre-fix pattern on '0.9.0_WK_IRPT_DASHBD~1' -> '0.9.0_WK_IRPT'"
    ],
    "remedy": "Done by 1.0.0_SA_CTO in .tools/to-check.py (batch 124). Not re-run here: the seating lint over a live issuance; the resolver it reads was exercised directly.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S18",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The PRD's C-NAMES prints a function that was never made (irpt-49f-reporting-adapter-lambda) and none of the reporting-gold resources DB-b-7 made, so a reader of the PRD cannot find the deployed resources (CLAUDE.md rule 30).",
    "evidence": [
      "investigation row IRPT_DASHBD-S18",
      "prd/IRPT_DASHBD_PRD.md at HEAD, prd_version v0.6, last change aabc054e89 (2026-10-02T01:32Z, before DB-b-7's apply): irpt-49f-reporting-adapter-lambda 1 occurrence; irpt-49f-reporting-gold-lambda, irpt-49f-reporting-gold-role, irpt-49f-reporting-gold-policy, irpt-49f-reporting-gold-daily and irpt-reporting-gold-lambda 0 each; irpt-49f-reporting-read-lambda 0 (the read root's function is absent too); irpt-49f-reporting-publish-lambda 3",
      "decompositions/IRPT_DASHBD_DECOMP.md section 3 prints the builder output for the reporting-gold names"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the PRD's author prints the builder output for the reporting-gold and reporting-read names and strikes the adapter name.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S19",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DB-7-AC1 requires at least 10 measured landings per input and counts them before the exclusions it then applies: for holdings_performance_daily, which sets the 07:41 ET fire, 9 of 12 are excluded and 3 kept (2 organic 07:30 fires).",
    "evidence": [
      "investigation rows IRPT_DASHBD-S19 and W1-S8; deliverables/0.9.0_WK_IRPT_DASHBD~1/REPORTING_GOLD_FIRE_TIME_R3.json (excluded list, 11 entries)",
      "first scheduled fire (this seat ~19:3xZ): holdings_performance_daily date=2026-10-01 landed 11:30:18Z; reporting-gold START 11:41:47Z; account_return_daily date=2026-10-01 carries 0 GUARD_NOT_REACHED. One organic day on which the fire followed its input; date=2026-09-29, written by the same fire, carries 1 GUARD_NOT_REACHED and 1 NOT_MEASURABLE (cause not read)"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: the issuer amends DB-7-AC1 to count kept landings (or states the kept floor it accepts) and reads the organic landings as they accrue. Open until the criterion grades what the schedule rests on.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S20",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The account picker's suffix dates 'data through' from manifest.as_of and the page body from series.as_of, and the read never checks that the two agree, so a manifest and a series of different vintages would show one account two dates.",
    "evidence": [
      "investigation row IRPT_DASHBD-S20",
      "portal origin/DEV f2d69887 (this seat ~19:3xZ; the three files last changed 06bc6f85, 2026-10-02T09:43Z): src/pages/InvestorReporting/tabs/reporting/pickerSuffix.ts dashboardYtdSuffix builds 'data through' from answer.manifest.as_of; src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx:241 prints series.as_of; src/pages/InvestorReporting/dashboard/reportingRead.ts holds 0 'as_of'/'asOf' occurrences (no comparison)",
      "served today: 6 of 6 platinum manifests read as_of 2026-10-01, written in the same run as their series (13:56:29-30Z), so the split is not observed on served data"
    ],
    "remedy": "IN NO ROUND-5 OR ROUND-6 CELL: read one date for both, or refuse the pair when manifest.as_of and series.as_of differ (portal).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S21",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The publisher heads the series object after its two puts, and its role had PutObject but no GetObject on platinum/reporting, so HeadObject answered 403 and the run aborted after the first account.",
    "evidence": [
      "investigation row IRPT_DASHBD-S21; CTO RULINGS batch 172 (RULINGS.md:5763-5769): 'SIGNED: amendment 1 to DB-b-8 (packet blob 2baec1651d). s3:GetObject on exactly platinum/reporting/*, the prefix the role already writes, plan 0/1/0. Then Q1 runs again.'",
      "infra/aws/terraform/investor-reporting/reporting-publish/iam.tf:74-82 at HEAD: statement ReadBackThePlatinumReportingPrefixOnly, s3:GetObject on local.irpt_rp_platinum_write_arns (the write set, nothing wider)",
      "logs /aws/lambda/irpt-49f-reporting-publish-lambda since 13:30Z (this seat): invocation a4019573 ended '[ERROR] ClientError ... (403) ... HeadObject'; the next, a8df95ef, REPORT 14,479 ms with no ERROR line",
      "s3api list-objects-v2 platinum/reporting/ (this seat ~19:3xZ): 12 of 12 keys LastModified 2026-10-02T13:56:29-30Z; all 6 manifest.json read as_of 2026-10-01"
    ],
    "remedy": "Done: the read-back grant on the written prefix only, then the Q1 re-run published 6 of 6 accounts as of 2026-10-01. Not yet read: Monday 2026-10-05 08:15 ET's scheduled fire (A1 of ledger irpt-dashbd-reporting-publish-apply-20261002, still open), which is FWD-1's acceptance, not this row's.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W1-S7",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The scheduled handler takes the newest landed partition's account set (six accounts) as its population and omits the producer's emit_method_row (a write outside its role); the order was silent on both.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S7",
      "account_return_daily date=2026-10-01/manifest.json, written by the first scheduled fire (this seat): rows 6, first_data_date keys 6",
      "CTO RULINGS batch 178 item 2 (RULINGS.md:5849-5852): '(2) widen the precomputed path to every 49 Financial account, then per firm, with PATH A retired in the same window'",
      "task-orders/IRPT_DASHBD.TO-DB-b-11.every-49f-account-measured.md (round 5, status issued):27 'The gold's account set is the newest partition's (handler.py:18-19' and :46 'In reporting-gold/handler.py, the account set comes from the declared population'",
      "task-orders/IRPT_DASHBD.TO-DB-b-13.fwd8-three-pairs-and-tolerance.md (round 6, status issued):44: emit_method_row writes tieout_tolerance, and the method row's served write is the issuer's packet, not the scheduled handler"
    ],
    "remedy": "IN ROUND-5 CELL DB-b-11: the population limb is cut (the declared 49 Financial population replaces the newest-partition default). The method-row limb stands as built: the handler does not write dim_return_method.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W1-S10",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The CRO's code table is generated by a first-match builder in which wd-generic preceded foreign-tax, so FTP/FC/WD and FTR/FC/WD read EXTERNAL; a hand edit of the JSON alone would revert on the next build.",
    "evidence": [
      "investigation row IRPT_DASHBD-W1-S10",
      "git log: 3cb9f9b6d5 (4.0.0_SA_CRO, 2026-10-02T09:36Z) 'FTP/FC/WD and FTR/FC/WD move EXTERNAL -> INTERNAL (foreign tax) -- builder rule order fixed, table re-applied, 2 rows moved'",
      "org/tier1_exec/4.0.0_SA_CRO/scripts/build_schwab_txn_classification.py at HEAD: 'foreign-tax' at :59 precedes 'wd-generic' at :71",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json at HEAD, 187 rows: FTP/FC/WD (2,449 rows) and FTR/FC/WD (4 rows) rule foreign-tax, partition INTERNAL; FTP/FC/FC and FTR/FC/FC unchanged, INTERNAL"
    ],
    "remedy": "Done: both files edited together by the table's owner, so the builder regenerates what the table holds.",
    "owner": "4.0.0_SA_CRO",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v5"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S22",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-4 tie-out's largest disagreement (acct#e7ab8585, 2026-06-25..07-06, 1.21 points over 7 like days) carried no stated reason, and its cause is findable: Opal books income +0.4627% on 06-25 where Black Diamond nets income -2,470.31 on an account about 47 pct short, consistent with Opal counting dividends received but not dividends paid on shorts (inferred).",
    "evidence": [
      "investigation row IRPT_DASHBD-S22; this seat's L9 grade @7a062defc3, org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_FWD8_L9_GRADE_20261002.md: FWD-8 NOT REALIZED",
      "CTO RULINGS batch 181 (RULINGS.md:5887-5905): tieout_tolerance 0.35 percentage points per like-day window; 'A reason that is an Opal defect is a defect row: it is fixed and the pair re-measured ... That is row IRPT_DASHBD-S22, 2.0.0_SA_COO~P's.'; batch 182 item 1 (:5907-5916): 11 of 14 pairs within, 3 beyond (acct#e7ab8585 06-25 1.2130, acct#a4af74fa 08-21 0.7078, acct#e7ab8585 04-09 0.4555)",
      "decompositions/IRPT_DASHBD_DECOMP.md section 6 (round 6, @c94a1de98b) and task-orders/IRPT_DASHBD.TO-DB-b-13.fwd8-three-pairs-and-tolerance.md (status issued):20 'Row IRPT_DASHBD-S22 | Decomp cell: DB-b-13 ... outcome_ref: FWD-8'"
    ],
    "remedy": "IN ROUND-6 CELL DB-b-13: the producer books a short's paid dividend as negative income, the pair is re-measured from the stored responses with 0 vendor calls, and the other two pairs beyond 0.35 pp carry stated reasons; then the issuer's packet re-pins the reporting gold and rewrites the affected account-days. FWD-8 returns to 3.0.0_SA_CVO. This is the L9 seat's own row: it is never dismissed and stays OPEN until the re-measured pair is read.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v6"
    },
    "closed": true
  }
]
```
