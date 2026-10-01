# IRPT_BCKEND -- project sweep 5 remediations

<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. Graduated at sweep 5's L9 (ADJUDICATION_v19.md). W86-S1 (REMEDIATION_v14) is NOT closed here although ~P's round-26 packet calls it disarmed: CTO 103088 disarms it together with S216 on a per-account read that shows 09-29, and that packet reads the Inflection frontier at 09-27.

```json
[
  {
    "id": "IRPT_BCKEND-W88-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The estate grants the table to other roles, not to irpt-ycharts-generate. comparison_catalogue.py takes the read as an injected callable (read_classifications) defaulting to no names; entry_for_ticker and build_catalogue name from the model catalogue and from a wired reader, else carry the ticker verbatim. Until a reader is wired and the role granted dynamodb:Scan on the table, production serves the 4 model entries only and 100 percent of ticker entries take the verbatim path, not the measured 4 in 5.",
    "evidence": [
      "investigation row IRPT_BCKEND-W88-S2 (0.9.0_WK_IRPT_BCKEND~88): IB-yr-242: the etf-classifications half of the catalogue has no read the served role is known to hold (a DynamoDB table, not a file), so it is an injected port left unwired and every non-model ticker is served verbatim u",
      "ycharts/generate/entry.py:161-165 at HEAD: read_comparison_catalogue passes read_classifications=None by default (this seat's read)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Wire read_classifications for the catalogue and grant irpt-ycharts-generate a read on etf-classifications through its Terraform root; until then every non-model ticker is served verbatim.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W91-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MEASURED: the counterpart's fixture is keyed by concrete route paths and names all three routes. The published note is stale; the contract file is read-only to this lane (docs/contracts/investor-reporting/v1/ is outside the order's write grant) so it was not edited. The 13 portal-derived seam nodes were fixed by moving the TEST; nothing was refused, because the portal moved TOWARD the contract (it now sends the paths routes.json publishes). Owner of the stale note: IRPT_BCKEND (publisher of routes.json). INERT: nothing reads consumer_operation to gate.",
    "evidence": [
      "investigation row IRPT_BCKEND-W91-S1 (0.9.0_WK_IRPT_BCKEND~91): routes.json says NO CONSUMER OPERATION names GET /status, GET /status/{jobId} and GET /export/{exportId}/download, but the consumer's smoke fixture (12 entries) now keys all three.",
      "routes.json at HEAD: the three rows still read 'NO CONSUMER OPERATION names this route' (this seat's read ~19:1xZ)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Correct the consumer_operation notes on status-summary, status-job and export-download in routes.json (the consumer's fixture now names all three), in the contract's own versioned edit.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W91-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED: for four of twelve operations no response came back and no handler ran; the outcome is recorded as BLOCKED-BY-W2-S16, which a later reader will take as a handler defect. ARMED because the mis-read is what any future cell citing the suite's census will read. Not fixed here: it is not one of the order's six causes and the order forbids fixing a neighbouring defect. The fix is in the same file (resolve the module from staged_from when source_dir does not hold it); disarm owner is the issuer of the next round.",
    "evidence": [
      "investigation row IRPT_BCKEND-W91-S2 (0.9.0_WK_IRPT_BCKEND~91): analysis-requests, analysis-report, status-summary and status-job read BLOCKED-BY-W2-S16 (ROUTE_NO_HANDLER) in the paired suite because declared_entry_point looks for generate_installed.py / status_installed.py in source",
      "pytest -s _contracts/tests/test_seam_paired.py at CLOUD 000f3f6c5e: 62 passed and 4 ROUTE_NO_HANDLER lines (this seat's run): green, but four operations never reach a handler",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Resolve the entry module from staged_from when source_dir does not hold it, so the four operations reach their handler; disarm when the suite prints no ROUTE_NO_HANDLER.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W92-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED: the vocabulary reaches the dict, on the finding items, not at its top level. ARMED because the portal reads these findings and was not checked here (no portal in this grant): if it renders only known action strings, RESOLVE_RETRY_EXHAUSTED now shows no action where it showed REPLACE_FILE. A top-level answer would need the contract, the wire type portal/src/pages/InvestorReporting/contracts/wire/AnalysisUploadResult.ts and their pinned hashes to move together.",
    "evidence": [
      "investigation row IRPT_BCKEND-W92-S1 (0.9.0_WK_IRPT_BCKEND~92): The order's premise that the served dict can take top-level `actions` and `public_reason_code` is refused by the published contract: AnalysisUploadResult is closed (additionalProperties false), so the correction vocabula",
      "0 non-test files under portal/src/pages/InvestorReporting name RESOLVE_RETRY_EXHAUSTED or REPLACE_FILE (this seat's read): the render path is unread, not shown safe",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Read how the portal renders a finding's actions for RESOLVE_RETRY_EXHAUSTED, or obtain a CTO ruling to widen the closed AnalysisUploadResult contract.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W92-S4",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED offline only; no AWS call was allowed. If the live failure is another exception class, the answer stays UNEXPECTED. ARMED until the route is read back on RPT-2e21b52e.",
    "evidence": [
      "investigation row IRPT_BCKEND-W92-S4 (0.9.0_WK_IRPT_BCKEND~92): The absent-bundle fix is proven against a doubled store error (NoSuchKey/NoSuchVersion) on the report blob read; the live cause of S213 (RPT-2e21b52e) was not read back.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "After deploy, read GET .../analysis/RPT-2e21b52e.../sections and expect NOT_READY; any other code keeps the row armed.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-W94-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MEASURED: the three-failure whole-directory result is a collection-order interaction between fixtures modules, not a fault of the ledger change; the named criterion invocations are unaffected. Not fixed (outside the grant).",
    "evidence": [
      "investigation row IRPT_BCKEND-W94-S2 (0.9.0_WK_IRPT_BCKEND~94): The whole ycharts/generate/tests directory collected by one pytest run fails 3 tests on a `fixtures` module-name collision (AttributeError TENANT/OWNERSHIP), including the new test_receipt_ledger.py; each file run alone ",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "The round-30 hygiene cell (the issuer's list item 3): per-file invocation or a module-name fix for the fixtures collision, plus the two base-red generate test files.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W97-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-deploy halts on the ROSTER-level unacked messages (RED deploy-ledger notices for several other slugs and a 1.0.0_SA_CTO RE 103053) that a worker has no way to act on; HALT_ACK=1 was not used because overriding a gate is outside the grant. No comp-pipescript MATCH line was produced for the lib.",
    "evidence": [
      "investigation row IRPT_BCKEND-W97-S2 (0.9.0_WK_IRPT_BCKEND~97): safe-deploy.sh refused the worker serial with a HALT-GATE on unacked inbox messages; the order's aws s3 cp fallback was used",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "safe-deploy's HALT-GATE refuses a worker serial on roster-level unacked notices a worker cannot act on; the gate needs a worker rule (its issuer's acks, or an audited worker path).",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W97-S3",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The chain is no longer dead at step 3, but the FULL chain still ends failed at step 33, so INF_C_02..INF_D_11 (the rest of the served gold) did not run this run and will not on the next scheduled run while the guard holds. The guard is protecting served NNA and is correct to refuse until a decision is recorded; that decision is not this cell's.",
    "evidence": [
      "investigation row IRPT_BCKEND-W97-S3 (0.9.0_WK_IRPT_BCKEND~97): With the ship, the INF gold chain now passes the raw writers and dies at step 33 INF_C_01 on the NNA partition coverage guard",
      "2.0.0_SA_COO~P round-26 packet @6bd17a7d15: ROUTED in the slug as a served-data decision above the workstream",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Rule the NNA coverage excusal for accounts 866/769/1096 ($40,000 gross from partition 2026-09-24); 2.0.0_SA_COO~P records it in lib/nna_coverage_excusals.json once ruled; the guard is never disabled.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S229",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Ownership moves to 2.0.0_SA_COO~Y by Andrew's word; nothing in the world moves with it. The resident is stopped, the retained message is unconsumed, and any Analysis submission would sit unconsumed. This seat's earlier YCharts acts (st5 install, W25 principal, the stop) are committed and their ledgers are CLOSED.",
    "evidence": [
      "investigation row IRPT_BCKEND-S229 (2.0.0_SA_COO~P): RE-SEAT of IRPT_BCKEND-S226 (ARMED, disarm_owner 2.0.0_SA_COO~P): on Andrew's word the owner of YCharts is 2.0.0_SA_COO~Y, so S226's disarm_owner is now 2.0.0_SA_COO~Y. The resident stays STOPPED per CTO ruling 103150 un",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Keep the resident stopped until CTO 103150's three conditions hold: the auth cause named, the retained message handled on purpose, the restart under a ledger.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S230",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The credential is fine. A probe authenticates on the first attempt with no OTP branch taken. So S225's remedy is mis-aimed: there is no auth to fix. MEASURED: authentication succeeds, task=probe, max_reacquisitions=1. NOT MEASURED, and explicitly not claimed: that a FULL session capture for a job succeeds. My run was task=probe, which is a different task from the one the resident drives, so a probe authenticating does not prove the resident's capture would. The three live candidates for 03:36 are therefore (a) the max_reacquisitions=1 budget being spent, since the job's FIRST recorded operation was session_refresh, (b) a lease conflict on YC_LEASE_*, and (c) a task-specific failure the probe does not exercise. None is excluded yet.",
    "evidence": [
      "investigation row IRPT_BCKEND-S230 (2.0.0_SA_COO~Y): The YCharts credential AUTHENTICATES right now: a capture on the canonical host wrapper returned rc=0 with receipt {ok: true, task: probe, authenticated: true}. So S225's CAPTURE_FAILED:AUTH_FAILED was NOT a standing aut",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Name the 03:36Z CAPTURE_FAILED:AUTH_FAILED cause among the three live candidates (reacquisition budget, lease conflict, task-specific) before the first job under the service principal.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S231",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED: principal lifetime is WINDOW-scoped while job lifetime is QUEUE-scoped, and the two are not reconciled anywhere. A job that does not reach a terminal state inside its window becomes permanently unrunnable -- not failed, not refused to a user, just retrying a refusal until it DLQs. This is structural, not specific to tonight: every window has this property, and tonight is simply the first time a job outlived one. NOT MEASURED, and not claimed: how many earlier jobs died this way. W21's and W22's reports completed inside their windows, and W24's two failures were vendor-side, so no prior instance is established.",
    "evidence": [
      "investigation row IRPT_BCKEND-S231 (2.0.0_SA_COO~Y): A job cannot outlive its window. The walk deletes its ui-walk principal at window close, and the resident resolves each job's RECORDED principal before doing anything, so REQ-86f1ce70 now refuses CurrentAuthorityRefused/",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "A permanent authority refusal (ACTOR_NOT_FOUND, ACTOR_FIRM_NOT_ALLOWED) becomes a terminal, user-visible state instead of retry-until-DLQ (the issuer's round-30 item 2); REQ-86f1ce70 is handled on purpose.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S232",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A UI-walk credential's lifetime is a browser session; a queued job's lifetime is until it is terminal. Binding the second to the first is what strands jobs (S231: two of them, three days apart). MEASURED: the service-principal class, the live svc- account, the disabled durable walker, and the absence of any record deciding the reuse. NOT MEASURED, and not claimed: whether the `service` userType as ticket_center models it is accepted by the IRPT authorizer and by current_authority.decide() unchanged. That is the first thing the remedy must establish, and it is a code read plus one test, not a guess.",
    "evidence": [
      "investigation row IRPT_BCKEND-S232 (2.0.0_SA_COO~Y): Opal already has a first-class SERVICE-PRINCIPAL pattern -- a `service` userType with firmId null and an allowedFirmIds scope -- used by at least three services, plus a live svc- account since July. IRPT Analysis diverge",
      "2.0.0_SA_COO~Y round-29 packet @a8c85aaa9e: the principal's login 200; 24 of 24 roles explicitDeny on its secret",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "The identity model is ruled and applied: svc-irpt-analysis exists (ledger irpt-svc-analysis-principal-20260930 CLOSED @4303ef0b2e). Disarm when the first job accepted under it reaches a terminal state.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S233",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "YCharts access existed and still does, shared, with its own freshness instrument. The Analysis journey duplicated the credential layer rather than using it. NOT MEASURED, and this is the hinge: whether YCharts publishes ANY report/export endpoint. Establishing it is a vendor probe and needs Andrew's per-use word, so the duplication may be PARTLY forced -- a rendered PDF with no REST equivalent genuinely needs the web-app path. NOT CLAIMED: that the shared gateway credential carries the entitlements the Analysis journey needs, or that one account can hold both sessions without eviction. S225's double-eviction reading makes the second question live rather than rhetorical -- two sessions on one vendor account is itself a candidate cause for an eviction, and nobody has tested that.",
    "evidence": [
      "investigation row IRPT_BCKEND-S233 (2.0.0_SA_COO~Y): There are TWO YCharts sessions in this estate. The opalgateway already runs Andrew's stated pattern -- a shared credential at ycharts/credentials driving real YCharts REST endpoints, with a freshness check -- while IRPT ",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Rule which credential and call shape the Analysis journey uses (the shared gateway session plus REST for data, browser automation for the export only), or show one account holds both sessions without eviction.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S235",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "For T = 2026-09-29 the silver had not landed 3h44m after its usual hour, the fire refused correctly (no guess, no stale read), and the served 49F gold is unchanged. Nothing is broken on the producer's side; the upstream silver landing is late or missed and its cause is not read here (off-task for this seat). NOT MEASURED: whether the Schwab source files for 09-29 reached OneDrive/S3 (the 49-schwab-conv ingest's input) and whether the conversion ran and failed or never ran. NOT CLAIMED: staleness under the freshness gate (it reads PASS); the claim is a departure from the feed's own measured hour.",
    "evidence": [
      "investigation row IRPT_BCKEND-S235 (2.0.0_SA_COO~P): opal-data-assets schwab/08335338/silver/dim_position/date=2026-09-29/ is ABSENT at 2026-09-30 13:3xZ; every earlier trading day's partition landed the next calendar morning at ~09:46Z (date=2026-09-28 at 09-29 09:46:44Z,",
      "s3api list-objects-v2 opal-data-assets schwab/08335338/silver/dim_position/date=2026-09- at ~19:1xZ (this seat): newest date=2026-09-28, landed 09-29 09:46:44Z; date=2026-09-29 still ABSENT, 33 h past the feed's measured hour",
      "irpt/49financial/gold/holdings_performance_manifest/ newest date=2026-09-28 (written 09-29 14:45Z)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Place the Schwab silver conversion's owner (the 49-schwab-conv ingest) and land date=2026-09-29; the producer's day math never revisits a missed day, so 09-29 is a permanent gap unless it is run.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S236",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The SECOND limb of the refusal clause is the true one. The producer CAN emit both historical days (rc=0, correct row counts) -- it simply cannot emit the four columns, because on these two dates it has no OK row to attach them to, and manufacturing a BMV to create one is forbidden by the engine's own REFUSE-not-fabricate guard and by GLD-a-4 / GLD-b-3. Re-emitting through the runner would rewrite both partitions with equivalent 11-column content, moving nothing and burning the two ETags for no gain. So: no S3 write was made, no deploy ledger was opened (there is no deploy to ledger), and both P26-3-AC1 and P26-3-AC2 stay FAIL by the clause rather than by an unattempted act.",
    "evidence": [
      "investigation row IRPT_BCKEND-S236 (0.4.0_DS_ClientPlatform~S): TO-IB-pr-263's refusal clause is met: the four columns were NEVER populated for these two runs BY DESIGN and the producer's own path cannot emit them. Both gap partitions carry ZERO OK rows (date=2024-07-08: 4,074 of 4,0",
      "2.0.0_SA_COO~P round-26 packet @6bd17a7d15: IB-pr-263 SUPERSEDED; S236 closes it",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "TO-IB-pr-263 is superseded (@ed0be5b557) and no column fill is owed. Rule the status vocabulary at the series' first partition: 4,074 rows of date=2024-07-08 read REFUSED-NO-BMV where NO-PRIOR-TRADING-DAY is true.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S237",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "For the window (2025-01-08, 2025-01-10] the CF term is INCOMPLETE by construction. The window spans two calendar days because the calendar correctly skips the closed one, but c02 reads a SINGLE day's flow_ledger, so every external flow that settled on 2025-01-09 is omitted from CF while its value is present in EMV. 44 served returns carry the resulting error, up to 91 percentage points in a single day. The same shape is NOT present at the other gap date: for date=2024-07-08 the flows are inside the 2024-07-09 run's BMV baseline, so nothing is orphaned there -- which is why this row is about 2025-01-09 alone.",
    "evidence": [
      "investigation row IRPT_BCKEND-S237 (0.4.0_DS_ClientPlatform~S): SERVED DEFECT, found while grounding S236: on 2025-01-10 the 49F twr_daily gold renders client CASH FLOWS as PERFORMANCE for 44 accounts, because the flows settled on 2025-01-09 -- a day the NYSE was CLOSED -- and NOTHIN",
      "2.0.0_SA_COO~P round-26 packet @6bd17a7d15: 'no IRPT_BCKEND cell; the CORRECT computation is written into IRPT_DASHBD DB-b-1's face @51c05d1530; the parity oracle's exposure is named for the CTO'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Place the served defect: 49F twr_daily date=2025-01-10 reads client flows as performance for 44 accounts (up to +91 pp). ~P states no IRPT_BCKEND cell (the engine is retired for IRPT serving by IB-pr-201); whoever serves twr_daily or its period returns owns the correction.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S239",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Neither branch as written. parity_period_returns LOADS the 2025-01-09 rows and then makes them harmless by a THIRD mechanism -- value-based neutrality -- which discards the status hole without refusing the window. The result is the bad branch's outcome (full propagation) reached by a path the question did not anticipate. The question's two-branch framing was itself the defect in my earlier reasoning: I assumed loading the non-OK rows would protect the window, because c02's own linker behaves that way, and the period module deliberately does not.",
    "evidence": [
      "investigation row IRPT_BCKEND-S239 (0.4.0_DS_ClientPlatform~S): ANSWERS the open question S237 left as the disarm owner's first act: the error DOES propagate into period returns -- it does not stop at the daily grain. parity_period_returns.py decides neutrality BY VALUE (r_net.isna()",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "The same placement as S237, at the period grain: parity_period_returns.py links the 2025-01-10 row as live (value-neutral linking), so every QTD/YTD/1Y/SI window spanning it carries the error on Opal's side of the Black Diamond parity comparison.",
    "owner": "1.0.0_SA_CTO",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-S238",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "MEASURED: the principal can READ another firm's directory population through the API today (1 entry of inflection served), and could SUBMIT an Analysis upload for inflection at K4 (the API admits the selected tenant); the resident would then refuse the JOB at decide() with ACTOR_FIRM_NOT_ALLOWED (293), so no vendor call and no report could be produced for a non-cottonwood firm -- but the upload, the normalized input and the request row would exist. CORRECTION TO THE PACKET'S CLAIM: 'recorded, not enforced' is now HALF-enforced -- enforced at the job (resident), not at the API. The window's three bodies are cottonwood and are unaffected; what the CTO re-reads is whether a resident-only mechanism plus an API-side convention is enough to open, or whether the API half (P's surface) is a precondition.",
    "evidence": [
      "investigation row IRPT_BCKEND-S238 (2.0.0_SA_COO~Y): CTO half condition 4 FIRED: under the new svc-irpt-analysis principal (allowedFirmIds cottonwood), one API read of an INFLECTION resource SUCCEEDED -- GET directory/search?selected_tenant=inflection&limit=1 served 1 infl",
      "2.0.0_SA_COO~Y round-29 packet @a8c85aaa9e: the negative control FIRED (1 inflection directory entry served)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "The API enforces allowedFirmIds for a service principal (_authz/served.py selected_tenant outside the list answers 403), per CTO 103318 as the top cell of ~P's next issuance (~Y's patch @4a3cabe67d); disarm on the CTO's re-read of ~Y's live negative control.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v30",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v30"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  }
]
```
