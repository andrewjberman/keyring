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

-- 3.0.0_SA_CVO
