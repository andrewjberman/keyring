# IRPT_FNTEND ROUND 8 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer). This work was done in a fork of this seat's session (same serial, same model).

**Input:**
- `2.0.0_SA_COO~F`'s drain-end packet, msg 96994. It reports 4 of 4 orders complete and drained: FE-s-46, FE-s-47, FE-s-48 and
  FE-s-49.
- The late row IRPT_FNTEND-S68, filed after that packet. The parent session directed that it be carried here.

## 0. CONCLUSION

- **Every row has a carrier.**
  - The 18 rows new since issuance 57cb17e329 are carried by C-S99..C-S107 @f5a69ab530.
  - The between-rounds row S68 is carried by C-S108 @23cad64541.
  - Carrier-less at HEAD: 0 of 246.
- **All 4 judgment criteria PASS**, each with a named qualification: F46-AC8, F47-AC11, F48-AC7 and F49-AC15.
- **10 items graduated.** REMEDIATION_v5.md @db4e444efb has 10 rows, round v8, with no route. The standing census reads 0 missing.
- **The finding for 1.0.0_SA_CTO and Andrew: the Investor Reporting portal gate is the ONLY admin wall.**
  - The backend is a firm wall. A partner firm's admin who calls the API directly would be served its own firm's data.
  - No endpoint serves yet: IRPT_BCKEND B15 builds the routes.
  - No PRD and no FWD names a backend admin wall.
  - It is carried on S66's remediation row as a decision, not as a defect.

## 1. L8 -- THE COMPILE

**Instrument:** every JSON fence of both investigation files, read at two git states. This was re-asserted in the generator,
`scratchpad/irpt_r8_gen.py`, before any write.

**At the census** (HEAD c6d652a6dc; INVESTIGATION_v2.md @5e5f074588):
- 245 ids at HEAD minus 227 at the issuance 57cb17e329 = 18 new, and 0 lost.
- Over both adjudication files (107 rows before this round), the carrier-less set equals those 18 exactly.
- The highest prior carrier is C-S98.
- Classes: 3 BLOCKING/INERT, 13 OBSERVATION/INERT, 2 OBSERVATION/ARMED.
- Task orders at HEAD: 49 of 49 `complete`.

**S68, a between-rounds row:**
- Filed @be5a2a5441 by 2.0.0_SA_COO~F (09:42:24Z), after the packet and after the census, and before any round-9 order.
- The gate's L10 limb refused the first REMEDIATION_v5 on it (section 6).
- Re-census at HEAD ab6c6de254: 246 ids, and S68 is the one carrier-less id (highest carrier C-S107).
- 2.0.0_SA_COO~F's 97028, as named by the parent session, reports the same: it added nothing else.

## 2. THE PER-ID LEDGER -- EVERY ROW, ITS DISPOSITION AND ITS CARRIER

| id | class / standing | disposition | carrier | remediation row (owner, state) |
|---|---|---|---|---|
| S66 | BLOCKING / INERT | GRADUATED | C-S104 | 1.0.0_SA_CTO, OPEN (the backend-wall half) |
| S67 | BLOCKING / INERT | DISMISSED_WITH_REASON | C-S100 | -- |
| W1-S71 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S101 | -- |
| W1-S72 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S101 | -- |
| W1-S73 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S101 | -- |
| W1-S74 | OBSERVATION / ARMED | GRADUATED | C-S103 | 2.0.0_SA_COO~F, REMEDIATED; disarm DISARMED 07:51:46Z |
| W1-S75 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S101 | -- |
| W2-S34 | BLOCKING / INERT | DISMISSED_WITH_REASON | C-S100 | -- |
| W2-S35 | OBSERVATION / INERT | GRADUATED | C-S106 | 2.0.0_SA_COO~F, OPEN |
| W3-S36 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S102 | -- |
| W3-S37 | OBSERVATION / INERT | GRADUATED | C-S105 | 1.0.0_SA_CTO, OPEN |
| W3-S38 | OBSERVATION / INERT | GRADUATED | C-S105 | 1.0.0_SA_CTO, OPEN |
| W3-S39 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S102 | -- |
| W3-S40 | OBSERVATION / ARMED | GRADUATED | C-S103 | 2.0.0_SA_COO~F, REMEDIATED; disarm DISARMED 07:51:46Z (owner 0.9.0_WK_IRPT_FNTEND~1) |
| W3-S41 | OBSERVATION / INERT | GRADUATED | C-S106 | 1.0.0_SA_CTO, OPEN |
| W4-S18 | OBSERVATION / INERT | DISMISSED_WITH_REASON | C-S102 | -- |
| W4-S19 | OBSERVATION / INERT | GRADUATED | C-S107 | 1.0.0_SA_CTO, OPEN |
| W4-S20 | OBSERVATION / INERT | GRADUATED | C-S107 | 2.0.0_SA_COO~F, OPEN |
| S68 | OBSERVATION / INERT | GRADUATED | C-S108 | 1.0.0_SA_CTO, OPEN (cell (A), round-8 analysis) |

The grade record is C-S99, with 4 entries in `grades`. In all: 19 ids, 10 GRADUATED and 9 DISMISSED_WITH_REASON.

**Why each dismissal:**
- **S67 and W2-S34** are closed in drained code at portal DEV 10c2f07d, under FE-s-49 amendment 1 (1.0.0_SA_CTO 96961 (a)).
  - `src/lib/firmAccess.ts` lists `/investor-reporting` 0 times, against 3 at 1f3ce9f0; the numstat is +0 -3.
  - `fe-s-14/allowlist.test.ts` is in FE-s-49's `<paths>`.
  - `admin-gate.test.ts:606` declares F49-AC10 and closes with `}, 20109)` at :716. That is 3 x 6703, the highest of the 6
    costs in `fe-s-49/recorded-costs.json`.
- **W1-S71, W1-S72, W1-S73 and W1-S75** are records, each verified at DEV 90d71d9e.
  - W1-S72 and W1-S75 are wording defects of the issuer's (owned in 96994). Neither moves a verdict.
  - For W1-S75: amendment 1's two sentences cannot both hold by measurement alone, since 18891 ms predates the ledger. The
    worker's BOOTSTRAP carry is the one reading that meets both.
- **W3-S39** is closed in drained code: adapt.ts:307 keeps the document's own reason first. **W3-S36 and W4-S18** are records
  of an order's wording.

## 3. L9 -- THE FOUR JUDGMENT CRITERIA

**What this seat ran and read:**
- `proof-of-spec-check.py <instance> <ids> --governing-order <order>` on the shared tree, not a worker's worktree. It reads
  `VALID (rc=0)` on 4 of 4. The logs are `scratchpad/posc_r8_FE-s-4{6,7,8,9}.log`.
- The portal, read with `git show` at DEV, because the portal is frozen. **This seat ran no `bun` test, browser or dev
  server.** Every run figure below that is not a source line is the worker's or the issuer's, and is named as such.

Instances:
- F46-AC8: `...~1/IRPT_FNTEND.TO-FE-s-46....proof_of_spec.json@1e8997ec6d`
- F47-AC11: `~3 ...@0a49c55855`
- F48-AC7: `~4 ...@a42c7e05df`
- F49-AC15: `~2 ...@a018979694`

### F46-AC8 -- MET WITH A NAMED QUALIFICATION

**Bar:** "a loaded box can no longer turn a later cell's census red through these two files, and every timeout is sized from
a measured cost."

**Read at DEV 90d71d9e** (identical at 10c2f07d):
- 8 changed timeouts: `window.test.ts:302 17625`, and `one-writer.test.ts` :436 20952, :452 11013, :590 20907, :626 15138,
  :764 21000, :779 19266 and :869 56673.
- The diff 1f3ce9f0..90d71d9e is 1+7 lines. The `}, 90000)` at one-writer :539 predates the cell.

**The committed ledger** (`fe-s-46/recorded-costs.json`: 24 runs, 16 tests, 707 costs):
- 8 of 16 tests have a highest cost of at least 2500 ms.
- 7 timeouts are exactly 3 x that cost.
- F40-AC5's is the order's named floor, 3 x 5875 (F41-AC2's control, run B01; `timeouts.test.ts:161`), against its own
  highest cost of 5735.
- All 8 are at or under 60000.

**The census measures nothing:**
- `timeouts.test.ts:66` `const LOAD = env.IRPT_FE_TIMEOUT_LOAD === '1'` gates every load arm.
- F46-AC6 prints 10 of 10 spawned processes: 8 git reads and 2 seeded scratch runs.

**Qualifications:**
1. "Can no longer" is bounded, not absolute. A load that triples a test's highest recorded cost still turns it red.
2. Every committed timeout stands on a carried BOOTSTRAP run: B01-B12, 35 costs. None stands on a run of the load path as
   it now stands. B03 and B04 carry a day-only date (W1-S75).
3. F41-AC5's control has 3327 ms of headroom under the cap. A committed cost above 20000 ms therefore has no legal timeout.
   This is W1-S74's residual, and only an opt-in load run plus a commit can reach it.
4. The class recurred outside these two files, in FE-s-49 (S67).

### F47-AC11 -- MET WITH A NAMED QUALIFICATION

**Bar:** "the adapter supplies the reason on the no-status path, the validator is unchanged, and no stated state carries it."

**Read at DEV f28fcc44** (identical at 10c2f07d):
- `contracts/adapt.ts:176` `NO_STATUS_REASON = 'The response carried no status stating its state, so its state is unknown.'`
- `:299` `const statedState = status?.state ?? null`
- `:307` `partialReason: statedState === null ? (current.partialReason ?? NO_STATUS_REASON) : current.partialReason`

So the reason is supplied only when no state is stated, and the document's own reason comes first (amendment 1, 96947).
`validate.ts` is one blob, 4fc0a042ae9c, at 1f3ce9f0, f28fcc44 and 10c2f07d. The worker's arms held 18 of 18 and 11 of 11.

**Qualification:** amendment 1 routed two excluded paths to the round-8 analysis, and both are graduated:
- W3-S37: a status member with no state keeps a reasonless default on its own availability.
- W3-S38: status-summary and status-job carry the reason on a document whose data says PARTIAL.

### F48-AC7 -- MET WITH A NAMED QUALIFICATION

**Bar:** "a cohort value the panel declines to assert reads 'withheld' at every render site, never 'unknown', and a value the
producer asserted is unchanged."

**Read at DEV ad732941** (identical at 10c2f07d):
- `header/ScopeSummary.tsx:120` is the one render site of a non-authoritative CohortFact. It builds `${c.axis}: withheld`
  under "Cohort (not asserted)".
- The worker's census finds 1 site. F48-AC3 holds the asserted path byte-identical.

**Qualification:** Holdings still renders a non-authoritative classification's partitions as 'unknown'
(`tabs/holdings/slices.ts:102` @10c2f07d), as the contract's own comment directs.
- It is not a CohortFact, so the bar's letter does not reach it. Whether RULING W does is 1.0.0_SA_CTO's call (W4-S19).
- The fixture prose at `fixtures/index.ts:77` is stale (W4-S20).

### F49-AC15 -- MET, WITH THE BACKEND-WALL ANSWER NAMED

**Bar:** "no client or partner-firm user, admin or not, reaches Investor Reporting or sees its nav item through the portal; no
allowlist grants what the gate refuses; the three gate hunks match c29a8b86; and the backend census says whether the UI is the
only wall."

**Read at DEV 10c2f07d:**
- `App.tsx:96` the nav item carries `requiresAdmin: true, requiresTier: 'internal'`.
- `:423` and `:575` wrap both routes in `<ProtectedRoute requireAdmin requireInternal>`.
- `ProtectedRoute.tsx:39` refuses role != admin, and `:44` refuses firmId != opal-capital.
- The nav filter's `requiresTier` is applied at :320 and :336.
- The allowlist has 0 entries.
- The nav line and both route lines equal c29a8b86's, 3 of 3, by this seat's own line read.
- The worker's figures: partner admins refused 6 of 6, non-admins 8 of 8, and the nav shown to 1 of 8 identities.

**The census's answer, re-read by this seat at workspace HEAD:**
- `_scope/resolve.py:186-187`: a caller with role=admin and any verified firm resolves as FIRM_OPERATIONS.
- `:193`: an advisor resolves as FIRM_ADVISOR.
- `_authz/served.py:575-576`: the only refusal is an absent verified firm. 0 lines name x-user-role or opal-capital.
- `_authz/enforce.py:272`: the only other refusal is UNKNOWN.

So the portal gate is the only admin wall. This is a source reading (vintage @6806f529ac), not a live call.

## 4. THE STANDING CHECKS (a) TO (e)

**(a) The Investor Reporting gate: role plus tier, both routes, the nav, the allowlist, fe-s-14. HOLDS at DEV 10c2f07d.**
- Role plus tier: `requireAdmin` tests role (:39) and `requireInternal` tests firmId opal-capital (:44), on both routes.
- The nav carries both predicates.
- The allowlist entries are removed: 3 -> 0, numstat +0 -3.
- fe-s-14 is granted and re-pointed: +0 at :112, -3 at :113.

**(b) W2-S35's control. CONFIRMED, graduated.**
- `fe-s-14/allowlist.test.ts:126` still refuses only `startsWith('3\t0\t')`, against FE-s-14's old baseline (:120, a
  working-copy diff).
- The re-pointed test (:102) reads committed trees and asserts +0 -3. A reader stuck at `0<TAB>3` passes both arms.
- It is INERT: other instruments confirm 0 of 3 entries. The remedy is a one-line re-point in the next cell granted that file.

**(c) The disarms of W1-S74 and W3-S40. SEEN IN CODE at DEV 90d71d9e**, committer time 2026-09-15T07:51:46Z.
- `timeouts.test.ts:66` gates every load and ledger arm.
- F46-AC3's bound reads the committed ledger (:708).
- `one-writer.test.ts:869` closes F41-AC5's control with `}, 56673)`.
- Both are recorded as `disarm` DISARMED on REMEDIATION_v5, and neither is recorded in prose.

**(d) W1-S75, F49-AC13, and the backend wall:**
- **W1-S75:** the ledger has 24 runs, 12 of them carried (B01-B12, 35 costs). B03 and B04 read "day only". Dismissed as an
  issuer wording defect; carried in F46-AC8 qualification (2).
- **F49-AC13:** 20109 = 3 x 6703, the highest of 6 costs in `fe-s-49/recorded-costs.json`. The census run times nothing.
- **The backend wall: does any FWD or PRD claim one? NO.**
  - `IRPT_FNTEND_PRD.md` @d1479bc5f0 (42005 bytes) and `IRPT_BCKEND_PRD.md` @b8e98d5a4d (97323 bytes) carry 0 tokens matching
    `\badmin\w*` (case-insensitive).
  - 4 of IRPT_BCKEND's 80 FWD lines match role or internal, and this seat read all 4. They cover identity vocabulary
    (`roles.ts`, "vocabulary only"), per-firm S3 prefix permissions, and YCharts ownership. None is an admin wall.
  - The decomposition @HEAD, line 1867 (R8.9, Rule 24(iv)), says: "Does NOT move: the backend's own admin gating".
  - So the UI-only wall contradicts no ratified outcome. Whether Andrew's condition 2 ("no clients are allowed to see that")
    needs a backend wall before B15 serves is a decision, carried on S66's row for 1.0.0_SA_CTO with Andrew's word.

**(e) The overlap with 2.0.0_SA_COO~D's feature branch gate.**
- **The branch:** `feature/d13-visual-elevation`, tip 46932888 (2.0.0_SA_COO~D, 05:40:44Z).
- **The gate lines agree.** Its nav line (:99) and route lines (:424, :576) equal DEV 10c2f07d's, 3 of 3. They are also
  equal at c29a8b86, 3 of 3. 46932888's later App.tsx change adds only a `usePortalContent()` warm, which is not a gate hunk.
- **10c2f07d is NOT in the branch:** is-ancestor rc=1, with merge-base control rc=0; the merge base is 787015e83b.
  - The branch and its merge base each list `/investor-reporting` 0 times in firmAccess. So the branch adds no grant, but it
    also lacks FE-s-49's tests and the fe-s-14 re-point.
  - 1.0.0_SA_CTO~A's `PREPARATION.md:116` @87cc999027 (notice 96996) requires 10c2f07d to be an ancestor of any promotion
    candidate. A candidate cut from the branch alone fails that test.
- **2 files a merge must reconcile.** The branch changes 169 files since the merge base. 4 are Investor Reporting files,
  from 0.9.0_WK_DSGN_REBRND~1's a65b939a and 15c2cb7f. DEV 10c2f07d also changed 2 of them since the merge base:
  - `tabs/analysis/StageDisplay.tsx`
  - `tabs/analysis/VariantSelector.tsx`

  This seat ran no merge-tree, because it would write objects into the frozen portal.
- **The merge now exists.** Portal DEV 43f18c17 is 0.0.0_AB_MSTR's promote integration (09:30:34Z); it is also origin DEV at
  10:08:08Z. It contains both 10c2f07d and 46932888 (is-ancestor rc=0 each). At 43f18c17:
  - the nav line (:99) and both route lines (:424, :576) equal 10c2f07d's, 3 of 3;
  - firmAccess lists `/investor-reporting` 0 times;
  - the 2 shared files carry 0 conflict-marker lines;
  - `fe-s-49/admin-gate.test.ts`, `fe-s-14/allowlist.test.ts` and `fe-s-46/recorded-costs.json` equal 10c2f07d's.

  Whether the merged content of the 2 shared files is right was not evaluated.

## 5. THE CARRIED ITEMS (packet 96994)

1. **W3-S37 and W3-S38** are graduated to the round-8 analysis, as amendment 1 routed them (C-S105).
2. **W2-S35** is confirmed and graduated (C-S106). See (b).
3. **W1-S75** is dismissed as a record, and carried in F46-AC8's qualification. See (d).
4. **F49-AC13** is confirmed: 20109 = 3 x 6703.
5. **F49-AC10's backend census** is confirmed by a source read. The portal gate is the only admin wall; no PRD names one.
   See (d).

## 6. THE REMEDIATION AND THE CENSUS

**The first REMEDIATION_v5 commit was REFUSED** by safe-commit (rc=1). The surprise-row gate's L10 limb read
"1 of 246 investigation item(s) under IRPT_FNTEND are NOT dispositioned ... IRPT_FNTEND-S68" against all 9 new rows.
- The bytes were held (17912 bytes, sha256 da11e389ed7b8ae5), and no override was used.
- On the parent session's direction, C-S108 then carried S68.
- **The mechanism was re-derived by this seat:**
  - `fe-s-13/gen-wire.ts:107-108` @10c2f07d hashes its text with no line-ending normalization.
  - `:293` digests the schema text, which it reads with `readFileSync(..., 'utf8')` at :485.
  - `generator.test.ts:77` normalizes only the committed file, and :79 compares.
  - In python, a different instrument from the filer's sha256sum: schema blob 4dd7ecd253 is f06c0029cd20 as LF and
    c83ce02d14c1 rendered CRLF. `StatusEnvelope.ts:5` carries the CRLF value.
- The 9 held rows were reused unchanged, and S68's row was added.

**REMEDIATION_v5.md @db4e444efb:**
- 10 rows, round v8. No row carries `route` or `loop_target`.
- 8 OPEN: 1.0.0_SA_CTO holds S66, W3-S37, W3-S38, W3-S41, W4-S19 and S68; 2.0.0_SA_COO~F holds W2-S35 and W4-S20.
- 2 REMEDIATED: W1-S74 and W3-S40, each with `disarm` DISARMED at 2026-09-15T07:51:46Z under its own row's disarm owner.
- `closed` is false on all 10.

**THE STANDING CENSUS, read at HEAD db4e444efb from the committed files.** The adjudication files are read in numeric
version order, and each id takes its latest disposition:

    STANDING CENSUS at HEAD: 71 graduated (latest disposition over 264 adjudicated ids) minus 88 remediation ids over 5 files = 0 missing []
    CARRIER-LESS at HEAD: 0 of 246 investigation ids over 2 files

## 7. GATE FACTS, COMMITS, PUSH STATE

**Commits** (each authored 3.0.0_SA_CVO via `.tools/safe-commit.sh`, in the foreground):
- **f5a69ab530**: ADJUDICATION_v2.md, C-S99..C-S107. The old 170824 bytes are an exact prefix of the new 195315 (+272, -0).
  - surprise-row-gate: 9 new rows of 63 checked, OK.
  - missions-tree-check: 0 violations.
  - The surprise corpus matched its 4-known baseline.
- **refused (rc=1)**: REMEDIATION_v5.md, 9 rows. The L10 limb refused on S68, 1 of 246 undispositioned. The bytes were held,
  with no override.
- **23cad64541**: ADJUDICATION_v2.md, C-S108. Exact prefix, 195315 -> 198485 bytes (+35). 1 new row of 64 checked, OK.
- **db4e444efb**: REMEDIATION_v5.md, 10 rows. The L10 precondition was admitted for all 10 rows: "49 task order(s) at HEAD
  on both roots, 0 open; 246 investigation item(s) across 9 channel file(s) in the index, 0 undispositioned".
  missions-tree-check: 0 violations.
- **This record and the round-8 step log**: their own commit, named in the report.

**jsonschema Draft 7:** 0 violations on the 10 carriers (investigation schema) and the 10 remediation rows (remediation schema).

**Push state, measured by `git ls-remote` at 10:08:08Z:**
- origin/CLOUD = 6a5b276f8b. f5a69ab530, 23cad64541 and db4e444efb are LOCAL: each is an ancestor of local HEAD and not of
  origin.
- Portal origin DEV = 43f18c17, which is also local DEV. It is 0.0.0_AB_MSTR's integration and contains 10c2f07d (rc=0).
  This seat does not push.

## 8. NOT CLAIMED, NOT EVALUATED

- **No test run by this seat.** No `bun` test, browser or dev-server run: the portal is frozen and a dev start writes into
  the main checkout. The run counts quoted are the worker's or the issuer's.
- **No live backend read.** "No endpoint serves yet" rests on the source comment at `investor-reporting.ts:14` @10c2f07d
  ("the /api/scoped/investor-reporting/* routes DO NOT EXIST yet (IRPT_BCKEND B15 builds them)"). No AWS read was made.
  The backend-wall reading is from source at the shared boundary, not per endpoint and not EXERCISED.
- **The 2 Investor Reporting files that the branch and DEV both changed** were read at 43f18c17 only for conflict markers,
  of which there are 0. Their merged content was not reviewed (see (e)).
- **Production consumers of W3-S37 and W3-S38:** whether any renders those values was not read.
- **Messages read on disk:** 96994 only. 97009, 97020 and 97028 are cited as the parent session named them. 96996 is cited
  as `PREPARATION.md` records it.
- **Chronology:** the step log's times are to the minute from tool order where no instrument stamped them.
