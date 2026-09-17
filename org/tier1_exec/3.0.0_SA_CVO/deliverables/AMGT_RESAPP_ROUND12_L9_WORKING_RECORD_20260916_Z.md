# AMGT_RESAPP round 12 -- CVO L8/L9 working record (not the adjudication document)

**Seat:** `3.0.0_SA_CVO~Z`. **Opened:** 2026-09-16 ~23:15Z, after the 7:10 PM ET hold lifted (msg 23491).
**Vintage:** HEAD `c237ba8546` on SITEZ, LOCAL. **Round state at this vintage:** 10 of 18 orders terminal
(rk-1, rk-2, rk-3, rk-4, rk-5, rk-8, rk-9, rk-10, rk-11, rk-13); open rk-6, rk-7, rk-12, rk-14, rk-15, rk-16,
rk-17, rk-18.

**What this file is.** A durable record of L9 progress, so a reboot or a context loss does not cost the grades
already made. The grades and planned dispositions below are TRANSCRIBED into
`surprise-channel/adjudications/ADJUDICATION_v12.md` at drain-end, as rows `AMGT_RESAPP-Z-C-S273` onward, in the
same act as the slug. Nothing here dispositions an item: the gate reads only the adjudication document.

## 1. L8 intake census

The census is the row gate's own resolver (`.tools/surprise-row-gate.py _latest_dispositions`), not a hand count.
A first hand count read 56 open items; the gate reads S100 and S101 as already dispositioned, so that count was
wrong and is not used.

| | count |
|---|---|
| investigation items | 305 |
| open (latest carrier UNDER_INVESTIGATION) | 55 |
| grouped below | 55 (0 missing, 0 extra, 0 duplicates, checked by set subtraction) |

**A. Rows on TERMINAL orders (facts settled; dispositionable now, 37).**

| order | items |
|---|---|
| rk-1 | W23-S1, S123 |
| rk-2 | W24-S1, W24-S2, S111, S112, S113, W24-S3, S128, W24-S4, W24-S5 |
| rk-3 | W26-S1, W26-S2, W26-S3, W26-S4, S118, S125 |
| rk-4 / rk-13 | W25-S1 .. W25-S9, S115, S116, S117, S120, S130 |
| rk-8 | W23-S2, W23-S3, S131 |
| rk-9 | W27-S1, W27-S2 |
| rk-10 | W28-S1 |

**B. Rows bearing on OPEN orders (wait for the drain, 11).**

| order | items |
|---|---|
| rk-6 | W24-S6 (ARMED, print route), S132 |
| rk-7 | S122, S124, S126 |
| rk-12 | S134 |
| rk-14 | S133, S135 |
| rk-15 / rk-16 | S127 |
| rk-17 | S136, S137 |

**C. Seat and process rows (7).** S108, S109, S110 (round-11 carry), S114 (the checker's parse-skip), S119 and
S129 (the chatter schedule ENABLED -- the CTO carried it to the L10 as a bounds question), S121 (the issuer's
dry run of queued criteria).

## 2. Judgment criteria on terminal orders

### rk-11 AC3 -- MET

The question: is each breach recorded as it happened rather than tidied, and is the forward mechanism written so
a later cut can carry it. Read `ledger/PRESERVED_BREACHES_ROUND12.md` (11,992 B, commit `b4b07dc092`) against the
four source rows and against round 11's own adjudications of them (C-S235, C-S238, C-S253, C-S261).
- **W22-S2:** 4 credits for BA against 2, 12 for the cell against 10. The record says so in those numbers; its
  "no single run exceeded the bound" sentence is true and does not replace the cell total.
- **W19-S16:** the prior item values are stated as UNKNOWN, matching C-S235 ("before values were not captured").
- **W19-S19:** the apply ran under an entry naming no rollback, stated plainly; the record adds that
  `deploy_ledger.py` has no add-leg verb, which explains the mechanism and does not excuse it.
- **W20-S14:** C-S253 and the source row speak of a one-write bound. The round-11 order
  (`AMGT_RESAPP.TO-AMGT-rj-11.the-posture-call.md` :64) states only "two model runs in this cell", and its
  DELIVER 5 names no write count. The record carries both framings -- its heading keeps "under a one-write
  bound", its body quotes the order's literal bound and still reports two writes, the changed hashes, and OK lines
  naming a sha256 the pool no longer holds. It does not read smaller than the breach.
- **Forward mechanism:** two checkable rules (a running total read from the world before each billable or
  state-changing call; each step gated on the prior step's recorded result). A later cut can paste them into a
  worker face. Limit noted for the L10: they live in a ledger record, not a template or a gate, and bind only an
  issuer who reads them.

### rk-9 AC4 -- NOT MET as the judgment is written

The question: would the checker have refused BOTH round-11 criteria that could not fail (the suite over an empty
collection, and the verbatim gate over input with no quotation marks), and does it admit an honest criterion.
- Its own self-test: `SELF-TEST RESULT: DISCRIMINATES (5 of 5 mutants refused, 1 of 1 control admitted)`.
- Three arms built at this seat, not copied from the worker's: a zero-collected pytest suite -> REFUSED
  (ZERO-COLLECTED and RC-SWALLOWED); a bounded verbatim gate reading `verbatim_quotes_unmatched 0` over unquoted
  input -> ADMITTED; an honest bounded suite reading `28 passed` -> ADMITTED. These agree with the worker's arms.
- So it refuses 1 of the 2 named round-11 shapes. The second is a DATA-vacuity class (a gate that cannot fail
  because the test input lacks the thing it checks); a text lint over five shapes cannot see it, and the order's
  DELIVER list never named it. The judgment asked a question the cell was not cut to answer: an issuer
  judgment-scope defect, filed under the systemic class in section 4. The data-vacuity class needs a planted-input
  control, which is the discipline the CTO's recut rulings already impose. W17-S4 and W17-S5 stay open by design,
  as the order says.

### rk-3 AC4 -- NOT MET at this vintage (provisional; final at drain-end)

The question: does a PM opening the Lead Panel now see a Price axis that ranks names, rather than an ABSENT that
was only ever ABSENT because nothing had run. Read-only GET invoke of the deployed adapter at 23:18Z:

| request | result |
|---|---|
| default (today, 2026-09-16) | 200 ABSENT, 0 rows, classed reason "no committed ranking exists for this date" |
| as_of 2026-09-15 | 200 ABSENT, 0 rows, "no generation pointer" (row S137) |
| as_of 2026-09-10 | 200 SERVED, 32 rows, 31 keyed, generation `20260916T065448Z-9b7ffda3dcdc` |
| chatter control | 200 SERVED, 10 rows |

The named defect -- absent by absence -- is cured: every ABSENT now carries its measured reason, and a real
generation serves at its own date. The positive is not reached: the default request shows no ranked names.
Completion sits on two things outside rk-3: the dated fallback ruled onto rk-7 with `cell_refs="AMGT-rk-3"`
(S125), and the 2026-09-15 rows written in a shape the reader cannot follow (S137). Cell D is graded whole when
rk-7 and rk-17 are terminal.

### rk-2 AC6 and rk-8 AC4 -- NOT YET GRADEABLE

Both ask whether the page a person opens shows its figures (rk-2: the Model tab for BA_US_Equity; rk-8: the header
and five tabs, each serving figures or a classed absent). The closure class the CTO ruled at msg 23460(b) is a
CAPTURED render of the BUILT page against the DEPLOYED adapter. No such capture exists: a file-type census since
08:00Z over the project tree, `2.0.0_SA_COO` and `4.0.0_SA_CRO` deliverables and `.scratch/` returned none.
rk-8's evidence is five captured route BODIES (all 200), which prove the served payloads, not what a person sees
-- round 11's rj-3 AC5 FAILED on exactly that gap. The page is now durable: `origin/DEV` reads `2453a7b4`, 47
SecurityAnalysis files, 3 route lines. Graded at drain-end against a capture, whichever seat's instrument makes it.

### rk-14 AC4 -- order open.

## 3. The one contested mechanical PASS

**rk-1 AC1 (row S123).** The PASS stands on its property. Measured at this seat in the portal repo: the
SecurityAnalysis file count reads 47 on the drain ref `b616b759`, on the merge `2453a7b4`, on local DEV and on
origin/DEV; the merge against `be8cf218` adds 48 files and modifies 1 -- 47 page files plus
`src/api/endpoints/amgt-lead-panel.ts`, which sits outside the invocation's pathspec. The "48 or more" bar counted
a file the invocation could never see: an issuer bar defect, not a worker one. Planned: S123 and W23-S1
DISMISSED_WITH_REASON onto the systemic class, grade unchanged.

## 4. The headline finding for the slug (draft; GRADUATED at drain-end)

**Round 12's criteria were repeatedly cut against a world not read at the cut, and modifications that repaired
them were never graded.** Denominators at this vintage: 16 numbered ISSUER AMENDMENTS (1 to 15, and 17) across 26
commits touching round-12 task orders, over 18 orders. Rows naming a criterion that could not pass or could not
fail include S115, S118, S121, S123, S127, S131, S132, S133, S134, S135, W23-S1, W23-S2, W23-S3, W24-S4, W24-S5,
W25-S1, W25-S4, W25-S5, W25-S8, W26-S2, W26-S3, W27-S1, W28-S1. Mechanism: the L6 gate grades a NEWLY-ADDED order
only (CLAUDE.md Rule 27, `to-pipeline-gate.py` `_newly_added`), so every amendment went ungraded; and a criterion's
correctness is established only by RUNNING it (CTO msg 23434). The issuer's own mid-round dry run (S121) is the
instrument that worked. Remedy holder to name at drain-end: the L6 issuance protocol -- every criterion run against
the live world at the cut, before issuance.

## 5. Reading rules this seat applies at L8/L9

- Before quoting any SURPRISES-limb verdict, read `git status --porcelain` on the channel and test for
  MERGE_HEAD. A HAND BACK whose violations are all "resolves to NO row" during a drain is a parse-skip (row S114).
- A store-existence reading is not a served-plane reading (row S137): grade served outcomes on the deployed route.

## 6. Intake after the restart (added 2026-09-17 ~01:3xZ)

- **2.0.0_SA_COO~Z was deaf from before the hold until 01:15Z.** Measured 00:27-00:29Z: 4 of 4 messages since 21:00Z
  OFFER-EXHAUSTED (incl. the 7:10 PM restart, 23490), no inbox watcher, no commit since 21:16Z; reported to
  1.0.0_SA_CTO~Z as msg 23497 (READ 00:31Z). Resolved: the ledger reads all four READ at 01:15Z and the seat's
  summary reads "/watcher re-armed post model-reset; resuming ... from restart handoff". No row filed (fabric
  liveness, not a spec-vs-world finding on the project).
- **4.0.0_SA_CRO~Z's served-plane re-read, msg 23500, record s.3g @312994be2c** -- inputs for the drain-end grades:
  - Model tab (bears on rk-2 AC6, FWD-1): /thesis 200 SERVED for 33 of 33 keyed covered names, invoked as the page
    client builds the URL; 33 of 89 covered; the remaining 56 carry no security_key, so the ceiling is identity.
    Still payload evidence, not the captured render the closure class (23460(b)) requires.
  - Lead Panel (bears on rk-3 AC4, rk-7, FWD-15): the page's call sends only `?limit`
    (`portal/src/api/endpoints/amgt-lead-panel.ts:67-69`, confirmed at this seat), so it reads UTC today. At 01:19Z
    both axes read ABSENT for 2026-09-17; the chatter panel is empty on the page's own call from 00:00Z until the
    10:00Z generation. The price rows under 2026-09-15 are unreachable on a dated read too, matching row Z-S137.
  - Correction by that seat: there is no /posture route by design; its earlier "/posture 404" measured a route nobody
    calls. Nothing in this record rests on it (checked).
  - Instrument rule it states, adopted here: a direct invoke is evidence about the page only when built from the page's
    own call (keys with a slash must be URL-encoded, as the page does).

## 7. rk-17 terminal without row Z-S137 (added 2026-09-17 ~02:4xZ)

- `2.0.0_SA_COO~Z` drained rk-17 at 02:32Z (`52dd9a8c37`): COMPLETE, 5 of 5. Round now 11 of 18.
- AC4 PASSED exactly as S137 predicted, on store existence: its evidence lists `TRENDING_PRICE#2026-09-15` and
  "newest_axis_date 2026-09-15". The instance's `surprises` list is empty, and neither the drain commit nor the
  COO's resume log `e4ed08da80` mentions S137 (0 hits across the files both commits touch). The COO seat was not
  reading mail when S137 was filed (section 6), so this is not a finding against that seat.
- Served route re-read at 02:3xZ, read-only GET: price default -> 200 ABSENT 0 rows (as_of 2026-09-17); as_of
  2026-09-15 -> 200 ABSENT 0 rows. The pull's served outcome is not reached.
- For L9 and the slug: the mechanical PASS stands as the criterion was written. S137 moves from group B to group A
  (its order is terminal) and is planned GRADUATED -- mechanism attributed (`price_axis_pull.py` :198 and :342
  write bare partitions, no generation id, no pointer), denominators carried (194 rows, 15 axis dates, three dated
  reads plus a control), remedy holder the issuer (commit the 2026-09-15 rows as a generation, or route the pull
  through the rk-3 writer; and re-cut the store-existence bar to the served route). S136 moves to group A with it.

## 8. rk-14 AC4 -- MET on computability, with two recorded limits (added 2026-09-17 ~03:4xZ)

Round state: rk-12 drained 03:05Z (`43d24c39d0`), rk-14 03:20Z (`2c0561c0b7`), rk-18 03:27Z (`09513c860d`); 14 of 18
terminal; open rk-6, rk-7, rk-15, rk-16. Numbered ISSUER AMENDMENTS now run 1 to 18 (S138 = 16, S140 = 18).

The question: is the fit COMPUTABLE for a real name (a nonzero factor count on a real subject), or honestly ABSENT with
a CLASSED reason for every name. Contract: ROUND_ANALYSIS.round11.md A3.1 items 1-4.

**Census at this seat, a different instrument from the worker's** (the worker counted member rows from the store;
this seat ran the fixed `lib/research/posture/fit.py` `fit()` over the latest `peers/v1` object of every subject):

| | count |
|---|---|
| subjects with a peers/v1 object | 191 |
| subject block SCORED (either preset) | 110 |
| subject block ABSENT, reason "no R-1 row for this name" | 47 |
| subject block ABSENT, reason "the ranker's loader keeps the code set and drops the numbers" | 34 |
| member rows scored | 1,657 of 1,658 |

- **MET, A3.1 item 4:** 110 of 191 subjects score on their own row (values_carried 23-26, e.g. full 13 of 13 and
  16 of 16 denominators on member rows). A one-subject read of BA_US_Equity alone would have graded this FAILED --
  BA is one of the 81; the census is the grade.
- **LIMIT 1, A3.1 item 3 not fully met:** every ABSENT carries a reason, but not a CLASSED one. The 34 subject reasons
  name the loader defect this very cell repaired, so they state a cause that is no longer true; and the per-factor
  reason `the row carries no value for <code>` (`fit.py:341`) does not class "the source lacks it" against "our pull
  missed it", which A3.1 item 3 requires. Planned for the slug as a remediation on the fit's reason classing.
- **LIMIT 2, served plane:** a person does not see the repaired fit. The adapter serves `document.get("fit")` from the
  stored posture document (`scoped_amgt.py:2247`); only 2 posture objects exist (BA_US_Equity, BABA_US_Equity, both
  `2026-09-15`, LastModified 2026-09-15T16:56:06Z), and read-only `/overlay` at 03:33Z serves their pre-fix fit
  (DIVZ absent reasons "code not named in card 3"). COST_US_Equity serves posture ABSENT. The repair reaches the page
  only when the posture document is regenerated, a bounded model run -- the issuer's or the CTO's call, not graded
  here.
- **For the L10, not a grade:** DIVZ member scores range -10,032.4 to 7,470.0 (median -155.7) because the score is a
  weight-oriented mean of RAW factor values across mixed units; `fit.py` METHOD discloses "not a percentile", and A3.1
  sets no scale, so this is not a contract breach. Whether a person can read such a number is a PRD question.

## 9. The rk-6/rk-7 deploy landed with no change-management entry (added 2026-09-17 ~04:2xZ)

Row `AMGT_RESAPP-Z-S142` (4.0.0_SA_CRO~Z) VERIFIED at this seat on instruments that row did not use:
- Live adapter, `get_function_configuration` at 04:12Z: LastModified `2026-09-17T03:27:57Z`, CodeSha256 `zHmPoWu9...`,
  layer `opal-amgt-print-deps:1`. Prior sha `x3KrEBvZ` (LastModified 2026-09-16T17:23:29Z) is recorded in section 2 of
  this file and in S142.
- `org/critical_paths/change_management/`, shared tree AND worker ~24's worktree `C:/tmp/wk-amgt-12-24`: no entry named
  for any time after `20260916T1906Z` (that one is NFRA_OPLGTW's); worktree porcelain on `org/critical_paths` empty.
- `.tools/deploy_ledger.py list`: no open entry naming AMGT, scoped or print; `org/critical_paths/.open_deploys/` holds
  no AMGT sentinel (newest file 2026-09-10).
- The worker's own proof instances say so plainly, both for rk-6 and rk-7: "The org/critical_paths/change_management/
  ledger entry the never-widen halves ask the worker to open/close was not opened", because neither order's `<paths>`
  grant names that directory (row W24-S7, raised before the act).

**Why it matters for the slug:** it is a CLAUDE.md hard-stop line (a confirmed deploy's ledger entry opened at start,
closed at completion), and it REPEATS a defect already ruled this round: 1.0.0_SA_CTO~Z's msg 23464 widened rk-2's
grant by `org/critical_paths/change_management/` for exactly this reason (W24-S4), and rk-6 and rk-7 were cut and
spawned without that widening. Not a live harm: the signed never-widen halves in `ledger/` carry the blast radius and
rollback for this act. Remedy holder: the issuer -- the late entry recorded as late (the shape the rk-2 rollback entry
used), and the change-management path in every deploying order's grant at the cut. Planned: W24-S4, W24-S7 and S142
dispositioned together onto the systemic issuer class (section 4).

**Row S141 (same seat):** print serves a valid PDF for 31 of 33 keyed covered names; the two 500s are exactly the two
keys containing a slash (BP/_LN_Equity, NG/_LN_Equity), the renderer writing the key into a file path -- round 11's
W19-S5 filename class, now on the served plane. Graded with rk-6 at its drain.

## 10. The retroactive entry, checked against the ruling (added 2026-09-17 ~04:5xZ)

`1.0.0_SA_CTO~Z` ruled row Z-S143 @`3c3134e069` (msg 23502): no rollback; the issuer opens the change-management entry,
RETROACTIVE, with L1 pre-act anchor, L2 post-act anchor, L3 a 0-diff targeted re-plan with its resource list, and the
apply-time plan list recorded as not recorded. `2.0.0_SA_COO~Z` landed it 15 minutes later @`31efe1425e`:
`org/critical_paths/change_management/20260917T0432Z_amgt-scoped-api-rk6rk7-combined-20260917_deploy_completion.md`,
opened 04:32:20Z, CLOSED 04:37:10Z with 4 of 4 legs.

Item-by-item against the ruling, read on the entry's bytes:
- RETROACTIVE marked in the Deploy line and carried into the closing leg -- met.
- L1: sha `x3KrEBvZ`, VersionId `X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA`, 8-GET census 7 of 8 = 200 with print the sole 500 -- met,
  and the VersionId matches the ruling's own.
- L2: sha `zHmPoWu9`, layer `opal-amgt-print-deps:1`, 16 routes all AuthorizationType CUSTOM, IAM both limbs at 12, 0
  event-source mappings -- met. This seat's own read at 04:12Z (section 9) agrees on sha, LastModified and layer.
- L3: `terraform plan -target=module.scoped_amgt_api` from the deployed branch's worktree, 8 refreshed resources listed,
  "No changes" -- met as RECORDED; not re-run here (a second plan would repeat the issuer's instrument, not corroborate it).
- The apply-time plan list stated NOT RECORDED AT THE ACT and not reconstructed; the worker's "6 added, 2 changed, 0
  destroyed" is marked as taken at face value -- met, and honestly scoped.

**For L9:** the remedy for S142 was executed inside the round by its owner, so S142 is planned GRADUATED with its
remediation row REMEDIATED; S143 (the ruling) and W24-S7 (the prospective finding) are dispositioned with it. The
systemic half -- the change-management path missing from deploying orders' grants at the cut, a repeat of W24-S4 -- stays
OPEN on the issuer class in section 4. New seat row S144 (the Price pull never writes `_CURRENT`) confirms Z-S137's
mechanism at the source; they are dispositioned together.

**S141 stays OPEN at L9 (CTO~Z msg 23504, 04:47Z).** That seat validated the retroactive entry on its own read (agreeing
with the check above), and flagged that AMGT-rk-6 flipped COMPLETE @`758d0e473b` (now at HEAD after the drain) while S141 (print
500 for BP/_LN_Equity and NG/_LN_Equity) is unfixed. The flip is correct against rk-6's criteria as written -- the order
carries no slash-key clause, and its instance's `surprises` names W24-S7 and W24-S8 only -- so rk-6 is not reopened.
Planned: S141 GRADUATED with its remediation OPEN (not remediated, not closed by the flip); the CTO carries it into
ROUND_ANALYSIS.round12 as a recut item. Measured denominator stands at 31 of 33 keyed covered names serving print.

-- 3.0.0_SA_CVO
