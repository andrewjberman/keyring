# AMGT_RESAPP task order -- `AMGT-rk-37` -- the five missing sheet rows as pulled fields, `CIE_DES` / `CIE_DES_BULK` as the header description, and the Base case (consensus EPS x trailing-median P/E; Upside and Downside ABSENT by ruling)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-37</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~39</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the model-block refresh
  cadence stays Andrew's; the standing collection-stays-off / no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned prefixes (`raw/bloomberg/`,
  `derived/model_block/` in `opal-data-harvest`) under credentials the producer already runs with on this box, and
  redeploys the existing Lambda `opal-amgt-scoped-api` through the existing Terraform resource
  `module.scoped_amgt_api.aws_lambda_function.this` with NO change to its role, policies, layers, memory, timeout or
  environment; it grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~39`, finishing CHAIN M's queue in the SAME worktree: `AMGT-rk-35` (done), `AMGT-rk-36`
(done), `AMGT-rk-37` (this one, last).** Your first act on this order prints `git rev-parse --short=10 HEAD` and confirms
`AMGT-rk-36`'s `<status>` reads `complete` and its change-management entry reads CLOSED; if either is false, STOP with a
row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~39;`. **NEVER RUN AN INSTALL.** **Bloomberg,
ANY scenario: READ `integrations/bloomberg/READ_HERE.md` FIRST.** This order's Bloomberg budget: ONE candidate-probe
`ReferenceDataRequest` on Caterpillar, then one full `pull` per validation name (five requests each after rk-36 --
header, history, three overrides), sixteen requests in all, on the three validation names and NOTHING for any covered
name. **No Seeking Alpha call in this order.**

## 1. THE CELL, inlined in full -- `AMGT-rk-37` (R14-M4; FWD-1, FWD-16; Model brief M5; Lead Panel L8; validation D6, D23; Andrew's card 5 of the six)

**The analysis row, verbatim** (`ledger/ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`, chain M, `R14-M2 -> M3 -> M4`):
*"... M4 the five missing sheet rows and `CIE_DES`/`CIE_DES_BULK` as pulled fields (the header description)"* -- serves
FWD-1, FWD-16, M2-M5, L8; co-sign **yes, each**. **Plus, placed here by the COO at the cut:** the Base case ruling of
`C-MODEL-WINDOW-AND-ROWS` (5) -- a ROWS clause that consumes the `BEST_EPS` FY1 cell `AMGT-rk-36` lands.

**The measured state:**
- *Rows* (Model brief @`f48864fce6` s.1.2 :66-71; `portal/src/pages/SecurityAnalysis/modelSheet.ts:38-59`): of the 17
  declared summary and margin rows, FIVE have `mnemonic: null` and always render ABSENT -- Revenue/Sh (`:39`), FCF
  yield (`:45`), FCF margin (`:48`), RoTA (`:51`), Earnings margin (`:58`). The page correctly refuses to compute them
  (`:13-14`, *"Nothing is derived to fill a row"*); every mnemonic the block carries but the sheet does not name still
  reaches the page through the SUBTRACTION group `OTHER_LINES_TITLE` (`:124-127`).
- *Description* (validation @`b527b93214` D6 :187-188, *"the header field list has no `CIE_DES`, although Bloomberg
  returned it for all three names"*; D23 :227-229; intake L8; PRD `C-DESCRIPTION-LINE`): `HEADER_FIELDS`
  (`model_block_pull.py:57-73`) carries neither `CIE_DES` nor `CIE_DES_BULK`; the reader
  `lib/research/api/scoped_amgt.py:2538-2605 read_description` looks for `DESCRIPTION_HEADER_MNEMONICS = ("CIE_DES",)`
  (`:2261`) on the block's header (`:2559-2573`), else serves sentence 1 of the drafted `company_description`
  UNCONDITIONALLY (`:2574-2592`), else ABSENT naming both probes (`:2593-2605`). Measured on the 12 served names:
  sentence 1 describes the business on 0 of 12 (Boeing: *"Commercial Airplanes revenue was $41,494 million in
  2025..."*; Home Depot: *"Consolidated net sales were $164.7 billion in fiscal 2025."*); CAT in validation:
  *"Construction Industries' total sales were $25.060 billion in 2025..."*.
- *Cases* (`scoped_amgt.py:2500-2508 _model_cases`): all three ABSENT, hard-coded, reason "no cell of this round lands
  them". Andrew ruled ~19:4xZ (frame card 5, `ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`):
  *"Base. I think the upside and downside cases can be discussed on methodology."*

**The PRD constraints this cell serves** (PRD v0.13 @`1699960261`):
- `C-MODEL-WINDOW-AND-ROWS` (`:872-885`), clause (2) verbatim: *"**Five sheet rows have no field today** (Revenue per
  share, FCF yield, FCF margin, return on total assets, earnings margin). The Bloomberg fields that carry them join the
  producer's field list; the page never computes them, and keeps refusing until the field exists."* Clause (5)
  verbatim (`:881-884`): *"**The Base case is consensus EPS x the security's own trailing-median P/E** (v0.12,
  Andrew-direct ~19:4xZ, *"Base."*), each input carrying its source and window. **Upside and Downside stay ABSENT**
  with the reason "methodology to be discussed with Andrew" (...); no seat chooses a spread."*
- `C-DESCRIPTION-LINE` (`:1180-1191`), verbatim: *"The one-line description has three sources, in this order: (1)
  Bloomberg's description field -- `CIE_DES`, else `CIE_DES_BULK` -- added to the model-block pull's header list and
  labelled as Bloomberg's ...; (2) else the first sentence of a VALIDATED drafted `company_description` section,
  marked machine, with its evidence ids, **ONLY if it passes a stated describes-the-business test** -- the test's
  wording is the cut's; (3) else ABSENT, naming every probe. ... the cell adds the field and the test. The adapter
  reads the field by the exact name the pull writes, and the long-text field's shape is measured on a real block
  before the reader is built against it."*
- `C-MODEL-FORECASTS` (`:861-870`): the consensus EPS input is rk-36's `BEST_EPS` FY1 cell, source `BBG` or
  `SA_FALLBACK`, never a reported figure. `C-BLOOMBERG-BASIS` (`:891-895`): basis text beside every new field; no other
  vendor's normalisation reconstructed. `C-UNIT-MAP-MEASURED` (`:848-859`): every new field's unit measured, never
  inferred. `C-VALIDATION-NAMES` (`:1652-1658`). `C-MODEL-WINDOW-AND-ROWS` (4): the yellow key on every call.

**RULED -- what you build:**

1. **The five rows as PULLED fields** (`HIST_FIELDS` `:78-98`, `FIELD_BASIS` `:107-144`, the builder's families in
   `build_unit_map.py`). **You do not type a mnemonic as fact.** For each row, PROBE candidates on `"CAT US Equity"`
   with ONE `reference_data` call carrying every candidate at once: a name Bloomberg does not serve comes back under
   `__field_errors__` (`blp_client.py:201-221`) and is recorded as REFUSED with Bloomberg's own message; a name that
   returns a value is adopted for that row. Candidates to test FIRST (UNVERIFIED unless stated): Revenue/Sh --
   `SALES_REV_PER_SH`, `REVENUE_PER_SH`; FCF yield -- `FREE_CASH_FLOW_YIELD` (the ONE candidate the estate already
   pulls: `lib/research/scores/peers_v.py:74-76` `FIELDS`, cited in the intake s.2C); FCF margin --
   `FREE_CASH_FLOW_MARGIN`, `FCF_MARGIN`; RoTA -- `RETURN_ON_TOT_ASSETS`, `RETURN_ON_TOTAL_ASSETS`; Earnings margin --
   `PROF_MARGIN`, `NET_INCOME_MARGIN`. Add your own candidates from Bloomberg's field definitions if these all refuse,
   and record every one tried. An adopted mnemonic joins `HIST_FIELDS` with a basis sentence (Bloomberg's own
   definition) and a builder family (per-share / percent / ratio, measured on the raw); a row with NO adopted mnemonic
   after the probe stays ABSENT on the page and is recorded in your report with every candidate and its refusal
   message -- that is an honest outcome, and a page still refusing to compute it is the correct one. **Nothing is
   derived from other rows, anywhere** (not in the producer, not in the adapter, not on the page).
2. **`CIE_DES` and `CIE_DES_BULK` as header fields** (`HEADER_FIELDS` `:57-73`), basis text "Bloomberg's company
   description (long text) / bulk description", TEXT family in the builder (a string is a MEASURED text unit, as
   `NAME` is). **MEASURE THE SHAPE FIRST** (PRD :1190-1191): print `type()` and length of what the client returns for
   each on CAT's raw `refdata.json` -- a bulk field may come back as a LIST of row dicts (`_el_to_py`), and the derive
   must then persist the joined text (rows in order, single spaces) as the header figure's `value`, with the raw shape
   preserved in the raw landing. Reader: `DESCRIPTION_HEADER_MNEMONICS = ("CIE_DES", "CIE_DES_BULK")` in that order
   (`:2261`) -- `CIE_DES` else `CIE_DES_BULK`, the served `source` naming which (`"bloomberg CIE_DES"` /
   `"bloomberg CIE_DES_BULK"`), `field` the exact mnemonic the pull writes.
3. **The describes-the-business test -- THE CUT'S WORDING, stated here and recorded in the code's docstring and on the
   served object as `describes_business_test: {passed, rule, failed_on}`:** a drafted sentence PASSES only if ALL
   three hold: (a) it contains NO amount or magnitude token -- none of `$`, `USD`, `EUR`, `JPY`, `GBP`, `AUD`,
   `million`, `billion`, `trillion`, `%`, `percent` -- and NO four-digit year; (b) it contains a business-descriptor
   phrase from this fixed list (folded, whole words): `is a`, `is an`, `is the`, `operates`, `provides`, `manufactures`,
   `develops`, `designs`, `engages in`, `offers`, `sells`, `produces`, `supplies`; (c) it contains none of the
   measure phrases `revenue`, `net sales`, `sales were`, `income was`, `margin was`. **Three planted negatives, each
   the PRD's or the validation's own measured sentence, MUST FAIL:** Boeing's, Home Depot's and CAT's sentences quoted
   above. **One positive MUST PASS:** *"Caterpillar Inc. is the world's leading manufacturer of construction and mining
   equipment, off-highway diesel and natural gas engines, industrial gas turbines and diesel-electric locomotives."* A
   failing sentence is NOT served; the object goes to (3) ABSENT with `probes: [{probe: "header CIE_DES", result},
   {probe: "header CIE_DES_BULK", result}, {probe: "drafting company_description sentence 1", result:
   "FAILED describes-the-business test", failed_on: <a|b|c>}]` -- every probe named. The route ORDER is the PRD's
   (Bloomberg first, then the tested sentence, then ABSENT) -- read `C-DESCRIPTION-LINE` at your worktree's HEAD before
   you write it; if its order has moved again, the PRD wins and you say so in your report.
4. **The Base case, on the BLOCK at derive** (the producer computes once; the adapter serves; the page never
   computes): `cases.base = {status: "SERVED", value: consensus_eps_fy1 x trailing_median_pe, formula: "consensus EPS
   (FY1) x trailing-median P/E", inputs: {consensus_eps: {value, mnemonic: "BEST_EPS", fiscal_period: "FY1",
   fiscal_year, period_end_date, source: "BBG"|"SA_FALLBACK"}, trailing_median_pe: {value, mnemonic: "PE_RATIO",
   window: [<the CLOSED fiscal years on this block carrying a numeric PE_RATIO>], n, source: "bloomberg-dapi"}},
   px_last: {value, mnemonic: "PX_LAST", vintage}}` -- `px_last` is CARRIED as context (the sheet's case reads
   EPS x multiple -> price -> return), NOT used to compute a return here: the ruling names a price, and a return is a
   derivation no seat was given. The median is over every closed year with a numeric `PE_RATIO` as Bloomberg reports
   it (its own basis, `C-BLOOMBERG-BASIS`; no floor on `n` is invented -- `n` is printed). ABSENT with its reason when
   there is no `BEST_EPS` FY1 figure (`"no consensus EPS on the landed block"` -- every covered name until its next
   pull) or no `PE_RATIO` history (`"no PE_RATIO history on the landed block"`). `cases.upside` and `cases.downside`
   are ALWAYS `{status: "ABSENT", reason: "methodology to be discussed with Andrew"}` -- that exact string.
5. **The adapter** (`_model_cases()` `:2500-2508`, called from `read_model` `:2532`): serves the block's `cases.base`
   as landed (SERVED with inputs, or ABSENT with the block's reason; a block with no `cases` key -- the 33 -- serves
   base ABSENT with reason `"no cases on the landed block (derived before C-MODEL-WINDOW-AND-ROWS (5))"`), and serves
   `upside` and `downside` ABSENT with the exact ruling reason **REGARDLESS of what the block carries** -- a number a
   block somehow carries in `cases.upside` is NEVER passed through (the planted negative in AC2). `read_description`
   as in items 2-3.
6. **NOT IN THIS CELL:** `modelSheet.ts`'s five `mnemonic: null` rows and the cases render on the page -- the portal is
   frozen and not on this order's surface; the new fields reach the page under "Other lines the block carries"
   (`modelSheet.ts:124-127`) until a portal cell maps them; named for the COO.
7. **The act, in order:** the CAT probe (item 1); `pull` then `derive` on exactly `"CAT US Equity" "CSL AU Equity"
   "6861 JP Equity"`; the tests (AC2); the deploy (section 3). **The 33 covered names are NOT pulled and NOT
   re-derived**; after the deploy their served `description` follows the new order and test (the 12 drafted names'
   segment sentences now FAIL the test and read ABSENT naming every probe -- the v0.12 measured "0 of 12", now on the
   served plane, which the never-widen pair names as the blast radius) and their `model.cases.base` reads ABSENT with
   the no-cases reason.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 chain M row `R14-M4` and s.5 card 2
@`9c8e04cd9a`, ANSWERED by Andrew ~19:4xZ (frame card 5, *"Base. ..."*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`); Model brief
@`f48864fce6` s.1.2, s.3, s.5 items 4 and 6, s.6 "Rows", s.7 (*"Do not compute missing rows on the page"*); Lead Panel
L8 and `4.0.0_SA_CRO~Z`'s L4-R correction of the description order (msg 23744); validation D6, D23. PRD **v0.13
@`1699960261`** (`C-MODEL-WINDOW-AND-ROWS` (2) and (5) :872-885; `C-DESCRIPTION-LINE` :1180-1191 as corrected at v0.12;
`C-MODEL-FORECASTS` :861-870). Code cited @HEAD (draft-time HEAD `8a788d2eaf`; `scoped_amgt.py` last touched
`e2d89be7da`; rk-34/35/36 will have moved `model_block_pull.py`'s and `scoped_amgt.py`'s line numbers -- re-read at spawn).

**ISSUER RULE -- ADAPTER SINGLE-WRITER QUEUE (`2.0.0_SA_COO~Z`, at the cut):** this order is one of the round-14 cells
that edit `lib/research/api/scoped_amgt.py` and/or redeploy `opal-amgt-scoped-api` (rk-36, rk-37, rk-43, rk-45, rk-53,
rk-61). The issuer spawns those cells ONE AT A TIME -- the next is cut from HEAD only after the previous has DRAINED --
so a worktree never carries adapter bytes behind the shared branch. Two obligations follow. (1) IMMEDIATELY BEFORE
`build-and-upload-scoped-amgt.sh`, run `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api
lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
and paste its output into the change-management entry: it MUST print nothing; if it prints a commit, STOP -- do not
build, do not apply -- file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and report; a deploy from bytes behind the
shared branch would REWIND another cell's served change. (2) The rollback target is the pre-act `CodeSha256` and the
artifact `VersionId` YOU read immediately before the apply (never a value copied from another order), recorded in the
entry before the build runs. THE ROLLBACK MECHANISM, as RULED on `1.0.0_SA_CTO~Z`'s source read (msg 23830): the Terraform
module (`infra/aws/terraform/modules/yang-lambda/main.tf:17-20`, `:38`) declares `data "aws_s3_object" "artifact"` with
bucket and key only and ALWAYS resolves the CURRENT version, so a rollback NEVER edits the module and never names a
VersionId to Terraform. Rollback = restore the pre-act bytes as the current version -- `aws s3api copy-object --bucket
opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source
"opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<pre-act VersionId>"` (bucket versioning
MEASURED `Enabled` by the issuer 2026-09-18 ~22:4xZ; RE-MEASURE it with `get-bucket-versioning` into the entry before the
build, and STOP if it reads anything else) -- then the SAME targeted `safe-apply`, and `get-function-configuration` must
print the pre-act `CodeSha256` again. Exercise nothing of this unless rolling back; record all of it before acting.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain M is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-37`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-37` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-37.sheet-rows-description-base-case.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (`modelSheet.ts`, `peers_v.py`, `blp_client.py`,
  the pool, the drafting store); this block governs WRITES. `portal/` is READ-ONLY to you. New tests:
  `lib/research/api/tests/test_description_line.py` and `lib/research/api/tests/test_model_cases.py`. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~39 <0.9.0_WK_AMGT_RESAPP~39@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **THE DEPLOY -- served output moves for the 33, so this is co-signed and its blast radius is WIDER than rk-36's.**
  Stated so the pair can name it: (i) `description` for every keyed name: the 12 names with a drafted
  `company_description` move from a served segment sentence to ABSENT-naming-every-probe unless the sentence passes
  the test (measured 0 of 12 pass); the 21 without drafting keep ABSENT with the probes now listed; NO covered name
  gains a Bloomberg description until its next pull (`CIE_DES` is not on their raw); (ii) `model.cases`: `base`
  ABSENT with the no-cases reason for all 33; `upside`/`downside` ABSENT with the ruling reason (the reason text
  changes from the round-13 text); (iii) `check_face` length for the 33 UNCHANGED; (iv) the three validation names
  unserved. Writers of the Lambda's bytes: ONE (the build script packaging THIS worktree). ROLLBACK from the LIVE
  pre-act hash of THIS act: pre-act `CodeSha256` and artifact VersionId recorded, the rk-2 rollback record as the
  precedent. **THE STALE-BYTES CHECK, NON-NEGOTIABLE, exactly as rk-36's:**
  `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  must be EMPTY or you STOP and file a row naming the commits (the COO merges forward; you never merge). Then the halt
  gate's session file (`AMGT-ri-2` `:22`), the entry OPENED BEFORE the build:
  `python .tools/deploy_ledger.py open --slug amgt-rk37-rows-description-base-case-20260918 --title "AMGT-rk-37: five sheet-row fields + CIE_DES/CIE_DES_BULK pulled; description order and describes-the-business test; Base case served, Upside/Downside ABSENT by ruling; co-signed rk-37 pair" --author 0.9.0_WK_AMGT_RESAPP~39 --leg "L1|git|producer fields + reader + cases + tests committed|commit hash" --leg "L2|activation|module.scoped_amgt_api.aws_lambda_function.this redeployed|TF apply 0 destroy + 0-diff replan + deployed CodeSha256 == uploaded sha" --leg "L3|verify|13 of 13 GET routes 200 pre/post, LOST=[] GAINED=[]; AC4; the 12 drafted names' description status listed pre/post|census + AC4 output" --window-hours 4`
  with its sentinel COMMITTED; the build `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`; the apply
  in the byte-exact form of the rk-19 SESSION_LOG `:43-65` / rk-30 record (`HALT_ACK=1`, `.tools/safe-apply.sh`,
  `-target=module.scoped_amgt_api.aws_lambda_function.this`) -- NEVER bare `terraform apply`, NEVER
  `aws lambda update-function-code`; the 13-route census pre and post; CLOSE with every leg proven before your grading read.

## 4. BOUNDS

**BLOOMBERG:** sixteen requests, all on the three validation names (one probe on CAT, five per name in the pull);
none on a covered name; every call yellow-keyed. **No Seeking Alpha call, no other vendor call.** **PORTAL FROZEN**
(read-only; item 6). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.**
No Terraform change beyond the targeted apply of the existing resource; no IAM. No non-ASCII in anything you write.
**PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. A row whose every candidate mnemonic Bloomberg
refuses is REPORTED, not computed; an Upside or Downside NUMBER served anywhere is a FAIL of this order, whatever its
source; a description sentence served past a failing test is a FAIL.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** (12 drafted names, 33 keyed, 17 sheet
rows, 5 target rows).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W39-S<k>`, `<k>` continuing from rk-36; `"project": "AMGT_RESAPP"` and `"fabric":
"site-z"`; textual splice, never re-serialize, never edit an existing row. **Found something off-task? APPEND ONE ROW AND
KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-37"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, importlib.util as u
s = u.spec_from_file_location('m', 'integrations/bloomberg/research/model_block_pull.py'); m = u.module_from_spec(s); s.loader.exec_module(m)
ROWS = json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/row_mnemonics.json', encoding='utf-8'))
print('row_map', json.dumps(ROWS, sort_keys=True))
print('CIE_in_HEADER_FIELDS', [x for x in ['CIE_DES', 'CIE_DES_BULK'] if x in m.HEADER_FIELDS], 'adopted_in_HIST_FIELDS', [v['mnemonic'] for v in ROWS.values() if v.get('mnemonic') and v['mnemonic'] in m.HIST_FIELDS])
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    b = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read()) if ks else {}
    figs = b.get('figures') or []
    hdr = {f['mnemonic']: f for f in figs if f.get('scope') == 'header'}
    desc = [(x, len(str(hdr[x].get('value')))) for x in ['CIE_DES', 'CIE_DES_BULK'] if x in hdr and str(hdr[x].get('value')).strip()]
    raw_stamp = b.get('raw_stamp_used'); ref = json.loads(s3.get_object(Bucket=B, Key='raw/bloomberg/' + k + '/' + str(raw_stamp) + '/refdata.json')['Body'].read()) if raw_stamp else {}
    rawrow = ref.get(b.get('security')) or {}
    print(k, 'block', ks[-1] if ks else None, 'description_scalars', desc, 'raw_shape', [(x, type(rawrow.get(x)).__name__) for x in ['CIE_DES', 'CIE_DES_BULK'] if x in rawrow], 'raw_field_errors', sorted((rawrow.get('__field_errors__') or {}).keys()))
    for row, v in sorted(ROWS.items()):
        mn = v.get('mnemonic')
        vals = [f for f in figs if f.get('scope') == 'fiscal_year_line_item' and f.get('mnemonic') == mn] if mn else []
        print('  ', row, 'mnemonic', mn, 'fiscal_values', len(vals), 'refused_candidates', v.get('refused'))
"</invocation><expect>THE FIELDS, MEASURED ON THE THREE VALIDATION NAMES: row_mnemonics.json (written by you from the CAT probe, one entry per target row: Revenue/Sh, FCF yield, FCF margin, RoTA, Earnings margin -- each with the adopted mnemonic or null, and refused = every candidate tried with Bloomberg's own field-error message) is printed; CIE_in_HEADER_FIELDS lists both; each of the three blocks carries at least one non-empty description scalar (CIE_DES or CIE_DES_BULK with its text length -- D6 measured Bloomberg returns it for all three) and raw_shape names the type the client returned for each (the shape measured BEFORE the reader was built); for every row with an adopted mnemonic, fiscal_values is greater than 0 on at least one of the three names and the mnemonic appears in HIST_FIELDS (a PULLED field, never derived); a row with null carries a non-empty refused list. A description missing on a validation name, an adopted row with 0 values on all three, or a null row with no refusal recorded is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-37"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest -q lib/research/api/tests/test_description_line.py lib/research/api/tests/test_model_cases.py -p no:cacheprovider 2>&1 | tail -25</invocation><expect>THE PLANTED CASES, OFFLINE: test_description_line.py asserts the describes-the-business test FAILS all three measured negatives verbatim -- Boeing (Commercial Airplanes revenue was $41,494 million in 2025...), Home Depot (Consolidated net sales were $164.7 billion in fiscal 2025.), CAT (Construction Industries' total sales were $25.060 billion in 2025...) -- naming the sub-rule each failed on; PASSES the Caterpillar positive sentence in section 1 item 3; and, through read_description on fixture blocks, serves a Bloomberg CIE_DES first when present, CIE_DES_BULK when only it is present (source naming the field), a drafted sentence ONLY past the test, and otherwise ABSENT with all three probes named. test_model_cases.py asserts _model_cases serves the block's base as landed (SERVED with inputs and window; ABSENT with the block's reason; ABSENT with the no-cases reason for a block without cases) and -- THE PLANTED NEGATIVE -- a fixture block whose cases.upside carries {status: SERVED, value: 123.0} is STILL served as upside ABSENT with reason methodology to be discussed with Andrew, and the same for downside. The tail shows N passed, 0 failed, 0 errors -- print the line. Any failure, or a served upside number, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-37"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import sys, json, statistics
sys.path.insert(0, '.')
from lib.research.api import scoped_amgt as a
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    blk = a.read_model_block(k)
    if not blk:
        print(k, 'NO_BLOCK'); continue
    d = a.read_description(k, identity={'security_key': k}, model_block=blk)
    print(k, 'description', d.get('status'), 'source', d.get('source'), 'field', d.get('field'), 'text_len', len(d.get('text') or ''), 'test', d.get('describes_business_test'), 'probes', d.get('probes'))
    m = a.read_model(k, identity={'security_key': k}, model_block=blk); c = m.get('cases') or {}
    figs = blk.get('figures') or []
    pes = [float(f['value']) for f in figs if f.get('scope') == 'fiscal_year_line_item' and f.get('mnemonic') == 'PE_RATIO' and isinstance(f.get('value'), (int, float))]
    eps = [f for f in figs if f.get('scope') == 'forecast' and f.get('mnemonic') == 'BEST_EPS' and f.get('fiscal_period') == 'FY1']
    recomputed = (float(eps[0]['value']) * statistics.median(pes)) if eps and pes else None
    base = c.get('base') or {}
    print('  base', base.get('status'), 'value', base.get('value'), 'recomputed', recomputed, 'agree', (recomputed is not None and base.get('value') is not None and abs(float(base['value']) - recomputed) < 1e-6), 'inputs', json.dumps(base.get('inputs'), sort_keys=True), 'reason', base.get('reason'))
    print('  upside', (c.get('upside') or {}).get('status'), repr((c.get('upside') or {}).get('reason')), 'downside', (c.get('downside') or {}).get('status'), repr((c.get('downside') or {}).get('reason')))
"</invocation><expect>THE ADAPTER, IN-PROCESS BY KEY, ON THE THREE VALIDATION NAMES (they are not in the crosswalk, so the served route cannot reach them yet; read_model_block/read_description/read_model read the pool by key exactly as the Lambda does): description reads SERVED with source bloomberg CIE_DES or bloomberg CIE_DES_BULK and field the exact mnemonic (route (1) wins; no drafting exists for these names), probes listed; base reads SERVED with value equal to the INDEPENDENT recomputation in this invocation (agree True: BEST_EPS FY1 from the block's own forecast figures x the median of the block's own PE_RATIO fiscal values -- a different instrument than the producer's code path) and inputs carrying consensus_eps {value, fiscal_year, period_end_date, source} and trailing_median_pe {value, window, n, source}; where a name has no BEST_EPS FY1 (rk-36's AC3 may have left a gap) base reads ABSENT with the no-consensus-EPS reason and agree is not required; upside and downside read ABSENT with reason exactly 'methodology to be discussed with Andrew' on all three. A base that disagrees with the recomputation, a base SERVED without its window, or any upside/downside not ABSENT with that exact string is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-37"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
cfg = lam.get_function_configuration(FunctionName='opal-amgt-scoped-api'); print('CodeSha256', cfg.get('CodeSha256'), 'LastModified', cfg.get('LastModified'))
for key in ['BA_US_Equity', 'HD_US_Equity', 'HOLLOW_NONEXISTENT_KEY_Equity']:
    payload = json.dumps({'rawPath': '/api/scoped/amgt/security/' + key + '/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
    body = json.loads(resp['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    hp = json.dumps({'rawPath': '/api/scoped/amgt/security/' + key + '/header', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    hb = json.loads(lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=hp)['Payload'].read())
    hi = json.loads(hb.get('body', '{}')) if isinstance(hb.get('body'), str) else hb.get('body', {})
    d = hi.get('description') or {}; c = (inner.get('model') or {}).get('cases') or {}
    print(key, 'thesis', body.get('statusCode'), 'header', hb.get('statusCode'), 'description', d.get('status'), 'source', d.get('source'), 'test', (d.get('describes_business_test') or {}).get('passed'), 'probes', len(d.get('probes') or []), 'text_head', (d.get('text') or '')[:60])
    print('  base', (c.get('base') or {}).get('status'), (c.get('base') or {}).get('reason'), 'upside', (c.get('upside') or {}).get('status'), repr((c.get('upside') or {}).get('reason')), 'downside', (c.get('downside') or {}).get('status'), 'check_face_len', len(inner.get('check_face') or []))
"</invocation><expect>THE SERVED PLANE AFTER THE REDEPLOY (post-act CodeSha256 printed, equal to the uploaded artifact's sha in the change-management entry; read the header route's exact rawPath from the 13-route census you ran pre-deploy and correct it here if the route name differs -- the description travels on the header payload, scoped_amgt.py:1895-1899): BA_US_Equity and HD_US_Equity -- the PRD's two measured negatives -- answer 200 on both routes with description ABSENT, test passed False, probes 3 (every probe named) and NO segment-sales text served (text_head empty), because their drafted sentence fails the describes-the-business test and their 2026-09-16 raw carries no CIE_DES; base ABSENT with the no-cases reason (they were derived before this order and are NOT re-derived); upside and downside ABSENT with reason exactly 'methodology to be discussed with Andrew'; check_face_len equal to each name's PRE-DEPLOY value you recorded. The PLANTED NEGATIVE HOLLOW_NONEXISTENT_KEY_Equity serves description ABSENT and every case ABSENT. A served segment sentence, a served case number, or a moved check_face length is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1 and AC3 run after the derive lands; AC2 before the deploy; AC4 only AFTER the redeploy, against the LIVE deployed
plane. Your report ALSO lists, for the 12 drafted names, `description.status` and `source` PRE and POST deploy (the
blast radius the pair named, measured).

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/AMGT_RESAPP.TO-AMGT-rk-37.sheet-rows-description-base-case.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); the change-management entry
CLOSED with all three legs proven and its sentinel removal committed; flip `<status>` to `complete`; commit with
`--only -- <paths>`. This is the LAST order of your queue: report once, naming: the sixteen Bloomberg requests; the
row-to-mnemonic map with every refusal message; the measured shape of `CIE_DES` / `CIE_DES_BULK`; the test's wording as
committed; the pre/post CodeSha256, the 13-route census, and the 12 drafted names' description status pre/post; the
rows filed across the whole queue.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~39</slot>
<fabric>site-z</fabric>
