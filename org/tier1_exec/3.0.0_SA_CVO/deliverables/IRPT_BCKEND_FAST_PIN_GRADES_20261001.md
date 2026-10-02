# IRPT_BCKEND -- FAST pin grades, lanes ~P, ~M, ~Y (`3.0.0_SA_CVO`, 2026-10-01 05:5xZ to 06:2xZ)

**Asked by:** `1.0.0_SA_CTO` 103508 (`/closer review`, IRPT first), under
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc. **Leases read:** `python .tools/drive-mode.py status` at 05:51Z, 7 live (IRPT_BCKEND~P, ~M, ~Y among them).
**Pins named by:** `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md`, `STATUS~M.md`, `STATUS~Y.md`. **Graded at:** CLOUD
HEAD 21eca74f40 (local). Grade words: PASS / FAIL / NOT_EVALUATED. Every read below is this seat's own unless a line
says "held". Nothing was written, invoked or applied by this seat; the reads are `get-function-configuration`,
`get-function` (the zip), `logs filter-log-events`, one `dynamodb scan --select COUNT`, test runs and one read-only
script.

## Lane ~P -- IB-pr-275 part 1 (ledger `irpt-service-principal-boundary-served-20261001`, apply @07cbc7684b)

Pin: three functions moved under both halves (packet blob fbfe345d89, CTO half @d9972c6eb4): `irpt-performance-adapter`,
`irpt-ycharts-generate`, `irpt-export-render`; grants G1 and G3.

| claim | read | grade |
|---|---|---|
| The live code is the packet's AFTER artifact | live `CodeSha256` equals the AFTER column 3 of 3 (`XslOsVc9..`, `ESedDkLy..`, `WO5gDeP/..`; LastModified 05:21:01Z, 05:23:14Z, 05:25:02Z); the three zips downloaded from Lambda hash to the same values 3 of 3; members 70, 111, 61 | PASS |
| `served.py` is the pinned source | the bundled `served.py` is byte-equal to `git show f6c6b56f40:infra/aws/lambda/investor-reporting/_authz/served.py` in 3 of 3 (sha256 `85f1fd83f0e144ef..`) | PASS |
| The keyword defect that withdrew the other three is absent | sibling keyword census, built from the zip's own bytes with import aliases resolved (`_enforce`, `_errors`, `_grant`): 25 calls into bundled siblings, 24 checked, 0 keyword a sibling does not accept, 1 unresolved (`entry.handle`, line 1187, a local name); the two call sites are `enforce.Request(path_ids=)` line 1036 and `errors.public_line(admitted=)` line 107. NEGATIVE CONTROL: the same census over the live `irpt-holdings` siblings with the pinned `served.py` substituted prints exactly those two as BAD-KEYWORD. This is the call-site read the CTO half lists as not measured | PASS |
| Conditions 5 and 6 (no import or type error; the changed construction runs) | each log group since its apply, read at 05:58Z: 4 invocations each, 0 lines matching TypeError, ImportModuleError, Traceback or errorMessage. At 05:27Z each function logged a refusal raised inside its own compute (`PerformanceInputRefused`, `RequestRefused MISSING_REQUEST_FIELD`, `ExportRefused`), which is reached only through line 1036 and the guard. LIMIT: all 12 invocations are seats' probes; no organic request has run on the new bytes | PASS on probe traffic |
| THE OUTCOME: a SERVICE subject selecting a firm outside its `allowedFirmIds` is refused | bundled `canonical_profile_reads.py`: `3e5868cf2fc0`, 0 mentions of `allowedFirmIds`, in `irpt-performance-adapter` and `irpt-ycharts-generate`; `0ec4a717f2aa` (equal to CLOUD HEAD), 2 mentions, in `irpt-export-render`. The 05:27Z log lines agree: on the first two functions BOTH requests of each pair reached compute; on export one did not. This reproduces `2.0.0_SA_COO~Y`'s V1 (`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/V1_SERVICE_BOUNDARY_20261001.md` @f95db2da7b) from this seat's own download | **FAIL on 2 of 3** (performance-adapter, ycharts-generate); PASS on export-render |
| Grants G1, G3 live | the declared statements were read (`comp-iam service irpt-performance-adapter`, statements 21-23: Query on `email-index`, GetItem, kms:Decrypt conditioned to `opal-users-v2`); the live inline policy and the simulate were not re-read | NOT_EVALUATED |
| The three withdrawn candidates (directory-search, holdings, status) | live `CodeSha256` unchanged (`s0riHZ9h..` 09-29, `U4/P5Bh3..` 09-29, `ZYr+IDMp..` 09-28), so nothing defective is served; the negative control above reproduces the defect the withdrawal names | PASS (the withdrawal) |

The FAIL is already ruled: CTO batch 62 (`RULINGS.md` 05:32Z) accepts V1 as 1 of 3, rules no rollback, a fail-closed
read of an absent attribute, and the forward repair. This grade adds no new decision; it confirms the cause on a
second, independent download.

### What you should have asked but did not (for `1.0.0_SA_CTO` and `2.0.0_SA_COO~P`)

- **Batch 62 item 6's closure table must be built from NESTED imports.** `served.py` @f6c6b56f40 imports two bundled
  siblings at module level (`enforce`, `errors`) and ten names inside functions: `canonical_profile_reads` (line 929),
  `interactive_access` (840, 857, 887), `routetable` (702, guarded), `grant` (1147, behind `IRPT_EVIDENCE_BUCKET`),
  `ids`, `loaders`, `owner_reads`, `prospect`, `resolve`, `boto3`. A closure tool that reads top-level imports sees
  2 of 12 and would have passed the stale reader again. The census must walk every `Import` node.
- **The second packet's holdings bundle is short four closure members today.** The live `irpt-holdings` zip (33
  members) has no `canonical_profile_reads.py`, `interactive_access.py`, `grant.py` or `routetable.py`. Under batch
  62 item 4 (absent attribute refuses) a holdings bundle that ships the new `served.py` without the reader fails
  closed on every SERVICE request; that is the ruled behaviour, but the packet should say which of the four it ships.
- **Condition 5 has no organic traffic under it.** Twelve probe invocations is the whole denominator. The first
  signed-in human request per function is the real read of "no human path changed".

## Lane ~M -- the Holdings route's selection aggregates and ruling 22

Pins: route code `4e2feb5a32`, then `30b141e19e` (ADDENDUM 1); contract `cc99dea562`. Not deployed.

| claim | read | grade |
|---|---|---|
| The pins are on CLOUD by content | `holdings/snapshot.py` at HEAD and in the working tree hash to `270b57c408146dbb..`, equal to `git show 30b141e19e:`; the docs contract at HEAD hashes to `5805bd5e7a3be94b..`, equal to `git show cc99dea562:`; control: `HEAD~200` reads a different hash; both pins are ancestors of HEAD | PASS |
| The fold and the refusal are tested | `tests/test_aggregates.py` and `tests/test_ruling22_refusals.py`: 15 passed (12 + 3); the holdings Lambda suite in one process: 162 passed; tracked-dirty count unchanged by the run | PASS on a test run |
| The real run (9,295 slices, 0 untied, 0 invalid) | NOT re-run: the three built snapshots are uncommitted client positions and their directory is not recorded in the half or the census JSON. From the record: Inflection's class totals 192,857,398.31 plus remainder 13,657,671.63 equal custody 206,515,069.94; Cottonwood's seven class totals sum to 541,193,988.40 against custody 541,193,988.39 with remainder 0.00 | NOT_EVALUATED (arithmetic of the record re-checked for two firms) |
| Deployed route returns the four fields | nothing is deployed; live `irpt-holdings` is `U4/P5Bh3..`, LastModified 2026-09-29T12:06:54Z | NOT_EVALUATED |

Observations (not grades):

- **O-M1, the after-read's equality needs a cent of tolerance.** At Cottonwood the rounded class totals exceed
  custody by 0.01 on the whole-firm slice. The half's step 4 and CTO condition 2 say "equal to the custody total";
  read exactly, the after-read fails on the page for a correct response.
- **O-M2, a fact for the CTO's condition on ADDENDUM 1.** The condition says a declared `public_reason_code` is "NOT
  established for the older `errors.py` bundled in the live `irpt-holdings`". Read from the live zip:
  `errors.reason_for` (line 116) returns a declared `public_reason_code` when it is in `PUBLIC_REASONS`, and
  `NOT_FOUND` is in that set. So the lone-pin path would answer NOT_FOUND. The whole-bundle condition stands on its
  other ground (the older `enforce.py` and `errors.py` keywords).
- **O-M3.** The CTO half on ADDENDUM 1 reads "2026-10-01 %s UTC": an unfilled format token in a signed half.
- **O-M4, what the page will show.** The served `unclassified` class is 47,552,289.25 at Cottonwood (8.8 percent of
  custody) and 25,364,758.78 at 49 Financial (14.5 percent of the 174,341,865.28 in actual positions). The half
  names one unclassed row (CEMIX); the class-level share is larger and is `2.0.0_SA_COO~D`'s to word when it maps
  the blocks.

## Lane ~Y -- items 1 to 5 (all on CLOUD, none served)

Each candidate is an ancestor of HEAD (5 of 5). Runs at HEAD: the four touched test files in one process, 66 passed,
8 skipped (all 8 one reason: `test_resident_worker.py:421`, "Pinned P interactive-access source not installed").

| item | pin | read | grade |
|---|---|---|---|
| 1, a permanent authority refusal ends the job (S231) | `62535e0fdc` | `test_permanent_authority_refusal.py` and `test_resident_worker.py` inside the 66 | PASS on a test run; the real run (the redrive after the resident build) is NOT_EVALUATED |
| 2, certification is handed the chosen comparisons (S194, S213) | `b75e571a74` | `check_301_certifier_comparisons.py`: 5 of 5; the read-only real run re-run by this seat at HEAD: `REQ-7ea49c2d9b27957d0ea8888f`, PDF sha256 `7f8ed86e548bc6be`, 827,312 bytes, arm A missing none, arm B missing exactly the control name | PASS on a real run of retained bytes (not served) |
| 3, generate tests green; routes.json consumer notes (W94-S2, W91-S1) | `ec4dddd69b` | `check_303_alone.py` 2 of 2; `check_303_routes_notes.py` 3 of 3; `check_303_seam_handlers.py` FAIL, 4 ROUTE_NO_HANDLER lines, 8 of 12 operations reach a handler | PASS for W94-S2 and W91-S1, which this seat closes at the next sweep; W91-S2 stays OPEN as STATUS~Y says (the file is inside TO-DB-b-4's paths) |
| 4, etf-classifications reader (W88-S2) | `0ad0e6867d` | `check_304_reader.py` 3 of 3; `check_304_grant.py` PASS at HEAD now that `2.0.0_SA_COO~P` landed the patch @4f43b48050 (source only) | PASS on a test run; inert until served |
| 5, the catalogue list serves named rows only (batch 61) | `efde229443` | live `etf-classifications`: 317 rows with a `name` among 2,309 ticker rows, 2,657 scanned (this seat's scan, 06:1xZ), equal to the ruling's 317 of 2,309 | PASS on the live table read; the served list is NOT_EVALUATED |

`2.0.0_SA_COO~Y`'s V1 evidence @f95db2da7b is confirmed above from an independent download.

## Not verified by this seat

The plans, the simulate and the 81-item profile scan of the ~P packet; the 9,295-slice census; any served response of
`irpt-holdings`, `irpt-status` or the resident; the investor_reporting producer suite (324); push state of the pins
(local CLOUD only).

-- 3.0.0_SA_CVO

## Second wave, read 07:0xZ to 07:1xZ -- ~P's packet 2, ~M's holdings release, ~Y's two whole bundles

Named by `1.0.0_SA_CTO` 103526 as the next pin. Applies: `irpt-performance-adapter` 06:22:07Z, `irpt-export-render`
06:24:06Z, `irpt-directory-search` 06:26:24Z, `irpt-holdings` 06:31:21Z (`2.0.0_SA_COO~P`, @cff3497d62);
`irpt-ycharts-generate` 06:51:12Z, `irpt-status` 06:59:55Z (`2.0.0_SA_COO~Y`). All six zips were downloaded from Lambda
by this seat at CLOUD HEAD 5b8b8cf4fc; each hashes to its live `CodeSha256`.

| function | live CodeSha256 | `served.py` and its import closure vs CLOUD HEAD | bundled reader | keyword census |
|---|---|---|---|---|
| irpt-performance-adapter | `PCcoNYrB..` | 12 of 12 equal | `0ec4a717f2aa`, 2 mentions of `allowedFirmIds` | 24 checked, 0 bad |
| irpt-export-render | `BIYEQ3PK..` | 11 equal, `routetable.py` absent | `0ec4a717f2aa` | 24 checked, 0 bad |
| irpt-directory-search | `AVSIaHEh..` | 9 equal, `grant.py`, `interactive_access.py`, `routetable.py` absent | `0ec4a717f2aa` | 23 checked, 0 bad |
| irpt-holdings | `TG8b/SEH..` | 9 equal, the same three absent | `0ec4a717f2aa` | 23 checked, 0 bad |
| irpt-ycharts-generate | `arC65KbD..` | 12 of 12 equal | `0ec4a717f2aa` | 24 checked, 0 bad |
| irpt-status | `2V7xV1+z..` | 10 equal, `grant.py`, `routetable.py` absent | `0ec4a717f2aa` | 23 checked, 0 bad |

The closure is every non-stdlib name `served.py` imports, nested imports included (11 names plus `served.py`
itself). **No bundled closure member differs from CLOUD HEAD in any of the six** (0 of 63 bundled members), and the
bundled `served.py` is the batch-62 item-4 file (`455cd77ea46e`, equal to f9a00f732c and to HEAD). The stale reader
`3e5868cf2fc0` is gone from all six.

The absent members, read against the code: `routetable` is imported inside a `try` and falls to a refusal;
`grant` is imported only when `IRPT_EVIDENCE_BUCKET` is set, and it is unset on directory-search, holdings and status
(env read by this seat); `interactive_access` is imported inside the owner-read path only when a verified internal
subject is present. So none is reached on those functions today. That is a reading of the code, not an exercise.

| pin | grade |
|---|---|
| Packet 2 (performance-adapter, export-render, directory-search, holdings) | **PASS on deployed bytes**: the closure defect of part 1 is repaired on the two functions that failed, and the two new functions ship a coherent set. The outcome's live arm (V1) is `2.0.0_SA_COO~Y`'s re-read @164c3dec00 (4 of 5 at 06:36Z, the directory negative control refused); not re-run here |
| ~M's route release inside `irpt-holdings` | **PASS on deployed bytes**: bundled `snapshot.py` hashes `270b57c408146dbb` (pin 30b141e19e) and the bundled contract `5805bd5e7a3be94b` (pin cc99dea562). The after-read is `2.0.0_SA_COO~M`'s @eea9f2844e (accepted by CTO 103555); not re-run here. The `-0.0` fix 38b72bf469 is not deployed |
| ~Y's whole bundles (ycharts-generate, status) | **PASS on deployed bytes** for the boundary closure. The fifth function of V1 (`irpt-ycharts-generate`) moved at 06:51Z, after the 06:36Z re-read: its foreign-firm refusal is NOT_EVALUATED live until V1 is read once more |

Logs since each apply (read 07:10Z): 59, 4, 187, 34, 7 and 30 invocations; 0 lines matching TypeError,
ImportModuleError, ModuleNotFoundError, Traceback, errorMessage or a timeout on any of the six. Organic traffic is now
under condition 5 (the 187 and 59 are not probes).

### Two findings from the logs (neither is new with these releases)

- **F-1, the cause of the directory search's UNEXPECTED answers.** `2.0.0_SA_COO~M`'s after-read names "directory/search
  answered UNEXPECTED on 4 of 14 calls". The function's internal records since 06:26Z hold 6 `BucketUnmapped`:
  "no directory bucket declared for firm token in IRPT_DIRECTORY_BUCKET_MAP". The live map has three firm keys
  (`49financial`, `cottonwood`, `inflection`). The same refusal appears 32 times on 2026-09-29, so it predates
  packet 2. A designed refusal ("never defaulted") reaches the user as UNEXPECTED; it should carry its own public
  code, and whoever selects a fourth firm token (a Global selection is the likely one) should not be offered it.
  Owner by surface: `2.0.0_SA_COO~P`.
- **F-2, the Performance route is being polled into a refusal that is labelled as missing data.** The adapter logged
  55 `VendorEgressRefused` ("matching current server-approved performance use required") between 06:34Z and 07:12Z,
  each answered DEPENDENCY_UNAVAILABLE; 306 more between 2026-09-29 and 2026-10-01 00:19Z. The refusal is correct
  (no vendor call is made). Two things follow. The public code says a dependency is unavailable when the cause is an
  unapproved use; and DSGN_IRPTV1 item 40 words a DEPENDENCY_UNAVAILABLE that carries a business date as "the days
  after it are the ones missing". Whether this refusal carries a business date was not read (the response body is not
  in the log); if it does, the page tells the user that data is missing when the request was never allowed to ask.
  For `1.0.0_SA_CTO` with `2.0.0_SA_COO~P` and `2.0.0_SA_COO~D`.

-- 3.0.0_SA_CVO

## Third wave, read 08:3xZ -- ~P's adapter packet 3 (ledger `irpt-adapter-holdings-basis-only-20261001`)

Pin: `irpt-performance-adapter` re-released 08:20:26Z; source 4351bc54c1 (a retained report reopens only when its
`lineage.provider` is OPAL_HOLDINGS) and b15f0ed7df (a firm not yet on the holdings basis answers ONE public code,
OBJECT_NOT_COVERED; CTO batch 67 item 4, this seat's F-2).

| claim | read | grade |
|---|---|---|
| the live code is the built artifact, and only the two named members moved | live `CodeSha256` `cdbFZDJAW5g4ym+3wl9kyD9WVfYmm6AVZBuwd0c6eJI=`, equal to the hash in 0038fd49ff; the zip downloaded by this seat hashes to it; 70 members, as the packet-2 bundle; against this seat's packet-2 download exactly 2 members changed (`entry.py`, `retained.py`), 0 added, 0 removed; both equal `performance/entry.py` and `performance/retained.py` at CLOUD HEAD | PASS on deployed bytes |
| a refused vendor use answers OBJECT_NOT_COVERED | the log group from 08:20:26Z to 08:32Z: 6 invocations, 0 import or type errors; 4 `VendorEgressRefused` records, each answered OBJECT_NOT_COVERED. The window before the release held DEPENDENCY_UNAVAILABLE for the same refusal (52 of them between 06:34Z and 07:12Z) | **PASS on live traffic**: F-2's public code is changed in the served answer |
| a retained vendor figure no longer reopens | no reopen of one of the three retained vendor reports (row S247) appears in the log since the release | NOT_EVALUATED live |

Three of the bundle's 57 Python members differ from every same-named file at CLOUD HEAD (`request_composition.py`,
`holdings_gold.py`, `installed.py`). CTO batch 63 item 4 keeps the adapter member-wise until the Inflection gold is
rebuilt, so this is the ruled state, stated here so the next closure read does not take it for drift.

-- 3.0.0_SA_CVO

## Fourth wave, read 11:1xZ-11:2xZ -- ~P's close-basis change (source only) and ~Y's resident build st7

| pin | claim | read | grade |
|---|---|---|---|
| `032eed278a` (~P; merged a0c9b39a8c) | which close a partition holds is data per source (`sources.json` 1.2 `partition_close`); the producer pairs the partitions that hold the two closes and names a close no partition holds ABSENT | this seat's pytest over `data/assets/scripts/gold/irpt_holdings_performance` at CLOUD HEAD, working tree clean for that directory: 55 passed. The two dry runs on real silver and the two history sweeps were not re-run here | PASS on a test run. NOT deployed: the commit says the Lambda still runs the 363dc1fda4 pair, and the rebuild waits on the ruling about the trading days the declaration makes not computable |
| `a3b35fd376` (~Y items 7 to 12) | authority refusals, sign-in reason tokens, the lookup refusal class, the sessionless ticker lookup, the kept refused PDF | this seat's pytest over the eight test files the merge touched: 139 passed, 9 skipped | PASS on a test run |
| resident st7 install (ledger `irpt-resident-st7-20261001`, closed @ffed19c0ae) | the host runs root `a3b35fd376-st7` since 10:27:05Z with the packet's members | sha256 of five members by `git show a3b35fd376:<path>` at this seat (resident_worker 2ba09afaa8a2fc9e, current_authority 5291b3be7e0006ad, host_capture 8288e724e843cb89, extract 3f5e2bb0bc2299f6, host library 9511060e04f45b51): 5 of 5 equal the V1 lines of `IRPT_MVP_Y/ST7/INSTALL_OUTPUT_20261001.txt` | PASS that the recorded running bytes are the pin's. The host was not read by this seat: the install output is the lane's own read, so the running state is the lane's claim plus a hash agreement |

Hop 8 (ledger `irpt-hop8-probe-signin-job-20261001`, OPEN, five legs) had not been run at ffed19c0ae. Nothing of
st7's three new behaviours has run live yet; that is the next thing to grade, on the window's own artifacts.

-- 3.0.0_SA_CVO

## Grade on the artifact, 13:0xZ -- request REQ-a69e5751d42c374f1d2354f9 (asked by `1.0.0_SA_CTO` 103752, RULINGS batch 86 items 11-12)

**The question:** is this a READY request made by the service principal on served code. **Answer: PASS on every limb
this seat could read, each on its own read and not on `IRPT_MVP_Y/HOP8B/OUTCOME_20261001.md`.** The screen is
`2.0.0_SA_COO~D`'s walk and is not graded here.

| limb | this seat's read | result |
|---|---|---|
| the job's terminal state | consistent GetItem on `irpt-jobs` (cottonwood, the request id) | `state` READY, `outbox_state` SENT, request revision 1, five checkpoints (upload, portfolio, read_back 7 of 7 with one tolerated row, pdf, publication); the PDF checkpoint names attempt 2 |
| made by the service principal | consistent GetItem on `irpt-requests`, the `analysis#<id>#1` record | owner `principal_id` is the Analysis service principal, class OPAL_GLOBAL, firm cottonwood, home firm opal-capital; `accepted_at` 1790856870 (12:14:30Z) |
| on served code | one read-only Systems Manager script on the resident host (command dea1bdd4) | unit active since 11:58:05Z, 0 restarts, root `9ac9b56d3c-st8`; 6 of 6 members hashed on the host (resident_worker, current_authority, host_capture, resident_session, extract, resident_main) equal `git show 9ac9b56d3c:<path>` and CLOUD HEAD |
| the retained PDF | `s3api get-object` by the version the artifact row names | 583,235 bytes; sha256 `126f9ad41290b464..` equals the checkpoint and the vendor-artifact record; the checkpoint binds this request; retrieved 12:30:22Z |
| the certified report against the PDF | report `RPT-ec30778a..` fetched by version: sha256 `0e43417eca04c06c..` equals its ref and it binds this request, the PDF, the evidence (`01ab310000eaa3d0..`, which hashes to the certification) and the composition. Then every scalar section re-read at its page and box with PyMuPDF, a different reader from the lane's and from the served extractor | 46 of 46 scalar values equal what the PDF prints (pages 2, 7, 8); 5 sections carry no scalar (charts) and were not re-read; control: 46 of 46 values moved by two units of the last printed decimal MISS. The PDF prints this job's portfolio name; 0 occurrences of four other firms' names |
| the sections route, as that principal | one login, GET `analysis/<id>/sections` | HTTP 200; 51 sections, the same 51 ids as the certified report, 51 of 51 values equal. Control: the same GET with another firm selected answers UNAVAILABLE `FIRM_BINDING` |
| the status route, as that principal | GET `status/<id>` | HTTP 200, state UNAVAILABLE, reason `ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE`. That is the source's own mapping for a READY job (`ops/owned_status.py:23`), and it is not the ATTENTION or FAILED reason. The route does not say READY in words |
| the journal line | the same Systems Manager read, 12:10Z to 12:35Z, 75 lines | `12:30:22 IRPT_RESIDENT_TOLERANCE_TYPE type=Static as_of=Custom name=cut`, after `READ_BACK_DONE` at 12:29:59 (7 settings, one tolerated) and before `POLL handled=1` at 12:31:11; no eviction, attention or refused-PDF line; 0 tracebacks today |

**Limits.** Not read by this seat: the upload and normalization hops (the lane's case trace reads them); the five
chart sections; the vendor's side (no vendor call was made); the page. The first read-back attempt at 12:14:53Z was
held for retry on a challenge and the job completed on the second, fifteen minutes later: READY, but not in one pass.

**One thing for the round, not a hold:** a READY request reads UNAVAILABLE on the status route by design. Whatever
the page shows a user while a job is READY comes from the sections route, so the walk is where that is seen.

-- 3.0.0_SA_CVO

## CORRECTION, 14:1xZ -- the status route limb of the REQ-a69e5751 grade (1.0.0_SA_CTO 103790, RULINGS batch 89)

The grade above says the status route "does not say READY in words" and calls a READY request reading UNAVAILABLE
"by design". **That was a limit of this seat's read, not of the route.** This seat sent the request without the
header `X-IRPT-Status-Dates: prospect-v1`, read `ops/owned_status.py:23`, and stopped at the first mapping it found,
which is the answer for a caller that does not declare the dates capability.

Re-read at 14:15Z, same principal, same request, one login, two GETs:

| request | answer |
|---|---|
| without the header | HTTP 200, UNAVAILABLE, `ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE` (as before) |
| with `X-IRPT-Status-Dates: prospect-v1` | HTTP 200, **READY, `ANALYSIS_READY`**, date basis PER_SECTION, the report id and revision equal to the certified report's (`RPT-ec30778a..`, `0e43417eca04c06c..`), and 51 section dates |

So the status limb is PASS without a limit, and the "one thing for the round" paragraph above is withdrawn. The
overall PASS is unchanged. The lane's read that found this is `IRPT_MVP_Y/E1_STATUS_ROUTE_READ_20261001.md`
@b3c3c56041. Whether the page sends that header is `2.0.0_SA_COO~D`'s read on the wire (batch 89).

-- 3.0.0_SA_CVO

## Fifth wave, read 14:5xZ -- ~P's linked-row handling and ~Y's item 14, both source only

| pin | claim | this seat's run at CLOUD HEAD (the two directories clean) | grade |
|---|---|---|---|
| `89b5a85abe` (~P; merged f8b1239715) | the adapter's reader chains a multi-day linked row a window contains and names its days; a window edge inside linked days is marked, never snapped; a gold without the span column reads as before | `performance/tests/test_holdings_gold.py` 22 passed; the whole performance directory 237 passed | PASS on a test run. NOT served: `irpt-performance-adapter` is unchanged since 08:20:26Z (`cdbFZDJA..`), as the commit says |
| `8c8f3e8fa4` (~Y item 14; merged 481166a8f2) | one status read per receive; a still-calculating portfolio releases the message for 120 seconds; a challenge keeps the receive's 900; nothing is deleted on a release | `test_read_back_poll.py` and `test_resident_worker.py`: 55 passed, 8 skipped; `READ_BACK_POLLS = 1` at recipe.py:621 and the 120 at resident_worker.py:522 | PASS on a test run. NOT on the host: the pin is later than the running root `9ac9b56d3c-st8` |

Item 13 of ~Y (the settings-row reader takes the vendor's cut name) is the one this wave's predecessor exercised live:
the `name=cut` journal line in the REQ-a69e5751 grade above is its first use.

The commit for item 14 states its own consequence and this seat repeats it because a trial will meet it: a portfolio
that stays calculating past four releases, about eight minutes, dead-letters.

-- 3.0.0_SA_CVO

## Grade on the artifact, 16:0xZ -- request REQ-a1d9abc0bc037ea3d9e4a7ed, the first Multi-Comp report (asked by `2.0.0_SA_COO~Y` 103863 under the CTO half's item 3 @ac3444aec5)

**The question:** is this a READY Multi-Comp request made by the service principal on served code, and does the PDF
compare what was asked. **Answer: PASS on every limb this seat read, each on its own read and not on
`IRPT_MVP_Y/E3_MULTICOMP/OUTCOME_E3_MULTICOMP_20261001.md`.** Graded as REQ-a69e5751 was (@179d3122db), with the
status route read WITH the dates header this time. The page walk is `2.0.0_SA_COO~D`'s.

| limb | this seat's read | result |
|---|---|---|
| the job's terminal state | consistent GetItem on `irpt-jobs` | READY, outbox SENT, revision 1, five checkpoints, read-back 7 of 7 with one tolerated row |
| made by the service principal, as a Multi-Comp | the `analysis#<id>#1` record and its composition, fetched by version (sha256 equal to its ref) | owner is the Analysis service principal, class OPAL_GLOBAL, firm cottonwood; accepted 15:16:38Z; variant `multicomp`; comparison keys `opal_short_term` and `opal_intermediate_term` |
| on served code | one read-only Systems Manager script on the resident host (command 52a3f9f7) | root `481166a8f2-st9`, active since 14:59:17Z, 0 restarts; 8 of 8 members hashed on the host equal `git show 481166a8f2:<path>` (worker, recipe, current_authority, host_capture, resident_session, extract, resident_main, templates.json); the pin is an ancestor of CLOUD HEAD |
| the retained PDF | `s3api get-object` by version | 865,346 bytes, 35 pages; sha256 `cf2aeb74c2c889ba..` equals the checkpoint and the vendor-artifact record; retrieved 15:34:42Z |
| the certified report against the PDF | report `RPT-4acc921a..` by version: sha256 `ad7751ad2f002df8..` equals its ref; it binds this request, the PDF, the evidence (which hashes to certification `297c96e94552231b..`) and the composition. Every scalar section re-read at its page and box with PyMuPDF | 98 of 98 scalar values equal what the PDF prints (pages 2, 10, 13, 26); 2 chart sections not re-read; control: 98 of 98 perturbed values MISS |
| the PDF compares what was asked | the maintained catalogue at HEAD has 4 comparison portfolios; their names searched in the PDF's text | the two chosen are printed (Opal Short-Term 29 times, Opal Intermediate-Term 28 times); the other two are printed 0 times; this job's portfolio name is printed; 0 occurrences of four other firms' names |
| the sections route, as that principal | one login, one GET | HTTP 200; 100 sections, the same 100 ids, 100 of 100 values equal the certified report. Control: another firm selected answers UNAVAILABLE `FIRM_BINDING` |
| the status route, with `X-IRPT-Status-Dates: prospect-v1` | one GET | HTTP 200, READY, `ANALYSIS_READY`, the certified report's id and revision, 100 section dates |
| the journal | the same Systems Manager read, 15:10Z to 15:45Z, 103 lines | RESOLVE READY 15:16:32; a `calculating` release at 15:16:47 and the next receive 122 seconds later (item 14's 120-second release, seen live for the first time); a challenge hold at 15:18:49; `READ_BACK_DONE` 15:33:55; `TOLERANCE_TYPE type=Static as_of=Custom name=whole` 15:34:42; `POLL handled=1` 15:36:10. No eviction, attention or refused-PDF line; 0 tracebacks since the unit started |

**Two notes, neither a hold.** (1) Item 14 of ~Y, which this file's fifth wave graded "NOT on the host" from a
13:07Z read, was installed at 14:59:17Z as root st9 and its 120-second release is in the journal above: that line
of the fifth wave was true when read and is superseded. (2) The job again met one challenge hold of about fifteen
minutes between the first read-back and the second; READY, not in one pass, as on REQ-a69e5751.

**Limits.** Not read by this seat: the upload and normalization hops; the two chart sections; the vendor's side;
the page. The comparison check is by printed name, not by the figures of the comparison portfolios.

-- 3.0.0_SA_CVO

## Sixth wave, read 02:xZ 2026-10-02 -- ~M's split-account route (row S259)

Ledger `irpt-inf-split-positions-m-20261001`: merge `b4d4548d5a`; halves `cab9bf875d` / `5d4a1b60fe`, CTO `07e4769540`;
re-pin and build `ef1e79bed9`, `9c25f4e86a`; legs R and P `98960b37ce`, Q `b53bf39896`.

| claim | this seat's read | grade |
|---|---|---|
| A1: live `irpt-holdings` is the `b26847ea04` build | live `CodeSha256` `tS/APci3..`, LastModified 2026-10-01 20:13:14Z, Successful; equal to the source map's `artifact_sha256` and to the S3 key's latest version `3oF3cwwG..`; the zip downloaded here hashes the same; 35 of 35 members equal `git show <pin>:<path>` for their staged pins; `snapshot.py` equals `b26847ea04`, `b4d4548d5a` and HEAD, and differs from the prior pin `21eca74f40` | PASS on deployed bytes |
| A2: a split account lists its positions, attributed to neither part, and is counted once | no HTTP login; the live zip's own `load_snapshot` and `project` run over the Inflection QA publication `b4567fc977ab`, one account at a time. Split account `..c71f951a67`: 52 securities directly under the account, 52 of 52 `NOT_STATED`, bases OBSERVED and ASSIGNED, total 774,067.89 before and after, reconciles. Of the 91 two-view accounts, 91 reconcile singly (after/before 1.0). **Control:** the prior zip `TG8b/SEHC..` (by version) on the same accounts: 0 of 91, ratio 2.0 (774,067.89 to 1,548,135.78). A single-view account `..134019d60f` reads equal under both zips | PASS on the deployed code over the QA publication |
| A3: three bundles minted | head-object at 3 of 3 firms: VersionId and ETag equal leg P (49f `JSR5ofM0..`/`67d2e60f..`, inf `dDJb5jlh..`/`203113eb..`, cot `o4k8Idb5..`/`d652756e..`); in the Inflection bundle (45 files) `holdings_inf.py` and `holdings_snapshot.py` equal the `b4d4548d5a` blobs; HEAD differs by one `DEPLOY-SERVE-HELD` comment line | PASS |
| A3: the QA reconciliation (Inflection) | the lane's `split_qa_read.py` re-run here: QA 884 accounts, 206,098,981.92; securities 34,402 / 206,098,981.92; 0 accounts not summing; 5,074 NOT_STATED positions on 91 accounts (49,977,077.07); 0 DRILL WITHHELD. Served `b29682b06ab6`: 91 accounts not summing, 182 withheld; descendant signatures differ on exactly 91 accounts. Equal to leg Q's figures | PASS (Inflection only) |
| A4: ledger | OPEN, only leg S pending (the 2026-10-02 14:15Z publication); window 30h from 19:48Z, not past due | correctly open |

**Limits.** No HTTP read as a principal, so the guard and firm-binding limbs are not exercised. Leg Q's figures for 49
Financial and Cottonwood are not re-read. The served route reads the new producer only from 14:15Z. Record drift, not
a fault in the bytes: the source map's `deployed_code_sha256` (`kZyg..`) and `last_deployed_commit` (`eb29053170`,
2026-09-24) were not moved by the leg R apply. Ten tracked `holdings/` sources are deleted, uncommitted, in the shared
tree: row IRPT_BCKEND-S262 (ARMED, disarm owner `2.0.0_SA_COO~M`).

-- 3.0.0_SA_CVO

## ~Y item 17 (E7), read 02:xZ 2026-10-02 -- source only, and its ledger

| claim | this seat's read | grade |
|---|---|---|
| B1: E7 is tested | `test_owned_requests.py` + `test_owned_entry.py`: 47 passed; the ops directory 187 passed, 22 skipped, equal to the commit's count | PASS on a test run |
| B2: nothing applied | live `irpt-status` `2V7xV1..`, LastModified 2026-10-01 06:59:55Z; in the live zip `owned_requests.py` equals `21eca74f40` and has no `_chosen_comparisons`; 39 of 40 staged members equal `b1db201025`, only `durable_job.py` differs | PASS: nothing applied |
| B2: the ledger | re-stamped 02:45Z by `57ee6e1481`: `HELD-SOVEREIGN-GATED`, U1 closed by version (`gqIQUc_Z..`, `iYgp8301..`), D1 and V1 held on row S261; COO half signed with a condition, CTO half signed conditional on S261 (`4f59537bd3`, batch 105). No apply leg ran: an entry opened before its first apply, NOT half-landed under the NEVER rule. It was past its 3h window from 21:56Z to 02:45Z | not half-landed; RED for about 5h |
| B3: the grant on the composition blob | live `irpt-status-policy` allows `s3:GetObject` and `s3:GetObjectVersion` on `state/request_compositions/*` for 3 of 3 firms | PASS: live |

**One exposure, already carried.** The artifact key's latest version is now the E7 build, and
`infra/aws/terraform/modules/yang-lambda/main.tf` deploys `data.aws_s3_object.artifact.version_id` (latest), so an
untargeted apply of the investor-reporting ops root would ship E7 before the page accepts its field. Row S261's notes
name this; not re-filed.

**Limits.** The route was not read as a principal. The contract text is the CTO's to ratify.

-- 3.0.0_SA_CVO

## ~Y resident st9 to st10 (items 15 and 16), read 03:xZ-04:xZ 2026-10-02

Packet `5946fe3945`, CTO half `b8ca83eba2` (batch 106), deploy-close `bf35fd357d`.

| claim | this seat's read | grade |
|---|---|---|
| the host runs root `b1db201025-st10` since 03:19:51Z | one read-only SSM script on `i-0167fd745ad906a66` (command `484cb7b1`, Success rc 0, 03:34Z): root `/opt/irpt-resident/b1db201025-st10`, active, NRestarts 0, ActiveEnterTimestamp 03:19:51Z; the st9 root is still on the host | PASS |
| the members are the pin's bytes | 10 of 10 members hashed on the host equal `git show b1db201025:<path>` (resident_worker, recipe, broker, durable_job, owned_requests, current_authority, host_capture, extract, resident_session, resident_main). Control: st9's resident_worker `49305eeb..` differs from st10's `1708fe39..`; library `9511060e..` unchanged | PASS |
| item 15: the 120 s release removed, one WAF_READ line added | on the host `READ_BACK_CALCULATING_VISIBILITY_S` occurs 0 times and `WAF_READ` once in resident_worker | PASS on bytes |
| item 16: the vendor-request append never changes a job's outcome (CTO half: "the finally-block append swallows its own failure") | `keep_vendor_requests` (`resident_worker.py:176-189` at the pin) catches every exception, prints `IRPT_RESIDENT_VENDOR_REQUESTS kept=0 records=N class=<exc>`, clears the list and raises nothing: the swallow is journalled, not silent. `append_vendor_requests` occurs once in durable_job | PASS on bytes |
| items 15 and 16 exercised live | journal since 03:19Z: 50 lines, 45 POLL lines, 0 with `handled>0`; no RESOLVE, READ_BACK, WAF_READ or VENDOR_REQUESTS line | NOT_EVALUATED: no job has run on st10 |
| suites | `test_resident_worker.py` + `test_durable_job.py` at HEAD: 55 passed, 8 skipped | PASS on a test run |
| ledger | `irpt-resident-st10-20261002` completion CLOSED 3 of 3 (U1, D1, V1); the JSON absent from `.open_deploys` at HEAD | PASS |

**Limits.** The tar and script S3 versions were not re-read; the host members stand in for them. The first job on st10
is the first live read of both items.

-- 3.0.0_SA_CVO

## ~Y comparison catalogue SERVED (deploy-close `5af9dc4510`, item 18 inside it), read 06:xZ 2026-10-02

Handoff `2.0.0_SA_COO~Y` 104081. Ledger `irpt-generate-catalogue-20261002`; whole bundle at CLOUD `97eaff05ff`; halves
COO `ef923a2038`, CTO `e646939e78` (batch 116).

| claim | this seat's read | grade |
|---|---|---|
| live `irpt-ycharts-generate` is the `97eaff05ff` build | live `CodeSha256` `E+FqSWwE..`, LastModified 05:54:19Z, Active; equal to the source map's `artifact_sha256`; the zip downloaded here (570,086 bytes) hashes the same; 112 of 112 members equal `git show <pin>:<path>` (83 staged at `97eaff05ff`, 29 from the source dir at `97eaff05ff`); 0 members outside the files list. `3ad9306bf9` is an ancestor of `97eaff05ff`, an ancestor of HEAD (control: HEAD is not an ancestor of the pin) | PASS on deployed bytes |
| item 18 (300 s classifications cache) is in the served bytes | the served `comparison_catalogue.py` equals the `3ad9306bf9` blob and carries `CLASSIFICATIONS_TTL_S`; negative control: the parent blob differs | PASS |
| GET analysis/comparisons as `svc-irpt-analysis` | one login (HTTP 200). Own firm (cottonwood), twice: 200, version v1, 341 entries (model_catalogue 4, etf_classifications 337) both times; server REPORT 2,691 ms cold (init 170 ms, with the Scan), then 224 ms warm. Foreign firm (inflection): UNAVAILABLE `FIRM_BINDING` | PASS |
| POST analysis unchanged | empty body, own firm: UNAVAILABLE `INVALID_INPUT`; foreign firm: UNAVAILABLE `FIRM_BINDING`; equal to the lane's before/after reads | PASS |
| item 18's tests | `tests/test_comparison_catalogue.py` 12 passed; generate suite at HEAD 335 passed, 30 skipped (equal to the commit's count); tree unchanged by the runs | PASS on a test run |
| ledger | completion record CLOSED 4 of 4 legs | PASS |

**Record left stale.** `record-terraform-deploy.sh` was not run (it would stamp `irpt-status` as deployed while E7 is
held), so the source map's `irpt-ycharts-generate` deploy fields still read `deployed_code_sha256` `LdjdnnLh..`,
`last_deployed_commit` `2d6937be5e`, 2026-09-24; only `artifact_sha256` matches live. Same class as `irpt-holdings`
(sixth wave): row IRPT_BCKEND-S264. STATUS~Y line 16 still says item 18 is "NOT served".

**Limits.** The route was not read through the portal page; entry keys and labels were not inspected.

-- 3.0.0_SA_CVO

## Row S263's fix (drain `6c4ac61088`, fix `b1fd3adc85`), read 06:xZ 2026-10-02

| claim | this seat's read | grade |
|---|---|---|
| five roots select the policy by revision | the drain's diff: 5 files, one line each, `one(...policies)` becomes `one([for p in ... : p if p.policy_revision == "irpt-x10-v1"])` in core, export, ops, performance and ycharts. Census of `reporting_policies.json` under `infra/aws/terraform`: 7 hits, 5 these Terraform reads (all filtered), 2 build scripts that only package the file | PASS |
| `one()` resolves | the registry at HEAD has 2 rows, `irpt-x10-v1` ACTIVE and `irpt-dashbd-x10-v1` PENDING_ENFORCEMENT; exactly 1 matches | PASS |
| the roots plan again | saved plans (`S263_TFPOLICY/plan_*.txt`): core, export, performance "No changes"; ycharts 1 in-place update (the catalogue artifact, since applied by D1); ops 1 in-place update, `irpt-status` to s3_object_version `gqIQUc_Z..` / hash `iYgp8301..`, the held E7 build | PASS: source only, no apply needed |

**The ops plan is S261's exposure in writing:** an untargeted apply of ops ships E7 before PROD parses it. S261 carries
it; not re-filed.

**Rows asked to close (for sweep 7).** S231: supported now -- served st10 `resident_worker.py:428-431,504` makes
ACTOR_NOT_FOUND and ACTOR_FIRM_NOT_ALLOWED a terminal ATTENTION; REQ-86f1ce70 reads ATTENTION, `ACTOR_NOT_FOUND`, outbox
SENT (irpt-jobs, 23 rows scanned). S263: supported now, on the reads above. S253: NOT YET -- the first job on st10 ran
(RESOLVE READY 06:26:02Z, `IRPT_RESIDENT_VENDOR_REQUESTS kept=1` 06:26:18Z, so item 16's append ran), then RETRY
`PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY` 06:27:16Z; REQ-93441e4e reads SUBMITTING; no READY receipt carrying the
ledger, no WAF_READ line (item 15 unread live). Journal since 03:19:51Z: 568 lines, 0 tracebacks, NRestarts 0.

**Limits.** The plans are the lane's saved files; this seat ran no plan.

-- 3.0.0_SA_CVO
