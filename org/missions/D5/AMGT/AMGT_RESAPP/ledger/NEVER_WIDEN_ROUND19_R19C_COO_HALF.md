# AMGT_RESAPP round 19 -- never-widen pair, R19-C -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at issuance.** The CTO half is
owed by `1.0.0_SA_CTO~Z` (ROUND_ANALYSIS.round18.md s.4 @5f10ddf969: "I owe the CTO half") at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_R19C_CTO_HALF.md`, under a section headed with the same
cell id. The order does not act on one half (its AC1).
**Sources:** decomposition s.27; `ledger/ROUND_ANALYSIS.round18.md` s.4 `:72-89` (@5f10ddf969); PRD v0.15
`C-EXEC-MANAGEMENT` `:738-748` (@437e219264); row `AMGT_RESAPP-Z-S194` (@896b54f147); the order
`task-orders/AMGT_RESAPP.TO-AMGT-rk-77.serve-fallback-roster.md`.
**Measured at the cut:** 2026-09-21 at HEAD `5f10ddf969`, read-only, by the issuer, with the order's own AC3, AC4 and
AC6 invocations dry-run against the live plane. Every value below is re-read by the order at spawn; where a re-read
differs, the ROLLBACK TARGET is the worker's AC4 value, never this file's.

## `AMGT-rk-77` -- serve the Bloomberg-fallback roster, labelled, with true absence labels

### THE ACT

ONE redeploy of Lambda `opal-amgt-scoped-api`, by `0.9.0_WK_AMGT_RESAPP~77`, through exactly this path:
`build-and-upload-scoped-amgt.sh` (one S3 write: a new version of
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`), then a TARGETED
`HALT_ACK=1 .tools/safe-apply.sh ... -target=module.scoped_amgt_api.aws_lambda_function.this` whose plan must read
`0 to add, 1 to change, 0 to destroy` on that one resource. Ledgered under slug `amgt-rk77-serve-fallback-roster`,
opened before the upload and closed on the post-act served read. **It spawns only after `AMGT-rk-76` (R19-B) has
drained** (order AC3 requires rk-76's `<status>complete</status>` at the worker's HEAD).

The code the artifact carries differs from the served code in EXACTLY two files, measured by subtraction over the
artifact's whole packaged population (the same 58 paths `AMGT-rk-74` censused). The served source is `7295ea257b`
(rk-74's code commit; live `CodeSha256 P4n1bVaacgbZDuC+6I0H8YoDASREqJWgSLrfUjnPom0=`, artifact `VersionId
o5x2gdqqdA.79nT7Ngpf6ymZ_LPbeN3a`). `git log --no-merges 7295ea257b..HEAD -- <58>` prints NOTHING at the cut. At the
act it may carry ONLY:
1. `lib/research/api/scoped_amgt.py` -- this cell's edit to `read_management` (commits authored by `~77`).
2. `lib/research/identity/crosswalk.py` -- **`AMGT-rk-76`** (R19-B), commits authored by `0.9.0_WK_AMGT_RESAPP~76`,
   ADDITIVE ONLY: `SLASH_SAFE_TOKEN`, `SlashSafeKeyError`, `slash_safe_key`, `security_key_from_slash_safe`,
   `security_key_partition`. Nothing on the served path calls them; rk-76's own AC3 proves every existing top-level
   name unchanged and no served key moved. Its hash is unknown at this cut; the order's AC3 admits it by AUTHOR and
   FILE and refuses anything else.

Any other packaged commit voids this half (order AC3 STOPs). `lib/research/management/**` (AMGT-rk-75, R19-A, same
round) is NOT packaged (0 of 58 paths; `scoped_amgt.py` imports nothing from `lib.research.management`, 0 hits), so it
is not a carry-along.

### BLAST RADIUS

What the act MAY move, and nothing else:
- **(B1) The `management` block served by the security routes, over the WHOLE management population** --
  `s3://opal-data-harvest/management/v1/` holds 18 objects: 15 security keys' dated objects + 3 `_pool/`. By class, measured live
  at the cut (thesis leaf, direct invoke, two invokes byte-equal over 15 of 15 names, 0 volatile paths):
  - **CSL_AU_Equity (14 officers stored) and 6861_JP_Equity (1)** -- ABSENT / ZERO_OFFICERS / `officer_count 0`
    today (FALSE: `roster_status UNRESOLVED-SOURCE`, `roster_source BLOOMBERG_FALLBACK`, `fallback.status OK`) ->
    SERVED: officers verbatim, the real `officer_count`, `roster_source BLOOMBERG_FALLBACK`, the filing's own
    `roster_status`/`roster_reason`/`absence_reason_*` beside them, `source_item` = the fixed label "Bloomberg
    COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)", `source_accession None`, `source_key` = the fallback's
    raw key, the failed filing's `source_*` as `filing_source_*`, the object's `fallback` block verbatim, NO pool read
    (`pool_read {"status": "NOT_READ", reason}`, pool averages None), and the CEO reading the SERVED branch already
    computes (`NOT_SEARCHED`, `urls_returned None` on both at the cut).
  - **The 8 FILING names** (BABA 7, BA 12, CAT 1, COST 13, HD 10, NU 9, SAP_GY 6, VLO 5 officers) -- SERVED today ->
    SERVED with EXACTLY two added keys, `roster_source` (FILING) and `roster_source_basis` (`object` for CAT; `derived:
    ...` for the 7 whose objects predate the field, every officer `source: filing`), inserted after `roster_reason`;
    every other key byte-equal.
  - **The 5 zero-officer names** (ASML_NA, HAL, INTU, KMB, PBR; 0 officers stored, UNRESOLVED-SOURCE, no fallback) --
    ABSENT / ZERO_OFFICERS / 0 today (TRUE) -> byte-equal, unchanged.
  - **A non-RESOLVED filing roster WITH officers and no fallback** -- 0 names today; would serve ABSENT with
    `absent_because ROSTER_UNRESOLVED_NO_FALLBACK` and its real count (the "an unresolved source with no fallback says
    so" arm of the ruling).
- **(B2) The `crosswalk.py` carry-along (rk-76)** -- additive functions, served path unchanged.
- **(B3) Function code attributes:** `CodeSha256`, `CodeSize`, `LastModified` of `opal-amgt-scoped-api`.
- **(B4) One new version of the artifact key** in `opal-313476888478-lambda-artifacts` (versioning `Enabled`); prior
  versions untouched.

NOT moved (asserted by the order, AC5/AC6): role `opal-amgt-scoped-api-role` and its 1 inline policy (PolicySha256
`9e440a8e5330...0494` at the cut, equal pre/post), environment keys `[HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE]`,
1 layer, timeout 29, memory 512, the route table and gateway, the 13 GET routes' status codes (13 of 13 = 200 at the
cut; LOST [] GAINED [] required), `amgt-resapp-chatter-axis` (NOT redeployed), any management, pool or crosswalk
object, the portal.

### WRITER CENSUS -- the ACT's own write set, then each named property's writers

Rows Z-S192 and Z-S193 apply: the act's OWN writes are counted one call deeper, and a named property's writers are
all counted.
- **The act's write set: N = 2 live writes**, both in the rk-74 shape: the build script's ONE artifact upload, and
  the targeted apply's ONE function-code update. The build writes otherwise only the gitignored local build dir; the
  plan precondition (`build_zip.py`, only if `chatter-axis-schedule.tf` lacks its `fileexists` guard) writes only the
  gitignored `.build/` zip, never applied (the apply is targeted). The redeployed code WRITES NOTHING at serve time:
  `read_management`'s new branches only read the management object the function already reads, and the fallback
  branch skips the pool read (one read FEWER). No S3, table or pool write.
- **Artifact key:** N = 1 writer this round -- this order. No other round-19 order builds or redeploys this function
  (rk-75 writes management objects and code outside the closure; rk-76 deploys nothing).
- **Function code of `opal-amgt-scoped-api`:** N = 1 writer -- this order's targeted safe-apply.
- **The served `management` block for a name:** N = 2 writers of its inputs this round, both read:
  (a) this cell's `read_management` rule -- the partition above;
  (b) `AMGT-rk-75` (R19-A) rewrites `ceo_public_profile` (its `basis` and a new `reason_code`) on the 3 validation
  names' management objects, which moves ONLY the served `ceo_public_profile` and `ceo_profile_reading.reason` of
  CAT/CSL/6861 -- never `roster_*`, officers or counts (rk-75's own pair: `ceo_profile` byte-equal, 3 conditional puts).
  The order's AC6 therefore sets the two CEO keys aside for those 3 names and grades the CEO reading only by
  `reading NOT_SEARCHED` and `urls_returned None`, which rk-75 does not move.
- **The management objects themselves:** 0 writers in this act.

### EXPECTED OUTCOME -- read from the producer's own rule, both branches

- **Branch A -- the population is as measured at the cut (15 names, the four classes above):** AC6 reads
  moved_to_fallback 2 (CSL 14, 6861 1), zero_unchanged 5, filing_plus_two 8, OUT_OF_CLASS 0, ZERO_OFFICERS iff zero 15
  of 15, 13 of 13 routes unchanged, policy hash unchanged. The page then renders CSL as "14 officer(s) from Bloomberg
  COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster), as of 2026-09-19", its pool line "the pool ABSENT
  (Bloomberg COMPANY_EXEC_OFFICERS carries no role start, ...)", and its CEO line NOT_SEARCHED -- all from fields the
  existing page already reads.
- **Branch B -- a management object landed or changed class between the cut and the act** (a new name, or a
  re-projection by a producer other than rk-75): the order's AC4 re-reads the population and AC6 grades against
  AC4's classes; the rule is the same (served iff officers > 0; labelled by `roster_source`), so the outcome per name
  follows its stored `officers` and `roster_source`, and nothing outside B1's block moves.
- **Branch C -- AC3 finds an unnamed packaged commit, or rk-76 not drained:** nothing is built or deployed.

### PER-KEY ROLLBACK

Read from THIS act's pre-act values (order AC4, `.scratch/rk77_pre.json`); the cut values are for orientation only.
- **Artifact key:** `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key
  research/opal-amgt-scoped-api.zip --copy-source
  "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<AC4 ArtifactVersionId>"`
  (`o5x2gdqqdA.79nT7Ngpf6ymZ_LPbeN3a` at the cut). No version is deleted; no Terraform edit.
- **Function code:** the same targeted `HALT_ACK=1 .tools/safe-apply.sh ... -target=module.scoped_amgt_api.aws_lambda_function.this`;
  then `get-function-configuration` must print AC4's `CodeSha256` (`P4n1bVaacgbZDuC+6I0H8YoDASREqJWgSLrfUjnPom0=` at the
  cut), and the 13-route census and the 15 management blocks must equal AC4's.
- **Served management block:** restored by the two steps above (no separate store holds it).
- **Management, pool, crosswalk objects, role, environment, routes:** nothing to roll back -- the act writes none.
- **Rollback trigger (any one):** post-act `CodeSha256` not equal to the uploaded sha; any of the 13 routes LOST; any
  management block OUT_OF_CLASS in AC6; a moved role policy hash. The ledger leg closes with the rollback proof and a
  BLOCKING row is filed.

### NOT COVERED

This half does not cover, and the act may not perform: any edit to `crosswalk.py` or to any
`lib/research/management/**` file; any write to a management, pool, crosswalk or filings object; any Bloomberg,
vendor or SERP call; an environment variable, role, policy, layer, timeout or memory change; any route table,
gateway route or authorizer change; any resource other than `module.scoped_amgt_api.aws_lambda_function.this` and the
one artifact key; a redeploy of `amgt-resapp-chatter-axis`; any packaged-file change other than the two named under
THE ACT (a third is a new half); a portal change (rendering `roster_reason` on a SERVED fallback block is a separate
cell); any rollback that deletes an artifact version. The held branch `wk-amgt-14-50` is not read or named as a
surface.

**Signature (COO):** signed `2.0.0_SA_COO~Z`, 2026-09-21, at the round-19 issuance (the issuance commit's hash is
the signature's vintage).
