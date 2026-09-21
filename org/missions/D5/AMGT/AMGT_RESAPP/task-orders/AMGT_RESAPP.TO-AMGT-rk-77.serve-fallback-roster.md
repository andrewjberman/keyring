# AMGT_RESAPP task order -- `AMGT-rk-77` -- `read_management` serves a NON-EMPTY Bloomberg-fallback roster, labelled as the fallback with the filing's own failure reason beside it, reports the REAL `officer_count`, and says `ZERO_OFFICERS` only when there are zero officers (row `Z-S194`, remedy (a)); `opal-amgt-scoped-api` is redeployed (carrying `AMGT-rk-76`'s additive `crosswalk.py`) under the round-19 R19-C never-widen pair, AFTER R19-B has drained

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-77</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~77</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence and reads or writes no
  schedule (the daily chatter schedule, chatter-axis-schedule.tf, is untouched). It OPENS one deploy-ledger entry with
  .tools/deploy_ledger.py before its first live write (the artifact upload) and CLOSES it on the post-act served read;
  the apply is TARGETED to module.scoped_amgt_api.aws_lambda_function.this and no other resource.
comp-iam: DECLARED-NOT-APPLICABLE -- the same shape as AMGT-rk-74's and AMGT-rk-37's redeploys of this function: the
  code moves under the existing opal-amgt-scoped-api-role through the existing Terraform resource with NO change to
  its role, policy, grant, environment variable, layer, timeout or memory, and NO new S3 call (the fallback branch
  reads the same management object the function already reads, and reads the management pool object LESS, not more).
  AC4/AC6 assert the role's inline policy hash IDENTICAL before and after.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~77`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **`lib/research/api/scoped_amgt.py`
AND EVERY FILE THE ADAPTER ARTIFACT PACKAGES HAS ONE WRITER AT ANY MOMENT: this order is the ONLY round-19 order that
writes or redeploys `opal-amgt-scoped-api`, and it is SEQUENCED BEHIND `AMGT-rk-76` (R19-B), whose `crosswalk.py`
change it carries.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~77;`. **NEVER RUN AN
INSTALL** (`terraform init` in the harvest root is a precondition, not an install into the tree). **Run the targeted
apply under a tool timeout of at least 600 s** -- `AMGT-rk-74`'s first apply hit a 120 s bound with nothing written.

## 1. THE CELL, inlined in full -- `AMGT-rk-77` (R19-C; row `AMGT_RESAPP-Z-S194`; co-sign YES)

**The ruling, verbatim (`ledger/ROUND_ANALYSIS.round18.md` @5f10ddf969, s.4 `:72-87`, `1.0.0_SA_CTO~Z`):** *"CALL 2 --
Z-S194: RULED remedy (a), serve the fallback roster, labelled. `C-EXEC-MANAGEMENT` (PRD :738-747, from Andrew's
2026-09-18 card 1) already says it: when the filing yields no RESOLVED roster, Bloomberg's `COMPANY_EXEC_OFFICERS`
fills the table (name and title only), every object carries `roster_source`, and the fallback never hides why the
filing failed. Only a roster with ZERO officers is withheld. The adapter (`scoped_amgt.py:2520-2533`) instead
withholds every non-RESOLVED roster and hard-codes `officer_count: 0`, so CSL (14 officers) and 6861 (1 officer) read
"zero officers". That is the adapter violating a ratified contract, not a choice between remedies. Cell R19-C: a
non-empty BLOOMBERG_FALLBACK roster is SERVED with `roster_source` and the filing's own failure reason; `officer_count`
is always the real count; an ABSENT label is TRUE in every branch (`ZERO_OFFICERS` only when there are zero officers;
an unresolved source with no fallback says so). It is an adapter redeploy under a never-widen pair; I owe the CTO half.
Sequenced behind R19-B inside the round, and its pair names R19-B's `crosswalk.py` commit as carry-along."* And
`:89`: *"Round 19 as issued: R19-A (re-projection), R19-B, then R19-C. One slug; R19-C sequenced behind R19-B."*

**The contract, verbatim (`prd/AMGT_RESAPP_PRD.md` v0.15 @437e219264, `C-EXEC-MANAGEMENT`, `:738-748`):** *"The
FILING's executive-officer section is the roster authority, and each officer's role start comes from it. When the
filing yields no RESOLVED roster, Bloomberg's `COMPANY_EXEC_OFFICERS` (name and title only, names kept verbatim) fills
the officer TABLE and is labelled on the page as a Bloomberg fallback. Role start, tenure and the pool comparison stay
ABSENT, with the reason that Bloomberg carries no role start. A RESOLVED filing roster replaces the fallback on the next
build. Every management object carries `roster_source` = FILING | BLOOMBERG_FALLBACK. The fallback never hides why
the filing failed: when a filing roster failed (an empty officer-section cut, or a section no declared shape reads),
its own `roster_status` and `roster_reason` stay on the object beside the Bloomberg officers, and the page shows them.
... A roster with ZERO officers is NOT SERVED. It is ABSENT with its reason."* (The PRD line carries one non-ASCII
marker glyph before "The fallback never hides"; it is omitted here.)

**THE MEASURED STATE (issuer, 2026-09-21 at HEAD `5f10ddf969`, read-only; re-measured by AC3/AC4 at spawn):**
- **The rule at HEAD** (`scoped_amgt.py` 3786 lines, last commit `7295ea257b` = rk-74), `read_management` `:2474-2566`:
  `:2518-2537` -- `if roster_status != "RESOLVED" or not officers:` -> `management_status ABSENT`, `absent_because
  "ZERO_OFFICERS"`, `reason` = `roster_reason`, `officer_count: 0` (hard-coded), no officers served. The SERVED branch
  `:2538-2565` reads the management pool object (`read_pool_object(MANAGEMENT_PREFIX, MANAGEMENT_POOL_NAME)`) and serves
  the officers verbatim with `source_accession`, `source_key`, `source_item`, the tenure averages, the pool comparison,
  `lusha_enrichment`, `ceo_public_profile` and `ceo_profile_reading`. **`roster_source` is served in NEITHER branch.**
- **The population -- every management object in `s3://opal-data-harvest/management/v1/` (18 objects: 15 security
  keys' dated objects + 3 `_pool/`), latest per key, 15 of 15:**

  | class | names | served today (thesis leaf, direct invoke) | after this cell |
  |---|---|---|---|
  | RESOLVED, officers > 0, `roster_source` FILING on the object | CAT_US_Equity (1) | SERVED | SERVED + `roster_source FILING`, `roster_source_basis object` |
  | RESOLVED, officers > 0, NO `roster_source` on the object (every officer `source: filing`) | BABA (7), BA (12), COST (13), HD (10), NU (9), SAP_GY (6), VLO (5) | SERVED | SERVED + `roster_source FILING`, `roster_source_basis` derived (section RULED item 3) |
  | UNRESOLVED-SOURCE, officers > 0, `roster_source BLOOMBERG_FALLBACK`, `fallback.status OK` | CSL_AU_Equity (14), 6861_JP_Equity (1) | ABSENT / ZERO_OFFICERS / officer_count 0 (FALSE) | **SERVED as the fallback** |
  | UNRESOLVED-SOURCE, 0 officers, no `roster_source`, no fallback block | ASML_NA, HAL, INTU, KMB, PBR | ABSENT / ZERO_OFFICERS / 0 (TRUE) | **byte-equal, unchanged** |

  Served today: SERVED 8, ABSENT 7 (15 of 15 routes 200). After: SERVED 10, ABSENT 5. **Two invokes of the same leaf
  return byte-equal management blocks (0 volatile leaf paths over 15 names)**, so pre/post equality is exact.
- **The two fallback objects** (`management/v1/<key>/2026-09-19.json`, latest version): CSL `roster_status
  UNRESOLVED-SOURCE`, `roster_source BLOOMBERG_FALLBACK`, 14 officers (each `source: bloomberg`, `role_start null`),
  `source_item None`, `source_accession None`, `source_key s3://opal-data-harvest/filings/v1/CSL_AU_Equity/UNRESOLVED-SOURCE.source.json`,
  `roster_reason` "the persisted filing is itself UNRESOLVED-SOURCE: every declared step failed ...",
  `absence_reason_class pull-missed`, `fallback {security, field COMPANY_EXEC_OFFICERS, status OK, entries_returned
  14, officers_parsed 14, raw_key raw/bloomberg/CSL_AU_Equity/20260921T162530Z/exec_officers.json, pulled_at, reason
  null, label "officers per Bloomberg COMPANY_EXEC_OFFICERS -- no filing roster; Bloomberg carries no role start, so
  role start, tenure and the pool comparison are ABSENT"}`. 6861: the same shape with 1 officer, `source_item ""`
  (empty string), `source_accession doc-1defdb68a7ffd3b7` (the FAILED filing's), `roster_reason` "... carries an EMPTY
  officer section (no item label) ...".
- **Why the served labels matter -- the page (read-only, `portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`
  @portal `db1c5f64`):** the SERVED branch prints `{n} officer(s) from {source_item ?? 'the filing'}{accession}`. Served
  VERBATIM, CSL would read **"14 officer(s) from the filing"** (source_item null) and 6861 **"1 officer(s) from ,
  accession doc-1defdb68a7ffd3b7"** -- both FALSE for a Bloomberg roster. The pool line prints
  `ABSENT (${pool_read.reason})` when `pool_avg_tenure_years` is null. Hence RULED items 2 and 4 below: the adapter
  serves TRUE values into the fields the existing page already renders. **The portal is NOT this cell's surface.**
- **Consumers of `read_management`:** `lib/research/api/tests/test_generation_and_pool_routes.py::test_13_...` (a
  RESOLVED roster and a missing object -- both UNCHANGED by this cell) and `test_13b_...` (the reading function only).
  No test asserts the old non-RESOLVED -> ABSENT rule.
- **CEO reading once served:** the SERVED branch adds `ceo_profile_reading(document["ceo_public_profile"])`. Measured
  on the stored objects: CSL and 6861 both read `NOT_SEARCHED`, `urls_returned None`. Their `reason` is the stored
  `ceo_public_profile.basis`: a status-code string ("NOT_SEARCHED / NO_VERIFIED_SITE -- ...") until `AMGT-rk-75`
  (R19-A, same round) re-projects it, then the plain sentence (CSL: "No verified company website was found, so the CEO
  web search was not run."). **Either is expected here**; this cell compares the CEO reading's `reading` and
  `urls_returned` only, never its `reason`.
- **Test baselines at HEAD `5f10ddf969`:** `lib/research/api/tests` 185 passed; `lib/research/identity/tests` 49 passed
  (AMGT-rk-76 adds 6; re-measure at spawn).

**RULED, what you build (in `lib/research/api/scoped_amgt.py`, `read_management` only):**
1. **The partition, by officer count first.** After the document is read: `officers = list(document.get("officers")
   or [])`.
   - `not officers` -> the ABSENT / `ZERO_OFFICERS` block EXACTLY as today (same keys, same values, `officer_count 0`).
     This branch's served bytes must not move (AC6 compares the 5 names byte-for-byte).
   - officers present AND `roster_source` (RULED item 3) is `BLOOMBERG_FALLBACK` -> the FALLBACK branch (item 2).
   - officers present AND `roster_status == "RESOLVED"` -> today's SERVED branch, plus item 3's two keys.
   - officers present, NOT RESOLVED, NOT a fallback (0 names today) -> ABSENT with `absent_because
     "ROSTER_UNRESOLVED_NO_FALLBACK"`, `officers []`, `officer_count` = the REAL count of the unaccepted rows, `reason` =
     `roster_reason` or "the filing roster is not RESOLVED and no Bloomberg fallback landed", plus the same
     `roster_status` / `roster_reason` / `absence_reason_*` / `source_*` keys the ZERO_OFFICERS block carries.
   **`ZERO_OFFICERS` is emitted ONLY when `officer_count == 0`.**
2. **The FALLBACK branch** serves `management_status "SERVED"`, `absent_because None`, and:
   - `officers` VERBATIM, `officer_count len(officers)`, `officers_with_tenure` counted as today,
     `avg_tenure_years document.get("avg_tenure_years")`, `avg_tenure_denominator` in today's format;
   - **NO pool read.** `pool_avg_tenure_years None`, `pool_denominator None`, and `pool_read {"status": "NOT_READ",
     "reason": "Bloomberg COMPANY_EXEC_OFFICERS carries no role start, so tenure and the pool comparison are ABSENT"}`
     (C-EXEC-MANAGEMENT: "Role start, tenure and the pool comparison stay ABSENT, with the reason that Bloomberg carries
     no role start");
   - `roster_source "BLOOMBERG_FALLBACK"`, `roster_source_basis "object"`, and the FILING's failure carried beside the
     officers: `roster_status`, `roster_reason`, `absence_reason_class`, `absence_reason_evidence` VERBATIM;
   - **the source fields name what the officers came from:** `source_item "Bloomberg COMPANY_EXEC_OFFICERS (fallback:
     no RESOLVED filing roster)"`, `source_accession None`, `source_key "s3://opal-data-harvest/" + fallback["raw_key"]`
     when the object's `fallback.raw_key` is a non-empty string, else `None`; the failed filing's own values VERBATIM as
     `filing_source_item`, `filing_source_accession`, `filing_source_key`;
   - `fallback` = the object's `fallback` block VERBATIM (it carries `label`, `pulled_at`, `raw_key`,
     `entries_returned`, `officers_parsed`);
   - `as_of`, `generated`, `lusha_enrichment`, `ceo_public_profile`, `ceo_profile_reading` exactly as the SERVED
     branch serves them.
   Nothing the object does not carry is invented; the only served strings the object does not hold verbatim are the
   `source_item` label and the `pool_read` reason, both fixed text stating the contract.
3. **`roster_source` on every SERVED block.** A helper `_roster_source(document, officers) -> (source, basis)`:
   the object's `roster_source` when it is `FILING` or `BLOOMBERG_FALLBACK` -> `(value, "object")`; else, when
   `roster_status == "RESOLVED"` and every officer carries `source == "filing"` -> `("FILING", "derived: RESOLVED
   filing roster, every officer source filing; the object predates the roster_source field")`; else `(None, "absent:
   the object carries no roster_source and the officers do not settle it")`. The SERVED (FILING) branch gains the two
   keys `roster_source` and `roster_source_basis`, inserted immediately after `roster_reason`; **no other key of that
   branch is added, removed, renamed, re-ordered or re-valued.**
4. **Tests, a new file `lib/research/api/tests/test_fallback_roster_served.py`**, offline (copy the `pool` fixture and
   `_identity` helper pattern from `test_generation_and_pool_routes.py:354-379`: a tmp pool root via
   `scoped_amgt.ENV_POOL_ROOT`, `_dynamodb` patched to fail loud, `pool_reader.clear_caches()`). Fixtures are built
   from the MEASURED shapes above (CSL-shaped 14-officer fallback, 6861-shaped 1-officer fallback with `source_item ""`
   and a failed accession, a 0-officer UNRESOLVED object, a RESOLVED object with and one without `roster_source`, and a
   non-RESOLVED filing roster with officers and no fallback). Arms, each printing its denominator:
   - `test_fallback_roster_is_served_labelled` -- both fallback fixtures: SERVED, `officer_count` 14 / 1, officers
     verbatim, `roster_source BLOOMBERG_FALLBACK`, `roster_status`/`roster_reason` carried, `source_item` the fallback
     label, `source_accession None`, `filing_source_accession` the failed accession, `source_key` the raw key,
     `pool_read.status NOT_READ` and no pool object read (a pool object planted at the same date is NOT served),
     `avg_tenure_denominator "0 of 14 officer(s) carry a role start"`;
   - `test_zero_officer_block_is_unchanged` -- the 0-officer fixture's block EQUALS the pinned pre-change code's block
     (key list and values);
   - `test_resolved_block_gains_only_roster_source` -- for both RESOLVED fixtures, the block minus `roster_source` and
     `roster_source_basis` EQUALS the pinned pre-change code's block, the two keys sit immediately after
     `roster_reason`, and the basis reads `object` / `derived: ...` respectively;
   - `test_unresolved_filing_roster_without_fallback_says_so` -- ABSENT, `absent_because
     ROSTER_UNRESOLVED_NO_FALLBACK`, `officer_count` the real row count, `officers []`;
   - `test_zero_officers_label_only_when_zero` -- over every fixture, `absent_because == "ZERO_OFFICERS"` if and only
     if `officer_count == 0`;
   - `test_pinned_copy_withholds_the_fallback` -- the DISCRIMINATING arm: the pinned pre-change code returns ABSENT /
     ZERO_OFFICERS / `officer_count 0` on the CSL-shaped fixture, proving the first arm discriminates.
   **THE PINNED PRE-CHANGE CODE is `git show 7295ea257b:lib/research/api/scoped_amgt.py`** -- the last commit that
   touched the file before this cell, pinned BY HASH as `PRE_FALLBACK_COMMIT = "7295ea257b..."` (full 40-hex from `git
   rev-parse 7295ea257b`), loaded into a temp file and imported under another module name, with its `_dynamodb`
   patched like the real module's. **NEVER `HEAD`, never a merge-base** (row `Z-S193`: a merge-base copy becomes this
   cell's own code once merged and the arm then fails on every tree).
5. **The deploy**, per section 3's DEPLOY block, under the pair, ledgered, with the rollback read from THIS act's
   pre-act values (AC4).

**Blast radius, for the halves to name (each writer counted -- ONE writer of the artifact key and ONE of the function:
this order):** (i) the `management` block of the security routes that serve it, for the 15 names that carry a
management object: CSL and 6861 move ABSENT -> SERVED (fallback-labelled); the 8 FILING names gain exactly two keys
(`roster_source`, `roster_source_basis`); the 5 zero-officer names do not move; (ii) `AMGT-rk-76`'s additive
`crosswalk.py` reaches the served plane (new functions nothing on the served path calls; served keys unchanged, per
rk-76's own AC3); (iii) `CodeSha256`, `CodeSize` and `LastModified` of `opal-amgt-scoped-api`. NOT moved: the role and
its policies, environment, layers, timeout 29, memory 512, the route set, the gateway, any other function
(`amgt-resapp-chatter-axis` is NOT redeployed), any pool object, any management object, any table, the portal.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`):** proven on a DRY RUN first (AC2, in-process on fixtures, no producer, no
write), then on the served plane over the WHOLE management population (15 of 15 names, AC4/AC6) plus the 13-route
status census on `BA_US_Equity`. `C-PRODUCTION-HOME`: the artifact is built from the repository's own sources, as today.

## 2. WHERE THIS CAME FROM

**ROUND 19**, decomposition s.27 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-18 analysis
`ledger/ROUND_ANALYSIS.round18.md` @ac58e01116 and its s.4 addendum @5f10ddf969 (msg 24015), row `AMGT_RESAPP-Z-S194`
(@896b54f147, ARMED, disarm_owner `1.0.0_SA_CTO~Z`), PRD v0.15 `C-EXEC-MANAGEMENT` `:738-748`.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES:** CO-SIGNED. The COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_R19C_COO_HALF.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_R19C_CTO_HALF.md`. "The pair is on file" MEANS: both files
exist in your worktree, each carries a section headed with `AMGT-rk-77`, and that section names this order's blast
radius -- INCLUDING `AMGT-rk-76` -- and the per-key rollback. Read both BEFORE your first live act (AC1). Either absent,
its `AMGT-rk-77` section missing, or rk-76 unnamed: run ONLY the read-only criteria (AC1, AC2, AC3), file a BLOCKING
row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

**ISSUER RULE -- THE SEQUENCE AND THE CARRY-ALONG:** the artifact packages the SAME 58 repo paths `AMGT-rk-74`
censused (listed in AC3). The served source is `7295ea257b` (rk-74's code commit; its deploy set the live
`CodeSha256 P4n1bVaacgbZDuC+6I0H8YoDASREqJWgSLrfUjnPom0=`, artifact `VersionId o5x2gdqqdA.79nT7Ngpf6ymZ_LPbeN3a`).
Measured at the cut: `git log --no-merges 7295ea257b..HEAD -- <58 paths>` prints NOTHING. **At your spawn, R19-B MUST
already be drained:** AC3 requires `AMGT-rk-76`'s order's status tag to read `complete` at your HEAD, and every
non-merge commit on the 58 paths since `7295ea257b` to be EITHER authored by `0.9.0_WK_AMGT_RESAPP~76` touching ONLY
`lib/research/identity/crosswalk.py`, OR authored by you touching ONLY `lib/research/api/scoped_amgt.py`. Anything else
is a packaged change the pair does not name: STOP, BLOCKING row, no deploy; the issuer re-cuts the halves. And no
commit may land on a packaged path on SITEZ after your worktree's base (the single-writer queue).

**ISSUER RULE -- THE ROLLBACK MECHANISM** (unchanged from rk-74): the module's `data "aws_s3_object" "artifact"`
resolves the CURRENT version, so a rollback never edits Terraform. Rollback = `aws s3api copy-object --bucket
opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source
"opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<AC4 VersionId>"`, then the SAME
targeted `safe-apply`, then `get-function-configuration` prints AC4's pre-act `CodeSha256`. No version is deleted.

**COLLISIONS, checked at the cut (names only):** round 19 is THREE cells. `AMGT-rk-75` (R19-A) writes
`lib/research/management/{enrich.py,ceo_search.py,management.schema.json}` + tests and re-projects
`ceo_public_profile` on the 3 validation names' management objects -- **no `lib/research/management` path is among the
58 packaged paths and `scoped_amgt.py` imports nothing from `lib.research.management` (0 hits)**, so rk-75 is NOT a
carry-along; its only effect here is the CEO reading's `reason` text on CAT/CSL/6861, which AC6 does not compare.
`AMGT-rk-76` (R19-B) writes `crosswalk.py` + a new identity test -- the carry-along above. The held branch
`wk-amgt-14-50` is NEVER read, shown, diffed or checked out.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_fallback_roster_served.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~77/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-77.serve-fallback-roster.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND19_R19C_*_HALF.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant (`crosswalk.py`, the portal page, the build
  script, `.tools/safe-apply.sh`, `.tools/deploy_ledger.py`, the tests). **`crosswalk.py` and every
  `lib/research/management` file are read, never written. The portal is never written.** The two halves are granted so
  they can be read in your worktree; you never edit them. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~77 <0.9.0_WK_AMGT_RESAPP~77@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Commit the
  adapter edit and the test BEFORE the deploy; name that hash in the ledger entry's title.
- **DEPLOY -- in this order, each step's evidence recorded verbatim in the ledger entry:**
  0. AC1, AC2, AC3, AC4 pass (read-only). AC1 failing = STOP. AC3 printing anything unexpected = STOP.
  1. `python .tools/deploy_ledger.py open --slug amgt-rk77-serve-fallback-roster --title "<AMGT-rk-77: fallback roster served + true absent labels + rk-76 crosswalk.py <hash(es)>; commit <hash>; co-signed R19-C pair COO <sha256> / CTO <sha256>>" --author 0.9.0_WK_AMGT_RESAPP~77 --leg "L1|verify|module.scoped_amgt_api.aws_lambda_function.this|targeted apply 0 destroy + 0-diff replan + CodeSha256 == uploaded sha + 13-route census LOST=[] GAINED=[] + management 15 of 15 per the AC6 classes + role policy sha unchanged"`
     -- BEFORE the first live write.
  2. `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` -- record the artifact sha256 (base64) and the
     upload `VersionId` into `.scratch/rk77_upload.json` as `{"sha256_b64": ..., "version_id": ...}` (Write tool or
     python, never a shell heredoc).
  3. `terraform -chdir=infra/aws/terraform/harvest init -input=false` once.
  4. Plan precondition exactly as rk-74's step 4 (`chatter-axis-schedule.tf` `fileexists` guard, else
     `python infra/aws/terraform/harvest/lambda_src/build_zip.py` into the gitignored `.build/`; never a placeholder zip).
  5. `terraform -chdir=infra/aws/terraform/harvest plan -input=false -lock=false -no-color -target=module.scoped_amgt_api.aws_lambda_function.this`
     -- must read `Plan: 0 to add, 1 to change, 0 to destroy.` naming ONLY that resource. Anything else: STOP, row,
     ledger left OPEN with the reason, no apply.
  6. `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -auto-approve -lock-timeout=60s -target=module.scoped_amgt_api.aws_lambda_function.this`
     under a tool timeout of at least 600 s -- must read `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
     Never bare `terraform apply`, never `aws lambda update-function-code`. If the tool bound is hit, verify
     `CodeSha256` unmoved and no state lock BEFORE any retry, and record it.
  7. AC5, AC6. Then `deploy_ledger.py close-leg --slug amgt-rk77-serve-fallback-roster --leg-id L1 --proof "<AC5 and AC6 output verbatim>"`
     and `deploy_ledger.py close --slug amgt-rk77-serve-fallback-roster`; commit the entry.

## 4. BOUNDS

**THIS ORDER MOVES SERVED OUTPUT**, ONLY under the pair, ONLY after AC3 prints what it must, ONLY through steps 1-7,
ONLY on `module.scoped_amgt_api.aws_lambda_function.this`. **THE ROLLBACK BRANCH:** AC5 reads a `CodeSha256` other than
the uploaded sha; or AC6 LOSES any of the 13 routes; or any of the 15 management blocks falls outside its AC6 class;
or the role policy hash moved -- execute the rollback (section 2), file a BLOCKING row, close the ledger leg with the
rollback proof. NEVER leave the deploy half-landed (CLAUDE.md NEVER-2).
**PORTAL: not your surface** -- the page renders the fields this cell serves as it stands; a portal change (showing
`roster_reason` on a SERVED fallback block) is NOT this cell. **COLLECTION STAYS OFF.** **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** No secret is needed. **No vendor call; no Bloomberg call** (every
live read is `lambda.invoke`, `get_function_configuration`, `head_object`, `get_bucket_versioning`,
`list_objects_v2`, `get_object` on management objects, `get_role_policy`, or a targeted Terraform plan). **No S3 write
but the artifact key; no pool write; no management write.** No non-ASCII in anything you write. **PUSH: never**
(LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- never by editing a management object, never by
editing the portal, never by an environment variable, never by editing `crosswalk.py`.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- the pytest baselines (185 api; 49 + rk-76's 6 identity),
the 13-route statusCodes and the 15-name management population are re-measured; they may have moved. If the population
is no longer 15 names or a name changed class since the cut, AC4 prints it and AC6 grades against AC4's classes, not
this section's table.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W77-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. Row `Z-S194`'s disarm is the CTO's and the
CVO's L9, not yours: name the outcome in your report and file nothing on its behalf. **Found something off-task?
APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import hashlib, io, os, re
d = "org/missions/D5/AMGT/AMGT_RESAPP/ledger/"
for half in ("NEVER_WIDEN_ROUND19_R19C_COO_HALF.md", "NEVER_WIDEN_ROUND19_R19C_CTO_HALF.md"):
    p = d + half
    if not os.path.exists(p):
        print(half, "ABSENT"); continue
    b = io.open(p, "rb").read()
    t = b.decode("utf-8", "replace")
    heads = [l for l in t.splitlines() if l.startswith("#") and "AMGT-rk-77" in l]
    print(half, "sha256", hashlib.sha256(b).hexdigest(), "rk77_section_headings", len(heads), "of 1", "mentions_rollback", len(re.findall(r"(?i)rollback", t)), "mentions_VersionId_or_CodeSha256", len(re.findall(r"VersionId|CodeSha256", t)), "names_rk76", len(re.findall(r"AMGT-rk-76", t)))
'</invocation><expect>both halves present, each printing a 64-hex sha256, rk77_section_headings 1 of 1, mentions_rollback at least 1, mentions_VersionId_or_CodeSha256 at least 1 and names_rk76 at least 1 -- the pair is on file and both halves name the rk-76 carry-along; an ABSENT half, 0 of 1 headings or names_rk76 0 REFUSES this criterion and STOPS the order after AC2 and AC3 (read-only)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests lib/research/identity/tests -q -p no:cacheprovider 2>&1 | tail -5 && python -m pytest lib/research/api/tests/test_fallback_roster_served.py -v -s -p no:cacheprovider 2>&1 | tail -40</invocation><expect>the first run's final line reads "N passed" with 0 failed and N = the api baseline (185 at the cut) + the identity baseline (49 at the cut, plus AMGT-rk-76's 6 once it has drained -- re-measure both at spawn BEFORE editing) + K, K = this cell's new tests; test_generation_and_pool_routes.py (test_13, test_13b) and test_scoped_amgt_mount.py pass UNCHANGED inside it; the second run passes 6 of 6 named arms (test_fallback_roster_is_served_labelled, test_zero_officer_block_is_unchanged, test_resolved_block_gains_only_roster_source, test_unresolved_filing_roster_without_fallback_says_so, test_zero_officers_label_only_when_zero, test_pinned_copy_withholds_the_fallback), each printing its denominator: the two fallback fixtures SERVED with officer_count 14 and 1 and roster_source BLOOMBERG_FALLBACK; the zero-officer block equal to the pinned 7295ea257b copy's; the two RESOLVED blocks equal to the pinned copy's minus exactly roster_source and roster_source_basis; ZERO_OFFICERS if and only if officer_count 0 over every fixture; and the pinned copy returning ABSENT / ZERO_OFFICERS / 0 on the CSL-shaped fixture (the arm discriminates)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import io, re, subprocess
P = """infra/aws/lambda/research/scoped_amgt_api/lambda_function.py lib/opal_data_harvest/__init__.py lib/opal_data_harvest/catalog.py lib/opal_data_harvest/storage.py lib/research/api/__init__.py lib/research/api/scoped_amgt.py lib/research/checkface/__init__.py lib/research/checkface/fixtures.py lib/research/checkface/markers.py lib/research/checkface/render_print.py lib/research/checkface/run_checks.py lib/research/checkface/salience_fixture.py lib/research/checkface/scopes.py lib/research/coverage/__init__.py lib/research/coverage/pool_reader.py lib/research/drafting/__init__.py lib/research/drafting/pipeline.py lib/research/drafting/producer.py lib/research/drafting/verbatim.py lib/research/freshness/__init__.py lib/research/freshness/build_view.py lib/research/identity/__init__.py lib/research/identity/crosswalk.py lib/research/ledger/__init__.py lib/research/ledger/ledger.py lib/research/lists/__init__.py lib/research/lists/rot.py lib/research/metrics/__init__.py lib/research/metrics/chatter_axis.py lib/research/metrics/chatter_gate.py lib/research/metrics/generation_writer.py lib/research/metrics/movement_gate.py lib/research/price/__init__.py lib/research/price/axis.py lib/research/print/__init__.py lib/research/print/render_pack.py lib/research/provenance/__init__.py lib/research/provenance/render_print.py lib/research/provenance/validate.py lib/research/rules/__init__.py lib/research/rules/figure.py lib/research/rules/identity.py lib/research/rules/item.py lib/research/rules/peer.py lib/research/rules/sentence.py lib/research/rules/source.py lib/research/scores/__init__.py lib/research/scores/classify.py lib/research/watchlist/__init__.py lib/research/watchlist/store.py lib/opal_data_harvest/article.schema.json lib/opal_data_harvest/security-article.schema.json lib/research/drafting/schema.json lib/research/rules/data/peer_overlap.json lib/research/rules/data/figure_units.json org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/publishers.json org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/social_accounts.json infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh""".split()
g = lambda *a: subprocess.run(["git"] + list(a), capture_output=True, text=True, encoding="utf-8").stdout
import os
print("packaged_paths", len(P), "of 58", "present", sum(1 for p in P if os.path.exists(p)))
o76 = "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-76.slash-safe-key.md"
t = io.open(o76, encoding="utf-8").read() if os.path.exists(o76) else ""
print("rk76_order_present", bool(t), "rk76_status_complete", bool(re.search("^<" + "status>complete</" + "status>$", t, re.M)))
base = g("merge-base", "HEAD", "SITEZ").strip()
late = g("log", "--no-merges", "--format=%h", base + "..SITEZ", "--", *P).split()
print("packaged_commits_on_SITEZ_since_base", len(late), "of 0 expected", late)
ok = {"0.9.0_WK_AMGT_RESAPP~76": {"lib/research/identity/crosswalk.py"}, "0.9.0_WK_AMGT_RESAPP~77": {"lib/research/api/scoped_amgt.py"}}
rows = [l.split("|", 2) for l in g("log", "--no-merges", "--format=%H|%an|%s", "7295ea257b..HEAD", "--", *P).splitlines() if l]
bad = []; seen = {"0.9.0_WK_AMGT_RESAPP~76": 0, "0.9.0_WK_AMGT_RESAPP~77": 0}
for h, an, s in rows:
    files = set(g("diff-tree", "--no-commit-id", "--name-only", "-r", h, "--", *P).split())
    allowed = ok.get(an)
    if allowed is None or not files <= allowed:
        bad.append((h[:10], an, sorted(files), s[:60]))
    else:
        seen[an] += 1
print("carry_along_since_served_source_7295ea257b", len(rows), "commit(s):", "rk76", seen["0.9.0_WK_AMGT_RESAPP~76"], "own", seen["0.9.0_WK_AMGT_RESAPP~77"], "UNNAMED", bad)
print("positive_control_last_crosswalk_commit", g("log", "--format=%h %an", "-1", "--", "lib/research/identity/crosswalk.py").strip())
'</invocation><expect>packaged_paths 58 of 58 present 58; rk76_order_present True rk76_status_complete True (R19-B has drained -- this order is sequenced behind it; False is a STOP before any live act); packaged_commits_on_SITEZ_since_base 0 of 0 expected [] (the single-writer queue holds); carry_along_since_served_source_7295ea257b lists rk76 at least 1 and own at least 1 with UNNAMED [] -- every packaged commit since the served source is either AMGT-rk-76 on crosswalk.py alone or this worker on scoped_amgt.py alone (0 commits at the cut, before either existed); positive_control_last_crosswalk_commit prints one line naming 0.9.0_WK_AMGT_RESAPP~76 (the log instrument works). ANY UNNAMED entry, or rk76 0 with rk76_status_complete True, is a STOP with a BLOCKING row and no deploy</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && mkdir -p .scratch && python -c '
import boto3, hashlib, io, json, re
from lib.research.api import scoped_amgt
lam = boto3.client("lambda"); s3 = boto3.client("s3"); iam = boto3.client("iam")
cfg = lam.get_function_configuration(FunctionName="opal-amgt-scoped-api")
pre = {"CodeSha256": cfg["CodeSha256"], "LastModified": cfg["LastModified"], "CodeSize": cfg["CodeSize"], "Timeout": cfg["Timeout"], "MemorySize": cfg["MemorySize"], "Layers": len(cfg.get("Layers", [])), "EnvKeys": sorted((cfg.get("Environment") or {}).get("Variables", {}).keys())}
ho = s3.head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
pre["ArtifactVersionId"] = ho.get("VersionId"); pre["BucketVersioning"] = s3.get_bucket_versioning(Bucket="opal-313476888478-lambda-artifacts").get("Status")
role = cfg["Role"].rsplit("/", 1)[-1]; names = sorted(iam.list_role_policies(RoleName=role)["PolicyNames"])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)["PolicyDocument"] for n in names}
pre["Role"] = role; pre["InlinePolicies"] = len(names); pre["PolicySha256"] = hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest()
def invoke(path, qs=None):
    ev = {"rawPath": path, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    if qs: ev["queryStringParameters"] = qs
    body = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    inner = body.get("body"); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == "{" else {}
    return body.get("statusCode"), inner
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith("GET")]
census = {}
for r in routes:
    p = r.replace("{movement}", "trending").replace("{subject}", "chatter").replace("{security_key}", "BA_US_Equity")
    census[r] = invoke(p, {"tickers": "BA US"} if "timeseries" in p else None)[0]
print("pre_census", len(census), "of 13 GET routes", json.dumps(census))
keys = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="management/v1/") for o in pg.get("Contents", [])]
names15 = sorted({m.group(1) for m in (re.match(r"^management/v1/(.+)/\d{4}-\d{2}-\d{2}\.json$", k) for k in keys) if m and m.group(1) != "_pool"})
latest = {}
for k in keys:
    mm = re.match(r"^management/v1/(.+)/\d{4}-\d{2}-\d{2}\.json$", k)
    if mm and mm.group(1) != "_pool": latest[mm.group(1)] = max(latest.get(mm.group(1), ""), k)
stored = {n: len(json.loads(s3.get_object(Bucket="opal-data-harvest", Key=latest[n])["Body"].read()).get("officers") or []) for n in names15}
print("stored_officers", json.dumps(stored, sort_keys=True))
mg = {}; cls = {}
for n in names15:
    st, inner = invoke("/api/scoped/amgt/security/%s/thesis" % n)
    m = inner.get("management") or {}
    mg[n] = m
    cls[n] = "%s/%s/%s" % (m.get("management_status"), m.get("absent_because"), m.get("officer_count"))
print("management_objects", len(keys), "names", len(names15), "served", sum(1 for m in mg.values() if m.get("management_status") == "SERVED"), "absent", sum(1 for m in mg.values() if m.get("management_status") == "ABSENT"))
print("pre_classes", json.dumps(cls, sort_keys=True))
print("roster_source_served_on", sum(1 for m in mg.values() if "roster_source" in m), "of", len(mg))
pre["census"] = census; pre["management"] = mg; pre["stored_officers"] = stored
io.open(".scratch/rk77_pre.json", "w", encoding="utf-8", newline="\n").write(json.dumps(pre, indent=1, default=str))
print("PRE-ACT", json.dumps({k: pre[k] for k in ("CodeSha256", "LastModified", "CodeSize", "ArtifactVersionId", "BucketVersioning", "Role", "InlinePolicies", "PolicySha256", "Timeout", "MemorySize", "Layers", "EnvKeys")}, default=str))
'</invocation><expect>PRE-ACT prints the LIVE CodeSha256 (P4n1bVaacgbZDuC+6I0H8YoDASREqJWgSLrfUjnPom0= at the cut, the rk-74 deploy; re-measure), the artifact's current VersionId (the rollback target of THIS act; o5x2gdqqdA.79nT7Ngpf6ymZ_LPbeN3a at the cut), BucketVersioning Enabled, the role with its inline policy count and PolicySha256, Timeout 29, MemorySize 512, Layers 1 and the two env keys; pre_census 13 of 13 with each statusCode recorded (13 x 200 at the cut); stored_officers per name (CSL_AU_Equity 14, 6861_JP_Equity 1, ASML_NA/HAL/INTU/KMB/PBR 0, and the 8 SERVED names equal to their served counts at the cut); management_objects 18 names 15 served 8 absent 7 at the cut, with pre_classes CSL_AU_Equity and 6861_JP_Equity ABSENT/ZERO_OFFICERS/0 (the defect: 14 and 1 officers stored), ASML_NA, HAL, INTU, KMB, PBR ABSENT/ZERO_OFFICERS/0, and the 8 others SERVED/None/<count> (BABA 7, BA 12, CAT 1, COST 13, HD 10, NU 9, SAP_GY 6, VLO 5); roster_source_served_on 0 of 15; all of it written to .scratch/rk77_pre.json for AC6. BucketVersioning other than Enabled is a STOP</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, io, json, re, subprocess
up = json.load(io.open(".scratch/rk77_upload.json", encoding="utf-8"))
pre = json.load(io.open(".scratch/rk77_pre.json", encoding="utf-8"))
cfg = boto3.client("lambda").get_function_configuration(FunctionName="opal-amgt-scoped-api")
print("post_CodeSha256", cfg["CodeSha256"], "equals_uploaded_sha", cfg["CodeSha256"] == up["sha256_b64"], "moved_from_pre", cfg["CodeSha256"] != pre["CodeSha256"])
print("Timeout", cfg["Timeout"], "MemorySize", cfg["MemorySize"], "Layers", len(cfg.get("Layers", [])), "EnvKeys_equal_pre", sorted((cfg.get("Environment") or {}).get("Variables", {}).keys()) == pre["EnvKeys"])
ho = boto3.client("s3").head_object(Bucket="opal-313476888478-lambda-artifacts", Key="research/opal-amgt-scoped-api.zip")
print("artifact_VersionId_now", ho.get("VersionId"), "equals_uploaded", ho.get("VersionId") == up["version_id"], "pre_act_VersionId", pre["ArtifactVersionId"])
r = subprocess.run(["terraform", "-chdir=infra/aws/terraform/harvest", "plan", "-input=false", "-lock=false", "-no-color", "-target=module.scoped_amgt_api.aws_lambda_function.this"], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=110)
print("replan_rc", r.returncode, re.findall(r"No changes\. Your infrastructure matches the configuration\.|Plan: \d+ to add, \d+ to change, \d+ to destroy\.", r.stdout + r.stderr))
'</invocation><expect>equals_uploaded_sha True and moved_from_pre True; Timeout 29, MemorySize 512, Layers 1, EnvKeys_equal_pre True; artifact_VersionId_now equals_uploaded True with the pre_act_VersionId printed beside it; replan_rc 0 with "No changes. Your infrastructure matches the configuration."</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-77"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c '
import boto3, hashlib, io, json
from lib.research.api import scoped_amgt
pre = json.load(io.open(".scratch/rk77_pre.json", encoding="utf-8"))
lam = boto3.client("lambda"); iam = boto3.client("iam")
def invoke(path, qs=None):
    ev = {"rawPath": path, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    if qs: ev["queryStringParameters"] = qs
    body = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    inner = body.get("body"); inner = json.loads(inner) if isinstance(inner, str) and inner[:1] == "{" else {}
    return body.get("statusCode"), inner
routes = [r.split()[1] for r in scoped_amgt.scoped_amgt_route_table() if r.startswith("GET")]
post = {}
for r in routes:
    p = r.replace("{movement}", "trending").replace("{subject}", "chatter").replace("{security_key}", "BA_US_Equity")
    post[r] = invoke(p, {"tickers": "BA US"} if "timeseries" in p else None)[0]
lost = [r for r in routes if pre["census"].get(r) == 200 and post[r] != 200]; gained = [r for r in routes if pre["census"].get(r) != 200 and post[r] == 200]
print("post_census", len(post), "of 13", "unchanged_status", sum(1 for r in routes if pre["census"].get(r) == post[r]), "of 13", "LOST", lost, "GAINED", gained)
VAL = {"CAT_US_Equity", "CSL_AU_Equity", "6861_JP_Equity"}
CEO = {"ceo_public_profile", "ceo_profile_reading"}
res = {"moved_to_fallback": [], "zero_unchanged": [], "filing_plus_two": [], "OUT_OF_CLASS": []}
for n, a in sorted(pre["management"].items()):
    b = invoke("/api/scoped/amgt/security/%s/thesis" % n)[1].get("management") or {}
    drop = CEO if n in VAL else set()
    if a.get("management_status") == "ABSENT" and a.get("officer_count") == 0 and b.get("management_status") == "SERVED" and b.get("roster_source") == "BLOOMBERG_FALLBACK":
        good = b.get("officer_count", 0) > 0 and b.get("absent_because") is None and b.get("source_accession") is None and str(b.get("source_item", "")).startswith("Bloomberg COMPANY_EXEC_OFFICERS") and (b.get("pool_read") or {}).get("status") == "NOT_READ" and b.get("roster_status") == a.get("roster_status") and b.get("roster_reason") == a.get("roster_reason") and (b.get("ceo_profile_reading") or {}).get("reading") == "NOT_SEARCHED" and (b.get("ceo_profile_reading") or {}).get("urls_returned") is None
        res["moved_to_fallback" if good else "OUT_OF_CLASS"].append("%s:%s" % (n, b.get("officer_count")))
    elif a.get("management_status") == "ABSENT":
        res["zero_unchanged" if (a == b and pre["stored_officers"].get(n) == 0) else "OUT_OF_CLASS"].append(n)
    else:
        extra = [k for k in b if k not in a]
        same = {k: v for k, v in b.items() if k not in ("roster_source", "roster_source_basis") and k not in drop} == {k: v for k, v in a.items() if k not in drop}
        order = list(b)[list(b).index("roster_reason") + 1:list(b).index("roster_reason") + 3] == ["roster_source", "roster_source_basis"] if "roster_reason" in b else False
        res["filing_plus_two" if (sorted(extra) == ["roster_source", "roster_source_basis"] and same and order and b.get("roster_source") == "FILING") else "OUT_OF_CLASS"].append(n)
print("management", len(pre["management"]), "names:", json.dumps({k: (len(v), v) for k, v in res.items()}))
allb = [invoke("/api/scoped/amgt/security/%s/thesis" % n)[1].get("management") or {} for n in pre["management"]]
print("ZERO_OFFICERS_iff_zero", sum(1 for m in allb if (m.get("absent_because") == "ZERO_OFFICERS") == (m.get("officer_count") == 0)), "of", len(allb))
role = pre["Role"]; names = sorted(iam.list_role_policies(RoleName=role)["PolicyNames"])
docs = {n: iam.get_role_policy(RoleName=role, PolicyName=n)["PolicyDocument"] for n in names}
print("role_policy_sha_unchanged", hashlib.sha256(json.dumps(docs, sort_keys=True).encode()).hexdigest() == pre["PolicySha256"], "inline_policies", len(names), "of", pre["InlinePolicies"])
'</invocation><expect>post_census 13 of 13 with unchanged_status 13 of 13, LOST [] and GAINED []; management 15 names at the cut with moved_to_fallback 2 ["6861_JP_Equity:1", "CSL_AU_Equity:14"] (SERVED, roster_source BLOOMBERG_FALLBACK, the real officer count, source_item the Bloomberg label, source_accession None, pool_read NOT_READ, the filing roster_status and roster_reason carried unchanged, CEO reading NOT_SEARCHED with urls_returned None), zero_unchanged 5 [ASML_NA_Equity, HAL_US_Equity, INTU_US_Equity, KMB_US_Equity, PBR_US_Equity] (byte-equal to AC4 AND 0 officers stored -- an ABSENT name with officers stored is OUT_OF_CLASS, so a fallback left unserved cannot hide here), filing_plus_two 8 (every key equal to AC4 but exactly roster_source FILING and roster_source_basis, placed right after roster_reason; for CAT the two CEO keys are set aside because AMGT-rk-75 may re-project its basis in this round) and OUT_OF_CLASS 0 [] -- the class counts are graded against AC4's own pre_classes if the population moved since the cut; ZERO_OFFICERS_iff_zero 15 of 15; role_policy_sha_unchanged True with the same inline policy count. ANY OUT_OF_CLASS name, any LOST route or a moved policy sha is the ROLLBACK BRANCH of section 4</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1-AC4 run BEFORE the deploy (AC4 immediately before step 1); AC5 and AC6 run AFTER step 6 against the LIVE
deployed plane by direct `lambda.invoke`, never a local import.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~77/AMGT_RESAPP.TO-AMGT-rk-77.serve-fallback-roster.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>` (the closed ledger entry and its sentinel travel in this commit). Report
once, naming the pre-act `CodeSha256` and artifact `VersionId` (AC4), the post-act `CodeSha256` (AC5), the AC6 class
counts with the two fallback names' served `officer_count`, `source_item` and `roster_reason`, and the two halves'
sha256 (AC1).

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>19</round>
<slot>~77</slot>
<fabric>site-z</fabric>
