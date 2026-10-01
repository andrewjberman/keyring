# Never-widen sign-off packet -- `irpt-ycharts-generate` and `irpt-status` as WHOLE bundles at CLOUD 21eca74f40, two grants first

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~06:4xZ.
**Authority:** CTO rulings batch 61 @8dcf5bbe7a items 2(b) and 3 (the whole-bundle rule), batch 62 @3b5f4863ce items 5
and 6 (the HEAD reader and the fail-closed `served.py` into `irpt-ycharts-generate`; the import closure printed), batch 65
@a6bba4533d (row S238 disarms on the API controls). **Ledger:** `irpt-analysis-whole-bundle-20261001` (OPEN @5d8a3b95b6;
legs B1, G1, F1, F2, V1, V2). No CRO half: no page text and no served figure changes.

## 1. The act, in this order

1. `safe-apply` targeted to `aws_iam_role_policy.generate` (root `investor-reporting/ycharts`): 0 to add, 1 to change. The
   one change is one added statement, `dynamodb:Scan` on `table/etf-classifications` (`ScanEtfClassificationsForComparisonNames`).
2. `safe-apply` targeted to `aws_iam_role_policy.irpt_status_service_profile_read` (root `investor-reporting/ops`): 1 to
   add. Three statements, the ones `irpt-ycharts-generate-role` already holds: `dynamodb:Query` on
   `opal-users-v2/index/email-index`, `dynamodb:GetItem` on the table, `kms:Decrypt` on the table's key conditioned to
   DynamoDB and to that table. Read at 06:3xZ: the policy does NOT exist on `irpt-status-role` (NoSuchEntity).
3. `simulate-principal-policy`, one resource per call: the Scan on the generate role; the three actions on the status
   role; `irpt-narrative-role` as the negative control in its own call. All allowed (and the control denied), or the act
   stops here.
4. Two targeted `safe-apply` runs, one function at a time, each on `aws_lambda_function.this` alone:

| function (module) | BEFORE: live CodeSha256 / S3 version in state | AFTER: sha256 / S3 version | members live -> new |
|---|---|---|---|
| `irpt-ycharts-generate` (`module.irpt_ycharts_generate`) | `ESedDkLy40enY0fsupacLrXaUXzFw+UauPKNauOqeYc=` / `BH8sOdyV6lknk1jj1qdIjIkKbDItmLVG` | `arC65KbDPPssn2UXFzAP/U+zzXgIiS/fIddCFR28a6M=` / `J52XmUEjOQihij3Zam1B.EAeW3GXA7yr` | 111 -> 112; changed 26; added 1 (`comparison_catalogue.py`); removed 0; 14 more differ in line endings only |
| `irpt-status` (`module.irpt_status`) | `ZYr+IDMpN0vtwnpxz+kOXKDMcjNpLrbbHdRm4TZerkY=` / `7Uz6kDd_FqoCwpEfhUNaPRkx3fsSezxJ` | `2V7xV1+zII4+g6tV722Tk5M9LWJFMzLShyjq6Q+v/J4=` / `m1LolBKFxtfUUbodMML8ZuM.Wfo6Op.C` | 43 -> 45; changed 15; added 2 (`canonical_profile_reads.py`, `maintained_sources.py`); removed 0 |

Targeted plans of the two roots, run after the uploads at 06:3xZ (`WHOLE_BUNDLE/plan_ycharts_targeted.txt`,
`plan_ops_targeted.txt`): ycharts `0 to add, 2 to change, 0 to destroy` (the role policy's one added statement; the
function's `s3_object_version` and `source_code_hash`); ops `1 to add, 1 to change, 0 to destroy` (the new policy; the
function's `s3_object_version` and `source_code_hash`, "28 unchanged attributes hidden", "4 unchanged blocks hidden").
Neither function's environment moves: `irpt-status` carries four variables and no `IRPT_EVIDENCE_BUCKET` (read live).

Builds: `build-and-upload.sh investor-reporting <fn>` from this seat's private worktree at 0e9cfbf9ff, whose tree is
21eca74f40 plus the re-pinned source map; no skip flag on either. Source map on CLOUD @3617b1001d: 83 of 83 and 40 of 40
staged entries at pin 21eca74f40; `artifact_sha256` equals each build. Both artifacts were downloaded by S3 version and
hash to the AFTER column.

## 2. The member census and the import closure (rulings batch 61 item 3, batch 62 item 6)

`live_walk/bundle_vs_live_census.py <fn> 21eca74f40 --zip <built zip>` compares the BUILT zip, the bundle the source-map
row describes at the pin, and the LIVE zip (each live zip hashes to its live CodeSha256). Line endings are folded for
text members. Full tables: `WHOLE_BUNDLE/census_<fn>.json`.

- **`irpt-ycharts-generate`: 112 members; 111 are the pin's bytes.** The one that is not is `fixtures/har/report.pdf`, a
  replay fixture whose worktree bytes differ from its blob (the live zip carries the same non-blob bytes; no served code
  path reads a replay fixture). 14 fixture and template members carry CRLF, as in the live zip.
- **`irpt-status`: 45 of 45 members are the pin's bytes; 0 carry CRLF.**
- **Import closure of `served.py`: 0 of 17 (generate) and 0 of 15 (status) closure members differ from the pin**, by this
  seat's tool and by `IRPT_MVP_P/served_import_closure.py --zip` (`closure_<fn>.json`: every member EQUAL). In the LIVE
  generate zip three closure members are older (`served.py`, `loaders.py`, `canonical_profile_reads.py`, the reader that
  left the boundary open); in the live status zip four are older and two are absent.
- `IRPT_MVP_P/sibling_interface_check.py` on the built zips: generate 17 modules, 108 cross-module calls, 0 findings;
  status 15 modules, 104 calls, 0 findings (the keyword defect that withdrew status from IB-pr-275 is absent).
- `irpt-status`'s `served.py` names two modules the bundle does not carry, `routetable` and `grant`. Both read at the
  pin: `routetable` is imported inside `try ... except ImportError` (`served.py:701-704`); `grant` only when
  `IRPT_EVIDENCE_BUCKET` is set (`:1148-1153`), which it is not on this function.

What each changed member carries (the commit the live bytes equal, and the commits the pin adds, are in the census):

| reached by | generate | status |
|---|---|---|
| the boundary | `served.py` +f9a00f732c; `canonical_profile_reads.py` +2704705672; `loaders.py` (one generated comment line) | `served.py` +8 commits (150 lines added: the route census, render-delegate path ids, render ports, the export service flow, the service boundary and its two amendments); `enforce.py` +2; `errors.py` +1; `loaders.py`; the reader and `maintained_sources.py` ADDED |
| the function's own operations | `generate_installed.py` and `entry.py` (the catalogue operation and its reader), `comparison_catalogue.py` ADDED, `uploads.py` (the correction words on a NEEDS_CORRECTION upload answer), `recipe.py` +8 (the composition's captured configuration; equal to the resident's since st6) | `status.py` (CORRECT words on NEEDS_CORRECTION), `owned_report.py` (NOT_READY for an absent report blob), `entry.py` (render ports, None without the bucket variable), `status_installed.py`, `handler.py` (directory search ranking, not a status operation) |
| bundled, run by the resident only | `resident_worker.py`, `resident_main.py`, `job.py`, `transport.py`, `broker.py`, `current_authority.py`, `publisher.py`, `publication.py`, `certify.py`, `extract.py` | -- |
| registry and contracts | `lib/opal_naming.py`, four registry files, `firm_registry.json`, two contract schemas | `lib/opal_naming.py`, four registry files, `firm_registry.json` |

## 3. Gates on the BUILT bytes (this seat's standing gates, plus the two instruments above)

| gate | generate | status |
|---|---|---|
| `zip_module_census.py --expect ...` (flat-zip name collisions) | 60 modules, 55 unique, 5 collisions, each winner the intended; FAIL none | 33 modules, 29 unique, 4 collisions, each winner the intended; FAIL none |
| `zip_cold_start_smoke.py` under the LIVE environment | PASS on `POST analysis` and on `GET analysis/comparisons`; 0 first-party modules from outside the zip | PASS on `GET status`; the owner-read refusal arm answers a NAMED refusal (UNAVAILABLE UNEXPECTED), not a 500 |
| `offline_submit_proof.py --live-env` (real composition, live reads, captured writes) | ACCEPTED on a real Cottonwood input: 9 writes captured, none left the process; 32 of 32 first-party modules from the extract | n/a |
| unit suites at the pin | `ycharts/generate/tests` 314 passed; `intake/tests` 253 passed; `_scope/tests` 207 passed; `_contracts` 184 passed | `ops/tests` 185 passed; `reports/tests` 88 passed, 1 failed (a test-path defect, `2.0.0_SA_COO~P`'s file: it passes when collected after the resident suite) |

Red and not this move's: `_authz/tests` 6 failed, 146 passed (row IRPT_BCKEND-W98-S1: the route census counts three
export routes as declared by no entry; `2.0.0_SA_COO~P`'s). `status_role_sim.py` was NOT run: its window-15 state
directory no longer exists on this device; the status role's reads are graded live by condition 4 instead.

## 4. Blast radius, by branch

Writers of each function's code pointer: 1 (its module). Writers of each role's inline policies: 1 (its root). Exactly
one function runs each BEFORE artifact (the two named). No image, alias, layer, queue, table or schema moves.

**`irpt-ycharts-generate`** (the submission, the upload, the catalogue):

| subject and request | BEFORE | AFTER |
|---|---|---|
| human, `POST analysis` / `POST analysis/inputs` | served | served; a submission's captured configuration comes from the HEAD recipe (the resident runs the same recipe since st6); a NEEDS_CORRECTION upload answer carries the correction words |
| SERVICE, selects a firm in its `allowedFirmIds` | served | served |
| SERVICE, selects a firm OUTSIDE its `allowedFirmIds` | **SERVED** (V1 measured it: INVALID_INPUT carrying Inflection's business date) | refused `FIRM_BINDING` |
| SERVICE whose row has no `allowedFirmIds` | served | refused `FIRM_BINDING` on every firm (batch 62 item 4); population 0 of 1 service principals |
| `GET analysis/comparisons` | no operation in the bundle | the operation exists and reads names with one Scan; the API route is NOT published (17 live routes, none for it), so nothing reaches it until the api root moves |

**`irpt-status`** (status, request history and read, sections):

| subject and request | BEFORE | AFTER |
|---|---|---|
| human, the five status operations | served | served; two answers change by design: sections for a report whose blob is absent read `NOT_READY` (was `UNEXPECTED`), and a NEEDS_CORRECTION envelope carries a `CORRECT` action with words |
| SERVICE, allowed firm | served (as any Opal subject) | served, once the role holds the profile read (step 2) |
| SERVICE, foreign firm or no `allowedFirmIds` | served | refused `FIRM_BINDING` |
| SERVICE, the profile read raises | n/a | refused `FIRM_BINDING` on every firm, its own included (fail closed): why the grant goes first |
| a RENDER_DELEGATE read | refused | refused (no `IRPT_EVIDENCE_BUCKET` on this function, so no render ports) |

**What this packet does NOT claim.** `irpt-status`'s `served.py` moves eight commits at once (150 lines). This seat
did not re-read each of those commits branch by branch; the HUMAN path's proof is the offline suites, the cold-start
arm under Dev-viewer headers, and conditions 4 and 6 below. This seat holds no human token: its live reads are as the
service principal.

## 5. Rollback, per key

- A function: `s3api copy-object` of its BEFORE version (table above) over the same key, then the same targeted
  `safe-apply` back to the BEFORE CodeSha256. Same window; both read-backs go in the ledger leg.
- The Scan statement: unused by BEFORE code and by any published route; it stays through a function rollback. Removing it
  is reverting the statement and one targeted apply.
- The status profile-read policy: add-only and unused by BEFORE code; it stays through a function rollback.

## 6. Conditions (each a stop)

1. The order of section 1. A simulate that is not allowed on every named action stops the act before any code moves.
2. Before each function's apply, one `lambda invoke` of the BEFORE code with an empty-headers event; after it, the same
   invoke of the AFTER code. Both return the `CONTRACT_VERSION` refusal envelope and no `errorMessage`.
3. After each apply `get-function-configuration` CodeSha256 equals the AFTER column, and a re-plan of the same target
   reads `No changes`.
4. One read set that reaches the changed path, per function, run BEFORE (done, 06:2xZ:
   `WHOLE_BUNDLE/SERVED_READS_BEFORE_20261001.json`) and AFTER with `live_walk/served_reads_before_after.py`, as the
   service principal selecting Cottonwood. Expected AFTER, per probe: status-summary `UNAVAILABLE NOT_FOUND`
   (unchanged); status-job for `REQ-7ea49c2d` unchanged (`ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE` today); request
   history 13 or more items; request read with the same keys; sections by request id 76 sections; `POST analysis` with
   an empty body `INVALID_INPUT` for Cottonwood and **`FIRM_BINDING` for Inflection** (leg V2, row S238's control on
   this function). Any other difference on a status probe is a rollback of that function.
5. Ten minutes of each function's log group after its apply: zero `TypeError`, zero `ImportModuleError`, zero
   `Unable to import module`.
6. The human path's live confirmation is `2.0.0_SA_COO~D`'s page walk of one READY request (batch 61 item 6). This seat
   tells that seat the moment `irpt-status` is applied; an `UNEXPECTED` on a human read there is a rollback of
   `irpt-status`.
7. A function whose condition 2, 3, 4 or 5 fails is rolled back in the same window, before the other function moves.
8. This packet does not open W27 and does not run the hop-7 job; that job has its own ledger leg and names the capture
   library and its three added `ctx.close()` sites (the st6 packet's condition 4).

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~06:4xZ, on this packet's bytes at the commit that carries it. The write set is one changed and one
new inline policy and two functions' code pointers; the blast radius is section 4; the rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01 06:3xZ, bound to this packet's pre-signature blob `f8c66bce79` (@40aa13548a). Signed on the order of section 1
(the Scan statement, the status role's profile read, the simulate, then two functions one at a time), the blast radius of section 4
and the rollback of section 5. The three things flagged in msg 103541 are read and accepted, section 4's stated limit included.

**Measured by this seat at signing (06:34Z-06:36Z), from BYTES:**

- Live `CodeSha256` equals the BEFORE column, 2 of 2.
- The two AFTER artifacts, downloaded by the version ids in section 1: sha256 equal to the AFTER column 2 of 2; each the latest
  version on its key; 112 and 45 members as stated.
- EVERY `.py` member of both zips compared with `git show 21eca74f40:<path>` (line endings folded): generate 61 of 61 byte-equal,
  status 34 of 34. The reader is `0ec4a717f2aa` (2 mentions of `allowedFirmIds`) and `served.py` is `455cd77ea46e` in both, the same
  two hashes this seat read in the four bundles of IB-pr-275 packet 2.
- NOT re-run here: the census, closure and interface tools, the cold-start and offline-submit gates, the suites, the plans, the
  before-reads. Non-Python members (fixtures, registry and contract files) were counted, not compared.

**Conditions, in addition to section 6's eight (each a stop):**

9. Between `irpt-status`'s apply and `2.0.0_SA_COO~D`'s walk, a human read answered `UNEXPECTED` that the before-reads did not show
   is a rollback of `irpt-status` under condition 7; the walk is asked for the same hour, not left to the next session.
10. Leg V2's print (`POST analysis` for Inflection answering `FIRM_BINDING`) is read by this seat. With V1 of IB-pr-275 packet 2,
    it is the last control row S238 waits on (rulings batch 65).
11. The catalogue's `GET analysis/comparisons` reads names with one table Scan per request. That is acceptable while no route
    reaches it. Before the api root publishes the route, the list is served from a read that is not a full-table Scan per request;
    that is a line on the catalogue's enrichment item, not a stop here.
12. Any deviation not named in this file stops the window for a new half.
