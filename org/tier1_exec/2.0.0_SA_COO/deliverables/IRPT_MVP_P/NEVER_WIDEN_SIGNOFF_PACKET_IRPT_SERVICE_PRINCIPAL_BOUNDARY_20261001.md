# Never-widen sign-off packet -- the served boundary refuses a SERVICE subject outside its allowedFirmIds (TO-IB-pr-271 served; IRPT_BCKEND round 27 cell IB-pr-275; row S238)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~05:1xZ. Ledger `irpt-service-principal-boundary-served-20261001` (OPEN @ac27684500, twelve legs).
Halves owed: `1.0.0_SA_CTO` (ROUND_ANALYSIS.sweep5.md @a50d8207bc section 1 row S238 and section 2 item 1; CTO 103439: "served moves
keep both halves and this seat signs on read") and `2.0.0_SA_COO~P` (signed below). No CRO half: no page text and no served figure
changes.

## 0. Scope change against the analysis: THREE functions and TWO grants now, not six and five

Sweep-5 section 2 item 1 names six functions and five grants. This packet covers three functions and two grants. The other three
candidates were DEFECTIVE and are withdrawn (commit 7823ef7e31, merged d753300219):

- `served.py` @f6c6b56f40 line 1036-1040 builds `enforce.Request(..., path_ids=...)` for every request that reaches enforcement, and
  line 107-108 calls `errors.public_line(..., admitted=...)` at every error site.
- The `enforce.py` and `errors.py` bundled in `irpt-directory-search` (@bc3727b3a3), `irpt-holdings` (@c76b7c7aee) and `irpt-status`
  (@bc3727b3a3) accept neither keyword (read from the uploaded zips: `Request.__init__(self, headers, operation, object_kind, object_id,
  params, job_id)`; `public_line(operation, public_reason_code, correlation_id)`). Applied, every request past the firm checks would have
  raised `TypeError` in those three functions.
- The 2026-09-30 candidate probe compared live against candidate on three events that all refuse BEFORE line 1036, so it read equal.
- Disarmed before this packet: the previous S3 version (metadata `content-sha256` equal to the live CodeSha256) was copied over each of
  the three keys, so their latest version is the live bytes; the three source-map rows are back at their live pins. Nothing was applied.

The three functions in this packet do not have the defect: their live `served.py` is one vintage (sha256 `3a2cdba2...`), the move is the
41-line pr-271 diff alone, and their bundled `enforce.py` and `errors.py` carry both keywords (checked on the uploaded zips, in each
of the three: `Request.__init__` lists `path_ids`; 55 module-level uses of sibling modules by `served.py`, 0 unresolved keyword or
name; `CanonicalProfileReaders.get_user` and `maintained_sources.py` present). Legs G2, G4, G5, F2, F5, F6 stay open on the ledger for a later packet.

## 1. The act, exactly, in this order

1. `safe-apply` targeted to `aws_iam_role_policy.performance_adapter_service_profile_read` (root `investor-reporting/performance`) and to
   `aws_iam_role_policy.export_render_service_profile_read` (root `investor-reporting/export`). Each plan: 1 to add, 0 to change, 0 to
   destroy. `irpt-ycharts-generate-role` already holds the same three statements (`ycharts/generate.tf`).
2. `simulate-principal-policy` on both roles: `dynamodb:Query` on the `email-index`, `dynamodb:GetItem` on the table, `kms:Decrypt` on
   the table's key with the two context entries; one resource per call; `irpt-ycharts-generate-role` as the positive control in its own
   call. All allowed, or the act stops here.
3. Three targeted `safe-apply` runs, one per function, each `Plan: 0 to add, 1 to change, 0 to destroy` on `aws_lambda_function.this`
   alone:

| function (module) | BEFORE CodeSha256 / S3 version | AFTER sha256 / S3 version | members: live -> new |
|---|---|---|---|
| `irpt-performance-adapter` (`module.irpt_performance_adapter`) | `+h/AH/RY7PK+MLuXyflt+YYzWg+jXHSXTOUBwr0EHbo=` / `TBy0pL.rwpHBE1BBqkyIDYC6Dky4QS7j` | `XslOsVc9AreOFwsgzC4frrDu4/m6ItTGeqoQRn8lN7M=` / `iDmIiCgnyXWB88FsyKGz8tdo8yvldIUA` | 70 -> 70; changed: `served.py`; added 0; removed 0 |
| `irpt-ycharts-generate` (`module.irpt_ycharts_generate`) | `inrij6hLQiz/ZtOL3Wnzu3aA3xekxlRxYSEajtYqVZw=` / `DWP1wKAI_ftLo9kcP3p_LC6vV1V2K6W2` | `ESedDkLy40enY0fsupacLrXaUXzFw+UauPKNauOqeYc=` / `BH8sOdyV6lknk1jj1qdIjIkKbDItmLVG` | 111 -> 111; changed: `served.py`; added 0; removed 0 |
| `irpt-export-render` (`module.irpt_export_render`) | `BORQ2shbblG4OIG387kkAKTxUUtbPhw6LoLVx0mqGM4=` / `O1Vu8CyDp6aKLZHRur_YhlftYjHrX.1B` | `WO5gDeP/fZ4jPl75NQ66BCR+9ixoRJVneIGsoBSxd6I=` / `9HpHNNQ_Ke98o3_MycbUdkMfBLDIDJus` | 59 -> 61; changed: `served.py`; added `canonical_profile_reads.py`, `maintained_sources.py`; removed 0 |

The member census compares each new artifact with the LIVE zip downloaded from Lambda (the downloaded bytes hash to the live
CodeSha256 in all three). The full plans of the six roots, run after the uploads at 04:5xZ: performance, directory, export, holdings and
ops each `1 to add, 1 to change, 0 to destroy`; ycharts `0 to add, 1 to change, 0 to destroy`; before the uploads each of the five read
`1 to add, 0, 0` (the grant alone) and ycharts read `No changes`. So nothing else in any root is pending.

Builds: `build-and-upload.sh investor-reporting <fn>` from a private worktree at bd968a95d3; source map @3242deb99b. `BAU_PARITY_SKIP=1`
on two builds, each named in that commit (three local build tools in `performance/`; `comparison_catalogue.py`, the pending member of
TO-IB-yr-261). Eight pending members of other cells are pinned to their live bytes, which is why each diff is `served.py` alone.

## 2. Every puller of what moves

Live plane, `lambda list-functions` auto-paginated and counted client-side: 224 functions, 11 named `irpt-*`. Exactly one function runs
each BEFORE artifact: `irpt-performance-adapter`, `irpt-ycharts-generate`, `irpt-export-render`. Source plane, `comp-find` of the three
key names over `infra/aws/terraform` (17 hits across 819 files): three comment lines in the three owning `.tf` files and 14
`CHANGELOG.json` records; no second module names any of the keys. No image, alias or layer moves.

Writers of each function's code pointer: 1 (its own module). Writers of each role's inline policy set: 1 (its own root). Writers of the
selected-firm decision for a SERVICE subject: 1 (`served.py` `Entry.handle`). Three properties, one rule each, read below.

## 3. Blast radius, by branch (the producer's own rule: `served.py` @f6c6b56f40 lines 920-947 and 990-995)

The only code that changes is reached when the trusted header `x-user-type` reads `service` AND the request selects a tenant. A human
subject never enters it.

| subject | BEFORE | AFTER |
|---|---|---|
| human, any selection | unchanged path | unchanged path (the new block is skipped) |
| SERVICE, selects a firm in its row's `allowedFirmIds` | served | served |
| SERVICE, row has no `allowedFirmIds` or the value `ALL` | served | served (unrestricted, as the row says) |
| SERVICE, selects a firm outside its `allowedFirmIds` | SERVED (the S238 hole) | refused `FIRM_BINDING` |
| SERVICE, no profile row | served | refused `FIRM_BINDING` (amendment 1 @c31230ea02: no row is never unrestricted) |
| SERVICE, the profile read raises (no grant, throttle, key denied) | served | refused `FIRM_BINDING` on every selected firm, its own included (fail closed) |

Population the SERVICE rows apply to, measured: `opal-users-v2` scan, 81 items, 52 `PROFILE` rows, `userType` values `service` 1,
`Dev` 6, absent 45. The one service principal is `svc-irpt-analysis@opalinvest.com`, `firmId opal-capital`, `allowedFirmIds
cottonwood`. After the move it is served for cottonwood and refused for every other firm.

The fail-closed branch is why the grants go first: with the code applied and the grant absent, `svc-irpt-analysis` is refused on
cottonwood too (the W27 job would fail; no human is affected). With the grants applied and the code not yet applied, nothing changes:
the roles hold a read they do not yet use.

What the grant adds to each of the two roles: `dynamodb:Query` on `opal-users-v2/index/email-index`, `dynamodb:GetItem` on the table,
`kms:Decrypt` on the table's key conditioned to DynamoDB and to this table. No Scan, no write, no wildcard.

## 4. Rollback, per key

- A function: `s3api copy-object` of its BEFORE version (table above) over the same key, then the same targeted `safe-apply` (0/1/0
  back to the BEFORE CodeSha256). Same window; both readbacks go in the ledger leg.
- A grant: it is add-only and unused by the BEFORE code; it stays through a function rollback. Removing it is deleting the root's
  `service_profile_read.tf` and one targeted apply (0/0/1 on the inline policy).

## 5. Conditions

1. Order as section 1; a simulate that is not allowed on all three actions stops the act before any code moves.
2. Before each function's apply, one `lambda invoke` of the BEFORE code with an empty-headers event; after it, the same invoke of the
   AFTER code. Both must return the `CONTRACT_VERSION` refusal envelope and no `errorMessage` (a cold import of the new bundle through
   the real entry point).
3. Post-apply `get-function-configuration` CodeSha256 equals the AFTER column; a re-plan of the same target reads `No changes`.
4. V1 (row S238's disarm): `svc-irpt-analysis` selecting a foreign firm is refused and selecting cottonwood is served, both prints read
   by `1.0.0_SA_CTO`. The run is `2.0.0_SA_COO~Y`'s (it owns that identity and the W27 job). The ledger closes at V1, never at the apply.
5. Ten minutes of each function's log group after its apply: zero `TypeError`, zero `ImportModuleError`.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~05:1xZ, on this packet's bytes at the commit that carries it. The write set is two inline policies and three
functions' code pointers; the blast radius is section 3, every branch read from `served.py` at the pin; the rollback is section 4.

## CTO half

(owed: `1.0.0_SA_CTO`, bound to this packet's pre-signature blob)
