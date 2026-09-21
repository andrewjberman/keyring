# AMGT_RESAPP task order -- `AMGT-rk-74` -- the served identity block names the crosswalk object that answered: `resolve_identity()` carries `crosswalk.loaded_from()` as its own field `crosswalk_source` beside `crosswalk_vintage`, closing W54-S2's second half, and `opal-amgt-scoped-api` is redeployed (carrying `AMGT-rk-68`'s `crosswalk.py` bytes) under the round-18 R18-A never-widen pair with a rollback read from THIS act's pre-act hash

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-74</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~74</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and reads or writes no
  schedule (the daily chatter schedule, chatter-axis-schedule.tf, is untouched). It OPENS one deploy-ledger entry with
  .tools/deploy_ledger.py before its first live write (the artifact upload) and CLOSES it on the post-act served read;
  the apply is TARGETED to module.scoped_amgt_api.aws_lambda_function.this and no other resource.
comp-iam: DECLARED-NOT-APPLICABLE -- the same shape as AMGT-rk-37's redeploy of this function: the code moves under
  the existing opal-amgt-scoped-api-role through the existing Terraform resource with NO change to its role, policy,
  grant, environment variable, layer, timeout or memory, and no new S3 call (the field is computed from the crosswalk
  load the function already performs). AC4/AC6 assert the role's inline policy hash IDENTICAL before and after.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~74`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **`lib/research/api/scoped_amgt.py`
AND EVERY FILE THE ADAPTER ARTIFACT PACKAGES HAS ONE WRITER AT ANY MOMENT (the single-writer queue, section 2): this
order is the ONLY round-18 order that writes or redeploys `opal-amgt-scoped-api`.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~74;`. **NEVER RUN AN INSTALL** (`terraform init` in the harvest root,
which downloads pinned providers into the gitignored `.terraform/`, is a precondition, not an install into the tree).

## 1. THE CELL, inlined in full -- `AMGT-rk-74` (R18-A; row `W54-S2`, second half; co-sign YES)

**The analysis row, verbatim (`ledger/ROUND_ANALYSIS.round17.md` @4a2f054389, `:82`):** *"R18-A | `scoped_amgt.py`
surfaces `crosswalk.loaded_from()` on the served answer as its own field (never inside the crosswalk document),
closing W54-S2's second half | `lib/research/api/scoped_amgt.py` + its tests | YES: adapter redeploy, never-widen
pair, 13/13 routes pre/post"*. The graduation table (`:47`): *"W54-S2 crosswalk vintage | PARTIAL: filter done
(`rk-68`), served-answer half open"*. Disjointness (`:87-89`): *"R18-A reads `loaded_from()` and does not edit
`crosswalk.py`. If the COO's decomposition finds R18-A must touch `crosswalk.py`, sequence R18-A behind R18-B's
`crosswalk.py` group."* **This order does NOT touch `crosswalk.py`** -- measured below: `loaded_from()` already exists
at HEAD and returns exactly the value to serve. The CTO's covering message (msg 23958, `1.0.0_SA_CTO~Z`): *"R18-A:
W54-S2's second half. scoped_amgt.py surfaces loaded_from() on the served answer as its own field. This is an
adapter redeploy with a never-widen pair; I owe the CTO half."*

**The bound this order inherits from `AMGT-rk-68` (its order, section 4, `:166-168`), verbatim:** *"THIS CELL
DEPLOYS NOTHING. BUT `crosswalk.py` IS IMPORTED BY THE PAGE ROUTE ..., SO THE NEXT `opal-amgt-scoped-api` REDEPLOY
CARRIES THIS CHANGE TO THE SERVED PLANE -- WHOEVER CUTS THAT REDEPLOY'S NEVER-WIDEN PAIR NAMES THIS CELL IN ITS BLAST
RADIUS."* **This redeploy IS that next redeploy**, and the pair names rk-68 (section 2).

**THE MEASURED STATE (issuer, 2026-09-21, read-only; re-measured by AC3/AC4 at spawn -- it may have moved):**
- **Served code:** `opal-amgt-scoped-api` `CodeSha256 QwET8XtX3Z53ylyStMoiX/yaC0Slfrc959+rUGlHGME=`, `LastModified
  2026-09-19T16:22:28Z` (the `AMGT-rk-37` redeploy), `CodeSize 800146`, `Timeout 29`, `MemorySize 512`, `Layers 1`,
  `EnvKeys [HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE]` (NO `AMGT_CROSSWALK_PATH` -- so the served load is the
  POOL branch), role `opal-amgt-scoped-api-role`. Artifact `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
  current `VersionId YjjMpD9ULicxQPnExgUVIbVQkUOQ_l8k` (16:14:30Z), bucket versioning `Enabled`.
- **Served SOURCE is `55e3a56854`** (the rk-37 worker tip, `ba25e6f4d7^2`). **THE CARRY-ALONG, measured by subtraction
  over the artifact's WHOLE packaged population** -- the 50 source files of the build script's transitive import
  closure (`build-and-upload-scoped-amgt.sh` embedded python, its seed dirs `lib/research/{api,metrics,checkface,rules,watchlist}`
  and closure roots `lib.research`, `lib.opal_data_harvest`), the 7 `DATA_MEMBERS` and the build script itself, 58
  paths: `git log 55e3a56854..HEAD -- <58 paths>` prints EXACTLY ONE commit, `0164b134ac` (`AMGT-rk-68`, round 16),
  on EXACTLY ONE file, `lib/research/identity/crosswalk.py` (+42/-5). Rounds 16-17's other cells (rk-65, 66, 67, 69,
  70) touch no packaged path. **So this artifact moves exactly two things: your `scoped_amgt.py` edit and rk-68's
  `crosswalk.py`.**
- **`crosswalk.py` @HEAD (938 lines):** `CROSSWALK_KEY_RE` `:69` (`^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$`),
  `CrosswalkKeyShapeError(LookupError)` `:72`, `_RESOLVED_FROM` `:650` (held BESIDE the document, keyed by the same
  cache key `load_crosswalk()` uses), `load_crosswalk()` `:698-719` (pool branch records `"s3://%s/%s" % (POOL_BUCKET,
  key)` at `:716`, local branch `"file:%s" % source` at `:713`), `loaded_from(path=None)` `:722-733` (loads if not
  cached, returns the recorded string), `_read_pool_latest()` `:736-` (paginated listing, refuses any non-matching key
  with `CrosswalkKeyShapeError` before reading any object). **No edit to this file is needed or permitted.**
- **Live crosswalk prefix:** `opal-data-harvest` `crosswalk/v1/` holds 2 keys, 2 matching `CROSSWALK_KEY_RE`, 0
  non-matching; newest `crosswalk/v1/2026-09-19.json`; each document's `as_of` equals its key's date (2 of 2). So after
  this redeploy rk-68's filter does NOT fire on today's population, and the served field reads
  `s3://opal-data-harvest/crosswalk/v1/2026-09-19.json` beside `crosswalk_vintage "2026-09-19"`.
- **`scoped_amgt.py` @HEAD (3775 lines; last commit `fe0435ce53`):** `from lib.research.identity import crosswalk`
  `:115`; `_identity_block(requested, security_key, display_ticker, bloomberg, status, basis, vintage, reason=None)`
  `:1697-1722` -- seven keys in a DELIBERATE order (`security_key, identity_status, crosswalk_vintage, display_ticker,
  bloomberg, requested, identity_basis`) plus `reason` when set; `_crosswalk_vintage()` `:1725-1730`
  (`document.get("as_of")` of the cached load); `resolve_identity()` `:1733-1830` -- the ONE boundary: `try:
  record = crosswalk.resolve(requested_text); vintage = _crosswalk_vintage()` / `except Exception as err: record =
  None; reason = "crosswalk not read: ..."` `:1772-1777`, then THREE `_identity_block` call sites: MEASURED via the
  crosswalk `:1784`, MEASURED on the landed block `:1807`, UNRESOLVED `:1821`. The `/security/` arm `:3609`;
  `scoped_amgt_route_table()` `:3745` -- 16 routes, 13 GET.
- **Consumers of the identity block (a new key must break none):** `lib/research/api/tests/test_route_boundary_identity.py:111`
  reads `block["crosswalk_vintage"]`; `test_generation_and_pool_routes.py:291`, `:379` build stub blocks (they do not
  compare against `_identity_block`'s key set); the portal reads `identity.crosswalk_vintage`
  (`portal/src/pages/SecurityAnalysis/types.ts:319`, `components/IdentityLine.tsx:64`) and ignores an unknown key.
  `crosswalk_source` occurs NOWHERE in `lib/`, `infra/aws/lambda/research/` or `portal/src` at HEAD (0 hits) -- no
  collision.
- **This order's AC4, dry-run by the issuer 2026-09-21 (read-only, output to scratch):** `live_crosswalk_keys 2 matching 2
  non_matching 0`; `pre_census 13 of 13` all 200; `pre_identity_blocks 7 of 8 security routes carrying_crosswalk_source 0
  vintages ['2026-09-19']`; role 1 inline policy, `PolicySha256 9e440a8e5330...`; BucketVersioning `Enabled`.
- **Test baselines at HEAD:** `lib/research/api/tests` 179 passed; `lib/research/identity/tests` 49 passed;
  `test_route_boundary_identity.py` 13 passed; `test_scoped_amgt_mount.py` 5 passed.

**RULED, what you build:**
1. **The field.** `_identity_block` gains ONE keyword parameter `source: Optional[str] = None`, and the dict gains
   the key `"crosswalk_source": source` placed IMMEDIATELY AFTER `"crosswalk_vintage"`. No existing key is renamed,
   removed, re-ordered relative to the others or re-valued. The docstring gains one sentence: `crosswalk_source` is
   the resolved object the crosswalk load answered from (`crosswalk.loaded_from()`), held on the served block, never
   inside the crosswalk document.
2. **The read.** In `resolve_identity()`, declare `source: Optional[str] = None` beside `vintage`, and set
   `source = crosswalk.loaded_from()` INSIDE the same `try` as `vintage`, on the line after it. When the crosswalk
   is not read, `source` stays `None` exactly as `vintage` does, and the existing `reason` carries why. All THREE call
   sites (`:1784`, `:1807`, `:1821`) pass `source=source`. `loaded_from()` is called with NO argument, the same
   source `load_crosswalk()` is called with in `_crosswalk_vintage()` -- it answers from the cache and is not a
   second S3 read. Nothing else in the module moves; the route table is untouched.
3. **The test**, `lib/research/api/tests/test_crosswalk_source_field.py`, offline by construction (the pattern of
   `test_route_boundary_identity.py`: `AMGT_CROSSWALK_PATH` pointed at the committed copy
   `deliverables/0.9.0_WK_AMGT_RESAPP~19/crosswalk.v1.2026-09-15.json`, the landed-block fixture from
   `conftest.land_model_block_in_pool`, and a fail-loud DynamoDB seam). Arms, each printing its denominator:
   (a) a MEASURED form (`BABA_US_Equity`, `BABA US`, `BABA_US`) -- 3 of 3 blocks carry `crosswalk_source ==
   "file:" + <copy path>` and `== crosswalk.loaded_from()`; (b) the landed-only control `BABACVOCTRL_US_Equity`
   (MEASURED on the landed block) carries the same value; (c) `ZZZ_NOPE_Equity` (UNRESOLVED) carries the same value;
   (d) with `crosswalk.resolve` monkeypatched to raise `crosswalk.CrosswalkKeyShapeError("planted")`, the block is
   UNRESOLVED, `crosswalk_source is None`, `crosswalk_vintage is None`, and `reason` starts
   `"crosswalk not read: CrosswalkKeyShapeError"` -- no exception escapes; (e) KEY ORDER: for every block above,
   `list(block)` with `"crosswalk_source"` removed equals HEAD's key order, and `"crosswalk_source"` sits at index 3
   (right after `crosswalk_vintage`); (f) the loaded document carries no `crosswalk_source`, `loaded_from` or
   `resolved` key (the value lives on the served block only). `test_scoped_amgt_mount.py` passes UNCHANGED.
4. **The deploy**, per section 3's DEPLOY block, under the pair, ledgered, with the rollback read from THIS act's
   pre-act values (AC4).

**Blast radius, for the halves to name (each writer counted -- ONE writer of the artifact key and ONE of the
function: this order):** (i) the identity block of every `/security/{key}/{overlay|thesis|peers|coverage|print|ledger|versions|compare}`
response GAINS one key, `crosswalk_source`; every other identity key keeps its value and order; (ii) `AMGT-rk-68`'s
`crosswalk.py` reaches the served plane: the pool listing becomes paginated and a non-dated key under
`crosswalk/v1/` now REFUSES the load (`CrosswalkKeyShapeError`) where the served bytes took newest-by-sort -- on
today's prefix (2 of 2 matching) it does not fire, and if it ever fires `resolve_identity`'s `except` turns it into
an UNRESOLVED identity with its reason, never a 500; (iii) `CodeSha256`, `CodeSize` and `LastModified` of
`opal-amgt-scoped-api`. NOT moved: the role and its policies, environment, layers, timeout 29, memory 512, the route
set, the gateway, any other function, any pool object, any table, `crosswalk.py` itself. **Rollback (the COO half's
`AMGT-rk-74` section states it; this is its shape):** `aws s3api copy-object` of the PRE-ACT artifact `VersionId`
(AC4) back onto the key, then the same targeted `safe-apply`, then `CodeSha256` read equal to AC4's pre-act value
and the 13-route census equal to AC4's baseline.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`):** the field is proven on a DRY RUN -- in-process `resolve_identity()`
calls on your worktree's bytes over three forms of one measured name, the landed-only control, an unresolved form
and a planted crosswalk refusal (AC2), none of which runs a producer or writes anywhere. The served plane is then
checked, not fleet-run: the 13 GET routes on ONE keyed name (`BA_US_Equity`, the round-13/14 sample), before and
after. `C-PRODUCTION-HOME`: the artifact is built from the repository's own sources; no worker folder is read by
production code (the two `~5/lists` data members are packaged by the build script exactly as today and are not
changed by this order).

**A DIRECT ACT RAN BESIDE THIS ROUND** (`AMGT-rk-48`, the live CEO search, `<direct_act>true</direct_act>`, drained
@5a2ebfa1e1): it rewrote `management/v1` objects in `opal-data-harvest` that the served routes READ. So the 13-route census
compares STATUS CODES only, never response bodies; the identity-block comparison in AC6 compares ONLY the
identity block (which reads the crosswalk, never `management/v1`).

## 2. WHERE THIS CAME FROM

**ROUND 18**, decomposition s.26 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-17 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round17.md` @4a2f054389 (`:47`, R18-A `:82`, disjointness
`:87-89`, the COO's L5 row `:100`) and msg 23958; the bound in `AMGT-rk-68`'s order section 4 (`:166-176`); row
`W54-S2` (its first half closed by rk-68 @0164b134ac).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The
pair is TWO ledger files: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18A_COO_HALF.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18A_CTO_HALF.md` (owed by `1.0.0_SA_CTO~Z` per msg
23958). "The pair is on file" MEANS: both files exist in your worktree, each carries a section headed `AMGT-rk-74`,
and that section names this order's blast radius -- INCLUDING `AMGT-rk-68` / `0164b134ac` -- and the per-key
rollback. Read both BEFORE your first live act and paste both files' sha256 into your report (AC1). Either file
absent, its `AMGT-rk-74` section missing, or rk-68 unnamed in it: run ONLY the read-only criteria (AC1, AC2, AC3),
file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

**ISSUER RULE -- THE SINGLE-WRITER QUEUE AND THE CARRY-ALONG (`2.0.0_SA_COO~Z`):** the artifact packages 58 repo
paths (section 1). Before `build-and-upload-scoped-amgt.sh` you run AC3, which (i) lists commits on `SITEZ` since
your worktree's merge-base on those 58 paths -- it MUST print nothing; anything printed means another act landed on a
packaged file since your spawn (R18-B is DEFERRED past manager review by Andrew-direct ~16:5xZ, so no round-18 order is a known candidate) -- STOP
with a BLOCKING row and deploy nothing; and (ii) lists the carry-along from the served source `55e3a56854` to your
HEAD on the same 58 paths -- it MUST be exactly `0164b134ac` plus your own commit(s) on `scoped_amgt.py` and the new
test. Any OTHER commit is a packaged change the pair does not name: STOP with a BLOCKING row; the issuer re-cuts
the halves, you never widen them.

**ISSUER RULE -- THE ROLLBACK MECHANISM:** the Terraform module (`infra/aws/terraform/modules/yang-lambda/main.tf`)
declares `data "aws_s3_object" "artifact"` with bucket and key only and ALWAYS resolves the CURRENT version, so a
rollback NEVER edits the module and never names a VersionId to Terraform. Rollback = restore the pre-act bytes as
the current version -- `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<pre-act VersionId>"`
(bucket versioning measured `Enabled` by the issuer 2026-09-21; AC4 RE-MEASURES it and you STOP if it reads anything
else) -- then the SAME targeted `safe-apply`, and `get-function-configuration` must print the pre-act `CodeSha256`
again. Record all of it before acting; exercise none of it unless rolling back. EVERY AMGT_RESAPP byte lands in
`opal-data-harvest`; this order writes to NO pool bucket at all -- its one S3 write is the Lambda artifact key in
`opal-313476888478-lambda-artifacts`, exactly as every prior redeploy of this function.

**COLLISIONS, checked at the cut (names only):** round 18 is TWO cells (R18-A, R18-C) after Andrew-direct ~16:5xZ
(record @c5532df80a): R18-B (production-home residue) is DEFERRED past manager review -- when it returns, any of its
groups touching one of the 58 packaged paths drains AFTER this order and carries its own pair -- and R18-D' is
parked. R18-C (CSL seed, battery code) touches no packaged path. The held branch `wk-amgt-14-50` is NEVER read, shown, diffed or checked out; its name is not a path
this order touches.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_crosswalk_source_field.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~74/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-74.served-crosswalk-vintage-field.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND18_R18A_*_HALF.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `lib/research/identity/crosswalk.py`,
  `infra/aws/terraform/harvest/scoped-amgt-api.tf`, `build-and-upload-scoped-amgt.sh`, `.tools/safe-apply.sh`,
  `.tools/deploy_ledger.py`, the round-14 `AMGT-rk-61` change-management entry and `lib/research/api/tests/*.py`
  freely); this block governs WRITES. **`crosswalk.py` is NOT granted: it is read, never written.** The two halves
  are granted so the pair can be read from your worktree; you never edit them. Scratch is `<your worktree>/.scratch/`
  only; the gitignored `.build/` and `.terraform/` under the harvest root are build outputs, never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~74 <0.9.0_WK_AMGT_RESAPP~74@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Commit the
  adapter edit and the test BEFORE the deploy so the artifact corresponds to a commit; name that hash in the ledger
  entry's title.
- **DEPLOY -- the procedure, in this order, each step's evidence recorded verbatim in the ledger entry:**
  0. AC1, AC2, AC3, AC4 pass (read-only). AC1 failing = STOP. AC3 printing anything unexpected = STOP.
  1. `python .tools/deploy_ledger.py open --slug amgt-rk74-served-crosswalk-source --title "<AMGT-rk-74: crosswalk_source on the identity block + rk-68 crosswalk.py 0164b134ac; commit <hash>; co-signed R18-A pair COO <sha256> / CTO <sha256>>" --author 0.9.0_WK_AMGT_RESAPP~74 --leg "L1|verify|module.scoped_amgt_api.aws_lambda_function.this|targeted apply 0 destroy + 0-diff replan + CodeSha256 == uploaded sha + 13-route census LOST=[] GAINED=[] + identity blocks equal pre-act minus crosswalk_source + crosswalk_source == newest pool key + role policy sha unchanged"`
     -- BEFORE the first live write; the sentinel lands in `org/critical_paths/.open_deploys/`.
  2. `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` -- record the local artifact sha256 (base64)
     it prints and the `VersionId` line after the upload into `.scratch/rk74_upload.json` as
     `{"sha256_b64": ..., "version_id": ...}` (written by the Write tool or python, never a shell heredoc).
  3. `terraform -chdir=infra/aws/terraform/harvest init -input=false` once.
  4. Plan precondition: if `chatter-axis-schedule.tf` carries `fileexists(local.chatter_axis_zip)` (`AMGT-rk-59`
     landed) nothing is needed; otherwise run `python infra/aws/terraform/harvest/lambda_src/build_zip.py` (writes
     only the gitignored `.build/` zip; the apply is targeted, so that zip is never applied). NEVER a placeholder zip.
  5. `terraform -chdir=infra/aws/terraform/harvest plan -input=false -lock=false -no-color -target=module.scoped_amgt_api.aws_lambda_function.this`
     -- must read `Plan: 0 to add, 1 to change, 0 to destroy.` naming ONLY that resource with `source_code_hash`
     (and the attributes the provider derives from it) changing. Any other resource, any destroy, any replace: STOP,
     row, ledger left OPEN with the reason, no apply.
  6. `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -auto-approve -lock-timeout=60s -target=module.scoped_amgt_api.aws_lambda_function.this`
     -- must read `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` Never bare `terraform apply`, never
     `aws lambda update-function-code`.
  7. AC5, AC6. Then `python .tools/deploy_ledger.py close-leg --slug amgt-rk74-served-crosswalk-source --leg-id L1 --proof "<AC5 and AC6 output verbatim>"`
     and `python .tools/deploy_ledger.py close --slug amgt-rk74-served-crosswalk-source`; commit the entry (it is
     COMMITTED, never left staged).

## 4. BOUNDS

**THIS ORDER MOVES SERVED OUTPUT.** It does so ONLY under the pair (section 2), ONLY after AC3 prints what it must,
ONLY through steps 1-7 above, and ONLY on `module.scoped_amgt_api.aws_lambda_function.this`. **THE ROLLBACK BRANCH:**
if AC5 reads a `CodeSha256` other than the uploaded sha, or AC6 LOSES any of the 13 routes, or any identity block
differs from its pre-act value in any key but `crosswalk_source`, or `crosswalk_source` is absent or unequal to the
newest pool key, or the role policy hash moved -- execute the rollback the COO half's `AMGT-rk-74` section names
(copy the AC4 `VersionId` back onto the artifact key, the same targeted `safe-apply`, `CodeSha256` read equal to
AC4's pre-act value, the census re-run equal to AC4's baseline), file a BLOCKING row, close the ledger leg with the
rollback proof. NEVER leave the deploy half-landed (CLAUDE.md NEVER-2).
PORTAL FROZEN (not your surface; displaying the field is not this cell). **COLLECTION STAYS OFF.** **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** Secrets through `comp-secrets` only (none is needed).
**No vendor call** (every live read is a `lambda.invoke`, `get_function_configuration`, `head_object`,
`get_bucket_versioning`, `list_objects_v2`, `get_role_policy` or a Terraform plan against Opal's own estate). **No
S3 write but the artifact key; no pool write; no crosswalk write.** No non-ASCII in anything you write. **PUSH:
never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing
`crosswalk.py`, never by adding the field INSIDE the crosswalk document, never by an environment variable, and
never by editing the route table. **If AC4 finds ANY non-matching key under `crosswalk/v1/`, STOP before the build
with a BLOCKING row naming the key:** rk-68's filter would turn every served identity UNRESOLVED on this redeploy,
and whether to proceed is the issuer's call, not yours.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the pytest baselines (179, 49,
13, 5), the 13-route statusCodes and the crosswalk prefix are re-measured at spawn; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W74-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import hashlib, io, os, re
d = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/"
for half in ("NEVER_WIDEN_ROUND18_R18A_COO_HALF.md", "NEVER_WIDEN_ROUND18_R18A_CTO_HALF.md"):
    p = d + half
    if not os.path.exists(p):
        print(half, "ABSENT"); continue
    b = io.open(p, "rb").read()
    t = b.decode("utf-8", "replace")
    heads = [l for l in t.splitlines() if l.startswith("#") and "AMGT-rk-74" in l]
    print(half, "sha256", hashlib.sha256(b).hexdigest(), "rk74_section_headings", len(heads), "of 1", "mentions_rollback", len(re.findall(r"(?i)rollback", t)), "mentions_VersionId_or_CodeSha256", len(re.findall(r"VersionId|CodeSha256", t)), "names_rk68", len(re.findall(r"AMGT-rk-68|0164b134ac", t)))
'</invocation><expect>both halves present, each printing a 64-hex sha256, rk74_section_headings 1 of 1, mentions_rollback at least 1, mentions_VersionId_or_CodeSha256 at least 1 and names_rk68 at least 1 -- the pair is on file, its AMGT-rk-74 sections name a rollback read from this act's own pre-act values, and both name the rk-68 carry-along; an ABSENT half, 0 of 1 headings or names_rk68 0 REFUSES this criterion and STOPS the order after AC2 and AC3 (read-only)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests lib/research/identity/tests -q 2>&1 | tail -15 && python -m pytest lib/research/api/tests/test_crosswalk_source_field.py -q -s 2>&1 | tail -25</invocation><expect>the first run's final line reads "N passed" with 0 failed and N at least 228 + K, where 228 = the 179 api and 49 identity tests re-measured at spawn and K the new file's tests; the second run passes and prints each arm's denominator: (a) 3 of 3 MEASURED forms carry crosswalk_source equal to "file:" + the committed copy path and equal to crosswalk.loaded_from(); (b) the landed-only control carries the same value; (c) the UNRESOLVED form carries the same value; (d) the planted CrosswalkKeyShapeError yields UNRESOLVED with crosswalk_source None, crosswalk_vintage None and a reason starting "crosswalk not read: CrosswalkKeyShapeError", no exception escaping; (e) every block's key order with crosswalk_source removed equals HEAD's order and crosswalk_source sits at index 3; (f) the loaded document carries none of crosswalk_source, loaded_from, resolved; test_scoped_amgt_mount.py passes UNCHANGED inside the first run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && set -- infra/aws/lambda/research/scoped_amgt_api/lambda_function.py lib/opal_data_harvest/__init__.py lib/opal_data_harvest/catalog.py lib/opal_data_harvest/storage.py lib/research/api/__init__.py lib/research/api/scoped_amgt.py lib/research/checkface/__init__.py lib/research/checkface/fixtures.py lib/research/checkface/markers.py lib/research/checkface/render_print.py lib/research/checkface/run_checks.py lib/research/checkface/salience_fixture.py lib/research/checkface/scopes.py lib/research/coverage/__init__.py lib/research/coverage/pool_reader.py lib/research/drafting/__init__.py lib/research/drafting/pipeline.py lib/research/drafting/producer.py lib/research/drafting/verbatim.py lib/research/freshness/__init__.py lib/research/freshness/build_view.py lib/research/identity/__init__.py lib/research/identity/crosswalk.py lib/research/ledger/__init__.py lib/research/ledger/ledger.py lib/research/lists/__init__.py lib/research/lists/rot.py lib/research/metrics/__init__.py lib/research/metrics/chatter_axis.py lib/research/metrics/chatter_gate.py lib/research/metrics/generation_writer.py lib/research/metrics/movement_gate.py lib/research/price/__init__.py lib/research/price/axis.py lib/research/print/__init__.py lib/research/print/render_pack.py lib/research/provenance/__init__.py lib/research/provenance/render_print.py lib/research/provenance/validate.py lib/research/rules/__init__.py lib/research/rules/figure.py lib/research/rules/identity.py lib/research/rules/item.py lib/research/rules/peer.py lib/research/rules/sentence.py lib/research/rules/source.py lib/research/scores/__init__.py lib/research/scores/classify.py lib/research/watchlist/__init__.py lib/research/watchlist/store.py lib/opal_data_harvest/article.schema.json lib/opal_data_harvest/security-article.schema.json lib/research/drafting/schema.json lib/research/rules/data/peer_overlap.json lib/research/rules/data/figure_units.json "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/publishers.json" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/social_accounts.json" infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh && echo "packaged_paths $# of 58" && B=$(git merge-base HEAD SITEZ) && echo "base $B" && echo "packaged_commits_on_SITEZ_since_base: $(git log --oneline $B..SITEZ -- "$@" | wc -l) of 0 expected" && git log --oneline $B..SITEZ -- "$@" && echo "carry_along_from_served_source_55e3a56854:" && git log --format="%h %s" 55e3a56854..HEAD -- "$@" | cut -c1-120 && echo "carry_along_files:" && git diff --stat 55e3a56854 HEAD -- "$@" | tail -8 && echo "positive_control_last_crosswalk_commit: $(git log --oneline -1 -- lib/research/identity/crosswalk.py | cut -c1-60)"</invocation><expect>packaged_paths 58 of 58; packaged_commits_on_SITEZ_since_base: 0 of 0 expected and the SITEZ log itself prints nothing (no act landed on a packaged file since this worktree's base -- the single-writer queue holds); carry_along_from_served_source_55e3a56854 lists EXACTLY 0164b134ac (AMGT-rk-68) plus this worker's own commit(s), and carry_along_files names EXACTLY lib/research/identity/crosswalk.py, lib/research/api/scoped_amgt.py (the new test file is not packaged); positive_control_last_crosswalk_commit prints one line (the log instrument works and the empty SITEZ read is a true zero). ANY other commit or file is a STOP with a BLOCKING row and no deploy</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch && python -c '
import boto3, hashlib, io, json, re
from lib.research.api import scoped_amgt
lam = boto3.client("lambda"); s3 = boto3.client("s3"); iam = boto3.client("iam")
cfg = lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")
pre = {"CodeSha256": cfg["CodeSha256"], "LastModified": cfg["LastModified"], "CodeSize": cfg["CodeSize"], "Timeout": cfg["Timeout"], "MemorySize": cfg["MemorySize"], "Layers": len(cfg.get("Layers", [])), "EnvKeys": sorted((cfg.get("Environment") or {}).get("Variables", {}).keys())}
ho = s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
pre["ArtifactVersionId"] = ho.get("VersionId"); pre["ArtifactETag"] = ho.get("ETag")
pre["BucketVersioning"] = s3.get_bucket_versioning(Bucket="opal-313476888478-lambda-artifacts").get("Status")
role = cfg["Role"].rsplit("/", 1)[-1]
names = sorted(iam.list_role_policies(RoleName=role)["PolicyNames"])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)["PolicyDocument"] for n in names}
pre["Role"] = role; pre["InlinePolicies"] = len(names); pre["PolicySha256"] = hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest()
keys = []
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="crosswalk/v1/"):
    keys.extend(o["Key"] for o in page.get("Contents", []))
bad = [k for k in keys if not re.match(r"^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$", k)]
pre["CrosswalkNewest"] = "s3://opal-data-harvest/" + max(keys) if keys and not bad else None
print("live_crosswalk_keys", len(keys), "matching", len(keys) - len(bad), "non_matching", len(bad), bad, "newest", pre["CrosswalkNewest"])
def invoke(path, qs=None):
    ev = {"rawPath": path, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    if qs: ev["queryStringParameters"] = qs
    body = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    inner = body.get("body"); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == "{" else {}
    return body.get("statusCode"), inner
key = "BA_US_Equity"
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith("GET")]
census = {}; ident = {}
for r in routes:
    p = r.replace("{movement}", "trending").replace("{subject}", "chatter").replace("{security_key}", key)
    st, inner = invoke(p, {"tickers": "BA US"} if "timeseries" in p else None)
    census[r] = st
    if isinstance(inner.get("identity"), dict): ident[r] = inner["identity"]
print("pre_census", len(census), "of 13 GET routes", json.dumps(census))
print("pre_identity_blocks", len(ident), "of", sum(1 for r in routes if "/security/" in r), "security routes", "carrying_crosswalk_source", sum(1 for v in ident.values() if "crosswalk_source" in v), "vintages", sorted({v.get("crosswalk_vintage") for v in ident.values()}, key=str))
pre["census"] = census; pre["identity"] = ident
io.open(".scratch/rk74_pre.json", "w", encoding="utf-8", newline="\n").write(json.dumps(pre, indent=1, default=str))
print("PRE-ACT", json.dumps({k: pre[k] for k in ("CodeSha256", "LastModified", "CodeSize", "ArtifactVersionId", "BucketVersioning", "Role", "InlinePolicies", "PolicySha256", "Timeout", "MemorySize", "Layers", "EnvKeys")}, default=str))
'</invocation><expect>PRE-ACT prints the LIVE CodeSha256 (QwET8XtX3Z53ylyStMoiX/yaC0Slfrc959+rUGlHGME= at the cut; re-measure), LastModified, CodeSize, the artifact's current VersionId (the rollback target of THIS act; YjjMpD9ULicxQPnExgUVIbVQkUOQ_l8k at the cut), BucketVersioning Enabled, the role name with its inline policy count and PolicySha256, Timeout 29, MemorySize 512, Layers 1 and the two env keys (no AMGT_CROSSWALK_PATH); live_crosswalk_keys N with non_matching 0 [] and the newest key printed (2 of 2 matching, newest s3://opal-data-harvest/crosswalk/v1/2026-09-19.json at the cut) -- ANY non-matching key is the section-4 STOP; pre_census 13 of 13 GET routes with each statusCode recorded; pre_identity_blocks M of 8 security routes (M 7 of 8 at the issuer's dry run of this exact invocation, 2026-09-21: every security leaf but print, whose body is not JSON; re-measure) with carrying_crosswalk_source 0 and vintages ['2026-09-19'] -- the defect baseline: the served block does not say which crosswalk object answered; all of it written to .scratch/rk74_pre.json for AC6. BucketVersioning other than Enabled is a STOP</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, io, json, re, subprocess
up = json.load(io.open(".scratch/rk74_upload.json", encoding="utf-8"))
pre = json.load(io.open(".scratch/rk74_pre.json", encoding="utf-8"))
cfg = boto3.client("lambda").get_function_configuration(FunctionName="opal-amgt-scoped-api")
print("post_CodeSha256", cfg["CodeSha256"], "equals_uploaded_sha", cfg["CodeSha256"] == up["sha256_b64"], "moved_from_pre", cfg["CodeSha256"] != pre["CodeSha256"])
print("post_LastModified", cfg["LastModified"], "Timeout", cfg["Timeout"], "MemorySize", cfg["MemorySize"], "Layers", len(cfg.get("Layers", [])), "EnvKeys", sorted((cfg.get("Environment") or {}).get("Variables", {}).keys()), "EnvKeys_equal_pre", sorted((cfg.get("Environment") or {}).get("Variables", {}).keys()) == pre["EnvKeys"])
ho = boto3.client("s3").head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
print("artifact_VersionId_now", ho.get("VersionId"), "equals_uploaded", ho.get("VersionId") == up["version_id"], "pre_act_VersionId", pre["ArtifactVersionId"])
r = subprocess.run(["terraform", "-chdir=infra/aws/terraform/harvest", "plan", "-input=false", "-lock=false", "-no-color", "-target=module.scoped_amgt_api.aws_lambda_function.this"], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=110)
out = r.stdout + r.stderr
print("replan_rc", r.returncode, re.findall(r"No changes\. Your infrastructure matches the configuration\.|Plan: \d+ to add, \d+ to change, \d+ to destroy\.", out))
'</invocation><expect>equals_uploaded_sha True and moved_from_pre True -- the deployed CodeSha256 is exactly the artifact this order built and uploaded, and it differs from AC4's pre-act value; Timeout 29, MemorySize 512, Layers 1 and EnvKeys_equal_pre True (nothing but the code moved); artifact_VersionId_now equals_uploaded True with the pre_act_VersionId printed beside it (the rollback target stays readable); replan_rc 0 with "No changes. Your infrastructure matches the configuration." -- the 0-diff targeted replan</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-74"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, hashlib, io, json
from lib.research.api import scoped_amgt
pre = json.load(io.open(".scratch/rk74_pre.json", encoding="utf-8"))
lam = boto3.client("lambda"); iam = boto3.client("iam")
def invoke(path, qs=None):
    ev = {"rawPath": path, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    if qs: ev["queryStringParameters"] = qs
    body = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    inner = body.get("body"); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == "{" else {}
    return body.get("statusCode"), inner
key = "BA_US_Equity"
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith("GET")]
post = {}; ident = {}
for r in routes:
    p = r.replace("{movement}", "trending").replace("{subject}", "chatter").replace("{security_key}", key)
    st, inner = invoke(p, {"tickers": "BA US"} if "timeseries" in p else None)
    post[r] = st
    if isinstance(inner.get("identity"), dict): ident[r] = inner["identity"]
lost = [r for r in routes if pre["census"].get(r) == 200 and post[r] != 200]
gained = [r for r in routes if pre["census"].get(r) != 200 and post[r] == 200]
print("post_census", len(post), "of 13 GET routes", "unchanged_status", sum(1 for r in routes if pre["census"].get(r) == post[r]), "of 13", "LOST", lost, "GAINED", gained)
same = [r for r in pre["identity"] if r in ident and {k: v for k, v in ident[r].items() if k != "crosswalk_source"} == pre["identity"][r]]
order_ok = [r for r in ident if list(ident[r])[3:4] == ["crosswalk_source"]]
src_ok = [r for r in ident if ident[r].get("crosswalk_source") == pre["CrosswalkNewest"]]
print("identity_blocks_equal_pre_minus_new_key", len(same), "of", len(pre["identity"]), "| post_blocks", len(ident), "| crosswalk_source_at_index_3", len(order_ok), "of", len(ident), "| crosswalk_source_equals_newest_pool_key", len(src_ok), "of", len(ident), pre["CrosswalkNewest"], "| vintages", sorted({v.get("crosswalk_vintage") for v in ident.values()}, key=str))
role = pre["Role"]
names = sorted(iam.list_role_policies(RoleName=role)["PolicyNames"])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)["PolicyDocument"] for n in names}
sha = hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest()
print("role_policy_sha_unchanged", sha == pre["PolicySha256"], "inline_policies", len(names), "of", pre["InlinePolicies"])
'</invocation><expect>post_census 13 of 13 with unchanged_status 13 of 13, LOST [] and GAINED [] (never-widen: no route's statusCode moved; bodies are NOT compared, because the rk-48 direct act rewrites management/v1 objects these routes read); identity_blocks_equal_pre_minus_new_key M of M with post_blocks M (every identity block the security routes served before the act is byte-equal after it once crosswalk_source is set aside -- no existing identity field moved); crosswalk_source_at_index_3 M of M and crosswalk_source_equals_newest_pool_key M of M naming the newest key AC4 printed (s3://opal-data-harvest/crosswalk/v1/2026-09-19.json at the cut), with the vintage beside it equal to that key's date (the field is on the SERVED plane, from the pool branch, and agrees with crosswalk_vintage; at AC4 it was carried by 0 of M); role_policy_sha_unchanged True with the same inline policy count -- any LOST route, any identity block unequal, any block without the field or naming another object, or a moved policy sha is the ROLLBACK BRANCH of section 4</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1-AC4 run BEFORE the deploy (AC4 is the pre-act read and baseline, immediately before step 1 of the
procedure); AC5 and AC6 run AFTER step 6 against the LIVE deployed plane, never a local import. The 13-route census
and the identity blocks are DIRECT `lambda.invoke` calls, exactly as every prior redeploy of this function was
censused.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~74/AMGT_RESAPP.TO-AMGT-rk-74.served-crosswalk-vintage-field.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>` (the closed ledger entry and its sentinel travel in this commit). Report
once, naming the pre-act `CodeSha256` and artifact `VersionId` (AC4), the post-act `CodeSha256` (AC5), the served
`crosswalk_source` value (AC6), and the two halves' sha256 (AC1), so the next adapter redeploy's pair can be read
against a known live state.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>18</round>
<slot>~74</slot>
<fabric>site-z</fabric>
