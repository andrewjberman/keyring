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
