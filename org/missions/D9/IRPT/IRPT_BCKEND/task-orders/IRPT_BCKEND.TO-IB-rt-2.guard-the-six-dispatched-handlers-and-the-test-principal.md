# TO IRPT_BCKEND.TO-IB-rt-2 -- GUARD THE SIX: the verified FirmBinding wrapper on every handler the real route file dispatches, real request handlers where a route pointed at a queue-only or capabilities-only function, the self-wrapping harness retired, and a test principal from the existing authorizer's own path or a HUMAN-GATED arm naming the operator's exact act

<to_id>IRPT_BCKEND.TO-IB-rt-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- handed by 2.0.0_SA_COO~B at 2026-09-11 ~14:3xZ after IB-rt-1 drained COMPLETE at 8abcb1563b (v1 frozen at c22f179bbf). Second order of slot ~2.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 2 | **Slug rows this cell closes:** W1-S10, W2-S7 (served-path half), W2-S9 (handler half) | **Decomp cell:** `IB-rt-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-2 (own), FWD-11 | **PRD candidate:** B3

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-2-2` on branch `wk-irpt_bckend-2-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** second in slot ~2, after IB-rt-1. IB-rtb-1 (slot ~1, last) replays what this cell guards and uses the principal this cell establishes.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B3 authorization enforcement on every route, warm-cache revocation
- **serves:** FWD-2 (own)
- **brief sections consumed:** O1 enforcement paragraph; II.3 cache/idempotency-key paragraph
- **contracts (P=produces, C=consumes):** C `ResolvedScope`; keys per II.3
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (CUSTOM authorizer pattern)
- **paths: new home:** `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** negative integration fixtures (swapped firm/advisor/account/relationship/report/PDF ids; revoked grant vs warm cache)
- **acceptance clause draft:** every negative request reveals no protected data; a cached result or artifact is reauthorized before serving; client names are never cache keys

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** GUARD THE SIX, THEN PROVE THE AUTHENTICATED PATH. The six actually-dispatched handlers (W1-S10) take the verified FirmBinding wrapper on the real route file; the harness that wrapped them itself is retired as evidence. The authenticated real-path swap arms need a principal: the CTO rules a test principal issued by the existing authorizer's own path under the existing entitlement class (no new permission, no vendor call); if the lane finds no such path exists, the arm is written HUMAN-GATED with the exact act an operator takes, never silently skipped.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- The population is the REAL route file (`docs/contracts/investor-reporting/v1/routes.json` after IB-rt-1): every route's integration target is read from the api root's Terraform, and every targeted function's entry point is wrapped by `_authz.guard()` with `FirmBinding` proven against the directory artifact -- including the three round 1 left unguarded because they were written before the route table existed: `POST /analysis` (a REAL request handler in `ycharts/generate/` that accepts the browser request half of `AnalysisRequest` (v0.10), builds the `resolved` half server-side through `_scope`'s Generate resolver -- the browser never submits it -- and enqueues the job; the queue-only entry stays for the worker), `GET /narrative/{reportId}` (`narrative/handler.py` gains the wrapper and a scope check on the report's firm), `GET /export/{exportId}` (a real export-status operation in `export/`, reading the receipt under the bound firm's prefix). `unguarded_routes()` over the real file reads `0 of N` and the census is a control on the census: one handler deliberately unregistered from the wrapper in a throwaway copy reads `1 of N`.
- Every guarded handler's refusal is the ONE envelope (`_authz`): public reason, correlation id, 0 protected bytes; `FirmBinding` takes the firm from the VERIFIED principal (the injected `X-Firm-Id` reconciled against the artifact's `firm_id_opaque`), never from a request-controlled field (W2-S9's handler half); the ownership-map projection is wired on the served path so a grant without projection is `UNPROJECTED-ID` (W2-S7's served-path half).
- The test principal: Phase 1 reads `infra/aws/lambda/portal-auth/` and the authorizer `opal-portal-authorizer` for the estate's own way to mint a JWT the validator accepts under an EXISTING entitlement class (a test user in the existing pool, a signing path the authorizer already trusts). If one exists and a worker may use it without a human, the battery mints a principal for one test firm and proves ONE authenticated request through the real path (CloudFront -> edge -> authorizer -> handler) and ONE swapped-firm refusal. If none exists, the arm is written `HUMAN-GATED` naming the exact operator act (which console, which user, which claim) and its expected reading -- never skipped silently. NO new permission, NO vendor call.
- The deploy: every function whose code changes here is rebuilt, its zip uploaded, its root applied under a ledger entry (roots: ycharts, narrative, export -- each state key its own; `-target` never), `CodeSha256` verified; every plan shows ONLY the function code/hash changes.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`_authz` with `guard()`, `FirmBinding`, `unguarded_routes()` and the refusal envelope (IB-s-3, 3cca035c66); the eleven live routes and the CloudFront path; `_scope` with the resolver, `id_projection`, `global.py` and the roster path; the round-1 replay's measurement 6 of 11 unguarded (three known: IB-s-1 directory x2, IB-s-11 performance; three new: analysis, narrative, export status).

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~12:3xZ, at IB-rt-1's first drain -- the second half of ROW W2-S16's disarm; channel row `IRPT_BCKEND-S26`):**
- **EVERY DISPATCHED HANDLER RETURNS THE v1 RESPONSE ENVELOPE.** IB-rt-1 publishes `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json` -- ONE envelope `{contract_version, operation, firm_id, data, status?}` with `data` the producer document -- and measured that the six handlers answer in three ad-hoc envelopes (0 of 11 validate). This cell, which owns and deploys the six, makes each handler's response validate against its response schema and its `data` against the document schema; the `X-Contract-Version` check is SERVED (a mismatched version refused `CONTRACT_VERSION` on the deployed function). The refusal envelope of `_authz` and the response envelope are two shapes of one family: `status` carries the `StatusEnvelope` on both.

---

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~17:3xZ, at the drain of this order's first report -- rows W2-S19..S27 read at aef37711d3; the order stays OPEN):**
- **W2-S19 GRANTED.** `<paths>` now carries `infra/aws/lambda/investor-reporting/ops/` and `infra/aws/terraform/investor-reporting/ops/`: `irpt-status` and its three routes are inside the six, and arm (a) reads `0 of N` over all eleven handler-bearing routes.
- **W2-S24 GRANTED, under the shared-surface rule (row W4-S15).** `<paths>` now carries `infra/aws/lambda/layers/irpt-common/` and `infra/aws/lambda/ci/lambda-layer-map.json`. `_authz` reaches the zips through the layer: rebuild the layer FROM THE TREE AT YOUR CUT (the union of every declared member list; the `carried_forward_members` block is removed by IB-rt-7 or by you, whichever touches the file first -- assert no duplicate member path), publish, repoint `3 of 3`, print the version you READ and the version you PUBLISHED. IB-rt-7 (slot ~1, cut at df84a8a952) is rebuilding the same layer now from a tree that predates your guard; whichever of you publishes second publishes the superset, because both build from the merged tree. The capabilities read prints `5 of 5` contracts and the `_authz` members present.
- **W2-S22 RESOLVED BY SEQUENCE.** IB-rt-4 is COMPLETE and merged (56525018f8 -> 3ed2c79443); its export apply landed and closed. From your re-cut onward `irpt-export-render` is this order's alone; the new entry module per function stands, and `export/handler.py` may now be touched where the guard needs it.
- **W2-S21 SPLIT BY OWNER.** `irpt-status` (5 of 7 declared build inputs absent) and `irpt-directory-search` (builder parity on a shared source dir) are THIS order's: register the truth in `lambda-source-map.json` -- a build input that does not exist in the tree is REMOVED from the list, never invented; two functions sharing one source dir carry two entries whose packaged lists are each derivable from the tree and whose parity check passes; every registered `artifact_sha256` equals the S3 object's `content-sha256` equals the live `CodeSha256` (`N of N` printed). `irpt-ycharts-generate` (7 of 25 absent) is IB-rt-9's and is carried to it by amendment. The CLOSED ledger entry that claims a byte-identical rebuild at a commit that lacks the inputs is a RECORD defect carried to L10 by name -- do not edit a closed entry.
- **W2-S23 IN LANE.** `_authz/errors.py` PUBLIC_REASONS gains `CONTRACT_VERSION` (it is the one envelope; the reason set is closed by design and grows by amendment, which this is). Arm (g)'s mismatched-header refusal is served with that code.
- **W2-S25 RULED.** A refusal is NEVER an instance of a response contract: it is v1's `StatusEnvelope`. Arm (g) grades SUCCESS responses against `responses/<operation>.response.schema.json` and REFUSALS against `StatusEnvelope`, both printed per operation; the v1 freeze at c22f179bbf stands and nothing in `docs/contracts/` is edited by this order.
- **W2-S27 IN LANE.** `performance/tenants.py` routes on the firm the boundary binds (the registry spelling resolved from the issued opaque id), and the `F-49F`/`F-COT`/`F-INF` spelling is retired from the adapter; the swap census covers performance after the change.
- **W3-S22 / W4-S24 ROUTED HERE.** `_authz/dispatch.py` was authored in this slot (173349a652) and collides with `export/dispatch.py` on the flat `sys.path` every export module shares (IB-rt-8's own tests cannot see its module). Rename `_authz/dispatch.py` to `_authz/authz_dispatch.py`, update every importer, and print a census of module basenames in `_authz/` against every function directory: `0` collisions. `export/dispatch.py` is not renamed.
- Arm (a)'s inherited `6 of 11` is retired by your census (`11 of 11` unguarded at the cut, row W2-S20); the battery prints the census it derives from `routes.json` + the source map + each root's `handler =`, never an inherited number.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~18:0xZ, at the drain of the wind-down branch 496a2767d2 -> 5347f30b34; for the SUCCESSOR run of this order):**
- **W2-S28 GRANTED.** `<paths>` now carries `infra/aws/lambda/investor-reporting/_contracts/`: the one importer of `_authz/dispatch.py` is `_contracts/tests/test_seam_paired.py:41`, so the rename to `_authz/authz_dispatch.py` updates that test in the same commit and leaves no shim at the old basename.
- **W1-S16 ROUTED HERE (from IB-rt-7, slot ~1):** `_authz.covers()` admits ANY advisor id for an admin principal while its docstring says "within the verified firm". No cross-firm bytes are reachable today (the firm is bound before the check), but the predicate and its docstring disagree on a security boundary: make `covers()` refuse an advisor id outside the verified firm for every principal class, add the negative to the swap census, and print it.
- **W2-S29 (two remedies, no preference in the row):** `irpt-directory-search` and `irpt-directory-refresh` share one source dir. RULED: split the packaged lists by an explicit per-function `files` list in `lambda-source-map.json` (the builder's parity check runs per function and must pass for both), not by moving code; the refresh runner's modules are not in the search zip.
- The committed battery result and the instance record the PRE-amendment numbers (`0 of 8 / 3 of 11`): they are REWRITTEN from a fresh run, never hand-edited. `directory` and `ops` declare `layers = []`, so the guarded entries' shared imports need the layer attached (or vendored) before those two zips are deployed; read the live `irpt-common` version immediately before publishing.
- Successor: read `deliverables/0.9.0_WK_IRPT_BCKEND~2/WIP_IB-rt-2_winddown.md` (496a2767d2) first. No ledger was opened by this order across two runs; nothing is half-landed.

**ISSUER CORRECTION (2.0.0_SA_COO~B, 2026-09-11 ~18:2xZ, at the drain of the wind-down branch e021ddcdfd -> 22f2238cd7; for the SUCCESSOR run):**
- **THE 'ABSENT BUILD INPUTS' PREMISE IS CONTESTED BY TWO INSTRUMENTS AND THE FACE NO LONGER ASSERTS IT.** Slot ~2 measured (W2-S21) that irpt-ycharts-generate declared 7 of 25 inputs that never existed and irpt-status 5 of 7; slot ~3 measured at a later tip (W3-S24) 26 declared, 26 resolving, 0 absent -- the 8 outside `source_dir` are flat-packaged SHARED libraries (`enforce`, `gate`, `keys`, `resolve`, `firm_registry.json`), and removing them strips the function's imports. The drain resolved irpt-status's file list in `lambda-source-map.json` as the UNION of both sides (the shared libraries slot ~3 declares plus the `entry.py` slot ~2 added), which is the non-destructive reading. RULE FOR THE SUCCESSOR: before removing ANY declared build input, resolve it the way the builder does (`source_dir` first, then the flat-packaged shared library roots), print `N of N resolve`, and remove only what resolves NOWHERE; an input that resolves outside `source_dir` is a shared library, not an absence.
- **A DEPLOY IS OWED (W3-S25), first act of the successor run of IB-rt-9, which holds the ycharts functions; this order rebuilds only the functions it deploys:** `_scope/resolve.py` gained `import ids` and the packaging followed only in the declaration -- the three functions shipping `resolve.py` are REBUILT from the tree and deployed under a ledger; `CodeSha256` equality cannot see this defect by construction, the import-closure check in the `/var/task` + `/opt/python` layout can.
- **THE LIVE PROBE STILL RUNS THE RETIRED PREDICATE** (`ycharts-session-probe`, LastModified 2026-05-22, rule ENABLED, every 6 hours): the rewrite is in the tree at 22f2238cd7, not in the world. Its redeploy rides IB-rt-9's arm (e) ledger; until then `SessionFresh=1` from that probe is not evidence of anything.

---

## ISSUER AMENDMENT -- 2026-09-11 ~22:5xZ (`2.0.0_SA_COO~B`, post-reboot re-entry). THIS BLOCK GOVERNS OVER EVERY LINE ABOVE IT.

**Authority:** Andrew-direct ~22:25Z at the `1.0.0_SA_CTO` terminal, VERBATIM AND ENTIRE: *"load up and get
/canonical-flow driving for COO~B (IRPT_BCKEND) and COO~F (IRPT_FNTEND)."* Relayed as msg 96019; recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_2225Z_RESUME_AFTER_REBOOT_DRIVE_BOTH_IRPT_LANES.md`
@4a90ec8d2f. It lifts exactly ONE thing: MSTR 95994's instruction 2, "start nothing new". **The round stays FROZEN
(Rule 27)** -- no re-cut, no PRD re-open; an off-spec finding is a surprise ROW and you keep working.

### A1. YOU ARE A COLD START. The IDENTITY section's *"the same subagent as round 1, continued with its context intact"* is FALSE and is STRUCK.
This device rebooted at ~22:0xZ. **Every worker subagent of this round is DEAD and cannot be resumed.** You carry no
prior context and must assume none. Your whole context is: THIS FACE (the newest amendment governs), and the WIP hand-off written for exactly this moment: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/WIP_IB-rt-2_winddown.md`. **READ THAT FILE BEFORE YOU READ ANYTHING ELSE IN THIS FACE'S BODY** -- it names what is done, what must not be re-done, and the traps this cell already paid for.

### A2. NEW WORKTREE -- the pair named in IDENTITY IS GONE.
- **Worktree:** `/c/tmp/wk-irpt-2-2b` on branch `wk-irpt_bckend-2-2b`, cut by the issuer from CLOUD HEAD `7d6db9bcfa`.
- The old pair (`/c/tmp/wk-irpt-2-2 on wk-irpt_bckend-2-2`) was REMOVED after its branch was verified an ancestor of the tip. Do not look for it, and
  **never spawn into an old worktree.**
- **Every path in this face is relative to the NEW worktree root**; make it absolute by prefixing `/c/tmp/wk-irpt-2-2b/`.
- First act unchanged: `git rev-parse --abbrev-ref HEAD`, then `test -d org && test -d .tools && echo TREE-OK`.

### A3. FRESH-WORKTREE TRAPS THIS ROUND HAS ALREADY PAID FOR -- none of these is yours to rediscover.
- **`.tools/terraform.exe` is gitignored and therefore ABSENT here.** Four roots read `rc 1` for want of
  `terraform init`, and **an rc is not a reading.** Resolve the binary by path; `init` each root before any plan.
- **`safe-apply.sh` has TWO identity gates.** `export OPAL_AGENT_SERIAL=...` satisfies only the commit-lane one; the
  halt gate reads `org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial`, gitignored per-session state **you must write
  yourself BEFORE any apply** (row W4-S2). Write it before you need it.
- **A rail denial ABORTS THE WHOLE BASH CALL**, so every later segment of an `&&` chain is a SILENT no-op --
  including your commit. Put a gated read in its own call, or verify the later segment's EFFECT.
- **`safe-commit.sh` force-adds gitignored files under a DIRECTORY pathspec** (it once staged a 685 MB provider
  binary). Always pass explicit FILE paths.
- **Heredoc backslashes arrive HALVED** in the Bash tool. Write scripts and commit messages with the Write tool.
- A raw `grep`/`find` over a directory is denied and routed to `comp-find`; a `cmd | grep` pipe RECEIVER is free.

### A4. THE DEPLOY PREREQUISITE IN THE WIP HAND-OFF's SECTION 5 IS **RULED**. DO NOT RE-OPEN IT AS A CHOICE.
The WIP frames it as *"attach the `irpt-common` layer to the functions that lack it, OR vendor the modules per
function"*. **Both halves rest on a premise the issuer measured FALSE at `7d6db9bcfa`, and the layer is the WRONG
CARRIER.**

**Measured, `infra/aws/lambda/ci/lambda-layer-map.json`, `layers["irpt-common"]` at HEAD:** irpt-common:5 carries
jsonschema 4.26.0 with transitive pins, the IRPT contract schemas, `bd_helpers`, and
`python/{ids.py,raw_keys.json,firm_registry.json,keys.py}`. **It does NOT carry `served.py`, `loaders.py`,
`enforce.py`, `errors.py` or `resolve.py`.** Attaching it to `directory` and `ops` would therefore NOT fix the
ImportError the WIP predicts -- it would publish a change that LOOKS like a remedy and leaves the gap standing.

**Measured, `infra/aws/lambda/ci/lambda-source-map.json` at HEAD** -- the shared modules each IRPT function already
declares as FLAT build inputs (denominator: 9 irpt-* functions of 214 declared):

```
irpt-status               enforce, errors, resolve, keys, ids     <- THE SHAPE TO COPY
irpt-ycharts-generate     enforce, errors, resolve, keys, ids
irpt-export-render        enforce, errors, resolve, ids
irpt-holdings             enforce, errors, resolve
irpt-directory-refresh    errors
irpt-directory-search     (none declared; 2 files total)
irpt-narrative            (none)
irpt-performance-adapter  (none)
```

**THE RULING: declare the shared modules as FLAT BUILD INPUTS in `lambda-source-map.json`, per function, exactly the
way `irpt-status` already does.** That is the estate's existing mechanism (BUILD LADDER rung 2 -- the estate already
has it), it is how four functions already resolve `enforce`/`resolve` today, and it needs neither a layer attachment
nor a vendor manifest. `infra/aws/lambda/layers/irpt-common/` and `lambda-layer-map.json` remain granted, but **you
are NOT to publish a layer version for this.** If you come to believe you must, that is a BLOCKING row to me, not an
act.

**AND `served.py` AND `loaders.py` ARE DECLARED BY NOBODY** -- you created them in this cell, so the gap is UNIFORM
across all six functions your entry modules touch, not confined to the two that read `layers = []`. Census the SIX,
print the denominator.

- **RESOLVE THE WAY THE BUILDER DOES, AND PRINT `N of N`.** This is the same trap slot ~3 paid for on W3-S24: a naive
  *does `source_dir/<name>` exist* check calls flat-packaged shared libraries ABSENT and invites you to delete them.
  A module is PRESENT if the builder resolves it from its home package at build time. **Remove only what resolves
  NOWHERE; add only what resolves nowhere.**
- **THE ONLY INSTRUMENT THAT CATCHES A MISSING MODULE IS AN EXTRACT-AND-IMPORT IN THE FLAT `/var/task` LAYOUT WITH
  THE REPO STRIPPED FROM `sys.path`, IN A FRESH INTERPRETER.** `CodeSha256` equality cannot see this by construction:
  a hash certifies bytes and nothing in the deploy path ever imports them. A saved-and-restored `sys.modules` is not
  isolation either -- only a new interpreter is.
- My `layers=` probe returned `?` for most rows because I probed a key name I did not confirm. **The
  layer-ATTACHMENT facts are UNMEASURED BY ME and are yours to measure from Terraform**, as the WIP did at
  `bebcab6315`. Do not quote my table for attachment.

### A5. THE `_authz/dispatch.py` RENAME IS UNBLOCKED. WIP section 6.5 is STALE.
It says *"do not start the rename until `_contracts/` is granted"*. **`_contracts/` WAS granted at `db1be7e127`**
(issuer amendment, same session). The rename's only importer is `_contracts/tests/test_seam_paired.py:41` and that
path is in lane. Do it, in one commit with its importer, leaving no shim at the old basename.

### A6. DEPLOY SEQUENCING -- YOU ARE SECOND, AND THIS IS NOT NEGOTIABLE.
Slot ~3 (IB-rt-9) owes a rebuild-and-deploy of `irpt-export-render`, `irpt-status` and `irpt-ycharts-generate` for
the `ids.py` packaging gap (row W3-S25), and that is ITS first ledgered act. **Three of those overlap your six.**
- **rt-9 deploys those three FIRST. You do NOT deploy them until I tell you its deploy has landed.** Ask me; do not
  read its branch and decide for yourself.
- Your own deploy of the guarded entries (arm (e)) re-points the Terraform `handler =` strings. Until that apply,
  the world runs the OLD handlers, which do not import `served`/`loaders` -- **so rt-9's deploy is safe ahead of
  yours, and yours is unsafe ahead of its declaration landing.** That asymmetry is the reason for the order.
- NEVER-2 stands: open the change-management ledger only with the room to CLOSE it in-session; commit the OPEN
  sentinel BEFORE the act and the CLOSE before the reads that grade it. Print
  `artifact_sha256 == S3 content-sha256 == live CodeSha256` for every function you deploy (W3-S18).

### A7. FIRST ACTS, IN ORDER (the WIP's section 4 stands, with A4 folded in).
1. Add `"irpt-status"` to `IN_LANE_FUNCTIONS` in `_authz/tests/test_guarded_entries.py` (ONE line; the census
   test's own copy of that set is already updated -- the two lists are separate).
2. Re-run `timeout 600 python -m pytest infra/aws/lambda/investor-reporting/_authz/tests/ -q` (104 passing before
   the line; expect 36 swaps after) and then `timeout 900 python
   org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.py`.
3. **Rewrite `battery_ib_rt_2.result.md` and the proof-of-spec instance FROM THAT OUTPUT.** Both currently record
   pre-amendment numbers and say so in their own text. **Do not hand-edit their numbers** -- that is a new vintage,
   not a correction.
4. Then the packaging census and declaration of A4; then the rename of A5; then, only after A6 clears, the deploy.

### A8. EVERYTHING IN THE WIP's SECTIONS 6 AND 7 STILL BINDS.
Do not re-measure the "6 of 11 unguarded" the face inherits (the real census at the cut was 11 of 11, row W2-S20).
Do not add a guard inside a wrapped handler module. Do not wire `ops`'s status loader to make an arm pass. Do not
add `expiry.py`/`refresh.py` to `irpt-directory-search`'s files. Do not re-derive the protected-string set as a flat
list. Do not assert REFUSED for the advisor swap -- the bar is that it never WIDENS. Read the `PUBLIC_REASONS` enum
before reaching for `CONTRACT_VERSION`.


## DELIVERABLE

The guarded entry points in `directory/`, `performance/`, `ycharts/generate/` (the request handler), `narrative/`, `export/` (the status operation); `_authz/tests/test_unguarded_census.py` with the control; the test-principal module `_authz/testprincipal.py` OR the `HUMAN-GATED` arm record `deliverables/0.9.0_WK_IRPT_BCKEND~2/RT2_test_principal_human_gated.md`; the ledger entries + sentinels for each root applied; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.py` and `.result.md`.

---

## BOUNDS

- **The subject is the real route file and the real entry points** (s.8 bound 12); a battery that wraps a copy proves nothing here.
- **No new IAM permission, no new user pool, no vendor call** for the principal; the existing authorizer's own path or a HUMAN-GATED arm.
- **The generate handler enqueues; it never runs the vendor chain inline**, and the queue-only worker entry keeps its consent gate.

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="RT2-AC1" cell_refs="IB-rt-2"><invocation>timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.py</invocation><expect>IBRT2-SIX-GUARDED</expect></criterion>
**`RT2-AC1` -- PASSES BY OUTPUT -- the census reads zero on the real file, the control reads one, every refusal is the envelope, the principal is real or the gate is named.**
**(a) ZERO OF N, AND THE CONTROL.** `unguarded_routes()` over `docs/contracts/investor-reporting/v1/routes.json` at HEAD reads `0 of N` (N = handler-bearing routes, printed); the throwaway copy with one handler unregistered reads `1 of N`.
**(b) SIX SWAPS ON EACH OF THE SIX, IN-PROCESS.** For each of the six handlers: swapped firm / advisor / account / relationship / report / PDF identifiers refused with 0 protected bytes (byte census per swap); a valid principal served; `36 of 36` refusals.
**(c) THE FIRM COMES FROM THE PRINCIPAL.** A request whose body or path carries a different firm than the verified principal is refused `FIRM_BINDING`; a reconciling pair is served; printed.
**(d) THE PROJECTION IS ON THE SERVED PATH.** Through the real directory dispatcher: a grant present with no projection -> `UNPROJECTED-ID` refusal; a grant with the projection -> the narrowed intersection (`N of M` accounts, printed).
**(e) DEPLOYED AND VERIFIED.** For each function changed: `get-function-configuration` `CodeSha256` equals the built zip's; each root's plan after the apply reads `No changes` (printed per root); ledgers CLOSED with sentinels committed (hashes).
**(g) ENVELOPE CONFORMANCE, SERVED (amendment, row W2-S16).** IB-rt-1's paired producer-to-consumer test re-run against the DEPLOYED functions (invoke by name with the validator's injected header set): `11 of 11` responses validate against their response schema and `data` against the document schema; a mismatched `X-Contract-Version` refused `CONTRACT_VERSION` on `11 of 11`; printed per operation.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, at the hand-off, from IB-rt-1's census, row W2-S18):** arm (g)'s denominator is the ROUTES THAT HAVE A DEPLOYED HANDLER AT THIS CELL'S HEAD, printed as `N of N`, with the one published route that has NO handler at HEAD (`holdings-snapshot`, IB-rt-7's) named and EXCLUDED on its own line, never counted as a pass or a fail. IB-rt-1 handed the census `CONFORMS 0 / BLOCKED-BY-W2-S16 8 / DEPLOYED-ONLY 1 / NOT-A-ROUTE 2`: of the eight blocked, seven are handlers answering in an ad-hoc envelope and one is the no-handler route -- the seven are this cell's, the eighth is IB-rt-7's. The `X-Contract-Version` check is committed and NOT served (IB-rt-1 deployed nothing); this cell serves it. The seam's response contracts live at `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json` (one envelope `{contract_version, operation, firm_id, data, status?}`, `additionalProperties: false`; `data` the producer document or a declared slice whose properties `$ref` the document's own subschemas).
**(f) THE PRINCIPAL.** Either: one authenticated request through the real path served and one swapped-firm request refused, the principal minted through the named existing path (secret names only, no values); or: the `HUMAN-GATED` record printed verbatim naming the operator's exact act -- and the arm reads `HUMAN-GATED`, which is admitted by this criterion as a PASS of the arm's own rule, never as a skip.

<criterion id="RT2-AC2" cell_refs="IB-rt-2" judgment="true"/>
**`RT2-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which of the six were unguarded for a reason that ALSO protected them (the consent gate, the identity-less request shape, the absent operation) and whether guarding changed that protection; whether the test principal, if minted, differs from a real advisor's in any claim the validator reads; and what the in-process swaps cannot show that IB-rtb-1's real-path run must. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT2-AC1, RT2-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/investor-reporting/performance/
infra/aws/lambda/investor-reporting/ycharts/generate/
infra/aws/lambda/investor-reporting/narrative/
infra/aws/lambda/investor-reporting/export/
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/investor-reporting/performance/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/terraform/investor-reporting/narrative/
infra/aws/terraform/investor-reporting/export/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt2.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/ops/
infra/aws/terraform/investor-reporting/ops/
infra/aws/lambda/layers/irpt-common/
infra/aws/lambda/ci/lambda-layer-map.json
infra/aws/lambda/investor-reporting/_contracts/
infra/aws/lambda/investor-reporting/holdings/
infra/aws/terraform/investor-reporting/holdings/
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-2` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-2</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-ycharts-generate, irpt-narrative, irpt-export-render, irpt-directory-search, irpt-performance-adapter` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-ycharts-generate, irpt-narrative, irpt-export-render, irpt-directory-search, irpt-performance-adapter` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT2-AC1, RT2-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.proof_of_spec.json RT2-AC1,RT2-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.

---

## ISSUER AMENDMENT 2 -- 2026-09-12T00:03:10Z (`2.0.0_SA_COO~B`). **SECTION A6 ABOVE IS STRUCK AND REVERSED.** This block governs over it and over every line above it.

**A6 SAID:** slot ~3 deploys `irpt-export-render`, `irpt-status` and `irpt-ycharts-generate` FIRST, and this cell is
held off those three until the issuer confirms the landing.

**A6 WAS WRONG, AND THE TREE REFUSED IT.** Slot ~3 measured the consequence and filed row `IRPT_BCKEND-W3-S26`
(BLOCKING; landed on CLOUD at `670092d321`) rather than overriding the order. **That refusal is ACCEPTED IN FULL and
the row is DISARMED at the issuer** by seat row `IRPT_BCKEND-S38`.

**THE MEASUREMENT THAT KILLED IT.** All three roots ALREADY carry this cell's committed, unapplied
`handler -> entry.lambda_handler` flip, and `terraform apply` is per-ROOT, not per-attribute -- so the apply that
lands the `ids.py` packaging fix also lands the handler flip, and the `entry` module is in no zip:

```
plan investor-reporting/ycharts  ~ handler "job.lambda_handler"     -> "entry.lambda_handler"   0 add, 1 change, 0 destroy
plan investor-reporting/ops      ~ handler "status.lambda_handler"  -> "entry.lambda_handler"   0 add, 1 change, 0 destroy
plan investor-reporting/export   ~ handler "handler.lambda_handler" -> "entry.lambda_handler"   0 add, 1 change, 0 destroy
```

EXERCISED, not asserted -- each zip extracted to a flat `/var/task`, imported in a FRESH python3.12 interpreter with
the repo stripped from `sys.path`, negative control armed: all three read
`IMPORT-FAIL entry: ModuleNotFoundError: No module named 'served'`. Nothing was deployed; all three functions are
`Active` on their live bytes and each live zip re-measured CLOSED under its own live handler.

### A9. THE NEW SEQUENCING -- THE WHOLE ACT IS THIS CELL'S, AND IT IS ATOMIC.
**`entry.py` + `served.py` + `loaders.py` + (where genuinely needed) `ids.py` MUST LAND IN ONE ARTIFACT PER FUNCTION,
and the apply that flips the `handler` is the SAME apply that ships them.** There is no first-in-line cell, nothing to
wait for, and no hold on any function. A6 split an atomic act across two cells; you are not inheriting a delay, you
are inheriting the whole act across all six roots.

### A10. FIVE MEASURED GIFTS FROM SLOT ~3 -- DO NOT RE-DERIVE ANY OF THEM.
1. **THE BUILD RECIPE IS PROVEN.** Rebuilding each live artifact from its own live member bytes reproduces the S3
   object BYTE-FOR-BYTE (3 of 3 REPRODUCED): sorted arcnames, `ZIP_DEFLATED` at zlib default,
   `date_time=(2026,9,11,0,0,0)`, `external_attr=0o644<<16`, and **`create_system=0`** -- that last is the
   non-obvious member.
2. **RESOLUTION THE WAY THE BUILDER DOES IT** -- `source_dir` first, then the flat shared roots -- reads
   **14 of 14, 10 of 10, 27 of 27; NOTHING RESOLVES NOWHERE.** This independently confirms W3-S24 and the drain's
   union rule: **REMOVE NOTHING.** (`handler.py` for `irpt-status` resolves from `.../directory/`, which looks wrong
   and is not.)
3. **DO NOT ADD `ids.py` TO `irpt-export-render`** (row W3-S27). That function was NEVER armed by the `ids.py` gap:
   `irpt-common:5` carries `python/ids.py` byte-identical to `_ids/ids.py` (14173 B, sha `fc1017b2523f2340...`) and
   that function mounts the layer. Difference control: rebuilt WITHOUT `ids.py`, layer mounted -> 13 of 13 CLOSED;
   without the layer -> 10 of 13. **W3-S25's armed reading was the NO-LAYER reading.** Adding it there is the second
   definition the entry's own note refuses for `keys.py`. The gap IS real for the two layer-less functions (armed
   control 5 of 8 CLOSED, `No module named 'ids'`).
4. **THE IMPORT DERIVATION IS THE ROOT CAUSE, AND NO IN-REPO TEST CAN SEE IT.** `entry.py:34-43` derives `_authz`
   from the file's PARENT DIRECTORY, which at `/var/task` is `/var`. It resolves in the tree and cannot resolve in
   the runtime. **Verification for this arm is therefore extract-and-import in the flat layout, fresh interpreter,
   repo off `sys.path`** -- an in-tree pytest passes on a zip that dies at cold start, and `CodeSha256` equality
   cannot see it by construction.
5. **A SHARED-DEPENDENCY DEFECT SITS BENEATH ALL OF THIS AND IS NOT YOURS TO FIX** (row W3-S28): the layer's
   `python/keys.py` is **21320 B** against the tree's `_keys/keys.py` **29894 B** (also `raw_keys.json` 5990/6064,
   `firm_registry.json` 5094/5229). `irpt-export-render` ships no `keys.py` and therefore runs the LAYER's OLDER key
   grammar -- **two grammars are live at once.** Do not repair it and do not let your packaging make it worse. If
   your work forces a choice about which `keys.py` a function resolves, that is a BLOCKING row to me.

Slot ~3 also built and import-verified corrected zips (`irpt-ycharts-generate`
`gU4v6NbjxbygxEDLdYURjAgeGPGx3Xc2qzKGldjnbnE=`, `irpt-export-render` `6S29BGvKhG6O1T4TmR1b3bMlkyOZ50RlKWAY2fi/wMg=`,
`irpt-status` `/wihp7Lgum/nlmFMP6kNAqp039rWrvaqfOyXvvl6lPs=`). They sit on ITS branch, are NOT uploaded, and
`irpt-status` still read 9 of 10 with `entry` OPEN -- a reference point, never a substitute for your own build.

**UNCHANGED:** NEVER-2 (a ledger opens only with the room to close it in-session; OPEN sentinel committed BEFORE the
act, CLOSE before the reads that grade it), `safe-apply.sh` only, and
`artifact_sha256 == S3 content-sha256 == live CodeSha256` printed per function.

---

## ISSUER AMENDMENT 3 -- 2026-09-12T02:00:09Z (`2.0.0_SA_COO~B`), on the FAIL report. This block governs over every line above it.

**THE DEPLOY IS ACCEPTED.** Six roots, one at a time, `artifact_sha256 == S3 content-sha256 == live CodeSha256` on
6 of 6, guarded entry live on 6 of 6, every post-apply plan `No changes`, ledger `irpt-bckend-rt2` CLOSED with its
12 legs and its sentinel gone from `org/critical_paths/.open_deploys/` -- verified by the issuer at HEAD, not taken
from the report. The proof-of-spec instance re-grades `VALID (rc=0)` with 17 of 17 surprise rows resolving. **The
`<status>` correctly stays open on a FAIL.**

**AND THE TWO RUNTIME-ONLY DEFECTS ARE THE RESULT OF THIS CELL, not a footnote to it.** Neither was visible to any
in-tree test, and either alone meant none of the six could have served a production event: the package roots
derived from the parent of `/var/task`, and `served.Entry.operation_of` resolving the operation by READING
`routes.json` while `api/integrations.tf:57` declares `payload_format_version = "2.0"` with no request template --
so every production request carried exactly the shape that triggers it. **A guard that cannot import is not a
guard, and a deploy that matches three hashes says nothing about either.**

### C1. W2-S30 -- THE HOLDINGS PATHS ARE GRANTED. The census is not wrong and must not be loosened.
Arm (a)'s whole-file denominator moved 11 -> 12 while this cell was dead, because IB-rt-7's `irpt-holdings` went
live on its published route. The census reads **1 of 12**, the remedy paths sat outside `<paths>`, and W2-S31
records that the census grades the `__irpt_guarded__` MARK while that handler enforces the same `FirmBinding`
inline -- **so this is a MARK gap, not a live cross-firm hole.**

**GRANTED, additive, for this cell only:** `infra/aws/lambda/investor-reporting/holdings/` and the holdings
Terraform root. **DO NOT loosen the census to make 1 of 12 read 0 of 12** -- the mark is the census's contract and
an inline enforcement that the instrument cannot see is exactly the gap worth keeping visible. Bring the handler
under the same mark the other eleven carry.

### C2. g2 IS RULED **HUMAN-GATED**, under this face's OWN rule, and is no longer a FAIL.
The face already says: *"If none exists, the arm is written HUMAN-GATED naming the exact operator act (which
console, which user, which claim) and its expected reading -- never skipped silently."* Arm (f) was recorded that
way and accepted. **g2 depends on the SAME principal and therefore takes the SAME treatment** -- write it
HUMAN-GATED with the exact operator act and its expected reading. This is the face's stated rule applied to a
dependent arm, NOT a bar being lowered: nothing is asserted that was not exercised, and the arm reads
HUMAN-GATED rather than PASS.

### C3. g3 -- THE POST-READ HALF IS NOT SHIPPED ALONE, AND YOUR REASONING FOR THAT IS ACCEPTED.
You declined to ship the post-read half because it leaves 11 of 11 version refusals non-conforming and costs a
second six-root deploy to move nothing. **That is correct and it is the same rule I applied to myself tonight:
do not take an expensive or irreversible act that does not achieve its stated purpose.**
The pre-read half needs an amendment to the FROZEN v1 contract (`source_dates.required = ['business_date']`, and a
pre-read refusal has no artifact while v1 admits no null). **A frozen-contract amendment is NOT mine mid-round and
NOT yours.** It is with `1.0.0_SA_CTO` as the ONE ask blocking this cell. Do not work around it, do not emit a
placeholder date, and do not relax the validator.

### C4. WHEN THE CONTRACT ANSWER ARRIVES, EVERYTHING REMAINING LANDS IN **ONE** DEPLOY.
C1's mark, g3's post-read half and whatever the contract answer permits for the pre-read half are ONE act, on the
roots they actually touch, under ONE ledger. **Do not deploy for C1 alone.** Sequencing discipline from amendment
2 section A9 stands unchanged: one root at a time, verify each before the next, the ledger enumerating every root
and its rollback before the first apply, and a hard stop on the first failing verify.

### C5. UNTIL THEN THIS ORDER IS PARKED, NOT ABANDONED, AND YOU ARE NOT WAITING IDLE.
`IB-rt-6` and `IB-rtb-1` both gate on THIS order being terminal, so three cells of the round sit behind it. The
issuer is carrying the one contract question to `1.0.0_SA_CTO` now. **Do the C1 mark and the g2 HUMAN-GATED
record as tree work (no deploy), commit them, and report.** That leaves exactly one thing outstanding when the
answer lands.

---

## ISSUER AMENDMENT 4 -- 2026-09-12T02:38:27Z (`2.0.0_SA_COO~B`): **g3 IS UNBLOCKED.** This block governs over every line above it.

`1.0.0_SA_CTO` ruled the frozen-contract question and LANDED it: **PRD v0.13 -> v0.14 @`b8e98d5a4d`**, CONTRACTS row
`StatusEnvelope`, item 3 "source dates", plus the generated
`docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json`. Amendment 3's C3 is discharged.

### D1. THE ENVELOPE SHAPE, AND IT IS A STATE-CONDITIONAL -- NOT A NULLABLE FIELD.
```
source_dates              STAYS REQUIRED at the top level. The key is ALWAYS present, so no consumer
                          ever branches on its existence.
business_date REQUIRED    on the ANSWER-BEARING states: READY, PARTIAL, STALE, NEEDS_CORRECTION, UNCERTAIN
business_date MAY BE      on the NO-ANSWER states:       QUEUED, RUNNING, UNAVAILABLE, FAILED
  ABSENT -- NEVER NULL    an ABSENT field says "no value exists"; a NULL invites "we had one and lost it".
                          `source_completion_date` and `as_of` are already ["string","null"] because they
                          can be genuinely unknown BEHIND a real answer. business_date is a different
                          question and does NOT get that treatment.
```
Mechanically an `allOf` with an `if`/`then` on `state`; the sub-object's unconditional `required` is gone. Exercised
by the CTO, not asserted: 11 of 11 cases across all nine states, every answer-bearing state REFUSING a missing
`business_date`, every no-answer state ADMITTING it, and a negative control on a bogus state firing so the
validator is not inert.

**WHY NOT NULLABLE, which was option (a) in my own framing of the question:** making `business_date` nullable
weakens EVERY envelope including a READY success -- a served READY carrying a null date would then validate, and
the one thing this contract must not permit is a successful answer omitting the date it is an answer FOR. The
0-of-11 failure was real; that fix would have traded a validation gap for a semantic hole in the success path.

### D2. ⚠ THE CUT IS WIDER THAN THE TWO HALVES I GAVE YOU. **FOUR** STATES, NOT TWO.
I cut this POST-READ vs PRE-READ. That was right as far as it went and **it was short by two.** The enum has NINE
states, and **QUEUED and RUNNING also carry no `business_date` by construction -- and neither is a refusal at
all.** A fix scoped to "refusals" leaves both failing validation exactly as before.
**So the boundary must satisfy all FOUR no-answer states, not the two refusal ones.** The amendment is cut as a
SUBTRACTION from the printed nine-state enum (9 MINUS the 5 answer-bearing = 4), never forward from the cases in
hand -- Rule 24, and the same class as the issuer error in S38, the zip-ownership error in S39, W4-S28's
certification coordinate and S41's version count. **Write your own check the same way: from the enum, minus the
answer-bearing five.** Do not enumerate the states you happen to be thinking about.

### D3. ⛔ THE POST-READ OBLIGATION IS NOT EXCUSED -- IT MOVED FROM THE SCHEMA TO THE BATTERY. NAME IT IN THE CELL.
The conditional makes `business_date` OPTIONAL on `UNAVAILABLE` and `FAILED`. **It does NOT bless omitting it
there.** A POST-READ refusal HAS an artifact and therefore HAS a business date and MUST emit it. **The schema can
no longer catch that omission, so the obligation is now the BATTERY's:** a post-read refusal that omits
`business_date` is a BATTERY FAILURE, not a schema failure. Write that into the cell explicitly so the weakening
is PAID FOR rather than granted, and so a later reader finds the rule instead of a hole where one used to be.

### D4. ⛔ DO NOT HAND-EDIT THE SCHEMA, AND DO NOT TRY TO REGENERATE IT.
- **The schema is GENERATED, not authored.** Its own header names the PRD CONTRACTS table row as the source of
  record, every property description quotes that table VERBATIM, and a property whose quoted source string does
  not appear in the section at the pin **IS A FABRICATION AND IS REFUSED BY THE IB-s-18 BATTERY.** A hand-edit
  does not land; it makes that battery right to refuse it. The schema already moved as part of the CTO's L4 act --
  it is not yours to touch.
- **The generator is ABSENT from this device.** The header names `.scratch/gen_contracts.py`; `.scratch/` is
  gitignored and the file is on no device here. **"Regenerate the schema" is NOT an executable instruction for
  anyone right now** -- do not attempt it and do not treat a failure to run it as your defect.

### D5. WHAT THIS MEANS FOR YOUR ARMS, AND WHAT STILL STANDS.
g3 is now satisfiable: the boundary emits an envelope with no `business_date` on all four no-answer states and it
validates. **Amendment 3 is otherwise unchanged** -- C1's holdings mark granted with the census NOT loosened, C2's
g2 HUMAN-GATED (the CTO confirmed explicitly this is the face's own rule applied, not a bar lowered, and told me
not to put it back), and **C4's ONE-DEPLOY rule**: the mark, the post-read emission and the envelope work all land
in a single deploy under one ledger, one root at a time, verified before the next, roster and rollbacks printed
before the first apply, hard stop on the first failing verify.

---

## ISSUER AMENDMENT 5 -- 2026-09-12T03:56:10Z (`2.0.0_SA_COO~B`). Governs over every line above it.

### E1. ⛔ THE C1 GRANT WAS PROSE-ONLY. THAT IS MY DEFECT AND IT IS NOW FIXED IN THE `<paths>` BLOCK.
Amendment 3 C1 granted `holdings/` "additively" in a prose sentence and **never added it to the `<paths>` block**.
The owned-paths lane gate reads the BLOCK, not the prose, so it refused your four holdings files and **the gate was
right**. Row `IRPT_BCKEND-W2-S41` is correct and it is mine.

Added to `<paths>` in this amendment's commit:
```
infra/aws/lambda/investor-reporting/holdings/
infra/aws/terraform/investor-reporting/holdings/
```
**Commit C1's four files now.** Nothing else about C1 changes: `holdings/entry.py` composes the same triple, and
`make_holdings_enforcer` keeps defaulting ownership to `_no_grant`. ⭐ Your reasoning there was exactly right and I
want it on the record: handing `Entry` the shared loaders -- what the other six do -- would have turned a route
that serves nothing into one that serves real holdings, and that is IB-rt-7's decision, not this cell's. **A mark
must not widen what it marks.**

### E2. ⭐ AND YOUR REFUSAL TO FLIP `<status>` WAS CORRECT. I am recording it as a finding, not as a delay.
You did not flip on 15 of 15 because **the `<paths>` grant is live only while the order is NON-TERMINAL**, so
flipping would have retired the grant and permanently orphaned C1's work. That is a real property of the gate that
no face states, and reading it correctly under a passing token is the opposite of the failure mode this round has
been full of. It goes in the round-close slug: **A TERMINAL FLIP REVOKES THE GRANTS THE ORDER CARRIES, so the flip
is the LAST act and never the act that frees you to finish.**

### E3. W2-S38 RULED: THE YCHARTS RIDER IS **IN**. Deploy it.
IB-rt-11's `intake/settings.json` edit is a declared build input of `irpt-ycharts-generate` and your deploy will
carry it. It is **INERT** on measurement -- the cell read the SERVED artifact (5104 B) against the tree (9670 B) and
showed the delta is ONLY an added sibling key, with the `settings` subtree and `cautions` byte-identical -- and it is
that cell's committed, accepted, in-lane work. Ship it.
**NAME IT IN THE LEDGER ENTRY as a rider on the `irpt-ycharts-generate` leg**, so the entry states what the apply
actually carries rather than only what this cell authored. ⚠ If your zip for that function picks up
`settings.json` without `fixtures/holdings/security_mapping.json`, or either without `parse.py`, that is a BLOCKING
row to me and a stop -- row `W3-S36` says the parser refuses at its first money column otherwise.

### E4. TAKE THE ONE DEPLOY NOW. C4 is satisfied, and the cost of waiting has changed.
Everything remaining is one atomic act and all of it is finally in lane: C1's holdings mark, the v0.14 envelope
work, the post-read `business_date` emission, the `W2-S39` cache-lifetime fix, and the ycharts rider.
⛔ **`W2-S39` IS THE REASON THIS IS NOW URGENT RATHER THAN MERELY READY.** You introduced a stale-payload defect and
removed it in the tree, and it is **STILL ARMED ON THE SIX LIVE FUNCTIONS until a deploy ships the fix** -- a
snapshot that must be refused was SERVED from a prior request's payload. Authorization was never at risk and you
say so plainly, which is the right disclosure; but a known armed serving defect sitting in production while we
sequence is a worse trade than any sequencing benefit. **You were right to stop rather than split the atomic act I
defined -- that was my sequencing to fix, and E1 fixes it.**

Sequencing discipline UNCHANGED and it binds hardest here: ONE ledger, opened only with the room to CLOSE it
in-session, OPEN sentinel committed BEFORE the act and CLOSE before the reads that grade it; **one root at a time,
each function verified by extract-and-import in the flat `/var/task` layout in a fresh interpreter with the repo off
`sys.path` BEFORE the next root**; the full root roster and each root's rollback printed before the first apply;
`artifact_sha256 == S3 content-sha256 == live CodeSha256` per function; and a HARD STOP on the first failing verify
with N-of-M applied stated in the ledger. If any root's plan shows anything beyond your own changes and the named
rider, that is a BLOCKING row and a stop.

### E5. THE FLIP IS THE LAST ACT.
After the deploy verifies: re-run the battery, rewrite the instance FROM that run, re-pin every artifact row to the
commit that CARRIES it, re-grade with `proof-of-spec-check`, and only then flip `<status>`. IB-rt-6 and IB-rtb-1
both gate on this order being terminal, so the flip releases two cells -- but not one moment before the deploy is
verified and the record matches the bytes.
