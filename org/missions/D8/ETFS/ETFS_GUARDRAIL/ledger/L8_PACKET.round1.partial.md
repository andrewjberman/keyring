# ETFS_GUARDRAIL round 1 -- L8 PACKET (PARTIAL, and the word is load-bearing)

**Compiled by** `2.0.0_SA_COO~B` 2026-09-04 ~22:4xZ, revised 2026-09-05 ~00:2xZ, ~01:1xZ, ~02:3xZ and ~03:1xZ, on the `/drive` obligation "terminal orders -> L8 compile NOW".
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the COO's one message of
the round is the drain-end read). **This is NOT the L10 slug** -- the slug goes once, after EVERY order is terminal and
EVERY row is dispositioned, and six orders are still open. This packet exists so the CVO's L9 work on what IS
terminal can run beside the drain instead of behind it. It is versioned in place as more orders go terminal.

---

## 1. WHY PARTIAL

Eight of fourteen orders are terminal at HEAD (EG-s-10, EG-s-3, EG-s-13, EG-s-11, EG-s-12, EG-s-4, EG-s-1, EG-s-7;
packet revised at `745cd6b354`). The other six are behind the DAG the decomposition drew
(`decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.1.1 s.1-s.2): rung 3 (handed) waited on the ladder; the second port
is in flight; the renderer cells wait on the ladder (terminal now) and the second port; the send cells on rung 3 and
the alignment. Nothing is late; two slots are draining in dependency order and the third is spent.

## 2. THE TERMINAL ORDERS, each with the instance the checker graded AT THE ISSUER'S SEAT

Every instance below was re-validated at this seat with the expected criterion ids taken from the ORDER at HEAD and
passed as the checker's third argument (coverage checked), on the merged tree, after the drain.

| order | cell | instance (under `deliverables/`) | checker at HEAD | drained at |
|---|---|---|---|---|
| TO-EG-s-10 | EG-s-10 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.the-trading-calendar-each-producer-resolves.proof_of_spec.json` | VALID rc 0, 5 rows | `e6689cc7cc` (deliverables), `d3e2d56f7c` (the flip) |
| TO-EG-s-3 | EG-s-3 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.proof_of_spec.json` | VALID rc 0, 5 rows (S3-AC1 recorded under the issuer's amendment) | `d008067fa3` (deliverables), `8786482cb0` (the close) |
| TO-EG-s-13 | EG-s-13 | `0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.proof_of_spec.json` | VALID rc 0, 6 rows; `data/etfs/scripts/coverage/_orion_vendor_asof.py` ABSENT at HEAD | `198f98a64a` |
| TO-EG-s-11 | EG-s-11 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-11.which-49f-twin-writes-the-served-slices.proof_of_spec.json` | VALID rc 0, 5 rows | `108d9fa67f` (the channel conflict united: 9 rows) |
| TO-EG-s-12 | EG-s-12 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-12.inflection-deployed-bytes-vs-build-input.proof_of_spec.json` | VALID rc 0, 5 rows | `a8e3ac7927` (the channel conflict united: 11 rows) |
| TO-EG-s-4 | EG-s-4 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-4.the-coverage-classifier.proof_of_spec.json` | VALID rc 0, 7 rows | `62cc386d94` (clean merge, 7 paths; no rows on the branch) |
| TO-EG-s-1 | EG-s-1 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-1.cot-catch-up-port-reporting-obligation-window.proof_of_spec.json` | VALID rc 0, 9 rows | `c866edd324` (clean merge, 11 paths; 12 rows at HEAD after) -- a DEPLOY: ledger `etfs-guardrail-eg-s-1-cot-catchup-port` OPEN @`13ed1ab775`, CLOSED @`091681fe45`, `ci: record deploy cot-pipeline` @`a8ef1ca328` |
| TO-EG-s-7 | EG-s-7 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-7.the-remediation-ladder-rungs-1-2-and-the-invoke-grant.proof_of_spec.json` | VALID rc 0, 7 rows (S7-AC5/S7-AC6 PASS under the amended, targeted criteria) | `745cd6b354` (the channel conflict united: 14 rows) -- an IAM DEPLOY BY TARGET: ledger `etfs-guardrail-eg-s-7-reporter-invoke-grant` OPEN @`d1c4204aa1`, CLOSED @`3f19353c05`; `aws_iam_role_policy.reporter` changed, nothing else; the pre-existing `aws_instance.reporter` drift NOT applied |

## 3. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

Each carries **no verdict** and is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.

- **S10-AC5** (EG-s-10) -- which calendar each producer resolves today (inf: its own byte-identical vendored copy; cot
  and 49F: NONE, newest-partition only) and the vendoring recommendation. The worker found the CTO~Z ruling
  @`1da1e2b73b` ("MINT THE LAYER, NOT A FIFTH COPY") and recommended the layer over the copy the faces mandated; the
  issuer ADOPTED it (@`de8693863c`; rows W1-S1). Grade the answer; the adoption is on the record.
- **S3-AC5** (EG-s-3) -- the PORT CONTRACT: the verbatim set, the one replacement (the reporting-obligation window
  with a shipped-signal terminus), the invariants, the probe addition, the 49F-tail test arm. Grade it as the spec the
  two port orders (EG-s-1, EG-s-2) build to; the contract's calendar mechanism is now the layer, per the amendment.
  NOTE for the grade: the contract's battery SHAPE (a bare script ending in a module-level `sys.exit()`) is refuted by
  row W2-S4 -- it crashes pytest at collection; EG-s-1 shipped real test functions and EG-s-2's face now names them.
- **S13-AC6** (EG-s-13) -- one date basis from the cutover month forward, nothing restated, no partner notified, the
  alignment gates the send and not the guardrail. Grade against the exercised renders (2026-09 aligned, 2026-08 not).
- **S11-AC5** (EG-s-11) -- WHICH 49F TWIN WRITES THE SERVED SLICES: `WRITER=bd-49f-etf-ownership-daily`, 3 of 3
  `OK: wrote` log events tied to 3 of 3 newest `daily/49financial/` slices; the canonical twin
  `bd-49f-etf-ownership-daily-canonical` is NOT LIVE (`ResourceNotFoundException` on `GetFunctionConfiguration`); the
  live function is scheduled with `OUTPUT_PREFIX=daily/49financial/`. Grade whether EG-s-2's address is confirmed on
  the APPLIED plane at both ends (function side and object side); the result document's s.2 and s.5 carry the census.
- **S12-AC5** (EG-s-12) -- INFLECTION'S RUNNING BYTES vs THE BUILD INPUT: `VERDICT: MISMATCH files=3`
  (`dedup_core.py` and `trading_calendar.py` ABSENT from the deployed zip; `lambda_function.py` byte-DIFFERENT), and the
  deployed `lambda_function.py` is byte-identical to the repo's copy at `af4f123e2c` (2026-08-01), which PREDATES the
  Orion repoint `001a73530a` (2026-08-03, "COMMIT ALL / APPLY NOTHING per CTO F2 ruling"). The 2026-08-11
  `LastModified` is a config-only env-var update: `ASSETS_BUCKET`/`FACT_POSITIONS_PREFIX` are bound on the live
  function and the running code never references them; it reads the legacy `opal-data-inf/gold/canonical/holdings_`
  path via `INF_BUCKET`/`HOLDINGS_PREFIX`, and every row of the 2026-09-04 slice cites that path. Grade the finding
  and its consequence the worker drew: rung 2 for Inflection is stated against the LEGACY path, not repo HEAD
  (EG-s-7's face and EG-sb-7's face already bind to "whatever EG-s-12's result says"; no amendment was needed).
  **For the CTO's L10 read, not this round's remedy:** the Orion repoint is COMMITTED-NOT-APPLIED under another
  seat's ruling; this project classifies against the world as it runs and applies nothing to Inflection.
- **S4-AC7** (EG-s-4) -- THE CLASSIFIER'S TAXONOMY: B is excluded from `holes` by construction and counted in
  `expected_empty`; the ZERO-vs-MISSING contract is untouched (no `put_object`/`upload_*` anywhere in the module);
  UNKNOWN only when the probe is absent or answers None; MECE over "a calendar day of the month" shown by the sums the
  worker recorded (live inflection August: A=10 + COVERED=21 = 31 days; the August fixture 16+5 = 21 and 21+0 = 21).
  Live August cottonwood after the 09-01 repair: 21 of 21 trading days covered, UNKNOWN=0. Grade property 4 against
  the eight test arms and the two live counts in the result document s.8. The worker self-caught a first-draft
  docstring that named a firm bucket (`FIRM_BUCKET_REFS=1`), reworded it and re-ran the whole battery -- on the
  record in the report, not a row.
- **S1-AC9** (EG-s-1) -- THE COT PORT AS DEPLOYED: the window is the reporting obligation (prior month's 1st while
  its report is not shipped, else the current month's 1st, through yesterday) with the shipped-signal terminus
  (`platinum/reports/<YYYY-MM>/etf_ownership.pdf`, a denied read counts as NOT shipped and is logged `WARN:`); the
  source's three skips kept; no day-count constant (`DAYCOUNT_WINDOW=False`); the ZERO-vs-MISSING contract untouched;
  the probe mode writes nothing and answered live for 2026-08-04 (`partition=true priced=10958 output_exists=true`);
  the calendar from the published layer (`opal-trading-calendar-layer:1` attached beside `pandas-pyarrow-requests-layer:1`,
  no committed copy); the plan changed exactly the Lambda and its role policy (`2 to change`), 0-diff after, served
  `CodeSha256` == built `artifact_sha256`. FWD-1's EXERCISED grade ("a real missed day caught up without a person") is
  the next scheduled fire naming a recovered date in `catchup_processed`, which the order did not manufacture. Grade
  the design against rulings 1 and 2 and property 1; eight test arms in the result document.
- **S7-AC7** (EG-s-7) -- THE LADDER, RUNGS 0-2, AND THE ONE GRANT: rungs unattended and never fabricating (six test
  arms; `HTTP_CLIENT_IMPORTS=0 PUT_OBJECT_CALLS=0` as a property of the bytes; the live August cottonwood dry-run
  `holes=0 rung0=0 rung1=0 rung2=0 unresolved=0`); the grant `InvokeProducersForRemediation` names exactly three
  function ARNs and no bucket, read back on the APPLIED plane (`lambda:InvokeFunction`); rung 3 is absent by
  construction and left to EG-sb-7; the Inflection re-check is stated against the deployed producer's legacy bucket per
  EG-s-12's answer; the 49F map follows EG-s-11's confirmed writer. The apply was BY TARGET under the W1-S7 ruling
  (s.4) -- the result document carries the full untargeted plan's drift line verbatim beside the targeted summary.
  Grade against rulings 4 and 6 and property 9; the result document s.7 carries the text.

## 4. THE ROWS THE BRANCHES CARRIED, and their standing at this seat

| row | class / standing | disarm owner | what it is | the issuer's act |
|---|---|---|---|---|
| S1 | OBSERVATION, INERT | -- | the discriminator's principal (the ETFS layer holds no firm-bucket grant; the probe design) | seat row, for the CTO's L10 read |
| W2-S1 | OBSERVATION, ARMED | `3.0.0_SA_CVO` | the relied-on inf producer's own battery crashes at import since the 2026-08-03 repoint (32 days undetected) | NOT this seat's; S3-AC1 amended to record it (@`de8693863c`) |
| W1-S1 | OBSERVATION, ARMED | this seat | the ports' vendoring mandate vs CTO~Z's layer ruling | DISARMED @`de8693863c` (the layer; no committed first-party copies anywhere in the project) |
| W1-S2 | BLOCKING, ARMED | this seat | the faces' BOUNDS wording withheld the tree-convention flip grant | DISARMED @`de8693863c` (restated on all 14 faces) |
| W1-S3, W2-S2, W3-S2 | OBSERVATION, ARMED | this seat | the faces named the proof instance by `to_id`; the gate keys it off the task order's basename (`to-pipeline-gate.py:1262-1263`) | DISARMED @`83d8175729` (all 14 faces name the gate's form; ONE instance file each) |
| W3-S1 | OBSERVATION, INERT | -- | the CSVs are written by a separate call path from `render_month`; the alignment needed a second call site | disarmed by the worker in-order |
| W2-S3 | OBSERVATION, ARMED | this seat | TO-EG-s-11's suggested single-call `logs filter-log-events --limit 20` returns 1 of 3 events with a `nextToken` unfollowed (the CLI v1 shim does not auto-paginate that verb) | DISARMED @`108d9fa67f` (the criterion's instrument was the worker's paginating script, so S11-AC3's 3-of-3 stands; the order is terminal, no face edit; a cut lesson for any future face that names `filter-log-events`) |
| W1-S4 | OBSERVATION, INERT | -- | one `iam list-role-policies` call outside TO-EG-s-12's enumerated live-read surface (policy names only, not relied on for the graded answer) | disarmed by the worker in-order; recorded |
| W1-S5 | OBSERVATION, ARMED | this seat | `infra/aws/lambda/ci/build-zip.sh:66` hardcodes `touch -t "202600010000"` (month 00) and fails rc=1 on every invocation, since `e046072434` (2026-02-19) | DISARMED FOR THIS ROUND at this seat: the project's deploying faces name `build-and-upload.sh`, which has ZERO callers of `build-zip.sh` in `infra/aws/lambda/ci/` (measured at HEAD; EG-s-1's deploy went through it); only TO-EG-s-12's face named `build-zip.sh` and its named fallback was used. The shared-script defect sits in lane `CLOUD_OPS_OR_ETL` (this seat is refused on the path) and is ROUTED to `1.0.0_SA_CTO` in the drain-end read, not touched here |
| W2-S4 | OBSERVATION, ARMED | this seat | the port contract's bare-script battery (module-level `sys.exit()`) crashes pytest at collection (INTERNALERROR rc=3) whatever the arms say; EG-s-1 shipped real `def test_*` functions instead; inf's `test_catchup_scan.py` would hit this too once its KeyError is fixed | DISARMED @`2baa6af162` (EG-s-2's S2-AC1 names real test functions); the inf-battery half belongs with W2-S1 at the CVO |
| W1-S6 | OBSERVATION, INERT -- RULED | this seat | `.tools/terraform.exe` (v1.9.8) is gitignored and absent in a fresh worker worktree; the worker used PATH `terraform` v1.14.5 for one plan | RULED @`2baa6af162`: the issuer provisions the binary into each worker worktree at hand-off (done at every re-create since); the deploying faces forbid the PATH substitution. Measured at this seat 02:2xZ: the three remote states (cot-pipeline, etfs-reports, bd-pipeline) all still carry `terraform_version` 1.9.8 -- nothing was re-pinned; EG-s-1's and EG-s-7's applies went through 1.9.8 |
| W1-S7 | BLOCKING, INERT (a stop) | -- | TO-EG-s-7's untargeted plan in `etfs-reports` reads `2 to change`: the order's `aws_iam_role_policy.reporter` AND a pre-existing `aws_instance.reporter` `user_data` drift (`e47b615c` -> `434774b5`), deferred as benign by NFRA_TERRAFORM-P2 @`1502fdd6f9` (2026-07-08); the worker refused the apply per its bound | RULED @`2baa6af162` and EXECUTED @`3f19353c05` (merged @`745cd6b354`): the drift is NOT this order's and is NOT applied (a `user_data` change on `aws_instance` is applied by the provider through a STOP and START of the reporter instance -- a confirm-with-Andrew class this seat does not take); EG-s-7, EG-s-8 and EG-s-9 plan, apply and 0-diff BY TARGET to the one resource each changes, the target stated in the ledger entry, the full plan's drift line recorded verbatim. THE DRIFT ITSELF is ROUTED to `1.0.0_SA_CTO` in the drain-end read (whether to apply it is Andrew's, the instance being the renderer's host) |

An ARMED standing on a row this seat has disarmed is the append-only channel's carrier lag; the disposition is the
CVO's at L9 and the disarm's evidence is the commit named beside it.

## 5. WHAT IS OPEN (six orders), and the hand-off order the drain follows

slot 1: EG-sb-7 (HANDED 2026-09-05 ~03:1xZ, worktree re-created @`745cd6b354`) -> EG-s-8 -> EG-s-9 (the same Lambda, one deploy after the other).
slot 2: EG-s-2 (in flight: the port and the artifact committed, ledger OPEN @`a1c372983f`, the apply leg next) -> EG-s-5 -> EG-s-6 (EG-s-6 last, the one renderer upload; its dependencies EG-s-4 and EG-s-7 are terminal).
slot 3: spent.
