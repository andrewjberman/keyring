# ROUND-N ANALYSIS -- DSGN_IRPTV1, rounds 5 and 7 (answering the CVO slug REMEDIATION_v3)

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~07:5xZ. **Answers:** 3.0.0_SA_CVO msg 101844, slug
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v3.md` @`e5c8c76afb`; grades
`ADJUDICATION_v5.md` @`ef3adb67c4` + @`f5777670db`. **Contract:** PRD `DSGN_IRPTV1_PRD.md` v0.16 @`f3026103f0`
(ADMITTED). **Recut by:** 2.0.0_SA_COO~D, in ONE issuance (round 8).

## 1. What the round measured

- **Judgment criteria, graded on the window-9 walk** (local portal DEV `200d257a`, 1440 px):
  - IVE41 (every account) and IVE47 (the Global merge): PASS;
  - IVE48 (the new classes): NOT_EVALUATED, waiting on ~M's values;
  - IVE37, 38, 39, 40, 42, 43, 44 and 45: FAIL.
- **Per UIR id:** 25 PASS, 16 FAIL, 5 NOT_EVALUATED (of 46 graded), plus FWD-20.
- **Rows:** 18. 12 are remedied and disarmed; 6 are open (W21-S2, W23-S1, W29-S8, W29-S9, W29-S10, S19).

**Reading:** the cells built their mechanisms and passed their mechanical checks, but the running page still fails 16
of Andrew's acceptance lines. The failures cluster into seven kinds of work (section 3). None is a new outcome: each
sits under an existing FWD, so this is an enrichment round, not a PRD addendum.

## 2. Rulings owed by this seat

### W29-S8 (BLOCKING): F45-AC9 (`scripts/dev-live.mjs`) and F57-AC2 (`contracts/adapt.ts`) fail on product paths no order grants

**RULED: a product-path cell in round 8, not a wider Q allowance.**
- The cell grants `scripts/dev-live.mjs`, `contracts/adapt.ts` and their two tests.
- Its bar is that F45-AC9 and F57-AC2 pass by fixing the cause.
- If a test's assertion is itself wrong against the ratified contract, the cell names the contract line and
  re-goldens with the served values kept (the W29-S2 pattern, CTO 101768).
- Why: a pinned test failing on a product path is signal about the product. An allowance would hide it.

### W29-S10 (BLOCKING): two 3-run samples gave different stable failing sets (15 vs 7)

**RULED: grade the S7 bar under a PINNED runner. No retries and no wider Q allowance (consistent with 101651).**
1. The round-8 harness cell pins the runner: a fixed test order/seed and isolated workers (or one worker).
2. **Pass** = three runs give the IDENTICAL failing set, and that set is a subset of the Q rows.
3. Tests that fail only under some orders are order-dependent. The cell fixes them, and names each fix.
4. W29-S9 (the flaky `iv-e-26.wire-regen.test.ts`) is folded into the same cell.
5. TO-IV-e-50 stays PARKED and is superseded by this cell. W21-S2, W23-S1 and S7 close on its pass.

### S17 (the Advisor Intelligence drill 403s for every principal, DISMISSED_WITH_REASON here)

It is routed to the AI data-route owner through 0.0.0_AB_MSTR, as the project ADVI_PERFRP (D2). The reads are
`/api/scoped/advisor-intelligence/platinum/advi/cottonwood/perfrp_*` and `platinum/accounts/*/summary.json`, 403 for
a superadmin on PROD.

### S19 (28 client screenshots at origin/CLOUD's tip)

- The disarm owner is 0.0.0_AB_MSTR: push the untrack @`cfed2c067b`.
- The history purge is Andrew's call; the CTO REC is to keep history.

## 3. The ENRICHMENT LIST -- round 8 (the COO cuts it in ONE issuance; each item keeps the UIR rows' acceptance lines verbatim)

| # | Work | UIR rows / rows | FWD |
|---|---|---|---|
| E1 | **Display names, never tenant keys**: the firm and client show a display name (`Cottonwood`, `49 Financial`), and the firm appears once | UIR-04, UIR-13, UIR-30 | FWD-2, FWD-15 |
| E2 | **Live search covers the page**: the sample panels never render behind the open result list | UIR-11 | FWD-3 |
| E3 | **Account picker entries**: each entry carries the account's value AND its YTD. FWD-20's YTD is added beside the value, not in place of it. The identical-label part stays ~M's UIR-26 | UIR-15 | FWD-19, FWD-20 |
| E4 | **One colour, one meaning**: account slices get distinct colours; no colour marks both a model and an asset class on one page | UIR-25, UIR-46, UIR-37 | FWD-12, FWD-13 |
| E5 | **The drill and its bases**: the breadcrumb names the account; every percentage states its base (of this account / of the client) or both views use one base; no one-slice pie for a one-child level | UIR-32, UIR-33, UIR-34, UIR-36, UIR-47, UIR-49 | FWD-14, FWD-6 |
| E6 | **Securities map filters**: model chips grouped and de-duplicated per account | UIR-41 | FWD-22 |
| E7 | **One date format; the source line names the source; the R10 exception label**: a section whose source cannot reach the page date says so ("Returns through Sep 18") | UIR-45; R10 @`54323a0fb5` | FWD-2, FWD-5 |
| E8 | **Walk coverage for the NOT_EVALUATED rows**: the round-8 walk exercises OVER WHAT expansion (UIR-17), a refusal state (UIR-18, UIR-19; by a fixture or a named refused account, read-only) and "About this scope" (UIR-22). UIR-50 grades when ~M's values land | UIR-17, 18, 19, 22, 50 | per row |
| E9 | **Another session's Analysis job is visible**: a request-list read (IRPT_BCKEND ~P's route) and its render | DSGN_IRPTV1-S18 | FWD-1 (Analysis hop) |
| E10 | **The product-path cell** (W29-S8) and **the pinned-runner harness cell** (W29-S10, W29-S9) | rows above | -- |
| E11 | **The export hop**: TO-IV-e-53 (Export preview carries selectedTenant) is in flight as a direct act. If it lands before the cut, the next window's K8 grades it; if not, it rides round 8 | DSGN_IRPTV1-S20, S22 | FWD-1 (export hop) |

**Sequencing guidance (the COO decides the chains):**
- E1 and E3 touch the header and picker; E4, E5 and E6 touch the holdings views; E7 touches Performance.
- E10 goes first on its own chain, so the round's mechanical grades are trustworthy.
- E9 needs ~P's route before its render cell.

## 4. Carried (not DSGN cells)

- UIR-26 (identical account labels) and UIR-48 (model amounts): IRPT_BCKEND ~M.
- IRPT_BCKEND-S152 (INF holdings 3 trading days behind): R4 (~M), Monday.
- IRPT_BCKEND-S157 (the COT retained face overstates its period): the release test-data item.

## 5. Push state

Everything cited is LOCAL on CLOUD (origin/CLOUD `262d0e8d16` per the CVO's ls-remote read).
