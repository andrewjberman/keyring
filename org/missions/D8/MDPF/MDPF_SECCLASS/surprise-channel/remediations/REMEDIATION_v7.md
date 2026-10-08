# MDPF_SECCLASS -- rounds 9-12 remediations (the graduations held by the gate)

<sweep_watermark>2026-10-08T13:01Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T13:01Z. These rows were graded at ADJUDICATION_v8 (round 9), v9 (round 10) and v10 (round 12) and drafted
there. They are landed now that TO-DEPLOY-e21 (superseded by e65), e42 and e66 are terminal on origin e7cf815088 (2.0.0_SA_COO~M1 msg
893). Every verdict rests on the reads recorded in those compiles. Carried unchanged: every row of REMEDIATION_v1..v6 not closed.

```json
[
  {
    "id": "MDPF_SECCLASS-W35-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The clean-name write v2 set carries registered/trademark signs in name values it would write to etf-classifications; CLAUDE.md bars non-ASCII in production AWS, and the check pins current_name to the live bytes, so the two cannot both hold.",
    "evidence": [
      "python byte scan of org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv at this HEAD: 10 bytes > 127, 4 characters > 127 (the row says 2 characters; the file at HEAD carries 4)",
      "investigation row MDPF_SECCLASS-W35-S3 (0.9.0_WK_MDPF_SECCLASS~35)"
    ],
    "remedy": "The e48 write half rules per key: strip the mark from the written clean name (and amend the check to compare the source name), or record the exception; no write before. Close when: the e48 half names the 4 characters' disposition and the written values read ASCII, or the exception is recorded in the half.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W31-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "E_18 hands the canonical producer only tickers absent from the old list and then looks them up in that same list, so the producer path for a first-held security returns nothing on every host, today, before any writer stops.",
    "evidence": [
      "data/black_diamond/scripts/gold/E_18.detect_new_securities.py at this HEAD: :215 `known = load_known_tickers(table)`, :247 `if not pk or pk in known:` (skip), :289-291 plan_rows(... bd_securities_lookup=default_bd_securities_lookup(BD_SECURITIES_TABLE))",
      "investigation row MDPF_SECCLASS-W31-S1 (0.9.0_WK_MDPF_SECCLASS~31)"
    ],
    "remedy": "Round-10 item 1: switch BD E_18 to the canonical lookup (REPOINTABLE) with a shipped caller. Close when: a BD gold run writes at least one 'e18-scheduled' row, or E_18 at HEAD passes canonical_lookup to plan_rows and the producer's live canonical count reads above 0.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W31-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A recurring producer (the rivalfunds new-security Lambda) does write the table, but only for securities an ETF holds; a client-first-held security outside every ETF still has no recurring producer, and the AI runner has no schedule.",
    "evidence": [
      "aws scheduler get-schedule mdpf-secclass-new-security-daily (2026-10-07 ~12:5xZ): ENABLED cron(0 10 ? * MON-FRI *)",
      "investigation row MDPF_SECCLASS-W31-S2 (0.9.0_WK_MDPF_SECCLASS~31)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 states in the round-9 analysis which recurring route classifies a client-first-held security (E_18 after its switch, or a scheduled AI run under its vendor word). Close when: the analysis names the route and the census line 'CANONICAL-PRODUCER NONE' is restated with this scope.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W31-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Daily GetItem bursts in the thousands on bd-securities are unattributed: no reader in the repo census accounts for them, so the census that gates the old list's removal may be missing a reader.",
    "evidence": [
      "the row's CloudWatch series (GetItem 5,337 on 09-29, 7,034 on 10-06) is the census's own instrument and was not re-pulled here; this seat's read is the E_18 code at :289-291, which issues per-candidate GetItems in the low single digits per run",
      "investigation row MDPF_SECCLASS-W31-S3 (0.9.0_WK_MDPF_SECCLASS~31)"
    ],
    "remedy": "Before the table is removed, attribute the bursts (CloudTrail data events on the table for one burst day, read-only) or record the BLIND in the removal half. Close when: a named caller for the 10-06 burst, or the removal half carries the unattributed-reader risk with its rollback.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W31-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "B_01b's unguarded scan of bd-securities is fatal to the nightly BD chain if the table goes, so the writer stop (SC-e-35) is a hard prerequisite of any table removal.",
    "evidence": [
      "data/black_diamond/scripts/gold/B_01b.classify_new_securities.py:155-160 scan_existing_keys does table.scan with no try; :256 calls it",
      "data/black_diamond/scripts/gold/gold_dispatch.sh:165 NONFATAL_IDS=\"E_18\" (B_01b absent)",
      "investigation row MDPF_SECCLASS-W31-S4 (0.9.0_WK_MDPF_SECCLASS~31)"
    ],
    "remedy": "Order the removal after SC-e-35 lands (B_01b no longer scans), or make B_01b's scan non-fatal; state the order in the removal half. Close when: B_01b at HEAD no longer scans bd-securities, or the removal half names SC-e-35 as its precondition.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W36-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The contract now lists Cash as a sub-class under both cash and fixed_income; which is meant is unruled (packet round-10 item 6).",
    "evidence": [
      "org/standards/MDPF_SECCLASS_CONTRACT.json at this HEAD: fields.sub_asset_class.values_by_class.cash = ['Cash','Money Market','T-Bill']; 'Cash' is also in values_by_class.fixed_income",
      "investigation row MDPF_SECCLASS-W36-S2 (0.9.0_WK_MDPF_SECCLASS~36)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 rules whether Cash is a sub-class of cash, of fixed_income, or both, and the contract is amended to match. Close when: the ruling is recorded and the contract's two lists agree with it.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W36-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-15 cannot reach zero by the planned AI run: 99 held keys fit no declared key form (cottonwood's $76.8M among them), and 150 AI keys overlap the old-list AI set, so one set's model calls are wasted.",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD15_AI_PLAN_{49financial,cottonwood,inflection}_20261007.json: ai_entries_also_in_old_list 46+45+59 = 150; route_amount_usd UNPLACED-KEY cottonwood 76,843,740.63; claim inferred",
      "investigation row MDPF_SECCLASS-W36-S3 (0.9.0_WK_MDPF_SECCLASS~36)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 rules on a key form (or an explicit out-of-scope list) for the 99 UNPLACED keys; the e49 and e32/e50 halves de-duplicate the 150 before either AI run. Close when: the 99 have a ruled path, and the two AI write sets are disjoint in their halves.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S54",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The issuer's own provisioning fetched ~487 packages from the public npm registry once (round 8); the tool still offers the install mode, so it can recur until the mechanism refuses it.",
    "evidence": [
      ".tools/wk-provision.sh at this HEAD: lines 149-152 still offer `--node-modules install`, which runs `bun install --frozen-lockfile` (a public-registry fetch on a cache miss); no guard refuses it",
      "laptop 1.0.0_SA_CTO msg 106215 (relayed to every dell1 seat, 0.0.0_AB_MSTR~DELL1 msg 225, 12:22Z): bun only inside a portal tree with node_modules, no registry probe; the disarm is a NFRA_CTLPLN cell at laptop 2.0.0_SA_COO~C",
      "investigation row MDPF_SECCLASS-S54 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "The NFRA_CTLPLN cell at 2.0.0_SA_COO~C makes the registry fetch refusable (its loopback-listener control); meanwhile 2.0.0_SA_COO~M1 provisions with `link` or `none` only; Andrew is told of the egress. Close when: the NFRA_CTLPLN cell's control passes on dell1, or wk-provision.sh refuses `install` on a Dell.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v13"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S58",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 0.7.0 (Cash is a sub-class of cash only) puts 3 DIRECT rows of SC-e-50's held reclassification set (CSHI, FIGXX, FISXX) outside the bound, planned fixed_income/Cash.",
    "evidence": [
      "investigation row MDPF_SECCLASS-S58 (2.0.0_SA_COO~M1), read by this seat at the round-10 compile (ADJUDICATION_v9 header)"
    ],
    "remedy": "Re-plan the e32/e50 set under contract 0.7.0 before its half goes to signature (CSHI cash/T-Bill; FIGXX, FISXX cash/Money Market). Close when old_list_held_census_check.py set reads ok=True.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W41-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The PRD and worker face place the hedge->alternatives fold in data/black_diamond/scripts/gold/lib/etf_classifier.py; it is in opal-partners-data's own etf_classifier.py (:99, :108), live on the /composition routes, off the page's route.",
    "evidence": [
      "investigation row MDPF_SECCLASS-W41-S2 (0.9.0_WK_MDPF_SECCLASS~41), read by this seat at the round-10 compile (ADJUDICATION_v9 header)"
    ],
    "remedy": "PRD section 2 pointer corrected by 1.0.0_SA_CTO~DELL1, and the fold in the API copy either removed or recorded as accepted off-route behavior. Close on the PRD edit plus that decision.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W41-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "159 of 3,322 served BD composition.json files carry a top holding with no asset_class_canonical; 28 list VXX under 'alternatives' (the old fold), all with an old data_as_of, rewritten byte-stale by a copy/touch step.",
    "evidence": [
      "investigation row MDPF_SECCLASS-W41-S3 (0.9.0_WK_MDPF_SECCLASS~41), read by this seat at the round-10 compile (ADJUDICATION_v9 header)"
    ],
    "remedy": "Decide whether non-current client files are recomputed or retired; close when a census of platinum/clients/*/composition.json reads 0 VXX-as-alternatives, or the CTO rules stale clients out of scope.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W41-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The live silver/bd_assets_dim.parquet has no canonical class columns: the scheduled union path (build_union_dim, --union-bronze) keeps the old column set, although the deployed builder adds them on the full-rebuild path.",
    "evidence": [
      "investigation row MDPF_SECCLASS-W41-S4 (0.9.0_WK_MDPF_SECCLASS~41), read by this seat at the round-10 compile (ADJUDICATION_v9 header)"
    ],
    "remedy": "SC-e-66 (union canonical columns) landed via TO-DEPLOY-e66; close when the next nightly bd_assets_dim.parquet carries asset_class_canonical and sub_asset_class_canonical (read the parquet schema).",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S60",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "COT's served concentration.json still classes SGIIX as multi_asset, a retired class, because the COT class input upstream of D_04 predates the six-class switch. The fix (e67, C_06 reclass) sits on a held line.",
    "evidence": [
      "head-object opal-data-cot platinum/clients/z09305621/concentration.json: ETag f347f1c3eac00395b5f06960e4ff5610, LastModified 2026-10-07T11:40:06Z (unchanged since the row)",
      "get-object of the same key (local scratch, deleted after the read): 1 holding with asset_class multi_asset -- SGIIX, market_value 25862.98",
      "round-12 packet: TO-SC-e67 (COT D_04 no multi_asset) is a HELD line, q/dell1/secclass-r12-held-e67/r1 @a5ce0efab3, deploy waits on limit item 5; at HEAD TO-SC-e67 reads <status>issued",
      "investigation row MDPF_SECCLASS-S60 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "Deploy the e67 held line under its pair (limit item 5). Then re-run R12_CHECKS/served_multi_asset_split.py over opal-data-cot. Close when: served_multi_asset_split.py reads post_switch=0 for opal-data-cot (denominator printed), and z09305621 concentration.json carries no multi_asset holding",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W32-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a07's --parity-control diffs against the ORIGINAL BD lib, which became a canonical-ticker-only reader at SC-t-1, so the control fails with the switch OFF (1,690 of 4,136) and cannot isolate the switch's own deltas.",
    "evidence": [
      "wk-MDPF_SECCLASS-32 @b0132b22a8 A07_SWITCH_BEFORE_AFTER_20261007.json: parity_before_strict ok=false 'A5-A07-PARITY-VS-SERVED: 2446 of 4136 agree ... mismatches 1690', canonical false; parity_after switch_deltas 447, changed_set_equals_before_after false",
      "investigation row MDPF_SECCLASS-W32-S1 (0.9.0_WK_MDPF_SECCLASS~32)"
    ],
    "remedy": "Re-base the parity control on a frozen copy of the pre-SC-t-1 four-layer lib (or on the served a07 output), so OFF reads 0 mismatches. Close when: a07 --parity-control --no-canonical reads 0 mismatches and, switch ON, its delta set equals the before/after changed set.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W32-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a07's last layer classes any key whose ticker is NaN as equity (str(NaN).upper()=='NAN' matches the ticker shape): 228 of 4,136 held keys at the base, 109 still after the canonical switch, served today in 49 Financial's equity bucket.",
    "evidence": [
      "wk-MDPF_SECCLASS-32 a07_dim_asset_classification.py:325-329: layer 4 `if ticker: t = str(ticker).strip().upper(); if t and re.fullmatch(r'[A-Z]{1,5}(\\.[A-Z])?', t): return 'equity'` with no NONE/NAN exclusion, while :252, :257, :303 exclude ('NONE','NAN')",
      "investigation row MDPF_SECCLASS-W32-S2 (0.9.0_WK_MDPF_SECCLASS~32)"
    ],
    "remedy": "Exclude NONE/NAN (and empty) in layer 4 as layers 1-3 already do; re-class the 109 under a never-widen half. Close when: a07's layer 4 refuses 'NAN' and a rebuild reads 0 keys with ticker NaN and source regex-name.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W32-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a07's _classifier_vintage is computed from bd-securities and the lib hash only, so once the canonical switch reads etf-classifications first, a change to that table does not move the vintage.",
    "evidence": [
      "wk-MDPF_SECCLASS-32 a07_dim_asset_classification.py:193 comment: classifier_vintage = sha256((ddb_payload + lib_hash)); the ddb payload is the bd-securities ticker_map; etf-classifications is in neither term",
      "investigation row MDPF_SECCLASS-W32-S3 (0.9.0_WK_MDPF_SECCLASS~32)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 rules whether the vintage form (pinned by CTO 87535/91555) gains the canonical substrate; the form change is a ruling, not a cell edit. Close when: A ruling is recorded and, if granted, a test shows a changed etf-classifications row moves the vintage.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W32-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The a07 half's rollback VersionId cannot be read from dell1 (the 49 Financial bucket denies this box), so the rollback key is named but its version is unread.",
    "evidence": [
      "head-object s3://opal-data-49financial/_code/a07_dim_asset_classification.py from dell1 (fork of 3.0.0_SA_CVO, 2026-10-07 ~13:0xZ): 403 Forbidden",
      "investigation row MDPF_SECCLASS-W32-S4 (0.9.0_WK_MDPF_SECCLASS~32)"
    ],
    "remedy": "The release seat (a principal the bucket admits) reads and records the live VersionId as the half's first step, before the act. Close when: The a07 half carries the live VersionId read at release, with the reader named.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W56-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The R12b ampersand rule, narrowed to 1-2 letters each side to satisfy the census, leaves names with longer halves mis-cased: CWGIX and WGIFX read 'Gr&inc', and IFF reads 'International Flavors&fragranc'. The amendment's literal wording would change 11 rows and fail AC3.",
    "evidence": [
      "git grep at HEAD: infra/aws/lambda/v2_portal/_shared/security_name.py:56 _AMP_TOKEN matches [A-Z]{1,2}&[A-Z]{1,2} -- the worker's narrowed reading, not the amendment's literal rule",
      "investigation row MDPF_SECCLASS-W56-S2 (0.9.0_WK_MDPF_SECCLASS~56)"
    ],
    "remedy": "The issuer rules whether a wider repair is wanted, or accepts the residual and records it. Close when: 2.0.0_SA_COO~M1 records a ruling, and the served names of CWGIX, WGIFX and IFF read as the ruling says",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S63",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The NAME:: skip is in the code at HEAD but not served: both gold code buckets serve the e65 module (3f1e6be8) without it, so a name-keyed security with the word CASH is still placed cash/Cash by the ticker leg in the gold runners.",
    "evidence": [
      "HEAD _shared/etf_classification_scheduled.py cash_token_match skips a NAME:: key (1fae201565, TO-SC-e65 amendment 3); md5 at HEAD 40ffa3fac380551704637adc8a3b6ff3",
      "s3api head-object code/gold/lib/_shared/etf_classification_scheduled.py: opal-data-bd ETag 3f1e6be8910952f33c88bf100c610ab6 LastModified 2026-10-08T01:49:54Z (the e65b rollback, row S68); opal-data-cot ETag 3f1e6be8... 2026-10-07T16:54:13Z -- both the PRE-skip module",
      "investigation row MDPF_SECCLASS-S63 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "TO-DEPLOY-e65b lands the amended module to both buckets once the dell1 cot deny is lifted (Andrew's item 2); tests/test_cash_token.py pins the two NAME:: examples as NOT cash. Close when: both opal-data-bd and opal-data-cot code/gold/lib/_shared/etf_classification_scheduled.py read the trunk md5 that carries the NAME:: skip",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S65",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The e49 order's context still cites a device-egress sentence as its vendor word, while the reserved card asked about the population. The order now sits with a dell1 seat (~SD), so the device half of the mismatch is moot; the population half is not answered by that sentence. Not adjudicated here.",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~SD/task_orders/MDPF_SECCLASS.TO-AI-e49.missing-list-ai-leg-laptop.md: <status>pending</status>; :28 'Vendor word: laptop 1.0.0_SA_CTO msg 106533, on Andrew-direct 2026-10-07 ~18:3xZ item 4 (The Dell Boxes have vendor ...'",
      "RESERVED_CARD_SC_e49_AI_LEG_VENDOR_WORD_20261007.md (2.0.0_SA_COO deliverables) exists; per the row its question was the population, not the device",
      "investigation row MDPF_SECCLASS-S65 (0.7.0_AE_CloudOps~SC)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 rules which instrument is e49's vendor authority (the signed CTO half's numbers, or a word on the population), and the order's context line cites it. Close when: TO-AI-e49's context line cites the instrument the CTO rules answers the population question, before any e49 vendor call",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S66",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "AC1 is still a correctness oracle, not a completeness one: a partial AI act (any landed count from 1 to planned) prints ok=True rc=0, so closing a NEVER-2 entry or flipping the order on AC1 alone closes an incomplete WORLD act.",
    "evidence": [
      "R12_CHECKS/ai_leg_verify.py:84 at HEAD: ok = not probs and gone == 0 and ma == 0 and landed > 0 and lcount == model_rows -- no unresolved == 0 term and no expected-count argument; the 0d91b0fa96 fix touched only the listing limb",
      "investigation row MDPF_SECCLASS-S66 (0.7.0_AE_CloudOps~SC)"
    ],
    "remedy": "ai_leg_verify.py adds unresolved == 0 (or takes the act's RECLASSIFY-WRITE line / expected count) to ok; until then every AI-leg close reads the completeness line, not AC1's ok. Close when: ai_leg_verify.py's ok predicate fails on unresolved > 0 (a re-run against a partial state prints ok=False)",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Two of the four staged _shared members are still pinned to pre-port bytes (the row said 3 of 4; measured now 2 of 4); a build today ships them green beside a worktree-read entrypoint. The guard detects drift, not staleness.",
    "evidence": [
      "infra/aws/lambda/ci/build-and-upload.sh:196-233 at HEAD: stages staged_from members via git show <pin>:<path> and refuses only on BLOB HASH MISMATCH vs the declaration; no pin-vs-HEAD staleness check (last change da72ce8b3c, 2026-10-07)",
      "lambda-source-map.json mdpf-secclass-new-security row, git show <pin>:path vs HEAD (fork read): _shared/etf_classification.py @87065e4565 DIFFERS; etf_classification_scheduled.py @87065e4565 DIFFERS; etf_classifications_dynamodb.py @87065e4565 SAME; rivalfunds_classification.py @5cbb530eb6 SAME",
      "investigation row MDPF_SECCLASS-D1-S1 (0.7.0_AE_CloudOps~SD)"
    ],
    "remedy": "The issuer re-pins the staged_from entries to the merged commit (declared sha256 updated) before any build of this Lambda; the builder's owner adds a stale-pin warning. Close when: every staged_from member of mdpf-secclass-new-security reads SAME between its pin and HEAD, or the builder refuses a stale pin",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S68",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The cross-box seat gate is still advisory: a predicted-STOP multi-bucket deploy starts and can half-land; this time the NEVER-2 rollback contained it.",
    "evidence": [
      ".tools/safe-deploy.sh at HEAD (seat-gates block ~:88-120): CROSSBOX-DEPLOY verdict=STOP adds to sg_bad, but blocks only when sg_mode=ENFORCE; otherwise 'WARN mode proceeds'",
      "test -f org/mcp/seat-gates.enforce: ABSENT, so WARN mode; the last safe-deploy change 5f6eaecb34 (NFRA_CTLPLN CT-s-3) did not change this",
      "s3api head-object opal-data-bd code/gold/lib/_shared/etf_classification_scheduled.py LastModified 2026-10-08T01:49:54Z ETag 3f1e6be8 (the in-session rollback the row records)",
      "investigation row MDPF_SECCLASS-S68 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "The gate's owner (NFRA_CTLPLN, laptop) makes CROSSBOX verdict=STOP fail closed before the first PUT, at least for a multi-bucket act, or sets the enforce flag; e65b stays held until the cot deny lifts. Close when: safe-deploy exits before any PUT on a CROSSBOX STOP (ENFORCE or a per-verdict fail-closed), read at HEAD",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "deploy_ledger.py regenerates a change_management entry and silently drops hand-written prose (only Sign-off survives), so a STOP narrative written in the entry the NEVER-2 law names is deleted at the next leg close.",
    "evidence": [
      "git log -- .tools/deploy_ledger.py: last change a4b8ac93e0 (2026-09-15, keeps only the Sign-off section on re-render); nothing after the row's 2026-10-08T02:30Z measurement",
      "the lost section is preserved in org/tier2_senior/0.7.0_AE_CloudOps~SD/deliverables/MDPF_SECCLASS_E57E61_PROOF_INSTANCE_AND_ACT_NARRATIVE_20261008.md (per the row)",
      "investigation row MDPF_SECCLASS-D1-S3 (0.7.0_AE_CloudOps~SD)"
    ],
    "remedy": "The tool's owner preserves non-generated sections on re-render (as a4b8ac93e0 did for Sign-off), or refuses and prints when it would delete committed prose; until then STOP narratives go in a deliverable the entry cites. Close when: a close-leg on an entry carrying a hand-written section keeps it, or the tool refuses with a printed reason, read at HEAD",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W62-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "17 rows still sit at fixed_income/Cash, outside the contract (Cash is a sub-class of cash only); the cell's 316 figure was not reproduced (328).",
    "evidence": [
      "TO-SC-e72 <status>complete</status> at HEAD; packet DRAIN_END_R12: cash_grade.py cash_rows=330, v3 328/328 at plan, 0 absent, 0 wrong; fixed_income/Cash=17 remain (sent to the CTO for round 13)",
      "investigation row MDPF_SECCLASS-D1-W62-S1 (0.9.0_WK_MDPF_SECCLASS~62)"
    ],
    "remedy": "Round 13 decides whether the 17 are legacy rows the V3 set re-plans or rows outside it, and places them cash/Cash under a pair. Close when: cash_grade.py reads fixed_income/Cash=0",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v13",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v13"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
