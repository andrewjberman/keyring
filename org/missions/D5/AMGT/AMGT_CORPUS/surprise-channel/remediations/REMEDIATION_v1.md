# AMGT_CORPUS -- surprise channel, REMEDIATION v1 -- RECONCILIATION of every graduated item carried without a row since round 2

Author: 3.0.0_SA_CVO~Z. Round: v41 (round 35). Fabric: site-z. Recorded: 2026-10-04T21:2xZ. **Reader:** `1.0.0_SA_CTO~Z`.

**What it reconciles.** The project had no remediation file. Every GRADUATED item's disposition lived only in prose tables in
ADJUDICATION_v1..v41, which `comp-surprise` cannot read: at 20:3xZ it counted 39 ARMED. `.tools/surprise-row-gate.py` refused the
three round-35 disarm rows while 95 graduated items had none. This file carries one row per item: the gate's 95 plus Z-S85, Z-W1-S29
and Z-W1-S30, which round 35 disarmed (ADJUDICATION_v41 section 3). That is 98 rows.

**Result:** 96 REMEDIATED (39 of them ARMED items now DISARMED, each `at` the UTC commit time of the fixing commit) and 2 OPEN:
- `Z-W4-S4` -- `lib/research/corpus/induction_request.py:60` still hard-codes `DELIVERABLES_DIR`, and the run writes its request file on
  every path, including `--pick`. A read-only mode, an output-directory argument or an access-grant ruling is still owed (ADJUDICATION_v8
  left it to whoever next cuts that cell).
- `Z-S86` -- the DE_US_Equity thesis/peers 404. The RESAPP fix (AMGT-aq-4) passes locally, but its redeploy order AMGT-aq-5 is still
  pending, and the deployed function reads FAIL.

**How each verdict was reached.** The items were split into four batches and drafted by read-only subagents of this seat. Each verdict
rests on one of:
- a fixing commit confirmed as an ancestor of HEAD;
- a path:line at HEAD;
- a task order's LAST `<status>`;
- a superseding row.

A record or observation that owes no act closes as "No act owed", citing the commit or ruling that settled it. This seat validated
all 98 rows against `org/surprise_channel/schemas/remediation_row.schema.json` (0 errors). It spot-checked 6 rows by re-running their
ancestry and reading their cited lines, and 2 more by line (`model_block_pull.py:943-947`, `test_induction_run.py:25-28`). All held.

**Where a fix landed but has never run, closed as REMEDIATED on the landed fix:**
- `Z-S62`: no conflicted `safe-merge --continue` has run since its fix.
- `Z-S75`: `assembled.harness.cjs` cannot run at portal DEV because of an unrelated missing module alias.

**Where the remedy differs from the one the row proposed:**
- `Z-S15`: an autouse fixture redirects `DELIVERABLES_DIR` instead of adding a parameter. It removes the same cause.
- `Z-W2-S8`: the row's premise was already false when it was filed (`PROOF_OF_SPEC.schema.json:253` has carried `judgment` since
  b4299fa5aa).

**Owner:** the row's `disarm_owner` where it was a serial; the leading serial where it was prose; `2.0.0_SA_COO~X` where it was absent.

```json
[
 {
  "id": "AMGT_CORPUS-Z-S10",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-c-11 AC3's literal invocation pipes the code census through `tail -30`, but the census now prints 32 lines (files_scanned, write_like_calls, 27 flagged-call lines, library_write_calls, positive_control flagged, positive_control_path), so the two header lines fall outside the window and AC3's own regex, which requires `files_scanned` BEFORE `library_write_calls 0`, cannot match the literal command's output while every value it grades is correct.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S10",
   "4c50cbc076 drain(AMGT_CORPUS.TO-CRPS-c-11): order closed complete on the issuer's own execution with the amended AC3 read",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-11.read-only-proof.md:107 AC3 invocation reads `| tail -40` at HEAD; :128 records the tail -30 -> tail -40 amendment",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-11.read-only-proof.md:141 last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v5.md:26 Z-S10 GRADUATED"
  ],
  "remedy": "Issuer amended CRPS-c-11 AC3's invocation window from tail -30 to tail -40 with the expect unchanged; the order closed complete, no act owed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S15",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The induction_batch_2026-09-24.json the d-5 worker COMMITTED in its deliverables dir (@7e1f39f327, drained @71e2409a43) is a TEST FIXTURE, not the dry run's artifact: it carries 'Registered Co' / 'Already Co' / 'Refused Co', because induction_run.run() writes the batch file into the hard-coded DELIVERABLES_DIR (:341-343 at 71e2409a43) and the tests call run(), so the last test to run overwrote the dry run's 20 real requests before the commit. The 11:09Z fire overwrote it again with the real 20; that as-fired list is kept at deliverables/2.0.0_SA_COO~X/evidence/induction_batch_2026-09-24_as_fired.json and the worker's committed copy is restored to HEAD bytes, so a reader of the drained tree sees a fixture where the record face promises the dry run's request list.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S15",
   "972d9a0e81 (CRPS-j-2) carries the autouse _redirect_deliverables_dir fixture in lib/research/corpus/tests/test_induction_run.py",
   "lib/research/corpus/tests/test_induction_run.py:25-28 autouse fixture monkeypatches induction_run.DELIVERABLES_DIR to tmp_path at HEAD",
   "lib/research/corpus/induction_run.py:97-98 docstring at HEAD: run() and write_readback() write under DELIVERABLES_DIR (tests redirect that constant)",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v5.md:30 Z-S15 GRADUATED as enrichment item 4"
  ],
  "remedy": "Tests no longer write the real deliverables dir: an autouse fixture redirects DELIVERABLES_DIR to tmp_path, so a test run cannot overwrite the committed batch file.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S19",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by its owner of AMGT_CORPUS-Z-S16 (the post-fire exposure: 20 twin records, 0 of 20 folders ingested): all three disarm conditions the row states are MET -- (1) the builder resolves a registration into its same-folder UNRESOLVED coverage record in place (2.0.0_SA_COO~Z @a2b84a1b2a, drained a5b9859e0a, crosswalk.py byte-identical at HEAD); (2) ONE re-mint of crosswalk/v1/2026-09-24.json through the unified builder under a fresh never-widen pair (COO 5de984f360, CTO #2 839b04a16c, in force 6236af5af4; CTO R-63 closes it): versions 23 -> 24, records 274 -> 254, MEASURED 214 with 214 of 214 keys present, UNRESOLVED 60 -> 40, resolved_folders 20, multi-claimed forms 0 of 521; (3) the re-ingest read resolved_folders 53 (stored 218, put_performed 94, AMBIGUOUS 0) and the production sequence ran for the 20 -- extraction v1+v2, typed, continuation (names 53, rebuilt 20), fund form, typecast, and dossiers (names 53, written 36 incl. all 20 new keys, existed 17) after the backlog scan vintage was re-minted (93 = 53 + 40 + 0). Z-S16 is legacy-shaped (no disarm clock) so it cannot advance in place; this row is the disarm carrier and cites it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S19",
   "a2b84a1b2a closer(crosswalk): a registration resolves its same-folder UNRESOLVED coverage record in place (disarm condition 1)",
   "a5b9859e0a drain(0.0.0_AB_MSTR~Z): a2b84a1b2a merged into CLOUD; ancestor of HEAD",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v5.md:31 Z-S16 GRADUATED, disarmed by Z-S19; :33 Z-S19 GRADUATED as the carrier"
  ],
  "remedy": "No act owed: this row is the owner's evidence-cited disarm carrier for Z-S16, and its three conditions were verified at L9.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S24",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "16 of the 40-name fire's folders are resolved in the served crosswalk but INVISIBLE to the corpus ingest: every folder whose registration ENRICHED an existing no-folder universe record lost its own association form. The ENRICH attach (crosswalk.build_crosswalk, @9ec1226a01 limb (a)) RETIRES the folder's UNRESOLVED coverage record, and that record was the only one carrying the folder's 'security-<hash>' form; the enriched record keeps only the universe side's forms (V_US_Equity: ['V_US', 'V_US_Equity']), while an APPENDED record keeps it (ADBE_US_Equity: ['ADBE_US', 'ADBE_US_Equity', 'security-37dddff4d4357038']). The ingest resolves a folder by that form, so it read resolved_folders 73, not 89.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S24",
   "74e6a76e5c closer(AMGT_EXPERIENCE identity): an ENRICH carries the folder's own association form (the retired record's forms move onto the enriched record)",
   "b58d5c1d53 closer: an ENRICH attach adds the folder's own form even with nothing to retire",
   "lib/research/identity/crosswalk.py:727-729 and :857-866 at HEAD: ENRICH retires the UNRESOLVED record and carries its association_keys onto the enriched record",
   "f95a8d22e8 surprise(AMGT_CORPUS-Z-S30, Z-S31): the re-ingest reads 94 of 94 folders resolved with 0 unresolved files, so Z-S31 disarms Z-S24",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v6.md:55 Z-S24 GRADUATED; :130 verified at 235 of 235 keyed and UNRESOLVED 0"
  ],
  "remedy": "The ENRICH attach now moves the retired UNRESOLVED record's association forms onto the enriched record; the re-mint and re-ingest read 94 of 94 folders resolved.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T02:17Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S28",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CORRECTION TO AMGT_CORPUS-Z-S27, filed as a new row because the channel is append-only: the Bloomberg credential was NEVER TESTED. Neither fill-failure mode applies, the login dialog carries NO error an hour and a quarter after the second submit, and the two 'spent' attempts were spent in OUR LEDGER and not necessarily at the vendor -- so the remaining act is ONE HUMAN CLICK on an already-filled form, not a sign-in.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S28",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v8.md:47-48 Z-S28 stands as the record of the budget-clock correction and graduates as record-only",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v8.md:39-40 Z-S32 reports 8194 LISTENING=1; Z-S27's blocking cause cleared"
  ],
  "remedy": "No act owed: the row is the CTO's record-only correction of Z-S27's budget-clock claim, and its substance is no longer live because the listener is up.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S32",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE RE-MINT RAN AND ITS SIGNED RADIUS HELD ON EVERY LIMB, verified by the SIGNER against S3 rather than taken from the runner: exactly ONE put on the new key, the prior key untouched at 25 versions, and exactly FIVE raw landings which are exactly the five NAMED securities. The served crosswalk now carries 94 folders with 235 of 235 records MEASURED and 0 UNRESOLVED, closing Z-S25's '89 of 94'. Z-S27's blocking cause is CLEARED.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S32",
   "c79872b0ff fire(AMGT_CORPUS re-mint): the ONE run under the re-mint pair",
   "f95a8d22e8 surprise(AMGT_CORPUS-Z-S30, Z-S31): the re-ingest reads 94 of 94 folders resolved with 0 unresolved files",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v8.md:39-40 Z-S32 closed on evidence (8194 LISTENING=1, live Bloomberg call in round 5)"
  ],
  "remedy": "No act owed: the re-mint held its signed radius, and the one limb the row left unmeasured (re-ingest of all 94) was read 94 of 94 resolved.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S36",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The dossier composer never reads the derived Model block: all 94 dossiers written 2026-09-25 by the round-4 sequence carry 9,471 model_rows with 0 values, 0 of 94 list a derived/model_block object among their inputs (extract, continuation and typecast only), and every row's absent reason reads 'Bloomberg figure pull not authorized (R-16 V3)' (dossier.py:117) -- a hard-coded reason that is now FALSE: the pull was authorized (Andrew @16ee7f6373, R-21) and 89 of 89 blocks are served (Z-S33). FWD-12's served Model tab is realized; its dossier half is not, and the dossier states a false reason for the gap.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S36",
   "9162530ba0 worker(AMGT_CORPUS.TO-CRPS-g-2): dossier model_rows reads the newest derived Model block per row",
   "lib/research/corpus/dossier.py:40-45 at HEAD: figures read from the NEWEST derived Model block; the constant not-authorized reason is retired",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-2.dossier-model-rows-from-block.md last <status> is complete",
   "e38a806050 packet(AMGT_CORPUS round 5): carries Z-S38, the disarm of Z-S36 on the served dossiers",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v8.md:24 Z-S36 GRADUATED, disarmed by Z-S38: 3,772 of 9,183 model_rows carry a value, 0 stale reasons"
  ],
  "remedy": "dossier model_rows now reads the newest derived Model block and derives absent reasons from the block; the rewrite served 3,772 of 9,183 rows with a value and 0 stale reasons.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-26T00:33Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S42",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM BY HOLD of AMGT_CORPUS-Z-S41 by its owner: this seat runs NO dossier --write (no production sequence, no single-name write) until CRPS-h-1 drains and its census reads 'read_dossier serves the last write N of N' with 'rewrites_on_unchanged_inputs' unchanged across a --write of one name. The writer census is this seat alone: every dossier write in the table's history came from this seat's production sequences (evidence/production_sequence_*.log) and no scheduled producer writes the table.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S42",
   "0ffe50d118 drain+row(AMGT_CORPUS round 6 h-1 exercised arm, AMGT_CORPUS-Z-S44): dossier --write twice printed unchanged; lifts the hold",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-1.dossier-newest-is-last-write.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v9.md:19 Z-S42 GRADUATED, the hold lifted by Z-S44"
  ],
  "remedy": "No act owed: the owner's dossier-write hold was lifted by Z-S44 after CRPS-h-1 drained and read_dossier served the last write 95 of 95.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S46",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM BY HOLD of AMGT_CORPUS-Z-S45 by its owner: this seat runs NO continuation --write (and so no h-5 served rewrite and no dossier rewrite for it) until the continuation readers prefer the current method version. The writer census is this seat alone: continuation --write has only ever run in this seat's production sequences, and no scheduled producer writes the table.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S46",
   "0dab2c4cdc surprise(AMGT_CORPUS-Z-S45..S46): the hold filed",
   "cf9f8dce71 ledger-close(AMGT_CORPUS round 7 act B step 2): rewrite landed 95 of 95, stale_pick 0; row Z-S49 lifts the hold",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v10.md:43 Z-S46 GRADUATED with Z-S45; :119 continuation_pick 95 current_method_available 95 stale_pick 0"
  ],
  "remedy": "No act owed: the continuation-write hold ended once the readers preferred the current method version; the pick census read 95 of 95 on /2.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S54",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "LIFT of AMGT_CORPUS-Z-S53 by its owner, and Z-W1-S9's close condition MEASURED MET: the dossier rewrite ran under the signed pair (COO b98e09953e, CTO 9ffd945889) with the table-aware case rule (CRPS-k-1 @19458b6130); every served case is its own columns of the team's scenario table with unit and page citation, and no served case is a heading or a table dump. Closing adjudication is the CVO's at L9 (AC3).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S54",
   "19458b6130 drain(AMGT_CORPUS round 9 CRPS-k-1): each case serves its own columns of the team's scenario table",
   "fd44f203a6 ledger-close(AMGT_CORPUS round 9 dossier rewrite): LANDED 95 of 95",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v12.md:27 Z-S53 and Z-S54 GRADUATED"
  ],
  "remedy": "No act owed: the owner's lift of Z-S53 after the signed dossier rewrite served every case as its own table columns.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S58",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A new library folder, 'Hitachi 6501 JP' (one file, Hitachi_Investment_Memo_2026_09_28_1.docx, synced 12:56:19Z), arrived six minutes after CRPS-o-1's run: the library reads 96 folders / 357 files, and FWD-4's population is no longer empty -- induction_request.run() reads unresolved_in_universe 1 of 96 and picks NONE ('no report states a ticker in the (Ticker: ...) form').",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S58",
   "166f02e312 L8+L9(AMGT_CORPUS round 15): crosswalk 236 -> 237 adds exactly 6501_JP_Equity; live library resolves 96 of 96",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v18.md:43 Z-S58 GRADUATED: Hitachi resolves; limbs driven in round 14 (p-2)"
  ],
  "remedy": "No act owed in this project: Hitachi 6501 JP now resolves in the crosswalk, and the WILL-ADD and REFUSES-ambiguous limbs were driven on planted folders.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S63",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A scheduled induction fire with a non-empty population appends its registration rows to lib/research/identity/registrations.json IN THE PINNED CHECKOUT (the task's WorkingDirectory), not in CLOUD's copy; the pool crosswalk carries the new names, but CLOUD's registrations.json does not, so a later crosswalk build from CLOUD inputs (crosswalk --write-pool, add_security, build_universe) would publish a record set WITHOUT them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S63",
   "55caac8a2e close(AMGT_RESAPP.TO-AMGT-zz-1): complete, 2 of 2 writers keep the planted record (the write_pool union)",
   "be2cf27545 sign(AMGT_CORPUS r-1 re-sign CTO half): SIGNED at pin 33c1d096a3, zz-1 an ancestor",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v25.md:12-13 amgt-induction-daily Ready, working directory pinned at 33c1d096a343, the pin carrying zz-1's pool union",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v25.md:45 Z-S63 GRADUATED: the fork cannot occur on the registered code"
  ],
  "remedy": "The registration union now sits inside write_pool for both writers (AMGT_RESAPP zz-1), and the scheduled task is pinned to the commit carrying it.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T04:18Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S68",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "model_block_pull._resolved_sign returns a field's per-security SAMPLED sign (one label from one value) for EVERY figure of that field on that security, so a loss-year figure reads POSITIVE: over the 97 blocks re-derived by round-23 y-4 leg c, figures whose plain sign label contradicts their own value went 886 served-before -> 1568 served-now on 49 blocks (the rebuild created per-security sign entries for more fields; with no entry the reader fell back to the figure's own sign, which was correct).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S68",
   "94301d5a9c drain(AMGT_CORPUS.TO-CRPS-y-2 amendments 1+2 / CRPS-y-5): _resolved_sign classifies each figure from its own value",
   "integrations/bloomberg/research/model_block_pull.py:943-947 at HEAD: the map's sampled sign is never served on a figure whose own value contradicts it",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-y-2.derive-no-sa-fallback.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v26.md:32 Z-S68 GRADUATED: 0 contradictions over 35,678 plain-signed served figures"
  ],
  "remedy": "_resolved_sign now classifies each figure from its own value (CRPS-y-5); the served census reads 0 contradictions over 35,678 plain-signed figures.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T09:26Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S76",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARMS AMGT_CORPUS-Z-W1-S28 (issuer ruling): BEST_DIV_YLD's served values ARE percent -- BA's consensus DPS over its price reproduces them exactly -- so printing 0.0% / 0.1% / 0.6% at the percent row type is correct and no conversion is needed; the defect is only the producer's unit LABEL 'DECIMAL' on that field.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S76",
   "b2aee0c0f2 direct-act(AMGT_CORPUS round 32 CRPS-ah-2): BEST_DIV_YLD under the 0.3 line decided by BEST_DPS / PX_LAST identity",
   "integrations/bloomberg/research/build_unit_map.py:361-367 at HEAD: CRPS-ah-2 yield identity, YIELD_IDENTITY_FIELDS BEST_DIV_YLD",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v38.md:1 BEST_DIV_YLD now labelled PERCENT on the served blocks, values unmoved"
  ],
  "remedy": "The producer's BEST_DIV_YLD unit label now reads PERCENT via the yield identity (CRPS-ah-2), with values unmoved on the served blocks.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S11",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-k-1: two shapes of the real scenario tables are not in the order's text -- a lone currency-symbol line after each value (AZN, BP, ML and 7 more), and a date + page-number footer line pair after the last row (8 names) -- and each is read as the table's own, not as a row.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S11",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-k-1.case-table-by-case.md last <status> is complete",
   "19458b6130 drain(AMGT_CORPUS round 9 CRPS-k-1): each case serves its own columns of the team's scenario table",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v12.md:30 Z-W1-S11 GRADUATED: the lone-symbol line reads as the prior value's unit"
  ],
  "remedy": "No act owed: the worker's two table-shape readings were accepted at L9 and CRPS-k-1 closed complete.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S16",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One of 159 served thesis pillars carries a lead with an empty paragraph: ML_FP_Equity's 'Nearing turn in cycle' has text '' and a citation passage that runs into the next 'RISKS AND CONSDIERATIONS' heading.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S16",
   "a53f4c4bfc proof(AMGT_CORPUS CRPS-p-5 amendment 1): ML_FP pillars 5 empty_text 0",
   "247d2dace6 ledger-close(AMGT_CORPUS round 14 continuation /3): LANDED 4 of 4 legs, served delta ML_FP thesis_pillars",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-5.mlfp-pillar-body.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v17.md:46 Z-W1-S16 GRADUATED: 5 of 5 bodies non-empty on the served object"
  ],
  "remedy": "The ML_FP pillar body was repaired (CRPS-p-5) and the served dossier carries 5 pillars with non-empty bodies.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S27",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "assembled.harness.cjs:336 asserts the ABSENT Model face carries the sentence 'No model in the research pack for this name yet'; CRPS-ad-3 item 5 (and face.cjs arm 7) bars 'in the research pack', so the two cannot both hold.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S27",
   "portal 54f3a252 AMGT_CORPUS round 28 issuer direct act: disarm row Z-W1-S27; ancestor of portal DEV HEAD ec65c5d6",
   "portal/src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs:343 at portal HEAD reads /\\bno model\\b/i with no pack phrase",
   "3b6fc8b6ce row(AMGT_CORPUS Z-S75): DISARMS Z-W1-S27",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v33.md:49 Z-W1-S27 GRADUATED, disarmed by Z-S75 (harness non-runnable at DEV, verified by text)"
  ],
  "remedy": "assembled.harness.cjs's ABSENT Model check was re-anchored to a no-model test without the research-pack phrase (Z-S75).",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-01T07:32Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S5",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-e-4 AC3's own check (e4_AC3.sh) runs `cd \"$(git rev-parse --show-toplevel)\"` then reads `portal/src/pages/SecurityAnalysis/types.ts` relative to that root -- in THIS worker's worktree (/c/tmp/wk-crps3-1) that root is the worktree's own toplevel, whose portal/ is an empty directory (same root cause as AMGT_CORPUS-Z-W1-S3: .gitmodules carries no submodule URL for portal, so no worktree of this project has portal content checked out), so the literal invocation FAILS with FileNotFoundError and cannot ever read PASS in this worktree, regardless of what the cited sheet says.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S5",
   "69288c8ca0 build(NFRA_OPALAI.OA-w-1): .gitmodules maps portal and opal_ai",
   ".gitmodules:5-7 at HEAD: [submodule portal] path = portal, url = https://github.com/Opal-Capital/portal.git",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-4.production-sequence-runner.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v6.md:57 Z-W1-S5 GRADUATED"
  ],
  "remedy": "The root cause is gone: .gitmodules now maps the portal submodule URL, and e-4 closed complete on the shared-tree substitute oracle.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S9",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-j-1 premise fails on the stored extractions: the 34 names with a case lead carry Upside/Base/Downside Case as three consecutive ROW LABELS of a scenario table (pdf class A, page 0), never a prose case; with the ruled block end the served rewrite gives Downside the whole numeric table and Upside/Base ABSENT.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S9",
   "19458b6130 drain(AMGT_CORPUS round 9 CRPS-k-1): each case serves its own columns of the team's scenario table",
   "fd44f203a6 ledger-close(AMGT_CORPUS round 9 dossier rewrite): LANDED 95 of 95, no served case is a heading or a table dump",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-k-1.case-table-by-case.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v12.md:26 Z-W1-S9 GRADUATED: split by case on 8 of 8 names read"
  ],
  "remedy": "A table-aware case rule (CRPS-k-1) splits the scenario table by case, and the signed rewrite served each case as its own columns.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-29T02:30Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S17",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "y-5 AC4 cannot pass as written: test_model_block_resolved_exception.py::test_dict_valued_field_unchanged asserts _resolved_sign('DICT_F','EXC JP Equity',1.0)=='NEGATIVE' (the map's sampled sign served against a positive value), which the ruled y-5 rule contradicts; that file is outside this order's paths.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S17",
   "bd28136864 amend(AMGT_CORPUS TO-CRPS-y-2 AMENDMENT 2): ruling on row Z-W2-S17",
   "94301d5a9c drain(CRPS-y-5): merged with AC4 reading 15 passed",
   "integrations/bloomberg/research/tests/test_model_block_resolved_exception.py:70 at HEAD asserts _resolved_sign('DICT_F', 'EXC JP Equity', 1.0) == 'POSITIVE'",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v28.md:13 Z-W2-S17 GRADUATED"
  ],
  "remedy": "Ruled by AMENDMENT 2: the superseded assertion now expects POSITIVE, and y-5 drained with AC4 at 15 passed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T09:26Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S7",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-f-2's RULED dry-run line format (chunk N of M fields=<k>, a COUNT only) would have broken the sibling test test_model_block_22_fields.py::test_dry_run_request_lines_carry_the_22 (a file outside this cell's <paths>, read-only) -- resolved by APPENDING the actual field list to the same line rather than editing that file.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S7",
   "0a5d0c3695 build(AMGT_CORPUS CRPS-f-2); 93440f9df1 drain merges it",
   "integrations/bloomberg/research/model_block_pull.py:1762 at HEAD prints request_fields= on the chunk line",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-2.hist-request-chunks.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v7.md:24 Z-W2-S7 GRADUATED"
  ],
  "remedy": "No act owed: the worker's count-plus-names dry-run line keeps both the ruled substring and the sibling test green, and it was accepted at L9.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W3-S4",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-e-3's AC1 <expect> `(?m)^\\d+ passed in ` can NEVER match the check script's own literal invocation: e3_AC1.sh runs pytest with `-k \"body_without_total or grown_corpus\"` against a 28-test file, and pytest's summary line for a filtered run is always 'N passed, M deselected in Xs' (M=26 here), never the bare 'N passed in Xs' form the regex anchors on -- verified with re.search, twice, both False, while the SAME two tests genuinely pass (confirmed separately via the unfiltered full-file run, 28 of 28).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S4",
   "03baefb8af amend(AMGT_CORPUS round 3 cut defects): AC1's expect on e-1/e-3/e-5 admits 'N passed, M deselected in' (row Z-W3-S4)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md:59 expect reads (?m)^\\d+ passed(, \\d+ deselected)? in at HEAD",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v6.md:53 Z-W3-S4 folds with Z-S22, GRADUATED"
  ],
  "remedy": "The issuer amended e-3 AC1's expect to admit pytest's filtered summary 'N passed, M deselected in'.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W4-S3",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The round-3 decomposition (AMGT_CORPUS_DECOMP.md, v3.0) never writes the concrete cell id CRPS-e-2 (or CRPS-e-1/3/4/5) anywhere in its text -- only the template 'CRPS-e-<n>' and the bare table label 'e-2' -- so proof-of-spec-check.py's CELL_ID_RE finds 0 declared cell ids in the doc and every round-3 worker's decomp_ref alignment check VIOLATES ('cell_ref CRPS-e-2 does NOT exist in ... AMGT_CORPUS_DECOMP.md'), independent of whether the cell's own AC1/AC2/AC3 all PASS-by-output.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S3",
   "03baefb8af amend(AMGT_CORPUS round 3 cut defects): the decomposition's rectangle cites the CRPS-e-<n> ids (adds the `CRPS-e-2` row)",
   "org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.round3.md:26 at HEAD carries the `CRPS-e-2` row",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-2.model-block-22-mnemonics.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v6.md:53 Z-W4-S3 folds with Z-S22, GRADUATED"
  ],
  "remedy": "The decomposition's rectangle now writes the concrete CRPS-e-<n> cell ids, so the decomp_ref alignment check resolves them.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W4-S9",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CORRECTION to AMGT_CORPUS-Z-W4-S8: the writer of integrations/bloomberg/research/field_map.json was this worker's own new test (test_model_block_pull_stage_derive_key), not the pre-existing integrations/bloomberg/research suite; model_block_pull.stage_derive calls _ensure_unit_map, which WRITES the tracked field_map.json for any security the map does not list.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S9",
   "24f7912522 fix(AMGT_CORPUS.TO-CRPS-z-4): the stage_derive test stubs _ensure_unit_map; row Z-W4-S9 corrects S8",
   "lib/research/identity/tests/test_slash_safe_key_sites.py:457 at HEAD monkeypatches mbp._ensure_unit_map to a no-op",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-z-4.slash-safe-key-sites.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v27.md:43 Z-W4-S8, Z-W4-S9 GRADUATED"
  ],
  "remedy": "The stage_derive test stubs _ensure_unit_map, so the suite leaves the tracked field_map.json clean.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S29",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Appending the 52 CRPS-aj-1 mnemonics breaks five existing tests that sit OUTSIDE this order's <paths> and so were not edited: test_model_block_22_fields.py::test_lists_carry_46_plus_22 (pins header 18 / hist 39 / forecast 11), test_hist_request_chunks.py::test_39_fields_chunk_into_25_and_14_order_preserved (pins 39 hist fields), test_build_unit_map_families.py::test_census_covers_every_pulled_mnemonic (the unit-family census names none of the 52), and test_currency_labels.py::test_december_block_equal_modulo_new_keys plus test_stage_derive_fye.py::test_december_name_byte_identical_to_pin (the December block now carries 7 more header names under unresolved).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S29",
   "68f09dce81 disarm(AMGT_CORPUS round 34 row Z-W1-S29): four test pins follow CRPS-aj-1's appended field lists",
   "9e4c1243e0 build(CRPS-ak-1): unit families for the 52 mnemonics, census 52 -> 0 unfamilied; 7c43d48775 drain merges it",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ak-1.unit-families-for-the-52.md last <status> is complete",
   "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v41.md:60 Z-W1-S29 DISARMED: -k 'families or census' 54 passed; 0 pointer units served"
  ],
  "remedy": "Four test pins follow the appended field lists, and CRPS-ak-1 gave the 52 mnemonics unit families; the census tests pass and 0 pointer units are served.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-04T01:47Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S12",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by their owner of the four ARMED closer rows AMGT_CORPUS-Z-S6, Z-S7, Z-S8 and Z-S9 (period ordering; scanner false negatives in lambda/class/parameter scopes, comprehension/loop/unpacking bindings, and definition-time defaults / class outer-name reads): each hazard is CLOSED at candidate dc2c0193ef by an independent re-review that PASSED all ten scanner controls and 5,040 period permutations, and that candidate is in CLOUD at b4a8638eeb. The four rows are legacy-shaped (hazard_standing/disarm_owner, no disarm clock) so they cannot advance in place under the row gate; this row is the disarm carrier and cites them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S12",
   "7f4a9d8c4e files this carrier row (owner's disarm of Z-S6..Z-S9 at dc2c0193ef, re-review 1c877a8c87)",
   "dc2c0193ef and b4a8638eeb are both ancestors of HEAD f7ad5dc777 (merge-base --is-ancestor, true)",
   "surprise-channel/adjudications/ADJUDICATION_v37.md:11 Z-S6..Z-S9 DISMISSED_WITH_REASON through Z-S12"
  ],
  "remedy": "No act owed: this row is the owner's disarm carrier for Z-S6..Z-S9, and the closing candidate it cites is in HEAD.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S16",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "EXPOSURE after the 11:11Z fire: the induction landed 20 MEASURED identities but the served crosswalk now carries, for each of the 20 folders, BOTH the folder's original UNRESOLVED coverage record AND the appended registration record, and both claim the folder's `security-<hash>` association form -- so crosswalk.resolve() reads those 20 forms AMBIGUOUS (a collision, refused) where it read an UNRESOLVED miss before, and the re-ingest at 11:19Z resolved the SAME 33 folders as before the fire (stored 124, put_performed 1, existed 123): 0 of the 20 inducted folders ingested. FWD-19 is REALIZED on identity and NOT on re-ingest.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S16",
   "a2b84a1b2a crosswalk fix: a registration whose folder matches an UNRESOLVED record resolves it in place (names Z-S16)",
   "lib/research/identity/crosswalk.py:738 at HEAD carries the Z-S16 closer remedy (one record per folder)",
   "2c24cc867d one crosswalk.main --write-pool re-mint on the fixed builder; 75f65d6655 Z-S19 disarm carrier, UNRESOLVED 60 -> 40"
  ],
  "remedy": "The crosswalk builder resolves an UNRESOLVED coverage record in place instead of appending a twin, and the pool was re-minted on the fixed builder.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T12:01Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S21",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "PRE-FLIGHT, before any write: the round-3 40-name induction fire, built in memory through add_security's own builder with its own _collision_mode per request, would leave 20 of the 40 folders with TWO records each -- 19 requests ENRICH a MEASURED universe record that has no folder (the folder is attached) while the folder's own UNRESOLVED coverage record stays beside it, and one folder's earlier UNRESOLVED registration row stays beside its new MEASURED row. UNRESOLVED would read 40 -> 20, not 0. The fire is HELD by its issuer; no put, no vendor call happened.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S21",
   "9ec1226a01 crosswalk: an ENRICH that attaches a folder RETIRES that folder's UNRESOLVED record; a MEASURED row supersedes an UNRESOLVED one",
   "lib/research/identity/crosswalk.py:725-733 at HEAD: superseded UNRESOLVED rows dropped, ENRICH retires the keyless record",
   "a41f6cf277 the 40-name fire's pre-flight PASSES on 9ec1226a01; 4be92efa19 identity 94 of 94"
  ],
  "remedy": "The ENRICH branch now retires the folder's UNRESOLVED record, and the held 40-name fire then passed its pre-flight.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S25",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "FWD-19's purpose number MEASURED on the served pool after the 40-name fire: 89 of 94 live research folders carry a MEASURED identity, SHORT BY FIVE -- four UNRESOLVED-only (the keyless registration rows the fire's already-registered path skipped, bloomberg_calls 0 each) plus AMD, which has NO pool record at all -- and the five are EXACTLY the five folders added since the builder's 89-name snapshot, so the shortfall IS the directory growth.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S25",
   "f7c42b02d5 Z-S32: served crosswalk carries 94 folders after the signed re-mint",
   "eaed38bac0 round-3 L10: identity CLOSED at 94 of 94 on two planes",
   "surprise-channel/adjudications/ADJUDICATION_v8.md:45 Z-S25 closed by the identity census reaching 95 == 95 == 95"
  ],
  "remedy": "The five-folder shortfall closed when the re-mint carried every live folder with a MEASURED identity.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S29",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The corrected FWD-12 re-pull (Bloomberg identifiers, 01:2xZ) lands refdata and bestdata WITH content but every histdata object is '{}' (2 bytes), 22 batches of 3 before this seat stopped it. CRPS-e-2 grew HIST_FIELDS from 23 to 39 (bb6b1f2f25), and blp_client.historical_data's handler returns early on any message without securityData (integrations/bloomberg/mcp/blp_client.py:285-287), so a request-level responseError is dropped and the call returns {} with rc 0. INFERRED, not measured here: Bloomberg's HistoricalDataRequest per-request field limit (widely documented as 25) rejects the 39-field request. The served history came from pulls at 23 fields.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S29",
   "93440f9df1 drain of CRPS-f-2 @0a5d0c3695 (chunked history, request-level error raised); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-2.hist-request-chunks.md last status complete",
   "integrations/bloomberg/mcp/blp_client.py:303-306 at HEAD raises BlpResponseError on responseError",
   "integrations/bloomberg/research/model_block_pull.py:321 HIST_FIELDS_PER_REQUEST = 25 and :740 _hist_field_chunks at HEAD",
   "de06482203 round-4 pull: 89 of 89 histdata non-empty; 82a1a3e7fd Z-S33 disarm carrier"
  ],
  "remedy": "The history request is chunked at 25 fields and blp_client raises a request-level responseError instead of returning {}.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T04:12Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S33",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by their owner of AMGT_CORPUS-Z-S26 (the FWD-12 incident: keys passed as identifiers, 31 served empty ~7 min then rolled back, 58 honest-empty) and AMGT_CORPUS-Z-S29 (history {} on a single 39-field request): CRPS-f-2 drained @93440f9df1 (history chunked at 25 fields, client raises a request-level error); the round-4 drain pulled with Bloomberg identifiers, a probe batch first -- history rows 12-20 on 3 of 3 -- then 89 of 89 raw objects non-empty on all three kinds, then the derive under the signed pair: 89 of 89 served blocks non-empty with 8-11 FY rows read through scoped_amgt, the 22 added mnemonics present as figures (20 on 44 keys). The 58 honest-empty blocks are superseded by newer stamps; no delete was reached. Both rows are legacy-shaped; this row is their carrier.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S33",
   "82a1a3e7fd files this carrier row",
   "de06482203 round-4 pull and derive: 89 of 89 served blocks non-empty; change entry closed with content proof",
   "surprise-channel/adjudications/ADJUDICATION_v7.md:16-18 Z-S33, Z-S26, Z-S29 GRADUATED"
  ],
  "remedy": "No act owed: this row is the owner's disarm carrier for Z-S26 and Z-S29, and its pull and derive landed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S37",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by its owner of AMGT_CORPUS-Z-S30 (extract refused a write-once collision on Copa's duplicate PDF and stopped the sequence): CRPS-f-3 drained @f221407bb9, and the round-4 production sequence ran 10 of 10 with rc 0 -- extract stored 353 of 353 report_ids, 0 crashes, the CPA pair a named 'duplicate-content ff0e11955cb266f4' skip in both extract stages; typed, continuation (94 names), dossier (94 written) and the coverage census (94 = 82 + 12 + 0 + 0) followed. Z-S30 is legacy-shaped; this row is its carrier.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S37",
   "f221407bb9 drain of CRPS-f-3 (one extract per report_id, named duplicate-content skip); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-3.duplicate-content-one-extract.md last status complete",
   "04832c4b48 commits evidence/production_sequence_r4 log: stored 353, crash 0, 10 of 10 steps rc 0",
   "surprise-channel/adjudications/ADJUDICATION_v7.md:23 Z-S30 GRADUATED through Z-S37"
  ],
  "remedy": "No act owed: this row is the owner's disarm carrier for Z-S30, and the duplicate-content extract fix ran whole in production.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S43",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "FWD-2's one bronze-without-silver row is EXPLAINED, not a loss: bronze holds 356 objects for 355 report_ids, because two PDFs are byte-identical copies ('Copa Holdings - 2025 Investor Day Presentation.pdf' and '... (1).pdf', content ff0e11955cb266f4), and silver writes ONE row per report_id by CRPS-f-3's design. 355 of 356 is the fence working. The round-5 analysis read 354/353 at an earlier vintage; the one-row gap is the same object.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S43",
   "ac7fc54651 files this row with evidence/bronze_silver_one_row_20260926.txt (objects 356, report_ids 355, duplicates 1)",
   "surprise-channel/adjudications/ADJUDICATION_v9.md:20 Z-S43 GRADUATED (the Copa Holdings byte-identical pair)"
  ],
  "remedy": "No act owed: the one bronze-without-silver row is the Copa byte-identical pair, which the one-row-per-report_id rule is meant to collapse.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S51",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Base-case rule this project's model-block derive computes moved under it: AMGT_RESAPP's worker @b56fef3032 (18:36Z today) made lib/research/api/case_rule.py the ONE rule (adjusted P/E) and model_block_pull._compute_cases delegates to it. Over the 97 block keys, cases-report now reads SERVED 69 vs round 7's 49 (21 ABSENT->SERVED, 1 SERVED->ABSENT: CAT_US, act A's re-mint) and 48 of 48 served-in-both at a different ratio. The stored blocks still carry the round-7 values; any derive now would move them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S51",
   "5151500c41 COO half and 0fbb50e84e CTO half signed for the round-9 k-2 re-derive",
   "f7c45f840e ledger-close: model-block re-derive LANDED 97 of 97, served 51 -> 69, 97 of 97 equal to case_rule",
   "surprise-channel/adjudications/ADJUDICATION_v12.md:29 Z-S51 GRADUATED (ran 97 of 97)"
  ],
  "remedy": "The re-derive under case_rule.py ran over all 97 keys under a signed pair and matched the rule's expected log.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S55",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "model_block_pull cases-report given the underscore key form (AMD_US_Equity) does not refuse: it prints 'base ABSENT ... no consensus EPS on the landed block' for every name (0 of 97 served); the Bloomberg form (AMD US Equity) reads 69 of 97 served. A wrong-shape key returns a real-looking verdict.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S55",
   "120ff9b27f drain of CRPS-l-4 (cases-report refuses an unresolvable key); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-4.cases-report-refuses-unresolved-key.md last status complete",
   "integrations/bloomberg/research/model_block_pull.py:1960 _cases_report_unresolved and :1987 its call at HEAD",
   "surprise-channel/adjudications/ADJUDICATION_v13.md:18 Z-S55 GRADUATED (planted_underscore rc 2)"
  ],
  "remedy": "cases-report now refuses a security it cannot resolve to landed raw before computing, so the underscore form no longer grades ABSENT.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S59",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The round-14 p-5 drain merge 34bbf74213 (safe-merge --continue after an append-only channel conflict) landed 6 files of 4.0.0_SA_CRO~Z (org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/*) that CRO~Z had staged in the shared index during the resolve window; they are attributed to 2.0.0_SA_COO~X in that commit.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S59",
   "ccf2a27c6b fix(safe-merge): the conflict state is what the MERGE could stage (names AMGT_CORPUS-Z-S59)",
   ".tools/safe-merge.sh:336 at HEAD carries the Z-S59 comment and the HEAD..MERGE_HEAD bound",
   "42b7ff4bd8 Z-S62 owner's disarm of Z-S59; surprise-channel/adjudications/ADJUDICATION_v19.md:27 GRADUATED (landing read, not exercised)"
  ],
  "remedy": "safe-merge bounds the conflict state to HEAD..MERGE_HEAD, so --continue refuses paths a peer staged in the shared index.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S64",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The model-block writer (integrations/bloomberg/research/model_block_pull.py) puts slash tickers under a LITERAL '/' key -- derived/model_block/BP/_LN_Equity/... (6 objects) -- and never through crosswalk.slash_safe_key, so BP/ LN and NG/ LN sit outside C-SLASH-SAFE-KEY on this surface; 0 objects exist under the slash-safe form BP-SLASH-_LN_Equity.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S64",
   "integrations/bloomberg/research/model_block_pull.py:1733 at HEAD: derived key built with crosswalk.slash_safe_key(sec_key)",
   "dc5cd3a3c3 aa-4 BP/NG pass COO half signed; 27bbd26ccf ADJUDICATION_v30 reads BP/NG on encoded keys",
   "surprise-channel/adjudications/ADJUDICATION_v30.md:35 Z-S64 GRADUATED"
  ],
  "remedy": "The model-block writer keys its derived objects through crosswalk.slash_safe_key, and BP/NG were re-derived on encoded keys.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S69",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "model_block header market figures take the REPORTING currency label: TSM_US_Equity CUR_MKT_CAP 2339877750964.95 is served with currency TWD (basis 'reporting (EQY_FUND_CRNCY)') while currencies.quote is USD, converted false, and the raw refdata carries CRNCY USD with the same value -- a USD figure labelled TWD. The same labelling rule places CUR_MKT_CAP / NET_DEBT / CURR_ENTP_VAL on 79 header figures across 27 mixed-currency securities; only TSM CUR_MKT_CAP is measured wrong, the other 78 are the rule's reach, unmeasured per figure.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S69",
   "5fe52a896a aa-1 merged and aa-2 ledger CLOSED (TSM CUR_MKT_CAP served USD); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aa-1.denomination-census.md last status complete",
   "integrations/bloomberg/research/model_block_pull.py:1028 and :1146 at HEAD: CRPS-aa-1 denomination rule (row Z-S69)",
   "21f7a96cf6 CTO half signed for the Z-S69 fix; surprise-channel/adjudications/ADJUDICATION_v30.md:34 GRADUATED"
  ],
  "remedy": "The header money figures follow the measured denomination, and TSM CUR_MKT_CAP is served labelled USD.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S84",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "In --mode dry-run the scheduled entry's model_block_admit step reads rc 1 at CLOUD 6527a03cc1: induction_run's dry run poisons boto3.client and admit's S3 read trips it, so the scheduled dry run cannot pre-flight the admit (or, from round 34, the refresh) step.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S84",
   "a5a561d96b drain of CRPS-ak-3 (restore_poison_sites; admit rc 0, refresh rc 0); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ak-3.dry-run-reads-rc0.md last status complete",
   "lib/research/corpus/induction_scheduled.py:99 restore_poison_sites and :136 its use at HEAD",
   "surprise-channel/adjudications/ADJUDICATION_v41.md:62 the 2026-10-04 log's later dry runs read rc 0"
  ],
  "remedy": "The scheduled dry run restores the poisoned sites after step 1, so the admit and refresh steps read rc 0.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S12",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-k-1: 6 of the 34 scenario tables are unreadable on the ruled 3 x k count -- the EPS row carries 14 values (the Base group has 4, not 5) -- so those names serve all three cases ABSENT with the reason.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S12",
   "b110086294 CRPS-l-3: six unreadable case tables served ABSENT with their own reason; org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-3.six-unreadable-case-tables.md last status complete",
   "surprise-channel/adjudications/ADJUDICATION_v13.md:17 Z-W1-S12 GRADUATED (absent_specific 6, absent_generic 0)"
  ],
  "remedy": "The six unreadable tables are served ABSENT with their own specific reason; the missing value is absent from the extraction and is rightly not served.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S20",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "test_build_unit_map_families.py::test_ratio_outside_the_band_stays_unresolved_and_band_is_not_widened pins classify_unit('IS_DIV_PER_SHR', 0.0, ..., header) == UNRESOLVED (line 88), so the zero-dividend families could not land inside classify_unit without breaking a builder suite the order requires green; that file is outside this order's paths.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S20",
   "717cbb0a14 issuer ruling: Z-W1-S20 the zero rule stays outside classify_unit",
   "integrations/bloomberg/research/build_unit_map.py:243 unit_from_basis_zero at HEAD; tests/test_build_unit_map_families.py:88 still pins classify_unit zero UNRESOLVED",
   "surprise-channel/adjudications/ADJUDICATION_v28.md:12 Z-W1-S20 GRADUATED"
  ],
  "remedy": "Ruled: the zero rule lives in unit_from_basis_zero via build_entries, so the pinned classify_unit test and the zero family both hold.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T11:53Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S28",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-ae-1 ruling 2 prints every Dividend yield cell as a percent at 1 dp, but the served E-column figure (BEST_DIV_YLD) is a DECIMAL fraction, so BA's 2026E-2028E cells read 0.0%, 0.1%, 0.6% from served values 0.00254, 0.14533, 0.60315 -- a number whose unit the page cannot read as the history's percent.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S28",
   "c12a0d6ffb Z-S76 disarms Z-W1-S28 (BA DPS / price x 100 = the served values)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ae-1.sheet-reads-like-the-analysts.md last status complete",
   "surprise-channel/adjudications/ADJUDICATION_v34.md:39 Z-W1-S28 GRADUATED, verified by arithmetic"
  ],
  "remedy": "Ruled by Z-S76: BEST_DIV_YLD is on the percent scale, so the page's percent print is correct.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-01T09:27Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S6",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The prescribed close-out command (`.tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <TO>`) returns INVALID (rc=1) on this cell's own, correctly-built instance -- not from anything in the acceptance rows, but from the ALIGNMENT limb: round 3's live decomposition doc (AMGT_CORPUS_DECOMP.md) names its five cells as bare `e-1`..`e-5` in its rectangle table, while the CRPS-e-4 task order's own <owned_cells>/cell_refs use the full form `CRPS-e-4` -- and the checker's CELL_ID_RE requires an uppercase-prefixed id (`[A-Z][A-Z0-9]*-[a-z]{1,4}-[a-z]?\\d+`), so it finds 0 distinct cell ids in the decomp doc and refuses EVERY cell_ref citing it, for all five round-3 cells alike, not only this one.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S6",
   "03baefb8af amend: the decomposition's rectangle cites the CRPS-e-<n> ids (AMGT_CORPUS_DECOMP.md changed)",
   "2b3c2761e8 Z-S22 disarm carrier: Z-W1-S6 cleared by the prefixed cell ids; all five round-3 instances VALID",
   "org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md:14 at HEAD cites the prefixed id CRPS-ak-1",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-4.production-sequence-runner.md last status complete"
  ],
  "remedy": "The decomposition's rectangle cites the prefixed CRPS-<cell> ids the orders' cell_refs cite, so the alignment limb resolves them.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S10",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "3 of 51 SERVED Base cases carry no `ratio_to_px_last`/`band` field at all -- an older-vintage model_block.json stamp predating CRPS-g-1's guard rewrite -- so a reader that trusts `ratio_to_px_last` alone silently reads a real SERVED case as not-computable.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S10",
   "f7c45f840e ledger-close: model-block re-derive LANDED 97 of 97; 6861_JP, CAT_US, CSL_AU un-serve with the rule's reason",
   "lib/research/api/case_rule.py:250-251 and :261-262 at HEAD: the one case rule writes ratio_to_px_last and band on a computed base",
   "surprise-channel/adjudications/ADJUDICATION_v12.md:28 Z-W2-S10 GRADUATED (verify keys 97 match 97)"
  ],
  "remedy": "All 97 model blocks were re-minted under the one rule, so no served Base case lacks its ratio and band fields.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-29T03:16Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S4",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Immediately after ISSUER AMENDMENT 2 landed, one --dry-run over the REAL 93-folder library read a population of 40 UNRESOLVED folders with Copa CPA and Uber Technologies UBER US EVIDENCED (ambiguous 0) -- a live, transient departure from the stable 60/ambiguous-2 shape every prior and every later measurement (three re-reads immediately after, plus the pre-amendment-1 and post-amendment-1 runs) reproduces; induction_request.measure_population/build_request (read-only to this cell, untouched by either amendment) resolve through the live crosswalk/registrations.json substrate, and the blip's timing lines up with the issuer's own revert of its mis-shaped fire-1 writes rather than with anything this cell edited.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S4",
   "44fb5dfb8d CRPS-d-5 ISSUER AMENDMENT 2 (the measurement this row records)",
   "eaed38bac0 round-3 L10: identity CLOSED at 94 of 94",
   "surprise-channel/adjudications/ADJUDICATION_v6.md:48 Z-W2-S4 already GRADUATED"
  ],
  "remedy": "No act owed: a one-read transient during the issuer's revert; the substrate then settled and identity closed at 94 of 94.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S8",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-f-2 Section 6 step 1 says the instance carries 'AC4 as a judgment row with no grade', but the literal checker invocation named in step 2 (ids AC1,AC2,AC3 only) refuses any acceptance row outside that exact set, and the schema's status/method enums have no judgment value either way -- AC4 omitted from the acceptance array, recorded in declared_exclusions instead.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S8",
   "org/standards/PROOF_OF_SPEC.schema.json:253 at HEAD: acceptance items carry a judgment field (added b4299fa5aa, 2026-09-03)",
   "93440f9df1 drain of CRPS-f-2 with the VALID instance; org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-2.hist-request-chunks.md last status complete",
   "surprise-channel/adjudications/ADJUDICATION_v7.md:24 Z-W2-S8 GRADUATED"
  ],
  "remedy": "No act owed: the instance recorded AC4 in declared_exclusions and checked VALID; the proof schema already carries a judgment row shape.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W3-S5",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "proof-of-spec-check.py's ALIGNMENT limb reads the decomp doc's own CELL_ID_RE-matched id space as EMPTY (0 distinct cell ids) at org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md, so every one of this TO's 3 criteria (cell_refs=\"CRPS-e-3\") is refused with 'cell_ref does NOT exist in the decomp' -- despite the decomp's own s.6 preflight line asserting 'CRPS-e-<n> matches the [a-z]{1,4}-[a-z]?\\d+ branch': the doc's cell table uses the BARE form `e-3` (no CRPS- project prefix), which the regex's required `[A-Z][A-Z0-9]*-` leading group never matches on its own, and the literal string 'CRPS-e-3' (or e-1..e-5) appears NOWHERE in the file. This makes the checker return INVALID (rc 1) for this TO regardless of every acceptance row's own status.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S5",
   "03baefb8af amend: the decomposition's rectangle cites the CRPS-e-<n> ids (row Z-W3-S5 named)",
   "2b3c2761e8 Z-S22 disarm carrier: Z-W3-S5 cleared; all five round-3 instances VALID",
   "org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md:14 at HEAD cites the prefixed id CRPS-ak-1",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md last status complete"
  ],
  "remedy": "The decomposition's rectangle cites the prefixed CRPS-<cell> ids the orders' cell_refs cite, so the alignment limb resolves them.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W4-S4",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-g-4's task order names lib/research/corpus/induction_request.py --pick as the FWD-4 read-only instrument, but the module hard-codes its write to org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/induction_request.json (DELIVERABLES_DIR, induction_request.py:60-63) -- a path outside this worker's own <paths> grant and this cell's read-only/no-write bound -- so the fence could not be freshly EXERCISED from this worktree; measured instead from the already-committed induction_request.json and the committed CRPS-c-5 proof_of_spec.json's recorded output_evidence at HEAD, both a prior real run. A second, unrelated drift found by the same probe: that prior run (as_of 2026-09-23) measured unresolved_in_universe 60 of 93; this worker's fresh backlog.coverage() read today measures 0 of 94 unresolved -- the backlog population FWD-4 exercises against has moved to empty since the cited evidence was produced.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S4",
   "lib/research/corpus/induction_request.py:60 DELIVERABLES_DIR still hard-coded at HEAD f7ad5dc777",
   "lib/research/corpus/induction_request.py:452-457 at HEAD: run() always makedirs and writes REQUEST_FILE_NAME there",
   "surprise-channel/adjudications/ADJUDICATION_v8.md:27 GRADUATED with the grant question left to whoever next cuts that cell; no commit names a fix"
  ],
  "remedy": "Still owed: induction_request.py writes its request file to ~2's deliverables on every run, so a read-only --pick mode or an output-dir argument (or a grant ruling) is needed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": false
 },
 {
  "id": "AMGT_CORPUS-Z-W5-S2",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The sparse worker cone omits infra/, so every lib.research.corpus CLI dies at import (lib/opal_naming.py reads infra/logic/registry/systems.json) and safe-commit's naming limb (ENFORCE) refuses the commit of any .json; CRPS-i-5's instruments ran only through a scratch wrapper that repoints REGISTRY_DIR at a copy from git HEAD, and its work is finished but UNCOMMITTED.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W5-S2",
   "68cc1b6356 complete(CRPS-i-5) committed the cell's work; org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-5.nineteen-outcome-evidence-round7.md last status complete",
   "4ef91aedfe drain of CRPS-i-5, re-graded VALID",
   "surprise-channel/adjudications/ADJUDICATION_v10.md:38 Z-W5-S2 GRADUATED (disarmed before the commit by sparse-checkout add)"
  ],
  "remedy": "The worker cone was widened by sparse-checkout add before the commit, and the cell's work landed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S30",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRNCY_ADJ_MKT_CAP: the producer's FIELD_BASIS says 'full currency units' but every landed value (BA 152984.02, GOOGL 4182279.8, BP/ LN 87634.56) is the same header's CUR_MKT_CAP divided by 1e6 exactly, so the unit read from the values is MILLIONS and the basis text is wrong.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S30",
   "1ed823496d issuer disarm: integrations/bloomberg/research/model_block_pull.py:465-466 FIELD_BASIS reads millions of that currency",
   "served BA CRNCY_ADJ_MKT_CAP unit MILLIONS value 152984.02 (read by 3.0.0_SA_CVO~Z)",
   "surprise-channel/adjudications/ADJUDICATION_v41.md:61 Z-W1-S30 DISARMED"
  ],
  "remedy": "The basis text reads millions and the served unit agrees.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-04T01:58Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S13",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "INCIDENT on served output, this seat's act: the 08:02:55Z induction fire (d-5 as first issued) re-minted s3://opal-data-harvest/crosswalk/v1/2026-09-24.json through CLOUD's build_crosswalk and REPLACED a signed object 2.0.0_SA_COO~Z had published at 03:32:47Z under a never-widen pair (523,207 bytes, MEASURED 194) with a 231,910-byte document (MEASURED 36 + 20 UNRESOLVED noise registrations) -- the served scoped API now reads ASML_US_Equity and AAPL_US_Equity UNRESOLVED where they read MEASURED/SERVED at 03:34Z. This seat's own exposure grade (msg 25324) compared against the WRONG before-object (the 2026-09-22 key) because it never head-objected the exact key it was about to write.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S13",
   "b00b740d0c (2026-09-24T11:23Z) row Z-S14: owner DISARM carrier for Z-S13, both conditions MET (signed object restored and verified 08:22Z; induction write through the unified builder, ONE put, MEASURED 194 -> 214, 194 of 194 prior keys present)",
   "lib/research/identity/crosswalk.py:647-649 at HEAD f7ad5dc777: build_crosswalk on CLOUD takes identity_universe (the second registration source), so CLOUD has one builder",
   "ADJUDICATION_v5.md:28: Z-S13 GRADUATED, disarmed by Z-S14, both conditions MET"
  ],
  "remedy": "The signed crosswalk/v1/2026-09-24 object was restored and re-written once through the unified builder under a complete pair; owner disarm carried by Z-S14.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T11:23Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S17",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The sector template producer (CRPS-c-7, `sector_template --write`) cannot re-run on a grown corpus: at 12:14:41Z it raised gold.GoldImmutableError on the FIRST business type it reached (business_type=consumer-cyclicals+consumer-services/fbb482677a438d92.json 'already holds a different sha256') because `_object_name(inputs)` (:431-435) hashes METHOD_VERSION plus that type's own inputs while the artifact body embeds the corpus-wide denominator `total` (218 reports today, 124 when the object was minted) -- so a type whose reports did not change gets the SAME name for a DIFFERENT body, and gold's never-overwrite rule refuses it, correctly. The loop stops at the first type, so no sector template was re-measured for any type today, including the types the 20 newly inducted names joined.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S17",
   "f72d8acf68 worker fix (CRPS-e-3): total leaves fields/the artifact body; drained at 1266b834ec (2026-09-24T19:48Z)",
   "lib/research/corpus/sector_template.py:354-358 and :411-416 at HEAD f7ad5dc777: total never enters fields; METHOD_VERSION = \"3\" at :97",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md last status: complete",
   "2b3c2761e8 row Z-S22 disarm carrier: sector_template --write rc 0 over 218 reports, a second run all existed; ADJUDICATION_v6.md:53 folds Z-S17 through Z-S22"
  ],
  "remedy": "CRPS-e-3 took the corpus-wide total out of the sector-template body and bumped METHOD_VERSION to 3, so an unchanged type keeps its name and body.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:48Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S22",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by their owner of eight ARMED rows, all the issuer's own round-3 cut defects or the sector-template refusal the round cut a cell for: Z-S17 and Z-W3-S3 (sector_template --write GoldImmutableError on a grown corpus) are cleared by CRPS-e-3 drained at 1266b834ec (total out of the body, METHOD_VERSION 2 -> 3, --write rc 0 over 218 reports, 9 objects written once, a second run all existed); Z-W3-S4 and Z-W2-S5 (AC1's expect could not match a -k pytest summary) are cleared by the issuer's amendment at 03baefb8af widening the expect to admit ', N deselected', after which e-3 and e-1 AC1 matched; Z-W4-S3, Z-W3-S5, Z-W1-S6 and Z-W2-S6 (the decomposition named its cells bare e-<n>, so the checker's alignment limb found 0 cell ids) are cleared by the same commit prefixing the rectangle to CRPS-e-1..CRPS-e-5, after which all five round-3 instances read VALID rc 0. The eight are legacy-shaped (no disarm clock) and cannot advance in place; this row is their disarm carrier and cites each.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S22",
   "2b3c2761e8 commits row Z-S22 citing drain 1266b834ec (e-3) and amendment 03baefb8af (AC1 expect, cell ids)",
   "ADJUDICATION_v6.md:53: Z-S22 GRADUATED and its eight targets fold with it, all eight verified to exist and be cited",
   "1266b834ec and 03baefb8af are both ancestors of HEAD f7ad5dc777 (merge-base --is-ancestor)"
  ],
  "remedy": "No act owed: this row is the owner disarm carrier for eight ARMED rows, and each cited fix is on CLOUD.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S26",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "INCIDENT on served output, this seat's act: the FWD-12 pull passed SECURITY KEYS (ADBE_US_Equity) to model_block_pull.py --securities, which expects Bloomberg identifiers (ADBE US Equity) and forms the key by replacing spaces (:395). Every DAPI request named a security that does not exist and landed an EMPTY raw object ({}), rc 0, 89 of 89 'landed'. The derive then minted 89 blocks with 0 FY rows and 0 figures (51 unresolved each), and newest-stamp-wins put them in front of the 31 keys that had served real blocks (~205 figures) from ~22:30:2xZ to 22:37:04Z. Rolled back by copying each prior block forward (31 of 31, verified through scoped_amgt.read_model_block). The 58 new keys still serve an empty block instead of none. The derive also rewrote field_map.json from empty data (+61,889/-7,653 lines, uncommitted); restored to HEAD.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S26",
   "de06482203 round-4 drain: Model block lands for 89 of 89 (histdata/refdata/bestdata non-empty 89 of 89) on the chunked 25+14 request",
   "82a1a3e7fd (2026-09-25T04:53Z) row Z-S33: disarm carrier for Z-S26 and Z-S29, 58 honest-empty blocks superseded by newer stamps",
   "integrations/bloomberg/research/model_block_pull.py:316 and :791 at HEAD f7ad5dc777: CRPS-f-2 chunking that avoids the {} history response",
   "ADJUDICATION_v7.md:17: Z-S26 GRADUATED through Z-S33, blocks now serve content"
  ],
  "remedy": "The round-4 pull used Bloomberg identifiers with a chunked history request and the derive landed 89 of 89 blocks with figures, superseding the empty blocks; disarm carried by Z-S33.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T04:53Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S30",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The production sequence after the re-mint stops at step 1: extract --write raises BronzeImmutableError on research-report-extract/security_key=CPA_US_Equity/ff0e11955cb266f4/extract.json. Copa's folder holds the SAME PDF under two names ('Copa Holdings - 2025 Investor Day Presentation.pdf' and '... (1).pdf'); both land under one report_id (the content hash), and the extract body carries 'bronze_key' (the s3 uri, filename included; extract.py:552), so the two bodies differ under one write-once name (extract.py:691) and the second put is refused -- aborting extraction for every name after it and skipping steps 2-10. The body is not a function of its key: the class of Z-S17.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S30",
   "1e65df55c3 worker fix (CRPS-f-3): a report stored under two file names yields ONE extract; drained at f221407bb9 (2026-09-25T03:54Z)",
   "lib/research/corpus/extract.py:658-697 at HEAD f7ad5dc777: group_canonical_bronze_keys and the duplicate-content print",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-3.duplicate-content-one-extract.md last status: complete",
   "ADJUDICATION_v7.md:23: Z-S30 GRADUATED through Z-S37, extract stored 353 of 353 report_ids, the CPA duplicate a NAMED skip"
  ],
  "remedy": "CRPS-f-3 groups content-duplicate bronze keys under one report_id and extracts only the canonical key, naming the skipped duplicate.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T03:54Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S34",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-f-1 (drained @eeb996b10e) passes the live research folders only in crosswalk.main's new --disclosure branch; the --write-pool branch (crosswalk.py:1356) still calls build_crosswalk without research_folders, so a put through it publishes research_folders_live and research_universe ABSENT. The order ruled that crosswalk.main passes the list; add_security._build_document does, crosswalk.main's write path does not. AC2 exercised only the --disclosure branch, so neither the worker's run nor this seat's re-grade could see the write path. crosswalk.main --write-pool is also the Peers producer's route to this key, so the two writers would disclose differently.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S34",
   "5ef2158828 fix: crosswalk.main --write-pool and --dry-run pass research_folders and research_root",
   "lib/research/identity/crosswalk.py:1465-1472 and :1490-1492 at HEAD f7ad5dc777: every CLI path builds with research_folders (comment names row Z-S34)",
   "8db3212dae (2026-09-25T05:54Z) remint: ONE crosswalk.main --write-pool under the signed pair, folders_in_records 94 == research_folders_live 94",
   "ADJUDICATION_v7.md:20: Z-S34 GRADUATED through Z-S35"
  ],
  "remedy": "crosswalk.main now passes research_folders/research_root on --write-pool and --dry-run, and the disclosure re-mint through that path verified folders_in_records == research_folders_live.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T05:54Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S38",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by its owner of AMGT_CORPUS-Z-S36 (dossier Model rows read no block and cited a stale 'not authorized' reason): CRPS-g-2 drained @9d90739261 (model_rows read the newest derived block by the served reader's rule, name it in inputs, derive every absent reason; the constant deleted), and the round-5 rebuild wrote 94 dossiers -- over the 91 written, every one names its Model block, 3,772 of 9,183 model_rows carry a value, 0 carry 'not authorized', 0 dossiers have zero values (round 4: 0 of 9,471). Z-S36 is legacy-shaped; this row is its carrier.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S38",
   "9d90739261 drain of CRPS-g-2 (worker 9162530ba0): dossier model_rows read the newest derived Model block",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-2.dossier-model-rows-from-block.md last status: complete",
   "ADJUDICATION_v8.md:24-25: Z-S36 and Z-S38 GRADUATED, 3,772 of 9,183 model_rows carry a value, 0 not authorized"
  ],
  "remedy": "No act owed: owner disarm carrier for Z-S36, whose fix (CRPS-g-2) is drained and measured on the served dossiers.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S44",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by its owner of AMGT_CORPUS-Z-S41 (read_dossier served the greatest inputs hash, not the last write, so write_one rewrote on unchanged inputs) and LIFT of the hold AMGT_CORPUS-Z-S42: CRPS-h-1 drained @dd82056420 (read_dossier returns the object written last on the newest as_of date), and FWD-17 (b)'s exercised arm read on the served table -- dossier --write --security-key IMB_LN_Equity, run twice, printed 'unchanged inputs_sha16 fc1e3a62101e4598 wrote 0' both times, and the store is byte-for-byte where it was: IMB 5 objects before and after, newest write 2026-09-25T21:45:30Z, table 373 objects, rewrites_on_unchanged_inputs 37 unchanged, read_dossier serves the last write 95 of 95.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S44",
   "dd82056420 drain of CRPS-h-1: read_dossier serves the last write on the newest date",
   "0ffe50d118 drain+row Z-S44: dossier --write IMB_LN_Equity twice wrote 0 at unchanged inputs_sha16",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-1.dossier-newest-is-last-write.md last status: complete",
   "ADJUDICATION_v9.md:19-21: Z-S42 and Z-S44 GRADUATED"
  ],
  "remedy": "No act owed: owner disarm/lift carrier for Z-S41 and Z-S42, whose fix (CRPS-h-1) is drained and exercised on the served table.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S52",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CORRECTION of AMGT_CORPUS-Z-W2-S11's worked example (asked by 1.0.0_SA_CTO~Z, round-7 analysis s.3): the row says 8306_JP_Equity's 'Model NEW VERSION' column K 'is genuinely empty of numbers' below the K43 'Base Case' title; its own producer's rows read below K43 = [2028, 2108.7834, 1.3782161070420165]. The column is not empty; the row's conclusion (0 of 42 plausible selections) does not rest on this example.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S52",
   "ADJUDICATION_v11.md:23 and :88: Z-S52 GRADUATED, the contradiction raised by ADJUDICATION_v10 FINDING B is resolved on the record"
  ],
  "remedy": "No act owed: an owner correction of Z-W2-S11 worked example that leaves that row grade unchanged.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S56",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM of AMGT_CORPUS-Z-W1-S13 by its owner: the three tests that pinned what CRPS-l-1 changed on purpose were updated under the issuer's AMENDMENT 2 (the order's <paths> widened by the issuer), and the corpus suite reads green; the red suite never reached CLOUD.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S56",
   "b40840e09a amendment 2 of CRPS-l-1 grants the two test files; 6eaa7545ea updates the three tests",
   "5b0b728ab1 drain merges wk-crps10-1; bc50ea89cf records row Z-S56 disarming Z-W1-S13",
   "ADJUDICATION_v13.md:16: Z-W1-S13 and Z-S56 GRADUATED, corpus suite 409 passed"
  ],
  "remedy": "No act owed: owner disarm carrier for Z-W1-S13, whose three pinned tests were updated under AMENDMENT 2 and merged green.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S60",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM of AMGT_CORPUS-Z-W5-S5 by its owner: the five period-led ML_FP pillars the PDF reader missed are now read (order CRPS-p-5 AMENDMENT 1) and SERVED -- read_dossier ML_FP_Equity returns 5 pillars with text; ML_FP no longer serves ABSENT.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S60",
   "37cfc36d5f period-led lead rule; merged 34bbf74213 under pair; 247d2dace6 ledger-close records Z-W5-S5 DISARMED (Z-S60)",
   "lib/research/corpus/continuation.py:598-602 at HEAD f7ad5dc777: bold_first lead ending in a period is accepted",
   "ADJUDICATION_v17.md:47: Z-W5-S5 and Z-S60 GRADUATED"
  ],
  "remedy": "No act owed: owner disarm carrier for Z-W5-S5, whose period-led pillar fix is merged and served.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S65",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Hitachi's model-block derive (build_unit_map additive merge) changed SHARED field-level entries in integrations/bloomberg/research/field_map.json beyond adding Hitachi: 4 fields' unit_status/sign_status flip MEASURED -> 'UNRESOLVED-ON-6501 JP Equity: sampled magnitude 11962163.4 does not discriminate absolute vs millions', and 1 field's unit/sign changes SHAPE from a scalar ('MILLIONS'/'POSITIVE') to a per-security dict; the pair's condition 3 (only 6501 keys added, 0 changed) fails, so the delta is WITHHELD uncommitted.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S65",
   "7a42db923d worker fix (CRPS-t-2); merged c95be7d59a (2026-09-30T01:36Z), replay shared_changed 0",
   "integrations/bloomberg/research/build_unit_map.py:892 and :996 at HEAD f7ad5dc777: per_security_detail[security][\"exception\"] scoped to that security",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-t-2.unit-map-exceptions.md last status: complete",
   "ADJUDICATION_v21.md:21: Z-S65 GRADUATED, shared_changed 0, shared_removed 0, type_changed 0"
  ],
  "remedy": "CRPS-t-2 makes build_unit_map record an ambiguous name as a per-security exception and never change a shared field status or type.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T01:36Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S71",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "After RESAPP r53 ac-3 moved the slash-key objects, lib/research/corpus/dossier.py still reads model blocks at the RAW key (`:927`, `:966`: MODEL_BLOCK_POOL_PREFIX + security_key, no slash_safe_key), so BP/_LN and NG/_LN dossiers stay built from the kept 2026-09-25 raw-key blocks: aa-4 re-derived both on the encoded keys and write_one wrote 0 (inputs unchanged).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S71",
   "0c234ef97d worker fix (CRPS-ab-1): dossier model-block paths through slash_safe_key; merged per f2f77b132a",
   "lib/research/corpus/dossier.py:927-928 and :967-968 at HEAD f7ad5dc777: base built from slash_safe_key(security_key)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ab-1.dossier-slash-safe.md last status: complete",
   "aa35ffcdca (2026-10-01T00:43Z) ab-4 ledger CLOSED; ADJUDICATION_v31.md:34: Z-S71 GRADUATED, newest BP/NG dossiers reference the encoded blocks"
  ],
  "remedy": "CRPS-ab-1 routes both dossier.py model-block readers through slash_safe_key, and ab-4 leg d rewrote BP and NG through the fixed reader.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-01T00:43Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S86",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "/api/scoped/amgt/security/DE_US_Equity/thesis and /peers return 404 on the live API (ui-walk 20261003T235538Z, 3 each), where the 2026-10-01 walk 20261001T083453Z read both 200; Deere is the BA posture card's comparison name.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S86",
   "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-aq-4.covered-no-block-designed-reason.md last status: complete (AC2 c26 PASS local only)",
   "org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-aq-5.the-code-redeploy.md last status: pending; its cut-time comp-adversary reads c26 FAIL on the deployed function",
   "ADJUDICATION_v40.md:43: Z-S86 GRADUATED and routed to AMGT_RESAPP"
  ],
  "remedy": "The route fix AMGT-aq-4 is complete in code but the redeploy AMGT-aq-5 is pending, so the live API still answers 404 for DE_US_Equity until aq-5 lands.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": false
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S13",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-l-1 (unit_as_written + currency, METHOD_VERSION /3) breaks 3 tests in files outside its <paths>: test_dossier_case_body.py::test_method_version_is_bumped_to_2 (pins /2), test_dossier_case_body.py::test_case_census_prints_per_name_states_and_the_exact_summary_line (pins the census final line without the two new columns), and test_dossier_case_layouts.py::test_a_round_9_k5_table_is_unchanged (reads base['unit'], the key l-1 replaces). Not edited: the write grant excludes them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S13",
   "b40840e09a amendment grants tests/test_dossier_case_body.py and tests/test_dossier_case_layouts.py; 6eaa7545ea updates the three tests",
   "5b0b728ab1 (2026-09-29T05:46Z) drain merges wk-crps10-1 with the suite green",
   "lib/research/corpus/tests/test_dossier_case_layouts.py:125 at HEAD f7ad5dc777 reads unit_as_written; test_dossier_case_body.py:158-159 pins the current METHOD_VERSION",
   "ADJUDICATION_v13.md:16: Z-W1-S13 GRADUATED, corpus suite 409 passed"
  ],
  "remedy": "AMENDMENT 2 granted the two test files and the three pinned tests were updated, so the corpus suite is green on the merged trunk.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-29T05:46Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S25",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The ruled ZERO-DOMINATED rule (strictly more than half exact zeros, any key) moves 334 other figures (EQY_DPS 167, IS_DIV_PER_SHR 167: PER SHARE -> ZERO-DOMINATED) and breaks test_a_mostly_zero_dividend_yield_still_reads_percent (4 of 5 zeros pinned PERCENT); I exempted the dividend fields, which AC1 and AC2 forced.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S25",
   "b239301bb1 amendment 1 of CRPS-ac-1: ACCEPT ZERO_DOMINATED_EXEMPT as built",
   "integrations/bloomberg/research/build_unit_map.py:555 and :575 at HEAD f7ad5dc777: ZERO_DOMINATED_EXEMPT frozenset applied",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ac-1.zero-dominated-class.md last status: complete",
   "ADJUDICATION_v32.md:32: Z-W1-S25 GRADUATED"
  ],
  "remedy": "The issuer ruled ACCEPT on the dividend exemption set as built; no further act owed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S3",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-d-3's READ-ONLY reference `portal/src/pages/SecurityAnalysis/types.ts` is unreadable in this worktree: `.gitmodules` is a tracked, genuinely EMPTY blob at HEAD (no submodule URL for `portal` at all) and `portal/` itself is an empty directory with no cached `.git/modules/portal` objects in the shared git-common-dir -- so DOSSIER_INTERFACE.md's side-by-side was built from the task order's OWN inlined quotation of that file's relevant lines (the `drafted_sections`/`ThesisBundle` slot list the order already reproduces verbatim), not from a fresh read of the file.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S3",
   "69288c8ca0 maps portal and opal_ai in .gitmodules",
   ".gitmodules:5-7 at HEAD f7ad5dc777: [submodule \"portal\"] path = portal with its url (295 bytes, no longer the empty blob)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-3.composed-dossier.md last status: complete"
  ],
  "remedy": "No act owed for the cell; the cause (an empty .gitmodules with no portal URL) is gone at HEAD.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S7",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-f-1's ruled build (folders_in_records ALWAYS, research_universe ALWAYS present in some form) cannot pass AC3 as written: lib/research/identity/crosswalk.schema.json is additionalProperties:false and is NOT in this worker's <paths>, so every build now raises inside write_pool's own schema validation -- 15 of 119 identity-suite tests fail, all on the identical cause.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S7",
   "347e636dbb amendment 1 grants lib/research/identity/crosswalk.schema.json; 856cc1f005 lands the four optional properties",
   "lib/research/identity/crosswalk.schema.json:185 (folders_in_records) and :527 (research_universe) at HEAD f7ad5dc777",
   "eeb996b10e (2026-09-25T05:18Z) drain of CRPS-f-1; org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-1.crosswalk-denominator-disclosure.md last status: complete",
   "ADJUDICATION_v7.md:21: Z-W1-S7 GRADUATED through Z-S35"
  ],
  "remedy": "Issuer AMENDMENT 1 granted crosswalk.schema.json and the worker added the disclosure properties, so the identity suite passes again.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T05:18Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S13",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A per-security exception under a SCALAR shared field (e.g. BEST_SALES, shared unit 'MILLIONS', 6501 UNRESOLVED) is invisible to the readers: model_block_pull._resolved_unit/_resolved_sign return the shared scalar for ANY security, so the served figure for 6501 reads MEASURED 'MILLIONS' although its own map entry says the magnitude did not discriminate.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S13",
   "e099da5cf3 worker fix (CRPS-u-1); drained 186d1cc8da (2026-09-30T02:31Z), AC1 6501 UNRESOLVED with control 8035 MILLIONS",
   "integrations/bloomberg/research/model_block_pull.py:900-907, :938 and :957 at HEAD f7ad5dc777: _scalar_exception read by _resolved_unit/_resolved_sign",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-u-1.scalar-exception-readers.md last status: complete",
   "ADJUDICATION_v22.md:32: Z-W2-S13 GRADUATED"
  ],
  "remedy": "CRPS-u-1 makes the scalar unit/sign readers honour a per-security exception or non-MEASURED status, so 6501 BEST_SALES serves UNRESOLVED.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T02:31Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S5",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-e-1's AC1 check (checks/round3/e1_AC1.sh, read-only) runs pytest with -k \"evidence_table or deliverables_dir or association_expected\" against test_induction_run.py (29 tests total, 20 pre-existing from round 2/CRPS-d-5); pytest's own summary line ALWAYS inserts \", N deselected\" before \" in \" whenever -k excludes any test, so the <expect> regex (?m)^\\d+ passed in  can never match a -k run that leaves anything deselected -- unsatisfiable as written on any file that carries tests outside the filter.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S5",
   "03baefb8af (2026-09-24T19:35Z) issuer amendment widens AC1 expect to (?m)^\\d+ passed(, \\d+ deselected)? in",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-1.curated-evidence-induction.md:69 carries the widened expect; last status: complete",
   "2b3c2761e8 row Z-S22 disarm carrier cites Z-W2-S5; ADJUDICATION_v6.md:53 folds it"
  ],
  "remedy": "The issuer widened AC1 expect to admit the deselected clause, after which e-1, e-3 and e-5 AC1 matched.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S9",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-g-2's RULED text says read the Model block 'by the same selection rule the served reader uses (read that rule from scoped_amgt; do not invent a different one)', but scoped_amgt._read_model_block_pool has NO client parameter -- it always resolves its own client via _pool_client() (env-driven, defaults to a real boto3.client) -- so calling it directly from build()/current_inputs()/write_one() broke 4 of test_dossier.py's own offline tests (POISON: boto3.client called), because those pre-existing tests pass a StubS3Client for every OTHER read in the same call and have no way to also configure AMGT_POOL_ROOT for a helper they never call directly.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S9",
   "9162530ba0 worker fix; drained 9d90739261",
   "lib/research/corpus/dossier.py:895 at HEAD f7ad5dc777: _model_block_read(security_key, client)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-g-2.dossier-model-rows-from-block.md last status: complete",
   "ADJUDICATION_v8.md:26: Z-W2-S9 GRADUATED, consolidation item not a defect of the round"
  ],
  "remedy": "No act owed: the worker threaded the call client through a local selection reader and the g-2 order drained; the duplicated rule is a recorded consolidation item, not a defect.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W3-S6",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-j-3's premise fails on the real landed raw: over every refdata+histdata stamp of the six ABSENT keys (6861_JP, BZLFY_US, CAT_US, CSL_AU, PBR_US, TSM_US; 18 stamps) NO stamp carries a single IS_COMP_EPS_ADJUSTED fiscal_year_line_item figure, so the built stamp-census reads newest_carries 0 older_carries 0 none_carries 6 sum 6 and the new selection moves nothing (AC3 newly_served 0).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S6",
   "ddba870b96 drain of CRPS-j-3 (newly_served 0); org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-j-3.derive-stamp-carries-rule-inputs.md last status: complete",
   "ADJUDICATION_v12.md:30 and :106: Z-W3-S6 GRADUATED, closed on the CTO ruling @74e1eea534"
  ],
  "remedy": "No act owed: the stamp selection is inert on the real population and the six keys were ruled to serve ABSENT with the rule reason.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W4-S5",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-p-4's population sweep enumerated 95 research_dossier partitions but read_dossier accepts 93: BP-SLASH-_LN_Equity and NG-SLASH-_LN_Equity raise SlashSafeKeyError when the partition name is passed as a key.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S5",
   "ADJUDICATION_v18.md:29 and :42: read path sound, BP/ and NG/ dossiers read through the slash-safe path; Z-W4-S5 GRADUATED",
   "lib/research/corpus/dossier.py:927-928 at HEAD f7ad5dc777 resolves keys through slash_safe_key"
  ],
  "remedy": "No act owed: the read path is sound and the 93 of 95 came from the sweep passing partition names as keys.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W5-S5",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "ML_FP's source paragraph for 'Nearing turn in cycle' is EMPTY (the next line is the RISKS AND CONSDIERATIONS heading), so CRPS-p-5 serves thesis_pillars ABSENT; but the same INVESTMENT THESIS block carries five period-led pillars (e.g. 'Irreplaceable brand and pricing power.') the PDF pillar reader never sees.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W5-S5",
   "af9e934ae2 amendment 1; 37cfc36d5f period-led lead rule; merged 34bbf74213 under pair",
   "lib/research/corpus/continuation.py:598-602 at HEAD f7ad5dc777: lead_prefix ending in a period accepted",
   "247d2dace6 (2026-09-29T20:46Z) ledger-close: served delta ML_FP thesis_pillars 0 -> 5, Z-W5-S5 DISARMED (Z-S60)",
   "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-5.mlfp-pillar-body.md last status: complete"
  ],
  "remedy": "CRPS-p-5 AMENDMENT 1 added a period-led bold-first lead rule, and ML_FP now serves its five pillars.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-29T20:46Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S14",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by its owner of AMGT_CORPUS-Z-S13 (the 08:02Z served-output incident): both disarm conditions the row states are MET -- (1) the signed 09-24 object was restored and verified by 2.0.0_SA_COO~Z at 08:22:33Z (VersionId aTOpDZTTPlIzLLoeTFumB8KHmv6A0txG, 523,207 B, sha 9bd953b9, MEASURED 194; ledger amgt-crosswalk-0924-rollback CLOSED), and (2) the later induction write went through the UNIFIED builder (add_security @a125f8be8b on CLOUD via 8c75f4f90d: --batch one put per run, the universe/v1 input on every build) under a complete never-widen pair (COO half 4bbd43777c, CTO half 9a6472e58f) at 11:11:02Z, ONE conditional put, versions 22 -> 23, MEASURED 194 -> 214 with all 194 prior keys present. Z-S13 is legacy-shaped (hazard_standing/disarm_owner, no disarm clock) so it cannot advance in place under the row gate; this row is the disarm carrier and cites it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S14",
   "a125f8be8b closer(add_security): one pool put per run via --batch, universe/v1 input on every build; drained to CLOUD by 8c75f4f90d (ancestor of HEAD)",
   "4bbd43777c COO half + 9a6472e58f CTO half: the never-widen pair the 11:11Z put ran under",
   "ADJUDICATION_v5.md:28-29: Z-S13 GRADUATED, disarmed by Z-S14; Z-S14 GRADUATED as the carrier"
  ],
  "remedy": "Carrier closes: Z-S13's two disarm conditions were met by the unified add_security builder and one put under a signed pair.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S18",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The decomposition's production sequence (v2.0 s.5 drain duty 2: extract v2, typed, continuation, templates, dossier) OMITS the step that tells the last two producers WHICH names exist: `continuation._resolved_security_keys` and `dossier._resolved_security_keys` enumerate names from `backlog.read_latest()` -- the newest research-backlog SCAN VINTAGE in gold -- and that vintage was round 1's (33 RESOLVED), so the first pass after the re-ingest rebuilt `names 33` (continuation: names 33 rebuilt 1 existed 32; dossier: names 33 written 33) and produced NOTHING for the 20 newly resolved folders whose 94 reports are in bronze, extracted and typed. This seat's sequencing miss, not a producer's: `backlog --write` (a new scan vintage, never overwritten) must precede continuation and dossier; the corrected chain is running.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S18",
   "deliverables/2.0.0_SA_COO~X/evidence/production_sequence_corrected_20260924T130440Z.log:1-2,98 backlog --write first (new scan vintage put_performed True), :155 continuation names 53 rebuilt 20 existed 33",
   "ADJUDICATION_v5.md:32: Z-S18 GRADUATED -- corrected chain ran"
  ],
  "remedy": "The omitted backlog --write step was inserted before continuation and dossier and the corrected chain ran; no further act owed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S23",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The round-3 40-name fire (505fc14404) resolved 36 of 40; the other 4 -- Alphabet GOOGL US, Eli Lilly LLY US, Quanta Services PWR, UnitedHealth Group UNH US -- made NO Bloomberg call and stay UNRESOLVED, because add_security's idempotency check (_register_one -> _find_existing, add_security.py:455-465 @e640337205) matches ANY earlier registration row for the folder and prints already-registered, and these 4 folders carry earlier KEYLESS (UNRESOLVED) registration rows. The pre-flight modelled the builder (which supersedes a keyless row once a MEASURED row exists, @9ec1226a01) but not this request-side skip, so it predicted UNRESOLVED 0 where the producer delivers 4.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S23",
   "e772a89bad (2.0.0_SA_COO~Z): a keyless registration row no longer counts as already-registered; HEAD lib/research/identity/add_security.py:216-221 'if not row.get(\"security_key\"): continue'",
   "c79872b0ff fire: ONE re-mint under the pair (COO ae79d37b0c, CTO 35e4cb93ef) registering GOOGL, LLY, PWR, UNH and AMD",
   "ADJUDICATION_v6.md:54,56: Z-S23 GRADUATED, closed by the re-mint verified at 235/235 keyed; Z-S31 its carrier"
  ],
  "remedy": "add_security._find_existing now skips keyless rows and the re-mint registered the 4 folders; disarmed through carrier Z-S31.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T01:56Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S27",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "THE BLOOMBERG BLOCK IS A SIGNED-OUT TERMINAL SITTING AT A VISIBLE LOGIN WINDOW, and the recovery record's four cheap remedies are now ALL ELIMINATED on this instance: 8194 has no listener across 6 probes, a bbcomm restart produced a new pid with still no listener, the network to Bloomberg is provably open with its control, and bbcomm's own sockets are loopback-only. A visible top-level window titled 'BLOOMBERG: Login' exists at pid 19952. The sign-in is the remedy, no seat may complete it, and both submit attempts are already spent.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S27",
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S32 (1.0.0_SA_CTO~Z, 09-25T02:10Z): 8194 LISTENING=1, Z-S27's blocking cause is CLEARED, the held re-mint ran",
   "ADJUDICATION_v8.md:39-40,152,167: Z-S27 closed on Z-S32 after v6 carried it"
  ],
  "remedy": "The terminal sign-in was completed and 8194 reads LISTENING; Z-S32 dispositions the blocking cause as cleared.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S31",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by their owner of AMGT_CORPUS-Z-S23 (4 folders skipped on keyless rows) and AMGT_CORPUS-Z-S24 (16 ENRICH folders lost their form; ingest read 73): the re-mint @c79872b0ff registered GOOGL, LLY, PWR, UNH and AMD with 5 calls into crosswalk/v1/2026-09-25.json (VersionId 9af5o6BzvZOV.ERosdvtDt7az4CW9nzO): 94 of 94 live research folders carry a MEASURED record AND their own harvester form, twins 0, multi-claimed 0 of 564 forms, 234 of 234 prior keys; the re-ingest then read resolved_folders 94 with 0 unresolved files. Both rows are legacy-shaped (no disarm clock); this row is their carrier.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S31",
   "e772a89bad, 74e6a76e5c, b58d5c1d53 (2.0.0_SA_COO~Z builder fixes, all ancestors of HEAD); HEAD lib/research/identity/add_security.py:216-221",
   "c79872b0ff: ONE re-mint into crosswalk/v1/2026-09-25.json under pair COO ae79d37b0c, CTO 35e4cb93ef",
   "ADJUDICATION_v6.md:56: Z-S31 GRADUATED as the carrier for Z-S23/Z-S24"
  ],
  "remedy": "Carrier closes: the builder fixes plus one re-mint under a fresh pair met the Z-S23 and Z-S24 disarm conditions.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S35",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM by their owner of AMGT_CORPUS-Z-S34 (crosswalk.main's write path omitted the live list) and the f-1 worker's AMGT_CORPUS-Z-W1-S7 (schema not granted) and AMGT_CORPUS-Z-W1-S8 (AC3 expect vs 'subtests passed'), all the issuer's cut or a gap closed on the identity surface: amendments 1-2 (@347e636dbb, @e050dbf203), f-1 drained @eeb996b10e, 2.0.0_SA_COO~Z's write-path fix @5ef2158828, and ONE disclosure re-mint of crosswalk/v1/2026-09-25.json under a signed pair (COO @f5b0a47429, CTO @081f598b9f): versions 1 -> 2 (VersionId PoGljdVKce67e4GnBEY5wVab7wdkRJZd), folders_in_records 94 == research_folders_live 94 == the distinct source_row.folder count computed from the records, snapshot_stale_against_live True, research_universe.folders 94, records byte-equal to the before-version.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S35",
   "347e636dbb and e050dbf203: CRPS-f-1 amendments 1-2; eeb996b10e f-1 drain",
   "5ef2158828 (2.0.0_SA_COO~Z): crosswalk.main --write-pool passes research_folders; HEAD lib/research/identity/crosswalk.py:1466-1472,1492",
   "f5b0a47429 COO half + 081f598b9f CTO half for the one disclosure re-mint",
   "ADJUDICATION_v7.md:19-21: Z-S35, Z-S34, Z-W1-S7, Z-W1-S8 GRADUATED"
  ],
  "remedy": "Carrier closes: the f-1 amendments, the crosswalk.main write-path fix and one disclosure re-mint under a signed pair landed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S41",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "FWD-17 (b) IS VIOLATED, but not on the name that raised it: dossier.read_dossier picks the newest object by KEY NAME, as_of=<date>.<inputs_sha16>, so on a date holding several objects it serves the one with the GREATEST INPUTS HASH, not the last written. write_one then compares fresh inputs against that stale pick, finds them different, and writes again: 37 of 95 names carry a 2026-09-26 object whose inputs hash repeats an earlier object's -- a rebuild that WROTE on unchanged inputs -- and replaying history, 58 names were served a stale dossier in 86 windows of 3.4 to 19.3 hours. IMB_LN_Equity, the candidate, is NOT a violation: its three 09-24 objects differ on fund_form and typecast inputs, and its hash order happened to match time order.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S41",
   "7adb677b72 fix(CRPS-h-1) drained at dd82056420 (ancestor of HEAD)",
   "HEAD lib/research/corpus/dossier.py:1319-1333 read_dossier picks via _pick_newest (newest date, then greatest LastModified, :1285-1293)",
   "task-orders/AMGT_CORPUS.TO-CRPS-h-1.dossier-newest-is-last-write.md last <status>complete</status>",
   "ADJUDICATION_v9.md:18: Z-S41 GRADUATED -- serves the last write 95 of 95, exercised arm wrote 0 twice"
  ],
  "remedy": "CRPS-h-1 made read_dossier serve the last write on the newest as_of date (S3 LastModified), not the greatest inputs hash.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-26T14:44Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S45",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "h-5's served rewrite WOULD LAND ON 49 OF 95 NAMES, not 95: continuation objects are named <sha16 of {method_version, inputs}>, so METHOD_VERSION /2 writes a NEW object for every name -- but both readers (continuation.read_latest and substrate._pick_stored) return the FIRST key in sorted order whose `inputs` equal current inputs, and `inputs` does not carry the method version. A /1 and a /2 object with identical inputs then compete by hash order: measured read-only over the 95 resolved names, the readers would serve /2 (with terms) on 49 and keep serving /1 (no terms) on 46. The same defect class as Z-S41 on the next table over.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S45",
   "bd5d79f1b7 drain(CRPS-i-1): the continuation readers select the current method version (ancestor of HEAD)",
   "HEAD lib/research/corpus/continuation.py:992-1021 read_latest -> _select_stored(candidates, METHOD_VERSION); lib/research/corpus/substrate.py:121-134 _pick_stored takes current_method_version",
   "task-orders/AMGT_CORPUS.TO-CRPS-i-1.continuation-readers-select-method-version.md last <status>complete</status>",
   "cf9f8dce71 ledger-close: dossier rewrite landed 95 of 95, stale_pick 0; ADJUDICATION_v10.md:37 Z-S45 GRADUATED"
  ],
  "remedy": "CRPS-i-1 made both continuation readers prefer the current METHOD_VERSION among input-matching objects; served 95 of 95 on /2.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-26T19:03Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S53",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM BY HOLD of AMGT_CORPUS-Z-W1-S9 by its owner: this seat runs NO dossier --write (the round-8 served rewrite included) until a case rule reads the scenario table by case. The writer census is this seat alone (the Z-S46 census stands: dossier --write runs only in this seat's drain acts; no scheduled producer writes the table).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S53",
   "19458b6130 drain(CRPS-k-1): each case serves its own columns of the scenario table",
   "b98e09953e COO half + 9ffd945889 CTO half: the round-9 dossier rewrite pair",
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S54: the lift, names 95 written 95, heading_only 0",
   "ADJUDICATION_v12.md:27: Z-S53 and Z-S54 GRADUATED"
  ],
  "remedy": "The hold was lifted by Z-S54 after the table-aware case rule landed and the dossier rewrite ran under its signed pair.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S57",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM of AMGT_CORPUS-Z-W1-S14 by its owner: the two method-version tests the ruled /4 bump turned red were updated under the issuer's AMENDMENT 1 to CRPS-m-2 (e119939999); the corpus suite reads 438 passed on the merged trunk (b274848977).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S57",
   "e119939999 AMENDMENT 1 to CRPS-m-2; 1cfd1e6737 worker update; b274848977 chain drain (ancestor of HEAD)",
   "HEAD lib/research/corpus/tests/test_dossier_case_unit.py:110 and test_dossier_case_body.py:159 assert amgt-corpus-dossier/5 == dossier.py:144 METHOD_VERSION",
   "ADJUDICATION_v14.md:15: Z-W1-S14 and its carrier Z-S57 GRADUATED"
  ],
  "remedy": "Carrier closes: AMENDMENT 1 granted the two version-pinning tests, the worker updated them and the chain merged green.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S62",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARM of AMGT_CORPUS-Z-S59 by its owner: .tools/safe-merge.sh fixed at ccf2a27c6b (0.0.0_AB_MSTR~Z) -- a conflicted merge now records only HEAD..MERGE_HEAD plus unmerged paths; any other staged path is WARNed and refused on --continue.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S62",
   "ccf2a27c6b fix(safe-merge, 0.0.0_AB_MSTR~Z) names AMGT_CORPUS-Z-S59 (ancestor of HEAD)",
   "HEAD .tools/safe-merge.sh:340-351 HEAD..MERGE_HEAD snapshot with comm-based foreign-path WARN (refined after ccf2a27c6b's SIGPIPE defect, :341-344)",
   "ADJUDICATION_v19.md:27-28: Z-S59 and Z-S62 GRADUATED (landing read, not exercised)"
  ],
  "remedy": "safe-merge.sh now bounds the conflict state by HEAD..MERGE_HEAD and refuses foreign staged paths on --continue.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S66",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "AMGT_RESAPP yy-6 (6a940b02b8) makes crosswalk.main --write-pool UNION-FIRST over the served pool, but the other crosswalk/v1 writer, add_security (build at add_security.py:366, put at :401), still builds WITHOUT served=, so Z-S63's fork survives on the path the scheduled induction fire uses and on every later CLOUD-side registration: a pinned-checkout fire's names are dropped by the next add_security put from CLOUD.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S66",
   "fde642f9f6 AMGT-zz-1: the served-pool union sits inside crosswalk.write_pool; drained to CLOUD at 5b55a4ee1d (ancestor of HEAD)",
   "HEAD lib/research/identity/crosswalk.py:1336 def write_pool, :1362-1366 union reads _read_pool_latest(client)[0]",
   "be2cf27545 CTO half: amgt-induction-daily re-pinned at 33c1d096a3 carrying zz-1",
   "ADJUDICATION_v25.md:45: Z-S63, Z-S66 GRADUATED on the pinned union"
  ],
  "remedy": "AMGT-zz-1 moved the served-pool union inside crosswalk.write_pool so both crosswalk/v1 writers carry it.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-30T04:28Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S75",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DISARMS AMGT_CORPUS-Z-W1-S27: assembled.harness.cjs's model check is re-anchored (portal 54f3a252, on local DEV 209678ff) -- the SERVED arm's denominator is the fiscal figures on the sheet's rows (it also broke once CRPS-ad-1 removed the Other lines, wider than S27 named) and the ABSENT arm reads 'no model' without a presupposed pack.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S75",
   "portal 54f3a252 (2026-10-01) re-anchor, ancestor of portal DEV HEAD ec65c5d6",
   "HEAD portal/src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs:332,343 /\\bno model\\b/i, no pack phrase",
   "ADJUDICATION_v33.md:49-50: Z-W1-S27 and Z-S75 GRADUATED (harness non-runnable at DEV for an unrelated module alias)"
  ],
  "remedy": "assembled.harness.cjs re-anchored: the ABSENT arm reads 'no model' with no pack phrase and the SERVED denominator is the sheet's fiscal figures.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S10",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-j-1 rule 4 read literally ('write nothing only when method_version EQUALS METHOD_VERSION') would break test_dossier_newest.py::test_write_one_unchanged_against_the_last_write_not_the_greatest_hash, whose seeded documents carry no method_version; write_one treats an ABSENT method_version as inputs-only, a PRESENT different one as changed.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S10",
   "8945d6b4cb build(CRPS-j-1) method-aware no-op, merged c858a00330 (ancestor of HEAD)",
   "HEAD lib/research/corpus/dossier.py:1361-1366 only a PRESENT different method_version voids the no-op",
   "task-orders/AMGT_CORPUS.TO-CRPS-j-1.case-body-under-heading.md last <status>complete</status>",
   "ADJUDICATION_v11.md:24,89: Z-W1-S10 GRADUATED, stale_pick 0 of 95"
  ],
  "remedy": "Absent method_version keeps the inputs-only no-op by design; no stored object lacks one, so no act owed.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S14",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-m-2's ruled METHOD_VERSION bump to /4 breaks 2 tests in files outside its <paths>: test_dossier_case_unit.py::test_method_version_is_3 and test_dossier_case_body.py::test_method_version_is_bumped_to_2 (each pins /3). Not edited: the write grant excludes them.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S14",
   "e119939999 AMENDMENT 1 (<paths> gains the two test files); 1cfd1e6737 tests updated; b274848977 drain (ancestor of HEAD)",
   "HEAD lib/research/corpus/tests/test_dossier_case_unit.py:110 and test_dossier_case_body.py:159 match dossier.py:144 METHOD_VERSION amgt-corpus-dossier/5",
   "task-orders/AMGT_CORPUS.TO-CRPS-m-2.positional-read-of-blank-base-cells.md last <status>complete</status>",
   "ADJUDICATION_v14.md:15,53: Z-W1-S14 GRADUATED"
  ],
  "remedy": "AMENDMENT 1 widened CRPS-m-2's paths to the two version-pinning tests, which were updated; the corpus suite is green.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-29T08:22Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S26",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "AC2 (bound.cjs AD1) cannot read 4 of 4 once the Other-lines group is removed as the order's item 2 requires: tabs.harness.cjs check model_fiscal_rows_rendered demands every fiscal figure rendered (cells === fiscal, 97/165 for BA now).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S26",
   "6d1c707a0f amend(CRPS-ad-1 AMENDMENT 1): ruling on Z-W1-S26, grants tabs.harness.cjs",
   "HEAD portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:389-395 fiscal denominator filtered to the sheet's mnemonics and years",
   "task-orders/AMGT_CORPUS.TO-CRPS-ad-1.sheet-in-the-sharepoint-shape.md last <status>complete</status>",
   "ADJUDICATION_v33.md:48: Z-W1-S26 GRADUATED"
  ],
  "remedy": "ad-1 AMENDMENT 1 granted tabs.harness.cjs and re-scoped its denominator to the fiscal figures the sheet carries.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S4",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "d-4's own model treats workbook-only/empty as sub-reasons WITHIN resolved-but-no-prose ('resolved, but no dossier CAN exist'), but dossier.build()/write_one has no report-count floor and the drain's production sequence already ran dossier build unconditionally over all 53 resolved names before continuing this worker -- so on the real corpus 9 of the 10 workbook-only folders (plus the 1 empty folder is UNRESOLVED, not resolved) already carry a real, stored, all-fields-absent dossier and read dossier-served under the literal per-folder rule, leaving a disposition-scoped never_prose_named at 0 where AC2's own regex requires non-zero. I resolved it by computing never_prose_named as a STRUCTURAL cross-cut over every folder's own files, independent of disposition, which reproduces the corpus's re-measured 11 (10 workbook-only, 1 empty) exactly and satisfies AC2 without narrowing dossier-served or hiding any folder from the tri-state sum.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S4",
   "task-orders/AMGT_CORPUS.TO-CRPS-d-4.coverage-census-93-of-93.md last <status>complete</status>",
   "ADJUDICATION_v5.md:123 adjudicates AMGT_CORPUS-Z-W1-S4 (GRADUATED in the round-2 adjudication)"
  ],
  "remedy": "No act owed: the worker's structural never_prose_named census met AC2 without narrowing any disposition.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W1-S8",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "After ISSUER AMENDMENT 1 (the crosswalk.schema.json fix) landed, the identity suite runs fully green (119 passed, 0 failed) but AC3's <expect> regex '(?m)^\\d+ passed in ' still does NOT match the real output 'N passed, 2 subtests passed in Ns', because lib/research/identity/tests/test_crosswalk_universe.py uses unittest subTest (pre-existing, unrelated to CRPS-f-1) and pytest's own summary line reads 'N passed, 2 subtests passed in ...' rather than 'N passed in ...'.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W1-S8",
   "e050dbf203 amend(CRPS-f-1 amendment 2): AC3's expect admits ', N subtests passed' (ancestor of HEAD)",
   "HEAD task-orders/AMGT_CORPUS.TO-CRPS-f-1.crosswalk-denominator-disclosure.md:87 expect (?m)^\\d+ passed(, \\d+ subtests passed)? in; last <status>complete</status>",
   "eeb996b10e f-1 drain; ADJUDICATION_v7.md:21 Z-W1-S8 GRADUATED through Z-S35"
  ],
  "remedy": "AMENDMENT 2 widened AC3's expect to admit pytest's ', N subtests passed' clause; f-1 then drained complete.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-25T05:00Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S14",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "build_unit_map's own CLI (main --securities) and model_block_pull._ensure_unit_map feed build_entries different headers: the CLI passes the raw header (CIE_DES_BULK as a row-dict list, no BEST_ forecast values), the producer pre-joins CIE_DES_BULK and merges the FY1 bestdata row, so the CLI replay reproduces 209 of the 214 committed Hitachi additions; 5 measured_on entries (BEST_DPS, BEST_EBITDA, BEST_EPS, BEST_PE_RATIO, CIE_DES_BULK) come out as exceptions instead.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S14",
   "933855d474 build(CRPS-u-2) prepare_header; db3344a99c drain (ancestor of HEAD)",
   "HEAD integrations/bloomberg/research/build_unit_map.py:1080 def prepare_header, used at :1357",
   "task-orders/AMGT_CORPUS.TO-CRPS-u-2.cli-producer-header.md last <status>complete</status>",
   "ADJUDICATION_v22.md:33: Z-W2-S14 GRADUATED, 214 of 214 on replay"
  ],
  "remedy": "CRPS-u-2 added build_unit_map.prepare_header so the CLI feeds build_entries the producer's header; replay reproduces 214 of 214.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W2-S6",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "proof-of-spec-check.py's ENFORCE alignment (forward-2, cell_ref->decomp) refuses ALL FIVE round-3 CRPS-e-* instances as structurally INVALID: every e-* task order's <owned_cells>/<criterion cell_refs> uses the prefixed form 'CRPS-e-N' (matching CELL_ID_RE), but the round-3 decompositions/AMGT_CORPUS_DECOMP.md itself declares its cells bare ('e-1' .. 'e-5', no CRPS- prefix, only visible in a markdown table cell |`e-1`|), which CELL_ID_RE (requires a leading uppercase letter) cannot match -- decomp id space measures 0 regardless of instance content, so 'CRPS-e-1' cited by any criterion resolves to nothing.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W2-S6",
   "03baefb8af amend(round 3 cut defects): the decomposition rectangle cites CRPS-e-<n> (ancestor of HEAD)",
   "03baefb8af:org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md:25 row `CRPS-e-1`",
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S22: carrier, five round-3 instances VALID rc 0",
   "ADJUDICATION_v6.md:53: Z-W2-S6 folds with Z-S22 GRADUATED"
  ],
  "remedy": "The issuer's amendment prefixed the round-3 decomposition rectangle to CRPS-e-1..CRPS-e-5, and all five instances read VALID.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:35Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W3-S3",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CRPS-e-3's own AC2 (`sector_template --write`, live 218-report corpus) cannot complete rc 0 even with the fix built and committed: 5 of 9 business types (consumer-cyclicals+consumer-services, consumer-non-cyclicals, energy, healthcare, utilities) still raise gold.GoldImmutableError on the SAME pre-existing method_version=2 object Z-S17 already named (business_type=consumer-cyclicals+consumer-services/fbb482677a438d92.json), because that object was minted by the PRE-FIX code and still carries `total` in its stored body -- so the NEW code's total-free body for the SAME unchanged inputs differs from the STORED body under the SAME object name, and write-once gold correctly refuses. The order's own bound forbids the two ways out (no METHOD_VERSION bump; no S3 delete/overwrite), so this collision is not resolvable inside CRPS-e-3's paths.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S3",
   "03baefb8af amendment reverses e-3's no-METHOD_VERSION-bump ruling; 1266b834ec e-3 drain (ancestors of HEAD)",
   "HEAD lib/research/corpus/sector_template.py:97 METHOD_VERSION = \"3\"; :349-358 total never enters fields or the body",
   "task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md last <status>complete</status>",
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S22: --write rc 0 over 218 reports, 9 objects written once; ADJUDICATION_v6.md:53"
  ],
  "remedy": "The issuer reversed the no-bump ruling: METHOD_VERSION 2 -> 3 with total out of the body, and --write ran rc 0.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-09-24T19:48Z"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W3-S7",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CRPS-l-4 premise differs: the underscore key does not fail to resolve a stamp; security_key() maps both forms to the same sec_key so the stamp resolves, and the failure is that the landed refdata/histdata are keyed by the Bloomberg string, so the underscore string indexes an empty block.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W3-S7",
   "80060666e7 CRPS-l-4 refusal; 120ff9b27f drain (ancestor of HEAD)",
   "HEAD integrations/bloomberg/research/model_block_pull.py:1961 CRPS-l-4 unresolvable-key check; tests/test_cases_report_refuses_unresolved.py present",
   "task-orders/AMGT_CORPUS.TO-CRPS-l-4.cases-report-refuses-unresolved-key.md last <status>complete</status>",
   "ADJUDICATION_v13.md:19,77: Z-W3-S7 GRADUATED (planted_underscore rc 2)"
  ],
  "remedy": "CRPS-l-4 makes cases-report refuse a key with no entry in the landed raw, whole invocation, before computing.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-W4-S8",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Running the integrations/bloomberg/research suite in a worktree rewrites the tracked file integrations/bloomberg/research/field_map.json (1013 insertions, 110 deletions after one full run), a file outside this order's paths; the worker restored it byte-for-byte from HEAD before committing.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S8",
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-W4-S9: corrects the attribution to test_model_block_pull_stage_derive_key",
   "24f7912522 fix(CRPS-z-4): the stage_derive test stubs _ensure_unit_map (ancestor of HEAD); HEAD lib/research/identity/tests/test_slash_safe_key_sites.py:457",
   "task-orders/AMGT_CORPUS.TO-CRPS-z-4.slash-safe-key-sites.md last <status>complete</status>",
   "ADJUDICATION_v27.md:43: Z-W4-S8, Z-W4-S9 GRADUATED"
  ],
  "remedy": "Superseded by Z-W4-S9: the writer was z-4's own new test, now stubbed so it never writes field_map.json.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "closed": true
 },
 {
  "id": "AMGT_CORPUS-Z-S85",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "schedule_induction.ps1 resolves the task's interpreter as the FIRST python on PATH, and PATH now resolves C:/Program Files/Python314/python.exe (no blpapi) ahead of Python311 (blpapi + boto3 + pyarrow): a plain -Register today would silently re-register amgt-induction-daily on an interpreter that cannot reach Bloomberg.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S85",
   "61c58e31bc drain(CRPS-ak-2): interpreter named, never PATH alone, blpapi REFUSE (ancestor of HEAD)",
   "HEAD lib/research/corpus/schedule_induction.ps1:22-28 precedence header; :95-102 REFUSED on a failed import blpapi",
   "task-orders/AMGT_CORPUS.TO-CRPS-ak-2.repin-explicit-interpreter.md last <status>complete</status>",
   "ADJUDICATION_v41.md:59: Z-S85 DISARMED; the live task names Python311"
  ],
  "remedy": "CRPS-ak-2 makes schedule_induction.ps1 name its interpreter (-Python, else the live task's) and refuse one that cannot import blpapi.",
  "owner": "2.0.0_SA_COO~X",
  "round": "v41",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~X",
   "round": "v41"
  },
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~X",
   "at": "2026-10-04T01:29Z"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
