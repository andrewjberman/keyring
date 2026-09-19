# AMGT_RESAPP task order -- `AMGT-rk-61` -- `handler()` slash-indifferent: the `/security/{key}/{leaf}` arm resolves ONE key whether the slash in `security_key` arrives encoded or literal, the question of what the gateway forwards stops mattering, and `opal-amgt-scoped-api` is redeployed (carrying `AMGT-rk-53`'s adapter bytes) under the chain-T never-widen pair with a rollback read from THIS act's pre-act hash

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-61</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~61</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- (comp-schedule 2026-09-18 ~15:55Z: scanned 5 of 5 carriers, C1=23 C2=6 C3=12 C4=21 C5=334,
  25 gates armed. C2 is the deploy ledger: 6 open entries at the cut; this order OPENS a seventh with
  .tools/deploy_ledger.py BEFORE its first live write (the artifact upload) and CLOSES it on the post-act served
  read. It arms no cron, alarm, monitor or cadence; the daily chatter schedule (chatter-axis-schedule.tf:172-184)
  is neither read nor written; the apply is TARGETED to module.scoped_amgt_api.aws_lambda_function.this and no
  other resource in the harvest root.)
comp-iam: RUN -- (comp-iam cross-reference 2026-09-18 ~15:55Z: 214 IAM roles parsed, 190 services scanned, 1131
  operations, 328 permission gaps across 31 services; opal-amgt-scoped-api is listed as UNRESOLVED-RESOURCE -- the
  lens cannot resolve one of the adapter's S3 resources from code, a lens limit this order neither opens nor
  closes. This order changes NO role, policy, grant, environment variable, layer, timeout or memory: the function's
  code moves under the existing opal-amgt-scoped-api-role through the yang-lambda module's artifact read
  (scoped-amgt-api.tf:228-259), and AC4/AC6 assert the role's inline policy documents hash IDENTICAL before and
  after the act -- 1 role, N inline policies, sha256 over their sorted JSON.)
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~61`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU ARE ONE OF SIX ADAPTER CELLS SPAWNED ONE AT A
TIME: `lib/research/api/scoped_amgt.py` has ONE writer at any moment, and this order is cut from HEAD AFTER
`AMGT-rk-53` drains, so your worktree carries rk-53's `generation_fields()`/`_ranking_reason()` bytes and your
redeploy is what puts them on the served plane (rk-53 deploys nothing itself).** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~61;`. **NEVER RUN AN INSTALL** (`terraform init` in the harvest root,
which downloads pinned providers into the gitignored `.terraform/`, is a precondition, not an install into the tree).

## 1. THE CELL, inlined in full -- `AMGT-rk-61` (R14-T7; row `AMGT_RESAPP-Z-W27-S10`; s.3.4; FWD-13; co-sign YES)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T7 `:147`):** *"W27-S10 (s.3.4):
`handler()` slash-indifferent"* -- serves FWD-13; co-sign yes. The ruling, s.3.4 (`:87-90`), verbatim: *"Slash-safe
routing (W27-S10, OPEN, ARMED). RULED: remove the question rather than answer it. Five instruments are closed on
whether the gateway forwards `%2F` encoded; the sixth -- an authenticated edge capture -- is blocked by MFA. So
`handler()` is made INDIFFERENT to an encoded versus a literal slash in `security_key`, and the question stops
mattering. It moves served output: never-widen pair. Cell R14-T7."* The co-sign discipline (`:158-160`): *"every cell
marked `yes` moves served output and gets a never-widen pair naming its blast radius, each writer COUNTED, and a
rollback read from the LIVE pre-act hash of THAT act. Each deploy opens its change-management entry BEFORE the first
live act and is committed, not staged."*

**The row this cell closes, `AMGT_RESAPP-Z-W27-S10` (`INVESTIGATION_v1.md:8530-8551`, OBSERVATION, ARMED, disarm
owner `1.0.0_SA_CTO~Z / 2.0.0_SA_COO~Z`), verbatim in its two binding fields.** `spec_asserts` (`:8549`):
*"AMGT-rk-23 (task order text): 'Print pack 500s on the two slash-bearing keys (BP/_LN_Equity, NG/_LN_Equity)
because the renderer writes the raw security key into a local file path' and AC1's expect element: 'served_ok equals
keyed_count ... Both slash keys now 200. failures empty.'"* `world_is` (`:8550`): *"Both BEFORE and AFTER this act's
live deploy, both slash keys read 404 with the ROUTER's own refusal reason, never a 500, and never reach
render_pack.py or _read_drafting_document at all -- the request is refused by handler()'s positional segment-count
match before any leaf branch runs. ... AC1 is graded FAIL on its own literal terms (served_ok 31 of 33,
failures={'BP/_LN_Equity': 404, 'NG/_LN_Equity': 404}, unchanged before/after). Fixing the router (e.g. joining
rest[1:-1] back into one key token for the /security/ arm, or requiring percent-encoding end-to-end so a raw `/`
never reaches path-splitting) is OUT OF SCOPE for this order's <paths> ..."* The measurement (`:8542-8544`) was
taken by DIRECT `lambda.invoke` with a literal slash on `rawPath`.

**The outcome it serves, PRD v0.13 @1699960261:** FWD-13 (`:384-388`, *"Everything on one page is about the same
company ... The numbers, the recent commentary, the comparison list and the social posts on a page are all about the
same company"*) and `C-IDENTITY-RESOLVED` (`:954-958`): a slash-bearing key that routes to a refusal on every leaf is
a page whose panels are about NO company; the route boundary (`C-ONE-IDENTITY`, `resolve_identity()` `:1712-1746`:
ONE resolution per request, carried unchanged) must receive the same string whichever way the slash arrived.

**THE MEASURED STATE, at HEAD (`scoped_amgt.py` @e2d89be7da, 3474 lines; cite these lines):**
- `_path()` `:3228-3234` reads `rawPath` first, then `path`, then `requestContext.http.path`. `handler()` `:3259-3398`:
  `rest = [segment for segment in path[len(ROUTE_PREFIX) :].split("/") if segment]` (`:3280`); the per-security arm
  `if rest[:1] == ["security"] and len(rest) == 3:` (`:3315`) with the boundary comment `:3316-3321` (*"the portal
  sends `encodeURIComponent(key)`, so a Bloomberg form arrives as `BABA%20US` on `rawPath`"*), `requested =
  unquote(rest[1])` (`:3322`), `identity = resolve_identity(requested)` (`:3323`), `leaf = rest[2]` (`:3324`), eight
  leaves `overlay|thesis|peers|coverage|print|ledger|versions|compare` (`:3325-3366`); the final refusal
  `raise AdapterError(404, "no /api/scoped/amgt route for {0} {1}")` (`:3396`). A literal slash yields four segments
  and falls to `:3396` -- the row's measurement.
- `scoped_amgt_route_table()` `:3444-3474` -- SIXTEEN routes, the source of truth `test_scoped_amgt_mount.py` diffs
  against `infra/aws/terraform/harvest/scoped-amgt-api.tf:286-308` in both directions; the count check `:315-322`.
  **The gateway's route keys carry a SINGLE-SEGMENT `{security_key}` and there is NO `{proxy+}` route**, so through
  the gateway a literal slash never reaches the Lambda at all (the gateway's own 404, before `handler()`), while the
  `%2F` form matches one segment and arrives on `rawPath` still encoded (payload format 2.0, `:324-331`) -- which is
  why the analysis measured *"all 13 read routes answer"* with *"keys sent in the page's own `%2F`-encoded shape"*
  (`:37`, `:39`). The route table and the gateway route set are NOT changed by this order (a `{proxy+}` route would
  change route precedence and the authorizer surface -- a wider blast radius no half has signed).
- The page encodes: `portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx:261` `encodeURIComponent(comparableKey)`.
- The slash-bearing keys are MEASURED crosswalk records: `BP/_LN_Equity` (`bloomberg` `BP/ LN`) and `NG/_LN_Equity`
  (`NG/ LN`), in the committed dry-run copy the route tests read (`test_route_boundary_identity.py:30-35`, `:61-67`).
- `AMGT-rk-53`'s adapter regions -- `generation_fields()` (`:404-417` at HEAD before rk-53) and `_ranking_reason()`
  (`:474-500`) -- are DISJOINT from `handler()`'s `/security` arm; your worktree carries them and your artifact ships
  them. Confirm before you touch the file: `git log --oneline -3 -- lib/research/api/scoped_amgt.py` shows rk-53's
  commit at or below the tip; if it does not, STOP with a row (the spawn is out of sequence).
- The deploy mechanism: `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` (`:1-11`: the artifact at
  `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` is read by
  `module.scoped_amgt_api.data.aws_s3_object.artifact` at evaluation time; `:97-98` bucket and key; `:109`
  `--build-only`; `:670` prints `VersionId` after the upload), then a TARGETED `terraform apply` on
  `module.scoped_amgt_api.aws_lambda_function.this` (`scoped-amgt-api.tf:228-259`; the round-13 precedent
  `org/critical_paths/change_management/20260918T0001Z_amgt-rk24-adapter-thesis-no-cik-reason-20260917_deploy_completion.md:15`:
  build-and-upload, targeted plan `0 to add, 1 to change, 0 to destroy`, `HALT_ACK=1 safe-apply.sh -target`,
  post-act `CodeSha256` equal to the uploaded sha, `13 of 13 GET routes -> 200, LOST=[] GAINED=[]`, 0-diff replan).
- The harvest root's plan precondition (row `AMGT_RESAPP-Z-W34-S1`, cell `AMGT-rk-59`): a fresh worktree has no
  `.build/chatter-axis-producer.zip` and `chatter-axis-schedule.tf:124` refuses to evaluate without it UNLESS rk-59's
  `fileexists(...)` expression has landed at HEAD. Section 3's DEPLOY step 4 covers both branches.

**RULED, what you build:**
1. **The arm** (`:3315-3324`): `if rest[:1] == ["security"] and len(rest) >= 3:`; `leaf = rest[-1]`;
   `requested = unquote("/".join(rest[1:-1]))`. One segment (`BP%2F_LN_Equity`) joins to itself and unquotes to
   `BP/_LN_Equity`; two segments (`BP`, `_LN_Equity`) join to the same string. Every leaf reads `leaf` and `requested`
   exactly as today; `resolve_identity()` is still called ONCE, on the joined string. The docstring `:3260-3274` gains
   one sentence stating that the key may span segments and the leaf is always the LAST segment. `scoped_amgt_route_table()`
   is untouched. Nothing else in `handler()` moves; an unknown leaf, a missing leaf and a bare `/security/<key>` still
   fall to the `:3396` refusal.
2. **The test**, `lib/research/api/tests/test_slash_safe_security_route.py`, offline by construction (the pattern of
   `test_route_boundary_identity.py`): (a) with `scoped_amgt.resolve_identity` monkeypatched to RECORD its argument
   and raise `scoped_amgt.AdapterError(299, "captured")`, `handler()` is invoked with a real event
   (`rawPath`, `requestContext.http.method GET`, header `x-firm-id: bd`) for BOTH forms of BOTH slash keys on ALL
   EIGHT leaves -- 32 of 32 return `statusCode 299` with `reason "captured"` and the recorded argument equal to the
   canonical key (`BP/_LN_Equity` / `NG/_LN_Equity`); (b) the same for the three validation names in canonical form
   (`CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` -- the strings the crosswalk convention assigns; resolution is
   NOT asserted, only that the boundary receives them unchanged) -- 24 of 24; (c) with `resolve_identity` patched to
   return a stub block (`{"security_key": None, "requested": <arg>, "status": "UNRESOLVED"}`), the three NEGATIVES
   `/security/BP/_LN_Equity` (leaf `_LN_Equity` is unknown), `/security/BP` and `/security/BP/_LN_Equity/nosuchleaf`
   return `statusCode 404` with a reason starting `no /api/scoped/amgt route for` -- 3 of 3; (d) the route table still
   has 16 entries and `test_scoped_amgt_mount.py` passes unchanged. Every arm prints its denominator.
3. **The deploy**, per section 3's DEPLOY block, under the pair, ledgered, with the rollback read from THIS act's
   pre-act values (AC4).

**Blast radius, for the halves to name (each writer counted -- ONE writer of the artifact key and ONE of the
function: this order):** (i) the `/security/{key}/{leaf}` router arm for every key in the 33-name population
(behaviour unchanged for keys without a slash; the two slash keys stop refusing on DIRECT invocation); (ii) the two
`lead-panel/rankings` responses gain the `empty_reason` field -- `AMGT-rk-53`'s adapter bytes riding this artifact;
(iii) `CodeSha256`, `CodeSize` and `LastModified` of `opal-amgt-scoped-api`. NOT moved: the role and its policies,
environment, layers, timeout 29, memory 512, the route set, the gateway, any other function, any pool object, any
table. **Rollback (the COO half's `AMGT-rk-61` section states it; this is its shape):** `aws s3api copy-object` of the
PRE-ACT artifact `VersionId` (AC4) back onto the key, then the same targeted `safe-apply`, then `CodeSha256` read
equal to AC4's pre-act value and the 13-route census equal to AC4's baseline.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** the router change is proven on a
DRY RUN -- in-process `handler()` invocations on your worktree's bytes over the two slash keys, the three validation
names and three planted negatives (AC2), none of which runs a producer or writes anywhere. The served plane is then
checked, not fleet-run: 13 GET routes on ONE keyed name (`BA_US_Equity`, the round-13 sample) plus the two slash keys
on three leaves (thesis, overlay, peers -- `print` is excluded from the live census for its render time; it is covered
in-process), before and after -- 2 of 33 slash-bearing names, never a re-run of anything. `C-PRODUCTION-HOME`
(`:1643-1650`): the artifact is built from the repository's own sources; no worker folder is read by production code.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.3.4 (`:87-90`), s.4 row R14-T7
(`:147`), the co-sign discipline (`:158-160`) and s.6 (`:207`); the row `AMGT_RESAPP-Z-W27-S10`
(`surprise-channel/investigations/INVESTIGATION_v1.md:8530-8551`, filed 2026-09-17T23:48Z by `0.9.0_WK_AMGT_RESAPP~27`).
PRD v0.13 @1699960261: FWD-13 (`:384-388`), `C-IDENTITY-RESOLVED` (`:954-958`), `C-PRODUCTION-HOME` (`:1643-1650`),
`C-VALIDATION-NAMES` (`:1652-1658`).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES AND THE SINGLE-WRITER QUEUE (`2.0.0_SA_COO~Z`, at the cut):** this
order is CO-SIGNED. The pair for chain T is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_T_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_T_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-61`, and that section names this order's blast
radius and the per-key rollback. Read both BEFORE your first live act and paste both files' sha256 into your report
(AC1). Either file absent or its `AMGT-rk-61` section missing: run ONLY the read-only criteria (AC1, AC2, AC3), file a
BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half. ADAPTER SINGLE-WRITER QUEUE: six
adapter cells are spawned ONE AT A TIME; before `build-and-upload-scoped-amgt.sh` you run AC3's census
(`git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface
infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`) and it MUST
print nothing; anything printed means another adapter act landed on `SITEZ` since your spawn -- STOP with a BLOCKING
row (disarm_owner `2.0.0_SA_COO~Z`) and deploy nothing. The rollback target is the pre-act `CodeSha256` and artifact
`VersionId` YOU read immediately before the apply (AC4), never a prior act's. EVERY AMGT_RESAPP byte lands in
`opal-data-harvest` (Andrew-direct ~21:45Z: *"opal-data-assets is solely for client data ... the whole pipeline will
exist within opal-data-harvest"*): this order writes to NO pool bucket at all; its one S3 write is the Lambda artifact
key in `opal-313476888478-lambda-artifacts`, the estate's artifact bucket, exactly as every prior redeploy of this
function.

**ISSUER RULE -- THE ROLLBACK MECHANISM (`2.0.0_SA_COO~Z`, on `1.0.0_SA_CTO~Z` msg 23830):** the Terraform module
(`infra/aws/terraform/modules/yang-lambda/main.tf:17-20`, `:38`) declares `data "aws_s3_object" "artifact"` with bucket and key
only and ALWAYS resolves the CURRENT version, so a rollback NEVER edits the module and never names a VersionId to Terraform.
Rollback = restore the pre-act bytes as the current version -- `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts
--key research/opal-amgt-scoped-api.zip --copy-source "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<pre-act VersionId>"`
(bucket versioning MEASURED `Enabled` by the issuer 2026-09-18 ~22:4xZ; RE-MEASURE it with `get-bucket-versioning` into the
entry before the build and STOP if it reads anything else) -- then the SAME targeted `safe-apply`, and
`get-function-configuration` must print the pre-act `CodeSha256` again. Record all of it before acting; exercise none of it
unless rolling back. ADAPTER SINGLE-WRITER QUEUE: this order is cut from HEAD after `AMGT-rk-53` drains, so its worktree carries
`rk-53`'s adapter bytes and this redeploy carries them to the served plane (the chain L half names that); the pre-build
`git log <merge-base>..SITEZ -- lib/research/api ...` MUST print nothing.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_slash_safe_security_route.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~61/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-61.router-slash-indifferent.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_T_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `infra/aws/terraform/harvest/scoped-amgt-api.tf`,
  `chatter-axis-schedule.tf`, `build-and-upload-scoped-amgt.sh`, `lambda_src/build_zip.py`, `.tools/safe-apply.sh`,
  `.tools/deploy_ledger.py`, the round-13 change-management entries and `lib/research/api/tests/*.py` freely); this
  block governs WRITES. The two halves are granted so the pair can be read from your worktree; you never edit them.
  Scratch is `<your worktree>/.scratch/` only; the gitignored `.build/` and `.terraform/` under the harvest root are
  build outputs, never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~61 <0.9.0_WK_AMGT_RESAPP~61@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Commit the
  adapter edit and the test BEFORE the deploy so the artifact corresponds to a commit; name that hash in the ledger
  entry's title.
- **DEPLOY -- the procedure, in this order, each step's evidence recorded verbatim in the ledger entry:**
  0. AC1, AC2, AC3, AC4 pass (read-only). AC1 failing = STOP. AC3 printing anything = STOP.
  1. `python .tools/deploy_ledger.py open --slug amgt-rk61-router-slash-indifferent --title "<AMGT-rk-61: handler slash-indifferent + rk-53 adapter bytes; commit <hash>; co-signed chain-T pair COO <sha256> / CTO <sha256>>" --author 0.9.0_WK_AMGT_RESAPP~61 --leg "L1|verify|module.scoped_amgt_api.aws_lambda_function.this|targeted apply 0 destroy + 0-diff replan + CodeSha256 == uploaded sha + 13-route census LOST=[] GAINED=[] + slash pairs 6 of 6 equal + role policy sha unchanged"`
     -- BEFORE the first live write; the sentinel lands in `org/critical_paths/.open_deploys/`.
  2. `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` -- record the local artifact sha256 (base64)
     it prints and the `VersionId` line (`:670`) into `.scratch/rk61_upload.json` as `{"sha256_b64": ..., "version_id": ...}`.
  3. `terraform -chdir=infra/aws/terraform/harvest init -input=false` once.
  4. Plan precondition: if `chatter-axis-schedule.tf` carries `fileexists(local.chatter_axis_zip)` at `:124`
     (`AMGT-rk-59` landed) nothing is needed; otherwise run `python infra/aws/terraform/harvest/lambda_src/build_zip.py`
     (writes only the gitignored `.build/` zip; the apply is targeted, so that zip is never applied). NEVER a
     placeholder zip.
  5. `terraform -chdir=infra/aws/terraform/harvest plan -input=false -lock=false -no-color -target=module.scoped_amgt_api.aws_lambda_function.this`
     -- must read `Plan: 0 to add, 1 to change, 0 to destroy.` naming ONLY that resource with `source_code_hash`
     (and the attributes the provider derives from it) changing. Any other resource, any destroy, any replace: STOP,
     row, ledger left OPEN with the reason, no apply.
  6. `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -auto-approve -lock-timeout=60s -target=module.scoped_amgt_api.aws_lambda_function.this`
     -- must read `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` Never bare `terraform apply`, never
     `aws lambda update-function-code`.
  7. AC5, AC6. Then `python .tools/deploy_ledger.py close-leg --slug amgt-rk61-router-slash-indifferent --leg-id L1 --proof "<AC5 and AC6 output verbatim>"`
     and `python .tools/deploy_ledger.py close --slug amgt-rk61-router-slash-indifferent`; commit the entry (it is
     COMMITTED, never left staged -- the round-13 COO half's own item 7).

## 4. BOUNDS

**THIS ORDER MOVES SERVED OUTPUT.** It does so ONLY under the pair (section 2), ONLY after AC3's census prints
nothing, ONLY through steps 1-7 above, and ONLY on `module.scoped_amgt_api.aws_lambda_function.this`. **THE
ROLLBACK BRANCH:** if AC5 reads a `CodeSha256` other than the uploaded sha, or AC6 LOSES any of the 13 routes, or any
slash pair is unequal, or the role policy hash moved -- execute the rollback the COO half's `AMGT-rk-61` section
names (copy the AC4 `VersionId` back onto the artifact key, the same targeted `safe-apply`, `CodeSha256` read equal to
AC4's pre-act value, the census re-run equal to AC4's baseline), file a BLOCKING row, close the ledger leg with the
rollback proof. NEVER leave the deploy half-landed (CLAUDE.md NEVER-2).
PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through `comp-secrets` only. **No vendor call** (none is named; every live read is a
`lambda.invoke`, `get_function_configuration`, `head_object`, `get_role_policy` or a Terraform plan against Opal's own
estate). No non-ASCII in anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by adding a `{proxy+}`
gateway route and never by editing the route table.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the 13-route statusCodes and
the slash keys' pre-act 404s are re-measured at spawn by AC4; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W61-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import hashlib, io, os, re
d = 'org/missions/D5/AMGT/AMGT_RESAPP/ledger/'
for half in ('NEVER_WIDEN_ROUND14_CHAIN_T_COO_HALVES.md', 'NEVER_WIDEN_ROUND14_CHAIN_T_CTO_HALVES.md'):
    p = d + half
    if not os.path.exists(p):
        print(half, 'ABSENT'); continue
    b = io.open(p, 'rb').read()
    t = b.decode('utf-8', 'replace')
    heads = [l for l in t.splitlines() if l.startswith('#') and 'AMGT-rk-61' in l]
    print(half, 'sha256', hashlib.sha256(b).hexdigest(), 'rk61_section_headings', len(heads), 'of 1', 'mentions_rollback', len(re.findall(r'(?i)rollback', t)), 'mentions_VersionId_or_CodeSha256', len(re.findall(r'VersionId|CodeSha256', t)))
"</invocation><expect>both halves present, each printing a 64-hex sha256, rk61_section_headings 1 of 1, mentions_rollback at least 1 and mentions_VersionId_or_CodeSha256 at least 1 -- the pair is on file and its AMGT-rk-61 sections name a rollback read from this act's own pre-act values; an ABSENT half or 0 of 1 headings REFUSES this criterion and STOPS the order after AC2 and AC3 (read-only)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests -q 2>&1 | tail -15</invocation><expect>ISSUER REPAIR (2.0.0_SA_COO~Z, 2026-09-19 ~09:5xZ, row AMGT_RESAPP-Z-W61-S1): a failure that REPRODUCES on SITEZ HEAD bytes (measured by the issuer at 198dd585b7: test_generation_and_pool_routes.py::test_13_management_is_M1_with_the_pool_average_at_the_same_as_of and ::test_13b_the_ceo_profile_reading_separates_the_two_absences, both AssertionError 'NOT_SEARCHED' == 'NOT_CONFIRMED_NOTHING_FOUND', 2 failed 159 passed) and whose file this cell's diff does not touch is PRE-EXISTING DRIFT, not this cell's defect: record the final line verbatim, print the census 'pre_existing_failures K of F (reproduced on SITEZ HEAD <hash>, files disjoint from the diff)', and grade PASS when F - K = 0 and every other arm below holds; the two tests ride W61-S1 to the slug. Otherwise as cut: the battery passes (a final line "N passed", 0 failed) and it carries the NEW file test_slash_safe_security_route.py whose arms print their denominators: 32 of 32 in-process handler() invocations (BP/_LN_Equity and NG/_LN_Equity, encoded %2F and literal slash, all eight leaves) reach the patched resolve_identity with the canonical key and return statusCode 299 reason "captured"; 24 of 24 for CAT_US_Equity, CSL_AU_Equity and 6861_JP_Equity unchanged at the boundary; 3 of 3 planted negatives (/security/BP/_LN_Equity, /security/BP, /security/BP/_LN_Equity/nosuchleaf) return 404 with a reason starting "no /api/scoped/amgt route for"; and test_scoped_amgt_mount.py passes UNCHANGED (the route table still equals scoped-amgt-api.tf's 16 keys) -- at HEAD the literal-slash half of the 32 would return 404</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && echo "base $(git merge-base HEAD SITEZ)" && echo "adapter_commits_on_SITEZ_since_base: $(git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh | wc -l) of 0 expected" && git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh && echo "positive_control_last_adapter_commit: $(git log --oneline -1 -- lib/research/api/scoped_amgt.py)"</invocation><expect>adapter_commits_on_SITEZ_since_base: 0 of 0 expected and the log itself prints nothing (no adapter act landed on SITEZ since this worktree's base -- the single-writer queue holds), while positive_control_last_adapter_commit prints one line (the log instrument works and the empty read is a true zero); ANY listed commit is a STOP with a BLOCKING row and no deploy</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, hashlib, io, json
from lib.research.api import scoped_amgt
lam = boto3.client('lambda'); s3 = boto3.client('s3'); iam = boto3.client('iam')
cfg = lam.get_function_configuration(FunctionName='opal-amgt-scoped-api')
pre = {'CodeSha256': cfg['CodeSha256'], 'LastModified': cfg['LastModified'], 'CodeSize': cfg['CodeSize'], 'Timeout': cfg['Timeout'], 'MemorySize': cfg['MemorySize'], 'Layers': len(cfg.get('Layers', [])), 'EnvKeys': sorted((cfg.get('Environment') or {}).get('Variables', {}).keys())}
ho = s3.head_object(Bucket='opal-313476888478-lambda-artifacts', Key='research/opal-amgt-scoped-api.zip')
pre['ArtifactVersionId'] = ho.get('VersionId'); pre['ArtifactETag'] = ho.get('ETag')
role = cfg['Role'].rsplit('/', 1)[-1]
names = sorted(iam.list_role_policies(RoleName=role)['PolicyNames'])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)['PolicyDocument'] for n in names}
pre['Role'] = role; pre['InlinePolicies'] = len(names); pre['PolicySha256'] = hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest()
def invoke(path, qs=None):
    ev = {'rawPath': path, 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}
    if qs: ev['queryStringParameters'] = qs
    body = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps(ev).encode())['Payload'].read())
    inner = body.get('body'); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == '{' else {}
    return body.get('statusCode'), (inner.get('reason') or '')[:60]
key = 'BA_US_Equity'
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith('GET')]
census = {}
for r in routes:
    p = r.replace('{movement}', 'trending').replace('{subject}', 'chatter').replace('{security_key}', key)
    census[r] = invoke(p, {'tickers': 'BA US'} if 'timeseries' in p else None)[0]
print('pre_census', len(census), 'of 13 GET routes', json.dumps(census))
slash = {}
for k in ('BP/_LN_Equity', 'NG/_LN_Equity'):
    for leaf in ('thesis', 'overlay', 'peers'):
        slash[k + '|' + leaf] = {'encoded': invoke('/api/scoped/amgt/security/' + k.replace('/', '%2F') + '/' + leaf), 'literal': invoke('/api/scoped/amgt/security/' + k + '/' + leaf)}
lit404 = sum(1 for v in slash.values() if v['literal'][0] == 404 and v['literal'][1].startswith('no /api/scoped/amgt route for'))
print('pre_slash_literal_router_404', lit404, 'of 6', json.dumps(slash))
pre['census'] = census; pre['slash'] = slash
io.open('.scratch/rk61_pre.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(pre, indent=1, default=str))
print('PRE-ACT', json.dumps({k: pre[k] for k in ('CodeSha256', 'LastModified', 'CodeSize', 'ArtifactVersionId', 'Role', 'InlinePolicies', 'PolicySha256', 'Timeout', 'MemorySize', 'Layers', 'EnvKeys')}, default=str))
"</invocation><expect>PRE-ACT prints the LIVE CodeSha256, LastModified, CodeSize, the artifact's current VersionId (the rollback target of THIS act), the role name with its inline policy count and PolicySha256, Timeout 29, MemorySize 512, Layers 1 and the two env keys; pre_census 13 of 13 GET routes with each route's statusCode recorded (all 200 at the cut; re-measure); pre_slash_literal_router_404 6 of 6 -- the defect baseline: every literal-slash direct invoke on both keys and three leaves is refused by the router's own reason, while the encoded form's statusCodes are recorded beside them; all of it written to .scratch/rk61_pre.json for AC6</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, io, json, re, subprocess
up = json.load(io.open('.scratch/rk61_upload.json', encoding='utf-8'))
pre = json.load(io.open('.scratch/rk61_pre.json', encoding='utf-8'))
cfg = boto3.client('lambda').get_function_configuration(FunctionName='opal-amgt-scoped-api')
print('post_CodeSha256', cfg['CodeSha256'], 'equals_uploaded_sha', cfg['CodeSha256'] == up['sha256_b64'], 'moved_from_pre', cfg['CodeSha256'] != pre['CodeSha256'])
print('post_LastModified', cfg['LastModified'], 'Timeout', cfg['Timeout'], 'MemorySize', cfg['MemorySize'], 'Layers', len(cfg.get('Layers', [])), 'EnvKeys', sorted((cfg.get('Environment') or {}).get('Variables', {}).keys()))
ho = boto3.client('s3').head_object(Bucket='opal-313476888478-lambda-artifacts', Key='research/opal-amgt-scoped-api.zip')
print('artifact_VersionId_now', ho.get('VersionId'), 'equals_uploaded', ho.get('VersionId') == up['version_id'], 'pre_act_VersionId', pre['ArtifactVersionId'])
r = subprocess.run(['terraform', '-chdir=infra/aws/terraform/harvest', 'plan', '-input=false', '-lock=false', '-no-color', '-target=module.scoped_amgt_api.aws_lambda_function.this'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
out = r.stdout + r.stderr
print('replan_rc', r.returncode, re.findall(r'No changes\. Your infrastructure matches the configuration\.|Plan: \d+ to add, \d+ to change, \d+ to destroy\.', out))
"</invocation><expect>equals_uploaded_sha True and moved_from_pre True -- the deployed CodeSha256 is exactly the artifact this order built and uploaded, and it differs from AC4's pre-act value; Timeout 29, MemorySize 512, Layers 1 and the same two EnvKeys as AC4 (nothing but the code moved); artifact_VersionId_now equals_uploaded True with the pre_act_VersionId printed beside it (the rollback target stays readable); replan_rc 0 with "No changes. Your infrastructure matches the configuration." -- the 0-diff targeted replan</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-61"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, hashlib, io, json
from lib.research.api import scoped_amgt
pre = json.load(io.open('.scratch/rk61_pre.json', encoding='utf-8'))
lam = boto3.client('lambda'); iam = boto3.client('iam')
def invoke(path, qs=None):
    ev = {'rawPath': path, 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}
    if qs: ev['queryStringParameters'] = qs
    body = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps(ev).encode())['Payload'].read())
    inner = body.get('body'); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == '{' else {}
    return body.get('statusCode'), (inner.get('reason') or '')[:60]
key = 'BA_US_Equity'
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith('GET')]
post = {}
for r in routes:
    p = r.replace('{movement}', 'trending').replace('{subject}', 'chatter').replace('{security_key}', key)
    post[r] = invoke(p, {'tickers': 'BA US'} if 'timeseries' in p else None)[0]
lost = [r for r in routes if pre['census'].get(r) == 200 and post[r] != 200]
gained = [r for r in routes if pre['census'].get(r) != 200 and post[r] == 200]
print('post_census', len(post), 'of 13 GET routes', 'unchanged_status', sum(1 for r in routes if pre['census'].get(r) == post[r]), 'of 13', 'LOST', lost, 'GAINED', gained)
pairs = {}
for k in ('BP/_LN_Equity', 'NG/_LN_Equity'):
    for leaf in ('thesis', 'overlay', 'peers'):
        e = invoke('/api/scoped/amgt/security/' + k.replace('/', '%2F') + '/' + leaf); l = invoke('/api/scoped/amgt/security/' + k + '/' + leaf)
        pairs[k + '|' + leaf] = {'encoded': e, 'literal': l, 'equal_status': e[0] == l[0], 'literal_router_refusal': l[1].startswith('no /api/scoped/amgt route for')}
print('slash_pairs_equal', sum(1 for v in pairs.values() if v['equal_status']), 'of 6', 'literal_router_refusals', sum(1 for v in pairs.values() if v['literal_router_refusal']), 'of 0 expected', json.dumps(pairs))
role = pre['Role']
names = sorted(iam.list_role_policies(RoleName=role)['PolicyNames'])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)['PolicyDocument'] for n in names}
sha = hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest()
print('role_policy_sha_unchanged', sha == pre['PolicySha256'], 'inline_policies', len(names), 'of', pre['InlinePolicies'])
rk = invoke('/api/scoped/amgt/lead-panel/rankings/breakout/chatter')
body = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath': '/api/scoped/amgt/lead-panel/rankings/breakout/chatter', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode())['Payload'].read())
inner = json.loads(body.get('body') or '{}')
print('rankings_breakout_status', rk[0], 'empty_reason_key_present', 'empty_reason' in inner, '(rk-53 adapter bytes served)')
"</invocation><expect>post_census 13 of 13 with unchanged_status 13 of 13, LOST [] and GAINED [] (never-widen: no route's statusCode moved); slash_pairs_equal 6 of 6 and literal_router_refusals 0 of 0 expected -- on the LIVE deployed plane, a literal slash and an encoded slash now yield the same statusCode on both keys and all three leaves, and the router's refusal reason is gone from the literal form (6 of 6 at AC4); role_policy_sha_unchanged True with the same inline policy count (the role did not move); rankings_breakout_status 200 with empty_reason_key_present True (AMGT-rk-53's adapter bytes reached the served plane through this artifact; at AC4 the key was absent) -- any LOST route, any unequal pair or a moved policy sha is the ROLLBACK BRANCH of section 4</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1-AC4 run BEFORE the deploy (AC4 is the pre-act read and baseline, immediately before step 1 of the
procedure); AC5 and AC6 run AFTER step 6 against the LIVE deployed plane, never a local import. The 13-route census
and the slash pairs are DIRECT `lambda.invoke` calls (the gateway's single-segment routes never forward a literal
slash, so the served-plane discriminator for the literal form is the direct invoke, exactly as the row measured it).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~61/AMGT_RESAPP.TO-AMGT-rk-61.router-slash-indifferent.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>` (the closed ledger entry and its sentinel travel in this commit). Report
once, naming the pre-act `CodeSha256` and artifact `VersionId` (AC4), the post-act `CodeSha256` (AC5), and the two
halves' sha256 (AC1), so the next adapter cell's pair can be read against a known live state.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>14</round>
<slot>~61</slot>
<fabric>site-z</fabric>
