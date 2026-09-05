# ETFS_GUARDRAIL round 1 -- L8 PACKET (PARTIAL, and the word is load-bearing)

**Compiled by** `2.0.0_SA_COO~B` 2026-09-04 ~22:4xZ, revised 2026-09-05 ~00:2xZ, ~01:1xZ, ~02:3xZ, ~03:1xZ, ~04:1xZ, ~05:3xZ and ~07:4xZ, on the `/drive` obligation "terminal orders -> L8 compile NOW".
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the COO's one message of
the round is the drain-end read). **This is NOT the L10 slug** -- the slug goes once, after EVERY order is terminal and
EVERY row is dispositioned, and ONE order is still open. This packet exists so the CVO's L9 work on what IS terminal
can run beside the drain instead of behind it. It is versioned in place; the next revision is the drain-end one.

**A CORRECTION TO EARLIER VERSIONS OF THIS PACKET (s.4, rows W1-S7 and W1-S8, and the seat row S2 that corrects them):**
the `aws_instance.reporter` `user_data` "drift" that earlier revisions described as "pre-existing ... deferred as benign
by NFRA_TERRAFORM-P2 @1502fdd6f9" was a FALSE drift -- a CRLF checkout artifact of the worker worktrees on this
`core.autocrlf=true` box. The live instance and the LF rendering of `instance.tf` at HEAD carry the same bytes (sha1
`e47b615c`); the plan's "new" hash (`434774b5`) is the CRLF rendering of the same heredoc. The July commit is about `ami`
and the public IP. Nothing live was ever touched by the false reading; the RESERVED classification stands as a class
and was applied to a premise that turned out false. Evidence in row S2.

---

## 1. WHY PARTIAL

Thirteen of fourteen orders are terminal at HEAD (EG-s-10, EG-s-3, EG-s-13, EG-s-11, EG-s-12, EG-s-4, EG-s-1, EG-s-7,
EG-s-2, EG-sb-7, EG-s-5, EG-s-8, EG-s-6; packet revised at `c17da2f4a8`). The last, EG-s-9 (the JOIN, the orchestrator's
second deploy), is in flight on slot 1. Slots 2 and 3 are spent and torn down.

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
| TO-EG-s-7 | EG-s-7 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-7.the-remediation-ladder-rungs-1-2-and-the-invoke-grant.proof_of_spec.json` | VALID rc 0, 7 rows (S7-AC5/S7-AC6 PASS under the amended, targeted criteria) | `745cd6b354` (the channel conflict united: 14 rows) -- an IAM DEPLOY BY TARGET: ledger `etfs-guardrail-eg-s-7-reporter-invoke-grant` OPEN @`d1c4204aa1`, CLOSED @`3f19353c05`; `aws_iam_role_policy.reporter` changed, nothing else |
| TO-EG-s-2 | EG-s-2 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-2.bd-49f-catch-up-port-the-tail-a-straight-port-misses.proof_of_spec.json` | VALID rc 0, 9 rows | `fb0776daae` (the channel conflict united: 15 rows) -- a DEPLOY: ledger `etfs-guardrail-eg-s-2-bd49f-catchup-port` OPEN @`a1c372983f`, CLOSED @`fcb3e42f31`; the plan changed exactly the two bound addresses in the wide `bd-pipeline` directory, `No changes.` after over the whole directory; the deploy's CHANGELOG.json entry landed by the issuer @`4b35d14ff4` (s.4, W2-S5) |
| TO-EG-sb-7 | EG-sb-7 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-sb-7.rung-3-stops-and-asks-a-person.proof_of_spec.json` | VALID rc 0, 5 rows | `c50c72f92a` (clean merge, 5 paths; no rows on the branch) |
| TO-EG-s-5 | EG-s-5 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-5.the-coverage-line-in-the-report.proof_of_spec.json` | VALID rc 0, 6 rows | `1c5603a696` (clean merge, 5 paths; no rows on the branch); no deploy |
| TO-EG-s-8 | EG-s-8 | `0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-8.the-one-terminal-ses-send.proof_of_spec.json` | VALID rc 0, 9 rows (S8-AC9 minted on row S3) | `f036a438fb` (the channel conflict united: 18 rows; the face conflict resolved to the issuer's amended text with the worker's flip) -- a LAMBDA DEPLOY BY TARGET: ledger `etfs-guardrail-eg-s-8-orchestrator-terminal-send` OPEN @`d0edf02b28`, CLOSED @`3472ad97cc`, `ci: record deploy etfs-reports` @`ee6e7e0580`; `aws_lambda_function.orchestrator` changed, nothing else; the live `terminal_qa` rehearsal invoked (StatusCode 200, no send); `_render_command` at HEAD passes `--gate` (`lambda_function.py:211`) |
| TO-EG-s-6 | EG-s-6 | `0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-6.the-pre-publish-gate-inside-the-renderer.proof_of_spec.json` | VALID rc 0, 8 rows | `c17da2f4a8` (the channel conflict united: 19 rows) -- the ONE RENDERER ARTIFACT UPLOAD: ledger `etfs-guardrail-eg-s-6-renderer-artifact-upload` OPEN @`d0823cd564`, CLOSED @`4cc172fe3d`; head-object MATCH 6 of 6 (the renderer, `__init__.py`, `classifier.py`, `remediate.py`, and the two build-time copies `trading_calendar.py` and `_orion_vendor_asof.py`); the coverage package listed at the box's pull prefix. The deploy-order window of row S3 is CLOSED: the box's renderer now accepts `--gate` |

## 3. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

Each carries **no verdict** and is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.

- **S10-AC5** (EG-s-10) -- which calendar each producer resolves today (inf: its own byte-identical vendored copy; cot
  and 49F: NONE, newest-partition only) and the vendoring recommendation. The worker found the CTO~Z ruling
  @`1da1e2b73b` ("MINT THE LAYER, NOT A FIFTH COPY") and recommended the layer over the copy the faces mandated; the
  issuer ADOPTED it (@`de8693863c`; rows W1-S1). Grade the answer; the adoption is on the record.
- **S3-AC5** (EG-s-3) -- the PORT CONTRACT: the verbatim set, the one replacement (the reporting-obligation window
  with a shipped-signal terminus), the invariants, the probe addition, the 49F-tail test arm. Grade it as the spec the
  two port orders (EG-s-1, EG-s-2) built to -- both are now deployed against it; the contract's calendar mechanism is
  the layer, per the amendment. NOTE for the grade: the contract's battery SHAPE (a bare script ending in a
  module-level `sys.exit()`) is refuted by row W2-S4 -- it crashes pytest at collection; both ports shipped real test
  functions.
- **S13-AC6** (EG-s-13) -- one date basis from the cutover month forward, nothing restated, no partner notified, the
  alignment gates the send and not the guardrail. Grade against the exercised renders (2026-09 aligned, 2026-08 not).
- **S11-AC5** (EG-s-11) -- WHICH 49F TWIN WRITES THE SERVED SLICES: `WRITER=bd-49f-etf-ownership-daily`, 3 of 3
  `OK: wrote` log events tied to 3 of 3 newest `daily/49financial/` slices; the canonical twin
  `bd-49f-etf-ownership-daily-canonical` is NOT LIVE (`ResourceNotFoundException` on `GetFunctionConfiguration`); the
  live function is scheduled with `OUTPUT_PREFIX=daily/49financial/`. Grade whether EG-s-2's address was confirmed on
  the APPLIED plane at both ends (function side and object side) -- EG-s-2 then ported into exactly that function.
- **S12-AC5** (EG-s-12) -- INFLECTION'S RUNNING BYTES vs THE BUILD INPUT: `VERDICT: MISMATCH files=3`
  (`dedup_core.py` and `trading_calendar.py` ABSENT from the deployed zip; `lambda_function.py` byte-DIFFERENT), and the
  deployed `lambda_function.py` is byte-identical to the repo's copy at `af4f123e2c` (2026-08-01), which PREDATES the
  Orion repoint `001a73530a` (2026-08-03, "COMMIT ALL / APPLY NOTHING per CTO F2 ruling"). The 2026-08-11
  `LastModified` is a config-only env-var update: `ASSETS_BUCKET`/`FACT_POSITIONS_PREFIX` are bound on the live
  function and the running code never references them; it reads the legacy `opal-data-inf/gold/canonical/holdings_`
  path via `INF_BUCKET`/`HOLDINGS_PREFIX`, and every row of the 2026-09-04 slice cites that path. Grade the finding
  and its consequence the worker drew: rung 2 for Inflection is stated against the LEGACY path, not repo HEAD
  (EG-s-7 built it so; EG-sb-7's provider map follows it). NOTE: unlike the reporter's `user_data` (s.4, S2), THIS
  mismatch was measured on the deployed zip's bytes against the build input, not on a hash of a checkout -- the
  worker diffed file contents (`dedup_core.py` and `trading_calendar.py` absent from the zip), which line endings
  cannot produce.
  **For the CTO's L10 read, not this round's remedy:** the Orion repoint is COMMITTED-NOT-APPLIED under another
  seat's ruling; this project classifies against the world as it runs and applies nothing to Inflection.
- **S4-AC7** (EG-s-4) -- THE CLASSIFIER'S TAXONOMY: B is excluded from `holes` by construction and counted in
  `expected_empty`; the ZERO-vs-MISSING contract is untouched (no `put_object`/`upload_*` anywhere in the module);
  UNKNOWN only when the probe is absent or answers None; MECE over "a calendar day of the month" shown by the sums the
  worker recorded (live inflection August: A=10 + COVERED=21 = 31 days; the August fixture 16+5 = 21 and 21+0 = 21).
  Live August cottonwood after the 09-01 repair: 21 of 21 trading days covered, UNKNOWN=0. Grade property 4 against
  the eight test arms and the two live counts in the result document s.8.
- **S1-AC9** (EG-s-1) -- THE COT PORT AS DEPLOYED: the window is the reporting obligation (prior month's 1st while
  its report is not shipped, else the current month's 1st, through yesterday) with the shipped-signal terminus
  (`platinum/reports/<YYYY-MM>/etf_ownership.pdf`, a denied read counts as NOT shipped and is logged `WARN:`); the
  source's three skips kept; no day-count constant; the ZERO-vs-MISSING contract untouched; the probe mode writes
  nothing and answered live for 2026-08-04 (`partition=true priced=10958 output_exists=true`); the calendar from the
  published layer; the plan changed exactly the Lambda and its role policy, 0-diff after, served `CodeSha256` == built
  `artifact_sha256`. FWD-1's EXERCISED grade is the next scheduled fire naming a recovered date in
  `catchup_processed`, which the order did not manufacture. Grade against rulings 1 and 2 and property 1.
- **S7-AC7** (EG-s-7) -- THE LADDER, RUNGS 0-2, AND THE ONE GRANT: rungs unattended and never fabricating (six test
  arms; `HTTP_CLIENT_IMPORTS=0 PUT_OBJECT_CALLS=0`; the live August cottonwood dry-run `holes=0 rung0=0 rung1=0
  rung2=0 unresolved=0`); the grant `InvokeProducersForRemediation` names exactly three function ARNs and no bucket,
  read back on the APPLIED plane; rung 3 absent by construction and left to EG-sb-7; the Inflection re-check stated
  against the deployed producer's legacy bucket; the 49F map following EG-s-11's confirmed writer. The apply was BY
  TARGET under the W1-S7 ruling; the "drift" that ruling worked around was false (s.4, S2), and the targeted apply
  changed exactly the one resource it meant to. Grade against rulings 4 and 6 and property 9. NOTE (row W2-S6): the
  ladder module sends NO probe of its own -- rung 0 is the classifier's injected probe, read from the `classes` it is
  handed -- so the Inflection hazard W2-S6 names lives in the gate's probe callable, where EG-s-6 contained it.
- **S2-AC9** (EG-s-2) -- THE 49F PORT AS DEPLOYED, WITH THE TAIL: ten arms including (i) a partition for day D that
  appears only on D+13 with today = D+14 -> D is returned and processed, and (j) the same fixture under the source's
  `CATCHUP_WINDOW_DAYS = 10` semantics -> D would NOT have been found (the negative control that tells the two designs
  apart); no day count re-proposed (`DAYCOUNT_WINDOW=False`); the DS module byte-identical to its source
  (`DS_MODULE_UNTOUCHED=True`, the one-producer law); the `skipped-empty-source` guard kept; the probe answered live
  for 2026-08-04 (`partition=true priced=93398 output_exists=true`); the layer attached; the plan changed exactly the
  two bound addresses in the wide `bd-pipeline` directory, `No changes.` after over the whole directory (no foreign
  drift there); served == built. FWD-1's EXERCISED grade is a real recovered date on a scheduled fire. Grade property
  2 against arms (i) and (j) and rulings 1 and 2.
- **S7B-AC5** (EG-sb-7) -- RUNG 3 IS A DIFFERENT ACTOR: `rung3_stop_and_ask` takes no invoke and no HTTP parameter
  (structurally cannot call a provider), the module still carries zero HTTP-client imports, every ask names date +
  partner + provider + class + reason with the PER-USE authorization line, and the stop fires only when something is
  unresolved (arm (h): zero unresolved writes nothing; never under dry-run). Grade against ruling card 4 and FWD-8's
  DONE WHEN ("the system has actually stopped and asked") -- EXERCISED needs a real unresolved month at the renderer's
  gate (EG-s-6, now live on the box), which this order did not manufacture; the eight arms and the direct
  `write=False` call are its exercise. The worker re-scoped test arm (e) to the post-rung-3 invariant and disclosed it
  in the result and the commit message rather than as a row -- read s.7 and decide whether that disclosure was the
  right carrier.
- **S5-AC6** (EG-s-5) -- THE COVERAGE LINE IN THE REPORT: computed from the classifier (imported through the package;
  `CLASSIFIER_IMPORTED=True SECOND_IMPL=0`) and rendered on EVERY path through `render_month` -- beneath each
  partner's SUMMARY row in the HTML and as the last `# coverage:` row of each firm's CSV with the numeric grid
  unchanged; four arms; the live August render carries three lines (21/21 for every partner). Grade property 6 and
  FWD-3's APPLIED grade ("the statement is in the report itself"); the REFUSE-path half is now verified at EG-s-6
  (S6-AC4: `COVERAGE_LINES_ON_REFUSE=3`).
- **S8-AC8** (EG-s-8) -- THE ONE TERMINAL SEND: exactly three `send_raw_email` call sites after the order (the two
  existing plus the terminal one), no topic created; the terminal send fires only from `_run`'s refusal branch when
  `coverage_unresolved.json` exists for the month, once, to `andrew@opalinvest.com` alone, naming each
  `date | partner | provider | class | reason` plus the egress ask; `absence_check` and `terminal_qa` make no SES call
  (five arms); the `terminal_qa` rehearsal invoked LIVE on the deployed function (StatusCode 200, no email); no
  schedule, alarm, monitor or env var added. Grade the carve-out's width (PRD s.0) and property 8. FWD-7's EXERCISED
  grade needs a REAL terminal failure, which by the PRD's own design should almost never happen -- the worker recorded
  the rehearsal and said so in s.9. ALSO on this order: the `--gate` seam (row S3), `_render_command` now passing the
  flag (`GATE_FLAG_IN_RENDER_COMMAND=True`, S8-AC9).
- **S6-AC8** (EG-s-6) -- THE GATE INSIDE THE RENDERER: a render precondition under `--gate`, not a standing service;
  catch-up runs before it (the ports are deployed; the ladder runs inside it); PUBLISH iff class C == 0 for every
  partner, B and D REPORTED in the verdict artifact and never swallowed; a REFUSE writes the verdict and unresolved
  artifacts and the refused HTML under `refused/`, writes NO `etf_ownership.pdf` at the publish key, exits 3, and so
  surfaces on the existing topic through the orchestrator's existing branches (now enriched by EG-s-8); six arms; the
  two live QA renders (`--no-ladder`): the pre-repair August fixture REFUSED with `holes=5` (rc=3, five live probe
  invokes of the deployed cot producer, no write) and August as it stands PUBLISHED (rc=0, zero invokes); the refused
  deck carries every partner's coverage line. Grade property 3 (both halves exercised on the fixture and the live
  month) and property 5. FWD-2's EXERCISED grade ("has actually refused a month, and the refusal reached a person") is
  a real refusal on a scheduled fire, which this order rehearsed and did not manufacture. Row W2-S6's mitigation (the
  gate never probes Inflection; its uncovered days classify UNKNOWN and go to rung 1) is part of what is graded here.

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
| W1-S5 | OBSERVATION, ARMED | this seat | `infra/aws/lambda/ci/build-zip.sh:66` hardcodes `touch -t "202600010000"` (month 00) and fails rc=1 on every invocation, since `e046072434` (2026-02-19) | DISARMED FOR THIS ROUND at this seat: the project's deploying faces name `build-and-upload.sh`, which has ZERO callers of `build-zip.sh` in `infra/aws/lambda/ci/` (measured at HEAD; both port deploys went through it); only TO-EG-s-12's face named `build-zip.sh` and its named fallback was used. The shared-script defect sits in lane `CLOUD_OPS_OR_ETL` (this seat is refused on the path) and is ROUTED to `1.0.0_SA_CTO` in the drain-end read, not touched here |
| W2-S4 | OBSERVATION, ARMED | this seat | the port contract's bare-script battery (module-level `sys.exit()`) crashes pytest at collection (INTERNALERROR rc=3) whatever the arms say; both ports shipped real `def test_*` functions instead; inf's `test_catchup_scan.py` would hit this too once its KeyError is fixed | DISARMED @`2baa6af162` (EG-s-2's S2-AC1 named real test functions; it shipped ten); the inf-battery half belongs with W2-S1 at the CVO |
| W1-S6 | OBSERVATION, INERT -- RULED | this seat | `.tools/terraform.exe` (v1.9.8) is gitignored and absent in a fresh worker worktree; the worker used PATH `terraform` v1.14.5 for one plan | RULED @`2baa6af162`: the issuer provisions the binary into each worker worktree at hand-off (done at every re-create since); the deploying faces forbid the PATH substitution. Measured at this seat 02:2xZ: the three remote states all still carry `terraform_version` 1.9.8 -- nothing was re-pinned; every apply of the round went through 1.9.8 |
| W1-S7 | BLOCKING, INERT (a stop) | -- | TO-EG-s-7's untargeted plan in `etfs-reports` read `2 to change`: the order's `aws_iam_role_policy.reporter` AND an `aws_instance.reporter` `user_data` diff (`e47b615c` -> `434774b5`); the worker refused the apply per its bound | RULED @`2baa6af162` and EXECUTED @`3f19353c05` (merged @`745cd6b354`): apply BY TARGET, the instance untouched -- correct. THE PREMISE CORRECTED by row S2: the diff was a CRLF checkout artifact, not a real drift, and the July commit the row cited (`1502fdd6f9`) is about `ami` and the public IP. The stop was still right (a plan naming a second resource is not applied), and nothing live was touched |
| W2-S5 | BLOCKING, ARMED | this seat | `record-terraform-deploy.sh`'s own commit also writes `infra/aws/terraform/bd-pipeline/CHANGELOG.json`, which TO-EG-s-2's deliberately narrow `<paths>` (two files under a wide directory) did not grant; the owned-paths gate refused the tool's commit; the worker committed the in-grant source-map half, left the CHANGELOG edit untouched in its worktree, and filed the row | DISARMED in two acts: the grant widened by that one path @`75985f2068` (the worker had already flipped, and a terminal order grants nothing, so no worker commit could carry it); the deploy record then landed from the issuer's seat @`4b35d14ff4` under the AUDITED lane override `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` (rule 14a's named escape for a lane refusal; `org/git-author-override-audit.log` 2026-09-05T04:03:26Z), one file, byte-for-byte from the worker's worktree, the entry verified to be this deploy's. The cut lesson: a deploying face's `<paths>` must name every file the deploy TOOL writes, not only the files the worker edits |
| W1-S8 | BLOCKING, INERT (a stop) | -- | TO-EG-s-8's TARGETED plan (`-target=aws_lambda_function.orchestrator`) still read `2 to change`: the orchestrator's config references `aws_instance.reporter.id` (`REPORTER_INSTANCE_ID`), a real dependency edge `-target` includes; the worker refused the apply and declined S8-AC7's live invoke against the undeployed function (its old fallback would have run a real render) | The stop and the declined invoke were both right. DISPOSITIONED by row S2 (the instance had no real change; with LF `.tf` files in the worktree it showed none) and the ruling @`446a064491`: the worker continued in place, the targeted plan read one resource (`0 to add, 1 to change, 0 to destroy`), the deploy landed, S8-AC7 ran AFTER it -- EXECUTED @`3472ad97cc`, merged @`f036a438fb` |
| S2 | OBSERVATION, ARMED | this seat | THE FALSE DRIFT: live `user_data` sha1 `e47b615c` == the LF rendering of `instance.tf` at HEAD; the plan's `434774b5` == the CRLF rendering; a fresh worktree on this `core.autocrlf=true` box checks out 414 of 414 `.tf` with CRLF (no `*.tf` eol rule in `.gitattributes`); the July commit is about `ami` and the public IP; the heredoc is unchanged since the file's creation | DISARMED at this seat: every `.tf` in every worker worktree normalized to LF at hand-off (eol-only; `git diff --ignore-cr-at-eol` empty); EG-s-8's and EG-s-9's faces carry the corrected text @`446a064491`; EG-s-8's targeted plan then read exactly one resource. The durable fix (`*.tf text eol=lf` in `.gitattributes`) is outside this lane and ROUTED to `1.0.0_SA_CTO` at drain-end. Cut lesson: a worker's worktree is a DIFFERENT CHECKOUT; a hash-sensitive plan there can differ from the main tree's by line endings alone |
| S3 | OBSERVATION, ARMED | this seat | THE `--gate` SEAM NO CELL OWNED: EG-s-6's face says the orchestrator "will pass it once EG-s-8 lands"; EG-s-8's face, EG-s-9's, the decomposition and the PRD carry no such line (0 hits); `_render_command` at HEAD passed no flag; the 10-01 fire would have rendered ungated and FWD-2 could never reach EXERCISED | DISARMED at this seat @`446a064491` and EXECUTED: TO-EG-s-8 gained deliverable item 5 and the minted criterion S8-AC9; `_render_command` at HEAD now passes `--gate` (`lambda_function.py:211`, deployed @`3472ad97cc`); the deploy-order window CLOSED when EG-s-6's renderer upload landed (`4cc172fe3d`, merged @`c17da2f4a8`) -- the box's renderer accepts the flag. Cut lesson: a seam is a cell's line, not a dependency's |
| W2-S6 | OBSERVATION, ARMED | this seat | TO-EG-s-6's probe design (`{"date": d, "probe": true}` for every partner, a non-probe answer read as UNKNOWN) is unsafe for Inflection: `inf-etf-ownership-daily` has NO probe-key handling (the ports added it to cot and 49F only; inf was a verify-only source, EG-s-3), so a probe invoke against a real Inflection hole would run the ordinary dated path and WRITE a real slice -- the invoke itself causes the write, and detecting it by response shape afterwards does not prevent it | DISARMED by the worker's own mitigation, confirmed at this seat: the gate never probes Inflection (`_PROBE_CAPABLE_PARTNERS` = cottonwood + 49financial); Inflection's uncovered days classify UNKNOWN with zero invokes and go to the ladder's rung 1, which is the intended dated re-run; `remediate.py` sends NO probe of its own (rung 0 is the classifier's injected probe, read from `classes`). Not triggered by the round's live criteria (August has zero Inflection holes). For the CTO's L10 read: EG-s-7's face said rung 0 would be "SKIPPED ... detected by the response shape" for a producer without probe mode -- a post-hoc detection that the gate's allowlist replaces with a pre-hoc one |

An ARMED standing on a row this seat has disarmed is the append-only channel's carrier lag; the disposition is the
CVO's at L9 and the disarm's evidence is the commit named beside it.

## 5. WHAT IS OPEN (one order)

slot 1: EG-s-9 (HANDED 2026-09-05 ~07:4xZ, worktree re-created @`df14ecd5f1` with LF `.tf` files and the terraform binary; the JOIN at four sites, the variable, the SES production-access read, the second by-target deploy of the orchestrator).
slots 2 and 3: spent; their worktrees and branches removed.

**What the drain-end read to the CTO will carry (sent once, after EG-s-9 drains):** the seat rows S1, S2, S3; the
inf battery (W2-S1/W2-S4) and the Inflection probe gap (W2-S6) for the CVO's disposition; `build-zip.sh` (W1-S5, lane
CLOUD_OPS_OR_ETL); the `*.tf text eol=lf` `.gitattributes` rule (S2); the Orion repoint's COMMITTED-NOT-APPLIED state
(S12-AC5); the CVO's watermark against the channel's row count.
