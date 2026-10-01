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
